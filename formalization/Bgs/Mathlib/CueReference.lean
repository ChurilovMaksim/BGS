module
public import Mathlib
@[expose] public section

/-!
# The CUE two-point reference `L_N(s) → (1 - e^{-2s}) / (4 s²)`

The repository README states the necessary two-point target

  `L_N(s) = N⁻² ∑_{m ≥ 1} e^{-2sm/N} |Tr U_N^m|² → (1 - e^{-2s}) / (4s²)`,

and identifies it as the CUE value via `E_CUE |Tr V^m|² = min(m, N)`
(Diaconis–Shahshahani / Rains).  The random-matrix input `min(m,N)` itself is a
classical theorem about Haar measure and is *not* re-proved here; we take the CUE
form factor `min(m,N)` as the definition of the reference sequence and prove:

* the exact closed form of the CUE series (`cue_series_hasSum`, `cueL_closed_form`);
* the limit `L_N^{CUE}(s) → (1 - e^{-2s})/(4s²)` for every `s > 0` (`cueL_tendsto`);
* the Laplace-transform identity `∫₀^∞ e^{-2sx} min(x,1) dx = (1 - e^{-2s})/(4s²)`
  (`laplace_min_one`), which identifies the limit as the continuum ramp–plateau;
* the ramp–plateau defect: `min(x,1) - x = 1 - x < 0` for `x > 1`
  (`plateau_defect_neg`).
-/

open Real Filter Topology BigOperators

namespace Bgs.Mathlib

/-- The CUE positive-power form factor `E_CUE |Tr V^m|² = min(m,N)`. -/
def cueFormFactor (N m : ℕ) : ℝ := (min m N : ℕ)

/-- The CUE reference value of the smoothed two-point statistic
`L_N(s) = N⁻² ∑_{m ≥ 1} e^{-2sm/N} E|Tr V^m|²`. -/
noncomputable def cueL (N : ℕ) (s : ℝ) : ℝ :=
  (1 / (N : ℝ) ^ 2) * ∑' m : ℕ, Real.exp (-2 * s * ((m + 1 : ℕ) : ℝ) / N) * cueFormFactor N (m + 1)

/-- Counting identity: `min(m+1, N) = #{k < N : k ≤ m}`. -/
theorem min_succ_eq_sum (N m : ℕ) :
    ((min (m + 1) N : ℕ) : ℝ) = ∑ k ∈ Finset.range N, if k ≤ m then (1 : ℝ) else 0 := by
  rw [Finset.sum_boole]
  congr 1
  have : (Finset.range N).filter (fun k => k ≤ m) = Finset.range (min (m + 1) N) := by
    ext k; simp; omega
  rw [this, Finset.card_range]

/-- Shifted geometric series. -/
theorem hasSum_shifted_geometric {q : ℝ} (h0 : 0 ≤ q) (h1 : q < 1) (k : ℕ) :
    HasSum (fun m : ℕ => if k ≤ m then q ^ (m + 1) else 0) (q ^ (k + 1) / (1 - q)) := by
  have hinj : Function.Injective (fun m : ℕ => m + k) := fun a b h => by simpa using h
  rw [← hinj.hasSum_iff]
  · have hg := (hasSum_geometric_of_lt_one h0 h1).mul_left (q ^ (k + 1))
    convert! hg using 1
    · ext m; simp only [Function.comp, le_add_iff_nonneg_left, zero_le, ite_true]; ring
  · intro x hx
    have : ¬ k ≤ x := by
      intro h; exact hx ⟨x - k, by simp; omega⟩
    simp [this]

/-- Exact closed form of the CUE series:
`∑_{m≥1} q^m min(m,N) = q (1 - q^N) / (1-q)²` for `0 ≤ q < 1`. -/
theorem cue_series_hasSum (N : ℕ) {q : ℝ} (h0 : 0 ≤ q) (h1 : q < 1) :
    HasSum (fun m : ℕ => q ^ (m + 1) * cueFormFactor N (m + 1)) (q * (1 - q ^ N) / (1 - q) ^ 2) := by
  have hfun : (fun m : ℕ => q ^ (m + 1) * cueFormFactor N (m + 1)) =
      fun m => ∑ k ∈ Finset.range N, if k ≤ m then q ^ (m + 1) else 0 := by
    ext m
    rw [cueFormFactor, min_succ_eq_sum, Finset.mul_sum]
    apply Finset.sum_congr rfl; intro k _
    split_ifs <;> simp
  rw [hfun]
  have hval : ∑ k ∈ Finset.range N, q ^ (k + 1) / (1 - q) = q * (1 - q ^ N) / (1 - q) ^ 2 := by
    have hq1 : q ≠ 1 := ne_of_lt h1
    have hq1' : 1 - q ≠ 0 := sub_ne_zero.2 (Ne.symm hq1)
    rw [← Finset.sum_div]
    simp_rw [pow_succ]
    rw [← Finset.sum_mul, geom_sum_eq hq1]
    field_simp
    ring
  rw [← hval]
  exact hasSum_sum fun k _ => hasSum_shifted_geometric h0 h1 k

