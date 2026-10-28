module
public import Mathlib
@[expose] public section

/-!
# Exact radial translation and an auxiliary centered-disk tail bound
(`mathematics/trace-bridge/bosonic_body_radial_translation.md`)

* `radial_norm_lt_one`, `one_sub_normSq_radial`, `radial_inverse`: for
  `z = ψ/√(1+|ψ|²)` one has `|z| < 1`, `1 − |z|² = 1/(1+|ψ|²)` and `ψ = z/√(1−|z|²)`;
  hence `log(1+|ψ|²) = −log(1−|z|²)` (`log_one_add_normSq_radial`).
* `disk_weight_integral`: `∫_{|z|<1} (1−|z|²)^a d²z = π/(1+a)` for `a ≥ 0`.
* `centered_disk_tail_bound`: with `z_N = −∑_{j<N} z_j`,
  `Ω_N = {|z_j| < 1, |∑ z_j| < 1}` and `H = ∑_{j ≤ N} −log(1 − |z_j|²)`, every function `S`
  with `e^{−S} ≤ e^{−cH}` on `Ω_N` (`c ≥ 0`) satisfies
  `∫_{Ω_N ∩ {H ≥ L}} e^{−S} ∏_{j<N} d²z_j ≤ e^{−cL/2} [π/(1+c/2)]^{N−1}`.
  (Here the `N − 1` free coordinates are indexed by `Fin n`, `n = N − 1`.)
* `absorbed_tail_bound`: with real scalar absorption, `e^{−S_α} ≤ e^{s/2}e^{−cH}` gives the
  bound `e^{s/2 − cL/2} [π/(1+c/2)]^{N−1}`.
-/

open Real MeasureTheory Set

namespace Bgs.Mathlib

namespace RadialTail

/-! ## The radial map `ψ ↦ ψ/√(1+|ψ|²)` -/

/-- The radial change of variables `z = ψ/√(1+|ψ|²)`. -/
noncomputable def radial (ψ : ℂ) : ℂ := ψ / (Real.sqrt (1 + ‖ψ‖ ^ 2) : ℂ)

lemma sqrt_one_add_pos (ψ : ℂ) : 0 < Real.sqrt (1 + ‖ψ‖ ^ 2) :=
  Real.sqrt_pos.2 (by positivity)

lemma norm_radial_sq (ψ : ℂ) : ‖radial ψ‖ ^ 2 = ‖ψ‖ ^ 2 / (1 + ‖ψ‖ ^ 2) := by
  rw [radial, norm_div, Complex.norm_real, Real.norm_eq_abs,
    abs_of_pos (sqrt_one_add_pos ψ), div_pow, Real.sq_sqrt (by positivity)]

theorem one_sub_normSq_radial (ψ : ℂ) : 1 - ‖radial ψ‖ ^ 2 = 1 / (1 + ‖ψ‖ ^ 2) := by
  rw [norm_radial_sq]
  field_simp
  ring

theorem radial_norm_lt_one (ψ : ℂ) : ‖radial ψ‖ < 1 := by
  have h := one_sub_normSq_radial ψ
  have hpos : 0 < 1 / (1 + ‖ψ‖ ^ 2) := by positivity
  have : ‖radial ψ‖ ^ 2 < 1 := by linarith
  nlinarith [norm_nonneg (radial ψ)]

theorem radial_inverse (ψ : ℂ) :
    ψ = radial ψ / (Real.sqrt (1 - ‖radial ψ‖ ^ 2) : ℂ) := by
  rw [one_sub_normSq_radial, Real.sqrt_div' _ (by positivity : (0:ℝ) ≤ 1 + ‖ψ‖ ^ 2),
    Real.sqrt_one, radial]
  have := sqrt_one_add_pos ψ
  have hne : (Real.sqrt (1 + ‖ψ‖ ^ 2) : ℂ) ≠ 0 := by exact_mod_cast this.ne'
  push_cast
  field_simp

theorem log_one_add_normSq_radial (ψ : ℂ) :
    Real.log (1 + ‖ψ‖ ^ 2) = -Real.log (1 - ‖radial ψ‖ ^ 2) := by
  rw [one_sub_normSq_radial, one_div, Real.log_inv, neg_neg]

/-! ## The disk integral -/

/-- The weight `(1 − |z|²)^a` on the unit disk, extended by zero. -/
noncomputable def diskWeight (a : ℝ) (z : ℂ) : ℝ :=
  if ‖z‖ < 1 then (1 - ‖z‖ ^ 2) ^ a else 0

