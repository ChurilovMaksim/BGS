# Line J: the d = 7 twisted coefficient in frozen R′ — exact sector law, certified growth, (±2,16), inheritance and a conditional refutation along m = 3p

Status: paper proofs, exact (integer/cyclotomic) checks, computer-assisted certificates (arb ball arithmetic plus float BLAS with
a-priori rounding bounds, as in Lines H/I), floating-point numerics and heuristics, each labelled below. Lean covers only small
arithmetic cores (`Bgs.LineJArith`, §9). Independent referee audit: `computations/verification/lineJ/referee/REPORT.md`:
* first round: ACCEPT AFTER FIXES (F1–F11);
* DELTA2: ACCEPT (DF8–DF10);
* J3 review: ACCEPT AFTER FIXES (J3-F1–F8);
* DELTA3: final verdict "ready to integrate", no blocking items.

The integration polish (L16-a, L16-b, citation check, J3-F8) is described in §10.

**Registered claims** (`record/claims.json`):

| § | claim | content | label |
|---|---|---|---|
| §2 | BGS-TRACE-221 | Prop J-C | [P + P-check] |
| §2 | BGS-TRACE-222 | sector-level antiunitary map | [P] |
| §3 | BGS-TRACE-223 | certificates | [CA] |
| §4 | BGS-TRACE-224 | window lemma | [P] |
| §4 | BGS-TRACE-225 | Theorem J | [CA] |
| §5 | BGS-TRACE-226 | Lemma L16 | [P] |
| §5 | BGS-TRACE-227 | (±2,16) negligibility | [CA] |
| §6 | BGS-TRACE-228 | inheritance theorem | [P] |
| §6 | BGS-TRACE-229 | prime-level complete sums | [P] |
| §6 | BGS-TRACE-230 | r(q) lemma | [P] |
| §7 | BGS-TRACE-231 | Theorem J3 | [CA, conditional] |
| §7 | BGS-TRACE-232 | H♮ | **open** |
| §7 | BGS-TRACE-233 | H_arg | **open** |

**BGS-TRACE-206 (frozen Conjecture R′) stays open.** No refutation is claimed. The packet is `computations/verification/lineJ/`, and the
integration record is `evidence/executions/20261031/lineJ/INTEGRATION.md`.

**Scope.** Everything here concerns the single-cosine **k1** kick 0.9 cos 2πq at η = 2 (ĝ(n) = iⁿJ_n(1.8)), with:
* the map S = [[3,4],[2,3]], λ = 3 + 2√2, m ≡ 3 (mod 6) (so 7 | h_m);
* the frozen definition of BGS-TRACE-206, with notation as in `lineI_rprime_reduction.md` §1;
* ρ ∈ {(2,8), (−2,8)} and, in §5, ρ ∈ {(2,16), (−2,16)}.

It says nothing about the Line B kick, Conjecture R (BGS-TRACE-179), R_NSW (BGS-TRACE-210) or BGS (BGS-BGS-001).

**Labels.**
* [P] paper proof (here or in the packet reports);
* [P-check] exact verification of a finite statement;
* [L] Lean-checked core;
* [CA] computer-assisted certificate;
* [N] floating-point numerics;
* [H] heuristic;
* [assessment] a judgement about routes, not a proof.

## 1. Set-up (from Line I)
Prop I2′ (BGS-TRACE-212) gives, for the d = 7 members t ∈ M₇(ρ), Z_t = ω_tZ_ρ/7 + Δ_t with |ω_t| = 1 and
Δ_t = 7⁻²Σ_{β≢0}Ẑ_ρ(β)G_t(β). Hence the frozen d = 7 deviation of ρ is cross_ρ + sq_ρ, where:
* sq_ρ = Σ_t|Δ_t|² ≥ 0;
* cross_ρ = 2Re(conj Z_ρ Σ_C Ẑ_{ρ,C}W_C(ρ, m)), with W_C = 7⁻⁴Σ_{t∈M₇(ρ)} conj G_t(0)Σ_{β∈C}G_t(β) summed over the 8 classes C of
  β ≢ 0 mod ±λ (6 elements each).

D7(m) := Σ_{ρ=(±2,8)}(cross_ρ + sq_ρ). The level 7 is included under the frozen cut-off (|Z_ρ|²/49 ≥ 4m) for every m ≥ 13 by BGS-TRACE-199.

## 2. Exact sector law and the leading coefficient — BGS-TRACE-221 [P + P-check], BGS-TRACE-222 [P]

