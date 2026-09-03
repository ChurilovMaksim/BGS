/-
  Exact finite certificate for the exceptional mixed-energy design N=461, K=23.

  Scientific scope: this file is a finite negative control. It is NOT a
  computation of the complete exceptional set E_23 and it is NOT a uniform
  theorem in K. The independent Python certificate is
  experiments/verification/verify_cayley_anchor_k23.py.

  This source is retained even when a local runtime cannot execute Lean.
-/

namespace Bgs.CayleyExceptionalK23

def N : Nat := 461
def K : Nat := 23
def a : Nat := 23

def powmod (b e m : Nat) : Nat := (Nat.pow b e) % m

def H : List Nat := (List.range K).map fun i => powmod a i N

def inv (x : Nat) : Nat := powmod x (N - 2) N

def difference (u v : Nat) : Nat :=
  (((u + N - 1) % N) * ((v + N - 1) % N) % N) *
    inv ((v + N - u) % N) % N

def admissiblePairs : List (Nat × Nat) :=
  (H.flatMap fun u =>
    H.filterMap fun v =>
      if u != 1 && v != 1 && u != v then some (u, v) else none)

def countAt (t : Nat) : Nat :=
  (admissiblePairs.filter fun uv => difference uv.1 uv.2 == t).length

def collisionEnergy : Nat :=
  (List.range N).foldl (fun s t => s + (countAt t) * (countAt t)) 0

def forcedBaseline : Nat := (K - 1) * (2 * K - 5)

theorem generator_closes : powmod a K N = 1 := by
  native_decide

theorem admissible_pair_count : admissiblePairs.length = 462 := by
  native_decide

theorem forced_baseline_value : forcedBaseline = 902 := by
  native_decide

theorem exceptional_energy : collisionEnergy = 1190 := by
  native_decide

theorem exceptional_not_forced : collisionEnergy != forcedBaseline := by
  native_decide

#print axioms generator_closes
#print axioms admissible_pair_count
#print axioms forced_baseline_value
#print axioms exceptional_energy
#print axioms exceptional_not_forced

end Bgs.CayleyExceptionalK23
