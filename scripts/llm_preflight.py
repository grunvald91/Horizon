"""Проверка ключа и модели перед запуском Horizon.

Пробует модель через Anthropic-формат (/v1/messages) и OpenAI-формат (/v1/chat/completions).
Если ID модели не подошёл, ищет похожий в списке /v1/models (например, grok-4.7 → grok-4-7).
Результат пишет в $GITHUB_ENV: HORIZON_PROVIDER, HORIZON_BASE_URL, HORIZON_MODEL.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request

BASE = os.environ.get("LLM_BASE", "https://api.claudehub.fun").rstrip("/")
KEY = os.environ.get("ANTHROPIC_API_KEY", "").strip()
WANTED = os.environ.get("HORIZON_MODEL", "grok-4.7").strip()


def call(url: str, body: dict | None, headers: dict) -> tuple[int, dict]:
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json", **headers})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read().decode() or "{}")
        except json.JSONDecodeError:
            return e.code, {}
    except Exception as e:  # сеть
        return 0, {"error": str(e)}


def try_anthropic(model: str) -> tuple[bool, str]:
    code, res = call(f"{BASE}/v1/messages",
                     {"model": model, "max_tokens": 16, "messages": [{"role": "user", "content": "ping"}]},
                     {"x-api-key": KEY, "authorization": f"Bearer {KEY}", "anthropic-version": "2023-06-01"})
    return code == 200 and bool(res.get("content")), f"{code} {str(res)[:200]}"


def try_openai(model: str) -> tuple[bool, str]:
    code, res = call(f"{BASE}/v1/chat/completions",
                     {"model": model, "max_tokens": 16, "messages": [{"role": "user", "content": "ping"}]},
                     {"authorization": f"Bearer {KEY}"})
    return code == 200 and bool(res.get("choices")), f"{code} {str(res)[:200]}"


def list_models() -> list[str]:
    for headers in ({"authorization": f"Bearer {KEY}"}, {"x-api-key": KEY, "anthropic-version": "2023-06-01"}):
        code, res = call(f"{BASE}/v1/models", None, headers)
        if code == 200 and isinstance(res.get("data"), list):
            return [m.get("id", "") for m in res["data"] if m.get("id")]
    return []


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def main() -> int:
    if not KEY:
        print("::error::Нет секрета ANTHROPIC_API_KEY (ключ sk-hub-... с claudehub.fun)")
        return 1

    candidates = [WANTED]
    models = list_models()
    if models:
        grok = [m for m in models if "grok" in m.lower()]
        print(f"Модели Grok у провайдера: {', '.join(grok) or 'не найдено'}")
        similar = [m for m in models if norm(m) == norm(WANTED) or norm(WANTED) in norm(m)]
        candidates += [m for m in similar if m not in candidates]

    for model in candidates:
        for provider, base_url, fn in (("anthropic", BASE, try_anthropic),
                                       ("openai", f"{BASE}/v1", try_openai)):
            ok, info = fn(model)
            print(f"{provider:9} {model}: {'OK' if ok else info}")
            if ok:
                with open(os.environ.get("GITHUB_ENV", os.devnull), "a") as f:
                    f.write(f"HORIZON_PROVIDER={provider}\nHORIZON_BASE_URL={base_url}\nHORIZON_MODEL={model}\n")
                print(f"Использую {model} через {provider}-формат")
                return 0

    print(f"::error::Модель {WANTED} не отвечает. Проверь ключ/баланс в app.claudehub.fun "
          "и точный ID модели (переменная HORIZON_MODEL).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
