module
public import Bgs.Mathlib.AbelPoisson
public import Bgs.Mathlib.CueReference
@[expose] public section

/-!
# The two-clock Gram falsifier (BGS-TRACE-008)

Source: `mathematics/trace-bridge/two_clock_gram_falsifier.md`.

For eigenphases `x : Fin N → ℝ` (in turns) put `p_m = ∑_j e^{2πi m x_j}` for `m ∈ ℤ`
(so `p_0 = N`, `p_{-m} = conj p_m`), the Toeplitz Gram matrix
`Γ_N = [N⁻¹ p_{b-a}]_{a,b}` and the Gram moment `G_N = N⁻¹ Tr Γ_N²`.

* `gramMoment_formula` — equation (4):
  `G_N = 1 + 2 N⁻³ ∑_{m=1}^{N-1} (N - m) |p_m|²`.
* `cueGramMoment_eq` — equation (5): inserting the CUE form factor `min(m, N)`
  gives `4/3 - 1/(3N²)`.
* `traceT_twoGon` — power sums of two regular `n`-gons at relative angle `φ/n`:
  `p_m = 0` unless `n ∣ m`, and `p_m = n (1 + e^{i m φ / n})` otherwise.
* `gramMoment_twoGon` — equation (7): `G_{2n} = 1 + cos²(φ/2)`.
* `exists_twoGon_cue_gram` — equation (3): for every `n ≥ 2` some
  `φ ∈ (0, π)` makes the two-gon match the CUE Gram value exactly.
* `abelL_twoGon` — equation (8), in exact (not only limiting) form:
  `L_{2n}(s) = B_φ(s) = ∑_{k ≥ 1} e^{-sk} cos²(kφ/2)` for every `n ≥ 1`.
* `twoClockB_closed_form` — equation (10).
* `twoClockB_le`, `twoClockB_ne_cue` — `B_φ(s) ≤ e^{-s}/(1 - e^{-s})`, and
  `B_φ` differs from the CUE target `(1 - e^{-2s})/(4s²)`.
-/

open Real Complex BigOperators Filter

namespace Bgs.Mathlib

/-- Integer-indexed power sums `p_m = ∑_j e^{2πi m x_j}`. -/
noncomputable def traceZ {N : ℕ} (x : Fin N → ℝ) (m : ℤ) : ℂ :=
  ∑ j, Complex.exp (2 * π * Complex.I * m * x j)

/-- The Toeplitz Gram matrix `Γ_N = [N⁻¹ p_{b-a}]`. -/
noncomputable def gramMatrix {N : ℕ} (x : Fin N → ℝ) : Matrix (Fin N) (Fin N) ℂ :=
  Matrix.of fun a b => traceZ x ((b : ℤ) - a) / N

/-- The Gram second moment `G_N = N⁻¹ Tr Γ_N²`. -/
noncomputable def gramMoment {N : ℕ} (x : Fin N → ℝ) : ℂ :=
  (1 / (N : ℂ)) * (gramMatrix x ^ 2).trace

/-- The CUE value of the Gram moment obtained by inserting the CUE form factor
`E|p_m|² = min(m, N)` into (4). -/
noncomputable def cueGramMoment (N : ℕ) : ℝ :=
  1 + 2 / (N : ℝ) ^ 3 * ∑ m ∈ Finset.Ico 1 N, ((N : ℝ) - m) * cueFormFactor N m

theorem traceZ_natCast {N : ℕ} (x : Fin N → ℝ) (m : ℕ) : traceZ x m = traceT x m := by
  simp [traceZ, traceT]

theorem traceZ_neg {N : ℕ} (x : Fin N → ℝ) (m : ℤ) :
    traceZ x (-m) = (starRingEnd ℂ) (traceZ x m) := by
  rw [traceZ, traceZ, map_sum]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [← Complex.exp_conj]
  congr 1
  simp only [map_mul, Complex.conj_ofReal, Complex.conj_I, map_intCast, map_ofNat]
  push_cast; ring

