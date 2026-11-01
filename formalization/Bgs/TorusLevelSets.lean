/-
  Finite torus level-set/orbit certificate at p=199.

  This module formalizes only finite combinatorics for
    Q(a,b)=a^2-ab-b^2 mod p
  and the cyclic action of A^T=[[2,1],[1,1]]. The analytic Weil
  intertwining relation that motivates the orbit interpretation is not proved
  here. Large finite evaluations use native_decide.
-/

namespace Bgs.TorusLevelSets

def p : Nat := 199
def K : Nat := 11

def Q (a b : Nat) : Nat :=
  (a * a + (p - 1) * a * b + (p - 1) * b * b) % p

def vectors : List (Nat × Nat) :=
  ((List.range p).flatMap fun a => (List.range p).map fun b => (a, b)).filter
    fun x => !(x.1 == 0 && x.2 == 0)

def level (q : Nat) : List (Nat × Nat) :=
  vectors.filter fun x => Q x.1 x.2 == q

def step (x : Nat × Nat) : Nat × Nat :=
  ((2 * x.1 + x.2) % p, (x.1 + x.2) % p)

def iter (n : Nat) (x : Nat × Nat) : Nat × Nat :=
  match n with
  | 0 => x
  | n + 1 => iter n (step x)

def orbitMin (x : Nat × Nat) : Nat × Nat :=
  let rec go : Nat → Nat × Nat → Nat × Nat → Nat × Nat
    | 0, _, best => best
    | n + 1, cur, best =>
      let nxt := step cur
      let better :=
        if nxt.1 < best.1 || (nxt.1 == best.1 && nxt.2 < best.2)
        then nxt else best
      go n nxt better
  go K x x

def dedup (l : List (Nat × Nat)) : List (Nat × Nat) :=
  l.foldl (fun acc x => if acc.contains x then acc else x :: acc) []

def orbitsInLevel (q : Nat) : Nat :=
  (dedup ((level q).map orbitMin)).length

def orderCheck : Bool :=
  (iter K (1, 0) == (1, 0) && iter K (0, 1) == (0, 1)) &&
  ((List.range (K - 1)).all fun j => !(iter (j + 1) (1, 0) == (1, 0)))

theorem action_generator_exact_order : orderCheck = true := by
  decide +kernel

def nonzeroLevelsUniform : Bool :=
  (List.range (p - 1)).all fun i => (level (i + 1)).length == p - 1

theorem nonzero_level_cardinality : nonzeroLevelsUniform = true := by
  native_decide

theorem zero_cone_cardinality : (level 0).length = 2 * p - 2 := by
  decide +kernel

def nonzeroOrbitCountUniform : Bool :=
  (List.range (p - 1)).all fun i => orbitsInLevel (i + 1) == (p - 1) / K

theorem nonzero_level_orbit_count : nonzeroOrbitCountUniform = true := by
  native_decide

theorem global_count_identity :
    (p - 1) * ((p - 1) / K) + (2 * p - 2) / K = (p * p - 1) / K := by
  decide

def freeAction : Bool :=
  (List.range (p - 1)).all fun i =>
    (level (i + 1)).all fun x =>
      (List.range (K - 1)).all fun j => !(iter (j + 1) x == x)

theorem nonzero_level_action_free : freeAction = true := by
  native_decide

#print axioms nonzero_level_cardinality
#print axioms zero_cone_cardinality
#print axioms nonzero_level_orbit_count
#print axioms global_count_identity
#print axioms nonzero_level_action_free

#print axioms action_generator_exact_order
end Bgs.TorusLevelSets
