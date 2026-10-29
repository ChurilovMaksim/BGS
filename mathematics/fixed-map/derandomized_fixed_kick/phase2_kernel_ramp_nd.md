> **Packet copy (Line B, IDs BGS-TRACE-163 to 182).** On main at 502af245 the highest TRACE id is BGS-TRACE-162, so 163 is the next free id; the block was not renumbered. This is the detailed phase report cited by `../derandomized_fixed_kick.md`, copied unchanged below this box. Its status labels ([P], [P-sketch], [N], [C], [Cert], [L], [H]) are the working labels; the **integration status of every claim is the one in `../derandomized_fixed_kick.md` and `record/claims.json`**, which follow the referee's table (audit §8.10) with the second-reader upgrades of 167, 169 and 173 (`computations/verification/lineB/second_reader/SECOND_READER_REPORT.md`). Path map: `phase2/code/`, `phase2/logs/` → `computations/verification/lineB/phase2/`, `…/phase2/logs/`; `phase2/lean/Phase2Checks.lean` → `formalization/Bgs/LineBPhase2.lean` (`Bgs.LineB.Phase2`).

# Phase 2: arithmetic kernel, exact ramp, coincidence theory, moments (final; referee fixes applied 2026-10-29)

> Convention [ref-fix]: everywhere below, ξ ranges over the q-sequence group G ≅ Fix(T^m), T = [[0,1],[−1,6]], with V = Z[λ]/(λ^m − 1). This is the group actually used by all phase-2 code (`Orbits`). Γ is the dihedral group of shifts and reversals of q-sequences. The ECPP certificates of phase 3 upgrade every BPSW statement below to proven primality (phase3/REPORT3.md §6). The fixed-η off-diagonal W_m of §D2 is decomposed exactly in phase 3 into a parity part (solved) and a remainder (open).


Phase-1 notation is used throughout (REPORT.md §1). Phase-1 REPORT.md is frozen except for the [ref-fix] items.

**Labels.**
- **[P]**: proved here.
- **[P+L]**: proved, with the finite instances kernel-checked in Lean.
- **[N]**: numerical, with logs in phase2/logs.
- **[C]**: conjecture.

## A. The arithmetic kernel is a Ramanujan kernel [P]

**Proposition K.** For ξ, ξ′ ∈ 𝒮 there is t = t(ξ, ξ′) ∈ (1/g′)Z/Z, independent of ν, such that for every unit ν mod g′

  k_ν(ξ) · conj k_ν(ξ′) = D_eff⁻¹ · e(ν̄ t),  where ν̄ = ν⁻¹ mod g′.

Hence

  K(ξ,ξ′) = D_eff⁻¹ · c_{g′}(g′t)/φ(g′) = D_eff⁻¹ · μ(q)/φ(q),  where q is the exact denominator of t.

Here c_{g′} is the Ramanujan sum.

*Proof.*
1. ξ − ξ′ = ζ ∈ 𝒮 − 𝒮 = Rad^⊥. Since ℬ is nondegenerate on V/Rad and |V/Rad| = |Rad^⊥|, there is γ₁ with ℬ(·, γ₁) = ⟨·, ζ⟩.
2. ℬ takes values in (1/g′)Z, so ℬ(β, γ₁) = νℬ(β, γ) with γ = ν̄γ₁.
3. Hence −ν𝒬(β) − ⟨β, ξ⟩ = −ν[𝒬(β + γ) − 𝒬(γ)] − ⟨β, ξ′⟩.
4. Substituting β ↦ β − γ gives k_ν(ξ) = e(ν𝒬(ν̄γ₁) + ⟨ν̄γ₁, ξ′⟩) · k_ν(ξ′) = e(ν̄ t) · k_ν(ξ′), with t = 𝒬(γ₁) + ⟨γ₁, ξ′⟩. Here we used νν̄² ≡ ν̄ mod g′ and 𝒬 ∈ (1/g′)Z.
5. The identity holds for every integer representative ν̄, so e(g′t) = 1, i.e. t ∈ (1/g′)Z.
6. |k_ν|² = 1/D_eff by Prop. R. Averaging e(ν̄t) over units gives the Ramanujan sum c_{g′}(a)/φ(g′) = μ(q)/φ(q). ∎

