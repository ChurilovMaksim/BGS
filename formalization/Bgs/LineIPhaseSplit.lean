import Bgs.LineN4Gauge
import Mathlib.Data.ZMod.Basic
import Mathlib.Algebra.BigOperators.Fin

/-!
# BGS-TRACE-211 — Line I Prop I1: relative phase split (finite-support form)

Source: `mathematics/fixed-map/lineI_rprime_reduction.md`, Prop I1; registry boundary of `BGS-TRACE-211`.
With modulus `M = 2h` (any `M ≥ 1`), a kick `Φ̂`, phases `P(n) ∈ ℤ`,
`Z(ν) = ∑_n Φ̂(n) e(−ν P(n)/M)`, a residue `ν₀` with `Z(ν₀) ≠ 0`,
`σ(p) = Z(ν₀)⁻¹ ∑_{P(n) ≡ p (mod M)} Φ̂(n) e(−ν₀ P(n)/M)` and `σ̂(δ) = ∑_{p ∈ ℤ/M} σ(p) e(−δ p/M)`:

* `sigma_mass` : `∑_p σ(p) = 1` (total mass `1`);
* `phase_split` : `Z(ν₀ + δ) = Z(ν₀) σ̂(δ)` for **every integer** `δ`.

**Partial coverage:** the kick is indexed by an arbitrary *finite* set of words `n` (the source allows
`∑ |Φ̂| < ∞`, e.g. the infinitely supported k1 kick with Bessel coefficients; the absolutely convergent case is
the same rearrangement and is formalized in `Bgs.LineISummable`, Lean batch 3).  `ν₀` may be any complex number (the "unit" hypothesis of
the source is not needed for the identity).  All proofs are kernel-checked.
-/

namespace Bgs.LineIPhaseSplit

open Bgs.LineN4Gauge Finset

theorem e_intCast (k : ℤ) : e (k : ℂ) = 1 := by
  unfold e
  have : 2 * (Real.pi : ℂ) * Complex.I * k = k * (2 * Real.pi * Complex.I) := by ring
  rw [this, Complex.exp_int_mul_two_pi_mul_I]

variable {ι : Type*} (s : Finset ι) (Φ : ι → ℂ) (P : ι → ℤ) (M : ℕ) [NeZero M]

/-- `Z(ν) = ∑_n Φ̂(n) e(−ν P(n)/M)`. -/
noncomputable def Z (ν : ℂ) : ℂ := ∑ n ∈ s, Φ n * e (-ν * P n / M)

/-- `σ(p) = Z(ν₀)⁻¹ ∑_{P(n) ≡ p} Φ̂(n) e(−ν₀ P(n)/M)`. -/
noncomputable def sigma (ν0 : ℂ) (p : ZMod M) : ℂ :=
  (Z s Φ P M ν0)⁻¹ * ∑ n ∈ s with ((P n : ZMod M) = p), Φ n * e (-ν0 * P n / M)

/-- `σ̂(δ) = ∑_p σ(p) e(−δ p/M)` (with the representative `p.val ∈ [0, M)`). -/
noncomputable def sigmaHat (ν0 δ : ℂ) : ℂ :=
  ∑ p : ZMod M, sigma s Φ P M ν0 p * e (-δ * (p.val : ℂ) / M)

theorem sigma_mass (ν0 : ℂ) (hZ : Z s Φ P M ν0 ≠ 0) : ∑ p : ZMod M, sigma s Φ P M ν0 p = 1 := by
  unfold sigma
  rw [← mul_sum, sum_fiberwise s (fun n => (P n : ZMod M))]
  exact inv_mul_cancel₀ hZ

/-- For `P(n) ≡ p (mod M)` and integer `δ`, `e(−δ p/M) = e(−δ P(n)/M)`. -/
theorem e_shift (δ : ℤ) (n : ι) :
    e (-(δ : ℂ) * (((P n : ZMod M)).val : ℂ) / M) = e (-(δ : ℂ) * P n / M) := by
  have hM : (M : ℂ) ≠ 0 := by exact_mod_cast NeZero.ne M
  have hv : (((P n : ZMod M)).val : ℤ) = P n % M := ZMod.val_intCast (P n)
  have hdiv : P n % M + (M:ℤ) * (P n / M) = P n := by exact Int.emod_add_mul_ediv (P n) M
  have key : -(δ : ℂ) * (((P n : ZMod M)).val : ℂ) / M
      = -(δ : ℂ) * P n / M + ((δ * (P n / M) : ℤ) : ℂ) := by
    have h1 : ((((P n : ZMod M)).val : ℕ) : ℂ) = ((P n % M : ℤ) : ℂ) := by exact_mod_cast hv
    rw [h1]
    have h2 : ((P n : ℤ) : ℂ) = ((P n % M : ℤ) : ℂ) + (M : ℂ) * ((P n / M : ℤ) : ℂ) := by
      exact_mod_cast hdiv.symm
    rw [h2]; push_cast; field_simp; ring
  rw [key, ← e_add, e_intCast, mul_one]

/-- **Prop I1:** `Z(ν₀ + δ) = Z(ν₀) σ̂(δ)` for every integer `δ`. -/
theorem phase_split (ν0 : ℂ) (hZ : Z s Φ P M ν0 ≠ 0) (δ : ℤ) :
    Z s Φ P M (ν0 + δ) = Z s Φ P M ν0 * sigmaHat s Φ P M ν0 δ := by
  unfold sigmaHat sigma
  simp_rw [mul_assoc, sum_mul]
  rw [mul_sum]
  simp_rw [← mul_assoc, mul_inv_cancel₀ hZ, one_mul]
  conv_lhs => unfold Z; rw [← sum_fiberwise s (fun n => (P n : ZMod M))]
  refine sum_congr rfl (fun p _ => sum_congr rfl (fun n hn => ?_))
  rw [mem_filter] at hn
  rw [← hn.2, e_shift P M δ n, mul_assoc, e_add]
  congr 2; ring

end Bgs.LineIPhaseSplit
