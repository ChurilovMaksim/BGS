# MANIFEST-P2MATH1 — фаза 2, пакет P2-MATH, волна 1 (foundations): `mathematics/*.md` → `mathematics/foundations/`

**Источник:** живой main после пакета P2-H (коммит `58b65d7` + браузерные удаления оригиналов P2-H); сборка — на пост-дереве P2-H (`p2_h_work/post_tree`). `record/claims.json` базы: git blob `6caca2fef44fc046225ae66a025c55e6183aebca` — сверен с живым main коннектором при сборке. Корень `mathematics/` базы сверен с живым main коннектором полностью: 340/340 записей, имена, типы и blob SHA совпадают (призраков в mathematics/ нет).
**Состав волны: 3 заметки, 1 новый тематический дом** — `mathematics/foundations/`. Тема и членство — строго по канонической карте `record/mathematics_topics.json` (тема `foundations`, ровно 3 пути). Порядок волн — по возрастанию связности (дизайн §7): foundations — единственная тема с нулевой реестровой связностью (ни одного упоминания ни в одном поле ни одного из 197 claims), без датированных имён и без членства в других темах.

## Переезжающие файлы

| Старый путь | Новый путь | SHA-256 содержимого | Байты |
|---|---|---|---|
| `mathematics/analytic_bracket_rigidity.md` | `mathematics/foundations/analytic_bracket_rigidity.md` | `dec5568e52b7da364c3c03fa4b686625a9264d8f7b330f2bd3307b15ce01ee1a` | 4445 |
| `mathematics/earlier_foundations.md` | `mathematics/foundations/earlier_foundations.md` | `f7b487b9a611f1b394d629f66b3974981636edb23acbad9f3cb6aeae60c41a8d` | 3259 |
| `mathematics/hyperbolic_signed_trace_extension.md` | `mathematics/foundations/hyperbolic_signed_trace_extension.md` | исходный: `b4ece3651da5127ecefdecdadb1bfe746342fa4a11c1d4ee6007559d8bb5da0c` (4931 Б); целевой: `b9c2d064b5b9e49ab6be8170dade4c5bd6cb32a70a17da8cb756c441de001a55` | 4934 |

Две заметки — байт-копии. `hyperbolic_signed_trace_extension.md` отредактирована ровно в одной строке (строка 4): её единственная исходящая ссылка на остающуюся в корне заметку `general_hyperbolic_prime_spectra.md` (тема spectral-obstructions, волна 8) переведена через границу волны: `](general_hyperbolic_prime_spectra.md)` → `](../general_hyperbolic_prime_spectra.md)`. Других относительных ссылок и путевых упоминаний в трёх заметках нет (полный скан при сборке).

## Эпохальная часть волны: ОТСУТСТВУЕТ (измерено, не предположено)

- `record/claims.json` волной не тронут: три заметки не упоминаются ни в одном поле (`source`, `proof_dependencies`, `evidence`, `verifiers`, `formalization`, `manuscript`, прочие) ни одного из 197 claims — полный скан JSON при сборке.
- Разбиение по классам эпохи для волны: запечатанные (96 строк wave2) — 0; follow-on `after_wave3` (94) — 0; дельта wave2 (5) — 0; wave3 (2) — 0. Поправок `historical_claim_amendments` не требуется; множество `approved` в `wave2_integration_audit.py` не расширяется; `record/claim_integration_epochs.json` не тронут.
- Контроль: выход `wave2_integration_audit.run()` на посте байт-идентичен базе (SHA-256 JSON `c020cba99ffd034358edffe49b377f59fe391ec6d8993251e161e566c320d5bb`; 96 исторических / 29 unchanged / 67 amended).

## Отредактированные тем же коммитом файлы (миграция потребителей)

