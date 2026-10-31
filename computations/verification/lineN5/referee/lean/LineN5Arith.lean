import Mathlib
/-! Referee (Grok Bot) cheap Lean targets for Line N5: rate comparisons, with λ = 3+2√2 < 5.8285 (see LineN4Arith.lam_bracket). -/
namespace LineN5
/-- family isotropic rate μ* λ^{-1/6} > T, sixth powers, worst case (smallest μ*, largest λ) -/
theorem fam_rate_gt_T : (1.28359:ℚ)^6 * 5.8285 < 1.9154712^6 := by norm_num
/-- cross-part rate μ*² λ^{-1/6} > ξ_lo -/
theorem cross_rate_gt_xi : (2.4586893:ℚ)^6 * 5.8285 < 1.9154712^12 := by norm_num
/-- and > λ^{1/2} (so φ⁻¹ × cross grows exponentially): μ*^12 > λ^3 · λ  -/
theorem cross_rate_gt_sqrt_lam : (5.8285:ℚ)^4 < 1.9154712^12 := by norm_num
/-- Lemma H algebra at p = 5: ε^5 = 41 + 29√2, ε'^5 = 41 - 29√2, sum 82 = 2 h_5, product -1 (so ε'^5 = -ε^-5) -/
theorem lemmaH_p5 : (41:ℤ)^2 - 2*29^2 = -1 := by norm_num
end LineN5
