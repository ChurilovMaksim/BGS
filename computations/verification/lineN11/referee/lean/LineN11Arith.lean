import Mathlib
/-! Referee arithmetic checks, Line N11 / N9b (Grok Bot audit). No sorry, no native_decide. -/

-- Λ = R + 2 w*  (N11 g_model2 values, rounded to 1e-10)
theorem Lam_re : |((61850:ℚ)/10^9 + 2*(343580/10^9)) - 74901/10^8| < 1/10^9 := by norm_num [abs_lt]
theorem Lam_im : |(-(19431:ℚ)/10^9 + 2*(195796/10^9)) - 372161/10^9| < 1/10^9 := by norm_num [abs_lt]

-- certified Re Λ_lo from archived enclosures: 2(Re fam_lo + Re near0_lo + Re e4_lo) - 2|w(e4s2)|_hi
theorem ReL_lo : (62383:ℚ)/10^8 < 2*((2883691903:ℚ)/10^13 + 235882003/10^13 + 35456/10^13) - 2*(424240/10^13) := by norm_num

-- Lower bound |1+X_gas| - 1 ≥ 2((1+a)^p - 1) with a = Re Λ_lo = 6.2383e-4; chunked Bernoulli in ℚ
theorem chunk_le (a : ℚ) (ha : 0 ≤ a) (c k : ℕ) : (1 + (c:ℚ)*a)^k ≤ (1+a)^(c*k) := by
  rw [pow_mul]; exact pow_le_pow_left₀ (by positivity) (one_add_mul_le_pow (by linarith) c) k
theorem hn161 : (2228:ℚ)/1000 < (1 + 8*(62383/10^8))^161 := by norm_num
theorem hn156 : (218:ℚ)/10 < (1 + 32*(62383/10^8))^156 := by norm_num
theorem key1289 (a X Y : ℚ) (ha : 0 ≤ a) (hY : 2228/1000 < Y) (hXY : Y ≤ X) :
    (245:ℚ)/100 < 2*(X*(1+a) - 1) := by nlinarith
theorem key5000 (X Y W : ℚ) (hY : 218/10 < Y) (hXY : Y ≤ X) (hW : 1 ≤ W) :
    (41:ℚ) < 2*(X*W - 1) := by nlinarith
/-- |1+X_gas| - 1 ≥ 2((1+ReΛ_lo)^p - 1) ≥ 2.45 at p = 1289 (N11: 2.468). -/
theorem bound1289 (a : ℚ) (ha : a = 62383/10^8) : (245:ℚ)/100 < 2*((1+a)^1289 - 1) := by
  have h0 : 0 ≤ a := by rw [ha]; norm_num
  have h := chunk_le a h0 8 161
  have hY : (2228:ℚ)/1000 < (1 + ((8:ℕ):ℚ)*a)^161 := by rw [ha]; push_cast; exact hn161
  have e : (1+a)^1289 = (1+a)^(8*161) * (1+a) := by rw [← pow_succ]
  rw [e]; exact key1289 a _ _ h0 hY h
/-- ≥ 41 at p = 5000 (N11: 43.2). -/
theorem bound5000 (a : ℚ) (ha : a = 62383/10^8) : (41:ℚ) < 2*((1+a)^5000 - 1) := by
  have h0 : 0 ≤ a := by rw [ha]; norm_num
  have h := chunk_le a h0 32 156
  have hY : (218:ℚ)/10 < (1 + ((32:ℕ):ℚ)*a)^156 := by rw [ha]; push_cast; exact hn156
  have hW : (1:ℚ) ≤ (1+a)^8 := one_le_pow₀ (by linarith)
  have e : (1+a)^5000 = (1+a)^(32*156) * (1+a)^8 := by rw [← pow_add]
  rw [e]; exact key5000 _ _ _ hY h hW

-- Coding lemma constants (s = √2, ε = 1+s)
theorem cmin_val (s : ℝ) (hs : s*s = 2) (h0 : 0 < s) : 2*s/(1+s) - 1 = 3 - 2*s := by
  rw [div_sub_one (by positivity), div_eq_iff (by positivity)]; linear_combination (2:ℝ)*hs
theorem g0_ok (s : ℝ) (hs : s*s = 2) (h0 : 0 < s) : 8/((41+29*s) - 1) < 3 - 2*s := by
  have h1 : (1.4142:ℝ) < s := by nlinarith
  have h2 : s < 1.4143 := by nlinarith
  rw [div_lt_iff₀ (by nlinarith)]; nlinarith
theorem eps5 (s : ℝ) (hs : s*s = 2) : (1+s)^5 = 41 + 29*s := by linear_combination (s^3 + 5*s^2 + 12*s + 20)*hs
-- injectivity mod γ̄: with coefficient bound B=4 (N11) G0=6 suffices; with the difference bound 2B=8, G0=6 fails, G0=7 works.
-- (ε/(ε-1))^2 = ε^2/2 = (3+2s)/2 ; condition K*(3+2s)/2 * ε^{-G0} < 1/2  ⇔  K*(3+2s) < ε^{G0}
theorem G0_B   (s : ℝ) (hs : s*s = 2) (h0 : 0 < s) : 16*(3+2*s) < 99 + 70*s ∧ ¬ (16*(3+2*s) < 41 + 29*s) := by
  constructor <;> [nlinarith; (push Not; nlinarith)]
theorem G0_2B  (s : ℝ) (hs : s*s = 2) (h0 : 0 < s) : ¬ (64*(3+2*s) < 99 + 70*s) ∧ 64*(3+2*s) < 239 + 169*s := by
  constructor <;> [(push Not; nlinarith); nlinarith]
theorem eps6 (s : ℝ) (hs : s*s = 2) : (1+s)^6 = 99 + 70*s := by linear_combination (s^4 + 6*s^3 + 17*s^2 + 32*s + 49)*hs
theorem eps7 (s : ℝ) (hs : s*s = 2) : (1+s)^7 = 239 + 169*s := by linear_combination (s^5 + 7*s^4 + 23*s^3 + 49*s^2 + 81*s + 119)*hs

-- κ = r2/μ*_lo
theorem kap85 : (44375:ℚ)/10^5 < (85/100)/(19154712/10^7) ∧ (85/100:ℚ)/(19154712/10^7) < 44376/10^5 := by norm_num
theorem kap80 : (41765:ℚ)/10^5 < (80/100)/(19154712/10^7) ∧ (80/100:ℚ)/(19154712/10^7) < 41766/10^5 := by norm_num
theorem kap_vs_meas : (769/1915:ℚ) < 41765/10^5 := by norm_num

-- N9b: Γ_eff(1/8) of the US point, m - s = 12, |r| = 1.3144e-3  ⇒ Γ_eff ∈ (1.1019, 1.1021)
theorem gUS_eff : ((11019/10^4)/(19154712/10^7):ℚ)^12 < 13144/10^7 ∧ (13144/10^7:ℚ) < ((11021/10^4)/(19154712/10^7))^12 := by norm_num
-- N9b: Γ_raw of US at p = 61 (m = 183) ∈ (1.847, 1.848)
theorem gUS_raw61 : ((1847/1000)/(19154712/10^7):ℚ)^183 < 13144/10^7 ∧ (13144/10^7:ℚ) < ((1848/1000)/(19154712/10^7))^183 := by norm_num
-- N9b: |r_US| = 1.315e-3 exceeds |w*| and Re Λ
theorem US_vs_w : (395453:ℚ)/10^9 < 13154/10^7 ∧ (74901:ℚ)/10^8 < 13154/10^7 := by norm_num
