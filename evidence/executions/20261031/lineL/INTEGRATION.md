# Integration record: Lines L, L2, L3 (BGS-TRACE-248..268; state reviews of BGS-TRACE-244, 245, 246)

Base: `origin/main` e9e1550a (merge of PR #63). Branch `line-L-op`. Commits as ChurilovMaksim (noreply). Times UTC+5.

## Sources
* Author packet `/workspace/bgs-lineL`: `REPORT_L.md` (v1), `REPORT_L_v2.md`, `NOTES_L.md`, `code/`, `logs/`, manifest `SHA256_L.txt`
  (verifies; own hash `SHA256_L.txt.sha256` matches); `L2/` (manifest `SHA256_L2.txt` verifies); `L3/` (manifest `SHA256_L3.txt` verifies;
  own hash matches). Copied to `computations/verification/lineL/` without `__pycache__`; no .npy/.npz.
* Referee `/workspace/audit/lineL` → `computations/verification/lineL/referee/` (manifest `SHA256.txt` verifies, including the final
  `REPORT.md` with the L2 and L3 sections). Verdicts: Line L first round ACCEPT AFTER FIXES F1–F5, DELTA (REPORT_L_v2) READY; L2 READY
  after text fixes L2-F1–F4; L3 READY after fixes L3-F1–F4.

## Errata applied at integration (author busy)
* `L2/REPORT_L2.md` §7: L2-F1 (h_m ≈ ½·2.4142^m, √h ≈ 1.5538^m, barrier thresholds exceed h_m itself), L2-F2 (B2 "height ≤ 4 sporadic
  collisions exist" needs η < 0.340, large p; Minkowski vector genuinely sporadic by Cauchy's root bound, 5.83 > 5; B1/B2 for split q,
  inert index q²), L2-F3 ((±2,16) "every p" → "all sufficiently large p"), L2-F4 ("K2′ too weak [P]" only at m where h_m has a prime
  q ∥ h_m in (max(c_W p², λ^{C_k+6.1e−6·m}), L_m); "all/most m" is [H]); Prop S block count min(r, 2I − k + 2). Author file:
  `pre_polish/L2/REPORT_L2.md` (sha256 6be0793b…, as in the L2 manifest), so `SHA256_L2.txt` now fails only for `L2/REPORT_L2.md`.
* `L3/REPORT_L3.md` §6: L3-F1 (M′ even; |F̂_{M′}| = 2/M′ on M′²/4 points, Σ = M′/2; |D_𝔮| ≤ 2h/q when |Z| ≤ h (m ≥ 495 via Prop K2);
  threshold ≈ 1.8808^m, still above L_m), L3-F2 (S3 exceptional prime 7, rank 3, not 3), L3-F3 (labels: S4 [P given Line G/I] + [N];
  Lemma Q Remark [H]; cost bound G^{3p}/q [H]; Reasons 2–3 [N]/[assessment]; "iterating CRT is not a descent" [assessment]), L3-F4 (FNDB
  sentence reworded as an analogy pointing to the need for kick-specific input). Author file: `pre_polish/L3/REPORT_L3.md` (sha256
  f9b76e03…), so `SHA256_L3.txt` now fails only for `L3/REPORT_L3.md`.

## Registry
* New: BGS-TRACE-248..268 (source `mathematics/fixed-map/lineL_op_open_range.md`); 256 (H_mean) open, the rest proved (257 is a proved
  implication from the open 256; 266 is proved given the Line G/I transfer law, dependencies 203, 216).
* State reviews: 244 open → proved [P + CA]; 245, 246 conditional → proved [P + CA] under the standing inputs (TRACE-197, J3 with L16,
  S_Z / Prop K2, Weil), m ≥ m₁ effective, not computed, c_W = 10^−25.62, q₀ = 10^13.2 (no explicit p₀); 246 carries the Prop S caveat.
  Titles of 245, 246 updated (no longer "conditional on OP"). Closure conditions removed for 244–246.
* Annotated, state unchanged: 247 (C1, open; Theorem U linked), 206 (frozen R′, OPEN), 256 (L3 annotation).
* `record/claim_integration_epochs.json`: 21 new after_wave3 rows; rows of 244–246 updated to the new states with explicit review text;
  206, 247 dispositions appended.
* Inventory: 21 new rows, rows 244–246 rebuilt, 206/247 re-mirrored, `source_blob_sha` = git blob of claims.json.
* Metadata: no new external reference; new cache snapshot `registry_metadata_20261031_lineL.json` (transitive impact sets of Dirichlet,
  Vinogradov, Weyl, Davenport, Weil only), pointer in `literature/metadata_audit.json`, report under `record/audits/`. Data-string change in
  `computations/maintenance/v4_negative_controls.py` (cache path lineK → lineL); no check weakened.
* Lean: `formalization/Bgs/LineLConst.lean` (core `decide`, no `native_decide`, no `sorry`, no axioms), imported in `Bgs.lean`;
  formalization README row and counts (30 further modules, 102 leaf modules).

## Checks done at integration
* Certificate reruns, L3 reruns (`integration_reruns/summary.txt`): identical outputs.
* `integration_checks/lineL_checks.py`: ALL_OK (constants of 251–253, 258, 260–262, 264, 265, 268).
* `lake exe cache get` + `lake build Bgs` (nice -n 10): exit 0, 8836 jobs.
* Checker suite: `checkers.log` vs `checkers_baseline_main_e9e1550a.log` (pre-existing failures on main unchanged).

## Deviations / notes
1. Neumann/Graf addition theorem, Jacobi–Anger, Minkowski (cube) and Cauchy's root bound are used without external-dependency records
   (standard textbook facts; named in the boundaries).
2. 1.6677²/ξ_lo = 1.13118…, Λ₁₆ = 0.12326; the reports quote 1.1311 and 0.12319 (rounded down, slightly understating the (±2,16) open
   range). BGS-TRACE-253 is registered in the exact form (1.6677²/ξ_lo)^{m(1+η)}; the constant 4.282 stays valid.
3. Non-vacuity of the Weil range: 2/c_W = 8.34·10²⁵ (the report rounds to 8.2·10²⁵); registered as ≈ 8.3·10²⁵.
4. REPORT_L_v2 cites a local `K2/REPORT_K2_v3.md`; the repository equivalent is the W-F7 errata in
   `computations/verification/lineK/K2/REPORT_K2_v2.md` §8.
5. Theorem U (254): the congruence form of the TRACE-206 phase P(n) is taken as given (referee caveat), stated in the boundary.
6. The L2 and L3 errata were written by the integrator, not the author.
7. Numerics, heuristics (deficit identity, slow-orbit model, Lemma Q Remark, cost bound) and assessments are notes only.

## Checker results (31 Oct 2026, completed by 15:43 UTC+5)
* Branch: render_bibliography, render_claim_registry, render_errata, render_research_views, render_spectral_research, render_status
  (all `--check`), scientific_registry_audit, repository_audit, wave3_integration_audit, audit_manuscript_references: exit 0.
* Pre-existing failures, identical on main e9e1550a (`checkers_baseline_main_e9e1550a.log`): wave2_integration_audit ("integrated wrapper
  mapping changed"), sync_return_sections (pandoc missing), check_spectral_edition ("source projection"), bibliographic_metadata_audit
  (EXT-BR-1975 drift), unittests. A second unittest run gave identical sorted FAIL/ERROR lists on branch and main (219 entries each,
  116 failures + 103 errors); the first branch run had one extra error (104), consistent with the known timeout of the routing test in a
  working tree that contains `formalization/.lake`.

## Owner audit of PR #64 (head d65557ef): fixes applied (31 Oct 2026, UTC+5)
Audit verdict MERGE-after-fixes. Changes: `record/claims.json`, the note `mathematics/fixed-map/lineL_op_open_range.md`, this file,
`formalization/Bgs/LineLConst.lean` (`#print axioms` lines only) and the regenerated registry views, inventory (`source_blob_sha`) and
epochs. Scripts: `integ_logs/edit_claims_R.py`, `edit_note_R.py`, `edit_inv_epochs_R.py` (integrator scratch, not in the repository).
* **R1 (strict option).** BGS-TRACE-245 and 246 no longer depend on BGS-TRACE-231 (conditional); they depend on its proved inputs
  212, 213, 225, 227, 228 instead (each in state proved; 197, 226, 238, 241 kept or added; 246 also gets 237 and 241). The ledger reads:
  standing inputs 197, 225, 226, 227, 238, 241 (all proved); only the proved identity and computer-assisted bounds of Line J
  (212/213/228) are used; the conditional conclusion of TRACE-231 and the open hypotheses 232, 233, 239, 256 are not used.
  BGS-TRACE-240 (Theorem K, conditional) is removed from the dependencies of 246 and 257; only its proved implication
  ("O♮^{<L}_m = o(ξ_lo^m) along an infinite subset of S⁺ ⇒ W′_m/m → ∞"), re-derived from its proved components (235; the proved parts of
  231 with 238; 237), is used, and this is stated explicitly. For 257 (a proved implication) the open antecedent H_mean (BGS-TRACE-256)
  is no longer listed as a dependency; the boundary says so. The boundaries of 245, 246, 253, 257, the 206 annotation phrase and the
  note §1 (standing inputs) are reworded accordingly.
* **R2.** In 246, 258 and the note §6: "holds unconditionally" → "holds without assuming frozen R′".
* **S2.** `#print axioms` for all 23 theorems of `Bgs.LineLConst` (was 14); all report "does not depend on any axioms"
  (`lean_axioms_LineLConst.log`).
* **S3.** 252 and the note §3 state δ_F = δ_OP/2.
* **S1 (policy, no new records).** The four standard results are not added to `literature/external_dependencies.json`. The schema would
  admit book references (precedent EXT-VINOGRADOV-1937), but a record there needs a source review that was read and pinned, a
  metadata-snapshot entry, an admission in `claim_integration_epochs.json` (`external_dependency_extension.added_ids`) and
  `external_dependencies` links on the claims; this was outside the scope of this fix round (claims.json and notes only), and the
  Minkowski and Cauchy textbook texts were not read here. Policy for Line L: standard textbook facts that are used as lemmas and are
  checked numerically or are elementary are named in the claim boundary, with a locator where one was read, and are not registered as
  external theorems. Locators: Neumann's addition theorem, DLMF 10.23.2 (for J and integer order no restriction on u, v; with u = v it
  gives Σ_a J_a(x) J_{a−d}(x) = δ_{d0}); Graf's addition theorem, DLMF 10.23.7; Jacobi–Anger, DLMF 10.12.1 with t = i e^{iθ} (giving
  e^{ix cos θ} = Σ_n iⁿ J_n(x) e^{inθ}) and 10.12.2–3 (both pages read on 31 Oct 2026). Minkowski's convex-body theorem (used for a cube in
  Lemma B2, BGS-TRACE-261) and Cauchy's root bound (|root| ≤ 1 + max|a_i/a_n|, L2-F2, BGS-TRACE-261): standard, no page pinned. None of
  the four is on the 244–246 chain; Graf and Jacobi–Anger were also checked numerically in the owner audit (errors < 3·10⁻³²).
  Registering them is a possible follow-up.
* **Deviation count (audit S4).** The deviations list above has 7 items. The integration report to the owner listed 9: it left out
  item 7 (notes only) and added three items recorded elsewhere: the changed titles of 245/246 (see "Registry"), the
  `v4_negative_controls.py` data string (see the metadata report), and that the L3 inheritance run at (7, 239) was not repeated at
  integration (only `inherit_test 5 41` and `excursion_check` were rerun, see `integration_reruns/summary.txt`). Nothing else is missing.
* **Dependency gate.** `computations/verification/lineL/integration_checks/proved_deps_gate.py` (log next to it) checks that no proved
  claim depends on a non-proved claim other than BGS-TRACE-206. The check is strict for 244–268 and fails on any new violation. Seven
  (claim, dependency) pairs outside Line L already violate the gate on main e9e1550a; they are listed in the script as data and left
  unchanged here: 076→060, 077→073, 080→060/073, RES-015→RES-014, RES-023→RES-022, 236→231. Result: GATE_OK.
* The metadata snapshot `registry_metadata_20261031_lineL.json` regenerates byte-identically (sha256 7d7d4900…), because the transitive
  impact sets are unchanged.
