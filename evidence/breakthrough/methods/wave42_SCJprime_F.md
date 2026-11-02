# Wave 42, task 5 — SCJ′ hypotheses F1–F4 at m = 252

## Verdict

F1–F4 verified at m = 252 (9t line, t = 28), no failure found.
729 splits with top-digit pairs (F1); nine D_84 components fully
verified all-blind, eight of them also fully verified non-split
(F2); phase gap exactly 2π/3 for the counted fiber-0 pair (F3);
distinctness holds on every test, though the m = 180
distinct-pairs proof fails as stated (210/252 distinct pairs),
so F4 stays empirical with its proof open. The confirmed
section alone is superpolynomial (kills c_J ≤ 15 strictly,
≤ 18 with the 21743569 tier) and far below D_252^{1/3},
consistent with γ = 1/3. Polynomial SCJ fails at m = 252 too.

## 1. Setup

m = 252 = 9·28, 3 ∤ 28, 4 | 252, v₃(252) = 2, so
v₃(D_252) = 2·2 + 2 = 6: the full 3-component is 729
(D_252 % 2187 = 1458 ≠ 0). D_84 | D_252 (verified), and
D_84 = 2^7·3^4·5^2·7^4·11^2·13^4·83^2·113^2·239^2·251^2
·337^2·4663^2·75937^2·45697^2 (sympy factorint, product
checked). Locked component: 2401 (7^4), fiber-0 rep 0,
C = (0, 2107), period 21, v₃ = 1 (625 ∤ D_252:
D_252 % 625 = 50, so the m = 180 locked component is
unavailable here). Free pair: 729 fiber-0, C = (378, 540)
↔ (378, 297), k = 20 ↔ 11, period 36 — the same C values
as at m = 180.

## 2. F1: 729 splits with top-digit pairs — VERIFIED

729 has 2 split fibers. Fiber 0: 9 orbits, period 36,
C = (378, 27k), k ∈ {20, 10, 14, 4, 11, 1, 8, 25, 5},
with THREE top-digit pairs k ↦ k − 9: (20, 11), (10, 1),
(14, 5). Fiber 1: 3 orbits, period 12, C = (405, 162/81/
405), with one pair (405, 405) ↔ (405, 162). The counted
pair is fiber-0 (20, 11).

## 3. F2: D_84 components non-split + all-blind

Method: vectorized kernel enumeration mod q0 (seed solve);
per component: seed count == q0; 84-periodicity for every
nonzero o (v₃(period o) ≤ 1, the top-digit-law criterion
with locked period 21, v₃ = 1); direct multiset collision
across (b, b′) for every nonzero o; split-ness by
fiber-vs-dihedral-orbit-size comparison.
FULL, 0 failures everywhere (per84_fail = col_fail = 0,
split_fibers = 0):

| q0 | seeds | fibers | multi-fibers | split |
| 25 | 25 | 5 | 4 | 0 |
| 121 | 121 | 11 | 10 | 0 |
| 6889 | 6889 | 83 | 82 | 0 |
| 12769 | 12769 | 285 | 284 | 0 |
| 28561 | 28561 | 1105 | 1104 | 0 |
| 57121 | 57121 | 4200 | 4199 | 0 |
| 63001 | 63001 | 501 | 500 | 0 |
| 113569 | 113569 | 2197 | 2196 | 0 |

21743569 (4663²): FULL periodicity + collision run
(chunked k-congruence solver, both equations asserted):
seeds = 21743569 = q exactly, nonzero 21743568,
per84_fail = 0, col_fail = 0. Split-ness NOT checked
for this component (global fiber grouping over 21.7M
rows infeasible); it enters only the tier-2 total.
75937², 45697²: SAMPLED, 299 sequences each (y0 = 0
family + y0 > 0 family; valid y0 are exactly the
multiples of p, gg2 = q, A2 = 0): per84_fail = 0,
col_fail = 0. Split-ness not checked.
NOT blind components: 81 (split at m = 252, 2 split
fibers) and 2401 (split — the locked component).
Correction log: an early sampled run used the mistyped
modulus 5766436969 (≠ 75937² = 5766427969) and found
0 seeds — artifact of the wrong modulus, discarded;
all runs above use exact prime powers.

## 4. F3: phase gap — VERIFIED for the counted section

Wave-34 formula at 729, m = 252 (729 kernel points,
spreads ~10⁻¹⁴): free pair (fiber 14, orbits 14 vs 18)
has phases 0.116355 vs −1.978040, gap exactly 2π/3,
orbit sizes 36/36. Stab(a, b) = {rot 0} only, so the
diagonal orbit sizes of (a, b, o) and (a, b′, o) are
504/504 (full Γ, verified on a sample config). Hence
Δ_F ≥ 2·504·504·(1 − cos 2π/3) = 762,048 per fiber.
Caveat: fiber-1 (fiber 15) orbits all have phase π/3
(1.047198) — its top-digit pair is phase-degenerate
(gap 0) and contributes nothing; F3-as-used rests on
the fiber-0 pair only. (Also observed: the 9 fiber-0
orbits partition into 3 phase-triples spaced 2π/3.)

## 5. F4: distinctness — HOLDS ON ALL TESTS, proof open

The m = 180 proof fails as stated: (a, b) pairs are
NOT all distinct at m = 252 (210/252: 168 singletons
+ 42 doubles). Repeats come from b, which takes only
18 distinct values in its 36-period; repeat gaps are
all ≡ 0 mod 21 (a_i = a_j forces i ≡ j mod 21). So
the wave-39 permutation π may swap within the 42
double pairs, and a collision would have to act
through such a swap preserving kernel-ness.
Tests, all pass: full-tuple collision 100/100 random
full configs (Test A analog); sampled distinctness
30/30 differ-at-all + 30/30 differ-at-one; swap test:
200 random configs × 42 double pairs — 0 swaps
preserve kernel-ness at all 8 components, hence 0
collision candidates. F4 holds empirically at m = 252;
the general distinctness proof (needed for the
γ = 1/3 family claim) remains open.

## 6. Section total at m = 252

Tier 1 (8 fully confirmed components incl. split-ness):
B = 3106096230378831595493305228225 ≈ 10^30.49;
total ≥ B · 762,048 ≈ 2.37×10^36, killing c_J ≤ 15
(252^15 ≈ 1.05×10^36). Tier 2 (adding 21743569):
B ≈ 6.75×10^37, total ≥ 5.15×10^43, killing
c_J ≤ 18 (252^18 ≈ 1.68×10^43). Both are far below
D_252^{1/3} ≈ 10^64.31 (log10 D_252 = 192.92), so the
section is consistent with γ = 1/3; the full D_84
product would give ~D_252^{1/3}. The remaining
unconfirmed D_84 mass (75937², 45697², sampled only)
can only raise the total.

## Limits

No Lean built; repository untouched. Scripts:
wave42_blind_m252.py (full checks + samples),
wave42_m252_big21743569.py (background full run),
wave42_phases_distinct.py (phases, Test A,
distinctness, swap test, totals).
