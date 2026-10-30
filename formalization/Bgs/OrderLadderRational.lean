set_option maxRecDepth 1000000
set_option maxHeartbeats 0
set_option exponentiation.threshold 4096

namespace Bgs.OrderLadderRational

/-!
# Rational witness for BGS-TRACE-120

This file certifies the integer comparisons used to place the cat-map
order on either side of the Abel threshold.  It does not formalize Weyl
operators, the trace-square identity, or the kick telescoping.  Those
steps are in `mathematics/fixed-map/order_ladder_abel.md`.
-/

theorem order_ladder_five_sixths : 361 * 3 < 156 * 7 := by
  decide

theorem order_ladder_exp_partial : 1957 * 7 > 720 * 19 := by
  decide

theorem order_ladder_exp_square : 109 > 15 * 7 := by
  decide

theorem order_ladder_half_gap : 7 * 7 < 12 * 5 := by
  decide

theorem order_ladder_three_quarter_gap : 5 * 4 < 7 * 3 := by
  decide

theorem order_ladder_distance_room : 41 * 7 < 5 * 60 := by
  decide

theorem order_ladder_return_margin : 156 * 4 > 205 * 3 := by
  decide

/-- `(19/20)² · 70600/83521 > 3/4`. -/
theorem order_ladder_four_returns : 361 * 70600 > 300 * 83521 := by
  decide

/-- One return at `N = 35` has weight below `3/4`, because `e^{12/35} > 4/3`. -/
theorem order_ladder_one_return_fails : 47 * 3 > 35 * 4 := by
  decide

/-- The pure return subsum at ratio `6/7` is below `3/4`. -/
theorem order_ladder_seven_return : 2401 * 4 < 3246 * 3 := by
  decide

theorem order_ladder_short_window :
    184981 * (10 : Nat) ^ 39 * (30 * (10 : Nat) ^ 39 + 1)
      < 160000 * (10 : Nat) ^ 80 := by
  decide

theorem order_ladder_long_window :
    184981 * (10 : Nat) ^ 104 * 420
      < 26 * ((10 : Nat) ^ 26 - 2) * (160000 * (10 : Nat) ^ 80 - 184981 * (10 : Nat) ^ 26) := by
  decide
#print axioms order_ladder_five_sixths
#print axioms order_ladder_exp_partial
#print axioms order_ladder_exp_square
#print axioms order_ladder_half_gap
#print axioms order_ladder_three_quarter_gap
#print axioms order_ladder_distance_room
#print axioms order_ladder_return_margin
#print axioms order_ladder_four_returns
#print axioms order_ladder_one_return_fails
#print axioms order_ladder_seven_return
#print axioms order_ladder_short_window
#print axioms order_ladder_long_window
end Bgs.OrderLadderRational