lemma diskWeight_nonneg (a : ℝ) (z : ℂ) : 0 ≤ diskWeight a z := by
  unfold diskWeight; split_ifs with h
  · exact Real.rpow_nonneg (by nlinarith [norm_nonneg z]) _
  · exact le_rfl

lemma diskWeight_le_one {a : ℝ} (ha : 0 ≤ a) (z : ℂ) : diskWeight a z ≤ 1 := by
  unfold diskWeight; split_ifs with h
  · exact Real.rpow_le_one (by nlinarith [norm_nonneg z]) (by nlinarith [norm_nonneg z]) ha
  · norm_num

/-- `∫₀¹ r (1−r²)^a dr = 1/(2(a+1))`. -/
lemma radial_integral {a : ℝ} (ha : 0 ≤ a) :
    ∫ r in (0 : ℝ)..1, r * (1 - r ^ 2) ^ a = 1 / (2 * (a + 1)) := by
  have hderiv : ∀ r ∈ Ioo (0 : ℝ) 1,
      HasDerivAt (fun r : ℝ => -(1 - r ^ 2) ^ (a + 1) / (2 * (a + 1))) (r * (1 - r ^ 2) ^ a) r := by
    intro r hr
    have hb : 0 < 1 - r ^ 2 := by nlinarith [hr.1, hr.2]
    have h1 : HasDerivAt (fun r : ℝ => 1 - r ^ 2) (-(2 * r)) r := by
      simpa using (hasDerivAt_pow 2 r).const_sub 1
    have h2 := h1.rpow_const (p := a + 1) (Or.inl hb.ne')
    have h3 := (h2.neg).div_const (2 * (a + 1))
    convert! h3 using 1
    rw [show a + 1 - 1 = a by ring]
    field_simp
  have hcont : ContinuousOn (fun r : ℝ => -(1 - r ^ 2) ^ (a + 1) / (2 * (a + 1))) (Icc 0 1) := by
    apply ContinuousOn.div_const
    apply ContinuousOn.neg
    apply ContinuousOn.rpow_const (by fun_prop)
    intro x _; right; linarith
  have hint : IntervalIntegrable (fun r : ℝ => r * (1 - r ^ 2) ^ a) volume 0 1 := by
    apply ContinuousOn.intervalIntegrable
    apply ContinuousOn.mul continuousOn_id
    apply ContinuousOn.rpow_const (by fun_prop)
    intro x _; right; exact ha
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt_of_le zero_le_one hcont hderiv hint]
  simp only [one_pow, sub_self, ne_eq, OfNat.ofNat_ne_zero, not_false_eq_true, zero_pow]
  rw [Real.zero_rpow (by linarith), sub_zero, Real.one_rpow]
  have : a + 1 ≠ 0 := by linarith
  field_simp
  ring

/-- **Disk integral** `∫_{|z|<1} (1 − |z|²)^a d²z = π/(1+a)`. -/
theorem disk_weight_integral {a : ℝ} (ha : 0 ≤ a) :
    ∫ z : ℂ, diskWeight a z = π / (1 + a) := by
  rw [← Complex.integral_comp_polarCoord_symm, polarCoord_target]
  have hfun : ∀ p ∈ Ioi (0 : ℝ) ×ˢ Ioo (-π) π,
      p.1 • diskWeight a (Complex.polarCoord.symm p) =
        (p.1 * (if p.1 < 1 then (1 - p.1 ^ 2) ^ a else 0)) * (1 : ℝ) := by
    intro p hp
    have hp1 : 0 < p.1 := hp.1
    simp only [diskWeight, Complex.norm_polarCoord_symm, abs_of_pos hp1, smul_eq_mul, mul_one]
  rw [setIntegral_congr_fun (measurableSet_Ioi.prod measurableSet_Ioo) hfun,
    Measure.volume_eq_prod,
    setIntegral_prod_mul (fun x : ℝ => x * (if x < 1 then (1 - x ^ 2) ^ a else 0))
      (fun _ : ℝ => (1 : ℝ))]
  simp only [integral_const, MeasurableSet.univ, measureReal_restrict_apply, univ_inter,
    Real.volume_real_Ioo, smul_eq_mul, mul_one]
  have hI : ∫ x in Ioi (0 : ℝ), x * (if x < 1 then (1 - x ^ 2) ^ a else 0) =
      ∫ r in (0 : ℝ)..1, r * (1 - r ^ 2) ^ a := by
    rw [intervalIntegral.integral_of_le zero_le_one, integral_Ioc_eq_integral_Ioo]
    rw [← integral_indicator measurableSet_Ioi, ← integral_indicator measurableSet_Ioo]
    congr 1
    funext x
    simp only [indicator, mem_Ioi, mem_Ioo]
    by_cases h0 : 0 < x
    · by_cases h1 : x < 1
      · simp [h0, h1]
      · simp [h0, h1]
    · simp [h0]
  rw [hI, radial_integral ha]
  have : π - -π = 2 * π := by ring
  rw [this, max_eq_left (by positivity)]
  have : a + 1 ≠ 0 := by linarith
  have : 1 + a ≠ 0 := by linarith
  field_simp
  ring

