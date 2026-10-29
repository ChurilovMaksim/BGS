set_option maxRecDepth 1000000
set_option maxHeartbeats 0
set_option exponentiation.threshold 4096

namespace Bgs.CrtCompositeRational

/-!
# Rational witness for BGS-TRACE-122

This file certifies the integer comparisons used to place every product of
two odd primes on a definite side of the Abel thresholds, together with the
positivity integers for the seven-family majorant. It does not formalize the
Chinese-remainder count, the order trichotomy, or the kick telescoping.
Those steps are in `mathematics/fixed-map/crt_composite_abel.md`.
-/

theorem crt_larger_short : 4 * 6 * 30 < 5 * 5 * 29 := by
  decide

theorem crt_both_large : 4 * 30 * 32 < 5 * 29 * 31 := by
  decide

theorem crt_seventeen : 48 * 18 ≤ 85 * 17 := by
  decide

theorem crt_three_even : 8 * 30 ≤ 15 * 29 := by
  decide

theorem crt_half_corner : 3 * 30 * 34 < 5 * 31 * 33 := by
  decide

theorem crt_inert_corner : 5 * 29 * 31 > 3 * 30 * 32 := by
  decide

theorem crt_three_primes : 12 * 84 > 5 * 195 := by
  decide

theorem crt_kick_threshold : (3 * 420 + 13 * 4) * 105 = 82 * 420 * 4 := by
  decide

theorem crt_twenty_one : 1485928284770040951 * 105 > 1861068320411356730 * 82 := by
  decide

theorem crt_three_short : 5704517734146 * 105 > 5603750430307 * 82 := by
  decide

theorem crt_twenty_one_plain : 1485928284770040951 * 4 > 1861068320411356730 * 3 := by
  decide

theorem crt_three_short_plain : 5704517734146 * 4 > 5603750430307 * 3 := by
  decide

theorem crt_seven_kick : (19796077 * 420 - 13 * 25256270) * 4 > 3 * 25256270 * 420 := by
  decide

theorem crt_quartic_gap : 61504580235 * 169 - 411438267366 = 9982835792349 := by
  decide

theorem crt_linear_gap : 13 * 9982835792349 - 429495755430 = 129347369545107 := by
  decide

theorem crt_quadratic_one : 110201 * 169 - 70323 = 18553646 := by
  decide

theorem crt_quadratic_two : 275135 * 169 - 45187 = 46452628 := by
  decide

theorem crt_factor_constant : (-70323) * (-45187) = 3177685401 := by
  decide

theorem crt_factor_linear :
    (-70323) * 237699 + 69629 * (-45187) = -19862032400 := by
  decide

theorem crt_factor_quadratic :
    (-70323) * 275135 + 69629 * 237699 + 110201 * (-45187) = -7777227521 := by
  decide

theorem crt_factor_cubic :
    69629 * 275135 + 110201 * 237699 = 45352042414 := by
  decide

theorem crt_factor_quartic : 110201 * 275135 = 30320152135 := by
  decide

theorem crt_n_at_13 :
    (((((200914962101 * 13 + 281046183404) * 13 - 3360079183489) * 13
      - 7015097338690) * 13 + 759755266431) * 13 + 3854354403900) * 13
      - 610115596992
    = 962927132597336369 := by
  decide

theorem crt_nprime_at_13 :
    ((((1205489772606 * 13 + 1405230917020) * 13 - 13440316733956) * 13
      - 21045292016070) * 13 + 1519510532862) * 13 + 3854354403900
    = 454663292137321722 := by
  decide

theorem crt_npprime_at_13 :
    (((6027448863030 * 13 + 5620923668080) * 13 - 40320950201868) * 13
      - 42090584032140) * 13 + 1519510532862
    = 177139237609770940 := by
  decide

theorem crt_derivative_leading : 6 * 200914962101 = 1205489772606 := by
  decide

theorem crt_second_leading : 98 * 61504580235 = 30 * 200914962101 := by
  decide

theorem crt_full_alpha : 36 * 38 * 899 > 840 * 37 * 39 := by
  decide

theorem crt_full_beta : 37 * 56 * 31 < 29 * 72 * 39 := by
  decide

theorem crt_full_gamma : 39 * 29 * 30 < 31 * 37 * 38 := by
  decide

theorem crt_full_unit : 29 * 31 < 37 * 39 := by
  decide

theorem crt_inert_numerator : 3 * 37 * 37 + 5 * 37 + 5 = 4297 := by
  decide

theorem crt_inert_denominator : 2 * 37 * 38 * 39 = 109668 := by
  decide

theorem crt_inert_extras :
    4297 * 1736 * 870 * 1798
      < 109668 * (29 * 870 * 1798 + 31 * 1736 * 1798 + 1736 * 870) := by
  decide

theorem crt_defect_endpoint :
    184981 * (10 : Nat) ^ 104 * 420
      < 26 * ((10 : Nat) ^ 26 - 2)
          * (160000 * (10 : Nat) ^ 80 - 184981 * (10 : Nat) ^ 26) := by
  decide
end Bgs.CrtCompositeRational
