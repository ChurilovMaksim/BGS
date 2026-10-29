set_option maxRecDepth 1000000
set_option maxHeartbeats 0

/-!
# Rational witness for BGS-TRACE-126

The coefficient function below is `fCoeff` from `TraceStatement.lean`, scaled by
4000. This file certifies the resulting integer table: 32 nonzero modes,
Hermitian symmetry, Hilbert--Schmidt energy 66033/160000, parity energy
663/4000000, the strict majorant 184981/160000, and the unreduced reversal
sum 66031/80000.

It does not formalize the trace closure, the phase average, or the folding
of those sums modulo N. Those arguments are in
`mathematics/fixed-map/interaction_phase_form_factor.md`.
-/

def rNum : Int → Int
  | 0 => 4
  | 1 => 2
  | -1 => 2
  | 7 => -2
  | -7 => -2
  | 6 => -1
  | -6 => -1
  | 8 => -1
  | -8 => -1
  | _ => 0

/-- Scaled coefficient `4000 * fCoeff(k, ℓ) = (re, im)`. -/
def coeff (k l : Int) : Int × Int :=
  if l = 0 then
    let re := (if k = 7 ∨ k = -7 then (2000 : Int) else 0) + 100 * rNum k
      - (if k = 0 then 400 else 0)
    let im := -5 * (rNum (k - 1) - rNum (k + 1))
    (re, im)
  else if l = 1 then
    (-3 * rNum k, -4 * rNum k)
  else if l = -1 then
    (-3 * rNum k, 4 * rNum k)
  else
    (0, 0)

def box : List (Int × Int) :=
  ((List.range 19).map fun i => (Int.ofNat i) - 9).flatMap fun k =>
    ((List.range 3).map fun j => (Int.ofNat j) - 1).map fun l => (k, l)

def sumSq : Int :=
  box.foldl (fun s p =>
    let c := coeff p.1 p.2
    s + c.1 * c.1 + c.2 * c.2) 0

def modeCount : Nat :=
  box.foldl (fun s p =>
    let c := coeff p.1 p.2
    s + if c.1 = 0 ∧ c.2 = 0 then 0 else 1) 0

def imagSq : Int :=
  box.foldl (fun s p =>
    let c := coeff p.1 p.2
    s + c.2 * c.2) 0

def hermitianOk : Bool :=
  box.all fun p =>
    let c := coeff p.1 p.2
    let d := coeff (-p.1) (-p.2)
    d.1 = c.1 ∧ d.2 = -c.2

/-- Numerator data for `(floor(sqrt(p q))+1)/q`, with `s` supplied and checked. -/
def majorantWitnesses : List (Int × Int × Nat) := [
  (-9, 0, 800), (-8, -1, 800), (-8, 0, 4019), (-8, 1, 800),
  (-7, -1, 400), (-7, 0, 180), (-7, 1, 400),
  (-6, -1, 800), (-6, 0, 4019), (-6, 1, 800), (-5, 0, 800),
  (-2, 0, 400), (-1, -1, 400), (-1, 0, 2009), (-1, 1, 400),
  (0, -1, 200), (0, 1, 200),
  (1, -1, 400), (1, 0, 2009), (1, 1, 400), (2, 0, 400), (5, 0, 800),
  (6, -1, 800), (6, 0, 4019), (6, 1, 800),
  (7, -1, 400), (7, 0, 180), (7, 1, 400),
  (8, -1, 800), (8, 0, 4019), (8, 1, 800), (9, 0, 800)
]

def witnessOk (k l : Int) (s : Nat) : Bool :=
  let c := coeff k l
  let n := (c.1 * c.1 + c.2 * c.2).natAbs
  let d : Nat := 16000000
  let g := Nat.gcd n d
  let p := n / g
  let q := d / g
  decide (s * s ≤ p * q) && decide (p * q < (s + 1) * (s + 1)) &&
    !decide (c.1 = 0 ∧ c.2 = 0)

def witnessesOk : Bool :=
  majorantWitnesses.all fun w => witnessOk w.1 w.2.1 w.2.2

def oneMajorant (k l : Int) (s : Nat) : Int × Int :=
  let c := coeff k l
  let n := (c.1 * c.1 + c.2 * c.2).natAbs
  let d : Nat := 16000000
  let g := Nat.gcd n d
  let q := d / g
  (Int.ofNat (s + 1), Int.ofNat q)

def addQ (a b : Int × Int) : Int × Int :=
  let n := a.1 * b.2 + b.1 * a.2
  let d := a.2 * b.2
  let g := Int.ofNat (Nat.gcd n.natAbs d.natAbs)
  (n / g, d / g)

def majorantSum : Int × Int :=
  majorantWitnesses.foldl (fun s w =>
    addQ s (oneMajorant w.1 w.2.1 w.2.2)) (0, 1)

def witnessCount : Nat :=
  majorantWitnesses.length

def revAt (a b : Int) : Int :=
  let cs := coeff a (-b)
  let ct := coeff (3 * a + 4 * b) (2 * a + 3 * b)
  let dr := cs.1 - ct.1
  let di := -cs.2 - ct.2
  dr * dr + di * di

def revSum : Int :=
  (List.range 81).foldl (fun s i =>
    (List.range 81).foldl (fun s j =>
      s + revAt ((Int.ofNat i) - 40) ((Int.ofNat j) - 40)) s) 0

theorem phase_mode_count : modeCount = 32 := by
  decide

theorem phase_hermitian : hermitianOk = true := by
  decide

theorem phase_energy_scaled : sumSq = 6603300 := by
  decide

theorem phase_energy :
    sumSq * 160000 = 66033 * 16000000 := by
  decide

theorem phase_imag_scaled : imagSq = 2652 := by
  decide

theorem phase_imag_energy :
    imagSq * 4000000 = 663 * 16000000 := by
  decide

theorem phase_parity_fraction :
    imagSq * 550275 = 221 * sumSq := by
  decide

theorem phase_witness_count : witnessCount = 32 := by
  decide

theorem phase_witnesses : witnessesOk = true := by
  decide

theorem phase_majorant : majorantSum = (184981, 160000) := by
  decide

theorem phase_majorant_beats_energy :
    66033 * 160000 * 160000 < 184981 * 184981 * 160000 := by
  decide

theorem phase_reversal_scaled : revSum = 13206200 := by
  decide

theorem phase_reversal :
    revSum * 80000 = 66031 * 16000000 := by
  decide

theorem phase_revival_41 :
    5 * 66033 * 1681 * 32000 = 111001473 * 160000 := by
  decide
