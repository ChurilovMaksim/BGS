import Mathlib

/-!
# Line G — finite/algebraic lemmas behind the resonance classification

* `phase_split`      : the rational-reconstruction identity  ν P/(2h) = (2a/b)·P/(4h) + k P / b  when  b ν = a + 2h k.
* `u_succ`, `w_succ` : the two-register automaton computing  u_j = Σ_{i<j} n_i ψ(j-i)  for any ψ with ψ(d+2) = 6ψ(d+1) − ψ(d).
* `quad_form`        : Σ_{i,j<m} ψ(|i−j|) n_i n_j = ψ(0) Σ n_j² + 2 Σ_j n_j u_j   (so P(n) mod b is read off the automaton).
* `re_dvd_re_pow`    : in ℤ[√2], α.re ∣ (α^k).re for odd k  (divisibility sequence),
  hence `nsw_dvd`    : h_d ∣ h_m whenever d ∣ m, m odd, where h_m = ((1+√2)^m).re (the NSW numbers).
* concrete certificates at m = 17 (by `norm_num`/`decide` on small facts; no `native_decide`), including
  `nsw_17 : nsw 17 = 1607521` (ties the m = 17 modulus to the NSW sequence).

Scope (integration note, BGS-TRACE-203 and 205): only the algebraic core is formalised (phase split, automaton
recursion, quadratic-form identity, NSW divisibility, m = 17 facts). The partial-trace law G2 (trace formula),
the dilution identity G3, sparsity G6 and the moment heuristic G7 are not formalised.
-/

namespace Bgs.LineG

open Finset BigOperators

/-- The rational-reconstruction identity (Theorem G1, algebraic core). -/
theorem phase_split (ν a b k h P : ℚ) (hb : b ≠ 0) (hh : h ≠ 0)
    (hrec : b * ν = a + 2 * h * k) :
    ν * P / (2 * h) = (2 * a / b) * (P / (4 * h)) + k * P / b := by
  have hν : ν = (a + 2 * h * k) / b := by field_simp; linarith
  subst hν
  field_simp
  ring

section automaton
variable (ψ n : ℕ → ℤ)

/-- u_j = Σ_{i<j} n_i ψ(j−i). -/
def u (j : ℕ) : ℤ := ∑ i ∈ range j, n i * ψ (j - i)
/-- w_j = Σ_{i<j} n_i ψ(j−1−i). -/
def w (j : ℕ) : ℤ := ∑ i ∈ range j, n i * ψ (j - 1 - i)

theorem w_succ (j : ℕ) : w ψ n (j + 1) = u ψ n j + n j * ψ 0 := by
  unfold w u
  rw [sum_range_succ]
  have h0 : j + 1 - 1 - j = 0 := by omega
  rw [h0]
  congr 1

theorem u_succ (hψ : ∀ d, ψ (d + 2) = 6 * ψ (d + 1) - ψ d) (j : ℕ) :
    u ψ n (j + 1) = 6 * u ψ n j - w ψ n j + n j * ψ 1 := by
  unfold u w
  rw [sum_range_succ, show j + 1 - j = 1 by omega]
  have : ∑ i ∈ range j, n i * ψ (j + 1 - i)
      = ∑ i ∈ range j, (6 * (n i * ψ (j - i)) - n i * ψ (j - 1 - i)) := by
    apply sum_congr rfl
    intro i hi
    have hi' : i < j := mem_range.mp hi
    have e1 : j + 1 - i = (j - 1 - i) + 2 := by omega
    have e2 : j - i = (j - 1 - i) + 1 := by omega
    rw [e1, hψ, ← e2]
    ring
  rw [this, sum_sub_distrib, ← mul_sum]

/-- symmetric quadratic form with coefficients ψ(|i−j|) -/
def Q (m : ℕ) : ℤ := ∑ i ∈ range m, ∑ j ∈ range m, ψ (Int.natAbs ((i : ℤ) - j)) * n i * n j

