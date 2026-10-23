import Std

/-
Arithmetic fragment only. This file has NOT been compiled: neither Lean
nor Lake is installed in the current environment. It does not formalize
matrix rank, finite-field Gauss sums, the cycle classification, or BGS.
-/

theorem activeDefectCost
    (h g R r : Nat)
    (hg : g ≤ h)
    (rankLoss : R ≤ 2 * g + r) :
    2 * (h - g) + max (2 * g) R ≤ 2 * h + r := by
  omega

theorem rankFourGivesSecondOrder
    (h g R r : Nat)
    (hg : g ≤ h)
    (rankLoss : R ≤ 2 * g + r)
    (rankFour : 4 ≤ R) :
    4 ≤ 2 * h + r := by
  omega
