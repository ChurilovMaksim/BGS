# Wave 19, task 1 — milestone-1 draft: both defects fixed, builds with sorry only

CONCISE note. Test copy only; main repository untouched, nothing pushed,
one sequential `lake build` (no parallel Mathlib builds).

## Verdict: BUILDS

`lake build Bgs.Breakthrough.LemmaYM1Fixed` in
`~/workspace/bgs-formalization/formalization/` (toolchain v4.33.1,
Mathlib v4.33.1 oleans prebuilt): **built in 769 s, 8706 jobs,
13 `sorry` warnings, 0 errors.** The olean exists
(`.lake/build/lib/lean/Bgs/Breakthrough/LemmaYM1Fixed.olean`).
The original milestone-1 draft was NOT modified (md5 unchanged:
`84236274ff5bf2feaf23a188f361b140`).

## The two fixes (only changes vs the wave-18 probe body)

1. **Import first.** The fixed copy starts with `import Mathlib` at
   line 1, before any doc comment. The draft's `/-! -/` module doc
   before its import is what Lean rejected (`invalid 'import'
   command`, wave 18, line 71). The draft's long header doc is kept
   as a section doc after the import, which is legal.
2. **`componentY_mod3` type fix.** The quantifier now binds
   `r : Fin 4` and both class sums use `.val`:
   `∀ r : Fin 4, classSum m 4 y' r.val = classSum m 4 y (π r).val`.
   The draft bound `r : ℕ` (inferred from `classSum`'s `r : ℕ`
   argument) and then applied `π : Fin 4 → Fin 4` to it — ill-typed.
   Mathematical meaning unchanged: the four class sums of `y'` are
   a dihedral permutation of those of `y`. Diff vs the probe is
   exactly this one line plus the fix-note comment.

## Import-path flag (UNRESOLVED, needs reconciliation with main)

This test copy contains no Derand module at all, so the fixed copy
uses `import Mathlib` + the same Derand stubs wave 18 used
(`pellX`/`pellY` mutual recursion, `Dm`, `gp`, opaque `pellQ`/`pellP`
as `Nat → Int`). The draft writes `import Bgs.LineB.Derand`
(dotted); wave 6 verified the real path as the FLAT
`import Bgs.LineBDerand` (namespace inside `Bgs.LineB.Derand`).
Neither form is testable here. Before any real build against main,
re-verify the import line via the GitHub connector against the
then-current HEAD; do not guess it.

## Caveats (honest limits)

- Stubs are NOT main's definitions: statement well-formedness only.
  If main's `pellQ`/`pellP` are not `Nat → Int`, the `pellC1`
  statement's `.toNat` needs a cast fix.
- All 13 proofs are `sorry`: this is not a verification of any
  theorem, and the file must not enter main or be cited as proved
  until every `sorry` is replaced and the axiom audit is clean.
- Build cost on this VM: ~13 min for one Mathlib-importing module
  (I/O-bound olean loading); sequential builds only.

## Files (test copy + notes only)

- Fixed copy: `~/workspace/bgs-formalization/formalization/Bgs/Breakthrough/LemmaYM1Fixed.lean`
- Build log: `~/workspace/bgs-breakthrough/methods/wave19_fixed_build.log`
- Original draft (untouched): `~/workspace/bgs-breakthrough/lean-drafts/LineBLemmaYMilestone1Draft.lean`
- Wave-18 diagnosis: `~/workspace/bgs-breakthrough/methods/wave18_task4_elaboration.md`
