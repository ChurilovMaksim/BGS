import Bgs.TraceStatement
import Mathlib.LinearAlgebra.Matrix.Notation

open Filter Topology MeasureTheory

namespace Bgs.Fm001Statement

/-!
# BGS-FM-001 — statement of the frozen-model classical symmetry theorem (statement formalization only)

This module formalizes **statements** from the project theorem `BGS-FM-001`
("Frozen-model classical symmetry theorem",
`mathematics/fixed-map/fixed_model_symmetry_theorem.md`), following the
statement-only pattern of `Bgs.TraceStatement`: it contains **definitions
and `Prop`s only**.  No theorem is proved here, no proof is claimed, and
there is no `sorry`, no `axiom` command and no `native_decide` anywhere in
this file.  The claim itself is `proved` in the registry by the project
proof; this file states (part of) what that proof proves, it does not
re-prove it.

## What is stated

* §1, the **exact Weyl dictionary**: the raw Weyl quantization `A_N` of
  the raw symbol `f` (see `Bgs.TraceStatement.AN`) equals the ordinary
  midpoint Weyl quantization of the corrected symbol `g` of formula (1)
  of the note.  The shift `q ↦ q + 1/2` in the `p`-dependent term is the
  whole content: it is forced coefficient-by-coefficient by the factor
  `(-1)^{kℓ}` relating `W_N` and `T_N`, and the dictionary identity below
  holds termwise for every `(k, ℓ)` in the support box.
* §3, the **exact Fourier data** of `g`: the weight identity
  `∑_v (|Re c_v| + |Im c_v|) |v|² = 51451/1000` and the mode count
  (exactly 32 nonzero modes).  Both were checked in exact rational
  arithmetic before writing (see the batch report); they are stated, not
  proved, here.

## What is NOT stated (honest gap, not an oversight)

The four conclusions of §2 of the note — `G_κ` Anosov and topologically
conjugate to `S`, trivial `C¹` centralizer, no `C¹` reversor, no `C¹`
conjugacy to an affine map — are **not** stated here.  Stating them would
require a `C¹`-diffeomorphism / Anosov API for the torus (including the
Hamiltonian flow `Φ_g^κ` as a function), which Mathlib v4.33.1 does not
provide in a directly usable form.  Inventing a schema with undefined
notions would not be a statement of the theorem.  Likewise the derivative
bounds (5) of the note (`‖X_g‖∞ ≤ 400`, `‖DX_g‖∞ ≤ 3000`,
`‖D²X_g‖∞ ≤ 200000`, in induced Euclidean norms) are not stated: they are
derived in the note by differentiating the Fourier series, and the exact
Fourier identity stated below is that derivation's input; stating the
bounds themselves would additionally need a norm-convention layer for
vector fields that this statement module does not build.

The cat-map matrix `S` is included as model data.  The coupling range of
the theorem is `0 < |κ| ≤ 10⁻¹²`; the fixed physical coupling
`τ = 10⁻⁸⁰` (see `Bgs.TraceStatement.tau`) gives `κ = τ/(2π)` in range.
-/

/-- The frozen-model factor `r(q) = (1 - cos 14πq)(1 + cos 2πq)`. -/
noncomputable def rFun (q : ℝ) : ℝ :=
  (1 - Real.cos (14 * Real.pi * q)) * (1 + Real.cos (2 * Real.pi * q))

/-- The ordinary midpoint symbol `g` of formula (1) of the note:
`g(q,p) = cos 14πq + r(q)/10 + r(q) sin 2πq / 100
  + r(q + 1/2) cos (2πp - α) / 100 - 1/10`,
with `cos α = -3/5`, `sin α = 4/5`, so that
`cos (2πp - α) = -(3/5) cos 2πp + (4/5) sin 2πp`.  No `arccos` is needed. -/
noncomputable def gFun (q p : ℝ) : ℝ :=
  Real.cos (14 * Real.pi * q) + rFun q / 10
    + rFun q * Real.sin (2 * Real.pi * q) / 100
    + rFun (q + 1 / 2) * (-(3 / 5) * Real.cos (2 * Real.pi * p)
        + (4 / 5) * Real.sin (2 * Real.pi * p)) / 100
    - 1 / 10

