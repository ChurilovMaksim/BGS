module

public import Mathlib

/-!
# BGS-TRACE-061: exact average over one fresh phase (Poisson integral)

Formalization of the Poisson-integral part of
`mathematics/trace-bridge/fresh_phase_average.md`.
-/

@[expose] public section

open Complex Metric Real

namespace Bgs.Mathlib

/-- Poisson moments: for `‖ζ‖ < 1` and every `k : ℕ`, the uniform average over the unit circle of
`w ^ k / |1 - ζ w|²` equals `conj ζ ^ k / (1 - |ζ|²)`. -/
theorem poisson_moment (ζ : ℂ) (hζ : ‖ζ‖ < 1) (k : ℕ) :
    circleAverage (fun w => w ^ k / ((normSq (1 - ζ * w) : ℝ) : ℂ)) 0 1
      = (starRingEnd ℂ ζ) ^ k / (1 - (normSq ζ : ℂ)) := by
  set G : ℂ → ℂ := fun z => z ^ k / (1 - ζ * z) with hG
  have hne : ∀ z : ℂ, ‖z‖ ≤ 1 → 1 - ζ * z ≠ 0 := by
    intro z hz h
    have h1 : ζ * z = 1 := by linear_combination -h
    have : ‖ζ * z‖ < 1 := by
      rw [norm_mul]
      calc ‖ζ‖ * ‖z‖ ≤ ‖ζ‖ * 1 := by gcongr
        _ < 1 := by simpa using hζ
    rw [h1] at this; simp at this
  have hdiff : DiffContOnCl ℂ G (ball 0 1) := by
    apply DifferentiableOn.diffContOnCl
    rw [closure_ball (0 : ℂ) one_ne_zero]
    intro z hz
    apply DifferentiableAt.differentiableWithinAt
    apply DifferentiableAt.div (by fun_prop) (by fun_prop)
    exact hne z (by simpa using hz)
  have hmem : (starRingEnd ℂ ζ) ∈ ball (0 : ℂ) 1 := by simpa using hζ
  have key := hdiff.two_pi_i_inv_smul_circleIntegral_sub_inv_smul hmem
  rw [circleAverage_eq_circleIntegral one_ne_zero]
  have hcongr : (∮ z in C(0, 1), (z - 0)⁻¹ • (z ^ k / ((normSq (1 - ζ * z) : ℝ) : ℂ)))
      = ∮ z in C(0, 1), (z - starRingEnd ℂ ζ)⁻¹ • G z := by
    apply circleIntegral.integral_congr zero_le_one
    intro z hz
    have hz1 : ‖z‖ = 1 := by simpa using hz
    have hzz : z * starRingEnd ℂ z = 1 := by
      rw [mul_conj, normSq_eq_norm_sq, hz1]; simp
    have h0 : z ≠ 0 := by rintro rfl; simp at hz1
    have h1 : 1 - ζ * z ≠ 0 := hne z hz1.le
    have h2 : z - starRingEnd ℂ ζ ≠ 0 := by
      intro h
      have : z = starRingEnd ℂ ζ := by linear_combination h
      rw [this] at hz1; simp at hz1; linarith
    have hn : ((normSq (1 - ζ * z) : ℝ) : ℂ) * z = (1 - ζ * z) * (z - starRingEnd ℂ ζ) := by
      rw [← mul_conj]
      simp only [map_sub, map_one, map_mul]
      linear_combination (-(1 - ζ * z) * starRingEnd ℂ ζ) * hzz
    have hn0 : ((normSq (1 - ζ * z) : ℝ) : ℂ) ≠ 0 := by
      intro h; rw [h, zero_mul] at hn
      exact mul_ne_zero h1 h2 hn.symm
    simp only [hG, smul_eq_mul, sub_zero]
    have e : z⁻¹ * (z ^ k / ((normSq (1 - ζ * z) : ℝ) : ℂ))
        = z ^ k / (((normSq (1 - ζ * z) : ℝ) : ℂ) * z) := by
      rw [inv_mul_eq_div, div_div]
    rw [e, hn]
    field_simp
  rw [hcongr, key, hG]
  simp only
  rw [← mul_conj]

/-- The rank-one denominator `d(w) = r + s - 2 Re(w γ)` of formula (1). -/
noncomputable def freshDenom (r s : ℝ) (γ w : ℂ) : ℝ := r + s - 2 * (w * γ).re

