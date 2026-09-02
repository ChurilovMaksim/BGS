/-
  RUN 92 — machine-checked certificate for the COUNTING part of
  Theorem 92.1 (the k=2 layer of the trace-fluctuation hypothesis H3),
  at the design prime N = 53, a = 10, K = ord(10) = 13.

  Theorem 92.1 (LEDGER RUN 92, THEORY §19.27) collapses the coset second
  moment A_S(q) = Σ_{i,j∈S} |J(χ_i,χ_j;q)|²  to

      A_S(q) = m² · [ (N−2) + S_off(q) ],

  where S_off(q) is a sum of e_N(q(x−y)) over the constraint set

      P = {(x,y) : x,y ∉ {0,1}, x ≠ y, x/y ∈ H, (x−1)/(y−1) ∈ H},

  H = <a> the K-cyclic subgroup, m = |S| = (N−1)/K.  The TWO COUNTING
  claims that make the reduction exact are formalised here by evaluation:

    P1  |P| = (K−1)(K−2)               (at N=53: 132 = 12·11);
    P2  the parametrisation (u,v) ↦ (x,y) = (u·y, ·) with
        y = (1−v)/(u−v), (u,v) ∈ H², u ≠ v, u,v ≠ 1, is a BIJECTION
        between {(u,v) : u,v ∈ H, u ≠ v, u,v ≠ 1} and P.

  P2 is the content that turns the character-orthogonality collapse into
  an explicit two-variable sum; it is checked by building both lists and
  comparing them as multisets after sorting (permutation-equality by
  pointwise comparison of the sorted lists).

  Scope (honest): this is a certificate at ONE prime, not a general
  proof — the general statement (Theorem 92.1 in full) needs the
  character-orthogonality algebra, which is Mathlib territory.  The
  design follows TorusLevelSets.lean (RUN 82): decidable finite
  statements settled by `native_decide`, with the axiom disclosure
  printed at the end.

  Lean 4.33.1, no Mathlib.  Build: `cd formal && lake build`.
-/

namespace Bgs.K2Reduction

/-- the design prime -/
def N : Nat := 53

/-- the generator a = 10 -/
def a : Nat := 10

/-- ord(10) mod 53 — certified by `ordA` below -/
def K : Nat := 13

def inv (x : Nat) : Nat := (x * x) % N  -- placeholder, real inv via pow below

/-- powmod helper -/
def powmod (b e m : Nat) : Nat :=
  (Nat.pow b e) % m

/-- modular inverse of x at prime N: x^(N-2) mod N -/
def minv2 (x : Nat) : Nat := powmod x (N - 2) N

/-- the subgroup H = <a>: successive powers -/
def H : List Nat :=
  (List.range K).map fun i => powmod a i N

/-- the annihilator coset size m = (N-1)/K -/
def m : Nat := (N - 1) / K

/-- constraint: both coordinates of (x,y) not in {0,1} and x ≠ y -/
def admissible (x y : Nat) : Bool :=
  !(x == 0) && !(x == 1) && !(y == 0) && !(y == 1) && !(x == y)

/-- x/y ∈ H and (x-1)/(y-1) ∈ H  (mod N), with x,y admissible -/
def inP (x y : Nat) : Bool :=
  admissible x y &&
  (H.contains ((x * minv2 y) % N)) &&
  (H.contains (((x - 1) * minv2 ((y - 1) % N)) % N))

/-- the constraint set P as a list of pairs, over x,y ∈ [2, N-1] -/
def P : List (Nat × Nat) :=
  ((List.range (N - 2)).map fun i => i + 2).flatMap fun x =>
    ((List.range (N - 2)).map fun j => j + 2).filterMap fun y =>
      if inP x y then some (x, y) else none

/-- the parametrisation domain: (u,v) ∈ H², u ≠ v, u,v ≠ 1 -/
def UV : List (Nat × Nat) :=
  (H.flatMap fun u => H.filterMap fun v =>
    if !(u == v) && !(u == 1) && !(v == 1)
    then some (u, v) else none)

/-- the parametrised pair: y = (1-v)/(u-v), x = u·y -/
def param (uv : Nat × Nat) : Nat × Nat :=
  let u := uv.1
  let v := uv.2
  let y := ((1 + N - v % N) % N * minv2 ((u + N - v) % N)) % N
  let x := (u * y) % N
  (x, y)


/-- insertion sort on pairs, for permutation-equality checking -/
def lePair (a b : Nat × Nat) : Bool :=
  a.1 < b.1 || (a.1 == b.1 && a.2 <= b.2)

def insertPair (h : Nat × Nat) : List (Nat × Nat) → List (Nat × Nat)
  | [] => [h]
  | x :: xs => if lePair h x then h :: x :: xs else x :: insertPair h xs

def sortPairs : List (Nat × Nat) → List (Nat × Nat)
  | [] => []
  | h :: t => insertPair h (sortPairs t)

/-! ## The certified claims -/

/-- P1: |P| = (K-1)(K-2) -/
theorem cardP : (P.length : Nat) = (K - 1) * (K - 2) := by
  native_decide

/-- P2: sorted P = sorted (map param UV) — the parametrisation is a
    bijection onto P -/
theorem param_bijection :
    sortPairs P = sortPairs (UV.map param) := by
  native_decide

/-- the subgroup really has K elements and m = (N-1)/K -/
theorem sizes : H.length = K ∧ m * K + 1 = N ∧ m = 4 := by
  native_decide

/-- ord(a) = K: a^K = 1 mod N and no earlier power returns 1 -/
theorem ordA :
    powmod a K N = 1 ∧
    (List.range (K - 1)).all fun i => !(powmod a (i + 1) N == 1) := by
  native_decide

#print axioms cardP
#print axioms param_bijection
#print axioms sizes
#print axioms ordA

end Bgs.K2Reduction
