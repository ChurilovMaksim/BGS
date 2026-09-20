import Lean.Elab.Tactic.Omega

/-!
Integer, cleared-denominator kernels used in the CUE/loop calculations.
These do not formalize trace expectations, real/complex analysis, or BGS.
Compilation status is recorded separately; source text is not a certificate.
-/

namespace Bgs.CueLoopKernels

/-- The positive-part expression in the cubic CUE reference. -/
def cubicReference (n a b : Int) : Int :=
  n - max (n-a) 0 - max (n-b) 0 + max (n-a-b) 0

theorem cubic_below_dimension (n a b : Int)
    (ha : 0 ≤ a) (hb : 0 ≤ b) (hab : a+b ≤ n) :
    cubicReference n a b = 0 := by
  unfold cubicReference
  omega

theorem cubic_positive_part (n a b : Int)
    (hn : 0 ≤ n) (ha : 0 ≤ a) (hb : 0 ≤ b) :
    cubicReference n a b = max 0 (min n (min a (min b (a+b-n)))) := by
  unfold cubicReference
  omega

/-- Here e₂ represents four times the real mixed quadratic defect,
    t represents s⁻² and z represents L/s² after clearing denominators. -/
theorem eliminate_cubic (l c q t z e₂ e₃ : Int)
    (h₂ : e₂ = 4*l + 4*c - t)
    (h₃ : e₃ = 16*l + 32*c + 16*q - 4*t - 8*z) :
    16*q = 16*l + 8*z - 4*t + e₃ - 8*e₂ := by
  omega

end Bgs.CueLoopKernels
