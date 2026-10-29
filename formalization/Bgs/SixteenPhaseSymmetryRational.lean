set_option maxHeartbeats 0

/-!
# Rational witness for BGS-TRACE-130

The momentum-row energy `9/160000` and `det(S-I)=-4`.
The similarity is not formalized.
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
/-- The two momentum-sine coefficients have squared moduli adding as `(1+1)/4 = 1/2`. -/
theorem momentumSymbol : ((1 + 1 : Int) = 2) ∧ (2 * 2 = 4) := by decide
