import Mathlib.NumberTheory.Zsqrtd.Basic
import Mathlib.Data.ZMod.Basic
import Mathlib.GroupTheory.OrderOfElement
import Mathlib.Algebra.Field.ZMod
import Mathlib.Tactic.LinearCombination

/-!
# BGS-FM-036 — §4 arithmetic of the Pell moduli (finite arithmetic facts only)

Source: `mathematics/locality/fixed_strength_locality.md`, §4
("Arithmetic multiplicities and individual cluster control").
Write `α = 1 + √2` and `N + F√2 = α^K` with `K` odd.  Certified here:

* `pell_norm` : `N² − 2F² = −1` (the Pell identity);
* for every modulus `m` with `m ∣ N`, in `ZMod m`, with the explicit
  inverse `s = 2F` of `F` (`s_mul_F : s·F = 1`): `s² = 2`,
  `(1 + s)^K = 1`, `h := 3 + 2s = (1 + s)²`, `h^K = 1`,
  `h − 1 = 2(1 + s)`;
* for `K` prime and every prime `p ∣ N`, in `ZMod p`:
  `orderOf h = K` (`orderOf_h`), `h^j ≠ 1` for `0 < j < K`
  (so `1 − h^j` is a unit), and `h^j ≠ −1` for every `j`
  (so `1 + h^j` is a unit).

(The source chooses `s = F⁻¹ (mod N)`; `2F` *is* that inverse, by
`s_mul_F`.)  **Not formalized (partial coverage of BGS-FM-036):** the
symplectic diagonalisation by `P`, the Weyl implementer, the multiplicity
count `n = (N − 1)/(2K)` of the cluster centres, and all of Theorem C's
spectral/analytic conclusions (cluster halfwidth `O(N^{-R})`, spacing
collapse, Wasserstein limits).  No `sorry`, no `native_decide`.
-/

namespace Bgs.PellModuliArith

/-- `α = 1 + √2`. -/
def alpha : ℤ√2 := ⟨1, 1⟩

theorem norm_alpha : alpha.norm = -1 := by
  simp [alpha, Zsqrtd.norm]

theorem norm_alpha_pow (K : ℕ) : (alpha ^ K).norm = (-1) ^ K := by
  induction K with
  | zero => simp [Zsqrtd.norm]
  | succ k ih => rw [pow_succ, Zsqrtd.norm_mul, ih, norm_alpha]; ring

/-- **Pell identity.** If `α^K = N + F√2` with `K` odd, then `N² − 2F² = −1`. -/
theorem pell_norm (K : ℕ) (hK : Odd K) :
    (alpha ^ K).re * (alpha ^ K).re - 2 * (alpha ^ K).im * (alpha ^ K).im = -1 := by
  have hn := norm_alpha_pow K
  rw [hK.neg_one_pow, Zsqrtd.norm_def] at hn
  linear_combination hn

section Modulus

variable (K : ℕ) (hK : Odd K) (m : ℕ) (hm : (m : ℤ) ∣ (alpha ^ K).re)
include hK hm

omit hK in
/-- `N ≡ 0` in `ZMod m`. -/
theorem N_zero : (((alpha ^ K).re : ℤ) : ZMod m) = 0 :=
  (ZMod.intCast_zmod_eq_zero_iff_dvd _ _).mpr hm

/-- `s = 2F` is the inverse of `F` modulo `m`. -/
theorem s_mul_F :
    (2 * ((alpha ^ K).im : ZMod m)) * ((alpha ^ K).im : ZMod m) = 1 := by
  have hp := congrArg (fun z : ℤ => (z : ZMod m)) (pell_norm K hK)
  simp only [Int.cast_sub, Int.cast_mul, Int.cast_ofNat, Int.cast_neg, Int.cast_one] at hp
  rw [N_zero K m hm] at hp
  linear_combination -hp

/-- `s² = 2` modulo `m`. -/
theorem s_sq :
    (2 * ((alpha ^ K).im : ZMod m)) ^ 2 = 2 := by
  have := s_mul_F K hK m hm
  linear_combination 2 * this

/-- The ring map `ℤ[√2] → ZMod m`, `√2 ↦ s`. -/
noncomputable def toZMod : ℤ√2 →+* ZMod m :=
  Zsqrtd.lift ⟨2 * ((alpha ^ K).im : ZMod m), by
    have := s_sq K hK m hm; push_cast; linear_combination this⟩

/-- `(1 + s)^K = N + F s = 1` modulo `m`. -/
theorem one_add_s_pow :
    (1 + 2 * ((alpha ^ K).im : ZMod m)) ^ K = 1 := by
  have hmap : toZMod K hK m hm (alpha ^ K)
      = (((alpha ^ K).re : ℤ) : ZMod m) + ((alpha ^ K).im : ZMod m) * (2 * ((alpha ^ K).im : ZMod m)) := by
    simp [toZMod, Zsqrtd.lift]
  have hα : toZMod K hK m hm alpha = 1 + 2 * ((alpha ^ K).im : ZMod m) := by
    simp [toZMod, Zsqrtd.lift, alpha]
  rw [map_pow, hα, N_zero K m hm, zero_add] at hmap
  linear_combination hmap + s_mul_F K hK m hm

