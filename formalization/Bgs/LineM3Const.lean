import Bgs.LineN16Arith

/-!
# BGS-TRACE-271 — Line M M3 constant arithmetic (part (c) only)

Source: `mathematics/fixed-map/lineMN_conductor_structure.md`, M3;
registry boundary of `BGS-TRACE-271`, part (c): with `μ_lo = 1.9154712`
and `λ = 3 + 2√2`,

* `rate_ge_113287` : `μ_lo² / λ^{2/3} ≥ 1.13287` (registered lower bound
  of the per-level floor rate `1.1328794`);
* `excess_ge_111238` : `μ_lo² / (λ^{2/3} · 1.0184224) ≥ 1.11238`, i.e. the
  floor rate exceeds the D7 demand rate `1.0184224` (BGS-TRACE-225) by a
  factor of at least `1.11238` (registered lower bound of `1.1123866`).

Remark (recorded, not a change of the claim): the ratio must be taken with
the unrounded rate; the rounded quotient `1.13287 / 1.0184224 = 1.1123773…`
is *below* `1.11238`.  The theorem below uses the exact expression.

Both are reduced to polynomial inequalities in `√2` (the first is
`Bgs.LineN16.scale_gt_113287`).  **Not formalized (partial coverage):**
parts (a), (b), (d), (e) of M3 — level inclusion, openness of the
conductor, the Prop K2 per-level bound and the Line F certified bound on
`|Z_ρ|`.  No `sorry`, no `native_decide`.
-/

namespace Bgs.LineM3Const

open Real

theorem lam_pos : (0 : ℝ) < 3 + 2 * √2 := by positivity

theorem lam_sq : (3 + 2 * √2 : ℝ) ^ 2 = 17 + 12 * √2 := by
  have h : (√2 : ℝ) ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  nlinarith [h]

/-- `(λ^{2/3})³ = λ²`. -/
theorem rpow_cube : ((3 + 2 * √2 : ℝ) ^ ((2 : ℝ) / 3)) ^ 3 = (3 + 2 * √2) ^ 2 := by
  rw [← Real.rpow_natCast, ← Real.rpow_mul lam_pos.le]
  norm_num

/-- Reduction: `c ≤ μ² / λ^{2/3}` follows from `c³ λ² ≤ μ⁶` for `c ≥ 0`. -/
theorem le_of_cube (c μ : ℝ) (hc : 0 ≤ c) (h : c ^ 3 * (17 + 12 * √2) ≤ μ ^ 6) :
    c ≤ μ ^ 2 / (3 + 2 * √2 : ℝ) ^ ((2 : ℝ) / 3) := by
  have hy : (0 : ℝ) < (3 + 2 * √2 : ℝ) ^ ((2 : ℝ) / 3) := Real.rpow_pos_of_pos lam_pos _
  rw [le_div_iff₀ hy]
  have h3 : (c * (3 + 2 * √2 : ℝ) ^ ((2 : ℝ) / 3)) ^ 3 ≤ (μ ^ 2) ^ 3 := by
    rw [mul_pow, rpow_cube, lam_sq, ← pow_mul]; simpa using h
  exact (pow_le_pow_iff_left₀ (by positivity) (by positivity) (by norm_num)).mp h3

/-- **M3 (c), floor rate:** `μ_lo² / λ^{2/3} ≥ 1.13287`. -/
theorem rate_ge_113287 :
    (1.13287 : ℝ) ≤ (1.9154712 : ℝ) ^ 2 / (3 + 2 * √2 : ℝ) ^ ((2 : ℝ) / 3) :=
  le_of_cube _ _ (by norm_num) Bgs.LineN16.scale_gt_113287.le

/-- **M3 (c), excess over the D7 demand:**
`μ_lo² / (λ^{2/3} · 1.0184224) ≥ 1.11238`. -/
theorem excess_ge_111238 :
    (1.11238 : ℝ) ≤ (1.9154712 : ℝ) ^ 2 / ((3 + 2 * √2 : ℝ) ^ ((2 : ℝ) / 3) * 1.0184224) := by
  have hs : √2 < (1.41421357 : ℝ) := by
    rw [Real.sqrt_lt' (by norm_num)]; norm_num
  have hpoly : (1.11238 * 1.0184224 : ℝ) ^ 3 * (17 + 12 * √2) ≤ 1.9154712 ^ 6 := by
    have : (1.11238 * 1.0184224 : ℝ) ^ 3 * (17 + 12 * 1.41421357) < 1.9154712 ^ 6 := by
      norm_num
    nlinarith [hs]
  have h := le_of_cube _ _ (by norm_num) hpoly
  rw [div_mul_eq_div_div, le_div_iff₀ (by norm_num : (0 : ℝ) < 1.0184224)]
  exact h

end Bgs.LineM3Const
