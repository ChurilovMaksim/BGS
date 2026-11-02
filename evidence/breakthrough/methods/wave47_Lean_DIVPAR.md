# Wave 47, task 8 — Lean draft of V3 (DIV/PAR, wave 46 §1): DRAFT ONLY

## Verdict
NO VERDICT YET — NOT machine-verified. The file is written and
manually reviewed, but the sequential build has NOT finished after
3h01m (see below), so nothing here is claimed proved. The build was
left running detached and can be collected later; killing it would
discard 3h of progress.

## What was formalized (only V3, nothing else)
V3 from `wave46_GapG_DIV_PAR.md` §1: `v₂(P_{2^s−1}+1) = s` for `s ≥ 1`,
where `P` is the Pell-type sequence of the ν = (1,0) analysis,
`P 0 = 0`, `P 1 = 1`, `P (n+2) = 6 * P (n+1) - P n`
(so `P 1 = 1`, `P 3 = 35`, `P 3 + 1 = 36` — this is NOT the standard
Pell sequence `1, 2, 5`, it is the companion of `y_{n+1} = 6 y_n - y_{n-1}`).

File: `Bgs/Breakthrough/DivParV3.lean` in the test-copy project only
(`~/workspace/bgs-formalization/formalization/`), `import Mathlib` on line 1,
namespace `Bgs.DivParV3`. The repository was not touched.

## Statement form (exact)
The valuation is stated in exact-divisibility form, which is the content
of `v₂(n) = s` for `n ≠ 0`:
`(2:ℤ)^s ∣ P (2^s - 1) + 1 ∧ ¬ (2:ℤ)^(s+1) ∣ P (2^s - 1) + 1`.
No `padicValNat` corollary is included: that would need a positivity lemma
for `P`, which is out of this task's narrow scope.

## What is proved vs assumed (exact)
- PROVED from the definitions (no `sorry` in the file):
  `P_add` (addition formula, two-step induction),
  `P_two_mul_add_one` (`P_{2n+1} = P_{n+1}² - P_n²`),
  `P_mod4_pair` / `P_mod4` (`P n ≡ n (mod 4)`, two-step induction),
  the V3 step `v3_step` and the assembly `v3` (bases `s = 1, 2` direct).
- ASSUMED as an explicit hypothesis, NOT proved here: `hV1`
  (wave 44 §2: `v₂(P_{2^s}) = s`, same divisibility form).
  Only its divisibility half is used, to get `2^(s+2) ∣ P (2^s)^2`
  from `2s ≥ s + 2` at `s ≥ 2`. So `v3` is proved CONDITIONAL on V1.
- The full DIV/PAR theorems of wave 46 are NOT formalized here;
  this task is V3 only, per the narrow retry brief.

## Proof shape (mirrors the note)
Step `s → s+1` (`s ≥ 2`): with `A = P (2^s - 1)`,
`P (2^(s+1) - 1) + 1 = P (2^s)^2 - (A-1)(A+1)` (doubling identity).
`A ≡ 3 (mod 4)` gives `v₂(A-1) = 1` exactly; the induction hypothesis
gives `v₂(A+1) = s` exactly, so `v₂((A-1)(A+1)) = s+1` exactly
(odd × odd product argument). `v₂(P (2^s)^2) = 2s ≥ s+2`, so the
difference has valuation exactly `s+1` (ultrametric step via
`dvd_sub` / `dvd_sub'`).

## Build result (exact, at interim report time)
- Command: `lake build Bgs.Breakthrough.DivParV3` (sequential, single build;
  no other Lean build ran concurrently — verified by process list).
- Elapsed at report: 3h01m and still running (lake PID 1789, lean worker
  PID 2088, both detached via `setsid nohup`); worker CPU only ~182s (~2%);
  worker olean reads ~100 GB and growing; NO olean produced yet;
  build log `methods/wave47_DivParV3_build.log` still 0 bytes (no errors
  reported, `#print axioms v3` not reached).
- Sorry count in source: 0 `sorry` tactics (only the word in a comment);
  this is NOT a verified count — the build never reached the file's end.
- Axiom audit (`#print axioms v3` in the file): NOT YET AVAILABLE.
- Cause: VM oversubscription, not the file. Available RAM oscillated
  350–2247 MB (other tenants hold ~5.5 GB invisible to this cell's `ps`);
  the worker's pages are evicted as fast as read (RSS 70–526 MB, all
  10496 Mathlib oleans mapped). Precedent: sequential builds finished here
  in 769–1150 s under better conditions; this one thrashed instead.
- The first exec-launched attempt was lost when its session was reaped;
  the detached build above is the single build reported here. Collect it
  later from the log path and the olean path
  `.lake/build/lib/lean/Bgs/Breakthrough/DivParV3.olean` (absent so far).
