import Mathlib
import Bgs.LineG

/-!
# Line I — arithmetic of h_m used by the Line I claims (BGS-TRACE-212, 215, 219)

Notation: α = 1 + √2 ∈ ℤ[√2], h_m = `Bgs.LineG.nsw m` = Re α^m, and U_m = `lucasU m` = Im α^m
(so U_m = (α^m − β^m)/(α − β) is the Lucas sequence of the pair α, β = 1 ± √2, (P,Q) = (2,−1), and
V_m = α^m + β^m = 2 h_m is its companion).

* `pell`            : h_m² − 2 U_m² = (−1)^m.
* `two_isSq_mod`    : for odd m and d ∣ h_m, d ∣ (2U_m)² − 2, i.e. 2 is a square mod d (so ε = (2/d) = +1 for
                      every odd prime d ∣ h_m; the inert branch of Prop. I2(b) is vacuous).
* `seven_dvd_nsw_iff` : 7 ∣ h_m ↔ m ≡ 3 (mod 6).
* `lucasU_two_mul`  : U_{2m} = 2 h_m U_m  (= U_m V_m).
* `nsw_dvd_lucasU_two_mul` : h_m ∣ U_{2m}.
* `primitive_dvd_nsw` : if a prime p divides U_{2m} (m ≥ 2) and no U_k with 0 < k < 2m (a primitive divisor in
  the sense of Bilu–Hanrot–Voutier), then p is odd, p ∣ h_m, and p ∤ h_{m'} for 0 < m' < m.
* `finite_set_fails` : given the primitive-divisor theorem as a hypothesis, every finite set S misses a prime
  factor of h_m for all sufficiently large m.
The existence of primitive divisors (Bilu–Hanrot–Voutier 2001; Carmichael 1913 for real Lucas pairs) is an
external theorem and is NOT formalised; `primitive_dvd_nsw` takes it as a hypothesis.
No `sorry`, no `native_decide`.
-/

namespace Bgs.LineIArith

open Zsqrtd Bgs.LineG

/-- α = 1 + √2. -/
def α : ℤ√2 := ⟨1, 1⟩

/-- Lucas U-sequence of (P,Q) = (2,−1): U_m = Im (1+√2)^m. -/
def lucasU (m : ℕ) : ℤ := (α ^ m).im

theorem nsw_eq (m : ℕ) : nsw m = (α ^ m).re := rfl

theorem norm_alpha : Zsqrtd.norm α = -1 := by decide

theorem pell (m : ℕ) : nsw m ^ 2 - 2 * lucasU m ^ 2 = (-1) ^ m := by
  have h : Zsqrtd.norm (α ^ m) = (-1) ^ m := by
    induction m with
    | zero => decide
    | succ k ih => rw [pow_succ, Zsqrtd.norm_mul, ih, norm_alpha, pow_succ]
  rw [Zsqrtd.norm_def] at h
  simp only [nsw_eq, lucasU]
  linear_combination h

theorem two_isSq_mod {m : ℕ} (hm : Odd m) {d : ℤ} (hd : d ∣ nsw m) :
    d ∣ (2 * lucasU m) ^ 2 - 2 := by
  have hp := pell m
  rw [hm.neg_one_pow] at hp
  have : (2 * lucasU m) ^ 2 - 2 = 2 * nsw m * nsw m := by linear_combination (-2 : ℤ) * hp
  rw [this]
  exact Dvd.dvd.mul_right (Dvd.dvd.mul_left hd 2) _

theorem lucasU_two_mul (m : ℕ) : lucasU (2 * m) = 2 * nsw m * lucasU m := by
  simp only [lucasU, nsw_eq, pow_mul']
  rw [sq, Zsqrtd.im_mul]; ring

theorem nsw_dvd_lucasU_two_mul (m : ℕ) : nsw m ∣ lucasU (2 * m) := by
  rw [lucasU_two_mul]; exact ⟨2 * lucasU m, by ring⟩

theorem lucasU_two : lucasU 2 = 2 := by decide

/-- Period 6 mod 7: h_{m+6} − h_m = 7 (14 h_m + 20 U_m). -/
theorem nsw_add_six (m : ℕ) : nsw (m + 6) - nsw m = 7 * (14 * nsw m + 20 * lucasU m) := by
  have h6 : α ^ 6 = ⟨99, 70⟩ := by decide
  simp only [nsw_eq, lucasU, pow_add, h6, Zsqrtd.re_mul]
  ring

theorem seven_dvd_nsw_iff (m : ℕ) : (7 : ℤ) ∣ nsw m ↔ m % 6 = 3 := by
  induction m using Nat.strong_induction_on with
  | _ m ih =>
    by_cases hm : m < 6
    · interval_cases m <;> decide
    · obtain ⟨k, rfl⟩ : ∃ k, m = k + 6 := ⟨m - 6, by omega⟩
      have hk := ih k (by omega)
      have hmod : (k + 6) % 6 = k % 6 := by omega
      rw [hmod, ← hk]
      have hd := nsw_add_six k
      constructor
      · intro h
        have : (7 : ℤ) ∣ nsw (k + 6) - (nsw (k + 6) - nsw k) := dvd_sub h ⟨_, hd⟩
        simpa using this
      · intro h
        have : (7 : ℤ) ∣ nsw k + (nsw (k + 6) - nsw k) := dvd_add h ⟨_, hd⟩
        simpa using this

/-- Consequence of a primitive divisor of U_{2m} (the BHV input is a hypothesis). -/
theorem primitive_dvd_nsw {p : ℕ} (hp : p.Prime) {m : ℕ} (hm : 2 ≤ m)
    (hdiv : (p : ℤ) ∣ lucasU (2 * m))
    (hprim : ∀ k, 0 < k → k < 2 * m → ¬ (p : ℤ) ∣ lucasU k) :
    p ≠ 2 ∧ (p : ℤ) ∣ nsw m ∧ ∀ m', 0 < m' → m' < m → ¬ (p : ℤ) ∣ nsw m' := by
  have hpZ : Prime (p : ℤ) := Nat.prime_iff_prime_int.mp hp
  have hp2 : ¬ (p : ℤ) ∣ 2 := by
    have := hprim 2 (by norm_num) (by omega)
    rwa [lucasU_two] at this
  have hpU : ¬ (p : ℤ) ∣ lucasU m := hprim m (by omega) (by omega)
  refine ⟨?_, ?_, ?_⟩
  · rintro rfl; exact hp2 (by norm_num)
  · rw [lucasU_two_mul] at hdiv
    rcases hpZ.dvd_or_dvd hdiv with h | h
    · rcases hpZ.dvd_or_dvd h with h' | h'
      · exact absurd h' hp2
      · exact h'
    · exact absurd h hpU
  · intro m' hm'0 hm' h
    exact hprim (2 * m') (by omega) (by omega) (dvd_trans h (nsw_dvd_lucasU_two_mul m'))

/-- Any finite set of primes misses a prime factor of h_m for all large m, GIVEN the primitive-divisor theorem
(Bilu–Hanrot–Voutier: U_n has a primitive prime divisor for every n > 30), which enters as the hypothesis `hBHV`. -/
theorem finite_set_fails
    (hBHV : ∀ n, 30 < n → ∃ p : ℕ, p.Prime ∧ (p : ℤ) ∣ lucasU n ∧ ∀ k, 0 < k → k < n → ¬ (p : ℤ) ∣ lucasU k)
    (S : Finset ℕ) : ∃ M, ∀ m, M ≤ m → ∃ p : ℕ, p.Prime ∧ p ∉ S ∧ (p : ℤ) ∣ nsw m := by
  classical
  let f : ℕ → ℕ := fun s => if h : ∃ m', 0 < m' ∧ (s : ℤ) ∣ nsw m' then Nat.find h else 0
  refine ⟨max 16 (S.sup f + 1), fun m hm => ?_⟩
  have hm16 : 16 ≤ m := le_of_max_le_left hm
  have hmS : S.sup f + 1 ≤ m := le_of_max_le_right hm
  obtain ⟨p, hp, hdiv, hprim⟩ := hBHV (2 * m) (by omega)
  obtain ⟨-, hpm, hnew⟩ := primitive_dvd_nsw hp (by omega) hdiv hprim
  refine ⟨p, hp, fun hpS => ?_, hpm⟩
  have hex : ∃ m', 0 < m' ∧ (p : ℤ) ∣ nsw m' := ⟨m, by omega, hpm⟩
  have hfp : f p = Nat.find hex := by simp only [f, dif_pos hex]
  have hle : f p ≤ S.sup f := Finset.le_sup hpS
  have hspec := Nat.find_spec hex
  have hmin : Nat.find hex ≤ m := Nat.find_min' hex ⟨by omega, hpm⟩
  rcases lt_or_eq_of_le hmin with hlt | heq
  · exact hnew _ hspec.1 hlt hspec.2
  · omega

#print axioms nsw_eq
#print axioms norm_alpha
#print axioms pell
#print axioms two_isSq_mod
#print axioms lucasU_two_mul
#print axioms nsw_dvd_lucasU_two_mul
#print axioms lucasU_two
#print axioms nsw_add_six
#print axioms seven_dvd_nsw_iff
#print axioms primitive_dvd_nsw
#print axioms finite_set_fails

end Bgs.LineIArith
