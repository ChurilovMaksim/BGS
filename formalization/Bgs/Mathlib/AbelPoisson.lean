module
public import Mathlib
@[expose] public section

/-!
# Abel–Poisson identity, the clock spectrum and clustered spectra
(BGS-TRACE-006, BGS-TRACE-007, BGS-TRACE-092 §1 prerequisites)

For eigenphases `x : Fin D → ℝ` (in units of a full turn) let
`T_m = ∑_j e^{2πi m x_j}` and
`L_D(s) = D⁻² ∑_{m ≥ 1} e^{-2sm/D} |T_m|²`.

* Poisson kernel: `1 + 2∑_{m≥1} q^m cos(mθ) = (1-q²)/(1 - 2q cos θ + q²)`
  (`poisson_hasSum`), and with `q = e^{-2s/D}` this equals
  `sinh(2s/D)/(cosh(2s/D) - cos θ)` (`poissonKernel_exp`).
* **Abel–Poisson identity** `2 L_D(s) + 1 = D⁻² ∑_{j,k} P_q(2π(x_j - x_k))`
  (`abelL_poisson_identity`).
* **Clock value** `L_D(s) = 1/(e^{2s} - 1)` for `x_j = j/D` (`abelL_clock`).
* **TRACE-006, Proposition 1 (grouped form)**: if the phases are split into `M`
  groups inside which `cos(2π(x_j - x_k)) ≥ cos(2π/D)`, then
  `L_D(s) ≥ (1/(2M)) sinh(2s/D)/(cosh(2s/D) - cos(2π/D)) - 1/2`
  (`abelL_cluster_lower_bound`).
* **TRACE-006, Proposition 2 (factorization)**: for the clustered phases
  `x_{j,r} = j/K - η + r h`, `T_m` factorizes and vanishes unless `K ∣ m`
  (`cluster_trace_factorization`, `cluster_trace_eq_zero`).
-/

open Real Complex BigOperators Filter

namespace Bgs.Mathlib

theorem exp_lt_one_of_neg' {y : ℝ} (h : y < 0) : Real.exp y < 1 := by
  rw [← Real.exp_zero]; exact Real.exp_lt_exp.2 h

/-- Traces of powers of a unitary with eigenphases `x_j` (in turns). -/
noncomputable def traceT {D : ℕ} (x : Fin D → ℝ) (m : ℕ) : ℂ :=
  ∑ j, Complex.exp (2 * π * Complex.I * m * x j)

/-- The smoothed two-point statistic `L_D(s) = D⁻² ∑_{m≥1} e^{-2sm/D} |T_m|²`. -/
noncomputable def abelL {D : ℕ} (x : Fin D → ℝ) (s : ℝ) : ℝ :=
  (1 / (D : ℝ) ^ 2) * ∑' m : ℕ, Real.exp (-2 * s * ((m + 1 : ℕ) : ℝ) / D) * ‖traceT x (m + 1)‖ ^ 2

/-- The Poisson kernel `P_q(θ) = (1 - q²)/(1 - 2q cos θ + q²)`. -/
noncomputable def poissonKernel (q θ : ℝ) : ℝ := (1 - q ^ 2) / (1 - 2 * q * Real.cos θ + q ^ 2)

theorem poisson_denom_pos {q : ℝ} (h0 : 0 ≤ q) (h1 : q < 1) (θ : ℝ) :
    0 < 1 - 2 * q * Real.cos θ + q ^ 2 := by
  have hc := Real.cos_le_one θ
  nlinarith [mul_le_mul_of_nonneg_left hc (by linarith : 0 ≤ 2 * q)]

