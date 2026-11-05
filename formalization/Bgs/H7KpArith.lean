/-! H7* scope integration (BGS-TRACE-344, 345): finite kernel checks of the K_p arithmetic.
No sorry, no native_decide; every theorem is `decide +kernel`; core Lean only (no Mathlib import).
u_0 = 1, u_1 = 7, u_{n+2} = 6 u_{n+1} - u_n; h_p = u_{(p-1)/2}; K_p = 4 h_p^2 + 3; h_{3p} = u_{(3p-1)/2} = h_p K_p.
* `seven_dvd_K`: for every prime 5 ≤ p < 200: 7 ∣ K_p, 7 ∤ h_p, 3 ∤ h_p, gcd(h_p, K_p) = 1 and u_{(3p-1)/2} = h_p K_p.
* `K_factorisations`: K_p for p = 5, 7, 11, 13, 17, 19, 23, 29, 31 equals the product of the listed prime powers;
  every listed factor is ≡ 1 (mod 3) and every listed factor other than 7 is ≡ 1 (mod 6p). Primality of the
  factors is NOT checked here (BPSW / trial division in computations/verification/h7_scope/code/kp_arith.py, h7h8.py).
* `crossings`: d = 3437426497, 24061985479 ∣ K_19 and d = 2735635252619983 ∣ K_29, gcd(d, h_p) = 1,
  ⌊h_{3p}/d²⌋ = 278, 5, 133, and λ = 3 + 2√2 has order 3p mod d (λ^{3p} ≡ 1, λ^3 ≢ 1, λ^p ≢ 1).
* `d4663`: 4663 ∣ K_7 = 228487, 4663² ≤ h_21, and λ has order 21 mod 4663.
Finite statements only; the general Lemmas 3 and 4 are paper proofs [P] (BGS-TRACE-344). -/
namespace Bgs.H7KpArith

/-- (u_n, u_{n+1}) with u_0 = 1, u_1 = 7, u_{n+2} = 6 u_{n+1} - u_n. -/
def upair : Nat → Nat × Nat
  | 0 => (1, 7)
  | n + 1 => let x := upair n; (x.2, 6 * x.2 - x.1)

def u (n : Nat) : Nat := (upair n).1
def hp (p : Nat) : Nat := u ((p - 1) / 2)
def K (p : Nat) : Nat := 4 * hp p ^ 2 + 3

/-- λ^n = x + y √2 mod d, λ = 3 + 2√2, as the pair (x, y). -/
def lamPow (d : Nat) : Nat → Nat × Nat
  | 0 => (1 % d, 0)
  | n + 1 => let r := lamPow d n; ((3 * r.1 + 4 * r.2) % d, (2 * r.1 + 3 * r.2) % d)

def orderIs3p (d p : Nat) : Bool :=
  lamPow d (3 * p) == (1 % d, 0) && lamPow d 3 != (1 % d, 0) && lamPow d p != (1 % d, 0)

/-- The primes 5 ≤ p < 200. -/
def primes5to199 : List Nat :=
  [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
   113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

theorem h_small :
    hp 5 = 41 ∧ hp 7 = 239 ∧ hp 19 = 9369319 ∧ hp 29 = 63018038201 ∧ K 3 = 199 ∧ K 3 % 7 = 3 := by
  decide +kernel

theorem seven_dvd_K :
    (primes5to199.all fun p => K p % 7 == 0 && hp p % 7 != 0 && hp p % 3 != 0 &&
      Nat.gcd (hp p) (K p) == 1 && u ((3 * p - 1) / 2) == hp p * K p) = true := by
  decide +kernel

theorem seven_dvd_K_5 : 7 ∣ K 5 := by decide +kernel
theorem seven_dvd_K_31 : 7 ∣ K 31 := by decide +kernel

/-- (p, [(q, e)]) : K_p = ∏ q^e. -/
def facts : List (Nat × List (Nat × Nat)) :=
  [(5, [(7, 1), (31, 2)]), (7, [(7, 2), (4663, 1)]), (11, [(7, 1), (37667521, 1)]),
   (13, [(7, 1), (313, 1), (4088137, 1)]), (17, [(7, 1), (409, 1), (3610372009, 1)]),
   (19, [(7, 1), (457, 1), (14593, 1), (7521721, 1)]), (23, [(7, 1), (57887325592525441, 1)]),
   (29, [(7, 1), (13921, 1), (5806729, 1), (28073057689, 1)]),
   (31, [(7, 1), (2643247, 1), (7159513, 1), (4073551591, 1)])]

def prodPow : List (Nat × Nat) → Nat
  | [] => 1
  | (q, e) :: t => q ^ e * prodPow t

def factOK (pf : Nat × List (Nat × Nat)) : Bool :=
  K pf.1 == prodPow pf.2 &&
    pf.2.all fun qe => qe.1 % 3 == 1 && (qe.1 == 7 || (qe.1 - 1) % (6 * pf.1) == 0)

theorem K_factorisations : facts.all factOK = true := by
  decide +kernel

theorem crossings :
    (K 19 % 3437426497 == 0 && K 19 % 24061985479 == 0 && K 29 % 2735635252619983 == 0 &&
      Nat.gcd 3437426497 (hp 19) == 1 && Nat.gcd 24061985479 (hp 19) == 1 &&
      Nat.gcd 2735635252619983 (hp 29) == 1 &&
      hp 19 * K 19 / 3437426497 ^ 2 == 278 && hp 19 * K 19 / 24061985479 ^ 2 == 5 &&
      hp 29 * K 29 / 2735635252619983 ^ 2 == 133 &&
      orderIs3p 3437426497 19 && orderIs3p 24061985479 19 && orderIs3p 2735635252619983 29) = true := by
  decide +kernel

theorem d4663 :
    (K 7 == 228487 && K 7 % 4663 == 0 && Nat.ble (4663 ^ 2) (hp 7 * K 7) && u 10 == hp 7 * K 7 &&
      orderIs3p 4663 7) = true := by
  decide +kernel

end Bgs.H7KpArith

#print axioms Bgs.H7KpArith.h_small
#print axioms Bgs.H7KpArith.seven_dvd_K
#print axioms Bgs.H7KpArith.seven_dvd_K_5
#print axioms Bgs.H7KpArith.seven_dvd_K_31
#print axioms Bgs.H7KpArith.K_factorisations
#print axioms Bgs.H7KpArith.crossings
#print axioms Bgs.H7KpArith.d4663
