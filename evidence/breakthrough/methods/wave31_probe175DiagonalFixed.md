# Wave 31, task 5 — diagonal-model 175 draft with the `[NeZero N]` fix: BUILDS

## Result

`Built Bgs.Breakthrough.LineB175DiagonalFixed`, `Build completed
successfully (8706 jobs)`, **0 errors**, **5 sorry warnings** (exactly one
per theorem), olean 101,544 bytes. The wave-30 defect is fixed: the draft
now elaborates as written, modulo the one deliberate change below.

## The fix (and why threading `[NeZero N]` was not the right shape)

The wave-30 probe failed at `def TrU_diag` (probe line 166): the matrix
product `((kickMatInf N ĝ * catMat N (a N)) ^ m).trace` needs
`Fintype (ZMod N)`, which Mathlib provides only under `[NeZero N]`, and
`TrU_diag` took a plain `N`. The diagnosis suggested threading
`[NeZero N]` through the def and every use site — but the use sites in
`diagonal_175` / `diagonal_175_m1` apply `TrU_diag` inside lambdas
`fun N => ‖TrU_diag m ĝ a N‖ ^ 2` passed to `winAvg`, whose function
argument is a plain `ℕ → ℝ`: no membership proof is available inside the
lambda to conjure the instance, so threading the instance would force
statement changes to both main theorems.

Instead the fixed copy case-splits inside the def body, keeping the
signature and **all theorem statements byte-identical to the draft**
(diff vs the wave-30 probe is 21 lines: this doc comment plus the body):

```lean
noncomputable def TrU_diag (m : ℕ) (ĝ : ℤ → ℂ) (a : ∀ N : ℕ, ZMod N) (N : ℕ) : ℂ :=
  if h : N = 0 then 0
  else
    haveI : NeZero N := ⟨h⟩
    ((Tsum.kickMatInf N ĝ * catMat N (a N)) ^ m).trace
```

`N = 0` gives `0` by convention; for `N ≠ 0` the instance comes from the
negation and the trace is exactly the product trace where it is used.
`TrU_diag_hTrU` already quantifies `∀ [NeZero N]`, so it is unaffected
as a (sorry) statement.

## Setup

Copied `lean-drafts/LineB175DiagonalDraft.lean` (original untouched, md5
`b3adc11407f8d3533ca5f23379d1628e`) to
`Bgs/Breakthrough/LineB175DiagonalFixed.lean`, reusing the wave-30 probe's
stub block verbatim (`import Mathlib` plus stubs for `Dm`, `gp`, `window`,
`winAvg`, `Btup`, `Ztup`, `nuAvgUnits`, `kickMatInf`, `catMat`). One
sequential build, lake on PATH via elan bin.

## Build incident (honest)

The first launch (plain backgrounded exec) died silently: no lean/lake
process remained, the log stayed 0 bytes, and its session id became
unknown to the process tracker. The build was relaunched detached via
`nohup` and then ran healthily (lean ~2.4 GB RSS, no page-cache thrash).
Detached-build wall time ≈ 39 min (lean start 21:06 → olean 21:45 UTC);
the wave-30 probe of the same file took 2247 s, so this is in range.

## Warnings (cosmetic only)

11 unused-variable linter warnings, all in the stub block (e.g. stub `ĝ`,
`a` at lines 44/50) — none in the draft body, same count as wave 30.

## Caveats

Stubs are not main's definitions; the real flat main imports are
unverifiable in this test copy (no Derand/NAverage modules here). All 5
proofs are `sorry` — statement well-formedness only, not a proof.
Repository untouched.
