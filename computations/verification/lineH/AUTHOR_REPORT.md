# Line H — report (final for this session, 2026-10-30 ~19:50 UTC+5)

Status tags: [P] paper proof, [CA] computer-assisted (arb + rigorous float error bounds), [Lean], [N] float numerics, [C] conjecture.

## 0. Summary (revised after the referee audit /workspace/audit/lineH/REPORT.md, verdict ACCEPT AFTER FIXES; all fixes applied)
* **H2 [CA].** Line B diagonal kick f_B, η = 2, s = −1 (ν* with **N ≡ +196** mod h_m), 49-state lifted operators (BGS-TRACE-197
  applied to TRACE-194).
  * V_0 has exactly one eigenvalue in |z| > 1.5. It is simple, with **1.846834 ≤ |μ*| ≤ 1.946835** (outward), well above
    λ^{1/4} = 1.553774.
  * All other spectrum: V_0 \ {μ*} in |z| < 1.5, V_2/4/6 in |z| < 1.45, E_* in |z| < 1.
  * Certificate of record for V_0: the referee's ref_rig.py. The author re-ran everything with the archived rig_spec.py v4
    (√2·γ_{2n+2}, padded inputs, code sha256 recorded).
* **Consequence [CA + P]: W̃rest_m(2)/m ≥ 1.4e4 for every odd m ≥ 47 with 3 ∤ m.**
  * **Conjecture R (TRACE-179), as stated, is false.**
  * R_NSW is violated at every m ≥ 47 with h_m prime (whether there are infinitely many such m is unknown).
  * The conclusion of TRACE-196 (s = −1) holds on the lifted space; H∞,7 as stated is neither proved nor needed.
  * Not covered: odd m with 3 ∤ m in {17,…,43}, every m with 3 | m, η ≠ 2, and s = +1.
* **H1 [N + P-conditional]:** see §1. Not reviewed by the referee. Line G m = 17 pre-registered test: all 15 bands PASS.
  The lifted cross-validation converges only for (2,4), with radius 1.4956.

## 1. H1 (Conjecture R′): status: NOT proved. Evidence plus a conditional reduction.

### 1.1 Evidence (numerical, pre-registered) [N]
* The Line G pre-registered m = 17 test (k1 kick, η = 2) passed all 15 bands. The Line G watcher ran it, not Line H.
  I re-hashed the prediction file and it matches sha256 fa8505f5…, and I read the log `bgs-lineG/logs/eval17_k1.log` myself.
  * Total F/2m = 39.0651.
  * Bulk F/2m (H = 8) = 2.0249.
  * Predicted resonant part Res/2m = 37.0184; actual = 37.0191.
  * W′_act/m = +0.092 with the formula-table definition, or +0.050 with the bulk definition.
* W′_act/m for k1, m = 9, 11, 13, 15, 17: −0.82, −0.31, −0.04, +0.23, +0.09. Line G's caveat was a monotone upward drift. That drift
  reversed at m = 17. Five points cannot establish o(m), so this is support for R′, not a proof.

### 1.2 Conditional reduction (what a uniform spectral gap would and would not give) [P, conditional]
Setting (Line G): ν has height b if ν ≡ a·b⁻¹ (mod 2h) with |a| ≤ b (rational reconstruction). Then Z_m(ν) is expressed through
b-dependent transfer operators L_{a,b,k} (k mod b). Suppose the following hypothesis holds.
> (UG) There are A, C, δ > 0 such that, for every non-resonant primitive (a,b) with b ≤ B, Z_m(ν) is a combination
> Σ_j c_j Tr L_j^m of at most C b^A operators with |c_j| ≤ C b^A and trace norms ≤ C b^A, all of spectral radius ≤ λ^{1/4} − δ.