**Sector decomposition.** This is checked exactly in `sectors_exact.py` and `logs/sectors_exact.json`. For each operator case (m mod 24 ∈ {9, 15, 21, 3}) and
each sign a = ±2, the 16-state G2 automaton of Line I has four rank-one sectors f_a, a ∈ {0, 2, 4, 6}, with A_nf_a = e(an/8)f_a.
* The complement is orthogonal to the read-out vector. Since the A_n are unitary and 8-periodic, the algebra they generate is a
  C*-algebra, so the complement is invariant and contributes 0.
* The read-out splits as J = Σ_a c_a(case, ρ), with |c_a| = ½ exactly in ℤ[ζ₈].

Hence Ẑ_ρ(β) = c_mΣ_a c_a(case, ρ)·⅓[Tr V_{β,a}^m − Tr E_{β,a}^m], where c_m = 1 − λ^{−m}. Here V_{β,a} and E_{β,a} are the twisted lifted vertex and
edge operators of Line I, with the automaton replaced by the scalar e(an/8) and the 3-cycle twist kept. So every top twisted orbit has
coefficient exactly ±(8th root of unity)/2 ≠ 0. This decides the question "c(β) ≠ 0", which BGS-TRACE-217 left open. As a float model
check [N], the formula reproduces the Line I class sums to ≤ 4e−7 (relative).

**Sector-level antiunitary map (BGS-TRACE-222) [P].** The letter weight is ĝ(n)e(Cn²/2)e(an/8)e(nτ_i(β)/7), with C = −4ac₀/8, so the sign of ρ
enters only through C ↦ −C.
1. Complex conjugation K (the disc centres are real, conj ĝ(n) = (−1)ⁿĝ(n) = e(4n/8)ĝ(n), and K M_C K = M_{−C}) gives
   K V^{(C)}_{β,a} K = V^{(−C)}_{−β,4−a}.
2. The reflection R: n → −n, s → −s, c → −c (rounding to cores is symmetric because λ is irrational) gives
   R V^{(−C)}_{−β,4−a} R = V^{(−C)}_{β,a−4}.
3. Combining the two: V^{(−2)}_{β,a+4} = (RK)V^{(+2)}_{β,a}(RK)⁻¹ with RK antiunitary. So σ(V^{(−2)}_{β,a+4}) = conj σ(V^{(+2)}_{β,a}) with
   multiplicities, and likewise for E.

This is BGS-TRACE-216 restricted to sectors. The sector operators do not depend on the case; only c_a(case, ρ) does. The referee's
Galerkin-level check covers all 64 pairs: sorted |entries| agree to 2e−41, and the top-6 eigenvalues are conjugate to 7.7e−15.

**Prop J-C (BGS-TRACE-221).** Write Ẑ_{±,C} = c_m(c^±_Cμ_{C,±}^m + ε^±_C). The leading part of cross₊ + cross₋ for class C is
2c_m²Re(B_Cξ_C^m), where ξ_C = μ*μ_{C,+} and **B_C = c₀ᶠ(c⁺_C − conj c⁻_C)W_C(+, m)**.

Proof ingredients:
* **W(−ρ) = conj W(ρ).** We have conj G_t(β) = G_{−t}(−β), C = −C and M₇(−ρ) = −M₇(ρ). This is also checked exactly in ℤ[ζ₇] (`exact_B.py`).
* **c₄ᶠ = −c₀ᶠ** for the Line F coefficients [P-check]. This is read from the exact sector table: c₄^{(case,−2)} = −c₀^{(case,−2)} in all 4 cases,
  and Line F's top sits in sector 4 for (−2) and in sector 0 for (+2) after conjugation (`fixes_checks.py`).

Exact values:
* **Sectors 2 and 6:** c⁺_a = conj c⁻_{a+4} = ½, so **B = 0 exactly** for every orbit in s2/s6. This covers the certified top of class 1:3
  (|μ₁:₃| ≈ 1.2837143, the largest twisted rate). The cancellation has to be exact, because 1:3's rate exceeds 2:1's, and it is exact,
  since it follows from the operator identity of BGS-TRACE-222. That the tops of 1:2 and 1:5 also lie in s6 is float-only [N] and is not
  used.
