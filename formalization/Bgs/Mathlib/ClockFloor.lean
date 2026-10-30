module
public import Bgs.Mathlib.AbelPoisson
@[expose] public section

/-!
# The universal clock floor `L_N(s) ≥ 1/(e^{2s} - 1)` (BGS-TRACE-007 / TRACE-092 §1)

For every unitary spectrum `x : Fin N → ℝ` and every `s > 0`,

  `L_N(s) = N⁻² ∑_{m≥1} e^{-2sm/N} |Tr U^m|² ≥ 1/(e^{2s} - 1)`,

with equality for the `N`-clock (`abelL_clock`).  The proof is a fully explicit,
elementary linear-programming certificate on the circle, equivalent to the
repository's decomposition (2) of TRACE-092: with `q = e^{-2s/N}` the Poisson kernel
`P(θ) = ∑_{m∈ℤ} q^{|m|} cos(mθ)` splits as `P = G + H`, where

* `G(θ) = ∑_{|m|<N} ĝ_m cos(mθ)` is a cosine polynomial with
  `ĝ_m = (sinh(2u) - 2u)/(2 sinh² s) ≥ 0`, `u = s(1 - |m|/N)`;
* `H(θ) = (N s/ sinh² s) · [Fej_N(θ)/N - sin²(Nθ/2) P(θ)/(N s)] ≥ 0` pointwise, where
  `Fej_N(θ) = ∑_{|m|<N} (1 - |m|/N) cos(mθ)`, and `H(0) = N s / sinh² s`.

Then `∑_{j,k} P(θ_j - θ_k) ≥ ĝ₀ N² + N H(0) = N² coth s`, which is the floor.
-/

open Real BigOperators Filter

namespace Bgs.Mathlib

/-! ## Coefficients -/

section Coeffs

variable (N : ℕ) (s : ℝ)

/-- `q = e^{-2s/N}`. -/
noncomputable def qN : ℝ := Real.exp (-2 * s / N)

/-- Poisson coefficients `q^{|m|}`. -/
noncomputable def pc (m : ℤ) : ℝ := qN N s ^ m.natAbs

/-- Fejér coefficients `(1 - |m|/N)₊`. -/
noncomputable def fejc (m : ℤ) : ℝ := if m.natAbs < N then 1 - (m.natAbs : ℝ) / N else 0

/-- Coefficients of `sin²(Nθ/2) P(θ)`. -/
noncomputable def sc (m : ℤ) : ℝ :=
  pc N s m / 2 - (pc N s (m - N) + pc N s (m + N)) / 4

/-- The constant `C = N s / sinh² s`. -/
noncomputable def cC : ℝ := N * s / Real.sinh s ^ 2

/-- Coefficients of the nonnegative part `H`. -/
noncomputable def hc (m : ℤ) : ℝ := cC N s * (fejc N m / N - sc N s m / (N * s))

/-- Coefficients of the positive-definite part `G = P - H`. -/
noncomputable def gc (m : ℤ) : ℝ := pc N s m - hc N s m

end Coeffs

/-- The Fejér cosine polynomial `Fej_N(θ) = ∑_{|m|<N} (1 - |m|/N) cos(mθ)`, written as
`(2 ∑_{k<N} (N-k) cos(kθ) - N)/N`. -/
noncomputable def fejSum (N : ℕ) (θ : ℝ) : ℝ :=
  (2 * ∑ k ∈ Finset.range N, ((N : ℝ) - k) * Real.cos (k * θ) - N) / N

/-- The nonnegative part `H(θ)`. -/
noncomputable def Hfun (N : ℕ) (s θ : ℝ) : ℝ :=
  cC N s * (fejSum N θ / N - Real.sin (N * θ / 2) ^ 2 * poissonKernel (qN N s) θ / (N * s))

variable {N : ℕ} {s : ℝ}

theorem qN_pos : 0 < qN N s := Real.exp_pos _

theorem qN_lt_one (hN : 1 ≤ N) (hs : 0 < s) : qN N s < 1 := by
  have : (0 : ℝ) < N := by exact_mod_cast hN
  exact exp_lt_one_of_neg' (div_neg_of_neg_of_pos (by linarith) this)

theorem qN_pow_N (hN : 1 ≤ N) : qN N s ^ N = Real.exp (-2 * s) := by
  have : (N : ℝ) ≠ 0 := by have : (0 : ℝ) < N := by exact_mod_cast hN
                           exact this.ne'
  rw [qN, ← Real.exp_nat_mul]; congr 1; field_simp

theorem sinh_sq_mul_exp (s : ℝ) :
    4 * Real.sinh s ^ 2 * Real.exp (-2 * s) = (1 - Real.exp (-2 * s)) ^ 2 := by
  have hE : Real.exp s * Real.exp (-s) = 1 := by rw [← Real.exp_add]; simp
  rw [Real.sinh_eq, show -2 * s = -s + -s by ring, Real.exp_add]
  linear_combination (Real.exp s * Real.exp (-s) + 1 - 2 * Real.exp (-s) ^ 2) * hE

