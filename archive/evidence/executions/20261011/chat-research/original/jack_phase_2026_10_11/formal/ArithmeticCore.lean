/-
UNCOMPILED DRAFT. Lean 4 and Mathlib are not installed in this environment.
This file covers only the real-arithmetic step after the Jack coefficient
identities have been proved. It does not formalize Jack polynomials, compact
groups, spherical functions or the point-process limit.
-/
import Mathlib

theorem jack_energy_denominator
    (N alpha K E : ℝ)
    (ha : 0 < alpha) (hK : 0 < K)
    (hE : 2 * K ^ 2 + 2 * (N - 1) * K / alpha ≤ E) :
    N + alpha * K ≤ 1 + alpha * E / (2 * K) := by
  have hne : alpha ≠ 0 := ne_of_gt ha
  have hscaled : alpha * (2 * K ^ 2 + 2 * (N - 1) * K / alpha)
      ≤ alpha * E := mul_le_mul_of_nonneg_left hE (le_of_lt ha)
  have hid : alpha * (2 * K ^ 2 + 2 * (N - 1) * K / alpha)
      = 2 * alpha * K ^ 2 + 2 * (N - 1) * K := by
    field_simp [hne]
    <;> ring
  rw [hid] at hscaled
  have hbound : (N + alpha * K - 1) * (2 * K) ≤ alpha * E := by
    nlinarith
  have hdiv : N + alpha * K - 1 ≤ alpha * E / (2 * K) :=
    (le_div_iff₀ (show 0 < 2 * K by positivity)).mpr hbound
  linarith

theorem jack_coefficient_arithmetic
    (N alpha K E c S : ℝ)
    (ha : 0 < alpha) (hK : 0 < K) (hc : 0 ≤ c)
    (hE : 2 * K ^ 2 + 2 * (N - 1) * K / alpha ≤ E)
    (hS : c * (1 + alpha * E / (2 * K)) ≤ S) :
    (N + alpha * K) * c ≤ S := by
  have hden := jack_energy_denominator N alpha K E ha hK hE
  have hmul := mul_le_mul_of_nonneg_right hden hc
  nlinarith

