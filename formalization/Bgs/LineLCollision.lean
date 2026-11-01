import Mathlib.NumberTheory.Zsqrtd.Basic
import Mathlib.Algebra.Polynomial.Div
import Mathlib.Algebra.Polynomial.AlgebraMap
import Mathlib.Tactic.ComputeDegree
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.IntervalCases

/-!
# BGS-TRACE-248 — Line L collision structure (algebraic part)

Source: `mathematics/fixed-map/lineL_op_open_range.md`, §2
("Collision structure [P]").  With `λ = 3 + 2√2 ∈ ℤ[√2]` and
`α_v = ∑_j v_j λ^j = v(λ)` for an integer coefficient vector `v`
(equivalently an integer polynomial `v(X)`):

* `lam_minpoly` : `λ² − 6λ + 1 = 0`;
* `alpha_eq_zero_iff` : `v(λ) = 0 ↔ (X² − 6X + 1) ∣ v(X)` in `ℤ[X]`;
* `carry_coeff` : if `v = (X² − 6X + 1)·E`, then
  `v_j = e_j − 6 e_{j−1} + e_{j−2}` (with `e_{−1} = e_{−2} = 0`);
* `no_small_collision_k6` : the referee check — the only
  `v ∈ ℤ⁶` with `|v_j| ≤ 3` and `∑_{j<6} v_j λ^j = 0` is `v = 0`
  (for the index range `j = 0..5`; since `λ` is a unit, a shifted index
  range `j = s..s+5` gives the same zero set).

**Not formalized (partial coverage of BGS-TRACE-248):** the Green's-function
carry bound `|e_j| ≤ C0g ∑_i |v_i| λ^{−|j+1−i|}` with `C0g = 1/(λ − λ⁻¹)`,
and the transfer-matrix reading of the collision sums `S_k`.
No `sorry`, no `native_decide`.
-/

namespace Bgs.LineLCollision

open Polynomial

/-- `λ = 3 + 2√2` in `ℤ[√2]`. -/
def lam : ℤ√2 := ⟨3, 2⟩

/-- The collision polynomial `X² − 6X + 1`. -/
noncomputable def P : ℤ[X] := X ^ 2 - C 6 * X + 1

theorem lam_minpoly : lam ^ 2 - 6 * lam + 1 = 0 := by
  rw [Zsqrtd.ext_iff]
  simp [lam, pow_two]

theorem P_natDegree : P.natDegree = 2 := by
  unfold P; compute_degree!

theorem P_monic : P.Monic := by
  unfold Monic leadingCoeff
  rw [P_natDegree]
  simp [P, coeff_X, coeff_one]

theorem aeval_P : aeval lam P = 0 := by
  have := lam_minpoly
  simp only [P, map_add, map_sub, map_mul, map_pow, aeval_X, aeval_C, map_one]
  simpa using this

/-- **α_v = 0 iff (X² − 6X + 1) divides v(X).** -/
theorem alpha_eq_zero_iff (v : ℤ[X]) : aeval lam v = 0 ↔ P ∣ v := by
  constructor
  · intro hv
    rw [← modByMonic_eq_zero_iff_dvd P_monic]
    set r := v %ₘ P with hr
    have hsplit := modByMonic_add_div v P
    have hr0 : aeval lam r = 0 := by
      have h := congrArg (aeval lam) hsplit
      rw [map_add, map_mul, aeval_P, zero_mul, add_zero, hv] at h
      exact h
    have hP1 : P ≠ 1 := by
      intro h; have := P_natDegree; rw [h, natDegree_one] at this; exact absurd this (by decide)
    have hdeg : r.natDegree ≤ 1 := by
      have := natDegree_modByMonic_lt v P_monic hP1
      rw [P_natDegree, ← hr] at this
      omega
    have hform := eq_X_add_C_of_natDegree_le_one hdeg
    rw [hform] at hr0
    simp only [map_add, map_mul, aeval_C, aeval_X] at hr0
    rw [Zsqrtd.ext_iff] at hr0
    simp [lam] at hr0
    obtain ⟨h1, h2⟩ := hr0
    have hb : r.coeff 1 = 0 := by linarith
    have ha : r.coeff 0 = 0 := by rw [hb] at h1; linarith
    rw [hform, ha, hb]; simp
  · rintro ⟨E, rfl⟩
    rw [map_mul, aeval_P, zero_mul]

