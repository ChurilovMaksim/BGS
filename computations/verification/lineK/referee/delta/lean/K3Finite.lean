/-! Line K, Lemma K3: finite checks (core Lean 4, `decide` only, no `native_decide`, no Mathlib).
Enclosure of arg xi / 2pi (J3 rat_excl, outward rounded): [0.887975909832077, 0.8879762669871324] ⊂ [Lo, Hi] with
Lo = 88797590/10^8, Hi = 88797628/10^8 (widening is conservative for "no fraction a/b in the enclosure"). -/

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
theorem bprime_ge (b : Nat) (h : 1339 ≤ b) : 447 ≤ b / 3 ∨ 447 ≤ b := by omega

#print axioms no_small_denominator
#print axioms exceptions_excluded
#print axioms sieve_enumeration
#print axioms sieve_survivors
#print axioms noFrac_sound
