/-
# BGS-TRACE-157 bridge: Gamma-diagonal vanishing for concrete phihatFix weights

Claim `BGS-TRACE-157` (proved, boundary in `LineDCoeff`'s header):
`c₁ = (2/π) Im Σ φhat(ξ) conj φhat(ξ') E[G(ξ) conj G(ξ')] β(ξ)`.
(a) The pairs `ξ' ∈ Γξ` contribute zero (both ensembles).
(e) `c₁(−N mod g'ₘ) = −c₁(N mod g'ₘ)`, so `c₁` averages to 0 over
residues and cannot equal `−2m²` uniformly in `N`.

What is proved here, and what is NOT (no invented definitions):

* Weights (no hypotheses at all): the weight factor
  `φhatFix(ξ) · star φhatFix(ξ')` is invariant under simultaneous
  Γ-translation of the pair (`weight_gamma_inv`, from
  `StrongKickBridge.phihatFix_smul`); on the Γ-diagonal it equals the
  modulus at `ξ` (`weight_diag`), hence takes only the two values
  `|V4|/D` or `0` under `IsCoprime s D` (`weight_diag_values`, from
  `OrbitPairFull.phihatFix_modulus_values`).
* Sign-flip reduction: if the weight factor is σ-invariant and `w·beta`
  flips sign under σ, then the whole concrete term flips sign
  (`c1TermPhi_sign_flip_of`); weight-invariance is automatic when σ
  acts by simultaneous Γ-translation (`c1TermPhi_sign_flip_of_gamma`).
  So the weights do not obstruct the pairing involution: the sign
  flip lives entirely in the analytic factors `w`/`beta`.
* (a): under an explicit σ-package for the concrete terms (σ preserves
  the Γ-diagonal set, is an involution, flips the sign of the concrete
  term, and has no nonzero fixed points), the Γ-diagonal sum vanishes
  (`diag_sum_phihatFix_eq_zero`, via `Coeff.diag_sum_eq_zero`), and
  hence the concrete `c₁` equals `(2/π)·Im` of the off-diagonal sum
  (`c1Sum_phihatFix_eq_offDiag`, via `Coeff.c1Sum_eq_offDiag`).
  The EXISTENCE of such a σ is NOT proved here: it is the analytic
  input (the pairing of Γ-pairs), stated as an explicit hypothesis.
* (e): NOT proved for the concrete sum. What is proved is the
  conditional transfer: IF the N-family of concrete sums equals the
  derivative coefficient (the analytic identification `hformula`,
  the content of 157 itself together with 150 — NOT derived here),
  and Psi is periodic/even/differentiable with collapse-negation
  (`hcollapseNeg`, also NOT proved here), THEN the concrete sums are
  odd in the residue, average to 0, and cannot equal `−2m²` uniformly
  (`c1SumPhi_odd_of_formula`, `c1SumPhi_avg_zero_of_formula`,
  `c1SumPhi_not_uniform_of_formula`, via `Coeff`'s `*_of_formula`).

No sorry, no axiom, no native_decide, no decide.
-/

import Bgs.LineDStrongKickBridge
import Bgs.LineDCoeff

namespace Bgs
namespace LineD
namespace CoeffBridge

open Bgs.LineD

/-- The Γ-diagonal predicate on pairs: `ξ'` lies in the Γ-orbit of `ξ`. -/
noncomputable def diagPair (m : ℕ) [NeZero m]
    (p : OrbitPair.Fix m × OrbitPair.Fix m) : Prop :=
  p.2 ∈ Parity.orbitFinset (DihedralGroup m) p.1

/-- Decidability of the Γ-diagonal predicate (via `Finset` membership).
Typeclass search does not unfold `diagPair`, so this is given explicitly. -/
noncomputable instance decPred_diagPair (m : ℕ) [NeZero m] :
    DecidablePred (diagPair m) := fun p => by
  show Decidable (p.2 ∈ Parity.orbitFinset (DihedralGroup m) p.1)
  infer_instance

/-- The concrete `c₁`-term with `phihatFix` weights:
`φhatFix(ξ) · star φhatFix(ξ') · w · beta` on the pair `(ξ, ξ')`. -/
noncomputable def c1TermPhi (m : ℕ) [NeZero m] (s : ℤ)
    (w beta : OrbitPair.Fix m × OrbitPair.Fix m → ℂ)
    (p : OrbitPair.Fix m × OrbitPair.Fix m) : ℂ :=
  Bgs.LineD.Coeff.c1Term (fun q => OrbitPairFull.phihatFix m s q.1)
    (fun q => OrbitPairFull.phihatFix m s q.2) w beta p

/-- The concrete `c₁`-sum with `phihatFix` weights. -/
noncomputable def c1SumPhi (m : ℕ) [NeZero m] (s : ℤ)
    (w beta : OrbitPair.Fix m × OrbitPair.Fix m → ℂ)
    (t : Finset (OrbitPair.Fix m × OrbitPair.Fix m)) : ℝ :=
  Bgs.LineD.Coeff.c1Sum (fun q => OrbitPairFull.phihatFix m s q.1)
    (fun q => OrbitPairFull.phihatFix m s q.2) w beta t

/-! ### Diagonal membership -/

/-- Membership in the Γ-diagonal, unfolded: `ξ' ∈ Γξ` iff some
`g` sends `ξ` to `ξ'`. -/
theorem diagPair_iff (m : ℕ) [NeZero m] (ξ ξ' : OrbitPair.Fix m) :
    diagPair m (ξ, ξ') ↔ ∃ g : DihedralGroup m, g • ξ = ξ' := by
  have h : diagPair m (ξ, ξ')
      ↔ ξ' ∈ Parity.orbitFinset (DihedralGroup m) ξ := Iff.rfl
  rw [h]
  simp only [Parity.orbitFinset, Finset.mem_filter, Finset.mem_univ, true_and]
  exact MulAction.mem_orbit_iff

/-! ### Weights: Γ-invariance and modulus values on the diagonal -/

/-- The weight factor is invariant under simultaneous Γ-translation
of the pair. No hypotheses: this is `phihatFix_smul` twice. -/
theorem weight_gamma_inv (m : ℕ) [NeZero m] (s : ℤ)
    (g : DihedralGroup m) (ξ ξ' : OrbitPair.Fix m) :
    OrbitPairFull.phihatFix m s (g • ξ)
        * star (OrbitPairFull.phihatFix m s (g • ξ'))
      = OrbitPairFull.phihatFix m s ξ
        * star (OrbitPairFull.phihatFix m s ξ') := by
  simp only [StrongKickBridge.phihatFix_smul]

/-- On the Γ-diagonal, the weight factor equals the modulus at `ξ`:
since `ξ' = g • ξ`, Γ-invariance identifies the two weights. -/
theorem weight_diag (m : ℕ) [NeZero m] (s : ℤ) (ξ ξ' : OrbitPair.Fix m)
    (h : diagPair m (ξ, ξ')) :
    OrbitPairFull.phihatFix m s ξ * star (OrbitPairFull.phihatFix m s ξ')
      = OrbitPairFull.phihatFix m s ξ
        * star (OrbitPairFull.phihatFix m s ξ) := by
  obtain ⟨g, hg⟩ := (diagPair_iff m ξ ξ').mp h
  rw [← hg, StrongKickBridge.phihatFix_smul]

/-- On the Γ-diagonal, the weight factor takes only the two modulus
values `|V4|/D` or `0` (under coprimality). -/
theorem weight_diag_values (m : ℕ) [NeZero m] (s : ℤ)
    (hs : IsCoprime s (Defs.Dm m)) (ξ ξ' : OrbitPair.Fix m)
    (h : diagPair m (ξ, ξ')) :
    OrbitPairFull.phihatFix m s ξ * star (OrbitPairFull.phihatFix m s ξ')
      = ((Fintype.card (OrbitPair.V4 m) : ℂ) / (Defs.Dm m : ℂ))
      ∨ OrbitPairFull.phihatFix m s ξ * star (OrbitPairFull.phihatFix m s ξ')
        = 0 := by
  rw [weight_diag m s ξ ξ' h]
  exact OrbitPairFull.phihatFix_modulus_values m s hs ξ

/-! ### Terms: unfolding and sign-flip reduction -/

/-- The concrete term, unfolded: weight × `w` × `beta`. -/
theorem c1TermPhi_apply (m : ℕ) [NeZero m] (s : ℤ)
    (w beta : OrbitPair.Fix m × OrbitPair.Fix m → ℂ)
    (p : OrbitPair.Fix m × OrbitPair.Fix m) :
    c1TermPhi m s w beta p
      = OrbitPairFull.phihatFix m s p.1
        * star (OrbitPairFull.phihatFix m s p.2) * w p * beta p := rfl

/-- If the weight factor is σ-invariant and `w·beta` flips sign under
σ, then the whole concrete term flips sign: the weights do not
obstruct the pairing involution. -/
theorem c1TermPhi_sign_flip_of (m : ℕ) [NeZero m] (s : ℤ)
    (w beta : OrbitPair.Fix m × OrbitPair.Fix m → ℂ)
    (σ : OrbitPair.Fix m × OrbitPair.Fix m → OrbitPair.Fix m × OrbitPair.Fix m)
    (p : OrbitPair.Fix m × OrbitPair.Fix m)
    (hweight : OrbitPairFull.phihatFix m s (σ p).1
        * star (OrbitPairFull.phihatFix m s (σ p).2)
      = OrbitPairFull.phihatFix m s p.1
        * star (OrbitPairFull.phihatFix m s p.2))
    (hwb : w (σ p) * beta (σ p) = -(w p * beta p)) :
    c1TermPhi m s w beta (σ p) = -c1TermPhi m s w beta p := by
  rw [c1TermPhi_apply, c1TermPhi_apply, hweight]
  calc OrbitPairFull.phihatFix m s p.1 * star (OrbitPairFull.phihatFix m s p.2)
          * w (σ p) * beta (σ p)
      = (OrbitPairFull.phihatFix m s p.1 * star (OrbitPairFull.phihatFix m s p.2))
          * (w (σ p) * beta (σ p)) := by ring
    _ = (OrbitPairFull.phihatFix m s p.1 * star (OrbitPairFull.phihatFix m s p.2))
          * (-(w p * beta p)) := by rw [hwb]
    _ = -(OrbitPairFull.phihatFix m s p.1 * star (OrbitPairFull.phihatFix m s p.2)
          * w p * beta p) := by ring

/-- Weight-invariance is automatic when σ acts by simultaneous
Γ-translation: then the sign flip of the term follows from the sign
flip of `w·beta` alone. -/
theorem c1TermPhi_sign_flip_of_gamma (m : ℕ) [NeZero m] (s : ℤ)
    (w beta : OrbitPair.Fix m × OrbitPair.Fix m → ℂ)
    (σ : OrbitPair.Fix m × OrbitPair.Fix m → OrbitPair.Fix m × OrbitPair.Fix m)
    (p : OrbitPair.Fix m × OrbitPair.Fix m)
    (hgamma : ∃ g : DihedralGroup m, σ p = (g • p.1, g • p.2))
    (hwb : w (σ p) * beta (σ p) = -(w p * beta p)) :
    c1TermPhi m s w beta (σ p) = -c1TermPhi m s w beta p := by
  apply c1TermPhi_sign_flip_of m s w beta σ p _ hwb
  obtain ⟨g, hg⟩ := hgamma
  rw [hg]
  exact weight_gamma_inv m s g p.1 p.2

/-! ### (a): diagonal vanishing for the concrete weights -/

/-- (a), diagonal part: under a σ-package for the concrete terms
(σ preserves the Γ-diagonal set, is an involution, flips the sign
of the concrete term, and has no nonzero fixed points), the
Γ-diagonal sum vanishes. The existence of such a σ is a hypothesis,
not proved here. -/
theorem diag_sum_phihatFix_eq_zero (m : ℕ) [NeZero m] (s : ℤ)
    (w beta : OrbitPair.Fix m × OrbitPair.Fix m → ℂ)
    (t : Finset (OrbitPair.Fix m × OrbitPair.Fix m))
    (σ : OrbitPair.Fix m × OrbitPair.Fix m → OrbitPair.Fix m × OrbitPair.Fix m)
    (hmem : ∀ p ∈ t.filter (diagPair m), σ p ∈ t.filter (diagPair m))
    (hsign : ∀ p ∈ t.filter (diagPair m),
      c1TermPhi m s w beta (σ p) = -c1TermPhi m s w beta p)
    (hfixed : ∀ p ∈ t.filter (diagPair m),
      c1TermPhi m s w beta p ≠ 0 → σ p ≠ p)
    (hinv : ∀ p ∈ t.filter (diagPair m), σ (σ p) = p) :
    ∑ p ∈ t.filter (diagPair m), c1TermPhi m s w beta p = 0 :=
  Bgs.LineD.Coeff.diag_sum_eq_zero t (diagPair m) (c1TermPhi m s w beta) σ
    hmem hsign hfixed hinv

/-- (a), full form: under the σ-package, the concrete `c₁` equals
`(2/π)·Im` of the off-diagonal sum. -/
theorem c1Sum_phihatFix_eq_offDiag (m : ℕ) [NeZero m] (s : ℤ)
    (w beta : OrbitPair.Fix m × OrbitPair.Fix m → ℂ)
    (t : Finset (OrbitPair.Fix m × OrbitPair.Fix m))
    (σ : OrbitPair.Fix m × OrbitPair.Fix m → OrbitPair.Fix m × OrbitPair.Fix m)
    (hmem : ∀ p ∈ t.filter (diagPair m), σ p ∈ t.filter (diagPair m))
    (hsign : ∀ p ∈ t.filter (diagPair m),
      c1TermPhi m s w beta (σ p) = -c1TermPhi m s w beta p)
    (hfixed : ∀ p ∈ t.filter (diagPair m),
      c1TermPhi m s w beta p ≠ 0 → σ p ≠ p)
    (hinv : ∀ p ∈ t.filter (diagPair m), σ (σ p) = p) :
    c1SumPhi m s w beta t
      = (2 / Real.pi)
        * (∑ p ∈ t.filter (fun p => ¬ diagPair m p),
            c1TermPhi m s w beta p).im := by
  apply Bgs.LineD.Coeff.c1Sum_eq_offDiag
  exact diag_sum_phihatFix_eq_zero m s w beta t σ hmem hsign hfixed hinv

/-! ### (e): conditional transfer to the concrete sums -/

/-- (e), conditional transfer, oddness: IF the N-family of concrete
sums equals the derivative coefficient (`hformula` — the analytic
identification, NOT proved here), and Psi is periodic/even/
differentiable with collapse-negation, THEN the concrete sums are
odd in the residue. -/
theorem c1SumPhi_odd_of_formula (m : ℕ) [NeZero m] (s : ℤ)
    (w beta : ℕ → OrbitPair.Fix m × OrbitPair.Fix m → ℂ)
    (Psi : ℝ → ℝ) (tStar : ℕ → ℝ) (D : ℝ) (g' : ℕ)
    (hper : Function.Periodic Psi 1) (heven : ∀ x, Psi (-x) = Psi x)
    (hdiff : Differentiable ℝ Psi)
    (hcollapseNeg : ∀ N₁ N₂ : ℕ, (N₁ + N₂) % g' = 0 →
      ∃ k : ℤ, tStar N₁ + tStar N₂ = (k : ℝ))
    (hformula : ∀ N : ℕ, c1SumPhi m s (w N) (beta N) Finset.univ
      = Bgs.LineD.Coeff.c1Of Psi tStar D N)
    {N₁ N₂ : ℕ} (h : (N₁ + N₂) % g' = 0) :
    c1SumPhi m s (w N₁) (beta N₁) Finset.univ
      = -c1SumPhi m s (w N₂) (beta N₂) Finset.univ :=
  Bgs.LineD.Coeff.c1Sum_odd_of_formula
    (fun N => c1SumPhi m s (w N) (beta N) Finset.univ)
    hper heven hdiff hcollapseNeg hformula h

/-- (e), conditional transfer, average zero over residues. -/
theorem c1SumPhi_avg_zero_of_formula (m : ℕ) [NeZero m] (s : ℤ)
    (w beta : ℕ → OrbitPair.Fix m × OrbitPair.Fix m → ℂ)
    (Psi : ℝ → ℝ) (tStar : ℕ → ℝ) (D : ℝ) (g' : ℕ) (hg' : 0 < g')
    (hper : Function.Periodic Psi 1) (heven : ∀ x, Psi (-x) = Psi x)
    (hdiff : Differentiable ℝ Psi)
    (hcollapseNeg : ∀ N₁ N₂ : ℕ, (N₁ + N₂) % g' = 0 →
      ∃ k : ℤ, tStar N₁ + tStar N₂ = (k : ℝ))
    (hformula : ∀ N : ℕ, c1SumPhi m s (w N) (beta N) Finset.univ
      = Bgs.LineD.Coeff.c1Of Psi tStar D N) :
    ∑ r ∈ Finset.range g', c1SumPhi m s (w r) (beta r) Finset.univ = 0 :=
  Bgs.LineD.Coeff.c1Sum_avg_zero_of_formula hg'
    (fun N => c1SumPhi m s (w N) (beta N) Finset.univ)
    hper heven hdiff hcollapseNeg hformula

/-- (e), conditional transfer, no uniform value `−2m²`. -/
theorem c1SumPhi_not_uniform_of_formula (m : ℕ) [NeZero m] (s : ℤ)
    (w beta : ℕ → OrbitPair.Fix m × OrbitPair.Fix m → ℂ)
    (Psi : ℝ → ℝ) (tStar : ℕ → ℝ) (D : ℝ) (g' : ℕ) (hg' : 1 ≤ g') (hm : 1 ≤ m)
    (hper : Function.Periodic Psi 1) (heven : ∀ x, Psi (-x) = Psi x)
    (hdiff : Differentiable ℝ Psi)
    (hcollapseNeg : ∀ N₁ N₂ : ℕ, (N₁ + N₂) % g' = 0 →
      ∃ k : ℤ, tStar N₁ + tStar N₂ = (k : ℝ))
    (hformula : ∀ N : ℕ, c1SumPhi m s (w N) (beta N) Finset.univ
      = Bgs.LineD.Coeff.c1Of Psi tStar D N) :
    ¬ ∀ r ∈ Finset.range g',
      c1SumPhi m s (w r) (beta r) Finset.univ = -2 * (m : ℝ) ^ 2 :=
  Bgs.LineD.Coeff.c1Sum_not_uniform_of_formula hg' hm
    (fun N => c1SumPhi m s (w N) (beta N) Finset.univ)
    hper heven hdiff hcollapseNeg hformula

/- Axiom audit for all main theorems of this module. -/
#print axioms Bgs.LineD.CoeffBridge.diagPair_iff
#print axioms Bgs.LineD.CoeffBridge.weight_gamma_inv
#print axioms Bgs.LineD.CoeffBridge.weight_diag
#print axioms Bgs.LineD.CoeffBridge.weight_diag_values
#print axioms Bgs.LineD.CoeffBridge.c1TermPhi_apply
#print axioms Bgs.LineD.CoeffBridge.c1TermPhi_sign_flip_of
#print axioms Bgs.LineD.CoeffBridge.c1TermPhi_sign_flip_of_gamma
#print axioms Bgs.LineD.CoeffBridge.diag_sum_phihatFix_eq_zero
#print axioms Bgs.LineD.CoeffBridge.c1Sum_phihatFix_eq_offDiag
#print axioms Bgs.LineD.CoeffBridge.c1SumPhi_odd_of_formula
#print axioms Bgs.LineD.CoeffBridge.c1SumPhi_avg_zero_of_formula
#print axioms Bgs.LineD.CoeffBridge.c1SumPhi_not_uniform_of_formula

end CoeffBridge
end LineD
end Bgs
