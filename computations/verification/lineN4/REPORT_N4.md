# REPORT_N4: Line N4 — full [CA] Λ certificates for (±2,8), Λ certificates for (±2,16), and the slow isotropic family at q = h_p

Labels: **[P]** proved here or cited proved; **[CA]** computer-assisted with ball arithmetic (arb via python-flint 0.9.0); **[CA*]** verified floating point;
**[N]** numerics, not rigorous; **[H]** heuristic. Times are Asia/Yekaterinburg (UTC+5). N3 files were only read, never edited. Nothing was pushed.

## 0. Summary

| item | result | label |
|---|---|---|
| (1) 8E | **Λ_free^{8E} ≤ 0.4915932 < 2.01046** (phase-blind Schur certificate in the Line F space; replaces N3's [CA*] 1.660338). Unit-point rate (Λ r₂)^{1/3} ≤ 0.80266 | [CA] + [P] |
| (1) 8V | **Λ_free^{8V} ≤ 1.9656353 < 2.00859** (arb τ-cell certificate with the N3 extremal norm R; margin kept). Unit-point rate ≤ 1.27438 | [CA] + [P] |
| (2) 16V | **Λ_free^{16V} ≤ 2.9413896 < 3.04126** (margin 3.3%), uniform over all twists τ, all 128 block factors (16 distinct actions × sign of a). Unit-point rate (Λ r₂)^{1/3} ≤ 1.45789 < 1.4742 | [CA] + [P] |
| (2) 16E | **Λ_free^{16E} ≤ 0.4474396 < 3.04280**. Unit-point rate ≤ 0.77812 | [CA] + [P] |
| (2) Lemma I₁₆ | the N3 intertwining lemma holds verbatim for the (±2,16) O1 spaces (0.9, 0.3) / (0.2, 0.3) with the 2-dim unitary internal factor | [P] |
| (3) | **Gauge lemma**: a real two-sided geometric twist is an exact coboundary; slow isotropic segments are gauge-conjugate to powers of the sector-4 operator, so their contribution has the closed form μ*^n·(rank one) + O(0.7691^n). The dominant isotropic family at q = h_p is identified exactly (sector-4 depth 16D = 1, i.e. 4β − q a prime generator of 𝔮; 2p points per line; 89% of |iso| at (21,239), 62% at (15,41)). Subtracting its rank-one slow part leaves remainder terms with **provable** rate ≤ 1.2426 < T on that family, **but** the leading term itself still needs the fast-half matrix element bounded by G^{p−n} with G ≤ 1.547 (worst case Λ gives 1.4468 > T), and the generic isotropic points are untouched. So the isotropic obstruction is **localised**, not closed. | [P] + [CA] + [N]; closure [H] |

## 1. Item (1): full [CA] certificates for (±2,8)

### 1.1 8E: phase-blind Schur certificate [CA]
- **Lemma S [P].** Let A = Σ_n c_n B_n with |c_n| ≤ W_n (any unimodular phases, any twist τ), and let M = Σ_n W_n |B_n| (entrywise absolute values in the
  orthonormal monomial basis of the Galerkin core). If x, y > 0 satisfy M x ≤ α x and Mᵀ y ≤ β y entrywise, then with D = diag(√(x/y)):
  ‖D⁻¹ A D‖₂ ≤ ‖D⁻¹ |A| D‖₂ ≤ ‖D⁻¹ M D‖₂ ≤ √(αβ). (Schur test with test vector p = √(xy).) The bound is uniform in τ and in the sector phases.
- Computation (`code/b16_schur.py E 4 0.8 40 60 128 … 0 8`, arb, prec 128): core 320 dims (K0 4, ρ 0.8, K 40, letters |n| ≤ 60, as Line F certE).
  α = 0.49158014, β = 0.49159551, **f = √(αβ) ≤ 0.4915878**; cond D = 1.31e4.
- Full operator (`code/b8E_final.py`): N3 §2.2 norm |||(u,t,y)||| = max(‖Ru‖, ‖t‖, b‖y‖) with R = D⁻¹ (‖R‖ = 13082, ‖R⁻¹‖ = 1), Line F errors
  ε = δ + Δ = 1.229e-10, ‖X‖ = 0.32074: penalty 5.3e-6. **Λ_free^{8E} ≤ 0.4915932** (equivalence constant κ = 4.3e4, p-independent).
- Consistency [CA]: Line F certified the 8E sector-4 complement radius 0.3825 ≤ 0.4916.
- An independent arb run of the cell scheme (identity norm) was started and stopped after 20 cells (all ‖A_τ‖ = 1.636598, flat in τ; logs kept as
  `logs/b8E_partial_w*.jsonl`); it is superseded by the Schur certificate.
- For 8V the phase-blind bound is 3.932 (useless against 2.00859), so 8V needs the twist-resolved cell scheme.

### 1.2 8V: arb τ-cell certificate [CA]
- `code/b_arb_cert.py` (ball arithmetic throughout; the float SVD frames U, V and S ≈ R⁻¹ are only used as test matrices, their effect is bounded rigorously):
  - exact blocks as N3 `i_verify.py` / Line F; C_n = R (w₀(n) B_n) S in arb for |n| ≤ 24; F = RS − I with ‖F‖_F ≤ 6.2e-15;
  - tail 24 < |n| ≤ 60: T₀ = ‖R‖_F ‖S‖_F Σ‖w₀B_n‖_F ≤ 1.61e-9 (letters > 60 are in Line F's Δ);
  - L₂ = Σ(2πn)²‖C_n‖_F ≤ 11080.9;
  - cell [t₀−h, t₀+h]: sup‖R A_τ R⁻¹‖ ≤ (‖X(t₀)‖ + h‖X′(t₀)‖ + h²L₂/2 + T₀)/(1 − ‖F‖); ‖X(t₀)‖ rigorously via M = U*XV, ‖M‖ ≤ max|M_ii| + ‖M − diag‖_F,
    ‖X‖ ≤ ‖M‖/√((1−‖U*U−I‖_F)(1−‖V*V−I‖_F)); ‖X′(t₀)‖ first by Frobenius, else spectral; else bisect.
  - 400 initial cells, target 1.9657 (the N3 [CA*] cell value), 2 worker processes (nice 5; the box had load 9–12 from other jobs), prec 80.
- Assembly (`code/b_assemble.py`): exact (Fraction) coverage check of [0,1] from cell labels; penalty with rigorous ‖R‖₂ ≤ ‖R‖_F, ‖R⁻¹‖ ≤ ‖S‖_F/(1−‖F‖).
- Result: 442 accepted cells (400 initial, 42 bisections, 77 cells needed the spectral ‖X′‖), coverage of [0,1] verified exactly, workers finished 19:39.
  Max cell bound **1.9656276** (max rigorous ‖X(t₀)‖ = 1.9232665, near τ = ½; the referee's independent arb value at 0.501375 is 1.92326823); ‖RS − I‖_F ≤ 6.2e-15;
  ‖R‖_F ≤ 35.874, ‖R⁻¹‖ ≤ 26.218; Line F ε = 1.90e-9, ‖X‖ = 6.159; penalty 7.7e-6; κ = 4036.
  **Λ_free^{8V} ≤ 1.9656353 < 2.00859 [CA]** (`logs/b8V_final.json`); unit-point rate (Λ r₂)^{1/3} ≤ **1.27438** < 1.28359. The N3 [CA*] value 1.965736 is confirmed and slightly improved.

## 2. Item (2): (±2,16) Λ

### 2.1 Operators
- TRACE-226 / J3: V_B(τ) = Σ_n ĝ(n) e(Cn²/2) e(nτ) [multiplier e(Cns) ∘ composition] ⊗ A_{B,n}, |C| = 4·2·c₀/16 = c₀/2, A_{B,n} the 2×2 monomial
  ζ₁₆-matrix of block B in its (f₁, f₂) basis (J3 `blocks16_exact.json`: f₁, f₂ orthogonal with equal norms, exact in Z[ζ₁₆], so the basis is orthonormal after scaling).
- **Fact [CA, exact data].** Among the 128 blocks (16 cases × 8) there are 16 distinct actions and exactly **two** permutation patterns:
  P_n = swap^{n+PAR}, PAR ∈ {0,1} (64 blocks each). Checked in `b16_schur.py`.

### 2.2 Core bound [CA]
- Lemma S with M = Σ_n |J_n(1.8)| |B_n| ⊗ P_n (independent of τ, of the ζ₁₆ phases, of the sign of a, hence of C's sign).
- `code/b16_schur.py V 4 1.2 55 60 128 … PAR` (990 dims) and `E 4 0.8 40 …` (640 dims), both PAR:
  - **16V: f ≤ 2.9413896** (α 2.9413889, β 2.9413903; float Perron root 2.9413889, which was the same in the (0.9,0.3) and (0.6,2.5) spaces [N]); cond D 1.03e4.
  - **16E: f ≤ 0.4474392**; cond D 1.21e4.

### 2.3 Error terms and tensor factor [CA + P]
- `code/cert_lift16.py` = Line F `cert_lift.py` with the multiplier coefficient c₀ → c₀/2 (one-line change, logged diff), same parameters as the 8 certificates:
  - V (K0 4, ρ 1.2, K 55, β 2.5, Nmax 60, Rmax 40): δ₁ 5.74e-13, δ₂ 3.28e-15, Δ 8.91e-16, ‖X‖ 0.95264.
  - E (K0 4, ρ 0.8, K 40, β 2.5): δ₁ 2.1e-23, δ₂ 5.30e-12, Δ 1.25e-17, ‖X‖ 0.10633.
- **Tensor factor [P].** Write A_{B,n} = D_n·swap^{n+PAR} with D_n diagonal unitary. The even-letter part Σ_{n even} K_n ⊗ D_n equals ½(L + L^{(−1)^n}) with phase
  twists ±1, each a direct sum of two scalar operators with unimodular letter phases, so every Line F bound (uniform in unimodular phases) applies; the odd
  part is the same times I ⊗ swap. Hence δ, Δ, ‖X‖ of the tensor operator are ≤ 2× the scalar bounds.
- Penalties (`code/b16_final.py`): 16V ε = 1.16e-12, ‖X‖ ≤ 1.905, penalty 3.9e-8; 16E ε = 1.06e-11, ‖X‖ ≤ 0.2127, penalty 3.8e-7.
- **Λ_free^{16V} ≤ 2.9413896 < 3.04126; Λ_free^{16E} ≤ 0.4474396 < 3.04280** [CA], for every PAR, every block, every twist sequence.

### 2.4 Lemma I₁₆ (intertwining) [P]
- O1 spaces (Line L / TRACE-249/250): 16V (ρ, β) = (0.9, 0.3), 16E (0.2, 0.3). Certificate spaces: (1.2, 2.5), (0.8, 2.5).
- The N3 Lemma I proof goes through with the same step counts (V: one in, two out; E: two and two):
  - V, O1 → F: θ ≤ (½ + 1.2/λ)/0.9 = 0.784 < 1; weight ratio ≤ e^{0.15 + 0.0515|n|}.
  - V, F → O1 (two steps): θ ≤ (0.5858 + 0.9/λ²)/1.2 = 0.510; weight exponent −0.3 + 2.5/λ² = −0.226 < 0.
  - E: identical to 8E (same spaces): θ = 0.635, exponent < 0.
  - The multiplier sup is e^{2π(c₀/2)|n|ρ} (smaller than for (±2,8)); the internal factor is unitary, so the Schur tests over sites are unchanged.
- Consequence: Theorem C (N2, with N2-F1 via Lemma I) holds for the (±2,16) families with Λ = Λ_free^{16V/E}. The unit-point rates (Λ r₂)^{1/3} are
  **1.45789 (16V) and 0.77812 (16E)**, below the (±2,16) target 1.4742, with r₂ from N2 Prop E [CA].
- **Scope remark.** At q = h_p (≈ λ^{p/2} = 1.342^m) the (±2,16) level is already absorbed by Line L §5(b) (threshold 1.1311^{m(1+η)}) for large p; the new Λ₁₆
  matters for Theorem C at smaller unit-point levels, where it is now available. N3 §4 item 4 ("(±2,16) Λ < 3.04, missing input") is **closed**.

## 3. Item (3): the slow isotropic contribution at q = h_p

### 3.1 Gauge lemma [P]
- Let L_τ Φ(s) = Σ_n w(n) e(nτ) e(κns) Φ((s+n)/λ) act on functions holomorphic near R (the lattice-of-discs space is its localisation), T_σΦ(s) = Φ(s+σ),
  G_νΦ(s) = e(νs)Φ(s). Direct substitution gives
  - L_τ T_σ = T_{λσ} L_{τ−κλσ}   and   L_τ G_ν = G_{ν/λ} L_{τ+ν/λ}.
- **Corollary.** For a real two-sided geometric twist τ_i = t₀ + aλ^i + bλ^{−i} (i = 0,…,n−1), with σ_i = −aλ^{i−1}/κ and ν_i = bλ^{1−i}:
  Π_{i<n} L_{τ_i} = T_{−λσ_{n−1}} G_{−bλ^{1−n}} · L_{t₀}^n · G_{λb} T_{σ_0}  (exactly; all intermediate gauges cancel).
- On the disc space this holds whenever the gauges are small (|σ|, |ν| below the disc margin): there the slow segment is *exactly* a conjugated power.

### 3.2 Isotropic twists are two-sided geometric, and the slow ones sit at the sector-4 fixed point [P]
- For isotropic β, τ_i = Tr(λ^i y) (N3 Lemma 1.1, y = β/q) is literally the real number yλ^i + y′λ^{−i}, reduced mod 1 only through e(nτ).
- The constant twist t₀ = ½ (sector 4) is Tr(λ^i z₄) mod 1 for the fixed point z₄ = ¼ of x ↦ λx on R/O^∨ (Tr(λ^i)/4 ≡ ½). Writing y = z₄ + δ (mod O^∨),
  τ_i = ½ + (δλ^i + δ′λ^{−i}): the gauge lemma applies with t₀ = ½. The window where both gauges are small has length
  n(δ) = log_λ(ε₀² q/D) + O(1), with the **sector-4 depth** D(β) := q·min_{w∈O^∨} |N(y − ¼ − w)| ∈ (1/16)Z.
- **The dominant family [P].** 16D = |N(γ)|/q with γ = 4qδ ∈ O; 16D = 1 ⇔ γ is a generator of 𝔮 (or 𝔮̄) ⇔ 4β ≡ q + γ. Its slow window is the longest
  possible, log_λ q + O(1) ≈ p/2 at q = h_p ≈ λ^{p/2}/2 (cf. Lemma E's log_λ q + 0.76).
- [N] (`code/c_depth4.py`, data = N2 TRACE-206 arrays): the 16D = 1 family has exactly **2p points per line** and carries **88.9%** of Σ|Ẑ| on each isotropic line
  at (21,239) (|Ẑ| = 172.74, the N3 "max iso point" 1.2780 = 172.74^{1/21}) and **62.0%** at (15,41). Next families: (21,239) 16D = 41 (6.8%), 25 (2.2%);
  (15,41) 16D = 7 (36.9%).
- Sector-4 spectrum at t₀ = ½ [CA, Line F certV]: |μ*| ∈ [1.91447, 1.91647]; complement spectral radius ≤ 0.76905 ([N] value |μ₂| = 0.72778, `code/c_mu2.py`).

### 3.3 Closed form and subtraction
- [P] On each period the slow window contributes U⁻¹ L_{½}^{n} U′ = μ*^n·U⁻¹Φψ*U′ + U⁻¹ Y^{n} U′ with ‖Y^n‖ ≤ C·0.7691^n.
  With three windings (m = 3p), Ẑ_β = μ*^{3n}·(lead)_β + (rem)_β where (lead)_β = (ψ̃*F_β Φ̃)²·(ψ̃*R F_β Φ̃) is a product of scalars
  (F_β = fast part of one period, length p − n ≈ p/2; Φ̃, ψ̃ gauge-transported eigenvectors).
- **Remainder [P + CA, constants not computed].** Bounding the fast parts by the certified free-family norms (κ Λ^{len}), the remainder terms on the 16D = 1 family
  have rates (q = λ^{p/2}, n = p/2): j complementary windows out of 3 give λ^{−1/6}(μ*^{3−j}·0.76905^j·Λ³)^{1/6} = **1.2426 (j=1), 1.0672 (j=2), 0.9165 (j=3)**,
  all < T = 1.28359 (μ* ≤ 1.916473 from Line F, Λ = 1.9656353 [CA]).
- **Leading term [assessment].** With the worst-case bound on F_β the leading term has rate λ^{−1/6}(μ*Λ)^{1/2} = **1.4468 > T**. Closing it needs
  |ψ̃*F_βΦ̃| ≤ G^{p−n} with **G ≤ 1.547**. F_β is a single deterministic product: its twists are frac(Tr(λ^i γ/(4q))), the base-λ digits of the explicit
  algebraic number γ/(4q) over p/2 steps. There is no averaging over the family (it is one ⟨λ⟩-orbit up to sign), so equidistribution tools do not apply.
  [N] At (21,239) the leading term is far below the threshold: 172.74 = μ*^{3n}·|lead| with n ≈ 4.7 implies an effective G ≈ 0.56 per fast step.
- **What subtraction leaves numerically [N].** Removing the 16D = 1 family lowers the absolute isotropic rate from 1.1604 to 1.0450 at (21,239) and from 1.0559
  to 0.9899 at (15,41).
- **Generic isotropic points.** Points with D ≍ q have no slow window; they still need line-averaging of p-step products beyond the Ehrenfest lag (N3 §1.6).
  The gauge lemma does not change this (with D large the gauges are large immediately).

### 3.4 Net for item (3)
- The slow-orbit contribution has an exact closed form [P] and its subleading part is provably below T on the dominant family [P + CA].
- The two remaining requirements are: (a) a sub-1.548 bound for one explicit fast-half matrix element (deterministic, single family); (b) the generic-line
  average (beyond Ehrenfest). Neither is proved. (a) is new and much narrower than before: it is a statement about one vector pushed through an explicit
  twist sequence of length ≈ p/2 = log_λ q, which is inside the Ehrenfest range, so a family-free argument (for example a cone or positivity argument for
  the sector-4 Perron vector under generic twists) is conceivable [H].

## 4. Status of the m = 3p programme after N4
- Theorem C′ (for p with h_p squarefree, N3-F8) now holds for all four families with fully [CA] Λ: 8V (1.9656353), 8E (0.49159), 16V (2.94139), 16E (0.44744), via Lemma I / I₁₆ [P].
- N3 §4 item 4 is closed. Items 1 (isotropic at q | h_p; now localised to (a) and (b) of §3.4), 2 (index loss at proper divisors) and 3 (K_p-levels) remain.
  R′ is **not** refuted along m = 3p.

## 5. Referee N3 fixes that concern N4 (audit/lineN3, received 18:35)
- **N3-F7 (certificate hygiene) — met by construction in N4 §1.** ‖R‖₂ ≤ ‖R‖_F and ‖R⁻¹‖ ≤ ‖S‖_F/(1−‖RS−I‖_F) are arb upper bounds (no float SVD);
  every twiddle e(nτ) is an acb ball; cell centres are arb balls of the exact rationals (2i+1)/(2·NC0) (± dyadic refinements), and the assembler
  recomputes every certified interval from its label in exact Fractions and checks coverage of [0,1]. The ball enclosure at a centre bounds X(t) for every
  t in the ball, so no ulp inflation is needed. The 8E and (±2,16) Schur certificates have no τ-grid at all.
- **N3-F6.** Λ_free^{(−2,8)} = Λ_free^{(+2,8)} and Λ_free^{(−2,16)} = Λ_free^{(+2,16)}: RK sends (C, a, τ) ↦ (−C, a−4, τ) letterwise and is an isometry of
  H(ρ,β) (weights symmetric in |c|, real disc centres, K and the reflection preserve H²); the twist is free. For (±2,16) the certificate is in any case
  sign-blind (only |C| enters M).
- **N3-F8.** Theorem C′ (all four families) is stated for p with h_p squarefree. [N] `code/d_squarefree.py`: for every prime q < 3·10⁶, ord_q(λ) was computed;
  2750 pairs (p, q) with q | h_p, p ≤ 10⁵ prime, were found and **none** has q² | h_p (λ^p ≢ 1 mod q²) (`logs/d_squarefree_3000000_100000.json`).
- **N3-F9.** Level 7·h_p: unit points [P-sketch] via modulated twists (written in N3 v2 §3); its isotropic part joins item 1. The N4 isotropic analysis (§3)
  applies verbatim at 7·h_p with t₀ = ½ + (period-3 shift), which is again a free-family twist.
- N3 v2 and N2 v3 are written (`N3/REPORT_N3_v2.md`, `N2/REPORT_N2_v3.md`); originals untouched.

## 6. Files (all under /workspace/bgs-lineN/N4)
- code: `a_probe.py`, `b_arb_cert.py`, `b_assemble.py`, `b16_probe.py`, `b16_perron.py`, `b16_schur.py`, `b16_final.py`, `b8E_final.py`, `cert_lift16.py`, `c_mu2.py`, `c_depth.py`, `c_depth4.py`, `d_squarefree.py`.
- logs: `b8V_w0.jsonl`, `b8V_w1.jsonl`, `b8V_final.json`, `b8E_final.json`, `b8_schur_{E,V}.json`, `b16_schur_{V,E}_P{0,1}.json` (+ `_d.npy`), `b16_final.json`,
  `cert16_{V,E}.json`, `c_mu2.out`, `c_depth4_m21_q239.json`, `c_depth4_m15_q41.json`, `c_depth_m21_q239.json`, `c_depth_m15_q41.json`, `a_probe.out`, `b16_probe_*.json`, `b8E_partial_w*.jsonl`, `d_squarefree_3000000_100000.json`.
- `NOTES_N4.md`, `SHA256_N4.txt`.
