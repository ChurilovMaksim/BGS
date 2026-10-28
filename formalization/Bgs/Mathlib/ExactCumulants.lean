module
public import Mathlib
public import Bgs.Mathlib.FormFactorCurve
@[expose] public section

/-!
# Exact fourth cumulants (BGS-TRACE-069)

Source: `mathematics/trace-bridge/exact_cumulants.md`.

Half-integer sums `hs f A L = ∑_{j<L} f(A + j + 1/2)` and their discrete antiderivative `hP`
(`hs_eq_hP`) give exact evaluations of all inverse-power sums over the active intervals
`R₁ = {k ∈ H_N : k - n ∈ H_N}`, `R₂ = {k ∈ H_N : k - 2n ∈ H_N}` (`H_N` = half-integers in
`(-N, N)`).

**CSE.** The five traces `T₁, T₂, T₃, T_{4b}, T_{4a}` are defined by their summands (2) (taken
from the document) and `cseKappa` by the grouping (1). Proved:
* partial fractions `cseT1_eval`, …, `cseT4a_eval`;
* **(3)** in all three ranges: `cseKappa_formula_short` (`1 ≤ n ≤ N`),
  `cseKappa_formula_middle` (`N ≤ n ≤ 2N`), `cseKappa_formula_plateau` (`n ≥ 2N`);
* **(4)** `cseKappa_diag`; the plateau already at `n = 2N - 1`: `cseKappa_two_mul_sub_one`;
* uniform bound `cseKappa_le`: `κ₂₂ ≤ N H₁(N)/8`;
* `hHarm_one_le_log`: `H₁(N) ≤ 2 + log(2N-1)`, and `cseM2_le` for the second moment (5)
  (the formula (5) itself is taken as the definition `cseM2`).

**CUE.** `cueKappa_grouping`, the exact variance **(7)** (`cueVar_short`, `cueVar_middle`,
`cueVar_long`), the bound `cueVar_le` (`≤ N² - N`) and the arithmetic form of **(8)**
(`cueVar_comparison`).

Not formalized: the Pfaffian/Toeplitz generating functions that produce (1), (2) and the CUE
trace values, the phase-contraction inequality used in (6)/(8), and (6) itself.
-/

open Finset

namespace Bgs.Mathlib

/-- `H_r(m) = ∑_{j<m} (j + 1/2)^{-r}`. -/
noncomputable def hHarm (r m : ℕ) : ℝ := ∑ j ∈ range m, (((j : ℝ) + 1 / 2)⁻¹) ^ r

/-- Sum of `f` over the `L` consecutive half-integers `A + 1/2, …, A + L - 1/2`. -/
noncomputable def hs (f : ℝ → ℝ) (A : ℤ) (L : ℕ) : ℝ :=
  ∑ j ∈ range L, f ((A : ℝ) + j + 1 / 2)

/-- Discrete antiderivative of `f` on half-integers, normalized at `0`. -/
noncomputable def hP (f : ℝ → ℝ) (c : ℤ) : ℝ :=
  if 0 ≤ c then ∑ j ∈ range c.toNat, f ((j : ℝ) + 1 / 2)
  else -∑ j ∈ range (-c).toNat, f (-((j : ℝ) + 1 / 2))

theorem hP_natCast (f : ℝ → ℝ) (m : ℕ) : hP f m = ∑ j ∈ range m, f ((j : ℝ) + 1 / 2) := by
  simp [hP]

theorem hP_neg_natCast (f : ℝ → ℝ) (m : ℕ) :
    hP f (-(m : ℤ)) = -∑ j ∈ range m, f (-((j : ℝ) + 1 / 2)) := by
  rcases Nat.eq_zero_or_pos m with rfl | hm
  · simp [hP]
  · have : ¬ (0 : ℤ) ≤ -(m : ℤ) := by omega
    simp only [hP, this, ↓reduceIte]
    simp

theorem hP_succ (f : ℝ → ℝ) (c : ℤ) : hP f (c + 1) = hP f c + f ((c : ℝ) + 1 / 2) := by
  obtain ⟨m, rfl | rfl⟩ := Int.eq_nat_or_neg c
  · have : (m : ℤ) + 1 = ((m + 1 : ℕ) : ℤ) := by push_cast; ring
    rw [this, hP_natCast, hP_natCast, sum_range_succ]
    push_cast; ring
  · cases m with
    | zero =>
      simp only [Nat.cast_zero, neg_zero, zero_add]
      rw [show (1 : ℤ) = ((1 : ℕ) : ℤ) by rfl, hP_natCast, show (0 : ℤ) = ((0 : ℕ) : ℤ) by rfl,
        hP_natCast]
      simp
    | succ m =>
      have : -((m + 1 : ℕ) : ℤ) + 1 = -(m : ℤ) := by push_cast; ring
      rw [this, hP_neg_natCast, hP_neg_natCast, sum_range_succ]
      push_cast
      ring_nf

