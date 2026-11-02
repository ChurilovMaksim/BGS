# Adversarial-рецензия: где формулировка сильнее доказательства

## Предмет и метод

Проверены: реестр `~/workspace/bgs-analysis/claims.json` (схема
`bgs-claims-v1`, обновлён 2026-10-29, 232 записи), `~/workspace/bgs-analysis/gap_summary_20261029.md`,
`~/workspace/bgs-analysis/audit_partial_20261029.md`,
`~/workspace/bgs-analysis/build_attempts.md` и
`~/workspace/bgs-formalization/formalization/README.md` (срез 29 октября).
Lean не собирался, файлы в main не менялись, ничего не удалялось.

Важная оговорка, без которой рецензия была бы несправедливой: сами
документы проекта во многих местах честны. Завышение возникает главным
образом тогда, когда цитируют голое поле `state: "proved"` из реестра,
отбрасывая соседние поля `ledger_status` и `boundary`. Поэтому почти
каждое исправление ниже — это не удаление результата, а возвращение
квалификатора, который в реестре уже есть, но теряется при цитировании.

## Счёт, посчитанный по реестру, а не взятый на веру

- Всего записей: 232. `proved`: 201, `verification-pending`: 14,
  `conditional`: 9, `open`: 8.
- Из 201 `proved`: со ссылкой в `formalization` — только 62, без ссылки — 139.
- Из 201 `proved`: без верификаторов (`verifiers: []`) — 34, без
  свидетельств (`evidence: []`) — 12.
- По тексту `ledger_status` среди `proved`: начинается с `PROJECT` — 119,
  начинается с `EXACT` — 35, содержит `AUTHOR` — 71, содержит
  `INDEPENDENT INTERNAL` — 62, содержит `REFEREE` — только 5.
- `proved` с внешними зависимостями (`external_dependencies` непусто) — 46.
- В 118 записях поле `boundary` содержит оговорки вида `NOT_RUN`,
  `not a …`, `not the …`, `only`.

Вывод из счёта один: число «201 proved» нельзя произносить без
продолжения «по внутреннему реестру проекта, из них 139 без ссылки
на Lean и только 5 с пометой о рецензенте».

## 16 пунктов завышения

### 1. «Proved» выдаётся за доказанное вообще, а это proved по внутреннему реестру

- Источник: `bgs-analysis/claims.json`, поле `state` у 201 записи;
  честная расшифровка — в `bgs-analysis/key_files/STATUS.md`:
  > «"Proved" reports the project registry at its stated scope, not external refereeing.»
- Завышение: в пересказе «proved» звучит как «доказано математическим
  сообществом», хотя 119 из 201 записей начинаются в `ledger_status`
  с `PROJECT`, а 71 содержат `AUTHOR`.
- Исправление одной фразой: «Доказано в рамках внутреннего реестра
  проекта, без внешнего рецензирования, если не указано иное.»

### 2. «Independent internal review» выдаётся за независимую проверку

- Источник: `claims.json`, 62 записи `proved` с `INDEPENDENT INTERNAL`
  в `ledger_status`, например BGS-RES-015:
  > «PROJECT PROOF (COMPLETE FINITE-DIFFERENCE PROOF) + INDEPENDENT INTERNAL REVIEW».
- Завышение: слово «independent» читается как «внешний независимый
  рецензент», хотя по смыслу реестра это внутренняя перепроверка
  внутри проекта; внешних рецензентов (`REFEREE`) — всего 5 записей.
- Исправление одной фразой: «Проверено повторной внутренней
  перепроверкой в проекте, а не внешним рецензентом.»

### 3. Авторская проверка выдаётся за проверку

- Источник: `claims.json`, 71 запись `proved` с `AUTHOR` в
  `ledger_status`, например BGS-TRACE-115:
  > «ANALYTIC PROOF + AUTHOR SELF-REVIEW».
- Завышение: «proof + check» в кратком пересказе превращается
  в два независимых голоса, хотя оба голоса — автор.
- Исправление одной фразой: «Авторское доказательство с авторской
  же проверкой; независимой проверки нет.»

### 4. Одиннадцать записей с удалённым верификатором и проваленным аудитом

