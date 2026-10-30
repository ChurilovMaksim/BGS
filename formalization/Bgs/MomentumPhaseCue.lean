set_option maxHeartbeats 0

namespace Bgs.MomentumPhaseCue

/-!
# Rational witness for BGS-TRACE-140, BGS-TRACE-141 and BGS-TRACE-142

The odd-symbol energy `9/125000`, the time-three error constant
`(3!)²(1+2·3·2) = 468`, the time-two constant `20`, and the residues
`27 mod 5, 7, 11, 13`. These are the residues at `t = 3` only.
The conditions `t = 1` and `t = 2` are not formalized, and `p = 13`
is not excluded from the form-factor statement. The form factor is not formalized.
-/

/-- Cross-multiplication of `(16/25)·(9/80000) = 9/125000`. -/
theorem oddEnergy : (16 : Int) * 9 * 125000 = 25 * 80000 * 9 := by decide

/-- `(3!)² · (1 + 2·3·2) = 36 · 13`. -/
theorem timeThreeConstant : (6 : Nat) * 6 * 13 = 468 := by decide

/-- Time-two constant `(2!)² · (1 + 2·2·1) = 20`. -/
theorem timeTwoConstant : (2 : Nat) * 2 * 5 = 20 := by decide

theorem exclude5 : (27 : Nat) % 5 = 2 := by decide
theorem exclude7 : (27 : Nat) % 7 = 6 := by decide
theorem exclude11 : (27 : Nat) % 11 = 5 := by decide

/-- Residue `27 ≡ 1 (mod 13)`, the `t = 3` check at this prime. -/
theorem hit13 : (27 : Nat) % 13 = 1 := by decide

#print axioms oddEnergy
#print axioms timeThreeConstant
#print axioms timeTwoConstant
#print axioms exclude5
#print axioms exclude7
#print axioms exclude11
#print axioms hit13
end Bgs.MomentumPhaseCue
