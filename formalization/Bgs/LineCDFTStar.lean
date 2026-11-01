import Mathlib.Analysis.SpecialFunctions.Complex.CircleAddChar
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Diagonal

/-!
# BGS-TRACE-143 — Theorem 1 (matrix identities): the Haar diagonal-phase cat map is conjugate to `D_θ′ F`

Source: `mathematics/fixed-map/random_phase_encounter_pairs.md`, Theorem 1; registry boundary of `BGS-TRACE-143`.
`N` odd (encoded by a unit `i8 = 8⁻¹` in `ℤ/N`, `8·i8 = 1`), `e_N(x) = ψ(x) = e(x/N)` (`ZMod.stdAddChar`),
`M_N(x, y) = N^{−1/2} e_N(−8⁻¹(3x² − 2xy + 3y²))`, `Δ = diag e_N(−3·8⁻¹x²)`, `F_c(x, y) = N^{−1/2} e_N(cxy)`, `F = F_1`,
`(Pf)(x) = f(2x)` (matrix `P x y = 1[y = 2x]`), `D_θ = diag e^{iθ_x}`.

* `M_eq` : `M_N = Δ F_{1/4} Δ` (with `4⁻¹ = 2·i8`);
* `P_F_eq` : `P F_{1/4} = F P`, i.e. `P F_{1/4} P⁻¹ = F`;
* `conj_DFT` : `(PΔ)(D_θ M_N) = (D_{θ′} F)(PΔ)` with `θ′_x = θ_{2x} − 2π·(6·8⁻¹(2x)²)/N` (residue representative), i.e.
  `D_θ M_N` is conjugate to `D_{θ′} F` by the monomial matrix `PΔ`;
* `PDelta_unitary` : `(PΔ)(PΔ)ᴴ = 1` (so the conjugation is unitary).

**Partial coverage:** the measure-preserving property of `θ ↦ θ′` (coordinate permutation plus translation of `𝕋^N`) and
the resulting equality of eigenvalue laws, the identification with the Gnutzmann–Seif class-AI star graph, the square-class
statement for a general cross coefficient (Remark 1′), the sign flip at primes `p ≡ 1 mod 4` (e.g. `p = 13, m = 4`) and the
floating-point checks are **not** formalized.  All proofs are kernel-checked.
-/

namespace Bgs.LineCDFTStar

open Matrix ComplexConjugate

variable {N : ℕ} [NeZero N] (i8 : ZMod N) (h8 : 8 * i8 = 1)

noncomputable abbrev ψ : AddChar (ZMod N) ℂ := ZMod.stdAddChar

noncomputable def c0 (N : ℕ) : ℂ := ((Real.sqrt N : ℝ) : ℂ)⁻¹

noncomputable def M : Matrix (ZMod N) (ZMod N) ℂ :=
  Matrix.of fun x y => c0 N * (ψ : AddChar (ZMod N) ℂ) (-(i8 * (3 * x ^ 2 - 2 * x * y + 3 * y ^ 2)))

noncomputable def Δ : Matrix (ZMod N) (ZMod N) ℂ :=
  diagonal fun x => (ψ : AddChar (ZMod N) ℂ) (-(3 * i8 * x ^ 2))

noncomputable def Fc (c : ZMod N) : Matrix (ZMod N) (ZMod N) ℂ :=
  Matrix.of fun x y => c0 N * (ψ : AddChar (ZMod N) ℂ) (c * x * y)

def P : Matrix (ZMod N) (ZMod N) ℂ := Matrix.of fun x y => if y = 2 * x then 1 else 0

noncomputable def D (θ : ZMod N → ℝ) : Matrix (ZMod N) (ZMod N) ℂ :=
  diagonal fun x => Complex.exp ((θ x : ℂ) * Complex.I)

noncomputable def θ' (θ : ZMod N → ℝ) (x : ZMod N) : ℝ :=
  θ (2 * x) - 2 * Real.pi * ((6 * i8 * (2 * x) ^ 2 : ZMod N).val : ℝ) / N

theorem M_eq : M i8 = Δ i8 * Fc (2 * i8) * Δ i8 := by
  ext x y
  simp only [M, Δ, Fc, of_apply, mul_diagonal, diagonal_mul]
  have : (ψ : AddChar (ZMod N) ℂ) (-(i8 * (3 * x ^ 2 - 2 * x * y + 3 * y ^ 2)))
      = (ψ : AddChar (ZMod N) ℂ) (-(3 * i8 * x ^ 2)) * (ψ : AddChar (ZMod N) ℂ) (2 * i8 * x * y)
        * (ψ : AddChar (ZMod N) ℂ) (-(3 * i8 * y ^ 2)) := by
    rw [← AddChar.map_add_eq_mul, ← AddChar.map_add_eq_mul]; congr 1; ring
  rw [this]; ring