**Check [N]** (logs/kernel_ramanujan.log, m = 2..7, up to 400×400 support pairs, all units):
- D_eff·K takes only the values μ(q)/φ(q), to within 6e-14.
- The phase law e(ν̄t) is confirmed.
- For odd m = 3, 5, 7 the only values are {1, −1/(h_m − 1)}, since h_m = 7, 41, 239 are prime.

So *K is a function of a single arithmetic invariant of the pair*: the "dual norm class" difference t. Pairs in the same class have weight 1/D_eff; other pairs are suppressed by 1/φ(q).

## B. Exact diagonal ramp for odd m, uniform in m [P]

**Lemma S (odd m) [P].**
- D_m = 4h_m², with h_m = Q_m/2 odd.
- V_2 ≅ Z/4 and Rad = V[4] = V_2.
- V^_2 = Fix(T) = the 4 constant q-sequences θ·𝟙 with 4θ ≡ 0, a cyclic group Z/4. [ref-fix: an earlier draft wrote Fix(S). The q-sequence group is Fix(T^m), T = [[0,1],[−1,6]], not Fix(S^m) by position sequence. Fix(S) also has 4 points but is Z/2 × Z/2.]
- 𝒮 = s + V^_odd for a single s ∈ Fix(T). In particular s is Γ-fixed, and ξ ↦ ξ − s is a Γ-equivariant bijection 𝒮 → V^_odd, with D_eff = h_m².

*Proof.* The 2-part of D is 4, so V_2 has order 4 and V_2 ⊂ V[4] ⊂ V_2. Fix(T) (the constant q-sequences) ⊂ V^[4] has order |det(T − I)| = 4, so it equals V^_2. Since Rad = V_2, the support condition ⟨γ, ξ⟩ = 𝒬(γ) for γ ∈ Rad fixes the 2-component ξ_2 = s and leaves the odd component free. ∎

**Lemma F (odd m) [P].** Let d | m. Then:
- every reflection of Γ fixes exactly h_d points of V^_odd of period dividing d;
- the rotation group fixes exactly h_d² such points (all period-d points).

*Proof.* A reflection fixing vertex c imposes Tr(λ^c(λ − λ⁻¹)x) = 0 on period-d points x. Then:
1. y = λ − λ⁻¹ = 4√2 has additive order h_d in V^(d) = O/(λ^d − 1): in Z[√2], λ^d − 1 = 2h_d ρ^d, and 2√2ρ^{−d} = 4b + a(2√2), where ρ^{−d} = a + b√2 is a unit, so gcd(a, b) = 1.
2. Hence |Fix| = D_d/h_d = 4h_d.
3. Its 2-part is V^_2 (of order 4), so its odd part has h_d elements. For odd d every reflection of Z_d fixes a vertex.
4. The period-d points form V^(d), with odd part of order h_d². ∎

**Theorem D (exact ramp, odd m) [P; checked against direct orbit counts for m ≤ 9, exactly].**

  2m − B_m^sym = h_m⁻² · Σ_{d|m} [ 2(m − d)·a(d) + d²·b(d) ],

where a(d) = Σ_{e|d} μ(d/e) h_e² and b(d) = Σ_{e|d} μ(d/e) h_e. Consequently

  B_m^sym = 2m − m²/h_m · (1 + O(λ^{−m/6})),  i.e.  B_m^sym/(2m) = 1 − (m/2h_m)(1 + o(1)),  with h_m ~ ρ^m/2 and ρ = 1 + √2.

*Proof.*
1. By Lemma S, Σ_{ξ∈𝒮}(2m − |Γξ|) = Σ_{x∈V^_odd}(2m − |Γx|).
2. For odd m a point of exact period d has orbit size 2d, or d if its orbit is reflection-symmetric. There are a(d) points of exact period d (Möbius inversion of h_d²).
3. By Lemma F and Möbius, each reflection fixes b(d) points of exact period d. A symmetric orbit of period d is fixed by exactly m/d reflections, so d·b(d) points of exact period d are symmetric.
4. Summing (2m − 2d)(a(d) − d·b(d)) + (2m − d)·d·b(d) over d gives the formula. The d = m term dominates, contributing m²(h_m − O(h_{m/3})) for the reflection-symmetric orbits. ∎