* **Sectors 0 and 4:** c⁺_a = −conj c⁻_{a+4}, so B_C = 2c₀ᶠc_a⁽⁺⁾W_C and |B_C| = |W_C|/2. The classes 2:1 and 0:1 **survive** (they double).
* **|W_C|.** |W_C| = (12/49)|cos(kπ/7)|, k ∈ {1, 2, 3}, or 6/49 when 7 | m, computed in arb from exact ℤ[ζ₇] histograms. W₂:₁ and W₀:₁
  are non-zero for all 28 residues j = m mod 168.
* **Period 168** [P + P-check]. (h_m, y′_m) are the coordinates of (1+√2)^m, and the order of 1+√2 mod 49 is 42 ([L]
  `pell49_period`). ν₀ ≡ ±2 (mod 7) is constant, and the sector constants have period 24. So B_C has period dividing lcm(24, 42) = 168.

When 7 | m (49 | h), all six dilations are units. Under the frozen rule M_d(ρ), level 7 then has exactly these 6 members; this is the
frozen definition itself.

## 3. Certificates — BGS-TRACE-223 [CA]
**Builder.** `certG_build_sector.py` is the audited Line I builder with the sector state factor (one state × 3-cycle).
* V: K0 = 5, ρ = 1.2, K = 60, β = 2.5, D = 1980.
* E: K0 = 4, ρ = 0.8, K = 40.

**Certifiers.**
* `rig_dom3b.py`: Line I v3, byte-identical.
* `rig_disc.py`: new. It is the same machinery on a small circle |z − c| = r, and the referee audited it line by line.
* `rig_spec.py`: Line H v4, rest mode.

The total perturbation in the count/disc certificates is pertT ≈ 2.37e−10, dominated by the deflation residual. Certified results:

| class (sector, +2 / −2) | count certificate | disc certificate (r = 1e−7) |
|---|---|---|
| 2:1 (s4 / s0) | exactly 3 eigenvalues in \|z\| > 0.8 | \|μ₂:₁\| ∈ [1.2835950326, 1.2835952326] |
| 0:1 (s0 / s4) | 3 in \|z\| > 0.9 | \|μ₀:₁\| ≤ 1.2624308 |
| 1:3 (s6 / s2) | 3 in \|z\| > 1.0 | \|μ₁:₃\| ≤ 1.2837144 |

* The orbits are {μ, ωμ, ω²μ} by the exact ℤ/3 symmetry.
* The other 58 V blocks are rest-certified with R ≤ 1.247 (Neumann order p = 64), and all 64 E blocks with R = 0.45.
* With μ* ∈ D(b₁₁, 2e−6) and |μ*| ∈ [1.9154712, 1.9154753] (Line F, BGS-TRACE-198):
  **|ξ₂:₁| = |μ*μ₂:₁| ≥ 2.4586893 > √λ = 2.4142136, and |ξ|/√λ ≥ 1.0184224**.

The referee reran the disc certificates, 3 count certificates and 12 rest certificates, plus a variant disc on the other orbit member.
All reproduce, and the negative control (r = 1e−8) fails as it should.

## 4. Window lemma and Theorem J — BGS-TRACE-224 [P], BGS-TRACE-225 [CA]
**Window lemma (BGS-TRACE-224).** Suppose θ ∈ [θ_lo, θ_up] ⊂ (0, π]. Then for any α, among N = ⌈2π/θ_lo⌉ consecutive k there is a k with
cos(α + kθ) ≥ cos(θ_up/2), and another with cos ≤ −cos(θ_up/2).

Proof: the closed arc of length θ_up ≥ θ around 0 (respectively π) cannot be jumped by steps of length θ. The first entry happens after
≤ ⌈(2π − θ_up)/θ⌉ ≤ N − 1 steps.
* [L] `window_step` is the real-line core.
* [L] `window_N` gives N = 6 and ⌈(2π − θ_up)/θ⌉ ≤ 5 for the constants below.

**Theorem J (BGS-TRACE-225) [CA].** Let m ≡ 3 (mod 6) and j = m mod 168. Let θ = 168·arg ξ₂:₁ mod 2π ∈ [1.1306771143, 1.1310541184] (from
both discs), so N = 6 and cos(θ_up/2) ≥ 0.8443062873.

For m ≥ M0(j), with cross₊ + cross₋ = 2c_m²Re(B₂:₁ξ^m) + 2c_m²Re(B₀:₁ξ₀:₁^m) + Err(m) (the 1:3 term vanishes exactly), we have
c_win|B₂:₁||ξ|^m > |B₀:₁||ξ₀:₁|^m + |Err|/(2c_m²). Err rigorously bounds all of the following:
* every non-top eigenvalue of all 64 V and 64 E (class, sector, sign) blocks (Lidskii and Weyl: Σ|λ|^m ≤ R^{m−1}‖·‖₁, with factor
  |c_a|/3 = 1/6);
