"""Публикует свежий дайджест Horizon в Telegram-канал.

Берёт последний файл data/summaries/horizon-<дата>-<язык>.md,
режет его на отдельные новости и отправляет каждую постом в канал.

Режимы запуска:
  python3 scripts/telegram_post.py                       — опубликовать всё сразу
  python3 scripts/telegram_post.py build-queue q.json    — сложить посты в очередь (утром)
  python3 scripts/telegram_post.py publish-queue q.json  — выпустить очередную порцию
        (запускать раз в час: посты делятся поровну на часы с WINDOW_START до WINDOW_END по МСК)

Переменные окружения:
  WINDOW_START / WINDOW_END — окно публикаций, часы по МСК (по умолчанию 9 и 21)
  TELEGRAM_BOT_TOKEN  — токен бота от @BotFather (обязательно)
  TELEGRAM_CHAT_ID    — необязательно: доп. чат (@username или -100…). Остальные чаты бот
                        находит сам — каналы и группы, куда его добавили (в канал — админом)
  DIGEST_LANG         — язык дайджеста, по умолчанию ru
  POST_MODE           — items (пост на каждую новость, по умолчанию)
                        или digest (весь дайджест одним сообщением)
  SEND_OVERVIEW       — 1/0, слать ли список заголовков перед новостями (по умолчанию 1)
  USE_RICH            — 1, чтобы пробовать sendRichMessage (Bot API 10.1+);
                        при ошибке автоматически откат на обычный sendMessage
  DRY_RUN             — 1, чтобы только напечатать посты, ничего не отправляя
"""

from __future__ import annotations

import glob
import html
import json
import math
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

CLASSIC_LIMIT = 4096
RICH_LIMIT = 32768
PAUSE_SEC = 3.5  # Telegram: не больше ~20 сообщений в минуту в один канал

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
LANG = os.environ.get("DIGEST_LANG", "ru").strip()
MODE = os.environ.get("POST_MODE", "items").strip()
SEND_OVERVIEW = os.environ.get("SEND_OVERVIEW", "1") == "1"
USE_RICH = os.environ.get("USE_RICH", "0") == "1"
DRY_RUN = os.environ.get("DRY_RUN", "0") == "1"
SUMMARIES_DIR = os.environ.get("SUMMARIES_DIR", "data/summaries")


# ---------- поиск файла ----------

def latest_summary() -> str | None:
    files = sorted(glob.glob(os.path.join(SUMMARIES_DIR, f"horizon-*-{LANG}.md")))
    return files[-1] if files else None


# ---------- Markdown -> Telegram HTML ----------

LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
CODE_RE = re.compile(r"`([^`]+)`")


def inline(md: str) -> str:
    """Переводит строку Markdown в безопасный Telegram HTML."""
    md = re.sub(r"\\([\\`*_{}\[\]()#+\-.!|>~])", r"\1", md)  # снять экранирование \( \)
    md = md.replace("⭐️", "⭐")

    placeholders: list[str] = []

    def keep(fragment: str) -> str:
        placeholders.append(fragment)
        return f"\x00{len(placeholders) - 1}\x00"

    md = CODE_RE.sub(lambda m: keep(f"<code>{html.escape(m.group(1))}</code>"), md)
    md = LINK_RE.sub(
        lambda m: keep(
            f'<a href="{html.escape(m.group(2), quote=True)}">{html.escape(m.group(1))}</a>'
        ),
        md,
    )
    md = html.escape(md, quote=False)
    md = BOLD_RE.sub(r"<b>\1</b>", md)
    return re.sub(r"\x00(\d+)\x00", lambda m: placeholders[int(m.group(1))], md)


def references_block(block: str) -> str:
    links = re.findall(r'<a href="([^"]+)">(.*?)</a>', block, flags=re.S)
    if not links:
        return ""
    lines = ["<b>Ссылки:</b>"]
    for url, title in links[:5]:
        title = html.unescape(re.sub(r"<[^>]+>", "", title)).strip() or url
        lines.append(f'• <a href="{html.escape(url, quote=True)}">{html.escape(title)}</a>')
    return "\n".join(lines)


LABELS_RU = {"Tags": "Теги", "Background": "Контекст", "Discussion": "Обсуждение",
             "References": "Ссылки", "Source": "Источник"}


