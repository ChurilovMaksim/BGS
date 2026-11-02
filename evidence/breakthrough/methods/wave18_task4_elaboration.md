# Wave 18, task 4 — first elaboration attempt: milestone-1 draft (TEST COPY ONLY)

CONCISE note. No file in the main repository was touched, nothing pushed,
one sequential `lake build` at a time. Test-copy project:
`~/workspace/bgs-formalization/formalization/` (toolchain v4.33.1, Mathlib
v4.33.1 oleans prebuilt).

## Verdict

The draft does NOT elaborate as written, but it is exactly TWO defects
away from elaborating (modulo `sorry` warnings): one blocking
command-order error, and one type error in the last theorem. Everything
else — all definitions and 12 of 13 theorems' statements — elaborates.

## Defect 1 (blocking): import after module docstring — faithful copy

File placed verbatim at `Bgs/Breakthrough/LemmaYM1.lean` in the test copy.
Build fails in 2.8 s, before any name resolution:

- `error: LemmaYM1.lean:71:0: invalid 'import' command, it must be used
  in the beginning of the file`
- Cause: the draft's long `/-! ... -/` header is a module-doc command,
  and Lean requires `import` before every other command. The header must
  move below the import (or become a plain `/- -/` comment).

## Test-copy limitation (separate from defect 1)

This test copy is an old (Oct 29) snapshot: it contains NO
`LineBDerand.lean` and no `Bgs/LineB/` directory anywhere, so the
draft's `import Bgs.LineB.Derand` is unresolvable here regardless.
Additional flag: wave 6 verified the real module path as the FLAT
`import Bgs.LineBDerand` (namespace inside `Bgs.LineB.Derand`), while
this draft writes `import Bgs.LineB.Derand`. The import line needs
re-verification against current main before any real build.

## Defect 2 (only error in the probe): `componentY_mod3` type mismatch

Probe file `Bgs/Breakthrough/ProbeM1.lean`: draft with `import Mathlib`
first plus stub Derand definitions mirroring the draft header verbatim
(mutual `pellX`/`pellY`, `Dm`, `gp`; `pellQ`/`pellP` as opaque
`Nat → Int`, per the draft's `.toNat` use in `pellC1`). The draft
itself was NOT modified. Single sequential build: 1148 s, result:

- 12 `sorry` warnings only (probe lines 108–262, one per theorem).
- Exactly ONE error, probe line 283:49, in `componentY_mod3`:
  `Application type mismatch: argument r has type ℕ but is expected
  to have type Fin 4 in the application π r`.
- Cause: `∀ r, ...` binds `r : ℕ` (from `classSum m 4 y' r`), but
  `π : Fin 4 → Fin 4` is then applied to it. The statement as written
  is ill-typed; the quantifier and the `(π r).val` coercion do not
  line up (diagnosis only, no fix applied).

## UNCHECKED items from the draft header: all resolved by the probe

`Fin` addition/negation in `IsDihedral`, `Multiset` literals
(`{0,0,0,0}` etc. over `ZMod 3`), `Finset.range`/`filter`/sum notation
in `classSum`, `Nat.factorization`, `.primeFactors`, `ZMod` numeral
literals, and the `seqFrom` equation-compiler definition — every one
elaborates. No unknown-name, cast, or notation errors anywhere else.

## Caveats (honest limits of this probe)

- Stubs are NOT main's definitions: the real Derand import is still
  untested, and if main's `pellQ`/`pellP` are not `Nat → Int`, the
  `pellC1` statement's `.toNat` needs a cast fix.
- The probe proves statement well-formedness only; all 13 proofs are
  `sorry`, so this is not a verification of any theorem.
- Build cost on this VM: ~19 min for one Mathlib-importing module
  (I/O-bound olean loading); sequential builds only, as required.

## Files (test copy only, new directory, existing modules untouched)

- Faithful copy: `~/workspace/bgs-formalization/formalization/Bgs/Breakthrough/LemmaYM1.lean`
- Probe (stubs + draft): `~/workspace/bgs-formalization/formalization/Bgs/Breakthrough/ProbeM1.lean`
- Probe build log: `~/workspace/bgs-breakthrough/methods/wave18_probe_build.log`
