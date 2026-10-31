/-! Lemma K3(a), exact range, by kernel `decide` (no native_decide): for 447 ≤ b' ≤ BMAX, b' ∉ {504,560,616,840},
every unit class r mod g' = gcd(56,b') has all cyclic gaps of V(b',r) = {v : gcd(v,b')=1, v ≡ r mod g'} at most b'/6
(i.e. 6*gap ≤ b'), and 1/6 < 18001/100000 ≤ A. -/
set_option maxRecDepth 1000000
set_option maxHeartbeats 0

/-- state: (first, prev, maxgap, seen) -/
def scan (bp g r : Nat) : Nat × Nat × Nat × Bool :=
  (List.range bp).foldl (fun (st : Nat × Nat × Nat × Bool) v =>
    let (f, pv, mg, seen) := st
    if v % g == r && Nat.gcd v bp == 1 then
      if seen then (f, v, max mg (v - pv), true) else (v, v, 0, true)
    else st) (0, 0, 0, false)

def maxGap (bp g r : Nat) : Nat :=
  let (f, pv, mg, seen) := scan bp g r
  if seen then max mg (f + bp - pv) else bp

def okB (bp : Nat) : Bool :=
  let g := Nat.gcd 56 bp
  (List.range g).all (fun r => Nat.gcd r g != 1 || 6 * maxGap bp g r ≤ bp)

def exc (bp : Nat) : Bool := bp == 504 || bp == 560 || bp == 616 || bp == 840

def okRange (lo n : Nat) : Bool := (List.range n).all (fun i => exc (lo+i) || okB (lo+i))

theorem sixth_lt_A : 100000 < 6 * 18001 := by decide
theorem gaps_2447 : okRange 2447 20 = true := by decide +kernel
#print axioms gaps_2447
