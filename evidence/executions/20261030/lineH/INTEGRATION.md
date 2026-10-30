# Line H integration record (30 October 2026)

Branch `lineH-49state-certificate`, created from `origin/main` at 24bd3988 (merge of PR #58; no later commits on main at
integration time). The packet was prepared against 1071af71, the PR #58 head; `git diff 1071af71 24bd3988` is empty, so nothing
relevant differs. IDs: the highest registered claim on main was BGS-TRACE-206; Line H takes BGS-TRACE-207, 208 and 209 as proposed.

## Packet bytes
`receipt.json` lists the sha256 of 83 packet files. 80 are committed at their packet paths; 78 of them are byte-identical. Three are not committed because they were applied rather than copied: `formalization/Bgs.lean.patch` (applied to `Bgs.lean`), and the registry proposals `record/new_claims_h.json` and `record/claim_changes_h.json` (applied to `record/claims.json`). Two committed packet files were changed at integration, on purpose:
* `formalization/Bgs/LineH.lean`: nine `#print axioms` lines (one per theorem, main's convention, checked by
  `../lineE-resonant-transfer/axioms_coverage.py`) were added before `end Bgs.LineH`. Removing those nine lines and the blank line
  before `end` restores the receipt's sha256 exactly (checked at integration).
* `mathematics/fixed-map/lineH_49state_certificate.md`: one paragraph after the status lines anchors the stable IDs
  BGS-TRACE-207/208/209 (`scientific_registry_audit.py` requires each claim ID in its source). Removing that paragraph restores the
  receipt's sha256.

The packet's top-level `README_verification.md`/`README_evidence.md` are identical to the two READMEs placed in the repository. Absolute scratch paths in hashed files are whitelisted, not edited:
[`PROVENANCE_PATHS.md`](../../../../computations/verification/lineH/PROVENANCE_PATHS.md).

## Registry
* New: BGS-TRACE-207 (proved), 208 (proved, computer-assisted), 209 (proved, computer-assisted).
* BGS-TRACE-179 (Conjecture R / R_NSW): **open → refuted** (owner decision, option A). The registry state vocabulary gains
  `refuted`: `ALLOWED_STATES` in `computations/verification/scientific_registry_audit.py` and `STATES` in
  `computations/maintenance/render_status.py`; no other script enumerates states. Evidence: BGS-TRACE-209 and this receipt;
  verifiers `bounds49.py`, `rig_spec.py`, referee `ref_rig.py`, `ref_bounds.py`. Scope of "refuted": R exactly as stated, for the
  Line B kick, through η = 2. R_NSW is not decided. BGS-BGS-001 is neither proved nor disproved. No dependency edge 179 ↔ 209 was added.
* BGS-TRACE-196 stays conditional (annotation; closure note). BGS-TRACE-194 and 197: annotations.
* `record/claim_verification_inventory.json` (source_blob_sha and mirrored rows) and `record/claim_integration_epochs.json`
  (179 state lineage and three follow-on rows) updated by script; generated views regenerated with `computations/maintenance/render_*.py`.

## Checks (all with `nice -n 10`)
| file | content |
|---|---|
| `lake_cache_get.log` | `lake exe cache get`: exit 0 (Mathlib from cache, not built from source) |
| `lake_build_Bgs.log` | full `lake build Bgs`: "Build completed successfully (8813 jobs)", exit 0; `Bgs.LineH` built (125 s); axioms of the 9 LineH theorems printed in the build |
| `lean_axioms_LineH.log` | `lake env lean AxiomsLineH.lean`: 8 × [propext, Classical.choice, Quot.sound], `shift4` [propext, Quot.sound]; no sorryAx, no ofReduceBool |
| `axioms_coverage.log` | static `#print axioms` coverage 1297/1297 (1288 on main + 9) |
| `checkers.log` | render `--check` ×6, scientific_registry_audit, repository_audit, wave3 audit, manuscript references, unit tests, and others; failures identical to pristine 24bd3988 are marked there |
| `manuscript_compile.log` | tectonic compile of the manuscript (scratch copy): exit 0, 368 pages, no warning in the Line H section |
| `integration_reruns/` | `kappa_check.py` (398 pairs OK), `bounds49.py` re-run (output byte-identical to `computations/verification/lineH/logs/bounds49_v4.json`, sha256 d1f56537…), referee `ref_bounds_on_v4.py` re-run with its two hard-coded input directories pointed at the repository copies (output identical to `logs/ref_bounds_on_v4.log`) |
