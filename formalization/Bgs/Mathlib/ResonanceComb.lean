module
public import Mathlib
@[expose] public section

/-!
# Scalar inputs of the Pell resonance-comb theorem
(`mathematics/pell/pell_resonance_comb.md`, proof of Theorem 1)

* `exp_I_taylor_bound`: the global Taylor inequality
  `|e^{iux} − ∑_{l<n} (iux)^l/l!| ≤ |ux|^n/n!` for all real `u, x` and all `n`.
* `gaussian_moment_ratio`: `A^{2r}(2r−1)!!/(2r)! = A^{2r}/(2^r r!)`.
* `gaussian_moment_ratio_tendsto`: this tends to `0` as `r → ∞` (the final limit in the
  order "first `K`, then `r`").
-/

open Complex Filter Topology

namespace Bgs.Mathlib

namespace ResonanceComb

/-- Taylor remainder of `y ↦ e^{iy}`. -/
noncomputable def rem (n : ℕ) (y : ℝ) : ℂ :=
  Complex.exp (y * I) - ∑ l ∈ Finset.range n, ((y : ℂ) * I) ^ l / (l.factorial : ℂ)

lemma rem_zero_eq (n : ℕ) : rem (n + 1) 0 = 0 := by
  simp [rem, Finset.sum_range_succ']

lemma hasDerivAt_rem (n : ℕ) (y : ℝ) : HasDerivAt (rem (n + 1)) (I * rem n y) y := by
  have hexp : HasDerivAt (fun y : ℝ => Complex.exp (y * I)) (Complex.exp (y * I) * I) y := by
    have := ((hasDerivAt_id (y : ℝ)).ofReal_comp.mul_const I).cexp
    simpa using this
  have hsum : HasDerivAt (fun y : ℝ => ∑ l ∈ Finset.range (n + 1),
      ((y : ℂ) * I) ^ l / (l.factorial : ℂ))
      (∑ l ∈ Finset.range n, I * (((y : ℂ) * I) ^ l / (l.factorial : ℂ))) y := by
    have e : (fun y : ℝ => ∑ l ∈ Finset.range (n + 1), ((y : ℂ) * I) ^ l / (l.factorial : ℂ)) =
        fun y : ℝ => ∑ l ∈ Finset.range n, ((y : ℂ) * I) ^ (l + 1) / ((l + 1).factorial : ℂ) +
          ((y : ℂ) * I) ^ 0 / ((0 : ℕ).factorial : ℂ) := by
      funext y; rw [Finset.sum_range_succ']
    rw [e]
    have : ∀ l ∈ Finset.range n, HasDerivAt (fun y : ℝ => ((y : ℂ) * I) ^ (l + 1) /
        ((l + 1).factorial : ℂ)) (I * (((y : ℂ) * I) ^ l / (l.factorial : ℂ))) y := by
      intro l _
      have h0 : HasDerivAt (fun z : ℂ => (z * I) ^ (l + 1) / ((l + 1).factorial : ℂ))
          (((l + 1 : ℕ) : ℂ) * ((y : ℂ) * I) ^ l * I / ((l + 1).factorial : ℂ)) (y : ℂ) := by
        have := ((hasDerivAt_mul_const (x := (y : ℂ)) I).fun_pow (l + 1)).div_const
          ((l + 1).factorial : ℂ)
        simpa using this
      convert! h0.comp_ofReal using 1
      rw [Nat.factorial_succ]; push_cast
      have : (l.factorial : ℂ) ≠ 0 := by exact_mod_cast (Nat.factorial_pos l).ne'
      field_simp
    have h := (HasDerivAt.fun_sum this).add_const (((y : ℂ) * I) ^ 0 / ((0 : ℕ).factorial : ℂ))
    exact h
  convert! hexp.sub hsum using 1
  simp only [rem]
  rw [mul_sub, Finset.mul_sum, mul_comm]

lemma rem_neg (n : ℕ) (y : ℝ) : rem n (-y) = starRingEnd ℂ (rem n y) := by
  simp only [rem, map_sub, map_sum, map_div₀, map_pow, map_mul, map_natCast, conj_ofReal,
    conj_I, ← Complex.exp_conj]
  push_cast
  congr 1
  · ring_nf
  · refine Finset.sum_congr rfl fun l _ => ?_
    ring_nf

/-- The bound for `y ≥ 0`, by induction on `n`. -/
lemma norm_rem_le_of_nonneg : ∀ (n : ℕ) {y : ℝ}, 0 ≤ y →
    ‖rem n y‖ ≤ y ^ n / (n.factorial : ℝ)
  | 0, y, _ => by
      simp only [rem, Finset.range_zero, Finset.sum_empty, sub_zero, pow_zero,
        Nat.factorial_zero, Nat.cast_one, div_one]
      rw [Complex.norm_exp_ofReal_mul_I]
  | n + 1, y, hy => by
      have ih : ∀ t : ℝ, 0 ≤ t → ‖rem n t‖ ≤ t ^ n / (n.factorial : ℝ) :=
        fun t ht => norm_rem_le_of_nonneg n ht
      have := image_norm_le_of_norm_deriv_right_le_deriv_boundary (f := rem (n + 1))
        (a := 0) (b := y) (f' := fun t => I * rem n t)
        (fun t _ => (hasDerivAt_rem n t).continuousAt.continuousWithinAt)
        (fun t _ => (hasDerivAt_rem n t).hasDerivWithinAt)
        (B := fun t => t ^ (n + 1) / ((n + 1).factorial : ℝ))
        (B' := fun t => t ^ n / (n.factorial : ℝ))
        (by rw [rem_zero_eq]; simp)
        (fun t => by
          have := ((hasDerivAt_pow (n + 1) t).div_const ((n + 1).factorial : ℝ))
          convert! this using 1
          rw [Nat.factorial_succ]; push_cast
          field_simp)
        (fun t ht => by
          rw [norm_mul, Complex.norm_I, one_mul]; exact ih t ht.1)
        (Set.right_mem_Icc.2 hy)
      exact this

/-- **Global Taylor inequality** `|e^{iy} − ∑_{l<n} (iy)^l/l!| ≤ |y|^n/n!`. -/
theorem norm_rem_le (n : ℕ) (y : ℝ) : ‖rem n y‖ ≤ |y| ^ n / (n.factorial : ℝ) := by
  rcases le_total 0 y with hy | hy
  · rw [abs_of_nonneg hy]; exact norm_rem_le_of_nonneg n hy
  · have := norm_rem_le_of_nonneg n (neg_nonneg.2 hy)
    rw [rem_neg, Complex.norm_conj] at this
    rwa [abs_of_nonpos hy]

/-- The form used in the proof: `|e^{iux} − ∑_{l<n} (iux)^l/l!| ≤ |ux|^n/n!`. -/
theorem exp_I_taylor_bound (u x : ℝ) (n : ℕ) :
    ‖Complex.exp (I * (u * x)) - ∑ l ∈ Finset.range n, (I * (u * x)) ^ l / (l.factorial : ℂ)‖
      ≤ |u * x| ^ n / (n.factorial : ℝ) := by
  have := norm_rem_le n (u * x)
  simp only [rem] at this
  convert! this using 3
  · push_cast; ring_nf
  · refine Finset.sum_congr rfl fun l _ => ?_
    push_cast; ring_nf

/-- `A^{2r} (2r−1)!! / (2r)! = A^{2r} / (2^r r!)`. -/
theorem gaussian_moment_ratio (A : ℝ) (r : ℕ) :
    A ^ (2 * r) * ((2 * r - 1).doubleFactorial : ℝ) / ((2 * r).factorial : ℝ) =
      A ^ (2 * r) / (2 ^ r * (r.factorial : ℝ)) := by
  rcases Nat.eq_zero_or_pos r with rfl | hr
  · simp
  · have h : (2 * r).factorial = (2 * r).doubleFactorial * (2 * r - 1).doubleFactorial := by
      obtain ⟨m, rfl⟩ : ∃ m, r = m + 1 := ⟨r - 1, by omega⟩
      rw [show 2 * (m + 1) = (2 * m + 1) + 1 by ring, Nat.factorial_eq_mul_doubleFactorial]
      rfl
    rw [h, Nat.doubleFactorial_two_mul]
    push_cast
    have : ((2 * r - 1).doubleFactorial : ℝ) ≠ 0 := by
      exact_mod_cast (Nat.doubleFactorial_pos _).ne'
    field_simp

/-- The Gaussian moment ratio tends to zero as `r → ∞`. -/
theorem gaussian_moment_ratio_tendsto (A : ℝ) :
    Tendsto (fun r : ℕ => A ^ (2 * r) * ((2 * r - 1).doubleFactorial : ℝ) /
      ((2 * r).factorial : ℝ)) atTop (𝓝 0) := by
  simp_rw [gaussian_moment_ratio]
  have h := FloorSemiring.tendsto_pow_div_factorial_atTop (A ^ 2 / 2)
  refine h.congr fun r => ?_
  rw [div_pow, pow_mul, div_div]

#print axioms rem_zero_eq
#print axioms hasDerivAt_rem
#print axioms rem_neg
#print axioms norm_rem_le_of_nonneg
#print axioms norm_rem_le
#print axioms exp_I_taylor_bound
#print axioms gaussian_moment_ratio
#print axioms gaussian_moment_ratio_tendsto
end ResonanceComb

end Bgs.Mathlib
