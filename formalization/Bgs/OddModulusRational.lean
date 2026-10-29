set_option maxRecDepth 1000000
set_option maxHeartbeats 0
set_option exponentiation.threshold 4096

/-!
# Rational witness for BGS-TRACE-124

This file certifies the closed integer comparisons used to place every odd
modulus above 3/4 or below 5/7, and to clear the fixed-kick margin inside
the stated windows. It does not formalize the kernel expansion, the
quadrant comparison, or the kick telescoping. Those steps are in
`mathematics/fixed-map/odd_modulus_abel.md`. The twenty-six inert rows
other than partner 13 are recomputed by the Python and C++ programs.
-/

theorem odd_thresholds : 5 * 4 < 7 * 3 := by
  decide

theorem odd_kick_threshold : (3 * 420 + 13 * 4) * 105 = 82 * 420 * 4 := by
  decide

theorem odd_u_fifteen : 499 * 7 < 806 * 5 := by
  decide

theorem odd_u_thirty_nine : 8705 * 7 < 14274 * 5 := by
  decide

theorem odd_u_sixty_five : 2283 * 7 < 3782 * 5 := by
  decide

theorem odd_u_eleven_thirteen : 1383 * 7 < 2318 * 5 := by
  decide

theorem odd_u_twenty_three_thirty_seven : 11512715 * 7 < 17117562 * 5 := by
  decide

theorem odd_corner_below : 108945 * 7 < 158158 * 5 := by
  decide

theorem odd_corner_gap_value : 5 * 158158 - 7 * 108945 = 49 * 575 ∧ 7 * 158158 = 49 * 22594 := by
  decide

theorem odd_corner_gap_defect : 575 * 420 < 22594 * 13 := by
  decide

theorem odd_tail_three :
    61 * 23 ^ 2 - 1097 * 23 - 56 = 6982 ∧
    2 * (61 * 23 - 518) = 1770 ∧
    (61 * 25 ^ 2 - 1097 * 25 - 56) + (61 * 23 ^ 2 - 1097 * 23 - 56) -
      2 * (61 * 24 ^ 2 - 1097 * 24 - 56) = 122 := by
  decide

theorem odd_tail_five :
    51 * 19 ^ 2 - 877 * 19 - 42 = 1706 ∧
    2 * (51 * 19 - 413) = 1112 ∧
    (51 * 21 ^ 2 - 877 * 21 - 42) + (51 * 19 ^ 2 - 877 * 19 - 42) -
      2 * (51 * 20 ^ 2 - 877 * 20 - 42) = 102 := by
  decide

theorem odd_tail_eleven :
    33 * 17 ^ 2 - 541 * 17 - 24 = 316 ∧
    2 * (33 * 17 - 254) = 614 ∧
    (33 * 19 ^ 2 - 541 * 19 - 24) + (33 * 17 ^ 2 - 541 * 17 - 24) -
      2 * (33 * 18 ^ 2 - 541 * 18 - 24) = 66 := by
  decide

theorem odd_tail_thirteen :
    961 * 17 ^ 2 - 15647 * 17 - 686 = 11044 ∧
    2 * (961 * 17 - 7343) = 17988 ∧
    (961 * 19 ^ 2 - 15647 * 19 - 686) + (961 * 17 ^ 2 - 15647 * 17 - 686) -
      2 * (961 * 18 ^ 2 - 15647 * 18 - 686) = 1922 := by
  decide

theorem odd_tail_nineteen :
    2029 * 23 ^ 2 - 32633 * 23 - 1400 = 321382 ∧
    2 * (2029 * 23 - 15302) = 62730 ∧
    (2029 * 25 ^ 2 - 32633 * 25 - 1400) + (2029 * 23 ^ 2 - 32633 * 23 - 1400) -
      2 * (2029 * 24 ^ 2 - 32633 * 24 - 1400) = 4058 := by
  decide

