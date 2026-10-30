set_option maxRecDepth 1000000
set_option maxHeartbeats 0

namespace Bgs.DiagonalPhaseShortTimeRational

/-!
# Rational witness for BGS-TRACE-128

Integer comparisons for the symmetric error constant, the time-three gap
between the closed form and the dihedral main term, the integer main terms
at dimensions 3, 5 and 7, and the Kloosterman quadruple census at the
primes 5 and 7. The occupation sum that identifies these integers with the
form factor is in `mathematics/fixed-map/diagonal_phase_short_time.md`.
This file does not sum the complex form factor.
-/

def fact : Nat → Nat
  | 0 => 1
  | n + 1 => (n + 1) * fact n

theorem subSubCancel (a b c : Int) : a - (b - c) = a - b + c := by
  rw [Int.sub_eq_add_neg, Int.neg_sub, Int.sub_eq_add_neg, ← Int.add_assoc, Int.add_comm a c,
      Int.add_assoc, Int.add_comm c (a + -b), ← Int.sub_eq_add_neg]

theorem prodExpand (N : Int) : (N - 1) * (N - 2) = N * N - 3 * N + 2 := by
  calc
    (N - 1) * (N - 2) = N * (N - 2) - (N - 2) := by rw [Int.sub_mul]; simp
    _ = N * N - 2 * N - (N - 2) := by rw [Int.mul_sub]; simp [Int.mul_comm]
    _ = N * N - 2 * N - N + 2 := by rw [subSubCancel]
    _ = N * N - (2 * N + N) + 2 := by rw [Int.sub_sub]
    _ = N * N - 3 * N + 2 := by
          have : (2 : Int) * N + N = 3 * N := by
            calc
              (2 : Int) * N + N = 2 * N + 1 * N := by simp
              _ = (2 + 1) * N := by rw [← Int.add_mul]
              _ = 3 * N := by simp
          rw [this]

def invMod (p x : Nat) : Nat :=
  (List.range p).foldl (fun acc a => if (a * x) % p = 1 then a else acc) 0

/-- Quadruples in `{1,...,p-1}^4` with equal sums and equal inverse sums. -/
def quadCount (p : Nat) : Nat :=
  (List.range (p - 1)).foldl (fun acc1 i1 =>
    let n1 := i1 + 1
    let inv1 := invMod p n1
    (List.range (p - 1)).foldl (fun acc2 i2 =>
      let n2 := i2 + 1
      let inv2 := invMod p n2
      (List.range (p - 1)).foldl (fun acc3 i3 =>
        let n3 := i3 + 1
        let inv3 := invMod p n3
        (List.range (p - 1)).foldl (fun acc4 i4 =>
          let n4 := i4 + 1
          let inv4 := invMod p n4
          let sumOk := (n1 + n2) % p == (n3 + n4) % p
          let invOk := (inv1 + inv2) % p == (inv3 + inv4) % p
          acc4 + if sumOk && invOk then 1 else 0) acc3) acc2) acc1) 0

theorem quadCount5 : quadCount 5 = 36 := by decide
theorem quadCount7 : quadCount 7 = 90 := by decide
theorem quadCap5 : quadCount 5 ≤ 3 * 4 * 4 := by decide
theorem quadCap7 : quadCount 7 ≤ 3 * 6 * 6 := by decide

theorem symErr3 : fact 3 * (1 + 3 * 2) = 42 := by decide
theorem symErr4 : fact 4 * (1 + 4 * 3) = 312 := by decide
theorem symErr5 : fact 5 * (1 + 5 * 4) = 2520 := by decide

theorem dihedral3 : 2 * 3 * fact 2 = 2 * fact 3 := by decide
theorem dihedral4 : 2 * 4 * fact 3 = 2 * fact 4 := by decide
theorem dihedral5 : 2 * 5 * fact 4 = 2 * fact 5 := by decide

