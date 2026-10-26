import Bgs.TraceStatement
import Mathlib.Analysis.CStarAlgebra.Matrix
import Mathlib.Analysis.SpecialFunctions.Pow.Real

open Filter Topology MeasureTheory
open scoped Matrix.Norms.L2Operator

namespace Bgs.Fm021Statement

/-!
# BGS-FM-021 — statement of the fixed-map position-chain theorem (statement formalization only)

This module formalizes **statements** from the project theorem `BGS-FM-021`
("Fixed-map position-chain singular mixing, cyclic ramp and marked
three-link cancellation", `mathematics/fixed-map/position_chain_mixing.md`),
following the statement-only pattern of `Bgs.TraceStatement`: it contains
**definitions and `Prop`s only**.  No theorem is proved here, no proof is
claimed, and there is no `sorry`, no `axiom` command and no `native_decide`
anywhere in this file.

Status labels below refer to the *project proof* (registry ledger status:
"PROJECT ANALYTIC PROOF + INDEPENDENT INTERNAL REVIEW + EXACT FINITE
CONTROLS"), not to this file: the `Prop`s marked PROVED state conclusions
of that proof, the one marked OPEN states the remaining pair target of §4
of the note, which the note itself leaves open ("exponential mixing of `P`
does not estimate this signed interference").

## Conventions

* `U_N` is the frozen propagator of `Bgs.TraceStatement.UN`, at the fixed
  coupling `τ = 10⁻⁸⁰`; `P_N(x, y) = |U_N(x, y)|²`, `J_N(x, y) = 1/N`.
* `‖·‖` on matrices is the L² operator norm: the scoped instance
  `Matrix.Norms.L2Operator` (see `Mathlib.Analysis.CStarAlgebra.Matrix`)
  is opened for this file, so `‖P_N - J_N‖` is exactly the note's
  `‖P_N - J_N‖_op` (induced Euclidean operator norm).
* `D_m = ∑_x d(x) |A(x)|²` counts ordered pairs related by cyclic
  rotation; it is written here via the rotation sets of
  `Bgs.TraceStatement.rotSet`, since the number of *distinct* rotations
  of a word equals its least cyclic period `d(x)`.
* The band statements use the ε–`N₀` form of uniform convergence on
  positive compact Heisenberg bands `aN ≤ m ≤ bN` (which forces `m ≥ 1`,
  so `D_m / m` is never a division by zero in the stated range).
* The marked three-link bound is stated in multiplied-out form
  (`‖E‖ · 2^{max L} ≤ C³N`), equivalent to `‖E‖ ≤ C³N·2^{-max L}` and
  avoiding negative powers in the statement.
-/

/-- The position transition matrix `P_N(x, y) = |U_N(x, y)|²`. -/
noncomputable def PN (N : ℕ) : Matrix (Fin N) (Fin N) ℂ :=
  fun x y => ((‖Bgs.TraceStatement.UN N x y‖ ^ 2 : ℝ) : ℂ)

/-- The uniform matrix `J_N(x, y) = 1/N`.  (At `N = 0` this is junk by the
`⁻¹` convention; every `Prop` below uses odd `N ≥ 1`.) -/
noncomputable def JN (N : ℕ) : Matrix (Fin N) (Fin N) ℂ :=
  fun _ _ => (N : ℂ)⁻¹

/-- The cyclic multiplicity `D_m = ∑_x d(x) |A(x)|²`, via rotation sets:
`∑_{y ∈ Rot(x)} |A(x)|² = d(x) |A(x)|²` since `|Rot(x)| = d(x)`. -/
noncomputable def Dm (N m : ℕ) : ℝ :=
  ∑ x : Fin m → Fin N, ∑ _y ∈ Bgs.TraceStatement.rotSet m x,
    ‖Bgs.TraceStatement.wordAmp N m x‖ ^ 2

/-- The signed residual `R_m = |Tr U_N^m|² - D_m`, so that exactly
`|Tr U_N^m|² = D_m + R_m` by definition. -/
noncomputable def Rm (N m : ℕ) : ℝ :=
  ‖(Bgs.TraceStatement.UN N ^ m).trace‖ ^ 2 - Dm N m

/-- The exact marked three-link expression `E_dist(L)` of §3 of the note:
the sum over pairwise distinct ports `a₁, a₂, a₃` and all `b₁, b₂, b₃` of
`∏_i (P^{L_i})_{a_i, b_i} · U_{b_i, a_{i+1}} · conj (U_{b_i, a_{i-1}})`,
indices mod 3.  Pairwise distinctness is written as three decidable
inequalities (equivalent to injectivity on `Fin 3`). -/
noncomputable def Edist (N : ℕ) (L : Fin 3 → ℕ) : ℂ :=
  ∑ a ∈ Finset.univ.filter
      (fun a : Fin 3 → Fin N => a 0 ≠ a 1 ∧ a 0 ≠ a 2 ∧ a 1 ≠ a 2),
    ∑ b : Fin 3 → Fin N,
      ∏ i : Fin 3, (PN N ^ L i) (a i) (b i)
        * Bgs.TraceStatement.UN N (b i) (a (i + 1))
        * star (Bgs.TraceStatement.UN N (b i) (a (i - 1)))

/-- The marked sum over all triples `L₁ + L₂ + L₃ = m - 3` (as functions
`Fin 3 → Fin (m + 1)`, so the sum is finite). -/
noncomputable def markedSum (N m : ℕ) : ℂ :=
  ∑ L ∈ Finset.univ.filter
      (fun L : Fin 3 → Fin (m + 1) => ∑ i, (L i).val = m - 3),
    Edist N (fun i => (L i).val)

/-- **FM-021 §1, constant gap (PROVED in the project proof; statement
only here).**  `limsup ‖P_N - J_N‖_op ≤ 10⁻⁶⁴` along odd `N`. -/
def fm021_mixing : Prop :=
  Filter.limsup (fun j : ℕ => ‖PN (2 * j + 1) - JN (2 * j + 1)‖) Filter.atTop
    ≤ 1 / 10 ^ 64

/-- **FM-021 §1, powers (PROVED in the project proof; statement only
here).**  Eventually, for every odd `N` and every `L ≥ 0`,
`‖P_N^L - J_N‖_op ≤ 2⁻ᴸ` (at `L = 0` this is `‖I - J‖ ≤ 1`). -/
def fm021_powers : Prop :=
  ∃ N₀ : ℕ, ∀ N : ℕ, N % 2 = 1 → N₀ ≤ N → ∀ L : ℕ,
    ‖PN N ^ L - JN N‖ ≤ 1 / 2 ^ L

/-- **FM-021 §4, trace ramp (PROVED in the project proof; statement only
here).**  `|Tr P_N^m - 1| → 0` uniformly for `m` in any positive compact
Heisenberg band `aN ≤ m ≤ bN`. -/
def fm021_trace_ramp : Prop :=
  ∀ a b : ℝ, 0 < a → a < b → ∀ ε : ℝ, 0 < ε → ∃ N₀ : ℕ,
    ∀ N : ℕ, N % 2 = 1 → N₀ ≤ N → ∀ m : ℕ,
      a * (N : ℝ) ≤ (m : ℝ) → (m : ℝ) ≤ b * (N : ℝ) →
        ‖(PN N ^ m).trace - 1‖ < ε

/-- **FM-021 §4, cyclic ramp (PROVED in the project proof; statement only
here).**  `|D_m / m - 1| → 0` uniformly for `m` in any positive compact
Heisenberg band. -/
def fm021_cyclic_ramp : Prop :=
  ∀ a b : ℝ, 0 < a → a < b → ∀ ε : ℝ, 0 < ε → ∃ N₀ : ℕ,
    ∀ N : ℕ, N % 2 = 1 → N₀ ≤ N → ∀ m : ℕ,
      a * (N : ℝ) ≤ (m : ℝ) → (m : ℝ) ≤ b * (N : ℝ) →
        |Dm N m / (m : ℝ) - 1| < ε

/-- **FM-021 §3, marked three-link bound (PROVED in the project proof;
statement only here).**  For some `C ≥ 0` and all large odd `N`,
`|E_dist(L)| ≤ C³N·2^{-max L}` for every triple `L` (stated multiplied
out; the cancellation argument covers all `L`, including zero link
lengths). -/
def fm021_marked_bound : Prop :=
  ∃ C : ℝ, 0 ≤ C ∧ ∃ N₀ : ℕ, ∀ N : ℕ, N % 2 = 1 → N₀ ≤ N →
    ∀ L : Fin 3 → ℕ,
      ‖Edist N L‖ * (2 : ℝ) ^ (L 0 ⊔ L 1 ⊔ L 2) ≤ C ^ 3 * (N : ℝ)

/-- **FM-021 §3, summed marked bound (PROVED in the project proof;
statement only here).**  For some `C ≥ 0` and all large odd `N`,
`|m² ∑_{L₁+L₂+L₃=m-3} E_dist(L)| ≤ C³m²·binom(m-1, 2)·N·2^{-(m-3)/3}`
for every `m ≥ 3`. -/
def fm021_marked_sum_bound : Prop :=
  ∃ C : ℝ, 0 ≤ C ∧ ∃ N₀ : ℕ, ∀ N : ℕ, N % 2 = 1 → N₀ ≤ N →
    ∀ m : ℕ, 3 ≤ m →
      ‖((m : ℂ)) ^ 2 * markedSum N m‖
        ≤ C ^ 3 * (m : ℝ) ^ 2 * (Nat.choose (m - 1) 2 : ℝ) * (N : ℝ)
          * (2 : ℝ) ^ (-((m : ℝ) - 3) / 3)

/-- **FM-021 §4, pair CUE target (OPEN; statement only here).**  For every
smooth compactly supported weight `w` in `(0, ∞)`,
`N⁻² ∑_m w(m/N) R_m → ∫₀^∞ (min(ξ, 1) - ξ) w(ξ) dξ` along odd `N`.
The sum is a `tsum` over all `m`; compact support of `w` makes it a
finite sum in disguise.  This is the remaining signed-interference
target of the note, not a consequence of the mixing bounds above. -/
def fm021_pair_target : Prop :=
  ∀ w : ℝ → ℝ, HasCompactSupport w → Function.support w ⊆ Set.Ioi (0 : ℝ) →
    ContDiff ℝ (⊤ : WithTop ℕ∞) w →
    Filter.Tendsto (fun j : ℕ => ((2 * j + 1 : ℝ) ^ 2)⁻¹ *
      ∑' m : ℕ, w ((m : ℝ) / (2 * j + 1 : ℝ)) * Rm (2 * j + 1) m)
      Filter.atTop (nhds (∫ ξ in Set.Ioi (0 : ℝ), (min ξ 1 - ξ) * w ξ))

end Bgs.Fm021Statement
