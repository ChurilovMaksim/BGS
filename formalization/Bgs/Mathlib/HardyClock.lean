module
public import Mathlib
@[expose] public section

/-!
# Hardy remainder weights for the radial clock extremum (BGS-TRACE-091)

The radial secular statistic of `mathematics/trace-bridge/hardy_spectral_remainder.md`
has the explicit remainder
`E(z) = (∑_{k=1}^{N-1} c_k d_k(a,b) z^k) / p(bz)` with weights
`d_k(a,b) = a^k - A b^k - D b^{N-k}`,
`A = (1 - a^N b^N)/(1 - b^{2N})`, `D = (a^N - b^N)/(1 - b^{2N})`.

This file formalizes the elementary ingredients of the equality classification
and of the CUE positivity statement:

* `hardyWeight_zero`, `hardyWeight_N`: the endpoint weights vanish;
* `hardyWeight_pos`: **every interior weight is strictly positive** for
  `0 < b < a < 1` (discrete maximum principle, §2.2 of the note);
* `abel_equality_obstruction`: the inequality
  `r^{-2k} + r^{-2(N-k)} < 1 + r^{-2N}` used in §4 to exclude equality
  away from the clock;
* `cue_hardy_excess_pos`: the limiting CUE excess (13) is strictly positive,
  `(t-s)^2 (1 - e^{-2s})/(4st) > (e^{-s} - e^{-t})^2/(1 - e^{-2t})` for `0 < s < t`.
-/

open Real

namespace Bgs.Mathlib

/-- The coefficient `A = (1 - a^N b^N)/(1 - b^{2N})`. -/
noncomputable def hardyA (N : ℕ) (a b : ℝ) : ℝ := (1 - a ^ N * b ^ N) / (1 - b ^ (2 * N))

/-- The coefficient `D = (a^N - b^N)/(1 - b^{2N})`. -/
noncomputable def hardyD (N : ℕ) (a b : ℝ) : ℝ := (a ^ N - b ^ N) / (1 - b ^ (2 * N))

/-- The Hardy remainder weights `d_k = a^k - A b^k - D b^{N-k}` (for `k ≤ N`). -/
noncomputable def hardyWeight (N : ℕ) (a b : ℝ) (k : ℕ) : ℝ :=
  a ^ k - hardyA N a b * b ^ k - hardyD N a b * b ^ (N - k)

section weights

variable {N : ℕ} {a b : ℝ}

lemma one_sub_b_pow_ne (hb0 : 0 < b) (hb1 : b < 1) (hN : 1 ≤ N) : 1 - b ^ (2 * N) ≠ 0 := by
  have : b ^ (2 * N) < 1 := pow_lt_one₀ hb0.le hb1 (by omega)
  linarith

theorem hardyWeight_zero (hb0 : 0 < b) (hb1 : b < 1) (hN : 1 ≤ N) :
    hardyWeight N a b 0 = 0 := by
  have h := one_sub_b_pow_ne hb0 hb1 hN
  simp only [hardyWeight, hardyA, hardyD, pow_zero, Nat.sub_zero]
  field_simp
  ring_nf

theorem hardyWeight_N (hb0 : 0 < b) (hb1 : b < 1) (hN : 1 ≤ N) :
    hardyWeight N a b N = 0 := by
  have h := one_sub_b_pow_ne hb0 hb1 hN
  simp only [hardyWeight, hardyA, hardyD, Nat.sub_self, pow_zero]
  field_simp
  rw [pow_mul]
  ring

/-- The second-difference identity
`d_{k+1} - (b + b⁻¹) d_k + d_{k-1} = (a + a⁻¹ - b - b⁻¹) a^k` for `1 ≤ k < N`. -/
theorem hardyWeight_second_difference (ha : 0 < a) (hb : 0 < b) {k : ℕ} (hk1 : 1 ≤ k)
    (hkN : k < N) :
    hardyWeight N a b (k + 1) - (b + b⁻¹) * hardyWeight N a b k + hardyWeight N a b (k - 1) =
      (a + a⁻¹ - b - b⁻¹) * a ^ k := by
  obtain ⟨j, rfl⟩ : ∃ j, k = j + 1 := ⟨k - 1, by omega⟩
  obtain ⟨i, hi⟩ : ∃ i, N - (j + 1) = i + 1 := ⟨N - (j + 1) - 1, by omega⟩
  have h1 : N - (j + 1 + 1) = i := by omega
  have h2 : N - (j + 1 - 1) = i + 2 := by omega
  have h3 : N - j = i + 2 := by omega
  simp only [hardyWeight, hi, h1, h3, Nat.add_sub_cancel]
  field_simp
  ring

