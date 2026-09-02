/-
  RUN 82 — machine-checked certificate for the COUNTING part of Theorem I
  (torus rigidity of the observable family), at the design prime p = 199.

  Theorem I says that the family V_n = P_+(T(n)+T(-n))P_+ depends on n only
  through the invariant quadratic form Q(n) = n_1^2 - n_1 n_2 - n_2^2 mod p,
  because the Hecke torus T (the centraliser of A in SL_2(Z/p)) acts
  transitively on each level set of Q.  The analytic half of the proof (the
  Weil intertwining property U_g T(n) U_g^* = T(gn)) is not formalised here.
  The COMBINATORIAL half is, and it is exactly what the transitivity claim
  reduces to for a fixed prime:

    C1  every nonzero level set of Q has exactly p - 1 points  (split case),
        and the cone {Q = 0} \ {0} has 2p - 2 points;
    C2  a nonzero level set splits into exactly |T|/K = (p-1)/K = m
        orbits of the cyclic group <A^T>;
    C0  ord(A^T) = K = 11 mod 199   (so the numbers in C2 are the right ones).

  These are decidable statements about a finite set, so they are settled by
  evaluation.  The evaluation is done by the compiler (`native_decide`), which
  adds `Lean.ofReduceBool` to the axiom set — see `#print axioms` at the end,
  and the disclosure in LEDGER RUN 82.  Kernel-only `decide` is not used
  because the search space (198 level sets x 39601 vectors) is far beyond
  kernel reduction.

  Lean 4.33.1, no Mathlib.  Build: `cd formal && lake build`.
-/

namespace Bgs

/-- the design prime -/
def p : Nat := 199

/-- the order of A mod p (certified by `ordA_eq` below) -/
def K : Nat := 11

/-- Q(n) = n₁² - n₁n₂ - n₂² mod p, written with `p - 1` for `-1`. -/
def Q (a b : Nat) : Nat := (a * a + (p - 1) * a * b + (p - 1) * b * b) % p

/-- all nonzero vectors of (Z/p)² -/
def vectors : List (Nat × Nat) :=
  ((List.range p).flatMap fun a => (List.range p).map fun b => (a, b)).filter
    fun x => !(x.1 == 0 && x.2 == 0)

/-- the level set of `q` -/
def level (q : Nat) : List (Nat × Nat) :=
  vectors.filter fun x => Q x.1 x.2 == q

/-- the action of A^T = [[2,1],[1,1]] on (Z/p)² -/
def step (x : Nat × Nat) : Nat × Nat := ((2 * x.1 + x.2) % p, (x.1 + x.2) % p)

def iter (n : Nat) (x : Nat × Nat) : Nat × Nat :=
  match n with
  | 0 => x
  | n + 1 => iter n (step x)

/-- lexicographic minimum of the `<A^T>`-orbit: a canonical orbit label -/
def orbitMin (x : Nat × Nat) : Nat × Nat :=
  let rec go : Nat → Nat × Nat → Nat × Nat → Nat × Nat
    | 0, _, best => best
    | n + 1, cur, best =>
      let nxt := step cur
      let better := if nxt.1 < best.1 || (nxt.1 == best.1 && nxt.2 < best.2)
                    then nxt else best
      go n nxt better
  go K x x

def dedup (l : List (Nat × Nat)) : List (Nat × Nat) :=
  l.foldl (fun acc x => if acc.contains x then acc else x :: acc) []

def orbitsInLevel (q : Nat) : Nat := (dedup ((level q).map orbitMin)).length

/-- C0: the order of A^T mod p is exactly K = 11. -/
def ordACheck : Bool :=
  (iter K (1, 0) == (1, 0) && iter K (0, 1) == (0, 1)) &&
  ((List.range (K - 1)).all fun j => !(iter (j + 1) (1, 0) == (1, 0)))

theorem ordA_eq : ordACheck = true := by native_decide

/-- C1a: every nonzero level set has exactly `p - 1` points. -/
def levelsUniform : Bool :=
  (List.range (p - 1)).all fun i => (level (i + 1)).length == p - 1

theorem C1a_levels_uniform : levelsUniform = true := by native_decide

/-- C1b: the cone has `2p - 2` points. -/
theorem C1b_cone : (level 0).length = 2 * p - 2 := by native_decide

/-- C2: each nonzero level set carries exactly `(p-1)/K = 18` orbits. -/
def orbitsUniform : Bool :=
  (List.range (p - 1)).all fun i => orbitsInLevel (i + 1) == (p - 1) / K

theorem C2_orbits_uniform : orbitsUniform = true := by native_decide

/-- The global bookkeeping identity of Theorem I(c) at this prime:
    (#nonzero level sets)·(orbits per level set) + (cone points)/K
      = (p² - 1)/K. -/
theorem C3_global_count :
    (p - 1) * ((p - 1) / K) + (2 * p - 2) / K = (p * p - 1) / K := by
  decide

/-- Every point of a nonzero level set has full orbit length K (the action of
    `<A^T>` on the level set is free) — the last ingredient of C2. -/
def freeAction : Bool :=
  (List.range (p - 1)).all fun i =>
    (level (i + 1)).all fun x =>
      (List.range (K - 1)).all fun j => !(iter (j + 1) x == x)

theorem C4_free_action : freeAction = true := by native_decide

#print axioms C1a_levels_uniform
#print axioms C2_orbits_uniform
#print axioms C3_global_count
#print axioms C4_free_action

end Bgs
