import Mathlib
/-! Lines N15, N17b, THEOREM_DRAFT v2: referee arithmetic checks (`mathematics/fixed-map/lineN5N18_gas_conditional.md`).
Referee file `computations/verification/lineN15/referee/lean/LineN15Arith.lean` (sha256 154d527f…), integrated verbatim inside the namespace `Bgs.LineN15`;
only `#print axioms` lines were added (one per theorem, 29). No sorry, no native_decide. -/
namespace Bgs.LineN15

/-! Referee lineN15 arithmetic (Grok Bot). No sorry, no native_decide. -/

/-- NSW-type sequence: h_p = x_p with (1+√2)^p = x_p + y_p √2. -/
def xy : ℕ → ℕ × ℕ
  | 0 => (1, 0)
  | n+1 => let (x, y) := xy n; (x + 2*y, x + y)
def hP (n : ℕ) : ℕ := (xy n).1

-- h_{3p} = h_p (4 h_p^2 + 3), 7 ∣ K_p  (p = 5, 7, 11, 13), h_15 = 7·31²·41
theorem h3p_5 : hP 15 = hP 5 * (4 * hP 5 ^ 2 + 3) := by decide
theorem h3p_7 : hP 21 = hP 7 * (4 * hP 7 ^ 2 + 3) := by decide
theorem h3p_11 : hP 33 = hP 11 * (4 * hP 11 ^ 2 + 3) := by decide
theorem h3p_13 : hP 39 = hP 13 * (4 * hP 13 ^ 2 + 3) := by decide
theorem seven_K : 7 ∣ 4 * hP 5 ^ 2 + 3 ∧ 7 ∣ 4 * hP 7 ^ 2 + 3 ∧ 7 ∣ 4 * hP 11 ^ 2 + 3 ∧ 7 ∣ 4 * hP 13 ^ 2 + 3 := by decide
theorem h15 : hP 15 = 7 * 31 ^ 2 * 41 := by decide
theorem h11 : hP 11 = 23 * 353 := by decide

-- CRT bookkeeping at h = 8119 (N17b §5b): φ(8119) = 7744, 7743 − 7371 = 372 = 21 + 351
theorem tot8119 : Nat.totient 8119 = 7744 := by
  have h23 : Nat.Prime 23 := by norm_num
  have h353 : Nat.Prime 353 := by norm_num
  have : (8119 : ℕ) = 23 * 353 := by norm_num
  rw [this, Nat.totient_mul (by norm_num), Nat.totient_prime h23, Nat.totient_prime h353]
theorem crt_counts : (23 - 2) * (353 - 2) = 7371 ∧ 7744 - 1 - 7371 = 372 ∧ (23 - 2) + (353 - 2) = 372 := by norm_num
theorem nratio : ((7371 : ℚ) / 8119) = (21 / 23) * (351 / 353) := by norm_num

-- N15 c3_mid derived constant: kappa_der < 5.863e-14 and KAP = 1e-13 + 2u ≥ kappa_der + 3u
-- u = 2^-53, γ_n = n u/(1 - n u), complex γ: √2 γ_{n+2}; √2 ≤ 1.41422, π ≤ 3.1416.
def u : ℚ := 1 / 2 ^ 53
def gam (n : ℚ) : ℚ := n * u / (1 - n * u)
def epsc : ℚ := 4 * u * (3.1416 * 30) + 16 * u
def kapd : ℚ := (1 + epsc) * (1 + 1.41422 * gam 57) * (1 + 1.41422 * gam 2) * (1 + gam 53) - 1
theorem epsc_bound : epsc < 4.3632e-14 := by unfold epsc u; norm_num
theorem kapd_bound : kapd < 5.879e-14 := by unfold kapd epsc gam u; norm_num
theorem kap_slack : kapd + 3 * u < 1e-13 + 2 * u := by unfold kapd epsc gam u; norm_num