theorem P_mul (A : Matrix (ZMod N) (ZMod N) ℂ) (x y : ZMod N) :
    ((P : Matrix (ZMod N) (ZMod N) ℂ) * A) x y = A (2 * x) y := by
  simp only [P, mul_apply, of_apply, ite_mul, one_mul, zero_mul]
  rw [Finset.sum_ite_eq']; simp

include h8 in
theorem mul_P (A : Matrix (ZMod N) (ZMod N) ℂ) (x y : ZMod N) :
    (A * (P : Matrix (ZMod N) (ZMod N) ℂ)) x y = A x (4 * i8 * y) := by
  simp only [P, mul_apply, of_apply, mul_ite, mul_one, mul_zero]
  rw [Finset.sum_eq_single (4 * i8 * y)]
  · have : y = 2 * (4 * i8 * y) := by linear_combination (-y) * h8
    simp [← this]
  · intro b _ hb
    have : y ≠ 2 * b := by
      intro h; apply hb; rw [h]; linear_combination (-b) * h8
    simp [this]
  · simp

include h8 in
theorem P_F_eq : P * Fc (2 * i8) = Fc 1 * P := by
  ext x y
  rw [P_mul, mul_P i8 h8]
  simp only [Fc, of_apply]
  congr 2
  ring

theorem psi_neg_val (a : ZMod N) :
    (ψ : AddChar (ZMod N) ℂ) (-a) = Complex.exp (-(2 * Real.pi * ((a.val : ℝ) / N) : ℝ) * Complex.I) := by
  rw [AddChar.map_neg_eq_conj, ZMod.stdAddChar_apply, ZMod.toCircle_apply, ← Complex.exp_conj]
  congr 1
  simp only [map_div₀, map_mul, Complex.conj_ofReal, Complex.conj_I, map_natCast, map_ofNat]
  push_cast; ring

include h8 in
/-- `(PΔ)(D_θ M_N) = (D_{θ′} F)(PΔ)`. -/
theorem conj_DFT (θ : ZMod N → ℝ) :
    (P * Δ i8) * (D θ * M i8) = (D (θ' i8 θ) * Fc 1) * (P * Δ i8) := by
  ext x y
  rw [Matrix.mul_assoc P, P_mul, ← Matrix.mul_assoc (D (θ' i8 θ) * Fc 1) P (Δ i8)]
  rw [Δ, mul_diagonal, mul_P i8 h8, diagonal_mul]
  simp only [D, M, Fc, of_apply, diagonal_mul]
  have hθ : Complex.exp (((θ' i8 θ x : ℝ) : ℂ) * Complex.I)
      = Complex.exp ((θ (2 * x) : ℂ) * Complex.I) * (ψ : AddChar (ZMod N) ℂ) (-(6 * i8 * (2 * x) ^ 2)) := by
    rw [psi_neg_val, ← Complex.exp_add]
    congr 1
    unfold θ'; push_cast; ring
  rw [hθ]
  have e1 : (ψ : AddChar (ZMod N) ℂ) (-(3 * i8 * (2 * x) ^ 2))
      * (ψ : AddChar (ZMod N) ℂ) (-(i8 * (3 * (2 * x) ^ 2 - 2 * (2 * x) * y + 3 * y ^ 2)))
      = (ψ : AddChar (ZMod N) ℂ) (-(6 * i8 * (2 * x) ^ 2))
      * (ψ : AddChar (ZMod N) ℂ) (1 * x * (4 * i8 * y)) * (ψ : AddChar (ZMod N) ℂ) (-(3 * i8 * y ^ 2)) := by
    rw [← AddChar.map_add_eq_mul, ← AddChar.map_add_eq_mul, ← AddChar.map_add_eq_mul]
    congr 1; ring
  linear_combination (Complex.exp ((θ (2 * x) : ℂ) * Complex.I) * c0 N) * e1

theorem Delta_mul_star : Δ i8 * (Δ i8)ᴴ = 1 := by
  simp only [Δ, diagonal_conjTranspose, diagonal_mul_diagonal]
  rw [← diagonal_one]; congr 1; funext x
  rw [Pi.star_apply, show star ((ψ : AddChar (ZMod N) ℂ) (-(3 * i8 * x ^ 2)))
      = conj ((ψ : AddChar (ZMod N) ℂ) (-(3 * i8 * x ^ 2))) from rfl,
    ← AddChar.map_neg_eq_conj, ← AddChar.map_add_eq_mul, add_neg_cancel, AddChar.map_zero_eq_one]

include h8 in
theorem P_mul_star : P * (P : Matrix (ZMod N) (ZMod N) ℂ)ᴴ = 1 := by
  ext x y
  rw [P_mul]
  simp only [P, conjTranspose_apply, of_apply, one_apply]
  by_cases hxy : x = y
  · subst hxy; rw [if_pos rfl, if_pos rfl, star_one]
  · have : ¬ (2 * x = 2 * y) := by
      intro h; apply hxy
      linear_combination (4 * i8) * h - (x - y) * h8
    rw [if_neg this, if_neg hxy, star_zero]

include h8 in
theorem PDelta_unitary : (P * Δ i8) * (P * Δ i8)ᴴ = 1 := by
  rw [conjTranspose_mul, Matrix.mul_assoc, ← Matrix.mul_assoc (Δ i8), Delta_mul_star, Matrix.one_mul,
    P_mul_star i8 h8]

end Bgs.LineCDFTStar