lemma diskWeight_integrable {a : ℝ} (ha : 0 ≤ a) : Integrable (diskWeight a) := by
  by_contra h
  have := integral_undef h
  rw [disk_weight_integral ha] at this
  have : 0 < π / (1 + a) := by positivity
  linarith

/-! ## The auxiliary tail bound -/

/-- The dependent last coordinate `z_N = −∑_{j<N} z_j`. -/
noncomputable def lastCoord {n : ℕ} (z : Fin n → ℂ) : ℂ := -∑ j, z j

/-- The auxiliary centered domain `Ω_N`. -/
def Omega (n : ℕ) : Set (Fin n → ℂ) := {z | (∀ j, ‖z j‖ < 1) ∧ ‖lastCoord z‖ < 1}

/-- The height `H = ∑_{j ≤ N} −log(1 − |z_j|²) = ∑ log(1+|ψ_j|²)`. -/
noncomputable def height {n : ℕ} (z : Fin n → ℂ) : ℝ :=
  ∑ j, -Real.log (1 - ‖z j‖ ^ 2) + -Real.log (1 - ‖lastCoord z‖ ^ 2)

lemma exp_neg_mul_neg_log {x c : ℝ} (hx : 0 < x) : Real.exp (-(c * -Real.log x)) = x ^ c := by
  rw [Real.rpow_def_of_pos hx]; congr 1; ring

