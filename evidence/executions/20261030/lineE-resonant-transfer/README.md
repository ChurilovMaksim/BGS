# Line E execution evidence (30 October 2026)

This directory backs `mathematics/fixed-map/resonant_residue_lineE.md` and `manuscript/unified_sections/resonant_residue_lineE.tex`.

**IDs.** On main at 347f1730 the highest registered TRACE id was BGS-TRACE-182. Line E takes BGS-TRACE-183 through BGS-TRACE-196; nothing was renumbered. BGS-TRACE-179, 180 and 182 are annotated only; their states are unchanged.

**Review state.** 183–192 (E1–E10) were audited by an independent referee (`computations/verification/lineE/referee/REPORT.md`); fixes F1–F13 and all nits are applied. 193–196 (E11–E14, "step 2") were audited by a second independent referee (`computations/verification/lineE/referee2/REPORT.md`, verdict "merge after fixes"); its fixes R1–R7 and the correct nits are applied. 193 is proved (computer-assisted via 187), 194 proved, 195 proved (computer-assisted, m = 11 and 13 only), 196 conditional. Every certified bound is quoted in the safe direction (lower bounds rounded down, enclosures outward).

## Non-claims

1. Conjecture R (BGS-TRACE-179) is not disproved, for any kick. Every unconditional growth statement covers finitely many m; the asymptotic statements (188, 196) are conditional.
2. Everything rigorous for all large m concerns the k1 kick 0.9 cos 2πq (the *k1-kick analogue* of R), not the TRACE-179 kick f_B.
3. For f_B, the rigorous content is finite-m lower bounds at m = 11 and 13 only (195; an m = 17 certificate is pending and nothing is claimed for it) and the exact 49-state law along 3 ∤ m (194). Nothing is claimed along 3 | m.
4. No BGS counterexample; nothing about eigenvalue statistics beyond the second moment of Tr U^m; no progress on BGS-TRACE-148.
5. BGS-TRACE-180 is contradicted only in its moment form; it is not contradicted as a convergence-in-law statement.
6. The resonance is an analogy to Keating–Mezzadri pseudo-symmetries; no pseudo-symmetry operator is exhibited and no instance of their mechanism is claimed.
7. The step-2 certificate (195) is IEEE double/long double arithmetic with an a-priori rounding bound (arb-rounded tables), not ball arithmetic. The second referee reproduced the m = 11 and 13 bounds with an independent directed-rounding interval kernel.

## Merge of main 4f9d4766 (2026-10-30)

The branch was brought up to date with a normal merge commit of `origin/main` at 4f9d4766 (three commits after 347f1730: LineCEncounter split and `#print axioms` coverage, Phase 1 docs, closure conditions for conditional claims). Changes made for the merge:

- `formalization/README.md`: textual conflict resolved by keeping both sides; the `LineE.lean` / `LineEResonance.lean` rows follow main's `LineDCerts.lean` row; counts updated to 22 further finite-certificate modules imported directly by `Bgs.lean` and 94 leaf modules (main: 20 and 92). Not changed here: main's count does not include the 8 `LineCEncounter*` submodules created by the split (it names only `LineCEncounter.lean`).
- `record/claims.json` regenerated from main's 4f9d4766 registry plus the Line E entries (not hand-merged): main's 13 new closure conditions are kept, and the two conditional Line E claims now carry a `closure_condition` (BGS-TRACE-188: H_infinity proved; BGS-TRACE-196: H_infinity,7(s) proved for some sign s), so all 15 conditional claims have one. Open Line E claims already had one. Generated surfaces re-rendered; this also refreshes `ERRATA.md`, `STATUS.md` and `record/claim_registry.md`, which were stale on main 4f9d4766 (their render `--check` fails there).
- `#print axioms` coverage in main's convention (one `#print axioms <name>` per theorem/lemma, inside the namespace before `end`): 12 lines in `LineE.lean`, 16 in `LineEResonance.lean`. `axioms_coverage.py` is a static check of that convention over `formalization/Bgs/**/*.lean`; it gives 1227/1227 on main 4f9d4766 and 1255/1255 on this branch (`axioms_coverage.log`).

## Lean (this checkout, `leanprover/lean4:v4.33.1`)