/-- Fourier coefficients `c_{kℓ}` of `g`, mirroring
`Bgs.TraceStatement.fCoeff` term by term.  The `ℓ = 0` terms are identical
to those of the raw symbol; the `ℓ = ±1` terms carry the extra shift
factor `(-1)^k` coming from `r(q + 1/2)`.  Support: `ℓ ∈ {-1, 0, 1}`,
`k ∈ [-9, 9]`; exactly 32 modes are nonzero (see `fm001_mode_count`). -/
noncomputable def gCoeff (k l : ℤ) : ℂ :=
  if l = 0 then
    (if k = 7 ∨ k = -7 then (1 : ℂ) / 2 else 0)
      + Bgs.TraceStatement.rCoeff k / 10
      + (Bgs.TraceStatement.rCoeff (k - 1) - Bgs.TraceStatement.rCoeff (k + 1))
        / (200 * Complex.I)
      - (if k = 0 then (1 : ℂ) / 10 else 0)
  else if l = 1 then
    Bgs.TraceStatement.rCoeff k * (-1 : ℂ) ^ k * ((-3 - 4 * Complex.I) / 1000)
  else if l = -1 then
    Bgs.TraceStatement.rCoeff k * (-1 : ℂ) ^ k * ((-3 + 4 * Complex.I) / 1000)
  else 0

/-- The ordinary midpoint Weyl operator `W_N(a, b) = (-1)^{ab} T_N(a, b)`.
The sign is a function of the *integer* representatives `a, b` (the
quantization below only ever uses small `ℓ, k`); `T_N` itself is
`Bgs.TraceStatement.weylT`. -/
noncomputable def weylW (N : ℕ) (a b : ℤ) : Matrix (Fin N) (Fin N) ℂ :=
  ((-1 : ℂ) ^ (a * b)) • Bgs.TraceStatement.weylT N (a : ZMod N) (b : ZMod N)

/-- The ordinary Weyl quantization of `g`: the same finite sum shape as
`Bgs.TraceStatement.AN`, with `gCoeff` and `weylW` in place of `fCoeff`
and `weylT`. -/
noncomputable def ANordinary (N : ℕ) : Matrix (Fin N) (Fin N) ℂ :=
  ∑ k ∈ Finset.Icc (-9) 9, ∑ l ∈ Finset.Icc (-1) 1,
    gCoeff k l • weylW N l k

/-- The cat-map matrix `S = [[3, 4], [2, 3]]` (model data; the flow
`G_κ = S ∘ Φ_g^κ` and its §2 conclusions are not stated — see header). -/
def SMat : Matrix (Fin 2) (Fin 2) ℤ := !![3, 4; 2, 3]

/-- **FM-001 §1, exact Weyl dictionary (statement only).**  For odd `N`,
the ordinary Weyl quantization of `g` equals the frozen kick `A_N`.
Termwise this is `gCoeff k ℓ · (-1)^{ℓk} = fCoeff k ℓ` for every
`(k, ℓ)` in the support box: at `ℓ = 0` the coefficients agree, and at
`ℓ = ±1` the two factors `(-1)^k` (shift) and `(-1)^{±k}` (midpoint sign)
cancel. -/
def fm001_dictionary : Prop :=
  ∀ N : ℕ, N % 2 = 1 → ANordinary N = Bgs.TraceStatement.AN N

/-- **FM-001 §3, exact Fourier weight (statement only).**
`∑_v (|Re c_v| + |Im c_v|) |v|² = 51451/1000 < 52`, summed over the
support box of `gCoeff` (all other coefficients vanish).  This is the
exact input from which the note derives the vector-field bounds (5). -/
def fm001_fourier_weight : Prop :=
  ∑ k ∈ Finset.Icc (-9) 9, ∑ l ∈ Finset.Icc (-1) 1,
    (|(gCoeff k l).re| + |(gCoeff k l).im|) * ((k ^ 2 + l ^ 2 : ℤ) : ℝ)
      = 51451 / 1000

/-- **FM-001 §3, mode count (statement only).**  Exactly 32 Fourier modes
of `g` are nonzero, inside the same support box. -/
def fm001_mode_count : Prop :=
  ((Finset.Icc (-9) 9 ×ˢ Finset.Icc (-1) 1).filter
    (fun p => gCoeff p.1 p.2 ≠ 0)).card = 32

end Bgs.Fm001Statement
