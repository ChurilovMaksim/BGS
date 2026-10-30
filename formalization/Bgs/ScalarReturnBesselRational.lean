set_option maxRecDepth 1000000
set_option maxHeartbeats 0

namespace Bgs.ScalarReturnBesselRational

/-!
# Rational witness for BGS-TRACE-129

Integer matrix orders, the momentum-row energy `9/160000`, and the
additive quadruple counts of the position orbit. The Bessel average is
not summed here.
-/

def matStep (n a b c d : Nat) : Nat × Nat × Nat × Nat :=
  ((3 * a + 2 * b) % n, (4 * a + 3 * b) % n, (3 * c + 2 * d) % n, (4 * c + 3 * d) % n)

def matPow (n : Nat) : Nat → Nat × Nat × Nat × Nat
  | 0 => (1 % n, 0, 0, 1 % n)
  | k + 1 =>
    let (a, b, c, d) := matPow n k
    matStep n a b c d

theorem detSI : (2 : Int) * 2 - 4 * 2 = -4 := by decide

theorem order5 : matPow 5 6 = (1, 0, 0, 1) := by decide
theorem order7 : matPow 7 3 = (1, 0, 0, 1) := by decide
theorem order11 : matPow 11 12 = (1, 0, 0, 1) := by decide
theorem notOrder5 : matPow 5 1 ≠ (1, 0, 0, 1) ∧ matPow 5 2 ≠ (1, 0, 0, 1) ∧ matPow 5 3 ≠ (1, 0, 0, 1) ∧ matPow 5 5 ≠ (1, 0, 0, 1) := by decide
theorem notOrder7 : matPow 7 1 ≠ (1, 0, 0, 1) ∧ matPow 7 2 ≠ (1, 0, 0, 1) := by decide

def row (n j : Nat) : Nat × Nat :=
  let (a, b, _, _) := matPow n j
  (a, b)

def quadCount (n m : Nat) : Nat :=
  (List.range m).foldl (fun acc a =>
    (List.range m).foldl (fun acc2 b =>
      let (ua, va) := row n a
      let (ub, vb) := row n b
      (List.range m).foldl (fun acc3 c =>
        (List.range m).foldl (fun acc4 d =>
          let (uc, vc) := row n c
          let (ud, vd) := row n d
          let ok := (ua + ub) % n == (uc + ud) % n && (va + vb) % n == (vc + vd) % n
          acc4 + if ok then 1 else 0) acc3) acc2) acc) 0

theorem quad5 : quadCount 5 6 = 90 := by decide
theorem quad7 : quadCount 7 3 = 15 := by decide
theorem perm5 : 2 * 6 * 6 - 6 = 66 := by decide
theorem perm7 : 2 * 3 * 3 - 3 = 15 := by decide

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

/-- Scaled energy `∑ 25 r(k)^2` of the `ℓ = 1` row, equal to `900 = 9/160000 · 4000^2`. -/
def oddSum : Int :=
  (List.range 19).foldl (fun acc i =>
    let k := Int.ofNat i - 9
    let r := rNum k
    acc + 25 * r * r) 0

theorem oddEnergy : oddSum = 900 := by decide
theorem oddRatio : (900 : Int) * 160000 = 9 * 16000000 := by decide
#print axioms detSI
#print axioms order5
#print axioms order7
#print axioms order11
#print axioms notOrder5
#print axioms notOrder7
#print axioms quad5
#print axioms quad7
#print axioms perm5
#print axioms perm7
#print axioms oddEnergy
#print axioms oddRatio
end Bgs.ScalarReturnBesselRational