* the Line F subleading error of Z₀ (H₀ = 2(T_V + T_E) ≤ 1506.18, uniformly in m since r₂ = 1) times every Ẑ, including class 1:3,
  whose leading part cancels exactly but whose product with the Z₀ error remains (relative rate μ₁:₃/ξ ≤ 0.52212);
* the square term (≤ Σ_ρ 6((6/7)Σ_C|Ẑ_C|)²);
* all Galerkin errors (inside the certificates).

The bracket divided by ξ_lo^m increases in m, because every subtracted rate is below ξ_lo: 0.98352 (0:1), 0.97150 (rest), 0.52212
(H₀ term) and 0.67024 (square). Using φ(2h) = φ(h) < h < λ^{m/2}/2:

> In every 6 consecutive terms m₀, m₀ + 168, …, m₀ + 840 of the class j with m₀ ≥ M0(j), there are m⁺ and m⁻ with
> **D7(m^±)/(m·φ(2h_m)) ≷ ±K_j·1.0184224^m/m**.
> Here M0(j) ∈ [297, 495] and K_j > 0 are tabulated per residue (packet `REPORT_v2.md` §3, `logs/assemble_v2.json`). From m₀ ≥ M1(j) ∈ [417, 621],
> both values are ≥ 1 in absolute value.

So the frozen d = 7, (±2,8) contribution φ⁻¹D7/m to W′/m is ≥ K_j·1.0184224^m/m in absolute value, **with each sign, for at least one
m in every 6 consecutive terms of each class j ≥ M0(j)**. This is not a statement for every m.

Per-residue table:

| j = m mod 168 | 7 ∣ m | \|W₂:₁\| | M0(j) | K_j | M1(j) |
|---|---|---|---|---|---|
| 3 | | 0.22065 | 339 | 0.2736 | 507 |
| 9 | | 0.05449 | 345 | 0.009975 | 513 |
| 15 | | 0.15269 | 351 | 0.1881 | 519 |
| 21 | yes | 0.12245 | 357 | 0.1367 | 525 |
| 27 | | 0.15269 | 363 | 0.2084 | 531 |
| 33 | | 0.05449 | 369 | 0.05093 | 537 |
| 39 | | 0.22065 | 375 | 0.3371 | 543 |
| 45 | | 0.22065 | 381 | 0.3426 | 549 |
| 51 | | 0.05449 | 387 | 0.06753 | 555 |
| 57 | | 0.15269 | 393 | 0.2368 | 561 |
| 63 | yes | 0.12245 | 399 | 0.1857 | 567 |
| 69 | | 0.15269 | 405 | 0.2428 | 573 |
| 75 | | 0.05449 | 411 | 0.07971 | 579 |
| 81 | | 0.22065 | 417 | 0.3616 | 417 |
| 87 | | 0.22065 | 423 | 0.3633 | 423 |
| 93 | | 0.05449 | 429 | 0.08465 | 597 |
| 99 | | 0.15269 | 435 | 0.2513 | 435 |
| 105 | yes | 0.12245 | 441 | 0.2003 | 441 |
| 111 | | 0.15269 | 447 | 0.2531 | 447 |
| 117 | | 0.05449 | 453 | 0.08828 | 621 |
| 123 | | 0.22065 | 459 | 0.369 | 459 |
| 129 | | 0.22065 | 297 | 0.042 | 465 |
| 135 | | 0.05449 | 471 | 0.08975 | 471 |
| 141 | | 0.15269 | 309 | 0.02464 | 477 |
| 147 | yes | 0.12245 | 483 | 0.2047 | 483 |
| 153 | | 0.15269 | 321 | 0.09275 | 489 |
| 159 | | 0.05449 | 495 | 0.09083 | 495 |
| 165 | | 0.22065 | 333 | 0.255 | 501 |

How the table is built:
* K_j = 4·bracket(M0)/ξ_lo^{M0}, with a 10⁻³ safety margin.
* The m⁻ side uses K_j⁻ = 2(2c²·bracket − sq)/ξ_lo^{M0}, which is ≥ the table value (F7).
* The referee reproduced M0 and M1 exactly with independent arb code, and got K_j⁺, K_j⁻ ≥ the table.

