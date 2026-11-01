import Bgs.LineIAliasing
import Mathlib.LinearAlgebra.Matrix.Trace

/-!
# BGS-TRACE-222 — Line J sector-level antiunitary map: letter weights and traces of products

Source: registry statement of `BGS-TRACE-222`.  The (±2,8) sector letter weight is
`w_{C,a,τ}(n) = ĝ(n) e(Cn²/2) e(an/8) e(nτ)` (`e(x) = exp(2πix)`), with `ĝ(n) = iⁿ J_n(1.8)`, which satisfies
`conj ĝ(n) = (−1)ⁿ ĝ(n)` and `ĝ(−n) = ĝ(n)` (these two Bessel facts enter as hypotheses `hK`, `hR`).

* `e_half_int` : `e(4n/8) = (−1)ⁿ`;
* `K_weight` : `conj w_{C,a,τ}(n) = w_{−C,4−a,−τ}(n)` (K sends `(C, a, τ) ↦ (−C, 4 − a, −τ)`);
* `R_weight` : `w_{C,a,τ}(−n) = w_{C,−a,−τ}(n)` (R sends `(C, a, τ) ↦ (C, −a, −τ)`);
* `RK_weight` : `conj w_{C,a,τ}(−n) = w_{−C,a−4,τ}(n)` — RK sends `(C, a, τ) ↦ (−C, a − 4, τ)` for **every** real twist `τ`
  and every real `C`, `a`; with `C = 2` this is the letter-level form of `(RK) V^{(+2)}_{τ,a} (RK)⁻¹ = V^{(−2)}_{τ,a+4}`
  (`a − 4 ≡ a + 4` mod 8);
* `trace_prod_conj` : (multiplicativity of antiunitary conjugation, finite-dimensional form) if
  `V′_i = U conj(V_i) U⁻¹` for every factor, then `Tr ∏_i V′_i = conj Tr ∏_i V_i` for every finite word;
  `trace_conj` : the single-operator case.

**Partial coverage:** the operators themselves (`V^{(C)} = ∑_n w(n) M_{Cn} C_n` on the real-centred disc lattices, the
reflection `n ↦ −n, s ↦ −s, c ↦ −c` with symmetric rounding, and RK as an isometry of the Line F spaces) are **not**
formalized; the trace statement is proved for matrices (any finite-dimensional truncation on which RK acts as
`X ↦ U conj(X) U⁻¹`), not for the trace-class operators on `ℓ²`.  The Galerkin referee check is numerical and out of
scope.  All proofs are kernel-checked.
-/

namespace Bgs.LineJSectorConj

open ComplexConjugate Bgs.LineN4Gauge Bgs.LineIAliasing

/-- `w_{C,a,τ}(n) = ĝ(n) e(Cn²/2) e(an/8) e(nτ)`. -/
noncomputable def w (g : ℤ → ℂ) (C a τ : ℝ) (n : ℤ) : ℂ :=
  g n * e ((C : ℂ) * n ^ 2 / 2) * e ((a : ℂ) * n / 8) * e ((n : ℂ) * τ)

theorem e_half_int (n : ℤ) : e (4 * (n : ℂ) / 8) = (-1) ^ n := by
  unfold e
  have : 2 * (Real.pi : ℂ) * Complex.I * (4 * (n : ℂ) / 8) = n * ((Real.pi : ℂ) * Complex.I) := by ring
  rw [this, Complex.exp_int_mul, Complex.exp_pi_mul_I]

theorem conj_e (x : ℝ) : conj (e (x : ℂ)) = e (-(x : ℂ)) := conj_e_real x

