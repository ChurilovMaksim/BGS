module
public import Mathlib
@[expose] public section

/-!
# The CSE form-factor curve: the harmonic-sum domination (BGS-TRACE-070)

Source: `mathematics/trace-bridge/form_factor_curve.md`, inequalities (3) and (4).

* `midpoint_le_log`: the midpoint bound `1/(j + 1/2) ≤ log(j+1) - log j` for `j ≥ 1`.
* **(3)** `harmonic_half_sum_le`: for `0 ≤ d < N`,
  `∑_{j=d}^{N-1} (j + 1/2)⁻¹ ≤ 2 + log (N/(d+1))`.
* **(4), index step** `ceil_index_bound`: with `n = ⌈N τ⌉` and `d = |N - n|`,
  `d + 1 ≥ N |τ - 1|`.
* `harmonic_half_sum_le_log_dist`: combining both, for `n = ⌈Nτ⌉ < N` the finite sum is
  dominated by `2 + log (1/|τ - 1|)`, the integrable majorant of (4).
-/

open Finset Real

namespace Bgs.Mathlib

/-- Midpoint bound: `1/(j + 1/2) ≤ ∫_j^{j+1} dx/x = log(j+1) - log j` for `j ≥ 1`. -/
theorem midpoint_le_log {j : ℕ} (hj : 1 ≤ j) :
    1 / ((j : ℝ) + 1 / 2) ≤ log ((j : ℝ) + 1) - log j := by
  have hj0 : (0 : ℝ) < j := by exact_mod_cast hj
  have h := Real.le_log_one_add_of_nonneg (x := 1 / (j : ℝ)) (by positivity)
  have e1 : 2 * (1 / (j : ℝ)) / (1 / j + 2) = 1 / ((j : ℝ) + 1 / 2) := by
    field_simp; ring
  have e2 : log (1 + 1 / (j : ℝ)) = log ((j : ℝ) + 1) - log j := by
    rw [← Real.log_div (by positivity) hj0.ne']
    congr 1; field_simp
  rwa [e1, e2] at h

/-- Telescoping the midpoint bound: `∑_{j=a}^{N-1} (j+1/2)⁻¹ ≤ log N - log a` for `1 ≤ a ≤ N`. -/
theorem harmonic_half_sum_le_log_ratio {a N : ℕ} (ha : 1 ≤ a) (haN : a ≤ N) :
    ∑ j ∈ Ico a N, 1 / ((j : ℝ) + 1 / 2) ≤ log N - log a := by
  induction N, haN using Nat.le_induction with
  | base => simp
  | succ N hN ih =>
    rw [Finset.sum_Ico_succ_top hN]
    have := midpoint_le_log (j := N) (le_trans ha hN)
    push_cast
    linarith

/-- **(3).**  For `0 ≤ d < N`: `∑_{j=d}^{N-1} (j + 1/2)⁻¹ ≤ 2 + log (N/(d+1))`. -/
theorem harmonic_half_sum_le {d N : ℕ} (hdN : d < N) :
    ∑ j ∈ Ico d N, 1 / ((j : ℝ) + 1 / 2) ≤ 2 + log ((N : ℝ) / (d + 1)) := by
  have hN0 : (0 : ℝ) < N := by exact_mod_cast (lt_of_le_of_lt (Nat.zero_le d) hdN)
  rcases Nat.eq_zero_or_pos d with rfl | hd
  · rw [Finset.sum_eq_sum_Ico_succ_bot hdN]
    have := harmonic_half_sum_le_log_ratio (a := 1) (N := N) le_rfl (by omega)
    simp only [Nat.cast_zero, zero_add, Nat.cast_one, log_one, sub_zero] at this ⊢
    rw [div_one]
    norm_num at this ⊢
    linarith
  · have hd0 : (0 : ℝ) < d := by exact_mod_cast hd
    have h1 := harmonic_half_sum_le_log_ratio (a := d) (N := N) hd hdN.le
    have h2 : log ((N : ℝ) / (d + 1)) = log N - log ((d : ℝ) + 1) :=
      Real.log_div hN0.ne' (by positivity)
    have h3 : log ((d : ℝ) + 1) - log d ≤ 2 := by
      rw [← Real.log_div (by positivity) hd0.ne']
      have hle : ((d : ℝ) + 1) / d ≤ 2 := by
        rw [div_le_iff₀ hd0]
        have : (1 : ℝ) ≤ d := by exact_mod_cast hd
        linarith
      have := Real.log_le_sub_one_of_pos (x := ((d : ℝ) + 1) / d) (by positivity)
      linarith
    rw [h2]
    linarith

/-- **(4), index step.**  With `n = ⌈N τ⌉` (`N > 0`) one has `|N - n| + 1 ≥ N |τ - 1|`. -/
theorem ceil_index_bound (N : ℕ) (τ : ℝ) :
    (N : ℝ) * |τ - 1| ≤ |(N : ℝ) - ⌈(N : ℝ) * τ⌉| + 1 := by
  have h1 : (N : ℝ) * τ ≤ ⌈(N : ℝ) * τ⌉ := Int.le_ceil _
  have h2 : (⌈(N : ℝ) * τ⌉ : ℝ) < N * τ + 1 := Int.ceil_lt_add_one _
  have hN : (0 : ℝ) ≤ N := Nat.cast_nonneg N
  rw [← abs_of_nonneg hN, ← abs_mul, abs_of_nonneg hN]
  calc |(N : ℝ) * (τ - 1)| = |((N : ℝ) * τ - ⌈(N : ℝ) * τ⌉) + (⌈(N : ℝ) * τ⌉ - N)| := by
        congr 1; ring
    _ ≤ |(N : ℝ) * τ - ⌈(N : ℝ) * τ⌉| + |(⌈(N : ℝ) * τ⌉ : ℝ) - N| := abs_add_le _ _
    _ ≤ 1 + |(N : ℝ) - ⌈(N : ℝ) * τ⌉| :=
        add_le_add (by rw [abs_le]; constructor <;> linarith) (le_of_eq (abs_sub_comm _ _))
    _ = _ := by ring

/-- **(4), domination below the singularity.**  If `n = ⌈Nτ⌉` satisfies `1 ≤ n < N` and
`τ ≠ 1`, then with `d = N - n` the finite harmonic sum is bounded by `2 + log (1/|τ - 1|)`. -/
theorem harmonic_half_sum_le_log_dist {N n : ℕ} {τ : ℝ}
    (hn : (n : ℤ) = ⌈(N : ℝ) * τ⌉) (hn1 : 1 ≤ n) (hnN : n < N) (hτ : τ ≠ 1) :
    ∑ j ∈ Ico (N - n) N, 1 / ((j : ℝ) + 1 / 2) ≤ 2 + log (1 / |τ - 1|) := by
  have hd : N - n < N := by omega
  have h3 := harmonic_half_sum_le hd
  have hidx := ceil_index_bound N τ
  rw [← hn] at hidx
  have hcast : ((N - n : ℕ) : ℝ) = |(N : ℝ) - ((n : ℤ) : ℝ)| := by
    push_cast [Nat.cast_sub hnN.le]
    rw [abs_of_nonneg (by have : (n : ℝ) < N := by exact_mod_cast hnN
                          linarith)]
  have hτ' : 0 < |τ - 1| := abs_pos.mpr (sub_ne_zero.mpr hτ)
  have hN0 : (0 : ℝ) < N := by exact_mod_cast (lt_of_le_of_lt (Nat.zero_le _) hnN)
  have hmono : (N : ℝ) / (((N - n : ℕ) : ℝ) + 1) ≤ 1 / |τ - 1| := by
    rw [div_le_div_iff₀ (by positivity) hτ', hcast]
    linarith
  have := Real.log_le_log (by positivity) hmono
  linarith

#print axioms midpoint_le_log
#print axioms harmonic_half_sum_le_log_ratio
#print axioms harmonic_half_sum_le
#print axioms ceil_index_bound
#print axioms harmonic_half_sum_le_log_dist
end Bgs.Mathlib
