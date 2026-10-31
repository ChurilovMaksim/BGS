import Mathlib
/-! Line N3 arithmetic (`mathematics/fixed-map/lineN2N4_inherited_level.md`, `computations/verification/lineN3/REPORT_N3_v2.md`).
Referee file `computations/verification/lineN3/referee/lean/LineN3Arith.lean` (sha256 7c52c8f1…), integrated unchanged inside the namespace
`Bgs.LineN3`, with `#print axioms` for every theorem. No sorry, no native_decide. λ ≥ 5828/1000 is used as a lower bound (λ = 3+2√2 = 5.8284…).
`rateV`, `rateE`, `margins` use the N3 [CA*] values; the registered Theorem C′ uses the N4 [CA] values (`Bgs.LineN4.unit_rates`). -/
namespace Bgs.LineN3
-- λ > 5.828 from √2 > 1.414
theorem lam_lb (s : ℝ) (hs : s^2 = 2) (hp : 0 < s) : (5828:ℝ)/1000 < 3 + 2*s := by nlinarith
-- Lemma I (V): O1→F one step, theta < 1  ⇐  1/2 + 1.2/λ < 0.75
theorem lemI_V_in (l : ℝ) (hl : 5828/1000 < l) : 1/2 + (12/10)/l < 3/4 := by
  have : (12/10)/l < 1/4 := by rw [div_lt_iff₀ (by linarith)]; linarith
  linarith
-- Lemma I (V): F→O1 two steps, weight exponent −0.25 + 2.5/λ² < 0
theorem lemI_V_out (l : ℝ) (hl : 5828/1000 < l) : (5/2)/l^2 < 1/4 := by
  have h : (10:ℝ) < l^2 := by nlinarith
  rw [div_lt_iff₀ (by positivity)]; linarith
-- Lemma I (E): F→O1 two steps exponent −0.3 + 2.5/λ² < 0; O1→F two steps theta: 0.1036 + 0.8/λ² < 0.2
theorem lemI_E_out (l : ℝ) (hl : 5828/1000 < l) : (5/2)/l^2 < 3/10 := by
  have h : (10:ℝ) < l^2 := by nlinarith
  rw [div_lt_iff₀ (by positivity)]; linarith
theorem lemI_E_in (l : ℝ) (hl : 5828/1000 < l) : 1036/10000 + (8/10)/l^2 < 2/10 := by
  have h : (33:ℝ) < l^2 := by nlinarith
  have : (8/10)/l^2 < 1/40 := by rw [div_lt_iff₀ (by positivity)]; linarith
  linarith
-- Theorem C′ rates: Λ·r₂ < 1.27440³ < T³ (8V); 8E
theorem rateV : (1965736:ℚ)/1000000 * (1052901/1000000) < (127440/100000)^3 := by norm_num
theorem rateV_T : (127440:ℚ)/100000 < 128359/100000 := by norm_num
theorem rateE : (1660338:ℚ)/1000000 * (1051923/1000000) < (120428/100000)^3 := by norm_num
-- Λ margins: 1.965736 < 2.00859 and 1.660338 < 2.01046
theorem margins : (1965736:ℚ)/1000000 < 200859/100000 ∧ (1660338:ℚ)/1000000 < 201046/100000 := by norm_num

#print axioms lam_lb
#print axioms lemI_V_in
#print axioms lemI_V_out
#print axioms lemI_E_out
#print axioms lemI_E_in
#print axioms rateV
#print axioms rateV_T
#print axioms rateE
#print axioms margins

end Bgs.LineN3
