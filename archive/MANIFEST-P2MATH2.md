# MANIFEST-P2MATH2 — фаза 2, пакет P2-MATH, волна 2 (locality): `mathematics/*.md` → `mathematics/locality/`

**Источник:** живой main после пакета P2-MATH волны 1 (коммит `6dc5bcf` + браузерные удаления 3 оригиналов волны 1; перепроверено 2026-10-24). Сборка — на пост-дереве волны 1 (`p2_math1_work/post_tree`). `record/claims.json` базы: git blob `6caca2fef44fc046225ae66a025c55e6183aebca` — совпадает с живым main (перепроверено родителем 2026-10-24). В репозиторий ничего не писалось; пуш — шаг родителя.
**Состав волны: 3 заметки, 1 новый тематический дом** — `mathematics/locality/`. Тема и членство — строго по канонической карте `record/mathematics_topics.json` (тема `locality`, ровно 3 пути; другие темы их не перечисляют). Порядок волн — по возрастанию связности (дизайн §7, план волн — pkg_p2_math1_final/REPORT.md §3): у locality — 3 follow-on `source` у `after_wave3` (BGS-FM-034/035/036), запечатанных источников нет, датированных имён нет, членства в других темах нет.

## Переезжающие файлы

| Старый путь | Новый путь | SHA-256 содержимого | Байты |
|---|---|---|---:|
| `mathematics/fixed_strength_locality.md` | `mathematics/locality/fixed_strength_locality.md` | `4d0618c993ebcdf63fedf755c40c4121279c9aefbaf7bda67bd73f2133abe74b` | 23526 |
| `mathematics/fourier_tail_locality.md` | `mathematics/locality/fourier_tail_locality.md` | `4ebfff04d676145e252a52c6fd96f0429b78234aff5fd6e15e8d7fbe864a64f6` | 676 |
| `mathematics/locality_robustness.md` | `mathematics/locality/locality_robustness.md` | `b954a52798389496fa7590fad6dc8be5bd037d192255c94d23429904815c5e9d` | 8096 |

Все три — байт-копии базы (SHA-256 равны исходникам). Единственная относительная ссылка внутри заметок — сиблинговая в `locality_robustness.md` строка 10 (`[fixed-strength locality](fixed_strength_locality.md)`); после переезда обеих заметок в один дом она остаётся валидной — пограничного перевода не требуется. Других относительных ссылок и путевых упоминаний в трёх заметках нет (полный скан при сборке).

## Эпохальная часть волны: ТОЛЬКО follow-on source ×3 (измерено, не предположено)

- Три claims `BGS-FM-034`, `BGS-FM-035`, `BGS-FM-036` (`state: proved`): поле `source` = `mathematics/fixed_strength_locality.md` → `mathematics/locality/fixed_strength_locality.md` в `record/claims.json` (3 строки; формат файла сохранён — построчная замена, механически, fail-closed: ровно 3 вхождения).
- Те же три claims — строки follow-on эпохи `after_wave3` в `record/claim_integration_epochs.json`; гейт follow-on (`wave2_integration_audit.run()`) пинит для каждой строки пару `state`+`source`: `active.get('state')==row['state'] and active.get('source')==row['source']`. Поэтому 3 строки `after_wave3` обновлены ТЕМ ЖЕ коммитом (прецедент P2-G1 и план волны: follow-on миграция source тем же коммитом).
- Измерено: ни один из трёх claims не входит в запечатанный снимок wave2 (96 строк), ни в дельту wave2 (5 IDs), ни в wave3 (2) — `check_prior_claims` их не ограничивает (они моложе запечатанного снимка; гейт после_wave3 подтверждает непересечение). Строки `historical_claim_amendments` НЕ добавляются; множество `approved` в `wave2_integration_audit.py` НЕ расширяется (остаётся 67); `wave2 run()` на посте — rc=0, выходной словарь байт-идентичен базе.
- Других полей claims с этими путями нет: полный скан всех 197 claims по всем полям — только 3 значения `source`.

## Отредактированные тем же коммитом файлы (миграция потребителей)

