# MANIFEST-F2 — фаза 1, пакет F-2 «реестровый»: рабочий слой корня `record/` → `archive/record/`

**Источник:** дерево `bgs_current` (≙ main после коммита эпохального фикса `4b236e3` и удалений пакета F-1).
**Состав: 73 файла, 890 806 Б** — поименный класс «архив с миграцией» приложения к `packageF_coupling.md` (94 файла) минус 21 удержанный файл (секция ниже). Копии байт-в-байт; содержимое архивных копий не редактируется, все переносимые ссылки разрешаются настоящим манифестом.

## Расщепление пакета F — закрытие

Пакет F-2 завершает архивную часть расщепления пакета F (305 файлов): F-1 «ядро» (168, коммит 9cf3d1d), F-2 «реестровый» (настоящий пакет), F-STAY (28 файлов остаются в корне, фазы 2/3), F-SPECTRAL (3 файла остаются до заморозки спектральной линии), `research_operating_protocol.md` (вне пакетов до решения владельца). Из 94 файлов класса F-2 переезжают 73; 21 удержан по трём доказанным рантайм/контрактным связкам (секция ниже) до отдельного пакета миграции карт и эпохальных контрактов по прецеденту удержанных файлов F-1.

## Миграции тем же коммитом

- `record/claims.json` — **82 путевых значения** (81 `evidence[]` + 1 `source`) по 73 переезжающим файлам: только префикс `record/…` → `archive/record/…`; структурный дифф проверен — иных изменений нет, число claims 197, статусы не меняются. Значения, указывающие на удержанные файлы (16), не тронуты.
- `record/claim_integration_epochs.json` — эпохальная регистрация по рецепту исправления B2 (один коммит: миграция + поправки + одобренное множество): **24 новые строки** `historical_claim_amendments` и **5 обновлённых строк** (только `fields.evidence`, `disposition`, `review`); множество `approved` в `computations/verification/wave2_integration_audit.py` расширено теми же 24 ID (18 → 42). Затронуты только поля `evidence` запечатанных claims, каждая изменённая запись — чистая префиксная миграция переезжающего файла (fail-closed проверка «снимок ↔ staged» пройдена по всем 29 claims). Пин follow-on эпохи `after_wave3` для BGS-TRACE-055: `source` обновлён тем же коммитом, что и поле `source` claim, `state` не меняется, диспозиция дополнена записью о переезде.
- Новые поправки: BGS-LOOP-001, BGS-FLOW-016, BGS-FLOW-017, BGS-FLOW-018, BGS-FLOW-019, BGS-FLOW-020, BGS-FM-018, BGS-FM-020, BGS-TRACE-014, BGS-FM-021, BGS-FM-022, BGS-TRACE-015, BGS-FM-023, BGS-TRACE-016, BGS-FORMAL-002, BGS-TRACE-017, BGS-FM-024, BGS-TRACE-018, BGS-FM-025, BGS-TRACE-019, BGS-TRACE-020, BGS-FM-026, BGS-TRACE-021, BGS-TRACE-022.
- Обновлённые поправки: BGS-FM-008, BGS-FM-010, BGS-FLOW-021, BGS-FM-019, BGS-FORMAL-003 (у BGS-FM-008, BGS-FM-010, BGS-FORMAL-003 поле `evidence` добавлено к существующим полям авторитетных исправлений; у BGS-FLOW-021, BGS-FM-019 список `evidence` заменён на пост-F-2 значение).
- `literature/external_dependencies.json` — **не изменяется**: все 18 вхождений `project_sources` по файлам пакета лежат в запечатанных контрактах эпохи (см. H-EXT ниже); файлы-цели удержаны, пути остаются валидными.
- Навигация — 38 markdown-ссылок в 24 живых документах (только URL; текст вне URL побайтно идентичен базе) и 4 печатных GitHub-href в `manuscript/unified_sections/fixed_map_frontier.tex` (точечная замена URL; регенерация секции из мигрированного источника воспроизводит ровно эти 4 archive-URL). Сгенерированные представления перегенерированы штатными рендерами: `record/claim_registry.md` и `record/scientific_dependency_graph.md` — по одной строке (источник BGS-TRACE-055).
- Одна ссылка сознательно НЕ мигрирована: `mathematics/fractional_hamming_cancellation.md` — хэш-пинированный научный вход wave2 replay (`wave2_replay_source_bindings.json`, `wave2_scoped_input_bindings.json`); его байты не меняются (прецедент F-1 §Б.5), ссылка на `fractional_hamming_review.md` разрешается настоящим манифестом.