/-- `x + x⁻¹` is strictly decreasing on `(0, 1)`. -/
lemma add_inv_lt_add_inv (hb : 0 < b) (hba : b < a) (ha1 : a < 1) :
    a + a⁻¹ < b + b⁻¹ := by
  have ha : 0 < a := hb.trans hba
  have e : b + b⁻¹ - (a + a⁻¹) = (a - b) * (1 - a * b) / (a * b) := by field_simp; ring
  have hab : a * b < 1 := by nlinarith
  have : 0 < (a - b) * (1 - a * b) / (a * b) := by
    apply div_pos (mul_pos (by linarith) (by linarith)) (by positivity)
  linarith

/-- **TRACE-091, §2.2.**  For `0 < b < a < 1` and `1 ≤ k ≤ N - 1`, the Hardy
remainder weight `d_k(a,b)` is strictly positive. -/
theorem hardyWeight_pos (hb : 0 < b) (hba : b < a) (ha1 : a < 1) {k : ℕ} (hk1 : 1 ≤ k)
    (hkN : k < N) : 0 < hardyWeight N a b k := by
  have ha : 0 < a := hb.trans hba
  have hN : 1 ≤ N := by omega
  have hb1 : b < 1 := hba.trans ha1
  -- minimum of `d` over the interior
  set S := Finset.Icc 1 (N - 1) with hS
  have hne : S.Nonempty := ⟨k, by simp [hS]; omega⟩
  obtain ⟨m, hmS, hmin⟩ := S.exists_min_image (hardyWeight N a b) hne
  simp only [hS, Finset.mem_Icc] at hmS
  suffices 0 < hardyWeight N a b m from
    lt_of_lt_of_le this (hmin k (by simp [hS]; omega))
  by_contra hcon
  push Not at hcon
  -- neighbours are at least `d_m`
  have hnext : hardyWeight N a b m ≤ hardyWeight N a b (m + 1) := by
    rcases Nat.lt_or_ge (m + 1) N with h | h
    · exact hmin _ (by simp [hS]; omega)
    · have : m + 1 = N := by omega
      rw [this, hardyWeight_N hb hb1 hN]; exact hcon
  have hprev : hardyWeight N a b m ≤ hardyWeight N a b (m - 1) := by
    rcases Nat.lt_or_ge 1 m with h | h
    · exact hmin _ (by simp [hS]; omega)
    · have : m - 1 = 0 := by omega
      rw [this, hardyWeight_zero hb hb1 hN]; exact hcon
  have hL := hardyWeight_second_difference (N := N) ha hb hmS.1 (by omega)
  have hdec := add_inv_lt_add_inv hb hba ha1
  have hpow : 0 < a ^ m := pow_pos ha m
  have h2 : 2 ≤ b + b⁻¹ := by
    have : 0 ≤ (b - 1) ^ 2 / b := by positivity
    have e : (b - 1) ^ 2 / b = b + b⁻¹ - 2 := by field_simp; ring
    linarith
  -- LHS of `hL` is ≥ (2 - b - b⁻¹) d_m ≥ 0, RHS is < 0
  have : 0 ≤ (2 - (b + b⁻¹)) * hardyWeight N a b m :=
    mul_nonneg_of_nonpos_of_nonpos (by linarith) hcon
  nlinarith

end weights

/-- **TRACE-091, §4.**  For `0 < r < 1` and `0 < k < N`,
`r^{-2k} + r^{-2(N-k)} < 1 + r^{-2N}`; this is the inequality excluding equality
in the Abel sum-of-squares identity away from the regular clock. -/
theorem abel_equality_obstruction {r : ℝ} (hr0 : 0 < r) (hr1 : r < 1) {N k : ℕ}
    (hk : 0 < k) (hkN : k < N) :
    (r ^ (2 * k))⁻¹ + (r ^ (2 * (N - k)))⁻¹ < 1 + (r ^ (2 * N))⁻¹ := by
  have hu : 1 < (r ^ (2 * k))⁻¹ := one_lt_inv₀ (by positivity) |>.2 (pow_lt_one₀ hr0.le hr1 (by omega))
  have hv : 1 < (r ^ (2 * (N - k)))⁻¹ :=
    one_lt_inv₀ (by positivity) |>.2 (pow_lt_one₀ hr0.le hr1 (by omega))
  have hprod : (r ^ (2 * N))⁻¹ = (r ^ (2 * k))⁻¹ * (r ^ (2 * (N - k)))⁻¹ := by
    rw [← mul_inv, ← pow_add]; congr 2; omega
  rw [hprod]
  nlinarith

