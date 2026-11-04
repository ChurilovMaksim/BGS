import Bgs.LineIHorocycle
import Bgs.LineIRegroupSummable

/-!
# BGS-TRACE-214 — Lemma I5′ for absolutely summable (infinite-support) kicks

Source: registry statement of `BGS-TRACE-214`.  This module removes the finite-support restriction of
`Bgs.LineIHorocycle`: the kick `Φ̂` is indexed by an arbitrary type `ι` (e.g. `ℤ^m`) with `∑ |Φ̂(n)| < ∞`,
`Z(θ) = ∑'_n Φ̂(n) e(−θP(n))` (`Bgs.LineISummable.Zq`), `Z_ν = Z(ν/M)`, `M = 2h`.  The weight is
`f(z_ν) = ∑_k c_k e(kν/M)` with `∑_k |c_k| < ∞` (`Bgs.LineIHorocycle.f`), `c_M` the Ramanujan sum
(`Bgs.LineIHorocycle.ram`), and `C(k) = ∑'_{(n,n′)} Φ̂(n) conj Φ̂(n′) 1[P(n) − P(n′) ≡ k mod M]` (absolutely convergent
pair series).

* `char_sumS` : `∑_{ν<M} |Z_ν|² e(kν/M) = M·C(k)`;
* `horocycle_allS` (a) : `∑_{ν mod M} |Z_ν|² f(z_ν) = M ∑_k c_k C(k)`;
* `horocycle_unitsS` (b) : `∑_{ν unit} |Z_ν|² f(z_ν) = ∑_k c_k ∑'_{(n,n′)} Φ̂(n) conj Φ̂(n′) c_M(k − P(n) + P(n′))`.

With `Bgs.LineIHorocycle` (finite support) this covers identities (a) and (b) for every kick with `∑|Φ̂| < ∞`.  The
remarks on the diagonal class and on the use for R′ are not identities of the claim and are not formalized.
All proofs are kernel-checked.
-/

namespace Bgs.LineIHorocycleSummable

open Finset ComplexConjugate Bgs.LineN4Gauge Bgs.LineISummable Bgs.LineIHorocycle

variable {ι : Type*} (Φ : ι → ℂ) (hΦ : Summable (fun n => ‖Φ n‖)) (P : ι → ℤ)

/-- `C(k) = ∑'_{(n,n′)} Φ̂(n) conj Φ̂(n′) 1[P(n) − P(n′) ≡ k mod M]`. -/
noncomputable def CS (M : ℕ) (k : ℤ) : ℂ :=
  ∑' z : ι × ι, Φ z.1 * conj (Φ z.2) * (if (M : ℤ) ∣ (P z.1 - P z.2 - k) then 1 else 0)

/-- Interchange of a finite `ν`-sum with the weight series, for any values `G ν`. -/
theorem interchangeG (N : Finset ℕ) (M : ℕ) (G : ℕ → ℂ) (c : ℤ → ℂ) (hc : Summable (fun k => ‖c k‖)) :
    ∑ ν ∈ N, G ν * f c M ν = ∑' k : ℤ, c k * ∑ ν ∈ N, G ν * e ((k : ℂ) * ν / M) := by
  unfold f
  simp_rw [← tsum_mul_left]
  rw [← Summable.tsum_finsetSum (fun ν _ => summable_weight c hc M ν _)]
  congr 1; funext k
  rw [Finset.mul_sum]
  refine sum_congr rfl (fun ν _ => ?_)
  ring