**Data.**
- Direct count = closed form for m = 1, 3, 5, 7, 9 (logs/deficit_odd.log): 1, 59, 1009, 11675, 112913 = Σ(2m − |Γξ|) over 𝒮.
- Ratio of the deficit to m²/h_m: 0.937, 0.984, 0.997, 1.0007, 0.99990, … → 1.
- For m = 41: B^sym/2m = 1 − 8.3·10⁻¹⁵.

So the diagonal ramp approaches the COE diagonal-approximation value 2m (2τ at τ = m/N → 0, fixed m) *exponentially fast and uniformly in m*, with the explicit leading correction m²/h_m. That correction is the self-retracing (palindromic) periodic orbits, which are counted once instead of twice.


**Addendum to Lemma S, proved for every odd m [P].** The all-ones vector **1** satisfies H·**1** = 4·**1**. So **1** ∈ Rad, and it has order exactly 4, because H⁻¹(2·**1**) = ½**1** ∉ Zᵐ. Hence V_2 = ⟨**1**⟩ ≅ Z/4, and 𝒬(**1**) = 2·**1**ᵀH⁻¹**1** = m/2 ≡ ½. The support condition ⟨γ,ξ⟩ ≡ 𝒬(γ) for γ = **1** and ξ = θ·**1** (θ ∈ ¼Z/Z) reads mθ ≡ ½. For odd m its only solution is θ = ½. So **𝒮 = ½·𝟙 + V^_odd for every odd m**, which matches support_shift.log for m ≤ 9. As a result the effective symbol at x ∈ V^_odd is c̃_k = (−1)^k c_k.

## C. Non-degeneracy (ND) and coincidences: task (1)

### C1. Exact correction formula (unconditional) [P]
B_m = Σ_{S(ξ)=S(ξ′)} K(ξ,ξ′). The Γ-related pairs give exactly B^sym = Σ_o |o|²/D_eff, because K is Γ-invariant and K(ξ,ξ) = 1/D_eff. Therefore

  **B_m = B^sym_m + E_m,  E_m = Σ_{S(ξ)=S(ξ′), ξ′∉Γξ} K(ξ,ξ′),  |E_m| ≤ #{non-Γ S-equal pairs}/D_eff,**

where K = μ(q)/(φ(q)D_eff) by Prop K. This makes Theorem 4 of REPORT.md unconditional in the form B_m = B^sym + E_m with an explicit E_m. At m = 6, E_m is the finite sum over the 14 ND-coincident adjacent orbit pairs listed in logs/nd2.log; phase 1 checked the value B_6 against it. What stays open is a *closed form* for E_m at every m (see C6).

### C2. p-splitting lemma [P]
Let p be prime, p ∤ M, and A: μ_{p^e} → Q(ζ_M) with Σ_w A(w)·w = 0. Then A(ζw) = A(w) for all ζ ∈ μ_p.
*Proof.* Q(ζ_M) and Q(ζ_{p^e}) are linearly disjoint over Q. Write w = ζ_{p^e}^r. A basis of Q(ζ_M)(ζ_{p^e}) over Q(ζ_M) is ζ_{p^e}^r with 0 ≤ r < φ(p^e). The only relations among the powers come from Φ_{p^e}(x) = Φ_p(x^{p^{e−1}}), i.e. from cosets of μ_p. ∎
*Corollary.* If A is supported on fewer than p points, then A ≡ 0. If all prime factors of the order of the roots exceed the support size, every vanishing sum vanishes formally (iterate over primes; this is the Lam–Leung / Conway–Jones mechanism in its easiest regime).

### C3. Galois covariance and the absence of hidden symmetries [P + finite computation]
- S(aξ) = σ_a(S(ξ)) for a ≡ 1 (mod 4), and multiplication by odd a preserves 𝒮. So rational S-equalities are Galois-stable. This is the only source of "arithmetic" coincidences apart from symbol symmetries.
- *Symbol symmetries.* Look for affine maps θ ↦ aθ + b on (1/n)Z/Z that preserve the aliased symbol f_n. They exist only for n = 7, where f ≡ 9/10 is constant on (1/7)Z and every unit a works.
  - For n ≤ 400 this is an exhaustive computation (logs/alias_symmetry.log; Lean `only_n7_has_symmetries` covers n ≤ 60).
  - For n ≥ 19 there is no aliasing. |c_k| = |c_1| forces a ≡ ±1. Since (10−i)/(10+i) is not a root of unity (its norm-1 Gaussian prime ratio is not a unit), a = 1 and b = 0.
