# Wave 26, task 3 — twin identity at m=48: PROVED

## Verdict

The twin identity is **proved in full** for qt ∈ {289, 332929}:
for every supported 2048-point p0 and every kernel point t mod qt,
sorted CRT(p0, a6, t) == sorted CRT(p0, a7, t) exactly (other
components zero, as in the wave-24 sweep). The proof is a general
lemma: it needs only period(p0) | 4, period(a6) = 12, a7 = a6∘σ,
and t of period L ∈ {8, 16} with half-period antiperiodicity.
Supportedness of p0 is not used. Repository untouched, no Lean.

## Setup

Positions Z/48, in 12-blocks. σ fixes odd positions and rotates
even positions by 8 within each 12-block: σ(2j) = 2j+8 mod 12.
Facts (verified): (σ1) σ preserves i mod 4; (σ2) σ acts blockwise,
hence permutes Z/12, Z/24, Z/48; (σ3) on one 12-block,
σ⁻¹ = [4,1,6,3,8,5,10,7,0,9,2,11], so σ⁻¹(c) − c ∈ {4, 0, −8}
for c ∈ Z/12 — in particular σ⁻¹(c) ≡ c (mod 4).

Orbit reps of the unique split 81-fiber (fiber 5, 36 points,
3 orbits of 12), 12-blocks:
a6 = [9,36,45,72,63,63,72,45,36,9,18,18] (×4),
a7 = [36,36,18,72,9,63,45,45,63,9,72,18] (×4),
a7 = a6∘σ (checked directly), a7 − a6 =
[27,0,−27,0,−54,0,−27,0,27,0,54,0] per block: divisible by 27,
zero on odd positions.

Component facts (all verified exactly):
- Supported 2048-points: 128 points, periods 1, 2, 4 (4 + 28 + 96).
  Period | 4 plus (σ1) gives p0∘σ = p0.
- 81 split-fiber points: all 36 have period 12.
- Kernel points mod p² are p·u with u a Fix sequence mod p
  (SNF seeds are multiples of p for every p² | D₄₈, g1 = g2 = p),
  so shift-by-k on t acts as M^k on u, M = [[6,−1],[1,0]].
- Matrix identities: M⁴ = −I, M⁸ = I (mod 17);
  M⁸ = −I, M¹⁶ = I (mod 577). Hence every t mod 289 has period 8
  with t_{j+4} = −t_j, and every t mod 332929 has period 16 with
  t_{j+8} = −t_j (both also checked directly on all kernel points).

## Proof

Let y = CRT(p0, a6, t), y′ = CRT(p0, a7, t), other components 0.
CRT is injective on (p0, a, t) triples, so sorted(y′) = sorted(y)
iff the triple multisets T = {(p0_i, a6_i, t_i)} and
T′ = {(p0_i, a7_i, t_i)} coincide. Since a7 = a6∘σ and p0∘σ = p0,
reindexing T′ by σ⁻¹ gives T′ = {(p0_j, a6_j, t_{σ⁻¹(j)})}.
Group positions by c = j mod 12: (p0_j, a6_j) = (p0_c, a6_c),
so it suffices that for every class c,
{t_{σ⁻¹(j)} : j ≡ c (mod 12)} = {t_j : j ≡ c (mod 12)}.
By (σ2), σ⁻¹(c+12k) = 12k + s with s = σ⁻¹₁₂(c), s ≡ c (mod 4).

Case L = 8 (qt = 289). Class-c values over k = 0..3 are
{t_c, t_{c+4}, t_c, t_{c+4}} = {t_c, −t_c, t_c, −t_c}, since
12k mod 8 ∈ {0, 4} and t_{x+4} = −t_x. The image class values are
{t_s, −t_s, t_s, −t_s}; s ≡ c (mod 4) and s − c ∈ {4, 0, −8}
give s ≡ c or c+4 (mod 8), hence t_s = ±t_c. Equal.

Case L = 16 (qt = 332929). Class-c values over k = 0..3 are
{t_c, t_{c+12}, t_{c+8}, t_{c+4}} = {t_c, −t_{c+4}, −t_c, t_{c+4}},
since 12k mod 16 ∈ {0, 12, 8, 4} and t_{x+8} = −t_x. The image
class values are {t_s, −t_{s+4}, −t_s, t_{s+4}} with s = c+4r,
r ∈ {−2,…,2}; by r mod 4 the pair (t_s, t_{s+4}) is
(t_c, t_{c+4}), (t_{c+4}, −t_c), (−t_c, −t_{c+4}), or (−t_{c+4}, t_c),
so the ±-multiset equals {t_c, −t_c, t_{c+4}, −t_{c+4}}. Equal.

Every class matches, so T′ = T, so sorted(y′) = sorted(y). ∎

## Why only 17 and 577

Kernel periods mod p² for the prime factors of D₄₈ (period of every
kernel point): 5→6, 7→3, 11→12, 17→8, 97→48, 577→16, 1153→24,
13729→48. The class argument needs L ∈ {8, 16}: the 12-step
pattern {12k mod L} must be sign-symmetric and stable under shifts
by multiples of 4 (the possible values of s − c). For other L it
fails in general. Explicit failure at qt = 25 (L = 6): kernel row 1,
t = [5,15,10,20,10,15]×8; class c = 0 has values {5,5,5,5} but its
σ⁻¹-image has {10,10,10,10} (12k mod 6 = 0 always, so the class
multiset is a single repeated value, moved by σ⁻¹). Sorted CRT
indeed differs for p0 = first rep of supported 2048-fiber 0.
This matches the wave-24 sweep: 0 survivors at every other qt.

## Computational confirmations

- Exact CRT identity at qt = 289: 11232/11232 combos
  (39 p0-first-reps × 288 nonzero t), not just mod-P.
- Exact CRT identity at qt = 332929: 200/200 random combos
  (all p0 in the fiber, all t).
- Class-multiset lemma directly: 0 failures over 3468 class checks
  at 289 (all t, all c); 0/24000 sampled at 332929.

## Scope limits (honest)

- Proved for the sweep setting: other components zero, p0 of period
  dividing 4, a6/a7 the 81-split reps. The lemma itself is general
  in (p0, a, t) as stated above, but it does not repair RB1 by
  itself: it explains why every (f2048 × split81 × f_qt) product at
  qt ∈ {289, 332929} contains mixing fibers — the counting repair
  of RB1 (multi-point f_qt, twin contributions) is still open.
- The 332929 full enumeration (13M combos) rests on the mod-P sweep
  plus the proof above, not on an exact full enumeration.