/-- The time-three closed numerator minus the dihedral main term, times `N^2`. -/
theorem time3MainDifference (N : Int) :
    (6 * N * N - 9 * N + 4) - 6 * ((N - 1) * (N - 2)) = 9 * N - 8 := by
  rw [prodExpand]
  have hAssoc : (6 : Int) * (N * N) = 6 * N * N := by rw [← Int.mul_assoc]
  have h18 : (6 : Int) * (3 * N) = 18 * N := by
    rw [← Int.mul_assoc]
    simp
  have h6 : 6 * (N * N - 3 * N + 2) = 6 * N * N - 18 * N + 12 := by
    calc
      6 * (N * N - 3 * N + 2) = 6 * (N * N - 3 * N) + 12 := by rw [Int.mul_add]; simp
      _ = (6 * (N * N) - 6 * (3 * N)) + 12 := by rw [Int.mul_sub]
      _ = (6 * N * N - 18 * N) + 12 := by rw [hAssoc, h18]
      _ = 6 * N * N - 18 * N + 12 := by rfl
  have regroup : 6 * N * N - 18 * N + 12 = 6 * N * N - (18 * N - 12) := by
    rw [← subSubCancel]
  rw [h6, regroup, subSubCancel]
  omega

theorem time3WithinBound (N : Nat) (h : 1 ≤ N) : 9 * N - 8 ≤ 42 * N := by
  omega

theorem main3At3 : 2 * 3 * (3 * 2 * 1) = 36 ∧ 3 * 3 * 3 = 27 := by decide
theorem main3At5 : 2 * 3 * (5 * 4 * 3) = 360 ∧ 5 * 5 * 5 = 125 := by decide
theorem main3At7 : 2 * 3 * (7 * 6 * 5) = 1260 ∧ 7 * 7 * 7 = 343 := by decide
theorem main4At3 : 2 * 4 * 0 = 0 ∧ 3 * 3 * 3 * 3 = 81 := by decide
theorem main4At5 : 2 * 4 * (5 * 4 * 3 * 2) = 960 ∧ 5 * 5 * 5 * 5 = 625 := by decide
theorem main4At7 : 2 * 4 * (7 * 6 * 5 * 4) = 6720 ∧ 7 * 7 * 7 * 7 = 2401 := by decide
theorem main5At3 : 2 * 5 * 0 = 0 ∧ 3 ^ 5 = 243 := by decide
theorem main5At5 : 2 * 5 * 0 = 0 ∧ 5 ^ 5 = 3125 := by decide
theorem main5At7 : 2 * 5 * (7 * 6 * 5 * 4 * 3) = 25200 ∧ 7 ^ 5 = 16807 := by decide

/-- The `p=3` trivial estimate at times 3, 4 and 5: `m!+m` against the proved factor. -/
theorem trivial3 : fact 3 + 3 ≤ fact 3 * (3 * 2 + 5) / 3 := by decide
theorem trivial4 : fact 4 + 4 ≤ fact 4 * (4 * 3 + 5) / 3 := by decide
theorem trivial5 : fact 5 + 5 ≤ fact 5 * (5 * 4 + 5) / 3 := by decide
#print axioms subSubCancel
#print axioms prodExpand
#print axioms quadCount5
#print axioms quadCount7
#print axioms quadCap5
#print axioms quadCap7
#print axioms symErr3
#print axioms symErr4
#print axioms symErr5
#print axioms dihedral3
#print axioms dihedral4
#print axioms dihedral5
#print axioms time3MainDifference
#print axioms time3WithinBound
#print axioms main3At3
#print axioms main3At5
#print axioms main3At7
#print axioms main4At3
#print axioms main4At5
#print axioms main4At7
#print axioms main5At3
#print axioms main5At5
#print axioms main5At7
#print axioms trivial3
#print axioms trivial4
#print axioms trivial5
end Bgs.DiagonalPhaseShortTimeRational
