import Mathlib.Data.Complex.Basic
import Mathlib.Data.Matrix.Mul
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic.NoncommRing
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum

/-! Algebraic trace-obstruction kernel for BGS-FM-009
    (`mathematics/fixed-map/frozen_common_antireversor_certificate.md`).

    Certified here: the necessary implication. If square matrices `A`
    and `M` over `ℂ` admit a common reversor in the following sense —
    there are matrices `Q`, `Q'` with `Q * Q' = 1` and `Q' * Q = 1`
    such that `Q' * A * Q = Aᵀ` and `Q' * M * Q = M`, and `M` is
    symmetric (`Mᵀ = M`) — then the trace of the commutator cube
    vanishes: `trace ([A, M]³) = 0`.

    The proof is the standard conjugation argument: conjugation by
    `Q'` sends the commutator to minus its transpose, hence sends its
    cube to minus the transpose of the cube, while the trace is
    invariant under both conjugation (by trace cyclicity) and
    transposition. So the trace equals its own negative, hence `0`
    in characteristic zero.

    NOT certified here: the nonzero computation `Tr[A_N, M_N]³ ≠ 0`
    (equation (1) of the source), which is the hard direction of
    FM-009 and rests on the deposited Laurent-polynomial certificate
    (2225-term `P`, 120-term `P₇`, cyclotomic exclusion). That
    computation remains project proof. This module certifies only the
    implication "common reversor ⇒ trace cube = 0", in the same kernel
    style as the other finite modules.

    Note: the proof below uses only `Q * Q' = 1` (the hypothesis
    `Q' * Q = 1` is stated, as `_hQ'Q`, for fidelity to the source, where
    `Q'` is the two-sided inverse, but is not needed for the trace identity). -/
namespace Bgs.Fm009TraceObstruction

open scoped Matrix

/-- If `A` and `M` admit a common reversor as above, the trace of the
    commutator cube vanishes. -/
theorem trace_cube_eq_zero_of_common_reversor {n : Type*} [Fintype n] [DecidableEq n]
    (A M Q Q' : Matrix n n ℂ)
    (hQQ' : Q * Q' = 1) (_hQ'Q : Q' * Q = 1)
    (hA : Q' * A * Q = Aᵀ) (hM : Q' * M * Q = M) (hMsym : Mᵀ = M) :
    Matrix.trace ((A * M - M * A) ^ 3) = 0 := by
  -- Conjugation by `Q'` distributes over products, using `Q * Q' = 1`
  -- to cancel the inserted middle factor.
  have insert : ∀ Y Z : Matrix n n ℂ, Q' * (Y * Z) * Q = (Q' * Y * Q) * (Q' * Z * Q) := by
    intro Y Z
    have h1 : (Q' * Y * Q) * (Q' * Z * Q) = Q' * Y * (Q * Q') * Z * Q := by
      noncomm_ring
    rw [h1, hQQ']
    noncomm_ring
  -- The conjugated commutator is minus the transposed commutator.
  have hX : Q' * (A * M - M * A) * Q = -((A * M - M * A)ᵀ) := by
    rw [mul_sub, sub_mul, insert, insert, hA, hM]
    rw [Matrix.transpose_sub, Matrix.transpose_mul, Matrix.transpose_mul, hMsym]
    noncomm_ring
  -- Conjugation distributes over the cube.
  have hCube : Q' * ((A * M - M * A) ^ 3) * Q = (Q' * (A * M - M * A) * Q) ^ 3 := by
    simp only [pow_three, insert, Matrix.mul_assoc]
  -- The trace equals its own negative.
  have hTr : Matrix.trace ((A * M - M * A) ^ 3)
      = -Matrix.trace ((A * M - M * A) ^ 3) := by
    have step1 : Matrix.trace ((A * M - M * A) ^ 3)
        = Matrix.trace (Q' * ((A * M - M * A) ^ 3) * Q) := by
      rw [Matrix.mul_assoc, Matrix.trace_mul_comm Q' (((A * M - M * A) ^ 3) * Q)]
      rw [Matrix.mul_assoc, hQQ', Matrix.mul_one]
    have hneg : (-((A * M - M * A)ᵀ)) ^ 3 = -(((A * M - M * A) ^ 3)ᵀ) := by
      rw [Matrix.transpose_pow]
      noncomm_ring
    calc Matrix.trace ((A * M - M * A) ^ 3)
        = Matrix.trace (Q' * ((A * M - M * A) ^ 3) * Q) := step1
      _ = Matrix.trace ((Q' * (A * M - M * A) * Q) ^ 3) := by rw [hCube]
      _ = Matrix.trace ((-((A * M - M * A)ᵀ)) ^ 3) := by rw [hX]
      _ = Matrix.trace (-(((A * M - M * A) ^ 3)ᵀ)) := by rw [hneg]
      _ = -Matrix.trace (((A * M - M * A) ^ 3)ᵀ) := by rw [Matrix.trace_neg]
      _ = -Matrix.trace ((A * M - M * A) ^ 3) := by rw [Matrix.trace_transpose]
  -- In characteristic zero, `t = -t` forces `t = 0`.
  have h3 : Matrix.trace ((A * M - M * A) ^ 3)
      + Matrix.trace ((A * M - M * A) ^ 3) = 0 := by
    linear_combination hTr
  have hne : (2 : ℂ) ≠ 0 := by exact_mod_cast (show (2 : ℕ) ≠ 0 by norm_num)
  have h20 : (2 : ℂ) * Matrix.trace ((A * M - M * A) ^ 3) = 0 := by
    rw [two_mul]
    exact h3
  exact (mul_eq_zero.mp h20).resolve_left hne

#print axioms trace_cube_eq_zero_of_common_reversor

end Bgs.Fm009TraceObstruction
