module
public import Mathlib
@[expose] public section

/-!
# Uniform massive covariance: the bound (B1) (uniform cluster lemma, §3)

Source: `mathematics/fixed-map/uniform_cluster_lemma.md`, §3.

* `cyclic_form_bounds`: on a cycle of length `m`, the zero-coupling Hessian form
  `vᵀH₀v = -(3/2) ∑ v_j² + (1/2) ∑ v_j v_{j+1}` satisfies `-2|v|² ≤ vᵀH₀v ≤ -|v|²`.
* `diagDominant_sup_bound`: if `K = D - R` with `D` diagonal, `D_jj ≥ a`,
  `∑_k |R_jk| ≤ b < a`, then `‖v‖_∞ ≤ ‖K v‖_∞ / (a - b)`; in particular `K` is invertible
  (`diagDominant_det_ne_zero`).
* `diagDominant_inv_row_sum`: `∑_k |(K⁻¹)_jk| ≤ 1/(a - b)`.
* `diagDominant_inv_decay`: if moreover `R` is nearest-neighbour for a distance `d`
  (`R_jl ≠ 0 → d j l ≤ 1`, `d` satisfying the triangle inequality and `d k k = 0`), then
  `|(K⁻¹)_jk| ≤ (1/(a - b)) (b/a)^{d(j,k)}`.
* `cluster_B1`: with the constants of the text, `a = 7/5`, `b = 3/5`:
  `∑_k |(K⁻¹)_jk| ≤ 5/4` and `|(K⁻¹)_jk| ≤ (5/4)(3/7)^{d(j,k)}`  — this is (B1).

The proof avoids the Neumann series: the row-sum bound is the `ℓ^∞` operator bound obtained
from diagonal dominance, and the decay follows by induction on the distance from `K K⁻¹ = 1`.
-/

open Finset Matrix

namespace Bgs.Mathlib

/-! ## The zero-coupling cyclic form -/

/-- `|∑_j v_j v_{j+1}| ≤ ∑_j v_j²` on a cycle `ZMod m`. -/
lemma cyclic_cross_le {m : ℕ} [NeZero m] (v : ZMod m → ℝ) :
    |∑ j, v j * v (j + 1)| ≤ ∑ j, v j ^ 2 := by
  have hshift : ∑ j, v (j + 1) ^ 2 = ∑ j, v j ^ 2 :=
    Fintype.sum_equiv (Equiv.addRight 1) _ _ (fun j => rfl)
  rw [abs_le]
  constructor
  · have : ∀ j, -(v j * v (j + 1)) ≤ (v j ^ 2 + v (j + 1) ^ 2) / 2 := fun j => by
      nlinarith [sq_nonneg (v j + v (j + 1))]
    have h := Finset.sum_le_sum fun j (_ : j ∈ univ) => this j
    rw [sum_neg_distrib, ← sum_div, sum_add_distrib, hshift] at h
    linarith
  · have : ∀ j, v j * v (j + 1) ≤ (v j ^ 2 + v (j + 1) ^ 2) / 2 := fun j => by
      nlinarith [sq_nonneg (v j - v (j + 1))]
    have h := Finset.sum_le_sum fun j (_ : j ∈ univ) => this j
    rw [← sum_div, sum_add_distrib, hshift] at h
    linarith

/-- **§3, zero coupling.**  `-2|v|² ≤ -(3/2)∑ v_j² + (1/2)∑ v_j v_{j+1} ≤ -|v|²`,
i.e. `-2I ≤ H₀ ≤ -I`. -/
theorem cyclic_form_bounds {m : ℕ} [NeZero m] (v : ZMod m → ℝ) :
    -2 * ∑ j, v j ^ 2 ≤ -(3 / 2) * ∑ j, v j ^ 2 + (1 / 2) * ∑ j, v j * v (j + 1) ∧
    -(3 / 2) * ∑ j, v j ^ 2 + (1 / 2) * ∑ j, v j * v (j + 1) ≤ -∑ j, v j ^ 2 := by
  have h := abs_le.mp (cyclic_cross_le v)
  constructor <;> linarith [h.1, h.2]

