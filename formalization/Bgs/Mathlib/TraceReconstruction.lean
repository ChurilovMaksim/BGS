module
public import Bgs.Mathlib.AbelPoisson
@[expose] public section

/-!
# Short traces do not determine the microscopic pair statistic (BGS-TRACE-001/002, §4)

Source: `mathematics/trace-bridge/trace_to_local_statistics_bridge.md`, §4,
"A concrete failure of reconstruction from short traces".

Let `N = 2M`.  Compare the spectrum `A` of all `N`-th roots of unity (each once) with the
spectrum `B` of all `M`-th roots of unity, each taken twice.  Then

* all traces agree in the linear window: `T_A(n) = T_B(n) = 0` for `1 ≤ n < M`
  (`clock_trace_window`, `doubled_trace_window`);
* for every test `φ` supported in `(-1/2, 1/2)` with `φ(0) = 1`, the factorial pair statistic
  `C_{2,N}(U; φ) = N⁻¹ ∑_{j ≠ k} ∑_{n ∈ ℤ} φ(N(θ_j - θ_k + n))` equals `0` for `A`
  and `1` for `B` (`pairStat_clock`, `pairStat_doubled`).

Hence exact agreement of all traces throughout a window of length `≍ N` does not determine
the microscopic pair statistic (`short_traces_do_not_determine_pair_statistic`).
-/

open Real Complex BigOperators Finset

namespace Bgs.Mathlib

/-- The factorial pair statistic `C_{2,N}(U;φ) = N⁻¹ ∑_{j≠k} Φ_N(θ_j - θ_k)` with the
`N`-scale periodization `Φ_N(t) = ∑_{n∈ℤ} φ(N(t+n))`. -/
noncomputable def pairStat {N : ℕ} (θ : Fin N → ℝ) (φ : ℝ → ℝ) : ℝ :=
  (1 / (N : ℝ)) * ∑ j, ∑ k ∈ univ.erase j, ∑' n : ℤ, φ (N * (θ j - θ k + n))

/-- The doubled spectrum: every `M`-th root of unity taken twice, `θ_j = (j mod M)/M`. -/
noncomputable def doubledPhases (M : ℕ) : Fin (2 * M) → ℝ := fun j => ((j : ℕ) % M : ℕ) / M

/-- A test supported in `(-1/2,1/2)` vanishes at nonzero integers. -/
lemma test_int_eq_zero {φ : ℝ → ℝ} (hsupp : ∀ t, φ t ≠ 0 → |t| < 1 / 2) {m : ℤ} (hm : m ≠ 0) :
    φ (m : ℝ) = 0 := by
  by_contra h
  have h1 := hsupp _ h
  have h2 : (1 : ℝ) ≤ |(m : ℝ)| := by
    rw [← Int.cast_abs]; exact_mod_cast Int.one_le_abs hm
  linarith

/-- Periodized sum at integer points avoiding `0`. -/
lemma tsum_test_eq_zero {φ : ℝ → ℝ} (hsupp : ∀ t, φ t ≠ 0 → |t| < 1 / 2) (f : ℤ → ℤ)
    (hf : ∀ n, f n ≠ 0) : ∑' n : ℤ, φ (f n : ℝ) = 0 := by
  have : (fun n : ℤ => φ (f n : ℝ)) = fun _ => 0 := funext fun n => test_int_eq_zero hsupp (hf n)
  rw [this, tsum_zero]

/-- Periodized sum at the points `N n`, `N ≥ 1`: only `n = 0` contributes. -/
lemma tsum_test_lattice {φ : ℝ → ℝ} (hsupp : ∀ t, φ t ≠ 0 → |t| < 1 / 2) {N : ℤ} (hN : N ≠ 0) :
    ∑' n : ℤ, φ ((N * n : ℤ) : ℝ) = φ 0 := by
  rw [tsum_eq_single 0]
  · simp
  · intro n hn
    exact test_int_eq_zero hsupp (mul_ne_zero hN hn)

lemma clock_trace_window {M : ℕ} (hM : 1 ≤ M) {n : ℕ} (hn1 : 1 ≤ n) (hn : n < M) :
    traceT (clockPhases (2 * M)) n = 0 := by
  rw [traceT_clock (by omega) n, if_neg]
  intro h
  have := Nat.le_of_dvd (by omega) h
  omega

