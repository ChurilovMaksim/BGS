import Bgs.Fm001Statement

/-!
# BGS-FM-001 — proofs of the §1 Weyl dictionary and the §3 Fourier data

This module **proves** three of the `Prop`s stated (without proof) in
`Bgs.Fm001Statement` for `BGS-FM-001`
(`mathematics/fixed-map/fixed_model_symmetry_theorem.md`):

* `fm001_dictionary_holds : fm001_dictionary` — §1, the ordinary midpoint
  Weyl quantization of the corrected symbol `g` equals the raw frozen kick
  `A_N` (for every odd `N`; the proof is termwise and in fact does not use
  oddness);
* `fm001_fourier_weight_holds : fm001_fourier_weight` — §3,
  `∑_v (|Re c_v| + |Im c_v|) |v|² = 51451/1000`;
* `fm001_mode_count_holds : fm001_mode_count` — §3, exactly 32 nonzero
  Fourier modes in the support box.

Method: the coefficients are rewritten exactly as Gaussian integers over
`4000` (`d_v = 4000 c_v`, as in the source), and the finite sums are then
evaluated in `ℤ` by `decide`.  No `sorry`, no `native_decide`.

**Not formalized (partial coverage of FM-001):** the §2 dynamical
conclusions (Anosov property, conjugacy to `S`, trivial `C¹` centralizer,
no `C¹` reversor, no affine conjugacy) and the derivative bounds (5).
-/

namespace Bgs.Fm001Exact

open Bgs.Fm001Statement Bgs.TraceStatement Complex

/-- `4 · r̂(k)` as an integer. -/
def r4 (k : ℤ) : ℤ :=
  if k = 0 then 4
  else if k = 1 ∨ k = -1 then 2
  else if k = 7 ∨ k = -7 then -2
  else if k = 6 ∨ k = -6 ∨ k = 8 ∨ k = -8 then -1
  else 0

theorem rCoeff_eq (k : ℤ) : rCoeff k = (r4 k : ℂ) / 4 := by
  unfold rCoeff r4
  split_ifs <;> push_cast <;> norm_num

/-- Parity sign `(-1)^k` as an integer. -/
def sgn (k : ℤ) : ℤ := (-1) ^ k.natAbs

theorem neg_one_zpow_eq (k : ℤ) : ((-1 : ℂ) ^ k) = (sgn k : ℂ) := by
  unfold sgn
  rcases Int.even_or_odd k with h | h
  · rw [h.neg_one_zpow, (Int.natAbs_even.mpr h).neg_one_pow]; simp
  · rw [h.neg_one_zpow, (Int.natAbs_odd.mpr h).neg_one_pow]; simp

/-- Real part of `4000 · c_{kℓ}`. -/
def dRe (k l : ℤ) : ℤ :=
  if l = 0 then
    (if k = 7 ∨ k = -7 then 2000 else 0) + 100 * r4 k - (if k = 0 then 400 else 0)
  else if l = 1 then -3 * r4 k * sgn k
  else if l = -1 then -3 * r4 k * sgn k
  else 0

/-- Imaginary part of `4000 · c_{kℓ}`. -/
def dIm (k l : ℤ) : ℤ :=
  if l = 0 then -5 * (r4 (k - 1) - r4 (k + 1))
  else if l = 1 then -4 * r4 k * sgn k
  else if l = -1 then 4 * r4 k * sgn k
  else 0

theorem gCoeff_eq (k l : ℤ) :
    gCoeff k l = ((dRe k l : ℂ) + (dIm k l : ℂ) * I) / 4000 := by
  unfold gCoeff dRe dIm
  simp only [rCoeff_eq, neg_one_zpow_eq]
  split_ifs <;> push_cast <;> simp only [div_eq_mul_inv, mul_inv_rev, Complex.inv_I] <;> ring

theorem gCoeff_re (k l : ℤ) : (gCoeff k l).re = (dRe k l : ℝ) / 4000 := by
  rw [gCoeff_eq]; simp

theorem gCoeff_im (k l : ℤ) : (gCoeff k l).im = (dIm k l : ℝ) / 4000 := by
  rw [gCoeff_eq]; simp

theorem sgn_mul_self (k : ℤ) : sgn k * sgn k = 1 := by
  unfold sgn; rw [← pow_add, ← two_mul, pow_mul]; simp

