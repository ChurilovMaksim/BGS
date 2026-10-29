set_option maxHeartbeats 0

namespace Bgs.HyperbolicShortTime

/-!
# Integer witness for BGS-TRACE-132

The error constants of the dihedral bound and the comparison showing that
the order-two majorant at `x = 1` exceeds `2 * 3` when `N = 11`.
The occupation sum is not formalized.
-/

def fact : Nat → Nat
  | 0 => 1
  | n + 1 => (n + 1) * fact n

theorem symErr3 : fact 3 * (1 + 3 * 2) = 42 := by decide
theorem symErr4 : fact 4 * (1 + 4 * 3) = 312 := by decide

/-- `13/36 + 9/36 = 22/36 = 11/18`, the value of the remainder majorant at `x = 1`. -/
theorem remainderParts : (13 : Int) + 9 = 22 := by decide
theorem remainderAtUnit : (22 : Int) * 18 = 11 * 36 := by decide

/-- At `N = 11` and `x = 1` the remainder majorant `N^2 * 11/18` exceeds `6`. -/
theorem majorantExceedsTwoM : (121 : Int) * 11 > 6 * 18 := by decide

theorem dihedral3 : (2 : Int) * 3 = 6 := by decide

end Bgs.HyperbolicShortTime