def md_to_html(md: str) -> str:
    for en, ru in LABELS_RU.items():
        md = md.replace(f"**{en}**", f"**{ru}**")
    md = re.sub(r"<a id=\"[^\"]*\"></a>", "", md)
    md = re.sub(
        r"<details>.*?</details>",
        lambda m: "\n" + "\n".join("\x01" + l for l in references_block(m.group(0)).splitlines()) + "\n",
        md,
        flags=re.S,
    )
    out: list[str] = []
    for raw in md.splitlines():
        line = raw.rstrip()
        if line.startswith("\x01"):
            out.append(line[1:])
        elif line.strip() == "---":
            out.append("")
        elif re.match(r"^#{1,6}\s", line):
            out.append("<b>" + inline(re.sub(r"^#{1,6}\s+", "", line)) + "</b>")
        elif line.startswith("> "):
            out.append("<i>" + inline(line[2:]) + "</i>")
        else:
            out.append(inline(line))
    text = "\n".join(out)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


# ---------- разбор дайджеста ----------

def split_digest(md: str) -> tuple[str, list[str]]:
    md = re.sub(r"\A---\n.*?\n---\n", "", md, flags=re.S)  # front matter, если есть
    parts = re.split(r'(?=<a id="item-[\w-]+"></a>)', md)
    head, items = parts[0], [p for p in parts[1:] if p.strip()]
    # заголовки разделов («## Technology News») между новостями в посты не нужны
    items = [re.sub(r"(?m)^\s*(---\s*)?\n?^##\s+[^\n]*\s*\Z", "", it).strip() for it in items]
    items = [re.sub(r"(?m)^##\s+[^#\n][^\n]*$", "", it).strip() for it in items]
    # якорные ссылки (#item-…) в оглавлении в Telegram не работают — убираем их
    head = re.sub(r"\[([^\]]+)\]\(#item-[\w-]+\)", r"\1", head)
    return head, items


def chunk(text: str, limit: int) -> list[str]:
    """Режет текст по абзацам/строкам так, чтобы не порвать HTML-теги."""
    if len(text) <= limit:
        return [text]
    pieces, current = [], ""
    for para in re.split(r"(\n\n)", text):
        if len(current) + len(para) <= limit:
            current += para
            continue
        if current.strip():
            pieces.append(current.strip())
        current = ""
        while len(para) > limit:  # очень длинный абзац — режем по строкам
            cut = para.rfind("\n", 0, limit)
            cut = cut if cut > 0 else para.rfind(" ", 0, limit)
            cut = cut if cut > 0 else limit
            pieces.append(para[:cut].strip())
            para = para[cut:]
        current = para
    if current.strip():
        pieces.append(current.strip())
    return pieces


# ---------- отправка ----------

def api(method: str, payload: dict) -> dict:
    req = urllib.request.Request(
        f"https://api.telegram.org/bot{TOKEN}/{method}",
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
    )
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as err:
            body = json.loads(err.read().decode() or "{}")
            retry = body.get("parameters", {}).get("retry_after")
            if err.code == 429 and retry:
                time.sleep(int(retry) + 1)
                continue
            return body
        except urllib.error.URLError:
            time.sleep(2 ** attempt)
    return {"ok": False, "description": "network error"}


rich_works = USE_RICH
LARGE_PREVIEW = os.environ.get("LARGE_PREVIEW", "1") == "1"


def preview_options(text: str) -> dict:
    """Превью по ссылке из заголовка (первоисточник): крупная картинка над текстом."""
    first = re.search(r'<a href="([^"]+)"', text)
    if not first:
        return {"is_disabled": True}
    opts = {"url": html.unescape(first.group(1))}
    if LARGE_PREVIEW:
        opts.update({"prefer_large_media": True, "show_above_text": True})
    return opts


GONE_ERRORS = ("chat not found", "bot was kicked", "bot is not a member", "have no rights",
               "not enough rights", "need administrator rights", "chat was deleted", "user is deactivated")


class ChatGone(Exception):
    """Бота удалили из чата или лишили прав — чат убираем из списка."""


