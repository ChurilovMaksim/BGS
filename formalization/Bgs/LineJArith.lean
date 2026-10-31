import Mathlib

/-!
# Line J — finite arithmetic cores used by the Line J claims

Only the statements below are formalised. The analytic and computer-assisted content of the Line J claims is not
(see `mathematics/fixed-map/lineJ_d7_twisted_coefficient.md`).

* `rank_core` (r(q) lemma, BGS-TRACE-230, algebraic core): in any commutative ring, for a unit ε and odd m,
  ε^m + (−ε⁻¹)^m = 0 ↔ (ε²)^m = 1. With ε = 1 + √2 in (ℤ[√2]/q) (ε̄ = −ε⁻¹, 2h_m = ε^m + ε̄^m, 2 invertible) this is
  q ∣ h_m ↔ λ^m ≡ 1 (λ = ε²). Passing to ℤ[√2]/q is done on paper.
* `pell49_period` (periodicity in Prop J-C, BGS-TRACE-221): the coordinates of (1+√2)^m modulo 49 have exact period 42.
  `pell49_lambda_order`: λ = (1+√2)² has exact order 21 modulo 49.
* `count_excl_one`, `count_units` (n_q in the inheritance theorem, BGS-TRACE-228): in ZMod q, the residues j ≠ 0
  with j ≠ b for a fixed b ≠ 0 number q − 2; the residues j ≠ 0 number q − 1.
* `window_step` (window lemma, BGS-TRACE-224, real-line core): if x < a and 0 < θ ≤ L, then k = ⌈(a − x)/θ⌉ satisfies
  a ≤ x + kθ ≤ a + L. Reduction mod 2π is done on paper.
* `window_N` (window lemma constants): for θ_lo = 1.130677114, ⌈2π/θ_lo⌉ = 6, and for θ_lo ≤ θ, θ_up = 1.131054118,
  (2π − θ_up)/θ ≤ 5.
No `sorry`, no `native_decide`.
-/

namespace Bgs.LineJArith

/-- r(q) lemma, algebraic core. -/
theorem rank_core {R : Type*} [CommRing R] (ε : Rˣ) {m : ℕ} (hm : Odd m) :
    ((ε : R) ^ m + (-((ε⁻¹ : Rˣ) : R)) ^ m = 0) ↔ (((ε : R) ^ 2) ^ m = 1) := by
  have hneg : (-((ε⁻¹ : Rˣ) : R)) ^ m = -(((ε⁻¹ : Rˣ) : R) ^ m) := hm.neg_pow _
  rw [hneg, ← sub_eq_add_neg]
  have hu : ((ε : R) ^ m) * (((ε⁻¹ : Rˣ) : R) ^ m) = 1 := by
    rw [← mul_pow]; simp
  constructor
  · intro h
    have h1 : (ε : R) ^ m = ((ε⁻¹ : Rˣ) : R) ^ m := sub_eq_zero.mp h
    calc ((ε : R) ^ 2) ^ m = (ε : R) ^ m * (ε : R) ^ m := by rw [← pow_mul, ← pow_add]; ring_nf
      _ = (ε : R) ^ m * ((ε⁻¹ : Rˣ) : R) ^ m := by rw [← h1]
      _ = 1 := hu
  · intro h
    have h2 : (ε : R) ^ m * (ε : R) ^ m = 1 := by
      rw [← h, ← pow_mul, ← pow_add]; ring_nf
    have : (ε : R) ^ m = ((ε⁻¹ : Rˣ) : R) ^ m := by
      calc (ε : R) ^ m = (ε : R) ^ m * ((ε : R) ^ m * ((ε⁻¹ : Rˣ) : R) ^ m) := by rw [hu, mul_one]
        _ = ((ε : R) ^ m * (ε : R) ^ m) * ((ε⁻¹ : Rˣ) : R) ^ m := by ring
        _ = ((ε⁻¹ : Rˣ) : R) ^ m := by rw [h2, one_mul]
    exact sub_eq_zero.mpr this

/-- One step of multiplication by 1 + √2 on coordinates: (a + b√2)(1 + √2) = (a + 2b) + (a + b)√2. -/
def step49 (p : ZMod 49 × ZMod 49) : ZMod 49 × ZMod 49 := (p.1 + 2 * p.2, p.1 + p.2)

/-- Coordinates of (1+√2)^m modulo 49. -/
def pell49 (m : ℕ) : ZMod 49 × ZMod 49 := step49^[m] (1, 0)

theorem pell49_period : pell49 42 = (1, 0) ∧ ∀ d ∈ ({1, 2, 3, 6, 7, 14, 21} : Finset ℕ), pell49 d ≠ (1, 0) := by
  decide