theorem hs_eq_hP (f : ℝ → ℝ) (A : ℤ) (L : ℕ) : hs f A L = hP f (A + L) - hP f A := by
  induction L with
  | zero => simp [hs]
  | succ L ih =>
    rw [hs, sum_range_succ, ← hs, ih, Nat.cast_succ, ← add_assoc, hP_succ]
    push_cast; ring


/-- Half-integers are nonzero. -/
theorem halfInt_ne_zero (m : ℤ) : (m : ℝ) + 1 / 2 ≠ 0 := by
  intro h
  have h2 : ((2 * m + 1 : ℤ) : ℝ) = 0 := by push_cast; linarith
  have : (2 * m + 1 : ℤ) = 0 := by exact_mod_cast h2
  omega

theorem hs_point_ne_zero (A c : ℤ) (j : ℕ) : (A : ℝ) + j + 1 / 2 - c ≠ 0 := by
  have := halfInt_ne_zero (A + j - c)
  push_cast at this
  convert this using 1; ring

theorem hs_point_ne_zero' (A : ℤ) (j : ℕ) : (A : ℝ) + j + 1 / 2 ≠ 0 := by
  simpa using hs_point_ne_zero A 0 j

/-- Antiderivative of `1/x`: `hP (·⁻¹) c = H_1(|c|)`. -/
theorem hP_inv (c : ℤ) : hP (fun x => x⁻¹) c = hHarm 1 c.natAbs := by
  obtain ⟨m, rfl | rfl⟩ := Int.eq_nat_or_neg c
  · rw [hP_natCast]; simp [hHarm]
  · rw [hP_neg_natCast, hHarm, ← sum_neg_distrib, Int.natAbs_neg, Int.natAbs_natCast]
    refine sum_congr rfl fun j _ => ?_
    rw [pow_one, inv_neg, neg_neg]

/-- Antiderivative of `1/x²`: `hP (·⁻²) c = sign(c) H_2(|c|)`. -/
theorem hP_invSq (c : ℤ) :
    hP (fun x => (x⁻¹) ^ 2) c = if 0 ≤ c then hHarm 2 c.natAbs else -hHarm 2 c.natAbs := by
  obtain ⟨m, rfl | rfl⟩ := Int.eq_nat_or_neg c
  · rw [hP_natCast]; simp [hHarm]
  · rcases Nat.eq_zero_or_pos m with rfl | hm
    · simp [hP, hHarm]
    · have : ¬ (0 : ℤ) ≤ -(m : ℤ) := by omega
      rw [hP_neg_natCast, hHarm, Int.natAbs_neg, Int.natAbs_natCast]; simp only [this, ↓reduceIte]
      congr 1; refine sum_congr rfl fun j _ => ?_
      rw [inv_neg, neg_sq]


theorem hs_eq_hP' (f : ℝ → ℝ) (A B : ℤ) (L : ℕ) (h : A + L = B) :
    hs f A L = hP f B - hP f A := by
  rw [hs_eq_hP, h]

/-! ## The five CSE traces, summand form (2) -/

/-- Left end `A₁ = n - N` and length `2N - n` of `R₁ = {k ∈ H_N : k - n ∈ H_N}`. -/
abbrev rA1 (N n : ℕ) : ℤ := (n : ℤ) - N
abbrev rL1 (N n : ℕ) : ℕ := 2 * N - n
/-- Left end `A₂ = 2n - N` and length `2N - 2n` of `R₂ = {k ∈ H_N : k - 2n ∈ H_N}`. -/
abbrev rA2 (N n : ℕ) : ℤ := 2 * (n : ℤ) - N
abbrev rL2 (N n : ℕ) : ℕ := 2 * N - 2 * n

noncomputable def cseT1 (N n : ℕ) : ℝ :=
  hs (fun k => 1 + (n : ℝ) ^ 2 / (4 * k * (k - n))) (rA1 N n) (rL1 N n)
noncomputable def cseT2 (N n : ℕ) : ℝ :=
  hs (fun k => 1 + (n : ℝ) ^ 2 / (k * (k - 2 * n))) (rA2 N n) (rL2 N n)
noncomputable def cseT3 (N n : ℕ) : ℝ :=
  hs (fun k => 1 + 3 * (n : ℝ) ^ 2 / (4 * k * (k - 2 * n))) (rA2 N n) (rL2 N n)
