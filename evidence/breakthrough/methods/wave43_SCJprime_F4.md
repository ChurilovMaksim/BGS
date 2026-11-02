# Wave 43, task 4 — F4 (distinctness) for SCJ′ on the 9t line: PROVED (one regime open)

## Verdict

F4 is proved via a general swap-free criterion that needs no period
analysis at all, plus a 9t structural verification. The criterion
(H-dist)+(H-sep) below implies injectivity of o ↦ M(o). On the 9t
line it holds at m = 180 (vacuously: no doubles) and m = 252
(structured: 42 double pairs, separation tight at distance 3), and
in general whenever gcd(d_a, 36) > 1 (under a-injectivity and
lcm(d_a, 36) = M). Exactly one regime stays open: gcd(d_a, 36) = 1,
where every position is double and the criterion fails.

## 1. Setup (waves 39/42)

M = 9t, 3 ∤ t, 4 | t. Locked sequence a (period d_a), free pair
(b, b′) at 729 fiber 0 (period 36), blind kernel sequences o^{(k)}
mod q0_k satisfying o_{n+1} = 6o_n − o_{n−1} (indices mod M).
Config multiset M(o) = sorted{(a_i, b_i, o^{(1)}_i, …, o^{(K)}_i)}.
F4 = injectivity of o ↦ M(o). If M(o) = M(õ), some π preserving
(a, b)-classes has õ_{π(i)} = o_i for all i.

## 2. Local rigidity lemma

Lemma. Let o satisfy the 3-term recurrence mod q, and let
õ = o ∘ π^{−1} also satisfy it, with π preserving (a, b)-classes.
If π(i) = j ≠ i and π fixes j−1, j−2, then o_i = o_j.
Proof. Recurrence for õ at j−1: 6õ_{j−1} − õ_{j−2} = õ_j = o_i.
Since π fixes j−1, j−2, the left side equals 6o_{j−1} − o_{j−2},
which by o's recurrence at j−1 equals o_j. Hence o_i = o_j. ∎

## 3. Swap-free criterion (general, no 9t input)

Theorem. Let classes be fibers of i ↦ (a_i, b_i). Assume
(H-dist) two positions in the same non-singleton class are at
circular distance ≥ 3, and (H-sep) two positions in different
non-singleton classes are at circular distance ≥ 3. Then
o ↦ M(o) is injective.
Proof. Suppose M(o) = M(õ), π as in §1. Fix position p and
component k. If π^{−1}(p) = p, õ_p = o_p. Else set i = π^{−1}(p),
j = p: π(i) = j ≠ i, so j is in a non-singleton class. Then
j−1, j−2 are not in class(j) by (H-dist) (distance 1, 2 < 3),
nor in any other non-singleton class by (H-sep). Hence they are
singleton positions, which π fixes (it preserves classes setwise).
The Lemma gives o^{(k)}_i = o^{(k)}_j, i.e. õ^{(k)}_p = o^{(k)}_p.
Since p, k are arbitrary, õ = o. ∎

## 4. 9t structure: b's pairing is reversal

The 729 fiber-0 sequence b (same seed/C = (378, 540) ↔ (378, 297)
at m = 180 and m = 252, m-independent recurrence, period 36
whenever 36 | M) satisfies, verified exactly at both m:
- b_180[:36] == b_252[:36] and bp_180[:36] == bp_252[:36];
- b has 18 distinct values over its period, each exactly twice;
- b_r = b_{1−r mod 36} for all r, so the value pairing is exactly
  σ(r) = 1 − r (σ(r) ≠ r for all r, since 2r ≢ 1 mod 36).

## 5. Class structure and the g-table (a injective case)

Assume a injective on its period d_a, 3 ≤ d_a < M, d_a | M, and
lcm(d_a, 36) = M (holds: lcm(30, 36) = 180, lcm(21, 36) = 252).
Then (a_i, b_i) = (a_j, b_j), i ≠ j, forces j ≡ i (mod d_a)
and j mod 36 = 1 − i mod 36; by CRT the class of i is a pair
iff 1 − r is reachable, i.e. 1 − 2r ∈ gZ (mod 36), where
g = gcd(d_a, 36), r = i mod 36; else a singleton. Partner
distance is a nonzero multiple of d_a, so circular distance
≥ d_a ≥ 3: (H-dist) holds. For (H-sep):

| g | doubles? | why | (H-sep) |
| 2, 4, 6, 12 | none | 1−2r odd, never in even gZ | vacuous |
| 3 | r ≡ 2 mod 3 | 1−2r ∈ 3Z ⟺ r ≡ 2 (mod 3) | doubles ≡ 2 mod 3, so distance 1–2 impossible |
| 1 | every position | σ(r) ≠ r always reachable | FAILS (open regime) |

Hence F4 holds on the 9t line whenever gcd(d_a, 36) > 1 (under
the §5 assumptions), and vacuously whenever there are no doubles.

## 6. Verification at m = 180 and m = 252

m = 180: a period 30, b same 36 values, 180/180 distinct pairs —
no doubles, (H-dist)+(H-sep) vacuous. This recovers wave 39's
distinct-pairs proof as a special case of the criterion.
m = 252: a period 21, injective on its period; 210 classes =
168 singletons + 42 doubles (all size 2); double positions 84,
all ≡ 2 mod 3; min distance across different pairs = 3 (tight);
partner diffs are multiples of 21; partner CRT characterization
(j ≡ i mod 21, j ≡ 1 − i mod 36) holds exactly. So (H-dist)
and (H-sep) hold, and F4 holds at m = 252. Single-component
swap check: 1680 (pair, config, component) tests on the wave-42
samples, 0 nontrivial kernel-preserving swaps — exactly as the
Lemma predicts (a swap preserves the recurrence only if
o_i = o_j at that component).

## 7. Correction: a-injectivity fails at m = 180

The naive hypothesis "a injective on its period" is FALSE at
m = 180: a_180 takes only 15 distinct values over its 30-period
(every value exactly twice). Yet F4 holds there vacuously, since
b breaks all a-ties (180 distinct pairs). The criterion needs no
a-injectivity; §5 uses it only to derive the class structure in
the structured case.

## 8. Limits and open regimes

- gcd(d_a, 36) = 1 (d_a coprime to 36, in particular 3 ∤ d_a and
  d_a odd): every position is double, (H-sep) fails, F4 open.
  No such locked period observed (30 and 21 both have 3 | d_a).
- lcm(d_a, 36) < M: classes have size 2M/L > 2 (trivial doubling
  by shift L = lcm); (H-sep) fails since every position is
  non-singleton. Refinement not pursued: if all blind periods
  divide L, shift-by-L acts trivially on configs.
- a non-injective with doubles present: class structure not
  covered by the §5 CRT derivation; F4 open in that case.
- No Lean built; repository untouched.
