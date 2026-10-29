set_option maxRecDepth 1000000
set_option maxHeartbeats 0

namespace Bgs.OrbitOrthogonalRational

/-!
# Rational witness for BGS-TRACE-118

This file certifies the integer comparisons used in the quadrature spike at
`N = u_203`.  It does not formalize Weyl operators, the matrix exponential,
or the trace.  Those steps are in
`mathematics/fixed-map/orbit_orthogonal_kick_spike.md` and are rechecked by
the Python and C++ verifiers.
-/

def iter : Nat → Int × Int
  | 0 => (1, 0)
  | n + 1 =>
    let (u, v) := iter n
    (u + 2 * v, u + v)

def u200 : Int := (iter 200).1
def v200 : Int := (iter 200).2
def u202 : Int := (iter 202).1
def v202 : Int := (iter 202).2
def u203 : Int := (iter 203).1
def v203 : Int := (iter 203).2
def u204 : Int := (iter 204).1
def v204 : Int := (iter 204).2
def u205 : Int := (iter 205).1
def u206 : Int := (iter 206).1
def v206 : Int := (iter 206).2
def u207 : Int := (iter 207).1
def u209 : Int := (iter 209).1

theorem orbit_norm : u203 * u203 - 2 * v203 * v203 = -1 := by
  decide

theorem orbit_odd : u203 % 2 = 1 := by
  decide

theorem orbit_bases : (iter 5).1 = 41 ∧ (iter 7).1 = 239 ∧ (iter 9).1 = 1393 := by
  decide

/-- For `t ≤ 100`, both components of `C^{±t} w + v` are strictly smaller than `u_203`. -/
theorem orbit_size_100 :
    10 * u200 + 9 < u203 ∧ u200 + 18 * v200 + 1 < u203 := by
  decide

/-- For `t = 101`, `|a| ≤ 4` and `|b| ≤ 5`. -/
theorem orbit_size_101 :
    9 * u202 + v202 + 9 < 5 * u203 ∧ u202 + 18 * v202 + 1 < 6 * u203 := by
  decide

theorem orbit_dominates_linear_form : u203 > 326 ∧ u203 > 154 := by
  decide

def ten : Int := 10
def bNum : Int := 184981
def bDen : Int := 160000
def sigN : Int := 1650797

def den2 : Int := 8 * ten ^ 166
def num2 : Int := 203 * sigN * u203 * u203
def den3 : Int := 6 * ten ^ 240 * bDen * bDen * bDen
def num3 : Int := 203 * 203 * 203 * u203 * u203 * u203 * bNum * bNum * bNum
def scale : Int := 3 * (2 : Int) ^ 96 * (5 : Int) ^ 86

theorem orbit_scale : scale * den2 = den3 := by
  decide

def numE : Int := num2 * scale + num3

/-- Cleared form of `(1 - 406/u_203) (1 - ε_2 - ε_3)^2 > 3/4`. -/
theorem orbit_gap :
    den3 > numE ∧
    4 * (u203 - 406) * (den3 - numE) ^ 2 > 3 * u203 * den3 ^ 2 := by
  decide

/-- Coarser majorants still lie under the budget used by the small comparison. -/
theorem orbit_coarse :
    203 * sigN * u203 * u203 * 1000 < 8 * ten ^ 166 ∧
    203 ^ 3 * u203 ^ 3 * bNum ^ 3 * 25 < 6 * ten ^ 240 * bDen ^ 3 ∧
    u203 > 406 * 1000 ∧
    4 * 999 * 959 ^ 2 > 3 * 1000 ^ 3 := by
  decide

/-- At `n = 205` the third-order remainder majorant is already at least 1. -/
theorem orbit_sentinel :
    205 ^ 3 * u205 ^ 3 * bNum ^ 3 ≥ 6 * ten ^ 240 * bDen ^ 3 := by
  decide

/-- Half-period size bounds used to classify overlaps at `n = 205` and `n = 207`. -/
theorem orbit_size_next :
    u205 > u203 ∧ u207 > u205 ∧ u209 > u207 ∧
    9 * u202 + v202 + 9 < u205 ∧
    u202 + 18 * v202 + 1 < u205 ∧
    9 * u204 + v204 + 9 < 5 * u205 ∧
    u204 + 18 * v204 + 1 < 6 * u205 ∧
    9 * u202 + v202 + 9 < u207 ∧
    u202 + 18 * v202 + 1 < u207 ∧
    9 * u204 + v204 + 9 < u207 ∧
    u204 + 18 * v204 + 1 < u207 ∧
    9 * u206 + v206 + 9 < 5 * u207 ∧
    u206 + 18 * v206 + 1 < 6 * u207 ∧
    u205 > 154 ∧ u207 > 154 := by
  decide

/-- The Hilbert--Schmidt triangle deficit exceeds 1 at `n = 205`. -/
theorem orbit_hs_triangle :
    205 * 205 * 66033 * u205 * u205 > 2 * ten ^ 160 * 160000 := by
  decide

def diskDen : Int := 2 * ten ^ 160 * 4000000
def num205 : Int := 205 * 1650797 * u205 * u205
def num207 : Int := 207 * 1650797 * u207 * u207

/-- At `n = 205` the pure second-order center still clears `3/4`. -/
theorem orbit_disk_room :
    num205 < diskDen ∧
    4 * (u205 - 410) * (diskDen - num205) ^ 2 > 3 * u205 * diskDen ^ 2 := by
  decide

/-- At `n = 207` the pure second-order center lies strictly below `3/4`. -/
theorem orbit_disk_ceiling :
    num207 < diskDen ∧
    4 * (diskDen - num207) ^ 2 < 3 * diskDen ^ 2 := by
  decide
end Bgs.OrbitOrthogonalRational
