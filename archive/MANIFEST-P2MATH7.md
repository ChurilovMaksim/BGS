# MANIFEST-P2MATH7 — волна 7 P2-MATH: тематический дом `mathematics/resonance-cohomology/`

Волна 7 пакета P2-MATH (фаза 2 реструктуризации BGS). По канонической карте тем
`record/mathematics_topics.json` тема `resonance-cohomology` (ровно 21 заметка, членство
однозначно — каждая из 21 встречается только в этой теме карты, проверено поиском стемов
по всем темам; датированных имён в теме нет) переезжает в новый дом
`mathematics/resonance-cohomology/`. Тем же коммитом мигрируют все живые потребители
(карта тем, вид темы, запечатанные и follow-on значения `claims.json`, строки эпох,
вид papers, errata, рукописные ссылки, прозовые/ссылочные упоминания, перегенерированные
навигационные виды, STATUS/ERRATA). Эпохальная часть: 2 новые запечатанные поправки
(BGS-RES-001/002, `fields={source}`), 2 расширенные запечатанные поправки
(BGS-RES-004/005, к существующим полям `evidence` добавлен `source`) и 7 follow-on
`source` (BGS-RES-014/015/018/019/020/022/023); множество `approved` 67 → 69;
`wave2_integration_audit.run()` отличается от базы ровно поправками
(`unchanged_prior_claims` 29 → 27, `explicitly_amended_prior_claims` 67 → 69).

База: живой main после закрытия волны 3 (`5b884c8`); локально
`p2_math7_work/base_tree` (байт-копия `p2_math3_work/post_tree`). Пост
`p2_math7_work/post_tree` — целевое состояние: 21 оригинал удалён локально.
Волна 4 НЕ приземлялась, и её post_tree сознательно не использован как база.

## 1. Карта переезда (старый → новый путь; SHA-256 новых файлов)

