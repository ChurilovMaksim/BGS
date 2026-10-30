module
public import Mathlib
@[expose] public section

/-!
# The hyperbolic cat map `S = [[3,4],[2,3]]`

This file formalizes the classical, finite-dimensional facts about the
matrix
\[ S = \begin{pmatrix} 3 & 4 \\ 2 & 3 \end{pmatrix} \]
that underlie the quantized frozen map `U_N = exp(i τ N A_N) M_N` of the
BGS repository:

* `S ∈ SL(2,ℤ)` (`catS_det`), `tr S = 6` (`catS_trace`);
* `S` preserves the Pell form `x² - 2y²` (`catS_preserves_pell`);
* Cayley–Hamilton `S² = 6S - 1` and the trace recurrence
  `tr S^(n+2) = 6 tr S^(n+1) - tr S^n` (`catS_trace_pow_rec`);
* closed form `tr S^n = λⁿ + λ⁻ⁿ` with `λ = 3 + 2√2 = (1+√2)²`
  (`catS_trace_pow_real`), hence hyperbolicity `tr S^n > 2` for `n ≥ 1`;
* the periodic-point determinant `det(Sⁿ - 1) = 2 - tr Sⁿ`
  (`catS_det_pow_sub_one`), which is nonzero for `n ≥ 1`;
* the admissible window of the TRACE-113 growth constant:
  `√(3+2√2) = 1+√2 > 1` (`trace113_window`).
-/

open Matrix

namespace Bgs.Mathlib

/-- The hyperbolic cat matrix `S = [[3,4],[2,3]]`. -/
def catS : Matrix (Fin 2) (Fin 2) ℤ := !![3, 4; 2, 3]

theorem catS_det : catS.det = 1 := by
  simp [catS, Matrix.det_fin_two]

theorem catS_trace : catS.trace = 6 := by
  simp [catS, Matrix.trace_fin_two]

/-- `S` preserves the Pell quadratic form `x² - 2y²`. -/
theorem catS_preserves_pell (x y : ℤ) :
    (3 * x + 4 * y) ^ 2 - 2 * (2 * x + 3 * y) ^ 2 = x ^ 2 - 2 * y ^ 2 := by
  ring

/-- The action of `S` on a column vector, matching `catS_preserves_pell`. -/
theorem catS_mulVec (x y : ℤ) :
    catS *ᵥ ![x, y] = ![3 * x + 4 * y, 2 * x + 3 * y] := by
  ext i; fin_cases i <;> simp [catS, Matrix.mulVec, dotProduct, Fin.sum_univ_two]

/-- Cayley–Hamilton for `S`: `S² = 6 S - 1`. -/
theorem catS_sq : catS ^ 2 = 6 • catS - 1 := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [catS, sq, Matrix.mul_apply, Fin.sum_univ_two]

/-- Trace recurrence: `tr S^(n+2) = 6 tr S^(n+1) - tr S^n`. -/
theorem catS_trace_pow_rec (n : ℕ) :
    (catS ^ (n + 2)).trace = 6 * (catS ^ (n + 1)).trace - (catS ^ n).trace := by
  have h : catS ^ (n + 2) = 6 • catS ^ (n + 1) - catS ^ n := by
    rw [pow_add, catS_sq, pow_succ, mul_sub, mul_smul_comm, mul_one]
  rw [h, Matrix.trace_sub, Matrix.trace_smul]
  simp

/-- The expanding eigenvalue `λ = 3 + 2√2`. -/
noncomputable def catLambda : ℝ := 3 + 2 * Real.sqrt 2

theorem catLambda_eq_sq : catLambda = (1 + Real.sqrt 2) ^ 2 := by
  have h := Real.sq_sqrt (show (0 : ℝ) ≤ 2 by norm_num)
  unfold catLambda; nlinarith

theorem catLambda_mul_inv : catLambda * (3 - 2 * Real.sqrt 2) = 1 := by
  have h := Real.sq_sqrt (show (0 : ℝ) ≤ 2 by norm_num)
  unfold catLambda; nlinarith

theorem one_lt_catLambda : 1 < catLambda := by
  unfold catLambda; nlinarith [Real.sqrt_nonneg 2]