Then, by Lidskii plus Weyl (|Tr L^m| ≤ ρ^{m−1}‖L‖₁), |Z_m(ν)|² ≤ C³ b^{6A} (λ^{1/4}−δ)^{2m}. There are at most 3H² values ν of height ≤ H,
and φ(2h) ≫ h/log log h with h ≍ λ^{m/2}. So the non-resonant ν of height ≤ H contribute at most
C″ H^{2+6A} log log h · ((λ^{1/4}−δ)²/λ^{1/2})^m = C″ H^{2+6A} e^{−c m} log m to F_m. That is o(1) for every H ≤ e^{c m/(3+6A)}, i.e. H ≤ h^{ε}.
**Consequence and obstruction.** Even (UG), which is not proved, only controls heights up to h^{ε}. The heights h^{ε} ≲ b ≲ √h carry the
bulk mass 2m (the RMT term), and there the number of operators and their dimension grow with b while m ≍ log h. A fixed-operator
spectral bound with the threshold λ^{1/4} is then useless: the Weyl constant alone is ≥ b^A ≫ λ^{m/4}. So W′ = o(m) needs a genuine
equidistribution or mean-square statement for the bulk Z_m(ν). It is essentially the RMT statement itself, and it does not follow from
any spectral gap. This is a structural reason why H1 is hard. It is not a proof that it is hard.

### 1.3 Numerical spectral-radius scan: inconclusive (honest failure) [N]
`code/h1_scan.py` (m = 13, k1, b ≤ 12, K = 8, |n| ≤ 5) computed Galerkin spectral radii of the Line G (a,b,k) operators.
* For |a|/b ≲ 0.2 the radii are 1.14–1.27, below λ^{1/4} = 1.5538. Examples: (±1, 3) gives 1.14 and 1.21; (±1, 5) gives 1.26 and 1.27.
* For larger |a|/b the multipliers e^{2π|4ac0/b| n ρ} make the truncated matrices extremely non-normal. The computed "radii" (11.07 at
  (±2, 4), 36.7 at (±3, 5), 1733 at (1, 1)) are truncation artefacts: they contradict the known actual growth rates of those families
  (≤ 1.92). They are **not** evidence of anything.

A meaningful scan needs the lifted/certified machinery of §2 for each (a,b). I did not complete it.

### 1.4 Lifted cross-validation of the Line G (a,b,k) operators (m = 13, k1) [N]
`code/h1_lift.py` builds the Line F vertex/edge lift (discs at integers, radius r) ⊗ A_n^{(b)} on C^{b²}, with the multiplier e(coef·n·u),
coef = −4ac₀/b. Results: `logs/h1_lift.log` and `logs/h1_conv.log` (cfg1: K0 = 3, r = 0.8, K = 24, |n| ≤ 5), `logs/h1_conv2.log`
(cfg2: K0 = 4, r = 0.7, K = 32, |n| ≤ 7). Leading |eig V|; the E radius is 0.35–0.40 in all cases.

| (a,b,k) | family N ≡ b/a | single-disc (h1_scan) | lifted cfg1 | lifted cfg2 | verdict |
|---|---|---|---|---|---|
| (−1,3,1) / (1,3,2) | ∓3 | 1.1388 / 1.2069 | 1.1400 / 1.2082 | – | agree (1e-3) |
| (−1,5,3) / (1,5,2) | ∓5 | 1.25806 / 1.27394 | 1.25803 / 1.27395 | – | agree (3e-5) |
| (±2,4) | ±2 | 11.07 (artefact) | 1.49555 | 1.49565 | **converged**, < λ^{1/4}; Line G two-point estimate 1.50 |
| (3,5,1) / (−3,5,4) | 5/3 | 37.0 / 36.7 (artefact) | 1.1389 / 1.2355 | not run | unconfirmed |
| (±4,6) | ±3/2 | 75.5 (artefact) | 1.2369 | not run | unconfirmed |
| (1,1,0) / (−1,1,0) | ±1 | 1733 / 1110 | 1.551 / 1.707 | 1.411 / 1.530 | **not converged**: no conclusion |

The lift removes the large-|a|/b ill-conditioning for b = 4 but not for |a|/b = 1. There the multiplier cost e^{2π·4c₀·r·|n|} ≥ e^{2.7|n|}
(r > 0.6036 is forced) competes with the decay of ĝ(n) = i^n J_n(1.8). A uniform-in-b gap therefore remains unverified even numerically
for |a|/b ~ 1. None of this is certified.

## 2. H2: certified 49-state operator for the Line B kick f_B (η = 2, s = −1, N ≡ +196) — after referee fixes [CA]

Status: computer-assisted (arb ball arithmetic plus float BLAS with a-priori rounding bounds) and a paper chain, with Lean for the
elementary steps. Independent referee audit: `computations/verification/lineH/referee/REPORT.md`, verdict ACCEPT AFTER FIXES. Fixes
1–5 and recommendations 6–10 are applied (§9).