noncomputable def cseT4b (N n : ℕ) : ℝ :=
  hs (fun k => 1 + 9 * (n : ℝ) ^ 2 / (16 * k * (k - 2 * n)) - (n : ℝ) ^ 2 / (16 * (k - n) ^ 2))
    (rA2 N n) (rL2 N n)
noncomputable def cseT4a (N n : ℕ) : ℝ :=
  hs (fun k => 1 + 3 * (n : ℝ) ^ 2 / (8 * k * (k - n))
      + (n : ℝ) ^ 2 / 16 * (1 / k ^ 2 + 1 / (k - n) ^ 2)) (rA1 N n) (rL1 N n)

/-- The CSE connected fourth cumulant, grouping (1). -/
noncomputable def cseKappa (N n : ℕ) : ℝ :=
  -(N : ℝ) + 2 * cseT1 N n - cseT2 N n / 2 + 2 * cseT3 N n - 2 * cseT4b N n - cseT4a N n

local notation "Iv" => fun x : ℝ => x⁻¹
local notation "Qv" => fun x : ℝ => (x⁻¹) ^ 2

theorem hs_point_ne_sub_nat (A : ℤ) (a n j : ℕ) : (A : ℝ) + j + 1 / 2 - a * n ≠ 0 := by
  have := hs_point_ne_zero A (a * n) j
  push_cast at this
  exact this

theorem hs_point_shift (A : ℤ) (a n j : ℕ) :
    (((A - a * n : ℤ)) : ℝ) + j + 1 / 2 = (A : ℝ) + j + 1 / 2 - a * n := by
  push_cast; ring

theorem cseT1_eval (N n : ℕ) (hn : 1 ≤ n) :
    cseT1 N n = rL1 N n + (n / 4 : ℝ) *
      (hs Iv (rA1 N n - n) (rL1 N n) - hs Iv (rA1 N n) (rL1 N n)) := by
  have hn0 : (n : ℝ) ≠ 0 := by positivity
  simp only [cseT1, hs, ← sum_sub_distrib, mul_sum]
  rw [show ((rL1 N n : ℕ) : ℝ) = ∑ _j ∈ range (rL1 N n), (1 : ℝ) by simp, ← sum_add_distrib]
  refine sum_congr rfl fun j _ => ?_
  have h1 := hs_point_ne_zero' (rA1 N n) j
  have h2 := hs_point_ne_zero (rA1 N n) n j
  rw [Int.cast_natCast] at h2
  have e : (((rA1 N n - n : ℤ)) : ℝ) + j + 1 / 2 = ((rA1 N n : ℤ) : ℝ) + j + 1 / 2 - n := by
    push_cast; ring
  rw [e]
  generalize ((rA1 N n : ℤ) : ℝ) + j + 1 / 2 = k at *
  field_simp
  ring


theorem cseT2_eval (N n : ℕ) (hn : 1 ≤ n) :
    cseT2 N n = rL2 N n + (n / 2 : ℝ) *
      (hs Iv (rA2 N n - 2 * n) (rL2 N n) - hs Iv (rA2 N n) (rL2 N n)) := by
  have hn0 : (n : ℝ) ≠ 0 := by positivity
  simp only [cseT2, hs, ← sum_sub_distrib, mul_sum]
  rw [show ((rL2 N n : ℕ) : ℝ) = ∑ _j ∈ range (rL2 N n), (1 : ℝ) by simp, ← sum_add_distrib]
  refine sum_congr rfl fun j _ => ?_
  have h1 := hs_point_ne_zero' (rA2 N n) j
  have h2 := hs_point_ne_sub_nat (rA2 N n) 2 n j
  rw [show (rA2 N n - 2 * n : ℤ) = rA2 N n - ((2 : ℕ) : ℤ) * n by norm_num, hs_point_shift]
  simp only [Nat.cast_ofNat] at h2 ⊢
  generalize ((rA2 N n : ℤ) : ℝ) + j + 1 / 2 = k at *
  have h2' : k - (n : ℝ) * 2 ≠ 0 := by rwa [mul_comm]
  field_simp
  ring

theorem cseT3_eval (N n : ℕ) (hn : 1 ≤ n) :
    cseT3 N n = rL2 N n + (3 * n / 8 : ℝ) *
      (hs Iv (rA2 N n - 2 * n) (rL2 N n) - hs Iv (rA2 N n) (rL2 N n)) := by
  have hn0 : (n : ℝ) ≠ 0 := by positivity
  simp only [cseT3, hs, ← sum_sub_distrib, mul_sum]
  rw [show ((rL2 N n : ℕ) : ℝ) = ∑ _j ∈ range (rL2 N n), (1 : ℝ) by simp, ← sum_add_distrib]
  refine sum_congr rfl fun j _ => ?_
  have h1 := hs_point_ne_zero' (rA2 N n) j
  have h2 := hs_point_ne_sub_nat (rA2 N n) 2 n j
  rw [show (rA2 N n - 2 * n : ℤ) = rA2 N n - ((2 : ℕ) : ℤ) * n by norm_num, hs_point_shift]
  simp only [Nat.cast_ofNat] at h2 ⊢
  generalize ((rA2 N n : ℤ) : ℝ) + j + 1 / 2 = k at *
  have h2' : k - (n : ℝ) * 2 ≠ 0 := by rwa [mul_comm]
  field_simp
  ring

