/-! Lemma W (BGS-TRACE-337), finite kernel check at small p. No sorry, no native_decide.
h_n = (ε^n + ε̄^n)/2 for ε = 1 + √2, via h_0 = h_1 = 1, h_{n+2} = 2 h_{n+1} + h_n.
Lemma W says every prime q ∣ h_p (p odd prime) satisfies q ≡ ±1 (mod 2p); since the classes ±1 are closed
under multiplication, every divisor d > 1 of h_p is then ≡ ±1 (mod 2p). The theorems below check this
divisor statement by `decide +kernel` for p = 3, 5, 7, 11, 13 (h_p = 7, 41, 239, 8119 = 23·353, 47321 = 79·599), and p ∤ h_p and
2 ∤ h_p for every odd prime p < 100. This is a finite check only; the general proof is the paper proof [P]. -/
namespace Bgs.H6LemmaW

/-- Pell-type pair (h_n, h_{n+1}). -/
def hpair : Nat → Nat × Nat
  | 0 => (1, 1)
  | n + 1 => let x := hpair n; (x.2, 2 * x.2 + x.1)

/-- h_n = (ε^n + ε̄^n)/2. -/
def h (n : Nat) : Nat := (hpair n).1

/-- Every divisor d > 1 of h_p is ≡ ±1 (mod 2p). -/
def divClassOK (p : Nat) : Bool :=
  (List.range (h p + 1)).all fun d => d ≤ 1 || h p % d != 0 || d % (2 * p) == 1 || d % (2 * p) == 2 * p - 1

theorem h_small : h 3 = 7 ∧ h 5 = 41 ∧ h 7 = 239 ∧ h 11 = 8119 ∧ h 13 = 47321 := by decide +kernel

theorem lemmaW_p3 : divClassOK 3 = true := by decide +kernel
theorem lemmaW_p5 : divClassOK 5 = true := by decide +kernel
theorem lemmaW_p7 : divClassOK 7 = true := by decide +kernel
theorem lemmaW_p11 : divClassOK 11 = true := by decide +kernel
theorem lemmaW_p13 : divClassOK 13 = true := by decide +kernel

/-- Odd primes p < 100. -/
def oddPrimes : List Nat := [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

/-- p ∤ h_p and h_p odd, for every odd prime p < 100. -/
theorem p_not_dvd_h : (oddPrimes.all fun p => h p % p != 0 && h p % 2 == 1) = true := by decide +kernel

#print axioms h_small
#print axioms lemmaW_p3
#print axioms lemmaW_p5
#print axioms lemmaW_p7
#print axioms lemmaW_p11
#print axioms lemmaW_p13
#print axioms p_not_dvd_h
end Bgs.H6LemmaW