### 2.1 1. Objects
* **Map and kick.** S = [[3,4],[2,3]] and λ = 3+2√2. The kick f_B is the Line B diagonal (l = 0) kick, with Fourier coefficients
  fCoeff(k,0) of `lineB/common/model.py`. This is the kick of BGS-TRACE-163/179/195. Take η = 2 and c₀ = 1/(λ−λ⁻¹).
* **Resonance.** s = −1, so ν* = ν_{7,−1} is the odd lift of (196)⁻¹ mod h_m, i.e. **N ≡ +196 (mod h_m)**. This uses the
  convention N ≡ −s·4a² of BGS-TRACE-194.
* **Law.** For odd m with 3 ∤ m, BGS-TRACE-194 (a = 7) gives the 49-state law with γ = 38 and λ₇⁻¹ = 32. These are m-independent.
* **Operators.** The lifted operators come from BGS-TRACE-197 (Line F §2, F1), applied to the TRACE-194 law with real shifts x = n/7:
  * (L_b Φ)_c = Σ_{n∈ℤ} w_b(n) [M_{n,c} C_{n,c}] ⊗ U_n Φ_{c′}.
  * Weights: w_b(n) = ĝ(n) e(s c₀x²/2 + bn/8), with ĝ the Fourier coefficients of e^{iηf_B}.
  * M_{n,c} = e(s c₀ x u), and C_{n,c}φ(u) = φ((u+x)/λ).
  * Vertex lattice V: c ∈ ℤ, c′ = round((c+x)/λ). Edge lattice E: c ∈ ℤ+½, with transitions only when the step is non-degenerate.
  * U_n acts on ℂ⁴⁹ by (U_n v)[λ₇⁻¹(σ+n)] += e(γ(nσ + 2⁻¹n²)/49) v[σ].
  * Space: the weighted ℓ²-sum of H²(D(c,ρ)) ⊗ ℂ⁴⁹ with ρ = 0.85, ω_c = e^{−3.5(|c|−R_c)₊}, R_c = 2 (V) and 3/2 (E).
  * These satisfy the hypotheses of BGS-TRACE-197: ρ > 0.6036 (V) and > 0.1036 (E), and ĝ is entire.

### 2.2 2. Lemma κ (sector coefficients for all m) [P + Lean core + exact check]
For every odd m with 3 ∤ m and s = ±1: κ = −k·u·y′ (mod 8) is odd. Hence, for c_b = 8⁻¹ Σ_{t mod 8} e((κt² − bt)/8):
|c_b| = ½ for b even and c_b = 0 for b odd.

*Proof.*
1. **h and y′ are odd.** h² + 1 = 2y′² forces h odd. Then h² + 1 ≡ 2 (mod 8), so y′² is odd and y′ is odd.
2. **k is odd.** 196ν + s = kh, the left side is odd, and h is odd.
3. **κ is odd.** u = 49⁻¹ ≡ 1 (mod 8), so κ ≡ −ky′ (mod 8) is odd.
4. **b odd.** The substitution t ↦ t+4 multiplies the summand by e(−4b/8) = −1, so the sum vanishes.
5. **b even, b = 2b′.** κ is invertible mod 8. The shift t ↦ t − κ⁻¹b′ completes the square, so |c_b| = |G(κ)|/8 with
   G(κ) = Σ_t e(κt²/8). For odd κ the residues κt² mod 8 are (0, κ, 4, κ, 0, κ, 4, κ). So G(κ) = 2 + 4e(κ/8) + 2e(½) = 4e(κ/8),
   and |c_b| = ½. ∎

* **Lean** (`Bgs.LineH`): h_odd, yp_odd, k_odd, kappa_odd, inv49_mod8, sq_residues_mod8, shift4.
* **Exact check** (`kappa_check.py`): all 398 pairs (m, s) with odd m ≤ 599 and 3 ∤ m, computed exactly in ℚ(√2).

### 2.3 3. The 49-state full-alphabet lifted trace identity [P]
For odd m with 3 ∤ m:

  **Z_m(ν*) = (1−λ^{−m}) Σ_{b∈{0,2,4,6}} c_b (Tr V_b^m − Tr E_b^m)**  (full alphabet, all words n ∈ ℤ^m).

