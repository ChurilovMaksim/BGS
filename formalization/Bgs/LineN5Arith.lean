import Mathlib
/-! Line N5 (slow isotropic family; N5 v1 referee, rate arithmetic only): referee arithmetic checks (`mathematics/fixed-map/lineN5N18_gas_conditional.md`).
Referee file `computations/verification/lineN5/referee/lean/LineN5Arith.lean` (sha256 cc0f4627…), integrated verbatim inside the namespace `Bgs.LineN5`;
only `#print axioms` lines were added (one per theorem, 4). No sorry, no native_decide. -/
namespace Bgs.LineN5

/-! Referee (Grok Bot) cheap Lean targets for Line N5: rate comparisons, with λ = 3+2√2 < 5.8285 (see LineN4Arith.lam_bracket). -/
/-- family isotropic rate μ* λ^{-1/6} > T, sixth powers, worst case (smallest μ*, largest λ) -/
theorem fam_rate_gt_T : (1.28359:ℚ)^6 * 5.8285 < 1.9154712^6 := by norm_num
/-- cross-part rate μ*² λ^{-1/6} > ξ_lo -/
theorem cross_rate_gt_xi : (2.4586893:ℚ)^6 * 5.8285 < 1.9154712^12 := by norm_num
/-- and > λ^{1/2} (so φ⁻¹ × cross grows exponentially): μ*^12 > λ^3 · λ  -/
theorem cross_rate_gt_sqrt_lam : (5.8285:ℚ)^4 < 1.9154712^12 := by norm_num
/-- Lemma H algebra at p = 5: ε^5 = 41 + 29√2, ε'^5 = 41 - 29√2, sum 82 = 2 h_5, product -1 (so ε'^5 = -ε^-5) -/
theorem lemmaH_p5 : (41:ℤ)^2 - 2*29^2 = -1 := by norm_num

#print axioms fam_rate_gt_T
#print axioms cross_rate_gt_xi
#print axioms cross_rate_gt_sqrt_lam
#print axioms lemmaH_p5

end Bgs.LineN5