theorem cseT4b_eval (N n : ℕ) (hn : 1 ≤ n) :
    cseT4b N n = rL2 N n + (9 * n / 32 : ℝ) *
      (hs Iv (rA2 N n - 2 * n) (rL2 N n) - hs Iv (rA2 N n) (rL2 N n))
      - (n ^ 2 / 16 : ℝ) * hs Qv (rA2 N n - n) (rL2 N n) := by
  have hn0 : (n : ℝ) ≠ 0 := by positivity
  simp only [cseT4b, hs, ← sum_sub_distrib, mul_sum]
  rw [show ((rL2 N n : ℕ) : ℝ) = ∑ _j ∈ range (rL2 N n), (1 : ℝ) by simp, ← sum_add_distrib,
    ← sum_sub_distrib]
  refine sum_congr rfl fun j _ => ?_
  have h1 := hs_point_ne_zero' (rA2 N n) j
  have h2 := hs_point_ne_sub_nat (rA2 N n) 2 n j
  have h3 := hs_point_ne_sub_nat (rA2 N n) 1 n j
  rw [show (rA2 N n - 2 * n : ℤ) = rA2 N n - ((2 : ℕ) : ℤ) * n by norm_num, hs_point_shift,
    show (rA2 N n - n : ℤ) = rA2 N n - ((1 : ℕ) : ℤ) * n by norm_num, hs_point_shift]
  simp only [Nat.cast_ofNat, Nat.cast_one, one_mul] at h2 h3 ⊢
  generalize ((rA2 N n : ℤ) : ℝ) + j + 1 / 2 = k at *
  have h2' : k - (n : ℝ) * 2 ≠ 0 := by rwa [mul_comm]
  field_simp
  ring

theorem cseT4a_eval (N n : ℕ) (hn : 1 ≤ n) :
    cseT4a N n = rL1 N n + (3 * n / 8 : ℝ) *
      (hs Iv (rA1 N n - n) (rL1 N n) - hs Iv (rA1 N n) (rL1 N n))
      + (n ^ 2 / 16 : ℝ) * (hs Qv (rA1 N n) (rL1 N n) + hs Qv (rA1 N n - n) (rL1 N n)) := by
  have hn0 : (n : ℝ) ≠ 0 := by positivity
  simp only [cseT4a, hs, ← sum_sub_distrib, ← sum_add_distrib, mul_sum]
  rw [show ((rL1 N n : ℕ) : ℝ) = ∑ _j ∈ range (rL1 N n), (1 : ℝ) by simp, ← sum_add_distrib,
    ← sum_add_distrib]
  refine sum_congr rfl fun j _ => ?_
  have h1 := hs_point_ne_zero' (rA1 N n) j
  have h3 := hs_point_ne_sub_nat (rA1 N n) 1 n j
  rw [show (rA1 N n - n : ℤ) = rA1 N n - ((1 : ℕ) : ℤ) * n by norm_num, hs_point_shift]
  simp only [Nat.cast_one, one_mul] at h3 ⊢
  generalize ((rA1 N n : ℤ) : ℝ) + j + 1 / 2 = k at *
  field_simp
  ring


