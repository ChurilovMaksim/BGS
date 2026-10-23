# MANIFEST-Map — phase 1, package Map (map migration): pinned `record/` files → `archive/record/`

**Scope:** the reduced map-migration package of the bindings track
(design `bindings_track_design.md` §A/§C; executor decisions of 23 October 2026):
**13 of the 19** map-pinned files held by packages F-1/F-2 move from `record/`
to `archive/record/`; **6 are held** with named dispositions (section below).
Copies are byte-for-byte; the content of the archival copies is not edited.
Every consuming map is migrated in the same commit. For every moved file the
content hash (`sha256`) is unchanged — the bytes do not change, so no hash
rotates. Exactly one hash in the package does change, and it is not a moved
file's: the charge map's row for the **held, live** `charge_strengthening_promotion.md`,
whose own navigation links this package edits (below) — the map pins the
sha256 of each file's *current* content, so that row's value is updated to
the edited file's sha256 (`76ab49d9…` → `2997f597…`), the package-E pattern
for a map pinning a file the package itself edits. Base: main at the
post-B-rest / Lean-statement state (constructed and control-verified by the
package assembly).

## Moved files (13)

| Old path | New path | git blob SHA | SHA-256 | Bytes |
|---|---|---|---|---:|
| `record/charge_strengthening_computation_contract.json` | `archive/record/charge_strengthening_computation_contract.json` | `8e4c7b36b1b652c928afe4110147b9759ce532f0` | `b13bd7b77103045d8c0805bfb9437f457acc060de05a2cd8392703e19e690ac8` | 3236 |
| `record/charge_strengthening_editorial_mapping.json` | `archive/record/charge_strengthening_editorial_mapping.json` | `9a5fdb6c72318b70fea827576bbf00df32379254` | `0adec3e3739a9d16bc5daff48d3253f4d14627e75274a073f7852678c5f2f8e5` | 6601 |
| `record/charge_strengthening_integration_proposal.md` | `archive/record/charge_strengthening_integration_proposal.md` | `8ad781b34e0b4850eb70e46b293afc31cbbbd5ef` | `d0fd8bcfc78774cb01d8b833f4a045534a7e897968bb22372ca59eac7c3e2622` | 3507 |
| `record/charge_strengthening_port_mapping.json` | `archive/record/charge_strengthening_port_mapping.json` | `ccd05d6a8ae8657a3033c6b5c422e70c5faf3821` | `23dd10287ce7ab23f95fdf60b93804ae7ee16bcbf8142059b6bc517975057158` | 1171 |
| `record/charge_strengthening_raw_mapping.json` | `archive/record/charge_strengthening_raw_mapping.json` | `01e1809657879748fcd79395c26b3e1a1b75c6a8` | `e044a6cb30aa4fbf302fc2c081f5a8bb02511e5119536edda8f335153037a4d0` | 31194 |
| `record/research_checkpoint_balanced_audit_import.json` | `archive/record/research_checkpoint_balanced_audit_import.json` | `522e47ec7f170a512918d85f7b223d523ac6311c` | `7c8a039620fb937d47d6c756f30a0b3616abf4a65e2abbbdb2ecc3cc70a1f7f0` | 4835 |
| `record/research_checkpoint_proof_mapping.json` | `archive/record/research_checkpoint_proof_mapping.json` | `4d3110ed6a7f93a53857b8c0441bd82399f9c42d` | `e90a13816745c805f88a930f50f178b54ef124a3a107cfc6a0d611bc585c6ceb` | 7473 |
| `record/residual125_uniform_review.md` | `archive/record/residual125_uniform_review.md` | `07c05fc809fa935acc02c44c92739702631e9629` | `2adfb22893df719fa8e650c34a70bd0e277148e10ae7bdc8df2d3ad37446172e` | 17321 |
| `record/balanced_hamming_review.md` | `archive/record/balanced_hamming_review.md` | `bae720452070da453248da54460eeb030bf1fee7` | `5b5fefbc8b92a0e389d71892d6601de404b8facfafb8798999b136afae565964` | 22145 |
| `record/coordinate_translation_review.md` | `archive/record/coordinate_translation_review.md` | `2ea415f94d50b2a161d2502983a2138f426a8cf6` | `da68023515d0e525de0c34fe14eff3b471a0fe039a7c62efb84f048b73e13b18` | 20604 |
| `record/all_coordinate_translation_review.md` | `archive/record/all_coordinate_translation_review.md` | `ca73e93ceaf6d2ea185fe70818b45c8f6f3d46dd` | `7b046dd79bdb000a0d84c150a1949d517fdb2043c3a81d6929e8c5e2ae17b4` | 18071 |
| `record/low_switch_offcharge_review.md` | `archive/record/low_switch_offcharge_review.md` | `e81599cc8ba5f1d1fec0949c2d3f8386284a53fe` | `eb50ca67558a40bdfc15bad02a5639bae90cd67de1ec8a2df27b6ed5b124db81` | 16181 |
| `record/half_radius_obstruction_review.md` | `archive/record/half_radius_obstruction_review.md` | `516235f1ce43af9bf77b89659e9d7d6baf623758` | `aff11c43342a27c87dbf9d2250c1fa30eb7157d99c97e524ab202d9320fad10e` | 17015 |

