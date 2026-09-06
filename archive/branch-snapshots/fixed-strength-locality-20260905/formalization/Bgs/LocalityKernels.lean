import Std

/-!
Algebraic kernels only. No semiclassical limit, operator norm estimate,
Gevrey theorem, or BGS assertion is formalized by this module.
-/
namespace Bgs.LocalityKernels

/-- On a support box the second image coordinate stays near a half-integer.
Coordinates are cleared by the common positive denominator 16*L. -/
theorem image_band (L u v : Int)
    (hu0 : -L <= u) (hu1 : u <= L)
    (hv0 : -L <= v) (hv1 : v <= L) :
    3*L <= 8*L+2*u+3*v ∧ 8*L+2*u+3*v <= 13*L := by
  constructor <;> omega

theorem excludes_support_strip (L u v : Int) (hL : 0 < L)
    (hu0 : -L <= u) (hu1 : u <= L)
    (hv0 : -L <= v) (hv1 : v <= L) :
    L < 8*L+2*u+3*v ∧ 8*L+2*u+3*v < 15*L := by
  constructor <;> omega

/-- The rational lower bound for the real inverse on the Cauchy disk. -/
theorem cauchy_disk_constant : (3 : Nat)*3008 > 6561 := by decide

/-- A factor N^2 loses precisely two powers in an all-orders remainder. -/
theorem exponent_budget (R p : Nat) :
    (R+p+3) - 2 > R+p := by omega

/-- Internal and external cyclic gap counts retain the full dimension. -/
theorem gap_partition (K n : Nat) (hn : 1 <= n) :
    K*(n-1)+K = K*n := by
  have h : n - 1 + 1 = n := by omega
  calc
    K*(n-1)+K = K*((n-1)+1) := by simp [Nat.mul_add]
    _ = K*n := by rw [h]

#print axioms image_band
#print axioms excludes_support_strip
#print axioms cauchy_disk_constant
#print axioms exponent_budget
#print axioms gap_partition

end Bgs.LocalityKernels