- *Shifted-symbol structure (odd m).* Over 800, c̃_{±7} = (−360, 0) [ref23-fix], and every other real part lies in {0, −20, −40}. So Σ_{k∉±7} 2|Re c̃_k| = 320 < 360 (Lean `big_weight_separation`). The equal-coefficient classes of c̃ are {7,−7}, {6,−8}, {8,−6}, {5,−9}, {−5,9}, and every other k is alone (Lean `coefficient_classes`).

### C4. Theorem N: unconditional formal ND for NSW-prime m [P]
**Hypotheses.** m ≥ 3 is odd and h = h_m = Q_m/2 is prime with h > 28m. Let K = {k : c_k ≠ 0} (|K| = 14). The proof uses:
- (a) λ^d ≢ k′/k (mod h) for all d and all k ≠ k′ in K;
- (b) λ^a + λ^b ≢ 6 = λ + λ⁻¹ unless {a,b} = {1,−1}.

**Lemma [ref23-fix] (referee, phases 2+3 audit §2.2).** For odd m with h_m prime and h_m > 18, (a) and (b) hold automatically (Frobenius/conjugation argument: λ^d ∈ F_h forces λ^d = ±1; λ^a + λ^b = λ + λ⁻¹ forces {λ^a, λ^b} = {λ, λ⁻¹}).

*Proof as checked by the second reader [second-reader fix, 2026-10-29].* Let R = O/hO = F_h[t]/(t² − 6t + 1) and let σ be the conjugation √8 ↦ −√8, so σ(λ) = λ⁻¹ and R^σ = F_h. Since 2B² = h² + 1 for ρ^m = h + B√2 (ρ = 1 + √2, m odd), 2 is a square mod h, so R ≅ F_h × F_h always splits (the inert case never occurs). (0) ord_h(λ) = m: λ^m − 1 = h·2ρ^m ∈ hO, and λ^d ≡ 1 with d | m, d < m would give h² | Nm(λ^d − 1) = −4h_d² with 0 < h_d < h. (a) If λ^d = r ∈ F_h then σ gives λ^{−d} = r, so r² = 1, r = ±1; r = −1 would give m | 2d, hence m | d and λ^d = 1. So k′ ≡ k mod h, and |k − k′| ≤ 18 < h gives k = k′. (b) If u + v = 6 with u = λ^a, v = λ^b, then σ gives u⁻¹ + v⁻¹ = 6, so uv = 1 and u is a root of t² − 6t + 1. In R ≅ F_h × F_h this polynomial has four roots, (λ₁,λ₂) = λ, (λ₂,λ₁) = λ⁻¹, (λ₁,λ₁), (λ₂,λ₂), so “the two roots” is not enough; but u = λ^a has norm uσ(u) = 1, while the last two roots have norm λ₁², λ₂² ≠ 1 (λ_i = ±1 would give 1 ∓ 6 + 1 ∈ {−4, 8} ≡ 0 mod h). Hence u ∈ {λ, λ⁻¹}, v = u⁻¹, and {a, b} ≡ {1, −1} mod m (a = b is impossible since λ² ≠ 1). ∎ Exhaustive check for all twelve listed NSW-prime m with h > 18 (m = 5 … 1493): computations/verification/lineB/second_reader/code/sr167_admissibility.py. Hence the former word "admissible" is deleted: Theorem N holds for every NSW-prime m with h > 28m.

**Conclusion.**
(i) Every S-coincidence S(ξ) = S(ξ′) on 𝒮 is *formal*: the weight functions P ↦ Σ_{(k,j): kx_j = P} c̃_k on F_h are equal.
(ii) Outside a set NG of at most N_m·h points of V^_odd ≅ F_h², every S-equal pair is Γ-related.
(iii) Every point has at most 4m² formal partners. Hence

  **|B_m − B^sym_m| = |E_m| ≤ 8m²N_m / h_m,  N_m = C(14m,2) + m + m(m(m+1)/2 − 1).**