-- KP criterion S0 + S1/(1+g0) ≤ a (printed values rounded against the claim)
theorem kp_g2 : (6.973771e-7 : ℚ) + 4.562510e-6 / 3 ≤ 2.329124e-6 := by norm_num
theorem kp_g3 : (1.318684e-6 : ℚ) + 9.781630e-6 / 4 ≤ 3.952295e-6 := by norm_num
theorem kp_g4 : (2.062875e-6 : ℚ) + 1.793574e-5 / 5 ≤ 5.932523e-6 := by norm_num
theorem kp_g5 : (2.836414e-6 : ℚ) + 2.872792e-5 / 6 ≤ 8.005618e-6 := by norm_num
theorem kp_g6 : (3.696009e-6 : ℚ) + 4.289458e-5 / 7 ≤ 1.031499e-5 := by norm_num
theorem kp_budget : (2.062875e-6 : ℚ) + 5.14476e-7 < 2.5774e-6 ∧ (2.5774e-6 : ℚ) < 6.234e-4 / 200 := by norm_num

-- δ_int rounding: coded upper 5.144750e-7 ≤ 5.14476e-7; N17b's a = 6.2289e-4 exceeds Re Λ_lo′ − δ_int (rounded the wrong way)
theorem dint_round : (5.144751e-7 : ℚ) ≤ 5.14476e-7 := by norm_num
theorem a_wrong_way : (6.234e-4 : ℚ) - 5.14476e-7 < 6.2289e-4 ∧ (6.234e-4 : ℚ) - 5.14415e-7 < 6.2289e-4 := by norm_num

-- carry Green kernel: Σ_k λ^{-|k|}/(4√2) = 1/4, via (λ+1)/(λ-1) = √2 with λ = 3+2√2; hence |e| ≤ 60/4 = 15 (strict ⇒ ≤ 14)
theorem green_ratio : (4 + 2 * Real.sqrt 2) = Real.sqrt 2 * (2 + 2 * Real.sqrt 2) := by
  have h : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  nlinarith [h]
theorem green_sum : (1 / (4 * Real.sqrt 2)) * Real.sqrt 2 = 1 / 4 := by
  have hpos : 0 < Real.sqrt 2 := Real.sqrt_pos.mpr (by norm_num)
  field_simp
theorem carry_bound : (60 : ℚ) / 4 = 15 := by norm_num

-- wrap exponent: q = (λ ρ²)^{3/2}; with λ < 5.828428: q² = (λρ²)³ < 0.30982²  (ρ = 0.28028), > 0.3098² with λ > 5.828427
theorem wrap_q_028028 : ((5.828428 : ℚ) * 0.28028 ^ 2) ^ 3 < 0.30982 ^ 2 ∧ (0.3098 : ℚ) ^ 2 < (5.828427 * 0.28028 ^ 2) ^ 3 := by norm_num
theorem wrap_q_030 : ((5.828428 : ℚ) * 0.30 ^ 2) ^ 3 < 0.37993 ^ 2 ∧ (0.37990 : ℚ) ^ 2 < (5.828427 * 0.30 ^ 2) ^ 3 := by norm_num
-- eps16 base: ε^{1/3}(1.6355/μ)^2 < 0.9781  ⇔  ε (1.6355/μ)^6 < 0.9781^3 (ε < 2.41422, μ = 1.9154712)
theorem eps16 : (2.41422 : ℚ) * (1.6355 / 1.9154712) ^ 6 < 0.9781 ^ 3 := by norm_num
-- threshold m = 13 fails, m = 15 holds (TRACE-199 bound, d^2 ≤ h), using rational under/over-estimates of 1.9154712^m
theorem incl_15 : ((1 - 1/5.8 ^ 15 : ℚ) * (1.9154712 ^ 15 - 3012.3) / 2) ^ 2 ≥ 4 * 15 * 275807 := by norm_num
theorem incl_13_fails : ((1.9154712 ^ 13 - 3012.3 : ℚ) / 2) ^ 2 < 4 * 13 * 47321 := by norm_num

#print axioms h3p_5
#print axioms h3p_7
#print axioms h3p_11
#print axioms h3p_13
#print axioms seven_K
#print axioms h15
#print axioms h11
#print axioms tot8119
#print axioms crt_counts
#print axioms nratio
#print axioms epsc_bound
#print axioms kapd_bound
#print axioms kap_slack
#print axioms kp_g2
#print axioms kp_g3
#print axioms kp_g4
#print axioms kp_g5
#print axioms kp_g6
#print axioms kp_budget
#print axioms dint_round
#print axioms a_wrong_way
#print axioms green_ratio
#print axioms green_sum
#print axioms carry_bound
#print axioms wrap_q_028028
#print axioms wrap_q_030
#print axioms eps16
#print axioms incl_15
#print axioms incl_13_fails

end Bgs.LineN15
