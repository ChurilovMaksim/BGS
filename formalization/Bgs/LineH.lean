import Mathlib

/-!
# Line H: elementary steps of the 49-state Line B certificate (BGS-TRACE-207..)

Generic lemmas (no certificate numbers enter Lean):

* `geom_tail` : if `0 ≤ R i ≤ μ`, `T i ≥ 0` and `∑ T i R i ^ n < μ ^ (n+1)`, then the same holds for every larger `n`.
* `dom_lower` : if `Z = c (w + A)` with `‖A‖ ≤ B`, then `‖c‖ (‖w‖ - B) ≤ ‖Z‖`  (the Lidskii/Weyl split of the trace).
* `h_odd`, `yp_odd`, `k_odd`, `kappa_odd` : the κ-lemma. If h² + 1 = 2y'² and 196ν + s = k h with s = ±1, then h, y', k are
  odd and κ = (−k·y') mod 8 is odd (u = 49⁻¹ ≡ 1 mod 8). Hence the sector coefficients have |c_b| = ½ (b even), 0 (b odd)
  for every odd m with 3 ∤ m (Gauss-sum step: `sq_residues_mod8`, `shift4`; the evaluation |Σ_t e(κt²/8)| = 4 is a paper step).
No `sorry`, no `native_decide`.
-/

namespace Bgs.LineH

open Finset

theorem geom_tail {ι : Type*} (s : Finset ι) (T R : ι → ℝ) (μ : ℝ) (hμ : 0 < μ)
    (hT : ∀ i ∈ s, 0 ≤ T i) (hR0 : ∀ i ∈ s, 0 ≤ R i) (hRμ : ∀ i ∈ s, R i ≤ μ)
    (n : ℕ) (h : ∑ i ∈ s, T i * R i ^ n < μ ^ (n + 1)) :
    ∀ k : ℕ, ∑ i ∈ s, T i * R i ^ (n + k) < μ ^ (n + 1 + k) := by
  intro k
  induction k with
  | zero => simpa using h
  | succ k ih =>
    have step : ∑ i ∈ s, T i * R i ^ (n + (k + 1)) ≤ μ * ∑ i ∈ s, T i * R i ^ (n + k) := by
      rw [Finset.mul_sum]
      apply Finset.sum_le_sum
      intro i hi
      have e : T i * R i ^ (n + (k + 1)) = (T i * R i ^ (n + k)) * R i := by ring
      rw [e]
      have hp : 0 ≤ T i * R i ^ (n + k) := mul_nonneg (hT i hi) (pow_nonneg (hR0 i hi) _)
      nlinarith [hRμ i hi, hp]
    have e2 : μ ^ (n + 1 + (k + 1)) = μ * μ ^ (n + 1 + k) := by ring
    rw [e2]
    calc ∑ i ∈ s, T i * R i ^ (n + (k + 1)) ≤ μ * ∑ i ∈ s, T i * R i ^ (n + k) := step
      _ < μ * μ ^ (n + 1 + k) := mul_lt_mul_of_pos_left ih hμ

theorem dom_lower (c w A Z : ℂ) (B : ℝ) (hZ : Z = c * (w + A)) (hA : ‖A‖ ≤ B) :
    ‖c‖ * (‖w‖ - B) ≤ ‖Z‖ := by
  subst hZ
  rw [norm_mul]
  apply mul_le_mul_of_nonneg_left _ (norm_nonneg c)
  have := norm_sub_norm_le w (-A)
  simp only [sub_neg_eq_add, norm_neg] at this
  linarith

theorem h_odd (h y : ℤ) (H : h ^ 2 + 1 = 2 * y ^ 2) : Odd h := by
  by_contra hc
  rw [Int.not_odd_iff_even] at hc
  obtain ⟨r, rfl⟩ := hc
  have h1 : Odd ((r + r) ^ 2 + 1) := ⟨2 * r ^ 2, by ring⟩
  have h2 : Even (2 * y ^ 2) := ⟨y ^ 2, by ring⟩
  rw [H] at h1
  exact (Int.not_even_iff_odd.mpr h1) h2

theorem yp_odd (h y : ℤ) (H : h ^ 2 + 1 = 2 * y ^ 2) : Odd y := by
  obtain ⟨a, rfl⟩ := h_odd h y H
  have hy2 : y ^ 2 = 2 * (a ^ 2 + a) + 1 := by nlinarith [H]
  have : Odd (y ^ 2) := ⟨a ^ 2 + a, hy2⟩
  exact (Int.odd_pow.mp this).resolve_right (by norm_num)

theorem k_odd (h k ν s : ℤ) (hs : s = 1 ∨ s = -1)
    (hk : 196 * ν + s = k * h) : Odd k := by
  have hodd : Odd (196 * ν + s) := by
    rcases hs with rfl | rfl
    · exact ⟨98 * ν, by ring⟩
    · exact ⟨98 * ν - 1, by ring⟩
  rw [hk] at hodd
  exact (Int.odd_mul.mp hodd).1

theorem kappa_odd (h y k ν s : ℤ) (H : h ^ 2 + 1 = 2 * y ^ 2) (hs : s = 1 ∨ s = -1)
    (hk : 196 * ν + s = k * h) : (-(k * 1 * y)) % 8 % 2 = 1 := by
  have hk' := k_odd h k ν s hs hk
  have hy := yp_odd h y H
  have ho : Odd (-(k * 1 * y)) := by
    rw [mul_one]; exact (Int.odd_mul.mpr ⟨hk', hy⟩).neg
  rw [Int.emod_emod_of_dvd _ (by norm_num : (2:ℤ) ∣ 8)]
  exact Int.odd_iff.mp ho

/-- u = 49⁻¹ mod 8 equals 1. -/
theorem inv49_mod8 : (49 * 1 : ℤ) % 8 = 1 := by norm_num

/-- For odd κ the residues κ t² mod 8 (t = 0..7) are 0, κ, 4, κ, 0, κ, 4, κ: hence Σ_t e(κt²/8) = 2 + 4e(κ/8) + 2e(1/2) = 4e(κ/8). -/
theorem sq_residues_mod8 : ∀ κ ∈ ({1, 3, 5, 7} : Finset ℕ),
    (List.range 8).map (fun t => κ * t * t % 8) = [0, κ, 4, κ, 0, κ, 4, κ] := by
  decide

/-- Shift t ↦ t + 4: κ(t+4)² − b(t+4) ≡ κt² − bt + 4 (mod 8) for b odd (any κ): the sum over t mod 8 changes sign, so c_b = 0. -/
theorem shift4 (κ b t : ℤ) (hb : Odd b) : (κ * (t + 4) ^ 2 - b * (t + 4) - (κ * t ^ 2 - b * t + 4)) % 8 = 0 := by
  obtain ⟨r, rfl⟩ := hb
  have : κ * (t + 4) ^ 2 - (2 * r + 1) * (t + 4) - (κ * t ^ 2 - (2 * r + 1) * t + 4) = 8 * (κ * t + 2 * κ - r - 1) := by ring
  rw [this]; simp

#print axioms geom_tail
#print axioms dom_lower
#print axioms h_odd
#print axioms yp_odd
#print axioms k_odd
#print axioms kappa_odd
#print axioms inv49_mod8
#print axioms sq_residues_mod8
#print axioms shift4

end Bgs.LineH