*Proof.* BGS-TRACE-194 writes each word's phase as
(s c₀/49)[Σ n_j s_j + Σ n_j²/2] + κ(Σn)²/8 + (γ/49)[Σ n_j σ_j + 2⁻¹ Σ n_j²],
where s_j is the real periodic IFS orbit and σ_j is the periodic orbit of σ ↦ λ₇⁻¹(σ+n) in ℤ/49. The κ-term is expanded into sectors
by the Gauss sum of §2. Fix a word n = (n₀, …, n_{m−1}).
1. **Trace of one closed-chain block.** The block product of L^m along a closed vertex (or edge) chain is
   (M_{n_{m−1}}C_{n_{m−1}}⋯M_{n₀}C_{n₀}) ⊗ (U_{n_{m−1}}⋯U_{n₀}). Its trace factorises as Tr(M_pC_ψ)·Tr(U_{n_{m−1}}⋯U_{n₀}).
2. **The scalar factor.** Tr(M_pC_ψ) = p(s*)/(1 − λ^{−m}), where s* is the attracting fixed point of the contraction ψ
   (Ruelle; Bandtlow–Jenkinson). This is exactly the scalar part used in BGS-TRACE-197.
3. **The ℂ⁴⁹ factor.** U_{n_{m−1}}⋯U_{n₀} is a monomial matrix: a permutation with unimodular phases. The underlying permutation is
   the affine map σ ↦ λ₇^{−m}σ + const on ℤ/49, and 1 − λ₇^{−m} is a unit mod 49 iff 3 ∤ m. So there is exactly one fixed point
   σ₀, and the trace equals the accumulated phase e(γ(Σ n_jσ_j + 2⁻¹Σ n_j²)/49) along the periodic orbit σ_j starting at σ₀.
4. **Counting.** By the counting identity of BGS-TRACE-197 (Lean Bgs.LineF.vertex_minus_edge, which allows real shifts),
   #closed vertex chains − #closed edge chains = 1 for every word. Hence
   Σ_{chains} Tr(V-block) − Σ_{chains} Tr(E-block) = (phase of n)/(1−λ^{−m}).
5. **Summation over words.** Absolute convergence in trace norm: Σ_n ‖[M C]_n ⊗ U_n‖₁ ≤ 49·Σ_n |w(n)| e^{2πc₀|x|ρ}/(1−θ_n)·ω-ratios.
   This sum is finite, and it is the certified trace-norm bound T of §4. So L_b^m = Σ_{words, chains} block products converges in
   trace norm, and Tr L_b^m is the sum of the block traces. Summing over words then gives the identity.

This extends BGS-TRACE-194, which is stated for finite alphabets, to the full alphabet on the lifted space. Numerical check
(`tracechk.py`): the certified operator family at K = 16/12 reproduces the exact full-alphabet class sums |Z_m(ν*)|² with relative
error 1.9e−9, 8.9e−9, 2.8e−9 and 5.1e−9 at m = 5, 7, 11, 13. The referee reproduced this exactly. ∎

### 2.4 4. Theorem H2 (certified spectrum) [CA]
Galerkin data (V: K = 30, or 24 on the outer discs, D = 6762; E: K = 22/18, D = 3920). Bounds are rounded up:

| | δ₁ | δ₂ | Δ | ‖X‖ | trace norm | ε_A |
|---|---|---|---|---|---|---|
| V | 2.03e−3 | 2.6e−5 | 2.60e−3 | 0.948 | 10672.622 | 5.4e−15 |
| E | 1.5e−12 | 6.41e−4 | 1.67e−3 | 0.074 | 1106.332 | 2.2e−15 |

**Theorem.**
1. V_0 has exactly one eigenvalue μ* in {|z| > 1.5}. It is algebraically simple, and |μ* − b₁₁| < 0.05.
   * b₁₁ = (1.343138408342213+1.3393884635946203j).
   * **1.846834 ≤ |μ*| ≤ 1.946835** (outward). Compare λ^{1/4} = 1.553773974….
2. σ(V_0) \ {μ*} ⊂ {|z| < 1.5}; σ(V_b) ⊂ {|z| < 1.45} for b = 2, 4, 6; σ(E_b) ⊂ {|z| < 1} for b = 0, 2, 4, 6.
3. ‖V_b‖₁ ≤ 10672.622 and ‖E_b‖₁ ≤ 1106.332.