Inputs used as [P]:
* BGS-TRACE-197 (lifted trace identity);
* BGS-TRACE-198/199 (μ*, H₀, r₂ = 1, and the d = 7 cut-off for m ≥ 13);
* BGS-TRACE-212 (I2′);
* BGS-TRACE-213 (decomposition of W′);
* BGS-TRACE-216 (symmetries).

**What Theorem J means for R′.**
* By BGS-TRACE-213, W′_m = W′_A,m + φ⁻¹(D7(m) + O_m), where O_m collects the deviations of all other (ρ, d).
* W′_A ≥ −4m (Prop I8).
* **Corollary J (conditional).** If O_m ≥ −C·mφ(2h_m) for all large m, then W′_m/m → +∞ along the m⁺, and frozen R′ fails.
* In particular, frozen R′, R′_A and "O_m = o(mφ)" cannot all hold.

O_m is **not** controlled here. It contains:
* the other levels d | h_m (whose prime support is unbounded, BGS-TRACE-219);
* the (±2,16) members (but see §5);
* any further members of 𝓟*.

## 5. The (±2,16) members — BGS-TRACE-226 [P], BGS-TRACE-227 [CA]
**Exact blocks** [P-check] (`J3/code/blocks16_exact.py`). For each of the 16 cases (m mod 48 × a = ±2), the 64-state (a,16) automaton
splits into 8 mutually orthogonal invariant 2-dimensional monomial blocks (f₁^B, f₂^B):
* the entries lie in {0} ∪ ζ₁₆^ℤ;
* the supports are 32 and 64, so the block bases are orthogonal but not normalised;
* the A_n act diagonally or by a swap, with ζ₁₆ phases;
* 𝟙 lies in the span.

Deduplication by (sign, block action) leaves 32 distinct factors. As a float check [N], `wordtest16` gives max |diff| 1.1e−14 over
3200 words.

**Lemma L16 (BGS-TRACE-226) [P].** Let ρ = (a,16), a = ±2, m ≡ 3 (mod 6). Then

Z_ρ(m) = (1 − λ^{−m})Σ_B[Tr((I⊗J_B)𝐕_B^m) − Tr((I⊗J_B)𝐄_B^m)],

where 𝐕_B = Σ_nĝ(n)e(Cn²/2)V_n⊗A_{B,n} on the lifted vertex lattice, 𝐄_B is defined likewise on the edge lattice, and C = −4ac₀/16. There is a
twisted analogue with the cyclic 3-state factor.

J_B is the coordinate matrix G_B⁻¹F_B^*δ₀α_B^*G_B of (P_Bδ₀)(P_B𝟙)^* in the non-normalised block basis. ½ bounds its coordinate operator
norm (L16-b), and that is the norm used in the assembly.

Proof:
1. Use G2 (BGS-TRACE-203) per word, restricted to the reachable set.
2. Use the per-word lift Tr_H C_w = Tr V_w − Tr E_w of BGS-TRACE-197. Its proof is uniform in the real multiplier constant, here |C| = c₀/2.
3. Resum. Dominated convergence applies because
   Σ_w|c_w|‖V_{n_m}⋯V_{n_1}‖₁ ≤ (Σ_n|ĝ(n)|‖V_n‖₁)^m < ∞ (L16-a), using ‖XY‖₁ ≤ ‖X‖₁‖Y‖₁ and ‖X⊗A‖₁ = ‖X‖₁‖A‖₁.
4. Restrict to the blocks exactly. The A_n are unitary of finite order, so the complement of the block span is invariant too.

The hypotheses of BGS-TRACE-197 at the parameters used are asserted in arb by the builder. The referee re-derived J_B from first
principles on the author's JSON (to 5e−16), and its coordinate norm is ≤ 0.5000000000000001.

**(±2,16) negligibility (BGS-TRACE-227) [CA].** There are 576 rest certificates: 32 factors × {V, E} × {untwisted, 8 d = 7 classes},
all certified.
* The certified rates are R_untw ≤ 1.6677 and R_tw ≤ 1.2587.
* The cross rate R_untwR_tw ≤ 2.0991 is 0.8538·ξ_lo, and the square rate R_tw² ≤ 1.5843 is 0.6444·ξ_lo.

Via L16, Cauchy and the certified resolvent, ‖T^{m−1}‖ ≤ R^m·fullR/(1 − F). With the crude weights |W_C| ≤ 36/49 and the square part
included, the full d = 7 contribution X16 of ρ = (±2,16) satisfies:
* |X16(m)| ≤ 0.01·(K_min/2)·ξ_lo^m for every m ≥ 213;
* the same bound, including all composite-level inherited copies (factor ≤ σ(h)/h ≤ 1 + (m/2)ln λ, §6), for every m ≥ 243.