- Источник: `claims.json`, `ledger_status` у BGS-TRACE-095,
  BGS-TRACE-096, BGS-TRACE-097, BGS-TRACE-098, BGS-TRACE-099,
  BGS-TRACE-100, BGS-TRACE-101, BGS-TRACE-102, BGS-TRACE-103,
  BGS-TRACE-104, BGS-TRACE-105:
  > «SOLE LISTED VERIFIER REMOVED: verify_integration.py IS AN INTEGRITY/SCOPE CHECK, NOT A PROOF CHECKER; ITS EVIDENCE all_packet_audit.json RECORDS all_valid: false (58 COMPLETED / 5 FAILED / 1 TIMEOUT)».
- Завышение: любое упоминание этих записей рядом со словом
  «верифицировано» — у них сейчас `verifiers: []`, а единственный
  названный ранее скрипт проверял целостность и объём, а не
  доказательство, и его же аудит дал `all_valid: false`.
- Исправление одной фразой: «Верификатор удалён как непригодный,
  его аудит дал all_valid: false; утверждение не верифицировано.»

### 5. Одиннадцать «proved» вообще без claim-specific контроля

- Источник: `claims.json`, BGS-TRACE-057, 058, 059, 061, 062, 063, 064,
  065, 066, 067, 068, `ledger_status`:
  > «PROJECT PROOF WITH EXPLICIT HYPOTHESES; INTERNAL AUDIT ONLY; NO CLAIM-SPECIFIC FINITE CONTROL (SHARED CHAT-RESEARCH CHECKPOINT SCRIPT REMOVED AS VERIFIER)».
- Завышение: статус `proved` при нулевом контроле, специфичном
  именно для этого утверждения, и при удалённом общем скрипте.
- Исправление одной фразой: «Проектное доказательство при явных
  гипотезах, без контрольного вычисления, специфичного для этого
  утверждения.»

### 6. Наличие ссылки на Lean выдаётся за полное доказательство теоремы в Lean

- Источник: `bgs-analysis/gap_summary_20261029.md`:
  > «наличие ссылки ≠ полное доказательство теоремы в Lean»;
  `formalization/README.md`, таблица «Active modules» — почти каждая
  строка содержит ограничение вида «only», «finite», «no … formalized».
- Завышение: фраза «формализовано в Lean» без указания, что именно
  формализовано: ядро, фрагмент, конечный случай или только
  формулировка.
- Исправление одной фразой: «В Lean формализован только названный
  фрагмент/ядро; полная теорема в Lean не доказана.»

### 7. Statement-only модули выдаются за формализацию утверждения

- Источник: `formalization/Bgs/TraceStatement.lean`, шапка:
  > «It contains definitions and `Prop`s only. Nothing here is a theorem about the family, and no proof of the criterion is given or claimed: the claim is OPEN»;
  то же устройство у `Fm001Statement.lean` и `Fm021Statement.lean`
  (README: «statement formalization only … no theorems and no proofs»).
- Завышение: в реестре у открытого BGS-TRACE-005 стоит непустое
  `formalization: ['formalization/Bgs/TraceStatement.lean']` — при
  беглом чтении это выглядит как «есть Lean-доказательство
  открытого утверждения».
- Исправление одной фразой: «В Lean записана только формулировка
  открытого утверждения; теорем и доказательств в модуле нет.»

### 8. Конечный случай выдаётся за общий результат

- Источник: `claims.json`, BGS-CAYLEY-002, `boundary`:
  > «formalization/Bgs/CayleyEnergy.lean proves the collision energies at the five explicit designs (199,11,139), (67,11,64), (521,13,101), (53,13,10) and (461,23,23) by native_decide; it states no general (for all K) reduction of the mixed layer to additive energy and no uniform cutoff theorem in K»;
  аналогично BGS-FM-037 — «Fixed finite design certificate at p=199 only …
  Not a general scale or level-set theorem».
- Завышение: заголовок «Cayley additive-energy reduction» без слова
  «пять явных дизайнов» читается как редукция вообще.
- Исправление одной фразой: «Доказано только для пяти явно
  перечисленных дизайнов; общей редукции для всех K нет.»

### 9. Частичный сертификат выдаётся за полный

