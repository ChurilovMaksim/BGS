# MANIFEST-P2MATH3 — волна 3 P2-MATH: тематический дом `mathematics/information-theory/`

Волна 3 пакета P2-MATH (фаза 2 реструктуризации BGS). По канонической карте тем
`record/mathematics_topics.json` тема `information-theory` (ровно 10 заметок, членство
однозначно — другие темы их не перечисляют, проверено) переезжает в новый дом
`mathematics/information-theory/`. Тем же коммитом мигрируют все живые потребители
(карта тем, значения `source`/`proof_dependencies`/`boundary` follow-on claim
BGS-RES-016 в `record/claims.json`, строка `after_wave3` BGS-RES-016 в
`record/claim_integration_epochs.json`, вид темы, рукописная ссылка, заголовок
верификатора, 4 прозовых/ссылочных упоминания в заметках, перегенерированные
навигационные виды). Эпохальная часть измеренно follow-on-only: поправок
`historical_claim_amendments` нет, множество `approved` не расширяется (67),
`wave2_integration_audit.run()` байт-идентичен базе.

База: живой main после закрытия волны 2 (`b736a27`); локально
`p2_math3_work/base_tree` (байт-копия `p2_math2_work/post_tree`).

## 1. Карта переезда (старый → новый путь; байт-копии, SHA-256 новых файлов)

| Старый путь | Новый путь | SHA-256 нового файла |
|---|---|---|
| `mathematics/bosonic_information_limits_20260907.md` | `mathematics/information-theory/bosonic_information_limits.md` | `b84f95ee91197908f2d5fcc19782c17d1cb3bc00b03c779332d9cb8f3693e11f` |
| `mathematics/coherent_aperture_minimax.md` | `mathematics/information-theory/coherent_aperture_minimax.md` | `decc7e4a6f653f6a2bd54b71a0ab8c89523a7eb346a340ab5c883652309c5255` |
| `mathematics/holomorphic_shell_identifiability.md` | `mathematics/information-theory/holomorphic_shell_identifiability.md` | `8b2e931d841261a137eb1d7fd539b6ca8c2d6f15fe42e53fd0d182e2d9aac1b7` |
| `mathematics/multiradius_polynomial_rigidity.md` | `mathematics/information-theory/multiradius_polynomial_rigidity.md` | `3ad312320d6878118c9c3f78037e4abc45d69a7ff7c466c6624899877364dcb0` |
| `mathematics/multisphere_polynomial_rigidity.md` | `mathematics/information-theory/multisphere_polynomial_rigidity.md` | `6629ee5a19c925f8c256ed43329f6daabd698b8b8cfc3e97ac32251812830802` |
| `mathematics/polynomial_shell_identifiability.md` | `mathematics/information-theory/polynomial_shell_identifiability.md` | `388d6d903e87a80e57d5564bda9ac47689d3d59e71651262bf7e91288415383f` |
| `mathematics/pure_loss_discrimination.md` | `mathematics/information-theory/pure_loss_discrimination.md` | `1e8e00f79d7de61eb5a5a6ba254f11b96cd777b0b4da55f25de238551e79987c` |
| `mathematics/quadratic_response_limits.md` | `mathematics/information-theory/quadratic_response_limits.md` | `0575e71470a98a5d324cd0d1fe7700f23b6bf3986c8c3a06d59104fd154feaa0` |
| `mathematics/shadow_tube_history_bridge.md` | `mathematics/information-theory/shadow_tube_history_bridge.md` | `12e72992e2c81fc542e390b3f42aabde805c0c27b35c3b8b57d73a5251d67059` |
| `mathematics/two_radius_quadrature_rigidity.md` | `mathematics/information-theory/two_radius_quadrature_rigidity.md` | `06295d40901054bc1babeac41623bca6aac5fb28b38c9f269a069cf47230fa12` |

Переименование `bosonic_information_limits_20260907.md` → `bosonic_information_limits.md`
— по правилу дизайна фазы 2 (§7/line 158: датированные имена при переезде заменяются
предметными); коллизий стема `bosonic_information_limits` в слое нет (проверено поиском
по всему дереву). Заголовок внутри файла (`# Bosonic information proof summary — 2026-09-07`)
сохранён как провенанс — переименовано только имя файла. Хэш `12e72992…` совпадает с
пином в `record/weighted_periodic_review.md` (независимый аудит 2026-10-06) — байт-копия
подтверждена третьей стороной записи.

## 2. Эпохальная часть: follow-on BGS-RES-016 (измерено, не предположено)

- Claim `BGS-RES-016` (`state: proved`) — единственный из 197 claims, упоминающий заметки
  волны (полный скан claims.json по всем полям всех строк).
