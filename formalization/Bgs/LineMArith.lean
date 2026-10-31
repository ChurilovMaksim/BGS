import Bgs.LineIArith
/-! Line M arithmetic (BGS-TRACE-269.., `mathematics/fixed-map/lineMN_conductor_structure.md`).
Referee file `computations/verification/lineM/referee/lean/LineMArith.lean` (sha256 a846ea30…), integrated with the namespace
`Bgs.LineMRef` renamed to `Bgs.LineM` and all `#print axioms` lines moved to the end. No sorry, no native_decide. -/
namespace Bgs.LineM
open Bgs.LineIArith Bgs.LineG

/-- 3 ∤ h_m for odd m (M4 input): from the Pell identity h² − 2U² = −1. -/
theorem three_not_dvd_nsw {m : ℕ} (hm : Odd m) : ¬ ((3 : ℤ) ∣ nsw m) := by
  intro h3
  have hp := pell m
  rw [hm.neg_one_pow] at hp
  obtain ⟨k, hk⟩ := h3
  have hz : ((nsw m ^ 2 - 2 * lucasU m ^ 2 : ℤ) : ZMod 3) = ((-1 : ℤ) : ZMod 3) := by rw [hp]
  rw [hk] at hz
  push_cast at hz
  have h33 : ((3 : ℤ) : ZMod 3) = 0 := by decide
  push_cast at h33
  rw [h33] at hz
  generalize (lucasU m : ZMod 3) = u at hz
  generalize (k : ZMod 3) = v at hz
  revert u v; decide

/-- Pell pair recurrence on ℕ: (x, y) ↦ (x + 2y, x + y), starting at (1, 0). -/
def pp : ℕ → ℕ × ℕ
  | 0 => (1, 0)
  | n + 1 => ((pp n).1 + 2 * (pp n).2, (pp n).1 + (pp n).2)

theorem pp_eq (n : ℕ) : ((pp n).1 : ℤ) = nsw n ∧ ((pp n).2 : ℤ) = lucasU n := by
  induction n with
  | zero => constructor <;> decide
  | succ n ih =>
    obtain ⟨h1, h2⟩ := ih
    simp only [pp, nsw_eq, lucasU, pow_succ] at *
    constructor
    · push_cast; rw [h1, h2]; simp [α]
    · push_cast; rw [h1, h2]; simp [α]

/-- M1 (strong divisibility), finite range: odd m, n < 60, kernel `decide`. -/
theorem strong_div_small :
    ∀ m < 60, ∀ n < 60, m % 2 = 1 → n % 2 = 1 →
      Nat.gcd (pp m).1 (pp n).1 = (pp (Nat.gcd m n)).1 := by
  decide +kernel

/-- 3 ∤ h_m for odd m < 200, finite range (redundant with `three_not_dvd_nsw`). -/
theorem three_small : ∀ m < 200, m % 2 = 1 → (pp m).1 % 3 ≠ 0 := by decide +kernel

/-- h_{3n} = h_n (4 h_n² + 3) for odd n, finite range. -/
theorem triple_small : ∀ n < 100, n % 2 = 1 → (pp (3*n)).1 = (pp n).1 * (4 * (pp n).1 ^ 2 + 3) := by
  decide +kernel

/-- h_{3n} = h_n (4 h_n² + 3) for every odd n (general, from Pell). -/
theorem nsw_three_mul {n : ℕ} (hn : Odd n) : nsw (3 * n) = nsw n * (4 * nsw n ^ 2 + 3) := by
  have hp := pell n
  rw [hn.neg_one_pow] at hp
  have e : nsw (3 * n) = nsw n ^ 3 + 6 * nsw n * lucasU n ^ 2 := by
    simp only [nsw_eq, lucasU, mul_comm 3 n, pow_mul]
    generalize α ^ n = z
    simp [pow_succ, pow_zero]; ring
  rw [e]; linear_combination (-3 * nsw n) * hp

/-- M4 family-disjointness core: if A, B ∣ h, gcd(A,B) ∣ 3 and 3 ∤ h then A*B ∣ h. -/
theorem coprime_core {A B h : ℕ} (hA : A ∣ h) (hB : B ∣ h) (hg : Nat.gcd A B ∣ 3) (h3 : ¬ 3 ∣ h) :
    A * B ∣ h := by
  have hcop : Nat.Coprime A B := by
    rcases (Nat.dvd_prime (by norm_num : Nat.Prime 3)).1 hg with h1 | h1
    · exact h1
    · exact absurd (h1 ▸ (Nat.gcd_dvd_left A B).trans hA) h3
  exact hcop.mul_dvd_of_dvd_of_dvd hA hB

/-- M7 input: for odd p, λ^p = (1+√2)^{2p} = 1 + 2 h_p (1+√2)^p in ℤ[√2]; hence λ^p ≡ 1 mod 2h_p. -/
theorem lam_pow_eq {p : ℕ} (hp : Odd p) :
    α ^ (2 * p) = 1 + (2 * nsw p : ℤ√2) * α ^ p := by
  have hP := pell p
  rw [hp.neg_one_pow] at hP
  rw [mul_comm 2 p, pow_mul]
  have hx : nsw p = (α ^ p).re := rfl
  have hy : lucasU p = (α ^ p).im := rfl
  rw [hx, hy] at hP
  rw [hx]
  generalize α ^ p = z at hP ⊢
  ext <;> simp [pow_two] <;> first | linear_combination -hP | linear_combination (0 : ℤ) * hP

end Bgs.LineM

#print axioms Bgs.LineM.three_not_dvd_nsw
#print axioms Bgs.LineM.pp_eq
#print axioms Bgs.LineM.strong_div_small
#print axioms Bgs.LineM.three_small
#print axioms Bgs.LineM.triple_small
#print axioms Bgs.LineM.nsw_three_mul
#print axioms Bgs.LineM.coprime_core
#print axioms Bgs.LineM.lam_pow_eq
