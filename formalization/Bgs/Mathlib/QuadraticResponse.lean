module
public import Mathlib
@[expose] public section

/-!
# Exact limits of quadratic-response data

Source: `mathematics/information-theory/quadratic_response_limits.md`.

**§1–2, exact arithmetic.**
* `allpass_identity`: `P(Z)P(Z⁻¹) = Q(Z)Q(Z⁻¹)` for `P(Z) = 1 - Z/2`, `Q(Z) = Z - 1/2`.
* `orbit_determinants`: for `A = (2,1;1,1)`, `v = (1,0)`, `w = Av`, `z = v + w`:
  `det(v, Av) = 1`, `det(z, Az) = 5` (so `v` and `z` lie on different orbits).
* `tail_symbol_constants`: `4π²·25/(3² - 4) = 20π²`, `P(λ)P(λ⁻¹) = -1/4` for
  `λ = (3+√5)/2`, and `20π² · 1/16 = 5π²/4`.
* `third_moments`: from `∫a³ = 24`, `∫a²·Ca = 4`, `∫a·(Ca)² = 16` and invariance
  `∫(Ca)³ = ∫a³`, the filtered seeds satisfy `∫f³ = 27`, `∫h³ = 0`.

**§4, cyclic-quantum transfer obstruction.**
* `lag_periodic`, `lag_at_period`: if `U` is unitary and `U^K = c·1` (`|c| = 1`), then
  `H_{r+K} = H_r` and `H_K = 0` for `H_r = (iN/2)[G, U^r G U^{-r}]`.
* `gram_singular_of_zero`: any Gram matrix (for an arbitrary sesquilinear pairing) of a
  family containing a zero member is singular; hence any Gram block of `H_1, …, H_m` with
  `m ≥ K` is singular (`lag_gram_singular`).
* `coercive_far_from_singular`: if `Re⟨x, A x⟩ ≥ c‖x‖²` for all `x` and `B` is singular,
  then `‖A - B‖ ≥ c` in operator norm.
-/

open Matrix Finset

namespace Bgs.Mathlib

/-! ## §1–2 -/

theorem allpass_identity {K : Type*} [Field K] (Z : K) (hZ : Z ≠ 0) :
    (1 - Z / 2) * (1 - Z⁻¹ / 2) = (Z - 1 / 2) * (Z⁻¹ - 1 / 2) := by
  field_simp

theorem orbit_determinants :
    let A : Matrix (Fin 2) (Fin 2) ℤ := !![2, 1; 1, 1]
    let v : Fin 2 → ℤ := ![1, 0]
    let w := A *ᵥ v
    let z := v + w
    Matrix.det (Matrix.of ![v, A *ᵥ v]) = 1 ∧ Matrix.det (Matrix.of ![z, A *ᵥ z]) = 5 := by
  intro A v w z
  simp only [A, v, w, z]
  constructor
  · simp [Matrix.det_fin_two, vecHead]
  · simp [Matrix.det_fin_two, vecHead, vecTail]

theorem tail_symbol_constants :
    4 * Real.pi ^ 2 * 25 / (3 ^ 2 - 4) = 20 * Real.pi ^ 2 ∧
    (let lam := (3 + Real.sqrt 5) / 2
     (1 - lam / 2) * (1 - lam⁻¹ / 2) = -1 / 4) ∧
    20 * Real.pi ^ 2 * (1 / 16) = 5 * Real.pi ^ 2 / 4 := by
  refine ⟨by ring, ?_, by ring⟩
  intro lam
  have h5 : Real.sqrt 5 ^ 2 = 5 := Real.sq_sqrt (by norm_num)
  have hpos : 0 < lam := by simp only [lam]; positivity
  have hinv : lam⁻¹ = (3 - Real.sqrt 5) / 2 := by
    apply inv_eq_of_mul_eq_one_right
    simp only [lam]
    nlinarith
  rw [hinv]; simp only [lam]; nlinarith

/-- **§2.**  Third moments of the filtered seeds `f = a - Ca/2`, `h = Ca - a/2`, from the
three exact Fourier integrals and the invariance `∫(Ca)³ = ∫a³`. -/
theorem third_moments {I3 I21 I12 I03 : ℝ} (h3 : I3 = 24) (h21 : I21 = 4) (h12 : I12 = 16)
    (hinv : I03 = I3) :
    -- `∫(a - Ca/2)³` expanded with `I3 = ∫a³`, `I21 = ∫a²Ca`, `I12 = ∫a(Ca)²`, `I03 = ∫(Ca)³`
    I3 - 3 / 2 * I21 + 3 / 4 * I12 - 1 / 8 * I03 = 27 ∧
    I03 - 3 / 2 * I12 + 3 / 4 * I21 - 1 / 8 * I3 = 0 := by
  subst h3 h21 h12; rw [hinv]
  constructor <;> norm_num

/-! ## §4: cyclic quantum maps -/

section Cyclic

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- The conjugated observable `U^r G U^{-r}` (with `U^{-1} = Uᴴ`). -/
noncomputable def conjPow (U G : Matrix n n ℂ) (r : ℕ) : Matrix n n ℂ := U ^ r * G * (Uᴴ) ^ r

/-- The lag observable `H_r = (iN/2)[G, U^r G U^{-r}]`. -/
noncomputable def lagObs (N : ℝ) (U G : Matrix n n ℂ) (r : ℕ) : Matrix n n ℂ :=
  (Complex.I * N / 2) • (G * conjPow U G r - conjPow U G r * G)

lemma conjTranspose_pow_scalar {U : Matrix n n ℂ} {K : ℕ} {c : ℂ} (hK : U ^ K = c • 1) :
    (Uᴴ) ^ K = star c • 1 := by
  rw [← conjTranspose_pow, hK, conjTranspose_smul, conjTranspose_one]

