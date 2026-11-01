import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Topology.Algebra.InfiniteSum.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp

/-!
# BGS-TRACE-297 — Line N4 gauge lemma (the two commutation relations)

Source: `mathematics/fixed-map/lineN2N4_inherited_level.md`, §3, and the
registry boundary of `BGS-TRACE-297`:
`L_τ Φ(s) = ∑_n w(n) e(nτ) e(κ n s) Φ((s + n)/λ)`, `e(x) = exp(2πi x)`.
With the translation `T_σ Φ(s) = Φ(s + σ)` and the modulation
`G_ν Φ(s) = e(ν s) Φ(s)`:

* `gauge_T` : `L_τ T_σ = T_{λσ} L_{τ − κλσ}`;
* `gauge_G` : `L_τ G_ν = G_{ν/λ} L_{τ + ν/λ}`;
* `T_G_comm` : `T_σ G_ν = e(νσ) G_ν T_σ` (the referee's unimodular scalar,
  N4-F1, `computations/verification/lineN4/referee/REPORT.md`).

The identities are proved for **arbitrary** weights `w : ℤ → ℂ`, real or
complex `κ, τ, σ, ν`, any `λ ≠ 0`, and **all** functions `Φ : ℂ → ℂ`, with
the series read as `tsum` (both sides are the same `tsum` termwise, so no
summability hypothesis is needed; on the source's space of functions
holomorphic near `ℝ`, where the series converge, they are the source's
identities).  **Not formalized (partial coverage of BGS-TRACE-297):** the
consequence that a product along a two-sided geometric twist
`t₀ + aλ^i + bλ^{−i}` is a gauge conjugate of `L_{t₀}^n` up to a unimodular
scalar.  No `sorry`, no `native_decide`.
-/

namespace Bgs.LineN4Gauge

open Complex

/-- `e(x) = exp(2πi x)`. -/
noncomputable def e (x : ℂ) : ℂ := Complex.exp (2 * Real.pi * I * x)

theorem e_add (x y : ℂ) : e x * e y = e (x + y) := by
  unfold e; rw [← Complex.exp_add]; congr 1; ring

variable (w : ℤ → ℂ) (κ lam : ℂ)

/-- The transfer operator `L_τ`. -/
noncomputable def L (τ : ℂ) (Φ : ℂ → ℂ) (s : ℂ) : ℂ :=
  ∑' n : ℤ, w n * e (n * τ) * e (κ * n * s) * Φ ((s + n) / lam)

/-- Translation `T_σ`. -/
def T (σ : ℂ) (Φ : ℂ → ℂ) (s : ℂ) : ℂ := Φ (s + σ)

/-- Modulation `G_ν`. -/
noncomputable def G (ν : ℂ) (Φ : ℂ → ℂ) (s : ℂ) : ℂ := e (ν * s) * Φ s

/-- **Gauge lemma, translation:** `L_τ T_σ = T_{λσ} L_{τ − κλσ}`. -/
theorem gauge_T (hlam : lam ≠ 0) (τ σ : ℂ) (Φ : ℂ → ℂ) :
    L w κ lam τ (T σ Φ) = T (lam * σ) (L w κ lam (τ - κ * lam * σ) Φ) := by
  funext s
  unfold L T
  refine tsum_congr (fun n => ?_)
  have harg : (s + n) / lam + σ = (s + lam * σ + n) / lam := by
    field_simp; ring
  have hexp : e (n * τ) * e (κ * n * s)
      = e (n * (τ - κ * lam * σ)) * e (κ * n * (s + lam * σ)) := by
    rw [e_add, e_add]; congr 1; ring
  rw [harg]
  linear_combination (w n * Φ ((s + lam * σ + n) / lam)) * hexp

/-- **Gauge lemma, modulation:** `L_τ G_ν = G_{ν/λ} L_{τ + ν/λ}`. -/
theorem gauge_G (τ ν : ℂ) (Φ : ℂ → ℂ) :
    L w κ lam τ (G ν Φ) = G (ν / lam) (L w κ lam (τ + ν / lam) Φ) := by
  funext s
  unfold L G
  rw [← tsum_mul_left]
  refine tsum_congr (fun n => ?_)
  have hexp : e (n * τ) * e (κ * n * s) * e (ν * ((s + n) / lam))
      = e (ν / lam * s) * (e (n * (τ + ν / lam)) * e (κ * n * s)) := by
    rw [e_add, e_add, e_add, e_add]; congr 1; ring
  linear_combination (w n * Φ ((s + n) / lam)) * hexp

/-- Gauges commute up to the unimodular scalar `e(νσ)` (referee N4-F1):
`T_σ G_ν = e(νσ) G_ν T_σ`. -/
theorem T_G_comm (σ ν : ℂ) (Φ : ℂ → ℂ) :
    T σ (G ν Φ) = fun s => e (ν * σ) * G ν (T σ Φ) s := by
  funext s
  unfold T G
  rw [← mul_assoc, e_add]; congr 2; ring

end Bgs.LineN4Gauge
