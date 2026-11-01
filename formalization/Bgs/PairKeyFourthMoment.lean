/-
  Finite fourth-moment pair-key certificate at p=53, a=10, K=13.

  Scope. This file certifies the finite pair-key multiplicities and the V4
  count at one design. It does not prove the general symbolic formula or any
  asymptotic spectral statement.

  Certified claims:
  * the diagonal key (1,1) has multiplicity p-2=51;
  * the pair-to-key map is injective off the diagonal;
  * the coupled four-variable constraint count is 423879.
-/

namespace Bgs.PairKeyFourthMoment

def N : Nat := 53
def a : Nat := 10
def K : Nat := 13

def powmod (b e m : Nat) : Nat := (Nat.pow b e) % m
def minv (x : Nat) : Nat := powmod x (N - 2) N

def H : List Nat := (List.range K).map fun i => powmod a i N

def admissible (x y : Nat) : Bool :=
  !(x == 0) && !(x == 1) && !(y == 0) && !(y == 1)

def allPairs : List (Nat × Nat) :=
  ((List.range (N - 2)).map fun i => i + 2).flatMap fun x =>
    ((List.range (N - 2)).map fun j => j + 2).filterMap fun y =>
      if admissible x y then some (x, y) else none

def crossOK (p q : Nat × Nat) : Bool :=
  H.contains (((p.1 * q.1) * minv ((p.2 * q.2) % N)) % N) &&
  H.contains ((((p.1 - 1) * (q.1 - 1)) *
    minv (((p.2 - 1) * (q.2 - 1)) % N)) % N)

def countV4 : Nat :=
  (allPairs.flatMap fun p =>
    (allPairs.filter fun q => crossOK p q).map fun _ => 1).length

def diagonalCount : Nat :=
  (allPairs.filter fun p => p.1 == p.2).length

def allOffDiagonal : List (Nat × Nat) :=
  allPairs.filter fun p => !(p.1 == p.2)

def keyOf (p : Nat × Nat) : Nat × Nat :=
  ((p.1 * minv p.2) % N,
   ((p.1 - 1) * minv ((p.2 - 1) % N)) % N)

def lePair (x y : Nat × Nat) : Bool :=
  x.1 < y.1 || (x.1 == y.1 && x.2 <= y.2)

def insertPair (h : Nat × Nat) : List (Nat × Nat) → List (Nat × Nat)
  | [] => [h]
  | x :: xs => if lePair h x then h :: x :: xs else x :: insertPair h xs

def sortPairs : List (Nat × Nat) → List (Nat × Nat)
  | [] => []
  | h :: t => insertPair h (sortPairs t)

def strictlySorted : List (Nat × Nat) → Bool
  | [] => true
  | [_] => true
  | x :: y :: rest => lePair x y && !(x == y) && strictlySorted (y :: rest)

theorem diagonal_multiplicity : diagonalCount = N - 2 := by
  decide +kernel

theorem off_diagonal_keys_injective :
    strictlySorted (sortPairs (allOffDiagonal.map keyOf)) = true := by
  native_decide

theorem coupled_constraint_count : countV4 = 423879 := by
  native_decide

#print axioms diagonal_multiplicity
#print axioms off_diagonal_keys_injective
#print axioms coupled_constraint_count

end Bgs.PairKeyFourthMoment
