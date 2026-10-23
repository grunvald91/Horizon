# Horizon — новости дня - 2026-10-23

> Из 42 материалов отобрано 20 важных

---

**Технологические новости**
1. [LLMs are making formal software verification feasible at a much larger scale](#item-tech-news-1) ⭐️ 8.0/10
2. [333 Tor-узлов с бэкдором отключены](#item-tech-news-2) ⭐️ 8.0/10
3. [SpaceX ведёт переговоры о аренде 80 тысяч базовых станций для создания оператора](#item-tech-news-3) ⭐️ 8.0/10
4. [OpenShell: безопасная приватная среда выполнения для флотов автономных агентов ИИ](#item-tech-news-4) ⭐️ 7.0/10
5. [Запуск полной прошивки iOS 16.5 на Android-устройствах](#item-tech-news-5) ⭐️ 7.0/10
6. [Подготовка GNU Taler к запуску в Германии](#item-tech-news-6) ⭐️ 7.0/10
7. [eMudhra прекращает глобальный бизнес по SSL/TLS сертификатам](#item-tech-news-7) ⭐️ 7.0/10
8. [Антропик донирует Agent Skills в Agentic AI Foundation](#item-tech-news-8) ⭐️ 7.0/10
9. [Carbon-X: открытая 14,8B модель ДНК и текста](#item-tech-news-9) ⭐️ 7.0/10
10. [Next-Concept Modeling: иерархический подход для ускоренной генерации текста](#item-tech-news-10) ⭐️ 7.0/10
11. [Open-XTTS-Trainer: Обучение XTTS v2 для новых языков](#item-tech-news-11) ⭐️ 7.0/10
12. [SteerTTS-edge: 11.84 МБ управляемая TTS-модель](#item-tech-news-12) ⭐️ 7.0/10
13. [Оракул выпустил предупреждение о критической уязвимости Java SE](#item-tech-news-13) ⭐️ 7.0/10
14. [小鹏 IRON 机器人升级：每 0.2 秒重新推理一次做出反馈](#item-tech-news-14) ⭐️ 7.0/10
15. [Запрещенный Nvidia B300 чип обнаружен в китайской государственной сети](#item-tech-news-15) ⭐️ 7.0/10
16. [DeepSeek и MiniMax завершили открытие и авторизацию ИИ за рубежом](#item-tech-news-16) ⭐️ 7.0/10
17. [Тренд Микро ошибочно отправила Linux-уязвимости в открытый LKML](#item-tech-news-17) ⭐️ 7.0/10
18. [Цены на отечественные большие модели удвоились до 13.46 юаня](#item-tech-news-18) ⭐️ 7.0/10

**Технологические блоги**
1. [vLLM обеспечивает поддержку MiniMax-M3.1-Flash с первого дня](#item-tech-blog-1) ⭐️ 8.0/10
2. [Производительность ПО: дизайн важнее языка](#item-tech-blog-2) ⭐️ 8.0/10

---

## Технологические новости

<a id="item-tech-news-1"></a>
### [LLMs are making formal software verification feasible at a much larger scale](https://www.anthropic.com/research/formal-verification) ⭐️ 8.0/10

Anthropic research shows LLMs can scale formal verification by generating proofs for RISC-V and Linux, previously infeasible at large scale.

hackernews · johnbender · Oct 22, 22:54 · [Обсуждение](https://news.ycombinator.com/item?id=50202217)

**Теги**: `#formal verification`, `#LLMs`, `#proof assistants`, `#RISC-V`, `#software reliability`

---

<a id="item-tech-news-2"></a>
### [333 Tor-узлов с бэкдором отключены](https://kaba.cx/posts/20261020_Tor/) ⭐️ 8.0/10

333 Tor-выходных узла с внедрённым бэкдором Ebury были отключены. Операторы Tor просканировали около 3000 узлов и обнаружили 333 заражённых, что составляет примерно 10%. Бэкдор позволяет перехватывать SSH-соединения на порту 22 и пересылать их на 12 серверов для кражи учетных данных. Узлы были помечены как BadExit 4 октября и полностью отключились на следующий день.

telegram · zaihuapd · Oct 22, 14:52

**Предыстория:** Выходные узлы в сети Tor позволяют пользователям подключаться к интернету. Ebury-бэкдор — это уязвимость, которая может быть использована для компрометации узлов и перехвата SSH-трафика. Атаки начались в августе, когда злоумышленники захватили серверы и блокировали порты для сбора незашифрованного почтового трафика.

**Последствия:** Пользователи Tor, использующие эти узлы для выхода в интернет, потеряли доступ к ним. Это влияет на анонимность и безопасность их соединений.

**Теги**: `#Tor`, `#backdoor`, `#security vulnerability`, `#SSH hijacking`, `#privacy`

---

<a id="item-tech-news-3"></a>
### [SpaceX ведёт переговоры о аренде 80 тысяч базовых станций для создания оператора](https://www.bloomberg.com/news/articles/2026-10-22/spacex-in-talks-to-access-80-000-cell-sites-for-wireless-network) ⭐️ 8.0/10

SpaceX ведёт переговоры о аренде 80 тысяч базовых станций у Crown Castle и других крупных инфраструктурных компаний для запуска собственного национального беспроводного оператора в США. Сделка может стоить десятки миллиардов долларов. После объявления акции Crown Castle выросли на 10% после закрытия, а у AT&amp;T, Verizon и T-Mobile упали примерно на 5%. SpaceX в этом месяце приобрела низкочастотный спектр и получила разрешение на запуск 15 тысяч спутников прямой связи с мобильными телефонами.

telegram · zaihuapd · Oct 23, 03:30

**Контекст Starlink и наземной связи:** SpaceX планирует арендовать 80 000 сотовых станций в США, чтобы запустить собственную национальную беспроводную сеть. Это развитие следует за приобретением низкочастотного спектра и одобрением запуска 15 000 спутников прямой связи с мобильными телефонами, что позволяет обычным смартфонам подключаться напрямую к спутниковой сети.

**Влияние на акции крупных телеком-операторов:** Акции AT&amp;T, Verizon и T-Mobile упали примерно на 5% после объявления SpaceX о переговорах по аренде 80 000 базовых станций для строительства собственной национальной беспроводной сети. Это отражает опасения инвесторов относительно прямой конкуренции в рынке мобильной связи.

<details><summary>Ссылки</summary>
<ul>
<li><a href="https://iz.ru/en/node/2189078">The media learned about SpaceX &#x27;s negotiations to lease 80,000 cell ...</a></li>
<li><a href="https://www.barrons.com/articles/spacex-stock-spectrum-telecom-at-t-e48e670c">SpaceX Is Crashing the Wireless Party. Telecom Stocks Are... - Barron&#x27;s</a></li>
<li><a href="https://www.spacex.com/launches/mission/?missionId=ax-4">SpaceX</a></li>
<li><a href="https://blog.kcex.com/markets/spacex-starlink-mobile-spectrum-deal-telecom-stocks-2026/">SpaceX Starlink Mobile Spectrum Deal: Why AT&amp;T, Verizon and T ...</a></li>
<li><a href="https://nai500.com/blog/2026/10/spacex-squeezes-at-t-verizon-t-mobile/">SpaceX Squeezes AT&amp;T, Verizon, T-Mobile | NAI 500</a></li>
<li><a href="https://www.indmoney.com/blog/us-stocks/why-verizon-att-tmobile-stocks-fell-spacex-deal">Why Verizon, AT&amp;T and T-Mobile Shares Fell After SpaceX’s 800 ...</a></li>

</ul>
</details>

**Теги**: `#SpaceX`, `#Starlink`, `#Telecommunications`, `#Wireless Infrastructure`, `#Spectrum`

---

<a id="item-tech-news-4"></a>
### [OpenShell: безопасная приватная среда выполнения для флотов автономных агентов ИИ](https://github.com/NVIDIA/OpenShell) ⭐️ 7.0/10

NVIDIA выпустила OpenShell — безопасную приватную среду выполнения для флотов автономных агентов ИИ. OpenShell ограничивает индивидуальные песочницы и коллективные разрешения, предотвращая сговор агентов, неавторизованные действия и экстракцию данных. Это решение позволяет агентам координировать задачи без риска нарушения безопасности или утечек.

hackernews · niemandhier · Oct 22, 17:44 · [Обсуждение](https://news.ycombinator.com/item?id=50198675)

**Безопасная среда выполнения для агентов ИИ:** Для безопасного использования флотов автономных агентов искусственного интеллекта необходима специализированная среда выполнения, которая ограничивает доступ каждого агента к ресурсам и предотвращает их взаимодействие для обхода ограничений. OpenShell предоставляет такую среду, объединяя индивидуальные песочницы с ядровым контролем, надзор за выполнением, централизованное управление и формальную верификацию политик. Это позволяет агентам читать файлы, устанавливать пакеты, вызывать API и использовать учетные данные без риска несанкционированного доступа или утечки данных.

**Влияние:** Организации, управляющие флотами агентов ИИ, могут безопасно предоставлять агентам доступ к файлам, пакетам и API, минимизируя риски коллюзии и экстракции данных. Это повышает надежность и безопасность систем на основе многоагентных технологий.

**Обсуждение сообщества:** В обсуждении пользователи подчеркивают, что OpenShell решает проблему коллюзии агентов через коллективные разрешения, хотя наивный подход может не хватить для предотвращения делегирования задач. Также отмечается использование контейнеров для управления агентами и ограничения сети для предотвращения экстракции данных.

<details><summary>Ссылки</summary>
<ul>
<li><a href="https://github.com/NVIDIA/OpenShell">GitHub - NVIDIA/OpenShell: OpenShell is the safe, private ...</a></li>
<li><a href="https://www.nvidia.com/en-us/ai/openshell/">NVIDIA OpenShell | Open, Secure Runtime for AI Agents</a></li>
<li><a href="https://build.nvidia.com/openshell">NVIDIA OpenShell</a></li>

</ul>
</details>

**Теги**: `#AI Agents`, `#Security`, `#Sandboxing`, `#Multi-Agent Systems`, `#NVIDIA`

---

<a id="item-tech-news-5"></a>
### [Запуск полной прошивки iOS 16.5 на Android-устройствах](https://github.com/oosexgang/hackios-xnu-kernel) ⭐️ 7.0/10

GitHub-проект позволяет запускать полную прошивку iOS 16.5 на Android-устройствах, включая POCO X5 Pro 5G и QEMU, с помощью кастомного ядра. Это исследовательский бенчмарк, где сессия длится заданное количество секунд, после чего ядро возвращается к загрузчику и передает лог. Доступен исходный код по адресу https://github.com/oosexgang/hackios-xnu-kernel и веб-сайт https://hackios-web.vercel.app/en.

hackernews · aghuang · Oct 22, 15:26 · [Обсуждение](https://news.ycombinator.com/item?id=50196718)

**Порт ядра XNU на Android:** Ядро XNU, которое является основой операционной системы Apple iOS, было выпущено с открытым исходным кодом, что позволяет его портировать на другие аппаратные платформы. Проект HackiOS демонстрирует успешную портировку ядра XNU версии xnu-8796.121.2 из iOS 16.5 на Android-устройства, такие как POCO X5 Pro 5G и эмулятор QEMU, с использованием кастомного EFI-загрузчика, замены драйверов, порта UEFI и слоя совместимости Wi-Fi Linux. Это позволяет запускать не изменённое пользовательское пространство iOS 16.5 в оперативной памяти без необходимости записи во флэш.

**Обсуждение в сообществе:** Пользователи находят проект впечатляющим благодаря работе на QEMU, POCO X5 Pro 5G и некоторых Xiaomi-устройствах. Однако часть комментаторов выражает сомнения в практической ценности, предлагая вместо этого запускать свободный Android на Apple-устройствах или хакать загрузчик Google-телефонов. Упоминается, что реплики iOS на Android могут повлиять на решения при покупке подержанных iPhone.

<details><summary>Ссылки</summary>
<ul>
<li><a href="https://github.com/oosexgang/hackios-xnu-kernel">GitHub - oosexgang/hackios-xnu-kernel</a></li>
<li><a href="https://daily.dev/posts/show-hn-run-full-ios-16-5-firmware-on-android-devices-1xbviab3j">Show HN: Run full iOS 16.5 firmware on Android Devices</a></li>
<li><a href="https://book.st-hakky.com/en/news/run-ios-16-5-firmware-on-android">HackiOS: Running unmodified iOS 16.5 on Android hardware</a></li>

</ul>
</details>

**Теги**: `#iOS reverse engineering`, `#Android firmware emulation`, `#kernel porting`, `#QEMU virtualization`, `#open source hardware hacking`

---

<a id="item-tech-news-6"></a>
### [Подготовка GNU Taler к запуску в Германии](https://www.taler.net/en/news/2026-13.html) ⭐️ 7.0/10

GNU Taler готовится к запуску в Германии в сотрудничестве с GLS Bank. Это открытая система цифровых платежей на основе слепых подписей, обеспечивающая приватность и интеграцию с банковскими счетами. Платежи не требуют доверия к платформе, в отличие от CBDC, которые полагаются на аппаратные enclaves.

hackernews · dewey · Oct 22, 16:14 · [Обсуждение](https://news.ycombinator.com/item?id=50197404)

**Разработка GNU Taler проектом NGI Taler:** Проект NGI Taler в течение трех лет работал над целью сделать Taler легально доступным в ЕС в качестве онлайн-платежной системы для повседневного использования.

**Влияние на клиентов GLS Bank:** Клиенты GLS Bank смогут проводить анонимные и безопасные транзакции с помощью GNU Taler без необходимости в отдельном банковском счете. Система разрабатывается как возможная основа для цифрового евро в Европе, с планами запуска в Германии и подачи заявки в BaFin на лицензию эмитента электронных денег.

**Обсуждение сообщества:** Комментарии пользователей отмечают техническое превосходство GNU Taler над Digital Euro благодаря меньшему доверию, необходимому для слепых подписей и онлайн-модели, по сравнению с требованиями к аппаратным enclaves для CBDC. Однако выражены опасения по поводу регуляторных ограничений на приватность и отсутствия поддержки работы в оффлайн-режиме, когда деньги истекают при длительном отключении.

<details><summary>Ссылки</summary>
<ul>
<li><a href="https://www.taler.net/en/news/2026-13.html">GNU Taler</a></li>
<li><a href="https://stage.taler.net/en/news/index.html">GNU Taler: News</a></li>
<li><a href="https://www.gls.de/taler/">Taler - in Zukunft digital &amp; sicher bezahlen - GLS Bank</a></li>
<li><a href="https://norberthaering.de/geldsystem/gnu-taler/">GLS testet Taler als Blaupause für den digitalen Euro und das ...</a></li>
<li><a href="https://www.taler.net/en/news/2026-13.html">GNU Taler</a></li>

</ul>
</details>

**Теги**: `#GNU Taler`, `#open source`, `#digital payments`, `#privacy`, `#fintech`

---

<a id="item-tech-news-7"></a>
### [eMudhra прекращает глобальный бизнес по SSL/TLS сертификатам](https://emudhra.com/en/press-release/emudhra-to-exit-global-ssl-tls-certificate-business) ⭐️ 7.0/10

eMudhra объявляет о прекращении своего глобального бизнеса по SSL/TLS сертификатам. Компания приняла это решение после инцидента безопасности, связанного с приватными ключами и проблемами в инфраструктуре. Инцидент вызвал дополнительное внимание к надежности центров сертификации в веб-ПКИ.

hackernews · bo0tzz · Oct 22, 13:33 · [Обсуждение](https://news.ycombinator.com/item?id=50195110)

**Инцидент с компрометацией сертификатов eMudhra:** Компания eMudhra объявила о добровольном выходе из глобального бизнеса по выпуску сертификатов SSL/TLS после обнаружения у восьми промежуточных сертификатов слабых приватных ключей. Этот инцидент, произошедший в октябре 2026 года, привел к отзыву доверия к корневым сертификатам eMudhra со стороны браузеров Chrome и Firefox. Обнаружение слабых ключей в инфраструктуре сертификатов подчеркивает уязвимости в системе Веб-PKI.

**Влияние на пользователей и организации:** Организации и пользователи, использующие сертификаты eMudhra для SSL/TLS, столкнутся с необходимостью замены сертификатов на сертификаты от других центров сертификации. Это вызвано решением компании добровольно выйти из глобального бизнеса по SSL/TLS сертификатам после инцидента, в котором были скомпрометированы приватные ключи восьми промежуточных CA.

**Обсуждение в Хакер Ньюс:** В комментариях к новости на Хакер Ньюс пользователи указывают на чрезмерную озабоченность по сравнению с уровнем сложности приватных ключей. Многие отмечают, что веб-ПКИ фундаментально уязвима, и концепция центров сертификации нуждается в переосмыслении, с упоминанием смягчающих мер от производителей браузеров.

<details><summary>Ссылки</summary>
<ul>
<li><a href="https://emudhra.com/en/press-release/emudhra-to-exit-global-ssl-tls-certificate-business">eMudhra to Exit global SSL / TLS Certificate Business</a></li>
<li><a href="https://thehackernews.com/2026/10/emudhra-to-exit-global-ssltls-business.html">eMudhra to Exit Global SSL / TLS Business After 8 Intermediate CA...</a></li>
<li><a href="https://blog.cloudflare.com/emudhra-certificate-compromise">8 eMudhra certificates are compromised. Here&#x27;s what you need ...</a></li>
<li><a href="https://securityboulevard.com/2026/10/emudhra-certificate-compromise-eight-weak-ca-keys-trigger-global-security-response/">eMudhra Certificate Compromise: Eight Weak CA Keys Trigger ...</a></li>
<li><a href="https://thehackernews.com/2026/10/emudhra-to-exit-global-ssltls-business.html">eMudhra to Exit Global SSL / TLS Business After 8 Intermediate CA...</a></li>
<li><a href="https://emudhra.com/en/press-release/emudhra-to-exit-global-ssl-tls-certificate-business">eMudhra to Exit global SSL / TLS Certificate Business</a></li>
<li><a href="https://www.moneycontrol.com/technology/emudhra-to-exit-global-website-security-certificate-business-after-key-generation-flaw-article-14057821.html">eMudhra to exit global website security certificate business after...</a></li>

</ul>
</details>

**Теги**: `#SSL/TLS`, `#Web PKI`, `#Certificate Authority`, `#Security Incident`, `#Cybersecurity`

---

<a id="item-tech-news-8"></a>
### [Антропик донирует Agent Skills в Agentic AI Foundation](https://simonwillison.net/2026/Oct/22/donating-agent-skills/) ⭐️ 7.0/10

Антропик донирует стандарт Agent Skills в Agentic AI Foundation под Linux Foundation. Компания заявляет о сохранении стандарта открытым, ориентированным на сообщество и нейтральным по отношению к поставщикам. Это происходит после донирования Model Context Protocol \(MCP\) и создания фонда совместно с Block и OpenAI в прошлом году.

rss · Simon Willison · Oct 22, 18:09

**Agentic AI Foundation и стандарт Agent Skills:** Agentic AI Foundation \(AAIF\) была основана в декабре 2025 года Anthropic, Block и OpenAI под управлением Linux Foundation. Anthropic ранее пожертвовала туда протокол Model Context Protocol \(MCP\) и теперь донирует стандарт Agent Skills, который был объявлен открытым стандартом в декабре 2025 года.

<details><summary>Ссылки</summary>
<ul>
<li><a href="https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation">Donating Agent Skills to the Agentic AI Foundation \ Anthropic</a></li>
<li><a href="https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation">Linux Foundation Announces the Formation of the Agentic AI ...</a></li>

</ul>
</details>

**Теги**: `#agentic ai`, `#anthropic`, `#ai standards`, `#open standards`, `#ai agents`

---

<a id="item-tech-news-9"></a>
### [Carbon-X: открытая 14,8B модель ДНК и текста](https://www.reddit.com/r/MachineLearning/comments/1xchayq/carbonx_is_an_open_148b_model_trained_jointly_on/) ⭐️ 7.0/10

Carbon-X — открытая декодерная модель с 14,8 млрд параметров, обученная совместно на ДНК и тексте с использованием общих токенов 6-меров. Модель достигает среднего 66,7% по пяти бенчмаркам ДНК при отключенном режиме мышления, что близко к 67,5% у GPT-6.1 Sol. Весы модели помещаются в одну 80 ГБ видеокарту в формате bfloat16 и распространяются под лицензией Apache 2.0.

reddit · r/MachineLearning · /u/jatingargiitk · Oct 22, 12:32

**Фон:** Совместное обучение моделей на ДНК и тексте с общими токенами 6-меров позволяет объединить два модальности в одной модели. Ранее такие подходы были ограничены большими вычислительными ресурсами, но дополнительное обучение на 302 млрд токенов делает это возможным для открытых моделей.

**Влияние:** Это позволяет проводить локальный анализ геномики для чувствительных датасетов на одном ГПИ, не требуя облачных сервисов.

**Теги**: `#DNA-text multimodal models`, `#bioinformatics AI`, `#open source LLMs`, `#single-GPU inference`, `#genomics`

---

<a id="item-tech-news-10"></a>
### [Next-Concept Modeling: иерархический подход для ускоренной генерации текста](https://www.reddit.com/r/MachineLearning/comments/1xd7bsu/i_just_came_across_nextconcept_modeling_and_the/) ⭐️ 7.0/10

В статье по Next-Concept Modeling \(NCM\) описывается иерархический подход на основе VQ-VAE. Модель генерирует дискретные коды на разных уровнях иерархии параллельно, начиная с грубого уровня, а затем переходит к более детальным кодам. Финальный декодер преобразует эти коды в текст. Авторы сообщают о скорости генерации, которая в 31 раз выше, чем у моделей диффузии на соответствующих бенчмарках.

reddit · r/MachineLearning · /u/PanelReader · Oct 23, 07:24

**Архитектура Next-Concept Modeling:** Next-Concept Modeling \(NCM\) — это двухэтапная, грубо-точная архитектура для генерации текста. Многоуровневая остаточная VQ-VAE кодирует текст в иерархию дискретных кодов, а трансформер генерирует один уровень за раз, предсказывая все коды в пределах уровня параллельно. Это позволяет значительно ускорить процесс генерации по сравнению с диффузионными моделями языка.

<details><summary>Ссылки</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2610.14162">Next - Concept Modeling : Fast, Parallel Coarse-to-Fine Text Generation</a></li>
<li><a href="https://github.com/HazyResearch/ncm">GitHub - HazyResearch/ ncm : NCM : Next Concept Modeling · GitHub</a></li>
<li><a href="https://huggingface.co/mrfakename/ncm-webgpu-weights/tree/main">mrfakename/ ncm -webgpu-weights at main</a></li>

</ul>
</details>

**Теги**: `#Next-Concept Modeling`, `#language model architectures`, `#parallel text generation`, `#fast inference`, `#hierarchical discrete codes`, `#VQ-VAE`

---

<a id="item-tech-news-11"></a>
### [Open-XTTS-Trainer: Обучение XTTS v2 для новых языков](https://www.reddit.com/r/MachineLearning/comments/1xcurgj/i_built_openxttstrainer_now_you_can_add_new/) ⭐️ 7.0/10

Пользователь выпустил Open-XTTS-Trainer — открытый модульный набор для обучения трёх компонентов XTTS v2. Теперь можно добавлять новые языковые скрипты, такие как хинди или арабский, и решать проблему с фиксированными словарями. Инструмент включает полный цикл обучения GPT, DVAE токенизатора и HiFi-GAN вокодера и доступен в виде 1-клик демо на Google Colab под лицензией MPL-2.0.

reddit · r/MachineLearning · /u/yashubhakt · Oct 22, 21:03

**Закрытие Coqui AI и пробелы в обучении XTTS v2:** После закрытия Coqui AI в 2023 году сообщество осталось без официальных обучающих рецептов для DVAE аудио токенизатора и Latent HiFi-GAN вокодера XTTS v2. Это привело к проблемам с дообучением модели для новых языковых скриптов, таких как арабский или хинди, из-за фиксированного словаря и зависимостей от torchcodec. В репозитории Coqui AI был открыт запрос на переобучение этих компонентов.

**Влияние:** Теперь пользователи могут обучать все компоненты XTTS v2 для поддержки новых языков без крашей матрицы эмбеддингов. Это решает проблему после закрытия Coqui AI и позволяет создавать локальные модели синтеза речи для индийских, арабских и других языков.

<details><summary>Ссылки</summary>
<ul>
<li><a href="https://github.com/coqui-ai/TTS/issues/3323">Retraining vocoder (hifigan) and dvae in XTTS #3323 - GitHub</a></li>
<li><a href="https://huggingface.co/amitbhakt/open-xtts-trainer">amitbhakt/open-xtts-trainer · Hugging Face</a></li>

</ul>
</details>

**Теги**: `#XTTS v2`, `#text-to-speech`, `#open-source`, `#machine-learning`, `#Coqui shutdown`

---

<a id="item-tech-news-12"></a>
### [SteerTTS-edge: 11.84 МБ управляемая TTS-модель](https://www.reddit.com/r/MachineLearning/comments/1xcum4s/we_shrank_our_steerable_small_tts_to_1184_mb_wer/) ⭐️ 7.0/10

Авторы выпустили SteerTTS-edge — 11.84 МБ квантованную версию управляемой TTS-модели. Модель прошла int4-квантизацию с помощью квантизации с обучением с учетом квантизации, архитектуру Mamba-3 и дистиллированный вокодер, при этом WER остался на уровне 0.96%, а UTMOS снизился на около 0.1. Все 12 параметров управления сохраняют 95% эффекта от версии fp32.

reddit · r/MachineLearning · /u/Working\_Hat5120 · Oct 22, 20:57

**SteerTTS: компактная управляемая система синтеза речи:** Модель SteerTTS от WhissleAI представляет собой компактную систему синтеза речи на английском языке, которая позволяет управлять параметрами произношения с помощью числовых контролей и тегов стиля. Ранее опубликованная версия v1 стала основой для дальнейшей оптимизации.

**Влияние:** Это открывает возможности для запуска SteerTTS-edge в приложениях на устройствах с ограниченной памятью, таких как мобильные телефоны, без значительной потери качества синтеза речи и функций управления.

<details><summary>Ссылки</summary>
<ul>
<li><a href="https://github.com/WhissleAI/steer-tts">GitHub - WhissleAI/steer-tts: SteerTTS: a tiny, measurably ...</a></li>
<li><a href="https://huggingface.co/WhissleAI/steer-tts">WhissleAI/steer-tts · Hugging Face</a></li>

</ul>
</details>

**Теги**: `#TTS`, `#model compression`, `#int4 quantization`, `#Mamba architecture`, `#edge deployment`

---

<a id="item-tech-news-13"></a>
### [Оракул выпустил предупреждение о критической уязвимости Java SE](https://www.oracle.com/security-alerts/alert-cve-2026-91403.html) ⭐️ 7.0/10

Оракул выпустил предупреждение о критической уязвимости CVE-2026-91403 в компоненте JSSE Java SE, которая позволяет удалённым атакующим без аутентификации нарушать конфиденциальность и целостность данных. Затронуты версии Java SE 8u511, 11.0.33, 17.0.21, 21.0.13, 25.0.5 и 27.0.1, а также GraalVM. Oracle предоставил патчи для обновления.

telegram · zaihuapd · Oct 22, 12:30

**Уязвимость в компоненте JSSE платформы Java SE:** Компонент JSSE платформы Java SE обеспечивает безопасные сетевые соединения. Уязвимость CVE-2026-91403 в этом компоненте позволяет злоумышленникам удаленно атаковать без аутентификации, нарушая конфиденциальность и целостность данных. Oracle выпустила предупреждение безопасности, затрагивающее несколько версий Java SE и GraalVM, и рекомендует пользователям как можно скорее обновить свои системы.

**Последствия для пользователей:** Пользователи и разработчики, использующие затронутые версии Java SE в производственных системах, должны немедленно обновить до исправленных версий, чтобы предотвратить удалённые атаки, угрожающие данным.

<details><summary>Ссылки</summary>
<ul>
<li><a href="https://www.oracle.com/security-alerts/cve-2026-91403verbose.html">Text Form of Security Alert CVE - 2026 - 91403 Risk Matrices</a></li>
<li><a href="https://blogs.oracle.com/security/security-alert-cve-2026-91403-released">Security Alert CVE - 2026 - 91403 Released | security</a></li>
<li><a href="https://www.cve.org/CVERecord?id=CVE-2026-91403">cve.org/CVERecord?id= CVE - 2026 - 91403</a></li>

</ul>
</details>

**Теги**: `#Java SE`, `#Security Vulnerability`, `#Oracle Patch`, `#JSSE`, `#Critical Update`

---

<a id="item-tech-news-14"></a>
### [小鹏 IRON 机器人升级：每 0.2 秒重新推理一次做出反馈](https://www.ithome.com/1/016/667.htm) ⭐️ 7.0/10

XPeng has upgraded its IRON humanoid robot with a second-generation VLA model that re-infers every 0.2 seconds and predicts actions up to 6 seconds ahead to handle dynamic interactions like unexpected hand changes.

telegram · zaihuapd · Oct 22, 13:37

**Теги**: `#VLA model`, `#humanoid robotics`, `#real-time inference`, `#embodied AI`, `#robotics`

---

<a id="item-tech-news-15"></a>
### [Запрещенный Nvidia B300 чип обнаружен в китайской государственной сети](https://theinference.org/article/china-s-state-money-bought-banned-nvidia-b300-servers-then-redacted-the-receipts) ⭐️ 7.0/10

Китайская государственная группа полупроводниковой аренды приобрела 32 сервера Asus с чипами Nvidia B300 для развертки в сети China Mobile Ningxia. Сделка на сумму свыше 3 млрд юаней является частью закупки более 700 серверов. Чип B300 относится к самому строгому уровню американского экспортного контроля, практически запрещенному для Китая. После первоначальной регистрации сделки документы были переподаны с закрашенным описанием оборудования, а Nvidia проводит расследование совместно с партнерами по производству.

telegram · zaihuapd · Oct 22, 15:22

**Экспортные ограничения США на чипы Nvidia B300:** Чипы Nvidia B300 входят в серию Blackwell и подпадают под самые жесткие экспортные ограничения США в отношении Китая. Через лизинговую компанию, финансируемую государственными фондами Шэньчжэня и Пекина, были профинансированы покупки более 700 серверов с этими чипами для China Mobile в Нинся. После подачи документов они были отредактированы, что привело к расследованию Nvidia совместно с партнерами по производству.

**Обход экспортных ограничений на чипы Nvidia B300:** Китайские государственные структуры через холдинговую лизинговую компанию приобрели 32 сервера Asus с чипами Nvidia B300 для развертывания в сети China Mobile в Нинся, несмотря на запрет. После подачи документов на транзакцию в них были удалены описания оборудования, что привело к расследованию Nvidia совместно с партнерами по производству и подчеркивает сложности enforcement экспортного контроля США на высокопроизводительные ИИ-чипы.

<details><summary>Ссылки</summary>
<ul>
<li><a href="https://finance.yahoo.com/technology/ai/articles/chinese-state-funds-backed-purchases-215942410.html?fr=sycsrp_catchall">Chinese state funds backed purchases of restricted Nvidia AI ...</a></li>
<li><a href="https://www.tftc.io/nvidia-blackwell-chinese-state-financing-export-controls">Nvidia Blackwell Chips Tied to Chinese State Financing · TFTC</a></li>
<li><a href="https://startupfortune.com/chinese-state-backed-lender-financed-nvidia-blackwell-chip-purchases-for-a-listed-firm/">Chinese state-backed lender financed Nvidia Blackwell chip ...</a></li>
<li><a href="https://geniustechlab.com/posts/2026-08-26-nvidia-supermicro-b300-smuggling-taiwan-china-export-controls-2026">Taiwan Indicts 9: The Nvidia B 300 Server Smuggling... | GeniusTechLab</a></li>
<li><a href="https://www.linkedin.com/posts/markdhirsch_ai-china-semiconductors-activity-7470150344644362240-VnP7">China Announces $2.85B AI Data Center Buildout | LinkedIn</a></li>
<li><a href="https://www.ft.com/content/6f806f6e-61c1-4b8d-9694-90d7328a7b54?syn-25a6b1a6=1">Nvidia AI chips worth $1bn smuggled to China after Trump export ...</a></li>

</ul>
</details>

**Теги**: `#Nvidia B300`, `#US export controls`, `#AI hardware supply chain`, `#China semiconductor procurement`, `#US-China tech tensions`

---

<a id="item-tech-news-16"></a>
### [DeepSeek и MiniMax завершили открытие и авторизацию ИИ за рубежом](https://mp.weixin.qq.com/s/hoeaIXEFagSHugSgMjFe9g) ⭐️ 7.0/10

После публичного обсуждения проекта пересмотра «Каталога технологий, ограниченных для экспорта» компании DeepSeek и MiniMax успешно прошли регистрацию и приступили к открытию исходного кода и авторизованному использованию своих технологий за рубежом. Каталог включает 23 позиции в сфере искусственного интеллекта, включая большие модели, интеллектуальных агентов, кластеры вычислений и обработку информации. Министерство торговли подчеркнуло, что основная цель — разграничение границ, а не простое ограничение экспорта.

telegram · zaihuapd · Oct 22, 16:10

**Контекст:** 16 октября Министерство торговли и Министерство науки и технологии КНР опубликовали проект пересмотра «Каталога технологий, ограниченных для экспорта», в который вошли 23 позиции в области ИИ. Это вызвало вопросы о возможном изменении политики в сторону большей открытости технологий. Компании DeepSeek и MiniMax, как ведущие игроки, уже завершили необходимые процедуры.

**Последствия:** Для разработчиков и организаций, использующих модели DeepSeek и MiniMax, это открывает возможности по открытию исходного кода и лицензированию за рубежом, увеличивая глобальный доступ к технологиям при соблюдении новых регуляторных рамок.

**Теги**: `#AI Export Controls`, `#Open Source AI`, `#China Tech Policy`, `#DeepSeek`, `#MiniMax`

---

<a id="item-tech-news-17"></a>
### [Тренд Микро ошибочно отправила Linux-уязвимости в открытый LKML](https://www.phoronix.com/news/LKML-New-Trend-Vulnerabilities) ⭐️ 7.0/10

Тренд Микро Zero Day Initiative ошибочно отправила несколько отчетов о Linux-ядерных уязвимостях в публичный список рассылки LKML вместо приватного канала безопасности. Уязвимости, включая удаленное выполнение кода через SMB Direct и гонки в KSMBD, имеют оценки CVSS до 9.0 и еще не исправлены в основном дереве. Линусовский номер два Грег Кроах-Хартман ответил на каждое сообщение, указав на ошибки в процессе.

telegram · zaihuapd · Oct 23, 04:30

**Предыстория:** Список рассылки LKML является основным публичным форумом для обсуждения изменений в Linux-ядре. Программа Zero Day Initiative Trend Micro предназначена для ответственного раскрытия уязвимостей, при котором отчеты обычно отправляются приватно разработчикам. Это позволяет подготовить и протестировать патчи до публичного анонса.

**Последствия:** Ошибка привела к потенциальному раскрытию высокосерьезных неисправленных уязвимостей публично до получения фиксов от разработчиков. Это может затронуть пользователей Linux и разработчиков, а также подчеркнуло проблемы в процессе ответственного раскрытия уязвимостей в открытом проекте.

**Теги**: `#Linux Kernel`, `#Security Vulnerability`, `#Responsible Disclosure`, `#LKML`, `#Greg Kroah-Hartman`

---

<a id="item-tech-news-18"></a>
### [Цены на отечественные большие модели удвоились до 13.46 юаня](https://mp.weixin.qq.com/s/JcsPrHgEkeseGBHAJ7s9mA) ⭐️ 7.0/10

Китайская академия информации и телекоммуникаций 23 октября 2026 года выпустила отчет о мониторинге производительности сервиса токенов больших моделей за 2026 год. После двух лет ценовой войны средняя цена отечественных больших моделей удвоилась с 6.8 юаня во второй половине 2025 года до 13.46 юаня. Нормализованная средняя цена типичных зарубежных моделей составляет 117.8 юаня.

telegram · zaihuapd · Oct 23, 06:05

**Ценовые войны на рынке больших моделей:** Китайская академия информации и коммуникационных технологий \(CAICT\) 23 октября 2026 года опубликовала доклад о производительности сервиса токенов больших моделей \(2026\). Данные мониторинга охватывают период с января по август 2026 года. В предыдущие два года на рынке больших моделей наблюдались интенсивные ценовые войны, что привело к снижению цен, а после этого начался их рост.

**Последствия для затрат:** Компании и разработчики, использующие отечественные большие модели, столкнутся с почти двукратным увеличением расходов на сервис токенов.

<details><summary>Ссылки</summary>
<ul>
<li><a href="https://www.sohu.com/a/1091556892_121124361">中国信通院人工智能所联合发布《大模型词元服务性能监测报告（2026年...</a></li>
<li><a href="https://www.caict.ac.cn/kxyj/qwfb/ztbg/202610/P020261023366841562136.pdf">大模型词元服务性能监测报告</a></li>

</ul>
</details>

**Теги**: `#AI pricing trends`, `#LLM costs`, `#China AI market`, `#CAICT report`, `#token service monitoring`

---

## Технологические блоги

<a id="item-tech-blog-1"></a>
### [vLLM обеспечивает поддержку MiniMax-M3.1-Flash с первого дня](https://vllm.ai/blog/2026-10-23-minimax-m31-flash) ⭐️ 8.0/10

rss · vLLM Blog · Oct 23, 00:00

**Фон:** МиниMax-M3.1-Flash представляет собой последнюю модель семейства MiniMax-M3, оптимизированную для задач рассуждения, кодирования, агентных и визуальных задач с использованием NVFP4 квантизации KV-кэша и MoE-весов. Традиционные подходы к инференсу таких моделей на длинных контекстах страдают от высокой задержки и низкой пропускной способности из-за ограничений памяти и вычислений.

**Решение:** vLLM обеспечивает поддержку модели с первого дня на графических процессорах NVIDIA Blackwell, Rubin и AMD MI350. Ключевые оптимизации включают использование инструкции QMUL4 для деквантизации формата NVFP4 в FP8 внутри ядра, ранний релиз TMEM в MegaMoE, параллелизм контекста декодирования индексер и слияние QKV GEMM с нормированием, RoPE и вставкой кэша KV, обеспечивающие ускорение префилла на 1.1–1.6 раза при 512+ токенах и снижение P50 времени до первого токена на 19% на TP4, а также бэкенд FlashInfer PrimiTS для drafter DSpark, ускоряющий на 1.3–2 раза. На AMD добавлены ядро MSA нативное для NVFP4 с таблицей деквантизации, DCP и моно ядро, дающие 2–3 раза прирост производительности, а бенчмарки показывают до 418.9 токенов в секунду на пользователя на GB300, 724.9 на Rubin и 133.3M токенов на доллар TCO на MI355X.

**Вывод:** vLLM достигает значительного ускорения и снижения затрат на обслуживание MiniMax-M3.1-Flash благодаря аппаратно-оптимизированным ядрам и фьюжнам. Это открывает путь к эффективному инференсу на длинных контекстах и агентных задачах на различных GPU.

**Теги**: `#vLLM`, `#MSA Sparse Attention`, `#NVFP4 Quantization`, `#Multi-GPU Optimization`, `#Speculative Decoding`

---

<a id="item-tech-blog-2"></a>
### [Производительность ПО: дизайн важнее языка](https://seangoedecke.com/software-is-slow-because-of-bad-design-not-slow-languages/) ⭐️ 8.0/10

rss · Sean Goedecke · Oct 23, 00:00

**Фон:** Многие считают, что искусственный интеллект ускорит программное обеспечение, переписав его на более быстрые языки, такие как C или Rust. Однако это не всегда так, потому что производительность программного обеспечения в большинстве случаев определяется дизайном, а не скоростью языка.

**Решение:** Рассмотрим простой сайт CRUD с базой данных. Для каждого запроса около 50% времени может уходить на запросы к базе данных. По закону Амдаля, переписывание на C ускорит только эту половину, давая прирост примерно в 1.5 раза. Многие программы тратят время на ожидание данных от внешних API или дисков, как в curl. Хотя некоторые задачи требуют много вычислений, медленные языки часто используют библиотеки на C для их выполнения, например cmark-gfm для преобразования markdown в HTML. В опыте автора значительные ускорения пришли от редизайна, таких как кэширование медленных операций, выполнение их асинхронно, параллельное выполнение или исправление N+1 проблем в SQL. Даже в случае переписывания программы Брайана Кантрилла из C в Rust, дизайн оказался важнее языка, приведя к ускорению на 30% за счет предпочтения Rust кеша-эффективным B-деревьям вместо бинарных деревьев поиска.

**Вывод:** Таким образом, переписывание программного обеспечения на быстрые языки не является эффективным способом ускорения в большинстве случаев. Для достижения значительных улучшений с помощью искусственного интеллекта следует сосредоточиться на профилировании и редизайне программы, чтобы уменьшить объем выполняемой работы.

**Теги**: `#software performance`, `#programming languages`, `#optimization`, `#I/O-bound`, `#software architecture`

---

