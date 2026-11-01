import Mathlib
/-! N21 key arithmetic (Grok Bot), H4 core→true conversion. No sorry, no native_decide.
All decimals are upper (resp. lower) roundings of the certified inputs printed in N21/logs
(conv_c CONST, tail_DT CONST, N8 n8_cert_fam.json, N13 b_arb.json). -/
open Real

/-! ### Lemma C: the projector-mismatch constant τ and the denominator -/
/-- τ = dPi·‖ψ_T‖·‖Φ_T‖ < 6.1374e-4. -/
theorem tau_lt : (2.7937608016e-5 : ℝ) * 6.5237371910 * 3.3674039287 < 6.1374e-4 := by norm_num
/-- den1 − τ > 0.999386 > 0, so the τ-corrected denominator of eq. (C3) is positive. -/
theorem den_tau_pos : (0.99999999989 : ℝ) - 6.1374e-4 > 0.999386 := by norm_num

/-! ### Lemma Q constants -/
/-- |s| < 1.9154733 (s = 1.357239924265973 − 1.3516424762972736 i). -/
theorem abs_s_up : (1.357239924265973 : ℝ) ^ 2 + 1.3516424762972736 ^ 2 < 1.9154733 ^ 2 := by norm_num
/-- |s| > 1.9154731. -/
theorem abs_s_lo : (1.9154731 : ℝ) ^ 2 < 1.357239924265973 ^ 2 + 1.3516424762972736 ^ 2 := by norm_num
/-- κ' = 0.45(1+η) + (1+η)·cond·δ_Q < 0.45000047 (η = 1e-6, cond ≤ 21.1030884, δ_Q ≤ 8.868e-10). -/
theorem kap_up : (0.45 : ℝ) * (1 + 1e-6) + (1 + 1e-6) * 21.1030884 * 8.868e-10 < 0.45000047 := by norm_num
/-- |s|·κ' < 0.86197 < 1 (Neumann series for R_A Q_A on |z| = 1). -/
theorem s_kap_lt : (1.9154733 : ℝ) * 0.45000047 < 0.86197 := by norm_num
/-- sup_{|z|=1} ‖R_A(z)‖ ≤ ‖Π_A‖/(|s|−1) + ‖Q_A‖ + cond·|s|κ'/(1−|s|κ') < 146.44. -/
theorem RA_up : (6.5237372 : ℝ) / (1.9154731 - 1) + 7.5237372 + 21.1030884 * 0.86197 / (1 - 0.86197) < 146.44 := by
  have h1 : (6.5237372 : ℝ) / (1.9154731 - 1) < 7.1262 := by rw [div_lt_iff₀ (by norm_num)]; norm_num
  have h2 : (21.1030884 : ℝ) * 0.86197 / (1 - 0.86197) < 131.785 := by rw [div_lt_iff₀ (by norm_num)]; norm_num
  linarith
/-- S_T ≤ √(R_A² + (Xn·R_A + 1)²) < 914.8. -/
theorem ST_up : (146.44 : ℝ) ^ 2 + (6.159194846 * 146.44 + 1) ^ 2 < 914.8 ^ 2 := by norm_num
/-- Pert·S_T < 1.8e-6 < 1. -/
theorem PertST : (1.9009998534e-9 : ℝ) * 914.8 < 1.8e-6 := by norm_num
/-- Rem = S_T²·Pert/(1 − Pert·S_T) < 1.591e-3. -/
theorem Rem_up : (914.8 : ℝ) ^ 2 * 1.9009998534e-9 / (1 - 1.8e-6) < 1.591e-3 := by
  rw [div_lt_iff₀ (by norm_num)]; norm_num
/-- |s/μ| ≤ |s|/(|s| − mus) < 1 + 1.2e-6. -/
theorem sr_up : (1.9154733 : ℝ) / (1.9154731 - 2.0000001e-6) < 1 + 1.2e-6 := by
  rw [div_lt_iff₀ (by norm_num)]; norm_num
