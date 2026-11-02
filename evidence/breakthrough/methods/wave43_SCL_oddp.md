# Wave 43, task 3 — SCL-poly for odd p: proved (e=1 unconditional, e=2 complete)

## Verdict

SCL (n_q ≤ 10) is already dead (wave 35: (816, 17⁴) has n_q = 18).
What Δ → 0 actually needs is not n_q ≤ 10 but Σ n_q s_q² ≤ poly(m)
(mechanism A). That is now proved for odd p. The tower bound, the
LTE level formula, and below-base vanishing assemble into a sharp
polynomial bound, and the last gap in level-2 vanishing (wave 39's
d ∈ {9,…,13} slot) is closed by exact factorization.

## 1. Setup (prior waves, cited)

R = ℤ[√2], α = 3+2√2, p odd, d = ord_𝔭(α) ≥ 3, e = v_𝔭(α^d−1) ≥ 1,
b = e+1. Component q = p^{2f} of D_m. Then (F2poly §0): p ∤ d,
component exists ⟺ d | m, and then f = e + v_p(m) (LTE; p ∤ d).
Tower (waves 36/37/39, odd p): genuine fibers are full preimages
of base fibers (LT1/LT2), degenerate fibers are exact p× lifts
(LT3), so for f ≥ b: N(f) ≤ (f−e)·N(b), where N(f) counts split
fibers at level f. Base bound (wave 38, orbit count):
N(b) ≤ 2p^{2e}/d. Below base (f ≤ e): level 1 by wave 32;
level 2 at e = 2 primes by wave 39 §2 (completed in §2 below).

## 2. Level-2 vanishing: complete for all e = 2 primes

Wave 39 §2 proves level-2 vanishing from (a) the all-distinct
case and (b) the paired case with swap-pair representatives.
Swap-pair existence: finite check for d = 14, 15, crude count
for d ≥ 15 (both wave 39, cited). The remaining slots were
whether any e = 2 prime has d ≤ 8 or d ∈ {9,…,13}. Both are
closed by exact factorization (factor D_d, compute ord/e):
- d ≤ 8: primes are 7(ord 3), 3(4), 41(5), 5(6), 239(7), 17(8),
  all e = 1. No e = 2 prime has d ≤ 8.
- d ∈ {9,…,13}: primes are 199(9), 29(10), 23(11), 353(11),
  11(12), 79(13), 599(13), all e = 1. No e = 2 prime has
  d ∈ {9,…,13}. (This was wave 39's only named gap.)
- d = 14, 15: the e = 2 primes are exactly 13 and 31
  (D_14, D_15 factored; other prime factors have e = 1),
  both covered by wave 39's level-2 census (0 split).
Hence level-2 vanishing holds for every e = 2 prime.

## 3. Theorem (SCL-poly, odd p)

Let p be odd, q = p^{2f} a component of D_m.
- If p ∤ m: f = e < b, below base ⟹ n_q = 0. (e = 1: level 1,
  wave 32. e = 2: §2 above. e ≥ 3: levels 2..e still open.)
- If p | m: f ≥ b, tower gives n_q = N(f) ≤ (f−e)·N(b)
  = v_p(m)·N(b) ≤ v_p(m)·2p^{2e}/d ≤ 2m^{2e}·log₂m
  (p ≤ m in tower regime; v_p(m) ≤ log₂m).
In particular: e = 1 ⟹ n_q ≤ 2m²·log₂m, unconditional;
e = 2 ⟹ n_q ≤ 2m⁴·log₂m, unconditional given e = 2;
under W_E (e ≤ E for all p) ⟹ n_q ≤ 2m^{2E}·log₂m
for every odd-p component.

## 4. Sharpness and checks

At base level (v_p(m) = 1), n_q = N(b). Exact values
(wave 38, reproduced by rerunning wave38_Nb_check.py):
p = 3: 1, p = 5: 2, p = 7: 5, p = 17: 18 (orbits Z = ∅ match
exactly, Z-invariance 0 bad). Consistency: (21, 7⁴) has n = 5
(wave 35); 3-part n_q ≤ v_3(m)·1 is exact at censused levels
(wave 42); (816, 17⁴) has n = 18 (wave 35).
Minimal 17-counterexample: (136, 17⁴). Here d = 8 | 136,
v_17(136) = 1, and v_17(D_136) = 4 verified exactly, so the
component sits at base level with n_q = 18 — same phenomenon
as (816, 17⁴) at the smallest possible m.
Trap: the d | m precondition is load-bearing, e.g. (40, 5)
has no 5-component (6 ∤ 40; v_5(D_40) = 0, verified).

## 5. Consequence for Δ → 0 v3

With s_q ≤ m² (wave 34) and ω(D_m) < 2.54m:
Σ_{odd q} n_q s_q² ≤ 5.08·m^{2E+5}·log₂m under W_E
(e = 1 part ≤ 5.08·m⁷·log₂m unconditionally).
Mechanism A, odd part (wave-35 v2 skeleton: N_A ≤ (Σ/4)·Q₂,
M_A ≤ 8m⁴, Q₂, S₂ ≤ 8m²): ΣΔ_F(A) ≤ 650·m^{2E+15}·log₂m
= o(D_m); under W₂: ≤ 650·m¹⁹·log₂m. So SCL drops out of
Δ → 0 v3 entirely, replaced by W₂ (verified to 10⁹) for the
odd-p part. Remaining hypotheses for Δ → 0 v3: H0 (proved),
W₂ (odd-p SCL-poly; open in general), SCJ′ (open), plus the
2-part polynomial bound (T_k pattern, modulo Gap G + U-lemma)
for the 2-part part of mechanism A.
Open (odd-p): below-base vanishing at levels 2..e for e ≥ 3
primes (none known); W_E / W₂ in general.

No Lean built, repository untouched. Checks: this note's
factorization/ord/e script (inline, exact integers) and
wave38_Nb_check.py (ALL CHECKS PASS on rerun).