- `record/mathematics_topics.json` — 3 пути темы `locality` переведены на новый дом; `updated` → `2026-10-24`. Остальные 9 тем не тронуты. Счётчик maintained: 334 == 334 (рекурсивные перечисления волны 1 в базе; зарегистрированное равенство — fail-closed контроль).
- `mathematics/topics/locality/README.md` — 9 относительных ссылок членства: `../../<заметка>.md` → `../../locality/<заметка>.md` (разделы членства, последовательность чтения, список файлов).
- `literature/folded_quadratic_sources.md` — 1 ссылка: `](../mathematics/fixed_strength_locality.md)` → `](../mathematics/locality/fixed_strength_locality.md)`.
- `mathematics/arithmetic_word_expansion_obstruction.md` (волны 8/10, позже) — 2 правки: 1 прозовое путевое упоминание `mathematics/fixed_strength_locality.md` → новый путь (действителен и после её собственного переезда) и 1 ссылка `[fixed_strength_locality.md](fixed_strength_locality.md)` → `(locality/fixed_strength_locality.md)` (цель переехала в дом; найдено репетицией разрешения ссылок).
- `mathematics/extremal_resonance_nondegeneracy.md` (волна 7, позже) — 1 голое код-спан упоминание `` `fourier_tail_locality.md` `` → путевая форма `` `locality/fourier_tail_locality.md` `` (заметка перестаёт быть соседом по корню; прецедент волны 1).
- `computations/verification/fixed_strength_locality.py` — 1 строка докстринга: `mathematics/fixed_strength_locality.md` → новый путь.
- `docs/corpus_atlas.md` — НЕ правится вручную: перегенерирован `render_research_views.py`; дифф — ровно 3 строки секции Locality (только пути; заголовки и счётчики 334/10/197 неизменны).
- `record/claim_registry.md` — перегенерирован `render_claim_registry.py`; дифф — ровно 3 строки (только `source` BGS-FM-034/035/036).
- `record/scientific_dependency_graph.md` — перегенерирован `render_research_views.py`; дифф — ровно 3 строки (только `source` BGS-FM-034/035/036).
- `record/scientific_dependencies.json` — перегенерирован тем же генератором, байт-идентичен базе (путей заметок не содержит) — в пуш НЕ входит.

## Сознательно НЕ мигрированные носители (разрешаются настоящим манифестом)

- Точная форма старого пути (`mathematics/<stem>.md`, 44 носителя на пост-дереве) — ВСЕ заморожены: `archive/**` (24 файла — манифесты и workspace-снимки своих дат, включая `archive/record/locality_delivery_status_20260905.md`), `evidence/executions/**` (17 файлов датированных манифестов прогонов, включая датированную квитанцию перепроверки `evidence/executions/20261022/repository-recheck/math_render.json`), `record/audits/20261006/coverage.json` (датированный снимок), `record/audits/era_baseline_attestation_20261023/inventory_abel.json`, `inventory_wick.json` (замороженные инвентаризации аттестации эпох, диспозиция HOLD).
- `literature/expansion_wavepacket_sources_20261004.md` — датированный литературный снимок (20261004): голое упоминание `fixed_strength_locality.md` в прозе (строка 19) не правится; датированные снимки разрешаются манифестом, не редактурой.
- Имена файлов верификаторов (`computations/verification/fixed_strength_locality.py`, `computations/verification/locality_robustness.py`, `computations/cpp/fixed_strength_locality_exact.cpp`) — кодовые имена верификаторов, не указатели на заметки; не трогаются (код-домены — не предмет P2-MATH).
- Сиблинговая ссылка `mathematics/locality/locality_robustness.md` строка 10 — живая и валидна в новом доме; не «остаток».
- Шаблонная фраза «Exact proof paths are unchanged» в `mathematics/topics/*/README.md` — boilerplate ревизии корпуса 2026-10-06 (прецедент волны 1), разрешён манифестом как датированная формулировка, не утверждение о текущей раскладке.

## Удаления (браузером, после landing копий и readback)

3 файла корня, поимённо: `mathematics/fixed_strength_locality.md`, `mathematics/fourier_tail_locality.md`, `mathematics/locality_robustness.md` — с пофайловой 404-сверкой и подтверждением существования `mathematics/locality/` с тремя файлами. Локальный post_tree сборки уже отражает целевое состояние (оригиналы удалены в модели).
