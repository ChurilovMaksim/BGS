set_option maxRecDepth 1000000
set_option maxHeartbeats 0
set_option exponentiation.threshold 4096

/-!
# Rational witness for BGS-TRACE-123

This file certifies the integer comparisons used to place every square-free
odd modulus with at least three distinct prime factors above 3/4, and to
clear the fixed-kick margin inside the stated windows. It does not formalize
the divisibility of the orders, the least-common-multiple bound, or the kick
telescoping. Those steps are in
`mathematics/fixed-map/squarefree_product_abel.md`.
-/

theorem sqf_four : 4 * 6 * 8 * 12 ≤ 3 * 3 * 5 * 7 * 11 := by
  decide

theorem sqf_five : 4 * 6 * 8 * 12 * 14 ≤ 6 * 3 * 5 * 7 * 11 * 13 := by
  decide

theorem sqf_at_least_five : 2 * 6 * 8 * 12 ≤ 3 * 5 * 7 * 11 := by
  decide

theorem sqf_three_seven : 4 * 8 * 12 ≤ 5 * 7 * 11 := by
  decide

theorem sqf_fifteen_tail : 72 * 30 ≤ 75 * 29 := by
  decide

theorem sqf_fifteen_slope : 3 * 29 - 72 = 15 := by
  decide

theorem sqf_seven_tail : 48 * 12 ≤ 63 * 11 := by
  decide

theorem sqf_seven_slope : 15 * 11 - 48 = 117 := by
  decide

theorem sqf_eleven_tail : 8 * 12 * 38 ≤ 9 * 11 * 37 := by
  decide

theorem sqf_eleven_slope : 9 * 11 - 8 * 12 = 3 := by
  decide

theorem sqf_thirteen_tail : 8 * 14 * 24 ≤ 9 * 13 * 23 := by
  decide

theorem sqf_thirteen_slope : 9 * 13 - 8 * 14 = 5 := by
  decide

theorem sqf_seventeen_tail : 8 * 18 * 20 ≤ 9 * 17 * 19 := by
  decide

theorem sqf_seventeen_slope : 17 - 8 = 9 := by
  decide

theorem sqf_return_corner : 4 * 38 * 185 = 152 * 5 * 37 := by
  decide

theorem sqf_return_slope : 20 * 37 = 740 := by
  decide

theorem sqf_wide_domain : 152 < 5 * 185 := by
  decide

theorem sqf_narrow_domain : 88 < 5 * 115 := by
  decide

theorem sqf_subset_domain : 168 < 5 * 195 := by
  decide

theorem sqf_kick_threshold : (3 * 420 + 13 * 4) * 105 = 82 * 420 * 4 := by
  decide

theorem sqf_wide : 4894346125 * 105 > 6236939544 * 82 := by
  decide

theorem sqf_narrow : 740666125 * 105 > 851428424 * 82 := by
  decide

theorem sqf_one_nine_five :
    54421025909829591004375115797555753149956840906272969117235 * 105
      > 53966707446709005093212565207656544939196850800058844271758 * 82 := by
  decide

theorem sqf_pure_105 : 12 * 12 ≤ 5 * 105 := by
  decide

theorem sqf_pure_165 : 12 * 12 ≤ 5 * 165 := by
  decide

theorem sqf_pure_255 : 12 * 24 ≤ 5 * 255 := by
  decide

theorem sqf_pure_285 : 12 * 60 ≤ 5 * 285 := by
  decide

theorem sqf_pure_345 : 12 * 132 ≤ 5 * 345 := by
  decide

theorem sqf_pure_195 : 12 * 84 > 5 * 195 := by
  decide

theorem sqf_miss_345 : 8 * 132 > 3 * 345 := by
  decide

theorem sqf_miss_195 : 8 * 84 > 3 * 195 := by
  decide

theorem sqf_kick_105 : 8 * 12 ≤ 3 * 105 := by
  decide

theorem sqf_kick_165 : 8 * 12 ≤ 3 * 165 := by
  decide

theorem sqf_kick_255 : 8 * 24 ≤ 3 * 255 := by
  decide

theorem sqf_kick_285 : 8 * 60 ≤ 3 * 285 := by
  decide

theorem sqf_kick_435 : 8 * 60 ≤ 3 * 435 := by
  decide

theorem sqf_kick_465 : 8 * 60 ≤ 3 * 465 := by
  decide

theorem sqf_kick_429 : 8 * 84 ≤ 3 * 429 := by
  decide

theorem sqf_kick_561 : 8 * 24 ≤ 3 * 561 := by
  decide

theorem sqf_kick_627 : 8 * 60 ≤ 3 * 627 := by
  decide

theorem sqf_kick_759 : 8 * 132 ≤ 3 * 759 := by
  decide

theorem sqf_kick_957 : 8 * 60 ≤ 3 * 957 := by
  decide

theorem sqf_kick_1023 : 8 * 60 ≤ 3 * 1023 := by
  decide

theorem sqf_kick_663 : 8 * 56 ≤ 3 * 663 := by
  decide

theorem sqf_kick_741 : 8 * 140 ≤ 3 * 741 := by
  decide
