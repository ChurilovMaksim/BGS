module
public import Mathlib
public import Bgs.Mathlib.AbelPoisson
public import Bgs.Mathlib.ClockRigidity
@[expose] public section

/-!
# Deleted clock: strict Hardy positivity does not identify a limiting excess
(`mathematics/trace-bridge/deleted_clock_hardy_boundary.md`, addition to BGS-TRACE-091)

`V_N` has as spectrum all `(N+1)`-st roots of unity except `1`, i.e. eigenphases
`x_j = (j+1)/(N+1)`, `j = 0, …, N−1`.

* `traceT_deleted`: `Tr V_N^m = N` if `(N+1) ∣ m` and `−1` otherwise.
* `abelL_deleted`: the exact value
  `L_N^del(s) = 1/(N²(e^{2s/N} − 1)) + (1 − 1/N²)/(e^{2s(1+1/N)} − 1)`.
* `abelL_deleted_gt_clock`: for `N ≥ 2` the Hardy excess over the clock floor is strictly
  positive (the spectrum is not a rotated `N`-clock).
* `abelL_deleted_tendsto`: nevertheless `L_N^del(s) → 1/(e^{2s} − 1)`.
* `abelL_deleted_excess_asymptotic`: more precisely
  `N (L_N^del(s) − 1/(e^{2s}−1)) → 1/(2s) − s/(2 sinh² s)`,
  and `deleted_coeff_pos`: this coefficient is strictly positive.
-/

open Real Complex BigOperators Filter Topology

namespace Bgs.Mathlib

/-- The deleted clock: the `(N+1)`-st roots of unity other than `1`. -/
noncomputable def deletedPhases (N : ℕ) : Fin N → ℝ := fun j => ((j : ℝ) + 1) / (N + 1)

theorem traceT_deleted (N m : ℕ) :
    traceT (deletedPhases N) m = if (N + 1) ∣ m then (N : ℂ) else -1 := by
  have hc := traceT_clock (D := N + 1) (by omega) m
  rw [traceT, Fin.sum_univ_succ] at hc
  have hsplit : traceT (deletedPhases N) m = traceT (clockPhases (N + 1)) m - 1 := by
    rw [traceT, traceT, Fin.sum_univ_succ]
    simp only [clockPhases, deletedPhases, Fin.val_zero, Fin.val_succ]
    push_cast
    simp
  rw [hsplit, traceT_clock (by omega)]
  split_ifs <;> push_cast <;> ring

lemma norm_traceT_deleted_sq (N m : ℕ) :
    ‖traceT (deletedPhases N) m‖ ^ 2 =
      1 + if (N + 1) ∣ m then ((N : ℝ) ^ 2 - 1) else 0 := by
  rw [traceT_deleted]
  split_ifs <;> simp