Here K_min = 0.0099848 is the minimum of K_j⁺, K_j⁻ over the 28 residues. It is ≥ the margin-reduced table value min K_j = 0.009975, so
the bound is ≤ 0.01·X7 wherever Theorem J's growth step holds.

The referee rebuilt 90 of the 576 certificates from scratch and re-certified them bit-identically, and independently recomputed the
assembly. The (±2,16) builds use the block basis `J3/logs/blocks16_exact.json`, sha256
814e4659b8868391df0bffd3ab509d1dcde1e878b43bc6fca06a52ffde073960 (J3-F8, §10).

## 6. Inheritance, prime levels and ranks — BGS-TRACE-228, 229, 230 [P]
**Inheritance theorem (BGS-TRACE-228) [P].** Let c, e be coprime odd integers with ce | h_m and c > 1, let d = ce, β′ ∈ O/c and β = eβ′
(O = ℤ[√2]). Then:
* (i) Ẑ^{(d)}_β = Ẑ^{(c)}_{β′};
* (ii) W_{d,β} = (n_e/e²)·W_{c,β′}.

Here n_e = #{j mod e : j a unit mod e, and ν₀ + (2h/d)j ≢ 0 mod ℓ for every prime ℓ | e with v_ℓ(h) = v_ℓ(d)} ≥ 0. It is independent of c, β′
and the sign of ρ. For a prime q: n_q = q − 2 if q ∥ h, and q − 1 if q² | h ([L] `count_excl_one`, `count_units` give the counts).

Proof:
* CRT: x/d ≡ xē/c + xc̄/e (mod 1).
* |G^{(e)}_u(0)|² = e² for units u, because x² − 2y² is non-degenerate mod odd e.
* The frozen exclusions are exactly "j a unit mod d".
* Mod c, (2h/d) ≡ (2h/c)ē, so j′ = ēj reproduces the level-c member set and its labels.
* The mod-e conditions are independent, which gives n_e.

The P-check compares class sums W_C in arb from exact integer histograms, to ≤ 9e−56 at (m, a, q) = (15, 2, 41), (15, −2, 31) and (33, 2, 23).

Consequences:
* Every composite-level copy of the d = 7 cross term is a **positive multiple** of it. Summed over the included levels, the factor is
  A_m = 1 + Σn_{D′}/D′² ∈ [1, σ(h)/h], the same for ±ρ, so the 1:3 cancellation persists.
* Square parts of every Dev_d are ≥ 0.

**Prime levels (BGS-TRACE-229) [P].** For a prime q ∥ h_m, completing the square gives conj G_t(0)G_t(β) = q²·e(N(β)t̄/q). The labels
t = jy′ cover F_q* except exactly one value t_b. Hence:
* W_{q,β} = q⁻²(−1 − e(N(β)t̄_b/q)), so |W_{q,β}| ≤ 2/q², for non-isotropic β;
* W_{q,β} = (q − 2)/q² for the 2(q − 1) isotropic β ≠ 0 (2 is a square mod q, since 2y′² ≡ 1).
* If q² | h, there is no missing label, and the values are 1/q² and (q − 1)/q².

The values reproduce numerically [N]: at q = 41, max q²|W| = 1.994 over the non-isotropic β and 39 over the isotropic β.

The suggestion that this suppresses the "slow-twist" danger on m = 3p is [H], not a proof.

**r(q) lemma (BGS-TRACE-230) [P].** For an odd prime q, let r(q) := ord_q(λ) in (ℤ[√2]/q)*. Then for odd m: q | h_m ⇔ r(q) | m.

Proof: with ε = 1 + √2 and ε̄ = −ε⁻¹, 2h_m = ε^m + ε̄^m = ε^m − ε^{−m} for odd m. So q | h_m ⇔ ε^{2m} ≡ 1 ⇔ λ^m ≡ 1.
* [L] `rank_core` is the ring identity used.
* h is the companion (V-type) sequence, so this is not the standard U-type rule.

Corollary: if r(q) = p is an odd prime, then q ≡ 1 (mod 2p).

On m = 3p (p prime, p ≠ 7), every prime q ≠ 7 dividing h_m has rank p or 3p, and 49 ∤ h_m, since λ has order 21 mod 49 ([L]
`pell49_lambda_order`). That small-rank levels would dominate D7 elsewhere, so that m = 3p is "forced", is [N, H] (`J3/code/levels_survey*.py`).

