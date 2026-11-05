import Mathlib.NumberTheory.LegendreSymbol.QuadraticReciprocity
import Mathlib.FieldTheory.Finite.Basic
import Mathlib.GroupTheory.OrderOfElement
import Bgs.H6LemmaW

/-! H5 structural-ceiling arithmetic (BGS-TRACE-348, 349, 350): general proofs, for every odd prime p.
No sorry, no native_decide.

Convention (BGS-TRACE-342, `Bgs.H6LemmaW`): ε = 1 + √2, ε^n = a_n + b_n √2, so a_n = (ε^n + ε̄^n)/2 = h_n
(`a_eq_h6`: a_n equals `Bgs.H6LemmaW.h n` for every n).  The proofs work in `ZMod q` with a square root s of 2,
e = 1 + s the image of ε, and use only a_n^2 - 2 b_n^2 = (-1)^n and e^n = a_n + b_n s.

* `prime_dvd_mod8`   : n odd, q prime, q ∣ h_n  ⟹  q % 8 = 1 ∨ q % 8 = 7.
* `prime_dvd_mod2p`  : p odd prime, q prime, q ∣ h_p  ⟹  q % (2p) = 1   (sharpens Lemma W, BGS-TRACE-342).
* `coprime_h`        : p ≠ p' odd primes  ⟹  gcd(h_p, h_p') = 1.
* `sg_dvd`           : n % 4 = 3 and 2n+1 prime  ⟹  (2n+1) ∣ h_n   (n need not be prime).
* `sg_iff`           : n odd, 2n+1 prime: (2n+1) ∣ h_n ↔ n % 4 = 3.
* `sg_minFac`        : p odd prime, p % 4 = 3, 2p+1 prime ⟹ minFac(h_p) = 2p+1, and 2p+1 < h_p for p ≥ 5.
The product formula h_p = ∏ (6 - 2 cos(2πk/p)) (BGS-TRACE-351) is NOT formalized here. -/
namespace Bgs.H5CeilingArith

/-- (a_n, b_n) with ε^n = a_n + b_n √2, ε = 1 + √2. -/
def ab : ℕ → ℤ × ℤ
  | 0 => (1, 0)
  | n + 1 => ((ab n).1 + 2 * (ab n).2, (ab n).1 + (ab n).2)

/-- a_n = h_n = (ε^n + ε̄^n)/2. -/
def a (n : ℕ) : ℤ := (ab n).1
/-- b_n, the √2-coefficient of ε^n. -/
def b (n : ℕ) : ℤ := (ab n).2

@[simp] lemma a_zero : a 0 = 1 := rfl
@[simp] lemma b_zero : b 0 = 0 := rfl
lemma a_succ (n : ℕ) : a (n + 1) = a n + 2 * b n := rfl
lemma b_succ (n : ℕ) : b (n + 1) = a n + b n := rfl

/-- The two-step recurrence a_{n+2} = 2 a_{n+1} + a_n. -/
lemma a_rec (n : ℕ) : a (n + 2) = 2 * a (n + 1) + a n := by
  rw [a_succ (n + 1), b_succ, a_succ]; ring

/-- Agreement with the repository convention `Bgs.H6LemmaW.h` (h_0 = h_1 = 1, h_{n+2} = 2 h_{n+1} + h_n). -/
theorem a_eq_h6 (n : ℕ) : a n = (Bgs.H6LemmaW.h n : ℤ) := by
  have key : ∀ n, a n = (Bgs.H6LemmaW.h n : ℤ) ∧ a (n + 1) = (Bgs.H6LemmaW.h (n + 1) : ℤ) := by
    intro n
    induction n with
    | zero => exact ⟨rfl, rfl⟩
    | succ k ih =>
      refine ⟨ih.2, ?_⟩
      have hh : Bgs.H6LemmaW.h (k + 2) = 2 * Bgs.H6LemmaW.h (k + 1) + Bgs.H6LemmaW.h k := rfl
      rw [a_rec, hh, ih.1, ih.2]; push_cast; ring
  exact (key n).1

/-- Pell norm: a_n^2 - 2 b_n^2 = (-1)^n. -/
theorem norm_ab (n : ℕ) : a n ^ 2 - 2 * b n ^ 2 = (-1) ^ n := by
  induction n with
  | zero => simp
  | succ k ih => rw [a_succ, b_succ, pow_succ]; linear_combination (-1 : ℤ) * ih

/-- h_n is odd. -/
theorem a_odd (n : ℕ) : Odd (a n) := by
  induction n with
  | zero => exact odd_one
  | succ k ih => rw [a_succ]; exact ih.add_even (even_two_mul _)

lemma norm_odd {n : ℕ} (hn : Odd n) : a n ^ 2 - 2 * b n ^ 2 = -1 := by
  rw [norm_ab, hn.neg_one_pow]

