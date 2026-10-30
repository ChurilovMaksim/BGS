set_option maxRecDepth 1000000
set_option maxHeartbeats 0
set_option exponentiation.threshold 4096

namespace Bgs.OrderTrichotomyRational

/-!
# Rational witness for BGS-TRACE-121

This file certifies the integer comparisons that place every odd prime,
and every odd prime power, on a definite side of the Abel thresholds.
It does not formalize the splitting law, the kernel count, or the kick
telescoping.  Those steps are in
`mathematics/fixed-map/order_trichotomy_abel.md`.
-/

/-- The degree-4 partial sum of `e^{16/17}` exceeds `1687/667`. -/
theorem order_trichotomy_sixteen : 213457 * 667 > 83521 * 1687 := by
  decide

/-- `667/1020 + 1/34 = 41/60`. -/
theorem order_trichotomy_half_assembly :
    (667 * 34 + 1020) * 60 = 41 * 1020 * 34 := by
  decide

theorem order_trichotomy_seven : 19796077 * 4 > 25256270 * 3 := by
  decide

theorem order_trichotomy_seven_tower : 7238798455 * 4 > 8237425794 * 3 := by
  decide

theorem order_trichotomy_split_tower : 427139065 * 7 < 600824064 * 5 := by
  decide

theorem order_trichotomy_long_tower : 3287 * 7 < 4840 * 5 := by
  decide

theorem order_trichotomy_long_kick : 72173 * 7 < 101640 * 5 := by
  decide

theorem order_trichotomy_three : (59 * 420 + 13 * 144) * 7 < 5 * 144 * 420 := by
  decide

theorem order_trichotomy_five : (349 * 420 + 13 * 1200) * 7 < 5 * 1200 * 420 := by
  decide

/-- `19796077/25256270 - 13/420 > 3/4`. -/
theorem order_trichotomy_seven_kick :
    (19796077 * 420 - 13 * 25256270) * 4 > 3 * 25256270 * 420 := by
  decide

/-- `7238798455/8237425794 - 13/420 > 3/4`. -/
theorem order_trichotomy_seven_tower_kick :
    (7238798455 * 420 - 13 * 8237425794) * 4 > 3 * 8237425794 * 420 := by
  decide

theorem order_trichotomy_square_gap : 5 * 25 - 12 * 5 - 12 = 53 := by
  decide

theorem order_trichotomy_window :
    184981 * (10 : Nat) ^ 100 * 4205768448
      < 14146865 * 2 * ((10 : Nat) ^ 25 - 2)
          * (160000 * (10 : Nat) ^ 80 - 184981 * (10 : Nat) ^ 25) := by
  decide
#print axioms order_trichotomy_sixteen
#print axioms order_trichotomy_half_assembly
#print axioms order_trichotomy_seven
#print axioms order_trichotomy_seven_tower
#print axioms order_trichotomy_split_tower
#print axioms order_trichotomy_long_tower
#print axioms order_trichotomy_long_kick
#print axioms order_trichotomy_three
#print axioms order_trichotomy_five
#print axioms order_trichotomy_seven_kick
#print axioms order_trichotomy_seven_tower_kick
#print axioms order_trichotomy_square_gap
#print axioms order_trichotomy_window
end Bgs.OrderTrichotomyRational
