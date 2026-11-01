import Bgs.LineIMoebius

/-!
# BGS-TRACE-218 — regrouping of the pair sums into `∑_j C_Z(jq)` (finite support)

Source: registry statement of `BGS-TRACE-218`.  Notation of `Bgs.LineIAliasing` / `Bgs.LineIMoebius`
(`Φ̂` supported on a finite set `s`, `P : s → ℤ`, `Z_m(θ) = ∑_n Φ̂(n) e(−θ P(n))`), and
`C_Z(k) = ∑_{n,n'} Φ̂(n) conj Φ̂(n') 1[P(n) − P(n') = k]`.

* `regroup_pairs` : `∑_{(n,n')} a(n,n') 1[q ∣ D(n,n')] = ∑'_{j∈ℤ} ∑_{(n,n')} a(n,n') 1[D(n,n') = jq]` (generic, `q ≥ 1`);
* `pairs_eq_tsum_CZ` : `∑_{n,n'} Φ̂(n) conj Φ̂(n') 1[q ∣ P(n) − P(n')] = ∑_{j∈ℤ} C_Z(jq)`;
* `aliasing_CZ` : `(1/q) ∑_{ν mod q} |Z_m(ν/q)|² = ∑_{j∈ℤ} C_Z(jq)` for every `q ≥ 1` (the first identity of the claim);
* `Fm_CZ` : `F_m = φ(2h)⁻¹ ∑_{e ∣ 2h} μ(e) (2h/e) ∑_{j∈ℤ} C_Z(j·2h/e)` (the Möbius formula, `M = 2h`).

**Partial coverage:** finite support only here (the first identity for `∑|Φ̂| < ∞` is the pair-series form of
`Bgs.LineISummable.aliasing_mean`); the summable Möbius case and the regrouping of absolutely convergent pair series are
**not** formalized; the "not claimed" heuristic assessment is out of scope.  All proofs are kernel-checked.
-/

namespace Bgs.LineIRegroup

open Finset ComplexConjugate Bgs.LineIAliasing Bgs.LineIMoebius

theorem regroup_pairs {κ : Type*} (T : Finset κ) (a : κ → ℂ) (D : κ → ℤ) (q : ℤ) (hq : q ≠ 0) :
    ∑ p ∈ T, a p * (if q ∣ D p then 1 else 0)
      = ∑' j : ℤ, ∑ p ∈ T, a p * (if D p = j * q then 1 else 0) := by
  set J := T.image (fun p => D p / q) with hJ
  rw [tsum_eq_sum (s := J)]
  · rw [sum_comm]
    refine sum_congr rfl (fun p hp => ?_)
    rw [← Finset.mul_sum]
    congr 1
    by_cases hd : q ∣ D p
    · obtain ⟨c, hc⟩ := hd
      rw [if_pos ⟨c, hc⟩]
      have hiff : ∀ j : ℤ, (D p = j * q) ↔ (j = c) := by
        intro j; rw [hc, mul_comm j q]
        exact ⟨fun h => (mul_left_cancel₀ hq h).symm, fun h => by rw [h]⟩
      rw [sum_congr rfl (fun j _ => if_congr (hiff j) rfl rfl), sum_ite_eq']
      have : c ∈ J := by
        rw [hJ, mem_image]; exact ⟨p, hp, by rw [hc, Int.mul_ediv_cancel_left _ hq]⟩
      rw [if_pos this]
    · rw [if_neg hd]
      refine (Finset.sum_eq_zero (fun j _ => ?_)).symm
      rw [if_neg]
      intro h; exact hd ⟨j, by rw [h, mul_comm]⟩
  · intro j hj
    refine Finset.sum_eq_zero (fun p hp => ?_)
    rw [if_neg, mul_zero]
    intro h
    apply hj
    rw [hJ, mem_image]
    exact ⟨p, hp, by rw [h, Int.mul_ediv_cancel _ hq]⟩

variable {ι : Type*} (s : Finset ι) (Φ : ι → ℂ) (P : ι → ℤ)

/-- `C_Z(k) = ∑_{n,n'} Φ̂(n) conj Φ̂(n') 1[P(n) − P(n') = k]`. -/
noncomputable def CZ (k : ℤ) : ℂ :=
  ∑ n ∈ s, ∑ n' ∈ s, Φ n * conj (Φ n') * (if P n - P n' = k then 1 else 0)

theorem pairs_eq_tsum_CZ (q : ℤ) (hq : q ≠ 0) :
    ∑ n ∈ s, ∑ n' ∈ s, Φ n * conj (Φ n') * (if q ∣ (P n - P n') then 1 else 0)
      = ∑' j : ℤ, CZ s Φ P (j * q) := by
  unfold CZ
  simp_rw [← sum_product' (f := fun n n' => Φ n * conj (Φ n') * (if q ∣ (P n - P n') then 1 else 0))]
  rw [regroup_pairs (s ×ˢ s) (fun p => Φ p.1 * conj (Φ p.2)) (fun p => P p.1 - P p.2) q hq]
  congr 1; funext j
  rw [sum_product]

theorem aliasing_CZ {q : ℕ} (hq : 0 < q) :
    (1 / (q : ℂ)) * ∑ ν ∈ range q, Z s Φ P ((ν / q : ℝ) : ℂ) * conj (Z s Φ P ((ν / q : ℝ) : ℂ))
      = ∑' j : ℤ, CZ s Φ P (j * q) := by
  rw [aliasing_mean s Φ P hq, pairs_eq_tsum_CZ s Φ P (q : ℤ) (by exact_mod_cast hq.ne')]

theorem Fm_CZ (M : ℕ) (hM : 0 < M) :
    Fm s Φ P M = ((Nat.totient M : ℂ))⁻¹ * ∑ e ∈ M.divisors, ((ArithmeticFunction.moebius e : ℤ) : ℂ) *
      (((M / e : ℕ) : ℂ) * ∑' j : ℤ, CZ s Φ P (j * ((M / e : ℕ) : ℤ))) := by
  rw [Fm_moebius s Φ P M hM]
  congr 1
  refine sum_congr rfl (fun e he => ?_)
  have hpos : 0 < M / e := Nat.div_pos (Nat.divisor_le he) (Nat.pos_of_mem_divisors he)
  rw [pairs_eq_tsum_CZ s Φ P _ (by exact_mod_cast hpos.ne')]

end Bgs.LineIRegroup