section ZModq
variable {q : ℕ} [Fact q.Prime]

/-- In `ZMod q`, with s^2 = 2: (1 + s)^n = a_n + b_n s. -/
lemma e_pow (s : ZMod q) (hs : s ^ 2 = 2) (n : ℕ) : (1 + s) ^ n = (a n : ZMod q) + (b n : ZMod q) * s := by
  induction n with
  | zero => simp
  | succ k ih =>
    rw [pow_succ, ih, a_succ, b_succ]; push_cast; linear_combination ((b k : ZMod q)) * hs

lemma q_ne_two {n : ℕ} (hq : (q : ℤ) ∣ a n) : q ≠ 2 := by
  rintro rfl
  obtain ⟨k, hk⟩ := a_odd n
  obtain ⟨m, hm⟩ := hq
  omega

lemma two_ne_zero' (hq2 : q ≠ 2) : (2 : ZMod q) ≠ 0 := by
  intro h
  have : ((2 : ℕ) : ZMod q) = 0 := by exact_mod_cast h
  rw [ZMod.natCast_eq_zero_iff] at this
  have hp := (Fact.out : q.Prime)
  have := (Nat.prime_dvd_prime_iff_eq hp Nat.prime_two).1 this
  exact hq2 this

lemma one_add_ne_zero (s : ZMod q) (hs : s ^ 2 = 2) : (1 + s) ≠ 0 := by
  intro h
  have : (1 + s) * (1 - s) = -1 := by linear_combination (-1 : ZMod q) * hs
  rw [h, zero_mul] at this
  exact one_ne_zero (neg_eq_zero.1 this.symm)

/-- If q ∣ h_n with n odd, then 2 b_n^2 = 1 in `ZMod q` and s = 2 b_n is a square root of 2. -/
lemma sqrt_two_of_dvd {n : ℕ} (hn : Odd n) (hq : (q : ℤ) ∣ a n) :
    (2 : ZMod q) * (b n : ZMod q) ^ 2 = 1 ∧ (2 * (b n : ZMod q)) ^ 2 = 2 := by
  have ha : (a n : ZMod q) = 0 := (ZMod.intCast_zmod_eq_zero_iff_dvd _ _).2 hq
  have hN : ((a n ^ 2 - 2 * b n ^ 2 : ℤ) : ZMod q) = ((-1 : ℤ) : ZMod q) := by rw [norm_odd hn]
  push_cast at hN
  rw [ha] at hN
  have h1 : (2 : ZMod q) * (b n : ZMod q) ^ 2 = 1 := by linear_combination (-1 : ZMod q) * hN
  exact ⟨h1, by linear_combination (2 : ZMod q) * h1⟩

/-- TRACE-348 (mod 8 part): n odd, q prime, q ∣ h_n ⟹ q ≡ ±1 (mod 8). -/
theorem prime_dvd_mod8 {n : ℕ} (hn : Odd n) (hq : (q : ℤ) ∣ a n) : q % 8 = 1 ∨ q % 8 = 7 := by
  have hq2 := q_ne_two hq
  refine (ZMod.exists_sq_eq_two_iff hq2).1 ?_
  obtain ⟨-, h2⟩ := sqrt_two_of_dvd hn hq
  exact ⟨2 * (b n : ZMod q), by rw [← sq]; exact h2.symm⟩

/-- For any square root s of 2 in `ZMod q` and q ∣ h_p (p odd prime): λ = (1 + s)^2 has order exactly p. -/
theorem orderOf_lambda {p : ℕ} [hp : Fact p.Prime] (hp2 : p ≠ 2) (hq : (q : ℤ) ∣ a p)
    (s : ZMod q) (hs : s ^ 2 = 2) : orderOf ((1 + s) ^ 2) = p := by
  have hpo : Odd p := hp.out.odd_of_ne_two hp2
  have hq2 := q_ne_two hq
  obtain ⟨h1, -⟩ := sqrt_two_of_dvd hpo hq
  have ha : (a p : ZMod q) = 0 := (ZMod.intCast_zmod_eq_zero_iff_dvd _ _).2 hq
  apply orderOf_eq_prime
  · rw [← pow_mul, mul_comm, pow_mul, e_pow s hs, ha, zero_add, mul_pow, hs]
    linear_combination h1
  · intro h
    have h' : (2 : ZMod q) * (1 + s) = 0 := by linear_combination h - hs
    rcases mul_eq_zero.1 h' with h0 | h0
    · exact two_ne_zero' hq2 h0
    · exact one_add_ne_zero s hs h0

