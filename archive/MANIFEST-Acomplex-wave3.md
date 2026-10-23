# MANIFEST-Acomplex-wave3 — phase 1, package Wave3: `evidence/wave3_checked_20261007` → `archive/evidence/wave3_checked_20261007`

Scope: the maximal safe partial move of the A-complex (design `bindings_track_design.md` §B.6;
executor decision of 23 October 2026: EXECUTE in phase 1). The whole wave3 tree
(43 files, 407 369 bytes, no binaries) moves byte-for-byte; the content of the archival
copies is not edited. Every consuming machine is migrated in the same commit:
wave3 replay source bindings (8 keys renamed, sha values unchanged), wave3 replay
contract (8 path values), wave3 promotion mapping (43 distinct path leaves: 42
`immutable_copies.path` + `v1_claims_artifact`; sha256/bytes pins unchanged), the
dormant wave3 integration audit (3 path literals — its pre-existing failure signature
`earlier theorem contract changed: BGS-CAYLEY-001` is preserved), claims.json
(8 leaves of BGS-TRACE-028/BGS-TRACE-029 — both unsealed wave3 follow-on claims, so
**no epoch amendments and no change to `record/claim_integration_epochs.json`**), and
navigation links in the 2 live source documents. The remaining A-complex trees
(research_checkpoint, wave2_checked, schur) do **not** move in phase 1 (design §B.3/B.7).

## Moved files (43)