/-- **Exact deleted-clock Abel statistic.** -/
theorem abelL_deleted {N : ℕ} (hN : 1 ≤ N) {s : ℝ} (hs : 0 < s) :
    abelL (deletedPhases N) s =
      1 / ((N : ℝ) ^ 2 * (Real.exp (2 * s / N) - 1))
        + (1 - 1 / (N : ℝ) ^ 2) / (Real.exp (2 * s * (1 + 1 / N)) - 1) := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  have hN0 : (N : ℝ) ≠ 0 := hNpos.ne'
  set q := Real.exp (-2 * s / N) with hq
  set r := Real.exp (-2 * s * (1 + 1 / N)) with hr
  have hq0 : 0 ≤ q := (Real.exp_pos _).le
  have hq1 : q < 1 := exp_lt_one_of_neg' (by
    have : 0 < 2 * s / N := by positivity
    rw [neg_mul, neg_div]; linarith)
  have hr0 : 0 ≤ r := (Real.exp_pos _).le
  have hr1 : r < 1 := exp_lt_one_of_neg' (by
    have : 0 < 2 * s * (1 + 1 / N) := by positivity
    nlinarith)
  -- the geometric part
  have hg1 : HasSum (fun m : ℕ => Real.exp (-2 * s * ((m + 1 : ℕ) : ℝ) / N)) (q / (1 - q)) := by
    have := (hasSum_geometric_of_lt_one hq0 hq1).mul_left q
    convert! this using 1
    · ext m
      rw [hq, ← Real.exp_nat_mul, ← Real.exp_add]
      congr 1; push_cast; ring
  -- the resonant part, supported on `(N+1) ∣ m+1`
  have hinj : Function.Injective (fun k : ℕ => (N + 1) * k + N) := by
    intro a b h; simp only at h
    have : (N + 1) * a = (N + 1) * b := by omega
    exact Nat.eq_of_mul_eq_mul_left (by omega) this
  have hg2 : HasSum (fun m : ℕ => if (N + 1) ∣ m + 1 then
      Real.exp (-2 * s * ((m + 1 : ℕ) : ℝ) / N) else 0) (r / (1 - r)) := by
    rw [← hinj.hasSum_iff]
    · have hg := (hasSum_geometric_of_lt_one hr0 hr1).mul_left r
      convert! hg using 1
      · ext k
        simp only [Function.comp]
        have hnat : (N + 1) * k + N + 1 = (N + 1) * (k + 1) := by ring
        have hdvd : (N + 1) ∣ (N + 1) * k + N + 1 := ⟨k + 1, hnat⟩
        simp only [hdvd, ↓reduceIte]
        rw [hnat, hr, ← Real.exp_nat_mul, ← Real.exp_add]
        congr 1; push_cast; field_simp; ring
    · intro m hm
      have hndvd : ¬ (N + 1) ∣ m + 1 := by
        rintro ⟨c, hc⟩
        cases c with
        | zero => simp at hc
        | succ c => exact hm ⟨c, by simp only; rw [Nat.mul_succ] at hc; omega⟩
      simp [hndvd]
  have hsum : HasSum (fun m : ℕ => Real.exp (-2 * s * ((m + 1 : ℕ) : ℝ) / N) *
      ‖traceT (deletedPhases N) (m + 1)‖ ^ 2)
      (q / (1 - q) + ((N : ℝ) ^ 2 - 1) * (r / (1 - r))) := by
    convert! hg1.add (hg2.mul_left ((N : ℝ) ^ 2 - 1)) using 1
    ext m
    rw [norm_traceT_deleted_sq]
    split_ifs <;> ring
  rw [abelL, hsum.tsum_eq]
  -- convert! `q/(1-q)` and `r/(1-r)` to the stated form
  have hqe : q * Real.exp (2 * s / N) = 1 := by
    rw [hq, ← Real.exp_add]; simp [neg_div]
  have hre : r * Real.exp (2 * s * (1 + 1 / N)) = 1 := by
    rw [hr, ← Real.exp_add]; simp
  have hE1 : Real.exp (2 * s / N) - 1 ≠ 0 := by
    have h0 : 0 < 2 * s / N := by positivity
    have := Real.add_one_lt_exp h0.ne'; linarith
  have hE2 : Real.exp (2 * s * (1 + 1 / N)) - 1 ≠ 0 := by
    have h0 : 0 < 2 * s * (1 + 1 / N) := by positivity
    have := Real.add_one_lt_exp h0.ne'; linarith
  have h1q : 1 - q ≠ 0 := by linarith
  have h1r : 1 - r ≠ 0 := by linarith
  have eq1 : q / (1 - q) = 1 / (Real.exp (2 * s / N) - 1) := by
    rw [div_eq_div_iff h1q hE1]; linear_combination hqe
  have eq2 : r / (1 - r) = 1 / (Real.exp (2 * s * (1 + 1 / N)) - 1) := by
    rw [div_eq_div_iff h1r hE2]; linear_combination hre
  rw [eq1, eq2]
  field_simp