/-- `G` has no coefficients at `|m| ≥ N`. -/
theorem gc_eq_zero (hN : 1 ≤ N) (hs : 0 < s) {m : ℤ} (hm : N ≤ m.natAbs) : gc N s m = 0 := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  have hsh : Real.sinh s ≠ 0 := (Real.sinh_pos_iff.2 hs).ne'
  have hfej : fejc N m = 0 := by simp only [fejc]; split_ifs <;> first | rfl | omega
  set k := m.natAbs with hkdef
  have habs : ((m - N).natAbs = k - N ∧ (m + N).natAbs = k + N) ∨
      ((m - N).natAbs = k + N ∧ (m + N).natAbs = k - N) := by omega
  have key : pc N s (m - N) + pc N s (m + N) = qN N s ^ (k - N) + qN N s ^ (k + N) := by
    rcases habs with ⟨h1, h2⟩ | ⟨h1, h2⟩
    · simp only [pc, h1, h2]
    · simp only [pc, h1, h2]; ring
  have hk : qN N s ^ k = qN N s ^ (k - N) * qN N s ^ N := by
    rw [← pow_add]; congr 1; omega
  have hk2 : qN N s ^ (k + N) = qN N s ^ (k - N) * qN N s ^ N * qN N s ^ N := by
    rw [← pow_add, ← pow_add]; congr 1; omega
  have hpc : pc N s m = qN N s ^ k := rfl
  simp only [gc, hc, sc, cC, hfej, key, hpc]
  rw [hk, hk2, qN_pow_N hN]
  have hrel := sinh_sq_mul_exp s
  generalize Real.exp (-2 * s) = Q at hrel ⊢
  generalize qN N s ^ (k - N) = r
  field_simp
  have h2 : r * (4 * Real.sinh s ^ 2 * Q) = r * (1 - Q) ^ 2 := by rw [hrel]
  ring_nf at h2 ⊢
  linarith

theorem qN_pow (j : ℕ) : qN N s ^ j = Real.exp (-2 * s * j / N) := by
  rw [qN, ← Real.exp_nat_mul]; congr 1; ring

theorem four_sinh_sq (s : ℝ) : 4 * Real.sinh s ^ 2 = Real.exp (2 * s) - 2 + Real.exp (-2 * s) := by
  have hE : Real.exp s * Real.exp (-s) = 1 := by rw [← Real.exp_add]; simp
  rw [Real.sinh_eq, show 2 * s = s + s by ring, show -2 * s = -s + -s by ring, Real.exp_add,
    Real.exp_add]
  have h2 : (Real.exp s - Real.exp (-s)) ^ 2 =
      Real.exp s * Real.exp s - 2 * (Real.exp s * Real.exp (-s)) + Real.exp (-s) * Real.exp (-s) := by
    ring
  rw [hE] at h2
  linarith [h2]

/-- Explicit `G` coefficients at `|m| < N`. -/
theorem gc_eq_of_lt (hN : 1 ≤ N) (hs : 0 < s) {m : ℤ} (hm : m.natAbs < N) :
    gc N s m = (Real.sinh (2 * (s * (1 - (m.natAbs : ℝ) / N))) - 2 * (s * (1 - (m.natAbs : ℝ) / N)))
      / (2 * Real.sinh s ^ 2) := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  have hsh : Real.sinh s ≠ 0 := (Real.sinh_pos_iff.2 hs).ne'
  set k := m.natAbs with hkdef
  have hfej : fejc N m = 1 - (k : ℝ) / N := by simp only [fejc]; rw [if_pos hm]
  have habs : ((m - N).natAbs = N - k ∧ (m + N).natAbs = N + k) ∨
      ((m - N).natAbs = N + k ∧ (m + N).natAbs = N - k) := by omega
  have hpc : pc N s m = qN N s ^ k := rfl
  have key : pc N s (m - N) + pc N s (m + N) = qN N s ^ (N - k) + qN N s ^ (N + k) := by
    rcases habs with ⟨h1, h2⟩ | ⟨h1, h2⟩
    · simp only [pc, h1, h2]
    · simp only [pc, h1, h2]; ring
  simp only [gc, hc, sc, cC, hfej, hpc, key]
  rw [qN_pow, qN_pow, qN_pow, Nat.cast_sub hm.le, Nat.cast_add]
  have e1 : -2 * s * ((N : ℝ) - k) / N = -2 * s + 2 * s * k / N := by field_simp; ring
  have e2 : -2 * s * ((N : ℝ) + k) / N = -2 * s + -(2 * s * k / N) := by field_simp; ring
  have e3 : -2 * s * (k : ℝ) / N = -(2 * s * k / N) := by ring
  have e4 : 2 * (s * (1 - (k : ℝ) / N)) = 2 * s - 2 * s * k / N := by ring
  rw [e1, e2, e3, e4, Real.exp_add, Real.exp_add, Real.sinh_eq (2 * s - 2 * s * k / N),
    Real.exp_sub,
    show -(2 * s - 2 * s * k / N) = -2 * s + 2 * s * k / N by ring, Real.exp_add]
  have hsq := four_sinh_sq s
  have hAB : Real.exp (2 * s * k / N) * Real.exp (-(2 * s * k / N)) = 1 := by
    rw [← Real.exp_add]; simp
  generalize Real.exp (2 * s * k / N) = B at hAB ⊢
  generalize Real.exp (-(2 * s * k / N)) = A at hAB ⊢
  generalize Real.exp (2 * s) = E2 at hsq ⊢
  generalize Real.exp (-2 * s) = e2 at hsq ⊢
  have hB : B ≠ 0 := by rintro rfl; simp at hAB
  have hsh2 : Real.sinh s ^ 2 = (E2 - 2 + e2) / 4 := by linarith
  rw [hsh2]
  have hden : E2 - 2 + e2 ≠ 0 := by
    rw [← hsq]; exact mul_ne_zero (by norm_num) (pow_ne_zero 2 hsh)
  have hA : A = 1 / B := by field_simp; linarith
  rw [hA]
  field_simp
  ring