/-- Closed form of the traces: `tr Sⁿ = λⁿ + λ⁻ⁿ`. -/
theorem catS_trace_pow_real (n : ℕ) :
    ((catS ^ n).trace : ℝ) = catLambda ^ n + catLambda⁻¹ ^ n := by
  have hinv : catLambda⁻¹ = 3 - 2 * Real.sqrt 2 := by
    exact inv_eq_of_mul_eq_one_right catLambda_mul_inv
  have h2 := Real.sq_sqrt (show (0 : ℝ) ≤ 2 by norm_num)
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    match n, ih with
    | 0, _ => simp; norm_num
    | 1, _ =>
      rw [pow_one, pow_one, hinv, catS_trace]; unfold catLambda; push_cast; ring
    | k + 2, ih =>
      rw [catS_trace_pow_rec]; push_cast
      rw [ih (k + 1) (by omega), ih k (by omega), hinv]
      unfold catLambda
      have e1 : (3 + 2 * Real.sqrt 2) ^ 2 = 6 * (3 + 2 * Real.sqrt 2) - 1 := by nlinarith
      have e2 : (3 - 2 * Real.sqrt 2) ^ 2 = 6 * (3 - 2 * Real.sqrt 2) - 1 := by nlinarith
      have : ∀ a : ℝ, a ^ 2 = 6 * a - 1 → a ^ (k + 2) = 6 * a ^ (k + 1) - a ^ k := by
        intro a ha; rw [pow_add, ha, pow_succ]; ring
      rw [this _ e1, this _ e2]; ring

/-- Hyperbolicity: `tr Sⁿ > 2` for every `n ≥ 1`. -/
theorem catS_trace_pow_gt_two (n : ℕ) (hn : 1 ≤ n) : 2 < (catS ^ n).trace := by
  have key : (2 : ℝ) < ((catS ^ n).trace : ℝ) := by
    rw [catS_trace_pow_real]
    have hl := one_lt_catLambda
    have hpos : 0 < catLambda := by linarith
    set a := catLambda ^ n
    have ha : 1 < a := one_lt_pow₀ hl (by omega)
    have : catLambda⁻¹ ^ n = a⁻¹ := by rw [inv_pow]
    rw [this]
    have ha0 : 0 < a := by linarith
    have : a + a⁻¹ - 2 = (a - 1) ^ 2 / a := by field_simp; ring
    have : 0 < (a - 1) ^ 2 / a := by
      apply div_pos _ ha0; nlinarith
    linarith
  exact_mod_cast key

/-- For a `2×2` matrix of determinant one, `det(A - 1) = 2 - tr A`. -/
theorem det_sub_one_of_det_one (A : Matrix (Fin 2) (Fin 2) ℤ) (h : A.det = 1) :
    (A - 1).det = 2 - A.trace := by
  rw [Matrix.det_fin_two] at h ⊢
  simp [Matrix.trace_fin_two] at h ⊢
  linarith

/-- Periodic-point determinant: `det(Sⁿ - 1) = 2 - tr Sⁿ`. -/
theorem catS_det_pow_sub_one (n : ℕ) : (catS ^ n - 1).det = 2 - (catS ^ n).trace :=
  det_sub_one_of_det_one _ (by rw [Matrix.det_pow, catS_det, one_pow])

/-- For `n ≥ 1`, `|det(Sⁿ - 1)| = tr Sⁿ - 2 > 0`: the number of period-`n` points of
the cat map on the torus is positive and given by the trace. -/
theorem catS_abs_det_pow_sub_one (n : ℕ) (hn : 1 ≤ n) :
    |(catS ^ n - 1).det| = (catS ^ n).trace - 2 ∧ 0 < (catS ^ n).trace - 2 := by
  have := catS_trace_pow_gt_two n hn
  rw [catS_det_pow_sub_one]
  constructor
  · rw [abs_of_neg (by linarith)]; ring
  · linarith

/-- TRACE-113 window: the admissible growth constants `1 < a < √(3+2√2)` form the
nonempty interval `(1, 1+√2)`, and `√(3+2√2) = 1+√2 = √λ`. -/
theorem trace113_window :
    Real.sqrt (3 + 2 * Real.sqrt 2) = 1 + Real.sqrt 2 ∧ 1 < 1 + Real.sqrt 2 := by
  refine ⟨?_, by have := Real.sqrt_pos.2 (show (0:ℝ) < 2 by norm_num); linarith⟩
  have h := Real.sq_sqrt (show (0 : ℝ) ≤ 2 by norm_num)
  rw [Real.sqrt_eq_iff_mul_self_eq] <;> nlinarith [Real.sqrt_nonneg 2]

#print axioms catS_det
#print axioms catS_trace
#print axioms catS_preserves_pell
#print axioms catS_mulVec
#print axioms catS_sq
#print axioms catS_trace_pow_rec
#print axioms catLambda_eq_sq
#print axioms catLambda_mul_inv
#print axioms one_lt_catLambda
#print axioms catS_trace_pow_real
#print axioms catS_trace_pow_gt_two
#print axioms det_sub_one_of_det_one
#print axioms catS_det_pow_sub_one
#print axioms catS_abs_det_pow_sub_one
#print axioms trace113_window
end Bgs.Mathlib
