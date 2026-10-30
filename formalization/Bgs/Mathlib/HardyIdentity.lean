module
public import Bgs.Mathlib.HardyClock
@[expose] public section

/-!
# The exact Hardy remainder identity for radial secular ratios (BGS-TRACE-091, Thm (5))

Source: `mathematics/trace-bridge/hardy_spectral_remainder.md`, §§1–2.

For a unitary spectrum `λ : Fin N → ℂ` (`‖λ_j‖ = 1`), let
`p(z) = det(I - zU) = ∏_j (1 - z λ_j) = ∑_{k ≤ N} c_k z^k` (`secular`, `secPoly`).
For `0 < b < 1` and real `a`, the normalized radial ratio is the circle average
`Z(a,b) = ⨍_{|z|=1} |p(az)|² / |p(bz)|²` (`radialRatio`).

**Theorem (`radialRatio_hardy_identity`).**
`Z(a,b) = 1 + (a^N - b^N)² / (1 - b^{2N}) + ⨍_{|z|=1} |E(z)|²`, where
`E(z) = (∑_k c_k d_k(a,b) z^k) / p(bz)` with the weights `d_k = hardyWeight N a b k`.

Consequences:
* `radialRatio_ge_clock` — the sharp clock minimum `Z(a,b) ≥ 1 + (a^N-b^N)²/(1-b^{2N})`;
* `radialRatio_eq_clock_iff` — for `0 < b < a < 1`, equality holds iff every interior
  secular coefficient `c_1, …, c_{N-1}` vanishes, i.e. `p(z) = 1 + c_N z^N`.

The proof is the note's rational orthogonality argument, realised with the mean value
property of holomorphic functions on the closed unit disc (`DiffContOnCl.circleAverage`):
`p(az)/p(bz) = A + D·W(z) + E(z)`, `W(z) = ∏(b - zλ_j)/p(bz)` unimodular on the circle,
`⨍ W = b^N`, `⨍ E = 0` and `⨍ W·conj E = 0`.
-/

open Complex Polynomial Real Finset Metric

namespace Bgs.Mathlib

variable {N : ℕ}

/-- The secular polynomial `p(z) = ∏_j (1 - z λ_j)` as a function. -/
noncomputable def secular (lam : Fin N → ℂ) (z : ℂ) : ℂ := ∏ j, (1 - z * lam j)

/-- The secular polynomial as a `Polynomial ℂ` (its coefficients are the `c_k`). -/
noncomputable def secPoly (lam : Fin N → ℂ) : Polynomial ℂ := ∏ j, (1 - C (lam j) * X)

/-- The normalized radial ratio `Z(a,b) = ⨍_{|z|=1} |p(az)|²/|p(bz)|²`. -/
noncomputable def radialRatio (lam : Fin N → ℂ) (a b : ℝ) : ℝ :=
  circleAverage (fun z => ‖secular lam (a * z)‖ ^ 2 / ‖secular lam (b * z)‖ ^ 2) 0 1

/-- Numerator of the Hardy remainder, `∑_k c_k d_k z^k`. -/
noncomputable def hardyNum (lam : Fin N → ℂ) (a b : ℝ) (z : ℂ) : ℂ :=
  ∑ k ∈ range (N + 1), (secPoly lam).coeff k * (hardyWeight N a b k : ℂ) * z ^ k

/-- The Hardy remainder `E(z) = (∑_k c_k d_k z^k) / p(bz)`. -/
noncomputable def hardyRem (lam : Fin N → ℂ) (a b : ℝ) (z : ℂ) : ℂ :=
  hardyNum lam a b z / secular lam (b * z)

/-! ## The secular polynomial -/

lemma secPoly_eval (lam : Fin N → ℂ) (z : ℂ) : (secPoly lam).eval z = secular lam z := by
  rw [secPoly, secular, eval_prod]
  refine Finset.prod_congr rfl fun j _ => ?_
  rw [eval_sub, eval_one, eval_mul, eval_C, eval_X, mul_comm]