lemma doubled_trace_window {M : ℕ} (hM : 1 ≤ M) {n : ℕ} (hn1 : 1 ≤ n) (hn : n < M) :
    traceT (doubledPhases M) n = 0 := by
  set g : ℕ → ℂ := fun i => Complex.exp (2 * π * Complex.I * n * (((i % M : ℕ) : ℝ) / M : ℝ))
    with hg
  have h1 : traceT (doubledPhases M) n = ∑ i ∈ range (2 * M), g i := by
    rw [traceT, ← Fin.sum_univ_eq_sum_range g]
    rfl
  have h2 : ∑ i ∈ range (2 * M), g i = 2 * traceT (clockPhases M) n := by
    rw [two_mul, Finset.sum_range_add, traceT]
    simp only [clockPhases]
    rw [Fin.sum_univ_eq_sum_range
      (fun i => Complex.exp (2 * π * Complex.I * n * ((i : ℝ) / M : ℝ)))]
    have e1 : ∀ i ∈ range M, g i = Complex.exp (2 * π * Complex.I * n * ((i : ℝ) / M : ℝ)) := by
      intro i hi
      rw [hg]; simp only
      rw [Nat.mod_eq_of_lt (Finset.mem_range.1 hi)]
    have e2 : ∀ i ∈ range M, g (M + i) =
        Complex.exp (2 * π * Complex.I * n * ((i : ℝ) / M : ℝ)) := by
      intro i hi
      rw [hg]; simp only
      rw [Nat.add_mod_left, Nat.mod_eq_of_lt (Finset.mem_range.1 hi)]
    rw [Finset.sum_congr rfl e1, Finset.sum_congr rfl e2]
    ring
  rw [h1, h2, traceT_clock hM n, if_neg (fun h => absurd (Nat.le_of_dvd (by omega) h)
    (by omega)), mul_zero]

lemma pairStat_clock {M : ℕ} (hM : 1 ≤ M) {φ : ℝ → ℝ} (hsupp : ∀ t, φ t ≠ 0 → |t| < 1 / 2) :
    pairStat (clockPhases (2 * M)) φ = 0 := by
  have hNpos : (0 : ℝ) < ((2 * M : ℕ) : ℝ) := by exact_mod_cast (by omega : 0 < 2 * M)
  rw [pairStat]
  convert mul_zero _ using 2
  refine Finset.sum_eq_zero fun j _ => Finset.sum_eq_zero fun k hk => ?_
  have hjk : j ≠ k := (Finset.ne_of_mem_erase hk).symm
  have e : ∀ n : ℤ, ((2 * M : ℕ) : ℝ) * (clockPhases (2 * M) j - clockPhases (2 * M) k + n) =
      (((j : ℕ) - (k : ℕ) + (2 * M : ℕ) * n : ℤ) : ℝ) := by
    intro n
    simp only [clockPhases]
    push_cast
    field_simp
  simp_rw [e]
  apply tsum_test_eq_zero hsupp
  intro n h
  have hj := j.isLt; have hk := k.isLt
  have hne : (j : ℕ) ≠ (k : ℕ) := fun h => hjk (Fin.ext h)
  rcases lt_trichotomy n 0 with hn | rfl | hn
  · have : ((2 * M : ℕ) : ℤ) * n ≤ -((2 * M : ℕ) : ℤ) := by nlinarith
    push_cast at this h; omega
  · simp at h; omega
  · have : ((2 * M : ℕ) : ℤ) ≤ ((2 * M : ℕ) : ℤ) * n := by nlinarith
    push_cast at this h; omega

