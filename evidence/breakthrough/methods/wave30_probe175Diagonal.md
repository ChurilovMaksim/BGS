# Wave 30, task 5 — diagonal-model 175 draft: elaboration probe

## Setup (pattern of the wave-29 shared-base probe)

- Copied `lean-drafts/LineB175DiagonalDraft.lean` (196 lines, md5
  `b3adc11407f8d3533ca5f23379d1628e`, unchanged after the probe) to
  `formalization/Bgs/Breakthrough/LineB175DiagonalProbe.lean`.
- Replaced its two main imports (`Bgs.LineBNAverageUnits`,
  `Bgs.LineBDerand`) with `import Mathlib` plus minimal stubs for exactly
  the names the draft uses: `Derand.Dm`, `Derand.gp`;
  `NAverage.window`, `NAverage.winAvg`; `NAverageBridge.Btup`,
  `NAverageBridge.Ztup`; `NAverageUnits.nuAvgUnits`;
  `Tsum.kickMatInf`; `Expand.catMat`; empty `TraceFormula` /
  `NAverageM1` namespaces (only opened, never referenced).
- Body verified byte-identical to the draft past the import block.
- One sequential `lake build Bgs.Breakthrough.LineB175DiagonalProbe`
  (lake on PATH via elan bin); no thrash, no parallel build.

## Result: DOES NOT BUILD — exactly one defect

- Build: 2247 s lean job, 8706 jobs, **1 elaboration error, build failed,
  no olean**.
- The 5 theorems all elaborate: exactly 5 `sorry` warnings, one per
  theorem (`TrU_diag_hTrU`, `diagonal_175`, `diagonal_175_m1`,
  `diagonal_175_m1_units_mean`, `diagonal_175_m1_Z_values`).
- The single error, probe line 166, is in `def TrU_diag`:
  `((Tsum.kickMatInf N ĝ * catMat N (a N)) ^ m).trace` fails with
  `failed to synthesize HMul (Matrix (ZMod N) (ZMod N) ℂ) …`.
  Cause: matrix multiplication needs `Fintype (ZMod N)`, which Mathlib
  provides only under `[NeZero N]`, and `TrU_diag` takes plain `N`
  with no instance argument.
- Confirming evidence: the identical product inside
  `TrU_diag_hTrU`'s statement (which quantifies `∀ [NeZero N]`
  before the equality) produces no error — the instance in scope
  there is exactly what the definition lacks.
- Fix direction for a future fixed copy (NOT applied here):
  thread `[NeZero N]` through `TrU_diag` and every use site
  (`diagonal_175`, `diagonal_175_m1` currently apply it to bare
  window elements with no `NeZero` instance in scope), or
  reformulate the trace without `Matrix.mul` over abstract `N`.
  In main the same question will recur: the bridge's trace is
  stated under whatever `NeZero`/`Fintype` hypotheses main's
  `kickMatInf`/`catMat` carry, so the draft as written is not yet
  a drop-in instantiation.

## Cosmetic only

- 11 unused-variable linter warnings, all inside the probe stub
  block (lines 12–50), none in the draft body.

## Caveats

- Stubs are not main's definitions; the real flat
  `Bgs.LineBDerand` / `Bgs.LineBNAverageUnits` imports are
  unverifiable in this test copy (no such modules here).
- All 5 proofs are `sorry` — statement well-formedness only.
- BGS repository untouched.

Log: `methods/wave30_probe175Diagonal_build.log`.
