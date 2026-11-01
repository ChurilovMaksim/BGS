import Bgs.LineJ3PrimeLevel

/-!
# BGS-TRACE-293 — Line N3 M6 condition C3: `W_{q,β}(−ρ) = conj W_{q,β}(ρ)` at prime levels

Source: `mathematics/fixed-map/lineN2N4_inherited_level.md`; registry boundary of `BGS-TRACE-293`.  Notation of
`Bgs.LineJ3PrimeLevel` (`q` prime, `W N t_b = q⁻² ∑_{t∈𝔽_q^*, t≠t_b} e(N t̄/q)`, `N = N(β) mod q`).

* `nu0_neg` : `8ν₀ ≡ 2s·g` with `8` a unit gives `ν₀(−ρ) = −ν₀(ρ)` (the sign `s` of `ρ = (±2, 8)` flips);
* `label_neg` : the missing label `t_b = j_b y′` with `ν₀ + c·j_b ≡ 0` (`c = 2h/q`, a unit mod `q`, `y′` independent of `ρ`)
  satisfies `t_b(−ρ) = −t_b(ρ)`;
* `W_neg_label` : `W N (−t_b) = conj (W N t_b)` for every `N` — hence `W_{q,β}(−ρ) = conj W_{q,β}(ρ)`;
* `W_sign_conj` : the combined statement from `ν₀(−ρ) = −ν₀(ρ)`; `isotropic_equal` : the isotropic weights `(q − 2)/q²` agree.

**Partial coverage:** prime levels only; the composite levels via inheritance (BGS-TRACE-228, `n_e` independent of the
sign) and the comparison with BGS-TRACE-221(ii) are **not** formalized; the label covering (that the members' labels miss
exactly `t_b`) is taken from the frozen definition as in BGS-TRACE-229.  All proofs are kernel-checked.
-/

namespace Bgs.LineN3SignConj

open Finset ComplexConjugate Bgs.LineJ3PrimeLevel

variable {q : ℕ} [hq : Fact q.Prime]

theorem nu0_neg (i8 g ν ν' : ZMod q) (h8 : 8 * i8 = 1) (hν : 8 * ν = 2 * g) (hν' : 8 * ν' = 2 * (-g)) : ν' = -ν := by
  linear_combination i8 * hν' + i8 * hν - (ν' + ν) * h8

/-- The missing label `t_b = j_b y′`, `ν₀ + c j_b = 0`, `c c̄ = 1`. -/
def label (_c cbar y ν0 : ZMod q) : ZMod q := (-ν0 * cbar) * y

theorem label_spec (c cbar _y ν0 : ZMod q) (hc : c * cbar = 1) : ν0 + c * (-ν0 * cbar) = 0 := by
  linear_combination (-ν0) * hc

theorem label_neg (c cbar y ν0 : ZMod q) : label c cbar y (-ν0) = -label c cbar y ν0 := by
  unfold label; ring

theorem W_neg_label (N tb : ZMod q) : W N (-tb) = conj (W N tb) := by
  unfold W
  rw [map_mul, map_sum, map_inv₀, map_pow, map_natCast]
  congr 1
  refine sum_nbij' (fun t => -t) (fun t => -t) (fun t ht => ?_) (fun t ht => ?_) (fun t _ => neg_neg t)
    (fun t _ => neg_neg t) (fun t _ => ?_)
  · simp only [mem_erase, mem_univ, and_true] at ht ⊢
    exact ⟨fun h => ht.1 (neg_eq_iff_eq_neg.mp h), neg_ne_zero.mpr ht.2⟩
  · simp only [mem_erase, mem_univ, and_true] at ht ⊢
    exact ⟨fun h => ht.1 (neg_injective h), neg_ne_zero.mpr ht.2⟩
  · rw [← AddChar.map_neg_eq_conj, inv_neg, mul_neg, neg_neg]

theorem W_sign_conj (c cbar y ν0 ν0' N : ZMod q) (hneg : ν0' = -ν0) :
    W N (label c cbar y ν0') = conj (W N (label c cbar y ν0)) := by
  rw [hneg, label_neg, W_neg_label]

theorem isotropic_equal (tb : ZMod q) (htb : tb ≠ 0) : W (0 : ZMod q) (-tb) = W 0 tb := by
  rw [W_isotropic htb, W_isotropic (neg_ne_zero.mpr htb)]

end Bgs.LineN3SignConj