/-- Counting pairs by their difference. -/
theorem sum_sum_sub_eq (g : ℤ → ℝ) (N : ℕ) :
    ∑ a ∈ Finset.range N, ∑ b ∈ Finset.range N, g ((b : ℤ) - a) =
      ∑ m ∈ Finset.range N, ((N : ℝ) - m) * (g m + g (-m)) - N * g 0 := by
  induction N with
  | zero => simp
  | succ N ih =>
    have h1 : ∀ a ∈ Finset.range (N+1), ∑ b ∈ Finset.range (N+1), g ((b : ℤ) - a) =
        ∑ b ∈ Finset.range N, g ((b : ℤ) - a) + g ((N : ℤ) - a) :=
      fun a _ => Finset.sum_range_succ _ _
    rw [Finset.sum_congr rfl h1, Finset.sum_add_distrib, Finset.sum_range_succ, ih,
      Finset.sum_range_succ (fun x => g ((N:ℤ) - x))]
    have h2 : ∑ x ∈ Finset.range N, g ((x : ℤ) - N) =
        ∑ m ∈ Finset.range N, g (-((m + 1 : ℕ) : ℤ)) := by
      rw [← Finset.sum_range_reflect]
      refine Finset.sum_congr rfl fun m hm => ?_
      simp at hm
      have e : (N - 1 - m : ℕ) + m + 1 = N := by omega
      have e' := congrArg (Nat.cast : ℕ → ℤ) e
      push_cast at e'
      congr 1; push_cast; linarith
    have h3 : ∑ x ∈ Finset.range N, g ((N : ℤ) - x) =
        ∑ m ∈ Finset.range N, g (((m + 1 : ℕ) : ℤ)) := by
      rw [← Finset.sum_range_reflect]
      refine Finset.sum_congr rfl fun m hm => ?_
      simp at hm
      have e : (N - 1 - m : ℕ) + m + 1 = N := by omega
      have e' := congrArg (Nat.cast : ℕ → ℤ) e
      push_cast at e'
      congr 1; push_cast; linarith
    rw [h2, h3]
    have h4 : ∑ m ∈ Finset.range (N + 1), (((N + 1 : ℕ) : ℝ) - m) * (g m + g (-m)) =
        ∑ m ∈ Finset.range N, ((N : ℝ) - m) * (g m + g (-m)) +
          ∑ m ∈ Finset.range (N+1), (g m + g (-m)) := by
      rw [Finset.sum_range_succ, Finset.sum_range_succ (fun m => g m + g (-m))]
      have : ∑ x ∈ Finset.range N, (((N + 1 : ℕ) : ℝ) - x) * (g x + g (-x)) =
          ∑ x ∈ Finset.range N, ((N : ℝ) - x) * (g x + g (-x)) +
            ∑ x ∈ Finset.range N, (g x + g (-x)) := by
        rw [← Finset.sum_add_distrib]; refine Finset.sum_congr rfl fun x _ => ?_; push_cast; ring
      rw [this]; push_cast; ring
    rw [h4, Finset.sum_range_succ' (fun m => g m + g (-m))]
    simp only [Finset.sum_add_distrib, sub_self, Nat.cast_zero, neg_zero]
    push_cast
    ring

/-- **TRACE-008, equation (4).** -/
theorem gramMoment_formula {N : ℕ} (hN : 1 ≤ N) (x : Fin N → ℝ) :
    gramMoment x = ((1 + 2 / (N : ℝ) ^ 3 *
      ∑ m ∈ Finset.Ico 1 N, ((N : ℝ) - m) * ‖traceT x m‖ ^ 2 : ℝ) : ℂ) := by
  set g : ℤ → ℝ := fun m => ‖traceZ x m‖ ^ 2 with hg
  have hgneg : ∀ m, g (-m) = g m := by
    intro m; simp only [hg, traceZ_neg, Complex.norm_conj]
  have hg0 : g 0 = (N : ℝ) ^ 2 := by simp [hg, traceZ]
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  have hstep : gramMoment x =
      (((1 / (N : ℝ) ^ 3) * ∑ a : Fin N, ∑ b : Fin N, g ((b : ℤ) - a) : ℝ) : ℂ) := by
    rw [gramMoment, Matrix.trace, sq]
    simp only [Matrix.diag, Matrix.mul_apply, gramMatrix, Matrix.of_apply]
    push_cast
    rw [Finset.mul_sum, Finset.mul_sum]
    refine Finset.sum_congr rfl fun a _ => ?_
    rw [Finset.mul_sum, Finset.mul_sum]
    refine Finset.sum_congr rfl fun b _ => ?_
    have : traceZ x ((a : ℤ) - b) = (starRingEnd ℂ) (traceZ x ((b : ℤ) - a)) := by
      rw [← traceZ_neg]; ring_nf
    rw [this, hg]; simp only
    rw [Complex.ofReal_pow, ← Complex.mul_conj']
    field_simp
  rw [hstep]
  congr 1
  rw [Fin.sum_univ_eq_sum_range (fun a => ∑ b : Fin N, g ((b : ℤ) - a))]
  have hin : ∀ i ∈ Finset.range N, ∑ b : Fin N, g ((b : ℤ) - i) =
      ∑ b ∈ Finset.range N, g ((b : ℤ) - i) :=
    fun i _ => Fin.sum_univ_eq_sum_range (fun b => g ((b : ℤ) - i)) N
  rw [Finset.sum_congr rfl hin, sum_sum_sub_eq]
  simp only [hgneg]
  rw [Finset.range_eq_Ico, Finset.sum_eq_sum_Ico_succ_bot hN]
  have hT : ∀ m ∈ Finset.Ico 1 N, ((N : ℝ) - m) * (g m + g m) =
      2 * (((N : ℝ) - m) * ‖traceT x m‖ ^ 2) := by
    intro m _; rw [hg]; simp only [traceZ_natCast]; ring
  rw [Finset.sum_congr rfl hT, ← Finset.mul_sum]
  simp only [Nat.cast_zero, sub_zero, hg0]
  field_simp
  ring

theorem sum_range_sub_mul (N : ℕ) :
    ∑ m ∈ Finset.Ico 1 N, ((N : ℝ) - m) * m = N * ((N : ℝ) ^ 2 - 1) / 6 := by
  have h : ∀ N : ℕ, ∑ m ∈ Finset.range N, ((N : ℝ) - m) * m = N * ((N : ℝ) ^ 2 - 1) / 6 := by
    intro N
    induction N with
    | zero => simp
    | succ N ih =>
      rw [Finset.sum_range_succ]
      have : ∑ m ∈ Finset.range N, (((N + 1 : ℕ) : ℝ) - m) * m =
          ∑ m ∈ Finset.range N, ((N : ℝ) - m) * m + ∑ m ∈ Finset.range N, (m : ℝ) := by
        rw [← Finset.sum_add_distrib]; refine Finset.sum_congr rfl fun m _ => ?_; push_cast; ring
      have hid : ∀ n : ℕ, ∑ m ∈ Finset.range n, (m : ℝ) = n * ((n : ℝ) - 1) / 2 := by
        intro n
        induction n with
        | zero => simp
        | succ n ihn => rw [Finset.sum_range_succ, ihn]; push_cast; ring
      rw [this, ih, hid]
      push_cast; ring
  rcases Nat.eq_zero_or_pos N with h0 | hpos
  · subst h0; simp
  · rw [← h N, Finset.range_eq_Ico, Finset.sum_eq_sum_Ico_succ_bot hpos]; simp

/-- **TRACE-008, equation (5).** -/
theorem cueGramMoment_eq {N : ℕ} (hN : 1 ≤ N) :
    cueGramMoment N = 4 / 3 - 1 / (3 * (N : ℝ) ^ 2) := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  have hff : ∀ m ∈ Finset.Ico 1 N, ((N : ℝ) - m) * cueFormFactor N m = ((N : ℝ) - m) * m := by
    intro m hm
    simp only [Finset.mem_Ico] at hm
    simp [cueFormFactor, Nat.min_eq_left hm.2.le]
  rw [cueGramMoment, Finset.sum_congr rfl hff, sum_range_sub_mul]
  field_simp
  ring

/-- Two regular `n`-gons at relative angle `φ/n`: phases `i/n` and `i/n + φ/(2πn)`. -/
noncomputable def twoGon (n : ℕ) (φ : ℝ) : Fin (n + n) → ℝ :=
  Fin.addCases (fun i : Fin n => (i : ℝ) / n) (fun i : Fin n => (i : ℝ) / n + φ / (2 * π * n))

theorem traceT_twoGon {n : ℕ} (hn : 1 ≤ n) (φ : ℝ) (m : ℕ) :
    traceT (twoGon n φ) m =
      if n ∣ m then (n : ℂ) * (1 + Complex.exp (Complex.I * m * φ / n)) else 0 := by
  have hn0 : (n : ℂ) ≠ 0 := by exact_mod_cast (show n ≠ 0 by omega)
  have hfac : traceT (twoGon n φ) m =
      traceT (clockPhases n) m * (1 + Complex.exp (Complex.I * m * φ / n)) := by
    rw [traceT, Fin.sum_univ_add, traceT, mul_add, mul_one, Finset.sum_mul]
    congr 1
    · refine Finset.sum_congr rfl fun i _ => ?_
      simp [twoGon, clockPhases]
    · refine Finset.sum_congr rfl fun i _ => ?_
      simp only [twoGon, Fin.addCases_right, clockPhases]
      rw [← Complex.exp_add]
      congr 1
      have hpi : (π : ℂ) ≠ 0 := by exact_mod_cast Real.pi_ne_zero
      push_cast
      field_simp
  rw [hfac, traceT_clock hn]
  split_ifs <;> simp

theorem norm_traceT_twoGon_mul {n : ℕ} (hn : 1 ≤ n) (φ : ℝ) (k : ℕ) :
    ‖traceT (twoGon n φ) (n * k)‖ ^ 2 = 4 * (n : ℝ) ^ 2 * Real.cos (k * φ / 2) ^ 2 := by
  have hn0 : (n : ℂ) ≠ 0 := by exact_mod_cast (show n ≠ 0 by omega)
  simp only [traceT_twoGon hn, dvd_mul_right, ↓reduceIte]
  have harg : Complex.I * ((n * k : ℕ) : ℂ) * φ / n = ((k * φ : ℝ) : ℂ) * Complex.I := by
    push_cast; field_simp
  rw [harg, norm_mul, Complex.norm_natCast, mul_pow]
  have h1 : ‖1 + Complex.exp (((k * φ : ℝ) : ℂ) * Complex.I)‖ ^ 2 =
      2 + 2 * Real.cos (k * φ) := by
    rw [← Complex.normSq_eq_norm_sq, Complex.normSq_apply]
    simp only [Complex.add_re, Complex.one_re, Complex.exp_ofReal_mul_I_re, Complex.add_im,
      Complex.one_im, Complex.exp_ofReal_mul_I_im, zero_add]
    nlinarith [Real.sin_sq_add_cos_sq (k * φ)]
  rw [h1]
  have h2 : Real.cos (k * φ) = 2 * Real.cos (k * φ / 2) ^ 2 - 1 := by
    rw [← Real.cos_two_mul]; ring_nf
  rw [h2]; ring

/-- **TRACE-008, equation (7).** -/
theorem gramMoment_twoGon {n : ℕ} (hn : 1 ≤ n) (φ : ℝ) :
    gramMoment (twoGon n φ) = ((1 + Real.cos (φ / 2) ^ 2 : ℝ) : ℂ) := by
  rw [gramMoment_formula (by omega)]
  congr 1
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  rw [Finset.sum_eq_single n]
  · have := norm_traceT_twoGon_mul hn φ 1
    rw [mul_one] at this
    rw [this]
    push_cast
    field_simp
    ring
  · intro m hm hmn
    simp only [Finset.mem_Ico] at hm
    have hndvd : ¬ n ∣ m := by
      rintro ⟨c, rfl⟩
      rcases c with _ | _ | c
      · omega
      · exact hmn (by ring)
      · nlinarith
    simp [traceT_twoGon hn, hndvd]
  · intro h; exfalso; apply h; simp only [Finset.mem_Ico]; omega

/-- **TRACE-008, equation (3).**  For every `n ≥ 2` there is a relative angle
`φ ∈ (0, π)` for which the two-gon spectrum of size `N = 2n` has exactly the CUE
Gram value `4/3 - 1/(3N²)`. -/
theorem exists_twoGon_cue_gram {n : ℕ} (hn : 2 ≤ n) :
    ∃ φ : ℝ, 0 < φ ∧ φ < π ∧ gramMoment (twoGon n φ) = (cueGramMoment (n + n) : ℂ) := by
  set N : ℝ := ((n + n : ℕ) : ℝ) with hN
  have hN4 : (4 : ℝ) ≤ N := by
    rw [hN]; push_cast
    have : (2 : ℝ) ≤ n := by exact_mod_cast hn
    linarith
  set v : ℝ := 1 / 3 - 1 / (3 * N ^ 2) with hv
  have hv0 : 0 < v := by
    rw [hv]
    have : 1 / (3 * N ^ 2) < 1 / 3 := by
      apply one_div_lt_one_div_of_lt (by norm_num); nlinarith
    linarith
  have hv1 : v < 1 := by
    rw [hv]; have : 0 < 1 / (3 * N ^ 2) := by positivity
    linarith
  set c := Real.sqrt v with hc
  have hc0 : 0 < c := Real.sqrt_pos.2 hv0
  have hc1 : c < 1 := by rw [hc, Real.sqrt_lt' one_pos]; simpa using hv1
  refine ⟨2 * Real.arccos c, by linarith [Real.arccos_pos.2 hc1], ?_, ?_⟩
  · linarith [Real.arccos_lt_pi_div_two.2 hc0]
  · rw [gramMoment_twoGon (by omega), cueGramMoment_eq (by omega)]
    congr 1
    rw [show 2 * Real.arccos c / 2 = Real.arccos c by ring,
      Real.cos_arccos (by linarith) hc1.le, hc, Real.sq_sqrt hv0.le, hv]
    ring

/-- The non-CUE limit function `B_φ(s) = ∑_{k ≥ 1} e^{-sk} cos²(kφ/2)`. -/
noncomputable def twoClockB (φ s : ℝ) : ℝ :=
  ∑' k : ℕ, Real.exp (-s * (k + 1 : ℕ)) * Real.cos ((k + 1 : ℕ) * φ / 2) ^ 2

theorem twoClockB_hasSum (φ : ℝ) {s : ℝ} (hs : 0 < s) :
    HasSum (fun k : ℕ => Real.exp (-s * (k + 1 : ℕ)) * Real.cos ((k + 1 : ℕ) * φ / 2) ^ 2)
      ((Real.exp (-s) / (1 - Real.exp (-s)) +
        (Real.exp (-s) * Real.cos φ - Real.exp (-s) ^ 2) /
          (1 - 2 * Real.exp (-s) * Real.cos φ + Real.exp (-s) ^ 2)) / 2) := by
  set q := Real.exp (-s) with hq
  have hq0 : 0 ≤ q := (Real.exp_pos _).le
  have hq1 : q < 1 := exp_lt_one_of_neg' (by linarith)
  have hgeo : HasSum (fun k : ℕ => q ^ (k + 1)) (q / (1 - q)) := by
    have := (hasSum_geometric_of_lt_one hq0 hq1).mul_left q
    convert! this using 1
    · ext k; ring
  have hpo := poisson_hasSum hq0 hq1 φ
  have hden := poisson_denom_pos hq0 hq1 φ
  have hP : (poissonKernel q φ - 1) / 2 =
      (q * Real.cos φ - q ^ 2) / (1 - 2 * q * Real.cos φ + q ^ 2) := by
    have hden' := hden.ne'
    rw [poissonKernel, div_sub_one hden', div_div, div_eq_div_iff (by positivity) hden']; ring
  rw [hP] at hpo
  have := (hgeo.add hpo).div_const 2
  convert! this using 1
  ext k
  have hexp : Real.exp (-s * ((k + 1 : ℕ) : ℝ)) = q ^ (k + 1) := by
    rw [hq, ← Real.exp_nat_mul]; congr 1; ring
  have hcos : Real.cos (((k + 1 : ℕ) : ℝ) * φ / 2) ^ 2 =
      (1 + Real.cos (((k + 1 : ℕ) : ℝ) * φ)) / 2 := by
    rw [Real.cos_sq, show 2 * (((k + 1 : ℕ) : ℝ) * φ / 2) = ((k + 1 : ℕ) : ℝ) * φ by ring]
    ring
  rw [hexp, hcos]
  ring

/-- **TRACE-008, equation (10).** -/
theorem twoClockB_closed_form (φ : ℝ) {s : ℝ} (hs : 0 < s) :
    twoClockB φ s = (Real.exp (-s) / (1 - Real.exp (-s)) +
        (Real.exp (-s) * Real.cos φ - Real.exp (-s) ^ 2) /
          (1 - 2 * Real.exp (-s) * Real.cos φ + Real.exp (-s) ^ 2)) / 2 :=
  (twoClockB_hasSum φ hs).tsum_eq

/-- **TRACE-008, equation (8), exact form.**  For every `n ≥ 1` and `s > 0`
the Abel statistic of the two-gon spectrum equals `B_φ(s)`. -/
theorem abelL_twoGon {n : ℕ} (hn : 1 ≤ n) (φ : ℝ) {s : ℝ} (hs : 0 < s) :
    abelL (twoGon n φ) s = twoClockB φ s := by
  have hnpos : (0 : ℝ) < n := by exact_mod_cast hn
  have hinj : Function.Injective (fun k : ℕ => n * k + (n - 1)) := by
    intro a b h; simp only at h
    have : n * a = n * b := by omega
    exact Nat.eq_of_mul_eq_mul_left (by omega) this
  set C := (Real.exp (-s) / (1 - Real.exp (-s)) +
        (Real.exp (-s) * Real.cos φ - Real.exp (-s) ^ 2) /
          (1 - 2 * Real.exp (-s) * Real.cos φ + Real.exp (-s) ^ 2)) / 2 with hC
  have hsum : HasSum (fun m : ℕ => Real.exp (-2 * s * ((m + 1 : ℕ) : ℝ) / ((n + n : ℕ) : ℝ)) *
      ‖traceT (twoGon n φ) (m + 1)‖ ^ 2) ((((n + n : ℕ) : ℝ)) ^ 2 * C) := by
    rw [← hinj.hasSum_iff]
    · convert! (twoClockB_hasSum φ hs).mul_left ((((n + n : ℕ) : ℝ)) ^ 2) using 1
      ext k
      simp only [Function.comp]
      have hnat : n * k + (n - 1) + 1 = n * (k + 1) := by rw [Nat.mul_succ]; omega
      rw [hnat, norm_traceT_twoGon_mul hn]
      have hcast : ((n * (k + 1) : ℕ) : ℝ) = n * ((k + 1 : ℕ) : ℝ) := by push_cast; ring
      rw [hcast]
      have he : -2 * s * ((n : ℝ) * ((k + 1 : ℕ) : ℝ)) / ((n + n : ℕ) : ℝ) =
          -s * ((k + 1 : ℕ) : ℝ) := by push_cast; field_simp; ring
      rw [he]
      push_cast
      ring
    · intro m hm
      have hndvd : ¬ n ∣ m + 1 := by
        rintro ⟨c, hc⟩
        cases c with
        | zero => simp at hc
        | succ c =>
          rw [Nat.mul_succ] at hc
          exact hm ⟨c, by simp only; omega⟩
      rw [traceT_twoGon hn]; simp [hndvd]
  rw [abelL, hsum.tsum_eq, twoClockB_closed_form φ hs, ← hC]
  have : (0 : ℝ) < ((n + n : ℕ) : ℝ) := by push_cast; linarith
  field_simp

theorem twoClockB_le (φ : ℝ) {s : ℝ} (hs : 0 < s) :
    twoClockB φ s ≤ Real.exp (-s) / (1 - Real.exp (-s)) := by
  set q := Real.exp (-s) with hq
  have hq0 : 0 ≤ q := (Real.exp_pos _).le
  have hq1 : q < 1 := exp_lt_one_of_neg' (by linarith)
  have hgeo : HasSum (fun k : ℕ => q ^ (k + 1)) (q / (1 - q)) := by
    have := (hasSum_geometric_of_lt_one hq0 hq1).mul_left q
    convert! this using 1
    · ext k; ring
  rw [twoClockB]
  refine hasSum_le (fun k => ?_) (twoClockB_hasSum φ hs).summable.hasSum hgeo
  have hexp : Real.exp (-s * ((k + 1 : ℕ) : ℝ)) = q ^ (k + 1) := by
    rw [hq, ← Real.exp_nat_mul]; congr 1; ring
  rw [hexp]
  have hc : Real.cos (((k + 1 : ℕ) : ℝ) * φ / 2) ^ 2 ≤ 1 := by
    rw [sq_le_one_iff_abs_le_one]; exact Real.abs_cos_le_one _
  have : 0 ≤ q ^ (k + 1) := pow_nonneg hq0 _
  nlinarith

/-- `B_φ` is not the CUE pair target `(1 - e^{-2s})/(4s²)`: they differ at `s = 8`. -/
theorem twoClockB_ne_cue (φ : ℝ) :
    twoClockB φ 8 < (1 - Real.exp (-2 * 8)) / (4 * 8 ^ 2) := by
  have hB := twoClockB_le φ (show (0 : ℝ) < 8 by norm_num)
  set q := Real.exp (-8) with hq
  have hq0 : 0 < q := Real.exp_pos _
  have he8 : (2800 : ℝ) ≤ Real.exp 8 := by
    have h1 := Real.exp_one_gt_d9
    have : Real.exp 8 = Real.exp 1 ^ 8 := by rw [← Real.exp_nat_mul]; norm_num
    rw [this]
    have h27 : (2.7 : ℝ) ≤ Real.exp 1 := by linarith
    calc (2800 : ℝ) ≤ 2.7 ^ 8 := by norm_num
      _ ≤ Real.exp 1 ^ 8 := pow_le_pow_left₀ (by norm_num) h27 8
  have hqle : q ≤ 1 / 2800 := by
    rw [hq, Real.exp_neg]
    rw [inv_eq_one_div]
    exact one_div_le_one_div_of_le (by norm_num) he8
  have hq2 : Real.exp (-2 * 8) = q ^ 2 := by
    rw [hq, ← Real.exp_nat_mul]; norm_num
  rw [hq2]
  have h1 : q / (1 - q) ≤ 1 / 2799 := by
    rw [div_le_div_iff₀ (by linarith) (by norm_num)]; linarith
  have h2 : (1 : ℝ) / 257 < (1 - q ^ 2) / (4 * 8 ^ 2) := by
    rw [div_lt_div_iff₀ (by norm_num) (by norm_num)]; nlinarith
  linarith

#print axioms traceZ_natCast
#print axioms traceZ_neg
#print axioms sum_sum_sub_eq
#print axioms gramMoment_formula
#print axioms sum_range_sub_mul
#print axioms cueGramMoment_eq
#print axioms traceT_twoGon
#print axioms norm_traceT_twoGon_mul
#print axioms gramMoment_twoGon
#print axioms exists_twoGon_cue_gram
#print axioms twoClockB_hasSum
#print axioms twoClockB_closed_form
#print axioms abelL_twoGon
#print axioms twoClockB_le
#print axioms twoClockB_ne_cue
end Bgs.Mathlib