/-- `Δ = √((r+s)² - 4|γ|²)`. -/
noncomputable def freshDelta (r s : ℝ) (γ : ℂ) : ℝ := √((r + s) ^ 2 - 4 * ‖γ‖ ^ 2)

/-- `ζ = 2γ / (r + s + Δ)`. -/
noncomputable def freshZeta (r s : ℝ) (γ : ℂ) : ℂ :=
  2 * γ / ((r + s + freshDelta r s γ : ℝ) : ℂ)

section FreshParams

variable {r s : ℝ} {γ : ℂ}

lemma fresh_disc_pos (hδ : ‖γ‖ ^ 2 < r * s) :
    0 < (r + s) ^ 2 - 4 * ‖γ‖ ^ 2 := by
  nlinarith [sq_nonneg (r - s)]

lemma freshDelta_pos (hδ : ‖γ‖ ^ 2 < r * s) :
    0 < freshDelta r s γ :=
  Real.sqrt_pos.mpr (fresh_disc_pos hδ)

lemma freshDelta_sq (hδ : ‖γ‖ ^ 2 < r * s) :
    freshDelta r s γ ^ 2 = (r + s) ^ 2 - 4 * ‖γ‖ ^ 2 :=
  Real.sq_sqrt (fresh_disc_pos hδ).le

lemma fresh_sum_pos (hr : 0 ≤ r) (hs : 0 ≤ s) (hδ : ‖γ‖ ^ 2 < r * s) :
    0 < r + s + freshDelta r s γ := by
  have := freshDelta_pos hδ
  linarith

/-- `|ζ| < 1` (the pole of the Poisson kernel lies outside the closed disc). -/
theorem freshZeta_norm_lt_one (hr : 0 ≤ r) (hs : 0 ≤ s) (hδ : ‖γ‖ ^ 2 < r * s) :
    ‖freshZeta r s γ‖ < 1 := by
  have hS := fresh_sum_pos hr hs hδ
  have hD := freshDelta_pos hδ
  unfold freshZeta
  rw [norm_div, norm_mul, Complex.norm_real, Real.norm_of_nonneg hS.le, div_lt_one hS]
  have h2 : 2 * ‖γ‖ < r + s := by
    have : (2 * ‖γ‖) ^ 2 < (r + s) ^ 2 := by nlinarith [sq_nonneg (r - s)]
    exact lt_of_pow_lt_pow_left₀ 2 (by linarith) this
  simp only [Complex.norm_ofNat]
  linarith

/-- The factorization `d(w) = (r+s+Δ)/2 · |1 - ζ w|²` on the unit circle. -/
theorem freshDenom_factor (hr : 0 ≤ r) (hs : 0 ≤ s) (hδ : ‖γ‖ ^ 2 < r * s)
    {w : ℂ} (hw : ‖w‖ = 1) :
    freshDenom r s γ w = (r + s + freshDelta r s γ) / 2 * normSq (1 - freshZeta r s γ * w) := by
  have hS := fresh_sum_pos hr hs hδ
  have hD2 := freshDelta_sq hδ
  have hz : freshZeta r s γ = (2 / (r + s + freshDelta r s γ) : ℝ) * γ := by
    unfold freshZeta; push_cast; ring
  set D := freshDelta r s γ
  set S := r + s + D with hSdef
  have hw2 : w.re ^ 2 + w.im ^ 2 = 1 := by
    have := Complex.normSq_eq_norm_sq w
    rw [hw, Complex.normSq_apply] at this; nlinarith
  have hg : ‖γ‖ ^ 2 = γ.re ^ 2 + γ.im ^ 2 := by
    rw [← Complex.normSq_eq_norm_sq, Complex.normSq_apply]; ring
  rw [hz, Complex.normSq_apply]
  unfold freshDenom
  simp only [Complex.sub_re, Complex.one_re, Complex.mul_re, Complex.ofReal_re,
    Complex.ofReal_im, Complex.sub_im, Complex.one_im, Complex.mul_im, zero_mul, sub_zero,
    zero_sub, add_zero]
  have hSne : S ≠ 0 := hS.ne'
  have key : S ^ 2 + 4 * ‖γ‖ ^ 2 = 2 * (r + s) * S := by
    rw [hSdef]; nlinarith [hD2]
  field_simp
  rw [hg] at key
  linear_combination (-4) * (γ.re ^ 2 + γ.im ^ 2) * hw2 - key

