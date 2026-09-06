/-
  RUN 94 — machine-checked certificate for the k=4 constraint-variety
  count |V4| at the design prime N = 53, a = 10, K = ord(10) = 13.

  The k=4 factorization (Theorem 92.2, THEORY §19.28) reduces the coset
  fourth moment to a sum over the 2-dimensional variety

    V4 = {(x,y,z,w) : x,y,z,w ∉ {0,1},
          x·z / (y·w) ∈ H,  (x−1)(z−1) / ((y−1)(w−1)) ∈ H},

  H = <a> the K-cyclic subgroup.  IMPORTANT: the individual pairs (x,y)
  carry NO constraint of their own — only the PRODUCT constraints across
  the two pairs.  This file certifies, by evaluation:

    V1  |V4| = 423879 at N = 53 (matches the R92.2 brute-force mask count
        and the R92.13 pair-key factorization — three independent
        computational routes now agree);
    V2  the pair→key map (x,y) ↦ (x/y, (x−1)/(y−1)) is INJECTIVE off the
        diagonal: the 2550 off-diagonal admissible pairs have 2550
        distinct keys (certified via strictly-sorted duplicate check);
    V3  the diagonal key (1,1) covers exactly N−2 = 51 pairs (x = y).

  V2+V3 give the exact pair-key multiplicities n(u,v) of the coupled-
  energy model (R92.15), which produced the EXACT predictions
  Z0 = 12063 and mean Σ₄ = 4143.46 at this design.

  Lean 4.33.1, no Mathlib.  Build: `cd formal && lake build`.
-/

namespace Bgs.K4Variety

def N : Nat := 53
def a : Nat := 10
def K : Nat := 13

def powmod (b e m : Nat) : Nat := (Nat.pow b e) % m
def minv2 (x : Nat) : Nat := powmod x (N - 2) N

/-- the subgroup H = <a> -/
def H : List Nat := (List.range K).map fun i => powmod a i N

/-- admissible pair: x,y ∉ {0,1} -/
def adm (x y : Nat) : Bool := !(x == 0) && !(x == 1) && !(y == 0) && !(y == 1)

/-- ALL admissible pairs (x,y) — NO individual constraint (the k=4
    constraints are product constraints across two pairs) -/
def allPairs : List (Nat × Nat) :=
  ((List.range (N - 2)).map fun i => i + 2).flatMap fun x =>
    ((List.range (N - 2)).map fun j => j + 2).filterMap fun y =>
      if adm x y then some (x, y) else none

/-- cross constraint for an ordered pair of pairs -/
def crossOK (p q : Nat × Nat) : Bool :=
  (H.contains (((p.1 * q.1) * minv2 ((p.2 * q.2) % N)) % N)) &&
  (H.contains ((((p.1 - 1) * (q.1 - 1)) * minv2 (((p.2 - 1) * (q.2 - 1)) % N)) % N))

/-- |V4| by the bilinear pair count over all admissible pairs -/
def countV4 : Nat :=
  (allPairs.flatMap fun p =>
    (allPairs.filter fun q => crossOK p q).map fun _ => 1).length

/-- diagonal pairs (x,x) — the key (1,1) class -/
def diagCount : Nat :=
  (allPairs.filter fun p => p.1 == p.2).length

/-- off-diagonal admissible pairs -/
def allOff : List (Nat × Nat) :=
  allPairs.filter fun p => !(p.1 == p.2)

/-- key of an off-diagonal pair -/
def keyOf (p : Nat × Nat) : Nat × Nat :=
  ((p.1 * minv2 p.2) % N, ((p.1 - 1) * minv2 ((p.2 - 1) % N)) % N)

/-- insertion sort on pairs -/
def lePair (a b : Nat × Nat) : Bool :=
  a.1 < b.1 || (a.1 == b.1 && a.2 <= b.2)

def insertPair (h : Nat × Nat) : List (Nat × Nat) → List (Nat × Nat)
  | [] => [h]
  | x :: xs => if lePair h x then h :: x :: xs else x :: insertPair h xs

def sortPairs : List (Nat × Nat) → List (Nat × Nat)
  | [] => []
  | h :: t => insertPair h (sortPairs t)

/-- strictly sorted = sorted with no consecutive duplicates -/
def strictlySorted : List (Nat × Nat) → Bool
  | [] => true
  | [_] => true
  | a :: b :: rest => lePair a b && !(a == b) && strictlySorted (b :: rest)

/-! ## The certified claims -/

/-- the diagonal key covers exactly N-2 pairs -/
theorem diag_exact : diagCount = N - 2 := by native_decide

/-- the keys of off-diagonal admissible pairs are DISTINCT (injectivity
    of the pair → key map off the diagonal) -/
theorem keys_injective :
    strictlySorted (sortPairs (allOff.map keyOf)) = true := by
  native_decide

/-- |V4| = 423879 (three independent routes agree) -/
theorem V4_count : countV4 = 423879 := by native_decide

#print axioms diag_exact
#print axioms keys_injective
#print axioms V4_count

end Bgs.K4Variety