| Старый путь | Новый путь | SHA-256 нового файла |
|---|---|---|
| `mathematics/analytic_coboundary_regularization.md` | `mathematics/resonance-cohomology/analytic_coboundary_regularization.md` | `da9a76401fc0af5ae6c86b195b853bee55518f4041dab614451c54cff693783a` |
| `mathematics/analytic_poisson_flatness_rigidity.md` | `mathematics/resonance-cohomology/analytic_poisson_flatness_rigidity.md` | `fb1c366ce728c597ac90283b248a29a797d5e265e73515b0f9794b70c611f018` |
| `mathematics/analytic_poisson_rigidity.md` | `mathematics/resonance-cohomology/analytic_poisson_rigidity.md` | `e34c94394d7d595e802b9c74bc524a7b7356ac823e592a862ed9ed16b8bcd480` |
| `mathematics/entire_temporal_gauge.md` | `mathematics/resonance-cohomology/entire_temporal_gauge.md` | `412a281ff05f84db7a29d164d4c4527c6829f55b218b24edc06719049d7a8b5e` |
| `mathematics/even_period_spin_resonance.md` | `mathematics/resonance-cohomology/even_period_spin_resonance.md` | `ba75e3bca2143b8f31beed259c394bc5c39369618e08a76db4598be7bf5e3f14` |
| `mathematics/extremal_resonance_nondegeneracy.md` | `mathematics/resonance-cohomology/extremal_resonance_nondegeneracy.md` | `fd65a519eacacc99ce2498ee1df0a4135f52b43f8f1f5d26e7919ec35d0df1e8` |
| `mathematics/finite_orbit_resonance_rigidity.md` | `mathematics/resonance-cohomology/finite_orbit_resonance_rigidity.md` | `85fa6da53381f8facdd496f999207db1c77710d8f7e4a51ee3b5b974473de7c5` |
| `mathematics/fourier_line_resonance_coercivity.md` | `mathematics/resonance-cohomology/fourier_line_resonance_coercivity.md` | `a62c91ec7cd945162406ef4f7f306cd9167e59f8722042934c75536ddbf37d0b` |
| `mathematics/frozen_full_lag_resonance.md` | `mathematics/resonance-cohomology/frozen_full_lag_resonance.md` | `80d416507287d1acf826b1b6f8fe4199635f67842352e22be3ed75f9a6cb592f` |
| `mathematics/generic_wiener_resonance.md` | `mathematics/resonance-cohomology/generic_wiener_resonance.md` | `7fdf789d5a5e7864fa541b4d2960964c3d209f99b7afa9dbb5ed0d40a73ddd6d` |
| `mathematics/infinite_orbit_resonance.md` | `mathematics/resonance-cohomology/infinite_orbit_resonance.md` | `e2257a4d123618519e0e6c7f2166eefaebb3710114fca20b6749a67e1fd809f5` |
| `mathematics/local_jet_resonance_obstruction.md` | `mathematics/resonance-cohomology/local_jet_resonance_obstruction.md` | `7180747e992253bff51a1f98d2790b0987cb874c3d4b789ead83d660773b5f8b` |
| `mathematics/phase_regularized_resonance.md` | `mathematics/resonance-cohomology/phase_regularized_resonance.md` | `a3ff184e6bdd0e8b7f033ca7d1f41d2c1b36b49f2f45f84dc6de9d56a842cd80` |
| `mathematics/quantitative_resonance_transversality.md` | `mathematics/resonance-cohomology/quantitative_resonance_transversality.md` | `8b62001b9b99f0da93a28435b65699ba62b71ce77daa2c9ab5f6857f17068d3e` |
| `mathematics/resonance_microscopic_obstruction.md` | `mathematics/resonance-cohomology/resonance_microscopic_obstruction.md` | `d739775b6d5d2be632894c25d78aead4ffe6aefc5a3b15b673429492d0d62602` |
| `mathematics/resonance_nondegeneracy_and_hessian.md` | `mathematics/resonance-cohomology/resonance_nondegeneracy_and_hessian.md` | `7f0d0423621139e20c042a0ebfd048d0989891e17c32abd5d32b8ac379347846` |
| `mathematics/resonance_riesz_regularization.md` | `mathematics/resonance-cohomology/resonance_riesz_regularization.md` | `262d92c15a5aa1d555186ab4ee7d6afdc49b99cb044107488551b9e98a47a989` |
| `mathematics/resonance_wiener_stability.md` | `mathematics/resonance-cohomology/resonance_wiener_stability.md` | `0c8a7075782604179adbf1c9ffd888ee0c4bb1580e3ffa46e59dcdd2926bae33` |
| `mathematics/temporal_resonance_hierarchy.md` | `mathematics/resonance-cohomology/temporal_resonance_hierarchy.md` | `a2cf32ac4939cdc427420b5fe9d1d183ff71eca0017231e9ebbd95f3c22dc396` |
| `mathematics/two_window_resonance_crossover.md` | `mathematics/resonance-cohomology/two_window_resonance_crossover.md` | `ce2ef7d7b0af9a4312db32aa2e0b6764f391d7388442d67a4a8ee546a0b41de0` |
| `mathematics/weighted_wiener_resonance.md` | `mathematics/resonance-cohomology/weighted_wiener_resonance.md` | `0014586f8b17cf7daffae6d8a433b2080c1ac5aa9832667f66b23711fa164886` |

18 из 21 — байт-копии (хэши совпадают с оригиналами базы). Хэш
`d739775b…` (resonance_microscopic_obstruction) совпадает с пином в
`supplement/fixed_map/algebraic-return/checkpoint.json` — независимое подтверждение
байт-копии. Переименование датированных имён не потребовалось (их нет в теме).

## 2. Перевод ссылок внутри переезжающих заметок (математическое содержимое не менялось)

- `analytic_poisson_rigidity.md`: `(general_hyperbolic_prime_spectra.md)` →
  `(../general_hyperbolic_prime_spectra.md)` (цель остаётся в корне).
- `even_period_spin_resonance.md`: `(hyperbolic_return_pressure.md)` →
  `(../hyperbolic_return_pressure.md)`; `(../computations/verification/even_period_spin_resonance.py)` →
  `(../../computations/verification/even_period_spin_resonance.py)`.
- `finite_orbit_resonance_rigidity.md`: 3 код-спана `mathematics/<stem>.md` →
  `mathematics/resonance-cohomology/<stem>.md` (extremal_resonance_nondegeneracy,
  entire_temporal_gauge, phase_regularized_resonance — сиблинги волны).
- Остальные 18 заметок ссылок `](…)` не содержат; сиблинговые прозовые упоминания
  голыми именами валидны в общем доме и не правятся (прецедент волн 2–3).
  Упоминание `mathematics/fixed_model_symmetry_theorem.md` во
  `frozen_full_lag_resonance.md:7` не тронуто: цель остаётся в корне.

## 3. Эпохальная часть