/-- Termwise dictionary: `c^g_{kℓ} · (-1)^{ℓk} = c^f_{kℓ}` for all `(k, ℓ)`. -/
theorem gCoeff_mul_sign (k l : ℤ) :
    gCoeff k l * (-1 : ℂ) ^ (l * k) = fCoeff k l := by
  unfold gCoeff fCoeff
  by_cases h0 : l = 0
  · subst h0; simp
  by_cases h1 : l = 1
  · subst h1
    simp only [if_neg h0, ↓reduceIte, one_mul, neg_one_zpow_eq]
    have := sgn_mul_self k
    have hc : ((sgn k : ℂ)) * (sgn k : ℂ) = 1 := by exact_mod_cast this
    linear_combination (rCoeff k * ((-3 - 4 * I) / 1000)) * hc
  by_cases h2 : l = -1
  · subst h2
    simp only [if_neg h0, if_neg h1, ↓reduceIte, neg_one_mul, neg_one_zpow_eq]
    have := sgn_mul_self k
    have hs : sgn (-k) = sgn k := by unfold sgn; rw [Int.natAbs_neg]
    rw [hs]
    have hc : ((sgn k : ℂ)) * (sgn k : ℂ) = 1 := by exact_mod_cast this
    linear_combination (rCoeff k * ((-3 + 4 * I) / 1000)) * hc
  · simp [h0, h1, h2]

/-- **FM-001 §1 (proved).** For odd `N` the ordinary midpoint Weyl
quantization of the corrected symbol `g` is exactly the raw frozen kick
`A_N`. -/
theorem fm001_dictionary_holds : fm001_dictionary := by
  intro N _
  unfold ANordinary AN weylW
  refine Finset.sum_congr rfl (fun k _ => Finset.sum_congr rfl (fun l _ => ?_))
  rw [smul_smul, gCoeff_mul_sign]

/-- The integer weight `∑ (|Re d_v| + |Im d_v|) |v|²` with `d_v = 4000 c_v`. -/
theorem weight_int :
    (∑ k ∈ Finset.Icc (-9 : ℤ) 9, ∑ l ∈ Finset.Icc (-1 : ℤ) 1,
      (|dRe k l| + |dIm k l|) * (k ^ 2 + l ^ 2)) = 205804 := by
  decide

/-- **FM-001 §3, exact Fourier weight (proved).**
`∑_v (|Re c_v| + |Im c_v|) |v|² = 51451/1000`. -/
theorem fm001_fourier_weight_holds : fm001_fourier_weight := by
  unfold fm001_fourier_weight
  have h : ∀ k l : ℤ, (|(gCoeff k l).re| + |(gCoeff k l).im|) * ((k ^ 2 + l ^ 2 : ℤ) : ℝ)
      = (((|dRe k l| + |dIm k l|) * (k ^ 2 + l ^ 2) : ℤ) : ℝ) / 4000 := by
    intro k l
    rw [gCoeff_re, gCoeff_im, abs_div, abs_div]
    push_cast
    rw [abs_of_pos (by norm_num : (0 : ℝ) < 4000)]
    ring
  simp only [h, ← Finset.sum_div]
  simp only [← Int.cast_sum, weight_int]
  norm_num

theorem gCoeff_ne_zero_iff (k l : ℤ) : gCoeff k l ≠ 0 ↔ (dRe k l ≠ 0 ∨ dIm k l ≠ 0) := by
  rw [Ne, Complex.ext_iff, gCoeff_re, gCoeff_im]
  simp only [Complex.zero_re, Complex.zero_im]
  constructor
  · intro h
    by_contra hc
    push Not at hc
    exact h ⟨by simp [hc.1], by simp [hc.2]⟩
  · rintro h ⟨h1, h2⟩
    have e1 : (dRe k l : ℝ) = 0 := by linarith
    have e2 : (dIm k l : ℝ) = 0 := by linarith
    rcases h with h | h
    · exact h (by exact_mod_cast e1)
    · exact h (by exact_mod_cast e2)

/-- **FM-001 §3, mode count (proved).** Exactly 32 nonzero Fourier modes. -/
theorem fm001_mode_count_holds : fm001_mode_count := by
  unfold fm001_mode_count
  rw [Finset.filter_congr (fun p _ => gCoeff_ne_zero_iff p.1 p.2)]
  decide

end Bgs.Fm001Exact
