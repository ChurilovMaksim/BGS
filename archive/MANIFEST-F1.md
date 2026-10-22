# MANIFEST-F1 — фаза 1, пакет F-1 «ядро»: рабочий слой корня `record/` → `archive/record/`

**Источник:** дерево `bgs_postC` (пост-C конфигурация, ≙ main `2401f0f` для областей пакета);
для `record/claims.json` актуальна staged-копия пакета B2 (миграция 10 путей evidence).
**Состав: 168 файлов, 1 002 264 Б** — поименный класс «архив (ядро)» приложения к
`packageF_coupling.md` минус 11 удержанных файлов (секция ниже). Копии байт-в-байт;
содержимое архивных копий не редактируется, все переносимые ссылки разрешаются
настоящим манифестом.

## Удержанные файлы (11) — НЕ входят в пакет

При сборке на собранном дереве обнаружены рантайм-связки класса «архив (ядро)» с живыми
replay-машинами, не видимые статическому анализу связности (потребитель итерирует
JSON-карту/биндинги обобщённо и требует каждый перечисленный файл на месте с сверкой
sha256). Файлы остаются в `record/` до отдельного пакета миграции карт по прецеденту
пакета E либо переклассификации в F-STAY. Доказательства и варианты — REPORT.md пакета, §Б.

| Файл (остаётся в `record/`) | git blob SHA | Байты | Связка |
|---|---|---|---|

| `record/charge_strengthening_computation_contract.json` | `8e4c7b36b1b652c928afe4110147b9759ce532f0` | 3236 | см. REPORT §Б |
| `record/charge_strengthening_editorial_mapping.json` | `9a5fdb6c72318b70fea827576bbf00df32379254` | 6601 | см. REPORT §Б |
| `record/charge_strengthening_integration_proposal.md` | `8ad781b34e0b4850eb70e46b293afc31cbbbd5ef` | 3507 | см. REPORT §Б |
| `record/charge_strengthening_port_mapping.json` | `ccd05d6a8ae8657a3033c6b5c422e70c5faf3821` | 1171 | см. REPORT §Б |
| `record/charge_strengthening_raw_mapping.json` | `01e1809657879748fcd79395c26b3e1a1b75c6a8` | 31194 | см. REPORT §Б |
| `record/checked_research_checkpoint_20261007.md` | `0d73c6f91bf4ea40f5e886c925df342e18d3106f` | 12974 | см. REPORT §Б |
| `record/research_checkpoint_import.json` | `a6013045374988dc110bbba86c9d3886cc71dfd7` | 164577 | см. REPORT §Б |
| `record/research_checkpoint_balanced_audit_import.json` | `522e47ec7f170a512918d85f7b223d523ac6311c` | 4835 | см. REPORT §Б |
| `record/research_checkpoint_proof_mapping.json` | `4d3110ed6a7f93a53857b8c0441bd82399f9c42d` | 7473 | см. REPORT §Б |
| `record/schur_replay_freshness_repair_receipt.json` | `b5a25a302df466652a75a12c258c5f84002eab61` | 15022 | см. REPORT §Б |
| `record/schur_reduction_promotion.md` | `1b1323f148144075a1491a811d69b245d0c6b417` | 7518 | см. REPORT §Б |

## Расщепление пакета F (вне настоящего пакета)

- **F-STAY — 28 файлов** остаются в корне `record/`: 8 governance/audit-required
  (`branch_protection_policy.md`, `consolidation_map.json`, `final_consolidation_audit_20260906.md`,
  `final_research_handoff_20260921.md`, `publication_review_20260912.md`,
  `repository_conventions.md`, `return_local_limits_review_20260913.md`,
  `return_obstruction_review_20260912.md`) и 20 живых машин с кодовыми потребителями.
  Судьба — фазы 2/3.
- **F-SPECTRAL — 3 файла** остаются до заморозки спектральной линии:
  `spectral_final_integration_20261021.md`, `spectral_master_audit_20261021.md`,
  `trace_closure_20261022.md`.
- **F-2 «реестровый» — 94 файла** (87 claims-пинов ∪ 13 EXT-пинов) переезжают отдельным
  пакетом с миграцией `claims.json` и `external_dependencies.json` тем же коммитом.
- **`research_operating_protocol.md`** — вне пакетов до решения владельца (претензия
  документа на действующий регламент при нуле ссылок с живой поверхности управления).

**Арифметическая сверка со спецификацией.** Сводная таблица §5.1 спецификации называет
F-1 «180 файлов / 1,27 МБ»; поименное приложение даёт 179 файлов класса «ядро». Разница —
ровно `research_operating_protocol.md` (7 766 Б): сводная цифра посчитана вычитанием
(305 − 28 − 3 − 94 = 180) без вычета файла владельца. Поименный список исчерпывает все
305 файлов пакета F ровно по одному разу (сверено с деревом). Из поименных 179 в пакет
входят 168; 11 удержаны (секция выше).

## Геометрическая диспозиция 11 заметок B2