## Удержанные файлы (21) — НЕ входят в пакет

Файлы остаются в `record/`; их blob SHA и связки зафиксированы здесь. Переезд — отдельным пакетом миграции карт/контрактов (паттерн пакета E и удержанных файлов F-1) либо решением по эпохальному каналу внешних контрактов.

### H-EXT — пины запечатанных внешних контрактов (13)

| Файл (остаётся в `record/`) | git blob SHA | Байты |
|---|---|---|
| `record/cat_jet_rank_review.md` | `220c056cd04775eeb1e4163f00841260c5caf42a` | 21641 |
| `record/circular_kernel_route_20261004.md` | `a618dd38841206b57ef8ec86b0bb278833ed04c9` | 6586 |
| `record/finite_seven_pivots_review.md` | `7305d920127fc2ba8e0969da1663083b521d77c0` | 19524 |
| `record/fm008_fresh_independent_review.md` | `1fe5339fa96b9a2eb583264cc4cc8f6bf9cb34ea` | 25098 |
| `record/frozen_algebraic_review_20260924.md` | `c3742877196e6b1f4950b8b4adacbcdcc71c7151` | 2259 |
| `record/frozen_rank_review_20260923.md` | `c5b8bc968327c7efb265337632bb100650179ce9` | 2673 |
| `record/heisenberg_note_review_20260930.md` | `5d4b389815f25b7e3545652dbe0f3cd13fc15b68` | 12374 |
| `record/intermediate_old_layers_promotion.md` | `004c9dbe0d3e437d1aad2fdf0d1e51c70a224879` | 2474 |
| `record/noise_removal_program_20261005.md` | `fad3440aafc1dc517f9185ed4f6ea26f8b935867` | 14255 |
| `record/nonlinear_pressure_review_20260923.md` | `83d1799d47a767b65cc89340d589efaff7699f11` | 5207 |
| `record/trace_variance_review.md` | `81ec3ec24bb396390c1c0a8b4f1c253d302fd4fe` | 15329 |
| `record/two_continuations_review_20260924.md` | `134d0ac838d6a03f640e79446f6e17ed5f13532e` | 6743 |
| `record/weighted_periodic_review.md` | `1e66352f59dfd0e17c50de69ab550f73dfce409b` | 22227 |
### H-CHARGE — карта источников charge replay (2)

| Файл (остаётся в `record/`) | git blob SHA | Байты |
|---|---|---|
| `record/charge_strengthening_dependency_contract.json` | `d3449c5b4e0a7934cdacebdde39b20348d9acddb` | 6852 |
| `record/charge_strengthening_promotion.md` | `55496aa73b4ae3f8d40c2c6b5aa5151830bb7678` | 6360 |
### H-PUB — public_path живых верификаторов (6)

| Файл (остаётся в `record/`) | git blob SHA | Байты |
|---|---|---|
| `record/all_coordinate_translation_review.md` | `ca73e93ceaf6d2ea185fe70818b45c8f6f3d46dd` | 18071 |
| `record/balanced_hamming_review.md` | `bae720452070da453248da54460eeb030bf1fee7` | 22145 |
| `record/coordinate_translation_review.md` | `2ea415f94d50b2a161d2502983a2138f426a8cf6` | 20604 |
| `record/half_radius_obstruction_review.md` | `516235f1ce43af9bf77b89659e9d7d6baf623758` | 17015 |
| `record/low_switch_offcharge_review.md` | `e81599cc8ba5f1d1fec0949c2d3f8386284a53fe` | 16181 |
| `record/residual125_uniform_review.md` | `07c05fc809fa935acc02c44c92739702631e9629` | 17321 |

Механизмы удержания (по одному абзацу на группу — в таблице выше порядок групп тот же):