**Certificate values** (decided in arb; the figures are display values rounded up). The test is F·R < 1, where
F = δ₁ + δ₂ + Δ + ε_A + κ(ε_H + |b₂₁|), all padded up by 1+2⁻⁴⁰. The archived code is rig_spec.py v4 (rounding constant √2·γ_{2n+2},
a-posteriori Householder residual).

| operator | contour | F·R (author v4, rounded up) | referee |
|---|---|---|---|
| V_0 dom | R = 1.5, r₁ = 0.05 | 0.9136 (disc), 0.6236 (circle) | 0.8947, 0.5916 (certificate of record) |
| V_0 dom | R = 1.5, r₁ = 0.1 | 0.5859, 0.6236 | 0.5658, 0.5916 |
| V_2 rest | R = 1.45 | 0.7317 | re-decided exactly |
| V_4 rest | R = 1.45 | 0.8409 | re-decided exactly |
| V_6 rest | R = 1.45 | 0.7321 | re-decided exactly |
| E_0 rest | R = 1.0 | 0.0531 | 0.024 (own code) |
| E_2 rest | R = 1.0 | 0.0531 | re-decided exactly |
| E_4 rest | R = 1.0 | 0.0531 | re-decided exactly |
| E_6 rest | R = 1.0 | 0.0531 | re-decided exactly |

* **V_0 certificate of record:** the referee's ref_rig.py output (`referee/refV0.json`): F·R₁ = 0.8947, F·R₂ = 0.5916 at
  (R, r₁) = (1.5, 0.05). The author's v4 re-run is consistent with it (table above).
* **Margin.** At r₁ = 0.05 the author's F·R₁ is 0.9136, a margin of 8.6%. Robustness cross-check at r₁ = 0.1: F·R₁ = 0.5859,
  which still certifies |μ*| ≥ 1.796834 > λ^{1/4}. The first admissible m is unchanged.

**Method.** Splitting: L = T₀′ + (L − T₀′) with T₀′ = [[A_core ⊕ 0, 0],[X, 0]].
* The Galerkin section is exact.
* δ₁, δ₂ (Taylor tails, Cauchy estimate), Δ (far blocks, letters |n| > 150, rows |c| > 40, analytic) and the trace norm are all
  computed in arb (cert49_build.py, ghat_arb.py).
* Core resolvent: explicit powers Y^j (p = 32 for V_0, 24 for V rest, 20 for E). Their norms are bounded with Higham's entrywise
  bound |fl(AB) − AB| ≤ √2·γ_{2n+2}|A||B|. That bound holds for any summation order or FMA, and it covers OpenBLAS's SkylakeX edge
  kernels (no Strassen).
* Neumann tail; Householder deflation for V_0 with an a-posteriori residual.
* Homotopy T₀′ + t(L − T₀′), t ∈ [0,1]: the Riesz projection ranks are constant.

### 2.5 5. Corollary (all m)
By §3, Lidskii, Weyl (Σ_{k≠*}|μ_k|^m ≤ R^{m−1}‖L‖₁) and §2: for odd m with 3 ∤ m,

  |Z_m(ν*)| ≥ ½(1−λ^{−m}) [μ_lo^m − 1.5^{m−1}T_V − 3·1.45^{m−1}T_V − 4T_E] > 0  for every such m ≥ 47

(m = 43 fails; m = 45 is excluded since 3 | 45).

Then F_m(2) ≥ |Z_m(ν*)|²/φ(2h_m). Here φ(2h_m) = φ(h_m) ≤ h_m − 1, because h_m is odd. Also W̃rest_m(2) ≥ F_m(2) − 4m, by
BGS-TRACE-165 (B^sym ≤ 2m) and BGS-TRACE-170 (|χ_m| ≤ 1). Lower bounds, rounded down (bounds49.py → bounds49_v4.json):

| m | 47 | 49 | 53 | 55 | 61 | 71 | 85 | 101 | 151 | 199 |
|---|---|---|---|---|---|---|---|---|---|---|
| F_m(2)/2m ≥ | 7000 | 3.8e4 | 2.8e5 | 6.4e5 | 5.5e6 | 1.5e8 | 1.6e10 | 3.5e12 | 7.6e19 | 9.2e26 |
| W̃rest_m(2)/m ≥ | 1.4e4 | 7.6e4 | 5.7e5 | 1.2e6 | 1.1e7 | 3.1e8 | 3.3e10 | 7.1e12 | 1.5e20 | 1.8e27 |

