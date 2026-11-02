# Wave 47, task 3 — L1* unit case at new prime powers: PURE COMPUTATION

## Verdict

Collision form CONFIRMED: 0 unexplained at 289, 361, 529, 343.
Sharp Stab equality REFUTED as a general identity: Stab(M) ⊆ predicted
in every group, equality rare. No proof attempted.

## Method

Same convention as wave46 `check_units`: units C in R/p^f grouped by
cycle multiset M(C) over one period T; violations = C outside the
dihedral orbit of the group rep; explained = C in {λ·o : λ unit,
o in orbit} (then λ ∈ Stab(M) automatically). Script:
wave47_L1star.py, validated by reproducing 25: 240/240, 0 unexplained.

## Counts

| mod | T | e=v_p(2T) | units | groups | violations | explained | unexplained | Stab = pred |
| 289 | 68 | 1 | 73984 | 168 | 60928 | 60928 | 0 | 32/168 |
| 361 | 190 | 1 | 129960 | 189 | 92340 | 92340 | 0 | 18/189 |
| 529 | 253 | 1 | 256036 | 517 | 122452 | 122452 | 0 | 11/517 |
| 343 | 147 | 2 | 86436 | 297 | 42336 | 42336 | 0 | 3/297 |

Total: 318,056 same-multiset collisions beyond dihedral, all explained.

## Stab form

Predicted {λ unit : λ ≡ ±1 mod p^{f−e}} has size 34/38/46/98.
Mismatches: 136 + 171 + 506 + 294, ALL proper subsets, 0 supersets,
0 incomparable. Examples: √2 at 289 has Stab = {±1} (size 2, not 34);
(1,0) at 529 and 343 has Stab = {1}. Surviving form: Stab(M) ⊆
predicted, not equality — the wave46 sharp form held only for its
checked examples (e.g. √2 at 25/49), not in general.

## Limits

Computation only. Units only; the non-unit degenerate locus (wave46 §4
counterexample) untouched. No Lean built, repository untouched.
