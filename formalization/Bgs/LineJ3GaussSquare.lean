import Bgs.LineJ3PrimeLevel

/-!
# BGS-TRACE-229 — completing the square and the isotropic count (closing the batch-2 gaps)

Source: `mathematics/fixed-map/lineI_rprime_reduction.md` §3 (completed square), `lineJ_d7_twisted_coefficient.md` §6
("Prime levels"); registry boundaries of `BGS-TRACE-212` (definition of `G_t(β)`) and `BGS-TRACE-229`.

`O/q` is modelled as `𝔽_q × 𝔽_q` (`(a, b) ↔ a + b√2`), `Nm(a, b) = a² − 2b²`, `Tr(βγ) = 2(β₁γ₁ + 2β₂γ₂)`, and
`G_t(β) = ∑_γ e(−(t·Nm γ + Tr βγ)/q)` (BGS-TRACE-212), `q` an odd prime, `ψ(x) = e(x/q)`.

* `completing_square` : `G_t(β) = e(t̄·Nm β/q)·G_t(0)` for `t ≠ 0`;
* `gauss_normSq` : `|G_t(0)|² = q²` (`conj G_t(0)·G_t(0) = q²`) for `t ≠ 0`;
* `conj_G_mul_G` : `conj G_t(0)·G_t(β) = q²·e(Nm(β) t̄/q)` — the source identity of BGS-TRACE-229;
* `W_eq` : `q⁻⁴ ∑_{t∈𝔽_q^*, t≠t_b} conj G_t(0) G_t(β) = W_{q,β}` of `Bgs.LineJ3PrimeLevel` (so the values `q⁻²(−1 − e(Nm β t̄_b/q))`,
  `|W| ≤ 2/q²`, `(q − 2)/q²`, and without a missing label `−1/q²`, `(q − 1)/q²` apply to the Gauss-sum weights);
* `two_isSq` : `2y′² = 1 (mod q) ⇒ (y′⁻¹)² = 2` (2 is a square mod q);
* `card_isotropic` : `#{β ≠ 0 : Nm β = 0} = 2(q − 1)` when `s² = 2`.

**Partial coverage:** the label covering (the labels `t = j y′` of the frozen members cover `𝔽_q^*` minus exactly one
`t_b`) depends on the frozen definition of BGS-TRACE-206 and is **not** formalized; the float checks are not formalized.
All proofs are kernel-checked.
-/

namespace Bgs.LineJ3GaussSquare

open Finset ComplexConjugate Bgs.LineJ3PrimeLevel

variable {q : ℕ} [hq : Fact q.Prime]

def Nm (x : ZMod q × ZMod q) : ZMod q := x.1 ^ 2 - 2 * x.2 ^ 2
def trmul (β γ : ZMod q × ZMod q) : ZMod q := 2 * (β.1 * γ.1 + 2 * (β.2 * γ.2))

/-- `G_t(β) = ∑_γ e(−(t·Nm γ + Tr βγ)/q)`. -/
noncomputable def G (t : ZMod q) (β : ZMod q × ZMod q) : ℂ :=
  ∑ γ : ZMod q × ZMod q, (ψ : AddChar (ZMod q) ℂ) (-(t * Nm γ + trmul β γ))

theorem completing_square {t : ZMod q} (ht : t ≠ 0) (β : ZMod q × ZMod q) :
    G t β = (ψ : AddChar (ZMod q) ℂ) (t⁻¹ * Nm β) * G t 0 := by
  set c : ZMod q × ZMod q := (t⁻¹ * β.1, -(t⁻¹ * β.2)) with hc
  unfold G
  rw [mul_sum]
  conv_lhs => rw [← Equiv.sum_comp (Equiv.subRight c)]
  refine sum_congr rfl (fun γ _ => ?_)
  rw [← AddChar.map_add_eq_mul]
  congr 1
  simp only [Equiv.subRight_apply, Nm, trmul, hc, Prod.fst_sub, Prod.snd_sub, Prod.fst_zero, Prod.snd_zero]
  field_simp
  ring

theorem two_ne_zero'' (hq2 : q ≠ 2) : (2 : ZMod q) ≠ 0 := by
  intro h
  have : ((2 : ℕ) : ZMod q) = 0 := by exact_mod_cast h
  rw [ZMod.natCast_eq_zero_iff] at this
  exact hq2 ((Nat.prime_dvd_prime_iff_eq hq.out Nat.prime_two).mp this)