/-- **Auxiliary tail bound.** -/
theorem centered_disk_tail_bound {n : ℕ} {c : ℝ} (hc : 0 ≤ c) (L : ℝ)
    (S : (Fin n → ℂ) → ℝ)
    (hS : ∀ z ∈ Omega n, Real.exp (-S z) ≤ Real.exp (-(c * height z))) :
    ∫ z in Omega n ∩ {z | L ≤ height z}, Real.exp (-S z) ≤
      Real.exp (-(c * L / 2)) * (π / (1 + c / 2)) ^ n := by
  have hc2 : 0 ≤ c / 2 := by linarith
  set g : (Fin n → ℂ) → ℝ := fun z => Real.exp (-(c * L / 2)) * ∏ j, diskWeight (c / 2) (z j)
  have hgint : Integrable g := by
    apply Integrable.const_mul
    exact Integrable.fintype_prod (f := fun _ => diskWeight (c / 2))
      (fun _ => diskWeight_integrable hc2)
  have hgval : ∫ z, g z = Real.exp (-(c * L / 2)) * (π / (1 + c / 2)) ^ n := by
    simp only [g]
    rw [integral_const_mul]
    congr 1
    rw [show (fun z : Fin n → ℂ => ∏ j, diskWeight (c / 2) (z j)) =
      fun z => ∏ j, (fun _ : Fin n => diskWeight (c / 2)) j (z j) from rfl]
    rw [integral_fintype_prod_volume_eq_prod]
    simp [disk_weight_integral hc2, div_pow]
  have hHm : Measurable (fun z : Fin n → ℂ => height z) := by
    unfold height lastCoord; fun_prop
  have hΩ : MeasurableSet (Omega n) := by
    have : Omega n = (⋂ j, {z : Fin n → ℂ | ‖z j‖ < 1}) ∩ {z | ‖lastCoord z‖ < 1} := by
      ext z; simp [Omega]
    rw [this]
    refine MeasurableSet.inter (MeasurableSet.iInter fun j => ?_) ?_
    · exact measurableSet_lt (by fun_prop) measurable_const
    · exact measurableSet_lt (by unfold lastCoord; fun_prop) measurable_const
  have hs : MeasurableSet (Omega n ∩ {z | L ≤ height z}) :=
    hΩ.inter (measurableSet_le measurable_const hHm)
  rw [← hgval]
  have hgnn : ∀ z, 0 ≤ g z := fun z =>
    mul_nonneg (Real.exp_pos _).le (Finset.prod_nonneg fun j _ => diskWeight_nonneg _ _)
  calc ∫ z in Omega n ∩ {z | L ≤ height z}, Real.exp (-S z)
      ≤ ∫ z in Omega n ∩ {z | L ≤ height z}, g z := by
        refine integral_mono_of_nonneg (Filter.Eventually.of_forall fun z => (Real.exp_pos _).le)
          hgint.integrableOn ?_
        refine ae_restrict_of_forall_mem hs fun z hz => ?_
        obtain ⟨⟨hz1, hzN⟩, hL⟩ := hz
        refine (hS z ⟨hz1, hzN⟩).trans ?_
        have hpos : ∀ j, 0 < 1 - ‖z j‖ ^ 2 := fun j => by nlinarith [norm_nonneg (z j), hz1 j]
        have hposN : 0 < 1 - ‖lastCoord z‖ ^ 2 := by nlinarith [norm_nonneg (lastCoord z)]
        -- `e^{-cH} ≤ e^{-cL/2} e^{-cH/2}`
        have h1 : Real.exp (-(c * height z)) ≤
            Real.exp (-(c * L / 2)) * Real.exp (-(c / 2 * height z)) := by
          have hL' : L ≤ height z := hL
          rw [← Real.exp_add]; apply Real.exp_le_exp.2
          nlinarith [mul_le_mul_of_nonneg_left hL' hc]
        refine h1.trans (mul_le_mul_of_nonneg_left ?_ (Real.exp_pos _).le)
        -- `e^{-cH/2} = ∏_{j ≤ N} (1-|z_j|²)^{c/2} ≤ ∏_{j<N} w(z_j)`
        have h2 : Real.exp (-(c / 2 * height z)) =
            (∏ j, (1 - ‖z j‖ ^ 2) ^ (c / 2)) * (1 - ‖lastCoord z‖ ^ 2) ^ (c / 2) := by
          rw [height, mul_add, neg_add, Real.exp_add, Finset.mul_sum, ← Finset.sum_neg_distrib,
            Real.exp_sum, exp_neg_mul_neg_log hposN]
          congr 1
          exact Finset.prod_congr rfl fun j _ => exp_neg_mul_neg_log (hpos j)
        rw [h2]
        have h3 : ∏ j, diskWeight (c / 2) (z j) = ∏ j, (1 - ‖z j‖ ^ 2) ^ (c / 2) :=
          Finset.prod_congr rfl fun j _ => by simp [diskWeight, hz1 j]
        rw [h3]
        refine mul_le_of_le_one_right
          (Finset.prod_nonneg fun j _ => Real.rpow_nonneg (hpos j).le _) ?_
        exact Real.rpow_le_one hposN.le (by nlinarith [norm_nonneg (lastCoord z)]) hc2
    _ ≤ ∫ z, g z := setIntegral_le_integral hgint (Filter.Eventually.of_forall hgnn)

/-- The same tail bound with real scalar absorption (real-absorption note, §3): if
`e^{−S_α} ≤ e^{s/2} e^{−cH}` on `Ω_N`, then the tail integral is at most
`e^{s/2 − cL/2} [π/(1+c/2)]^{N−1}`. -/
theorem absorbed_tail_bound {n : ℕ} {c : ℝ} (hc : 0 ≤ c) (L s : ℝ)
    (S : (Fin n → ℂ) → ℝ)
    (hS : ∀ z ∈ Omega n, Real.exp (-S z) ≤ Real.exp (s / 2) * Real.exp (-(c * height z))) :
    ∫ z in Omega n ∩ {z | L ≤ height z}, Real.exp (-S z) ≤
      Real.exp (s / 2 - c * L / 2) * (π / (1 + c / 2)) ^ n := by
  have h := centered_disk_tail_bound hc L (fun z => S z + s / 2) (fun z hz => by
    have := hS z hz
    rw [neg_add, Real.exp_add, Real.exp_neg (s / 2)]
    rw [← div_eq_mul_inv, div_le_iff₀' (Real.exp_pos _)]
    exact this)
  have e : ∀ z, Real.exp (-S z) = Real.exp (s / 2) * Real.exp (-(S z + s / 2)) := fun z => by
    rw [← Real.exp_add]; ring_nf
  simp_rw [e]
  rw [integral_const_mul, show s / 2 - c * L / 2 = s / 2 + -(c * L / 2) by ring, Real.exp_add,
    mul_assoc]
  exact mul_le_mul_of_nonneg_left h (Real.exp_pos _).le

end RadialTail

end Bgs.Mathlib