| file | content |
|---|---|
| `lake_cache_get.log` | `lake exe cache get`: exit 0, 8690 cached files already decompressed. Mathlib was not built from source. |
| `lake_build_Bgs.log` | full `lake build Bgs` with `Bgs.LineE` and `Bgs.LineEResonance` imported after `Bgs.LineBPhase4`; rerun after the merge: "Build completed successfully (8810 jobs)", exit 0; `Bgs.LineE` (115 s) and `Bgs.LineEResonance` (28 s) rebuilt under machine load. The log carries the in-file `#print axioms` output; the 28 Line E lines are 24 [propext], 1 [propext, Quot.sound], 3 [propext, Classical.choice, Quot.sound]. Pre-existing modules from main (e.g. `SevenPrimary`, `CayleyEnergy`, `PellCoboundary`) report `native_decide` auxiliary axioms in this output; none of them is a Line E module. |
| `AxiomsLineE.lean`, `lean_axioms_LineE.log` | `#print axioms` for all 28 theorems: 24 [propext], 1 [propext, Quot.sound], 3 [propext, Classical.choice, Quot.sound]. No sorryAx, no ofReduceBool. No `sorry`/`native_decide` in either module (the only matches are comments). |
| `axioms_coverage.py`, `axioms_coverage.log` | static `#print axioms` coverage: 1255/1255 theorem/lemma declarations, exit 0 |
| `controls/`, `lean_controls.log` | 5/5 false controls rejected for the expected reason (`decide` proves the proposition false); the script counts any other failure as BAD |

## Repository checkers

`checkers.log` (merged checkout; pandoc 3.12.1 on PATH). Exit 0: scientific registry audit, repository audit, text-control audit, all render `--check` scripts, manuscript reference audit, the three section-sync `--check` scripts (finite-orbit and fixed-map SKIP as hand-edited), wave3 source closure, `compileall -W error::SyntaxWarning`.

Exit 1 on pristine main 4f9d4766 as well (not caused by this branch): `wave3_integration_audit.py` ("old claim contract changed outside reviewed amendment: BGS-FM-004", from main's closure-condition commit 4f9d4766; it passed on this branch before the merge); and, identically on main 347f1730: bibliographic `--self-test` (EXT-BR-1975 dependency graph), `wave2_portable_replay.py --check-sources` (sealed digest of `mathematics/position_chain_mixing.md`), `wave2_integration_audit.py` (integrated wrapper mapping).

`unittest_summary.log` (before the merge): `python -m unittest discover -s computations/maintenance/tests` gives 116 failures / 103 errors / 1 skip on pristine main with system python (sympy missing) and 104 failures / 4 errors with the full scientific venv, and in both runs the same set on this branch, except one 30 s subprocess timeout (`test_fractional_routing`) caused by machine load from the certificate jobs; it passes when rerun alone (logged).

`manuscript_compile.log` (before the merge; main 4f9d4766 changed no manuscript file): `pdflatex` is not installed, so `build_unified_manuscript.py` was not run. A tectonic 0.15.0 compile of `BGS_unified.tex` halts at a pre-existing error on main (`derandomized_fixed_kick.tex:94`, a `]` inside a theorem optional argument; line unchanged by this branch). With that one line braced in a scratch copy (not committed), the whole manuscript, including the new section, compiles with no undefined references.

GitHub Actions was not executed.

## Numerical certificates

- k1 IFS certificates (183–187): `computations/verification/lineE/logs/cert_*.json|.out` and `*_bounds.*`, regenerated with the fixed code by `code/run_certs.sh` (python-flint 0.9.0). All 9 × 4 sectors certified. The certified |μ*| bounds are identical to the refereed run; the sector-4 b11 midpoints differ by ≤ 1.3e-61.
- f_B class-sum certificates (195): `computations/verification/lineE/step2/cert_class.jsonl` (residues ±196 and ±4). The m = 17 certificate (`cert_class.py full 17 2.0 196,-196 7`, started 2026-10-30 06:39:56 UTC) was still running at commit time; `cert_class.jsonl` contains m = 5, 7, 11, 13 only and no m = 17 bound is claimed. The pre-registered prediction is in `step2/predictions.jsonl` (written 06:41:06 UTC).

- `zres_rebuild_check.log` (N4): `zres.c` now carries `#pragma GCC optimize("fp-contract=off")` and is built by `step2/build_zres.sh`, which refuses FMA builds. Without the pragma and flag GCC emits 10 FMA instructions; with the pragma, 0. The rebuilt kernel reproduces the committed m = 11 record bit for bit.
- `referee2_lean_rerun.log`: the second referee's `Audit57.lean` (exit 0; axioms ⊆ {propext, Classical.choice, Quot.sound}; its `#eval` controls print `false`) and `Neg57.lean` run from the repository. In `Neg57.lean`, `bad1` and `bad2` are rejected ("decide proved that the proposition … is false"). `bad3 : nsw 4 % 7 = 0` is **accepted**, correctly: j = 4 means m = 9 and 7 | h_9 (3 | 9), as `nsw_mod7` says. So `bad3` is a true statement mislabelled as a negative control in the referee file (copied unchanged); it is not a failure of the formalisation.
- `referee2_ivcert_rerun.log`: the second referee's interval kernel, run from its repository location; it reproduces the referee's m = 11 enclosures.

`receipt.json`: sha256 of the main integrated files (working tree at commit time), including the referee class-sum tables `T_*.npy` (N10), the ID assignment, the fixes applied (F1–F13, R1–R7, nits), the environment, and the m = 17 pre-registration record (external timestamp: push of e3b83dcb, PR #57 opened 2026-10-30T08:20:32Z).