/-- Closed form of `L_N^{CUE}(s)`, with `q = e^{-2s/N}`. -/
theorem cueL_closed_form {N : ℕ} (hN : 1 ≤ N) {s : ℝ} (hs : 0 < s) :
    cueL N s = (1 / (N : ℝ) ^ 2) *
      (Real.exp (-2 * s / N) * (1 - Real.exp (-2 * s)) / (1 - Real.exp (-2 * s / N)) ^ 2) := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  set q := Real.exp (-2 * s / N) with hq
  have h0 : 0 ≤ q := (Real.exp_pos _).le
  have h1 : q < 1 := by
    rw [hq, ← Real.exp_zero]; exact Real.exp_lt_exp.2 (div_neg_of_neg_of_pos (by linarith) hNpos)
  have hqN : q ^ N = Real.exp (-2 * s) := by
    rw [hq, ← Real.exp_nat_mul]; congr 1; field_simp
  rw [cueL, ← hqN]
  congr 1
  rw [← (cue_series_hasSum N h0 h1).tsum_eq]
  congr 1; ext m
  congr 1
  rw [hq, ← Real.exp_nat_mul]; congr 1; ring

/-- `N (1 - e^{-2s/N}) → 2s`. -/
theorem tendsto_N_one_sub_exp {s : ℝ} (hs : 0 < s) :
    Tendsto (fun N : ℕ => (N : ℝ) * (1 - Real.exp (-2 * s / N))) atTop (𝓝 (2 * s)) := by
  have hslope : Tendsto (slope Real.exp 0) (𝓝[≠] 0) (𝓝 1) := by
    have := (Real.hasDerivAt_exp 0)
    rw [hasDerivAt_iff_tendsto_slope] at this
    simpa using this
  have hh : Tendsto (fun N : ℕ => (-2 * s) / (N : ℝ)) atTop (𝓝[≠] 0) := by
    apply tendsto_nhdsWithin_iff.2
    refine ⟨tendsto_const_div_atTop_nhds_zero_nat _, ?_⟩
    filter_upwards [eventually_ge_atTop 1] with N hN
    have : (0 : ℝ) < N := by exact_mod_cast hN
    simp only [Set.mem_compl_iff, Set.mem_singleton_iff]
    exact div_ne_zero (by linarith) this.ne'
  have hcomp := (hslope.comp hh).const_mul (2 * s)
  rw [mul_one] at hcomp
  apply hcomp.congr'
  filter_upwards [eventually_ge_atTop 1] with N hN
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  simp only [Function.comp, slope, Real.exp_zero, vsub_eq_sub, smul_eq_mul, sub_zero]
  field_simp
  ring

/-- **The CUE two-point reference.**  For every `s > 0`,
`L_N^{CUE}(s) → (1 - e^{-2s}) / (4 s²)`. -/
theorem cueL_tendsto {s : ℝ} (hs : 0 < s) :
    Tendsto (fun N : ℕ => cueL N s) atTop (𝓝 ((1 - Real.exp (-2 * s)) / (4 * s ^ 2))) := by
  have hq : Tendsto (fun N : ℕ => Real.exp (-2 * s / N)) atTop (𝓝 1) := by
    have := (Real.continuous_exp.tendsto 0).comp (tendsto_const_div_atTop_nhds_zero_nat (-2 * s))
    rw [Real.exp_zero] at this; exact this
  have hden := (tendsto_N_one_sub_exp hs).pow 2
  have hlim := (hq.mul_const (1 - Real.exp (-2 * s))).div hden (by positivity)
  have htarget : 1 * (1 - Real.exp (-2 * s)) / (2 * s) ^ 2 = (1 - Real.exp (-2 * s)) / (4 * s ^ 2) := by
    ring
  rw [htarget] at hlim
  apply hlim.congr'
  filter_upwards [eventually_ge_atTop 1] with N hN
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  have hq1 : 1 - Real.exp (-2 * s / N) ≠ 0 := by
    apply sub_ne_zero.2; apply Ne.symm; rw [Ne, Real.exp_eq_one_iff]
    exact div_ne_zero (by linarith) hNpos.ne'
  rw [cueL_closed_form hN hs, Pi.div_apply]
  field_simp

