module
public import Mathlib
@[expose] public section

/-!
# The `Sine₂` kernel, its pair correlation and its form factor

The README's unitary-class reference process has kernel
`K(x) = sin(πx)/(πx)` and distinct-point two-point function `ρ₂(x) = 1 - K(x)²`.
We prove the elementary facts used throughout the repository:

* `0 ≤ ρ₂ ≤ 1`, `ρ₂(0) = 0` (level repulsion), `ρ₂(n) = 1` at nonzero integers,
  and `ρ₂(x) → 1` as `x → ∞` (`sine2Pair_*`);
* **form factor**: `∫_{-1}^{1} (1 - |t|) cos(2π x t) dt = K(x)²`
  (`sineKernel_sq_eq_fourier_triangle`), i.e. the Fourier transform of `K²` is the
  triangle `(1-|t|)₊`; consequently the CUE form factor `min(|t|,1)` equals
  `1 - (1-|t|)₊` (`cue_form_factor_eq_one_sub_triangle`), matching the CUE trace
  value `min(m,N)/N` at `t = m/N`.
-/

open Real Filter Topology

namespace Bgs.Mathlib

/-- The sine kernel `K(x) = sin(πx)/(πx)` (with `K(0) = 1`). -/
noncomputable def sineKernel (x : ℝ) : ℝ := Real.sinc (π * x)

/-- The `Sine₂` distinct-point pair correlation `ρ₂(x) = 1 - K(x)²`. -/
noncomputable def sine2Pair (x : ℝ) : ℝ := 1 - sineKernel x ^ 2

theorem sineKernel_zero : sineKernel 0 = 1 := by simp [sineKernel]

theorem sineKernel_of_ne_zero {x : ℝ} (hx : x ≠ 0) : sineKernel x = sin (π * x) / (π * x) :=
  Real.sinc_of_ne_zero (mul_ne_zero pi_ne_zero hx)

theorem sineKernel_sq_le_one (x : ℝ) : sineKernel x ^ 2 ≤ 1 := by
  have := Real.abs_sinc_le_one (π * x)
  rw [sineKernel, ← sq_abs]
  nlinarith [abs_nonneg (Real.sinc (π * x))]

theorem sine2Pair_nonneg (x : ℝ) : 0 ≤ sine2Pair x := by
  unfold sine2Pair; linarith [sineKernel_sq_le_one x]

theorem sine2Pair_le_one (x : ℝ) : sine2Pair x ≤ 1 := by
  unfold sine2Pair; nlinarith [sq_nonneg (sineKernel x)]

/-- Level repulsion: `ρ₂(0) = 0`. -/
theorem sine2Pair_zero : sine2Pair 0 = 0 := by simp [sine2Pair, sineKernel_zero]

/-- `ρ₂(n) = 1` at every nonzero integer. -/
theorem sine2Pair_int {n : ℤ} (hn : n ≠ 0) : sine2Pair n = 1 := by
  have hx : (n : ℝ) ≠ 0 := by exact_mod_cast hn
  rw [sine2Pair, sineKernel_of_ne_zero hx, mul_comm, Real.sin_int_mul_pi]
  simp

