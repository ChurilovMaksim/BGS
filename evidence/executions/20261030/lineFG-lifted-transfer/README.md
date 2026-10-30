# Lines F and G execution evidence (30 October 2026)

This directory backs `mathematics/fixed-map/lifted_transfer_lineF.md`, `mathematics/fixed-map/resonance_classification_lineG.md` and `manuscript/unified_sections/lifted_transfer_lineFG.tex`.

**IDs.** On main at e378ad11 (after PR #57) the highest registered TRACE id was BGS-TRACE-196. Lines F and G take BGS-TRACE-197 through BGS-TRACE-206, exactly as proposed by the referee; nothing was renumbered. BGS-TRACE-179, 187, 188, 191 and 196 are annotated only; their states are unchanged.

**States.** 197 proved; 198, 199, 200, 201 proved (computer-assisted); 202 open (numerical); 203 proved (finite alphabet); 204 open; 205 open (numerical record); 206 open. The registry has no conjecture state (allowed: proved, conditional, open, verification-pending), so Conjecture R′ (206) is registered as open with a `closure_condition`.

**Review state.** Both lines were audited by an independent referee (`computations/verification/lineFG/referee/REPORT.md`). Blocking fixes applied:

1. Every quoted bound is rounded in the safe direction (`computations/verification/lineF/code/safe_table.py` → `logs/safe_table.md`): e.g. W̃rest_m/m ≥ 8.06 (not 8.07) at m = 15, |μ*| ∈ [1.9154712, 1.9154753] at η = 2, ‖L_V‖₁ ≤ 730.15, and the η = 1.25 table and enclosure are consistent.
2. H∞ wording: BGS-TRACE-199 proves the *conclusion* of BGS-TRACE-188 (k1, η = 2) on a different, explicit space; H∞ as stated in 188 is neither proved nor needed, and 188 stays conditional.
3. η = 2.5 is included only with the sector-6 = sector-2 reflection lemma ((UΦ)_k(s) = Φ_{−k}(−s), U L_w U⁻¹ = L_{w(−·)}; proof in the note) and a completed E-lattice certificate. The η = 2.5 run finished after the referee audit and was not seen by the referee.
4. F7 is float evidence ("stable under two discretisations").
5. Lean is in `formalization/Bgs/LineF.lean` and `LineG.lean` (namespaces `Bgs.LineF`, `Bgs.LineG`), imported by `Bgs.lean`, with hypotheses stated in the theorems and one `#print axioms` per theorem.
6. The Line G §3 overclaim about Conjecture R is removed; R′ is frozen to one definition (the "pred" quantities of `computations/verification/lineG/code/formula_table.py`, k1 only); G3 is open (sketch) and G7 is a heuristic.
7. Nit F.7: `bounds_lift.py` asserts its closed form (2048-bit check of 2(h−1) < λ^{m/2}); all six η rows regenerate identically.
8. Referee material and packets carry no absolute scratch paths.

**Pre-registration.** `computations/verification/lineG/PREDICTIONS_m17.json` (sha256 fa8505f503790ae2c6265f917debdd4b023b2c50b79412daac7d14f72b8aa344) is committed here; this commit is its first external record. A k1 m = 17 evaluation finished on the integration machine during integration, after the referee audit; it is unreviewed and is neither included nor used. Nothing is claimed at m = 17.

## Non-claims

1. Conjecture R (BGS-TRACE-179, the Line B kick f_B) is not disproved; BGS-TRACE-196 stays conditional.
2. Every unconditional all-m statement concerns the k1 kick 0.9 cos 2πq (and f7 for 3 ∤ m, 200), not f_B.
3. The η-window (0.951, 3.212) and the f_B lifted eigenvalues are float evidence (202).
4. R′ (206) rests on four values m = 9, …, 15 with an upward drift; it is not a statement about Conjecture R.
5. No BGS counterexample; no progress on BGS-TRACE-148.

## Lean (`leanprover/lean4:v4.33.1`)

| file | content |
|---|---|
| `lake_cache_get.log` | `lake exe cache get`: exit 0, 8690 files already decompressed; Mathlib not built from source. |
| `lake_build_Bgs.log` | `nice -n 10 lake build Bgs`: "Build completed successfully (8812 jobs)", exit 0. `Bgs.LineF` and `Bgs.LineG` built (66 s each under load); one linter warning in `LineF.lean` (unused `push_cast`). |
| `AxiomsLineFG.lean`, `lean_axioms_LineFG.log` | `#print axioms` for all 33 theorems: 23 [propext, Classical.choice, Quot.sound], 2 [propext, Quot.sound], 6 [propext], 2 none. No sorryAx, no ofReduceBool; no `sorry`/`native_decide` in either module. |
| `controls/`, `lean_controls.log` | 4/4 false controls (wrong `nsw` values, a false divisibility, a false Pell identity) rejected for the expected reason. |
| `axioms_coverage.log` | main's static checker (`../lineE-resonant-transfer/axioms_coverage.py`): 1288/1288 theorem/lemma declarations (1255 on main + 33), exit 0. |

The Lean layer covers combinatorial and algebraic cores only: the vertex-minus-edge counting identity of 197 (rounding maps with hypotheses 0 ≤ μ < 1), the G1 phase split, the G1′ automaton and quadratic-form identity, h_d ∣ h_m for d ∣ m with m odd (all m), and m = 17 facts. The analytic trace-class statements and the arb certificates are not formalised.

## Repository checkers

`checkers.log` (pandoc 3.12.1 on PATH): exit 0 for the scientific registry audit (290 claims), repository audit, text-control audit, wave3 integration audit, all render `--check` scripts, the manuscript reference audit, the three section-sync `--check` scripts (SKIP as hand-edited), wave3 source closure and `compileall`. Exit 1, identically on pristine main e378ad11 (not caused by this branch): `wave2_integration_audit.py` (integrated wrapper mapping), `bibliographic_metadata_audit.py --self-test` (EXT-BR-1975 dependency graph), `wave2_portable_replay.py --check-sources` (`mathematics/position_chain_mixing.md`).

`manuscript_compile.log`: tectonic compile (pdflatex is not installed); see the log for the pre-existing error on main and the scratch-copy compile including the new section.

GitHub Actions was not executed.

## Receipt

`receipt.json`: base, ID assignment, fixes, environment, Lean logs, the pre-registration hash, non-claims, and sha256 of the notes, the section, the Lean modules, key scripts, the safe table, all certificates and bounds JSONs, and the referee report.
