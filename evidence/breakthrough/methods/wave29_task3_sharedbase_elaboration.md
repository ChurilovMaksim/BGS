# Wave 29, task 3 — Shared-base elaboration probe

## Verdict

The shared-base file **builds as written** (with stubs) — no defects at
all, unlike the M1/M2/M3 probes, which each needed fixes. This is
expected: the file already applies the fixed-copy fixes (import on
line 1; `r : Fin t` with `.val`; ascribed `Fin m` constructor plus
`hm : 0 < m` in `bijective_tau`).

## Method

- Original untouched: `lean-drafts/LineBLemmaYSharedBase.lean`, 508
  lines, md5 `bb74187a65449853e84ae6d9fa17b8fc` before and after.
- Probe copy: `Bgs/Breakthrough/LemmaYSharedBaseProbe.lean` (543
  lines). Line-1 flat import replaced by `import Mathlib` plus stub
  Derand definitions in namespace `Bgs.LineB.Derand`, following the
  M1/M3 pattern: `pellX`/`pellY` mutual recursion, `Dm` as in main's
  account, `gp` by main's formula, `pellP`/`pellQ` as the standard
  Pell sequences. The task named only `Dm, pellX, pellY, gp`, but the
  file also uses `pellQ`/`pellP` (in `pellC1`), so those stubs were
  added too — without them elaboration would fail on unknown
  constants. Body verified identical to the original modulo one
  blank separator line.
- One sequential `lake build Bgs.Breakthrough.LemmaYSharedBaseProbe`
  (lake on PATH via `export PATH="$HOME/.elan/bin:$PATH"`). No
  parallel Mathlib build, no thrash: lean ran at ~17% CPU, 2.7 GB
  RSS, steady progress.

## Result

- `⚠ [8706/8706] Built Bgs.Breakthrough.LemmaYSharedBaseProbe (1150s)`
- `Build completed successfully (8706 jobs).`
- Errors: **0**. Sorry warnings: **34**, exactly one per theorem
  (34 theorems; an initial count of 35 was a false positive from a
  doc-comment line starting with "theorems"). All 8 definitions
  (`seqFrom`, `IsFix`, `classSum`, `seqMultiset`,
  `perClassMultiset`, `IsDihedral`, `block`, `StabM`) elaborate
  cleanly.
- Olean exists: `.lake/build/lib/lean/Bgs/Breakthrough/
  LemmaYSharedBaseProbe.olean` (379 KB).
- Defect categories: **none**. Nothing to diagnose, nothing fixed.

## Caveats (standing)

- Stubs are not main's definitions; the real flat import
  `Bgs.LineBDerand` is unverifiable in this test copy (no Derand
  module here).
- All 34 proofs are `sorry` — statement well-formedness only, not
  a proof, and not for main. The transport from the milestone files
  to the restated theorems is still unproved by design (see the
  file's header).
- BGS repository untouched; no push; no other build run.

## Files

- Probe: `formalization/Bgs/Breakthrough/LemmaYSharedBaseProbe.lean`
- Build log: `methods/wave29_probeSharedBase_build.log`
- Original: `bgs-breakthrough/lean-drafts/LineBLemmaYSharedBase.lean`
