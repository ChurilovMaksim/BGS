import Mathlib.Analysis.Normed.Algebra.MatrixExponential
import Mathlib.Analysis.Distribution.SchwartzSpace.Deriv
import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.LinearAlgebra.Matrix.Charpoly.Coeff
import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Matrix.Mul
import Mathlib.Data.ZMod.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

/-!
# BGS-TRACE-005 — statement of the open problem (statement formalization only)

This module formalizes the **statement** of the open claim `BGS-TRACE-005`
("Model-specific signed Heisenberg-scale desymmetrized joint-trace estimate")
for the frozen BGS propagator family.  It contains **definitions and `Prop`s
only**.  Nothing here is a theorem about the family, and no proof of the
criterion is given or claimed: the claim is OPEN (see `record/claims.json`,
`mathematics/open_questions.md` §B, and the canonical self-contained
formulation `record/remaining_breakthrough_task_20261021.md`).

## What the statement says

For odd `N ≥ 3` let `U_N = exp(i τ N A_N) M_N` with the fixed coupling
`τ = 10^{-80}`, the raw modular Weyl operators `T_N(a,b)`, the cat-map matrix
`M_N`, and `A_N` the raw Weyl quantization of the fixed symbol `f - 1/10`
(all defined below, literally as in the sources).

Required conclusion (the registry closure condition of `BGS-TRACE-005`):
for every fixed `k ≥ 2` and every admissible test function `b`
(real Schwartz, `b ≥ 0`, `sup b < 1`, `b̂ ∈ C_c^∞`, Fourier convention
`b̂(ξ) = ∫ b(x) e^{-2πiξx} dx`),

  `Δ_{k,N}(b) = M^U_{k,N}(b) - e_k(T_{N,b}) ⟶ 0`  along odd `N`,

where `M^U_{k,N}` is the signed factorial joint-trace statistic (the modulus
is outside the complete sum; no absolute values are taken inside) and
`e_k(T_{N,b})` is the exact finite-dimensional Haar `U(N)` (CUE) reference:
the `k`-th elementary symmetric function of the eigenvalues of the Toeplitz
matrix `T_{N,b}`.  By the repo's proved implication `BGS-TRACE-086`
(`mathematics/all_order_process_closure_20261015.md`), this criterion implies
the required local law `Ξ_{N,α} ⇒ Sine₂` of
`record/remaining_breakthrough_task_20261021.md` §2; the Sine₂ convergence
itself is not re-stated here (Mathlib has no determinantal point-process
API — see the design report).

## Definitional choices (all repo-sanctioned)

