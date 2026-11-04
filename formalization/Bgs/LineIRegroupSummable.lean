import Bgs.LineIMoebiusSummable
import Bgs.LineIRegroup

/-!
# BGS-TRACE-218 — regrouping of absolutely convergent pair series into `∑_j C_Z(jq)`

Source: registry statement of `BGS-TRACE-218`.  Notation of `Bgs.LineISummable` / `Bgs.LineIMoebiusSummable`: the kick
`Φ̂` is indexed by an arbitrary type `ι` (e.g. `ℤ^m`) with `∑ |Φ̂(n)| < ∞`, `Z_m(θ) = ∑'_n Φ̂(n) e(−θ P(n))`, and
`C_Z(k) = ∑'_{(n,n′)} Φ̂(n) conj Φ̂(n′) 1[P(n) − P(n′) = k]` (an absolutely convergent pair series).

* `regroup_tsum` : for `∑ |a| < ∞` and `q ≠ 0`, `∑'_p a(p) 1[q ∣ D(p)] = ∑'_{j∈ℤ} ∑'_p a(p) 1[D(p) = jq]` (generic);
* `pairs_eq_tsum_CZS` : `∑'_{(n,n′)} Φ̂(n) conj Φ̂(n′) 1[q ∣ P(n) − P(n′)] = ∑'_{j∈ℤ} C_Z(jq)`;
* `aliasing_CZS` : `(1/q) ∑_{ν mod q} |Z_m(ν/q)|² = ∑_{j∈ℤ} C_Z(jq)` for every `q ≥ 1` (first identity of the claim);
* `FmS_CZS` : `F_m = φ(2h)⁻¹ ∑_{e ∣ 2h} μ(e) (2h/e) ∑_{j∈ℤ} C_Z(j·2h/e)` (Möbius formula, `M = 2h`).

Together with the finite-support module `Bgs.LineIRegroup` this covers both identities of the claim for every kick with
`∑ |Φ̂| < ∞`.  The "not claimed" heuristic assessment is out of scope.  All proofs are kernel-checked.
-/

namespace Bgs.LineIRegroupSummable

open Finset ComplexConjugate Bgs.LineISummable Bgs.LineIMoebiusSummable

theorem regroup_tsum {κ : Type*} (a : κ → ℂ) (ha : Summable (fun p => ‖a p‖)) (D : κ → ℤ) (q : ℤ) (hq : q ≠ 0) :
    ∑' p, a p * (if q ∣ D p then 1 else 0)
      = ∑' j : ℤ, ∑' p, a p * (if D p = j * q then 1 else 0) := by
  set F : ℤ → κ → ℂ := fun j p => a p * (if D p = j * q then 1 else 0) with hF
  have hinner : ∀ p, ∑' j : ℤ, F j p = a p * (if q ∣ D p then 1 else 0) := by
    intro p
    by_cases hd : q ∣ D p
    · obtain ⟨c, hc⟩ := hd
      rw [if_pos ⟨c, hc⟩, tsum_eq_single c]
      · simp [hF, hc, mul_comm]
      · intro j hj
        simp only [hF]
        rw [if_neg, mul_zero]
        intro h; apply hj
        rw [hc, mul_comm q c] at h
        exact (mul_right_cancel₀ hq h).symm
    · rw [if_neg hd, mul_zero]
      refine (tsum_congr (fun j => ?_)).trans tsum_zero
      simp only [hF]
      rw [if_neg, mul_zero]
      intro h; exact hd ⟨j, by rw [h, mul_comm]⟩
  have hsum : Summable (Function.uncurry F) := by
    let g : κ → ℤ × κ := fun p => (D p / q, p)
    have hg : Function.Injective g := fun p p' h => (Prod.ext_iff.mp h).2
    rw [← hg.summable_iff]
    · refine Summable.of_norm_bounded ha (fun p => ?_)
      simp only [Function.comp, Function.uncurry, g, hF, norm_mul]
      split_ifs <;> simp
    · rintro ⟨j, p⟩ hx
      simp only [Function.uncurry, hF]
      rw [if_neg, mul_zero]
      intro h; apply hx
      exact ⟨p, by simp [g, h, Int.mul_ediv_cancel _ hq]⟩
  rw [← hsum.tsum_comm]
  exact (tsum_congr hinner).symm

variable {ι : Type*} (Φ : ι → ℂ) (hΦ : Summable (fun n => ‖Φ n‖)) (P : ι → ℤ)

/-- `C_Z(k) = ∑'_{(n,n′)} Φ̂(n) conj Φ̂(n′) 1[P(n) − P(n′) = k]`. -/
noncomputable def CZS (k : ℤ) : ℂ :=
  ∑' z : ι × ι, Φ z.1 * conj (Φ z.2) * (if P z.1 - P z.2 = k then 1 else 0)

include hΦ in
theorem summable_pair : Summable (fun z : ι × ι => ‖Φ z.1 * conj (Φ z.2)‖) := by
  have := summable_mul_of_summable_norm (R := ℝ) (f := fun n => ‖Φ n‖) (g := fun n => ‖Φ n‖)
    (by simpa using hΦ) (by simpa using hΦ)
  refine this.congr (fun z => ?_)
  simp

include hΦ in
theorem pairs_eq_tsum_CZS (q : ℤ) (hq : q ≠ 0) :
    ∑' z : ι × ι, Φ z.1 * conj (Φ z.2) * (if q ∣ (P z.1 - P z.2) then 1 else 0)
      = ∑' j : ℤ, CZS Φ P (j * q) :=
  regroup_tsum (fun z : ι × ι => Φ z.1 * conj (Φ z.2)) (summable_pair Φ hΦ) (fun z => P z.1 - P z.2) q hq

include hΦ in
/-- **First identity (summable kick):** `(1/q) ∑_{ν mod q} |Z_m(ν/q)|² = ∑_{j∈ℤ} C_Z(jq)`. -/
theorem aliasing_CZS {q : ℕ} (hq : 0 < q) :
    (1 / (q : ℂ)) * ∑ ν ∈ range q, Zq Φ P ((ν : ℝ) / q) * conj (Zq Φ P ((ν : ℝ) / q))
      = ∑' j : ℤ, CZS Φ P (j * q) := by
  rw [aliasing_mean Φ hΦ P hq, pairs_eq_tsum_CZS Φ hΦ P (q : ℤ) (by exact_mod_cast hq.ne')]

include hΦ in
/-- **Möbius formula in `C_Z` form (summable kick):** `F_m = φ(M)⁻¹ ∑_{e ∣ M} μ(e) (M/e) ∑_j C_Z(j M/e)`. -/
theorem FmS_CZS (M : ℕ) (hM : 0 < M) :
    FmS Φ P M = ((Nat.totient M : ℂ))⁻¹ * ∑ e ∈ M.divisors, ((ArithmeticFunction.moebius e : ℤ) : ℂ) *
      (((M / e : ℕ) : ℂ) * ∑' j : ℤ, CZS Φ P (j * ((M / e : ℕ) : ℤ))) := by
  rw [FmS_moebius Φ hΦ P M hM]
  congr 1
  refine sum_congr rfl (fun e he => ?_)
  have hpos : 0 < M / e := Nat.div_pos (Nat.divisor_le he) (Nat.pos_of_mem_divisors he)
  rw [pairs_eq_tsum_CZS Φ hΦ P _ (by exact_mod_cast hpos.ne')]

end Bgs.LineIRegroupSummable
