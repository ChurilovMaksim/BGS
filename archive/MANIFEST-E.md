# Archive manifest — package E: record/*_originals + research_checkpoint_seals → archive/record/…

Source tree: the post-package-C tree, corresponding to main @ `2401f0f` for this
area (for `formalization/` and `.github/workflows/ci.yml` the tree may differ from
that commit; neither references this package). All 30 files of the five directories
`record/fractional_hamming_provenance_repair_originals/`,
`record/research_checkpoint_protocol_originals/`,
`record/research_checkpoint_seals/`,
`record/charge_replay_loader_originals/` and
`record/schur_replay_freshness_originals/` move byte-for-byte;
the blob SHA below is the git blob of the file at its old path.

Links from `record/claims.json` to the moved trees: **0** (verified). No live
navigation links to this package exist anywhere in the tree.

**The package's single accompanying edit:** `record/schur_replay_freshness_repair_map.json`
stays in place, but its two `maintained_wrapper_deltas[].historical_copy` values are
repointed to the new prefix `archive/record/schur_replay_freshness_originals/…`.
This edit is load-bearing: the CI chain `unittest discover →
test_schur_replay_freshness.py` reads both originals through the map and checks
them against the map's (unchanged) sha256 pins. Map sha256 before the move:
`9b6d29ad80c8fae151d2774880eca56b7eddbf723ce5c3968f4aadffd2fb6c6b`;
after the edit: `bbd3184b245f55900f00bf761fb2bfd62ce3760490a2c23a3cac3e0d298189ef`.

**Consequence for the Schur freshness receipt:** `record/schur_replay_freshness_repair_receipt.json`
pins the repair map by `$.repair_map.sha256 = 9b6d29ad…` — that pin now refers to
the *pre-move* map and is thereby a historical record. The receipt has no runtime
consumer (the freshness test reads the map, not the receipt); nothing breaks.
Anyone re-verifying the repair in a later audit must read the receipt together
with this manifest, or the map-hash comparison will show a false mismatch.

**Seals:** the four manifests in `research_checkpoint_seals/` are content-sealed;
their own paths do not occur inside them. Their sha256 pins in
`record/research_checkpoint_import.json` (which stays, unedited, as a frozen
record of the import placement) remain valid by construction:
charge `cc68dc10…`, schur delivery `30b317c6…`, astra corrected `b95f0e55…`,
astra signed boundary `75a5f723…`.

**Note for package A (not an action of this package):** the Schur delivery seal
(and, by the same scheme, the charge seal) contains repository-relative links
into evidence trees that belong to package A
(`evidence/schur_reduction_20261007/**`). When package A moves, those links become
frozen references inside an already-archived seal and are to be resolved through
package A's manifest.

**Unedited references:** 30 further path fields in four frozen record-root JSONs
(`charge_replay_loader_repair_map.json` — 3, `fractional_hamming_provenance_repair_20261007.json` — 13,
`research_checkpoint_import.json` — 4 destinations, `research_checkpoint_protocol_source_delta.json` — 10)
and 518 lines in 23 evidence files (whole-tree manifests and wave acceptance
records) cite the old paths. They are records of a past state of the tree and are
deliberately not edited; **old references resolve through this manifest**
(old path → new path → blob SHA).

