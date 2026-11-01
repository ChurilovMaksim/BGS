import Bgs.LineIMoebius
import Bgs.LineISummable

/-!
# BGS-TRACE-218 — the Möbius formula for absolutely summable kicks

Source: registry statement of `BGS-TRACE-218`.  Notation of `Bgs.LineISummable` (kick `Φ̂` on an arbitrary index type
with `∑|Φ̂(n)| < ∞`, `Z(θ) = ∑'_n Φ̂(n) e(−θP(n))`) and `Bgs.LineIMoebius` (`M = 2h`).

* `FmS_moebius` : `F_m = φ(M)⁻¹ ∑_{ν unit mod M} |Z(ν/M)|²
   = φ(M)⁻¹ ∑_{e ∣ M} μ(e) (M/e) ∑'_{(n,n′)} Φ̂(n) conj Φ̂(n′) 1[(M/e) ∣ P(n) − P(n′)]` for every `M ≥ 1`.

**Partial coverage:** the regrouping of the absolutely convergent pair series into `∑_j C_Z(j·M/e)` is **not**
formalized here (it is formalized for finite support in `Bgs.LineIRegroup`); the heuristic assessment is not part of the
claim.  All proofs are kernel-checked.
-/

namespace Bgs.LineIMoebiusSummable

open Finset ComplexConjugate Bgs.LineIMoebius Bgs.LineISummable
open scoped ArithmeticFunction.Moebius

variable {ι : Type*} (Φ : ι → ℂ) (hΦ : Summable (fun n => ‖Φ n‖)) (P : ι → ℤ)

/-- `F_m = φ(M)⁻¹ ∑_{ν unit mod M} |Z(ν/M)|²` for a summable kick. -/
noncomputable def FmS (M : ℕ) : ℂ :=
  ((Nat.totient M : ℂ))⁻¹ * ∑ ν ∈ (range M).filter (fun ν => Nat.Coprime ν M),
    Zq Φ P ((ν : ℝ) / M) * conj (Zq Φ P ((ν : ℝ) / M))

include hΦ in
theorem FmS_moebius (M : ℕ) (hM : 0 < M) :
    FmS Φ P M = ((Nat.totient M : ℂ))⁻¹ * ∑ e ∈ M.divisors, ((μ e : ℤ) : ℂ) * (((M / e : ℕ) : ℂ) *
      ∑' z : ι × ι, Φ z.1 * conj (Φ z.2) * (if ((M / e : ℕ) : ℤ) ∣ (P z.1 - P z.2) then 1 else 0)) := by
  unfold FmS
  congr 1
  rw [sum_units_moebius M hM (fun ν => Zq Φ P ((ν : ℝ) / M) * conj (Zq Φ P ((ν : ℝ) / M)))]
  refine sum_congr rfl (fun e he => ?_)
  congr 1
  have heM : e ∣ M := Nat.dvd_of_mem_divisors he
  have he0 : 0 < e := Nat.pos_of_mem_divisors he
  have hq : 0 < M / e := Nat.div_pos (Nat.le_of_dvd hM heM) he0
  have hal := aliasing_mean Φ hΦ P hq
  have hq' : ((M / e : ℕ) : ℂ) ≠ 0 := by exact_mod_cast hq.ne'
  have hpt : ∀ ν' : ℕ, (((e * ν' : ℕ) : ℝ) / M) = ((ν' : ℝ) / ((M / e : ℕ) : ℝ)) := by
    intro ν'
    rw [Nat.cast_div heM (by exact_mod_cast he0.ne')]
    have : (e : ℝ) ≠ 0 := by exact_mod_cast he0.ne'
    have : (M : ℝ) ≠ 0 := by exact_mod_cast hM.ne'
    push_cast; field_simp
  simp only [hpt]
  rw [← hal]
  field_simp

end Bgs.LineIMoebiusSummable