## 7. Theorem J3 and the remaining hypotheses — BGS-TRACE-231 [CA, conditional], BGS-TRACE-232, 233 (open)
**Definitions.**
* m = 3p with p prime and m ≥ 495 (= max M0(j) over j ∈ 3·(ℤ/56)*). Then j = m mod 168 ∈ 3·(ℤ/56)*, and 7 ∥ h_m.
* S⁺ = {m = 3p : cos(arg(B_jξ^m)) ≥ 0.84431}. This lies inside the window arc of Theorem J, since 0.84431 > c_win = 0.8443063.
* O♮_m is the sum of the cross parts over all (ρ ∈ 𝓟*, included d, β of conductor ∉ {1, 7}). It covers:
  * prime(-power) levels of rank p or 3p;
  * their inherited copies (positive multiples by §6);
  * mixed 7·c parts.

**Theorem J3 (BGS-TRACE-231).**
1. [P] Identity (BGS-TRACE-212, 213, 228): W′_m = W′_A + φ⁻¹[A_m·X7_m + X16_m + Q_m + O♮_m]. Here X7 is the d = 7 cross part of (±2,8),
   X16 is the d = 7 part of (±2,16) including its inherited copies, Q_m ≥ 0 collects the square parts, and A_m ≥ 1.
2. [CA] On S⁺, X7_m ≥ (K_j/2)ξ_lo^m (Theorem J). Also |X16_m| ≤ 0.01·(K_min/2)ξ_lo^m (BGS-TRACE-227), and W′_A ≥ −4m.

Hence on S⁺: **W′_m ≥ −4m + 0.99·K_j·1.0184224^m + φ⁻¹O♮_m**.

**S⁺ is infinite under H_arg.** Let α = 3·arg ξ/2π, and fix p₀ mod 56 with gcd(p₀, 56) = 1.
* For every integer H ≠ 0, insert 1_{p≡p₀(56)} = (1/56)Σ_k e(k(p − p₀)/56). Vinogradov's theorem (EXT-VINOGRADOV-1937: Σ_{p≤x}e(pγ) = o(π(x)) for
  irrational γ), applied to each Hα + k/56, then gives Σ_{p≤x, p≡p₀}e(pHα) = o(π(x)).
* The prime number theorem in arithmetic progressions (EXT-DAVENPORT-1980) gives #{p ≤ x : p ≡ p₀} ~ π(x)/24.
* The Weyl criterion (EXT-WEYL-1916) then shows that (pα) is equidistributed over p ≡ p₀ (mod 56).

On this class B_j is fixed, so S⁺ has relative density arccos(0.84431)/π = 0.18001 among primes p ≡ p₀ (mod 56), p ≥ 167.

[CA] `J3/code/rat_excl.py` (outward rounding) shows arg ξ/2π ∈ [0.88797591, 0.88797627]. It is not a rational with denominator < 1339; the
least denominator in the interval is 1339 (1189/1339).

**Corollary (dichotomy), in the referee's wording.** *Frozen R′ (BGS-TRACE-206) is false along m = 3p under H♮ and H_arg.
Unconditionally, if R′ holds, the conductor ∉ {1, 7} parts must cancel the d = 7 term exponentially on S⁺.* Precisely:
* assuming H_arg, R′ ⇒ φ⁻¹O♮_m ≤ −0.99K_j·1.0184^m + 4m + o(m) along the infinite set S⁺;
* without H_arg, the same holds along S⁺ whenever S⁺ is infinite.

**H♮ (BGS-TRACE-232, open).** For some δ > 0, O♮_m ≥ −(1 − δ)·0.99·(K_j/2)·ξ_lo^m for infinitely many m ∈ S⁺. A sufficient form is
|O♮_m| ≤ e^{o(m)}r^m with r < ξ_lo = 2.4587.

H♮ is substantive. It needs twisted-rate bounds that are uniform in the conductor, at unboundedly many conductors (BGS-TRACE-219). A
Parseval route is circular with R′_A, and no equidistribution theorem for twisted transfer products along hyperbolic toral orbits is
available. Evidence is [N/H] only (slow-twist survey, effective rate ≈ 1.0; generic radii ≤ 1.06).

**H_arg (BGS-TRACE-233, open).** arg ξ₂:₁/2π ∉ ℚ. Only denominators < 1339 are excluded [CA]. A sharper μ* enclosure can only raise
that bound; it can never prove irrationality. A possible removal route, not carried out, is Dirichlet for p mod 56b plus a
Jacobsthal-type gap bound and a finite check for small b.