/-- Decorrelation at large distance: `ρ₂(x) → 1` as `x → ∞`. -/
theorem sine2Pair_tendsto_one : Tendsto sine2Pair atTop (𝓝 1) := by
  have hK : Tendsto sineKernel atTop (𝓝 0) := by
    have hbound : Tendsto (fun x : ℝ => 1 / (π * x)) atTop (𝓝 0) := by
      have := (tendsto_const_mul_atTop_of_pos pi_pos).2 tendsto_id
      refine this.inv_tendsto_atTop.congr' (Eventually.of_forall fun x => ?_)
      simp [one_div]
    apply squeeze_zero_norm' _ hbound
    filter_upwards [eventually_gt_atTop 0] with x hx
    have hpx : 0 < π * x := mul_pos pi_pos hx
    rw [sineKernel_of_ne_zero hx.ne', Real.norm_eq_abs, abs_div, abs_of_pos hpx]
    exact div_le_div_of_nonneg_right (Real.abs_sin_le_one _) hpx.le
  have := (hK.pow 2).const_sub 1
  show Tendsto (fun x => 1 - sineKernel x ^ 2) atTop (𝓝 1)
  simpa using this

/-- Half-line form factor: `2 ∫₀¹ (1 - t) cos(2πxt) dt = K(x)²`. -/
theorem sineKernel_sq_eq_half_fourier (x : ℝ) :
    2 * ∫ t in (0 : ℝ)..1, (1 - t) * cos (2 * π * x * t) = sineKernel x ^ 2 := by
  by_cases hx : x = 0
  · subst hx
    simp only [mul_zero, zero_mul, Real.cos_zero, mul_one, sineKernel_zero]
    rw [intervalIntegral.integral_sub intervalIntegrable_const intervalIntegral.intervalIntegrable_id,
      integral_id]
    norm_num
  set w := 2 * π * x with hw
  have hw0 : w ≠ 0 := by rw [hw]; exact mul_ne_zero (mul_ne_zero two_ne_zero pi_ne_zero) hx
  have hderiv : ∀ t ∈ Set.uIcc (0 : ℝ) 1,
      HasDerivAt (fun t : ℝ => (1 - t) * sin (w * t) / w - cos (w * t) / w ^ 2)
        ((1 - t) * cos (w * t)) t := by
    intro t _
    have e1 : HasDerivAt (fun t : ℝ => 1 - t) (-1) t := by
      simpa using (hasDerivAt_id' t).const_sub 1
    have e2 : HasDerivAt (fun t : ℝ => sin (w * t)) (cos (w * t) * (w * 1)) t :=
      ((hasDerivAt_id' t).const_mul w).sin
    have e3 : HasDerivAt (fun t : ℝ => cos (w * t)) (-sin (w * t) * (w * 1)) t :=
      ((hasDerivAt_id' t).const_mul w).cos
    convert! ((e1.mul e2).div_const w).sub (e3.div_const (w ^ 2)) using 1
    field_simp
    ring
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv
    (by apply Continuous.intervalIntegrable; fun_prop)]
  simp only [sub_self, zero_mul, zero_div, mul_zero, Real.sin_zero, Real.cos_zero, mul_one,
    sub_zero]
  rw [sineKernel_of_ne_zero hx]
  have hcos : cos w = 1 - 2 * sin (π * x) ^ 2 := by
    rw [hw, show 2 * π * x = 2 * (π * x) by ring, Real.cos_two_mul, Real.cos_sq']; ring
  rw [hcos, hw]
  have hpx : π * x ≠ 0 := mul_ne_zero pi_ne_zero hx
  field_simp
  ring

/-- **Form factor of `Sine₂`.**  For every real `x`,
`∫_{-1}^{1} (1 - |t|) cos(2π x t) dt = K(x)²`. -/
theorem sineKernel_sq_eq_fourier_triangle (x : ℝ) :
    ∫ t in (-1 : ℝ)..1, (1 - |t|) * cos (2 * π * x * t) = sineKernel x ^ 2 := by
  have hint : ∀ a b : ℝ, IntervalIntegrable (fun t : ℝ => (1 - |t|) * cos (2 * π * x * t))
      MeasureTheory.volume a b := fun a b => by
    apply Continuous.intervalIntegrable; fun_prop
  rw [← intervalIntegral.integral_add_adjacent_intervals (hint (-1) 0) (hint 0 1)]
  have hneg : ∫ t in (-1 : ℝ)..0, (1 - |t|) * cos (2 * π * x * t) =
      ∫ t in (0 : ℝ)..1, (1 - |t|) * cos (2 * π * x * t) := by
    have := intervalIntegral.integral_comp_neg (a := (0 : ℝ)) (b := 1)
      (fun t : ℝ => (1 - |t|) * cos (2 * π * x * t))
    simp only [abs_neg, mul_neg, Real.cos_neg, neg_zero] at this
    exact this.symm
  have hpos : ∫ t in (0 : ℝ)..1, (1 - |t|) * cos (2 * π * x * t) =
      ∫ t in (0 : ℝ)..1, (1 - t) * cos (2 * π * x * t) := by
    apply intervalIntegral.integral_congr
    intro t ht
    rw [Set.uIcc_of_le zero_le_one] at ht
    simp only [abs_of_nonneg ht.1]
  rw [hneg, hpos, ← two_mul, sineKernel_sq_eq_half_fourier]

/-- The CUE form factor in scaled time is one minus the `Sine₂` triangle:
`min(|t|, 1) = 1 - (1 - |t|)₊`. -/
theorem cue_form_factor_eq_one_sub_triangle (t : ℝ) :
    min |t| 1 = 1 - max (1 - |t|) 0 := by
  rcases le_total |t| 1 with h | h
  · rw [min_eq_left h, max_eq_left (by linarith)]; ring
  · rw [min_eq_right h, max_eq_right (by linarith)]; ring

#print axioms sineKernel_zero
#print axioms sineKernel_of_ne_zero
#print axioms sineKernel_sq_le_one
#print axioms sine2Pair_nonneg
#print axioms sine2Pair_le_one
#print axioms sine2Pair_zero
#print axioms sine2Pair_int
#print axioms sine2Pair_tendsto_one
#print axioms sineKernel_sq_eq_half_fourier
#print axioms sineKernel_sq_eq_fourier_triangle
#print axioms cue_form_factor_eq_one_sub_triangle
end Bgs.Mathlib