| Old path | New path | Blob SHA (git) | Bytes |
|---|---|---|---|
| `record/charge_replay_loader_originals/charge_strengthening_replay.diff` | `archive/record/charge_replay_loader_originals/charge_strengthening_replay.diff` | `52e66bd7db54a29b395947a5e08e7a62fc2cf945` | 2118 |
| `record/charge_replay_loader_originals/charge_strengthening_replay.py` | `archive/record/charge_replay_loader_originals/charge_strengthening_replay.py` | `4c8c50886170a75b8ba50b24c89d4ad53390cd70` | 9610 |
| `record/charge_replay_loader_originals/charge_strengthening_replay_sources.json` | `archive/record/charge_replay_loader_originals/charge_strengthening_replay_sources.json` | `0e9a1ecf26f3eeb2632f18ca0116ffe881dc16b4` | 22116 |
| `record/fractional_hamming_provenance_repair_originals/computations__maintenance__tests__test_replay_artifact_routing.py.original` | `archive/record/fractional_hamming_provenance_repair_originals/computations__maintenance__tests__test_replay_artifact_routing.py.original` | `822817a63a9c09e7c503a86e00f045927615fdc4` | 1855 |
| `record/fractional_hamming_provenance_repair_originals/computations__maintenance__verify_workspace.py.original` | `archive/record/fractional_hamming_provenance_repair_originals/computations__maintenance__verify_workspace.py.original` | `c2643d4f10dc59b22bb4f7c3b62062ace188d6fd` | 22627 |
| `record/fractional_hamming_provenance_repair_originals/computations__verification__fractional_hamming__check_routing.py.original` | `archive/record/fractional_hamming_provenance_repair_originals/computations__verification__fractional_hamming__check_routing.py.original` | `7c60a4b43ad5e0eff235aa23999d3a0c74efd479` | 6599 |
| `record/fractional_hamming_provenance_repair_originals/computations__verification__fractional_hamming__full_replay.py.original` | `archive/record/fractional_hamming_provenance_repair_originals/computations__verification__fractional_hamming__full_replay.py.original` | `e3aad86f5399181577bb8ab38f2c0fdba34d870d` | 12361 |
| `record/fractional_hamming_provenance_repair_originals/computations__verification__fractional_hamming_full_end_2_1.py.original` | `archive/record/fractional_hamming_provenance_repair_originals/computations__verification__fractional_hamming_full_end_2_1.py.original` | `0a400783053ead5f64b3afc1f9189c8263ae3347` | 272 |
| `record/fractional_hamming_provenance_repair_originals/computations__verification__fractional_hamming_full_end_2_2.py.original` | `archive/record/fractional_hamming_provenance_repair_originals/computations__verification__fractional_hamming_full_end_2_2.py.original` | `6097c5b98f27bf4c1e8392a30208aaff8bca58a9` | 272 |
| `record/fractional_hamming_provenance_repair_originals/computations__verification__fractional_hamming_full_end_2_3.py.original` | `archive/record/fractional_hamming_provenance_repair_originals/computations__verification__fractional_hamming_full_end_2_3.py.original` | `5a91a366ca802138e9380c402f7fe2b52fff3850` | 272 |
| `record/fractional_hamming_provenance_repair_originals/computations__verification__fractional_hamming_full_end_3_2.py.original` | `archive/record/fractional_hamming_provenance_repair_originals/computations__verification__fractional_hamming_full_end_3_2.py.original` | `6c21cd207a21d650916939395f10deb1c6693e8a` | 272 |
| `record/fractional_hamming_provenance_repair_originals/computations__verification__fractional_hamming_network.py.original` | `archive/record/fractional_hamming_provenance_repair_originals/computations__verification__fractional_hamming_network.py.original` | `8478874335c9a2e2aec48c468bf3d81ddd68a51d` | 267 |
| `record/fractional_hamming_provenance_repair_originals/computations__verification__fractional_hamming_offcharge_bound.py.original` | `archive/record/fractional_hamming_provenance_repair_originals/computations__verification__fractional_hamming_offcharge_bound.py.original` | `aa6375fc9531a05d9078a25bd920b64e0ccbda38` | 275 |
| `record/fractional_hamming_provenance_repair_originals/computations__verification__fractional_hamming_replay.py.original` | `archive/record/fractional_hamming_provenance_repair_originals/computations__verification__fractional_hamming_replay.py.original` | `5971bef4341d8ecb23731f043b325740c37395f1` | 5200 |
| `record/fractional_hamming_provenance_repair_originals/computations__verification__fractional_hamming_top_gram.py.original` | `archive/record/fractional_hamming_provenance_repair_originals/computations__verification__fractional_hamming_top_gram.py.original` | `7ae9d4a8453551e471cb26c4efc3fcc40372ad53` | 268 |
| `record/fractional_hamming_provenance_repair_originals/computations__verification__fractional_hamming_torus.py.original` | `archive/record/fractional_hamming_provenance_repair_originals/computations__verification__fractional_hamming_torus.py.original` | `b3b1279ee4ef8f032915335299dacf063276d556` | 265 |
| `record/research_checkpoint_protocol_originals/research_checkpoint_replay_v1.py` | `archive/record/research_checkpoint_protocol_originals/research_checkpoint_replay_v1.py` | `6807b3c2c794e867aee980ece8e8e327b6a046c1` | 9002 |
| `record/research_checkpoint_protocol_originals/research_checkpoint_replay_v1.py.diff` | `archive/record/research_checkpoint_protocol_originals/research_checkpoint_replay_v1.py.diff` | `a66419cc7aca51e71c30734c4c431b5aeda459c6` | 3957 |
| `record/research_checkpoint_protocol_originals/research_checkpoint_replay_v2.py` | `archive/record/research_checkpoint_protocol_originals/research_checkpoint_replay_v2.py` | `4867fc6670858bcce4ae06a79a70d45e0b1762ba` | 10632 |
| `record/research_checkpoint_protocol_originals/research_checkpoint_replay_v2_to_v3.diff` | `archive/record/research_checkpoint_protocol_originals/research_checkpoint_replay_v2_to_v3.diff` | `02c05e08c66061d72dee6c6222a4cad735cb3c9e` | 12507 |
| `record/research_checkpoint_protocol_originals/test_research_checkpoint_portability_v1.py` | `archive/record/research_checkpoint_protocol_originals/test_research_checkpoint_portability_v1.py` | `2bb0cf1795a7c56d4c59b04a624d98cf69bc4362` | 7262 |
| `record/research_checkpoint_protocol_originals/test_research_checkpoint_portability_v1.py.diff` | `archive/record/research_checkpoint_protocol_originals/test_research_checkpoint_portability_v1.py.diff` | `bf27a7583139767ede1be62ac78bae96619d7ead` | 3267 |
| `record/research_checkpoint_protocol_originals/test_research_checkpoint_portability_v2.py` | `archive/record/research_checkpoint_protocol_originals/test_research_checkpoint_portability_v2.py` | `2b6e4c33dddcf69df25aff465812c67f936e9f30` | 9944 |
| `record/research_checkpoint_protocol_originals/test_research_checkpoint_portability_v2_to_v3.diff` | `archive/record/research_checkpoint_protocol_originals/test_research_checkpoint_portability_v2_to_v3.diff` | `5c69911e304a75b8b25341ede6860a2cb8250c5f` | 2468 |
| `record/research_checkpoint_seals/bgs_astra_corrected_integral_manifest.json` | `archive/record/research_checkpoint_seals/bgs_astra_corrected_integral_manifest.json` | `53b47d798d683e1a54d42d7134d6b510699724f2` | 6082 |
| `record/research_checkpoint_seals/bgs_astra_signed_boundary_checkpoint_manifest.json` | `archive/record/research_checkpoint_seals/bgs_astra_signed_boundary_checkpoint_manifest.json` | `22c660a849dd256c8d25f42cef7492c10fe72910` | 12869 |
| `record/research_checkpoint_seals/bgs_charge_strengthening_promotion_promotion_manifest.json` | `archive/record/research_checkpoint_seals/bgs_charge_strengthening_promotion_promotion_manifest.json` | `6251ac31e4c948e280012f5359e93e78a4dbbf5d` | 91513 |
| `record/research_checkpoint_seals/bgs_schur_reduction_promotion_delivery_manifest.json` | `archive/record/research_checkpoint_seals/bgs_schur_reduction_promotion_delivery_manifest.json` | `7cb116498550452a99e9cd289b75e4c7a7daa712` | 32098 |
| `record/schur_replay_freshness_originals/balanced_pair_schur.py` | `archive/record/schur_replay_freshness_originals/balanced_pair_schur.py` | `e1ab09a360900c08937a4c9097b448b57cd9d3aa` | 722 |
| `record/schur_replay_freshness_originals/full_replay.py` | `archive/record/schur_replay_freshness_originals/full_replay.py` | `5d7431d6c52c5a7d4a0274b2d30fd15a6f7ee4be` | 14680 |

Total: 30 files, 301652 bytes.
