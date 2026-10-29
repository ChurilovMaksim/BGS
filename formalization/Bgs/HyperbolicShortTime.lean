set_option maxHeartbeats 0

namespace Bgs.HyperbolicShortTime

/-!
# Arithmetic of integers written in BGS-TRACE-132

`3! * 7 = 42`, `4! * 13 = 312`, `13 + 9 = 22`, `22 * 18 = 11 * 36`,
and `121 * 11 > 6 * 18`. These comparisons do not formalize the
occupation estimate, the form factor, or `D_2`.
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

end Bgs.HyperbolicShortTime
