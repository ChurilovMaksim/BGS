import Mathlib
/-! Referee arithmetic checks, Line N12 + N11b (Grok Bot audit). No sorry, no native_decide. -/

-- N12 adapted norm: cond(H) from the arb-certified eigenvalue brackets c_lo = 0.7208, c_hi = 15.1811
theorem cond_bracket : (15181/1000:ℚ)/(7208/10000) < 21062/1000 ∧ (21060/1000:ℚ) < (151811/10000)/(7208/10000) := by norm_num
-- cell add-on Lip_H/(2*4096)
theorem cell_add : (1672/10:ℚ)/8192 < 205/10000 := by norm_num
-- quadratic step bound at the edge |t| = 1/256
theorem quad_edge : (1:ℚ) + 3190*(1/256)^2 < 10487/10000 := by norm_num
-- type counts: 25 ordered type pairs × 2 signs × (15 G-values for h=0 + 16 for h=1); coded n=2G+h ≥ 5
theorem n_types : 25*2*(15+16) = 1550 ∧ 25*2*(13+14) = 1350 ∧ 1550 - 1350 = 200 := by norm_num
-- δ_int vs budget; and with the referee's uncoded short-gap composites (9.95e-7) added
theorem dint_ratio : (5144/10^10:ℚ)/(623397/10^9) < 826/10^6 := by norm_num
theorem dint_plus_short : (5144/10^10:ℚ) + 995/10^9 < (623397/10^9)/400 := by norm_num
-- Re Λ_lo' = Re Λ_lo - 2*10*(2.2e-8): the c16 charge is 200 × |c16| (|c16| ≈ 2.2e-9)
theorem c16_charge : (6238370:ℚ)/10^10 - 2*10*(22/10^9) = 6233970/10^10 ∧ 2*10*(22/10^9:ℚ) = 200*(22/10^10) := by norm_num
-- relabelling example of N12: 4√2 − 2ε = 2ε⁻¹  (ε = 1+s, ε⁻¹ = s−1)
theorem relabel (s : ℝ) (hs : s*s = 2) : 4*s - 2*(1+s) = 2*(s-1) ∧ (1+s)*(s-1) = 1 := by
  constructor <;> [ring; linear_combination hs]
-- N11b: λ^5 − 1 = 2 h_5 ε^5 with h_5 = 41 (so twists are p-periodic), ε^5 = 41+29s, λ^5 = ε^10
theorem lam5 (s : ℝ) (hs : s*s = 2) : (41+29*s)^2 - 1 = 2*41*(41+29*s) := by linear_combination 841*hs
-- N11b: |κ(u)| = |−1 − e(x)| ≤ 2 (triangle inequality on the unit circle)
theorem kappa_le_two (z : ℂ) (hz : ‖z‖ = 1) : ‖(-1:ℂ) - z‖ ≤ 2 := by
  calc ‖(-1:ℂ) - z‖ ≤ ‖(-1:ℂ)‖ + ‖z‖ := norm_sub_le _ _
    _ = 2 := by rw [hz]; norm_num
-- N11b exponents (ratios per p): C' bulk ε(1.2744/μ*)^3 < e^{-0.341} ≈ 0.71108 ;  uses s < 1.41422
theorem Cprime_ratio : (241422/100000:ℚ)*((12744/10000)/(19154712/10^7))^3 < 71110/100000 := by norm_num
-- unit gas: |1+Λ+Λ_U|^2 / (|1+Λ|^2 ε^2) < 0.4148^2  (e^{-0.880} ≈ 0.41478), ε > 2.41421
theorem unitgas_ratio :
    let a : ℚ := 1 + 74901/10^8 + 1005429/10^9; let b : ℚ := 372161/10^9 - 1834361/10^9
    let c : ℚ := 1 + 74901/10^8; let d : ℚ := 372161/10^9
    (a^2+b^2) < (41480/100000)^2 * (241421/100000)^2 * (c^2+d^2) := by norm_num