/-- A rotated clock with `N ≥ 2` has vanishing first trace. -/
lemma traceT_one_of_rotated {N : ℕ} (hN : 2 ≤ N) {x : Fin N → ℝ} (hx : IsRotatedClock x) :
    traceT x 1 = 0 := by
  obtain ⟨c, σ, hσ⟩ := hx
  choose n hn using hσ
  have hterm : ∀ j, Complex.exp (2 * π * Complex.I * ((1 : ℕ) : ℂ) * (x j : ℂ)) =
      Complex.exp (2 * π * Complex.I * c) *
        Complex.exp (2 * π * Complex.I * ((1 : ℕ) : ℂ) * (clockPhases N (σ j) : ℂ)) := by
    intro j
    rw [← Complex.exp_add, hn j, clockPhases]
    have : Complex.exp (2 * π * Complex.I * (n j : ℂ)) = 1 := by
      rw [Complex.exp_eq_one_iff]; exact ⟨n j, by ring⟩
    push_cast
    rw [show 2 * ↑π * Complex.I * 1 * (↑c + ↑↑(σ j) / ↑N + ↑(n j)) =
      (2 * ↑π * Complex.I * ↑c + 2 * ↑π * Complex.I * 1 * (↑↑(σ j) / ↑N)) +
        2 * ↑π * Complex.I * ↑(n j) by ring, Complex.exp_add, this, mul_one]
  rw [traceT]
  simp_rw [hterm]
  rw [← Finset.mul_sum]
  rw [show (∑ j, Complex.exp (2 * π * Complex.I * ((1 : ℕ) : ℂ) * (clockPhases N (σ j) : ℂ))) =
      traceT (clockPhases N) 1 from
    Equiv.sum_comp σ (fun j => Complex.exp (2 * π * Complex.I * ((1 : ℕ) : ℂ) *
      (clockPhases N j : ℂ)))]
  rw [traceT_clock (by omega)]
  have : ¬ N ∣ 1 := fun h => by have := Nat.le_of_dvd one_pos h; omega
  simp [this]

/-- For `N ≥ 2` the deleted clock is not a rotated clock. -/
theorem deleted_not_rotatedClock {N : ℕ} (hN : 2 ≤ N) : ¬ IsRotatedClock (deletedPhases N) := by
  intro h
  have h1 := traceT_one_of_rotated hN h
  rw [traceT_deleted] at h1
  have : ¬ (N + 1) ∣ 1 := fun h => by have := Nat.le_of_dvd one_pos h; omega
  simp [this] at h1

/-- **Strict Hardy positivity** for every finite `N ≥ 2`. -/
theorem abelL_deleted_gt_clock {N : ℕ} (hN : 2 ≤ N) {s : ℝ} (hs : 0 < s) :
    1 / (Real.exp (2 * s) - 1) < abelL (deletedPhases N) s :=
  abelL_gt_clock (by omega) _ (deleted_not_rotatedClock hN) hs

/-! ## The excess nevertheless tends to zero -/

lemma tendsto_inv_nat_nhdsNE :
    Tendsto (fun N : ℕ => (1 : ℝ) / N) atTop (𝓝[≠] 0) := by
  refine tendsto_nhdsWithin_iff.2 ⟨tendsto_one_div_atTop_nhds_zero_nat, ?_⟩
  filter_upwards [eventually_ge_atTop 1] with N hN
  have : (0 : ℝ) < N := by exact_mod_cast hN
  exact (one_div_pos.2 this).ne'

/-- `N (e^{2s/N} − 1) → 2s`. -/
lemma tendsto_N_exp_sub_one (s : ℝ) :
    Tendsto (fun N : ℕ => (N : ℝ) * (Real.exp (2 * s / N) - 1)) atTop (𝓝 (2 * s)) := by
  have hd : HasDerivAt (fun t : ℝ => Real.exp (2 * s * t)) (2 * s) 0 := by
    have := ((hasDerivAt_id (0 : ℝ)).const_mul (2 * s)).exp
    simpa using this
  have hsl := hd.tendsto_slope_zero
  have hc := hsl.comp tendsto_inv_nat_nhdsNE
  refine hc.congr' ?_
  filter_upwards [eventually_ge_atTop 1] with N hN
  have : (N : ℝ) ≠ 0 := by have : (0 : ℝ) < N := by exact_mod_cast hN
                           exact this.ne'
  simp only [Function.comp, zero_add, mul_zero, Real.exp_zero, smul_eq_mul, one_div, inv_inv]
  congr 3

/-- `F(x) = 1/(e^x − 1)` has derivative `−e^x/(e^x−1)²` at `x > 0`. -/
lemma hasDerivAt_bose {x : ℝ} (hx : 0 < x) :
    HasDerivAt (fun y => 1 / (Real.exp y - 1)) (-(Real.exp x) / (Real.exp x - 1) ^ 2) x := by
  have hne : Real.exp x - 1 ≠ 0 := by
    have := Real.add_one_lt_exp hx.ne'; linarith
  have := ((Real.hasDerivAt_exp x).sub_const 1).inv hne
  simp only [one_div]
  convert! this using 1