/-- The Laplace transform of the continuum ramp–plateau `min(x,1)`:
`∫₀^∞ e^{-2sx} min(x,1) dx = (1 - e^{-2s}) / (4s²)` for `s > 0`. -/
theorem laplace_min_one {s : ℝ} (hs : 0 < s) :
    ∫ x in Set.Ioi (0 : ℝ), Real.exp (-2 * s * x) * min x 1 =
      (1 - Real.exp (-2 * s)) / (4 * s ^ 2) := by
  have hneg : -2 * s < 0 := by linarith
  have hcont : Continuous fun x : ℝ => Real.exp (-2 * s * x) * min x 1 := by fun_prop
  have h1 : ∫ x in Set.Ioc (0 : ℝ) 1, Real.exp (-2 * s * x) * min x 1 =
      1 / (2 * s) ^ 2 - (1 / (2 * s) + 1 / (2 * s) ^ 2) * Real.exp (-2 * s) := by
    rw [← intervalIntegral.integral_of_le zero_le_one]
    have hcongr : ∫ x in (0 : ℝ)..1, Real.exp (-2 * s * x) * min x 1 =
        ∫ x in (0 : ℝ)..1, x * Real.exp (-2 * s * x) := by
      apply intervalIntegral.integral_congr
      intro x hx
      rw [Set.uIcc_of_le zero_le_one] at hx
      simp only [min_eq_left hx.2]; ring
    rw [hcongr]
    have hderiv : ∀ x ∈ Set.uIcc (0 : ℝ) 1,
        HasDerivAt (fun x : ℝ => -(x / (2 * s) + 1 / (2 * s) ^ 2) * Real.exp (-2 * s * x))
          (x * Real.exp (-2 * s * x)) x := by
      intro x _
      have e1 : HasDerivAt (fun y : ℝ => -(y / (2 * s) + 1 / (2 * s) ^ 2)) (-(1 / (2 * s))) x :=
        (((hasDerivAt_id' x).div_const (2 * s)).add_const (1 / (2 * s) ^ 2)).neg
      have e2 : HasDerivAt (fun y : ℝ => Real.exp (-2 * s * y))
          (Real.exp (-2 * s * x) * (-2 * s * 1)) x :=
        ((hasDerivAt_id' x).const_mul (-2 * s)).exp
      convert! e1.mul e2 using 1
      field_simp
      ring
    rw [intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv
      (by apply Continuous.intervalIntegrable; fun_prop)]
    simp only [mul_zero, Real.exp_zero, mul_one, zero_div, zero_add]
    ring
  have h2 : ∫ x in Set.Ioi (1 : ℝ), Real.exp (-2 * s * x) * min x 1 = Real.exp (-2 * s) / (2 * s) := by
    rw [MeasureTheory.setIntegral_congr_fun measurableSet_Ioi
      (g := fun x => Real.exp (-2 * s * x)) (fun x hx => by
        simp only [min_eq_right (le_of_lt (Set.mem_Ioi.1 hx)), mul_one])]
    rw [integral_exp_mul_Ioi hneg, mul_one]
    field_simp
  have hint1 : MeasureTheory.IntegrableOn (fun x : ℝ => Real.exp (-2 * s * x) * min x 1)
      (Set.Ioc 0 1) :=
    (hcont.integrableOn_Icc).mono_set Set.Ioc_subset_Icc_self
  have hint2 : MeasureTheory.IntegrableOn (fun x : ℝ => Real.exp (-2 * s * x) * min x 1)
      (Set.Ioi 1) := by
    refine (integrableOn_exp_mul_Ioi hneg 1).congr_fun (fun x hx => ?_) measurableSet_Ioi
    simp only [min_eq_right (le_of_lt (Set.mem_Ioi.1 hx)), mul_one]
  rw [← Set.Ioc_union_Ioi_eq_Ioi zero_le_one,
    MeasureTheory.setIntegral_union (Set.Ioc_disjoint_Ioi le_rfl) measurableSet_Ioi hint1 hint2,
    h1, h2]
  field_simp
  ring

/-- The ramp–plateau defect: above the Heisenberg time `x = 1`, the CUE value
`min(x,1)` lies strictly below the cyclic ramp `x`, by `1 - x < 0`. -/
theorem plateau_defect_neg {x : ℝ} (hx : 1 < x) : min x 1 - x = 1 - x ∧ 1 - x < 0 := by
  refine ⟨by rw [min_eq_right hx.le], by linarith⟩

#print axioms min_succ_eq_sum
#print axioms hasSum_shifted_geometric
#print axioms cue_series_hasSum
#print axioms cueL_closed_form
#print axioms tendsto_N_one_sub_exp
#print axioms cueL_tendsto
#print axioms laplace_min_one
#print axioms plateau_defect_neg
end Bgs.Mathlib