- Источник: `claims.json`, BGS-CAYLEY-001, `boundary`:
  > «at (461,23) original_pair_vs_explicit_key, direct_vs_fast_distribution and twist_collapse are NOT_RUN_AT_THIS_SIZE (q_values_checked [1] only) … its corpus check verifies file presence and JSON parsing only».
- Завышение: вердикт «PASS» в квитанции — корпусного уровня, а
  отдельные проверки на крупнейших размерах не запускались вовсе.
- Исправление одной фразой: «Сертификат частичен: на крупнейших
  размерах часть проверок не запускалась.»

### 10. `native_decide` выдаётся за обычное доказательство

- Источник: `formalization/README.md`, раздел «Trust boundary»:
  > «Large finite propositions in several modules use `native_decide`. Their acceptance includes trust in native compilation/evaluation … They are not independent small-kernel recomputations of the finite search»;
  в срезе 29 октября слово `native_decide` встречается в 16 файлах,
  но в трёх это только комментарий (в том числе AnalyticOrbitKernels
  прямо пишет, что native_decide НЕ используется); тактика
  `by native_decide` в коде — в 12 файлах (CayleyEnergy,
  CayleyCurveEnergy, FourCutKernel, MagneticTraceSmall,
  PairKeyFourthMoment, PairKeySecondMoment, PellCoboundary,
  PellCohomology, SevenPrimary, TorusLevelSets и др.),
  а `seven_primary_certificate.md` прямо говорит то же про
  SevenPrimary.
- Завышение: «доказано в Lean» без упоминания, что часть теорем
  держится на доверии к нативной компиляции и вычислению, а не
  на проверке малым ядром.
- Исправление одной фразой: «Доказательство использует native_decide
  и потому включает доверие к нативной компиляции и вычислению.»

### 11. Достаточность выдаётся за саму оценку

- Источник: `claims.json`, BGS-TRACE-003, `boundary`:
  > «Triangle-inequality sufficiency only; averaging is before modulus. … The exact signed bridge is viable but its actual-map estimate is open»;
  BGS-TRACE-004, `boundary`:
  > «Requires positive normalized spectral averages and a reference Schwartz limit; a single fixed bandwidth is insufficient».
- Завышение: заголовок TRACE-003 — «Weighted Heisenberg-scale
  joint-trace comparison is sufficient for band-limited microscopic
  RMT correlations» — при цитировании без слова «sufficient»
  превращается в утверждение о самой микроскопической статистике.
- Исправление одной фразой: «Доказана только достаточность
  сравнения; сама оценка для отображения открыта.»

### 12. Условное утверждение цитируется без условия

- Источник: `claims.json`, BGS-FM-004 (`conditional`), `boundary`:
  > «Normalized mixed-residual decay hypotheses remain unproved for the frozen propagator»;
  BGS-TRACE-060 (`conditional`):
  > «CONDITIONAL ON ALL-TIME FLATNESS»;
  BGS-RES-014 (`conditional`):
  > «PROJECT PROOF; CONDITIONAL ON THE FOUR-ATOM GAP SEPARATION LEMMA»;
  BGS-LOOP-001 (`conditional`), `boundary`:
  > «Actual anchors, long-long signed residual and full hierarchy remain open. Formalization coverage is integer kernels only».
- Завышение: импликация «если гипотеза, то следствие» цитируется
  как следствие; у LOOP-001 к тому же Lean покрывает только
  целочисленные ядра.
- Исправление одной фразой: «Следствие доказано только при
  недоказанной гипотезе, названной в boundary.»

### 13. Гипотеза спрятана в имени леммы / названии результата

- Источник: `claims.json`, BGS-TRACE-142 (`verification-pending`),
  `boundary`:
  > «the non-injective remainder is not bounded, so the limit m(1+e^{-vm}) is verification-pending»;
  при этом заголовок — «Gaussian momentum-phase crossover from 2m to m»,
  а `ledger_status` — «ANALYTIC MAIN TERMS + MONTE CARLO SANITY CHECK + AUTHOR SELF-REVIEW».
- Завышение: «главный член + Монте-Карло» подаётся как предел;
  неограниченный остаток — это ровно то, что отделяет главный
  член от предела.