/-- One-variable quadratic Gauss sum `g(a) = ∑_x e(a x²/q)`. -/
noncomputable def g (a : ZMod q) : ℂ := ∑ x : ZMod q, (ψ : AddChar (ZMod q) ℂ) (a * x ^ 2)

theorem g_normSq (hq2 : q ≠ 2) {a : ZMod q} (ha : a ≠ 0) : g a * conj (g a) = q := by
  have h2 := two_ne_zero'' (q := q) hq2
  unfold g
  rw [map_sum, sum_mul_sum]
  have : ∀ x x' : ZMod q, (ψ : AddChar (ZMod q) ℂ) (a * x ^ 2) * conj ((ψ : AddChar (ZMod q) ℂ) (a * x' ^ 2))
      = (ψ : AddChar (ZMod q) ℂ) (a * x ^ 2 - a * x' ^ 2) := by
    intro x x'
    rw [← AddChar.map_neg_eq_conj, ← AddChar.map_add_eq_mul]; congr 1; ring
  simp_rw [this]
  rw [sum_comm]
  have hre : ∀ x' : ZMod q, ∑ x : ZMod q, (ψ : AddChar (ZMod q) ℂ) (a * x ^ 2 - a * x' ^ 2)
      = ∑ u : ZMod q, (ψ : AddChar (ZMod q) ℂ) (a * u ^ 2) * (ψ : AddChar (ZMod q) ℂ) (x' * (2 * a * u)) := by
    intro x'
    rw [← Equiv.sum_comp (Equiv.addRight x')]
    refine sum_congr rfl (fun u _ => ?_)
    rw [← AddChar.map_add_eq_mul]; congr 1; simp only [Equiv.coe_addRight]; ring
  simp_rw [hre]
  rw [sum_comm]
  simp_rw [← mul_sum]
  have horth : ∀ u : ZMod q, ∑ x' : ZMod q, (ψ : AddChar (ZMod q) ℂ) (x' * (2 * a * u))
      = if u = 0 then (q : ℂ) else 0 := by
    intro u
    rw [AddChar.sum_mulShift _ (ZMod.isPrimitive_stdAddChar q), ZMod.card]
    by_cases hu : u = 0
    · simp [hu]
    · have : 2 * a * u ≠ 0 := mul_ne_zero (mul_ne_zero h2 ha) hu
      simp [hu, this]
  simp_rw [horth]
  simp

theorem G_zero_split (t : ZMod q) : G t 0 = g (-t) * g (2 * t) := by
  unfold G g
  rw [sum_mul_sum, ← Fintype.sum_prod_type']
  refine sum_congr rfl (fun γ _ => ?_)
  rw [← AddChar.map_add_eq_mul]; congr 1
  simp only [Nm, trmul, Prod.fst_zero, Prod.snd_zero]; ring

theorem gauss_normSq (hq2 : q ≠ 2) {t : ZMod q} (ht : t ≠ 0) : conj (G t 0) * G t 0 = (q : ℂ) ^ 2 := by
  have h2 := two_ne_zero'' (q := q) hq2
  rw [G_zero_split, map_mul]
  have e1 := g_normSq hq2 (neg_ne_zero.mpr ht)
  have e2 := g_normSq hq2 (mul_ne_zero h2 ht)
  linear_combination (g (2 * t) * conj (g (2 * t))) * e1 + (q : ℂ) * e2

/-- `conj G_t(0)·G_t(β) = q²·e(Nm(β) t̄/q)` for `t ≠ 0`. -/
theorem conj_G_mul_G (hq2 : q ≠ 2) {t : ZMod q} (ht : t ≠ 0) (β : ZMod q × ZMod q) :
    conj (G t 0) * G t β = (q : ℂ) ^ 2 * (ψ : AddChar (ZMod q) ℂ) (Nm β * t⁻¹) := by
  rw [completing_square ht β, mul_comm ((ψ : AddChar (ZMod q) ℂ) _), ← mul_assoc, gauss_normSq hq2 ht, mul_comm t⁻¹]

/-- `q⁻⁴ ∑_{t∈𝔽_q^*, t≠t_b} conj G_t(0) G_t(β) = W_{q,β}` (the weight of `Bgs.LineJ3PrimeLevel`). -/
theorem W_eq (hq2 : q ≠ 2) (β : ZMod q × ZMod q) (tb : ZMod q) :
    ((q : ℂ) ^ 4)⁻¹ * ∑ t ∈ (univ.erase (0 : ZMod q)).erase tb, conj (G t 0) * G t β = W (Nm β) tb := by
  have hq0 : (q : ℂ) ≠ 0 := by exact_mod_cast hq.out.ne_zero
  unfold W
  rw [sum_congr rfl (fun t ht => conj_G_mul_G hq2 (ne_of_mem_erase (mem_of_mem_erase ht)) β), ← mul_sum,
    ← mul_assoc]
  congr 1
  field_simp

theorem two_isSq {y : ZMod q} (hy : 2 * y ^ 2 = 1) : (y⁻¹) ^ 2 = 2 := by
  have hy0 : y ≠ 0 := by rintro rfl; simp at hy
  calc (y⁻¹) ^ 2 = (y⁻¹) ^ 2 * (2 * y ^ 2) := by rw [hy, mul_one]
    _ = 2 := by field_simp

theorem card_isotropic (hq2 : q ≠ 2) {s : ZMod q} (hs : s ^ 2 = 2) :
    (univ.filter (fun β : ZMod q × ZMod q => β ≠ 0 ∧ Nm β = 0)).card = 2 * (q - 1) := by
  have h2 := two_ne_zero'' (q := q) hq2
  have hs0 : s ≠ 0 := by rintro rfl; simp at hs; exact h2 hs.symm
  -- count the zeros of Nm, fibre by fibre over β₂
  have hfib : ∀ b : ZMod q, (univ.filter (fun a : ZMod q => a ^ 2 - 2 * b ^ 2 = 0)).card
      = if b = 0 then 1 else 2 := by
    intro b
    have hset : univ.filter (fun a : ZMod q => a ^ 2 - 2 * b ^ 2 = 0) = {s * b, -(s * b)} := by
      ext a
      simp only [mem_filter, mem_univ, true_and, mem_insert, mem_singleton]
      constructor
      · intro h
        have : (a - s * b) * (a + s * b) = 0 := by linear_combination h - b ^ 2 * hs
        rcases mul_eq_zero.mp this with h1 | h1
        · left; linear_combination h1
        · right; linear_combination h1
      · rintro (rfl | rfl) <;> linear_combination b ^ 2 * hs
    rw [hset]
    split_ifs with hb
    · simp [hb]
    · rw [card_pair]
      intro h
      have : 2 * (s * b) = 0 := by linear_combination h
      rcases mul_eq_zero.mp this with h' | h'
      · exact h2 h'
      · exact (mul_ne_zero hs0 hb) h'
  have hall : (univ.filter (fun β : ZMod q × ZMod q => Nm β = 0)).card = 2 * q - 1 := by
    rw [card_filter, Fintype.sum_prod_type_right]
    have hcol : ∀ b : ZMod q, (∑ a : ZMod q, if Nm (a, b) = 0 then 1 else 0) = if b = 0 then 1 else 2 := by
      intro b; rw [← hfib b, card_filter]; rfl
    simp_rw [hcol]
    rw [sum_ite, sum_const, sum_const]
    have : (univ.filter (fun b : ZMod q => b = 0)).card = 1 := by
      rw [filter_eq' univ (0 : ZMod q)]; simp
    have h' : (univ.filter (fun b : ZMod q => ¬ b = 0)).card = q - 1 := by
      rw [filter_ne' univ (0 : ZMod q), card_erase_of_mem (mem_univ _), card_univ, ZMod.card]
    rw [this, h']
    have := hq.out.two_le
    simp; omega
  have hsplit : univ.filter (fun β : ZMod q × ZMod q => β ≠ 0 ∧ Nm β = 0)
      = (univ.filter (fun β : ZMod q × ZMod q => Nm β = 0)).erase 0 := by
    ext β; simp
  rw [hsplit, card_erase_of_mem (mem_filter.mpr ⟨mem_univ _, by simp [Nm]⟩), hall]
  omega

end Bgs.LineJ3GaussSquare
