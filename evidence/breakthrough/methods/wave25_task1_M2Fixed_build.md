# Wave 25, task 1 — milestone-2 fixed-copy build (TEST COPY ONLY)

CONCISE note. No file in the main repository was touched, nothing pushed,
one sequential `lake build` at a time. Test-copy project:
`~/workspace/bgs-formalization/formalization/` (toolchain v4.33.1, Mathlib
v4.33.1 oleans prebuilt). The M2 draft itself was NOT modified.

## Verdict: BUILDS

Fixed copy `Bgs/Breakthrough/LemmaYM2Fixed.lean` builds with sorry only:

- `⚠ [8706/8706] Built Bgs.Breakthrough.LemmaYM2Fixed (1115s)`
- `Build completed successfully (8706 jobs).`, `BUILD_EXIT: 0`
- **0 errors**, **12 sorry warnings** (one per theorem, lines 80, 85, 92,
  102, 112, 122, 128, 138, 149, 154, 163, 173)
- Olean exists: `.lake/build/lib/lean/Bgs/Breakthrough/LemmaYM2Fixed.olean`
  (255,952 bytes), plus `.ilean`, hashes, `.trace`
- Wall time 19m39s (`time` on the wrapper; lake reports 1115s)

This is statement well-formedness only: all 12 proofs are `sorry`, stubs
are not main's definitions, nothing here is for main until every `sorry`
is replaced and `sorryAx = 0`.

## Fixes applied (exactly the wave-20 diagnosis, nothing else)

Source: `bgs-breakthrough/lean-drafts/LineBLemmaYMilestone2Draft.lean`
(md5 `0c3421d9fab8eef85a9651ca6a17f22e`, unchanged before and after).
Diff vs the draft shows only the header/import/stub block plus:

1. Import moved to line 1: draft's flat `import Bgs.LineBDerand` (already
   flat after the wave-21 fix) replaced by `import Mathlib` + the wave-20
   probe stubs (`pellX`/`pellY` mutual recursion, `Dm` — the only Derand
   name the draft uses, at `v3_Dm`). The draft's `/-! -/` module doc was
   moved below the import, as in the wave-19 M1 fixed copy.
2. `π r` mismatch, four theorems — quantifier now binds `r : Fin t`,
   both sides use `.val` (`r.val` left, `(π r).val` right):
   `componentY_mod3pow` (Fin 4), `componentY_mod2pow`
   (Fin (Nat.gcd m 4)), `pattern_mod32` (Fin 4), `pattern_lemma` (Fin 4).
   Mathematical meaning unchanged.

All 7 definitions and all 12 theorems elaborate; the wave-20 UNCHECKED
cross-modulus `ZMod` casts in `scaling_bij`, `top_digit`, `doubling`
resolve, as in the probe.

## First attempt died, retry succeeded (provenance, honest)

The first foreground build session was killed at ~12 min with no output
and no olean (empty log — an artifact of piping through `tail`, which
buffers to end of stream). No thrash signature was seen before the kill
(lean CPU accumulating steadily, RAM available rising as the cache
warmed); the cause of the kill is unknown, and it was NOT a build
verdict. The retry ran detached (`nohup`, direct log redirect) with the
identical fixed copy and succeeded as above. No parallel Mathlib build
ran at any point; the build slot was verified free before each attempt.

## Test-copy limitation (separate from the verdict)

This test copy is an old snapshot with NO Derand module, so the real
flat import `Bgs.LineBDerand` is unverifiable here regardless of path.
The fixed copy uses `import Mathlib` + stubs, exactly as the wave-19/23
M1/M3 fixed copies did.

## Files

- This note: `methods/wave25_task1_M2Fixed_build.md`
- Fixed copy (test copy only): `Bgs/Breakthrough/LemmaYM2Fixed.lean`
- Build log: `methods/wave25_probeM2Fixed_build.log`
- Diagnosis applied: `methods/wave20_task1_M2_elaboration.md`