theorem gc_nonneg (hN : 1 ≤ N) (hs : 0 < s) (m : ℤ) : 0 ≤ gc N s m := by
  by_cases hm : m.natAbs < N
  · rw [gc_eq_of_lt hN hs hm]
    have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
    have hu : 0 ≤ 2 * (s * (1 - (m.natAbs : ℝ) / N)) := by
      have : (m.natAbs : ℝ) / N ≤ 1 := by
        rw [div_le_one hNpos]; exact_mod_cast hm.le
      have := hs.le
      positivity
    apply div_nonneg (by linarith [Real.self_le_sinh_iff.2 hu]) (by positivity)
  · rw [gc_eq_zero hN hs (by omega)]

theorem gc_zero (hN : 1 ≤ N) (hs : 0 < s) :
    gc N s 0 = (Real.sinh (2 * s) - 2 * s) / (2 * Real.sinh s ^ 2) := by
  have := gc_eq_of_lt hN hs (m := 0) (by simp; omega)
  simpa using this

/-! ## Series -/

/-- Poisson series over `ℤ`: `∑_m q^{|m|} cos(mθ) = P(θ)`. -/
theorem pc_hasSum (hN : 1 ≤ N) (hs : 0 < s) (θ : ℝ) :
    HasSum (fun m : ℤ => pc N s m * Real.cos (m * θ)) (poissonKernel (qN N s) θ) := by
  have hP := poisson_hasSum (qN_pos (N := N) (s := s)).le (qN_lt_one hN hs) θ
  have e1 : (fun n : ℕ => pc N s ((n : ℤ) + 1) * Real.cos ((((n : ℤ) + 1 : ℤ) : ℝ) * θ)) =
      fun n : ℕ => qN N s ^ (n + 1) * Real.cos (((n + 1 : ℕ) : ℝ) * θ) := by
    funext n
    have h : ((n : ℤ) + 1).natAbs = n + 1 := by omega
    simp only [pc, h]
    push_cast; rfl
  have e2 : (fun n : ℕ => pc N s (-((n : ℤ) + 1)) * Real.cos (((-((n : ℤ) + 1) : ℤ) : ℝ) * θ)) =
      fun n : ℕ => qN N s ^ (n + 1) * Real.cos (((n + 1 : ℕ) : ℝ) * θ) := by
    funext n
    have h : (-((n : ℤ) + 1)).natAbs = n + 1 := by omega
    simp only [pc, h]
    push_cast
    rw [neg_mul, Real.cos_neg]
  have h1 : HasSum (fun n : ℕ => pc N s ((n : ℤ) + 1) * Real.cos ((((n : ℤ) + 1 : ℤ) : ℝ) * θ))
      ((poissonKernel (qN N s) θ - 1) / 2) := by rw [e1]; exact hP
  have h2 : HasSum (fun n : ℕ => pc N s (-((n : ℤ) + 1)) * Real.cos (((-((n : ℤ) + 1) : ℤ) : ℝ) * θ))
      ((poissonKernel (qN N s) θ - 1) / 2) := by rw [e2]; exact hP
  have h3 := HasSum.of_add_one_of_neg_add_one (f := fun m : ℤ => pc N s m * Real.cos (m * θ)) h1 h2
  have h0 : pc N s 0 * Real.cos (((0 : ℤ) : ℝ) * θ) = 1 := by simp [pc]
  rw [h0] at h3
  convert! h3 using 1
  ring

theorem pc_pos (m : ℤ) : 0 < pc N s m := pow_pos qN_pos _

theorem pc_summable (hN : 1 ≤ N) (hs : 0 < s) : Summable (pc N s) := by
  have := (pc_hasSum hN hs 0).summable
  simpa using this

theorem sc_hasSum (hN : 1 ≤ N) (hs : 0 < s) (θ : ℝ) :
    HasSum (fun m : ℤ => sc N s m * Real.cos (m * θ))
      (Real.sin (N * θ / 2) ^ 2 * poissonKernel (qN N s) θ) := by
  have hpcS := pc_summable hN hs
  have hsumm : ∀ c : ℤ, Summable (fun m : ℤ => pc N s (m + c) * Real.cos (m * θ)) := by
    intro c
    refine Summable.of_norm_bounded ((Equiv.addRight c).summable_iff.2 hpcS) (fun m => ?_)
    simp only [Function.comp_apply, Equiv.coe_addRight]
    rw [norm_mul, Real.norm_eq_abs, Real.norm_eq_abs, abs_of_pos (pc_pos _)]
    exact mul_le_of_le_one_right (pc_pos _).le (Real.abs_cos_le_one _)
  obtain ⟨A, hA⟩ := hsumm (-(N : ℤ))
  obtain ⟨B, hB⟩ := hsumm (N : ℤ)
  have hA' : HasSum (fun m : ℤ => pc N s m * Real.cos (((m : ℝ) + N) * θ)) A := by
    have h := (Equiv.addRight (N : ℤ)).hasSum_iff.2 hA
    have e : ((fun m : ℤ => pc N s (m + -(N : ℤ)) * Real.cos (m * θ)) ∘ (Equiv.addRight (N : ℤ))) =
        fun m : ℤ => pc N s m * Real.cos (((m : ℝ) + N) * θ) := by
      funext m
      simp only [Function.comp_apply, Equiv.coe_addRight, add_neg_cancel_right]
      push_cast; rfl
    rw [e] at h; exact h
  have hB' : HasSum (fun m : ℤ => pc N s m * Real.cos (((m : ℝ) - N) * θ)) B := by
    have h := (Equiv.addRight (-(N : ℤ))).hasSum_iff.2 hB
    have e : ((fun m : ℤ => pc N s (m + (N : ℤ)) * Real.cos (m * θ)) ∘ (Equiv.addRight (-(N : ℤ)))) =
        fun m : ℤ => pc N s m * Real.cos (((m : ℝ) - N) * θ) := by
      funext m
      simp only [Function.comp_apply, Equiv.coe_addRight, neg_add_cancel_right]
      push_cast; rw [sub_eq_add_neg]
    rw [e] at h; exact h
  have hAB : A + B = 2 * Real.cos (N * θ) * poissonKernel (qN N s) θ := by
    have h2 := (pc_hasSum hN hs θ).mul_left (2 * Real.cos (N * θ))
    have e : (fun m : ℤ => 2 * Real.cos (N * θ) * (pc N s m * Real.cos (m * θ))) =
        fun m : ℤ => pc N s m * Real.cos (((m : ℝ) + N) * θ) +
          pc N s m * Real.cos (((m : ℝ) - N) * θ) := by
      funext m
      rw [add_mul, sub_mul, Real.cos_add, Real.cos_sub]; ring
    rw [e] at h2
    exact (hA'.add hB').unique h2
  have hfin := ((pc_hasSum hN hs θ).mul_left (1 / 2)).sub ((hA.add hB).mul_left (1 / 4))
  have e : (fun m : ℤ => 1 / 2 * (pc N s m * Real.cos (m * θ)) -
      1 / 4 * (pc N s (m + -(N : ℤ)) * Real.cos (m * θ) + pc N s (m + (N : ℤ)) * Real.cos (m * θ))) =
      fun m : ℤ => sc N s m * Real.cos (m * θ) := by
    funext m
    simp only [sc, ← sub_eq_add_neg]
    ring
  rw [e] at hfin
  convert! hfin using 1
  rw [Real.sin_sq_eq_half_sub, show 2 * ((N : ℝ) * θ / 2) = N * θ by ring, hAB]
  ring