1. **H-EXT.** `literature/external_dependencies.json`: все 18 вхождений `project_sources` по 13 файлам лежат в записях запечатанного снимка 39 (EXT-EV-2015, EXT-PESIN-1977, EXT-RUELLE-1978 ×2 файла, EXT-PP-1990 ×2, EXT-POPESCU-2023 ×6, EXT-ROY-2016, EXT-COHEN-2025, EXT-KLZF-2022, EXT-LEMOINE-2025, EXT-EHL-2018, EXT-MANE-1981). `check_external_epoch` требует равенства контракта со снимком по всем полям, кроме `metadata_audit`; канала reviewed-поправок для внешних контрактов механизм не имеет (в отличие от claims). Миграция путей сломала бы эпохальный тест, а переезд без миграции — `require_path` научного аудита. Прецедент пакета C (EXT-PITTEL-2016) неприменим: та запись входит в разрешённое расширение эпохи, а не в запечатанные 39.
2. **H-CHARGE.** `record/charge_strengthening_replay_sources.json` (F-STAY) перечисляет оба файла с sha256; `charge_strengthening_replay.py` (`sources()`) требует каждый файл карты на месте как регулярный файл со сверкой хэша — та же связка, что удержала 5 файлов ядра в F-1.
3. **H-PUB.** STAY-карты `residual125_promotion_map.json`, `central_residual_promotion_map.json`, `half_radius_promotion_map.json` держат `public_path` + `public_sha256` на 6 файлов; живые верификаторы реестра (`residual125_certificates.py`, `central_residual_extension.py`, `half_radius_obstructions.py`) читают файл по `public_path` и сверяют sha256. На собранном дереве все три верификатора и charge replay проходят с удержанными файлами на месте.

## Геометрическая диспозиция 11-й заметки B2

`record/noise_removal_program_20261005.md` — 11-я заметка пакета B2 — удержана группой H-EXT (пины EXT-LEMOINE-2025 и EXT-EHL-2018). Её относительная ссылка `../evidence/executions/20261005-noise-removal-integration.json` при переезде в `archive/record/` разрешилась бы ровно в архивную квитанцию B2 геометрией раскладки; поскольку заметка остаётся в `record/`, ссылка остаётся формально мёртвой по своему текущему адресу (состояние существует с пакета B2) и разрешается настоящим манифестом совместно с MANIFEST-B2. Диспозиция закроется тем пакетом, который переместит заметку.

## Переезжающие файлы (73)