- `record/mathematics_topics.json` — 3 пути темы `foundations` переведены на новый дом; поле `policy` переформулировано под целевую раскладку фазы 2 (канонический путь каждой заметки записан в карте; членство навигационно и может цитировать заметку в нескольких темах всегда по её единственному каноническому пути; `mathematics/topics/` — читательские виды, не дубликаты); `updated` → `2026-10-23`. Остальные 9 тем и их пути не тронуты.
- `computations/maintenance/render_research_views.py` — исправление атлас-глоба, обязательное для первой волны (дизайн §7): maintained-множество считается рекурсивно (`rglob`) по корню и тематическим домам `mathematics/`, с исключением поддеревьев `topics/` (читательские виды) и `spectral_research/` (спектральное издание — не proof notes карты тем) и с прежним исключением 4 канонических корневых файлов по имени на уровне корня. Существующее равенство registered == maintained — счётчик maintained: заметка, потерянная при переезде, или путь карты без файла роняют `--check` и аудит. До/после волны счётчик равен 334.
- `computations/verification/scientific_registry_audit.py` — зеркальное исправление того же корневого глоба в `audit_topics()` (второй потребитель того же предположения «заметки только в корне»; дизайном не был назван, найден сборкой по падению контроля на посте: `mathematics topic map mismatch; stale=[3 новых пути]`). Семантика и текст отказа сохранены.
- `mathematics/topics/foundations/README.md` — 3 ссылки «Complete source membership»: `../../<заметка>` → `../../foundations/<заметка>`.
- `mathematics/topics/README.md` — абзац раскладки: вместо «stable paths in mathematics/» зафиксировано устройство фазы 2 (корень + тематические дома волнами, карта старых→новых путей — манифесты волн). Индекс тем — живой навигационный документ системы тем.
- Путевые упоминания в прозе (код-спаны, не ссылки; перевод в путевую форму, поскольку заметка перестаёт быть соседом по корню): `mathematics/open_questions.md` (1), `mathematics/results_20260907_addendum.md` (1), `mathematics/analytic_coboundary_regularization.md` (1) — `` `analytic_bracket_rigidity.md` `` → `` `foundations/analytic_bracket_rigidity.md` ``.
- `papers/resonance-cohomology/paper.json` — 1 строка `authoritative_sources`: `mathematics/analytic_bracket_rigidity.md` → `mathematics/foundations/analytic_bracket_rigidity.md`.
- `docs/corpus_atlas.md` — НЕ редактируется вручную: перегенерирован исправленным `render_research_views.py`; дифф — ровно 3 строки секции Foundations (только пути; заголовки и счётчики 334/10/197 неизменны). Остальные два выхода генератора (`record/scientific_dependency_graph.md`, `record/scientific_dependencies.json`) перегенерированы байт-идентично (у заметок волны нет claims) и в пакет не входят.

## Сознательно НЕ мигрированные носители (разрешаются настоящим манифестом)

- Замороженные инвентаризации и манифесты своих дат с прежними путями: `archive/evidence/**` (28 файлов), `evidence/executions/**` (17 файлов, включая `evidence/executions/20261022/repository-recheck/math_render.json` — датированная квитанция перепроверки), `archive/record/claim_ledger_addendum_20260907.md`.
- `record/audits/20261006/coverage.json` — датированный снимок аудита; `record/audits/era_baseline_attestation_20261023/inventory_abel.json`, `inventory_wick.json` — замороженные инвентаризации аттестации эпох (диспозиция HOLD пакета аттестации).
- Запечатанные входные копии комплекса: `evidence/research_checkpoint_20261007/raw/**` и `evidence/wave2_checked_20261007/raw/provenance/base_navigation/mathematics/open_questions.md` содержат голое упоминание `` `analytic_bracket_rigidity.md` `` — байты запечатанных входов не правятся никогда.
- Шаблонная фраза «Exact proof paths are unchanged» во всех 10 `mathematics/topics/*/README.md` — единый boilerplate о ревизии корпуса 2026-10-06 (ссылка рядом датирована); поименно не правится, разрешена настоящим манифестом как датированная формулировка ревизии, а не утверждение о текущей раскладке.
- `mathematics/README.md` — датированный журнал слоя; формулировка «canonical theorem sources live at stable paths in this directory» в его записях не правится волной 1 (заметок волны не упоминает); актуализация прозы корневых входов — на усмотрение родителя отдельным микрокоммитом фазы 2.

## Удаления (браузером, после landing копий)

3 файла корня: `mathematics/analytic_bracket_rigidity.md`, `mathematics/earlier_foundations.md`, `mathematics/hyperbolic_signed_trace_extension.md` — с пофайловой 404-сверкой и подтверждением существования `mathematics/foundations/` с тремя файлами.