**Proof.**
- (i) By the Addendum, S(½+x) = Σ_{k∈K} c̃_k Σ_j e(kx_j/h) with x_j ∈ F_h. In S(ξ) − S(ξ′), at most 28m roots of unity of order h appear, with coefficients in Q(i). Since h > 28m, C2 applies.
- (iii) Write x_j = Tr(λ^j x) = Aμ^j + Bμ^{−j} over F_{h²} (μ an eigenvalue of λ, of order m). Then x_j = v has at most 2 solutions j for each v. At a point P the weight is −0.45·c₇(P) − r with r ∈ [0, 0.4], where c₇(P) = #{(±7, j) hitting P}, by C3. So formal equality determines c₇(·), hence the multiset {±7x_j}, hence {±x_j} (7 is invertible mod h). A partner x′ is determined by (x′₀, x′₁) ∈ {±x_j}², which gives at most 4m² partners.
- (ii) Call x generic if it satisfies:
  - G1: the 14m points kx_j are pairwise distinct and nonzero;
  - G2: x_a + x_b = x_{j−1} + x_{j+1} only for {a,b} = {j−1, j+1}.

  Each condition has the form Tr(yx) ≠ 0 with y ≠ 0. For G1 this uses (a) and ord(λ) = m; for G2 it uses (b), multiplied by λ^j. So each condition fails on a line of h points, and there are N_m conditions.

  Take x and x′ both generic and formally equal. The class of k = 1 is a singleton, so x_j = x′_{π(j)} for a bijection π. Then 6x_j = x′_{π(j)−1} + x′_{π(j)+1} = x_a + x_b, so by G2 π maps neighbours to neighbours. Hence π ∈ D_m and x′ ∈ Γx.

  Non-Γ pairs therefore involve a non-generic point: at most 2·N_m h·4m² ordered pairs, each with |K| ≤ 1/D_eff = 1/h². ∎

**Instances.** NSW-prime m are those with h_m prime (OEIS A088165 indices). All of the following satisfy every hypothesis (now automatic by the Lemma) (logs/nsw_admissible.log):

| m | log10 of the bound |
|---|---|
| 7 | 3.91 |
| 19 | 1.08 |
| 29 | −1.99 |
| 47 | −8.01 |
| 59 | −12.19 |
| 163 | −50.08 |
| 257 | −85.17 |
| 421 | −146.96 |
| 937 | −342.82 |
| 947 | −346.62 |
| 1493 | −554.66 |

- Primality is deterministic for m ≤ 47. For larger m it was BPSW here and is now ECPP-certified (phase 3, PARI `primecert` + `primecertisvalid`).
- m = 3 and m = 5 fail h > 28m. (Phase 1 checked ND exactly there anyway.)
- The m = 7 and m = 19 hypotheses are kernel-checked in Lean, including trial-division primality of 9 369 319 (`thmN_m7`, `thmN_m19_*`).

**Combined with Theorem D [ref23-fix]:** for each NSW-prime m, |B_m − B^sym_m| ≤ 8m²N_m/h_m = O(m⁵/h_m). The bound is nontrivial from m = 29 (it is 10^{3.91} at m = 7 and 12 at m = 19); from m = 47 on it is below 10^{−8}. This concerns the η-Bohr mean B_m, not F_m(η) at fixed η, and is proved only for the eleven listed m: whether infinitely many NSW primes exist is open.

### C5. Second-order ND (pair sums) [N, 40-digit floating point] [ref23-fix]
ND^{(2)} asks that S(o₁) + S(o₂) = S(o₃) + S(o₄) only trivially. It is needed for the fourth moment. I checked it with 40-digit mpmath on all orbit pairs (logs/nd2.log):

| m | Result |
|---|---|
| 2, 3, 5 | ND^{(2)} holds |
| 7 | ND^{(2)} holds (8.8·10⁶ pair sums). The 887 float-tolerance hits are near-misses with |diff| ≥ 6·10⁻¹⁴, not coincidences |
| 4 | fails: 5 non-trivial coincidences |
| 6 | fails: 1107 non-trivial coincidences, plus 14 ND¹-coincident adjacent orbits |

The m = 4 and m = 6 failures sit on small torsion: point orders 2–24 at m = 4, and {1, 4, 5, 7, 10, 20, 28, 35, 70, 140} at m = 6 (logs/nd2_orders.log). This is exactly the regime where the support sizes exceed the small prime factors and C2 does not apply.