- `record/claims.json`, 4 значения: `source` → новый дом (гейт follow-on пинит
  `state`+`source`); `proof_dependencies` ×2 → новые дома (поля не запинены для
  follow-on — потребительская миграция); проза `boundary` → новый путь
  `two_radius_quadrature_rigidity.md` (не запинено).
- `record/claim_integration_epochs.json`: 1 строка `after_wave3` — `source` → новый дом;
  проза `disposition` → новый путь (гейт требует только `state`+`source` и непустой
  disposition; содержимое прозы не запинено).
- Измерено: BGS-RES-016 отсутствует в запечатанном снимке wave2 (96 строк), дельте wave2
  (5 IDs), wave3 (2 IDs) и в `historical_claim_amendments`; `approved` остаётся 67;
  `historical_claim_amendments` — 67 строк без добавлений; внешних epoch-гейтов по этим
  полям нет (`test_external_epoch_preservation` проверяет только external-зависимости
  и запечатанные строки).

## 3. Миграции живых потребителей (тем же коммитом)

- `record/mathematics_topics.json` — 10 путей темы; `updated` уже `2026-10-24` (волна 2).
- `mathematics/topics/information-theory/README.md` — 18 относительных ссылок
  `](../../<stem>.md)` → `](../../information-theory/<stem>.md)` (bosonic — с переименованием);
  метка membership `[bosonic_information_limits_20260907]` → `[bosonic_information_limits]`;
  метка reading-sequence `[3. bosonic information limits 20260907]` → `[3. bosonic information limits]`.
- `manuscript/unified_sections/fixed_map_frontier.tex` — 1 `\href` на GitHub-blob старого
  пути → новый дом.
- `computations/verification/history_localization.wl` — 1 путь в заголовке комментария →
  новый дом.
- `mathematics/fixed_map_resolvent_frontier.md` — 1 markdown-ссылка
  `(shadow_tube_history_bridge.md)` → `(information-theory/shadow_tube_history_bridge.md)`.
- `mathematics/weighted_periodic_equidistribution.md` — 1 код-спан →
  `` `information-theory/shadow_tube_history_bridge.md` ``.
- `mathematics/physical_homoclinic_weights.md` — 1 прозовое упоминание → путевая форма.
- `mathematics/resonance_riesz_regularization.md` — 1 прозовое упоминание
  (`see quadratic_response_limits.md`) → путевая форма.
- `docs/corpus_atlas.md`, `record/claim_registry.md`, `record/scientific_dependency_graph.md` —
  перегенерированы (диффы — только пути/строка BGS-RES-016; счётчики 334/10/197 неизменны).
  `record/scientific_dependencies.json` перегенерирован байт-идентично — в пакет не входит.
- Сиблинговые прозовые упоминания внутри переехавших заметок
  (`multiradius_polynomial_rigidity.md` → `two_radius_quadrature_rigidity.md`,
  `multisphere_polynomial_rigidity.md` → `multiradius_polynomial_rigidity.md`) —
  валидны в общем доме, не правятся (прецедент волны 2).

## 4. Носители старых путей, НЕ правленные волной (классификация)

- **Замороженные (не правятся; разрешаются настоящим манифестом):**
  `archive/**` — датированные манифесты/acceptance-снимки со старыми путями;
  `evidence/executions/**` — датированные манифесты прогонов;
  `record/audits/20261006/coverage.json`, `record/audits/era_baseline_attestation_20261023/*` —
  датированные/аттестованные инвентаризации;
  `record/weighted_periodic_review.md` — датированный аудит 2026-10-06 с хэш-пинами
  (редактирование сфальсифицировало бы запись проверки);
  запечатанные входные копии `evidence/wave2_checked_20261007/raw/**`,
  `evidence/research_checkpoint_20261007/raw/**`.
- **Корректны как есть:** докстринг `computations/verification/multiradius_rigidity.py`
  (голое имя файла без пути — имя не менялось);
  `computations/information_limits_20260907.md` (имена кодовых файлов `.py`/`.cpp`,
  не заметки); `manuscript/BGS_unified.tex` (`\input` `.tex`-секции, не заметки);
  `record/claim_ledger.md` (путь `.tex`-секции рукописи).
- **Boilerplate:** «Exact proof paths are unchanged» во всех видах тем — идентичный шаблон.

## 5. Контроли

Счётчик maintained: 334 == 334 на посте (равенство registered == maintained в
`render_research_views.py` и `scientific_registry_audit.py`). Полная таблица контролей —
в `pkg_p2_math3_final/REPORT.md` §5; репетиция разрешения — §6 (все markdown-ссылки
всех затронутых файлов резолвятся — урок волны 2).
