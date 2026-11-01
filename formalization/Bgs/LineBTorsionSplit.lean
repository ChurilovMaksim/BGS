import Mathlib.Data.ZMod.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Analysis.Complex.Basic

/-!
# BGS-TRACE-178 — exact torsion-class split `F = F_gen + F_tor` of the Prop C formula

Source: `mathematics/fixed-map/derandomized_fixed_kick.md` (BGS-TRACE-169, 178) and
`mathematics/fixed-map/derandomized_fixed_kick/phase4_parity_certificate.md` §2.3; registry boundary of `BGS-TRACE-178`.
Prop C (BGS-TRACE-169): `F_m = h⁻² ∑_{r,r′} A_r conj A_{r′} μ(q_{rr′})/φ(q_{rr′})` over the norm classes `r, r′ mod h`.
For a prime `p ∣ h` let `R_p = {r : r ≡ 0 mod p}`; `F_gen` sums the pairs with `r, r′ ∉ R_p` and `F_tor` the remaining pairs.

* `torsion_split` : `F = F_gen + F_tor`, for **any** pair weight `w(r, r′)` (in particular `μ(q_{rr′})/φ(q_{rr′})`) and any
  coefficients `A_r`.

**Partial coverage:** Prop C itself (BGS-TRACE-169) is not formalized here — the identity is stated for the Prop C
expression with an arbitrary weight, so it does not depend on it; the computed values (m = 9: p = 7, 199; m = 11:
p = 23, 353) and their reading are numerical and **not** formalized.  All proofs are kernel-checked.
-/

namespace Bgs.LineBTorsionSplit

open Finset ComplexConjugate

variable (h p : ℕ) [NeZero h] (A : ZMod h → ℂ) (w : ZMod h → ZMod h → ℂ)

/-- `r ∈ R_p` iff `r ≡ 0 (mod p)` (representative `r.val`; for `p ∣ h` this is well defined mod `h`). -/
def tor (r : ZMod h) : Prop := p ∣ r.val

instance (r : ZMod h) : Decidable (tor h p r) := by unfold tor; infer_instance

noncomputable def F : ℂ := ((h : ℂ) ^ 2)⁻¹ * ∑ r, ∑ r', A r * conj (A r') * w r r'

noncomputable def Fgen : ℂ :=
  ((h : ℂ) ^ 2)⁻¹ * ∑ r, ∑ r', if (¬ tor h p r ∧ ¬ tor h p r') then A r * conj (A r') * w r r' else 0

noncomputable def Ftor : ℂ :=
  ((h : ℂ) ^ 2)⁻¹ * ∑ r, ∑ r', if (¬ tor h p r ∧ ¬ tor h p r') then 0 else A r * conj (A r') * w r r'

theorem torsion_split : F h A w = Fgen h p A w + Ftor h p A w := by
  unfold F Fgen Ftor
  rw [← mul_add, ← sum_add_distrib]
  congr 1
  refine sum_congr rfl (fun r _ => ?_)
  rw [← sum_add_distrib]
  refine sum_congr rfl (fun r' _ => ?_)
  split_ifs <;> simp

end Bgs.LineBTorsionSplit
