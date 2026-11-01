import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.Real.Pi.Bounds

/-!
# BGS-RES-023 — arithmetic link from the deposited margin integer `B` to the printed (ND.10) constant

Source: registry boundary of `BGS-RES-023`; data:
`evidence/executions/20261006/corpus-revision/final/checks/certificates-mpuvq_28/resonance_nondegeneracy_margin.json`
(field `B`, `B_bit_length = 712`, `B_le_2_pow_714 = true`).

* `B_bit_length` : the deposited integer `B` has exactly 712 binary digits (`2^711 ≤ B < 2^712`);
* `B_le_two_pow_714` : `B ≤ 2^714`;
* `nd10_of_margin` : for any `Γ` and any `X ≥ 0` (standing for `‖g‖₂⁴`),
  `Γ ≥ (π²/41472)·2^(−2B)·X` implies the printed (ND.10) bound `Γ ≥ (π²/41472)·2^(−2^715)·X`.

**Partial coverage:** this is only the final arithmetic step of the claim.  The bound
`Γ_T(g) ≥ (π²/41472)·2^(−2B)‖g‖₂⁴` on `P_8` itself rests on the deposited radius-eight certificate (5,704
deductions, replayed by `check_resonance_certificate.py`) and the margin compiler
(`resonance_nondegeneracy_margin.py`); neither the certificate replay nor the compilation of `B` is formalized.
The value of `B` is copied verbatim from the deposited JSON.  All proofs are kernel-checked.
-/

namespace Bgs.ResonanceMarginConst

set_option exponentiation.threshold 1024

/-- The deposited margin integer `B` (verbatim from `resonance_nondegeneracy_margin.json`). -/
def B : ℕ :=
  10903138006885609236303645681036445652092448503236660095433749448140870687126503932503067765649880683195400080147209105771921647025190251832351509507048924272543297838428942812751161026711828729692160000000000000000

theorem B_bit_length : 2 ^ 711 ≤ B ∧ B < 2 ^ 712 := by
  unfold B; constructor <;> decide +kernel

theorem B_le_two_pow_714 : B ≤ 2 ^ 714 := by
  unfold B; decide +kernel

/-- `B ≤ 2^714` gives `2^(−2B) ≥ 2^(−2^715)`, hence (ND.10) with the printed constant. -/
theorem nd10_of_margin (Γ X : ℝ) (hX : 0 ≤ X)
    (h : (Real.pi ^ 2 / 41472) * (2 : ℝ) ^ (-(2 * (B : ℝ))) * X ≤ Γ) :
    (Real.pi ^ 2 / 41472) * (2 : ℝ) ^ (-((2 : ℝ) ^ (715 : ℕ))) * X ≤ Γ := by
  refine le_trans ?_ h
  have hB : (B : ℝ) ≤ (2 : ℝ) ^ (714 : ℕ) := by exact_mod_cast B_le_two_pow_714
  have hexp : -((2 : ℝ) ^ (715 : ℕ)) ≤ -(2 * (B : ℝ)) := by
    have : (2 : ℝ) ^ (715 : ℕ) = 2 * (2 : ℝ) ^ (714 : ℕ) := by rw [pow_succ]; ring
    rw [this]; linarith
  have hpow : (2 : ℝ) ^ (-((2 : ℝ) ^ (715 : ℕ))) ≤ (2 : ℝ) ^ (-(2 * (B : ℝ))) :=
    Real.rpow_le_rpow_of_exponent_le (by norm_num) hexp
  have hc : 0 ≤ Real.pi ^ 2 / 41472 := by positivity
  exact mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left hpow hc) hX

end Bgs.ResonanceMarginConst