def send(text: str, chat_id: str | int | None = None) -> bool:
    global rich_works
    chat_id = chat_id if chat_id is not None else CHAT_ID
    if DRY_RUN:
        print("=" * 60 + f"\n[{len(text)} символов → {chat_id}]\n{text}\n")
        return True

    if rich_works and len(text) <= RICH_LIMIT:
        res = api("sendRichMessage", {"chat_id": chat_id, "rich_message": {"html": text}})
        if res.get("ok"):
            return True
        print(f"sendRichMessage не сработал ({res.get('description')}), перехожу на sendMessage")
        rich_works = False

    ok = True
    for i, part in enumerate(chunk(text, CLASSIC_LIMIT)):
        payload = {"chat_id": chat_id, "text": part, "parse_mode": "HTML"}
        payload["link_preview_options"] = preview_options(part) if i == 0 else {"is_disabled": True}
        res = api("sendMessage", payload)
        if not res.get("ok") and "link_preview_options" in payload:
            payload.pop("link_preview_options")  # если превью не принято — шлём без него
            res = api("sendMessage", payload)
        _raise_if_gone(res)
        if not res.get("ok"):
            print(f"HTML не принят ({res.get('description')}), отправляю простым текстом")
            plain = html.unescape(re.sub(r"<[^>]+>", "", part))
            res = api("sendMessage", {"chat_id": chat_id, "text": plain[:CLASSIC_LIMIT]})
            _raise_if_gone(res)
        if not res.get("ok"):
            print(f"Ошибка отправки в {chat_id}: {res}", file=sys.stderr)
            ok = False
        time.sleep(PAUSE_SEC)
    return ok


def _raise_if_gone(res: dict) -> None:
    if res.get("ok"):
        return
    desc = str(res.get("description", "")).lower()
    if res.get("error_code") == 403 or any(e in desc for e in GONE_ERRORS):
        raise ChatGone(res.get("description"))


# ---------- чаты: бот сам узнаёт, куда его добавили ----------

ACTIVE = {"administrator", "member", "creator"}


def sync_chats(chats_path: str) -> dict:
    """Читает getUpdates (добавили/удалили бота) и обновляет список чатов."""
    state = {"offset": 0, "chats": {}}
    if os.path.exists(chats_path):
        with open(chats_path, encoding="utf-8") as f:
            state.update(json.load(f))
    chats: dict = state["chats"]

    if not DRY_RUN:
        res = api("getUpdates", {"offset": state["offset"], "timeout": 0,
                                 "allowed_updates": ["my_chat_member", "message", "channel_post"]})
        if not res.get("ok"):
            print(f"getUpdates не сработал: {res.get('description')}"
                  " (если у бота стоит webhook — его надо снять: deleteWebhook)", file=sys.stderr)
        for upd in res.get("result", []):
            state["offset"] = upd["update_id"] + 1
            change = upd.get("my_chat_member")
            if not change:
                continue
            chat = change["chat"]
            status = change["new_chat_member"]["status"]
            key = str(chat["id"])
            if chat.get("type") == "private":
                continue  # в личку новости не шлём
            if status in ACTIVE:
                if chat["type"] == "channel" and status != "administrator":
                    continue  # в канал бот пишет только админом
                chats[key] = {"title": chat.get("title", ""), "type": chat["type"]}
                print(f"+ чат: {chat.get('title')} ({key})")
            elif key in chats:
                chats.pop(key)
                print(f"− чат: {chat.get('title')} ({key})")

    if CHAT_ID and CHAT_ID not in chats:
        chats[CHAT_ID] = {"title": "из секрета TELEGRAM_CHAT_ID", "type": "manual"}
    _save(chats_path, state)
    return state


def build_posts(md: str, with_overview: bool) -> list[str]:
    if MODE == "digest":
        return [md_to_html(md)]
    head, items = split_digest(md)
    if not items:
        return []  # пустой день — в канал ничего не идёт
    posts = [md_to_html(head)] if with_overview and head.strip() else []
    return posts + [md_to_html(item) for item in items]


# ---------- очередь: собрать утром, раскидать в течение дня ----------

MSK = timezone(timedelta(hours=3))
WINDOW_START = int(os.environ.get("WINDOW_START", "9"))   # первый пост, час по МСК
WINDOW_END = int(os.environ.get("WINDOW_END", "21"))      # последний пост, час по МСК