* `D_U` is defined through traces by the exact partition/Möbius identity —
  Theorem 1 (formulas (5), (7)) of `mathematics/trace-bridge/trace_to_local_statistics_bridge.md`
  (status EXACT there) and §3 of the canonical task text ("without
  diagonalization, `D_U` is computed from `p_n = Tr U_N^n`").  The primary
  eigenphase definition (4) of the bridge is thereby avoided; no content is
  changed, since the identity is exact for every unitary (indeed every
  square) matrix.
* `p_{-n} = conj (p_n)`, `p_0 = N`, as fixed in the canonical task text §3.
* `A_N` is the finite Weyl sum of the symbol's Fourier coefficients: `f`
  is a trigonometric polynomial, so the Fourier series of `f - 1/10` has
  exactly 32 nonzero modes.  The coefficient function `fCoeff` below mirrors
  the defining expression of `f` term by term; the same algebra, in exact
  rationals, is `coefficient_checks()` in
  `computations/verification/physical_kick_trace_checks.py`
  (support 32, `(0,0)` mode absent, Hermitian symmetry).
* `e_k` of the Toeplitz reference is taken from the characteristic
  polynomial, `e_k(λ) = (-1)^k [X^{N-k}] χ_T(X)`, which for the Hermitian
  positive-semidefinite `T_{N,b}` is the elementary symmetric function of
  its eigenvalues with multiplicity — the repo's own finite CUE reference
  (determinant identity (3) of `all_order_process_closure_20261015.md`).

Sources for every object are tabulated in
`phase6_trace_statement_design.md` (executor's report, outside the repo).
-/

open Filter Topology MeasureTheory

namespace Bgs.TraceStatement

/-- The fixed coupling `τ = 10^{-80}` of the frozen family.  It is a fixed
positive real number; it is *not* sent to `0` with `N`. -/
noncomputable def tau : ℝ := 1 / 10 ^ 80

/-- The root of unity factor `e_N(t) = exp (2πi t / N)` for `t : ZMod N`,
via the least representative `t.val`. -/
noncomputable def eN (N : ℕ) (t : ZMod N) : ℂ :=
  Complex.exp (2 * Real.pi * Complex.I / (N : ℂ)) ^ t.val

/-- The index embedding `Fin N → ZMod N`, `x ↦ x.val`.  The repo indexes
all frozen-family matrices by `Z/N`; the matrices here are indexed by
`Fin N` (whose `Fintype`/ring instances are unconditional in Mathlib,
unlike those of `ZMod N`), and all index arithmetic is performed on the
values in `ZMod N` through this embedding, i.e. modulo `N` on the nose. -/
def finZ (N : ℕ) (x : Fin N) : ZMod N := (x.val : ZMod N)

/-- The raw modular Weyl operator `T_N(a, b)`, defined by
`(T_N(a,b) ψ)(x) = e_N (b (x + 2⁻¹ a)) ψ (x + a)` for `x ∈ Z/N`.
Matrix entries (indices read in `ZMod N` via `finZ`):
`T x y = e_N (b (x + 2⁻¹ a))` if `y = x + a` in `ZMod N`, else `0`.
Here `2⁻¹` is the inverse of `2` modulo `N` (a unit for odd `N`). -/
noncomputable def weylT (N : ℕ) (a b : ZMod N) : Matrix (Fin N) (Fin N) ℂ :=
  fun x y => if finZ N y = finZ N x + a
    then eN N (b * (finZ N x + (2 : ZMod N)⁻¹ * a)) else 0

/-- The cat-map matrix `M_N`:
`(M_N)_{xy} = N^{-1/2} e_N (-8⁻¹ (3x² - 2xy + 3y²))` for `x, y ∈ Z/N`
(read via `finZ`), with `8⁻¹` the inverse of `8` modulo `N`. -/
noncomputable def MN (N : ℕ) : Matrix (Fin N) (Fin N) ℂ :=
  fun x y => ((Real.sqrt (N : ℝ))⁻¹ : ℂ)
    * eN N (-(8 : ZMod N)⁻¹ * (3 * finZ N x ^ 2 - 2 * finZ N x * finZ N y
      + 3 * finZ N y ^ 2))

/-- Fourier coefficients of `r(q) = (1 - cos 14πq) (1 + cos 2πq)` in the
basis `e^{2πi k q}`: `r̂(0) = 1`, `r̂(±1) = 1/2`, `r̂(±7) = -1/2`,
`r̂(±6) = r̂(±8) = -1/4`, all other coefficients `0`. -/
noncomputable def rCoeff (k : ℤ) : ℂ :=
  if k = 0 then 1
  else if k = 1 ∨ k = -1 then 1 / 2
  else if k = 7 ∨ k = -7 then -1 / 2
  else if k = 6 ∨ k = -6 ∨ k = 8 ∨ k = -8 then -1 / 4
  else 0

/-- Fourier coefficients `c_{kl}` of the centered symbol `f - 1/10`, where
`f(q,p) = cos 14πq + r(q)/10 + r(q) sin 2πq / 100
        + r(q) cos (2πp - α₀) / 100`,  `e^{iα₀} = (-3 + 4i)/5`.

The definition mirrors `f` term by term:
* the `cos 14πq` term contributes `1/2` at `(±7, 0)`;
* the `r/10` term contributes `rCoeff k / 10` at `l = 0`;
* the `r sin 2πq / 100` term contributes
  `(rCoeff (k-1) - rCoeff (k+1)) / (200 i)` at `l = 0`, since
  `sin 2πq = (e^{2πiq} - e^{-2πiq}) / (2i)`;
* the `r cos (2πp - α₀) / 100` term contributes `rCoeff k * (-3 ∓ 4i) / 1000`
  at `l = ±1`, since the `e^{±2πip}` coefficients of `cos (2πp - α₀)` are
  `e^{∓iα₀} / 2 = (-3 ∓ 4i) / 10`;
* centering subtracts `1/10` at `(0, 0)` (which makes `c_{00} = 0`).

Support: `l ∈ {-1, 0, 1}`, `k ∈ [-9, 9]`; exactly 32 modes are nonzero. -/
noncomputable def fCoeff (k l : ℤ) : ℂ :=
  if l = 0 then
    (if k = 7 ∨ k = -7 then (1 : ℂ) / 2 else 0)
      + rCoeff k / 10
      + (rCoeff (k - 1) - rCoeff (k + 1)) / (200 * Complex.I)
      - (if k = 0 then (1 : ℂ) / 10 else 0)
  else if l = 1 then rCoeff k * ((-3 - 4 * Complex.I) / 1000)
  else if l = -1 then rCoeff k * ((-3 + 4 * Complex.I) / 1000)
  else 0

/-- The quantized kick `A_N = ∑_{k,l} c_{kl} T_N(l, k)`: the raw Weyl
quantization of `f - 1/10` under `e^{2πi(kq + lp)} ↦ T_N(l, k)`.
The sum runs over the full support box of `fCoeff`. -/
noncomputable def AN (N : ℕ) : Matrix (Fin N) (Fin N) ℂ :=
  ∑ k ∈ Finset.Icc (-9) 9, ∑ l ∈ Finset.Icc (-1) 1,
    fCoeff k l • weylT N (l : ZMod N) (k : ZMod N)

/-- The frozen propagator `U_N = exp (i τ N A_N) M_N`, with the matrix
exponential (`NormedSpace.exp`, the exponential power series; for complex
matrices this is the usual matrix exponential). -/
noncomputable def UN (N : ℕ) : Matrix (Fin N) (Fin N) ℂ :=
  NormedSpace.exp ((Complex.I * (tau : ℂ) * (N : ℂ)) • AN N) * MN N

/-- The trace powers `p_s = Tr (U_N^s)` for `s : ℤ`, with the repo's fixed
conventions `p_0 = N` (automatic: `Tr 1 = N`) and `p_{-n} = conj (p_n)`. -/
noncomputable def ptr (N : ℕ) (s : ℤ) : ℂ :=
  if 0 ≤ s then ((UN N) ^ s.toNat).trace
  else star ((UN N) ^ (-s).toNat).trace

/-- The set partitions of the index type `Fin k`, as a finset of finsets of
blocks: pairwise disjoint nonempty blocks whose union is everything.
(Mathlib v4.33.1 has no `Finset.partitions`; this is the bridge note's
partition lattice `Π_k` of `{1, …, k}`.) -/
def partitionsOf (k : ℕ) : Finset (Finset (Finset (Fin k))) :=
  Finset.univ.filter fun π =>
    (∀ B ∈ π, B.Nonempty) ∧
    (∀ B₁ ∈ π, ∀ B₂ ∈ π, B₁ ≠ B₂ → Disjoint B₁ B₂) ∧
    π.biUnion id = Finset.univ

/-- The distinct-index joint exponential sum `D_U(m)`, defined through the
traces `ptr` by the exact partition/Möbius identity
`D_U(m) = ∑_{π ∈ Part(k)} ∏_{B ∈ π} (-1)^{|B|-1} (|B|-1)! · p_{∑_{a ∈ B} m_a}`
(bridge note, formulas (5) and (7)).  The modulus is *not* taken here; the
signed sum is the object of the criterion. -/
noncomputable def DU (N : ℕ) (k : ℕ) (m : Fin k → ℤ) : ℂ :=
  ∑ π ∈ partitionsOf k,
    ∏ B ∈ π, ((-1 : ℂ) ^ (B.card - 1) * (Nat.factorial (B.card - 1) : ℂ))
      * ptr N (∑ a ∈ B, m a)

/-- The Fourier transform in the repo's convention:
`b̂(ξ) = ∫ b(x) e^{-2πiξx} dx`.  (Mathlib's `𝓕` uses the opposite sign in
the exponent; the repo convention is used throughout this module.) -/
noncomputable def fourierC (b : ℝ → ℝ) (ξ : ℝ) : ℂ :=
  ∫ x : ℝ, (b x : ℂ) * Complex.exp (-(2 * Real.pi * Complex.I) * (ξ : ℂ) * (x : ℂ))

/-- Admissible test functions of the criterion: real Schwartz functions
`b ≥ 0` with `sup b < 1` and `b̂ ∈ C_c^∞(ℝ)` in the repo Fourier
convention.  (The smoothness is stated for `fourierC b`; since
`fourierC b ξ = 𝓕b (-ξ)` up to the sign convention, this is the same class
as `b̂` smooth in either convention.) -/
def Admissible (b : SchwartzMap ℝ ℝ) : Prop :=
  (∀ x, 0 ≤ b x) ∧
  (∃ s : ℝ, s < 1 ∧ ∀ x, b x ≤ s) ∧
  HasCompactSupport (fun ξ => fourierC (⇑b) ξ) ∧
  ContDiff ℝ (⊤ : WithTop ℕ∞) (fun ξ => fourierC (⇑b) ξ)

/-- The exact finite-dimensional CUE reference matrix
`(T_{N,b})_{ij} = N^{-1} b̂((i - j) / N)`, `0 ≤ i, j < N`:
Hermitian positive semidefinite with `Tr T_{N,b} = ∫ b`. -/
noncomputable def TNb (N : ℕ) (b : SchwartzMap ℝ ℝ) :
    Matrix (Fin N) (Fin N) ℂ :=
  fun i j => (N : ℂ)⁻¹ * fourierC (⇑b) (((i : ℝ) - (j : ℝ)) / (N : ℝ))

/-- The `k`-th elementary symmetric function of the eigenvalues of a complex
matrix, read off its characteristic polynomial:
`e_k(λ) = (-1)^k [X^{n-k}] χ_A(X)`.  For a diagonalizable matrix these are
the eigenvalues with algebraic (= geometric) multiplicity; in particular
this gives the repo's `e_k(T_{N,b})`, the Haar `U(N)` reference value of
the statistic `Mstat`. -/
noncomputable def ekMat {n : ℕ} (A : Matrix (Fin n) (Fin n) ℂ) (k : ℕ) : ℂ :=
  if k ≤ n then (-1 : ℂ) ^ k * A.charpoly.coeff (n - k) else 0

/-- The signed factorial joint-trace statistic
`M^U_{k,N}(b) = (1 / (k! N^k)) ∑_{m ∈ ℤ^k, ∑ m_a = 0} ∏_a b̂(m_a / N) D_U(m)`.
Only finitely many terms are nonzero for admissible `b` (compact Fourier
support), so the `∑'` over the zero-sum subtype is a finite sum in
disguise.  No modulus is taken anywhere: cancellation inside the sum is
the content of the criterion. -/
noncomputable def Mstat (N : ℕ) (k : ℕ) (b : SchwartzMap ℝ ℝ) : ℂ :=
  ((Nat.factorial k : ℂ) * (N : ℂ) ^ k)⁻¹ *
    ∑' (m : {m : Fin k → ℤ // ∑ a, m a = 0}),
      (∏ a, fourierC (⇑b) ((m.1 a : ℝ) / (N : ℝ))) * DU N k m.1

/-- The discrepancy `Δ_{k,N}(b) = M^U_{k,N}(b) - e_k(T_{N,b})`. -/
noncomputable def Delta (N : ℕ) (k : ℕ) (b : SchwartzMap ℝ ℝ) : ℂ :=
  Mstat N k b - ekMat (TNb N b) k

/-- **The statement of `BGS-TRACE-005` (open).**

For every fixed `k ≥ 2` and every admissible `b`, `Δ_{k,N}(b) → 0` as
`N → ∞` through odd values (`N = 2j + 1`).  This is the registry closure
condition: the CUE-subtracted signed factorial joint-trace sum tends to
zero, with the modulus outside the complete sum, for the unchanged frozen
propagator, at every fixed order and every compact Fourier bandwidth.
No rate, and no uniformity in `k` or in the bandwidth, is asserted. -/
def trace005_statement : Prop :=
  ∀ k : ℕ, 2 ≤ k → ∀ b : SchwartzMap ℝ ℝ, Admissible b →
    Tendsto (fun j : ℕ => Delta (2 * j + 1) k b) atTop (nhds 0)

/-! ## The first open test: `k = 2` with the specific test function `b_*`

Canonical task text §5, and formula (9) of
`mathematics/all_order_process_closure_20261015.md`. -/

/-- The bump `φ(ξ) = e^{-1/(1-ξ²)}` for `|ξ| < 1`, `0` otherwise. -/
noncomputable def phiFun (ξ : ℝ) : ℝ :=
  if |ξ| < 1 then Real.exp (-(1 / (1 - ξ ^ 2))) else 0

/-- `I = ∫ φ`. -/
noncomputable def phiInt : ℝ := ∫ ξ : ℝ, phiFun ξ

/-- The inverse Fourier transform of `φ` in the repo convention:
`(F⁻¹φ)(x) = ∫ φ(ξ) e^{+2πiξx} dξ` (real-valued, since `φ` is even). -/
noncomputable def phiInv (x : ℝ) : ℂ :=
  ∫ ξ : ℝ, (phiFun ξ : ℂ)
    * Complex.exp (2 * Real.pi * Complex.I * (ξ : ℂ) * (x : ℂ))

/-- The first test function `b_* = |F⁻¹φ|² / (2 I²)`.  It is admissible
(`b_* ≥ 0`, `b_*(0) = 1/2`, band-limited), and
`ŵ = |b̂_*|² = (φ * φ)² / (4 I⁴)` is supported in `[-2, 2]`. -/
noncomputable def bstar (x : ℝ) : ℝ :=
  ‖phiInv x‖ ^ 2 / (2 * phiInt ^ 2)

/-- The pair weight `w(t) = |b̂_*(t)|²`. -/
noncomputable def wFun (t : ℝ) : ℝ := ‖fourierC bstar t‖ ^ 2

/-- The pair discrepancy at level `N`, in the exact form of the first test:
`Δ_{2,N}(b_*) = N^{-2} ∑_{1 ≤ m < 2N} w(m/N) (|Tr U_N^m|² - min(m, N))`.
The truncation `m < 2N` is exact because `w` is supported in `[-2, 2]`. -/
noncomputable def delta2 (N : ℕ) : ℝ :=
  ((N : ℝ) ^ 2)⁻¹ * ∑ m ∈ Finset.Icc 1 (2 * N - 1),
    wFun ((m : ℝ) / (N : ℝ))
      * (‖((UN N) ^ m).trace‖ ^ 2 - min (m : ℝ) (N : ℝ))

/-- **The first open test of `BGS-TRACE-005` (open)**: `Δ_{2,N}(b_*) → 0`
along odd `N`.  This is the `k = 2`, `b = b_*` instance of
`trace005_statement` (via formula (9) of the closure note); it is stated
separately because the canonical task isolates it as the first test, and
because a pair test alone does not imply the higher orders. -/
def trace005_k2_test : Prop :=
  Tendsto (fun j : ℕ => delta2 (2 * j + 1)) atTop (nhds 0)

/-! ## The mandatory negative plateau correction (data of the first test)

Canonical task text §5.  With the cyclic-word decomposition
`|Tr U_N^m|² = D_{m,N} + Y_{m,N}` (diagonal/rotation part plus off-diagonal
part, defined below), the pair target, *if* the positive intensity estimate
for the frozen matrices is used, is equivalent to
`N^{-2} ∑_{m < 2N} w(m/N) Y_{m,N} → -δ_*` with the strictly positive
plateau `δ_* = ∫₁² (t - 1) w(t) dt`.  In particular the off-diagonal sum
must **not** vanish: its limit is the negative constant `-δ_*`.  This is
an additional (conditional) form of the first goal, not its solution, and
it is not part of `trace005_statement`. -/

/-- The plateau constant `δ_* = ∫₁² (t - 1) w(t) dt`. -/
noncomputable def deltaStar : ℝ :=
  ∫ t in Set.Icc 1 2, (t - 1) * wFun t

/-- The repo's stated elementary lower bound for the plateau:
`δ_* ≥ 2^{-17} e^{-64/7} > 0` (canonical task text §5; an estimate about
the explicit weight `w` alone, independent of the open problem). -/
def deltaStar_lower_bound : Prop :=
  (2 : ℝ) ^ (-17 : ℤ) * Real.exp (-(64 / 7 : ℝ)) ≤ deltaStar

/-- Cyclic addition of positions in `Fin m`: `j + r` modulo `m`.
(Positivity of `m` comes from `j.isLt`: a position exists only if
`m ≥ 1`.) -/
def cycAdd {m : ℕ} (j r : Fin m) : Fin m :=
  ⟨(j.val + r.val) % m,
    Nat.mod_lt _ (Nat.lt_of_le_of_lt (Nat.zero_le _) j.isLt)⟩

/-- The cyclic successor of a position in `Fin m`. -/
def cycSucc {m : ℕ} (j : Fin m) : Fin m :=
  ⟨(j.val + 1) % m,
    Nat.mod_lt _ (Nat.lt_of_le_of_lt (Nat.zero_le _) j.isLt)⟩

/-- The amplitude of a cyclic word `x : Fin m → Fin N`:
`a(x) = ∏_j U_N (x_j, x_{j+1})`, the last factor closing the cycle
(`x_m = x_0` is the `cycSucc` step). -/
noncomputable def wordAmp (N : ℕ) (m : ℕ) (x : Fin m → Fin N) : ℂ :=
  ∏ j : Fin m, (UN N) (x j) (x (cycSucc j))

/-- The set of distinct cyclic rotations of a word `x`. -/
noncomputable def rotSet (m : ℕ) (x : Fin m → Fin N) :
    Finset (Fin m → Fin N) :=
  @Finset.image (Fin m) (Fin m → Fin N) (Classical.decEq _)
    (fun r j => x (cycAdd j r)) Finset.univ

/-- The diagonal (rotation) part
`D_{m,N} = ∑_x ∑_{y ∈ Rot(x)} a(x) conj (a(y))`. -/
noncomputable def diagPart (N m : ℕ) : ℂ :=
  ∑ x : Fin m → Fin N, ∑ y ∈ rotSet m x,
    wordAmp N m x * star (wordAmp N m y)

/-- The off-diagonal part
`Y_{m,N} = ∑_x ∑_{y ∉ Rot(x)} a(x) conj (a(y))`, so that exactly
`|Tr U_N^m|² = D_{m,N} + Y_{m,N}`. -/
noncomputable def offDiagPart (N m : ℕ) : ℂ :=
  ∑ x : Fin m → Fin N, ∑ y ∈ (Finset.univ \ rotSet m x),
    wordAmp N m x * star (wordAmp N m y)

/-- **The plateau form of the pair target (conditional reformulation,
open).**  `N^{-2} ∑_{1 ≤ m < 2N} w(m/N) Y_{m,N} → -δ_*` along odd `N`.
Per the canonical task text §5 this is the form the pair test takes after
the diagonal part is controlled by the positive intensity estimate for
the frozen matrices; that estimate is itself an additional hypothesis
there (its norm term is not specified in closed form in the sources), so
this `Prop` is recorded as a separate equivalent-form target, not as
part of `trace005_statement`. -/
def trace005_k2_plateau_form : Prop :=
  Tendsto (fun j : ℕ =>
    ((2 * j + 1 : ℝ) ^ 2)⁻¹ * ∑ m ∈ Finset.Icc 1 (2 * (2 * j + 1) - 1),
      (wFun ((m : ℝ) / (2 * j + 1 : ℝ)) : ℂ)
        * offDiagPart (2 * j + 1) m)
    atTop (nhds (-(deltaStar : ℂ)))

end Bgs.TraceStatement