| Old path | New path | git blob SHA | SHA-256 | Bytes |
|---|---|---|---|---:|
| `evidence/wave3_checked_20261007/raw/convex_review/audit.md` | `archive/evidence/wave3_checked_20261007/raw/convex_review/audit.md` | `7171be258bb51297db5acc9166a522f2bd647a58` | `1b0940b69fa8dceda6405b4dd8194ab0cb7fdbb8d89777eb2d6f69a8a9819aff` | 18096 |
| `evidence/wave3_checked_20261007/raw/convex_review/author_snapshot/annealed_compact_pinch_stability.md` | `archive/evidence/wave3_checked_20261007/raw/convex_review/author_snapshot/annealed_compact_pinch_stability.md` | `829d400e67a75ddcf26102da4b0385920ad98bf1` | `e28c5dec22270066ff2069c5568bb4ba19040bd20f97873bc11c0140f13507e6` | 10148 |
| `evidence/wave3_checked_20261007/raw/convex_review/author_snapshot/conditional_convex_pinch_resummation.md` | `archive/evidence/wave3_checked_20261007/raw/convex_review/author_snapshot/conditional_convex_pinch_resummation.md` | `9cd7b4913c087820df58a0152c65d2b96db1a55c` | `1a324c8ef0963dded61b84dfde27736e96cd85f55271d2a3d6dcb97ef7a1a0b0` | 16404 |
| `evidence/wave3_checked_20261007/raw/convex_review/author_snapshot/exact_controls.py` | `archive/evidence/wave3_checked_20261007/raw/convex_review/author_snapshot/exact_controls.py` | `fc6147e87c0af9ab1265de379fa16235ec3a7b80` | `4cd6dbfe585b61e33fb15a37c672ecf3eb9a87598dcbcdd828e14a90b65add0a` | 8111 |
| `evidence/wave3_checked_20261007/raw/convex_review/author_snapshot/exact_controls_result.json` | `archive/evidence/wave3_checked_20261007/raw/convex_review/author_snapshot/exact_controls_result.json` | `360925b367299fc7b2e2356a539b974aa1a47b71` | `13c635af35d07502abf4153ca59ef20ef8f5ea2dc659562906f99ef33becfafa` | 705 |
| `evidence/wave3_checked_20261007/raw/convex_review/author_snapshot/source_bindings.json` | `archive/evidence/wave3_checked_20261007/raw/convex_review/author_snapshot/source_bindings.json` | `03bfc702aca0d6442d4343001a3230df06398405` | `ea3cf235498dbb3febcc707b54aee8d3378e81ce423e38bd2e30a021d79096d0` | 1795 |
| `evidence/wave3_checked_20261007/raw/convex_review/independent_bounded_controls.py` | `archive/evidence/wave3_checked_20261007/raw/convex_review/independent_bounded_controls.py` | `b5def97993900fc3a1b994843b6da6e2c955a8df` | `17978210ab3ec005a2b0a4654a1b79f54d3320d996a9c830367e86311aa0acc1` | 3444 |
| `evidence/wave3_checked_20261007/raw/convex_review/independent_bounded_controls_result.json` | `archive/evidence/wave3_checked_20261007/raw/convex_review/independent_bounded_controls_result.json` | `96562b59231464a7741f1f7d82d7b1e7b87e6811` | `3db91588656b681318d0b6f489a3c7d7efd8d27d68280a51b7829b6df2b84df4` | 434 |
| `evidence/wave3_checked_20261007/raw/convex_review/reproduced_exact_controls_stdout.json` | `archive/evidence/wave3_checked_20261007/raw/convex_review/reproduced_exact_controls_stdout.json` | `360925b367299fc7b2e2356a539b974aa1a47b71` | `13c635af35d07502abf4153ca59ef20ef8f5ea2dc659562906f99ef33becfafa` | 705 |
| `evidence/wave3_checked_20261007/raw/convex_review/review_manifest.json` | `archive/evidence/wave3_checked_20261007/raw/convex_review/review_manifest.json` | `fd0b9f53d7058eca9123c526092acbaa26c5afc2` | `fa9461f344c0a3ad95dae11ae6401569ced634ed6dc36c55ed4d66990143a0a0` | 1209 |
| `evidence/wave3_checked_20261007/raw/provenance/wave2_claims_v1.json` | `archive/evidence/wave3_checked_20261007/raw/provenance/wave2_claims_v1.json` | `1e6cb04d2ada73d4018584fad4f3e5cff7faec84` | `c6bd871451ca118e16f4f800422f8d9ffb0ae9ab69ec94177f6c0cfc6942cfe0` | 147502 |
| `evidence/wave3_checked_20261007/raw/right_overlap/accepted_left_controls/check_overlap.py` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/accepted_left_controls/check_overlap.py` | `5783199f3eadfbd3db5f8a0c0b2bf34276218470` | `da8cc8f11f955e26c7c7996e7dca34bf5d5c7ed148866e81b315a3d48e5c313c` | 4858 |
| `evidence/wave3_checked_20261007/raw/right_overlap/accepted_left_controls/checks.json` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/accepted_left_controls/checks.json` | `9febc1de998caaf76d253b0f89edd5712d2c72f5` | `46d9b3899a2fda44e079e953eb4fb2c5f19dc1a0539471bcbaa48bcc832b6da7` | 5905 |
| `evidence/wave3_checked_20261007/raw/right_overlap/accepted_left_controls/checks.rerun.log` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/accepted_left_controls/checks.rerun.log` | `a7e193abdf7891b3116b1341cbfe316cf34b7bdf` | `0f9783b79a79b56fc9304df544c127843072c7d29d13457ec46b4bc6cc212c04` | 326 |
| `evidence/wave3_checked_20261007/raw/right_overlap/accepted_left_controls/checks_optimized.json` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/accepted_left_controls/checks_optimized.json` | `e9d8754417fc7eec5e57fd63869400501eade338` | `e8eabaa8965d4249ed578c44b6b9827ef66e76eda778e4f1884c82b85935644c` | 5905 |
| `evidence/wave3_checked_20261007/raw/right_overlap/accepted_left_controls/checks_optimized.rerun.log` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/accepted_left_controls/checks_optimized.rerun.log` | `7bb02e76b6d6203bb4a57c830ad50430daa19844` | `b85bda067e2e50efeb22c944f3aa16bba3f1ffa4d27964c44e50d4e81bb63b44` | 326 |
| `evidence/wave3_checked_20261007/raw/right_overlap/accepted_left_controls/normal.log` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/accepted_left_controls/normal.log` | `98641c8c2084de1b141e01ba3f33dc0904db6ded` | `3040f2237735b0591df78a8af37e010ddfd392557fb3e82b3f54d224f8d5fa39` | 326 |
| `evidence/wave3_checked_20261007/raw/right_overlap/accepted_left_controls/optimized.log` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/accepted_left_controls/optimized.log` | `4f86c6d248d7f9a8257a029d1a4fab1a701a934e` | `e91a888cf8a68498c7411f7737c44f9169039786aee39d979208899c7e785f69` | 326 |
| `evidence/wave3_checked_20261007/raw/right_overlap/authorized_exports/RIGHT_FRAME_HANDOFF.md` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/authorized_exports/RIGHT_FRAME_HANDOFF.md` | `6d0909ca808ff09c9f6cdb06adb0bed4603c0c94` | `416d7e114ad7319b35effddad0a42d27ab5e0abbe16b8a58d3f350035c09358f` | 4697 |
| `evidence/wave3_checked_20261007/raw/right_overlap/authorized_exports/right_overlap_and_unmasked_insertions.md` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/authorized_exports/right_overlap_and_unmasked_insertions.md` | `915f0e19be772ee840a0f3ec2e3fa4775fdc1095` | `4c149ab775835c42f4bdb537c558252bf8e129c4b359ef30f6fe1a8578ed8f3e` | 18848 |
| `evidence/wave3_checked_20261007/raw/right_overlap/authorized_exports/self_audit.md` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/authorized_exports/self_audit.md` | `f8521188053a673571118cb04cbd266440377ce1` | `e15de2140749e3d33639b425dcae18332746c29f29feb9c8c15478a5a12cd0b0` | 5469 |
| `evidence/wave3_checked_20261007/raw/right_overlap/authorized_exports/transpose_reduction.md` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/authorized_exports/transpose_reduction.md` | `83dec5e2b8d7e0526011bd34e9e2320159b5ff0f` | `83425306c15e3b7b69626ccd53c46c8c077bfa13078d6314961fe6f95b61ee30` | 5187 |
| `evidence/wave3_checked_20261007/raw/right_overlap/broad_scope_review.md` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/broad_scope_review.md` | `32a8b7c8de80ee83c433fab3d0000d4266d6e9db` | `3e5827718a02e66fbd17ce67fd2c5dbc63002e57cf0429360683038cedf7b83e` | 17040 |
| `evidence/wave3_checked_20261007/raw/right_overlap/check_separated_independent.py` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/check_separated_independent.py` | `23f38271c0efac491e431ea22270815d9996eef1` | `bd1afc7b262d22edc22cdfc2ab89378ae0a50fad29b0c232d628aa865ed85a39` | 4821 |
| `evidence/wave3_checked_20261007/raw/right_overlap/check_transpose.py` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/check_transpose.py` | `796a2cd247b3b2ada0f41e5c4d9e959390b992fd` | `ccb43714478a9183410692da53154805992a4dd06322159ecac4183f28f6f358` | 4860 |
| `evidence/wave3_checked_20261007/raw/right_overlap/computation_manifest.json` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/computation_manifest.json` | `98548fe2affc753ee5d4242c7411f6cf00a3d9e9` | `96082889a9dbc1cadabd6aa8321c2c7d8fe10b7c8f44e153b26f061f14f5eefc` | 7492 |
| `evidence/wave3_checked_20261007/raw/right_overlap/independent_review.md` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/independent_review.md` | `4397a7515bf71ed0ba81ba7ebf164aa324edd353` | `69f5dca32dc46b93bd021e73f072234e05a53f363f726b11c425c7079d626e66` | 30694 |
| `evidence/wave3_checked_20261007/raw/right_overlap/review_receipt.json` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/review_receipt.json` | `07c8b36626744d192fdd6e5ab23e68be0378a7bf` | `d42c276b517d1d8523a25e04476bdd73af593bc6959c6a40cb156033d6d608c8` | 6341 |
| `evidence/wave3_checked_20261007/raw/right_overlap/run_controls.py` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/run_controls.py` | `bea3306d6f957e2840793c819a042b538a22f741` | `e7f08a5b1621149c8cc3b7f2be2f535871e8788909d080cb04ad7f3812ee0404` | 4504 |
| `evidence/wave3_checked_20261007/raw/right_overlap/separated_checks.json` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/separated_checks.json` | `448d44c8b2aa877a5b6f03a9f9083d510986fee9` | `1f6422b91f3532f084cab0567a1f4f2a752ecfe646244f6237078a8c156c39fd` | 10123 |
| `evidence/wave3_checked_20261007/raw/right_overlap/separated_checks.rerun.log` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/separated_checks.rerun.log` | `461bf0f4bddd4c8bfa6c54b197519b0ee27b5ba5` | `40882f804e11ef00dd3fdf115114f8cf3ed93bab867ce8216027bb7773ddd8c6` | 310 |
| `evidence/wave3_checked_20261007/raw/right_overlap/separated_checks_optimized.json` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/separated_checks_optimized.json` | `0349336c20871194d3a2508ee745423667d14bbd` | `8fd747d24e9ee40d1f7bb145c27cb1abf3a10e2fc4e8e0bfb19150f24ac8473c` | 10123 |
| `evidence/wave3_checked_20261007/raw/right_overlap/separated_checks_optimized.rerun.log` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/separated_checks_optimized.rerun.log` | `33a310e73c858239f8763cd077f7ae5ab7b20cab` | `13db05fa1d2a7b97767234804b391d7b37baa389b2661c20f1cd3c5cf33a07cf` | 310 |
| `evidence/wave3_checked_20261007/raw/right_overlap/separated_normal.log` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/separated_normal.log` | `4d7e046b3d03705c6236f19ee095493936221492` | `3fd12faccb5d54d957649e0367685c49ffe4072b6d2d31a8a364e83e0314aecf` | 310 |
| `evidence/wave3_checked_20261007/raw/right_overlap/separated_optimized.log` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/separated_optimized.log` | `be1998a24f413ca0dd9374d4ecd88409d496891f` | `e8fd35d663dece00cbc068dab82c4b7a0dd3d14f2f536e68f9e718c0a3fc0b00` | 310 |
| `evidence/wave3_checked_20261007/raw/right_overlap/transpose_checks.json` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/transpose_checks.json` | `7a9d3ea72d33d0ad51caa251e7876ce1b4d3d188` | `72e86c793201c8b3d307442421f3d5a5f4140bd73138c6bafa910ce723b13a34` | 7261 |
| `evidence/wave3_checked_20261007/raw/right_overlap/transpose_checks.rerun.log` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/transpose_checks.rerun.log` | `a41628a4c54553372c030dffc2f62c52a2dee9f8` | `cbf6a35e28a529d689f45b4e178a65851027aade85421af2885dfbdcc9a49c4c` | 341 |
| `evidence/wave3_checked_20261007/raw/right_overlap/transpose_checks_optimized.json` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/transpose_checks_optimized.json` | `fb1e181f41d420c2f857a303c0d35a4007f8ca0b` | `0c969345deacdfb7b006504dae1b04e91b4c426dbeb0377709a97aedf1ebf384` | 7261 |
| `evidence/wave3_checked_20261007/raw/right_overlap/transpose_checks_optimized.rerun.log` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/transpose_checks_optimized.rerun.log` | `fc000000e77bd26d795fc0869955b4a03b781f42` | `b18081a58d384dfc91fdc360baf867f538638968d7ca9edb9b6c28797e4a4ed2` | 341 |
| `evidence/wave3_checked_20261007/raw/right_overlap/transpose_normal.log` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/transpose_normal.log` | `e8badac148c6ba103086122b3ca977c266066f2d` | `f11f35076419d33a38c82cbf8b2e2bde91ba0796fe2871c651b9cc77a7fd242f` | 342 |
| `evidence/wave3_checked_20261007/raw/right_overlap/transpose_optimized.log` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/transpose_optimized.log` | `8f4eecdb0bff66d3e30a3d3156ad0cdf0fb0715d` | `a2f90973c2a87d0d44fcfdba4f42b033e196c031de7a924f5864c9d70576eda0` | 341 |
| `evidence/wave3_checked_20261007/raw/right_overlap/transpose_pre_export_review.md` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/transpose_pre_export_review.md` | `97ce3d245c3dd554925b67a8c3ee00a93ac666b3` | `dc2f909feb296eb8d2b1099536848e2c821779e67185e51ab1be5e41135318e9` | 13620 |
| `evidence/wave3_checked_20261007/raw/right_overlap/validate_manifest.py` | `archive/evidence/wave3_checked_20261007/raw/right_overlap/validate_manifest.py` | `5e08ef1a294223692f2d1999ae95b092d549bdfa` | `4f94cc4dea9689b0547ff7efa608d52cfd951e2db76c5d9227f4706fa2205c16` | 19898 |

## Same-commit migrations

- `record/wave3_replay_source_bindings.json`: 8 tree keys renamed to the archive prefix; their sha256 pin values unchanged; the 2 code keys and the contract key not renamed. One pin value rotates by necessity: the contract key's sha256, because the contract file's own bytes change in this commit (its 8 path values) — `36922db684054a0ac061778231dcfad377752690bbd2e6b0d8a57e85e75e8b68` → `191fa45e497d1c422b5528d048fd72977eaa8e39caad7c0ca434adad37af3af2`, the package-E / Map pattern for a map pinning a file the package itself edits. Without the rotation the wave3 replay fails source authentication on the contract.
- `record/wave3_replay_contract.json`: 8 path values (4 `source` + 4 `expected`) re-pointed; declared check counts [72, 227, 1486, 8708] unchanged.
- `record/wave3_promotion_mapping.json`: 42 `immutable_copies.path` + `v1_claims_artifact` re-pointed; every sha256/bytes pin unchanged and re-verified against the moved bytes.
- `computations/verification/wave3_integration_audit.py`: 3 path literals (right_overlap root, convex_review root, rglob root) re-pointed; logic untouched.
- `record/claims.json`: 8 leaves (BGS-TRACE-028: proof_dependencies ×2, evidence ×2; BGS-TRACE-029: proof_dependencies ×2, evidence ×2) re-pointed. Epoch file byte-identical.
- `mathematics/convex_pinch_weak_noise_and_deconvolution.md`: 4 links; `mathematics/right_frame_unmasked_pinch_hierarchy.md`: 2 links re-pointed (`../archive/evidence/…`).

## Recorded residual

The promotion mapping's embedded `cards` (promotion-time copies of the TRACE-028/029 claim cards)
contain 8 path strings duplicating the claims.json leaves; per the design's enumeration (§B.6 item 3:
42 `immutable_copies.path` + `v1_claims_artifact` = 43 distinct paths) they are **not** edited:
the cards are the frozen promotion record, no live consumer reads their path strings
(wave3 audit reads card `id`/`source` only; wave2 audit reads only the card ID set), and all 8
paths are within the 42 immutable copies whose `path` fields this package does migrate.
They resolve via this manifest. Frozen carriers elsewhere (archived workspace captures under
`archive/evidence/executions/…` and `archive/evidence/combined_wave3_v4_acceptance_20261007/…`)
likewise retain the old prefix as historical content, per the frozen-carrier doctrine.