lemma pairStat_doubled {M : ℕ} (hM : 1 ≤ M) {φ : ℝ → ℝ} (hsupp : ∀ t, φ t ≠ 0 → |t| < 1 / 2)
    (h0 : φ 0 = 1) : pairStat (doubledPhases M) φ = 1 := by
  have hNpos : (0 : ℝ) < ((2 * M : ℕ) : ℝ) := by exact_mod_cast (by omega : 0 < 2 * M)
  have hterm : ∀ j k : Fin (2 * M), ∑' n : ℤ,
      φ (((2 * M : ℕ) : ℝ) * (doubledPhases M j - doubledPhases M k + n)) =
      if (j : ℕ) % M = (k : ℕ) % M then 1 else 0 := by
    intro j k
    have e : ∀ n : ℤ, ((2 * M : ℕ) : ℝ) * (doubledPhases M j - doubledPhases M k + n) =
        ((2 * (((j : ℕ) % M : ℕ) : ℤ) - 2 * (((k : ℕ) % M : ℕ) : ℤ) + (2 * M : ℕ) * n : ℤ) : ℝ) := by
      intro n
      have hM0 : (M : ℝ) ≠ 0 := by exact_mod_cast (by omega : M ≠ 0)
      simp only [doubledPhases, Int.cast_add, Int.cast_sub, Int.cast_mul, Int.cast_ofNat,
        Int.cast_natCast, Nat.cast_mul, Nat.cast_ofNat]
      field_simp
    simp_rw [e]
    split_ifs with hjk
    · rw [hjk]
      simp only [sub_self, zero_add]
      rw [tsum_test_lattice hsupp (by exact_mod_cast (by omega : 2 * M ≠ 0)), h0]
    · apply tsum_test_eq_zero hsupp
      intro n h
      have ha := Nat.mod_lt (j : ℕ) (by omega : 0 < M)
      have hb := Nat.mod_lt (k : ℕ) (by omega : 0 < M)
      rcases lt_trichotomy n 0 with hn | rfl | hn
      · have : ((2 * M : ℕ) : ℤ) * n ≤ -((2 * M : ℕ) : ℤ) := by nlinarith
        push_cast at this h; omega
      · simp at h; omega
      · have : ((2 * M : ℕ) : ℤ) ≤ ((2 * M : ℕ) : ℤ) * n := by nlinarith
        push_cast at this h; omega
  have hcount : ∀ j : Fin (2 * M), ∑ k ∈ univ.erase j,
      (if (j : ℕ) % M = (k : ℕ) % M then (1 : ℝ) else 0) = 1 := by
    intro j
    have hj := j.isLt
    set p : Fin (2 * M) := ⟨if (j : ℕ) < M then (j : ℕ) + M else (j : ℕ) - M, by split_ifs <;> omega⟩
      with hp
    have hpj : p ≠ j := by
      intro h; have := congrArg Fin.val h; simp only [hp] at this; split_ifs at this <;> omega
    rw [Finset.sum_eq_single p]
    · rw [if_pos]
      simp only [hp]
      split_ifs with h
      · rw [Nat.add_mod_right]
      · conv_lhs => rw [show (j : ℕ) = ((j : ℕ) - M) + M by omega, Nat.add_mod_right]
    · intro k hk hkp
      rw [if_neg]
      intro hmod
      apply hkp
      have hkj : k ≠ j := Finset.ne_of_mem_erase hk
      have hk' := k.isLt
      apply Fin.ext
      simp only [hp]
      have hkj' : (k : ℕ) ≠ (j : ℕ) := fun h => hkj (Fin.ext h)
      split_ifs with h
      · have h1 : (j : ℕ) % M = (j : ℕ) := Nat.mod_eq_of_lt h
        by_cases hkM : (k : ℕ) < M
        · rw [Nat.mod_eq_of_lt hkM] at hmod; omega
        · have : (k : ℕ) % M = (k : ℕ) - M := by
            rw [Nat.mod_eq_sub_mod (by omega), Nat.mod_eq_of_lt (by omega)]
          omega
      · have h1 : (j : ℕ) % M = (j : ℕ) - M := by
          rw [Nat.mod_eq_sub_mod (by omega), Nat.mod_eq_of_lt (by omega)]
        by_cases hkM : (k : ℕ) < M
        · rw [Nat.mod_eq_of_lt hkM] at hmod; omega
        · have : (k : ℕ) % M = (k : ℕ) - M := by
            rw [Nat.mod_eq_sub_mod (by omega), Nat.mod_eq_of_lt (by omega)]
          omega
    · intro h; exact absurd (Finset.mem_erase.2 ⟨hpj, Finset.mem_univ p⟩) h
  rw [pairStat]
  simp_rw [hterm, hcount]
  simp only [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul, mul_one]
  field_simp

/-- **Failure of reconstruction from short traces.**  For `N = 2M`, the `N`-clock and the doubled
`M`-clock have identical traces `T(n) = 0` for `1 ≤ n < M` (and `T(0) = N`), yet for every test
`φ` supported in `(-1/2,1/2)` with `φ(0) = 1` their pair statistics are `0` and `1`. -/
theorem short_traces_do_not_determine_pair_statistic {M : ℕ} (hM : 1 ≤ M) {φ : ℝ → ℝ}
    (hsupp : ∀ t, φ t ≠ 0 → |t| < 1 / 2) (h0 : φ 0 = 1) :
    (∀ n : ℕ, n < M → traceT (clockPhases (2 * M)) n = traceT (doubledPhases M) n) ∧
      pairStat (clockPhases (2 * M)) φ = 0 ∧ pairStat (doubledPhases M) φ = 1 := by
  refine ⟨fun n hn => ?_, pairStat_clock hM hsupp, pairStat_doubled hM hsupp h0⟩
  rcases Nat.eq_zero_or_pos n with rfl | hn1
  · simp [traceT]
  · rw [clock_trace_window hM hn1 hn, doubled_trace_window hM hn1 hn]

end Bgs.Mathlib