10 из 11 заметок, пинивших квитанции пакета B2 относительными ссылками, входят в F-1:
`all_order_program_20261005.md`, `critical_noise_program_20261005.md`,
`folded_quadratic_audit_20261004.md`, `folded_quadratic_review_20261001.md`,
`frozen_operator_transfer_program_20261006.md`, `growing_degree_program_20261005.md`,
`heisenberg_pair_program_20261005.md`, `polynomial_coboundary_review_20261004.md`,
`resonant_density_review_20261001.md`, `signed_heisenberg_review_20260930.md`.
Их ссылки вида `../evidence/executions/<квитанция>.json` после переезда заметок
`record/ → archive/record/` разрешаются в `archive/evidence/executions/<квитанция>.json` —
фактический адрес квитанций после пакета B2 — **без единой правки** (геометрия раскладки
`archive/<исходный путь>`). Остальные evidence-ссылки этих заметок (манифесты внутри
`evidence/executions/<дата>/…`) указывают на неархивированные деревья и в байтовых копиях
не меняются. 11-я заметка, `noise_removal_program_20261005.md`, дополнительно пинится
EXT-записями и входит в **F-2**; её диспозиция относится к пакету F-2.

## Сопутствующие правки того же пакета

- `record/errata.json` — ровно 1 значение: `entries[31]` (ERR-032), поле `authority`:
  `record/repository_reconciliation_20261020.md` → `archive/record/repository_reconciliation_20261020.md`
  (аудит реестра делает `require_path` по каждому `authority`).
- Навигационная миграция: 103 markdown-ссылки на переезжающие файлы F-1 в 47 живых
  документах (канон корня `record/README.md`, `record/claim_ledger.md`, `record/retractions.md`;
  корневые `CHANGELOG.md`, `REPRODUCE_unified.md`, `RESEARCH.md`; `mathematics/**`,
  `literature/**`, README разделов) переведены на `archive/record/…`. В каждом файле
  изменены только URL ссылок; текст вне URL побайтно совпадает с базой.
- `manuscript/unified_sections/fixed_map_frontier.tex` — точечная миграция 9 печатных
  GitHub-href на 7 переезжающих файлов F-1 (6 оставшихся href секции указывают на файлы
  F-2 и мигрируют с F-2). Секция генерируется из `mathematics/fixed_map_resolvent_frontier.md`
  (её 9 ссылок мигрированы в источнике; сквозная регенерация на собранном дереве
  воспроизводит ровно эти 9 archive-URL). Полная регенерация в пакет не входила: на
  базовом дереве зафиксирован предсуществующий форматный дрейф генератора (pandoc:
  обёртки hypertarget и переносы дисплейных формул, 1108 строк диффа) — диспозиция фазы 4,
  а `--check` генератора на базе падает до всяких правок пакета.
- **Не мигрирована** единственная ссылка в `mathematics/balanced_pair_schur_reduction.md`
  (на удержанный `schur_reduction_promotion.md` — ссылка остаётся живой, файл на месте).
  Файл является хэш-пинированным научным входом Schur replay (`unchanged_scientific_bindings`
  карты свежести и биндинги replay сверяют его байты с живым деревом); любая его правка
  ломает replay до обновления пинов — см. REPORT §Б.

## Файлы пакета (старый путь → новый путь → git blob SHA → байты)

| Старый путь | Новый путь | git blob SHA | Байты |
|---|---|---|---|

