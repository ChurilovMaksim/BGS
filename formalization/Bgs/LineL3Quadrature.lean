import Bgs.LineLLineOrth
import Mathlib.NumberTheory.Real.Irrational

/-!
# BGS-TRACE-267 — Lemma Q closure: `γ ∈ 𝔮 ∖ 0 ⇒ |Nm γ| ≥ q`, and the average is exactly `c₀`

Source: registry statement of `BGS-TRACE-267`.  Notation of `Bgs.LineLLineOrth` (`O = ℤ[√2] ≅ ℤ × ℤ`, `γ = a + b√2`,
`Nm γ = a² − 2b²`, `𝔮 = ker φ_s ∘ red` for a root `s² = 2` mod `q`, `ℓ(𝔮)` the isotropic line).

* `nm_eq_zero_iff` : `a² − 2b² = 0 ⇔ a = b = 0` in `ℤ` (irrationality of `√2`);
* `q_le_abs_nm` : `γ ∈ 𝔮`, `γ ≠ 0 ⇒ q ≤ |Nm γ|` (batch-2 `norm_dvd_of_mem` plus the previous item);
* `lemmaQ_c0` : if `c_γ = 0` for every `γ ≠ 0` with `|Nm γ| ≥ q`, then `(1/q) ∑_{β∈ℓ(𝔮)} F(β/q) = c₀` exactly.

**Partial coverage:** the use for `F = f_k` (the band `[I_k − T_k(q), I_k + T_k(q)]` for the isotropic-line mean block
energy with the numerical `T_k(q)`) is **not** formalized.  All proofs are kernel-checked.
-/

namespace Bgs.LineL3Quadrature

open Finset Bgs.LineLLineOrth

theorem nm_eq_zero_iff (a b : ℤ) : a ^ 2 - 2 * b ^ 2 = 0 ↔ a = 0 ∧ b = 0 := by
  constructor
  · intro h
    by_cases hb : b = 0
    · subst hb
      exact ⟨by nlinarith [sq_nonneg a, pow_eq_zero_iff (n := 2) (a := a) two_ne_zero], rfl⟩
    · exfalso
      have hbR : (b : ℝ) ≠ 0 := by exact_mod_cast hb
      have hR : (a : ℝ) ^ 2 = 2 * (b : ℝ) ^ 2 := by
        have : ((a ^ 2 - 2 * b ^ 2 : ℤ) : ℝ) = 0 := by rw [h]; simp
        push_cast at this; linarith
      have hsq : Real.sqrt 2 = |(a : ℝ) / b| := by
        rw [← Real.sqrt_sq_eq_abs, div_pow, hR, mul_div_assoc, div_self (pow_ne_zero 2 hbR), mul_one]
      apply irrational_sqrt_two
      refine ⟨|(a : ℚ) / b|, ?_⟩
      rw [hsq]; push_cast; rfl
  · rintro ⟨rfl, rfl⟩; ring

variable {q : ℕ} [hq : Fact q.Prime]

theorem q_le_abs_nm (s : ZMod q) (hs : s ^ 2 = 2) (γ : ℤ × ℤ) (h : φ s (red γ) = 0) (hγ : γ ≠ 0) :
    (q : ℤ) ≤ |γ.1 ^ 2 - 2 * γ.2 ^ 2| := by
  have hd := norm_dvd_of_mem s hs γ h
  have hne : γ.1 ^ 2 - 2 * γ.2 ^ 2 ≠ 0 := by
    intro h0
    obtain ⟨h1, h2⟩ := (nm_eq_zero_iff _ _).mp h0
    exact hγ (Prod.ext h1 h2)
  exact Int.le_of_dvd (abs_pos.mpr hne) ((dvd_abs _ _).mpr hd)

theorem lemmaQ_c0 (hq2 : q ≠ 2) (s : ZMod q) (hs : s ^ 2 = 2) (c : ℤ × ℤ → ℂ) (hc : Summable c)
    (hlow : ∀ γ : ℤ × ℤ, γ ≠ 0 → (q : ℤ) ≤ |γ.1 ^ 2 - 2 * γ.2 ^ 2| → c γ = 0) :
    (1 / (q : ℂ)) * ∑ β ∈ ell s, (∑' γ : ℤ × ℤ, c γ * (ψ : AddChar (ZMod q) ℂ) (trmul (red γ) β)) = c 0 := by
  rw [lemmaQ hq2 s c hc, tsum_eq_single 0]
  · have : φ s (red (0 : ℤ × ℤ)) = 0 := by unfold φ red; simp
    rw [if_pos this]
  · intro γ hγ
    split_ifs with h
    · exact hlow γ hγ (q_le_abs_nm s hs γ h hγ)
    · rfl

end Bgs.LineL3Quadrature
