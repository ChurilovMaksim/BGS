import Std

/- Compiled with Lean 4.33.1 on 11 October 2026. Finite arithmetic kernel only; no analytic, representation-theoretic, rank-classification or BGS formalization. -/

namespace Bgs.ActiveRankDefect
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

#print axioms activeDefectCost
#print axioms rankFourGivesSecondOrder
end Bgs.ActiveRankDefect
