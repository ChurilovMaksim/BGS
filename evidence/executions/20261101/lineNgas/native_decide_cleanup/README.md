# Legacy native_decide cleanup (1 November 2026)

Lean v4.33.1. `lake exe cache get` exit 0 (`lake_cache_get.log`). Each `native_decide` proof was replaced by `decide +kernel`
(kernel-checked, no `Lean.ofReduceBool` axiom) and the module rebuilt alone with a 100–240 s timeout and a memory guard
(trial killed when the summed `lean` RSS, including the shared .olean mappings of about 0.5–0.7 GB, passed 2.8 GB). Only proofs
that built within the limits were kept; statements are unchanged. Trials: `trials_summary.txt`.

**Count:** 88 uses in 12 modules → **37 uses in 8 modules** (51 replaced).

| module | before | after | kept native_decide, reason |
|---|---|---|---|
| HistoricalMobiusDegenerateFiber | 4 | 0 | — |
| PairKeySecondMoment | 4 | 0 | — |
| PellCohomology | 5 | 0 | — |
| CayleyCurveEnergy | 5 | 0 | — |
| CayleyEnergy | 21 | 2 | `k23_energy`, `k23_has_excess` (design (461,23,23)): memory guard |
| FibonacciRatioSmall | 5 | 2 | lines 85, 92: memory guard |
| MagneticTraceSmall | 5 | 1 | line 64: memory guard |
| TorusLevelSets | 5 | 3 | lines 62, 71, 83: memory guard / timeout |
| PellCoboundary | 7 | 3 | lines 45, 48, 51: memory guard / timeout |
| PairKeyFourthMoment | 3 | 2 | line 73: kernel "deep recursion detected" (insertion sort); line 76: memory guard |
| FourCutKernel | 2 | 2 | both: memory guard (unguarded first trial reached 5.8 GB in 45 s) |
| SevenPrimary | 22 | 22 | first 6 single-proof trials: 4 timeouts > 100 s, 2 memory guard; the rest not tried within the time box |

Builds: one module at a time (`lake_build_modules.log`), then `lake build` exit 0, "Build completed successfully (8862 jobs)",
no `sorry`/`sorryAx` (`lake_build_Bgs.log`; peak lean RssAnon 0.39 GB).
The boundary of BGS-CAYLEY-002 still says "by native_decide" for all five designs; it is a protected old-claim contract (the
wave2/wave3 integration audits reject an unreviewed amendment), so it was not edited. It is conservative: 19 of its 21 theorems
now need less trust than it states.

## Checks (branch final-p17-nd after merging origin/main 9a5bd186)
* `checks_branch.log`: 23 checkers incl. the 8 render `--check` scripts: 22 exit 0. `sync_return_sections.py --check` exits 1
  with "pandoc not found on PATH"; origin/main gives the same on this box (environment).
* `unittest.log`: 266 tests, 1 error, 1 skipped. The error is the 30 s subprocess timeout in
  `test_fractional_routing`; run alone it passes (`unittest_fractional_alone.log`, OK in 42 s), the environment-dependent
  behaviour already recorded in PR #66 (the test copies the built `formalization/.lake`).