lemma normSq_freshZeta :
    normSq (freshZeta r s γ) = 4 * ‖γ‖ ^ 2 / (r + s + freshDelta r s γ) ^ 2 := by
  unfold freshZeta
  rw [map_div₀, map_mul, Complex.normSq_ofReal, Complex.normSq_eq_norm_sq,
    Complex.normSq_eq_norm_sq]
  norm_num
  ring

/-- Formula (2) of TRACE-061: for every `k : ℕ`, the uniform average over the fresh phase
`w ∈ S¹` of `w ^ k / d(w)` equals `conj ζ ^ k / Δ`.  In particular (`k = 0`) `E_w 1/d(w) = 1/Δ`.
The hypothesis `|γ|² < r s` is the non-collinearity condition `δ = r s - |γ|² > 0`. -/
theorem fresh_phase_moment (hr : 0 ≤ r) (hs : 0 ≤ s) (hδ : ‖γ‖ ^ 2 < r * s) (k : ℕ) :
    circleAverage (fun w => w ^ k / (freshDenom r s γ w : ℂ)) 0 1
      = (starRingEnd ℂ (freshZeta r s γ)) ^ k / (freshDelta r s γ : ℂ) := by
  have hS := fresh_sum_pos hr hs hδ
  have hD := freshDelta_pos hδ
  have hD2 := freshDelta_sq hδ
  have hzeta := freshZeta_norm_lt_one hr hs hδ
  have hcongr : circleAverage (fun w => w ^ k / (freshDenom r s γ w : ℂ)) 0 1
      = circleAverage ((2 / (r + s + freshDelta r s γ) : ℂ) •
          (fun w => w ^ k / ((normSq (1 - freshZeta r s γ * w) : ℝ) : ℂ))) 0 1 := by
    apply circleAverage_congr_sphere
    intro w hw
    have hw1 : ‖w‖ = 1 := by simpa using hw
    simp only [Pi.smul_apply, smul_eq_mul]
    rw [freshDenom_factor hr hs hδ hw1]
    have hS' : ((r + s + freshDelta r s γ : ℝ) : ℂ) ≠ 0 := by exact_mod_cast hS.ne'
    push_cast
    push_cast at hS'
    field_simp
  rw [hcongr, circleAverage_smul, poisson_moment _ hzeta, smul_eq_mul,
    normSq_freshZeta]
  set D := freshDelta r s γ
  set S := r + s + D with hSdef
  have key : S ^ 2 - 4 * ‖γ‖ ^ 2 = 2 * D * S := by
    rw [hSdef]; nlinarith [hD2]
  have h1 : (1 : ℂ) - ((4 * ‖γ‖ ^ 2 / S ^ 2 : ℝ) : ℂ) = ((2 * D / S : ℝ) : ℂ) := by
    rw [← Complex.ofReal_one, ← Complex.ofReal_sub]
    congr 1
    field_simp
    linarith
  rw [h1]
  have hSc : (S : ℂ) ≠ 0 := by exact_mod_cast hS.ne'
  have hDc : (D : ℂ) ≠ 0 := by exact_mod_cast hD.ne'
  have e2 : ((2 : ℂ) / (↑r + ↑s + ↑D)) = 2 / (S : ℂ) := by rw [hSdef]; push_cast; ring
  rw [e2]
  push_cast
  field_simp

lemma freshDenom_pos (hr : 0 ≤ r) (hs : 0 ≤ s) (hδ : ‖γ‖ ^ 2 < r * s)
    {w : ℂ} (hw : ‖w‖ = 1) : 0 < freshDenom r s γ w := by
  rw [freshDenom_factor hr hs hδ hw]
  have hS := fresh_sum_pos hr hs hδ
  have hz := freshZeta_norm_lt_one hr hs hδ
  have hne : 1 - freshZeta r s γ * w ≠ 0 := by
    intro h
    have h1 : freshZeta r s γ * w = 1 := by linear_combination -h
    have := congrArg norm h1
    rw [norm_mul, hw, mul_one, norm_one] at this
    linarith
  have := Complex.normSq_pos.mpr hne
  positivity

lemma continuous_freshDenom : Continuous (fun w => (freshDenom r s γ w : ℂ)) := by
  unfold freshDenom; fun_prop

