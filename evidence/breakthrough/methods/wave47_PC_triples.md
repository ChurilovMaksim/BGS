# Wave 47, task 4 — PC triple intersections and 1153²

## Verdict

TBD (pending runs).

## 1. Reduction: full PC follows from triples (q1, q2, 81)

Lemma (2-set Helly). Let F be an indexed family of subsets of a set,
with all pairwise intersections nonempty, containing a 2-element set
A = {a, b}. If every triple (F1, F2, A) has nonempty intersection,
then the total intersection is nonempty.

Proof. Suppose the total intersection is empty. Then a is killed at
some component qa (a not in Pi_qa) and b at some qb. If qa = qb, then
Pi_qa meets Pi_81 = A in nothing, against pairwise. So qa != qb, and
Pi_qa ∩ Pi_qb ∩ A is empty: a is killed at qa, b at qb. Contradiction.

Application. For a global pair at m = 24, Pi_81 is always exactly a
2-set (wave 46 §3, re-verified in code: 1680/1680 ordered fiber pairs
have |Pi| = 2), Pi_49 is always full (186/186), and pairwise
compatibility holds for all small pairs (wave 46, 16,211,212 joint
pairs, 0 failures). Hence full PC follows from the triples
(q1, q2, 81) for all component pairs (q1, q2): the 6 small triples
below, plus (q, 1153², 81) for q in {25, 121, 289, 512} (§3), plus the
trivial cases with 49 or 81 itself. No §3a dependence: the argument
uses only Pi sets of actual global pairs.

## 2. Small triples: exhaustive, 0 failures

Method: sigma-method (wave47_PC_triples.cpp). For a base triple, pick
a non-constant component as sigma-source; enumerate value-preserving
bijections sigma by backtracking, recurrence-pruned for the other
components (node cap 2000, exact direct fallback on overflow). Mate =
base o sigma, so jointness holds by construction and every joint
triple arises. Validated on pairs first: (81, 512) joint = 3,781,916
exactly as wave 46, 0 failures; (25, 49) joint = 12,114 exactly as
wave 46, 0 failures.

| triple | joint triples | failures | overflows (fallback) |
|---|---|---|---|
| (25, 121, 81) | 5,566,128 | 0 | 2,929,424 (all groups; exact fallback) |
| (25, 289, 81) | 29,246,376 | 0 | 994,928 (4,516,392 joint via fallback) |
| (25, 512, 81) | TBD | TBD | TBD |
| (121, 289, 81) | TBD | TBD | TBD |
| (121, 512, 81) | TBD | TBD | TBD |
| (289, 512, 81) | TBD | TBD | TBD |

## 3. Triples with 1153²

Method (wave47_PC_triples1153.cpp): enumerate joint pairs at (q, 81)
with sigma-source 81; for each common sigma != id, compute
V(sigma) = {(a, b) : s(a, b) o sigma in ker_1153} over F_1153.
dim 0: only D = 0, Pi full, OK. dim 1: Pi_1153 constant over D != 0
(scaling), checked once. dim 2: sigma must be dihedral, whose induced
class map lies in Pi_q, Pi_81, Pi_1153 (asserted); non-dihedral dim 2
falls back to brute force over all D. Bases with a constant component
reduce to pair checks, covered by §4.

| triple | joint pairs | sigmas | dim0 | dim1 | dim2dih | dim2non | failures | unresolved |
|---|---|---|---|---|---|---|---|---|
| (25, 1153², 81) | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| (121, 1153², 81) | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| (289, 1153², 81) | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| (512, 1153², 81) | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## 4. Pair searches (q, 1153²) and single 1153²

Method (wave47_PC_pairs1153.cpp): wave-44 cell method generalized.
Points (yq, s); cells = q-marginal x s-marginal groups; fibers by
pair-multiset hash + exact sorted keys; in a fiber only distinct
profile-pairs are checked (same profile-pair shares pi = s0, exact).

| check | points | fibers | pairs | failures |
|---|---|---|---|---|
| pair (25, 1153²) | TBD | TBD | TBD | TBD |
| pair (49, 1153²) | TBD | TBD | TBD | TBD |
| pair (81, 1153²) | TBD | TBD | TBD | TBD |
| pair (121, 1153²) | TBD | TBD | TBD | TBD |
| pair (512, 1153²) | TBD | TBD | TBD | TBD |
| single 1153² | TBD | TBD | TBD | TBD |

These close gap (2) directly, and cover the constant-component cases
of §3: constant-81 triples reduce to pair (q, 1153²) (Pi_81 full);
constant-q triples reduce to pair (81, 1153²); both-constant reduces
to single 1153².

## 5. What remains

TBD.

## Files

- This note: `methods/wave47_PC_triples.md`
- `wave47_PC_triples.cpp` (pairs + small triples),
  `wave47_PC_triples1153.cpp` (sigma/V triples),
  `wave47_PC_pairs1153.cpp` (cell pairs + single 1153²),
  `wave47_triples_all.log` (small-triple runs).