theorem pell49_periodic (m : ℕ) : pell49 (m + 42) = pell49 m := by
  unfold pell49
  rw [Function.iterate_add_apply]
  have : step49^[42] (1, 0) = (1, 0) := pell49_period.1
  rw [this]

/-- λ = (1+√2)² has exact order 21 modulo 49 (so 49 ∣ h_m needs 21 ∣ m for odd m). -/
theorem pell49_lambda_order : pell49 (2 * 21) = (1, 0) ∧
    ∀ d ∈ ({1, 3, 7} : Finset ℕ), pell49 (2 * d) ≠ (1, 0) := by
  decide

/-- n_q for q ∥ h: one nonzero residue is excluded. -/
theorem count_excl_one (q : ℕ) [NeZero q] (b : ZMod q) (hb : b ≠ 0) :
    (Finset.univ.filter (fun j : ZMod q => j ≠ 0 ∧ j ≠ b)).card = q - 2 := by
  have h1 : (Finset.univ.filter (fun j : ZMod q => j ≠ 0 ∧ j ≠ b)) =
      (Finset.univ.erase (0 : ZMod q)).erase b := by
    ext j; simp [and_comm]
  rw [h1, Finset.card_erase_of_mem (by simp [hb]), Finset.card_erase_of_mem (Finset.mem_univ _),
    Finset.card_univ, ZMod.card]
  omega

/-- n_q for q² ∣ h: no residue is excluded beyond j ≠ 0. -/
theorem count_units (q : ℕ) [NeZero q] :
    (Finset.univ.filter (fun j : ZMod q => j ≠ 0)).card = q - 1 := by
  have h1 : (Finset.univ.filter (fun j : ZMod q => j ≠ 0)) = Finset.univ.erase (0 : ZMod q) := by
    ext j; simp
  rw [h1, Finset.card_erase_of_mem (Finset.mem_univ _), Finset.card_univ, ZMod.card]

/-- Window lemma, real-line core: steps of length θ ≤ L cannot jump over [a, a + L]. -/
theorem window_step {x a θ L : ℝ} (hx : x < a) (hθ : 0 < θ) (hθL : θ ≤ L) :
    a ≤ x + (⌈(a - x) / θ⌉ : ℝ) * θ ∧ x + (⌈(a - x) / θ⌉ : ℝ) * θ ≤ a + L ∧
      (1 : ℤ) ≤ ⌈(a - x) / θ⌉ := by
  set k := ⌈(a - x) / θ⌉ with hk
  have hc1 : (a - x) / θ ≤ (k : ℝ) := Int.le_ceil _
  have hc2 : (k : ℝ) < (a - x) / θ + 1 := Int.ceil_lt_add_one _
  have hpos : 0 < (a - x) / θ := div_pos (by linarith) hθ
  refine ⟨?_, ?_, ?_⟩
  · have := (div_le_iff₀ hθ).mp hc1; linarith
  · have h3 : (k : ℝ) * θ < ((a - x) / θ + 1) * θ := mul_lt_mul_of_pos_right hc2 hθ
    have h4 : ((a - x) / θ + 1) * θ = (a - x) + θ := by field_simp
    linarith
  · have : (0 : ℝ) < k := lt_of_lt_of_le hpos hc1
    exact_mod_cast (show (0 : ℤ) < k by exact_mod_cast this)

/-- Window lemma constants of Theorem J: N = ⌈2π/θ_lo⌉ = 6 and (2π − θ_up)/θ ≤ 5 for θ ≥ θ_lo. -/
theorem window_N : ⌈2 * Real.pi / (1130677114 / 1000000000 : ℝ)⌉ = 6 ∧
    ∀ θ : ℝ, (1130677114 / 1000000000 : ℝ) ≤ θ →
      (2 * Real.pi - 1131054118 / 1000000000) / θ ≤ 5 := by
  have hlo := Real.pi_gt_d6
  have hhi := Real.pi_lt_d6
  constructor
  · rw [Int.ceil_eq_iff]
    constructor
    · rw [lt_div_iff₀ (by norm_num)]; push_cast; nlinarith
    · rw [div_le_iff₀ (by norm_num)]; push_cast; nlinarith
  · intro θ hθ
    have hθp : 0 < θ := lt_of_lt_of_le (by norm_num) hθ
    rw [div_le_iff₀ hθp]; nlinarith

#print axioms rank_core
#print axioms pell49_period
#print axioms pell49_periodic
#print axioms pell49_lambda_order
#print axioms count_excl_one
#print axioms count_units
#print axioms window_step
#print axioms window_N

end Bgs.LineJArith
