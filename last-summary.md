# Horizon — новости дня - 2026-10-24

> Из 35 материалов отобрано 11 важных

---

**Технологические новости**
1. [Moonshot AI анонсирует Kimi K3.1 Pro и Highspeed](#item-tech-news-1) ⭐️ 8.0/10
2. [Рой как единый агент обучения с подкреплением](#item-tech-news-2) ⭐️ 8.0/10
3. [Dessa: Модель разговора, обученная только на речи](#item-tech-news-3) ⭐️ 7.0/10
4. [Is this the new cyber normal?](#item-tech-news-4) ⭐️ 7.0/10
5. [http2shell: RCE в Brotли для HTTP/2](#item-tech-news-5) ⭐️ 7.0/10
6. [Quick Study: быстрый инструмент для масляной живописи](#item-tech-news-6) ⭐️ 7.0/10
7. [Amazon Trainium наносит удар по королю обучения](#item-tech-news-7) ⭐️ 7.0/10
8. [Next-Concept Modeling: ускорение генерации текста в 31 раз](#item-tech-news-8) ⭐️ 7.0/10
9. [Память в больших языковых моделях: запоминаем больше или забываем?](#item-tech-news-9) ⭐️ 7.0/10
10. [PHP Foundation рекомендует временно отключить функцию отслеживания прогресса загрузки](#item-tech-news-10) ⭐️ 7.0/10
11. [Google обновила политику конфиденциальности для персонализированной рекламы](#item-tech-news-11) ⭐️ 7.0/10

---

## Технологические новости

<a id="item-tech-news-1"></a>
### [Moonshot AI анонсирует Kimi K3.1 Pro и Highspeed](https://www.kimi.ai/blog/kimi-k3-1-pro) ⭐️ 8.0/10

Moonshot AI объявила об обновлениях моделей Kimi K3.1 Pro и K3.1 Pro Highspeed. Эти модели представляют собой значительное улучшение больших языковых моделей с фокусом на производительность и безопасность. Анонс привлекает внимание сообщества благодаря обсуждениям практик выравнивания и глобальных последствий для ИИ.

hackernews · Jowsey · Oct 23, 16:59 · [Обсуждение](https://news.ycombinator.com/item?id=50212065)

**Обновление моделей Kimi K3.1 Pro:** Модели Kimi K3.1 Pro и Kimi K3.1 Pro Highspeed представляют собой обновление серии больших языковых моделей Kimi от компании Moonshot AI. Это следует за выпуском Kimi K3 в июле 2026 года, который был самой крупной открытой моделью с 2,8 триллионами параметров. Новая модель Kimi K3.1 Pro имеет 3 триллиона параметров, контекстное окно в 1 миллион токенов и доступна с открытыми весами.

**Открытые модели Kimi K3 для локального развертывания:** Модели Kimi K3.1 Pro и Highspeed теперь доступны в открытом весе на Hugging Face. Это позволяет разработчикам и организациям локально запускать мультимодальные агенты с контекстом в 1 миллион токенов для задач агентного кодирования, создания игр и обработки знаний, снижая затраты и повышая контроль над данными.

**Обсуждения в сообществе:** Пользователи отмечают, что модели иногда идентифицируют себя как Kimi от Moonshot, но принимают идентичность ChatGPT и ссылаются на глобальные системные руководства или «оценщика». Обсуждения также касаются подхода к кибербезопасности и результатов тестов Pac-Man, где Kimi K3.1 Pro показывает производительность, сравнимую с Claude Sonnet 5.5.

<details><summary>Ссылки</summary>
<ul>
<li><a href="https://extrapolator.ai/2026/10/23/moonshot-ai-releases-kimi-k3-1-pro-open-weights-with-1m-context/">Moonshot AI releases Kimi K3.1 Pro open weights with 1M ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kimi_%28AI%29">Kimi (AI) - Wikipedia</a></li>
<li><a href="https://www.kimi.ai/">Kimi AI with K3 | Built for Agentic Coding &amp; Knowledge Work</a></li>
<li><a href="https://onefast.ai/">OneFast API – Open &amp; Proprietary LLMs for Problem Solvers</a></li>
<li><a href="https://huggingface.co/moonshotai/Kimi-K3">moonshotai/ Kimi -K3 · Hugging Face</a></li>

</ul>
</details>

**Теги**: `#Kimi K3.1 Pro`, `#Moonshot AI`, `#LLM release`, `#AI safety`, `#Chinese AI models`

---

<a id="item-tech-news-2"></a>
### [Рой как единый агент обучения с подкреплением](https://www.reddit.com/r/MachineLearning/comments/1xdhf7r/r_the_hive_mind_is_a_single_reinforcement/) ⭐️ 8.0/10

Доказательство устанавливает математическую эквивалентность коллективного принятия решений через локальную имитацию в роях, таких как выбор места гнезда пчелами с помощью танца вальца, и одного агента обучения с подкреплением в среде многоруких бандитов. Распределение стратегий в популяции обновляется в соответствии с макроуровневым алгоритмом обучения с подкреплением, который мы называем Обучение Мейнарда-Кросса \(MCL\), где N индивидов действуют как N параллельных выборок среды с эффективной скоростью обучения alpha = 1/N. Это соответствие сохраняется как для модели имитации успеха, так и для взвешенной модели избирателя.

reddit · r/MachineLearning · /u/mistlab · Oct 23, 15:37

**Математическая эквивалентность имитации в роях и многоруких бандитов:** Многорукие бандиты — это модель принятия решений в обучении с подкреплением, где агент выбирает среди нескольких рук для максимизации вознаграждения. Коллективное принятие решений в роях насекомых, таких как пчёлы, основано на локальной имитации соседей по правилам имитации успеха или взвешенного голосования. Данная работа доказывает, что эти процессы имитации математически идентичны одному агенту обучения с подкреплением, агрегирующему выборки из многих параллельных сред.

**Влияние:** Доказав математическую эквивалентность локальной социальной имитации и одного агента обучения с подкреплением, работа предоставляет формальный механизм, объясняющий, как интеллект «умоподобной рои» и пробно-ошибочное обучение возникают на уровне группы из простых необучающихся индивидов. Помимо подтверждения эволюционных теорий коллективного познания в биологии, этот подход предлагает новые инструменты для анализа имитативных динамик в социальных и экономических системах и для разработки масштабируемых децентрализованных алгоритмов роевой робототехники.

<details><summary>Ссылки</summary>
<ul>
<li><a href="https://arxiv.org/abs/2410.17517">The Hive Mind is a Single Reinforcement Learning Agent</a></li>
<li><a href="https://link.springer.com/article/10.1007/s11721-026-00264-7">The hive mind is a single reinforcement learning agent - Springer</a></li>

</ul>
</details>

**Теги**: `#reinforcement learning`, `#swarm intelligence`, `#multi-armed bandits`, `#collective decision making`, `#theoretical equivalence`, `#multi-agent systems`

---

<a id="item-tech-news-3"></a>
### [Dessa: Модель разговора, обученная только на речи](https://block.xyz/dessa) ⭐️ 7.0/10

Dessa — это новая модель разговорного искусственного интеллекта, обученная исключительно на данных речи. Она обеспечивает естественное взаимодействие в полном дуплексе с низкой задержкой на потребительском оборудовании, таком как MacBook Pro M4 Max. Модель была обучена на одном NVIDIA GB200 NVL72, что делает её достижимой для локального развертывания. Демонстрации показывают впечатляющую реалистичность голосового общения.

hackernews · dsr12 · Oct 23, 19:09 · [Обсуждение](https://news.ycombinator.com/item?id=50213925)

**Обучение моделей только на речевых данных:** Традиционные большие языковые модели обучаются преимущественно на текстовых данных, что приводит к потере нюансов речи при использовании голосового интерфейса. Обучение моделей исключительно на данных разговоров человека позволяет захватывать все аспекты естественного общения, включая паузы, интонацию и эмоциональные оттенки, и может быть выполнено с значительно меньшим объемом данных.

**Воздействие:** Это открывает разработчикам возможность создания полностью локальных голосовых ассистентов с низкой задержкой на оборудовании MacBook Pro M4 Max.

**Обсуждение в сообществе:** Комментаторы отмечают впечатляющую эффективность обучения на одном GPU и локальное выполнение, называя это большим достижением для инди-разработчиков. Однако есть опасения по поводу маркетинговых заявлений и проблем с вызовом инструментов.

<details><summary>Ссылки</summary>
<ul>
<li><a href="https://block.xyz/dessa">Dessa - the Conversation Model trained only on speech - block.xyz</a></li>
<li><a href="https://aicoder.com/news/news-20261024-block-dessa-full-duplex-speech-model-trained-only-on-speech">Block unveils Dessa: a full-duplex speech model trained from ...</a></li>
<li><a href="https://www.unite.ai/block-unveils-dessa-a-full-duplex-speech-model-trained-on-conversation/">Block Unveils Dessa, a Full-Duplex Speech Model Trained on ...</a></li>

</ul>
</details>

**Теги**: `#conversational AI`, `#voice models`, `#full-duplex systems`, `#local machine learning`, `#speech processing`

---

<a id="item-tech-news-4"></a>
### [Is this the new cyber normal?](https://drew.silcock.dev/blog/is-this-the-new-cyber-normal/) ⭐️ 7.0/10

Blog post questions whether frequent cyber incidents like supermarket hacks signal a new normal in cybersecurity due to LLM-driven vulnerability speed, as discussed in high-engagement Hacker News comments.

hackernews · drewsberry · Oct 23, 11:04 · [Обсуждение](https://news.ycombinator.com/item?id=50207115)

**Теги**: `#cybersecurity`, `#LLMs`, `#zero-day exploits`, `#security debt`, `#vulnerability management`

---

<a id="item-tech-news-5"></a>
### [http2shell: RCE в Brotли для HTTP/2](https://nitter.click/AikidoSecurity/status/2113759110625906950?__galadriel=lPmlGl9id4oAd5UeBwMhlYKArHyr6lR2IDGujPwB5HV2kQ1aLoPWFd5A9sGuzNcmrp8fUso8qygmHcKTDZ8MNHWqQ3bDJcycV87xp_0VypzQLYj6O_RRHlZuQqj33oASGY2YLSoAiMjeOZN40h7Stf8AG7DPrGZbAPVKUXy36HoMudRbvwF3_r2uYNmfJMhpKzywQDM6Ab8) ⭐️ 7.0/10

Обнаружена критическая уязвимость http2shell — удалённое выполнение кода в обработке Brotли в HTTP/2. Уязвимость затрагивает Node.js, Python и другие runtimes, где включена декомпрессия Brotли. Фикс доступен в версии Brotли 1.2.1, предыдущие версии до 1.2.0 уязвимы.

hackernews · cowlevel · Oct 23, 23:30 · [Обсуждение](https://news.ycombinator.com/item?id=50216791)

**Контекст уязвимости:** Эта уязвимость http2shell связана с ошибкой в памяти в библиотеке Brotli при декомпрессии данных в формате HTTP/2, что затрагивает Node.js, Python и другие среды выполнения. Библиотека Brotli не получала обновлений почти год, с фиксом, закоммиченным в феврале, но обновление пакета Python до версии 1.2.1 появилось позже. Простой сервер Node.js не автоматически декомпрессирует тела Brotli-запросов, для активации уязвимости требуется промежуточное ПО или явные вызовы, аналогично другим платформам.

**Удалённое выполнение кода в Node.js и Python:** Затронутые пользователи Node.js и Python должны немедленно обновить свои версии до патченных релизов, чтобы предотвратить удалённое выполнение произвольного кода при декомпрессии Brotli-данных в HTTP/2-запросах.

**Обсуждение в сообществе:** В комментариях обсуждается, что уязвимость в основном влияет на клиентов, поскольку на серверах в Node.js, Python и C\# декомпрессия Brotли не включена по умолчанию. Также пользователи критикуют название уязвимости и отсутствие обновлений библиотеки Brotли почти год.

<details><summary>Ссылки</summary>
<ul>
<li><a href="https://thehackernews.com/2026/10/researchers-demonstrate-node2shell-rce.html">Researchers Demonstrate Node 2 Shell RCE Exploit on Node . js Build...</a></li>
<li><a href="https://www.aikido.dev/blog/node2shell-nodejs-brotli-rce-cve-2026-111497">Node 2 Shell : Node . js Brotli vulnerability allows remote code...</a></li>
<li><a href="https://pypi.org/project/brotli/">brotli · PyPI</a></li>
<li><a href="https://security.snyk.io/package/pip/brotli/1.2.1">brotli 1.2.1 | Snyk - security.snyk.io</a></li>
<li><a href="https://pwn.watch/i/nodejs-october-2026-security-releases">Node2Shell / HTTP2Shell: Brotli RCE (CVE-2026-111497) in Node ...</a></li>
<li><a href="https://blogs.jsmon.sh/cve-2026-111497-node-js-brotli-decoder-rce-node2shell-explained/">CVE-2026-111497: Node.js Brotli Decoder RCE — Node2Shell ...</a></li>
<li><a href="https://dev.to/anoymask/patch-alert-critical-gitlab-and-php-flaws-plus-nodejs-security-updates-43k9">Urgent Patch Alert: PHP2Shell, GitLab RCE, and Node.js Brotli RCE</a></li>

</ul>
</details>

**Теги**: `#HTTP/2`, `#Brotli`, `#RCE`, `#Node.js`, `#Security`

---

<a id="item-tech-news-6"></a>
### [Quick Study: быстрый инструмент для масляной живописи](https://simonwillison.net/2026/Oct/23/quick-study-painter/) ⭐️ 7.0/10

Simon Willison представил инструмент Quick Study, который преобразует фотографии в имитацию масляных картин за несколько секунд с помощью элемента холста и оператора Собеля. Пользователи загружают фото, и инструмент создаёт художественную версию изображения. Это основано на промпте для Claude Opus 5.5 High и не требует внешних библиотек, кроме шрифтов Google.

rss · Simon Willison · Oct 23, 21:35

**Фон:** Предыдущий эксперимент автора с Claude Fable симулировал акварельную иллюстрацию с помощью P5.js. Quick Study развивает эту идею, применяя элемент холста для имитации масляной живописи с использованием оператора Собеля для обнаружения границ.

**Влияние:** Пользователи могут быстро создавать художественные версии своих фотографий с помощью этого инструмента. Разработчики могут использовать этот подход для прототипирования подобных приложений обработки изображений.

**Теги**: `#AI-assisted development`, `#web canvas`, `#image processing`, `#artistic rendering`, `#rapid prototyping`

---

<a id="item-tech-news-7"></a>
### [Amazon Trainium наносит удар по королю обучения](https://newsletter.semianalysis.com/p/amazons-trainium-takes-a-strike-at) ⭐️ 7.0/10

Чип Amazon Trainium теперь применим для рабочих нагрузок по обучению искусственного интеллекта благодаря нативной интеграции с PyTorch и инструментам вроде TorchTitan, высококачественной непрерывной интеграции и профилировщику GPU Impossible Profiler. Это позволяет Amazon оспаривать доминирование NVIDIA в рынке оборудования для обучения. Хотя изменения инкрементальны, а не революционные, они делают Trainium конкурентным вариантом для разработчиков, использующих PyTorch.

rss · Semianalysis · Oct 23, 19:06

**Нативная поддержка PyTorch для AWS Trainium:** TorchNeuron является открытым исходным код расширением PyTorch, обеспечивающим нативную поддержку для чипов AWS Trainium. Это позволяет разработчикам использовать стандартные инструменты PyTorch, включая eager-режим для быстрой итерации и экспериментов, torch.compile для компиляции и распределенные фреймворки вроде TorchTitan с Fully Sharded Data Parallelism \(FSDP\). Таким образом, Trainium становится жизнеспособным для обучения моделей, а не только для задач инференса.

**Amazon Trainium теперь применим для обучения ИИ:** Amazon Trainium теперь конкурентоспособен для задач обучения моделей ИИ благодаря нативной интеграции с PyTorch и инструментам вроде TorchTitan. Это позволяет разработчикам и организациям тренировать крупные модели на чипах Amazon, снижая зависимость от NVIDIA и оптимизируя затраты.

<details><summary>Ссылки</summary>
<ul>
<li><a href="https://www.aboutamazon.com/news/innovation-at-amazon/torchneuron-pytorch-aws-trainium-chips-ai">Amazon&#x27;s TorchNeuron runs PyTorch on AWS Trainium chips</a></li>
<li><a href="https://awsdocs-neuron.readthedocs-hosted.com/en/v2.28.0/frameworks/torch/pytorch-native-overview.html">Native PyTorch for AWS Trainium — AWS Neuron Documentation</a></li>
<li><a href="https://pytorch.org/blog/introducing-torchneuron-native-pytorch-backend-for-aws-trainium/">Introducing TorchNeuron: Native PyTorch backend for AWS Trainium</a></li>
<li><a href="https://savedelete.com/read/amazon-trainium-ai-chips-2026.html">Amazon Takes On Nvidia: Selling Its Trainium AI Chips ...</a></li>
<li><a href="https://vucense.com/tech-reviews/compute-chips/amazon-trainium-ai-chip-adoption-sovereign-silicon/">Amazon Trainium 3 vs NVIDIA: Who Is Actually Switching (2026)</a></li>
<li><a href="https://truevalueresearch.com/articles/amzn-aws-trainium-2026.html">Amazon AWS Trainium 2 Is Nvidia&#x27;s First Real Competitor ...</a></li>

</ul>
</details>

**Теги**: `#Amazon Trainium`, `#AI Training Hardware`, `#NVIDIA Competition`, `#PyTorch`, `#Machine Learning Infrastructure`

---

<a id="item-tech-news-8"></a>
### [Next-Concept Modeling: ускорение генерации текста в 31 раз](https://www.reddit.com/r/MachineLearning/comments/1xd7bsu/i_just_came_across_nextconcept_modeling_and_the/) ⭐️ 7.0/10

В статье представлено Next-Concept Modeling \(NCM\) — иерархический метод дискретных кодов на основе VQ-VAE для ускоренной генерации текста. Модель сначала генерирует коды на грубом уровне, а затем предсказывает коды на более тонких уровнях в параллель. Декодер преобразует эти представления в текст. Авторы сообщают о скорости генерации текста до 31 раза выше, чем у базовых моделей диффузии на определенных бенчмарках.

reddit · r/MachineLearning · /u/PanelReader · Oct 23, 07:24

**Иерархическое кодирование с VQ-VAE:** Иерархическое моделирование с дискретными кодами, созданными с помощью векторно-квантизированного вариационного автокодировщика \(VQ-VAE\), позволяет представлять текст на разных уровнях детализации. В модели моделирования следующего концепта трансформер генерирует один уровень за раз, предсказывая все коды на уровне параллельно.

**Влияние Next-Concept Modeling на эффективность генерации текста:** Next-Concept Modeling предлагает иерархические дискретные коды для параллельной генерации от грубого уровня к тонкому, что приводит к ускорению генерации текста до 31 раза по сравнению с диффузионными моделями языковых моделей и снижает вычислительные затраты на этапе инференса.

<details><summary>Ссылки</summary>
<ul>
<li><a href="https://arxiv.org/abs/2610.14162">[2610.14162] Next-Concept Modeling: Fast, Parallel Coarse-to ...</a></li>
<li><a href="https://arxiv.org/pdf/2610.14162">Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text ...</a></li>
<li><a href="https://huggingface.co/papers/2610.14162">Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text ...</a></li>
<li><a href="https://arxiv.org/pdf/2610.14162">Next - Concept Modeling : Fast, Parallel Coarse-to-Fine Text Generation</a></li>

</ul>
</details>

**Теги**: `#Next-Concept Modeling`, `#hierarchical text generation`, `#language model efficiency`, `#VQ-VAE`, `#fast inference`

---

<a id="item-tech-news-9"></a>
### [Память в больших языковых моделях: запоминаем больше или забываем?](https://www.reddit.com/r/MachineLearning/comments/1xdpek9/are_we_solving_llm_memory_by_remembering_more/) ⭐️ 7.0/10

Пост утверждает, что модели с длинным контекстом в больших языковых моделях в основном решают проблему извлечения информации, а не управления памятью через забывание устаревших данных. Например, в агентах для кодирования, когда таймаут API меняется с 30 секунд на 5 секунд, обе версии остаются в контексте, и модель продолжает использовать старое значение без обновления знаний. Автор сравнивает подходы Трансформеров и RAG, требующие разрешения конфликтов между старой и новой информацией, с линейным вниманием, где ассоциации накапливаются, и новыми архитектурами вроде DeltaNet с обновлениями на основе ошибки предсказания и BDH \(Dragon Hatchling\) с геббсовой пластичностью синапсов. Пост предлагает тестировать, обновляет ли модель ответ при наличии противоречивых новых данных, сохраняя предыдущие знания, и интересуется подходящими бенчмарками.

reddit · r/MachineLearning · /u/Prestigious-Tip6030 · Oct 23, 20:39

**Проблема памяти LLM:** Проблема памяти в LLM выходит за рамки простого увеличения длины контекста, поскольку модели с длинным контекстом фокусируются на запоминании, но не всегда на забывании устаревших фактов, как в примерах с изменяющимися API в агентах кодирования. Традиционные архитектуры вроде Трансформеров и RAG сохраняют как старую, так и новую информацию, требуя разрешения конфликтов, в то время как DeltaNet использует обновления на основе ошибок предсказаний, а BDH \(Dragon Hatchling\) применяет геббаново обучение для пластичности синапсов. Это делает актуальным вопрос о тестировании моделей на адаптацию к противоречивым доказательствам и разработке соответствующих бенчмарков.

<details><summary>Ссылки</summary>
<ul>
<li><a href="https://blog.gopenai.com/attention-from-first-principles-deltanet-a8bd26bcbe9a">DeltaNet : Error -Driven Linear Attention with the Delta Rule | GoPenAI</a></li>
<li><a href="https://sustcsonglin.github.io/blog/2024/deltanet-3/">DeltaNet Explained (Part III) | Songlin Yang</a></li>
<li><a href="https://arxiv.org/abs/2509.26507">The Dragon Hatchling: The Missing Link between the ...</a></li>
<li><a href="https://pathway.com/research/bdh-explainer">BDH Architecture Explained: Pathway’s Dragon Hatchling</a></li>

</ul>
</details>

**Теги**: `#LLM memory`, `#long-context models`, `#continual learning`, `#knowledge updating`, `#DeltaNet`

---

<a id="item-tech-news-10"></a>
### [PHP Foundation рекомендует временно отключить функцию отслеживания прогресса загрузки](https://x.com/ThePHPF/status/2113580383875019242) ⭐️ 7.0/10

PHP Foundation рекомендует пользователям временно отключить функцию отслеживания прогресса загрузки, установив параметр включения отслеживания прогресса загрузки в 0, перед выпуском следующей версии PHP. Это необходимо для предотвращения уязвимости удаленного выполнения кода CVE-2026-115560. Уязвимость затрагивает только те приложения, где не по умолчанию обработчик сериализации переключен на «php». Ранее аналогичная рекомендация была дана из-за CVE-2026-109619.

telegram · zaihuapd · Oct 23, 13:46

**Функция отслеживания прогресса загрузки:** Функция отслеживания прогресса загрузки в PHP позволяет приложениям отображать прогресс загрузки файлов, записывая данные в суперглобальную переменную $\_SESSION. Она включена по умолчанию. Фонд PHP рекомендует временно отключить параметр session.upload\_progress.enabled, чтобы предотвратить уязвимость удаленного выполнения кода CVE-2026-115560 в следующей версии PHP, затрагивающую только приложения, где нестандартный serialize\_handler переключается на «php» во время выполнения.

**Рекомендация по отключению функции прогресса загрузки:** PHP-разработчики и организации, использующие загрузку файлов и сессии, должны временно отключить директиву session.upload\_progress.enabled в конфигурации PHP, чтобы предотвратить уязвимость удаленного выполнения кода \(RCE\) CVE-2026-115560 в следующей версии PHP. Это не влияет на стандартную функциональность загрузки файлов.

<details><summary>Ссылки</summary>
<ul>
<li><a href="https://www.getastra.com/blog/security-advisory/cve-2026-115560/">CVE-2026-115560: Another PHP Session-Handler RCE</a></li>
<li><a href="https://threatlandscape.io/blog/php-cve-2026-115560-session-upload-progress-rce-advisory">PHP CVE-2026-115560: Disable session.upload_progress.enabled</a></li>
<li><a href="https://github.com/ivst/CVE-2026-115560">CVE-2026-115560 — PHP session upload progress mitigation</a></li>
<li><a href="https://community.freepbx.org/t/php-cve-patching/110401">PHP CVE Patching - Security - FreePBX Community Forums</a></li>
<li><a href="https://github.com/eness/php2shell-CVE-2026-109618-CVE-2026-109619-PoC/blob/main/README.md">php 2shell-CVE- 2026 -109618-CVE- 2026 -109619-PoC/README.md at...</a></li>
<li><a href="https://socradar.io/blog/php2shell-cve-2026-109618-cve-2026-109619/">PHP 2Shell CVE- 2026 -109618 &amp; 109619: Affected Versions &amp; Fix</a></li>

</ul>
</details>

**Теги**: `#PHP`, `#Security Advisory`, `#RCE Vulnerability`, `#File Uploads`, `#Open Source`

---

<a id="item-tech-news-11"></a>
### [Google обновила политику конфиденциальности для персонализированной рекламы](https://www.theverge.com/tech/1017600/google-personal-intelligence-privacy-policy-ads-update) ⭐️ 7.0/10

Google обновила политику конфиденциальности, разрешив использовать данные из Gmail, Photos и Drive для персонализированной рекламы при включении функций Персональный интеллект, интегрированных с поиском и Гемини. Ранее политика гарантировала, что такие данные не будут применяться для рекламы. Google заявляет, что рекламодатели не получают доступ к файлам пользователей или их идентичности, не проводят таргетирование по чувствительным категориям; отключить эту опцию можно в настройках персонализации поиска.

telegram · zaihuapd · Oct 24, 02:37

**Personal Intelligence в Gemini:** Personal Intelligence — это функция в экосистеме Google Gemini, которая позволяет пользователям подключать данные из Gmail, Google Photos и Google Drive для персонализации ответов ИИ в поиске и Gemini. При включении функции Gemini может получать доступ к конкретному содержимому в Gmail, Google Photos, истории YouTube и активности поиска.

**Последствия для пользователей:** Пользователи, включившие Персональный интеллект, могут видеть персонализированную рекламу на основе данных из Gmail, Photos и Drive, но могут отключить эту функцию в настройках поиска. Это изменение политики может повлиять на восприятие приватности данных в Google.

<details><summary>Ссылки</summary>
<ul>
<li><a href="https://gemini.google.com/">Google Gemini</a></li>
<li><a href="https://gemini.google/subscriptions/">Google AI Pro &amp; Ultra — get access to Gemini 3.1 Pro &amp; more</a></li>
<li><a href="https://tech-now.io/en/blogs/google-gemini-adds-personal-intelligence-to-tap-gmail-drive-and-photos/">Google Gemini Adds Personal Intelligence to Tap Gmail , Drive and...</a></li>

</ul>
</details>

**Теги**: `#Google Privacy Policy Change`, `#Personal Intelligence`, `#Gemini AI`, `#Data for Advertising`, `#AI Privacy`

---

