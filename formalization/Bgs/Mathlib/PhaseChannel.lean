module
public import Mathlib
@[expose] public section

/-!
# Elementary inputs of the max-entry phase channel (BGS-TRACE-053)

* Every entry of every positive power of a row-stochastic matrix with entries at most `δ`
  is at most `δ` (`stochastic_pow_entry_le`): "a stochastic row makes each new entry a convex
  combination of entries already at most `δ`".
* The degree-two coefficient bound `|S_ij S_ji| ≤ δ = max |S_ab|²` (`degree_two_coeff_le`).
* The unistochastic matrix `P_ij = |S_ij|²` of a unitary is doubly stochastic, so the first
  lemma applies to it (`unistochastic_pow_entry_le`).
-/

open Matrix BigOperators

namespace Bgs.Mathlib

/-- Positive powers of a nonnegative row-stochastic matrix with entries `≤ δ` have entries `≤ δ`. -/
theorem stochastic_pow_entry_le {m : ℕ} (P : Matrix (Fin m) (Fin m) ℝ) (δ : ℝ)
    (hnn : ∀ i j, 0 ≤ P i j) (hrow : ∀ i, ∑ j, P i j = 1) (hδ : ∀ i j, P i j ≤ δ) :
    ∀ n : ℕ, ∀ i j, (P ^ (n + 1)) i j ≤ δ := by
  intro n
  induction n with
  | zero => simpa using hδ
  | succ n ih =>
    intro i j
    rw [pow_succ', Matrix.mul_apply]
    calc ∑ k, P i k * (P ^ (n + 1)) k j ≤ ∑ k, P i k * δ :=
          Finset.sum_le_sum fun k _ => mul_le_mul_of_nonneg_left (ih k j) (hnn i k)
      _ = δ := by rw [← Finset.sum_mul, hrow, one_mul]

/-- The degree-two coefficient bound: `|S_ij S_ji| ≤ δ` whenever all `|S_ab|² ≤ δ`. -/
theorem degree_two_coeff_le {m : ℕ} (S : Matrix (Fin m) (Fin m) ℂ) (δ : ℝ)
    (hδ : ∀ a b, ‖S a b‖ ^ 2 ≤ δ) (i j : Fin m) : ‖S i j * S j i‖ ≤ δ := by
  rw [norm_mul]
  nlinarith [hδ i j, hδ j i, sq_nonneg (‖S i j‖ - ‖S j i‖)]

/-- For a unitary `S`, all positive powers of `P = |S|^{∘2}` have entries at most
`δ = max |S_ab|²`. -/
theorem unistochastic_pow_entry_le {m : ℕ} {S : Matrix (Fin m) (Fin m) ℂ}
    (hS : S ∈ Matrix.unitaryGroup (Fin m) ℂ) (δ : ℝ) (hδ : ∀ a b, ‖S a b‖ ^ 2 ≤ δ) (n : ℕ)
    (i j : Fin m) : ((Matrix.of fun a b => ‖S a b‖ ^ 2) ^ (n + 1)) i j ≤ δ := by
  apply stochastic_pow_entry_le _ δ (fun a b => by simp) _ (fun a b => by simpa using hδ a b)
  intro a
  have h : S * Sᴴ = 1 := Matrix.mem_unitaryGroup_iff.1 hS
  have := congrFun (congrFun h a) a
  simp only [Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.one_apply_eq] at this
  have h2 : ((∑ k, ‖S a k‖ ^ 2 : ℝ) : ℂ) = 1 := by
    rw [← this]; push_cast
    apply Finset.sum_congr rfl; intro k _
    rw [RCLike.star_def, Complex.mul_conj']
  simpa using (by exact_mod_cast h2 : (∑ k, ‖S a k‖ ^ 2 : ℝ) = 1)

end Bgs.Mathlib