### 3.1. Запечатанные поправки: 2 новые + 2 расширенные (не 4 новые)

Измерение против запечатанного снимка wave2 (96 строк,
`evidence/wave2_checked_20261007/raw/provenance/base_navigation/record/claims.json`,
каноническая SHA: `sort_keys=True`, `separators=(',',':')`, `ensure_ascii=False`):

- BGS-RES-001 (`proved`): текущая строка == запечатанной, SHA
  `cfb98698942a7fb3e60d595778c646d292fde6a35de2427c32eb56b0009c8ac8`.
  Новая строка amendments (в хвост списка): `fields={source:
  mathematics/resonance-cohomology/fourier_line_resonance_coercivity.md}`,
  disposition в стиле волны 4, `review: archive/MANIFEST-P2MATH7.md`.
- BGS-RES-002 (`proved`): текущая строка == запечатанной, SHA
  `61fa140d852598eec623d75010c7539ef3feb611d607a82d930a64aa3408ea7d`.
  Новая строка amendments: `fields={source:
  mathematics/resonance-cohomology/local_jet_resonance_obstruction.md}`.
- BGS-RES-004 (`proved`): уже поправлен в фазе 1 (пакет A-plain): текущая строка
  отличается от запечатанной ТОЛЬКО полем `evidence` (SHA запечатанной строки
  `e594bd61b82d8daff7c934fb0cffd3e1ae9e3ba72e28b765964b42b36f807392`),
  и строка amendments уже существует. Вторая строка на тот же id невозможна
  механически: `check_prior_claims` строит `amendments={row['id']:row}` и требует
  `len(amendments)==len(rows)` и `set(amendments)==approved`. Поэтому существующая
  строка РАСШИРЕНА: `fields` стало `{evidence: [...], source:
  mathematics/resonance-cohomology/finite_orbit_resonance_rigidity.md}`;
  `historical_row_sha256` не менялся; disposition дополнен предложением о переезде
  фазы 2 со ссылкой на этот манифест; `review` переставлен на
  `archive/MANIFEST-P2MATH7.md` (этот манифест документирует и унаследованную
  evidence-часть, и новое поле source).
- BGS-RES-005 (`proved`): аналогично, фаза-1 evidence-поправка (SHA запечатанной
  строки `b6991b4cb86f8de92efc9ed15549d52284c5317ae4f3d1579622d5ba7ea267f8`);
  `fields` расширено до `{evidence: [...], source:
  mathematics/resonance-cohomology/frozen_full_lag_resonance.md}`; disposition и
  review — как у RES-004.
- Итог: строк amendments 67 → 69, множество `approved` в
  `computations/verification/wave2_integration_audit.py` 67 → 69
  (`BGS-RES-001`, `BGS-RES-002` добавлены в хвост литерала). Статусных изменений
  нет нигде. Негативные контроли пройдены: аудит без RES-001 (и отдельно без
  RES-002) в `approved` отвергает пост-данные (`explicit epoch review`); подмена
  `source` в строке RES-001 отвергается (`outside reviewed amendment`).

### 3.2. Follow-on source ×7 (claims.json + строки after_wave3 тем же коммитом)

- BGS-RES-014 (`conditional`): `source` → новый дом; `proof_dependencies` ×2 →
  новые дома; проза `boundary` (phase_regularized_resonance) → новый путь;
  строка after_wave3: `source` → новый дом, проза `disposition`
  (phase_regularized_resonance) → новый путь.
- BGS-RES-015 (`proved`): `source` → новый дом; проза `dependency_scope`
  (two_window_resonance_crossover) → новый путь; строка after_wave3: `source`.
- BGS-RES-018 (`proved`): `source` → новый дом; `proof_dependencies[0]`
  (infinite_orbit_resonance) → новый дом; строка after_wave3: `source`.
- BGS-RES-019 (`proved`): `source` → новый дом; строка after_wave3: `source`.
  Путь лога evidence и модуль верификатора — кодовые имена, не тронуты.
- BGS-RES-020 (`proved`): `source` → новый дом; строка after_wave3: `source`.
  Путь `.tex` в `manuscript[]` не тронут (секция не переезжает).
- BGS-RES-022 (`verification-pending`) и BGS-RES-023 (`proved`): `source` →
  новый дом; строки after_wave3: `source`. Обе не входят в запечатанный снимок
  wave2 — это follow-on, а не поправки.