def build_queue(queue_path: str) -> int:
    path = latest_summary()
    if not path:
        print(f"Дайджест не найден в {SUMMARIES_DIR} для языка {LANG}.")
        return 1
    md = open(path, encoding="utf-8").read()
    posts = build_posts(md, with_overview=SEND_OVERVIEW)
    queue = {"date": datetime.now(MSK).date().isoformat(), "source": os.path.basename(path), "posts": posts}
    with open(queue_path, "w", encoding="utf-8") as f:
        json.dump(queue, f, ensure_ascii=False, indent=1)
    print(f"В очереди {len(posts)} постов на {queue['date']}")
    return 0


def publish_queue(queue_path: str, chats_path: str) -> int:
    state = sync_chats(chats_path)
    chats: dict = state["chats"]
    if not chats:
        print("Бот пока не добавлен ни в один чат — публиковать некуда.")
        return 0
    if not os.path.exists(queue_path):
        print("Очереди нет — публиковать нечего.")
        return 0
    with open(queue_path, encoding="utf-8") as f:
        queue = json.load(f)
    posts: list[str] = queue.get("posts", [])
    now = datetime.now(MSK)

    if queue.get("date") != now.date().isoformat():
        if posts:
            print(f"Очередь за {queue.get('date')} устарела, {len(posts)} постов пропускаю.")
            queue["posts"] = []
            _save(queue_path, queue)
        return 0
    if not posts:
        print("На сегодня всё опубликовано.")
        return 0
    if now.hour < WINDOW_START:
        print(f"Рано: окно публикаций с {WINDOW_START}:00 МСК.")
        return 0

    # сколько запусков осталось до конца окна (запуск раз в час) — делим поровну
    slots_left = max(1, WINDOW_END - now.hour + 1)
    batch = math.ceil(len(posts) / slots_left)
    print(f"{now:%H:%M} МСК: в очереди {len(posts)}, осталось слотов {slots_left}, публикую {batch}")

    print("Чаты: " + ", ".join(f"{c['title'] or cid}" for cid, c in chats.items()))

    failures = 0
    for _ in range(batch):
        post = posts.pop(0)
        for cid in list(chats):
            try:
                failures += not send(post, cid)
            except ChatGone as err:
                print(f"Бот больше не может писать в {chats[cid]['title'] or cid} ({err}) — убираю из списка")
                chats.pop(cid)
        queue["posts"] = posts
        _save(queue_path, queue)  # сохраняем после каждого поста, чтобы не задвоить при сбое
        _save(chats_path, state)
    return 1 if failures else 0


def _save(queue_path: str, queue: dict) -> None:
    with open(queue_path, "w", encoding="utf-8") as f:
        json.dump(queue, f, ensure_ascii=False, indent=1)


def main() -> int:
    args = sys.argv[1:]
    action = args[0] if args else "now"

    if action == "build-queue":
        return build_queue(args[1] if len(args) > 1 else "queue.json")

    if not DRY_RUN and not TOKEN:
        print("Нужен секрет TELEGRAM_BOT_TOKEN", file=sys.stderr)
        return 1

    if action == "publish-queue":
        queue_path = args[1] if len(args) > 1 else "queue.json"
        chats_path = args[2] if len(args) > 2 else os.path.join(os.path.dirname(queue_path) or ".", "chats.json")
        return publish_queue(queue_path, chats_path)

    if not CHAT_ID:
        print("Для разовой отправки нужен TELEGRAM_CHAT_ID", file=sys.stderr)
        return 1

    path = latest_summary()
    if not path:
        print(f"Дайджест не найден в {SUMMARIES_DIR} для языка {LANG} — отправлять нечего.")
        return 0
    print(f"Публикую {path}")
    md = open(path, encoding="utf-8").read()

    if MODE == "digest":
        return 0 if send(md_to_html(md)) else 1

    head, items = split_digest(md)
    if not items:  # пустой день — шлём то, что есть
        return 0 if send(md_to_html(head)) else 1

    failures = 0
    if SEND_OVERVIEW and head.strip():
        failures += not send(md_to_html(head))
    for item in items:
        failures += not send(md_to_html(item))
    print(f"Готово: {len(items)} новостей, ошибок: {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
