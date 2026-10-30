# Line H integration record (30 October 2026)

Branch `lineH-49state-certificate`, created from `origin/main` at 24bd3988 (merge of PR #58; no later commits on main at
integration time). The packet was prepared against 1071af71, the PR #58 head; `git diff 1071af71 24bd3988` is empty, so nothing
relevant differs. IDs: the highest registered claim on main was BGS-TRACE-206; Line H takes BGS-TRACE-207, 208 and 209 as proposed, and BGS-TRACE-210 for the R_NSW split (owner audit).

## Packet bytes
`receipt.json` lists the sha256 of 83 packet files. 80 are committed at their packet paths; 78 of them are byte-identical. Three are not committed because they were applied rather than copied: `formalization/Bgs.lean.patch` (applied to `Bgs.lean`), and the registry proposals `record/new_claims_h.json` and `record/claim_changes_h.json` (applied to `record/claims.json`). Two committed packet files were changed at integration, on purpose:
* `formalization/Bgs/LineH.lean`: nine `#print axioms` lines (one per theorem, main's convention, checked by
  `../lineE-resonant-transfer/axioms_coverage.py`) were added before `end Bgs.LineH`. Removing those nine lines and the blank line
  before `end` restores the receipt's sha256 exactly (checked at integration).
* `mathematics/fixed-map/lineH_49state_certificate.md`: one paragraph after the status lines anchors the stable IDs
  BGS-TRACE-207/208/209 (`scientific_registry_audit.py` requires each claim ID in its source). Removing that paragraph restores the
  receipt's sha256.
* `mathematics/fixed-map/lineH_49state_certificate.md`, second change (owner audit of PR #59, items A1–A3, 2026-10-30).
  Four in-place replacements (packet text → committed text), and the anchor paragraph now names BGS-TRACE-210:
  1. A2: "since h_d | h_m for d | m (BGS-TRACE-205, G5)." → "since h_d | h_m for d | m with m odd (Lean `Bgs.LineG.nsw_dvd`,
     `formalization/Bgs/LineG.lean`; not registered by a proved claim)." The packet cited open BGS-TRACE-205 (G5); the fact used is the
     Lean-proved lemma `Bgs.LineG.nsw_dvd` (axioms propext, Classical.choice, Quot.sound). No proved registry claim registers it
     (the only claims with `LineG.lean` as formalization are BGS-TRACE-203, about the partial-trace law, and the open 205).
  2. A1: "applies: R_NSW is violated" → "applies: R_NSW (registered as BGS-TRACE-210, open) is violated".
  3. A2: "BGS-TRACE-205 G5 (h_d | h_m, used only for R_NSW)" → "the Lean lemma `Bgs.LineG.nsw_dvd` in `formalization/Bgs/LineG.lean`
     (h_d | h_m, used only for R_NSW)" (§7 Dependencies).
  4. A3: "(`referee/refV0.json`)" → "(`referee/out/refV0.json`)" (§V_0 certificate of record; the file is at `referee/out/`).
  No mathematical content changed.

**Restoring the receipt hashes.** `python3 evidence/executions/20261030/lineH/restore_packet_bytes.py` undoes all documented edits of
both files in memory (drops the anchor paragraph and its preceding blank line, reverses replacements 1–4, drops the nine
`#print axioms` lines and the blank line before `end Bgs.LineH`) and compares with `receipt.json`; it prints `OK` for both files at
this commit. `--write DIR` saves the restored packet copies under DIR.

The packet's top-level `README_verification.md`/`README_evidence.md` are identical to the two READMEs placed in the repository. Absolute scratch paths in hashed files are whitelisted, not edited:
[`PROVENANCE_PATHS.md`](../../../../computations/verification/lineH/PROVENANCE_PATHS.md).

## Registry
* New: BGS-TRACE-207 (proved), 208 (proved, computer-assisted), 209 (proved, computer-assisted).
* BGS-TRACE-179 (Conjecture R; titled "Conjecture R / R_NSW" before this branch): **open → refuted** (owner decision, option A). The registry state vocabulary gains
  `refuted`: `ALLOWED_STATES` in `computations/verification/scientific_registry_audit.py` and `STATES` in
  `computations/maintenance/render_status.py`; no other script enumerates states. Evidence: BGS-TRACE-209 and this receipt;
  verifiers `bounds49.py`, `rig_spec.py`, referee `ref_rig.py`, `ref_bounds.py`. Scope of "refuted": R exactly as stated, for the
  Line B kick, through η = 2. BGS-BGS-001 is neither proved nor disproved. No dependency edge 179 ↔ 209 was added (owner audit A4).
* New (owner audit A1): **BGS-TRACE-210** "Conjecture R_NSW: W~rest_m(eta) = o(m) along m with h_m prime", state **open**, split
  out of 179, which is retitled "Conjecture R: W~rest_m(eta) = o(m) uniformly on compact eta-ranges". Boundary: violated at every
  m ≥ 47 with h_m prime by BGS-TRACE-209; whether there are infinitely many such m is unknown, so undecided. Dependencies 170, 177;
  209 is cited in the boundary and evidence only (not a dependency edge). Source anchor: `derandomized_fixed_kick.md#claim-210`.
  Epochs: dated row (2026-10-30) for 210. 209's boundary now points to 210 and cites `Bgs.LineG.nsw_dvd` instead of BGS-TRACE-205 G5.
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
