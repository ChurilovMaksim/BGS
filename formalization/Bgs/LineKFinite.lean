/-!
# Line K — finite checks for Lemma K3 and Theorem K3 (BGS-TRACE-234, 235)

Adapted from the author's core-Lean files `computations/verification/lineK/lean/K3Finite.lean` and `K3Gaps.lean`
(definitions and statements unchanged; wrapped in a namespace). Core Lean only, no Mathlib import.
`decide` / `decide +kernel` only; no `native_decide`, no `sorry`.

* `noFrac_sound`, `no_small_denominator`, `exceptions_excluded`: no fraction a/b lies in the widened enclosure
  [0.88797590, 0.88797628] ⊇ the certified enclosure of arg ξ/2π (J3 `rat_excl`, outward rounded) for 1 ≤ b < 1339,
  nor for b ∈ {1512, 560, 1680, 616, 1848, 2520}.
* `sieve_enumeration`, `sieve_survivors`, `big_prime_excluded`: the finite part of the sieve step of Lemma K3(b)
  (subsets of {3, 5, 11, 13, 17, 19}; 9 survivors, all with 56(F+1)/A_low ≤ 2645; the ℓ = 23 inequality).
  The inclusion–exclusion inequality and the monotonicity step for ℓ > 23 are paper steps.
* `bprime_ge`: 3 ∣ b → 1339 ≤ b → 447 ≤ b / 3.
* `okRange`, `gaps_447`: Lemma K3(a) in the form "every non-exceptional b' has maximal cyclic gap ≤ b'/6 for every unit
  class", checked by kernel `decide +kernel` here only for 447 ≤ b' ≤ 466. The full range 447..2645 is checked by the
  62 chunk files in `computations/verification/lineK/lean/` (logs and rerun in `evidence/executions/20261031/lineK/`),
  which are NOT part of `lake build Bgs` (memory: 12 GB or more for a 100-modulus chunk).
* `sixth_lt_A`: 1/6 < 18001/100000. That 18001/100000 ≤ A = arccos(0.84431)/π is an arb bound [CA], not formalised.
Not formalised: the sieve inequality, the arb bound on A, CRT/Dirichlet/Vinogradov, and everything analytic.
-/

namespace Bgs.LineK
def Lo : Nat := 88797590
def Hi : Nat := 88797628
def D  : Nat := 100000000

/-- no integer a with Lo*b ≤ a*D ≤ Hi*b ; a := ceil(Lo*b/D) is the only candidate. -/
def noFrac (b : Nat) : Bool := Hi * b < ((Lo * b + D - 1) / D) * D

theorem noFrac_sound (b : Nat) (h : noFrac b = true) : ∀ a, ¬ (Lo * b ≤ a * D ∧ a * D ≤ Hi * b) := by
  intro a ⟨h1, h2⟩
  have h' : Hi * b < ((Lo * b + D - 1) / D) * D := of_decide_eq_true h
  have hD : 0 < D := by decide
  have hlt : (Lo * b + D - 1) / D < a + 1 := by
    rw [Nat.div_lt_iff_lt_mul hD]
    have : Lo * b + D - 1 < a * D + D := by omega
    simpa [Nat.add_mul, Nat.one_mul] using this
  have hc : (Lo * b + D - 1) / D ≤ a := Nat.lt_succ_iff.mp hlt
  have hm : ((Lo * b + D - 1) / D) * D ≤ a * D := Nat.mul_le_mul_right D hc
  omega

set_option maxRecDepth 200000

/-- (K3, rat_excl consistency) no fraction with denominator 1 ≤ b < 1339 lies in [Lo, Hi]. -/
theorem no_small_denominator : (List.range 1339).all (fun b => b == 0 || noFrac b) = true := by decide

/-- (K3 exceptions) the candidate denominators for b' ∈ {504,560,616,840}. -/
theorem exceptions_excluded : [1512, 560, 1680, 616, 1848, 2520].all noFrac = true := by decide

