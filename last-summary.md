# Horizon Daily - 2026-10-17

> From 35 items, 9 important content pieces were selected

---

**Technology News**
1. [Claude Anthropic: Непрерывный AI-assisted code review](#item-tech-news-1) ⭐️ 8.0/10
2. [ORL: 2788 токенов/с на RTX 5090 для диффузионных LLM](#item-tech-news-2) ⭐️ 8.0/10
3. [Китайская мобильная Гонконг и операторы Макао завершили сети U6GHz](#item-tech-news-3) ⭐️ 8.0/10
4. [DeepSeek-v4.1-Flash-1017: Быстрая открытая модель для кодирования](#item-tech-news-4) ⭐️ 7.0/10
5. [Show HN: Llmspeed – feel how fast a local LLM runs before you buy the hardware](#item-tech-news-5) ⭐️ 7.0/10
6. [EpochGo: Локально-первый многоагентный AutoML-движок с Ollama LLMs и Scikit-Learn](#item-tech-news-6) ⭐️ 7.0/10
7. [Маск: все объявления на X под эстетическими стандартами](#item-tech-news-7) ⭐️ 7.0/10
8. [Безпроводной jailbreak для iPhone 18 Pro](#item-tech-news-8) ⭐️ 7.0/10

**Financial News**
1. [Беркшир Хатхауэй инвестирует в Bending Spoons](#item-finance-news-1) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Claude Anthropic: Непрерывный AI-assisted code review](https://simonwillison.net/2026/Oct/16/code-review/) ⭐️ 8.0/10

Команда Claude в Anthropic перешла на непрерывный AI-assisted code review во время написания кода, аналогично spellcheck. Ранее ревью было gate-процессом: написать код, открыть PR и ждать ревью от коллеги. Теперь ревью происходит непрерывно, и большинство изменений проверяются Claude хотя бы один раз до человеческого ревью. Это ловит рутинные ошибки и освобождает внимание команды для вопросов более высокого уровня.

rss · Simon Willison · Oct 16, 22:06

**「Предыстория code review」** Традиционный code review был gate-процессом на конце разработки. Он требовал человеческого ревьюера, который читал весь код перед слиянием. Это позволяло выявлять ошибки, но создавало задержки в разработке.

**「Влияние на разработку」** Команды могут сосредоточить внимание на более сложных вопросах и scrutiny вместо рутинных ошибок, повышая общую производительность разработки.

**Tags**: `#anthropic`, `#claude`, `#code-review`, `#ai-assisted-development`, `#software-engineering`

---

<a id="item-tech-news-2"></a>
### [ORL: 2788 токенов/с на RTX 5090 для диффузионных LLM](https://www.reddit.com/r/MachineLearning/comments/1x7qgr0/research_2788_tokenss_on_a_single_rtx_5090_with_a/) ⭐️ 8.0/10

Представлена ORL \(On-Policy Residual Learning\) для диффузионных языковых моделей. Достигнута скорость 2788 токенов/с на одном RTX 5090 с LLaDA-2.1-mini + ORL в NVFP4, а также до 6.9× прироста end-to-end throughput на QwenDLM-4B. Полный стек — модели, код обучения, движок dlmrt — открыт для использования.

reddit · r/MachineLearning · /u/arty\_photography · Oct 16, 20:03

**「Фон」** Диффузионные языковые модели генерируют несколько токенов параллельно за один проход денойзинга, в отличие от автогрессивных моделей, которые выводят токен за токеном. Сходимость в меньшее количество шагов остаётся сложной задачей. ORL решает это через on-policy residual learning, тренируя модель на self-generated residuals, и Adjacent Entropy Contraction для ускорения уменьшения неопределённости.

**「Влияние」** Пользователи RTX 5090 получают доступ к диффузионным LLM со скоростью 2788 токенов/с в одиночных запросах, а все исходные коды и модели доступны для локального развертывания и дообучения.

**Tags**: `#diffusion LLMs`, `#LLM inference optimization`, `#open source AI`, `#RTX 5090 benchmarks`, `#machine learning research`

---

<a id="item-tech-news-3"></a>
### [Китайская мобильная Гонконг и операторы Макао завершили сети U6GHz](https://www.hk.chinamobile.com/tc/home/news/20261018pr) ⭐️ 8.0/10

Китайская мобильная Гонконг \(CMHK\) завершила строительство первого в Гонконге U6GHz сети в районе Ван Чой и провела тестирование, а в тот же день Macau Telecom \(CTM\) запустила глобально первую коммерческую сцену U6GHz в отеле Meixi Meigao, а China Telecom Macau \(CTMO\) установила демонстрационную базу и запустила полевые тесты. Сегмент U6GHz обеспечивает непрерывный большой bandwidth, являясь ключевым ресурсом для эволюции 5G-A и 6G, и через спектральную агрегацию CMHK достигла скоростей более 3 Гбит/с, а CTM использует станции VitaAAU с технологиями 256TRx и RetinaMIMO, обеспечивающими покрытие на уровне 5G n78 \(3.5 GHz\). Операторы заявили, что будут развивать 6G на этой основе.

telegram · zaihuapd · Oct 17, 13:02

**「U6GHz: спектр для 5G-A и 6G」** Верхний диапазон 6 ГГц \(U6GHz\) предоставляет непрерывный широкий спектральный диапазон и является ключевым ресурсом для эволюции 5G-Advanced и будущих сетей 6G. В ответ на предложение правительства Гонконга по созданию сетей 5G-Advanced в верхнем диапазоне 6/7 ГГц \(«U6G»\) China Mobile Hong Kong провела полевые испытания для изучения радиохарактеристик этого частотного диапазона. В ноябре 2024 года Гонконг стал первым регионом в мире, аукционировавшим этот частотный диапазон для общественных мобильных услуг, и China Mobile Hong Kong успешно выиграла 100 МГц непрерывного спектра.

**「Поддержка 5G-A и 6G в Гонконге и Макао」** Развертывание U6GHz сетей China Mobile Hong Kong и Macau в Гонконге и Макао обеспечивает пользователям скорости интернета свыше 3 Гбит/с через спектральную агрегацию и технологии RetinaMIMO, что напрямую поддерживает развитие 5G-A и 6G в этих регионах.

<details><summary>References</summary>
<ul>
<li><a href="https://finance.yahoo.com/technology/articles/china-mobile-hong-kong-establishes-160000855.html?fr=sycsrp_catchall">China Mobile Hong Kong Establishes Hong Kong&#x27;s First U6G Network</a></li>
<li><a href="https://www.ofca.gov.hk/filemanager/ofca/en/content_669/tr202501_01.pdf">China Mobile Hong Kong (“CMHK”) 6/7 GHz Band (“U6G”) Mobile ...</a></li>
<li><a href="https://trangcongnghe.com/news/pr-newswire/125427-china-mobile-hong-kong-establishes-hong-kongs-first-u6g-network.html">China Mobile Hong Kong Establishes Hong Kong&#x27;s First U6G ...</a></li>
<li><a href="https://www.youtube.com/watch?v=_vT_gT6Vd1A">What is 6 G and why is China ahead? - YouTube</a></li>

</ul>
</details>

**Tags**: `#U6GHz`, `#5G-A`, `#6G`, `#Spectrum Aggregation`, `#MIMO`

---

<a id="item-tech-news-4"></a>
### [DeepSeek-v4.1-Flash-1017: Быстрая открытая модель для кодирования](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) ⭐️ 7.0/10

DeepSeek AI выпустила DeepSeek-v4.1-Flash-1017 — минорное обновление DeepSeek-V4.1-Flash. Это быстрая открытая модель, ориентированная на кодирование, которая превосходит конкурентов по бенчмаркам, включая Sol 5.6. Модель выделяется высокой скоростью \(токены в секунду, TTFT\), прозрачностью \(видимый CoT\) и подходит для агентных рабочих процессов. Она доступна через Hugging Face, OpenRouter и API DeepSeek.

hackernews · theykk · Oct 17, 08:21 · [Discussion](https://news.ycombinator.com/item?id=50129045)

**「Предыстория」** DeepSeek-V4.1-Flash является частью серии моделей DeepSeek, оптимизированных для задач кодирования и агентного ИИ. Предыдущие версии уже демонстрировали сильные результаты в открытых LLM для программирования, что сделало их популярными среди разработчиков.

**「Влияние」** Для разработчиков и команд, использующих ИИ в рабочих процессах кодирования, DeepSeek-v4.1-Flash предлагает более быструю обработку и прозрачность, что может повысить продуктивность в агентных системах. Это может способствовать диверсификации экосистемы LLM, поощряя использование открытых моделей.

**「Обсуждение в сообществе」** В комментариях пользователи отмечают, что несмотря на бенчмарки, модель кажется лучше благодаря высокой скорости и возможности видеть цепочку рассуждений без случайных блокировок. Сравнения показывают практические преимущества в реальных задачах кодирования, таких как анализ больших кодовых баз.

**Tags**: `#DeepSeek`, `#LLM`, `#coding benchmarks`, `#open-source AI`, `#model release`

---

<a id="item-tech-news-5"></a>
### [Show HN: Llmspeed – feel how fast a local LLM runs before you buy the hardware](https://llmspeed.dev/) ⭐️ 7.0/10

Show HN post for Llmspeed.dev, a benchmarking site allowing users to feel local LLM runtimes before buying GPUs or systems, sparking interest in accurate inference performance metrics.

hackernews · albinstman · Oct 17, 04:36 · [Discussion](https://news.ycombinator.com/item?id=50127979)

**Tags**: `#local LLMs`, `#hardware benchmarking`, `#AI inference`, `#Show HN`, `#benchmark realism`

---

<a id="item-tech-news-6"></a>
### [EpochGo: Локально-первый многоагентный AutoML-движок с Ollama LLMs и Scikit-Learn](https://www.reddit.com/r/MachineLearning/comments/1x8c2sq/epochgo_localfirst_multiagent_automl_engine_using/) ⭐️ 7.0/10

Релиз EpochGo представляет собой локально-первый многоагентный AutoML-движок, использующий оффлайн-модели Ollama \(qwen2.5-coder:7b\) для рассуждений и детерминированные пайплайны Scikit-Learn для выполнения. Это решение устраняет проблемы облачных затрат, рисков утечек табличных данных и галлюцинаций LLM при математическом моделировании. Движок работает полностью оффлайн на стандартном потребительском оборудовании \(Mac/Linux/Windows с 16 ГБ RAM\) без затрат на облачные вычисления.

reddit · r/MachineLearning · /u/Grouchy-Excitement28 · Oct 17, 14:48

**「Локальные LLM и детерминированные пайплайны」** Традиционные агентные фреймворки AutoML полагаются на облачные LLM, что приводит к recurring затратам и рискам утечки данных. LLM часто допускают ошибки в линейной алгебре, гиперпараметровой оптимизации и градиентном спуске. Локальные решения, использующие Ollama для reasoning и детерминированные пайплайны Scikit-Learn, решают эти проблемы, обеспечивая 100% оффлайн работу на потребительском оборудовании.

**「Влияние」** Пользователи могут разрабатывать и развертывать модели AutoML локально без облачных расходов и рисков приватности данных, обеспечивая соответствие нормам GDPR и DPDP.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/AryanDinakaran/EpochGo">GitHub - AryanDinakaran/EpochGo: Autonomous, local-first ...</a></li>
<li><a href="https://agihunt.info/en/p/1a1318c357f3b3cab84fb4b48df">EpochGo: local-first multi-agent AutoML… · AGI Hunt</a></li>
<li><a href="https://github.com/AryanDinakaran/EpochGo/blob/main/README.md">EpochGo/README.md at main · AryanDinakaran/EpochGo · GitHub</a></li>

</ul>
</details>

**Tags**: `#AutoML`, `#Ollama`, `#Scikit-Learn`, `#Local AI`, `#Open Source ML Tools`

---

<a id="item-tech-news-7"></a>
### [Маск: все объявления на X под эстетическими стандартами](https://x.com/elonmusk/status/2111131160348688395) ⭐️ 7.0/10

Элон Маск объявил, что все объявления на платформе X теперь будут подчиняться разумным эстетическим стандартам. Реклама, которая выглядит уродливо, слишком громко, шумно или содержит чрезмерно преувеличенные утверждения о продукте, больше не будет размещаться. Это изменение напрямую затрагивает всех рекламодателей, размещающих объявления на X.

telegram · zaihuapd · Oct 17, 00:22

**「Эстетические стандарты для рекламы на X」** Elon Musk объявил о введении разумных эстетических стандартов для всех рекламных объявлений на платформе X. Это включает запрет на размещение объявлений, которые считаются уродливыми, громкими, шумными или содержащими завышенные утверждения о продуктах. Такое правило является частью политики платформы по улучшению качества рекламы и пользовательского опыта.

**「Последствия для рекламодателей」** Рекламодатели будут вынуждены адаптировать креативы объявлений, чтобы соответствовать новым требованиям, что может ограничить использование определенных типов рекламы на платформе.

<details><summary>References</summary>
<ul>
<li>Elon Musk Sets New Aesthetic Standards for X Ads</li>
<li>&#x27;Reasonable aesthetic standard&#x27;: Elon Musk says X will ban ugly ...</li>
<li>Elon Musk announces Twitter ad aesthetic standards - Facebook</li>

</ul>
</details>

**Tags**: `#X platform`, `#Elon Musk`, `#advertising policy`, `#social media standards`, `#platform governance`

---

<a id="item-tech-news-8"></a>
### [Безпроводной jailbreak для iPhone 18 Pro](https://x.com/calif_io/status/2111080240978223545?s=20) ⭐️ 7.0/10

Была публично продемонстрирована безпроводной jailbreak для iPhone 18 Pro, сохраняющий состояние после перезагрузки без компьютера. Это первый полный публичный jailbreak с iOS 9. Атака использует подсистему cryptex, подделку TSS тикетов и обход PAC защиты. Apple 14 сентября закрыла 273 уязвимости, но атака обходит патчи.

telegram · zaihuapd · Oct 17, 10:34

**「Untethered jailbreak: концепция и значение」** Untethered jailbreak — это метод взлома iOS-устройств, при котором root-доступ сохраняется после перезагрузки без подключения компьютера для повторного применения. В отличие от tethered jailbreak&\#x27;ов, требующих постоянного вмешательства, untethered-варианты позволяют устройству оставаться взломанным автономно. Демонстрация на iPhone 18 Pro с iOS 27.0.1, проведённая командой Calif.io на Hexacon 2026, стала первым публичным полным джейлбрейком с iOS 9.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kucoin.com/news/flash/untethered-iphone-18-pro-jailbreak-survives-reboot-implications-for-crypto-custody">Untethered iPhone 18 Pro Jailbreak Survives Reboot ... - KuCoin</a></li>
<li><a href="https://cybersecuritynews.com/ios-27-0-1-jailbreak-demonstrated/">iOS 27.0.1 Untethered Jailbreak Demonstrated on iPhone 18 Pro</a></li>
<li><a href="https://www.explainx.ai/blog/calif-io-ios-27-0-1-untethered-jailbreak-iphone-18-pro-hexacon-ai-claimed-vs-verified-2026">iOS 27.0.1 Untethered Jailbreak: AI Role Checked (2026 ...</a></li>

</ul>
</details>

**Tags**: `#untethered jailbreak`, `#iOS security`, `#Apple security research`, `#iPhone hardware`, `#security bypass techniques`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Беркшир Хатхауэй инвестирует в Bending Spoons](https://www.cnbc.com/2026/10/17/bending-spoons-wants-to-revive-software-castoffs-berkshire-investing.html) ⭐️ 7.0/10

Беркшир Хатхауэй инвестировал более 900 миллионов долларов в Bending Spoons, включая долю в 330 миллионов долларов. Инвестиция, объявленная на этой неделе, привела к росту акций компании на 41% в первый день торгов, хотя часть этих прибылей была утрачена позже.

rss · CNBC Finance · Oct 17, 15:11

**「Фон」** Bending Spoons, миланская компания, владеющая старыми интернет-именами вроде AOL, Vimeo, Eventbrite и Evernote, получила крупное вложение от Беркшира Хатхауэя вскоре после своего дебюта на Nasdaq в июле.

**「Влияние」** Инвестиция подчеркивает влияние искусственного интеллекта на сектор программного обеспечения как услуги \(SaaS\), приводящее к сокращениям в портфеле Bending Spoons, включая Airtable, и снижению оценок устаревших продуктов.

**Tags**: `#Berkshire Hathaway`, `#Bending Spoons`, `#AI SaaS disruption`, `#Software M&amp;A`, `#SaaSpocalypse`

---