lemma fresh_circleIntegrable_div (hr : 0 ≤ r) (hs : 0 ≤ s) (hδ : ‖γ‖ ^ 2 < r * s)
    {g : ℂ → ℂ} (hg : Continuous g) :
    CircleIntegrable (fun w => g w / (freshDenom r s γ w : ℂ)) 0 1 := by
  apply ContinuousOn.circleIntegrable zero_le_one
  apply ContinuousOn.div hg.continuousOn continuous_freshDenom.continuousOn
  intro w hw
  have hw1 : ‖w‖ = 1 := by simpa using hw
  exact_mod_cast (freshDenom_pos hr hs hδ hw1).ne'

/-- The conjugate moment: `E_w conj(w) / d(w) = ζ / Δ`. -/
theorem fresh_phase_conj_moment (hr : 0 ≤ r) (hs : 0 ≤ s) (hδ : ‖γ‖ ^ 2 < r * s) :
    circleAverage (fun w => starRingEnd ℂ w / (freshDenom r s γ w : ℂ)) 0 1
      = freshZeta r s γ / (freshDelta r s γ : ℂ) := by
  have hI := fresh_circleIntegrable_div hr hs hδ (g := fun w => w ^ 1) (by fun_prop)
  have h := (Complex.conjCLE.toContinuousLinearMap.restrictScalars ℝ).circleAverage_comp_comm hI
  have e : ((Complex.conjCLE.toContinuousLinearMap.restrictScalars ℝ) ∘
      (fun w => w ^ 1 / (freshDenom r s γ w : ℂ)))
      = fun w => starRingEnd ℂ w / (freshDenom r s γ w : ℂ) := by
    funext w; simp
  rw [e, fresh_phase_moment hr hs hδ 1] at h
  rw [h]; simp