/-! Sieve enumeration (Lemma K3(b)). A_low = 18001/100000 ≤ A = arccos(0.84431)/pi (arb: 0.18001064843...).
For S ⊆ {3,5,11,13,17,19}: num = Π 2ℓ, den = Π (ℓ-1), R = Π ℓ; F = num/den.
"possible failure" :⇔ F + 1 ≥ A_low * R  ⇔ (num+den)*10^5 ≥ 18001*R*den.
Claim: every possible failure has 56*(F+1)/A_low ≤ 2645, i.e. 56*(num+den)*10^5 ≤ 2645*18001*den. -/
def subsetsOf : List Nat → List (List Nat)
  | [] => [[]]
  | x :: xs => let r := subsetsOf xs; r ++ r.map (x :: ·)

def num (S : List Nat) : Nat := S.foldl (fun acc l => acc * (2*l)) 1
def den (S : List Nat) : Nat := S.foldl (fun acc l => acc * (l-1)) 1
def rad (S : List Nat) : Nat := S.foldl (fun acc l => acc * l) 1
def possibleFail (S : List Nat) : Bool := 18001 * rad S * den S ≤ (num S + den S) * 100000
def bounded (S : List Nat) : Bool := 56 * (num S + den S) * 100000 ≤ 2645 * 18001 * den S

theorem sieve_enumeration :
    (subsetsOf [3,5,11,13,17,19]).all (fun S => !possibleFail S || bounded S) = true := by decide

/-- the surviving sets are exactly ∅,{3},{5},{11},{13},{17},{3,5},{3,11},{3,13}. -/
theorem sieve_survivors :
    ((subsetsOf [3,5,11,13,17,19]).filter possibleFail).length = 9 := by decide

/-- primes ℓ ≥ 23 are excluded: 2/(23-1) < A_low - 1/23  (then also for all ℓ ≥ 23, since the left side decreases
and R ≥ ℓ ≥ 23; the monotonicity step is by hand). -/
theorem big_prime_excluded : 2 * 23 * 100000 < (18001 * 23 - 100000) * 22 := by decide

/-- bookkeeping: b ≥ 1339 ⇒ b/gcd(3,b) ≥ 447. -/
theorem bprime_ge (b : Nat) (h3 : 3 ∣ b) (h : 1339 ≤ b) : 447 ≤ b / 3 := by omega

/-! ## Lemma K3(a): gap check (definitions of `K3Gaps.lean`) -/
set_option maxRecDepth 1000000

/-- state: (first, prev, maxgap, seen) -/
def scan (bp g r : Nat) : Nat × Nat × Nat × Bool :=
  (List.range bp).foldl (fun (st : Nat × Nat × Nat × Bool) v =>
    let (f, pv, mg, seen) := st
    if v % g == r && Nat.gcd v bp == 1 then
      if seen then (f, v, max mg (v - pv), true) else (v, v, 0, true)
    else st) (0, 0, 0, false)

def maxGap (bp g r : Nat) : Nat :=
  let (f, pv, mg, seen) := scan bp g r
  if seen then max mg (f + bp - pv) else bp

def okB (bp : Nat) : Bool :=
  let g := Nat.gcd 56 bp
  (List.range g).all (fun r => Nat.gcd r g != 1 || 6 * maxGap bp g r ≤ bp)

def exc (bp : Nat) : Bool := bp == 504 || bp == 560 || bp == 616 || bp == 840

def okRange (lo n : Nat) : Bool := (List.range n).all (fun i => exc (lo+i) || okB (lo+i))

theorem sixth_lt_A : 100000 < 6 * 18001 := by decide

/-- Lemma K3(a) on 447 ≤ b' ≤ 466 (the full range is checked outside `lake build Bgs`). -/
theorem gaps_447 : okRange 447 20 = true := by decide +kernel

end Bgs.LineK

#print axioms Bgs.LineK.noFrac_sound
#print axioms Bgs.LineK.no_small_denominator
#print axioms Bgs.LineK.exceptions_excluded
#print axioms Bgs.LineK.sieve_enumeration
#print axioms Bgs.LineK.sieve_survivors
#print axioms Bgs.LineK.big_prime_excluded
#print axioms Bgs.LineK.bprime_ge
#print axioms Bgs.LineK.sixth_lt_A
#print axioms Bgs.LineK.gaps_447