theorem K_weight (g : ℤ → ℂ) (hK : ∀ n, conj (g n) = (-1) ^ n * g n) (C a τ : ℝ) (n : ℤ) :
    conj (w g C a τ n) = w g (-C) (4 - a) (-τ) n := by
  unfold w
  have h1 : (C : ℂ) * n ^ 2 / 2 = ((C * n ^ 2 / 2 : ℝ) : ℂ) := by push_cast; ring
  have h2 : (a : ℂ) * n / 8 = ((a * n / 8 : ℝ) : ℂ) := by push_cast; ring
  have h3 : (n : ℂ) * τ = ((n * τ : ℝ) : ℂ) := by push_cast; ring
  simp only [map_mul]
  rw [h1, h2, h3, conj_e, conj_e, conj_e, hK]
  have h4 : (((4 - a : ℝ)) : ℂ) * n / 8 = 4 * (n : ℂ) / 8 + -((a * n / 8 : ℝ) : ℂ) := by push_cast; ring
  rw [h4, ← e_add, e_half_int]
  push_cast; ring_nf

theorem R_weight (g : ℤ → ℂ) (hR : ∀ n, g (-n) = g n) (C a τ : ℝ) (n : ℤ) :
    w g C a τ (-n) = w g C (-a) (-τ) n := by
  unfold w
  rw [hR]; push_cast; ring_nf

theorem RK_weight (g : ℤ → ℂ) (hK : ∀ n, conj (g n) = (-1) ^ n * g n) (hR : ∀ n, g (-n) = g n)
    (C a τ : ℝ) (n : ℤ) :
    conj (w g C a τ (-n)) = w g (-C) (a - 4) τ n := by
  rw [K_weight g hK, R_weight g hR]
  congr 1 <;> ring

section Matrices

variable {ι : Type*} [Fintype ι] [DecidableEq ι]

omit [DecidableEq ι] in
theorem trace_map_conj (X : Matrix ι ι ℂ) : (X.map conj).trace = conj X.trace := by
  unfold Matrix.trace; rw [map_sum]; rfl

theorem trace_conj (U Uinv X : Matrix ι ι ℂ) (h1 : Uinv * U = 1) :
    (U * X.map conj * Uinv).trace = conj X.trace := by
  rw [Matrix.trace_mul_comm, ← Matrix.mul_assoc, h1, Matrix.one_mul, trace_map_conj]

theorem prod_conj (U Uinv : Matrix ι ι ℂ) (h1 : Uinv * U = 1) (h2 : U * Uinv = 1) (Vs : List (Matrix ι ι ℂ)) :
    (Vs.map (fun V : Matrix ι ι ℂ => U * V.map conj * Uinv)).prod = U * (Vs.prod).map conj * Uinv := by
  induction Vs with
  | nil =>
    simp only [List.map_nil, List.prod_nil]
    rw [show (1 : Matrix ι ι ℂ).map conj = 1 from Matrix.map_one _ (map_zero _) (map_one _), Matrix.mul_one, h2]
  | cons A Vs ih =>
    rw [List.map_cons, List.prod_cons, ih, List.prod_cons]
    rw [show (A * Vs.prod).map conj = A.map conj * (Vs.prod).map conj from
      Matrix.map_mul (f := (starRingEnd ℂ : ℂ →+* ℂ))]
    calc U * A.map conj * Uinv * (U * (Vs.prod).map conj * Uinv)
        = U * A.map conj * (Uinv * U) * (Vs.prod).map conj * Uinv := by simp only [Matrix.mul_assoc]
      _ = _ := by rw [h1, Matrix.mul_one]; simp only [Matrix.mul_assoc]

/-- **Traces of non-autonomous products:** `Tr ∏ V′_i = conj Tr ∏ V_i` when `V′_i = U conj(V_i) U⁻¹`. -/
theorem trace_prod_conj (U Uinv : Matrix ι ι ℂ) (h1 : Uinv * U = 1) (h2 : U * Uinv = 1)
    (Vs : List (Matrix ι ι ℂ)) :
    ((Vs.map (fun V : Matrix ι ι ℂ => U * V.map conj * Uinv)).prod).trace = conj (Vs.prod).trace := by
  rw [prod_conj U Uinv h1 h2, trace_conj U Uinv _ h1]

end Matrices

end Bgs.LineJSectorConj