### C6. What remains open in (1) [C = conjecture]
- **Conjecture ND-odd.** For every odd m, E_m = O(m^C/h_m). Theorem N proves this when h_m is prime (admissibility is automatic [ref23-fix]).
- For composite h_m, C2 applies prime-by-prime only when every prime factor p of h_m has p > 28m. Small prime factors (h_d | h_m for d | m, e.g. h_9 = 1393 = 7·199 with 7 = h_3) allow genuine vanishing sums. The torsion of order ≤ 28m that is needed has size ≤ Π_{d|m, small} h_d² and could in principle be enumerated. I have not done this in general.
- Even m: the 2-adic part (V_2 larger, 0 ∈ 𝒮) produces the small-torsion coincidences seen at m = 4 and 6. No closed form for E_m is derived.
- Honest status of "classify failures exactly": **not achieved for all m.** Proved instead:
  - every failure is a formal identity unless it lives on p-torsion with p ≤ 28m;
  - failures are absent for generic points of NSW-prime m;
  - an exact correction E_m with the bound above.

## D. Moments and the CLT: task (3)

### D1. Theorem G: joint (ν, Bohr-η) moments [P, conditional on ND^{(≤k)}]
Average over ν ∈ (Z/g′)^× and over the Bohr variable. Under ND^{(≤k)} (sums of k orbit values coincide only trivially, including relations with unequal numbers of terms (needed for E Z^aZ̄^b → 0) [ref23-fix]),

  E|Z_m|^{2k} = M_k := Σ_{|a|=k} (k!/Πa_o!)² Π_o w_o^{a_o},  w_o = |o|²/D_eff (ν-independent by Prop K),

and k!·B^k(1 − k²w_max/B) ≤ M_k ≤ k!·B^k with w_max ≤ 4m²/D_eff. Since w_max/B → 0, Z_m/√B_m → complex Gaussian in moments. This is a **conditional CLT**: exact at the verified finite m; the limit is conditional [ref23-fix].

Predicted joint M4/B² = 2 − Σ|o|⁴/(D_eff²B²): m = 3: 1.8738; m = 5: 1.99397; m = 7: 1.999754. These are rigorous at m = 2, 3, 5, 7, where ND^{(2)} is verified exactly.

### D2. Fixed η, averaging over ν only [N + reduction; the theorem is OPEN]
logs/fixed_eta_moments.log uses m = 9 (1188 units ν) and η = 25…1600:
- F/B = 0.97–1.07 for η ≥ 50;
- M4 = 1.93–2.04 and M6 = 5.5–6.4 (Gaussian: 2 and 6);
- |E Z²|/E|Z|² ≤ 0.09;
- KS distance of |Z|²/F against Exp(1) is 0.013–0.022, below the 5% critical value 0.039.

m = 7 and 8 behave the same way; m = 5 and 6 are noisier.

**Reduction [S] (superseded by phase-3 Theorem W) [ref23-fix].** Expand in the n-picture: F_m(η) = Σ_{n,n′} Φ̂(n)Φ̂(n′)* ρ(Q(n) − Q(n′)). The Γ-diagonal equals 2m − Δ_m(η). Δ ≥ 0 is exponentially small: reflections contribute ~κ^{(m−1)/2} with κ = Σ|ĝ|⁴. κ is computed in logs/s0_table.log, e.g. κ(25) = 6.0·10⁻³ and κ(100) = 1.7·10⁻³. So the fixed-η second moment is 2m − Δ_m(η) + W_m(η), where W_m is the non-Γ off-diagonal. **Proving W_m(η) = o(m) would give the fixed-η ramp; I have not proved this.** W_m is a sum of complete torus/Kloosterman-type sums over V. Weil-type square-root cancellation suffices only at the Gaussian scale, not uniformly in η. The fixed-η CLT (task 3) therefore remains **open**, with strong numerical support.

## E. Uniform-in-m window: task (2)

**Bohr side [P, odd m].** Theorem D gives 2m − B^sym_m = m²/h_m·(1+o(1)) uniformly. With C4, |B_m/2m − 1| is explicitly small for each listed NSW-prime m ≥ 29 [ref23-fix], with no restriction relative to N. For the remaining odd m this is conditional on Conjecture ND-odd.

**N-average side (Theorem U) [P].** Averaging over N ∈ (X, 2X], gcd(N, D_m) = 1 [ref23-fix],

  ⟨|Tr U_N^m|²⟩_N = F_m(η) + O( m·s2·s0^{2m−1}/X + D_m·min(s0^{2m}, D_eff)/X ),

