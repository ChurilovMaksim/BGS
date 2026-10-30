module
public import Bgs.Mathlib.CatMap
@[expose] public section

/-!
# Exact periodic-point grids of the fixed cat map (BGS-FM-012)

With `C = [[1,2],[1,1]]` one has `C² = S` and `Cᵐ = [[x_m, 2y_m],[y_m, x_m]]`, where
`x₀ = 1, y₀ = 0, x_{m+1} = x_m + 2y_m, y_{m+1} = x_m + y_m`.  We prove:

* `C² = S` (`catC_sq`), the closed form of `Cᵐ` (`catC_pow`) and the Pell identity
  `x_m² - 2 y_m² = (-1)^m` (`pell_xy`);
* the exact factorizations `Sᵐ - 1 = 2x_m Cᵐ` (`m` odd) and `Sᵐ - 1 = 2y_m J Cᵐ` (`m` even),
  `J = [[0,2],[1,0]]` (`catS_pow_sub_one_odd`, `catS_pow_sub_one_even`);
* the annihilator lattices `(Sᵐ - 1)ᵀ ℤ² = 2x_m ℤ × 2x_m ℤ` (odd) and
  `2y_m ℤ × 4y_m ℤ` (even) (`annihilator_odd`, `annihilator_even`);
* the periodic-point counts `|det(Sᵐ - 1)| = 4x_m²` (odd), `8y_m²` (even)
  (`fix_count_odd`, `fix_count_even`);
* the shortest annihilator frequencies `ℓ₁..ℓ₆ = 2,4,14,24,82,140` and `ℓ_m ≥ 14` for `m ≥ 3`
  (`ell_values`, `ell_ge_fourteen`).
-/

open Matrix

namespace Bgs.Mathlib

/-- `C = [[1,2],[1,1]]`, a square root of the cat matrix. -/
def catC : Matrix (Fin 2) (Fin 2) ℤ := !![1, 2; 1, 1]

/-- `J = [[0,2],[1,0]]`. -/
def catJ : Matrix (Fin 2) (Fin 2) ℤ := !![0, 2; 1, 0]

/-- The Pell pair `(x_m, y_m)`. -/
def pellXY : ℕ → ℤ × ℤ
  | 0 => (1, 0)
  | m + 1 => ((pellXY m).1 + 2 * (pellXY m).2, (pellXY m).1 + (pellXY m).2)

/-- `x_m`. -/
def px (m : ℕ) : ℤ := (pellXY m).1
/-- `y_m`. -/
def py (m : ℕ) : ℤ := (pellXY m).2

theorem px_succ (m : ℕ) : px (m + 1) = px m + 2 * py m := rfl
theorem py_succ (m : ℕ) : py (m + 1) = px m + py m := rfl
theorem px_zero : px 0 = 1 := rfl
theorem py_zero : py 0 = 0 := rfl

theorem catC_sq : catC ^ 2 = catS := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [catC, catS, sq, Matrix.mul_apply, Fin.sum_univ_two]

theorem catC_pow (m : ℕ) : catC ^ m = !![px m, 2 * py m; py m, px m] := by
  induction m with
  | zero => ext i j; fin_cases i <;> fin_cases j <;> simp [px, py, pellXY]
  | succ m ih =>
    rw [pow_succ, ih]
    ext i j; fin_cases i <;> fin_cases j <;>
      simp [catC, Matrix.mul_apply, Fin.sum_univ_two, px_succ, py_succ] <;> ring

/-- Pell identity `x_m² - 2y_m² = (-1)^m`. -/
theorem pell_xy (m : ℕ) : px m ^ 2 - 2 * py m ^ 2 = (-1) ^ m := by
  induction m with
  | zero => simp [px, py, pellXY]
  | succ m ih => rw [px_succ, py_succ, pow_succ (-1 : ℤ), ← ih]; ring

theorem pxy_nonneg (m : ℕ) : 1 ≤ px m ∧ 0 ≤ py m := by
  induction m with
  | zero => simp [px, py, pellXY]
  | succ m ih => rw [px_succ, py_succ]; constructor <;> linarith [ih.1, ih.2]

theorem px_mono : Monotone px :=
  monotone_nat_of_le_succ fun m => by rw [px_succ]; linarith [(pxy_nonneg m).2]

theorem py_mono : Monotone py :=
  monotone_nat_of_le_succ fun m => by rw [py_succ]; linarith [(pxy_nonneg m).1]

theorem catS_pow_eq_sq (m : ℕ) : catS ^ m = (catC ^ m) ^ 2 := by
  rw [← catC_sq, ← pow_mul, ← pow_mul, mul_comm]

theorem pell_odd {m : ℕ} (hm : Odd m) : px m ^ 2 - 2 * py m ^ 2 = -1 := by
  rw [pell_xy, hm.neg_one_pow]

theorem pell_even {m : ℕ} (hm : Even m) : px m ^ 2 - 2 * py m ^ 2 = 1 := by
  rw [pell_xy, hm.neg_one_pow]

/-- `Sᵐ - 1 = 2 x_m Cᵐ` for odd `m`. -/
theorem catS_pow_sub_one_odd {m : ℕ} (hm : Odd m) : catS ^ m - 1 = (2 * px m) • catC ^ m := by
  have h := pell_odd hm
  rw [catS_pow_eq_sq, catC_pow]
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [sq] <;> nlinarith [h]