theorem rem_mu1 : (1.591e-3 : ℝ) / 1.9154 < 8.31e-4 := by rw [div_lt_iff₀ (by norm_num)]; norm_num
theorem rem_mu2 : (1.591e-3 : ℝ) / 1.9154 ^ 2 < 4.34e-4 := by rw [div_lt_iff₀ (by norm_num)]; norm_num
/-- m(1) = |s/μ|(cond·κ' + xs·‖Q_A‖) + Rem/|μ| < 33.69. -/
theorem m1_up : (1 + 1.2e-6 : ℝ) * (21.1030884 * 0.45000047 + 3.2154952 * 7.5237372) + 1.591e-3 / 1.9154 < 33.69 := by
  have h : (1 + 1.2e-6 : ℝ) * (21.1030884 * 0.45000047 + 3.2154952 * 7.5237372) < 33.68902 := by norm_num
  linarith [rem_mu1]
/-- m(2) = |s/μ|²·cond·(κ'² + xs·κ') + Rem/|μ|² < 34.81. -/
theorem m2_up : (1 + 1.2e-6 : ℝ) ^ 2 * (21.1030884 * (0.45000047 ^ 2 + 3.2154952 * 0.45000047)) + 1.591e-3 / 1.9154 ^ 2 < 34.81 := by
  have h : (1 + 1.2e-6 : ℝ) ^ 2 * (21.1030884 * (0.45000047 ^ 2 + 3.2154952 * 0.45000047)) < 34.8092 := by norm_num
  linarith [rem_mu2]
/-- K₀ = ‖Π‖ + max_k m(k) < 56.78 (m(k) decreasing for k ≥ 2 since κ' < 1). -/
theorem K0_up : (21.968115037 : ℝ) + 34.81 < 56.78 := by norm_num
/-- the rate ρ = 0.5225 dominates both decay rates: 1/|μ| < ρ, |s/μ|κ' < ρ, and λρ > 1. -/
theorem rho_mu : (1 : ℝ) < 0.5225 * (1.9154731 - 2.0000001e-6) := by norm_num
theorem rho_kap : (1 + 1.2e-6 : ℝ) * 0.45000047 < 0.5225 := by norm_num
theorem lam_rho : (1 : ℝ) < (3 + 2 * √2) * 0.5225 := by
  have h : (0 : ℝ) ≤ √2 := Real.sqrt_nonneg 2
  nlinarith

/-! ### Final δ_true and its use -/
/-- δ_true ≤ (G ≤ 15) 2.2101666e-6 + (16 ≤ G ≤ 36, box) 2.7126552e-6 + (37 ≤ G ≤ 60, Lemma D^T) 1.0842558e-7
    + (G > 60) 3.1e-13 < 5.0313e-6. -/
theorem delta_true_sum : (2.2101666e-6 : ℝ) + 2.7126552e-6 + 1.0842558e-7 + 3.1e-13 < 5.0313e-6 := by norm_num
/-- budget: A_bad^KP (2.063e-6) + δ_true < Re Λ_lo' = 6.234e-4, margin > 100×. -/
theorem budget : (2.063e-6 : ℝ) + 5.0313e-6 < 6.234e-4 / 87 := by norm_num
/-- crossover monotonicity at the new p* = 1397: envelope slope 2e^γ/(2p*+1) < 0.002 < 0.02195 ≤ G'(p*). -/
theorem env_slope_1397 : 2 * exp eulerMascheroniConstant / (2 * 1397 + 1) < (0.002 : ℝ) := by
  have h1 : exp eulerMascheroniConstant < exp 1 :=
    exp_lt_exp.mpr (eulerMascheroniConstant_lt_two_thirds.trans (by norm_num))
  have h2 := Real.exp_one_lt_d9
  rw [div_lt_iff₀ (by norm_num)]
  nlinarith [h1, h2]
/-- geometric remainder of the analytic tail: ρ = 0.5225 and λ^{-1/2} < 0.5 are both < 1. -/
theorem lam_half : (1 : ℝ) < 0.5 ^ 2 * (3 + 2 * √2) := by
  have h : (1 : ℝ) < √2 := by rw [Real.lt_sqrt] <;> norm_num
  nlinarith