/-- `h = 3 + 2s = (1 + s)²`, `h^K = 1` and `h − 1 = 2(1 + s)` modulo `m`. -/
theorem h_facts :
    (3 + 2 * (2 * ((alpha ^ K).im : ZMod m))) = (1 + 2 * ((alpha ^ K).im : ZMod m)) ^ 2
    ∧ (3 + 2 * (2 * ((alpha ^ K).im : ZMod m))) ^ K = 1
    ∧ (3 + 2 * (2 * ((alpha ^ K).im : ZMod m))) - 1 = 2 * (1 + 2 * ((alpha ^ K).im : ZMod m)) := by
  have hsq : (3 + 2 * (2 * ((alpha ^ K).im : ZMod m))) = (1 + 2 * ((alpha ^ K).im : ZMod m)) ^ 2 := by
    have := s_sq K hK m hm
    linear_combination -this
  refine ⟨hsq, ?_, by ring⟩
  rw [hsq, ← pow_mul, mul_comm 2 K, pow_mul, one_add_s_pow K hK m hm, one_pow]

end Modulus

/-- `N` is odd. -/
theorem N_odd (K : ℕ) (hK : Odd K) : Odd (alpha ^ K).re := by
  have h := pell_norm K hK
  by_contra hc
  rw [Int.not_odd_iff_even] at hc
  obtain ⟨t, ht⟩ := hc
  rw [ht] at h
  have h2 : (2 : ℤ) ∣ -1 := ⟨2 * t * t - (alpha ^ K).im * (alpha ^ K).im, by linear_combination -h⟩
  omega

section Prime

variable (K : ℕ) (hKp : K.Prime) (hK : Odd K) (p : ℕ) [hp : Fact p.Prime]
  (hpN : (p : ℤ) ∣ (alpha ^ K).re)
include hKp hK hpN

omit hKp in
theorem p_ne_two : p ≠ 2 := by
  intro h2
  subst h2
  have := N_odd K hK
  obtain ⟨t, ht⟩ := this
  rw [ht] at hpN
  push_cast at hpN
  omega

omit hKp in
theorem two_ne_zero' : (2 : ZMod p) ≠ 0 := by
  intro h
  have : ((2 : ℕ) : ZMod p) = 0 := by exact_mod_cast h
  rw [ZMod.natCast_eq_zero_iff] at this
  have := (Nat.prime_dvd_prime_iff_eq hp.out Nat.prime_two).mp this
  exact p_ne_two K hK p hpN this

theorem h_ne_one : (3 + 2 * (2 * ((alpha ^ K).im : ZMod p))) ≠ 1 := by
  intro h
  have h1 := (h_facts K hK p hpN).2.2
  rw [h, sub_self] at h1
  have hu := one_add_s_pow K hK p hpN
  have h2 := two_ne_zero' K hK p hpN
  have hz : (1 + 2 * ((alpha ^ K).im : ZMod p)) = 0 := by
    rcases mul_eq_zero.mp h1.symm with h3 | h3
    · exact absurd h3 h2
    · exact h3
  rw [hz, zero_pow (Nat.Prime.ne_zero hKp)] at hu
  exact zero_ne_one hu

/-- **Modulo each prime divisor of `N`, the order of `h` is exactly `K`.** -/
theorem orderOf_h : orderOf (3 + 2 * (2 * ((alpha ^ K).im : ZMod p))) = K := by
  have : Fact K.Prime := ⟨hKp⟩
  exact orderOf_eq_prime (h_facts K hK p hpN).2.1 (h_ne_one K hKp hK p hpN)

/-- `h^j ≠ 1` for `0 < j < K`, i.e. `1 − h^j` is a unit modulo `p`. -/
theorem h_pow_ne_one (j : ℕ) (hj0 : 0 < j) (hjK : j < K) :
    (3 + 2 * (2 * ((alpha ^ K).im : ZMod p))) ^ j ≠ 1 := by
  intro h
  have := orderOf_dvd_of_pow_eq_one h
  rw [orderOf_h K hKp hK p hpN] at this
  exact absurd (Nat.le_of_dvd hj0 this) (by omega)

/-- `h^j ≠ −1` for every `j`, i.e. `1 + h^j` is a unit modulo `p`. -/
theorem h_pow_ne_neg_one (j : ℕ) :
    (3 + 2 * (2 * ((alpha ^ K).im : ZMod p))) ^ j ≠ -1 := by
  intro h
  have h2j : (3 + 2 * (2 * ((alpha ^ K).im : ZMod p))) ^ (2 * j) = 1 := by
    rw [pow_mul', h]; norm_num
  have hdvd := orderOf_dvd_of_pow_eq_one h2j
  rw [orderOf_h K hKp hK p hpN] at hdvd
  have hcop : Nat.Coprime K 2 := by
    rw [Nat.coprime_two_right]; exact hK
  have hKj : K ∣ j := hcop.dvd_of_dvd_mul_left hdvd
  obtain ⟨c, rfl⟩ := hKj
  rw [pow_mul, (h_facts K hK p hpN).2.1, one_pow] at h
  have : (2 : ZMod p) = 0 := by linear_combination h
  exact two_ne_zero' K hK p hpN this

end Prime

end Bgs.PellModuliArith