/-- `Sᵐ - 1 = 2 y_m J Cᵐ` for even `m`. -/
theorem catS_pow_sub_one_even {m : ℕ} (hm : Even m) :
    catS ^ m - 1 = (2 * py m) • (catJ * catC ^ m) := by
  have h := pell_even hm
  rw [catS_pow_eq_sq, catC_pow]
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [catJ, sq] <;> nlinarith [h]

/-- Periodic-point count for odd `m`: `det(Sᵐ - 1) = -4 x_m²`. -/
theorem fix_count_odd {m : ℕ} (hm : Odd m) : (catS ^ m - 1).det = -4 * px m ^ 2 := by
  have h := pell_odd hm
  rw [catS_pow_eq_sq, catC_pow, Matrix.det_fin_two]
  simp [sq]
  nlinarith [h]

/-- Periodic-point count for even `m`: `det(Sᵐ - 1) = -8 y_m²`. -/
theorem fix_count_even {m : ℕ} (hm : Even m) : (catS ^ m - 1).det = -8 * py m ^ 2 := by
  have h := pell_even hm
  rw [catS_pow_eq_sq, catC_pow, Matrix.det_fin_two]
  simp [sq]
  nlinarith [h]

/-- Annihilator lattice for odd `m`: `(Sᵐ - 1)ᵀ ℤ² = 2x_m ℤ × 2x_m ℤ`. -/
theorem annihilator_odd {m : ℕ} (hm : Odd m) (v : Fin 2 → ℤ) :
    (∃ w, (catS ^ m - 1)ᵀ *ᵥ w = v) ↔ (2 * px m ∣ v 0 ∧ 2 * px m ∣ v 1) := by
  have h := pell_odd hm
  rw [catS_pow_sub_one_odd hm, catC_pow]
  constructor
  · rintro ⟨w, rfl⟩
    simp [Matrix.mulVec, dotProduct, Fin.sum_univ_two, Matrix.transpose_apply]
    constructor
    · exact ⟨px m * w 0 + py m * w 1, by ring⟩
    · exact ⟨2 * py m * w 0 + px m * w 1, by ring⟩
  · rintro ⟨⟨a, ha⟩, ⟨b, hb⟩⟩
    refine ⟨![-px m * a + py m * b, 2 * py m * a - px m * b], ?_⟩
    ext i; fin_cases i
    · simp [Matrix.mulVec, dotProduct, Fin.sum_univ_two, Matrix.transpose_apply, ha]
      linear_combination (-(2 * px m * a)) * h
    · simp [Matrix.mulVec, dotProduct, Fin.sum_univ_two, Matrix.transpose_apply, hb]
      linear_combination (-(2 * px m * b)) * h

/-- Annihilator lattice for even `m`: `(Sᵐ - 1)ᵀ ℤ² = 2y_m ℤ × 4y_m ℤ`. -/
theorem annihilator_even {m : ℕ} (hm : Even m) (v : Fin 2 → ℤ) :
    (∃ w, (catS ^ m - 1)ᵀ *ᵥ w = v) ↔ (2 * py m ∣ v 0 ∧ 4 * py m ∣ v 1) := by
  have h := pell_even hm
  rw [catS_pow_sub_one_even hm, catC_pow]
  constructor
  · rintro ⟨w, rfl⟩
    simp [catJ, Matrix.mulVec, dotProduct, Fin.sum_univ_two, Matrix.transpose_apply]
    constructor
    · exact ⟨2 * py m * w 0 + px m * w 1, by ring⟩
    · exact ⟨px m * w 0 + py m * w 1, by ring⟩
  · rintro ⟨⟨a, ha⟩, ⟨b, hb⟩⟩
    refine ⟨![-py m * a + px m * b, px m * a - 2 * py m * b], ?_⟩
    ext i; fin_cases i
    · simp [catJ, Matrix.mulVec, dotProduct, Fin.sum_univ_two, Matrix.transpose_apply, ha]
      linear_combination (2 * py m * a) * h
    · simp [catJ, Matrix.mulVec, dotProduct, Fin.sum_univ_two, Matrix.transpose_apply, hb]
      linear_combination (4 * py m * b) * h

/-- The shortest annihilator frequencies `ℓ₁, …, ℓ₆ = 2, 4, 14, 24, 82, 140`. -/
theorem ell_values :
    (2 * px 1, 2 * py 2, 2 * px 3, 2 * py 4, 2 * px 5, 2 * py 6) = (2, 4, 14, 24, 82, 140) := by
  decide

/-- `ℓ_m ≥ 14` for every `m ≥ 3`. -/
theorem ell_ge_fourteen {m : ℕ} (hm : 3 ≤ m) :
    (Odd m → 14 ≤ 2 * px m) ∧ (Even m → 14 ≤ 2 * py m) := by
  constructor
  · intro _
    have := px_mono hm
    have h3 : px 3 = 7 := by decide
    omega
  · intro he
    have h4 : 4 ≤ m := by
      rcases he with ⟨k, hk⟩; omega
    have := py_mono h4
    have h4' : py 4 = 12 := by decide
    omega

#print axioms px_succ
#print axioms py_succ
#print axioms px_zero
#print axioms py_zero
#print axioms catC_sq
#print axioms catC_pow
#print axioms pell_xy
#print axioms pxy_nonneg
#print axioms px_mono
#print axioms py_mono
#print axioms catS_pow_eq_sq
#print axioms pell_odd
#print axioms pell_even
#print axioms catS_pow_sub_one_odd
#print axioms catS_pow_sub_one_even
#print axioms fix_count_odd
#print axioms fix_count_even
#print axioms annihilator_odd
#print axioms annihilator_even
#print axioms ell_values
#print axioms ell_ge_fourteen
end Bgs.Mathlib
