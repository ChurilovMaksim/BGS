# MANIFEST-P2REV — фаза 2, пакет P2-REV: `record/reviews/` и `record/research_candidates/` → `archive/`

**Источник:** живой main после пакета Pittel-cache (коммит `c6a4e383`): claims.json blob `f66a228ee12f9e8a8f60148f7bba4494c4327616` сверен с живым main коннектором при сборке; blobs всех 8 файлов сверены с листингами живого main.
**Состав: 8 файлов, 40 751 Б** — остаток корня `record/`, не вошедший в фазу 1 (packageF_coupling §2.7: опциональный подпакет F-2b, не исполнен; дизайн фазы 2 §8). Копии байт-в-байт; содержимое архивных копий не редактируется, все переносимые ссылки разрешаются настоящим манифестом.

## Переезжающие файлы

| Старый путь | Новый путь | git blob SHA | Байты |
|---|---|---|---|
| `record/reviews/abel_rigidity_20261016.md` | `archive/record/reviews/abel_rigidity_20261016.md` | `d4ad3d2d806765eb25578a29376abf12080d7336` | 16119 |
| `record/reviews/equal_edge_factorial_20261016.md` | `archive/record/reviews/equal_edge_factorial_20261016.md` | `2500af1c2a7b1774d2642740254c6815755d4656` | 10158 |
| `record/reviews/gaussian_hessian_20261016.md` | `archive/record/reviews/gaussian_hessian_20261016.md` | `213344c7b8bdd222b2261375f48ac82cff6b4ba4` | 5228 |
| `record/reviews/wick_poisson_20261016.md` | `archive/record/reviews/wick_poisson_20261016.md` | `e6cedcf239e0929c0fc7fb8f52714834a94b5206` | 6175 |
| `record/research_candidates/20261011/README.md` | `archive/record/research_candidates/20261011/README.md` | `bdcc8673fdeca96f6063d6f9c0a1a14e9dc5a2bd` | 701 |
| `record/research_candidates/20261011/all_moment_delay_bootstrap.md` | `archive/record/research_candidates/20261011/all_moment_delay_bootstrap.md` | `660e9ba2f184db499771b96ab7ec5fd4cf04e94a` | 705 |
| `record/research_candidates/20261011/conditional_clock_universality.md` | `archive/record/research_candidates/20261011/conditional_clock_universality.md` | `e0b1cbcf055756fd6ade5508c5d8b85c8ec57ce6` | 931 |
| `record/research_candidates/20261011/fourth_delay_law.md` | `archive/record/research_candidates/20261011/fourth_delay_law.md` | `f8e0533f16e9554a12f13f2b8758c1862b1f7702` | 734 |

## Миграции тем же коммитом

- `record/claims.json` — **4 путевых значения**, все в поле `proof_dependencies[0]`: BGS-TRACE-092 → `archive/record/reviews/abel_rigidity_20261016.md`; BGS-TRACE-093 → `archive/record/reviews/gaussian_hessian_20261016.md`; BGS-TRACE-094 → `archive/record/reviews/wick_poisson_20261016.md`; BGS-TRACE-055 → `archive/record/research_candidates/20261011/README.md`. Рекурсивный структурный дифф проверен: меняются только эти 4 листа; число claims 197; статусы, состояния и остальные поля не меняются; канонический формат файла сохранён (правка побайтно минимальна).
- **Эпохальная регистрация не требуется (измерено, не предположено).** Ни один из четырёх claims не входит в запечатанный снимок wave2 (96 строк): все четыре — follow-on эпохи `after_wave3` в `record/claim_integration_epochs.json`. Гейт follow-on (`wave2_integration_audit.run`) пинит по каждому ID только `state` и `source`; поле `proof_dependencies` эпохальным механизмом не пинится. Следствия: строк `historical_claim_amendments` не добавляется, множество `approved` в `wave2_integration_audit.py` не расширяется (остаётся 67), follow-on строки не редактируются, результат `wave2 run()` на пост-дереве байт-идентичен базе (29 unchanged / 67 amended).
- Навигация — **4 URL в 3 живых документах** `mathematics/` (только URL; текст вне URL побайтно идентичен базе): `abel_clock_rigidity_20261016.md` (1), `gaussian_equal_edge_20261016.md` (2: equal_edge_factorial и gaussian_hessian), `wick_collision_poisson_20261016.md` (1) — префикс `../record/reviews/…` → `../archive/record/reviews/…`.
- Сгенерированные поверхности (`record/claim_registry.md`, `record/scientific_dependency_graph.md`, `record/scientific_dependencies.json`, `docs/corpus_atlas.md`) путей пакета не содержат (перепись при сборке) и не перегенерируются; все render `--check` проходят на пост-дереве.

## Сознательно НЕ мигрированные носители (разрешаются настоящим манифестом)

- **Пакеты эпохи 20261016 (HOLD, дизайн фазы 2 §11.3):** `evidence/executions/20261016/abel-gaussian/source_manifest.json`, `evidence/executions/20261016/wick-poisson/{source_manifest.json, README.md, remote_publish.json}` пинят/цитируют reviews по старым путям. Это неприкосновенный провенанс с уже зафиксированной диспозицией HOLD (перепись эпохи 20261016): манифесты не перепинниваются и не редактируются.
- **Аттестация эпох:** `record/audits/era_baseline_attestation_20261023/inventory_{abel,wick}.json` — датированные записи аттестации (2026-10-23), перечисляют пути эпохи как исторические факты; не редактируются.
- **Замороженные копии под `archive/`:** workspace-снимки исполнений 20261011–20261020 и журналы интеграции (`archive/record/chat_integration_20261011.md` и др.) содержат старые пути как провенанс своего времени; не редактируются.
- **Внутренние относительные ссылки самих копий** (копии байт-идентичны, по доктрине F-1/F-2 не редактируются): ссылки вида `](../../mathematics/…)` и `](../../evidence/…)` из `archive/record/reviews/` геометрически разрешаются настоящим манифестом; ссылки внутри `archive/record/research_candidates/20261011/` на соседние файлы каталога (`conditional_clock_universality.md`, `fourth_delay_law.md`) остаются геометрически валидными, а `](../../cavity_continuation_20261011.md)` разрешается в `archive/record/cavity_continuation_20261011.md` геометрией архивной раскладки.
- **Прозовое упоминание без ссылки:** `mathematics/fourth_delay_law_20261011.md` называет `all_moment_delay_bootstrap.md` по имени в тексте (не URL) — по доктрине F-2 мигрируют только URL; упоминание разрешается настоящим манифестом.
- `record/equal_edge_factorial` как claim-ссылка отсутствует: файл держится только навигационной ссылкой из `mathematics/gaussian_equal_edge_20261016.md` (мигрирована выше) и пинами HOLD-пакетов.

## Удаления (следующим шагом, браузером)

Оригиналы: `record/reviews/` (4 файла) и `record/research_candidates/20261011/` (4 файла) — два каталоговых удаления после пуша копий и правок, с 404-сверкой поимённо.
