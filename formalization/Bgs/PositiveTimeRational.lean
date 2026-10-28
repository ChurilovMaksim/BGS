set_option maxRecDepth 1000000
set_option maxHeartbeats 0
set_option exponentiation.threshold 4096

/-!
# Rational witness for BGS-TRACE-119

This file certifies the integer comparisons used in the positive-time
expansion at `N = u_205`.  It does not formalize Weyl operators, diagram
partitions, or the trace.  Those steps are in
`mathematics/fixed-map/positive_time_spike.md` and are rechecked by the
Python and C++ verifiers.
-/

def iter : Nat → Int × Int
  | 0 => (1, 0)
  | n + 1 =>
    let (u, v) := iter n
    (u + 2 * v, u + v)

def u205 : Int := (iter 205).1
def v205 : Int := (iter 205).2
def u372 : Int := (iter 372).1
def v372 : Int := (iter 372).2
def u10 : Int := (iter 10).1
def v10 : Int := (iter 10).2

def ten : Int := 10
def bNum : Int := 184981
def bDen : Int := 160000

def fact : Nat → Nat
  | 0 => 1
  | n + 1 => (n + 1) * fact n

theorem positive_time_norm_205 : u205 * u205 - 2 * v205 * v205 = -1 := by
  decide

theorem positive_time_bases : u10 = 3363 ∧ v10 = 2378 := by
  decide

/-- `(18·11)² α^372 < 2 u_205²`, the norm block at diameter 186. -/
theorem positive_time_norm_block :
    let c : Int := 198 * 198
    let left : Int := 2 * u205 * u205
    c * u372 < left ∧
      (left - c * u372) ^ 2 > 2 * (c * v372) ^ 2 := by
  decide

/-- `4860 β^5 < 1`, with `β^5 = u_10 - v_10 √2`. -/
theorem positive_time_gap :
    let c : Int := 4860
    2 * (c * v10) ^ 2 > (c * u10 - 1) ^ 2 := by
  decide

theorem positive_time_scale :
    410 * u205 * bNum < 7 * bDen * ten ^ 80 := by
  decide

theorem positive_time_tail :
    100 * (7 : Int) ^ 12 * 26 < fact 12 * (2 : Int) ^ 12 * 19 := by
  decide

def window (m : Nat) : Nat :=
  4 * (m - 1) + 1

/-- Degree-`m` pinned activity, numerator over the common degree-11 denominator. -/
def activityTerm (m : Nat) : Int :=
  let w : Int := window m
  let comb : Int := w ^ m - (w - 1) ^ m
  205 * comb * (u205 * bNum) ^ m
    * ((fact 11 : Int) / (fact m : Int))
    * ten ^ (80 * (11 - m))
    * bDen ^ (11 - m)

def activityNum : Int :=
  activityTerm 3 + activityTerm 4 + activityTerm 5 + activityTerm 6
    + activityTerm 7 + activityTerm 8 + activityTerm 9 + activityTerm 10
    + activityTerm 11

def activityDen : Int :=
  (fact 11 : Int) * ten ^ 880 * bDen ^ 11

theorem positive_time_phi3 : 23 * activityNum < activityDen := by
  decide

theorem positive_time_phi2 :
    61500 * (u205 * bNum) ^ 2 < 18 * ten ^ 160 * bDen ^ 2 := by
  decide

theorem positive_time_coarse :
    (9 : Int) * 23 + 100 < 7 * 46 ∧
      12 * 2097 < 32890 := by
  decide

def denEps : Int := 8 * ten ^ 166
def numEps : Int := 205 * 1650797 * u205 * u205

/-- Cleared form of `(1 - 410/u_205) (1 - ε_2 - 1/12)² > 3/4`. -/
theorem positive_time_abel :
    11 * denEps > 12 * numEps ∧
      4 * (u205 - 410) * (11 * denEps - 12 * numEps) ^ 2
        > 3 * u205 * (12 * denEps) ^ 2 := by
  decide