/-- `e^{2s}/(e^{2s}−1)² = 1/(4 sinh² s)`. -/
lemma exp_two_div_sq_eq (s : ℝ) (hs : 0 < s) :
    Real.exp (2 * s) / (Real.exp (2 * s) - 1) ^ 2 = 1 / (4 * Real.sinh s ^ 2) := by
  have h1 : Real.exp (2 * s) - 1 = 2 * Real.exp s * Real.sinh s := by
    rw [Real.sinh_eq, show 2 * s = s + s by ring, Real.exp_add, Real.exp_neg]
    field_simp
  have hsh : 0 < Real.sinh s := Real.sinh_pos_iff.2 hs
  rw [h1, show 2 * s = s + s by ring, Real.exp_add]
  field_simp
  ring

/-- **The excess tends to zero.** -/
theorem abelL_deleted_tendsto {s : ℝ} (hs : 0 < s) :
    Tendsto (fun N : ℕ => abelL (deletedPhases N) s) atTop (𝓝 (1 / (Real.exp (2 * s) - 1))) := by
  have hE : Real.exp (2 * s) - 1 ≠ 0 := by
    have := Real.add_one_lt_exp (show 2 * s ≠ 0 by positivity); linarith
  have hinv : Tendsto (fun N : ℕ => (1 : ℝ) / N) atTop (𝓝 0) := tendsto_one_div_atTop_nhds_zero_nat
  -- first term: `1/(N · N(e^{2s/N}-1)) → 0`
  have hNinf : Tendsto (fun N : ℕ => (N : ℝ)) atTop atTop := tendsto_natCast_atTop_atTop
  have h1 : Tendsto (fun N : ℕ => 1 / ((N : ℝ) ^ 2 * (Real.exp (2 * s / N) - 1))) atTop (𝓝 0) := by
    have hprod : Tendsto (fun N : ℕ => (N : ℝ) * ((N : ℝ) * (Real.exp (2 * s / N) - 1)))
        atTop atTop :=
      hNinf.atTop_mul_pos (by positivity) (tendsto_N_exp_sub_one s)
    have := hprod.inv_tendsto_atTop
    refine (this.congr' ?_)
    filter_upwards with N
    simp only [Pi.inv_apply, one_div]; ring_nf
  -- second term
  have harg : Tendsto (fun N : ℕ => 2 * s * (1 + 1 / (N : ℝ))) atTop (𝓝 (2 * s)) := by
    have := (hinv.const_add 1).const_mul (2 * s)
    simpa using this
  have hcont : ContinuousAt (fun y => (1 : ℝ) / (Real.exp y - 1)) (2 * s) :=
    (hasDerivAt_bose (by positivity)).continuousAt
  have h2 : Tendsto (fun N : ℕ => (1 - 1 / (N : ℝ) ^ 2) / (Real.exp (2 * s * (1 + 1 / N)) - 1))
      atTop (𝓝 (1 / (Real.exp (2 * s) - 1))) := by
    have hsq : Tendsto (fun N : ℕ => 1 - 1 / (N : ℝ) ^ 2) atTop (𝓝 1) := by
      have := (hinv.pow 2).const_sub 1
      simpa [div_pow] using this
    have := hsq.mul (hcont.tendsto.comp harg)
    simp only [one_mul] at this
    refine this.congr' ?_
    filter_upwards with N
    simp [Function.comp, div_eq_mul_inv]
  have := h1.add h2
  rw [zero_add] at this
  refine this.congr' ?_
  filter_upwards [eventually_ge_atTop 1] with N hN
  rw [abelL_deleted hN hs]

/-- The first-order coefficient `1/(2s) − s/(2 sinh² s)` is strictly positive. -/
theorem deleted_coeff_pos {s : ℝ} (hs : 0 < s) :
    0 < 1 / (2 * s) - s / (2 * Real.sinh s ^ 2) := by
  have hsh : s < Real.sinh s := Real.self_lt_sinh_iff.2 hs
  have hsq : s ^ 2 < Real.sinh s ^ 2 := pow_lt_pow_left₀ hsh hs.le (by norm_num)
  have hpos : 0 < Real.sinh s := by linarith
  rw [sub_pos, div_lt_div_iff₀ (by positivity) (by positivity)]
  nlinarith

/-- **First-order asymptotics of the excess**:
`N (L_N^del(s) − 1/(e^{2s}−1)) → 1/(2s) − s/(2 sinh² s)`. -/
theorem abelL_deleted_excess_asymptotic {s : ℝ} (hs : 0 < s) :
    Tendsto (fun N : ℕ => (N : ℝ) * (abelL (deletedPhases N) s - 1 / (Real.exp (2 * s) - 1)))
      atTop (𝓝 (1 / (2 * s) - s / (2 * Real.sinh s ^ 2))) := by
  set F : ℝ → ℝ := fun y => 1 / (Real.exp y - 1) with hF
  have hinv : Tendsto (fun N : ℕ => (1 : ℝ) / N) atTop (𝓝 0) := tendsto_one_div_atTop_nhds_zero_nat
  -- term A: `1/(N(e^{2s/N}-1)) → 1/(2s)`
  have hA : Tendsto (fun N : ℕ => 1 / ((N : ℝ) * (Real.exp (2 * s / N) - 1))) atTop
      (𝓝 (1 / (2 * s))) := by
    have := (tendsto_N_exp_sub_one s).inv₀ (by positivity)
    simp only [one_div]; exact this
  -- term B: `F(2s(1+1/N))/N → 0`
  have harg : Tendsto (fun N : ℕ => 2 * s * (1 + 1 / (N : ℝ))) atTop (𝓝 (2 * s)) := by
    have := (hinv.const_add 1).const_mul (2 * s)
    simpa using this
  have hderiv := hasDerivAt_bose (x := 2 * s) (by positivity)
  have hB : Tendsto (fun N : ℕ => F (2 * s * (1 + 1 / (N : ℝ))) * (1 / N)) atTop (𝓝 0) := by
    have := (hderiv.continuousAt.tendsto.comp harg).mul hinv
    simpa [hF] using this
  -- term C: `N (F(2s + 2s/N) − F(2s)) → 2s F'(2s)`
  have hC : Tendsto (fun N : ℕ => (N : ℝ) * (F (2 * s * (1 + 1 / (N : ℝ))) - F (2 * s))) atTop
      (𝓝 (2 * s * (-(Real.exp (2 * s)) / (Real.exp (2 * s) - 1) ^ 2))) := by
    have hsl := hderiv.tendsto_slope_zero
    have hh : Tendsto (fun N : ℕ => 2 * s * (1 / (N : ℝ))) atTop (𝓝[≠] 0) := by
      refine tendsto_nhdsWithin_iff.2 ⟨?_, ?_⟩
      · simpa using hinv.const_mul (2 * s)
      · filter_upwards [eventually_ge_atTop 1] with N hN
        have : (0 : ℝ) < N := by exact_mod_cast hN
        exact (by positivity : (0:ℝ) < 2 * s * (1 / N)).ne'
    have := (hsl.comp hh).const_mul (2 * s)
    refine this.congr' ?_
    filter_upwards [eventually_ge_atTop 1] with N hN
    have hN0 : (N : ℝ) ≠ 0 := by have : (0 : ℝ) < N := by exact_mod_cast hN
                                 exact this.ne'
    simp only [Function.comp, smul_eq_mul]
    rw [show 2 * s + 2 * s * (1 / (N : ℝ)) = 2 * s * (1 + 1 / N) by ring]
    simp only [hF]
    field_simp
  have hsum := (hA.sub hB).add hC
  have hval : 1 / (2 * s) - 0 + 2 * s * (-(Real.exp (2 * s)) / (Real.exp (2 * s) - 1) ^ 2) =
      1 / (2 * s) - s / (2 * Real.sinh s ^ 2) := by
    rw [neg_div, exp_two_div_sq_eq s hs]
    have hsh : 0 < Real.sinh s := Real.sinh_pos_iff.2 hs
    field_simp; ring
  rw [hval] at hsum
  refine hsum.congr' ?_
  filter_upwards [eventually_ge_atTop 1] with N hN
  have hN0 : (N : ℝ) ≠ 0 := by have : (0 : ℝ) < N := by exact_mod_cast hN
                               exact this.ne'
  rw [abelL_deleted hN hs]
  simp only [hF]
  field_simp
  ring

end Bgs.Mathlib
