import Mathlib
/-!
# Line N20 — renewal lemma, joint-carry Green bound, conditional H1 ⇒ H3 arithmetic
Grok Bot, 2026-11-01. No `sorry`, no `native_decide`.
-/
namespace LineN20T

/-! ## 1. Renewal lemma (REPORT_N20 Lemma R): geometric bound uniform in the length.
`t n` majorises ‖𝒯_n‖ (paths 0 → 0 of length n), `e k` majorises ‖𝓔_k‖ (first-return excursions of length k);
the first-return decomposition gives t(n+1) ≤ Σ_{k=0}^{n} e(k+1) t(n−k). If Σ_k e_k r^{−k} ≤ 1 then t n ≤ rⁿ. -/
theorem renewal (e t : ℕ → ℝ) (r : ℝ) (hr : 0 < r) (he : ∀ k, 0 ≤ e k)
    (h0 : t 0 ≤ 1)
    (hrec : ∀ n, t (n+1) ≤ ∑ k ∈ Finset.range (n+1), e (k+1) * t (n - k))
    (hsum : ∀ N, ∑ k ∈ Finset.range N, e (k+1) * (r⁻¹) ^ (k+1) ≤ 1) :
    ∀ n, t n ≤ r ^ n := by
  intro n
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    cases n with
    | zero => simpa using h0
    | succ n =>
      have hr0 : r ≠ 0 := hr.ne'
      calc t (n+1) ≤ ∑ k ∈ Finset.range (n+1), e (k+1) * t (n - k) := hrec n
        _ ≤ ∑ k ∈ Finset.range (n+1), e (k+1) * r ^ (n - k) := by
          apply Finset.sum_le_sum
          intro k hk
          exact mul_le_mul_of_nonneg_left (ih (n - k) (by omega)) (he _)
        _ = r ^ (n+1) * ∑ k ∈ Finset.range (n+1), e (k+1) * (r⁻¹) ^ (k+1) := by
          rw [Finset.mul_sum]
          apply Finset.sum_congr rfl
          intro k hk
          have hk' : k < n + 1 := Finset.mem_range.mp hk
          have hp : r ^ (n+1) = r ^ (n - k) * r ^ (k+1) := by
            rw [← pow_add]; congr 1; omega
          rw [hp, inv_pow]
          have hq : r ^ (k+1) ≠ 0 := pow_ne_zero _ hr0
          field_simp
        _ ≤ r ^ (n+1) * 1 := mul_le_mul_of_nonneg_left (hsum _) (pow_nonneg hr.le _)
        _ = r ^ (n+1) := mul_one _

/-! ## 2. Joint (ε-chain) carries: Green ℓ¹ norm of 1/(z² − 2z − 1) and the bound |e| ≤ 51 -/
theorem eps_green_l1 : (Real.sqrt 2 + 1) / (2 * Real.sqrt 2) = (2 + Real.sqrt 2) / 4 := by
  have h2 : Real.sqrt 2 * Real.sqrt 2 = 2 := Real.mul_self_sqrt (by norm_num)
  have hs : Real.sqrt 2 ≠ 0 := by positivity
  field_simp; nlinarith [h2]
theorem eps_carry_lt52 : 60 * ((2 + Real.sqrt 2) / 4) < 52 := by
  have : Real.sqrt 2 < 22/15 := by
    rw [Real.sqrt_lt' (by norm_num)]; norm_num
  linarith
theorem eps_carry_ge51 : 51 < 60 * ((2 + Real.sqrt 2) / 4) := by
  have : (7/5 : ℝ) < Real.sqrt 2 := by
    rw [Real.lt_sqrt (by norm_num)]; norm_num
  linarith
/-- integer carries with |e| < 52 satisfy |e| ≤ 51 -/
theorem eps_carry_int (e : ℤ) (h : |e| < 52) : |e| ≤ 51 := by
  rcases abs_lt.mp h with ⟨h1, h2⟩
  exact abs_le.mpr ⟨by omega, by omega⟩
/-- the single-window λ-carry Green norm 1/4 is smaller than the joint one (2+√2)/4 -/
theorem joint_bigger : (1:ℝ)/4 < (2 + Real.sqrt 2) / 4 := by
  have : (0:ℝ) < Real.sqrt 2 := by positivity
  linarith

/-! ## 3. Conditional H1 ⇒ H3 bookkeeping (REPORT_N20 Prop. K): rational checks of the arb outputs (tail_kp.json).
C^{3/2} is bounded by a rational t with t² ≥ C³; the geometric factors are arb-enclosed in tail_kp.py. -/
theorem c32_082 : (0.082 : ℚ) ^ 3 ≤ 0.023482 ^ 2 := by norm_num
theorem c32_088e4 : (8.8e-4 : ℚ) ^ 3 ≤ 2.6106e-5 ^ 2 := by norm_num
/-- Prop. K, J₀ = 12, C = 0.082 (arb upper bounds from tail_kp.json, rounded up): KP and budget -/
theorem kp_J12_C082 : (3.445646e-4 : ℚ) + 1.147569e-2 / 5 ≤ 2.692494e-3 ∧
    (3.445646e-4 : ℚ) + 2.470e-6 < 6.234e-4 := by norm_num
/-- Prop. K, J₀ = 12, C = 8.8e-4 (2 × measured size) -/
theorem kp_J12_C88e5 : (2.379785e-6 : ℚ) + 2.854120e-5 / 5 ≤ 8.249783e-6 ∧
    (2.379785e-6 : ℚ) + 2.470e-6 < 6.234e-4 / 100 := by norm_num
/-- Prop. K, J₀ = 14 (finite part through j = 14, Thm A), C = 0.082 -/
theorem kp_J14_C082 : (1.316583e-4 : ℚ) + 4.867908e-3 / 5 ≤ 1.127e-3 ∧
    (1.316583e-4 : ℚ) + 2.470e-6 < 6.234e-4 := by norm_num
/-- margin of the certified shell constant: max_j C_cert(j) (j ≤ 14) ≤ 4.36e-4 vs 0.082 -/
theorem shell_margin : (0.082 : ℚ) / 4.36e-4 > 188 := by norm_num
