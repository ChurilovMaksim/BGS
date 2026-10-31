import Mathlib
/-! Lines N12b, N13: referee arithmetic checks (`mathematics/fixed-map/lineN5N18_gas_conditional.md`).
Referee file `computations/verification/lineN13/referee/lean/LineN13Arith.lean` (sha256 af3bac86…), integrated verbatim inside the namespace `Bgs.LineN13`;
only `#print axioms` lines were added (one per theorem, 15). No sorry, no native_decide. -/
namespace Bgs.LineN13

/-! Referee arithmetic checks, Lines N12b + N13 (Grok Bot audit). No sorry, no native_decide. -/

-- ℓ³ ≤ ℓ² step used in N13 §4.2:  (Σ x³)² ≤ (Σ x²)³ for x ≥ 0, i.e. Σ|w| ≤ (Σ|r_A r_B|²)^{3/2}.
theorem l3_le_l2 {ι : Type*} (s : Finset ι) (x : ι → ℝ) (hx : ∀ i, 0 ≤ x i) :
    (∑ i ∈ s, x i ^ 3) ^ 2 ≤ (∑ i ∈ s, x i ^ 2) ^ 3 := by
  set S := ∑ i ∈ s, x i ^ 2
  have hS : 0 ≤ S := Finset.sum_nonneg (fun i _ => sq_nonneg (x i))
  have h1 : (∑ i ∈ s, x i * x i ^ 2) ^ 2 ≤ (∑ i ∈ s, x i ^ 2) * (∑ i ∈ s, (x i ^ 2) ^ 2) :=
    Finset.sum_mul_sq_le_sq_mul_sq s (fun i => x i) (fun i => x i ^ 2)
  have h2 : ∑ i ∈ s, (x i ^ 2) ^ 2 ≤ S * S := by
    rw [Finset.sum_mul]
    apply Finset.sum_le_sum
    intro i hi
    have hle : x i ^ 2 ≤ S := Finset.single_le_sum (f := fun j => x j ^ 2) (fun j _ => sq_nonneg (x j)) hi
    nlinarith [sq_nonneg (x i)]
  have h3 : ∑ i ∈ s, x i ^ 3 = ∑ i ∈ s, x i * x i ^ 2 := by
    apply Finset.sum_congr rfl; intro i _; ring
  rw [h3]
  calc (∑ i ∈ s, x i * x i ^ 2) ^ 2 ≤ S * (∑ i ∈ s, (x i ^ 2) ^ 2) := h1
    _ ≤ S * (S * S) := mul_le_mul_of_nonneg_left h2 hS
    _ = S ^ 3 := by ring

-- T' = μ* ε^{-1/3}:  1.4295 > T'  ⇔ 1.4295³ ε > μ*³ ; uses ε > 2.41421356
theorem orbit_n4_above_Tp : (19154712/10^7:ℚ)^3 < (14295/10^4)^3 * (241421356/10^8) := by norm_num
theorem Tp_upper : (19154712/10^7:ℚ)^3 < (142786/10^5)^3 * (241421356/10^8) := by norm_num
theorem Tp_lower : (142785/10^5:ℚ)^3 * (241421357/10^8) < (19154712/10^7)^3 := by norm_num
-- fugacity at the most favourable admissible Γ (→ T'): q = μ*/(λΓ) ≥ 0.23016 (λ < 5.828428, Γ ≤ 1.42786)
theorem q_lower : (23016/10^5:ℚ) < (19154712/10^7) / ((5828428/10^6) * (142786/10^5)) := by norm_num
-- z(L)/K = q^L[(1+L)/(1-q) + q/(1-q)^2] at q = 0.23016:  L=1 > 0.687, L=2 > 0.2269
theorem zL1 : let q : ℚ := 23016/10^5; (687/1000:ℚ) < q*(2/(1-q) + q/(1-q)^2) := by norm_num
theorem zL2 : let q : ℚ := 23016/10^5; (2269/10^4:ℚ) < q^2*(3/(1-q) + q/(1-q)^2) := by norm_num
-- rank-p requirement z < 2.08e-4 ⇒ K < 3.03e-4 (L=1), K < 9.17e-4 (L=2)
theorem K_L1 (K : ℚ) (hK : 0 ≤ K) (h : K * (687/1000) < 208/10^6) : K < 303/10^6 := by nlinarith
theorem K_L2 (K : ℚ) (hK : 0 ≤ K) (h : K * (2269/10^4) < 208/10^6) : K < 917/10^6 := by nlinarith
-- budget per p in modulus form: 3z < ln(1+ReΛ_lo) ≈ 6.236e-4 ⇒ z < 2.08e-4 (ln(1+x) ≤ x)
theorem z_req : 3*(208/10^6:ℚ) ≤ 624/10^6 := by norm_num
-- N13 quadratic bound at the edge, cond
theorem quad_edge : (1:ℚ) + 101/10^14 + 4260*(1/256)^2 < 10651/10000 := by norm_num
theorem cond13 : (151962/10^4:ℚ)/(72010/10^5) < 211031/10^4 := by norm_num
-- Lemma D rate: max(0.45, λ^{-1/2}) = 0.45 since 0.45² λ > 1 (λ > 5.828)
theorem rateD : (1:ℚ) < (45/100)^2 * (5828/1000) := by norm_num
-- i.i.d. shell rate: λρ² < 0.4331 and (λρ²)^{3/2} < 0.2851, i.e. (λρ²)^3 < 0.2851²
theorem shell_rate : (5828428/10^6:ℚ)*(27255/10^5)^2 < 4331/10^4 ∧ ((4331/10^4:ℚ))^3 < (2851/10^4)^2 := by norm_num
-- absolute coded activity per site exceeds the budget rate: 2·4.2937e-4 > 6.234e-4
theorem abs_vs_budget : (6234/10^7:ℚ) < 2*(42937/10^8) := by norm_num

#print axioms l3_le_l2
#print axioms orbit_n4_above_Tp
#print axioms Tp_upper
#print axioms Tp_lower
#print axioms q_lower
#print axioms zL1
#print axioms zL2
#print axioms K_L1
#print axioms K_L2
#print axioms z_req
#print axioms quad_edge
#print axioms cond13
#print axioms rateD
#print axioms shell_rate
#print axioms abs_vs_budget

end Bgs.LineN13