/-- **Carries:** if `v = (X² − 6X + 1) E` then
`v_{j+2} = e_{j+2} − 6 e_{j+1} + e_j`, `v_1 = e_1 − 6 e_0`, `v_0 = e_0`. -/
theorem carry_coeff (E : ℤ[X]) (j : ℕ) :
    (P * E).coeff (j + 2) = E.coeff (j + 2) - 6 * E.coeff (j + 1) + E.coeff j
    ∧ (P * E).coeff 1 = E.coeff 1 - 6 * E.coeff 0
    ∧ (P * E).coeff 0 = E.coeff 0 := by
  have hPE : P * E = X ^ 2 * E - C 6 * (X * E) + E := by unfold P; ring
  refine ⟨?_, ?_, ?_⟩ <;> rw [hPE]
  · simp only [coeff_add, coeff_sub, coeff_C_mul, coeff_X_pow_mul, coeff_X_mul]
    ring
  · simp only [coeff_add, coeff_sub, coeff_C_mul, coeff_X_mul]
    rw [coeff_X_pow_mul']; simp; ring
  · simp only [coeff_add, coeff_sub, coeff_C_mul]
    rw [coeff_X_pow_mul', coeff_X_mul_zero]; simp

/-- Powers `λ^j = x_j + y_j √2`, `j = 0..5`. -/
theorem lam_pows :
    lam ^ 0 = ⟨1, 0⟩ ∧ lam ^ 1 = ⟨3, 2⟩ ∧ lam ^ 2 = ⟨17, 12⟩ ∧
    lam ^ 3 = ⟨99, 70⟩ ∧ lam ^ 4 = ⟨577, 408⟩ ∧ lam ^ 5 = ⟨3363, 2378⟩ := by
  refine ⟨rfl, ?_, ?_, ?_, ?_, ?_⟩ <;>
    simp [lam, pow_succ, Zsqrtd.ext_iff]

/-- **Referee check (k = 6):** the only collision `∑_{j<6} v_j λ^j = 0`
with all `|v_j| ≤ 3` is `v = 0`. -/
theorem no_small_collision_k6 (v : Fin 6 → ℤ) (hb : ∀ j, |v j| ≤ 3)
    (hz : ∑ j : Fin 6, (v j : ℤ√2) * lam ^ (j : ℕ) = 0) : v = 0 := by
  obtain ⟨p0, p1, p2, p3, p4, p5⟩ := lam_pows
  simp only [Fin.sum_univ_six, Fin.val_zero, Fin.val_one, Fin.val_two] at hz
  rw [show ((3 : Fin 6) : ℕ) = 3 from rfl, show ((4 : Fin 6) : ℕ) = 4 from rfl,
    show ((5 : Fin 6) : ℕ) = 5 from rfl, p0, p1, p2, p3, p4, p5] at hz
  rw [Zsqrtd.ext_iff] at hz
  simp at hz
  obtain ⟨hre, him⟩ := hz
  have b0 := abs_le.mp (hb 0); have b1 := abs_le.mp (hb 1); have b2 := abs_le.mp (hb 2)
  have b3 := abs_le.mp (hb 3); have b4 := abs_le.mp (hb 4); have b5 := abs_le.mp (hb 5)
  have key : v 0 = 0 ∧ v 1 = 0 ∧ v 2 = 0 ∧ v 3 = 0 ∧ v 4 = 0 ∧ v 5 = 0 := by
    obtain ⟨l5, u5⟩ := b5
    obtain ⟨l4, u4⟩ := b4
    obtain ⟨l3, u3⟩ := b3
    interval_cases h5 : v 5 <;> interval_cases h4 : v 4 <;> interval_cases h3 : v 3 <;> omega
  funext j
  fin_cases j <;> simp [key]

end Bgs.LineLCollision
