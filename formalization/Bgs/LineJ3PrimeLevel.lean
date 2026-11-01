import Mathlib.Analysis.SpecialFunctions.Complex.CircleAddChar
import Mathlib.NumberTheory.LegendreSymbol.AddCharacter
import Mathlib.Data.ZMod.Basic

/-!
# BGS-TRACE-229 — Line J3 prime levels: the complete-sum step (finite-field part)

Source: `mathematics/fixed-map/lineJ_d7_twisted_coefficient.md` §6 "Prime levels"; registry boundary of `BGS-TRACE-229`.
For a prime `q`, write `ψ(x) = e(x/q)` (`ZMod.stdAddChar`, i.e. `exp(2πi·x.val/q)`), `N = N(β) mod q`, and let
`t_b ∈ F_q^*` be the single missing label.  After completing the square (source step
`conj G_t(0) G_t(β) = q²·e(N(β) t̄/q)`) the weight is
`W_{q,β} = q⁻² ∑_{t ∈ F_q^*, t ≠ t_b} e(N t̄/q)`; this file proves, for that sum:

* `W_nonisotropic` : `N ≠ 0 ⇒ W = q⁻²(−1 − e(N t̄_b/q))`, and `W_nonisotropic_norm` : `‖W‖ ≤ 2/q²`;
* `W_isotropic` : `N = 0 ⇒ W = (q − 2)/q²`;
* `Wfull_nonisotropic`, `Wfull_isotropic` (case `q² | h`, no missing label):
  `q⁻² ∑_{t ∈ F_q^*} e(N t̄/q) = −1/q²` (absolute value `1/q²`) resp. `(q − 1)/q²`.

**Partial coverage:** the completing-the-square identity `conj G_t(0)G_t(β) = q² e(N(β)t̄/q)`, the fact that the labels
`t = j y′` cover `F_q^*` minus exactly one value `t_b`, and the count `2(q − 1)` of isotropic `β ≠ 0` (with `2` a square
mod `q`) are the source's inputs and are **not** formalized in this file; this file formalizes the complete character-sum
evaluation and the resulting values/bound.  (Lean batch 3: the completing-the-square identity, `2` a square and the isotropic
count are proved in `Bgs.LineJ3GaussSquare`; only the label covering remains unformalized.)  The float checks (q = 41, 31) are not formalized.  The claim's
heuristic remark on m = 3p is not part of the claim.  All proofs are kernel-checked.
-/

namespace Bgs.LineJ3PrimeLevel

open Finset

variable {q : ℕ} [hq : Fact q.Prime]

/-- `ψ(x) = e(x/q)` on `ZMod q`. -/
noncomputable abbrev ψ : AddChar (ZMod q) ℂ := ZMod.stdAddChar

theorem psi_ne_one : (ψ : AddChar (ZMod q) ℂ) ≠ 1 := by
  intro h
  have h1 : (ψ : AddChar (ZMod q) ℂ) 1 = (ψ : AddChar (ZMod q) ℂ) 0 := by
    rw [h, AddChar.map_zero_eq_one]; rfl
  have := ZMod.injective_stdAddChar h1
  exact one_ne_zero this

theorem psi_norm (x : ZMod q) : ‖(ψ : AddChar (ZMod q) ℂ) x‖ = 1 := by
  rw [ZMod.stdAddChar_apply]; exact Circle.norm_coe _

/-- `∑_{t ∈ F_q} e(N t̄/q) = 0` for `N ≠ 0` (with `0⁻¹ = 0`). -/
theorem sum_inv_all {N : ZMod q} (hN : N ≠ 0) : ∑ t : ZMod q, (ψ : AddChar (ZMod q) ℂ) (N * t⁻¹) = 0 := by
  have hinj : Function.Injective (fun t : ZMod q => N * t⁻¹) := by
    intro x y hxy
    simpa using mul_left_cancel₀ hN hxy
  have hbij : Function.Bijective (fun t : ZMod q => N * t⁻¹) := Finite.injective_iff_bijective.mp hinj
  rw [Function.Bijective.sum_comp hbij (fun x => (ψ : AddChar (ZMod q) ℂ) x)]
  exact AddChar.sum_eq_zero_of_ne_one psi_ne_one

