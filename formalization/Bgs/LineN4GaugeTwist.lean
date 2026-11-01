import Bgs.LineN4Gauge

/-!
# BGS-TRACE-297 — geometric-twist corollary of the Line N4 gauge lemma

Source: `computations/verification/lineN4/REPORT_N4.md` §3.1 (Corollary) and the registry boundary of
`BGS-TRACE-297`: "a product along a two-sided geometric twist `t₀ + aλ^i + bλ^{−i}` is a gauge conjugate of
`L_{t₀}^n` up to a unimodular scalar".  With `τ_i = t₀ + aλ^i + bλ^{−i}`, `σ_i = −aλ^{i−1}/κ`, `ν_i = bλ^{1−i}`
(`κ ≠ 0`, `λ ≠ 0`) and the ordered product `Π_{i<n} L_{τ_i} = L_{τ_{n−1}} ∘ ⋯ ∘ L_{τ_0}` (`twistProd`):

* `twist_step` : `L_{τ_i} = T_{−σ_{i+1}} G_{−ν_{i+1}} L_{t₀} G_{ν_i} T_{σ_i}`;
* `twist_product` : `Π_{i<n} L_{τ_i} = T_{−λσ_{n−1}} G_{−bλ^{1−n}} · L_{t₀}^n · G_{λb} T_{σ_0}`
  (written with `σ_n = λσ_{n−1}`, `ν_n = bλ^{1−n}`, `ν_0 = λb`), i.e. the REPORT_N4 formula **exactly**;
* `twist_product_up_to_scalar` : the registered form — there is `c` with `‖c‖ = 1` (here `c = 1`) such that the
  product equals `c` times the gauge conjugate.

With this composition order and this nesting of the gauges the scalar is exactly `1`; the referee's
unimodular factor `e(νσ)` (N4-F1, `T_G_comm`) only appears if the `T` and `G` gauges are reordered.  The
identities hold for arbitrary weights, complex `a, b, t₀`, and all functions `ℂ → ℂ` (series as `tsum`).
**Not formalized:** the disc-space (small-gauge) reading and every bound built on it.  All proofs are kernel-checked.
-/

namespace Bgs.LineN4GaugeTwist

open Bgs.LineN4Gauge Complex

variable (w : ℤ → ℂ) (κ lam : ℂ)

theorem T_cancel (x : ℂ) (Φ : ℂ → ℂ) : T (-x) (T x Φ) = Φ := by
  funext s; simp [T]

theorem G_cancel (x : ℂ) (Φ : ℂ → ℂ) : G (-x) (G x Φ) = Φ := by
  funext s; unfold G; rw [← mul_assoc, e_add]
  have : -x * s + x * s = 0 := by ring
  rw [this]; simp [e]

theorem T_cancel' (x : ℂ) (Φ : ℂ → ℂ) : T x (T (-x) Φ) = Φ := by
  simpa using T_cancel (-x) Φ

theorem G_cancel' (x : ℂ) (Φ : ℂ → ℂ) : G x (G (-x) Φ) = Φ := by
  simpa using G_cancel (-x) Φ

/-- Twist parameters. -/
noncomputable def tau (t0 a b : ℂ) (i : ℕ) : ℂ := t0 + a * lam ^ i + b / lam ^ i
noncomputable def sig (a : ℂ) (i : ℕ) : ℂ := -a * lam ^ i / (κ * lam)
noncomputable def nu (b : ℂ) (i : ℕ) : ℂ := b * lam / lam ^ i

/-- The ordered product `L_{τ_{n−1}} ∘ ⋯ ∘ L_{τ_0}`. -/
noncomputable def twistProd (t0 a b : ℂ) : ℕ → (ℂ → ℂ) → (ℂ → ℂ)
  | 0, Φ => Φ
  | n + 1, Φ => L w κ lam (tau lam t0 a b n) (twistProd t0 a b n Φ)

theorem twist_step (hk : κ ≠ 0) (hl : lam ≠ 0) (t0 a b : ℂ) (i : ℕ) (Φ : ℂ → ℂ) :
    L w κ lam (tau lam t0 a b i) Φ
      = T (-sig κ lam a (i + 1)) (G (-nu lam b (i + 1))
          (L w κ lam t0 (G (nu lam b i) (T (sig κ lam a i) Φ)))) := by
  have hli : lam ^ i ≠ 0 := pow_ne_zero _ hl
  rw [gauge_G, gauge_T w κ lam hl]
  have hν : nu lam b i / lam = nu lam b (i + 1) := by
    unfold nu; field_simp; ring
  have hσ : lam * sig κ lam a i = sig κ lam a (i + 1) := by
    unfold sig; field_simp; ring
  have hτ : t0 + nu lam b (i + 1) - κ * lam * sig κ lam a i = tau lam t0 a b i := by
    unfold nu sig tau; field_simp; ring
  rw [hν, hσ, hτ, G_cancel, T_cancel]

/-- **Corollary (exact form):** `Π_{i<n} L_{τ_i} = T_{−σ_n} G_{−ν_n} L_{t₀}^n G_{ν_0} T_{σ_0}`. -/
theorem twist_product (hk : κ ≠ 0) (hl : lam ≠ 0) (t0 a b : ℂ) (n : ℕ) (Φ : ℂ → ℂ) :
    twistProd w κ lam t0 a b n Φ
      = T (-sig κ lam a n) (G (-nu lam b n)
          ((L w κ lam t0)^[n] (G (nu lam b 0) (T (sig κ lam a 0) Φ)))) := by
  induction n with
  | zero => simp [twistProd, G_cancel, T_cancel]
  | succ n ih =>
    rw [twistProd, ih, twist_step w κ lam hk hl, T_cancel', G_cancel', Function.iterate_succ_apply']

/-- The gauge endpoints are those of REPORT_N4: `σ_n = λσ_{n−1}`, `ν_n = bλ^{1−n}` (as `bλ/λ^n`), `ν_0 = λb`. -/
theorem endpoints (hk : κ ≠ 0) (hl : lam ≠ 0) (a b : ℂ) (n : ℕ) :
    sig κ lam a (n + 1) = lam * sig κ lam a n ∧ nu lam b 0 = lam * b := by
  constructor
  · unfold sig; field_simp; ring
  · unfold nu; simp; ring

/-- **Registered form:** the product is, up to a unimodular scalar (here exactly `1`), the gauge conjugate
`T_{−σ_n} G_{−ν_n} L_{t₀}^n G_{ν_0} T_{σ_0}` of `L_{t₀}^n`. -/
theorem twist_product_up_to_scalar (hk : κ ≠ 0) (hl : lam ≠ 0) (t0 a b : ℂ) (n : ℕ) :
    ∃ c : ℂ, ‖c‖ = 1 ∧ ∀ Φ : ℂ → ℂ, twistProd w κ lam t0 a b n Φ
      = fun s => c * T (-sig κ lam a n) (G (-nu lam b n)
          ((L w κ lam t0)^[n] (G (nu lam b 0) (T (sig κ lam a 0) Φ)))) s :=
  ⟨1, by simp, fun Φ => by rw [twist_product w κ lam hk hl]; simp⟩

end Bgs.LineN4GaugeTwist
