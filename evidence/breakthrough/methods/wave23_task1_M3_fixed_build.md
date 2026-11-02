# Wave 23, task 1 — milestone-3 fixed-copy build (TEST COPY ONLY)

CONCISE note. No file in the main repository was touched, nothing pushed.
Test-copy project: `~/workspace/bgs-formalization/formalization/`
(toolchain v4.33.1, Mathlib v4.33.1 oleans prebuilt). One sequential
`lake build` (no parallel Mathlib builds).

## Verdict: BUILDS

`lake build Bgs.Breakthrough.LemmaYM3Fixed` in the test copy:
**861 s, 8706 jobs, 0 errors, 6 `sorry` warnings, olean exists**
(`.lake/build/lib/lean/Bgs/Breakthrough/LemmaYM3Fixed.olean`,
183696 bytes). Same job count as milestones 1–2; the wave-22
full-Mathlib thrash did not recur (VM quiet, cache warm, lean
progressed steadily, no page-cache stall).

## Fixed copy

`Bgs/Breakthrough/LemmaYM3Fixed.lean` (test copy only), built from the
draft by script. Diff of the body vs the draft is exactly 5 lines —
the 3 diagnosed fixes from `wave22_task1_M3_elaboration.md`, nothing else:
(1) `import Mathlib` as the first command (draft's module doc before its
import is what Lean rejects; test-copy adaptation: flat
`import Bgs.LineBDerand` replaced by `import Mathlib` + the wave-22
Derand stubs, pellX/pellY mutual, Dm as in main);
(2) `pi2_pi3` (hypothesis `hπ₂`, conclusion) and `lemmaY_modD`: the
quantifier binds `r : Fin t`, class sums / per-class multisets use
`.val` (milestone-1 fix);
(3) `bijective_tau`: ascribed constructor
`(⟨σ i % m, Nat.mod_lt _ hm⟩ : Fin m)` plus a new hypothesis
`hm : 0 < m` (`by omega` cannot prove `σ i % m < m` for variable `m`).
The 6 `sorry` warnings are exactly the 6 theorems (`pair_lemma`,
`lemmaS`, `bijective_tau`, `pi2_pi3`, `lemmaY_modD`,
`support_union_fibers`); all 7 definitions elaborate cleanly.

## Environment note (for future probes)

First launch failed instantly with exit 127: `lake` is not in the
exec shell's PATH. Fix: `export PATH="$HOME/.elan/bin:$PATH"`
(elan toolchain dir holds `lake`/`lean`). The 127 run wrote no
build output and is not a draft defect.

## Caveats

- All 6 proofs are `sorry`: statement well-formedness only, not a
  proof, and nothing here is for main until every `sorry` is replaced
  and `sorryAx = 0`.
- Stubs are not main's definitions; the real flat import is
  unverifiable in this test copy (no Derand module here).
- Original draft untouched (md5 `0da6bda84d70d201712e0009244238f8`,
  as in wave 22).
- With all three milestones now building as fixed copies (M1: 769 s,
  M2: diagnosed, M3: 861 s), the whole Lemma Y chain exists as
  well-formed sorry-statements; the remaining work is proofs, not
  statement repair.

## Files

- Fixed copy (test copy only):
  `Bgs/Breakthrough/LemmaYM3Fixed.lean`
- Build log: `methods/wave23_probeM3Fixed_build.log`
- This note: `methods/wave23_task1_M3_fixed_build.md`