/-- `omega` after unfolding the interval abbreviations. -/
macro "r_omega" : tactic =>
  `(tactic| (try simp only [rA1]) <;> (try simp only [rA2]) <;> (try simp only [rL1]) <;>
    (try simp only [rL2]) <;> omega)

theorem hs_eq_hP'' (f : ℝ → ℝ) (A A' B : ℤ) (L : ℕ) (hA : A = A') (hB : A + L = B) :
    hs f A L = hP f B - hP f A' := by
  rw [hs_eq_hP, hB, hA]

theorem hP_inv_nat (m : ℕ) : hP Iv (m : ℤ) = hHarm 1 m := by
  rw [hP_inv]; rfl
theorem hP_inv_negNat (m : ℕ) : hP Iv (-(m : ℤ)) = hHarm 1 m := by
  rw [hP_inv, Int.natAbs_neg, Int.natAbs_natCast]
theorem hP_invSq_nat (m : ℕ) : hP Qv (m : ℤ) = hHarm 2 m := by
  rw [hP_invSq]; simp
theorem hP_invSq_negNat (m : ℕ) : hP Qv (-(m : ℤ)) = -hHarm 2 m := by
  rcases Nat.eq_zero_or_pos m with rfl | hm
  · simp [hP, hHarm]
  · rw [hP_invSq]
    have : ¬ (0 : ℤ) ≤ -(m : ℤ) := by omega
    simp only [this, ↓reduceIte, Int.natAbs_neg, Int.natAbs_natCast]

/-- **(3), first range** (`1 ≤ n ≤ N`, including the continuation to `n = N`):
`κ₂₂ = (n/8)[2H₁(N-n) - H₁(N) - H₁(|N-2n|)] - (n²/8)[H₂(N) - H₂(N-n)]`. -/
theorem cseKappa_formula_short (N n : ℕ) (hn : 1 ≤ n) (hnN : n ≤ N) :
    cseKappa N n = n / 8 * (2 * hHarm 1 (N - n) - hHarm 1 N - hHarm 1 ((N : ℤ) - 2 * n).natAbs)
      - (n : ℝ) ^ 2 / 8 * (hHarm 2 N - hHarm 2 (N - n)) := by
  rw [cseKappa, cseT1_eval N n hn, cseT2_eval N n hn, cseT3_eval N n hn, cseT4b_eval N n hn,
    cseT4a_eval N n hn]
  have hL1 : ((rL1 N n : ℕ) : ℝ) = 2 * N - n := by
    rw [rL1, Nat.cast_sub (by omega)]; push_cast; ring
  have hL2 : ((rL2 N n : ℕ) : ℝ) = 2 * N - 2 * n := by
    rw [rL2, Nat.cast_sub (by omega)]; push_cast; ring
  rw [hs_eq_hP'' Iv _ (-(N : ℤ)) ((N - n : ℕ) : ℤ) _ (by r_omega) (by r_omega),
    hs_eq_hP'' Iv _ (-((N - n : ℕ) : ℤ)) (N : ℤ) _ (by r_omega) (by r_omega),
    hs_eq_hP'' Qv (rA2 N n - n) (-((N - n : ℕ) : ℤ)) ((N - n : ℕ) : ℤ) _ (by r_omega) (by r_omega),
    hs_eq_hP'' Qv (rA1 N n) (-((N - n : ℕ) : ℤ)) (N : ℤ) _ (by r_omega) (by r_omega),
    hs_eq_hP'' Qv (rA1 N n - n) (-(N : ℤ)) ((N - n : ℕ) : ℤ) _ (by r_omega) (by r_omega)]
  rcases le_or_gt (2 * n) N with h2 | h2
  · rw [hs_eq_hP'' Iv _ (-(N : ℤ)) ((N - 2 * n : ℕ) : ℤ) _ (by r_omega) (by r_omega),
      hs_eq_hP'' Iv (rA2 N n) (-((N - 2 * n : ℕ) : ℤ)) (N : ℤ) _ (by r_omega) (by r_omega),
      show ((N : ℤ) - 2 * n).natAbs = N - 2 * n by omega]
    simp only [hP_inv_nat, hP_inv_negNat, hP_invSq_nat, hP_invSq_negNat, hL1, hL2]
    ring
  · rw [hs_eq_hP'' Iv _ (-(N : ℤ)) (-((2 * n - N : ℕ) : ℤ)) _ (by r_omega) (by r_omega),
      hs_eq_hP'' Iv (rA2 N n) ((2 * n - N : ℕ) : ℤ) (N : ℤ) _ (by r_omega) (by r_omega),
      show ((N : ℤ) - 2 * n).natAbs = 2 * n - N by omega]
    simp only [hP_inv_nat, hP_inv_negNat, hP_invSq_nat, hP_invSq_negNat, hL1, hL2]
    ring


theorem cseR2_empty (N n : ℕ) (h : N ≤ n) :
    cseT2 N n = 0 ∧ cseT3 N n = 0 ∧ cseT4b N n = 0 := by
  have : rL2 N n = 0 := by simp only [rL2]; omega
  simp [cseT2, cseT3, cseT4b, hs, this]

theorem cseR1_empty (N n : ℕ) (h : 2 * N ≤ n) : cseT1 N n = 0 ∧ cseT4a N n = 0 := by
  have : rL1 N n = 0 := by simp only [rL1]; omega
  simp [cseT1, cseT4a, hs, this]

/-- **(3), middle range** `N ≤ n ≤ 2N`:
`κ₂₂ = N - n - (n/4)[H₁(N) - H₁(n-N)] - (n²/8)[H₂(N) - H₂(n-N)]`. -/
theorem cseKappa_formula_middle (N n : ℕ) (hn : 1 ≤ n) (hNn : N ≤ n) (hn2 : n ≤ 2 * N) :
    cseKappa N n = N - n - n / 4 * (hHarm 1 N - hHarm 1 (n - N))
      - (n : ℝ) ^ 2 / 8 * (hHarm 2 N - hHarm 2 (n - N)) := by
  obtain ⟨e2, e3, e4⟩ := cseR2_empty N n hNn
  rw [cseKappa, e2, e3, e4, cseT1_eval N n hn, cseT4a_eval N n hn]
  have hL1 : ((rL1 N n : ℕ) : ℝ) = 2 * N - n := by
    rw [rL1, Nat.cast_sub (by omega)]; push_cast; ring
  rw [hs_eq_hP'' Iv _ (-(N : ℤ)) (-((n - N : ℕ) : ℤ)) _ (by r_omega) (by r_omega),
    hs_eq_hP'' Iv (rA1 N n) ((n - N : ℕ) : ℤ) (N : ℤ) _ (by r_omega) (by r_omega),
    hs_eq_hP'' Qv (rA1 N n) ((n - N : ℕ) : ℤ) (N : ℤ) _ (by r_omega) (by r_omega),
    hs_eq_hP'' Qv (rA1 N n - n) (-(N : ℤ)) (-((n - N : ℕ) : ℤ)) _ (by r_omega) (by r_omega)]
  simp only [hP_inv_nat, hP_inv_negNat, hP_invSq_nat, hP_invSq_negNat, hL1]
  ring

/-- **(3), plateau** `n ≥ 2N`: `κ₂₂ = -N`. -/
theorem cseKappa_formula_plateau (N n : ℕ) (h : 2 * N ≤ n) : cseKappa N n = -N := by
  obtain ⟨e2, e3, e4⟩ := cseR2_empty N n (by omega)
  obtain ⟨e1, e5⟩ := cseR1_empty N n h
  rw [cseKappa, e1, e2, e3, e4, e5]; ring

/-- **(4)**: `κ₂₂(N, N) = -(N/4) H₁(N) - (N²/8) H₂(N)`. -/
theorem cseKappa_diag (N : ℕ) (hN : 1 ≤ N) :
    cseKappa N N = -(N / 4 : ℝ) * hHarm 1 N - (N : ℝ) ^ 2 / 8 * hHarm 2 N := by
  rw [cseKappa_formula_middle N N hN le_rfl (by omega)]
  simp [hHarm]

/-- The plateau already starts at `n = 2N - 1`. -/
theorem cseKappa_two_mul_sub_one (N : ℕ) (hN : 1 ≤ N) : cseKappa N (2 * N - 1) = -N := by
  rw [cseKappa_formula_middle N (2 * N - 1) (by omega) (by omega) (by omega)]
  have e : 2 * N - 1 - N = N - 1 := by omega
  rw [e]
  obtain ⟨M, rfl⟩ : ∃ M, N = M + 1 := ⟨N - 1, by omega⟩
  simp only [Nat.add_sub_cancel, hHarm, sum_range_succ]
  have e2 : ((2 * (M + 1) - 1 : ℕ) : ℝ) = 2 * M + 1 := by
    rw [Nat.cast_sub (by omega)]; push_cast; ring
  rw [e2]
  push_cast
  have hM : (M : ℝ) + 1 / 2 ≠ 0 := by positivity
  field_simp
  ring


/-! ## The uniform conditional bound -/

theorem hHarm_nonneg (r m : ℕ) : 0 ≤ hHarm r m :=
  sum_nonneg fun j _ => by positivity

theorem hHarm_mono (r : ℕ) {m m' : ℕ} (h : m ≤ m') : hHarm r m ≤ hHarm r m' :=
  sum_le_sum_of_subset_of_nonneg (range_subset_range.2 h) fun j _ _ => by positivity

/-- **Uniform bound**: `κ₂₂ ≤ N H₁(N)/8` for every positive time `n`. -/
theorem cseKappa_le (N n : ℕ) (hn : 1 ≤ n) : cseKappa N n ≤ N * hHarm 1 N / 8 := by
  have h1N := hHarm_nonneg 1 N
  rcases le_or_gt n N with h | h
  · rw [cseKappa_formula_short N n hn h]
    have a := hHarm_mono 1 (show N - n ≤ N by omega)
    have g := hHarm_mono 2 (show N - n ≤ N by omega)
    have b := hHarm_nonneg 1 ((N : ℤ) - 2 * n).natAbs
    have hnN : (n : ℝ) ≤ N := by exact_mod_cast h
    have hn0 : (0 : ℝ) ≤ n := by positivity
    have : (n : ℝ) * hHarm 1 N ≤ N * hHarm 1 N := mul_le_mul_of_nonneg_right hnN h1N
    nlinarith [mul_nonneg hn0 (sub_nonneg.2 a), mul_nonneg (sq_nonneg (n : ℝ)) (sub_nonneg.2 g),
      mul_nonneg hn0 b]
  · rcases le_or_gt n (2 * N) with h2 | h2
    · rw [cseKappa_formula_middle N n hn h.le h2]
      have a := hHarm_mono 1 (show n - N ≤ N by omega)
      have g := hHarm_mono 2 (show n - N ≤ N by omega)
      have hnN : (N : ℝ) ≤ n := by exact_mod_cast h.le
      have hn0 : (0 : ℝ) ≤ n := by positivity
      nlinarith [mul_nonneg hn0 (sub_nonneg.2 a), mul_nonneg (sq_nonneg (n : ℝ)) (sub_nonneg.2 g),
        mul_nonneg (Nat.cast_nonneg N : (0 : ℝ) ≤ N) h1N]
    · rw [cseKappa_formula_plateau N n h2.le]
      have : (0 : ℝ) ≤ N * hHarm 1 N := by positivity
      linarith [(Nat.cast_nonneg N : (0 : ℝ) ≤ N)]

/-- `H₁(N) ≤ 2 + log(2N - 1)` for `N ≥ 1` (input to the second-moment bound after (5)). -/
theorem hHarm_one_le_log (N : ℕ) (hN : 1 ≤ N) :
    hHarm 1 N ≤ 2 + Real.log (2 * N - 1) := by
  have h := harmonic_half_sum_le (d := 0) (N := N) (by omega)
  have e : hHarm 1 N = ∑ j ∈ Ico 0 N, 1 / ((j : ℝ) + 1 / 2) := by
    rw [hHarm, ← range_eq_Ico]; simp
  have hN1 : (1 : ℝ) ≤ N := by exact_mod_cast hN
  have hl : Real.log ((N : ℝ) / ((0 : ℕ) + 1)) ≤ Real.log (2 * N - 1) := by
    simp only [Nat.cast_zero, zero_add, div_one]
    exact Real.log_le_log (by linarith) (by linarith)
  rw [e]; linarith

/-- The CSE exact second moment (5), taken from the document:
`m₂ = n/2 + (n/4)[H₁(N) - H₁(|N-n|)]` for `n ≤ 2N` and `m₂ = N` for `n ≥ 2N`. -/
noncomputable def cseM2 (N n : ℕ) : ℝ :=
  if n ≤ 2 * N then n / 2 + n / 4 * (hHarm 1 N - hHarm 1 ((N : ℤ) - n).natAbs) else N

/-- Bound after (5): `m₂ ≤ N [2 + ½ log(2N - 1)]` for `N ≥ 1`. -/
theorem cseM2_le (N n : ℕ) (hN : 1 ≤ N) :
    cseM2 N n ≤ N * (2 + Real.log (2 * N - 1) / 2) := by
  have hN1 : (1 : ℝ) ≤ N := by exact_mod_cast hN
  have hlog : 0 ≤ Real.log (2 * N - 1) := Real.log_nonneg (by linarith)
  have hH := hHarm_one_le_log N hN
  rw [cseM2]
  split_ifs with h
  · have hn : (n : ℝ) ≤ 2 * N := by exact_mod_cast h
    have hn0 : (0 : ℝ) ≤ n := by positivity
    have b := hHarm_nonneg 1 ((N : ℤ) - n).natAbs
    have h1 : (n : ℝ) / 4 * (hHarm 1 N - hHarm 1 ((N : ℤ) - n).natAbs) ≤ n / 4 * hHarm 1 N :=
      mul_le_mul_of_nonneg_left (by linarith) (by positivity)
    have h2 : (n : ℝ) / 4 * hHarm 1 N ≤ N / 2 * (2 + Real.log (2 * N - 1)) := by
      have := hHarm_nonneg 1 N
      calc (n : ℝ) / 4 * hHarm 1 N ≤ N / 2 * hHarm 1 N :=
            mul_le_mul_of_nonneg_right (by linarith) this
        _ ≤ N / 2 * (2 + Real.log (2 * N - 1)) :=
            mul_le_mul_of_nonneg_left hH (by positivity)
    nlinarith
  · nlinarith

/-! ## CUE: exact variance (7) and the all-time comparison (8) -/

/-- CUE second moment `m₂ = min(n, N)`. -/
noncomputable def cueM2 (N n : ℕ) : ℝ := min n N

/-- CUE connected fourth cumulant `κ₂₂ = -N + 2(N-n)₊ - (N-2n)₊`. -/
noncomputable def cueKappa (N n : ℕ) : ℝ := -(N : ℝ) + 2 * ((N - n : ℕ) : ℝ) - ((N - 2 * n : ℕ) : ℝ)

/-- The CUE grouping `κ₂₂ = -N + 4T₁ - T₂ + 4T₃ - 4T_{4b} - 2T_{4a}` with the unweighted-shift
traces `T₁ = T_{4a} = (N-n)₊`, `T₂ = T₃ = T_{4b} = (N-2n)₊`. -/
theorem cueKappa_grouping (N n : ℕ) :
    cueKappa N n = -(N : ℝ) + 4 * ((N - n : ℕ) : ℝ) - ((N - 2 * n : ℕ) : ℝ)
      + 4 * ((N - 2 * n : ℕ) : ℝ) - 4 * ((N - 2 * n : ℕ) : ℝ) - 2 * ((N - n : ℕ) : ℝ) := by
  rw [cueKappa]; ring

/-- `Var |p_n|² = m₂² + κ₂₂` (rotation invariance gives `E p_n² = 0`). -/
noncomputable def cueVar (N n : ℕ) : ℝ := cueM2 N n ^ 2 + cueKappa N n

/-- **(7)**, first range: `Var |p_n|² = n²` for `2n ≤ N`. -/
theorem cueVar_short (N n : ℕ) (h : 2 * n ≤ N) : cueVar N n = (n : ℝ) ^ 2 := by
  have h1 : min (n : ℝ) N = n := min_eq_left (by exact_mod_cast (by omega : n ≤ N))
  rw [cueVar, cueM2, cueKappa, h1, Nat.cast_sub (by omega), Nat.cast_sub h]
  push_cast; ring

/-- **(7)**, middle range: `Var |p_n|² = n² - 2n + N` for `N ≤ 2n`, `n ≤ N`. -/
theorem cueVar_middle (N n : ℕ) (h1 : N ≤ 2 * n) (h2 : n ≤ N) :
    cueVar N n = (n : ℝ) ^ 2 - 2 * n + N := by
  have hm : min (n : ℝ) N = n := min_eq_left (by exact_mod_cast h2)
  have hz : N - 2 * n = 0 := by omega
  rw [cueVar, cueM2, cueKappa, hm, Nat.cast_sub h2, hz]
  push_cast; ring

/-- **(7)**, long range: `Var |p_n|² = N² - N` for `n ≥ N`. -/
theorem cueVar_long (N n : ℕ) (h : N ≤ n) : cueVar N n = (N : ℝ) ^ 2 - N := by
  have hm : min (n : ℝ) N = N := min_eq_right (by exact_mod_cast h)
  have hz1 : N - n = 0 := by omega
  have hz2 : N - 2 * n = 0 := by omega
  rw [cueVar, cueM2, cueKappa, hm, hz1, hz2]
  push_cast; ring

/-- Each branch of (7) is at most `N² - N` when `N ≥ 2`. -/
theorem cueVar_le (N n : ℕ) (hN : 2 ≤ N) : cueVar N n ≤ (N : ℝ) ^ 2 - N := by
  have hN' : (2 : ℝ) ≤ N := by exact_mod_cast hN
  rcases le_or_gt (2 * n) N with h | h
  · rw [cueVar_short N n h]
    have : (2 * n : ℝ) ≤ N := by exact_mod_cast h
    nlinarith [(Nat.cast_nonneg n : (0 : ℝ) ≤ n)]
  · rcases le_or_gt n N with h2 | h2
    · rw [cueVar_middle N n h.le h2]
      have a : (n : ℝ) ≤ N := by exact_mod_cast h2
      have b : (1 : ℝ) ≤ n := by exact_mod_cast (by omega : 1 ≤ n)
      nlinarith
    · rw [cueVar_long N n h2.le]

/-- **(8)**, arithmetic form: `Var |p_n|² / (N²(N+1)) ≤ (1 - 1/N)/(N+1)` uniformly in `n`, for
`N ≥ 2`. (The phase-contraction inequality that converts this into the bound on
`E_Q |K_{N,Q}(n) - K̄_{2,N}(n)|²` is a separate result and is not formalized here.) -/
theorem cueVar_comparison (N n : ℕ) (hN : 2 ≤ N) :
    cueVar N n / ((N : ℝ) ^ 2 * (N + 1)) ≤ (1 - 1 / (N : ℝ)) / (N + 1) := by
  have hN' : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
  rw [div_le_div_iff₀ (by positivity) (by positivity)]
  have := cueVar_le N n hN
  have e : (1 - 1 / (N : ℝ)) * ((N : ℝ) ^ 2 * (N + 1)) = ((N : ℝ) ^ 2 - N) * (N + 1) := by
    field_simp
  rw [e]
  exact mul_le_mul_of_nonneg_right this (by positivity)

end Bgs.Mathlib
