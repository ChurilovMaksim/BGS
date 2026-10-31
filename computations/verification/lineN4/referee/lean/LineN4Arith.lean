import Mathlib
/-! Referee (Grok Bot) cheap Lean targets for Line N4: pure rational arithmetic behind the stated margins.
 λ = 3 + 2√2 is handled through rational brackets 5.8284 < λ < 5.8285. -/
namespace LineN4

/-- rational bracket for λ = 3+2√2 -/
theorem lam_bracket : (5.8284:ℝ) < 3 + 2*Real.sqrt 2 ∧ 3 + 2*Real.sqrt 2 < 5.8285 := by
  have h2 : (0:ℝ) ≤ Real.sqrt 2 := Real.sqrt_nonneg 2
  have hs : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  constructor <;> nlinarith [hs, h2]

/-- certificate assembly: max cell / core bound + penalty ≤ stated Λ, and Λ below the N2 thresholds -/
theorem assembly :
    (1.9656276:ℚ) + 0.0000077 ≤ 1.9656353 ∧ (0.4915878:ℚ) + 0.0000054 ≤ 0.4915932 ∧
    (2.9413896:ℚ) ≤ 2.9413896 ∧ (0.4474392:ℚ) + 0.0000004 ≤ 0.4474396 ∧
    (1.9656353:ℚ) < 2.00859 ∧ (0.4915932:ℚ) < 2.01046 ∧ (2.9413896:ℚ) < 3.04126 ∧ (0.4474396:ℚ) < 3.04280 := by
  norm_num

/-- unit-point rates (Λ r₂)^{1/3} below targets T = 1.28359 (8) and 1.4742 (16), in cubed form -/
theorem unit_rates :
    (1.9656353:ℚ)*1.0529012 < 1.28359^3 ∧ (0.4915932:ℚ)*1.0519234 < 1.28359^3 ∧
    (2.9413896:ℚ)*1.0534557 < 1.4742^3 ∧ (0.4474396:ℚ)*1.0529202 < 1.4742^3 ∧
    (1.9656353:ℚ)*1.0529012 < 1.27438^3 ∧ (2.9413896:ℚ)*1.0534557 < 1.45789^3 := by
  norm_num

/-- remainder rates λ^{-1/6}(μ^{3-j} c^j Λ³)^{1/6} < T for j = 1,2,3, in sixth-power form with λ > 5.8284,
    μ* ≤ 1.916473, c = 0.76905, Λ = 1.9656353 -/
theorem remainder_rates :
    (1.916473:ℚ)^2*0.76905*1.9656353^3 < 1.28359^6*5.8284 ∧
    (1.916473:ℚ)*0.76905^2*1.9656353^3 < 1.28359^6*5.8284 ∧
    (0.76905:ℚ)^3*1.9656353^3 < 1.28359^6*5.8284 ∧
    (1.916473:ℚ)^2*0.76905*1.9656353^3 < 1.2426^6*5.8284 := by
  norm_num

/-- leading term: worst case rate λ^{-1/6}(μΛ)^{1/2} exceeds T even with the smallest μ* and largest λ -/
theorem leading_fails : (1.28359:ℚ)^6*5.8285 < (1.91447*1.9656353)^3 := by norm_num

end LineN4
