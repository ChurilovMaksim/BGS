/-
# BGS-TRACE-157(a), reality version: the Gamma-diagonal sum is real

This is the redesign of 157(a) from `staging/phase4/lineD_157sigma_plan.md`
§5. It REPLACES the sigma-pairing route for (a) — it does not repair it:

* The sigma package in `CoeffBridge.diag_sum_phihatFix_eq_zero` is
  correct as a conditional implication, but UNINSTANTIABLE for the
  true factors: `hsign` and `hfixed` are FALSE, not merely unproved
  (the diagonal term is Gamma-invariant and equals
  `|φ̂|² · E[β] ≠ 0`; see the plan §3–§4). No involution of the
  "coordinate permutation ± swap" shape can work, so none is sought
  here.
* What the source (Proposition D6(a) of
  `mathematics/fixed-map/band_limited_kick_bridge.md`) actually proves
  is REALITY: the diagonal term equals `|φ̂(ξ)|² · E[β(ξ)] ∈ ℝ`, and
  `c₁` takes `(2/π)·Im` of the whole sum, so the diagonal part is
  invisible in `c₁` — without the diagonal sum itself being zero.

What is proved here, and what is NOT:

* Weight reality, no hypotheses: `(z * star z).im = 0` for any `z : ℂ`
  (`mul_star_self_im`), hence on the Gamma-diagonal the weight
  factor `φhatFix(ξ) · star φhatFix(ξ')` is real, via
  `CoeffBridge.weight_diag` (which identifies it with `φ · star φ`).
* Diagonal reality, ONE analytic hypothesis: if `(w p * beta p).im = 0`
  on the Gamma-diagonal (`hdiagReal`), then the diagonal sum is real
  (`diag_sum_phihatFix_im_eq_zero`), and hence the concrete `c₁`
  equals `(2/π)·Im` of the off-diagonal sum
  (`c1SumPhi_eq_offDiag_of_real`). This is exactly the conclusion
  (a) needs: the diagonal part contributes nothing to `c₁`.
* `hdiagReal` is NOT discharged here. It decomposes into exactly the
  ingredients D6(a) proves in the source — (i) `w = 1` on the diagonal
  (`G^{⊗m}` coordinate-permutation invariance, `|G| = 1` for both
  ensembles) and (ii) `E[β(ξ)]` real (`E[v''] = 0`, `v'ᵀH⁻¹v'` real) —
  and all of them belong to the analytic layer (the same layer as
  `hformula`), for which the Lean tree currently has no language:
  no `G^{⊗m}`, no ensembles, no `V_θ`, `v'`, `v''`, no analytic `H⁻¹`.
  Discharging `hdiagReal` is the remaining analytic step for (a),
  shared with the `hformula` layer, not a combinatorial gap.
* NOT touched: the sigma theorems in `CoeffBridge` (kept as abstract
  lemmas), the (e)-transfers (`hformula`, `hcollapseNeg`), and the
  exact value of the diagonal sum as a complex number (in general
  nonzero — it is only its imaginary part that vanishes).

No placeholder proofs; the only hypotheses are the explicitly named
`hdiagReal` (and the ambient `[NeZero m]` instance argument).
-/

import Bgs.LineDCoeffBridge

namespace Bgs
namespace LineD
namespace CoeffReality

open Bgs.LineD

/-! ### Step 1: a modulus weight is real, with no hypotheses -/

/-- For any complex `z`, the product `z * star z` is real: it is
`‖z‖²` cast to `ℂ`. No hypotheses at all. -/
theorem mul_star_self_im (z : ℂ) : (z * star z).im = 0 := by
  have h : z * star z = ((Complex.normSq z : ℝ) : ℂ) := by
    rw [Complex.star_def]
    exact Complex.mul_conj z
  rw [h]
  simp

/-! ### Step 2: a diagonal term is real under `hdiagReal` -/

/-- The concrete term, regrouped as weight × (`w` × `beta`). -/
theorem c1TermPhi_eq_weight_mul (m : ℕ) [NeZero m] (s : ℤ)
    (w beta : OrbitPair.Fix m × OrbitPair.Fix m → ℂ)
    (p : OrbitPair.Fix m × OrbitPair.Fix m) :
    CoeffBridge.c1TermPhi m s w beta p
      = (OrbitPairFull.phihatFix m s p.1
          * star (OrbitPairFull.phihatFix m s p.2)) * (w p * beta p) := by
  rw [CoeffBridge.c1TermPhi_apply]
  ring

