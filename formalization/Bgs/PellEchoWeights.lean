import Lean.Elab.Tactic.Omega

/-!
Cleared-denominator algebraic kernels for the Pell Floquet/echo construction.
These statements do not formalize an analytic limit or microscopic BGS.
Their formal status requires a successful build, not source inspection alone.
-/

namespace Bgs.PellEchoWeights

def numerator (K j : Int) : Int := K - 1 - 2 * j

theorem adjacent_difference (K j : Int) :
    numerator K j - numerator K (j - 1) = -2 := by
  unfold numerator
  omega

theorem cyclic_jump (K : Int) :
    numerator K 0 - numerator K (K - 1) = 2 * (K - 1) := by
  unfold numerator
  omega

/-- The coefficient difference away from the cyclic seam. -/
theorem echo_nonwrapped (K j s : Int) :
    numerator K j + 2 * s - numerator K (j - s) = 0 := by
  unfold numerator
  omega

/-- Crossing the cyclic seam contributes precisely one complete denominator. -/
theorem echo_wrapped (K j s : Int) :
    numerator K j + 2 * s - numerator K (j - s + K) = 2 * K := by
  unfold numerator
  omega

/-- The small weight on one side of the half-period. -/
theorem half_period_left (ell r : Int) :
    numerator (2 * ell + 1) (ell - r) = 2 * r := by
  unfold numerator
  omega

/-- The small weight on the other side of the half-period. -/
theorem half_period_right (ell r : Int) :
    numerator (2 * ell + 1) (ell + 1 + r) = -2 * (r + 1) := by
  unfold numerator
  omega

end Bgs.PellEchoWeights