/-- The Fejér part as a (finitely supported) series. -/
theorem fejc_hasSum (hN : 1 ≤ N) (θ : ℝ) :
    HasSum (fun m : ℤ => fejc N m * Real.cos (m * θ)) (fejSum N θ) := by
  obtain ⟨M, rfl⟩ : ∃ M, N = M + 1 := ⟨N - 1, by omega⟩
  set g : ℕ → ℝ := fun n => (((M : ℝ) + 1) - ((n : ℝ) + 1)) / ((M : ℝ) + 1) *
    Real.cos (((n : ℝ) + 1) * θ) with hg
  have hval : ∀ n : ℕ, ∀ z : ℤ, z.natAbs = n + 1 → Real.cos ((z : ℝ) * θ) = Real.cos (((n : ℝ) + 1) * θ) →
      fejc (M + 1) z * Real.cos ((z : ℝ) * θ) = if n < M then g n else 0 := by
    intro n z hz hc
    simp only [fejc, hz, hc, hg]
    split_ifs with h1 h2 h2
    · push_cast; field_simp
    · omega
    · omega
    · simp
  have e1 : (fun n : ℕ => fejc (M + 1) ((n : ℤ) + 1) * Real.cos ((((n : ℤ) + 1 : ℤ) : ℝ) * θ)) =
      fun n : ℕ => if n < M then g n else 0 := by
    funext n
    exact hval n _ (by omega) (by push_cast; rfl)
  have e2 : (fun n : ℕ => fejc (M + 1) (-((n : ℤ) + 1)) * Real.cos (((-((n : ℤ) + 1) : ℤ) : ℝ) * θ)) =
      fun n : ℕ => if n < M then g n else 0 := by
    funext n
    exact hval n _ (by omega) (by push_cast; rw [neg_mul, Real.cos_neg])
  have hS : HasSum (fun n : ℕ => if n < M then g n else 0) (∑ n ∈ Finset.range M, g n) := by
    have : HasSum (fun n : ℕ => if n < M then g n else 0)
        (∑ n ∈ Finset.range M, if n < M then g n else 0) :=
      hasSum_sum_of_ne_finset_zero (fun n hn => by rw [Finset.mem_range] at hn; simp [hn])
    convert! this using 1
    apply Finset.sum_congr rfl; intro n hn
    rw [Finset.mem_range] at hn; simp [hn]
  have h1 : HasSum (fun n : ℕ => fejc (M + 1) ((n : ℤ) + 1) * Real.cos ((((n : ℤ) + 1 : ℤ) : ℝ) * θ))
      (∑ n ∈ Finset.range M, g n) := by rw [e1]; exact hS
  have h2 : HasSum (fun n : ℕ => fejc (M + 1) (-((n : ℤ) + 1)) * Real.cos (((-((n : ℤ) + 1) : ℤ) : ℝ) * θ))
      (∑ n ∈ Finset.range M, g n) := by rw [e2]; exact hS
  have h3 := HasSum.of_add_one_of_neg_add_one
    (f := fun m : ℤ => fejc (M + 1) m * Real.cos (m * θ)) h1 h2
  have h0 : fejc (M + 1) 0 * Real.cos (((0 : ℤ) : ℝ) * θ) = 1 := by simp [fejc]
  rw [h0] at h3
  convert! h3 using 1
  rw [fejSum, Finset.sum_range_succ']
  have hM : ((M : ℝ) + 1) ≠ 0 := by positivity
  have hsum : ∑ n ∈ Finset.range M, g n = (∑ n ∈ Finset.range M,
      (((M : ℝ) + 1) - ((n : ℝ) + 1)) * Real.cos (((n : ℝ) + 1) * θ)) / ((M : ℝ) + 1) := by
    rw [Finset.sum_div]
    apply Finset.sum_congr rfl; intro n _
    simp only [hg]; ring
  have hT : ∑ n ∈ Finset.range M, (((M + 1 : ℕ) : ℝ) - ((n + 1 : ℕ) : ℝ)) *
      Real.cos (((n + 1 : ℕ) : ℝ) * θ) = ∑ n ∈ Finset.range M,
      (((M : ℝ) + 1) - ((n : ℝ) + 1)) * Real.cos (((n : ℝ) + 1) * θ) := by
    push_cast; rfl
  rw [hT, hsum]
  generalize ∑ n ∈ Finset.range M, (((M : ℝ) + 1) - ((n : ℝ) + 1)) * Real.cos (((n : ℝ) + 1) * θ) = T
  push_cast
  simp only [zero_mul, Real.cos_zero, mul_one, sub_zero]
  field_simp
  ring

theorem hc_hasSum (hN : 1 ≤ N) (hs : 0 < s) (θ : ℝ) :
    HasSum (fun m : ℤ => hc N s m * Real.cos (m * θ)) (Hfun N s θ) := by
  have h := (((fejc_hasSum hN θ).div_const N).sub ((sc_hasSum hN hs θ).div_const (N * s))).mul_left
    (cC N s)
  convert! h using 1
  · ext m; simp only [hc]; ring

/-- The `G` series is a finite cosine polynomial. -/
theorem gc_hasSum (hN : 1 ≤ N) (hs : 0 < s) (θ : ℝ) :
    HasSum (fun m : ℤ => gc N s m * Real.cos (m * θ))
      (∑ m ∈ Finset.Ioo (-(N : ℤ)) N, gc N s m * Real.cos (m * θ)) := by
  apply hasSum_sum_of_ne_finset_zero
  intro m hm
  rw [Finset.mem_Ioo] at hm
  rw [gc_eq_zero hN hs (by omega), zero_mul]

/-! ## Pointwise facts about `H` -/

theorem dirichlet_mul (θ : ℝ) (n : ℕ) :
    (2 * ∑ k ∈ Finset.range (n + 1), Real.cos (k * θ) - 1) * (1 - Real.cos θ) =
      Real.cos (n * θ) - Real.cos ((n + 1 : ℕ) * θ) := by
  induction n with
  | zero => simp; norm_num
  | succ n ih =>
    rw [Finset.sum_range_succ]
    have h2 : 2 * Real.cos (((n + 1 : ℕ) : ℝ) * θ) * Real.cos θ =
        Real.cos (((n + 1 + 1 : ℕ) : ℝ) * θ) + Real.cos ((n : ℝ) * θ) := by
      have e1 : (((n + 1 + 1 : ℕ) : ℝ) * θ) = ((n + 1 : ℕ) : ℝ) * θ + θ := by push_cast; ring
      have e2 : ((n : ℝ) * θ) = ((n + 1 : ℕ) : ℝ) * θ - θ := by push_cast; ring
      rw [e1, e2, Real.cos_add, Real.cos_sub]; ring
    have : (2 * (∑ k ∈ Finset.range (n + 1), Real.cos (k * θ) + Real.cos (((n + 1 : ℕ) : ℝ) * θ)) - 1)
        * (1 - Real.cos θ) = (2 * ∑ k ∈ Finset.range (n + 1), Real.cos (k * θ) - 1) * (1 - Real.cos θ)
        + 2 * Real.cos (((n + 1 : ℕ) : ℝ) * θ) - 2 * Real.cos (((n + 1 : ℕ) : ℝ) * θ) * Real.cos θ := by
      ring
    rw [this, ih, h2]
    push_cast; ring

theorem fej_aux (θ : ℝ) (N : ℕ) :
    (2 * ∑ k ∈ Finset.range N, ((N : ℝ) - k) * Real.cos (k * θ) - N) * (1 - Real.cos θ) =
      1 - Real.cos (N * θ) := by
  induction N with
  | zero => simp
  | succ N ih =>
    have hsplit : ∑ k ∈ Finset.range (N + 1), (((N + 1 : ℕ) : ℝ) - k) * Real.cos (k * θ) =
        ∑ k ∈ Finset.range N, ((N : ℝ) - k) * Real.cos (k * θ) +
          ∑ k ∈ Finset.range (N + 1), Real.cos (k * θ) := by
      rw [show (∑ k ∈ Finset.range (N + 1), (((N + 1 : ℕ) : ℝ) - k) * Real.cos (k * θ)) =
          ∑ k ∈ Finset.range (N + 1), (((N : ℝ) - k) * Real.cos (k * θ) + Real.cos (k * θ)) from
          Finset.sum_congr rfl (fun k _ => by push_cast; ring)]
      rw [Finset.sum_add_distrib, Finset.sum_range_succ (fun k : ℕ => ((N : ℝ) - k) * Real.cos (k * θ))]
      simp
    rw [hsplit]
    have := dirichlet_mul θ N
    have e : (2 * (∑ k ∈ Finset.range N, ((N : ℝ) - k) * Real.cos (k * θ) +
        ∑ k ∈ Finset.range (N + 1), Real.cos (k * θ)) - ((N + 1 : ℕ) : ℝ)) * (1 - Real.cos θ) =
        (2 * ∑ k ∈ Finset.range N, ((N : ℝ) - k) * Real.cos (k * θ) - N) * (1 - Real.cos θ) +
        (2 * ∑ k ∈ Finset.range (N + 1), Real.cos (k * θ) - 1) * (1 - Real.cos θ) := by
      push_cast; ring
    rw [e, ih, this]
    ring

/-- Fejér closed form `Fej_N(θ) · (1 - cos θ) = (1 - cos Nθ)/N`. -/
theorem fejSum_mul (θ : ℝ) :
    fejSum N θ * (1 - Real.cos θ) = (1 - Real.cos (N * θ)) / N := by
  rw [fejSum, div_mul_eq_mul_div, fej_aux]

theorem sum_range_sub (N : ℕ) : ∑ k ∈ Finset.range N, ((N : ℝ) - k) = N * (N + 1) / 2 := by
  induction N with
  | zero => simp
  | succ N ih =>
    rw [show (∑ k ∈ Finset.range (N + 1), (((N + 1 : ℕ) : ℝ) - k)) =
        ∑ k ∈ Finset.range (N + 1), (((N : ℝ) - k) + 1) from
        Finset.sum_congr rfl (fun k _ => by push_cast; ring)]
    rw [Finset.sum_add_distrib, Finset.sum_range_succ, ih]
    simp; ring

theorem fejSum_zero (hN : 1 ≤ N) : fejSum N 0 = N := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  simp only [fejSum, mul_zero, Real.cos_zero, mul_one]
  rw [sum_range_sub]
  field_simp
  ring

theorem Hfun_zero (hN : 1 ≤ N) (hs : 0 < s) : Hfun N s 0 = N * s / Real.sinh s ^ 2 := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  simp only [Hfun, fejSum_zero hN, mul_zero, zero_div, Real.sin_zero]
  simp only [cC]
  field_simp
  ring

theorem sinh_le_mul_cosh (t : ℝ) (ht : 0 ≤ t) : Real.sinh t ≤ t * Real.cosh t := by
  let g := fun t : ℝ => t * Real.cosh t - Real.sinh t
  have hd : ∀ x, HasDerivAt g (x * Real.sinh x) x := by
    intro x
    have := ((hasDerivAt_id' x).mul (Real.hasDerivAt_cosh x)).sub (Real.hasDerivAt_sinh x)
    convert! this using 1
    ring
  have hmono : MonotoneOn g (Set.Ici 0) := by
    apply monotoneOn_of_deriv_nonneg (convex_Ici 0)
    · exact (show Continuous g by fun_prop).continuousOn
    · intro x _; exact (hd x).differentiableAt.differentiableWithinAt
    · intro x hx
      rw [interior_Ici] at hx
      rw [(hd x).deriv]
      exact mul_nonneg (le_of_lt hx) (Real.sinh_nonneg_iff.2 (le_of_lt hx))
  have := hmono (Set.mem_Ici.2 le_rfl) (Set.mem_Ici.2 ht) ht
  simp only [g, zero_mul, Real.sinh_zero, sub_zero] at this
  linarith

/-- The key scalar inequality `2 sinh a ≤ a (cosh a + 1)` for `a ≥ 0`. -/
theorem two_sinh_le (a : ℝ) (ha : 0 ≤ a) : 2 * Real.sinh a ≤ a * (Real.cosh a + 1) := by
  have h := sinh_le_mul_cosh (a / 2) (by linarith)
  have hc : 0 < Real.cosh (a / 2) := Real.cosh_pos _
  have e1 : Real.sinh a = 2 * Real.sinh (a / 2) * Real.cosh (a / 2) := by
    rw [← Real.sinh_two_mul]; ring_nf
  have e2 : Real.cosh a = 2 * Real.cosh (a / 2) ^ 2 - 1 := by
    have h := Real.cosh_two_mul (a / 2)
    rw [show 2 * (a / 2) = a by ring] at h
    rw [h, Real.cosh_sq]; ring
  rw [e1, e2]
  nlinarith [mul_le_mul_of_nonneg_left h hc.le]

theorem Hfun_nonneg (hN : 1 ≤ N) (hs : 0 < s) (θ : ℝ) : 0 ≤ Hfun N s θ := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  have hC : 0 < cC N s := by
    unfold cC
    have : 0 < Real.sinh s := Real.sinh_pos_iff.2 hs
    positivity
  by_cases hcos : Real.cos θ = 1
  · obtain ⟨n, hn⟩ := (Real.cos_eq_one_iff θ).1 hcos
    have e : (fun m : ℤ => hc N s m * Real.cos (m * θ)) = fun m : ℤ => hc N s m * Real.cos (m * 0) := by
      funext m
      rw [← hn, show (m : ℝ) * (n * (2 * π)) = ((m * n : ℤ) : ℝ) * (2 * π) by push_cast; ring,
        Real.cos_int_mul_two_pi]
      simp
    have h1 := hc_hasSum hN hs θ
    rw [e] at h1
    rw [h1.unique (hc_hasSum hN hs 0), Hfun_zero hN hs]
    have : 0 < Real.sinh s := Real.sinh_pos_iff.2 hs
    positivity
  · have hc1 : 0 < 1 - Real.cos θ := by
      have := Real.cos_le_one θ
      exact sub_pos.2 (lt_of_le_of_ne this hcos)
    set a := 2 * s / N with ha
    have hapos : 0 < a := div_pos (by linarith) hNpos
    have hq : qN N s = Real.exp (-a) := by rw [qN, ha]; congr 1; ring
    have hF : fejSum N θ = (1 - Real.cos (N * θ)) / (N * (1 - Real.cos θ)) := by
      rw [eq_div_iff (by positivity), ← mul_assoc, mul_comm (fejSum N θ) N, mul_assoc,
        fejSum_mul θ]
      field_simp
    have hsin : Real.sin (N * θ / 2) ^ 2 = (1 - Real.cos (N * θ)) / 2 := by
      rw [Real.sin_sq_eq_half_sub, show 2 * ((N : ℝ) * θ / 2) = N * θ by ring]; ring
    have hX : 0 ≤ 1 - Real.cos (N * θ) := by linarith [Real.cos_le_one (N * θ)]
    have hcosh : Real.cos θ < Real.cosh a := by
      have := Real.cos_le_one θ; have := Real.one_lt_cosh.2 hapos.ne'; linarith
    have hP : poissonKernel (qN N s) θ = Real.sinh a / (Real.cosh a - Real.cos θ) := by
      rw [hq, poissonKernel_exp a θ hapos]
    -- main scalar inequality: P · N (1 - cos θ) ≤ 2 s
    have hkey : Real.sinh a * (1 - Real.cos θ) ≤ a * (Real.cosh a - Real.cos θ) := by
      have h1 := two_sinh_le a hapos.le
      have h2 := Real.self_le_sinh_iff.2 hapos.le
      have h3 : 1 - Real.cos θ ≤ 2 := by linarith [Real.neg_one_le_cos θ]
      nlinarith [mul_le_mul_of_nonneg_left h3 (sub_nonneg.2 h2)]
    have hbr : poissonKernel (qN N s) θ / (2 * (N * s)) ≤ 1 / (N * N * (1 - Real.cos θ)) := by
      rw [hP, div_div, div_le_div_iff₀ (by positivity) (by positivity)]
      have hs' : 2 * s = N * a := by rw [ha]; field_simp
      have e : (Real.cosh a - Real.cos θ) * (2 * (N * s)) = N * N * (a * (Real.cosh a - Real.cos θ)) := by
        rw [show (2 * (N * s) : ℝ) = N * (2 * s) by ring, hs']; ring
      rw [one_mul, e]
      have := mul_le_mul_of_nonneg_left hkey (by positivity : (0 : ℝ) ≤ N * N)
      linarith
    unfold Hfun
    rw [hF, hsin]
    apply mul_nonneg hC.le
    have : (1 - Real.cos (N * θ)) / 2 * poissonKernel (qN N s) θ / (N * s) =
        (1 - Real.cos (N * θ)) * (poissonKernel (qN N s) θ / (2 * (N * s))) := by ring
    have h2 : (1 - Real.cos (N * θ)) / (N * (1 - Real.cos θ)) / N =
        (1 - Real.cos (N * θ)) * (1 / (N * N * (1 - Real.cos θ))) := by
      field_simp
    rw [this, h2, sub_nonneg]
    exact mul_le_mul_of_nonneg_left hbr hX

/-! ## The floor -/

/-- Pair sums of cosines are nonnegative: `∑_{j,k} cos(m(θ_j - θ_k)) = |T_m|² ≥ 0`. -/
theorem pair_cos_sum_nonneg {D : ℕ} (x : Fin D → ℝ) (m : ℤ) :
    0 ≤ ∑ j, ∑ k, Real.cos (m * (2 * π * (x j - x k))) := by
  have h := norm_traceT_sq x m.natAbs
  have e : ∀ α : ℝ, Real.cos ((m : ℝ) * α) = Real.cos ((m.natAbs : ℝ) * α) := by
    intro α
    simp only [Nat.cast_natAbs, Int.cast_abs]
    rcases abs_choice ((m : ℤ) : ℝ) with h | h <;> rw [h]
    rw [neg_mul, Real.cos_neg]
  simp_rw [e]
  rw [← h]
  positivity

/-- **Energy lower bound.**  `∑_{j,k} P(2π(x_j - x_k)) ≥ N² coth s`. -/
theorem poisson_energy_ge (hN : 1 ≤ N) (x : Fin N → ℝ) (hs : 0 < s) :
    (N : ℝ) ^ 2 * (Real.cosh s / Real.sinh s) ≤
      ∑ j, ∑ k, poissonKernel (qN N s) (2 * π * (x j - x k)) := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  have hsh : 0 < Real.sinh s := Real.sinh_pos_iff.2 hs
  set G : ℝ → ℝ := fun θ => ∑ m ∈ Finset.Ioo (-(N : ℤ)) N, gc N s m * Real.cos (m * θ) with hG
  have hdec : ∀ θ, poissonKernel (qN N s) θ = G θ + Hfun N s θ := by
    intro θ
    have h := (gc_hasSum hN hs θ).add (hc_hasSum hN hs θ)
    have e : (fun m : ℤ => gc N s m * Real.cos (m * θ) + hc N s m * Real.cos (m * θ)) =
        fun m : ℤ => pc N s m * Real.cos (m * θ) := by
      funext m; simp only [gc]; ring
    rw [e] at h
    exact (pc_hasSum hN hs θ).unique h
  simp_rw [hdec, Finset.sum_add_distrib]
  -- the `G` part
  have hGsum : gc N s 0 * (N : ℝ) ^ 2 ≤ ∑ j, ∑ k, G (2 * π * (x j - x k)) := by
    have hswap : ∑ j, ∑ k, G (2 * π * (x j - x k)) = ∑ m ∈ Finset.Ioo (-(N : ℤ)) N,
        gc N s m * ∑ j, ∑ k, Real.cos (m * (2 * π * (x j - x k))) := by
      calc ∑ j, ∑ k, G (2 * π * (x j - x k))
          = ∑ j, ∑ m ∈ Finset.Ioo (-(N : ℤ)) N, ∑ k,
              gc N s m * Real.cos (m * (2 * π * (x j - x k))) := by
            apply Finset.sum_congr rfl; intro j _
            simp only [hG]
            exact Finset.sum_comm
        _ = ∑ m ∈ Finset.Ioo (-(N : ℤ)) N, ∑ j, ∑ k,
              gc N s m * Real.cos (m * (2 * π * (x j - x k))) := Finset.sum_comm
        _ = _ := by simp only [Finset.mul_sum]
    rw [hswap]
    have h0 : (0 : ℤ) ∈ Finset.Ioo (-(N : ℤ)) N := by
      rw [Finset.mem_Ioo]; omega
    have := Finset.single_le_sum (f := fun m : ℤ => gc N s m *
      ∑ j, ∑ k, Real.cos (m * (2 * π * (x j - x k))))
      (fun m _ => mul_nonneg (gc_nonneg hN hs m) (pair_cos_sum_nonneg x m)) h0
    simp only [Int.cast_zero, zero_mul, Real.cos_zero, Finset.sum_const, Finset.card_univ,
      Fintype.card_fin, nsmul_eq_mul, mul_one] at this
    calc gc N s 0 * (N : ℝ) ^ 2 = gc N s 0 * (N * N) := by ring
      _ ≤ _ := this
  -- the `H` part
  have hHsum : (N : ℝ) * (N * s / Real.sinh s ^ 2) ≤ ∑ j, ∑ k, Hfun N s (2 * π * (x j - x k)) := by
    have : ∀ j : Fin N, N * s / Real.sinh s ^ 2 ≤ ∑ k, Hfun N s (2 * π * (x j - x k)) := by
      intro j
      have := Finset.single_le_sum (f := fun k => Hfun N s (2 * π * (x j - x k)))
        (fun k _ => Hfun_nonneg hN hs _) (Finset.mem_univ j)
      simp only [sub_self, mul_zero] at this
      rwa [Hfun_zero hN hs] at this
    calc (N : ℝ) * (N * s / Real.sinh s ^ 2) = ∑ _j : Fin N, N * s / Real.sinh s ^ 2 := by
          simp
      _ ≤ _ := Finset.sum_le_sum fun j _ => this j
  have hval : gc N s 0 * (N : ℝ) ^ 2 + N * (N * s / Real.sinh s ^ 2) =
      (N : ℝ) ^ 2 * (Real.cosh s / Real.sinh s) := by
    rw [gc_zero hN hs, Real.sinh_two_mul]
    field_simp
    ring
  linarith

/-- **The universal clock floor.**  For every spectrum of size `N ≥ 1` and `s > 0`,
`L_N(s) ≥ 1/(e^{2s} - 1)`, the value attained by the `N`-clock. -/
theorem abelL_ge_clock (hN : 1 ≤ N) (x : Fin N → ℝ) (hs : 0 < s) :
    1 / (Real.exp (2 * s) - 1) ≤ abelL x s := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  have hid := abelL_poisson_identity hN x hs
  have hE := poisson_energy_ge hN x hs
  have hsh : 0 < Real.sinh s := Real.sinh_pos_iff.2 hs
  have hcoth : Real.cosh s / Real.sinh s ≤ 2 * abelL x s + 1 := by
    rw [hid]
    rw [show Real.exp (-2 * s / N) = qN N s from rfl]
    calc Real.cosh s / Real.sinh s = (1 / (N : ℝ) ^ 2) * ((N : ℝ) ^ 2 * (Real.cosh s / Real.sinh s)) := by
          field_simp
      _ ≤ _ := mul_le_mul_of_nonneg_left hE (by positivity)
  have hval : 1 / (Real.exp (2 * s) - 1) = (Real.cosh s / Real.sinh s - 1) / 2 := by
    have hE1 : Real.exp s * Real.exp (-s) = 1 := by rw [← Real.exp_add]; simp
    have h2 : Real.exp (2 * s) = Real.exp s * Real.exp s := by rw [← Real.exp_add]; ring_nf
    rw [Real.cosh_eq, Real.sinh_eq, h2]
    have hpos : Real.exp s - Real.exp (-s) ≠ 0 := by
      have : Real.exp (-s) < Real.exp s := Real.exp_lt_exp.2 (by linarith)
      linarith
    have hpos2 : Real.exp s * Real.exp s - 1 ≠ 0 := by
      have : 1 < Real.exp s := by
        rw [← Real.exp_zero]; exact Real.exp_lt_exp.2 hs
      nlinarith
    have hEpos : 0 < Real.exp s := Real.exp_pos s
    have he : Real.exp (-s) = 1 / Real.exp s := by
      rw [eq_div_iff hEpos.ne']; linarith
    have hpos3 : Real.exp s ^ 2 - 1 ≠ 0 := by rw [sq]; exact hpos2
    rw [he] at hpos ⊢
    field_simp
    ring
  rw [hval]
  linarith

#print axioms qN_pos
#print axioms qN_lt_one
#print axioms qN_pow_N
#print axioms sinh_sq_mul_exp
#print axioms gc_eq_zero
#print axioms qN_pow
#print axioms four_sinh_sq
#print axioms gc_eq_of_lt
#print axioms gc_nonneg
#print axioms gc_zero
#print axioms pc_hasSum
#print axioms pc_pos
#print axioms pc_summable
#print axioms sc_hasSum
#print axioms fejc_hasSum
#print axioms hc_hasSum
#print axioms gc_hasSum
#print axioms dirichlet_mul
#print axioms fej_aux
#print axioms fejSum_mul
#print axioms sum_range_sub
#print axioms fejSum_zero
#print axioms Hfun_zero
#print axioms sinh_le_mul_cosh
#print axioms two_sinh_le
#print axioms Hfun_nonneg
#print axioms pair_cos_sum_nonneg
#print axioms poisson_energy_ge
#print axioms abelL_ge_clock
end Bgs.Mathlib