include hΦ in
theorem pair_charS (N : Finset ℕ) (M : ℕ) (k : ℤ) :
    ∑ ν ∈ N, Zq Φ P ((ν : ℝ) / M) * conj (Zq Φ P ((ν : ℝ) / M)) * e ((k : ℂ) * ν / M)
      = ∑' z : ι × ι, Φ z.1 * conj (Φ z.2) * ∑ ν ∈ N, e ((ν : ℂ) * ((k - P z.1 + P z.2 : ℤ) : ℂ) / M) := by
  simp_rw [Zq_mul_conj Φ hΦ P, ← tsum_mul_right]
  have hs : ∀ ν ∈ N, Summable (fun z : ι × ι =>
      Φ z.1 * conj (Φ z.2) * e (-(((ν : ℝ) / M : ℝ) : ℂ) * ((P z.1 - P z.2 : ℤ) : ℂ)) * e ((k : ℂ) * ν / M)) := by
    intro ν _
    refine Summable.of_norm_bounded (Bgs.LineIRegroupSummable.summable_pair Φ hΦ) (fun z => ?_)
    rw [norm_mul, norm_mul]
    have h1 : -(((ν : ℝ) / M : ℝ) : ℂ) * ((P z.1 - P z.2 : ℤ) : ℂ)
        = ((-((ν : ℝ) / M) * (P z.1 - P z.2 : ℤ) : ℝ) : ℂ) := by push_cast; ring
    rw [h1, norm_e_real, e_real_arg, norm_e_real]; simp
  rw [← Summable.tsum_finsetSum hs]
  congr 1; funext z
  rw [Finset.mul_sum]
  refine sum_congr rfl (fun ν _ => ?_)
  rw [mul_assoc, e_add]
  congr 2
  push_cast; ring

include hΦ in
theorem char_sumS {M : ℕ} (hM : 0 < M) (k : ℤ) :
    ∑ ν ∈ range M, Zq Φ P ((ν : ℝ) / M) * conj (Zq Φ P ((ν : ℝ) / M)) * e ((k : ℂ) * ν / M)
      = (M : ℂ) * CS Φ P M k := by
  rw [pair_charS Φ hΦ, CS, ← tsum_mul_left]
  congr 1; funext z
  have : ∀ ν : ℕ, e ((ν : ℂ) * ((k - P z.1 + P z.2 : ℤ) : ℂ) / M)
      = e (-(ν : ℂ) * ((P z.1 - P z.2 - k : ℤ) : ℂ) / M) := by
    intro ν; congr 1; push_cast; ring
  simp_rw [this]
  rw [Bgs.LineIAliasing.geom_root_sum hM]
  split_ifs <;> ring

include hΦ in
/-- **(a), summable kick:** `∑_{ν mod M} |Z_ν|² f(z_ν) = M ∑_k c_k C(k)`. -/
theorem horocycle_allS {M : ℕ} (hM : 0 < M) (c : ℤ → ℂ) (hc : Summable (fun k => ‖c k‖)) :
    ∑ ν ∈ range M, Zq Φ P ((ν : ℝ) / M) * conj (Zq Φ P ((ν : ℝ) / M)) * f c M ν
      = (M : ℂ) * ∑' k : ℤ, c k * CS Φ P M k := by
  rw [interchangeG _ M _ c hc, ← tsum_mul_left]
  congr 1; funext k
  rw [char_sumS Φ hΦ P hM]; ring

include hΦ in
/-- **(b), summable kick:** `∑_{ν unit} |Z_ν|² f(z_ν) = ∑_k c_k ∑'_{(n,n′)} Φ̂(n) conj Φ̂(n′) c_M(k − P(n) + P(n′))`. -/
theorem horocycle_unitsS (M : ℕ) (c : ℤ → ℂ) (hc : Summable (fun k => ‖c k‖)) :
    ∑ ν ∈ (range M).filter (fun ν => Nat.Coprime ν M),
        Zq Φ P ((ν : ℝ) / M) * conj (Zq Φ P ((ν : ℝ) / M)) * f c M ν
      = ∑' k : ℤ, c k * ∑' z : ι × ι, Φ z.1 * conj (Φ z.2) * ram M (k - P z.1 + P z.2) := by
  rw [interchangeG _ M _ c hc]
  congr 1; funext k
  rw [pair_charS Φ hΦ]
  rfl

end Bgs.LineIHorocycleSummable
