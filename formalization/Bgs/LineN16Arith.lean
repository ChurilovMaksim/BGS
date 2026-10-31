import Mathlib
/-! Lines N16, N18b, THEOREM_DRAFT v3 (final referee): referee arithmetic checks (`mathematics/fixed-map/lineN5N18_gas_conditional.md`).
Referee file `computations/verification/lineN16/referee/lean/LineN16Arith.lean` (sha256 007d0bd4…), integrated verbatim inside the namespace `Bgs.LineN16`;
only `#print axioms` lines were added (one per theorem, 8). No sorry, no native_decide. -/
namespace Bgs.LineN16

/-! lineN16 referee arithmetic (Grok Bot). No sorry, no native_decide. -/
open Real

/-- ε⁴ = 17 + 12√2 for ε = 1 + √2. -/
theorem eps4 : (1 + √2 : ℝ) ^ 4 = 17 + 12 * √2 := by
  have h : (√2 : ℝ) ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have h4 : (√2 : ℝ) ^ 4 = 4 := by nlinarith [h]
  have h3 : (√2 : ℝ) ^ 3 = 2 * √2 := by
    have : (√2:ℝ)^3 = (√2)^2 * √2 := by ring
    rw [this, h]
  nlinarith [h, h3, h4]

/-- growth scale μ²/ε^{4/3} < 1.13288 (μ = 1.9154712): μ⁶ < 1.13288³·ε⁴.  So "S_ρ ≥ c·1.13288^m" rounds the rate UP. -/
theorem scale_lt_113288 : (1.9154712 : ℝ) ^ 6 < 1.13288 ^ 3 * (17 + 12 * √2) := by
  have hs : (1.41421356 : ℝ) < √2 := by
    rw [Real.lt_sqrt] <;> norm_num
  have : (1.9154712 : ℝ) ^ 6 < 1.13288 ^ 3 * (17 + 12 * 1.41421356) := by norm_num
  nlinarith [hs]

/-- and the registry value 1.13287 (TRACE-271) is a valid lower rate: 1.13287³·ε⁴ < μ⁶. -/
theorem scale_gt_113287 : (1.13287 : ℝ) ^ 3 * (17 + 12 * √2) < 1.9154712 ^ 6 := by
  have hs : √2 < (1.41421357 : ℝ) := by
    rw [Real.sqrt_lt' (by norm_num)]; norm_num
  have : (1.13287 : ℝ) ^ 3 * (17 + 12 * 1.41421357) < 1.9154712 ^ 6 := by norm_num
  nlinarith [hs]

/-- T′ = μ/ε^{1/3} > 1.42785 : 1.42785³·(1+√2) < μ³. -/
theorem Tprime_gt : (1.42785 : ℝ) ^ 3 * (1 + √2) < 1.9154712 ^ 3 := by
  have hs : √2 < (1.41421357 : ℝ) := by
    rw [Real.sqrt_lt' (by norm_num)]; norm_num
  have : (1.42785 : ℝ) ^ 3 * (1 + 1.41421357) < 1.9154712 ^ 3 := by norm_num
  nlinarith [hs]

/-- N18b monotonicity: envelope slope bound 2e^γ/(2p+1) at p* = 1386 is < 0.0219 ≤ G'(p*). -/
theorem env_slope_small : 2 * exp eulerMascheroniConstant / (2 * 1386 + 1) < (0.0219 : ℝ) := by
  have h1 : exp eulerMascheroniConstant < exp 1 :=
    exp_lt_exp.mpr (eulerMascheroniConstant_lt_two_thirds.trans (by norm_num))
  have h2 := Real.exp_one_lt_d9
  rw [div_lt_iff₀ (by norm_num)]
  nlinarith [h1, h2]

/-- Lemma 1 constant: ⌈x⌉ < x + 1 gives λ^{n*-n} < λ²·(16δ²h²/d)·λ^{-n}; the factor is λ², not λ (λ > 1). -/
theorem lemma1_C (x : ℝ) : (⌈x⌉ : ℝ) < x + 1 := Int.ceil_lt_add_one x

/-- collision-constant margin 0.082/4.4e-4 > 186. -/
theorem coll_margin : (186 : ℝ) < 0.082 / 4.4e-4 := by norm_num

/-- s₀ = 1/(2√2): |N(γ)| ≥ 1/8 on O^∨ ⇒ max(|a|,|b|)² ≥ |ab| ≥ 1/8. -/
theorem max_sq_ge (a b : ℝ) : |a * b| ≤ max |a| |b| ^ 2 := by
  rw [abs_mul, sq]
  exact mul_le_mul (le_max_left _ _) (le_max_right _ _) (abs_nonneg _) (le_trans (abs_nonneg _) (le_max_left _ _))

#print axioms eps4
#print axioms scale_lt_113288
#print axioms scale_gt_113287
#print axioms Tprime_gt
#print axioms env_slope_small
#print axioms lemma1_C
#print axioms coll_margin
#print axioms max_sq_ge

end Bgs.LineN16