/-- TRACE-348 (mod 2p part, sharpened Lemma W): p odd prime, q prime, q ∣ h_p ⟹ q ≡ 1 (mod 2p). -/
theorem prime_dvd_mod2p {p : ℕ} [hp : Fact p.Prime] (hp2 : p ≠ 2) (hq : (q : ℤ) ∣ a p) :
    q % (2 * p) = 1 := by
  have hpo : Odd p := hp.out.odd_of_ne_two hp2
  have hq2 := q_ne_two hq
  obtain ⟨-, hs⟩ := sqrt_two_of_dvd hpo hq
  set s : ZMod q := 2 * (b p : ZMod q)
  have hord := orderOf_lambda hp2 hq s hs
  have hne : ((1 + s) ^ 2) ≠ 0 := pow_ne_zero _ (one_add_ne_zero s hs)
  have hdvd : p ∣ q - 1 := hord ▸ orderOf_dvd_of_pow_eq_one (ZMod.pow_card_sub_one_eq_one hne)
  have hqo : Odd q := (Fact.out : q.Prime).odd_of_ne_two hq2
  have h2 : 2 ∣ q - 1 := by obtain ⟨k, hk⟩ := hqo; omega
  have hcop : Nat.Coprime 2 p := (Nat.coprime_two_left).2 hpo
  have h2p : 2 * p ∣ q - 1 := hcop.mul_dvd_of_dvd_of_dvd h2 hdvd
  have hq1 : 1 ≤ q := (Fact.out : q.Prime).one_lt.le
  have hp3 : 3 ≤ p := by have := hp.out.two_le; omega
  have hm := (Nat.modEq_iff_dvd' hq1).2 h2p
  unfold Nat.ModEq at hm
  rw [← hm, Nat.mod_eq_of_lt (by omega)]

end ZModq

/-- TRACE-349: h_p and h_p' are coprime for distinct odd primes p, p'. -/
theorem coprime_h {p p' : ℕ} (hp : p.Prime) (hp' : p'.Prime) (hp2 : p ≠ 2) (hp2' : p' ≠ 2) (hne : p ≠ p') :
    Int.gcd (a p) (a p') = 1 := by
  by_contra hg
  obtain ⟨q, hqp, hqd⟩ := Nat.exists_prime_and_dvd hg
  have : Fact q.Prime := ⟨hqp⟩
  have : Fact p.Prime := ⟨hp⟩
  have : Fact p'.Prime := ⟨hp'⟩
  have hq1 : (q : ℤ) ∣ a p := (Int.natCast_dvd_natCast.2 hqd).trans (Int.gcd_dvd_left _ _)
  have hq2 : (q : ℤ) ∣ a p' := (Int.natCast_dvd_natCast.2 hqd).trans (Int.gcd_dvd_right _ _)
  obtain ⟨-, hs⟩ := sqrt_two_of_dvd (hp.odd_of_ne_two hp2) hq1
  have e1 := orderOf_lambda hp2 hq1 _ hs
  have e2 := orderOf_lambda hp2' hq2 _ hs
  exact hne (e1.symm.trans e2)

/-- TRACE-350: n % 4 = 3 and q = 2n + 1 prime ⟹ q ∣ h_n (n need not be prime). -/
theorem sg_dvd {n : ℕ} (hn : n % 4 = 3) (hq : (2 * n + 1).Prime) : ((2 * n + 1 : ℕ) : ℤ) ∣ a n := by
  set q := 2 * n + 1 with hqdef
  have : Fact q.Prime := ⟨hq⟩
  have hq2 : q ≠ 2 := by omega
  have h8 : q % 8 = 7 := by omega
  obtain ⟨s, hs'⟩ := (ZMod.exists_sq_eq_two_iff hq2).2 (Or.inr h8)
  have hs : s ^ 2 = 2 := by rw [hs']; ring
  have hno : Odd n := by refine ⟨n / 2, ?_⟩; omega
  have he0 := one_add_ne_zero s hs
  have hF : (1 + s) ^ (2 * n) = 1 := by
    have := ZMod.pow_card_sub_one_eq_one he0
    rwa [show q - 1 = 2 * n by omega] at this
  have hN : ((a n ^ 2 - 2 * b n ^ 2 : ℤ) : ZMod q) = ((-1 : ℤ) : ZMod q) := by rw [norm_odd hno]
  push_cast at hN
  have hE := e_pow s hs n
  -- e^{2n} - 1 = 2 a_n e^n
  have hid : (1 + s) ^ (2 * n) - 1 = 2 * (a n : ZMod q) * (1 + s) ^ n := by
    rw [pow_mul', hE]
    linear_combination ((b n : ZMod q)) ^ 2 * hs - hN
  rw [hF, sub_self] at hid
  have h0 : (2 : ZMod q) * (a n : ZMod q) * (1 + s) ^ n = 0 := hid.symm
  rcases mul_eq_zero.1 h0 with h0 | h0
  · rcases mul_eq_zero.1 h0 with h0 | h0
    · exact absurd h0 (two_ne_zero' hq2)
    · exact (ZMod.intCast_zmod_eq_zero_iff_dvd _ _).1 h0
  · exact absurd h0 (pow_ne_zero _ he0)

/-- TRACE-350 converse: for odd n and prime 2n + 1, (2n+1) ∣ h_n ↔ n % 4 = 3. -/
theorem sg_iff {n : ℕ} (hn : Odd n) (hq : (2 * n + 1).Prime) :
    ((2 * n + 1 : ℕ) : ℤ) ∣ a n ↔ n % 4 = 3 := by
  constructor
  · intro hd
    have : Fact (2 * n + 1).Prime := ⟨hq⟩
    have h8 := prime_dvd_mod8 hn hd
    obtain ⟨k, hk⟩ := hn
    omega
  · intro h; exact sg_dvd h hq

lemma a_pos (n : ℕ) : 1 ≤ a n ∧ 0 ≤ b n := by
  induction n with
  | zero => simp
  | succ k ih => rw [a_succ, b_succ]; constructor <;> linarith [ih.1, ih.2]

lemma a_ge_pow (n : ℕ) : (2 : ℤ) ^ n ≤ a (n + 1) := by
  have key : ∀ n, (2 : ℤ) ^ n ≤ a (n + 1) ∧ (2 : ℤ) ^ (n + 1) ≤ a (n + 2) := by
    intro n
    induction n with
    | zero => exact ⟨by decide, by decide⟩
    | succ k ih =>
      refine ⟨ih.2, ?_⟩
      rw [a_rec (k + 1), pow_succ]
      linarith [ih.2, (a_pos (k + 1)).1]
  exact (key n).1

/-- TRACE-350: on the family, the least prime factor of h_p is exactly 2p + 1, and h_p is composite for p ≥ 5. -/
theorem sg_minFac {p : ℕ} (hp : p.Prime) (h4 : p % 4 = 3) (hq : (2 * p + 1).Prime) :
    Nat.minFac (a p).natAbs = 2 * p + 1 ∧ (5 ≤ p → 2 * p + 1 < (a p).natAbs) := by
  have : Fact p.Prime := ⟨hp⟩
  have hp2 : p ≠ 2 := by omega
  have hd := sg_dvd h4 hq
  have hdn : (2 * p + 1) ∣ (a p).natAbs := Int.natCast_dvd.1 hd
  have hpos := (a_pos p).1
  have hlarge : 2 * p + 1 ≤ (a p).natAbs := Nat.le_of_dvd (by omega) hdn
  have hne1 : (a p).natAbs ≠ 1 := by omega
  refine ⟨le_antisymm (Nat.minFac_le_of_dvd (by omega) hdn) ?_, ?_⟩
  · have hmp := Nat.minFac_prime hne1
    have : Fact (Nat.minFac (a p).natAbs).Prime := ⟨hmp⟩
    have hmd : ((Nat.minFac (a p).natAbs : ℕ) : ℤ) ∣ a p :=
      Int.natCast_dvd.2 (Nat.minFac_dvd _)
    have hmod := prime_dvd_mod2p hp2 hmd
    have h1 := hmp.one_lt
    have hd' : 2 * p ∣ Nat.minFac (a p).natAbs - 1 := by
      have := (Nat.dvd_sub_mod (Nat.minFac (a p).natAbs) : 2 * p ∣ _ - _ % (2 * p))
      rwa [hmod] at this
    have := Nat.le_of_dvd (by omega) hd'
    omega
  · intro h5
    obtain ⟨k, rfl⟩ : ∃ k, p = k + 5 := ⟨p - 5, by omega⟩
    have hg := a_ge_pow (k + 4)
    have hk : (k : ℤ) < 2 ^ k := by exact_mod_cast Nat.lt_two_pow_self
    have h16 : (2 : ℤ) ^ (k + 4) = 16 * 2 ^ k := by ring
    rw [show k + 4 + 1 = k + 5 by ring] at hg
    have : (2 * (k + 5) + 1 : ℤ) < a (k + 5) := by linarith
    omega

end Bgs.H5CeilingArith

#print axioms Bgs.H5CeilingArith.a_eq_h6
#print axioms Bgs.H5CeilingArith.norm_ab
#print axioms Bgs.H5CeilingArith.prime_dvd_mod8
#print axioms Bgs.H5CeilingArith.orderOf_lambda
#print axioms Bgs.H5CeilingArith.prime_dvd_mod2p
#print axioms Bgs.H5CeilingArith.coprime_h
#print axioms Bgs.H5CeilingArith.sg_dvd
#print axioms Bgs.H5CeilingArith.sg_iff
#print axioms Bgs.H5CeilingArith.sg_minFac
