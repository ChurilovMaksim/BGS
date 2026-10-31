import Mathlib
/-! Line N4 arithmetic (`mathematics/fixed-map/lineN2N4_inherited_level.md`, `computations/verification/lineN4/REPORT_N4_v2.md`).
Referee file `computations/verification/lineN4/referee/lean/LineN4Arith.lean` (sha256 550cc1be…), integrated inside the namespace `Bgs.LineN4`.
Changes at integration: (1) the 16V bound is 2.9413897, not 2.9413896 (I-1; the referee's `(2.9413896:ℚ) ≤ 2.9413896` omitted the
16V penalty 3.9e-8), see `lam16V_rounding`; (2) the referee's `remainder_rates` and `leading_fails` are left out: they concern the
single-slow-window analysis of N4 §3.3–§3.4, which Line N5 supersedes (REPORT_N4_v2 I-2) and which is not registered;
(3) added `unit_rates_registered` (8E/16E rates, margins) and `lemI16_V` (Lemma I₁₆ exponents). `#print axioms` for every theorem. No sorry, no native_decide.
λ = 3 + 2√2 is handled through rational brackets 5.8284 < λ < 5.8285. -/
namespace Bgs.LineN4

/-- rational bracket for λ = 3+2√2 -/
theorem lam_bracket : (5.8284:ℝ) < 3 + 2*Real.sqrt 2 ∧ 3 + 2*Real.sqrt 2 < 5.8285 := by
  have h2 : (0:ℝ) ≤ Real.sqrt 2 := Real.sqrt_nonneg 2
  have hs : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  constructor <;> nlinarith [hs, h2]

/-- certificate assembly: max cell / core bound + penalty ≤ stated Λ, and Λ below the N2 thresholds -/
theorem assembly :
    (1.9656276:ℚ) + 0.0000077 ≤ 1.9656353 ∧ (0.4915878:ℚ) + 0.0000054 ≤ 0.4915932 ∧
    (2.9413896:ℚ) + 0.0000001 ≤ 2.9413897 ∧ (0.4474392:ℚ) + 0.0000004 ≤ 0.4474396 ∧
    (1.9656353:ℚ) < 2.00859 ∧ (0.4915932:ℚ) < 2.01046 ∧ (2.9413897:ℚ) < 3.04126 ∧ (0.4474396:ℚ) < 3.04280 := by
  norm_num

/-- unit-point rates (Λ r₂)^{1/3} below targets T = 1.28359 (8) and 1.4742 (16), in cubed form -/
theorem unit_rates :
    (1.9656353:ℚ)*1.0529012 < 1.28359^3 ∧ (0.4915932:ℚ)*1.0519234 < 1.28359^3 ∧
    (2.9413897:ℚ)*1.0534557 < 1.4742^3 ∧ (0.4474396:ℚ)*1.0529202 < 1.4742^3 ∧
    (1.9656353:ℚ)*1.0529012 < 1.27438^3 ∧ (2.9413897:ℚ)*1.0534557 < 1.45789^3 := by
  norm_num

/-- Theorem C′ unit-point rates as registered (cubed form): 8E 0.80266, 16E 0.77812, and the 8V margin δ: 1.27438 ≤ (1 − 0.0071)·1.28359. -/
theorem unit_rates_registered :
    (0.4915932:ℚ)*1.0519234 < 0.80266^3 ∧ (0.4474396:ℚ)*1.0529202 < 0.77812^3 ∧
    (1.27438:ℚ) ≤ (1 - 0.0071)*1.28359 ∧ (1.45789:ℚ) ≤ (1 - 0.011)*1.4742 := by
  norm_num

/-- Integration check (I-1): the 16V core bound f = 2.94138957 (≤ 2.9413896) plus the penalty 3.9e-8 (≤ 1e-7) does not fit under the
    author's rounded 2.9413896, which is why the registered bound is 2.9413897. -/
theorem lam16V_rounding : (2.9413896:ℚ) < 2.94138957 + 0.000000039 := by norm_num

/-- Lemma I₁₆ (V): O1→F one step θ = (1/2 + 1.2/λ)/0.9 < 1 and F→O1 two steps weight exponent −0.3 + 2.5/λ² < 0 (λ > 5.828). -/
theorem lemI16_V (l : ℝ) (hl : 5828/1000 < l) : 1/2 + (12/10)/l < 9/10 ∧ (5/2)/l^2 < 3/10 := by
  have h : (10:ℝ) < l^2 := by nlinarith
  constructor
  · have : (12/10)/l < 4/10 := by rw [div_lt_iff₀ (by linarith)]; linarith
    linarith
  · rw [div_lt_iff₀ (by positivity)]; linarith

#print axioms lam_bracket
#print axioms assembly
#print axioms unit_rates
#print axioms unit_rates_registered
#print axioms lam16V_rounding
#print axioms lemI16_V

end Bgs.LineN4