| `record/abel_window_research_20260922.md` | `archive/record/abel_window_research_20260922.md` | `26d9eef0cd48449d90b8d2009c72bf168bedb0f5` | 11547 |
| `record/actual_commutant_bibliographic_impact_20261006.json` | `archive/record/actual_commutant_bibliographic_impact_20261006.json` | `fc9d968147140281b8b0010dd7a69d1cfd5fcea3` | 4034 |
| `record/all_order_program_20261005.md` | `archive/record/all_order_program_20261005.md` | `b87aace0ec460048d88958aa94bdd4bec7c2171d` | 6996 |
| `record/aperture_minimax_review.md` | `archive/record/aperture_minimax_review.md` | `d02280aa258f9688ebd4337ef7d2602de714d23a` | 3314 |
| `record/bgs_program_20260925.md` | `archive/record/bgs_program_20260925.md` | `5b00e729235bf4d99f67320aaad4e4d807d0a9f7` | 7799 |
| `record/bibliographic_impact_20261020.json` | `archive/record/bibliographic_impact_20261020.json` | `5ae68a8721f016763b8ebda58ea61d80a6d33a35` | 8263 |
| `record/bibliographic_impact_feedback_20261013.json` | `archive/record/bibliographic_impact_feedback_20261013.json` | `258bfe25c4c2df6145474c46f87e48c725b15a41` | 1144 |
| `record/bibliographic_impact_green_20261013.json` | `archive/record/bibliographic_impact_green_20261013.json` | `dcefe32c261f79cb8ef3b17c45e1f43cf4d0b838` | 558 |
| `record/bibliographic_impact_haar_20261012.json` | `archive/record/bibliographic_impact_haar_20261012.json` | `41424b541697696eee54e70449c15af96d996bed` | 1224 |
| `record/bibliographic_impact_review_20261006.md` | `archive/record/bibliographic_impact_review_20261006.md` | `ff4c14b2c0d901f1dbd931181a3c86916267d2b1` | 4352 |
| `record/bibliographic_impact_variance_20261013.json` | `archive/record/bibliographic_impact_variance_20261013.json` | `79cf12a13dfd67fbaf7c3f41cf70f1e1d14acbce` | 517 |
| `record/bosonic_information_claims_20260907.md` | `archive/record/bosonic_information_claims_20260907.md` | `042bc541301960699b0a37be69adf186c08b5ccf` | 2252 |
| `record/cavity_continuation_20261011.md` | `archive/record/cavity_continuation_20261011.md` | `de19403a7afa9e3fed5438294f87425f123c0d5f` | 8621 |
| `record/cayley_trace_review_20260909.md` | `archive/record/cayley_trace_review_20260909.md` | `bb89d0b51a1f6082b56636cbbfa0563a458baecc` | 7152 |
| `record/charge_replay_loader_repair_map.json` | `archive/record/charge_replay_loader_repair_map.json` | `909598f1eac17a6b4d7d38cb029bbe2df117f62e` | 1202 |
| `record/checked_checkpoint_acceptance_20261007.md` | `archive/record/checked_checkpoint_acceptance_20261007.md` | `e2155cc73a757fab82ee876982f7504bed0247b3` | 2176 |
| `record/checked_checkpoint_postrun_delta.json` | `archive/record/checked_checkpoint_postrun_delta.json` | `52c7bd7234d6bfc64da303e52afffac8f6ce7558` | 8002 |
| `record/checkpoint_ci_artifact_routing.json` | `archive/record/checkpoint_ci_artifact_routing.json` | `9179fd2fba3f2ee1004b7c8fefe7bb204a5e8066` | 546 |
| `record/claim_ledger_addendum_20260907.md` | `archive/record/claim_ledger_addendum_20260907.md` | `1f10ffd6ebe051c7f70888bbc197ef673665bc7d` | 12339 |
| `record/clock_universality_continuation_20261011.md` | `archive/record/clock_universality_continuation_20261011.md` | `bee5156db55bdbeb84e9e8c8f3f701e9400233d8` | 3713 |
| `record/coboundary_continuation_20260905.md` | `archive/record/coboundary_continuation_20260905.md` | `0aa4c95ffd950d8f55d1b0bf12da5b1ee1c14888` | 6792 |
| `record/coboundary_joint_review_20260930.md` | `archive/record/coboundary_joint_review_20260930.md` | `f46330becefea88cb94a79254286afb76a168956` | 7771 |
| `record/coboundary_mobius_review_20260929.md` | `archive/record/coboundary_mobius_review_20260929.md` | `3280385bd2944173e4b8788290a0324bfcccf43c` | 6997 |
| `record/coherent_first_return_continuation_20261014.md` | `archive/record/coherent_first_return_continuation_20261014.md` | `067796c32220f95a69dcbe75c94d75625ad6f764` | 1721 |
| `record/cohesive_bibliographic_impact_20261006.json` | `archive/record/cohesive_bibliographic_impact_20261006.json` | `82c13444e587d17621c73a0123558e3e9263a70f` | 4868 |
| `record/cohesive_integration_20261006.md` | `archive/record/cohesive_integration_20261006.md` | `13361f0f0a96fb86768469b6df65f9d84ca4c350` | 1706 |
| `record/cohesive_integration_delta.json` | `archive/record/cohesive_integration_delta.json` | `a5df809f3c87a44838f612d821962f7ca3aa48b5` | 5952 |
| `record/cohesive_postrun_evidence_delta.json` | `archive/record/cohesive_postrun_evidence_delta.json` | `238ab6cf2bcf472c8f2b5856c17d0752d68b3b3d` | 4800 |
| `record/collective_cat_bibliographic_impact.json` | `archive/record/collective_cat_bibliographic_impact.json` | `35ab54b7dbd85d9f12cc6c2c33c69ebf62e9d22b` | 3534 |
| `record/collective_cat_integration_20261006.md` | `archive/record/collective_cat_integration_20261006.md` | `e05229ceacb33690287ebe0a0610d36929b452c6` | 1659 |
| `record/collective_cat_integration_delta.json` | `archive/record/collective_cat_integration_delta.json` | `8d5e4aba9b22051796067faacb0eb1e9ccef175e` | 5992 |
| `record/collective_cat_postrun_evidence_delta.json` | `archive/record/collective_cat_postrun_evidence_delta.json` | `cf415494c01f02483421b0bc88934c15d61e0044` | 5249 |
| `record/collective_diffusion_program_20261006.md` | `archive/record/collective_diffusion_program_20261006.md` | `e74a1311b913d645c5884b43a2a52fedfafd5b82` | 5421 |
| `record/combined_wave3_v4_acceptance_20261007.md` | `archive/record/combined_wave3_v4_acceptance_20261007.md` | `23af28327a360102233c297c6ea142939fdbe55a` | 1073 |
| `record/constructive_batch_integration_20261006.md` | `archive/record/constructive_batch_integration_20261006.md` | `b3a59865e32ac54b2e2a9cc464d67968809d26f0` | 4004 |
| `record/constructive_bibliographic_impact_20261006.json` | `archive/record/constructive_bibliographic_impact_20261006.json` | `a84434d58f92827b893025f722f123c57bebcc86` | 491 |
| `record/constructive_manuscript_typesetting_delta_20261006.json` | `archive/record/constructive_manuscript_typesetting_delta_20261006.json` | `50af1865dfa7e7bc520cb531a54e74e86e1e6650` | 1862 |
| `record/continuation_review_20260906.md` | `archive/record/continuation_review_20260906.md` | `4cc3dfae4e9aa4196dee8f431acd3e8d9e3e0bf1` | 6295 |
| `record/corpus_revision_20261006.md` | `archive/record/corpus_revision_20261006.md` | `9ad3b0c509707f5c34786c8656acfc980c8f7f9c` | 12721 |
| `record/critical_noise_program_20261005.md` | `archive/record/critical_noise_program_20261005.md` | `3bbc39d0c5ac2c4ea439788737e00ec84f7cd586` | 8439 |
| `record/cue_upload_review_20260927.md` | `archive/record/cue_upload_review_20260927.md` | `40ebb9372a1023d117579657d1a8d5cdfdfc0621` | 14540 |
| `record/entry_flatness_route_20261011.md` | `archive/record/entry_flatness_route_20261011.md` | `4a26b3eb532ebdaf33083dc12329e9cb15c5bd1f` | 3493 |
| `record/expansion_wavepacket_review_20261004.md` | `archive/record/expansion_wavepacket_review_20261004.md` | `54a7d526cb163cb64ea62bc9653ca2aa3b4d58ad` | 5290 |
| `record/factorial_intermediate_bibliographic_impact.json` | `archive/record/factorial_intermediate_bibliographic_impact.json` | `6cad725fa2169f506ee1960d883d3b0614582b83` | 7171 |
| `record/factorial_intermediate_integration_20261007.md` | `archive/record/factorial_intermediate_integration_20261007.md` | `7c578b23bb82785446c531b09e7c2afdd1b11461` | 2039 |
| `record/factorial_intermediate_integration_delta.json` | `archive/record/factorial_intermediate_integration_delta.json` | `13d0d4b307cd736fc63781d637f6225d12138818` | 6429 |
| `record/factorial_intermediate_postrun_evidence_delta.json` | `archive/record/factorial_intermediate_postrun_evidence_delta.json` | `848260ee1616346d56035545102c1ad9219ab739` | 5419 |
| `record/feedback_flatness_continuation_20261013.md` | `archive/record/feedback_flatness_continuation_20261013.md` | `c7325a7503cec4f580e668f888c16be75e0bc7d1` | 2851 |
| `record/final_manuscript_build_20260906.json` | `archive/record/final_manuscript_build_20260906.json` | `f1b5d7c2bca10ca375295235396dd24df252649d` | 2217 |
| `record/final_verification_followup_20260906.json` | `archive/record/final_verification_followup_20260906.json` | `d7bd533960885d092ec6684e02ce5f3d30a1eeb9` | 2539 |
| `record/finite_orbit_proof_audit_20260922.md` | `archive/record/finite_orbit_proof_audit_20260922.md` | `dde4a1ebeeb218c20361024694efef117e30cac7` | 6524 |
| `record/finite_orbit_secondary_review_20260922.md` | `archive/record/finite_orbit_secondary_review_20260922.md` | `6d2c308329564effaefbaeb2468315fedcb62f1c` | 13667 |
| `record/first_seven_bibliographic_impact_20261006.json` | `archive/record/first_seven_bibliographic_impact_20261006.json` | `4e0cfc54e00a366f9f4596a7a4134c615b82cc17` | 2086 |
| `record/first_seven_integration_20261006.md` | `archive/record/first_seven_integration_20261006.md` | `13fe1ff7b6d5ffe182493b9f5a3ccf2f0e23b025` | 3345 |
| `record/first_seven_integration_delta.json` | `archive/record/first_seven_integration_delta.json` | `9aebfb8c9f1fb4b4d870025a834e10ae82e12e6d` | 5164 |
| `record/first_seven_postrun_evidence_delta.json` | `archive/record/first_seven_postrun_evidence_delta.json` | `6077737eb301b0da3d03b153d55b9b9d622f87dc` | 5537 |
| `record/fixed_map_attachment_audit_20260916.md` | `archive/record/fixed_map_attachment_audit_20260916.md` | `28010147f48ddfae0f91df65841030381f81ae27` | 12513 |
| `record/fixed_map_publication_20260920.md` | `archive/record/fixed_map_publication_20260920.md` | `22a38e45895a39a70e295ffe53efee4104d66e89` | 5386 |
| `record/fixed_strength_locality_audit.md` | `archive/record/fixed_strength_locality_audit.md` | `244055216b74949fddaefbf883df623a8ec0392b` | 5800 |
| `record/floquet_continuation_20260905.md` | `archive/record/floquet_continuation_20260905.md` | `e5a2c2078d123b82355c0d339d1055f99b4fbd77` | 6280 |
| `record/floquet_validation_corrections.md` | `archive/record/floquet_validation_corrections.md` | `eae53286432543b72ccc21d1757b90b817a48a61` | 2223 |
| `record/folded_quadratic_audit_20261004.md` | `archive/record/folded_quadratic_audit_20261004.md` | `d6b0ce5e2ceb5d3f1c07be928552ee157ed6f42a` | 6345 |
| `record/folded_quadratic_review_20261001.md` | `archive/record/folded_quadratic_review_20261001.md` | `46caaf3992a36f6485aaa203bbcbf950085a9969` | 4839 |
| `record/fourth_delay_continuation_20261011.md` | `archive/record/fourth_delay_continuation_20261011.md` | `bd73aeef39876dbb622f900f165b7ab828e7c798` | 3030 |
| `record/fractional_hamming_claim_contract.json` | `archive/record/fractional_hamming_claim_contract.json` | `86417bf1e24616c8d152bf35e4867ea2e6257797` | 2172 |
| `record/fractional_hamming_execution_partition.json` | `archive/record/fractional_hamming_execution_partition.json` | `3ad8766e32cfad3d32502a04472d2a863815cb1c` | 893 |
| `record/fractional_hamming_path_relocation.json` | `archive/record/fractional_hamming_path_relocation.json` | `9df5aa219f7ae90757e87edea4d99c5c0bd39f50` | 1975 |
| `record/fractional_hamming_promotion.md` | `archive/record/fractional_hamming_promotion.md` | `ddd05938477c5df73824078290eae003f8bc99d2` | 3844 |
| `record/fractional_hamming_provenance_repair_20261007.json` | `archive/record/fractional_hamming_provenance_repair_20261007.json` | `d500b845d5c2cf52aa968ef649d5ebf1c2c832bb` | 8977 |
| `record/fractional_hamming_provenance_repair_20261007.md` | `archive/record/fractional_hamming_provenance_repair_20261007.md` | `67a8d8388ab6df596cd65d6110eb4df7abbb34a6` | 2144 |
| `record/fractional_hamming_public_receipt_mapping.json` | `archive/record/fractional_hamming_public_receipt_mapping.json` | `88e484f3ed8967d825f1733428b028f1c1094480` | 2496 |
| `record/frontier_pass_20260904.md` | `archive/record/frontier_pass_20260904.md` | `0ff8b14fa5538fb4aadc82f70ccecc2714acd3e8` | 6970 |
| `record/frontier_pass_20260905.md` | `archive/record/frontier_pass_20260905.md` | `e1f79e7efd00ce8e36ee282f7d032daa4757f0e6` | 10638 |
| `record/frozen_antireversor_review_20260924.md` | `archive/record/frozen_antireversor_review_20260924.md` | `b137dc290a04822a004dbd78100cf7523e7dec09` | 1935 |
| `record/frozen_full_lag_review_20260923.md` | `archive/record/frozen_full_lag_review_20260923.md` | `8104eb05ac15344781c0e7b8dabfe29019a468d4` | 7855 |
| `record/frozen_operator_transfer_program_20261006.md` | `archive/record/frozen_operator_transfer_program_20261006.md` | `75bd9931cc416860a9d5670b28309ace22953ad6` | 5600 |
| `record/frozen_seven_cut_review_20260924.md` | `archive/record/frozen_seven_cut_review_20260924.md` | `4b11385a21ecbc791c35d7890de18ee625d84aed` | 2683 |
| `record/general_hyperbolic_continuation_20260905.md` | `archive/record/general_hyperbolic_continuation_20260905.md` | `2841c568db97be4b4e452f0d541c5c88dc4ea47c` | 5371 |
| `record/general_start_review_20261004.md` | `archive/record/general_start_review_20261004.md` | `acb384ee5f0ebfd5a2a73f2989a6878f9b51536a` | 14488 |
| `record/global_rotated_box_bibliographic_impact_20261006.json` | `archive/record/global_rotated_box_bibliographic_impact_20261006.json` | `1b0586d3134289a486cbc0210d9d29c677263550` | 1680 |
| `record/global_rotated_box_order_clarification.json` | `archive/record/global_rotated_box_order_clarification.json` | `bed704129fec5faece431521a5f356df8086ce05` | 762 |
| `record/global_rotated_box_source_mapping.json` | `archive/record/global_rotated_box_source_mapping.json` | `c7c07186073212c90f76c979b2022b6e9a9ef038` | 2243 |
| `record/green_compression_continuation_20261013.md` | `archive/record/green_compression_continuation_20261013.md` | `4597cf82ee1e152a31a447c5153b1752870b8586` | 2055 |
| `record/growing_degree_program_20261005.md` | `archive/record/growing_degree_program_20261005.md` | `c94525b343d36e2701d8b7e959380c27b641701f` | 10280 |
| `record/haar_feedback_continuation_20261012.md` | `archive/record/haar_feedback_continuation_20261012.md` | `43d0b40fe84ee4de0e6ac11464a9fdf65720618b` | 3268 |
| `record/heisenberg_pair_program_20261005.md` | `archive/record/heisenberg_pair_program_20261005.md` | `94f5a2364a79b1bf32ffff2d1b0b3e1f74719c59` | 9591 |
| `record/heisenberg_wkb_editorial_mapping.json` | `archive/record/heisenberg_wkb_editorial_mapping.json` | `d4e5f4c433d7dcba9b1e330d061daf0f86f9839a` | 33990 |
| `record/holomorphic_shell_review.md` | `archive/record/holomorphic_shell_review.md` | `94ca45268a2f029c3b827e77d8cc4fd18c89cc88` | 4416 |
| `record/homoclinic_promotion_mapping.json` | `archive/record/homoclinic_promotion_mapping.json` | `0bd3e315fbc9b6eba48bb42438cebbe36b337d2e` | 2395 |
| `record/homoclinic_review.md` | `archive/record/homoclinic_review.md` | `e9050ea7042afa0fa5291de50db512dc36d3e640` | 19883 |
| `record/husimi_shell_review.md` | `archive/record/husimi_shell_review.md` | `7065e43be1c2907ee9f4b698e6f28dd13ee56bc4` | 4691 |
| `record/integration_20260922.md` | `archive/record/integration_20260922.md` | `9cbe6cbee067959d6344970b38281d78b55e5ee5` | 6258 |
| `record/integration_20260923.md` | `archive/record/integration_20260923.md` | `67dac3eb3c62b70c45d108b65431a29ff6e38036` | 4207 |
| `record/intermediate_ci_portability_repair_20261007.md` | `archive/record/intermediate_ci_portability_repair_20261007.md` | `c2f88dc42a46afc09ff128e28e7f5bfd8ed3dc0e` | 1859 |
| `record/inventory_snapshot.py` | `archive/record/inventory_snapshot.py` | `d0ad93063866213d2694d95c171c616750fdbc4f` | 2447 |
| `record/julia_migration.md` | `archive/record/julia_migration.md` | `d596daabad5528bfd134e19e3aba89380e5e1e27` | 5882 |
| `record/locality_delivery_status_20260905.md` | `archive/record/locality_delivery_status_20260905.md` | `010972bf46be429347a016f9a0d5a37d7350a2ff` | 3404 |
| `record/locality_packet_executed_20260905.md` | `archive/record/locality_packet_executed_20260905.md` | `7d2ce4f2d4b9cc3f292761bade0085fe01f57f76` | 5287 |
| `record/microscopic_rounding_review.md` | `archive/record/microscopic_rounding_review.md` | `9934cb30be3412bc1406029fe7fe7984cd1034fb` | 3822 |
| `record/next_proofs_integration_20261006.md` | `archive/record/next_proofs_integration_20261006.md` | `c4d5879f45587fe02b6ac6a4937a1399d74037cf` | 3577 |
| `record/odd_newest_promotion_map.json` | `archive/record/odd_newest_promotion_map.json` | `1e0070ef57f0114b3735012846e522e32ef08e1e` | 2519 |
| `record/original_channel_gap_program_20261006.md` | `archive/record/original_channel_gap_program_20261006.md` | `afb90482eee239cfba295dfa84d681c8d694f481` | 2906 |
| `record/paired_higher_integration_20261006.md` | `archive/record/paired_higher_integration_20261006.md` | `7903a583d78884b3478e251ba010d9ed255a779d` | 2086 |
| `record/paired_higher_integration_delta.json` | `archive/record/paired_higher_integration_delta.json` | `5f5ec46e30bfd89b594ba4626be7777d68374888` | 3515 |
| `record/paired_higher_postrun_evidence_delta.json` | `archive/record/paired_higher_postrun_evidence_delta.json` | `c67d6dc0e5bf11ec91d85ccdda27cd849cbbdd40` | 5209 |
| `record/paired_phase_display_formatting.json` | `archive/record/paired_phase_display_formatting.json` | `4f67b702cf0cd92c0417f24a760ff7fcab05bde8` | 370 |
| `record/pell_harmonic_returns_review_20260910.md` | `archive/record/pell_harmonic_returns_review_20260910.md` | `3706846bf91fe0ca2801ad0f34868fe492fc9a23` | 7090 |
| `record/pell_harmonic_transition_review_20260909.md` | `archive/record/pell_harmonic_transition_review_20260909.md` | `d444756cef548c38aedef67369dc87cf33d5bd9c` | 7736 |
| `record/phase_checkpoint_bibliographic_impact.json` | `archive/record/phase_checkpoint_bibliographic_impact.json` | `f4575ac9673b79de93cb523a53d3e333ca4cb101` | 3513 |
| `record/polar_wkb_angle_normalization.json` | `archive/record/polar_wkb_angle_normalization.json` | `6d8c78a5ad886b1150b197ec929b6ccc0d7f033f` | 799 |
| `record/polar_wkb_bibliographic_impact_20261006.json` | `archive/record/polar_wkb_bibliographic_impact_20261006.json` | `622e2a755ffa5b9a7f065ba5badf024be15031e0` | 3018 |
| `record/polar_wkb_integration_check.json` | `archive/record/polar_wkb_integration_check.json` | `de9c15680687fd0a7b8f446866e3df4a48820109` | 1538 |
| `record/polar_wkb_review.md` | `archive/record/polar_wkb_review.md` | `4d6373e25a6dd82faa956220e5a3e53fcbf509ab` | 8163 |
| `record/polynomial_coboundary_review_20261004.md` | `archive/record/polynomial_coboundary_review_20261004.md` | `39aefc67403886d6f0fdf4eb88b6ac64bf6aff99` | 11904 |
| `record/prime_resonant_review_20260930.md` | `archive/record/prime_resonant_review_20260930.md` | `06c3f014b1b1ac02165046d634cb6d6f8bdd2b32` | 7168 |
| `record/pure_loss_discrimination_review_20260907.md` | `archive/record/pure_loss_discrimination_review_20260907.md` | `c94b819ac03e1c67a84b68e54b0909f84bc1dee5` | 2020 |
| `record/quadratic_noise_program_20260928.md` | `archive/record/quadratic_noise_program_20260928.md` | `8cb8633034658c5b0f5829b21c82860bbac887f5` | 8418 |
| `record/quadratic_noise_review_20260929.md` | `archive/record/quadratic_noise_review_20260929.md` | `6be888f0e5ace75f9258cdd6354eb158863297d9` | 7207 |
| `record/r6_checked_checkpoint_import.json` | `archive/record/r6_checked_checkpoint_import.json` | `015a6506b7308b6f032caaf8b8d270986d5ca9ed` | 64568 |
| `record/r6_checked_repair_20261007.md` | `archive/record/r6_checked_repair_20261007.md` | `8e3651f75a60742683aaaa8b52deea09662e0725` | 4480 |
| `record/ramified_first_seven_integration_20261006.md` | `archive/record/ramified_first_seven_integration_20261006.md` | `a48cd5a76c3277a54eb6c41690ce514a1c019ac5` | 2693 |
| `record/ramified_first_seven_integration_delta.json` | `archive/record/ramified_first_seven_integration_delta.json` | `42d4db84994b1b3b192bf15324659c5b20d83cc3` | 6195 |
| `record/ramified_first_seven_postrun_evidence_delta.json` | `archive/record/ramified_first_seven_postrun_evidence_delta.json` | `8e3e36f8117ac7cbf90c84e17302133b9e4c4b8a` | 5270 |
| `record/rare_phase_gaussian_review_20260907.md` | `archive/record/rare_phase_gaussian_review_20260907.md` | `bb3f190b78a71317decf9f54345e915190456b1f` | 5318 |
| `record/reconstruction.md` | `archive/record/reconstruction.md` | `fc627f5658e59440f51f8b4784092ba6b617f304` | 3135 |
| `record/recovery_audit_20260920.md` | `archive/record/recovery_audit_20260920.md` | `e9903ff4830f4736b5df0e52c838ec6c4c240a5c` | 8520 |
| `record/referee_audit_20260905.md` | `archive/record/referee_audit_20260905.md` | `b4c3f83939bae0d9a9af476b465f59246eaecce6` | 4316 |
| `record/referee_audit_20260908.md` | `archive/record/referee_audit_20260908.md` | `47de87778500fe026937ad5eaae4e8d2c9e1c8bf` | 8714 |
| `record/remaining_breakthrough_task_20261020.md` | `archive/record/remaining_breakthrough_task_20261020.md` | `1af168db7b93f5fcbf2fcc3a45156ec304d79145` | 8242 |
| `record/repository_reconciliation_20261020.md` | `archive/record/repository_reconciliation_20261020.md` | `c90d13902397ad9b387a0389df679f07c912b47b` | 3829 |
| `record/research_checkpoint_partial_review.json` | `archive/record/research_checkpoint_partial_review.json` | `ff4e150d1a387e8dfc1491c0bb2627539fee0984` | 4263 |
| `record/research_checkpoint_protocol_source_delta.json` | `archive/record/research_checkpoint_protocol_source_delta.json` | `596b65a03c33dee1dae3b167cc0a0181358df8b3` | 3674 |
| `record/research_continuation_20261016.md` | `archive/record/research_continuation_20261016.md` | `abaf932c6de3f271476896919fa2e17148e7e4af` | 14600 |
| `record/research_cycle_20260922.md` | `archive/record/research_cycle_20260922.md` | `91c892b41302856e24f0477ecfdd8044f9774d66` | 3531 |
| `record/research_pass_20260922.md` | `archive/record/research_pass_20260922.md` | `2d58ab21af72e4d2c94731e7f5b9d3d848689536` | 6687 |
| `record/research_pass_20260925.md` | `archive/record/research_pass_20260925.md` | `c14339b01967a566ca1c6a344eaf56bf8e0576ea` | 3289 |
| `record/research_pass_cue_flow_20260925.md` | `archive/record/research_pass_cue_flow_20260925.md` | `9d55bfb8f85f6e907131104f077ce98df9225e36` | 7921 |
| `record/research_routes.md` | `archive/record/research_routes.md` | `2bf97e7d1350bb4d87b5a0bbc6684fafb495fc3c` | 9910 |
| `record/residual_batch_bibliographic_impact.json` | `archive/record/residual_batch_bibliographic_impact.json` | `46d380a4f3255da1114a11362670d65c0c03a114` | 15942 |
| `record/residual_batch_editorial_adjustments.json` | `archive/record/residual_batch_editorial_adjustments.json` | `0d0a8211fc064caba60e9283b1bc578495163444` | 533 |
| `record/residual_batch_integration_20261007.md` | `archive/record/residual_batch_integration_20261007.md` | `41a925b676572c0360f6c79aa89455364875476c` | 3276 |
| `record/residual_batch_overlay_import.json` | `archive/record/residual_batch_overlay_import.json` | `1abe394139df6d7d6b06f8c82abeb1a36ef5d603` | 2815 |
| `record/residual_batch_postrun_evidence_delta.json` | `archive/record/residual_batch_postrun_evidence_delta.json` | `96256531a7b2402fb18651f51136b9f1a8d69a3d` | 10424 |
| `record/residual_batch_source_delta.json` | `archive/record/residual_batch_source_delta.json` | `d8d95cdff59d6522acf4add6ea19c20ebfc9e3e1` | 62620 |
| `record/resonance_continuation_20260905.md` | `archive/record/resonance_continuation_20260905.md` | `bf434bd19b068b4a31861ce5a1a100af6c2f6754` | 5039 |
| `record/resonant_density_review_20261001.md` | `archive/record/resonant_density_review_20261001.md` | `6321d7bf9665191eb52ceb3b8d47865087494f88` | 7510 |
| `record/reversal_channel_continuation_20261011.md` | `archive/record/reversal_channel_continuation_20261011.md` | `05a7c7f5ff2eecd99f39bb3c2d2cdbcf5ce2d0be` | 3669 |
| `record/rigidity_review_20260905.md` | `archive/record/rigidity_review_20260905.md` | `c5933cc49529c4aa29f9e4b2de7fd2d9551b3d4b` | 6693 |
| `record/round5_code_review_20261006.md` | `archive/record/round5_code_review_20261006.md` | `86f5055b4245c644511ba6afc78c3abffa4640d3` | 3620 |
| `record/schur_reduction_source_closure.json` | `archive/record/schur_reduction_source_closure.json` | `76acb8e49505e4b4a8514e254a5c94eaceaf458c` | 6081 |
| `record/schur_replay_freshness_import.json` | `archive/record/schur_replay_freshness_import.json` | `5a3234706c09e7abf5459b17be867aae3fc0ae40` | 8980 |
| `record/session_integrity_audit_20260907.md` | `archive/record/session_integrity_audit_20260907.md` | `e1a4e99fc155f583e49eccd0bd466ef3a9c05542` | 9150 |
| `record/session_publication_transport_20260907.md` | `archive/record/session_publication_transport_20260907.md` | `e1a2fde2b843522e24748d36af4e60897ff384b5` | 751 |
| `record/session_science_sync_20260907.md` | `archive/record/session_science_sync_20260907.md` | `4676847d9e92da3a6b8023f519116236578506a7` | 5731 |
| `record/seven_primary_formal_promotion_map.json` | `archive/record/seven_primary_formal_promotion_map.json` | `bd7c8c4b2976e66f67e9b1bb2a437ad9294579cc` | 552 |
| `record/signed_heisenberg_review_20260930.md` | `archive/record/signed_heisenberg_review_20260930.md` | `3d2ff66f2759770ce6d5eb4e4ea334d2976f7816` | 5367 |
| `record/spectral_coherence_continuation_20261014.md` | `archive/record/spectral_coherence_continuation_20261014.md` | `4ee04e55e8ea2a2660a6176e4858ea12be4ea221` | 3224 |
| `record/submitted_article_review_20260924.md` | `archive/record/submitted_article_review_20260924.md` | `e6a3d5c1fa04d679f64e3cc7121178f0bfe7382f` | 7829 |
| `record/temporal_integration_20260906.md` | `archive/record/temporal_integration_20260906.md` | `6b96be0bea9b089a9788086480c5d858dba2344e` | 2970 |
| `record/toolchain_followup_20261020.md` | `archive/record/toolchain_followup_20261020.md` | `2ae5451a913e1be3a273b2e4d178161a11f01c6a` | 732 |
| `record/two_step_drift_continuation_20261012.md` | `archive/record/two_step_drift_continuation_20261012.md` | `0ec3fe80a571c8d6b118e89bbb4136787815c9bf` | 2515 |
| `record/two_step_variance_continuation_20261013.md` | `archive/record/two_step_variance_continuation_20261013.md` | `8b51b0748c125fc45f9e1f86785fbc5812b93455` | 1316 |
| `record/unitary_two_step_continuation_20261012.md` | `archive/record/unitary_two_step_continuation_20261012.md` | `024e9ae6484a614a759639ffc70fbfac3896caf3` | 2570 |
| `record/wave2_bibliographic_impact.json` | `archive/record/wave2_bibliographic_impact.json` | `8ecaf8291e554b33198b6f916afc7bac6a4e93d0` | 3240 |
| `record/wave2_inherited_replay_compatibility.json` | `archive/record/wave2_inherited_replay_compatibility.json` | `c93eaa014dd45b5de47133564bc989375e3bb337` | 1764 |
| `record/wave3_bibliographic_impact.json` | `archive/record/wave3_bibliographic_impact.json` | `0647eeda6a90971f6db5e3e3057f9f4a4fb68a02` | 3127 |
| `record/wave3_checked_integration_20261007.md` | `archive/record/wave3_checked_integration_20261007.md` | `129a0aa8b77018d18d2a9762bd2eec1bb23cde17` | 3286 |
| `record/wick_poisson_continuation_20261016.md` | `archive/record/wick_poisson_continuation_20261016.md` | `583646598b46474cabe41515b4862f25691c8c2f` | 8741 |