- Всего в claims.json изменено 16 значений (4 запечатанных source + 12 follow-on
  значений); остальные поля claims не тронуты. `formalization[]` путей
  mathematics/ не содержит.

### 3.3. Проверка блокера: 0 хитов (урок волны 4)

- `literature/external_dependencies.json`: полный скан всех 21 стемов по текущим
  57 строкам и по запечатанным 39 строкам снимка
  (`archive/evidence/executions/20261011/chat-research/baselines/external_dependencies_20261007.json`) —
  0 хитов, в т.ч. по `project_sources`. Запечатанный контракт внешней эпохи не
  затронут; файл в пакет не входит.
- Errata — не блокер, а живые указатели: ERR-048 `authority` →
  новый дом; ERR-051 `authority` → новый дом и проза `downstream`
  (resonance_nondegeneracy_and_hessian) → новый путь. На строках errata
  эпохальных пинов нет; аудит errata требует разрешения `authority` —
  миграция обязательна.

## 4. Миграции живых потребителей (тем же коммитом)

- `record/mathematics_topics.json` — 21 путь темы; `updated` уже `2026-10-24`,
  не менялся.
- `mathematics/topics/resonance-cohomology/README.md` — 28 вхождений ссылок
  `](../../<stem>.md)` → `](../../resonance-cohomology/<stem>.md)` (21 членство +
  3 featured + 4 reading-sequence); ссылка `](../../../archive/record/corpus_revision_20261006.md)`
  не тронута (урок волны 3).
- `papers/resonance-cohomology/README.md` — 4 ссылки → новые дома;
  `papers/resonance-cohomology/paper.json` — 5 `authoritative_sources` → новые
  дома (запись foundations не тронута).
- `computations/verification/repository_audit.py` — ACTIVE-пути ×2
  (fourier_line_resonance_coercivity, local_jet_resonance_obstruction) → новые дома.
- `computations/maintenance/sync_finite_orbit_section.py` — SOURCE →
  `mathematics/resonance-cohomology/finite_orbit_resonance_rigidity.md`.
  Депонированная глава `manuscript/unified_sections/finite_orbit_resonance.tex`
  намеренно НЕ правлена вручную: она уже stale на базе (pandoc-дрейф), а её
  `% Source SHA256` не меняется (заметка — байт-копия); `\path`-упоминания
  обновятся при следующей sync-регенерации (практика волн 1–4).
- `record/generated_sources.json` — `authoritative_sources` sync-правила →
  новый дом (аудит требует разрешения этих путей).
- `manuscript/unified_sections/fixed_map_frontier.tex` — 1 `\href` GitHub-blob
  (frozen_full_lag_resonance) → новый дом;
  `manuscript/unified_sections/return_gas.tex` — 1 `\href`
  (even_period_spin_resonance) → новый дом;
  `manuscript/unified_sections/return_periodic.tex` — 1 `\href`
  (weighted_wiener_resonance) → новый дом.
- `mathematics/fixed_harmonic_return_gas.md` — 1 ссылка →
  `resonance-cohomology/even_period_spin_resonance.md`;
  `mathematics/fixed_map_resolvent_frontier.md` — 1 ссылка →
  `resonance-cohomology/frozen_full_lag_resonance.md`;
  `mathematics/nonlinear_bracket_pressure.md` — 1 ссылка →
  `resonance-cohomology/frozen_full_lag_resonance.md`;
  `mathematics/periodic_point_trace_comparison.md` — 1 ссылка →
  `resonance-cohomology/weighted_wiener_resonance.md`.
- `mathematics/open_questions.md` — 4 код-спана → путевая форма
  `resonance-cohomology/<stem>.md` (форма волны 4: generic_wiener_resonance,
  resonance_wiener_stability, analytic_coboundary_regularization,
  finite_orbit_resonance_rigidity).
- `mathematics/balanced_phase_controllability.md` — прозовое упоминание →
  `resonance-cohomology/resonance_riesz_regularization.md`;
  `mathematics/exact_homoclinic_potential.md` — прозовое упоминание →
  `resonance-cohomology/extremal_resonance_nondegeneracy.md`;
  `mathematics/information-theory/quadratic_response_limits.md` — прозовое
  упоминание → `resonance-cohomology/phase_regularized_resonance.md`
  (форма волны 3: дом-относительная путевая форма).
