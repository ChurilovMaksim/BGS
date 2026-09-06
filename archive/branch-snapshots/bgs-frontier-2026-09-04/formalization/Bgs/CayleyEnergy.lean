/-
  Reusable exact finite certificates for the mixed Cayley collision energy.

  This module deliberately proves only finite statements at explicit designs.
  It does not compute E_K for arbitrary K and does not promote the fixed-K
  computations to a uniform theorem in K.

  The same designs are checked independently by
  computations/cpp/cayley_energy_verifier.cpp and the Python verification
  layer.
-/

namespace Bgs.CayleyEnergy

def powmod (b e m : Nat) : Nat := (Nat.pow b e) % m

def subgroup (N K a : Nat) : List Nat :=
  (List.range K).map fun i => powmod a i N

def invModPrime (N x : Nat) : Nat := powmod x (N - 2) N

def keyDifference (N u v : Nat) : Nat :=
  (((u + N - 1) % N) * ((v + N - 1) % N) % N) *
    invModPrime N ((v + N - u) % N) % N

def admissiblePairs (N K a : Nat) : List (Nat × Nat) :=
  (subgroup N K a).flatMap fun u =>
    (subgroup N K a).filterMap fun v =>
      if u != 1 && v != 1 && u != v then some (u, v) else none

def countAt (N K a t : Nat) : Nat :=
  ((admissiblePairs N K a).filter fun uv =>
    keyDifference N uv.1 uv.2 == t).length

def collisionEnergy (N K a : Nat) : Nat :=
  (List.range N).foldl
    (fun total t =>
      let count := countAt N K a t
      total + count * count)
    0

def forcedBaseline (K : Nat) : Nat := (K - 1) * (2 * K - 5)

def generatorExactOrder (N K a : Nat) : Bool :=
  powmod a K N == 1 &&
    (List.range (K - 1)).all fun i => !(powmod a (i + 1) N == 1)

/-! ## K = 11: one generic and one exceptional reduction. -/

theorem k11_generic_generator :
    generatorExactOrder 199 11 139 = true := by
  native_decide

theorem k11_generic_pair_count :
    (admissiblePairs 199 11 139).length = 90 := by
  native_decide

theorem k11_generic_energy :
    collisionEnergy 199 11 139 = 170 := by
  native_decide

theorem k11_generic_is_forced :
    collisionEnergy 199 11 139 = forcedBaseline 11 := by
  native_decide

theorem k11_exceptional_generator :
    generatorExactOrder 67 11 64 = true := by
  native_decide

theorem k11_exceptional_pair_count :
    (admissiblePairs 67 11 64).length = 90 := by
  native_decide

theorem k11_exceptional_energy :
    collisionEnergy 67 11 64 = 218 := by
  native_decide

theorem k11_exceptional_has_excess :
    collisionEnergy 67 11 64 > forcedBaseline 11 := by
  native_decide

/-! ## K = 13: one generic and one exceptional reduction. -/

theorem k13_generic_generator :
    generatorExactOrder 521 13 101 = true := by
  native_decide

theorem k13_generic_pair_count :
    (admissiblePairs 521 13 101).length = 132 := by
  native_decide

theorem k13_generic_energy :
    collisionEnergy 521 13 101 = 252 := by
  native_decide

theorem k13_generic_is_forced :
    collisionEnergy 521 13 101 = forcedBaseline 13 := by
  native_decide

theorem k13_exceptional_generator :
    generatorExactOrder 53 13 10 = true := by
  native_decide

theorem k13_exceptional_pair_count :
    (admissiblePairs 53 13 10).length = 132 := by
  native_decide

theorem k13_exceptional_energy :
    collisionEnergy 53 13 10 = 460 := by
  native_decide

theorem k13_exceptional_has_excess :
    collisionEnergy 53 13 10 > forcedBaseline 13 := by
  native_decide

/-! ## K = 23 non-uniformity witness. -/

theorem k23_generator :
    generatorExactOrder 461 23 23 = true := by
  native_decide

theorem k23_pair_count :
    (admissiblePairs 461 23 23).length = 462 := by
  native_decide

theorem k23_forced_baseline :
    forcedBaseline 23 = 902 := by
  native_decide

theorem k23_energy :
    collisionEnergy 461 23 23 = 1190 := by
  native_decide

theorem k23_has_excess :
    collisionEnergy 461 23 23 > forcedBaseline 23 := by
  native_decide

#print axioms k11_generic_energy
#print axioms k11_exceptional_energy
#print axioms k13_generic_energy
#print axioms k13_exceptional_energy
#print axioms k23_energy
#print axioms k23_has_excess

end Bgs.CayleyEnergy
