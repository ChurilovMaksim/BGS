import Mathlib

/-!
# BGS-TRACE-273 — Line M M4b: the inclusion step `|Z_ρ|² ≥ 4 m h ⇒ every d ∣ h, 1 < d ≤ √h, is included`

Source: registry statement of `BGS-TRACE-273`.  The frozen (±2,8) inclusion rule includes a level `d ∣ h` when
`|Z_ρ|²/d² ≥ 4m`.

* `included_of_bound` : if `|Z_ρ|² ≥ 4 m h` and `d² ≤ h` (`d ≥ 1`), then `|Z_ρ|²/d² ≥ 4m`;
* `included_all` : the same for every divisor `d ∣ h` with `1 < d` and `d ≤ √h` (no borderline level).

**Partial coverage:** only this deduction is formalized.  The certified Line F F3 lower bound
`|Z_ρ| ≥ (1/2)(1 − λ^{−m})(μ_lo^m − 3012.4)`, the interval check `|Z_ρ|² ≥ 4 m h_m` for odd `m ∈ [15, 20001]`, the
monotonicity argument beyond, and the `m = 9, 11, 13` remarks are **not** formalized; they enter as the hypothesis
`hZ`.  All proofs are kernel-checked.
-/

namespace Bgs.LineMInclusion

theorem included_of_bound (Z2 : ℝ) (m h d : ℕ) (hZ : 4 * (m : ℝ) * h ≤ Z2) (hd : 1 ≤ d) (hdh : d ^ 2 ≤ h) :
    4 * (m : ℝ) ≤ Z2 / (d : ℝ) ^ 2 := by
  have hd0 : (0 : ℝ) < (d : ℝ) ^ 2 := by positivity
  rw [le_div_iff₀ hd0]
  have : ((d : ℝ) ^ 2) ≤ h := by exact_mod_cast hdh
  have hm : (0 : ℝ) ≤ 4 * m := by positivity
  nlinarith

theorem included_all (Z2 : ℝ) (m h : ℕ) (hZ : 4 * (m : ℝ) * h ≤ Z2) :
    ∀ d ∈ h.divisors, 1 < d → (d : ℝ) ≤ Real.sqrt h → 4 * (m : ℝ) ≤ Z2 / (d : ℝ) ^ 2 := by
  intro d _ hd1 hds
  refine included_of_bound Z2 m h d hZ hd1.le ?_
  have h0 : (0 : ℝ) ≤ d := by positivity
  have : (d : ℝ) ^ 2 ≤ h := by
    calc (d : ℝ) ^ 2 ≤ (Real.sqrt h) ^ 2 := pow_le_pow_left₀ h0 hds 2
      _ = h := Real.sq_sqrt (by positivity)
  exact_mod_cast this

end Bgs.LineMInclusion