/-! ## Diagonally dominant matrices -/

variable {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- **`ℓ^∞` lower bound.**  If `K = diag(d) - R`, `d_j ≥ a`, `∑_k |R_jk| ≤ b < a` and
`|(K v)_k| ≤ W` for all `k`, then `|v_j| ≤ W / (a - b)` for all `j`. -/
theorem diagDominant_sup_bound (d : ι → ℝ) (R : Matrix ι ι ℝ) {a b W : ℝ}
    (hd : ∀ j, a ≤ d j) (hR : ∀ j, ∑ k, |R j k| ≤ b) (hab : b < a) (v : ι → ℝ)
    (hW : ∀ k, |((diagonal d - R) *ᵥ v) k| ≤ W) (j : ι) :
    |v j| ≤ W / (a - b) := by
  obtain ⟨j0, -, hj0⟩ := Finset.exists_max_image univ (fun k => |v k|) ⟨j, mem_univ j⟩
  have hb0 : 0 ≤ b := le_trans (Finset.sum_nonneg fun k _ => abs_nonneg _) (hR j)
  have ha0 : 0 < a := lt_of_le_of_lt hb0 hab
  have hsum : |∑ k, R j0 k * v k| ≤ b * |v j0| := by
    calc |∑ k, R j0 k * v k| ≤ ∑ k, |R j0 k * v k| := abs_sum_le_sum_abs _ _
      _ = ∑ k, |R j0 k| * |v k| := by simp [abs_mul]
      _ ≤ ∑ k, |R j0 k| * |v j0| :=
          Finset.sum_le_sum fun k _ => mul_le_mul_of_nonneg_left (hj0 k (mem_univ k))
            (abs_nonneg _)
      _ = (∑ k, |R j0 k|) * |v j0| := by rw [sum_mul]
      _ ≤ b * |v j0| := mul_le_mul_of_nonneg_right (hR j0) (abs_nonneg _)
  have hK : ((diagonal d - R) *ᵥ v) j0 = d j0 * v j0 - ∑ k, R j0 k * v k := by
    simp only [mulVec, dotProduct, Matrix.sub_apply, sub_mul, sum_sub_distrib, diagonal_apply,
      ite_mul, zero_mul, Finset.sum_ite_eq, mem_univ, ite_true]
  have h1 : (a - b) * |v j0| ≤ W := by
    have := hW j0
    rw [hK] at this
    have hdv : a * |v j0| ≤ |d j0 * v j0| := by
      rw [abs_mul, abs_of_pos (lt_of_lt_of_le ha0 (hd j0))]
      exact mul_le_mul_of_nonneg_right (hd j0) (abs_nonneg _)
    have := abs_sub_abs_le_abs_sub (d j0 * v j0) (∑ k, R j0 k * v k)
    linarith
  rw [le_div_iff₀ (by linarith)]
  calc |v j| * (a - b) ≤ |v j0| * (a - b) :=
        mul_le_mul_of_nonneg_right (hj0 j (mem_univ j)) (by linarith)
    _ ≤ W := by linarith

/-- A strictly diagonally dominant matrix in the above sense is invertible. -/
theorem diagDominant_det_ne_zero (d : ι → ℝ) (R : Matrix ι ι ℝ) {a b : ℝ}
    (hd : ∀ j, a ≤ d j) (hR : ∀ j, ∑ k, |R j k| ≤ b) (hab : b < a) :
    (diagonal d - R).det ≠ 0 := by
  intro hdet
  obtain ⟨v, hv0, hv⟩ := Matrix.exists_mulVec_eq_zero_iff.mpr hdet
  apply hv0
  funext j
  have := diagDominant_sup_bound d R hd hR hab v (W := 0) (fun k => by simp [hv]) j
  simp only [zero_div] at this
  simpa using abs_nonpos_iff.mp this

/-- **Row sums of the inverse.**  `∑_k |(K⁻¹)_jk| ≤ 1/(a - b)`. -/
theorem diagDominant_inv_row_sum (d : ι → ℝ) (R : Matrix ι ι ℝ) {a b : ℝ}
    (hd : ∀ j, a ≤ d j) (hR : ∀ j, ∑ k, |R j k| ≤ b) (hab : b < a) (j : ι) :
    ∑ k, |(diagonal d - R)⁻¹ j k| ≤ 1 / (a - b) := by
  set K := diagonal d - R
  have hunit : IsUnit K.det := isUnit_iff_ne_zero.mpr (diagDominant_det_ne_zero d R hd hR hab)
  set w : ι → ℝ := fun k => SignType.sign (K⁻¹ j k)
  have hw : ∀ k, |w k| ≤ 1 := fun k => by
    simp only [w]; rcases lt_trichotomy (K⁻¹ j k) 0 with h | h | h <;> simp [h]
  set v := K⁻¹ *ᵥ w
  have hKv : K *ᵥ v = w := by
    simp only [v, mulVec_mulVec, mul_nonsing_inv _ hunit, one_mulVec]
  have hv := diagDominant_sup_bound d R hd hR hab v (W := 1) (fun k => by rw [hKv]; exact hw k) j
  have hvj : v j = ∑ k, |K⁻¹ j k| := by
    simp only [v, mulVec, dotProduct, w]
    exact Finset.sum_congr rfl fun k _ => by
      rcases lt_trichotomy (K⁻¹ j k) 0 with h | h | h <;> simp [h, abs_of_neg, abs_of_pos]
  rw [← hvj]
  exact (le_abs_self _).trans hv

/-- **Exponential decay of the inverse.**  If `R` only couples points at distance `≤ 1` for
a distance `d` with `d k k = 0` and the triangle inequality, then
`|(K⁻¹)_jk| ≤ (1/(a - b)) · (b/a)^{d(j,k)}`. -/
theorem diagDominant_inv_decay (d : ι → ℝ) (R : Matrix ι ι ℝ) {a b : ℝ}
    (hd : ∀ j, a ≤ d j) (hR : ∀ j, ∑ k, |R j k| ≤ b) (hab : b < a)
    (dist : ι → ι → ℕ) (hdist0 : ∀ k, dist k k = 0)
    (htri : ∀ j l k, dist j k ≤ dist j l + dist l k)
    (hloc : ∀ j l, R j l ≠ 0 → dist j l ≤ 1) (j k : ι) :
    |(diagonal d - R)⁻¹ j k| ≤ (1 / (a - b)) * (b / a) ^ dist j k := by
  set K := diagonal d - R with hKdef
  set C := 1 / (a - b)
  have hunit : IsUnit K.det := isUnit_iff_ne_zero.mpr (diagDominant_det_ne_zero d R hd hR hab)
  have hb0 : 0 ≤ b := le_trans (Finset.sum_nonneg fun k _ => abs_nonneg _) (hR j)
  have ha0 : 0 < a := lt_of_le_of_lt hb0 hab
  have hC : 0 ≤ C := by simp only [C]; rw [one_div]; exact inv_nonneg.mpr (by linarith)
  -- entrywise bound from the row sums
  have hentry : ∀ j k, |K⁻¹ j k| ≤ C := fun j k =>
    (Finset.single_le_sum (f := fun k => |K⁻¹ j k|) (fun _ _ => abs_nonneg _)
      (mem_univ k)).trans (diagDominant_inv_row_sum d R hd hR hab j)
  -- the identity `K K⁻¹ = 1` row by row
  have hrow : ∀ j k, j ≠ k → d j * K⁻¹ j k = ∑ l, R j l * K⁻¹ l k := by
    intro j k hjk
    have h := congrFun (congrFun (mul_nonsing_inv K hunit) j) k
    rw [one_apply_ne hjk, mul_apply] at h
    simp only [hKdef] at h ⊢
    simp only [Matrix.sub_apply, sub_mul, sum_sub_distrib, diagonal_apply, ite_mul, zero_mul,
      Finset.sum_ite_eq, mem_univ, ite_true] at h
    linarith
  have key : ∀ n : ℕ, ∀ j k, n ≤ dist j k → |K⁻¹ j k| ≤ C * (b / a) ^ n := by
    intro n
    induction n with
    | zero => intro j k _; simpa using hentry j k
    | succ n ih =>
      intro j k hn
      have hjk : j ≠ k := by rintro rfl; rw [hdist0] at hn; omega
      have hdj : 0 < d j := lt_of_lt_of_le ha0 (hd j)
      have hbound : ∀ l, |R j l * K⁻¹ l k| ≤ |R j l| * (C * (b / a) ^ n) := by
        intro l
        rw [abs_mul]
        by_cases hRl : R j l = 0
        · simp [hRl]
        · refine mul_le_mul_of_nonneg_left (ih l k ?_) (abs_nonneg _)
          have := htri j l k
          have := hloc j l hRl
          omega
      have h1 : d j * |K⁻¹ j k| ≤ b * (C * (b / a) ^ n) := by
        rw [← abs_of_pos hdj, ← abs_mul, hrow j k hjk]
        calc |∑ l, R j l * K⁻¹ l k| ≤ ∑ l, |R j l * K⁻¹ l k| := abs_sum_le_sum_abs _ _
          _ ≤ ∑ l, |R j l| * (C * (b / a) ^ n) := Finset.sum_le_sum fun l _ => hbound l
          _ = (∑ l, |R j l|) * (C * (b / a) ^ n) := by rw [sum_mul]
          _ ≤ b * (C * (b / a) ^ n) :=
              mul_le_mul_of_nonneg_right (hR j) (by positivity)
      have h2 : a * |K⁻¹ j k| ≤ b * (C * (b / a) ^ n) :=
        le_trans (mul_le_mul_of_nonneg_right (hd j) (abs_nonneg _)) h1
      rw [pow_succ]
      calc |K⁻¹ j k| ≤ b * (C * (b / a) ^ n) / a := (le_div_iff₀' ha0).mpr h2
        _ = C * ((b / a) ^ n * (b / a)) := by field_simp
  exact key _ j k le_rfl

/-- **(B1).**  With `D_jj ≥ 7/5` and `∑_k |R_jk| ≤ 3/5` (nearest-neighbour `R`):
`∑_k |(K⁻¹)_jk| ≤ 5/4` and `|(K⁻¹)_jk| ≤ (5/4)(3/7)^{d(j,k)}`. -/
theorem cluster_B1 (d : ι → ℝ) (R : Matrix ι ι ℝ)
    (hd : ∀ j, 7 / 5 ≤ d j) (hR : ∀ j, ∑ k, |R j k| ≤ 3 / 5)
    (dist : ι → ι → ℕ) (hdist0 : ∀ k, dist k k = 0)
    (htri : ∀ j l k, dist j k ≤ dist j l + dist l k)
    (hloc : ∀ j l, R j l ≠ 0 → dist j l ≤ 1) :
    (diagonal d - R).det ≠ 0 ∧
    (∀ j, ∑ k, |(diagonal d - R)⁻¹ j k| ≤ 5 / 4) ∧
    (∀ j k, |(diagonal d - R)⁻¹ j k| ≤ 5 / 4 * (3 / 7) ^ dist j k) := by
  have hab : (3 / 5 : ℝ) < 7 / 5 := by norm_num
  refine ⟨diagDominant_det_ne_zero d R hd hR hab, fun j => ?_, fun j k => ?_⟩
  · have := diagDominant_inv_row_sum d R hd hR hab j
    norm_num at this ⊢; linarith
  · have := diagDominant_inv_decay d R hd hR hab dist hdist0 htri hloc j k
    norm_num at this ⊢; linarith

#print axioms cyclic_cross_le
#print axioms cyclic_form_bounds
#print axioms diagDominant_sup_bound
#print axioms diagDominant_det_ne_zero
#print axioms diagDominant_inv_row_sum
#print axioms diagDominant_inv_decay
#print axioms cluster_B1
end Bgs.Mathlib
