# Wave 22, task 1 — milestone-3 elaboration probe (TEST COPY ONLY)

CONCISE note. No file in the main repository was touched, nothing pushed.
Test-copy project: `~/workspace/bgs-formalization/formalization/`
(toolchain v4.33.1, Mathlib v4.33.1 oleans prebuilt). The M3 draft itself
was NOT modified (md5 `0da6bda84d70d201712e0009244238f8`, unchanged).

## Verdict

The milestone-3 draft does NOT build as written. It has the known
import-position defect (exact copy) plus TWO error categories in the
probe — three `π r` mismatches of the milestone-1/2 kind, and one
compound defect in `bijective_tau`. Everything else elaborates.
Caveat: the full-Mathlib probe did NOT complete (page-cache thrash,
below); the error categories come from a targeted-import probe instead.
All four errors are import-independent by reasoning (they concern the
draft's own definitions and core tactic behaviour), but a category that
only appears under full Mathlib cannot be excluded until a full build
converges.

## Defect 1 (blocking, exact copy): import after module docstring

File placed verbatim at `Bgs/Breakthrough/LemmaYM3.lean` in the test
copy. Build fails in 5.7 s, before any name resolution:

- `error: Bgs/Breakthrough/LemmaYM3.lean:17:0: invalid 'import' command,
  it must be used in the beginning of the file`
- Same as milestones 1–2: the long `/-! ... -/` header is a module-doc
  command; the import must move to line 1 (or the header must become a
  plain `/- -/` comment). Position defect, not a path defect — the
  flat `import Bgs.LineBDerand` (wave-21 fix) is already in the draft.

## Full-Mathlib probe did NOT converge (environment, not draft)

Probe `Bgs/Breakthrough/ProbeM3.lean` (`import Mathlib` + stub Derand
defs, M1/M2 pattern). First attempt: lean process gone after ~29 min,
empty log, no olean, no error. Second attempt, measured: 47.6 GB disk
reads in ~25 min with user CPU frozen (~2.7 s total), one thread stuck
in `read_extent_buffer_pages` — the documented page-cache-thrash
failure mode (TOOLS.md), here with a cold cache and only ~1.1–1.3 GB
RAM available against 6 GB Mathlib oleans. The build was killed, not
converged. An Init-only probe (`ProbeM3Lite.lean`) is uninformative:
`ZMod` itself is unknown without imports.

## Probe that worked: targeted imports, 60 s, 4 errors

Probe `Bgs/Breakthrough/ProbeM3T.lean`: `Mathlib.Data.ZMod.Basic`,
`Mathlib.Data.Finset.Basic`, `Mathlib.Data.Multiset.Defs`,
`Mathlib.Algebra.BigOperators.Group.Finset.Basic`,
`Mathlib.Algebra.BigOperators.Group.Multiset.Basic` + stub Derand defs
(`pellX`/`pellY` mutual, `Dm` as in main). Direct `lake env lean`:
60 s, exit 1, exactly 4 errors, 3 `sorry` warnings.

## Defect 2 (× 3): `π r` type mismatch, milestone-1/2 pattern

`classSum` and `perClassMultiset` take `r : ℕ`, so `∀ r` binds `r : ℕ`
while `π : Fin t → Fin t` is applied to it. Fix (diagnosis only, NOT
applied): the milestone-1 fix — bind `r : Fin t`, use `.val` on the
class sums / per-class multisets:

| probe line | theorem | expected type |
|---|---|---|
| 119:117 | `pi2_pi3`, hypothesis `hπ₂` (`π₂ r`) | `Fin 4` |
| 122:108 | `pi2_pi3`, conclusion (`π r`) | `Fin 4` |
| 136:131 | `lemmaY_modD` (`π r`) | `Fin (m.gcd 4)` |

NOT affected: `pi2_pi3` hypothesis `hπ₃` (`v' r` forces `r : Fin 4`)
and `lemmaS` (`(γ r).val` with `r : Fin 4` from `Finset.univ.filter`).

## Defect 3 (compound): `bijective_tau` hypothesis `hσbij`

Probe line 102:62: `Function.Bijective (fun i : Fin m =>
⟨σ i % m, by omega⟩)` fails with "Invalid `⟨...⟩` notation: the
expected type of this term could not be determined" — the codomain
`β` of `Bijective` is a metavariable, so the anonymous constructor
has no expected type. Fix part 1: ascribe it,
`(⟨σ i % m, ...⟩ : Fin m)`. Fix part 2 (verified by a separate test):
`by omega` CANNOT prove `σ i % m < m` for variable `m` — omega
treats `x % m` as an atom for non-literal modulus, and fails with or
without `0 < m` in context. Fix part 2: add a hypothesis `hm : 0 < m`
(`bijective_tau` currently has none: `P ∣ m` and `4 ∣ P` do not imply
`m > 0`) and use `Nat.mod_lt _ hm` instead of `by omega`.

## What elaborates

- All 7 definitions: `seqFrom`, `IsFix`, `classSum`, `seqMultiset`,
  `perClassMultiset`, `IsDihedral`, `StabM`.
- 3 theorems with only `sorry` warnings (probe lines 61, 79, 145):
  `pair_lemma` (T6.1), `lemmaS` (T6.2), `support_union_fibers` (T7.2).
- The 3 error theorems (`bijective_tau`, `pi2_pi3`, `lemmaY_modD`)
  have no `sorry` warning: their statements fail before the proof.
- Header-UNCHECKED spots now resolved: the `Fin`/`Multiset`/`Finset`
  notations and the `∑`-over-`Finset.univ.filter` sums of
  `perClassMultiset` values in `lemmaS` elaborate. The two-modulus
  version of T6.3 remains UNCHECKED by design (the draft states the
  one-modulus version only).

## Test-copy limitation (separate from defects 1–3)

This test copy has NO Derand module, so the real flat import is
unverifiable here regardless of path. Stubs mirror main's account
(`pellX`/`pellY` mutual recursion, `Dm m = 2 * (pellX m - 1)`,
`Nat → Int`), so the `(Dm m).toNat` cast in `lemmaY_modD` needs no
further check on the stub side — but stubs are not main's definitions.

## Caveats

- All 6 proofs are `sorry`: statement well-formedness only, not a
  proof, and nothing here is for main until every `sorry` is replaced
  and `sorryAx = 0`.
- The full-Mathlib probe must be re-run when the VM is quiet / the
  cache is warm before claiming the complete M1/M2-pattern verdict.

## Files

- This note: `methods/wave22_task1_M3_elaboration.md`
- Exact copy (test copy only): `Bgs/Breakthrough/LemmaYM3.lean`
- Full-Mathlib probe (did not converge):
  `Bgs/Breakthrough/ProbeM3.lean`, log `methods/wave22_probeM3_build.log`
  (empty — build killed during thrash)
- Targeted probe (diagnosis source):
  `Bgs/Breakthrough/ProbeM3T.lean`, log `methods/wave22_probeM3T.log`
- Init-only probe (uninformative): `Bgs/Breakthrough/ProbeM3Lite.lean`
