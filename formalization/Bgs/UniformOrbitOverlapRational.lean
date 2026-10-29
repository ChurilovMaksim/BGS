set_option maxRecDepth 1000000
set_option maxHeartbeats 0
set_option exponentiation.threshold 4096

/-!
# Rational witness for BGS-TRACE-125

This file certifies the integer seeds, the 32-mode mass, the lag-1
coefficient, the exponent-1 box count, and the exhaustive support scan at
`N = 41`. It does not formalize the Pell induction, the archimedean
embedding, or the quadratic-form descent. Those steps are in
`mathematics/fixed-map/uniform_orbit_overlap.md`.
-/

def iter : Nat → Int × Int
  | 0 => (1, 0)
  | n + 1 =>
    let (u, v) := iter n
    (u + 2 * v, u + v)

theorem overlap_seeds :
    (iter 2) = (3, 2) ∧ (iter 4) = (17, 12) ∧ (iter 5) = (41, 29) ∧
      (iter 7) = (239, 169) := by
  decide

theorem overlap_norm :
    (iter 4).1 * (iter 4).1 - 2 * (iter 4).2 * (iter 4).2 = 1 ∧
      (iter 7).1 * (iter 7).1 - 2 * (iter 7).2 * (iter 7).2 = -1 := by
  decide

theorem overlap_archimedean : (104 : Int) * 104 * 2 - 128 * 128 = 5248 := by
  decide

theorem overlap_coefficient : (66033 : Int) * 25 - 28 = 1650797 ∧ 160000 * 25 = 4000000 := by
  decide

theorem overlap_quadratic_seed :
    (49 : Int) * 17 * 17 - 144 * 17 - 243 = 11470 ∧ 98 * 17 - 95 = 1571 := by
  decide

theorem overlap_positivity :
    7 * ((7 : Int) * 17 * 17 - 10 * 17 + 19) = (7 * 17 - 5) * (7 * 17 - 5) + 108 := by
  decide

theorem overlap_rhs : 2 * (2 * (4 : Int) * 9 + 5) = 154 ∧ 163 < 239 ∧ 154 < 239 := by
  decide

theorem overlap_expansion :
    ((81 : Int) - 2 * 16 = 49) ∧ ((-2 : Int) * 72 = -144) ∧
      ((-81 : Int) - 2 * 81 = -243) ∧ ((49 : Int) * 2 - 98 = 0) ∧
      ((49 : Int) - 144 + 95 = 0) := by
  decide

def rNum (k : Int) : Int :=
  if k = 0 then 4
  else if k.natAbs = 1 then 2
  else if k.natAbs = 7 then -2
  else if k.natAbs = 6 then -1
  else if k.natAbs = 8 then -1
  else 0

def fRe (k l : Int) : Int :=
  if l = 0 then
    (if k.natAbs = 7 then 2000 else 0) + rNum k * 100 - (if k = 0 then 400 else 0)
  else if l = 1 ∨ l = -1 then -3 * rNum k
  else 0

def fIm (k l : Int) : Int :=
  if l = 0 then 5 * (rNum (k + 1) - rNum (k - 1))
  else if l = 1 then -4 * rNum k
  else if l = -1 then 4 * rNum k
  else 0

def ks : List Int := [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def ls : List Int := [-1, 0, 1]

def modeCount : Nat :=
  ks.foldl (fun acc k =>
    ls.foldl (fun acc l =>
      if fRe k l != 0 || fIm k l != 0 then acc + 1 else acc) acc) 0

def hermitianOk : Bool :=
  ks.all fun k =>
    ls.all fun l =>
      fRe (-k) (-l) == fRe k l && fIm (-k) (-l) == -fIm k l

def sigmaNum : Int :=
  ks.foldl (fun acc k =>
    ls.foldl (fun acc l =>
      if fRe k l != 0 || fIm k l != 0 then
        acc + fRe k l * fRe k l + fIm k l * fIm k l
      else acc) acc) 0

theorem overlap_modes : modeCount = 32 ∧ hermitianOk = true := by
  decide

theorem overlap_sigma : sigmaNum * 160000 = (66033 : Int) * 4000 * 4000 := by
  decide

def inBox (x y : Int) : Bool :=
  decide (x.natAbs ≤ 9) && decide (y.natAbs ≤ 1)

def boxCount (forward : Bool) : Nat :=
  ks.foldl (fun acc k =>
    ls.foldl (fun acc l =>
      let x := if forward then 3 * k + 2 * l else 3 * k - 2 * l
      let y := if forward then 4 * k + 3 * l else -4 * k + 3 * l
      if inBox x y then acc + 1 else acc) acc) 0

def forwardHits : Bool :=
  inBox (3 * 0 + 2 * 0) (4 * 0 + 3 * 0) &&
    inBox (3 * 1 + 2 * (-1)) (4 * 1 + 3 * (-1)) &&
    inBox (3 * (-1) + 2 * 1) (4 * (-1) + 3 * 1) &&
    boxCount true == 3

def inverseHits : Bool :=
  inBox (3 * 0 - 2 * 0) (-4 * 0 + 3 * 0) &&
    inBox (3 * 1 - 2 * 1) (-4 * 1 + 3 * 1) &&
    inBox (3 * (-1) - 2 * (-1)) (-4 * (-1) + 3 * (-1)) &&
    boxCount false == 3

theorem overlap_box : forwardHits = true ∧ inverseHits = true := by
  decide

def support : List (Int × Int) :=
  ks.foldl (fun acc k =>
    ls.foldl (fun acc l =>
      if fRe k l != 0 || fIm k l != 0 then acc ++ [(k, l)] else acc) acc) []

def mod41 (x : Int) : Int :=
  let r := x % 41
  if r < 0 then r + 41 else r

def powC : Nat → Int × Int × Int × Int
  | 0 => (1, 0, 0, 1)
  | r + 1 =>
    let (a, b, c, d) := powC r
    (3 * a + 2 * c, 3 * b + 2 * d, 4 * a + 3 * c, 4 * b + 3 * d)

def lagData (r : Nat) : Int × Int × Nat :=
  let (a, b, c, d) := powC r
  support.foldl (fun acc z =>
    let x := mod41 (-(a * z.1 + b * z.2))
    let y := mod41 (-(c * z.1 + d * z.2))
    support.foldl (fun acc w =>
      if mod41 w.1 == x && mod41 w.2 == y then
        let re := fRe w.1 w.2 * fRe z.1 z.2 - fIm w.1 w.2 * fIm z.1 z.2
        let im := fRe w.1 w.2 * fIm z.1 z.2 + fIm w.1 w.2 * fRe z.1 z.2
        (acc.1 + re, acc.2.1 + im, acc.2.2 + 1)
      else acc) acc) (0, 0, 0)

def middleScan : Bool :=
  let d1 := lagData 1
  let d2 := lagData 2
  let d3 := lagData 3
  let d4 := lagData 4
  d1.1 == -56 && d1.2.1 == 0 && d1.2.2 == 2 &&
    d2.1 == 0 && d2.2.1 == 0 && d2.2.2 == 0 &&
    d3.1 == 0 && d3.2.1 == 0 && d3.2.2 == 0 &&
    d4.1 == -56 && d4.2.1 == 0 && d4.2.2 == 2

theorem overlap_scan : middleScan = true := by
  decide

theorem overlap_mass :
    (sigmaNum + 2 * (-56)) * 4000000 = (1650797 : Int) * 4000 * 4000 := by
  decide