| Старый путь | Новый путь | git blob SHA | Байты |
|---|---|---|---|
| `record/actual_commutant_consolidation_review.md` | `archive/record/actual_commutant_consolidation_review.md` | `d1677bade051404851afc07ab35e3cd53a024c40` | 4548 |
| `record/actual_commutant_integration_map.json` | `archive/record/actual_commutant_integration_map.json` | `fca40d28df32cea52f7f89b8dedf2110639eed2f` | 20090 |
| `record/all_order_review_20261005.md` | `archive/record/all_order_review_20261005.md` | `dc87ae30b122f5d4c5ef72a396325c766acf2a36` | 24488 |
| `record/arithmetic_translation_review_20261006.md` | `archive/record/arithmetic_translation_review_20261006.md` | `19660f26af2852b7517073a3116023d55587c8eb` | 15175 |
| `record/cat_jet_even_obstruction_review.md` | `archive/record/cat_jet_even_obstruction_review.md` | `44191581d126c19582e9c506d8c7758451fe5475` | 16547 |
| `record/cat_jet_even_review.md` | `archive/record/cat_jet_even_review.md` | `621cbf6a89732898f23cc5ee87ba30e7a460d20f` | 17917 |
| `record/cat_jet_finite_review.md` | `archive/record/cat_jet_finite_review.md` | `4372f1a6f99e579da7ebd21c027c7f1dbf12d273` | 14157 |
| `record/cat_jet_multiplicity_review.md` | `archive/record/cat_jet_multiplicity_review.md` | `0f81600f2ff429aee5dd7af02770488b93a95a0e` | 14676 |
| `record/cat_jet_newest_review.md` | `archive/record/cat_jet_newest_review.md` | `065d01ae86e51c0bd47f34ccff901f093e08a2e4` | 20308 |
| `record/cat_jet_odd_review.md` | `archive/record/cat_jet_odd_review.md` | `aba485b5f01f4c311c2d0ef1a0c200bcef422fc2` | 21135 |
| `record/cat_jet_promotion_mapping.json` | `archive/record/cat_jet_promotion_mapping.json` | `2911056ab8cc5910e3cc287fa3d50bb1ada0f1e0` | 27490 |
| `record/cat_jet_tower_review.md` | `archive/record/cat_jet_tower_review.md` | `c1da8c13b93b4cd83391bd67568a37cdc883a7d0` | 18335 |
| `record/clock_control_review_20261006.md` | `archive/record/clock_control_review_20261006.md` | `ccfb4ee719ebab86de2ba569f0e2a6efd3230ff0` | 1777 |
| `record/collective_diffusion_review_20261006.md` | `archive/record/collective_diffusion_review_20261006.md` | `5aab900fbc9ea0af714ef0936f5caafd03a0be33` | 6574 |
| `record/collective_hierarchy_review.md` | `archive/record/collective_hierarchy_review.md` | `4886fa7a9b5fa49a735d1411c1877540af52e1df` | 21812 |
| `record/collective_promotion_mapping.json` | `archive/record/collective_promotion_mapping.json` | `e6d875eaa71d61145c035a616159afdf0379bc03` | 15759 |
| `record/critical_noise_review_20261005.md` | `archive/record/critical_noise_review_20261005.md` | `ff98cf8d86bcdb103f5cd009e96fd308dc605277` | 9181 |
| `record/exceptional_seven_mapping.json` | `archive/record/exceptional_seven_mapping.json` | `399d0414f675d411959cfb312ebc97631f16b07c` | 1529 |
| `record/exceptional_seven_review.md` | `archive/record/exceptional_seven_review.md` | `8eedbc687c8312be1d9e72fcba98701e07db46e9` | 1161 |
| `record/factorial_diagonal_promotion_mapping.json` | `archive/record/factorial_diagonal_promotion_mapping.json` | `62dad53117d2d80da5e5f077c2deeb6da1f2cc8f` | 16604 |
| `record/factorial_diagonal_review.md` | `archive/record/factorial_diagonal_review.md` | `fa5a0fca277dd3acb5e8b1166172315f6d47aadc` | 22237 |
| `record/first_old_layer_review.md` | `archive/record/first_old_layer_review.md` | `5b5a456e40df497474bc73ee0166d76164612945` | 12954 |
| `record/first_seven_independent_review.md` | `archive/record/first_seven_independent_review.md` | `502ec81c5eb9ffbe9f6517b18624748acea96290` | 18133 |
| `record/first_seven_promotion_mapping.json` | `archive/record/first_seven_promotion_mapping.json` | `ba07aacfe235c853f2bfb572daf0d99d4bd61ee5` | 2464 |
| `record/five_cluster_input_review.md` | `archive/record/five_cluster_input_review.md` | `150b802fd31d50548c4e8515ffea40ded2109bb3` | 14278 |
| `record/fm008_fresh_audit_mapping.json` | `archive/record/fm008_fresh_audit_mapping.json` | `54d371e58f39f2c792a54224015e20a4e3d1d987` | 2974 |
| `record/four_block_independent_review_20261006.md` | `archive/record/four_block_independent_review_20261006.md` | `428cbc2550384ba1aac1871ec234bf14b4ae8ff6` | 3930 |
| `record/four_cut_lean_review_20261006.md` | `archive/record/four_cut_lean_review_20261006.md` | `ecf7727dee606c28257c7d0108ed9c0cf4f85413` | 11491 |
| `record/four_cut_rank_two_review_20261006.md` | `archive/record/four_cut_rank_two_review_20261006.md` | `81bb94658771e41472772e3b74b029f0e05d65e8` | 11482 |
| `record/fractional_hamming_raw_mapping.json` | `archive/record/fractional_hamming_raw_mapping.json` | `3ff68fc39f99827734c811fa8a4fc1b6acf5541b` | 22861 |
| `record/fractional_hamming_review.md` | `archive/record/fractional_hamming_review.md` | `28eb604948c2b3f21d620e31bd565b62958d6098` | 7973 |
| `record/frozen_operator_transfer_review_20261006.md` | `archive/record/frozen_operator_transfer_review_20261006.md` | `bea84d8cfe7f72d1cb3e15ba0ab53cf5fcc9eb36` | 6829 |
| `record/global_rotated_box_integration_delta.json` | `archive/record/global_rotated_box_integration_delta.json` | `0d6b1a7459c06ff52cbdb66b5d95803bd563af7d` | 8084 |
| `record/global_rotated_box_review_scope.md` | `archive/record/global_rotated_box_review_scope.md` | `39aab3bc4f33524fc99c5ee20c48bdf331b7769b` | 22935 |
| `record/growing_degree_review_20261005.md` | `archive/record/growing_degree_review_20261005.md` | `fa387d4f4842f906c10ff3386eef8030535273e5` | 7495 |
| `record/heisenberg_pair_review_20261005.md` | `archive/record/heisenberg_pair_review_20261005.md` | `f465534c312750e184b468dbea9b3dd444c8a62e` | 5811 |
| `record/heisenberg_wkb_integration_delta.json` | `archive/record/heisenberg_wkb_integration_delta.json` | `b4a1606fd31c9537fbdc1f9c0c0af05d1fa7a98e` | 1019 |
| `record/heisenberg_wkb_prior_attribution.json` | `archive/record/heisenberg_wkb_prior_attribution.json` | `e5ea1ec4f613dbe73f73a8a71621f08690d1b781` | 896 |
| `record/heisenberg_wkb_review_provenance.json` | `archive/record/heisenberg_wkb_review_provenance.json` | `00c6596582a974d12ce7f738e2db20993c8040d3` | 1461 |
| `record/heisenberg_wkb_review_scope.md` | `archive/record/heisenberg_wkb_review_scope.md` | `5cd30da0a680c4f515a3b12f9397553ed3eaecc7` | 2849 |
| `record/intermediate_old_layers_promotion_mapping.json` | `archive/record/intermediate_old_layers_promotion_mapping.json` | `c8071325426cef2bf03a82cbcfc8670cd8f5d163` | 6724 |
| `record/intermediate_return_review.md` | `archive/record/intermediate_return_review.md` | `b22c976f22a3d601bdc41ea65a1279d664c2086b` | 17724 |
| `record/loop_test_reductions_review_20261006.md` | `archive/record/loop_test_reductions_review_20261006.md` | `7544e1c42b42973d19c5703d2e59694bdb5d4420` | 5256 |
| `record/marked_path_independent_review_20261006.md` | `archive/record/marked_path_independent_review_20261006.md` | `6d161e09b605a47b98183a97865e6ff0ee9be05c` | 11906 |
| `record/mixed_ordered_diagonal_review.md` | `archive/record/mixed_ordered_diagonal_review.md` | `c7d7ff60f8bff595e71d9408449dafdfb0010cdc` | 23430 |
| `record/next_proofs_consolidation_review_20261006.md` | `archive/record/next_proofs_consolidation_review_20261006.md` | `08e7ac838c2f836f0eabcb87e759447a0fd3cc3d` | 3733 |
| `record/odd_newest_sector_review.md` | `archive/record/odd_newest_sector_review.md` | `875b207c364fe3e8b7aefd21605566eb220b0fc8` | 25226 |
| `record/odd_sector_count_combination_review.md` | `archive/record/odd_sector_count_combination_review.md` | `a98cdd27b2845a46c889b4101a28743580b1ab35` | 4027 |
| `record/ordered_diagonal_mapping.json` | `archive/record/ordered_diagonal_mapping.json` | `cd9deb7b71175cff6293c695b61185aeed072f49` | 6009 |
| `record/ordered_diagonal_review.md` | `archive/record/ordered_diagonal_review.md` | `f23471b6e11599271cb95a61804050e84f4f6f6e` | 23521 |
| `record/original_channel_gap_review_20261006.md` | `archive/record/original_channel_gap_review_20261006.md` | `f0e7b8d785cb5804d76b45fb4b7334de980fca75` | 7863 |
| `record/paired_phase_promotion_mapping.json` | `archive/record/paired_phase_promotion_mapping.json` | `f61a779cfabb1c2e35bbc20f727887977d60b0b7` | 7172 |
| `record/paired_phase_review.md` | `archive/record/paired_phase_review.md` | `e232f6e6b2340effc88b769a2dad8abe96c5de0c` | 18206 |
| `record/path_theorems_review_20261006.md` | `archive/record/path_theorems_review_20261006.md` | `9aaff5c65be1dc144cd8904ba2ad9814d4d505f2` | 8749 |
| `record/phase_frostman_review.md` | `archive/record/phase_frostman_review.md` | `2084361bd2719c5046c9444cd8fbe6a2d61a3a90` | 14539 |
| `record/physical_homoclinic_weights_review.md` | `archive/record/physical_homoclinic_weights_review.md` | `0940709c37e5b4e13b3ff899416878b5c8a3d70d` | 21192 |
| `record/quadratic_occupation_review.md` | `archive/record/quadratic_occupation_review.md` | `ec411c7ad235c70b40e312975bde9b5723ba833e` | 15397 |
| `record/quadratic_slow_source_review.md` | `archive/record/quadratic_slow_source_review.md` | `83ccbe6bb1d2313e21b3e2dc55cb9c18b4c0e0a4` | 14403 |
| `record/quantum_homoclinic_first_loop_review.md` | `archive/record/quantum_homoclinic_first_loop_review.md` | `2ebf4e38b3e09ca29781a7b7e22585c53fc35f65` | 18675 |
| `record/ramified_first_seven_promotion_mapping.json` | `archive/record/ramified_first_seven_promotion_mapping.json` | `dcbd31285ce7b16fa9cc971de7cd31e59ab54466` | 2782 |
| `record/ramified_first_seven_review.md` | `archive/record/ramified_first_seven_review.md` | `7b04ef727a21fd7dca37d5928ac4db807feaa71d` | 17196 |
| `record/ramified_higher_promotion_mapping.json` | `archive/record/ramified_higher_promotion_mapping.json` | `d1efe62316f76a58251eb75abcb4e9286841d95a` | 1794 |
| `record/ramified_higher_review.md` | `archive/record/ramified_higher_review.md` | `4e10d04ea9e6d02e425bdac00005c0021dcdc7da` | 17216 |
| `record/research_checkpoint_20261008.md` | `archive/record/research_checkpoint_20261008.md` | `c6befb6893ad52282c22d3bd8199997b4e47bc72` | 9052 |
| `record/residual25_affine_review.md` | `archive/record/residual25_affine_review.md` | `4578d683e41086898f783df2f0add3dc7f75b4ab` | 15437 |
| `record/schur_reduction_integration_proposal.json` | `archive/record/schur_reduction_integration_proposal.json` | `33a8f7ed987cb5f65f000dcf850d61d13527bf7f` | 3207 |
| `record/selected_weighted_interface_review.md` | `archive/record/selected_weighted_interface_review.md` | `b9d0ae5cd9900d9c0bd1065416b3537985390d56` | 17382 |
| `record/seven_primary_semantic_review.md` | `archive/record/seven_primary_semantic_review.md` | `9e9b7c00a06badf0277d0bdf5f5ee64086a4aec6` | 10835 |
| `record/spectral_extension_promotion_mapping.json` | `archive/record/spectral_extension_promotion_mapping.json` | `36b16ac5162dfc8cf5a8f8bd9107e73ba50e090c` | 14712 |
| `record/stationary_cyclic_residual_review.md` | `archive/record/stationary_cyclic_residual_review.md` | `3fb7a4e0b5878f9a5269b5bfe5ad3e7f38d29ace` | 8057 |
| `record/three_block_independent_review_20261006.md` | `archive/record/three_block_independent_review_20261006.md` | `4deb4f4dbd9f7add8712467f3a436dd8907ebd83` | 10245 |
| `record/uniform_five_cluster_review.md` | `archive/record/uniform_five_cluster_review.md` | `bc52436f3efc2a00a409c8342d71f9eb4c2ba385` | 18040 |
| `record/weighted_support_promotion_mapping.json` | `archive/record/weighted_support_promotion_mapping.json` | `ff7d110454098b8f6dd009b94153da84e5072a6a` | 13680 |