/-- The Poisson series: `∑_{m≥0} q^{m+1} cos((m+1)θ) = (P_q(θ) - 1)/2`. -/
theorem poisson_hasSum {q : ℝ} (h0 : 0 ≤ q) (h1 : q < 1) (θ : ℝ) :
    HasSum (fun m : ℕ => q ^ (m + 1) * Real.cos ((m + 1 : ℕ) * θ)) ((poissonKernel q θ - 1) / 2) := by
  set z : ℂ := (q : ℂ) * Complex.exp (θ * Complex.I) with hz
  have hzn : ‖z‖ < 1 := by
    rw [hz, norm_mul, Complex.norm_exp_ofReal_mul_I, mul_one, Complex.norm_real,
      Real.norm_eq_abs, abs_of_nonneg h0]
    exact h1
  have hgeom : HasSum (fun m : ℕ => z ^ (m + 1)) (z / (1 - z)) := by
    have := (hasSum_geometric_of_norm_lt_one hzn).mul_left z
    simpa [pow_succ', div_eq_mul_inv] using this
  have hre := Complex.hasSum_re hgeom
  have hterm : ∀ m : ℕ, (z ^ (m + 1)).re = q ^ (m + 1) * Real.cos ((m + 1 : ℕ) * θ) := by
    intro m
    rw [hz, mul_pow, ← Complex.exp_nat_mul, ← Complex.ofReal_pow]
    rw [show ((m + 1 : ℕ) : ℂ) * (θ * Complex.I) = (((m + 1 : ℕ) : ℝ) * θ : ℝ) * Complex.I by
      push_cast; ring]
    rw [Complex.re_ofReal_mul, Complex.exp_ofReal_mul_I_re]
  have hval : (z / (1 - z)).re = (poissonKernel q θ - 1) / 2 := by
    have hden := poisson_denom_pos h0 h1 θ
    have hzre : z.re = q * Real.cos θ := by
      rw [hz, Complex.re_ofReal_mul, Complex.exp_ofReal_mul_I_re]
    have hzim : z.im = q * Real.sin θ := by
      rw [hz, Complex.im_ofReal_mul, Complex.exp_ofReal_mul_I_im]
    have hns : Complex.normSq (1 - z) = 1 - 2 * q * Real.cos θ + q ^ 2 := by
      rw [Complex.normSq_apply]
      simp only [Complex.sub_re, Complex.one_re, Complex.sub_im, Complex.one_im, hzre, hzim]
      nlinarith [Real.sin_sq_add_cos_sq θ]
    rw [Complex.div_re, hns]
    simp only [Complex.sub_re, Complex.one_re, Complex.sub_im, Complex.one_im, hzre, hzim]
    unfold poissonKernel
    rw [← add_div, div_sub_one hden.ne', div_div,
      div_eq_div_iff hden.ne' (by positivity)]
    linear_combination (-2 * q ^ 2 * (1 - 2 * q * Real.cos θ + q ^ 2)) * Real.sin_sq_add_cos_sq θ
  rw [← hval]
  convert! hre using 1
  ext m; rw [hterm]

/-- With `q = e^{-2s/D}`, `P_q(θ) = sinh(2s/D)/(cosh(2s/D) - cos θ)`. -/
theorem poissonKernel_exp (a θ : ℝ) (ha : 0 < a) :
    poissonKernel (Real.exp (-a)) θ = Real.sinh a / (Real.cosh a - Real.cos θ) := by
  have hq : Real.exp (-a) * Real.exp a = 1 := by rw [← Real.exp_add]; simp
  have hc : Real.cos θ < Real.cosh a := by
    have := Real.cos_le_one θ
    have := Real.one_lt_cosh.2 ha.ne'
    linarith
  rw [poissonKernel, Real.sinh_eq, Real.cosh_eq]
  have hpos : 0 < Real.exp a := Real.exp_pos a
  have hden : 0 < 1 - 2 * Real.exp (-a) * Real.cos θ + Real.exp (-a) ^ 2 :=
    poisson_denom_pos (Real.exp_pos _).le (exp_lt_one_of_neg' (by linarith)) θ
  have hden2 : (Real.exp a + Real.exp (-a)) / 2 - Real.cos θ ≠ 0 := by
    rw [← Real.cosh_eq]; linarith
  rw [div_eq_div_iff hden.ne' hden2]
  linear_combination (Real.cos θ - Real.exp (-a)) * hq

/-- `|T_m|² = ∑_{j,k} cos(2π m (x_j - x_k))`. -/
theorem norm_traceT_sq {D : ℕ} (x : Fin D → ℝ) (m : ℕ) :
    ‖traceT x m‖ ^ 2 = ∑ j, ∑ k, Real.cos (m * (2 * π * (x j - x k))) := by
  have h : ((‖traceT x m‖ ^ 2 : ℝ) : ℂ) = traceT x m * (starRingEnd ℂ) (traceT x m) := by
    rw [Complex.mul_conj', Complex.ofReal_pow]
  have h2 : traceT x m * (starRingEnd ℂ) (traceT x m) =
      ∑ j, ∑ k, Complex.exp (((m * (2 * π * (x j - x k)) : ℝ) : ℂ) * Complex.I) := by
    rw [traceT, map_sum, Finset.sum_mul_sum]
    apply Finset.sum_congr rfl; intro j _
    apply Finset.sum_congr rfl; intro k _
    rw [← Complex.exp_conj, ← Complex.exp_add]
    congr 1
    simp only [map_mul, Complex.conj_ofReal, Complex.conj_I, map_natCast, map_ofNat]
    push_cast; ring
  have h3 := congrArg Complex.re (h.trans h2)
  rw [Complex.ofReal_re] at h3
  rw [h3, Complex.re_sum]
  apply Finset.sum_congr rfl; intro j _
  rw [Complex.re_sum]
  apply Finset.sum_congr rfl; intro k _
  exact Complex.exp_ofReal_mul_I_re _

/-- **Abel–Poisson identity.**  For `D ≥ 1`, `s > 0` and `q = e^{-2s/D}`,
`2 L_D(s) + 1 = D⁻² ∑_{j,k} P_q(2π(x_j - x_k))`. -/
theorem abelL_poisson_identity {D : ℕ} (hD : 1 ≤ D) (x : Fin D → ℝ) {s : ℝ} (hs : 0 < s) :
    2 * abelL x s + 1 =
      (1 / (D : ℝ) ^ 2) * ∑ j, ∑ k, poissonKernel (Real.exp (-2 * s / D)) (2 * π * (x j - x k)) := by
  have hDpos : (0 : ℝ) < D := by exact_mod_cast hD
  set q := Real.exp (-2 * s / D) with hqdef
  have h0 : 0 ≤ q := (Real.exp_pos _).le
  have h1 : q < 1 := by
    rw [hqdef]; exact exp_lt_one_of_neg' (div_neg_of_neg_of_pos (by linarith) hDpos)
  have hsum : HasSum (fun m : ℕ => Real.exp (-2 * s * ((m + 1 : ℕ) : ℝ) / D) * ‖traceT x (m + 1)‖ ^ 2)
      (∑ j, ∑ k, (poissonKernel q (2 * π * (x j - x k)) - 1) / 2) := by
    have hfun : (fun m : ℕ => Real.exp (-2 * s * ((m + 1 : ℕ) : ℝ) / D) * ‖traceT x (m + 1)‖ ^ 2) =
        fun m => ∑ j, ∑ k, q ^ (m + 1) * Real.cos ((m + 1 : ℕ) * (2 * π * (x j - x k))) := by
      ext m
      rw [norm_traceT_sq, Finset.mul_sum]
      congr 1; ext j; rw [Finset.mul_sum]
      congr 1; ext k
      congr 1
      rw [hqdef, ← Real.exp_nat_mul]; congr 1; ring
    rw [hfun]
    exact hasSum_sum fun j _ => hasSum_sum fun k _ => poisson_hasSum h0 h1 _
  rw [abelL, hsum.tsum_eq]
  have e : ∀ j : Fin D, ∑ k, (poissonKernel q (2 * π * (x j - x k)) - 1) / 2 =
      (∑ k, poissonKernel q (2 * π * (x j - x k)) - D) / 2 := by
    intro j
    rw [← Finset.sum_div, Finset.sum_sub_distrib]
    simp
  simp only [e]
  rw [← Finset.sum_div, Finset.sum_sub_distrib]
  simp only [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
  field_simp
  ring

/-- The `D`-clock spectrum `x_j = j/D`. -/
noncomputable def clockPhases (D : ℕ) : Fin D → ℝ := fun j => (j : ℝ) / D

/-- Traces of the clock: `T_m = D` if `D ∣ m`, and `0` otherwise. -/
theorem traceT_clock {D : ℕ} (hD : 1 ≤ D) (m : ℕ) :
    traceT (clockPhases D) m = if D ∣ m then (D : ℂ) else 0 := by
  have hD0 : D ≠ 0 := by omega
  set ω := Complex.exp (2 * π * Complex.I / D) with hω
  have hprim : IsPrimitiveRoot ω D := Complex.isPrimitiveRoot_exp D hD0
  have hterm : ∀ j : Fin D, Complex.exp (2 * π * Complex.I * m * (clockPhases D j : ℝ)) =
      (ω ^ m) ^ (j : ℕ) := by
    intro j
    rw [hω, ← Complex.exp_nat_mul, ← Complex.exp_nat_mul, clockPhases]
    congr 1; push_cast; field_simp
  rw [traceT]
  simp_rw [hterm]
  rw [Fin.sum_univ_eq_sum_range (fun i => (ω ^ m) ^ i)]
  split_ifs with hdvd
  · have : ω ^ m = 1 := (hprim.pow_eq_one_iff_dvd m).2 hdvd
    simp [this]
  · have hne : ω ^ m ≠ 1 := fun h => hdvd ((hprim.pow_eq_one_iff_dvd m).1 h)
    rw [geom_sum_eq hne, ← pow_mul, mul_comm, pow_mul, hprim.pow_eq_one, one_pow, sub_self,
      zero_div]

/-- **Clock value** `L_D(s) = 1/(e^{2s} - 1)` for the `D`-clock. -/
theorem abelL_clock {D : ℕ} (hD : 1 ≤ D) {s : ℝ} (hs : 0 < s) :
    abelL (clockPhases D) s = 1 / (Real.exp (2 * s) - 1) := by
  have hDpos : (0 : ℝ) < D := by exact_mod_cast hD
  have hr0 : 0 ≤ Real.exp (-2 * s) := (Real.exp_pos _).le
  have hr1 : Real.exp (-2 * s) < 1 := exp_lt_one_of_neg' (by linarith)
  have hD0 : (D : ℝ) ≠ 0 := hDpos.ne'
  -- reindex the nonzero terms `m + 1 = D (k + 1)`
  have hinj : Function.Injective (fun k : ℕ => D * k + (D - 1)) := by
    intro a b h; simp only at h
    have : D * a = D * b := by omega
    exact Nat.eq_of_mul_eq_mul_left (by omega) this
  have hsum : HasSum (fun m : ℕ => Real.exp (-2 * s * ((m + 1 : ℕ) : ℝ) / D) *
      ‖traceT (clockPhases D) (m + 1)‖ ^ 2) ((D : ℝ) ^ 2 * (Real.exp (-2 * s) / (1 - Real.exp (-2 * s)))) := by
    rw [← hinj.hasSum_iff]
    · have hg := ((hasSum_geometric_of_lt_one hr0 hr1).mul_left (Real.exp (-2 * s))).mul_left
        ((D : ℝ) ^ 2)
      convert! hg using 1
      · ext k
        simp only [Function.comp]
        have hnat : D * k + (D - 1) + 1 = D * (k + 1) := by rw [Nat.mul_succ]; omega
        have hdvd : D ∣ D * k + (D - 1) + 1 := ⟨k + 1, hnat⟩
        rw [traceT_clock hD]; simp only [hdvd, ↓reduceIte, Complex.norm_natCast]
        have hcast : ((D * k + (D - 1) + 1 : ℕ) : ℝ) = D * (k + 1) := by
          rw [hnat]; push_cast; ring
        rw [hcast, ← Real.exp_nat_mul, ← Real.exp_add]
        rw [show -2 * s * ((D : ℝ) * (k + 1)) / D = -2 * s + (k : ℝ) * (-2 * s) by
          field_simp; ring]
        ring
    · intro m hm
      have hndvd : ¬ D ∣ m + 1 := by
        rintro ⟨c, hc⟩
        cases c with
        | zero => simp at hc
        | succ c =>
          rw [Nat.mul_succ] at hc
          exact hm ⟨c, by simp only; omega⟩
      rw [traceT_clock hD]; simp [hndvd]
  rw [abelL, hsum.tsum_eq]
  have hE : Real.exp (2 * s) * Real.exp (-2 * s) = 1 := by rw [← Real.exp_add]; simp
  have h1 : 1 - Real.exp (-2 * s) ≠ 0 := by linarith
  have h2 : Real.exp (2 * s) - 1 ≠ 0 := by
    have := Real.add_one_lt_exp (show 2 * s ≠ 0 by positivity); linarith
  rw [← mul_assoc, one_div_mul_cancel (by positivity), one_mul, div_eq_div_iff h1 h2]
  linear_combination hE

/-- Pair-count identity: `#{(j,k) : g j = g k} = ∑_t b_t²`, and by Cauchy–Schwarz it is at
least `D²/M`. -/
theorem pair_count_ge {D M : ℕ} (hM : 1 ≤ M) (g : Fin D → Fin M) :
    ((D : ℝ) ^ 2) / M ≤ ∑ j, ∑ k, if g j = g k then (1 : ℝ) else 0 := by
  set b : Fin M → ℝ := fun t => ((Finset.univ.filter fun j => g j = t).card : ℝ) with hb
  have hrow : ∀ j, (∑ k, if g j = g k then (1 : ℝ) else 0) = b (g j) := by
    intro j
    rw [Finset.sum_boole, hb]
    congr 2
    ext k; simp [eq_comm]
  have hsq : (∑ j, ∑ k, if g j = g k then (1 : ℝ) else 0) = ∑ t, b t ^ 2 := by
    simp_rw [hrow]
    rw [← Finset.sum_fiberwise Finset.univ g (fun j => b (g j))]
    apply Finset.sum_congr rfl; intro t _
    rw [Finset.sum_congr rfl (fun j hj => by rw [(Finset.mem_filter.1 hj).2])]
    rw [Finset.sum_const, nsmul_eq_mul, sq]
  have htot : ∑ t, b t = D := by
    rw [hb]
    have := Finset.card_eq_sum_card_fiberwise (s := Finset.univ) (t := Finset.univ) (f := g)
      (fun _ _ => Finset.mem_univ _)
    rw [Finset.card_univ, Fintype.card_fin] at this
    show ∑ t, ((Finset.univ.filter fun j => g j = t).card : ℝ) = D
    exact_mod_cast this.symm
  have hcs := sq_sum_le_card_mul_sum_sq (s := Finset.univ) (f := b)
  rw [htot, Finset.card_univ, Fintype.card_fin] at hcs
  rw [hsq, div_le_iff₀ (by exact_mod_cast hM)]
  linarith

/-- **TRACE-006, Proposition 1 (grouped form).**  If the `D ≥ 2` eigenphases are split by
`g` into `M` groups inside which `cos(2π(x_j - x_k)) ≥ cos(2π/D)` (circular distance at most
`1/D`), then for every `s > 0`,
`L_D(s) ≥ (1/(2M)) · sinh(2s/D)/(cosh(2s/D) - cos(2π/D)) - 1/2`. -/
theorem abelL_cluster_lower_bound {D M : ℕ} (hD : 1 ≤ D) (hM : 1 ≤ M) (x : Fin D → ℝ)
    (g : Fin D → Fin M)
    (hclose : ∀ j k, g j = g k → Real.cos (2 * π / D) ≤ Real.cos (2 * π * (x j - x k)))
    {s : ℝ} (hs : 0 < s) :
    (1 / (2 * M)) * (Real.sinh (2 * s / D) / (Real.cosh (2 * s / D) - Real.cos (2 * π / D)))
      - 1 / 2 ≤ abelL x s := by
  have hDpos : (0 : ℝ) < D := by exact_mod_cast hD
  have hMpos : (0 : ℝ) < M := by exact_mod_cast hM
  set a := 2 * s / D with ha
  have hapos : 0 < a := div_pos (by linarith) hDpos
  have hid := abelL_poisson_identity hD x hs
  have hq : Real.exp (-2 * s / D) = Real.exp (-a) := by rw [ha]; congr 1; ring
  rw [hq] at hid
  simp_rw [poissonKernel_exp a _ hapos] at hid
  have hsh : 0 < Real.sinh a := Real.sinh_pos_iff.2 hapos
  have hcosh : ∀ θ, Real.cos θ < Real.cosh a := fun θ => by
    have := Real.cos_le_one θ; have := Real.one_lt_cosh.2 hapos.ne'; linarith
  set P0 := Real.sinh a / (Real.cosh a - Real.cos (2 * π / D)) with hP0
  have hP0pos : 0 < P0 := div_pos hsh (by linarith [hcosh (2 * π / D)])
  have hterm : ∀ j k, (if g j = g k then P0 else 0) ≤
      Real.sinh a / (Real.cosh a - Real.cos (2 * π * (x j - x k))) := by
    intro j k
    split_ifs with h
    · apply div_le_div_of_nonneg_left hsh.le (by linarith [hcosh (2 * π * (x j - x k))])
      linarith [hclose j k h]
    · exact (div_pos hsh (by linarith [hcosh (2 * π * (x j - x k))])).le
  have hsum : P0 * (((D : ℝ) ^ 2) / M) ≤
      ∑ j, ∑ k, Real.sinh a / (Real.cosh a - Real.cos (2 * π * (x j - x k))) := by
    calc P0 * (((D : ℝ) ^ 2) / M) ≤ P0 * ∑ j, ∑ k, if g j = g k then (1 : ℝ) else 0 :=
          mul_le_mul_of_nonneg_left (pair_count_ge hM g) hP0pos.le
      _ = ∑ j, ∑ k, if g j = g k then P0 else 0 := by
          rw [Finset.mul_sum]; congr 1; ext j; rw [Finset.mul_sum]; congr 1; ext k
          split_ifs <;> simp
      _ ≤ _ := Finset.sum_le_sum fun j _ => Finset.sum_le_sum fun k _ => hterm j k
  have hL : abelL x s = ((1 / (D : ℝ) ^ 2) *
      ∑ j, ∑ k, Real.sinh a / (Real.cosh a - Real.cos (2 * π * (x j - x k))) - 1) / 2 := by
    linarith
  rw [hL]
  have h2 : (1 / (D : ℝ) ^ 2) * (P0 * (((D : ℝ) ^ 2) / M)) = P0 / M := by
    field_simp
  have h3 : (1 / (D : ℝ) ^ 2) * (P0 * (((D : ℝ) ^ 2) / M)) ≤ (1 / (D : ℝ) ^ 2) *
      ∑ j, ∑ k, Real.sinh a / (Real.cosh a - Real.cos (2 * π * (x j - x k))) :=
    mul_le_mul_of_nonneg_left hsum (by positivity)
  rw [h2] at h3
  have : 1 / (2 * (M : ℝ)) * P0 = (P0 / M) / 2 := by field_simp
  rw [this]
  linarith

/-- **TRACE-006, Proposition 2 (factorization).**  For the clustered phases
`x_{j,r} = j/K - η + r h` (`0 ≤ j < K`, `0 ≤ r < n`),
`∑_{j,r} e^{2πi m x_{j,r}} = e^{-2πimη} (∑_j e^{2πimj/K}) (∑_r e^{2πimrh})`. -/
theorem cluster_trace_factorization (K n m : ℕ) (η h : ℝ) :
    (∑ p : Fin K × Fin n,
        Complex.exp (2 * π * Complex.I * m * (((p.1 : ℝ) / K - η + (p.2 : ℝ) * h : ℝ)))) =
      Complex.exp (-(2 * π * Complex.I * m * η)) * traceT (clockPhases K) m *
        ∑ r : Fin n, Complex.exp (2 * π * Complex.I * m * ((r : ℝ) * h : ℝ)) := by
  rw [Fintype.sum_prod_type]
  simp only [traceT, Finset.mul_sum, Finset.sum_mul]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun j _ => Finset.sum_congr rfl fun r _ => ?_
  rw [← Complex.exp_add, ← Complex.exp_add, clockPhases]
  congr 1
  push_cast
  ring

/-- Consequently the clustered trace vanishes unless `K ∣ m`. -/
theorem cluster_trace_eq_zero {K : ℕ} (hK : 1 ≤ K) (n : ℕ) {m : ℕ} (hm : ¬ K ∣ m) (η h : ℝ) :
    (∑ p : Fin K × Fin n,
        Complex.exp (2 * π * Complex.I * m * (((p.1 : ℝ) / K - η + (p.2 : ℝ) * h : ℝ)))) = 0 := by
  rw [cluster_trace_factorization, traceT_clock hK]
  simp [hm]

end Bgs.Mathlib