- Исправление одной фразой: «Вычислен только гауссов главный член;
  предел не доказан, так как остаток не ограничен.»

### 14. Неинформативная оценка выдаётся за содержательную

- Источник: `claims.json`, BGS-TRACE-134, `ledger_status`:
  > «EXPLICIT BOUND NON-INFORMATIVE AT COMPUTABLE N (LIMIT THEOREM)»;
  `key_files/README.md`:
  > «at λ=1/4 it first drops below 1 near N≈10^{191}, so only the limit is proved»;
  аналогично BGS-FM-011, `boundary`:
  > «Explicit enormous N-dependent lower gap … vastly below 1/N, giving no local occupation, Abel, or CUE estimate».
- Завышение: «эффективная оценка» без чисел звучит как
  применимая оценка; на деле первая — пуста при любом
  вычислимом N, вторая — на порядки ниже микроскопического
  масштаба 1/N.
- Исправление одной фразой: «Доказан только предел; явная оценка
  при вычислимых N неинформативна.»

### 15. Внешняя теорема выдаётся за результат проекта

- Источник: `claims.json`, 46 записей `proved` с непустым
  `external_dependencies`, например BGS-FM-011 (EXT-ROY-2016),
  BGS-TRACE-007 (EXT-CK-2006), BGS-CUE-001 (EXT-BAB-2013).
- Завышение: «доказано в проекте» без называния внешнего входа
  приписывает проекту чужую теорему и скрывает зависимость
  от её условий.
- Исправление одной фразой: «Результат проекта при использовании
  внешней теоремы, названной в external_dependencies.»

### 16. Сборка Lean выдаётся за текущую, хотя пост-мердж сборка не заявлена

- Источник: `formalization/README.md`:
  > «its raw execution logs were not recoverable after the environment change»;
  > «Hosted CI did not independently validate the merged source because the repository owner reported exhausted GitHub Actions minutes. No post-merge Lean build is claimed»;
  `bgs-analysis/build_attempts.md`: локальный `lake build Bgs`
  29–30 октября завершился EXIT:1 — модуль `Bgs.LineCEncounter`
  убит по OOM (код 137), агрегатор `Bgs.olean` не собран.
- Завышение: запись BGS-FORMAL-001 с `ledger_status`
  «CURRENT PINNED BUILD VERIFIED» при цитировании без даты
  и коммита звучит как «весь граф Lean проверен сейчас»,
  хотя для слитого состояния это не заявлено, а локальная
  попытка на этой ВМ упала по памяти.
- Исправление одной фразой: «Сборка проверена для закреплённого
  состояния на указанную дату; пост-мердж сборка не заявлена.»

## Что как доказанное цитировать нельзя — по реестру 2026-10-29

### Категория A. Нельзя вообще: это не proved

31 запись. Цитирование любой из них со словом «доказано»
— ошибка независимо от контекста.

- Open (8): BGS-BGS-001, BGS-CAYLEY-005, BGS-INFO-001, BGS-RES-003,
  BGS-TRACE-005, BGS-TRACE-136, BGS-TRACE-137, BGS-TRACE-148.
  Центральная микроскопическая BGS — это BGS-BGS-001, а её
  ключевая оценка — BGS-TRACE-005.
- Verification-pending (14): BGS-CAYLEY-003, BGS-TRACE-055,
  BGS-TRACE-096, BGS-TRACE-098, BGS-TRACE-099, BGS-TRACE-100,
  BGS-TRACE-101, BGS-TRACE-102, BGS-TRACE-103, BGS-TRACE-104,
  BGS-TRACE-105, BGS-RES-022, BGS-TRACE-142, BGS-TRACE-147.
  Отдельно: TRACE-147 имеет сильный компьютерный корпус
  (независимый replay, m ≤ 12), но статус — именно pending,
  и «promotion is a separate status decision».
- Conditional (9): BGS-FM-004, BGS-LOOP-001, BGS-TRACE-060,
  BGS-TRACE-073, BGS-FM-033, BGS-TRACE-095, BGS-TRACE-097,
  BGS-RES-014, BGS-RET-003.
  Их можно цитировать только в форме «если …, то …» с явным
  условием из `boundary`/`closure_condition`.

### Категория B. Можно только с квалификатором «по внутреннему реестру проекта»