/-- Formula (3) of TRACE-061, entrywise: with the output phase removed, the fresh-phase average
of `R₀ - (a - w̄ b)(a - w̄ b)* / d(w)` is `R₀ - (a a* + b b* - ζ̄ a b* - ζ b a*) / Δ`. -/
theorem fresh_phase_conjugated_average (hr : 0 ≤ r) (hs : 0 ≤ s) (hδ : ‖γ‖ ^ 2 < r * s)
    (R₀ a₁ b₁ a₂ b₂ : ℂ) :
    circleAverage (fun w => R₀ - (a₁ - starRingEnd ℂ w * b₁)
        * starRingEnd ℂ (a₂ - starRingEnd ℂ w * b₂) / (freshDenom r s γ w : ℂ)) 0 1
      = R₀ - (a₁ * starRingEnd ℂ a₂ + b₁ * starRingEnd ℂ b₂
          - starRingEnd ℂ (freshZeta r s γ) * a₁ * starRingEnd ℂ b₂
          - freshZeta r s γ * b₁ * starRingEnd ℂ a₂) / (freshDelta r s γ : ℂ) := by
  set c₀ := a₁ * starRingEnd ℂ a₂ + b₁ * starRingEnd ℂ b₂
  set c₁ := a₁ * starRingEnd ℂ b₂
  set c₂ := b₁ * starRingEnd ℂ a₂
  set f₀ : ℂ → ℂ := fun w => w ^ 0 / (freshDenom r s γ w : ℂ) with hf₀
  set f₁ : ℂ → ℂ := fun w => w ^ 1 / (freshDenom r s γ w : ℂ) with hf₁
  set f₂ : ℂ → ℂ := fun w => starRingEnd ℂ w / (freshDenom r s γ w : ℂ) with hf₂
  have hcongr : circleAverage (fun w => R₀ - (a₁ - starRingEnd ℂ w * b₁)
        * starRingEnd ℂ (a₂ - starRingEnd ℂ w * b₂) / (freshDenom r s γ w : ℂ)) 0 1
      = circleAverage ((fun _ => R₀) - (c₀ • f₀ - c₁ • f₁ - c₂ • f₂)) 0 1 := by
    apply circleAverage_congr_sphere
    intro w hw
    have hw1 : ‖w‖ = 1 := by simpa using hw
    have hww : starRingEnd ℂ w * w = 1 := by
      rw [conj_mul', hw1]; simp
    simp only [Pi.sub_apply, Pi.smul_apply, hf₀, hf₁, hf₂, smul_eq_mul, map_sub, map_mul,
      Complex.conj_conj, c₀, c₁, c₂]
    have hd : (freshDenom r s γ w : ℂ) ≠ 0 := by
      exact_mod_cast (freshDenom_pos hr hs hδ hw1).ne'
    field_simp
    linear_combination (-(b₁ * starRingEnd ℂ b₂)) * hww
  have I0 : CircleIntegrable f₀ 0 1 :=
    fresh_circleIntegrable_div hr hs hδ (g := fun w => w ^ 0) (by fun_prop)
  have I1 : CircleIntegrable f₁ 0 1 :=
    fresh_circleIntegrable_div hr hs hδ (g := fun w => w ^ 1) (by fun_prop)
  have I2 : CircleIntegrable f₂ 0 1 :=
    fresh_circleIntegrable_div hr hs hδ (g := fun w => starRingEnd ℂ w) Complex.continuous_conj
  have J0 : CircleIntegrable (c₀ • f₀) 0 1 := I0.const_smul
  have J1 : CircleIntegrable (c₁ • f₁) 0 1 := I1.const_smul
  have J2 : CircleIntegrable (c₂ • f₂) 0 1 := I2.const_smul
  rw [hcongr, circleAverage_sub (circleIntegrable_const _ _ _) ((J0.sub J1).sub J2),
    circleAverage_const, circleAverage_sub (J0.sub J1) J2, circleAverage_sub J0 J1,
    circleAverage_smul, circleAverage_smul, circleAverage_smul,
    hf₀, hf₁, hf₂, fresh_phase_moment hr hs hδ 0, fresh_phase_moment hr hs hδ 1,
    fresh_phase_conj_moment hr hs hδ]
  simp only [smul_eq_mul, pow_zero, pow_one]
  ring

/-- Formula (6) of TRACE-061: the removed output row has leverage `R'(w) = δ / d(w)` with
`δ = r s - |γ|²`, and its fresh-phase average is `δ / Δ`. -/
theorem fresh_phase_leverage_average (hr : 0 ≤ r) (hs : 0 ≤ s) (hδ : ‖γ‖ ^ 2 < r * s) :
    circleAverage (fun w => ((r * s - ‖γ‖ ^ 2 : ℝ) : ℂ) / (freshDenom r s γ w : ℂ)) 0 1
      = ((r * s - ‖γ‖ ^ 2 : ℝ) : ℂ) / (freshDelta r s γ : ℂ) := by
  have h := fresh_phase_moment hr hs hδ 0
  simp only [pow_zero] at h
  have e : (fun w => ((r * s - ‖γ‖ ^ 2 : ℝ) : ℂ) / (freshDenom r s γ w : ℂ))
      = ((r * s - ‖γ‖ ^ 2 : ℝ) : ℂ) • (fun w => 1 / (freshDenom r s γ w : ℂ)) := by
    funext w; simp [div_eq_mul_inv]
  rw [e, circleAverage_smul, h, smul_eq_mul]
  ring

/-- Formula (7) of TRACE-061 (leverage part), case `X = I`: then `r = s = 1` and the averaged
leverage of the removed output row is `½√(1 - |γ|²)`. -/
theorem fresh_phase_leverage_identity (hγ : ‖γ‖ < 1) :
    ((1 * 1 - ‖γ‖ ^ 2 : ℝ) : ℂ) / (freshDelta 1 1 γ : ℂ)
      = ((√(1 - ‖γ‖ ^ 2) / 2 : ℝ) : ℂ) := by
  have h1 : 0 < 1 - ‖γ‖ ^ 2 := by nlinarith [norm_nonneg γ]
  have hD : freshDelta 1 1 γ = 2 * √(1 - ‖γ‖ ^ 2) := by
    unfold freshDelta
    rw [show ((1 : ℝ) + 1) ^ 2 - 4 * ‖γ‖ ^ 2 = 2 ^ 2 * (1 - ‖γ‖ ^ 2) by ring,
      Real.sqrt_mul (by norm_num), Real.sqrt_sq (by norm_num)]
  rw [hD, ← Complex.ofReal_div]
  congr 1
  have hs : 0 < √(1 - ‖γ‖ ^ 2) := Real.sqrt_pos.mpr h1
  have hsq := Real.sq_sqrt h1.le
  field_simp
  nlinarith [hsq]

end FreshParams
end Bgs.Mathlib