## 8. Numerics and assessment (not claims)
**[N] m = 201…453** (`code/numerics_large_m.py`). The method uses the exact sector law with float spectra of the D = 1980 blocks and Z₀
from the Line F leading term, normalised by m·h (< m·φ). D7/(mh) values:

| m | D7/(mh) |
|---|---|
| 201 | −0.0023 |
| 249 | +0.164 |
| 333 | −0.409 |
| 375 | +0.969 |
| 381 | −0.939 |
| 435 | +1.38 |
| 441 | −1.43 |
| 447 | +2.18 |

* The two ρ halves of class 1:3 are equal and opposite in every row.
* The referee independently reproduced 8 of these values to all printed digits.
* W′ itself cannot be computed at these m.

**[assessment] Strategy** (packet `STRATEGY_v2.md`, after referee fix F10).
* Any proof of frozen R′ must show that O_m compensates D7 up to o(mφ); exact cancellation is not required.
* Frozen R′ should be regarded as false as an assessment, not a theorem. The uncontrolled O_m has unbounded prime support.
* Suggested replacement: an arithmetically corrected R′_corr, with explicit corrections at the levels where some
  r_tw(d, C)·|μ_ρ| > √λ. It is not registered.
* Proving R′_A in a residue class is not possible with current tools.

## 9. Lean
`formalization/Bgs/LineJArith.lean` contains no `sorry` and no `native_decide`; its axioms are a subset of propext, Classical.choice
and Quot.sound. It holds:

| theorem | content | claim |
|---|---|---|
| `rank_core` | ring core of the r(q) lemma | 230 |
| `pell49_period`, `pell49_periodic` | coordinates of (1+√2)^m mod 49 have exact period 42 | 221 |
| `pell49_lambda_order` | λ has order 21 mod 49 | 221, 230 |
| `count_excl_one`, `count_units` | n_q counts | 228 |
| `window_step`, `window_N` | window lemma real-line core and constants | 224 |

These are auxiliary finite facts only. The analytic and computer-assisted content of 221–231 is **not** formalised, and no claim is
labelled Lean-formalised beyond these statements.

## 10. Review record and integration polish
The referee report, with its first round, DELTA2, J3 review and DELTA3, is `computations/verification/lineJ/referee/REPORT.md`.

Integration polish, after the final verdict, is applied in the packet copy of `J3/REPORT_J3_v2.md`. The author's version is in
`pre_polish/`, with its sha256. Items:
* **L16-a.** The domination bound is written out.
* **L16-b.** J_B is a coordinate matrix in the non-normalised block basis.
* **Citation.** The v2 citation "Iwaniec–Kowalski Thm 13.6" was checked. IK Theorem 13.6 is Vinogradov's minor-arc estimate for
  ΣΛ(n)e(αn), as confirmed by several citing papers. Alone it does not give o(π(x)) for every irrational α, which also needs the major arcs.
  The text now cites Vinogradov's equidistribution theorem itself: *The Method of Trigonometrical Sums*, Ch. XI, recorded in
  Kuipers–Niederreiter Ch. 1 §2 Notes. IK Ch. 13 and Vaughan Ch. 3 are kept as chapter-level references, and the PNT in progressions
  replaces "Dirichlet" for the density.
* **J3-F8.** The basis sha256 is recorded (`J3/logs/SHA256_blocks16_basis.txt`; check `integration_checks/lineJ_J3F8_basis_provenance.py`).

## 11. Dependencies
* **Earlier claims:**
  * BGS-TRACE-183 (ν*);
  * 197 (lifted identity);
  * 198/199 (μ*, H₀, cut-off);
  * 203 (G2);
  * 206 (frozen R′);
  * 207 (finite monomial state factors, termwise);
  * 212 (I2′);
  * 213 (decomposition of W′);
  * 216 (symmetries);
  * 219 (unbounded prime support).

  BGS-TRACE-217 is not a logical dependency. Its certifier `rig_dom3b.py` (v3) is reused byte-identically as code, and 221 decides the
  question c(β) ≠ 0 that it left open.
* **External:**
  * EXT-VINOGRADOV-1937;
  * EXT-WEYL-1916;
  * EXT-DAVENPORT-1980.

  The standard Lidskii theorem and Weyl inequality for trace-class operators are used as in Line F and are not separately registered.
