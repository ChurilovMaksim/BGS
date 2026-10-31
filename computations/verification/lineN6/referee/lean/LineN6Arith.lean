import Mathlib
/-! Referee arithmetic checks for BGS Line N6 (Grok Bot audit). Uses only norm_num / nlinarith / linarith. -/

/-- F_m constant: 16 (Re w*_lo - E) >= 2.3e-3 with Re w*_lo = 2.890e-4, E <= 1.4311e-4 (also with the 1.44e-4 variant). -/
theorem fm_const : (16:ℚ) * (2890/10^7 - 14311/10^8) ≥ 23/10^4 := by norm_num
theorem fm_const_144 : (16:ℚ) * (2890/10^7 - 144/10^6) ≥ 23/10^4 := by norm_num
/-- E(290) <= Re w*_lo / 2  (the margin is only ~1%). -/
theorem E_half : (14311:ℚ)/10^8 < (28895/10^8)/2 := by norm_num

/-- Prop X error formula at w = 290 with N6's printed upper bounds:
 6 (T1 Gb + 1) eta (Pi*rmax + eta)^5 <= 1.4312e-4. -/
theorem E290 :
    6 * ((381182:ℚ)/1000 * 390538489 + 1) * (11559/10^24) * ((21968116:ℚ)/10^6 * 3066/10^4 + 1/10^19)^5
      ≤ 14312/10^8 := by norm_num

/-- the dominant eta term: coll = 2 Gb^2 R2p mu^(-145) <= 1.1559e-20, using mu >= 1.9154712. -/
theorem coll290 :
    2 * (390538489:ℚ)^2 * (32248382/10^4) ≤ (11559/10^24) * ((19154712:ℚ)/10^7)^145 := by norm_num

/-- p0 bookkeeping: half-window floor(((p-1)/2-1)/2) for p = 1165 and p = 1163 (both give 290). -/
theorem p0_1165 : ((1165 - 1)/2 - 1)/2 = 290 := by norm_num
theorem p0_1163 : ((1163 - 1)/2 - 1)/2 = 290 := by norm_num
theorem p0_1161 : ((1161 - 1)/2 - 1)/2 = 289 := by norm_num

/-- rate comparisons used by the C' absorption -/
theorem rate1 : (1274:ℚ)/1000 < 142785/100000 := by norm_num
theorem rate2 : (145789:ℚ)/100000 < 164/100 := by norm_num

/-- lambda bracket -/
theorem lam_bracket : (58284:ℝ)/10^4 < 3 + 2*Real.sqrt 2 ∧ 3 + 2*Real.sqrt 2 < 58285/10^4 := by
  have h0 : (0:ℝ) ≤ Real.sqrt 2 := Real.sqrt_nonneg 2
  have hs : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  constructor <;> nlinarith [hs, h0]

/-- FINDING N6-F(rounding): the target written "1.640 = mu*^2/(1.6677 lambda^(1/6))" is rounded UP; the true value is 1.639991.
 (mu^2/(1.6677*1.640))^6 < 5.8284 < lambda, so 1.640 exceeds the target; 1.6399 is a valid strict target. -/
theorem rate16_rounded_up : ((19154712:ℚ)^2/10^14 / (16677/10^4 * 164/100))^6 < 58284/10^4 := by norm_num
theorem rate16_ok : ((19154712:ℚ)^2/10^14 / (16677/10^4 * 16399/10^4))^6 > 58285/10^4 := by norm_num
theorem rate16_real : (3 + 2*Real.sqrt 2) < ((19154712:ℝ)^2/10^14 / (16677/10^4 * 16399/10^4))^6 := by
  have h := (lam_bracket).2
  have h2 : ((58285:ℝ)/10^4) < ((19154712:ℝ)^2/10^14 / (16677/10^4 * 16399/10^4))^6 := by norm_num
  linarith
theorem rate2' : (145789:ℚ)/100000 < 16399/10^4 := by norm_num

/-- c* box from the n_cert boxes (corner bounds of |rA|^2, |rB|^2, squared moduli, rational):
 |rA|^2 >= 0.171955^2+0.165149^2, |rB|^2 >= 0.175382^2+0.240429^2 and c*^2 = (|rA|^2|rB|^2)^3 >= (3.447e-4)^2. -/
theorem cstar_lo :
    (((171955:ℚ)/10^6)^2 + (165149/10^6)^2) ^ 3 * (((175382:ℚ)/10^6)^2 + (240429/10^6)^2) ^ 3 ≥ (3447/10^7)^2 := by norm_num
theorem cstar_hi :
    (((178406:ℚ)/10^6)^2 + (171600/10^6)^2) ^ 3 * (((181806:ℚ)/10^6)^2 + (246853/10^6)^2) ^ 3 ≤ (4443/10^7)^2 := by norm_num