with s0 = Σ|ĝ|, s2 = Σn²|ĝ|. So the N-average reproduces the ν-average F_m(η) uniformly for [ref23-fix]

  **m ≤ (1−ε)·c(η)·log X,  c(η) = 1/(log λ + 2 log s0(η)).**

Explicit constants (logs/s0_table.log):

| η | s0 | c(η) |
|---|---|---|
| 0.5 | 1.56 | 0.377 |
| 1 | 2.10 | 0.308 |
| 5 | 5.63 | 0.192 |
| 25 | 16.96 | 0.135 |
| 100 | 32.29 | 0.115 |

For comparison, the Ehrenfest time is m_E = log N/log λ = 0.567·log N.

So **the rigorous uniform window is a fixed fraction c(η)·log λ ∈ (0.20, 0.66) of the Ehrenfest scale for η ∈ [0.5, 100] (→ 0 as η → ∞; X ~ N)** [ref23-fix]. The N-average reproduces the ν-average F_m(η) uniformly for m ≤ (1−ε)c(η)log X. The value 2m is obtained only after the additional η-Bohr average (Theorems 4/5, N), or at fixed η for m ≫ m_*(η) under Conjecture R (phase 3/4); at fixed η and m ≪ m_*(η), F_m(η) ≈ 4m (phase-3 parity term).
- Reaching m up to (1−ε)·m_E needs control of the near-coincidence gap δ_m. The only rigorous bound I have is Liouville's, δ_m ≥ A^{−(d−1)}/800 with d ≤ 4√D, which is far too weak: it gives only m ≲ 2 log_λ log(τX) for the *fixed-η* (N-only) statement.
- Numerically, δ_m is much larger: the min nonzero pair-sum gap is 1.0·10⁻¹⁰ at m = 7 (nd2.log).

## F. Full 32-mode kick: task (4) — NOT DONE
Not attempted in this phase. The l ≠ 0 modes break the diagonal (Pell-norm) structure of Lemma Q. The CUE value m would require the off-diagonal Weyl modes to randomise the Γ-orbit phases, i.e. to kill the reflection half of 2m. No result is claimed.

## G. Lean (finite cores) [L]
File: phase2/lean/Phase2Checks.lean (copy built in /workspace/bgs-build/formalization/Bgs/). It uses `decide` only, with no native_decide, after `lake exe cache get`; Mathlib was not built from source. The build succeeded. `#print axioms` gives none or only [propext] (logs/lean_phase2.log).
- `thmD_matches_direct`: the Theorem D closed form equals the direct deficits 1, 59, 1009, 11675, 112913 for m = 1, 3, 5, 7, 9.
- `only_n7_has_symmetries` (n ≤ 60) and `n7_all_units`.
- `big_weight_separation` and `coefficient_classes` (symbol structure used in C4).
- `thmN_m7`, `thmN_m19_{h,prime,order,condA,condB}`: all Theorem N hypotheses for m = 7 and 19, including primality of 239 and 9 369 319 by trial division and modular-exponentiation Fermat inverses.

## H. Novelty and status summary
Labels: [P] proved here, [N] numerical, [C] conjecture, [L] Lean-checked.
- **New [P]:**
  - Prop K (Ramanujan-sum kernel);
  - Lemma S plus Addendum (support = ½ + V^_odd);
  - Theorem D (closed-form odd-m deficit, uniform in m);
  - the p-splitting reduction and the symmetry classification of the symbol;
  - Theorem N (explicit bound |B_m − B^sym_m| ≤ 8m²N_m/h_m; it holds for every NSW-prime m with h > 28m; the 11 listed m are those with h_m certified prime; nontrivial from m = 29) [ref8-fix];
  - Theorem G (conditional moment CLT);
  - Theorem U with explicit c(η).
- **Prior art:** Boasman–Keating 1995 (Fourier/Gauss expansion); NSW numbers and primes (OEIS A002315/A088165); Lam–Leung and Conway–Jones (vanishing sums).
- **Open:**
  - ND for all m (composite h, even m);
  - an even-m deficit formula;
  - the fixed-η (ν-only) limit law: numerically Gaussian, unproved;
  - the full Ehrenfest window;
  - the full-kick CUE value.

Reproduce: `cd phase2/code && <venv>/bin/python X.py` for each script listed in logs/, and `lake build Bgs.Phase2Checks`.
