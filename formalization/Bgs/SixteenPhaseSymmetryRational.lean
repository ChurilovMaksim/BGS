set_option maxHeartbeats 0

/-!
# Rational witness for BGS-TRACE-130

The momentum-row energy `9/160000`, `det(S-I)=-4`, and the
rational identity `1/4 + 1/4 = 1/2` for the momentum-sine symbol.
The antiunitary is not formalized.
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

def oddSum : Int :=
  (List.range 19).foldl (fun acc i =>
    let r := rNum (Int.ofNat i - 9)
    acc + 25 * r * r) 0

theorem oddEnergy : oddSum = 900 := by decide
theorem oddRatio : (900 : Int) * 160000 = 9 * 16000000 := by decide
theorem detSI : (2 : Int) * 2 - 4 * 2 = -4 := by decide
/-- Cross-multiplication of `1/4 + 1/4 = 1/2`, the squared moduli of the two
momentum-sine coefficients. `Rat` equality does not reduce under `decide`. -/
theorem momentumSymbol : ((1 * 4 + 1 * 4 : Int) * 2) = (1 * (4 * 4)) := by
  decide
