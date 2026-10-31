import Mathlib
/-! Referee arithmetic checks for BGS Line N7 (Grok Bot audit). Uses only norm_num / field_simp / ring / nlinarith / linear_combination. -/

/-- Identity (I) of REPORT_N7 §2, abstract form.  x = ε (≠0), s = √2 (≠0), a = x^k, sg = (-1)^k (so ε'^k = sg/a),
P = x^(2k+1) = a*a*x with P = 2q + 1/P (i.e. 2q = ε^p − ε^{−p}).  For y = x^(2i) (any power, here kept abstract):
 y·e·(a·x − sg/a)/s/(8q) = e·y/a/(4s) + e·(y/(a·P) − sg·y/a)/(8·s·q). -/
theorem identity_I (x s q a sg y e P : ℝ) (hx : x ≠ 0) (hs : s ≠ 0) (hq : q ≠ 0) (ha : a ≠ 0) (hP : P = a*a*x)
    (hP0 : P ≠ 0) (h2q : P = 2*q + 1/P) :
    y*e*(a*x - sg/a)/s/(8*q) = e*y/a/(4*s) + e*(y/(a*P) - sg*y/a)/(8*s*q) := by
  have hP' : a*a*x = 2*q + 1/P := by rw [← hP]; exact h2q
  field_simp
  rw [hP] at h2q ⊢
  field_simp at h2q
  linear_combination (4*y*e) * h2q

/-- N7 F5: composite-weight worst case. omega <= p ln eps/ln(2p-1) at p = 1165 is <= 132.5;
 loss 2*omega/(2p-1) <= 0.1138, and 2.3344e-3*(1-0.1138) >= 2.06e-3. -/
theorem loss_1165 : (2:ℚ)*1325/10/(2*1165-1) ≤ 1138/10000 := by norm_num
theorem fm206 : (23344:ℚ)/10^7*(1 - 1138/10000) ≥ 206/10^5 := by norm_num

/-- (±2,16) rate gap: 1.6355^2 < 2.7350 (i.e. 1.6355 < sqrt(mu*^2 lam^{-1/6})), and 1.6355^2/2.7350 <= 0.97802. -/
theorem r16_sq : (16355:ℚ)^2/10^8 < 27350/10^4 := by norm_num
theorem r16_rate : (16355:ℚ)^2/10^8/(27350/10^4) ≤ 97802/100000 := by norm_num
/-- contour radius |b11|+r1 = 1.6154129681 + 0.02 <= 1.6355 -/
theorem contour : (16154129681:ℚ)/10^10 + 2/100 ≤ 16355/10^4 := by norm_num

/-- §4.4 threshold: mu*^3 lam^{-1/2}/Lambda = 1.48100 at Lambda = 1.9656; robust form with Lambda <= 1.9657 with mu* >= 1.9154712, Lambda <= 1.9657,
 lam^{1/2} = 1+sqrt2 <= 2.41422. -/
theorem thr1481 : ((19154712:ℚ)/10^7)^3 / (241422/10^5) / (19657/10^4) ≥ 14808/10000 := by norm_num
/-- sup-norm exponent: (Lambda/mu*)^6 vs lam^{0.088}: (1.9656/1.9154712)^6 >= lam^0.08 i.e. ^{6*25} >= lam^2 (lam<=5.8285) -/
theorem supexp : ((19656:ℚ)/10^4/(19154712/10^7))^(150) ≥ (58285/10^4)^2 := by norm_num
