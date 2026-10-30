module
public import Mathlib
@[expose] public section

/-!
# Eigenlines of hyperbolic matrices in `SL(2,ℤ)` have irrational slope
(arithmetic input of `mathematics/foundations/analytic_bracket_rigidity.md`)

The density step of the analytic bracket-rigidity proof uses: *an eigenline of a hyperbolic
integral determinant-one matrix has irrational slope.*

* `hyperbolic_eigenvalue_irrational`: if `|t| > 2` and `μ² − tμ + 1 = 0`, then `μ` is
  irrational.
* `hyperbolic_eigenline_irrational`: if `S ∈ M₂(ℤ)`, `det S = 1`, `|tr S| > 2`, and `v ≠ 0` is a
  real eigenvector, then `v₁ ≠ 0` and the slope `v₀/v₁` is irrational (in particular `v₀ ≠ 0`
  as well).
* `catS_eigenline_irrational`: the case of the project matrix `S = [[3,4],[2,3]]`.
-/

open Matrix

namespace Bgs.Mathlib

/-- No integer square equals `t² − 4` when `|t| > 2`. -/
lemma int_sq_ne_sq_sub_four {t k : ℤ} (ht : 2 < |t|) : k ^ 2 ≠ t ^ 2 - 4 := by
  intro h
  have hk : |k| < |t| := by
    exact sq_lt_sq.1 (by linarith)
  have hk' : |k| ≤ |t| - 1 := by omega
  have h0 : 0 ≤ |k| := abs_nonneg k
  have : |k| ^ 2 ≤ (|t| - 1) ^ 2 := pow_le_pow_left₀ h0 hk' 2
  rw [sq_abs] at this
  have : (|t| - 1) ^ 2 = t ^ 2 - 2 * |t| + 1 := by rw [sub_sq, sq_abs]; ring
  nlinarith

/-- Eigenvalues of hyperbolic integral matrices of determinant one are irrational. -/
theorem hyperbolic_eigenvalue_irrational {t : ℤ} (ht : 2 < |t|) {μ : ℝ}
    (hμ : μ ^ 2 - t * μ + 1 = 0) : Irrational μ := by
  rintro ⟨q, rfl⟩
  set x : ℝ := 2 * (q : ℝ) - t with hx
  have hx2 : x ^ 2 = ((t ^ 2 - 4 : ℤ) : ℝ) := by
    push_cast; rw [hx]; linear_combination 4 * hμ
  by_cases hint : ∃ k : ℤ, x = k
  · obtain ⟨k, hk⟩ := hint
    rw [hk] at hx2
    exact int_sq_ne_sq_sub_four ht (by exact_mod_cast hx2)
  · have hirr : Irrational x := irrational_nrt_of_notint_nrt 2 (t ^ 2 - 4) hx2 hint two_pos
    exact hirr ⟨2 * q - t, by rw [hx]; push_cast; ring⟩

/-- **Eigenlines of hyperbolic `SL(2,ℤ)` matrices have irrational slope.** -/
theorem hyperbolic_eigenline_irrational (S : Matrix (Fin 2) (Fin 2) ℤ) (hdet : S.det = 1)
    (htr : 2 < |S.trace|) (v : Fin 2 → ℝ) (hv : v ≠ 0) (μ : ℝ)
    (hev : (S.map (Int.cast : ℤ → ℝ)) *ᵥ v = μ • v) :
    v 1 ≠ 0 ∧ Irrational (v 0 / v 1) := by
  have e0 := congrFun hev 0
  have e1 := congrFun hev 1
  simp only [mulVec, dotProduct, Fin.sum_univ_two, map_apply, Pi.smul_apply,
    smul_eq_mul] at e0 e1
  rw [det_fin_two] at hdet
  have htrace : S.trace = S 0 0 + S 1 1 := by simp [trace, Fin.sum_univ_two]
  have hdetR : (S 0 0 : ℝ) * S 1 1 - S 0 1 * S 1 0 = 1 := by exact_mod_cast hdet
  -- characteristic equation
  have hchar : μ ^ 2 - ((S.trace : ℤ) : ℝ) * μ + 1 = 0 := by
    rw [htrace]; push_cast
    have h0 : (μ ^ 2 - (S 0 0 + S 1 1) * μ + 1) * v 0 = 0 := by
      linear_combination ((S 1 1 : ℝ) - μ) * e0 - (S 0 1 : ℝ) * e1 - v 0 * hdetR
    have h1 : (μ ^ 2 - (S 0 0 + S 1 1) * μ + 1) * v 1 = 0 := by
      linear_combination -(S 1 0 : ℝ) * e0 + ((S 0 0 : ℝ) - μ) * e1 - v 1 * hdetR
    by_contra hne
    apply hv
    funext i
    fin_cases i
    · exact (mul_eq_zero.1 h0).resolve_left hne
    · exact (mul_eq_zero.1 h1).resolve_left hne
  have hirr := hyperbolic_eigenvalue_irrational htr hchar
  have hv1 : v 1 ≠ 0 := by
    intro h1
    rw [h1] at e0 e1
    have hv0 : v 0 ≠ 0 := by
      intro h0; apply hv; funext i; fin_cases i <;> simp [h0, h1]
    have : μ = S 0 0 := by
      have := mul_right_cancel₀ hv0 (show μ * v 0 = (S 0 0 : ℝ) * v 0 by linarith)
      exact this
    exact hirr ⟨S 0 0, by rw [this]; push_cast; rfl⟩
  refine ⟨hv1, ?_⟩
  rintro ⟨q, hq⟩
  -- the second eigen-equation gives `μ = S₁₀ q + S₁₁`
  have hμ : μ = S 1 0 * (q : ℝ) + S 1 1 := by
    have hv0 : v 0 = q * v 1 := by rw [hq]; field_simp
    rw [hv0] at e1
    exact (mul_right_cancel₀ hv1 (by linarith : μ * v 1 = (S 1 0 * q + S 1 1) * v 1))
  exact hirr ⟨S 1 0 * q + S 1 1, by rw [hμ]; push_cast; ring⟩

/-- The project cat map `S = [[3,4],[2,3]]` has irrational eigenline slopes. -/
theorem catS_eigenline_irrational (v : Fin 2 → ℝ) (hv : v ≠ 0) (μ : ℝ)
    (hev : ((!![3, 4; 2, 3] : Matrix (Fin 2) (Fin 2) ℤ).map (Int.cast : ℤ → ℝ)) *ᵥ v = μ • v) :
    v 1 ≠ 0 ∧ Irrational (v 0 / v 1) :=
  hyperbolic_eigenline_irrational _ (by simp [det_fin_two])
    (by simp [trace, Fin.sum_univ_two]) v hv μ hev

#print axioms int_sq_ne_sq_sub_four
#print axioms hyperbolic_eigenvalue_irrational
#print axioms hyperbolic_eigenline_irrational
#print axioms catS_eigenline_irrational
end Bgs.Mathlib
