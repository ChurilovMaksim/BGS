# Wave 47, task 10 — Split-fiber periods: gap (3) of the T_k assembly

## Verdict

Gap (3) (wave46 §7) is CLOSED modulo exactly the standing T_k hypotheses
(Gap G, the 2-part U-lemma, the Drift Lemma) — no new named lemma is
needed. Proved here: 4 | p unconditionally; 8 ≤ p for every level
j ≥ 5 by an exact level-independent mod-32 computation; lift period
4p modulo drift-odd; NEW ratio p = 4o; and the induction giving
p ≤ N/4. A period here is a point's period; fibers are
period-homogeneous (invariant (d) below, verified at m ≤ 256).

## 0. Setup

Level j: N = m = 2^j, Q = 2^{2j+3}; kernel sequences y_{i+1} = 6y_i −
y_{i−1} mod Q; Γ = shifts + reversal; a fiber = equal sorted multiset;
split = ≥ 2 Γ-orbits; on-support = all 16 torsion conditions hold.

## 1. 4 | p — proved unconditionally

The period set {k : shift-by-k fixes y} is a subgroup of Z containing
N, so p | N = 2^j and p = 2^t. It remains to exclude p = 1, 2 for
points in split fibers. p = 1: constant sequence c; any point with
multiset {c × N} is c itself — singleton fiber. p = 2: y alternates
(a, b), a ≠ b; any fiber point has seed in {a, b}² (values are the
multiset), and (a, a), (b, b) give constant multisets ≠ target, so
the fiber is {(a, b), (b, a)} = one Γ-orbit (shift swaps them).
Hence no split fiber contains a point of period 1 or 2, so 4 | p.

## 2. 8 ≤ p — proved by exact mod-32 computation (script A)

Every period-dividing-4 point at level j is (Q/32)·r with r a mod-32
sequence: wave38(c) (SNF diag(12, 96)) gives exactly 128 such points
at every level, all on-support, with fixed Ŷ-set. Reduction: M^32 ≡ I
mod 32 (checked: M^4 ≡ [[5,20],[12,29]], M^8 ≡ [[9,8],[24,25]],
M^16 ≡ [[17,16],[16,17]]), so every seed (x, y) in the point's value
set {a, b, c, d}² is a kernel point for j ≥ 5 (its mod-32 period
divides 32 | N), and the full fiber is exactly the 16 seed sequences
with matching multiset — the multiset test 4·count_S(v) =
L_S·count_P(v) is level-independent (N cancels).
Result (wave47_Tk_periods_A.py): 128 seeds; period distribution
{1: 4, 2: 28, 4: 96}; 39 distinct fibers = 39 Γ-orbits; 0 split
fibers; 0 mixed-period fibers. (An early L = 1 slicing bug dropped
the 4 constant points, giving 36 fibers; the 36-vs-39 audit caught
it and the fix was verified.) Therefore no point of period dividing
4 lies in a split fiber at any level j ≥ 5, i.e. 8 ≤ p for every
point of an on-support split fiber. (All 128 points are on-support
by wave38(c), so the on-support qualifier changes nothing here.)

## 3. Lift period = 4p — proved modulo drift-odd

Let y at level j have period p (4 | p by §1), y' = ȳ + Qδ its lift,
D_r = δ_{r+p} − δ_r = C + Dr mod 4 (wave37; lift-independent since
4 | p). Drift-odd is C odd, D even, so D_r is odd for all r.
Then: p | q' (reduction mod Q has period p); q' | 4p since
δ_{i+4p} − δ_i = Σ_{k<4} D_{i+kp} = 4C + 4Di + 6Dp ≡ 0 mod 4
(D even, 4 | p ⟹ Dp ≡ 0 mod 8); q' ≠ p since D_i is odd; and
q' ≠ 2p since δ_{i+2p} − δ_i = 2D_i + Dp ≡ 2 mod 4 (2D_i ≡ 2 as
D_i is odd; Dp ≡ 0 mod 4). With q' | 4p and p | q', q' = 4p. ∎
Drift-odd is the Drift Lemma (standing; split ⟹ ν = (1,1) is Gap G).

## 4. NEW fibers have (o, p) = (2, 8) or (4, 16) — ratio 4

The 10 fully-colliding period-≤4 sources (wave38(c), j-independent
(Ŷ, e, C, D)) have block drift (script C, identical at m = 32, 64):
q = 4 sources: (C+Dr) = (3,1,3,1) or (3,3,3,3) (all odd) — lift
period 4t with t minimal such that t(C+Dr) ≡ 0 ∀r gives t = 4,
q' = 16, 4 lift orbits; q ≤ 2 sources: (C+Dr) = (2,2,2,2) — q' = 8
(q' = 2 excluded since δ_{i+4} − δ_i = 2 ≠ 0; q' = 4 needs
C+Dr ≡ 0), 2 lift orbits. Hence NEW fibers are (o, p) = (4, 16) ×5
and (2, 8) ×5, ratio exactly 4. Script D confirms this profile
parametrically at j = 5..10 (m = 32..1024) with no census, and the
OLD step 256 → 512: all 20 fibers lift to period 4p with 4 lift
orbits per point. Script B (census JSONs) confirms p = 4o for every
on-support split fiber at m = 32 (5 × (2,8)), 64 (10 NEW), 128
(10 NEW + 5 OLD (8,32)), 256 (10 NEW + 10 OLD (8,32), (16,64)),
max period = N/4 at every level.

## 5. Induction: p ≤ N/4

Invariant at level j ≥ 5, for every on-support split fiber F:
(a) p_F = 4o_F; (b) o_F ≤ 2^{j−4}; (c) o_F is a power of 2;
(d) all points of F have period p_F. Then p_F ≤ 2^{j−2} = N/4.
Base j = 5: script B, 5 × (o, p) = (2, 8). Step j → j+1:
NEW fibers satisfy (a)–(d) by §4 (o ≤ 4 ≤ 2^{j−3} for j ≥ 5).
OLD fibers are F' = ρ^{−1}(F) for a level-j on-support split fiber
F (Lemma P, modulo the Drift Lemma; wave36 §3 bijection): F'
lifting supported ⟹ o_F < 2^{j−4} (Lemma S, modulo Gap G +
U-lemma); by (c), o_F ≤ 2^{j−5}, so o_{F'} = 4o_F ≤ 2^{j−3} (type
rule o ↦ 4o); p_{F'} = 4p_F = 4·4o_F = 4o_{F'} by §3 and (a);
(c), (d) preserved (drift-odd is uniform on F). NEW-profile
completeness (no p ≥ 8 non-split orbit fully collides) is Lemma B
modulo Gap G via the Split Bit direction. ∎

## 6. What remains

Nothing new: gap (3) now rests only on the pre-existing T_k cluster
— Gap G (Split Bit side), the 2-part U-lemma (via Lemma S), the
Drift Lemma (drift-odd, via §3 and Lemma P) — plus the proved
wave37/38 inputs (type rule, Lemma B mechanism, (Ŷ, e, C, D)
j-independence). Unconditional closure of gap (3) needs exactly the
same work as unconditional T_k; the minor gap adds no dependency.
No Lean built, repository untouched.

## Files

- wave47_Tk_periods_A.py (mod-32 fiber census: 128 seeds, 0 split)
- wave47_Tk_periods_B.py (census fiber periods, m = 32..256)
- wave47_Tk_periods_C.py ((C, D) + lift periods of the 10 sources)
- wave47_Tk_periods_D.py (NEW to m = 1024; OLD step 256 → 512)