/-- `H_{r+K} = H_r` when `U^K = c·1` with `|c| = 1`. -/
theorem conjPow_periodic {U G : Matrix n n ℂ} {K : ℕ} {c : ℂ} (hK : U ^ K = c • 1)
    (hc : c * star c = 1) (r : ℕ) : conjPow U G (r + K) = conjPow U G r := by
  unfold conjPow
  rw [pow_add, pow_add, hK, conjTranspose_pow_scalar hK]
  simp only [Matrix.mul_smul, Matrix.smul_mul, Matrix.mul_one, smul_smul]
  rw [show (star c * c) = c * star c by ring, hc, one_smul]

theorem lag_periodic (N : ℝ) {U G : Matrix n n ℂ} {K : ℕ} {c : ℂ} (hK : U ^ K = c • 1)
    (hc : c * star c = 1) (r : ℕ) : lagObs N U G (r + K) = lagObs N U G r := by
  unfold lagObs; rw [conjPow_periodic hK hc]

/-- `H_K = 0`. -/
theorem lag_at_period (N : ℝ) {U G : Matrix n n ℂ} {K : ℕ} {c : ℂ} (hK : U ^ K = c • 1)
    (hc : c * star c = 1) : lagObs N U G K = 0 := by
  have h := conjPow_periodic (G := G) hK hc 0
  rw [zero_add] at h
  unfold lagObs
  rw [h]
  simp [conjPow]

/-- A Gram matrix `(B(H_a, H_b))_{a,b}` of a family with a zero member is singular, for any
sesquilinear (indeed, any additive-in-the-first-slot) pairing `B`. -/
theorem gram_singular_of_zero {ι V : Type*} [Fintype ι] [DecidableEq ι] [AddCommGroup V]
    (B : V →+ V → ℂ) (H : ι → V) {a : ι} (ha : H a = 0) :
    (Matrix.of fun i j => B (H i) (H j)).det = 0 := by
  apply det_eq_zero_of_row_eq_zero a
  intro j
  simp [ha]

/-- **§4.**  Any Gram block of `H_1, …, H_m` with `m ≥ K ≥ 1` is singular. -/
theorem lag_gram_singular (N : ℝ) {U G : Matrix n n ℂ} {K : ℕ} {c : ℂ} (hK : U ^ K = c • 1)
    (hc : c * star c = 1) (hK1 : 1 ≤ K) (m : ℕ) (hm : K ≤ m)
    (B : Matrix n n ℂ →+ Matrix n n ℂ → ℂ) :
    (Matrix.of fun i j : Fin m => B (lagObs N U G (i + 1)) (lagObs N U G (j + 1))).det = 0 :=
  gram_singular_of_zero B (fun i : Fin m => lagObs N U G (i + 1)) (a := ⟨K - 1, by omega⟩)
    (by simp only; rw [show K - 1 + 1 = K by omega]; exact lag_at_period N hK hc)

end Cyclic

section Coercive

open scoped Matrix.Norms.L2Operator

variable {m : Type*} [Fintype m] [DecidableEq m]

/-- **§4.**  If `A` is coercive, `Re⟨x, A x⟩ ≥ c ‖x‖²`, and `B` is singular, then
`‖A - B‖ ≥ c` in the operator norm. -/
theorem coercive_far_from_singular {A B : Matrix m m ℂ} {c : ℝ}
    (hA : ∀ x : EuclideanSpace ℂ m,
      c * ‖x‖ ^ 2 ≤ (inner ℂ x ((EuclideanSpace.equiv m ℂ).symm (A *ᵥ x))).re)
    (hB : B.det = 0) : c ≤ ‖A - B‖ := by
  obtain ⟨v, hv0, hv⟩ := Matrix.exists_mulVec_eq_zero_iff.mpr hB
  set x : EuclideanSpace ℂ m := (EuclideanSpace.equiv m ℂ).symm v
  have hx0 : x ≠ 0 := by
    intro h; apply hv0
    have := congrArg (EuclideanSpace.equiv m ℂ) h
    simpa [x] using this
  have hxpos : 0 < ‖x‖ := norm_pos_iff.mpr hx0
  have hAB : (A - B) *ᵥ x = A *ᵥ x := by
    have : B *ᵥ x = 0 := hv
    rw [sub_mulVec, this, sub_zero]
  have h1 := hA x
  have h2 : (inner ℂ x ((EuclideanSpace.equiv m ℂ).symm (A *ᵥ x))).re ≤
      ‖x‖ * ‖(EuclideanSpace.equiv m ℂ).symm (A *ᵥ x)‖ :=
    (Complex.re_le_norm _).trans (norm_inner_le_norm _ _)
  have h3 : ‖(EuclideanSpace.equiv m ℂ).symm ((A - B) *ᵥ x)‖ ≤ ‖A - B‖ * ‖x‖ :=
    l2_opNorm_mulVec _ _
  rw [hAB] at h3
  have : c * ‖x‖ ^ 2 ≤ ‖A - B‖ * ‖x‖ ^ 2 := by nlinarith
  exact le_of_mul_le_mul_right this (by positivity)

end Coercive

#print axioms allpass_identity
#print axioms orbit_determinants
#print axioms tail_symbol_constants
#print axioms third_moments
#print axioms conjTranspose_pow_scalar
#print axioms conjPow_periodic
#print axioms lag_periodic
#print axioms lag_at_period
#print axioms gram_singular_of_zero
#print axioms lag_gram_singular
#print axioms coercive_far_from_singular
end Bgs.Mathlib