theorem odd_tail_twenty_three :
    533 * 50 ^ 2 - 26109 * 50 - 968 = 26082 ∧
    2 * (533 * 50 - 12788) = 27724 ∧
    (533 * 52 ^ 2 - 26109 * 52 - 968) + (533 * 50 ^ 2 - 26109 * 50 - 968) -
      2 * (533 * 51 ^ 2 - 26109 * 51 - 968) = 1066 := by
  decide

theorem odd_large_numerator : 11 * 31 ^ 3 - 311 * 31 ^ 2 - 701 * 31 - 7 = 7092 := by
  decide

theorem odd_large_first : 33 * 31 ^ 2 - 589 * 31 - 1001 = 12453 := by
  decide

theorem odd_large_second : 66 * 31 - 556 = 1490 ∧
    (33 * 32 ^ 2 - 589 * 32 - 1001) - (33 * 31 ^ 2 - 589 * 31 - 1001) = 1490 := by
  decide

theorem odd_drop_base : 5 * 5 ^ 3 - 12 * 5 ^ 2 - 24 * 5 - 12 = 193 := by
  decide

theorem odd_drop_step : 15 * 5 ^ 2 - 9 * 5 - 31 = 299 := by
  decide

theorem odd_raise_three : 21 * 5 - 24 = 81 := by
  decide

theorem odd_raise_partner : 15 * 5 ^ 2 - 48 * 5 - 48 = 87 := by
  decide

theorem odd_drop_195 : 12 * 84 < 5 * 195 * 3 ∧ 12 * 84 > 5 * 195 := by
  decide

theorem odd_radical_105 : 12 * 12 ≤ 5 * 105 ∧ 8 * 12 ≤ 3 * 105 ∧ 8 * 12 ≤ 3 * 315 := by
  decide

theorem odd_floor_room : 3 * 45 ^ 2 > 1 := by
  decide

theorem odd_return_threshold : (4 * 10 ^ 24 + 1) * 100 < 81 * 5 * 10 ^ 24 := by
  decide

theorem odd_fifteen_ratio : 4 * 10 ^ 24 < 5 * 10 ^ 24 ∧ 10 ^ 26 / 15 > 10 ^ 24 := by
  decide

theorem odd_series_domain : 81 < 5 * 100 := by
  decide

theorem odd_lower_21 : 265028515609711 * 105 > 309078510309860 * 82 := by
  decide

theorem odd_lower_195 : 50134551873841695 * 105 > 54792051773384968 * 82 := by
  decide

theorem odd_lower_inert_a2 : 26832108548323 * 105 > 33947639168772 * 82 := by
  decide

theorem odd_lower_three_short_a1 : 114226176533733 * 105 > 112075008606140 * 82 := by
  decide

theorem odd_lower_three_short_a2 : 2228970493853307 * 105 > 2479202684534320 * 82 := by
  decide

theorem odd_inert_thirteen :
    16323101582366123785899971 * 105 > 20875800430500088687646340 * 82 := by
  decide

theorem odd_inert_tail_pure : 13146189928817400 * 4 > 17402756940259603 * 3 := by
  decide

theorem odd_inert_tail_kick : 13146189928817400 * 105 < 17402756940259603 * 82 := by
  decide

theorem odd_defect_domain : 184981 * (2 * 10 ^ 26) < 160000 * 10 ^ 80 := by
  decide

theorem odd_defect_endpoint :
    184981 * (2 * 10 ^ 26) ^ 4 * 16733546028 <
      857840479 * 2 * (2 * 10 ^ 26 - 2) * (160000 * 10 ^ 80 - 184981 * (2 * 10 ^ 26)) := by
  decide

theorem odd_majorant_exceeds : 184981 * 10 ^ 154 > 320000 := by
  decide

theorem odd_majorant_defined : 184981 * 10 ^ 79 < 160000 * 10 ^ 80 := by
  decide
