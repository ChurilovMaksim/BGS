import Mathlib.Analysis.SpecialFunctions.Complex.CircleAddChar

/-!
# BGS-TRACE-204 — Line G G3 dilution identity (completed square at every odd level `d`)

Source: `mathematics/fixed-map/resonance_classification_lineG.md`, `lineI_rprime_reduction.md` §3; registry boundary of
`BGS-TRACE-204`.  `O/d` is modelled as `ℤ/d × ℤ/d` (`(a, b) ↔ a + b√2`), `Nm(a, b) = a² − 2b²`, `Tr(βγ) = 2(β₁γ₁ + 2β₂γ₂)`,
`ψ(x) = e(x/d)`, `G_t(β) = ∑_γ e(−(t·Nm γ + Tr βγ)/d)`, `G_d(t) = G_t(0)`; `t` a unit mod `d` with inverse `t̄`.  `d` is any
modulus (prime or composite; oddness is not needed for this identity).

* `completing_square` : `t·Nm γ + Tr βγ = t·Nm(γ + t̄·conj β) − t̄·Nm β` in `ℤ/d`, hence `G_t(β) = e(t̄·Nm β/d)·G_d(t)`;
* `dilution` : for any twisted sums `Ẑ(β)`, `d⁻² ∑_β Ẑ(β) G_t(β) = (G_d(t)/d²) ∑_β e(t̄·Nm β/d) Ẑ(β)` — with Prop I2′
  (`Z(ν₀ + 2hj/d) = d⁻² ∑_β Ẑ(β)G_t(β)`, BGS-TRACE-212) this is the displayed G3 formula;
* `sum_neg_invariant` : the weighted sum is unchanged under `β ↦ −β` (`Nm(−β) = Nm β`).

**Partial coverage:** Prop I2′ (BGS-TRACE-212; the Fourier step and the congruence `P(n) ≡ y′Nm(α_n)`) is the input, not
re-proved here; `|G_d(t)| = d` is formalized only at prime levels (`Bgs.LineJ3GaussSquare.gauss_normSq`), not for composite
`d`; the brute-force checks are not formalized.  All proofs are kernel-checked.
-/

namespace Bgs.LineGDilution

open Finset

variable {d : ℕ} [NeZero d]

noncomputable abbrev ψ : AddChar (ZMod d) ℂ := ZMod.stdAddChar

def Nm (x : ZMod d × ZMod d) : ZMod d := x.1 ^ 2 - 2 * x.2 ^ 2
def trmul (β γ : ZMod d × ZMod d) : ZMod d := 2 * (β.1 * γ.1 + 2 * (β.2 * γ.2))
/-- Galois conjugate `conj(a + b√2) = a − b√2`. -/
def cj (x : ZMod d × ZMod d) : ZMod d × ZMod d := (x.1, -x.2)

noncomputable def G (t : ZMod d) (β : ZMod d × ZMod d) : ℂ :=
  ∑ γ : ZMod d × ZMod d, (ψ : AddChar (ZMod d) ℂ) (-(t * Nm γ + trmul β γ))

omit [NeZero d] in
theorem square_identity (t tb : ZMod d) (ht : t * tb = 1) (β γ : ZMod d × ZMod d) :
    t * Nm γ + trmul β γ = t * Nm (γ + tb • cj β) - tb * Nm β := by
  simp only [Nm, trmul, cj, Prod.fst_add, Prod.snd_add, Prod.smul_fst, Prod.smul_snd, smul_eq_mul]
  linear_combination (-(2 * β.1 * γ.1 + 4 * β.2 * γ.2 + tb * β.1 ^ 2 - 2 * tb * β.2 ^ 2)) * ht

theorem completing_square (t tb : ZMod d) (ht : t * tb = 1) (β : ZMod d × ZMod d) :
    G t β = (ψ : AddChar (ZMod d) ℂ) (tb * Nm β) * G t 0 := by
  unfold G
  rw [mul_sum]
  conv_rhs => rw [← Equiv.sum_comp (Equiv.addRight (tb • cj β))]
  refine sum_congr rfl (fun γ _ => ?_)
  rw [← AddChar.map_add_eq_mul, square_identity t tb ht β γ]
  congr 1
  have h0 : ∀ x : ZMod d × ZMod d, trmul 0 x = 0 := by intro x; unfold trmul; rw [Prod.fst_zero, Prod.snd_zero]; ring
  rw [h0, Equiv.coe_addRight]; ring

theorem dilution (t tb : ZMod d) (ht : t * tb = 1) (Zhat : ZMod d × ZMod d → ℂ) :
    ((d : ℂ) ^ 2)⁻¹ * ∑ β, Zhat β * G t β
      = (G t 0 / (d : ℂ) ^ 2) * ∑ β, (ψ : AddChar (ZMod d) ℂ) (tb * Nm β) * Zhat β := by
  rw [Finset.mul_sum, Finset.mul_sum]
  refine sum_congr rfl (fun β _ => ?_)
  rw [completing_square t tb ht β]; ring

theorem sum_neg_invariant (tb : ZMod d) (Zhat : ZMod d × ZMod d → ℂ) :
    ∑ β, (ψ : AddChar (ZMod d) ℂ) (tb * Nm β) * Zhat (-β)
      = ∑ β, (ψ : AddChar (ZMod d) ℂ) (tb * Nm β) * Zhat β := by
  rw [← Equiv.sum_comp (Equiv.neg (ZMod d × ZMod d))]
  refine sum_congr rfl (fun β _ => ?_)
  have hN : Nm (-β) = Nm β := by unfold Nm; rw [Prod.fst_neg, Prod.snd_neg]; ring
  rw [Equiv.neg_apply, hN, neg_neg]

end Bgs.LineGDilution