Total moved: 13 files / 176 566 bytes.

## Same-commit migrations

- `record/charge_strengthening_replay_sources.json` (F-STAY map, does not move):
  `files[112]`, `files[114]`, `files[115]`, `files[116]`, `files[118]` `path`
  values → `archive/record/…`. Rows 113 (`charge_strengthening_dependency_contract.json`)
  and 117 (`charge_strengthening_promotion.md`) are **not** migrated (held files).
  The `sha256` values of all re-pointed rows are unchanged. Row 117's `sha256`
  is updated to the post-edit sha256 of the held promotion file
  (`2997f59727043bd37e273142e89bfe18ced34ee0368da911350d6cbe2deff051`),
  because this package edits that file's navigation links (below) and the map
  pins current content; the replay's `sources()` check verifies it.
- `record/research_checkpoint_source_bindings.json` (F-STAY map, does not move):
  the keys `record/research_checkpoint_balanced_audit_import.json` and
  `record/research_checkpoint_proof_mapping.json` are renamed to their
  `archive/record/…` forms; values (sha256) unchanged. The key
  `record/research_checkpoint_import.json` is **not** renamed (held file).
- `record/residual125_promotion_map.json`: entry [1] `public_path` →
  `archive/record/residual125_uniform_review.md` (`public_sha256` unchanged).
- `record/central_residual_promotion_map.json`: entries [3], [4], [21], [29]
  `public_path` → `archive/record/…` for balanced_hamming, coordinate_translation,
  all_coordinate_translation, low_switch_offcharge reviews (`public_sha256`
  unchanged). Prose `status_edits` texts mentioning the old paths are historical
  records of applied edits and are not rewritten.
- `record/half_radius_promotion_map.json`: entry [2] `public_path` →
  `archive/record/half_radius_obstruction_review.md` (`public_sha256` unchanged).
- `record/claims.json` — **6 path values, all `evidence[]`, pure `archive/`
  prefixes**: BGS-FM-026 `evidence[16]` (residual125_uniform_review);
  BGS-TRACE-021 `evidence[0,1,2,3,9]` (balanced_hamming, coordinate_translation,
  all_coordinate_translation, low_switch_offcharge, half_radius_obstruction
  reviews). TRACE-021 `evidence[11]` and `evidence[12]` (dependency_contract,
  promotion — held) and BGS-FM-027 `evidence[0]` (dependency_contract — held)
  are not touched. No status, source or other field changes.
- `record/claim_integration_epochs.json` — epoch registration by the standing
  recipe, **extensions only**: the existing amendment rows for BGS-FM-026 and
  BGS-TRACE-021 have their `fields.evidence` updated to the full post-package
  arrays, a package-Map clause appended to `disposition` (original text
  preserved), and `archive/MANIFEST-Map.md` appended to `review`.
  `historical_row_sha256` values are unchanged, **no new amendment rows are
  added**, and the `approved` set literal in
  `computations/verification/wave2_integration_audit.py` is **not** changed
  (both IDs are already approved; the audit code is not part of this package).