* Both bounds increase in m (asserted in bounds49.py).
* For odd m ≥ 599 with 3 ∤ m: F_m/2m ≥ C·g^m/m with C ≥ 0.2499 and g = μ_lo²/√λ ≥ 1.41279. This is increasing in m and tends to ∞.
* Lean: `geom_tail` (monotone propagation in m) and `dom_lower` (the triangle step).

**Main consequence.** **W̃rest_m(2)/m ≥ 1.4e4 for every odd m ≥ 47 with 3 ∤ m.** Hence:
* **Conjecture R (BGS-TRACE-179), as stated, is false.** For every compact η-range [η₀, η₁] ∋ 2, max_η |W̃rest_m(η)| ≥ 1.4e4·m along
  an infinite set of odd m, so it is not o(m). (R is still open for compact ranges that do not contain 2.)
* **R_NSW.** If h_m is prime then m is prime, since h_d | h_m for d | m (BGS-TRACE-205, G5). So 3 ∤ m for m > 3, and the bound
  applies: R_NSW is violated at every m ≥ 47 with h_m prime. Whether there are infinitely many such m is unknown. If there are,
  R_NSW is false; otherwise it is vacuous.
* **TRACE-196.** This proves the conclusion of BGS-TRACE-196 (s = −1) unconditionally, but computer-assisted, on the explicit lifted
  space of BGS-TRACE-197. Hypothesis H_∞,7 as stated there (the TRACE-194 operators on a single-disc Banach space) is neither proved
  nor needed.

### 2.6 6. Not covered (exact list)
* **Odd m with 3 ∤ m in {17, 19, 23, 25, 29, 31, 35, 37, 41, 43}.** No bound: there the Weyl term dominates. m = 11, 13 are covered
  by BGS-TRACE-195; m = 5, 7 have nothing.
* **Every m with 3 | m:** the 49-state law does not apply.
* **η ≠ 2.**
* **s = +1:** not certified, and not needed.
* **Other frameworks:** the trace-class and Hardy-space setting is only the lifted one of BGS-TRACE-197.

### 2.7 7. Dependencies (cited, not re-proved)
BGS-TRACE-194 (law), BGS-TRACE-197 (lifted identity and counting), BGS-TRACE-165 and 170 (B^sym ≤ 2m and |χ| ≤ 1),
BGS-TRACE-205 G5 (h_d | h_m, used only for R_NSW), python-flint/arb, IEEE binary64 round-to-nearest, and OpenBLAS zgemm without Strassen.

### 2.8 8. Checks and controls
* Referee:
  * independent V_0 and E_0 certificates;
  * exact-rational re-decision of every certificate and the chain;
  * 120 Galerkin entries by an independent method (≤ 2.3e−14);
  * tracechk reproduced exactly;
  * bounds49 reproduced byte-identically.
* Float |μ| = 1.8968346 lies inside the enclosure (ARPACK, and Line F lift49.py).
* Negative control: asking whether V_0's whole spectrum lies inside R = 1.6, 1.85 or 1.9 fails, as it must.
* R = 1.35 and 1.4 fail for V_2/V_4/V_6.

### 2.9 9. Referee fixes applied
1. **Provenance.**
   * The referee's certificate (ref_rig.py, refV0.json) is adopted as the V_0 record, unchanged and with sha256.
   * V_0 was re-run with the archived rig_spec.py v4. V_4 (the tightest rest sector), V_2, V_6 and E_0..E_6 were also re-run with v4,
     on rebuilt matrices.
   * The code sha256 is recorded inside every output JSON (provenance block) and in SHA256_code_v4_runs.txt.
2. **Rounding constant:** √2·γ_{2n+2}.
3. **Padding and display values.**
   * JSON inputs are padded up by 1+2⁻⁴⁰.
   * Outputs are rounded outward with nextafter.
   * The tail constant is stated as C ≥ 0.2499.
4. **Wording and table.**
   * Table values recomputed from bounds49 v3 with 2-digit floor rounding.
   * Sign corrected: N ≡ +196.
   * Citations corrected: BGS-TRACE-197 applied to BGS-TRACE-194, and φ(2h) = φ(h) ≤ h−1.
   * Lemma κ added (§2).
5. **Scope:** §5 and §6.

Recommendations:
6. The 49-state identity is written out (§3).
7. The Lean file is built in the repo formalization tree.
8. The margin is noted.
9. V_4 was re-run.
10. Times are given in UTC+5.