theorem quad_form (m : ℕ) :
    Q ψ n m = ψ 0 * ∑ j ∈ range m, n j ^ 2 + 2 * ∑ j ∈ range m, n j * u ψ n j := by
  induction m with
  | zero => simp [Q]
  | succ m ih =>
    have hrow : ∑ j ∈ range m, ψ (Int.natAbs ((m : ℤ) - j)) * n m * n j = n m * u ψ n m := by
      unfold u; rw [mul_sum]; apply sum_congr rfl; intro j hj
      have hj' : j < m := mem_range.mp hj
      have : Int.natAbs ((m : ℤ) - j) = m - j := by omega
      rw [this]; ring
    have hcol : ∑ i ∈ range m, ψ (Int.natAbs ((i : ℤ) - m)) * n i * n m = n m * u ψ n m := by
      rw [← hrow]; apply sum_congr rfl; intro i hi
      have : Int.natAbs ((i : ℤ) - m) = Int.natAbs ((m : ℤ) - i) := by omega
      rw [this]; ring
    unfold Q at ih ⊢
    rw [sum_range_succ]
    simp only [sum_range_succ]
    rw [show (∑ x ∈ range m, (∑ x_1 ∈ range m, ψ (Int.natAbs ((x:ℤ) - x_1)) * n x * n x_1
          + ψ (Int.natAbs ((x:ℤ) - m)) * n x * n m))
        = (∑ x ∈ range m, ∑ x_1 ∈ range m, ψ (Int.natAbs ((x:ℤ) - x_1)) * n x * n x_1)
          + ∑ x ∈ range m, ψ (Int.natAbs ((x:ℤ) - m)) * n x * n m from sum_add_distrib]
    rw [ih, hcol, hrow]
    simp
    ring
end automaton

section nsw
open Zsqrtd

/-- For odd k, α.re ∣ (α^k).re ; for even k, α.re ∣ (α^k).im  (ℤ[√2]). -/
theorem re_dvd_pow (α : ℤ√2) : ∀ k : ℕ, (Odd k → α.re ∣ (α ^ k).re) ∧ (Even k → α.re ∣ (α ^ k).im) := by
  intro k
  induction k with
  | zero => exact ⟨fun h => absurd h (by decide), fun _ => by simp⟩
  | succ k ih =>
    refine ⟨fun hk => ?_, fun hk => ?_⟩
    · have he : Even k := by rcases hk with ⟨t, ht⟩; exact ⟨t, by omega⟩
      obtain ⟨c, hc⟩ := ih.2 he
      rw [pow_succ, Zsqrtd.re_mul, hc]
      exact ⟨(α ^ k).re + 2 * c * α.im, by ring⟩
    · have ho : Odd k := by rcases hk with ⟨t, ht⟩; exact ⟨t - 1, by omega⟩
      obtain ⟨c, hc⟩ := ih.1 ho
      rw [pow_succ, Zsqrtd.im_mul, hc]
      exact ⟨c * α.im + (α ^ k).im, by ring⟩

/-- NSW numbers h_m = Re (1+√2)^m  (h_1=1, h_3=7, h_5=41, ...). -/
def nsw (m : ℕ) : ℤ := (((⟨1, 1⟩ : ℤ√2)) ^ m).re

theorem nsw_dvd {d m : ℕ} (hdm : d ∣ m) (hm : Odd m) : nsw d ∣ nsw m := by
  obtain ⟨k, rfl⟩ := hdm
  have hk : Odd k := (Nat.odd_mul.mp hm).2
  unfold nsw
  rw [pow_mul]
  exact (re_dvd_pow _ k).1 hk

theorem nsw_3 : nsw 3 = 7 := by decide
theorem nsw_5 : nsw 5 = 41 := by decide
theorem nsw_7 : nsw 7 = 239 := by decide
theorem nsw_17 : nsw 17 = 1607521 := by decide
end nsw

/-! ## concrete facts used at m = 17 (pre-registration targets) -/
section m17
-- h_17 = 1607521 = 103 * 15607, y'_17 with h^2+1 = 2 y'^2
theorem h17_factor : (1607521 : ℤ) = 103 * 15607 := by norm_num
theorem h17_pell : (1607521 : ℤ) ^ 2 + 1 = 2 * 1136689 ^ 2 := by norm_num
end m17

#print axioms phase_split
#print axioms w_succ
#print axioms u_succ
#print axioms quad_form
#print axioms re_dvd_pow
#print axioms nsw_dvd
#print axioms nsw_3
#print axioms nsw_5
#print axioms nsw_7
#print axioms nsw_17
#print axioms h17_factor
#print axioms h17_pell

end Bgs.LineG