- Navigation (URL-only edits; text outside the targets byte-identical, verified
  by reverse substitution):
  - `record/charge_strengthening_promotion.md` (**held file, edited in place**):
    its 4 link targets to moved charge siblings (computation contract,
    editorial mapping, integration proposal, raw mapping) →
    `../archive/record/…`. Its link to the held dependency contract is unchanged.
  - `mathematics/phase_trace_checkpoint.md`: the link
    `../record/research_checkpoint_proof_mapping.json` →
    `../archive/record/research_checkpoint_proof_mapping.json`. Its link to the
    held dependency contract is unchanged.
- Not edited, by design: prose mentions of the moved review paths inside
  hash-pinned mathematics sources (`balanced_hamming_hierarchy.md`,
  `macroscopic_coordinate_translation.md`, `all_coordinate_translation.md`,
  `fourier_half_radius_obstruction.md`, `symplectic_half_radius_obstruction.md`)
  — those bytes are pinned by the promotion maps above and resolve through
  this manifest; the pinned carriers
  `mathematics/onestep_charge_gap.md`, `mathematics/global_switch_transfer.md`,
  `mathematics/balanced_pair_schur_reduction.md` and
  `literature/color_one_boundary_qualification_20261007.md` are likewise
  untouched (their link targets are the held files below, which stay live).

## Held files (6) — NOT part of this package

The files remain in `record/`; a future move requires the named condition.

| File (stays in `record/`) | git blob SHA | Bytes | Disposition |
|---|---|---:|---|
| `record/charge_strengthening_dependency_contract.json` | `d3449c5b4e0a7934cdacebdde39b20348d9acddb` | 6852 | Linked from the hash-pinned live carrier `mathematics/onestep_charge_gap.md` (wave2 bindings, pin verified live); a dead link in a pinned document is worse than the file in `record/` (F-1 §Б.5 precedent). The unpinned link from `mathematics/phase_trace_checkpoint.md` stays valid because the file stays. Charge map row 113 and the FM-027 / TRACE-021[11] claims leaves stay pointed at `record/`. Moves only if the pinned-carrier link class is accepted as manifest-resolved, or the carriers are unpinned in phase 7. |
| `record/charge_strengthening_promotion.md` | `55496aa73b4ae3f8d40c2c6b5aa5151830bb7678` | 6360 | Linked from two hash-pinned live carriers (`mathematics/onestep_charge_gap.md`, `mathematics/global_switch_transfer.md`). Charge map row 117 and TRACE-021[12] stay. The file itself is live and unpinned, so its own outgoing links to the 13 moved files are migrated in this package (above). |
| `record/research_checkpoint_import.json` | `a6013045374988dc110bbba86c9d3886cc71dfd7` | 164577 | Linked from the hash-pinned `literature/color_one_boundary_qualification_20261007.md`; its rc-bindings key is not renamed. Its internal textual mentions of the moved charge files are the frozen content of a historical import artifact and resolve through this manifest. |
| `record/checked_research_checkpoint_20261007.md` | `27ac3bb285b44b1326ab219b4627c489d44a095a` | 12982 | Replay-visible identifier: the scoped-bindings key is an element of the wave2 echo task's `PINS` and of the sealed expected outputs inside `evidence/wave2_checked_20261007`. Renaming the key would re-base sealed replay outputs — a re-basing project (phases 2/3/7), not a migration. |
| `record/schur_replay_freshness_repair_receipt.json` | `b5a25a302df466652a75a12c258c5f84002eab61` | 15022 | Held as a pair with `schur_reduction_promotion.md` (design §A.6): its only live link is the sibling link inside the held `checked_research_checkpoint_20261007.md`; the freshness map's `receipt` field is informational (no code consumer reads it). |
| `record/schur_reduction_promotion.md` | `1b1323f148144075a1491a811d69b245d0c6b417` | 7518 | Direct F-1 §Б.5 precedent: linked from the hash-pinned `mathematics/balanced_pair_schur_reduction.md` (pin live and verified). Its disposition is revisited together with the `evidence/schur_reduction_20261007` tree decision. |