lemma secPoly_natDegree_le (lam : Fin N → ℂ) : (secPoly lam).natDegree ≤ N := by
  unfold secPoly
  refine (natDegree_prod_le _ _).trans ?_
  have : ∀ j ∈ (univ : Finset (Fin N)), (1 - C (lam j) * X).natDegree ≤ 1 := by
    intro j _
    refine (natDegree_sub_le _ _).trans ?_
    simp only [natDegree_one, zero_le, max_le_iff, true_and]
    exact natDegree_C_mul_le _ _ |>.trans (by simp)
  refine (Finset.sum_le_sum this).trans ?_
  simp

lemma secular_eq_sum (lam : Fin N → ℂ) (z : ℂ) :
    secular lam z = ∑ k ∈ range (N + 1), (secPoly lam).coeff k * z ^ k := by
  rw [← secPoly_eval, eval_eq_sum_range' (Nat.lt_succ_of_le (secPoly_natDegree_le lam))]

/-- The reflected polynomial `∏_j (b - z λ_j) = ∑_k c_k b^{N-k} z^k`. -/
lemma reflected_eq_sum (lam : Fin N → ℂ) {b : ℂ} (hb : b ≠ 0) (z : ℂ) :
    ∏ j, (b - z * lam j) = ∑ k ∈ range (N + 1), (secPoly lam).coeff k * b ^ (N - k) * z ^ k := by
  have h1 : ∏ j, (b - z * lam j) = b ^ N * secular lam (z / b) := by
    have : b ^ N = ∏ _j : Fin N, b := by simp
    rw [secular, this, ← Finset.prod_mul_distrib]
    refine Finset.prod_congr rfl fun j _ => ?_
    field_simp
  rw [h1, secular_eq_sum, Finset.mul_sum]
  refine Finset.sum_congr rfl fun k hk => ?_
  have hk' : k ≤ N := Nat.lt_succ_iff.1 (Finset.mem_range.1 hk)
  rw [div_pow]
  have : b ^ N = b ^ (N - k) * b ^ k := by rw [← pow_add, Nat.sub_add_cancel hk']
  rw [this]
  field_simp

lemma secular_zero (lam : Fin N → ℂ) : secular lam 0 = 1 := by
  simp [secular]

lemma secular_ne_zero (lam : Fin N → ℂ) (hlam : ∀ j, ‖lam j‖ = 1) {b : ℝ} (hb0 : 0 ≤ b)
    (hb1 : b < 1) {z : ℂ} (hz : ‖z‖ ≤ 1) : secular lam (b * z) ≠ 0 := by
  rw [secular, Finset.prod_ne_zero_iff]
  intro j _ h
  have h1 : (b : ℂ) * z * lam j = 1 := by linear_combination -h
  have := congrArg norm h1
  rw [norm_mul, norm_mul, hlam j, Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg hb0] at this
  simp at this
  nlinarith [norm_nonneg z]

lemma differentiable_secular (lam : Fin N → ℂ) : Differentiable ℂ (secular lam) := by
  unfold secular
  fun_prop

/-! ## Mean value property for rational functions with denominator `p(bz)` -/

lemma circleAverage_div_secular (lam : Fin N → ℂ) (hlam : ∀ j, ‖lam j‖ = 1) {b : ℝ}
    (hb0 : 0 ≤ b) (hb1 : b < 1) {Φ : ℂ → ℂ} (hΦ : Differentiable ℂ Φ) :
    circleAverage (fun z => Φ z / secular lam (b * z)) 0 1 = Φ 0 := by
  have hd : DiffContOnCl ℂ (fun z => Φ z / secular lam (b * z)) (ball 0 |1|) := by
    apply DifferentiableOn.diffContOnCl
    rw [abs_one, closure_ball _ one_ne_zero]
    intro z hz
    apply DifferentiableAt.differentiableWithinAt
    apply hΦ.differentiableAt.div
    · exact ((differentiable_secular lam).comp (differentiable_id.const_mul _)).differentiableAt
    · exact secular_ne_zero lam hlam hb0 hb1 (by simpa using hz)
  rw [hd.circleAverage]
  simp [secular]

/-! ## Identities on the unit circle -/

/-- `|∏(b - zλ_j)| = |p(bz)|` on the unit circle. -/
lemma norm_reflected_eq (lam : Fin N → ℂ) (hlam : ∀ j, ‖lam j‖ = 1) (b : ℝ) {z : ℂ}
    (hz : ‖z‖ = 1) : ‖∏ j, ((b : ℂ) - z * lam j)‖ = ‖secular lam (b * z)‖ := by
  rw [secular, norm_prod, norm_prod]
  refine Finset.prod_congr rfl fun j _ => ?_
  have hu : ‖z * lam j‖ = 1 := by rw [norm_mul, hz, hlam j, one_mul]
  have hc : (starRingEnd ℂ) (z * lam j) * (z * lam j) = 1 := by
    rw [Complex.conj_mul', hu]; simp
  have : (b : ℂ) - z * lam j = -(z * lam j) * (starRingEnd ℂ) (1 - b * z * lam j) := by
    simp only [map_sub, map_one, map_mul, Complex.conj_ofReal]
    have : (starRingEnd ℂ) z * (starRingEnd ℂ) (lam j) * (z * lam j) = 1 := by
      rw [← map_mul]; exact hc
    linear_combination (-(b : ℂ)) * this
  rw [this, norm_mul, norm_neg, hu, one_mul, Complex.norm_conj, mul_assoc]

/-- `conj(p(bz)) · z^N · ∏ λ_j = (-1)^N ∏(b - zλ_j)` on the unit circle. -/
lemma conj_secular_mul (lam : Fin N → ℂ) (hlam : ∀ j, ‖lam j‖ = 1) (b : ℝ) {z : ℂ}
    (hz : ‖z‖ = 1) :
    (starRingEnd ℂ) (secular lam (b * z)) * z ^ N * ∏ j, lam j =
      (-1) ^ N * ∏ j, ((b : ℂ) - z * lam j) := by
  have hzN : z ^ N = ∏ _j : Fin N, z := by simp
  have hmN : (-1 : ℂ) ^ N = ∏ _j : Fin N, (-1 : ℂ) := by simp
  rw [secular, map_prod, hzN, hmN, ← Finset.prod_mul_distrib, ← Finset.prod_mul_distrib,
    ← Finset.prod_mul_distrib]
  refine Finset.prod_congr rfl fun j _ => ?_
  have hu : ‖z * lam j‖ = 1 := by rw [norm_mul, hz, hlam j, one_mul]
  have hc : (starRingEnd ℂ) (z * lam j) * (z * lam j) = 1 := by
    rw [Complex.conj_mul', hu]; simp
  simp only [map_sub, map_one, map_mul, Complex.conj_ofReal] at hc ⊢
  linear_combination (-(b : ℂ)) * hc

/-- The reflected numerator `S(z) = ∑_k conj(c_k d_k) z^{N-k}`. -/
noncomputable def hardyNumRefl (lam : Fin N → ℂ) (a b : ℝ) (z : ℂ) : ℂ :=
  ∑ k ∈ range (N + 1), (starRingEnd ℂ) ((secPoly lam).coeff k * (hardyWeight N a b k : ℂ)) *
    z ^ (N - k)

lemma conj_hardyNum (lam : Fin N → ℂ) (a b : ℝ) {z : ℂ} (hz : ‖z‖ = 1) :
    z ^ N * (starRingEnd ℂ) (hardyNum lam a b z) = hardyNumRefl lam a b z := by
  have hzc : z * (starRingEnd ℂ) z = 1 := by
    rw [Complex.mul_conj', hz]; simp
  rw [hardyNum, hardyNumRefl, map_sum, Finset.mul_sum]
  refine Finset.sum_congr rfl fun k hk => ?_
  have hk' : k ≤ N := Nat.lt_succ_iff.1 (Finset.mem_range.1 hk)
  rw [map_mul (starRingEnd ℂ) _ (z ^ k), map_pow]
  have : z ^ N = z ^ (N - k) * z ^ k := by rw [← pow_add, Nat.sub_add_cancel hk']
  rw [this]
  have h2 : z ^ k * (starRingEnd ℂ) z ^ k = 1 := by rw [← mul_pow, hzc, one_pow]
  linear_combination ((starRingEnd ℂ) ((secPoly lam).coeff k * (hardyWeight N a b k : ℂ)) *
    z ^ (N - k)) * h2

lemma hardyNumRefl_zero (lam : Fin N → ℂ) {a b : ℝ} (hb0 : 0 < b) (hb1 : b < 1) (hN : 1 ≤ N) :
    hardyNumRefl lam a b 0 = 0 := by
  rw [hardyNumRefl, Finset.sum_eq_single N]
  · rw [hardyWeight_N hb0 hb1 hN]; simp
  · intro k hk hkN
    have hk' : k < N := lt_of_le_of_ne (Nat.lt_succ_iff.1 (Finset.mem_range.1 hk)) hkN
    rw [zero_pow (by omega), mul_zero]
  · intro h; exact absurd (Finset.mem_range.2 (Nat.lt_succ_self N)) h

lemma hardyNum_zero (lam : Fin N → ℂ) {a b : ℝ} (hb0 : 0 < b) (hb1 : b < 1) (hN : 1 ≤ N) :
    hardyNum lam a b 0 = 0 := by
  rw [hardyNum, Finset.sum_eq_single 0]
  · rw [hardyWeight_zero hb0 hb1 hN]; simp
  · intro k _ hk0
    rw [zero_pow hk0, mul_zero]
  · intro h; exact absurd (Finset.mem_range.2 (Nat.succ_pos N)) h

/-- The decomposition `p(az) = A p(bz) + D ∏(b - zλ_j) + ∑ c_k d_k z^k`. -/
lemma secular_decomp (lam : Fin N → ℂ) (a : ℝ) {b : ℝ} (hb : b ≠ 0) (z : ℂ) :
    secular lam (a * z) = (hardyA N a b : ℂ) * secular lam (b * z) +
      (hardyD N a b : ℂ) * ∏ j, ((b : ℂ) - z * lam j) + hardyNum lam a b z := by
  rw [secular_eq_sum, secular_eq_sum, reflected_eq_sum lam (by exact_mod_cast hb), hardyNum,
    Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun k _ => ?_
  simp only [hardyWeight]
  push_cast
  ring

/-- Pointwise expansion of `‖A + D W + E‖²` for real `A, D`. -/
lemma norm_sq_expand (A D : ℝ) (W E : ℂ) :
    ‖(A : ℂ) + D * W + E‖ ^ 2 = A ^ 2 + D ^ 2 * ‖W‖ ^ 2 + ‖E‖ ^ 2 + 2 * A * D * W.re +
      2 * A * E.re + 2 * D * (W * (starRingEnd ℂ) E).re := by
  simp only [Complex.sq_norm, Complex.normSq_apply, Complex.add_re, Complex.add_im,
    Complex.mul_re, Complex.mul_im, Complex.ofReal_re, Complex.ofReal_im, Complex.conj_re,
    Complex.conj_im]
  ring

lemma clock_constant_identity {N : ℕ} {a b : ℝ} (hb0 : 0 < b) (hb1 : b < 1) (hN : 1 ≤ N) :
    hardyA N a b ^ 2 + hardyD N a b ^ 2 + 2 * hardyA N a b * hardyD N a b * b ^ N =
      1 + (a ^ N - b ^ N) ^ 2 / (1 - b ^ (2 * N)) := by
  have h := one_sub_b_pow_ne hb0 hb1 hN
  have e : b ^ (2 * N) = (b ^ N) ^ 2 := by rw [← pow_mul, mul_comm]
  rw [e] at h ⊢
  simp only [hardyA, hardyD]
  rw [e]
  field_simp
  ring

/-! ## Main theorem -/

/-- **Exact Hardy remainder identity (TRACE-091, (5)).** -/
theorem radialRatio_hardy_identity (lam : Fin N → ℂ) (hlam : ∀ j, ‖lam j‖ = 1) (hN : 1 ≤ N)
    (a : ℝ) {b : ℝ} (hb0 : 0 < b) (hb1 : b < 1) :
    radialRatio lam a b = 1 + (a ^ N - b ^ N) ^ 2 / (1 - b ^ (2 * N)) +
      circleAverage (fun z => ‖hardyRem lam a b z‖ ^ 2) 0 1 := by
  set A := hardyA N a b
  set D := hardyD N a b
  set q : ℂ → ℂ := fun z => secular lam (b * z) with hq
  set u : ℂ → ℂ := fun z => ∏ j, ((b : ℂ) - z * lam j) with hu
  set κ : ℂ := (-1) ^ N * ∏ j, lam j with hκ
  set Φ : ℂ → ℂ := fun z => (2 * A * D : ℝ) * u z + (2 * A : ℝ) * hardyNum lam a b z +
    (2 * D : ℝ) * (κ * hardyNumRefl lam a b z) with hΦ
  have hqne : ∀ z : ℂ, ‖z‖ ≤ 1 → q z ≠ 0 := fun z hz =>
    secular_ne_zero lam hlam hb0.le hb1 hz
  have hsph : ∀ z ∈ sphere (0 : ℂ) |1|, ‖z‖ = 1 := by
    intro z hz; simpa using hz
  -- pointwise identity on the circle
  have hpt : Set.EqOn (fun z => ‖secular lam (a * z)‖ ^ 2 / ‖secular lam (b * z)‖ ^ 2)
      (fun z => (A ^ 2 + D ^ 2) + (‖hardyRem lam a b z‖ ^ 2 + (Φ z / q z).re))
      (sphere (0 : ℂ) |1|) := by
    intro z hz
    have hz1 := hsph z hz
    have hq0 := hqne z hz1.le
    have hqc : (starRingEnd ℂ) (q z) ≠ 0 := by
      exact (_root_.map_ne_zero (starRingEnd ℂ)).2 hq0
    set W := u z / q z with hW
    set E := hardyRem lam a b z with hE
    have hWn : ‖W‖ = 1 := by
      rw [hW, norm_div, hu, hq]; simp only
      rw [norm_reflected_eq lam hlam b hz1, div_self]
      exact norm_ne_zero_iff.2 hq0
    have hdec : secular lam (a * z) / q z = (A : ℂ) + D * W + E := by
      rw [hW, hE, hardyRem, secular_decomp lam a hb0.ne' z]
      simp only [hq, hu] at hq0 ⊢
      rw [add_div, add_div, mul_div_assoc, div_self hq0, mul_one, mul_div_assoc]
    have hWE : W * (starRingEnd ℂ) E = κ * hardyNumRefl lam a b z / q z := by
      have hc := conj_secular_mul lam hlam b hz1
      have hr := conj_hardyNum lam a b hz1
      rw [hW, hE, hardyRem, map_div₀, ← hr, hκ]
      simp only [hu, hq] at hc hqc hq0 ⊢
      have hpm : ((-1 : ℂ) ^ N) ^ 2 = 1 := by rw [← pow_mul, mul_comm, pow_mul]; simp
      rw [div_mul_div_comm, div_eq_div_iff (mul_ne_zero hq0 hqc) hq0]
      linear_combination (-(secular lam (b * z)) * (-1 : ℂ) ^ N *
        (starRingEnd ℂ) (hardyNum lam a b z)) * hc +
        (-(secular lam (b * z)) * (∏ j, ((b : ℂ) - z * lam j)) *
          (starRingEnd ℂ) (hardyNum lam a b z)) * hpm
    have hre : (Φ z / q z).re = 2 * A * D * W.re + 2 * A * E.re +
        2 * D * (W * (starRingEnd ℂ) E).re := by
      rw [hWE, hW, hE, hardyRem]
      simp only [hΦ, add_div, mul_div_assoc, Complex.add_re, Complex.re_ofReal_mul]
      rfl
    simp only
    rw [← div_pow, ← norm_div, show secular lam (b * z) = q z from rfl, hdec, norm_sq_expand,
      hWn, hre]
    ring
  rw [radialRatio, circleAverage_congr_sphere hpt]
  -- integrability
  have hcontE : ContinuousOn (fun z => ‖hardyRem lam a b z‖ ^ 2) (sphere (0 : ℂ) |1|) := by
    apply ContinuousOn.pow
    apply ContinuousOn.norm
    intro z hz
    apply ContinuousAt.continuousWithinAt
    apply ContinuousAt.div
    · exact (show Differentiable ℂ (hardyNum lam a b) by unfold hardyNum; fun_prop).continuous.continuousAt
    · exact ((differentiable_secular lam).comp (differentiable_id.const_mul _)).continuous.continuousAt
    · exact hqne z (hsph z hz).le
  have hΦd : Differentiable ℂ Φ := by
    simp only [hΦ, hu, hardyNum, hardyNumRefl]; fun_prop
  have hcontΦ : ContinuousOn (fun z => Φ z / q z) (sphere (0 : ℂ) |1|) := by
    intro z hz
    apply ContinuousAt.continuousWithinAt
    apply ContinuousAt.div hΦd.continuous.continuousAt
    · exact ((differentiable_secular lam).comp (differentiable_id.const_mul _)).continuous.continuousAt
    · exact hqne z (hsph z hz).le
  have hI1 : CircleIntegrable (fun z => ‖hardyRem lam a b z‖ ^ 2) 0 1 :=
    hcontE.circleIntegrable'
  have hI2c : CircleIntegrable (fun z => Φ z / q z) 0 1 := hcontΦ.circleIntegrable'
  have hI2 : CircleIntegrable (fun z => (Φ z / q z).re) 0 1 :=
    (Complex.continuous_re.comp_continuousOn hcontΦ).circleIntegrable'
  have hI12 : CircleIntegrable (fun z => ‖hardyRem lam a b z‖ ^ 2 + (Φ z / q z).re) 0 1 :=
    hI1.add hI2
  rw [circleAverage_fun_add (circleIntegrable_const _ _ _) hI12,
    circleAverage_const, circleAverage_fun_add hI1 hI2]
  have hre : circleAverage (fun z => (Φ z / q z).re) 0 1 = (circleAverage (fun z => Φ z / q z) 0 1).re :=
    Complex.reCLM.circleAverage_comp_comm hI2c
  rw [hre, circleAverage_div_secular lam hlam hb0.le hb1 hΦd]
  have hΦ0 : Φ 0 = ((2 * A * D * b ^ N : ℝ) : ℂ) := by
    simp only [hΦ, hu, hardyNum_zero lam hb0 hb1 hN, hardyNumRefl_zero lam hb0 hb1 hN]
    simp
  rw [hΦ0, Complex.ofReal_re, ← clock_constant_identity hb0 hb1 hN]
  ring

/-- **Sharp clock minimum.** -/
theorem radialRatio_ge_clock (lam : Fin N → ℂ) (hlam : ∀ j, ‖lam j‖ = 1) (hN : 1 ≤ N)
    (a : ℝ) {b : ℝ} (hb0 : 0 < b) (hb1 : b < 1) :
    1 + (a ^ N - b ^ N) ^ 2 / (1 - b ^ (2 * N)) ≤ radialRatio lam a b := by
  rw [radialRatio_hardy_identity lam hlam hN a hb0 hb1]
  have : 0 ≤ circleAverage (fun z => ‖hardyRem lam a b z‖ ^ 2) 0 1 :=
    circleAverage_nonneg_of_nonneg fun z _ => by positivity
  linarith

/-- A continuous nonnegative function on the unit circle with zero circle average vanishes
at every point `e^{iθ}`, `θ ∈ (0, 2π]`. -/
lemma circleAverage_eq_zero_vanish {f : ℂ → ℝ} (hc : ContinuousOn f (sphere (0 : ℂ) 1))
    (hnn : ∀ z ∈ sphere (0 : ℂ) 1, 0 ≤ f z) (h0 : circleAverage f 0 1 = 0) :
    ∀ θ ∈ Set.Ioc 0 (2 * π), f (circleMap 0 1 θ) = 0 := by
  have hmem : ∀ θ, circleMap (0 : ℂ) 1 θ ∈ sphere (0 : ℂ) 1 := fun θ =>
    circleMap_mem_sphere 0 zero_le_one θ
  have hgc : Continuous (fun θ => f (circleMap 0 1 θ)) :=
    hc.comp_continuous (continuous_circleMap 0 1) hmem
  rw [circleAverage_def, smul_eq_mul] at h0
  have hI : ∫ θ in (0 : ℝ)..2 * π, f (circleMap 0 1 θ) = 0 := by
    rcases mul_eq_zero.1 h0 with h | h
    · exfalso; have : (0 : ℝ) < (2 * π)⁻¹ := by positivity
      linarith
    · exact h
  rw [intervalIntegral.integral_eq_zero_iff_of_nonneg_ae
    (Filter.Eventually.of_forall fun θ => hnn _ (hmem θ)) (hgc.intervalIntegrable _ _)] at hI
  have he : Set.Ioc (2 * π) 0 = ∅ := Set.Ioc_eq_empty (by linarith [Real.pi_pos])
  rw [he, Set.union_empty] at hI
  exact fun θ hθ => MeasureTheory.Measure.eqOn_Ioc_of_ae_eq _ hI hgc.continuousOn
    continuousOn_const hθ

/-- The numerator `∑ c_k d_k X^k` as a polynomial. -/
noncomputable def hardyPoly (lam : Fin N → ℂ) (a b : ℝ) : Polynomial ℂ :=
  ∑ k ∈ range (N + 1), C ((secPoly lam).coeff k * (hardyWeight N a b k : ℂ)) * X ^ k

lemma hardyPoly_eval (lam : Fin N → ℂ) (a b : ℝ) (z : ℂ) :
    (hardyPoly lam a b).eval z = hardyNum lam a b z := by
  simp [hardyPoly, hardyNum, eval_finsetSum]

lemma hardyPoly_coeff (lam : Fin N → ℂ) (a b : ℝ) {k : ℕ} (hk : k ≤ N) :
    (hardyPoly lam a b).coeff k = (secPoly lam).coeff k * (hardyWeight N a b k : ℂ) := by
  rw [hardyPoly, finsetSum_coeff, Finset.sum_eq_single k]
  · rw [coeff_C_mul_X_pow, if_pos rfl]
  · intro j _ hjk
    rw [coeff_C_mul_X_pow, if_neg (Ne.symm hjk)]
  · intro h; exact absurd (Finset.mem_range.2 (Nat.lt_succ_of_le hk)) h

/-- **Equality classification.**  For `0 < b < a < 1`, the clock value is attained iff all
interior secular coefficients vanish (`p(z) = 1 + c_N z^N`). -/
theorem radialRatio_eq_clock_iff (lam : Fin N → ℂ) (hlam : ∀ j, ‖lam j‖ = 1) (hN : 1 ≤ N)
    {a b : ℝ} (hb0 : 0 < b) (hba : b < a) (ha1 : a < 1) :
    radialRatio lam a b = 1 + (a ^ N - b ^ N) ^ 2 / (1 - b ^ (2 * N)) ↔
      ∀ k, 1 ≤ k → k < N → (secPoly lam).coeff k = 0 := by
  have hb1 : b < 1 := hba.trans ha1
  rw [radialRatio_hardy_identity lam hlam hN a hb0 hb1]
  constructor
  · intro h
    have h0 : circleAverage (fun z => ‖hardyRem lam a b z‖ ^ 2) 0 1 = 0 := by linarith
    have hqne : ∀ z : ℂ, ‖z‖ ≤ 1 → secular lam (b * z) ≠ 0 := fun z hz =>
      secular_ne_zero lam hlam hb0.le hb1 hz
    have hcont : ContinuousOn (fun z => ‖hardyRem lam a b z‖ ^ 2) (sphere (0 : ℂ) 1) := by
      apply ContinuousOn.pow
      apply ContinuousOn.norm
      intro z hz
      apply ContinuousAt.continuousWithinAt
      apply ContinuousAt.div
      · exact (show Differentiable ℂ (hardyNum lam a b) by unfold hardyNum; fun_prop).continuous.continuousAt
      · exact ((differentiable_secular lam).comp (differentiable_id.const_mul _)).continuous.continuousAt
      · exact hqne z (by simpa using le_of_eq (mem_sphere_zero_iff_norm.1 hz))
    have hvan := circleAverage_eq_zero_vanish hcont (fun z _ => by positivity) h0
    have hroot : ∀ θ ∈ Set.Ioc 0 (2 * π), (hardyPoly lam a b).IsRoot (circleMap 0 1 θ) := by
      intro θ hθ
      have h1 := hvan θ hθ
      simp only [hardyRem, sq_eq_zero_iff, norm_eq_zero, div_eq_zero_iff] at h1
      rw [IsRoot, hardyPoly_eval]
      rcases h1 with h1 | h1
      · exact h1
      · exfalso; exact hqne _ (by simp) h1
    have hpoly : hardyPoly lam a b = 0 := by
      apply eq_zero_of_infinite_isRoot
      have hinj : (Set.Ioc (0 : ℝ) (2 * π)).InjOn (circleMap 0 1) := by
        have := injOn_circleMap_of_abs_sub_le (a := 0) (b := 2 * π) (c := 0) one_ne_zero
          (by rw [zero_sub, abs_neg, abs_of_pos (by positivity)])
        rwa [Set.uIoc_of_le (by positivity)] at this
      refine Set.Infinite.mono ?_ ((Set.Ioc_infinite (by positivity)).image hinj)
      rintro _ ⟨θ, hθ, rfl⟩
      exact hroot θ hθ
    intro k hk1 hkN
    have hc := hardyPoly_coeff lam a b (k := k) hkN.le
    rw [hpoly, coeff_zero] at hc
    have hw : (hardyWeight N a b k : ℂ) ≠ 0 := by
      exact_mod_cast (hardyWeight_pos hb0 hba ha1 hk1 hkN).ne'
    exact (mul_eq_zero.1 hc.symm).resolve_right hw
  · intro hc
    have hnum : ∀ z, hardyNum lam a b z = 0 := by
      intro z
      rw [hardyNum]
      refine Finset.sum_eq_zero fun k hk => ?_
      have hk' := Nat.lt_succ_iff.1 (Finset.mem_range.1 hk)
      rcases Nat.eq_zero_or_pos k with rfl | hk0
      · rw [hardyWeight_zero hb0 hb1 hN]; simp
      rcases eq_or_lt_of_le hk' with rfl | hkN
      · rw [hardyWeight_N hb0 hb1 hN]; simp
      rw [hc k hk0 hkN]; simp
    have : (fun z => ‖hardyRem lam a b z‖ ^ 2) = fun _ => (0 : ℝ) := by
      funext z; simp [hardyRem, hnum]
    rw [this, circleAverage_const]
    ring

#print axioms secPoly_eval
#print axioms secPoly_natDegree_le
#print axioms secular_eq_sum
#print axioms reflected_eq_sum
#print axioms secular_zero
#print axioms secular_ne_zero
#print axioms differentiable_secular
#print axioms circleAverage_div_secular
#print axioms norm_reflected_eq
#print axioms conj_secular_mul
#print axioms conj_hardyNum
#print axioms hardyNumRefl_zero
#print axioms hardyNum_zero
#print axioms secular_decomp
#print axioms norm_sq_expand
#print axioms clock_constant_identity
#print axioms radialRatio_hardy_identity
#print axioms radialRatio_ge_clock
#print axioms circleAverage_eq_zero_vanish
#print axioms hardyPoly_eval
#print axioms hardyPoly_coeff
#print axioms radialRatio_eq_clock_iff
end Bgs.Mathlib