/-- `∑_{t ∈ F_q^*} e(N t̄/q) = −1` for `N ≠ 0`. -/
theorem sum_inv_units {N : ZMod q} (hN : N ≠ 0) :
    ∑ t ∈ univ.erase (0 : ZMod q), (ψ : AddChar (ZMod q) ℂ) (N * t⁻¹) = -1 := by
  rw [sum_erase_eq_sub (mem_univ _), sum_inv_all hN]
  simp

/-- The weight `W_{q,β} = q⁻² ∑_{t ∈ F_q^*, t ≠ t_b} e(N t̄/q)`. -/
noncomputable def W (N tb : ZMod q) : ℂ :=
  ((q : ℂ) ^ 2)⁻¹ * ∑ t ∈ (univ.erase (0 : ZMod q)).erase tb, (ψ : AddChar (ZMod q) ℂ) (N * t⁻¹)

/-- No missing label (`q² | h`): `q⁻² ∑_{t ∈ F_q^*} e(N t̄/q)`. -/
noncomputable def Wfull (N : ZMod q) : ℂ :=
  ((q : ℂ) ^ 2)⁻¹ * ∑ t ∈ univ.erase (0 : ZMod q), (ψ : AddChar (ZMod q) ℂ) (N * t⁻¹)

theorem W_nonisotropic {N tb : ZMod q} (hN : N ≠ 0) (htb : tb ≠ 0) :
    W N tb = ((q : ℂ) ^ 2)⁻¹ * (-1 - (ψ : AddChar (ZMod q) ℂ) (N * tb⁻¹)) := by
  unfold W
  rw [sum_erase_eq_sub (mem_erase.mpr ⟨htb, mem_univ _⟩), sum_inv_units hN]

theorem W_nonisotropic_norm {N tb : ZMod q} (hN : N ≠ 0) (htb : tb ≠ 0) :
    ‖W N tb‖ ≤ 2 / (q : ℝ) ^ 2 := by
  rw [W_nonisotropic hN htb, norm_mul, norm_inv, norm_pow, Complex.norm_natCast]
  have h : ‖(-1 : ℂ) - (ψ : AddChar (ZMod q) ℂ) (N * tb⁻¹)‖ ≤ 2 := by
    calc _ ≤ ‖(-1 : ℂ)‖ + ‖(ψ : AddChar (ZMod q) ℂ) (N * tb⁻¹)‖ := norm_sub_le _ _
      _ = 2 := by rw [psi_norm]; norm_num
  have hq0 : (0 : ℝ) < (q : ℝ) ^ 2 := by
    have := hq.out.pos; positivity
  rw [div_eq_inv_mul]
  exact mul_le_mul_of_nonneg_left h (inv_nonneg.mpr hq0.le)

theorem card_units_erase {tb : ZMod q} (htb : tb ≠ 0) :
    ((univ.erase (0 : ZMod q)).erase tb).card = q - 2 := by
  rw [card_erase_of_mem (mem_erase.mpr ⟨htb, mem_univ _⟩), card_erase_of_mem (mem_univ _),
    card_univ, ZMod.card]
  omega

theorem W_isotropic {tb : ZMod q} (htb : tb ≠ 0) :
    W (0 : ZMod q) tb = ((q : ℂ) - 2) / (q : ℂ) ^ 2 := by
  unfold W
  simp only [zero_mul, AddChar.map_zero_eq_one, sum_const, card_units_erase htb, nsmul_eq_mul, mul_one]
  have h2 : 2 ≤ q := hq.out.two_le
  rw [Nat.cast_sub h2]; push_cast; ring

theorem Wfull_nonisotropic {N : ZMod q} (hN : N ≠ 0) : Wfull N = -((q : ℂ) ^ 2)⁻¹ := by
  unfold Wfull; rw [sum_inv_units hN]; ring

theorem Wfull_isotropic : Wfull (0 : ZMod q) = ((q : ℂ) - 1) / (q : ℂ) ^ 2 := by
  unfold Wfull
  simp only [zero_mul, AddChar.map_zero_eq_one, sum_const, nsmul_eq_mul, mul_one]
  rw [card_erase_of_mem (mem_univ _), card_univ, ZMod.card]
  have h1 : 1 ≤ q := hq.out.one_lt.le
  rw [Nat.cast_sub h1]; push_cast; ring

end Bgs.LineJ3PrimeLevel
