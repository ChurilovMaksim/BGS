import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Data.Matrix.Mul
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FinCases

/-!
# BGS-FM-009 — integer arithmetic of `S³ − I` (finite kernel)

Source: `mathematics/fixed-map/frozen_common_antireversor_certificate.md`,
the paragraph after equation (4).  With `S = [[3,4],[2,3]]`:

* `S_cube : S³ = [[99,140],[70,99]]`;
* `S_cube_sub_one : S³ − I = 14 · B` with `B = [[7,10],[5,7]]`;
* `det_B : det B = −1`, hence `det (S³ − I) = −196`
  (`det_S_cube_sub_one`);
* `det_unit_of_coprime` : for every `N` coprime to `14` (in particular every
  odd `N` with `7 ∤ N`), `det (S³ − I)` is a unit in `ZMod N`, i.e.
  `I − S³` is invertible modulo `N` (the source's "for `7 ∤ N`, `I − S³` is
  invertible modulo `N`").

**Scope.** This complements `Bgs.Fm009TraceObstruction` (the implication
"common reversor ⇒ `Tr [A,M]³ = 0`").  Not formalized: the metaplectic
character formula, `|Tr M_N³| = gcd(N, 7)`, the Laurent-polynomial
identity (4), and the cyclotomic exclusion behind `Tr [A_N, M_N]³ ≠ 0`.
No `sorry`, no `native_decide`.
-/

namespace Bgs.Fm009CubeArith

open Matrix

/-- The cat matrix `S = [[3,4],[2,3]]`. -/
def S : Matrix (Fin 2) (Fin 2) ℤ := !![3, 4; 2, 3]

/-- `B = [[7,10],[5,7]]`. -/
def B : Matrix (Fin 2) (Fin 2) ℤ := !![7, 10; 5, 7]

theorem S_cube : S ^ 3 = !![99, 140; 70, 99] := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [S, pow_succ, Matrix.mul_apply, Fin.sum_univ_two]

theorem S_cube_sub_one : S ^ 3 - 1 = (14 : ℤ) • B := by
  rw [S_cube]
  ext i j; fin_cases i <;> fin_cases j <;> simp [B]

theorem det_B : B.det = -1 := by
  simp [B, Matrix.det_fin_two]

theorem det_S_cube_sub_one : (S ^ 3 - 1).det = -196 := by
  rw [S_cube_sub_one, Matrix.det_smul, det_B]; simp

/-- For `N` coprime to `14`, `det (S³ − I) = −196` is a unit modulo `N`. -/
theorem det_unit_of_coprime (N : ℕ) (hN : Nat.Coprime 14 N) :
    IsUnit (((S ^ 3 - 1).det : ℤ) : ZMod N) := by
  rw [det_S_cube_sub_one]
  have h196 : Nat.Coprime 196 N := by
    have : (196 : ℕ) = 14 ^ 2 := by norm_num
    rw [this]; exact Nat.Coprime.pow_left 2 hN
  have hu : IsUnit ((196 : ℕ) : ZMod N) := (ZMod.unitOfCoprime 196 h196).isUnit
  have : (((-196 : ℤ)) : ZMod N) = -((196 : ℕ) : ZMod N) := by push_cast; ring
  rw [this]; exact hu.neg

end Bgs.Fm009CubeArith