- `literature/finite_orbit_20260922.md` — 4 код-спана путей → новые дома.
  Суждение сборки (зафиксировано явно): файл датирован, но это живая
  литературная заметка с путевыми указателями, а не архивный снимок и не
  ACTIVE-список; оставлять 4 протухших пути хуже, чем обновить их. Если
  родитель предпочитает замороженную трактовку — откатить только этот файл.
- `computations/cpp/resonance_complex_replay.cpp` — комментарий с путём →
  новый дом; `computations/verification/nonlinear_pressure_variance.py` —
  докстринг с путём (frozen_full_lag_resonance) → новый дом;
  `computations/verification/resonance_nondegeneracy_margin.py` — докстринг
  с путём (resonance_nondegeneracy_and_hessian) → новый дом (прецедент волны 4:
  докстринг с путём мигрирует; голые имена файлов в докстрингах и импорты
  модулей верификаторов — кодовые имена, не тронуты).
- `supplement/fixed_map/continuation-20260921/README.md` — 2 ссылки →
  новые дома.
- `docs/corpus_atlas.md`, `record/claim_registry.md`,
  `record/scientific_dependency_graph.md` — перегенерированы (диффы — ровно
  21 строка атласа / 11 строк реестра / 11 строк графа: только пути; счётчики
  334/197 неизменны). `record/scientific_dependencies.json` перегенерирован
  байт-идентично — в пакет не входит. `mathematics/results.md` и
  `literature/references.bib` перегенерированы байт-идентично — в пакет не входят.
- `STATUS.md` — перегенерирован (ровно 1 строка: 67 → 69 historical amendments).
  `ERRATA.md` — перегенерирована (ровно 1 строка: проза downstream ERR-051).

## 5. Остаточный скан (пост): живых указателей на старые пути — только классы ниже

Полный поиск 21 стема и старых корневых путей по пост-дереву (103 носителя):
- **Живые, с новыми путями (ожидаемо):** всё из §3–§4.
- **Живые, корректны как есть:** сиблинговые прозовые упоминания голыми именами
  внутри переехавших заметок; голые имена файлов в докстрингах верификаторов,
  импорты модулей, имена кодовых файлов, комментарий Lean
  (`formalization/Bgs/AnalyticOrbitKernels.lean` — голое имя, не путь);
  `\input` `.tex`-секции; пути `.tex`-секций в `claim_ledger.md`
  (нет стемов волны); голое имя в `record/final_research_handoff_20260921.md`
  (список имён файлов, не пути — имена не менялись); пины
  `record/publication_review_20260912.md` (имя модуля верификатора + хэш,
  не путь заметки); `--only`-имена в `REPRODUCE_unified.md`;
  `return_checks`-имена в `computations/maintenance/verify_workspace.py`.
- **Намеренно оставленные старые пути (3 файла, каждый классифицирован):**
  - `manuscript/unified_sections/finite_orbit_resonance.tex` — 3 `\path`
    (extremal_resonance_nondegeneracy, entire_temporal_gauge,
    phase_regularized_resonance): sync-выход, stale на базе; обновится при
    следующей sync-регенерации (см. §4).
  - `record/claim_integration_epochs.json` — 4 старых пути: это намеренные
    исторические цитаты в disposition поправок RES-001/002/004/005
    («from mathematics/<stem>.md to …»); новых путей в файле 16.
  - `supplement/fixed_map/algebraic-return/checkpoint.json` — 1 ключ-путь
    (resonance_microscopic_obstruction) с хэш-пином `d739775b…`: запись
    о проверенных байтах, потребителей у файла нет; хэш по-прежнему совпадает
    с байтами переехавшего файла (§1).
- **Замороженные носители (не правятся; разрешаются этим манифестом):**
  `archive/**`, `evidence/**` (включая `evidence/certificates/` и
  `evidence/fixed_map_publication/` — датированные снимки с именами модулей
  и хэшами `.tex`, не путями заметок), `record/audits/**`,
  запечатанные входы `evidence/wave2_checked_20261007/raw/**`,
  `evidence/research_checkpoint_20261007/raw/**`.
- **Записи с датой/пинами (не правятся):** `mathematics/results_20260907_addendum.md`
  (голые имена файлов, не пути); `record/claim_ledger.md` (нарратив, стемов
  волны нет).
- Проверено отдельно: ни одного старого корневого пути
  `mathematics/<stem>.md` вне перечисленных классов — 0; ни одного
  неразрешённого пути в claims.json (259 путей) — 0.