/-! ### Positivity of the limiting CUE Hardy excess -/

/-- `tanh x ≤ x`, i.e. `sinh x ≤ x cosh x` for `x ≥ 0` (re-proved locally). -/
lemma sinh_le_mul_cosh' {x : ℝ} (hx : 0 ≤ x) : Real.sinh x ≤ x * Real.cosh x := by
  -- `g(x) = x cosh x - sinh x` has derivative `x sinh x ≥ 0`
  let g : ℝ → ℝ := fun t => t * Real.cosh t - Real.sinh t
  have hg : ∀ t, HasDerivAt g (t * Real.sinh t) t := by
    intro t
    have := ((hasDerivAt_id' t).mul (Real.hasDerivAt_cosh t)).sub (Real.hasDerivAt_sinh t)
    convert! this using 1
    ring
  have hmono : MonotoneOn g (Set.Ici 0) := by
    apply monotoneOn_of_deriv_nonneg (convex_Ici 0)
    · exact fun t _ => (hg t).continuousAt.continuousWithinAt
    · exact fun t _ => (hg t).differentiableAt.differentiableWithinAt
    · intro t ht
      rw [interior_Ici] at ht
      rw [(hg t).deriv]
      exact mul_nonneg (le_of_lt ht) (Real.sinh_nonneg_iff.2 (le_of_lt ht))
  have := hmono (Set.mem_Ici.2 le_rfl) (Set.mem_Ici.2 hx) hx
  simp [g] at this
  linarith

/-- `sinh x / x` is strictly increasing on `(0, ∞)`. -/
lemma sinh_div_strictMonoOn : StrictMonoOn (fun x : ℝ => Real.sinh x / x) (Set.Ioi 0) := by
  have hd : ∀ x : ℝ, 0 < x →
      HasDerivAt (fun x : ℝ => Real.sinh x / x) ((x * Real.cosh x - Real.sinh x) / x ^ 2) x := by
    intro x hx
    have := (Real.hasDerivAt_sinh x).div (hasDerivAt_id' x) hx.ne'
    convert! this using 1
    ring
  apply strictMonoOn_of_deriv_pos (convex_Ioi 0)
  · exact fun x hx => (hd x hx).continuousAt.continuousWithinAt
  · intro x hx
    rw [interior_Ioi] at hx
    have hx' : (0 : ℝ) < x := hx
    rw [(hd x hx).deriv]
    apply div_pos _ (by positivity)
    have h1 := sinh_le_mul_cosh' (le_of_lt (half_pos hx'))
    have hs : Real.sinh x = 2 * Real.sinh (x / 2) * Real.cosh (x / 2) := by
      rw [← Real.sinh_two_mul]; ring_nf
    have hc : Real.cosh x = Real.cosh (x / 2) ^ 2 + Real.sinh (x / 2) ^ 2 := by
      have := Real.cosh_two_mul (x / 2)
      rw [show 2 * (x / 2) = x by ring] at this
      exact this
    have hsh : 0 < Real.sinh (x / 2) := Real.sinh_pos_iff.2 (half_pos hx')
    have hch : 0 < Real.cosh (x / 2) := Real.cosh_pos _
    rw [hs, hc]
    nlinarith [mul_pos hsh hch, mul_pos (mul_pos hx' hsh) hsh]

lemma one_lt_sinh_div {x : ℝ} (hx : 0 < x) : 1 < Real.sinh x / x := by
  rw [lt_div_iff₀ hx, one_mul]
  exact Real.self_lt_sinh_iff.2 hx

/-- **TRACE-091, (13).**  The microscopic CUE mean of the Hardy remainder is strictly
positive: for `0 < s < t`,
`(e^{-s} - e^{-t})^2/(1 - e^{-2t}) < (t-s)^2 (1 - e^{-2s})/(4 s t)`. -/
theorem cue_hardy_excess_pos {s t : ℝ} (hs : 0 < s) (hst : s < t) :
    (Real.exp (-s) - Real.exp (-t)) ^ 2 / (1 - Real.exp (-2 * t)) <
      (t - s) ^ 2 * (1 - Real.exp (-2 * s)) / (4 * s * t) := by
  have ht : 0 < t := hs.trans hst
  set h := (t - s) / 2 with hh
  have hh0 : 0 < h := by rw [hh]; linarith
  -- hyperbolic rewriting
  have e1 : Real.exp (-s) - Real.exp (-t) = 2 * Real.exp (-(s + t) / 2) * Real.sinh h := by
    rw [Real.sinh_eq, show 2 * Real.exp (-(s + t) / 2) * ((Real.exp h - Real.exp (-h)) / 2) =
      Real.exp (-(s + t) / 2) * Real.exp h - Real.exp (-(s + t) / 2) * Real.exp (-h) by ring,
      ← Real.exp_add, ← Real.exp_add]
    congr 1 <;> congr 1 <;> rw [hh] <;> ring
  have e2 : 1 - Real.exp (-2 * t) = 2 * Real.exp (-t) * Real.sinh t := by
    rw [Real.sinh_eq]; field_simp
    rw [mul_sub, ← Real.exp_add, ← Real.exp_add]; ring_nf; rw [Real.exp_zero]; ring
  have e3 : 1 - Real.exp (-2 * s) = 2 * Real.exp (-s) * Real.sinh s := by
    rw [Real.sinh_eq]; field_simp
    rw [mul_sub, ← Real.exp_add, ← Real.exp_add]; ring_nf; rw [Real.exp_zero]; ring
  have hsht : 0 < Real.sinh t := Real.sinh_pos_iff.2 ht
  have hshs : 0 < Real.sinh s := Real.sinh_pos_iff.2 hs
  have hshh : 0 < Real.sinh h := Real.sinh_pos_iff.2 hh0
  -- the key chain `(sinh h / h)^2 ≤ sinh(2h)/(2h) < sinh t / t < (sinh s/s)(sinh t/t)`
  have k1 : (Real.sinh h / h) ^ 2 ≤ Real.sinh (2 * h) / (2 * h) := by
    rw [Real.sinh_two_mul, div_pow]
    rw [div_le_div_iff₀ (by positivity) (by positivity)]
    have := sinh_le_mul_cosh' hh0.le
    nlinarith [mul_pos hshh hh0]
  have k2 : Real.sinh (2 * h) / (2 * h) < Real.sinh t / t :=
    sinh_div_strictMonoOn (show (0 : ℝ) < 2 * h by positivity) ht (by rw [hh]; linarith)
  have k3 : Real.sinh t / t < (Real.sinh s / s) * (Real.sinh t / t) := by
    have := one_lt_sinh_div hs
    have : 0 < Real.sinh t / t := by positivity
    nlinarith
  have key : (Real.sinh h / h) ^ 2 < (Real.sinh s / s) * (Real.sinh t / t) := by linarith
  rw [e1, e2, e3]
  have hts : t - s = 2 * h := by rw [hh]; ring
  rw [hts]
  have hE : Real.exp (-(s + t) / 2) ^ 2 = Real.exp (-s) * Real.exp (-t) := by
    rw [← Real.exp_nat_mul, ← Real.exp_add]; congr 1; push_cast; ring
  rw [div_lt_div_iff₀ (by positivity) (by positivity)]
  have hes : 0 < Real.exp (-s) := Real.exp_pos _
  have het : 0 < Real.exp (-t) := Real.exp_pos _
  rw [div_pow, div_mul_div_comm, div_lt_div_iff₀ (by positivity) (by positivity)] at key
  have : (2 * Real.exp (-(s + t) / 2) * Real.sinh h) ^ 2 * (4 * s * t) =
      16 * (Real.exp (-s) * Real.exp (-t)) * (Real.sinh h ^ 2 * (s * t)) := by
    rw [← hE]; ring
  rw [this]
  have : (2 * h) ^ 2 * (2 * Real.exp (-s) * Real.sinh s) * (2 * Real.exp (-t) * Real.sinh t) =
      16 * (Real.exp (-s) * Real.exp (-t)) * (Real.sinh s * Real.sinh t * h ^ 2) := by ring
  rw [this]
  apply mul_lt_mul_of_pos_left _ (by positivity)
  linarith

#print axioms one_sub_b_pow_ne
#print axioms hardyWeight_zero
#print axioms hardyWeight_N
#print axioms hardyWeight_second_difference
#print axioms add_inv_lt_add_inv
#print axioms hardyWeight_pos
#print axioms abel_equality_obstruction
#print axioms sinh_le_mul_cosh'
#print axioms sinh_div_strictMonoOn
#print axioms one_lt_sinh_div
#print axioms cue_hardy_excess_pos
end Bgs.Mathlib
