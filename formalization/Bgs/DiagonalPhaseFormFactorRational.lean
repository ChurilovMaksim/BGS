set_option maxRecDepth 1000000
set_option maxHeartbeats 0

namespace Bgs.DiagonalPhaseFormFactorRational

/-!
# Rational witness for BGS-TRACE-127

Integer matrix factorizations for `S^2-I` and `S^3-I`, and the comparisons
`(2N-1)/N > 1`, `(6N^2-9N+4)/N^2 > 1` and `< 6`. The path count that
identifies these rationals with the diagonal-phase form factor is in
`mathematics/fixed-map/diagonal_phase_form_factor.md`. This file does not
formalize that count, the trace closure, or the sixteen-phase sample.
-/

theorem subSubCancel (a b c : Int) : a - (b - c) = a - b + c := by
  rw [Int.sub_eq_add_neg, Int.neg_sub, Int.sub_eq_add_neg, ← Int.add_assoc, Int.add_comm a c,
      Int.add_assoc, Int.add_comm c (a + -b), ← Int.sub_eq_add_neg]

/-- `(5N-4)(N-1) = 5N^2 - 9N + 4` in `ℤ`. -/
theorem time3Numerator (N : Int) : (5 * N - 4) * (N - 1) = 5 * N * N - 9 * N + 4 := by
  calc
    (5 * N - 4) * (N - 1)
        = 5 * N * (N - 1) - 4 * (N - 1) := by rw [Int.sub_mul]
    _ = (5 * N * N - 5 * N) - (4 * N - 4) := by rw [Int.mul_sub, Int.mul_sub]; simp
    _ = 5 * N * N - 5 * N - 4 * N + 4 := by rw [subSubCancel]
    _ = 5 * N * N - (5 * N + 4 * N) + 4 := by rw [Int.sub_sub]
    _ = 5 * N * N - 9 * N + 4 := by
          have : (5 : Int) * N + 4 * N = 9 * N := by rw [← Int.add_mul]; simp
          rw [this]

theorem time2Gap (N : Nat) (h : 2 ≤ N) : N < 2 * N - 1 := by
  omega

theorem time3Gap (N : Int) (hN : 3 ≤ N) : 0 < 5 * N * N - 9 * N + 4 := by
  rw [← time3Numerator]
  exact Int.mul_pos (by omega) (by omega)

theorem time3BelowSix (N : Int) (_hN : 1 ≤ N) : 6 * N * N - 9 * N + 4 < 6 * N * N := by
  omega

theorem time2AtMostTwo (N : Int) : 2 * N - 1 ≤ 2 * N := by
  omega

/-- `S^2 = [[17,24],[12,17]]` and `det(S^2-I) = -32`. -/
theorem s2Det : (16 : Int) * 16 - 24 * 12 = -32 := by
  decide

theorem s2Entries :
    ((3 : Int) * 3 + 4 * 2 = 17) ∧ (3 * 4 + 4 * 3 = 24) ∧
    (2 * 3 + 3 * 2 = 12) ∧ (2 * 4 + 3 * 3 = 17) := by
  decide

/-- `A = [[7,10],[5,7]]`, `det A = -1`, and `14A+I = S^3`. -/
theorem s3Factor :
    ((7 : Int) * 7 - 10 * 5 = -1) ∧
    (14 * 7 + 1 = 99) ∧ (14 * 10 = 140) ∧
    (14 * 5 = 70) := by
  decide

theorem s3Entries :
    ((17 : Int) * 3 + 24 * 2 = 99) ∧ (17 * 4 + 24 * 3 = 140) ∧
    (12 * 3 + 17 * 2 = 70) ∧ (12 * 4 + 17 * 3 = 99) := by
  decide

theorem revivalAt7 : (6 : Int) * 49 - 9 * 7 + 4 = 235 := by
  decide

theorem pureRevivalAt7 : (7 : Int) * 7 = 49 := by
  decide

theorem sixBelowFortyNine : (6 : Int) < 49 := by
  decide

/-- Brute-force count of `(a,b) mod N` with `(S^3-I)(a,b) = 0`,
where `S^3-I = [[98,140],[70,98]]`. -/
def kernelCount3 (N : Nat) : Nat :=
  (List.range N).foldl (fun acc a =>
    (List.range N).foldl (fun acc2 b =>
      let e1 := (98 * a + 140 * b) % N
      let e2 := (70 * a + 98 * b) % N
      acc2 + if e1 = 0 ∧ e2 = 0 then 1 else 0) acc) 0

theorem kernelCount3_7 : kernelCount3 7 = 49 := by decide
theorem kernelCount3_9 : kernelCount3 9 = 1 := by decide
theorem kernelCount3_21 : kernelCount3 21 = 49 := by decide
theorem kernelCount3_49 : kernelCount3 49 = 49 := by decide
end Bgs.DiagonalPhaseFormFactorRational
