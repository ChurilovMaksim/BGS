import Mathlib
/-! Cheap Line N3 arithmetic checks (referee). λ ≥ 5828/1000 is used as a lower bound (λ = 3+2√2 = 5.8284…). -/
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
