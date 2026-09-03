/-
  Finite pair-key second-moment certificate at p=53, a=10, K=13.

  Scope. This file checks the finite combinatorial core only. It does not
  formalize the general character-orthogonality derivation and is not a
  uniform theorem in p or K.

  Certified claims:
  * the off-diagonal constraint set P has (K-1)(K-2)=132 points;
  * the (u,v)-parametrization is a bijection onto P at this design;
  * a has exact order K and m=(p-1)/K=4.

  The larger finite searches use native_decide; CI builds every active module.
-/

namespace Bgs.PairKeySecondMoment

def N : Nat := 53
def a : Nat := 10
def K : Nat := 13

def powmod (b e m : Nat) : Nat := (Nat.pow b e) % m
def minv (x : Nat) : Nat := powmod x (N - 2) N

def H : List Nat := (List.range K).map fun i => powmod a i N
def m : Nat := (N - 1) / K

def admissible (x y : Nat) : Bool :=
  !(x == 0) && !(x == 1) && !(y == 0) && !(y == 1) && !(x == y)

def inP (x y : Nat) : Bool :=
  admissible x y &&
  H.contains ((x * minv y) % N) &&
  H.contains (((x - 1) * minv ((y - 1) % N)) % N)

def P : List (Nat × Nat) :=
  ((List.range (N - 2)).map fun i => i + 2).flatMap fun x =>
    ((List.range (N - 2)).map fun j => j + 2).filterMap fun y =>
      if inP x y then some (x, y) else none

def UV : List (Nat × Nat) :=
  H.flatMap fun u => H.filterMap fun v =>
    if !(u == v) && !(u == 1) && !(v == 1) then some (u, v) else none

def param (uv : Nat × Nat) : Nat × Nat :=
  let u := uv.1
  let v := uv.2
  let y := ((1 + N - v % N) % N * minv ((u + N - v) % N)) % N
  let x := (u * y) % N
  (x, y)

def lePair (x y : Nat × Nat) : Bool :=
  x.1 < y.1 || (x.1 == y.1 && x.2 <= y.2)

def insertPair (h : Nat × Nat) : List (Nat × Nat) → List (Nat × Nat)
  | [] => [h]
  | x :: xs => if lePair h x then h :: x :: xs else x :: insertPair h xs

def sortPairs : List (Nat × Nat) → List (Nat × Nat)
  | [] => []
  | h :: t => insertPair h (sortPairs t)

theorem constraint_count : P.length = (K - 1) * (K - 2) := by
  native_decide

theorem parameterization_bijection :
    sortPairs P = sortPairs (UV.map param) := by
  native_decide

theorem design_sizes : H.length = K ∧ m * K + 1 = N ∧ m = 4 := by
  native_decide

theorem generator_exact_order :
    powmod a K N = 1 ∧
    (List.range (K - 1)).all fun i => !(powmod a (i + 1) N == 1) := by
  native_decide

#print axioms constraint_count
#print axioms parameterization_bijection
#print axioms design_sizes
#print axioms generator_exact_order

end Bgs.PairKeySecondMoment