Все 201 `proved`, если не выполнено ни одно из условий ниже.
Внутри категории особо слабы (нет ни верификатора, ни внешнего
рецензента — цитировать их как «проверенные» нельзя даже
с оговоркой про проект, нужна оговорка про отсутствие проверки):

- Proved без верификаторов (34): BGS-FM-001, BGS-FM-002, BGS-FM-003,
  BGS-FM-011, BGS-FORMAL-001, BGS-RES-001, BGS-RES-002, BGS-RES-007,
  BGS-TRACE-001, BGS-TRACE-002, BGS-TRACE-003, BGS-TRACE-004,
  BGS-TRACE-006, BGS-TRACE-007, BGS-TRACE-057, BGS-TRACE-058,
  BGS-TRACE-059, BGS-TRACE-061, BGS-TRACE-062, BGS-TRACE-063,
  BGS-TRACE-064, BGS-TRACE-065, BGS-TRACE-066, BGS-TRACE-067,
  BGS-TRACE-068, BGS-TRACE-083, BGS-CAYLEY-010, BGS-RES-015,
  BGS-RES-018, BGS-RES-021, BGS-TRACE-108, BGS-FM-037,
  BGS-TRACE-115, BGS-TRACE-116.
- Proved без свидетельств (12): BGS-RES-006, BGS-TRACE-008,
  BGS-CUE-001, BGS-FLOW-001, BGS-FLOW-002, BGS-CAYLEY-007,
  BGS-CAYLEY-010, BGS-RES-008, BGS-RES-017, BGS-RES-020,
  BGS-CAYLEY-011, BGS-FM-037.
- Proved без ссылки на Lean (139) — полный список в
  `bgs-analysis/gap_proved_no_formalization.csv`; цитировать их
  как «формализованные» нельзя, только как «проектные
  доказательства без Lean-ссылки».

### Категория C. Можно только в узком объёме, названном в boundary

Даже если запись `proved`, её объём — ровно то, что написано
в `boundary`, а не заголовок:

- BGS-CAYLEY-002 — только пять дизайнов, без общей редукции.
- BGS-CAYLEY-001 — частичный сертификат, часть проверок
  на крупнейших размерах не запускалась.
- BGS-FM-037, BGS-TRACE-117 (только n ≤ 201 для кика; предел
  при N → ∞ не доказан), BGS-TRACE-127 (времена 1–3, а не
  все времена), BGS-TRACE-134 (только предел, оценка
  неинформативна при вычислимых N), BGS-FM-011 (зазор много
  ниже 1/N, без локальных следствий).
- Все модули из таблицы README с пометами «only», «finite»,
  «no … formalized», а также SevenPrimary и FourCutKernel
  (только конечные предикаты/счёты, с доверием к native
  вычислению; общей теоремы о коммутанте в Lean нет).
- BGS-FORMAL-001 — только для закреплённого состояния
  на указанную дату; пост-мердж сборка не заявлена (пункт 16).

## Что в проекте уже честно — и ломать это не надо

- `formalization/README.md`: раздел «Trust boundary», таблица
  модулей с ограничениями, фраза «No active module proves the
  general analytic limits, eigenvector-overlap estimate or BGS».
- `key_files/STATUS.md`: «"Proved" reports the project registry
  at its stated scope, not external refereeing».
- `key_files/README.md`: после почти каждого блока — «BGS-TRACE-005
  and BGS-BGS-001 remain open».
- Поля `boundary` и `closure_condition` в самом `claims.json` —
  именно они спасают реестр от того, чтобы стать списком
  завышений. Проблема не в их отсутствии, а в том, что их
  отбрасывают при цитировании.

## Правило цитирования, предлагаемое проекту

Одно предложение-шаблон для любой ссылки на реестр:

> «По внутреннему реестру проекта BGS (обновлён 2026-10-29,
> запись <ID>, состояние <state>, см. её boundary) …»

— и дальше только то, что действительно написано в `boundary`,
с сохранением слов «finite», «only», «conditional», «partial»,
«project proof», «author check», «native_decide» там, где они
стоят в источнике. Если предложение нельзя произнести в этой
форме без потери смысла — значит, цитата завышена.
