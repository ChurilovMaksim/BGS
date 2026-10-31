import Mathlib
/-! Referee arithmetic checks, Lines N13b, N14b, N14 (Grok Bot audit). No sorry, no native_decide. -/

def stepXY (q : ℕ × ℕ) : ℕ × ℕ := (q.1 + 2*q.2, q.1 + q.2)
/-- x-coordinate of (1+√2)^p = x + y√2 -/
def hP (p : ℕ) : ℕ := (stepXY^[p-1] (1,1)).1

theorem h5 : hP 5 = 41 := by decide
theorem h7 : hP 7 = 239 := by decide
theorem h11 : hP 11 = 23 * 353 := by decide
theorem h13 : hP 13 = 79 * 599 := by decide
theorem h17 : hP 17 = 103 * 15607 := by decide
theorem h31 : hP 31 = 424577 * 865087 := by rfl
theorem h19 : hP 19 = 9369319 := by rfl
-- primality (small NSW primes and the p = 31 factors); larger p (29, 47, 59, 163, 257) checked with FLINT's proving test
theorem p41 : Nat.Prime 41 := by norm_num
theorem p239 : Nat.Prime 239 := by norm_num
theorem p9369319 : Nat.Prime 9369319 := by norm_num
theorem p424577 : Nat.Prime 424577 := by norm_num
theorem p865087 : Nat.Prime 865087 := by norm_num
theorem p353 : Nat.Prime 353 := by norm_num
theorem p23 : Nat.Prime 23 := by norm_num

-- exact mixed-class point counts at p = 11: |H_d| = (2d-1)(q-1)^2  (d iso part, q = h/d unit part)
theorem H353 : (2*353-1)*(23-1)^2 = 341220 ∧ 341220 * 353 < 2 * 8119^2 := by norm_num
theorem H23 : (2*23-1)*(353-1)^2 = 5575680 ∧ 5575680 * 23 < 2 * 8119^2 := by norm_num
-- mixed weight: exact max |κ|/n ≤ 2/(q_u-2) = 2/21 < 2^ω·2d/h = 4·353/8119
theorem weight_bound : (2:ℚ)/21 < 4*353/8119 := by norm_num

-- C′ per-p ratio ε(1.2744/μ*)^3 ∈ (0.7109, 0.7110), so the coverage base 1/ratio ∈ (1.4064, 1.4067)
theorem Cprime_ratio :
    (7109/10000:ℚ) < (241421356/10^8)*((12744/10000)/(19154712/10^7))^3 ∧
    (241421357/10^8:ℚ)*((12744/10000)/(19154712/10^7))^3 < 7110/10000 := by norm_num
theorem coverA : (14064/10000:ℚ) * (7110/10000) < 1 ∧ 1 < (14067/10000:ℚ) * (7109/10000) := by norm_num
-- √h_p base √ε lies between: 1.4066² < ε < 1.588²  (so balanced semiprimes fall in Lemma 2's range, not in C′'s)
theorem sqrt_eps_between : (14066/10000:ℚ)^2 < 241421356/10^8 ∧ (241421357/10^8:ℚ) < (1588/1000)^2 := by norm_num
-- c_B: Λ_free^3/(Λ_free r2) = Λ_free^2/r2 ∈ (3.6695, 3.6697)
theorem cB_ratio : (36695/10000:ℚ) < (19656353/10^7)^2/(10529012/10^7) ∧
    (19656353/10^7:ℚ)^2/(10529012/10^7) < 36697/10000 := by norm_num
-- p = 31: largest proper divisor 865087 < 1.588^31 but > 1.4066^31 (newly covered by Lemma 2, not by C′)
theorem p31_cover : (865087:ℚ) < (1588/1000)^31 ∧ (14066/10000:ℚ)^31 < 865087 := by norm_num
-- μ*³/λ < 1.2059 (N13b quotes 1.2061; λ > 5.8284271)
theorem mu3_over_lam : (19154712/10^7:ℚ)^3 / (58284271/10^7) < 12059/10000 := by norm_num
-- R₃(4) = 1.153 < μ*³/λ (> 1.2057) < R₃(5) = 1.217
theorem press_threshold : (1153/1000:ℚ) < (19154712/10^7)^3/(58284272/10^7) ∧
    (19154712/10^7:ℚ)^3/(58284271/10^7) < 1217/1000 := by norm_num
-- N14 rate: λρ̄² < 0.4579 (ρ̄_true ≤ 0.28028) and (λρ̄²)^{3/2} < 0.31
theorem rate14 : (58284272/10^7:ℚ)*(28028/10^5)^2 < 4579/10^4 ∧ (4579/10^4:ℚ)^3 < (31/100)^2 := by norm_num
theorem core_true : (1+1/1000:ℚ)*(28/100) = 28028/10^5 := by norm_num
-- (A) budget: A_bad(g0=6, certified finite part) + δ_int + Lemma-D tail < Re Λ_lo′/100
theorem budget14 : (366436/10^11:ℚ) + 514415/10^12 + 156/10^10 < (6234/10^7)/100 := by norm_num
-- short types reconcile: 27 + 4 + 169 = 200 ; 95 + 1 (α = 4) = 96
theorem short_reconcile : 27 + 4 + 169 = 200 ∧ 95 + 1 = 96 := by norm_num