/-- A diagonal term is real under the single analytic hypothesis
`hdiagReal`: on the diagonal the weight is `φ · star φ` (real by
step 1), and `w · beta` is real by hypothesis, so their product
is real. -/
theorem diag_term_im_eq_zero (m : ℕ) [NeZero m] (s : ℤ)
    (w beta : OrbitPair.Fix m × OrbitPair.Fix m → ℂ)
    (t : Finset (OrbitPair.Fix m × OrbitPair.Fix m))
    (hdiagReal : ∀ p ∈ t.filter (CoeffBridge.diagPair m),
      (w p * beta p).im = 0)
    (p : OrbitPair.Fix m × OrbitPair.Fix m)
    (hp : p ∈ t.filter (CoeffBridge.diagPair m)) :
    (CoeffBridge.c1TermPhi m s w beta p).im = 0 := by
  have hdiag : CoeffBridge.diagPair m p := (Finset.mem_filter.mp hp).2
  rw [c1TermPhi_eq_weight_mul,
    CoeffBridge.weight_diag m s p.1 p.2 hdiag,
    Complex.mul_im, mul_star_self_im, hdiagReal p hp]
  simp

/-! ### Step 3: imaginary part of a sum is the sum of imaginary parts -/

/-- Additivity of `Complex.im` over a finite sum, via `map_sum`
for the additive monoid homomorphism `Complex.im`. -/
theorem sum_im {ι : Type*} (s : Finset ι) (f : ι → ℂ) :
    (∑ i ∈ s, f i).im = ∑ i ∈ s, (f i).im :=
  map_sum (⟨⟨Complex.im, Complex.zero_im⟩, Complex.add_im⟩ : ℂ →+ ℝ) f s

/-! ### Step 4: the diagonal sum is real, and `c₁` sees only the off-diagonal part -/

/-- (a), reality form: under `hdiagReal`, the imaginary part of the
Gamma-diagonal sum vanishes. Note the conclusion is about `.im`,
not about the sum itself — the diagonal sum as a complex number is
in general nonzero. -/
theorem diag_sum_phihatFix_im_eq_zero (m : ℕ) [NeZero m] (s : ℤ)
    (w beta : OrbitPair.Fix m × OrbitPair.Fix m → ℂ)
    (t : Finset (OrbitPair.Fix m × OrbitPair.Fix m))
    (hdiagReal : ∀ p ∈ t.filter (CoeffBridge.diagPair m),
      (w p * beta p).im = 0) :
    (∑ p ∈ t.filter (CoeffBridge.diagPair m),
      CoeffBridge.c1TermPhi m s w beta p).im = 0 := by
  rw [sum_im]
  apply Finset.sum_eq_zero
  intro p hp
  exact diag_term_im_eq_zero m s w beta t hdiagReal p hp

/-- The concrete `c₁` in terms of the diagonal sum, unfolded once
so that `Coeff.sum_split` applies to the `c1TermPhi` sum. -/
theorem c1SumPhi_eq (m : ℕ) [NeZero m] (s : ℤ)
    (w beta : OrbitPair.Fix m × OrbitPair.Fix m → ℂ)
    (t : Finset (OrbitPair.Fix m × OrbitPair.Fix m)) :
    CoeffBridge.c1SumPhi m s w beta t
      = (2 / Real.pi)
        * (∑ p ∈ t, CoeffBridge.c1TermPhi m s w beta p).im := rfl

/-- (a), full form: under the single analytic hypothesis `hdiagReal`,
the concrete `c₁` equals `(2/π)·Im` of the off-diagonal sum. The
diagonal part contributes nothing to `c₁`, exactly as the boundary
of 157(a) requires — via reality, not via a pairing involution. -/
theorem c1SumPhi_eq_offDiag_of_real (m : ℕ) [NeZero m] (s : ℤ)
    (w beta : OrbitPair.Fix m × OrbitPair.Fix m → ℂ)
    (t : Finset (OrbitPair.Fix m × OrbitPair.Fix m))
    (hdiagReal : ∀ p ∈ t.filter (CoeffBridge.diagPair m),
      (w p * beta p).im = 0) :
    CoeffBridge.c1SumPhi m s w beta t
      = (2 / Real.pi)
        * (∑ p ∈ t.filter (fun p => ¬ CoeffBridge.diagPair m p),
            CoeffBridge.c1TermPhi m s w beta p).im := by
  rw [c1SumPhi_eq,
    Coeff.sum_split t (CoeffBridge.diagPair m)
      (CoeffBridge.c1TermPhi m s w beta),
    Complex.add_im, diag_sum_phihatFix_im_eq_zero m s w beta t hdiagReal,
    zero_add]

/- Axiom audit for all main theorems of this module. -/
#print axioms Bgs.LineD.CoeffReality.mul_star_self_im
#print axioms Bgs.LineD.CoeffReality.c1TermPhi_eq_weight_mul
#print axioms Bgs.LineD.CoeffReality.diag_term_im_eq_zero
#print axioms Bgs.LineD.CoeffReality.sum_im
#print axioms Bgs.LineD.CoeffReality.diag_sum_phihatFix_im_eq_zero
#print axioms Bgs.LineD.CoeffReality.c1SumPhi_eq
#print axioms Bgs.LineD.CoeffReality.c1SumPhi_eq_offDiag_of_real

end CoeffReality
end LineD
end Bgs
