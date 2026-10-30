module
public import Bgs.Mathlib.HardyIdentity
public import Bgs.Mathlib.ClockRigidity
@[expose] public section

/-!
# Equality in the radial Hardy minimum iff the spectrum is a rotated regular `N`-gon
(BGS-TRACE-091, §2.2)

For a spectrum of phases `x : Fin N → ℝ` (eigenvalues `λ_j = e^{2πi x_j}`), the interior
secular coefficients `c_1, …, c_{N-1}` of `p(z) = ∏_j (1 - z λ_j)` all vanish iff the
spectrum is a rotated `N`-clock (`interior_coeff_zero_iff_rotated`).  Combined with the
exact Hardy identity this gives the note's equality statement:

* `radialRatio_eq_clock_iff_rotated` — for `N ≥ 1` and `0 < b < a < 1`,
  `Z(a,b) = 1 + (a^N - b^N)²/(1 - b^{2N})` iff the eigenvalues form a rotated regular
  `N`-gon (repeated eigenvalues are excluded automatically).
-/

open Complex Polynomial Real Finset

namespace Bgs.Mathlib

variable {N : ℕ}

/-- Eigenvalues `λ_j = e^{2πi x_j}` of a phase spectrum. -/
noncomputable def phaseEig (x : Fin N → ℝ) (j : Fin N) : ℂ :=
  Complex.exp (2 * π * Complex.I * (x j : ℂ))

lemma norm_phaseEig (x : Fin N → ℝ) (j : Fin N) : ‖phaseEig x j‖ = 1 := by
  rw [phaseEig, show 2 * (π : ℂ) * Complex.I * (x j : ℂ) = ((2 * π * x j : ℝ) : ℂ) * Complex.I by
    push_cast; ring, Complex.norm_exp_ofReal_mul_I]

lemma phaseEig_ne_zero (x : Fin N → ℝ) (j : Fin N) : phaseEig x j ≠ 0 :=
  Complex.exp_ne_zero _

/-- `λ_j = λ_k` iff `x_j - x_k ∈ ℤ`; `λ_j^N = λ_k^N` iff `N (x_j - x_k) ∈ ℤ`. -/
lemma phaseEig_pow_eq_iff (x : Fin N → ℝ) (M : ℕ) (j k : Fin N) :
    phaseEig x j ^ M = phaseEig x k ^ M ↔ ∃ n : ℤ, (M : ℝ) * (x j - x k) = n := by
  rw [phaseEig, phaseEig, ← Complex.exp_nat_mul, ← Complex.exp_nat_mul,
    Complex.exp_eq_exp_iff_exists_int]
  have hpi : (2 * π * Complex.I : ℂ) ≠ 0 := by simp [Real.pi_ne_zero, Complex.I_ne_zero]
  constructor
  · rintro ⟨n, hn⟩
    refine ⟨n, ?_⟩
    have : ((M * (x j - x k) : ℝ) : ℂ) * (2 * π * Complex.I) = (n : ℂ) * (2 * π * Complex.I) := by
      push_cast; linear_combination hn
    exact_mod_cast mul_right_cancel₀ hpi this
  · rintro ⟨n, hn⟩
    refine ⟨n, ?_⟩
    have : ((M * (x j - x k) : ℝ) : ℂ) = (n : ℂ) := by exact_mod_cast hn
    push_cast at this
    linear_combination (2 * π * Complex.I) * this

/-- Product form `p = C(∏(-λ_j)) · ∏ (X - C λ_j⁻¹)`. -/
lemma secPoly_prod_form (lam : Fin N → ℂ) (hlam : ∀ j, lam j ≠ 0) :
    secPoly lam = C (∏ j, -lam j) * ∏ j, (X - C (lam j)⁻¹) := by
  rw [secPoly, map_prod, ← Finset.prod_mul_distrib]
  refine Finset.prod_congr rfl fun j _ => ?_
  rw [mul_sub, ← C_mul, show -lam j * (lam j)⁻¹ = -1 by field_simp; simp [hlam j]]
  simp only [C_neg, C_1]
  ring

/-- The secular polynomial in product form `C(∏(-λ_j)) · ∏ (X - C λ_j⁻¹)`; its roots are the
`λ_j⁻¹`. -/
lemma secPoly_roots (lam : Fin N → ℂ) (hlam : ∀ j, lam j ≠ 0) :
    (secPoly lam).roots = (Finset.univ.val.map fun j => (lam j)⁻¹) := by
  rw [secPoly_prod_form lam hlam,
    roots_C_mul _ (Finset.prod_ne_zero_iff.2 fun j _ => neg_ne_zero.2 (hlam j)),
    Finset.prod_eq_multiset_prod]
  have : (Finset.univ.val.map fun j => X - C (lam j)⁻¹) =
      ((Finset.univ.val.map fun j => (lam j)⁻¹).map fun a => X - C a) := by
    rw [Multiset.map_map]; rfl
  rw [this, roots_multiset_prod_X_sub_C]

/-- If the interior coefficients vanish, `p = C c_N · X^N + 1`. -/
lemma secPoly_eq_of_interior (hN : 1 ≤ N) (lam : Fin N → ℂ)
    (hc : ∀ k, 1 ≤ k → k < N → (secPoly lam).coeff k = 0) :
    secPoly lam = C ((secPoly lam).coeff N) * X ^ N + 1 := by
  ext k
  rw [coeff_add, coeff_C_mul_X_pow, coeff_one]
  rcases Nat.eq_zero_or_pos k with rfl | hk0
  · rw [if_neg (by omega), if_pos rfl, zero_add, coeff_zero_eq_eval_zero,
      secPoly_eval, secular_zero]
  rw [if_neg (by omega : ¬ (k = 0)), add_zero]
  rcases lt_trichotomy k N with hkN | rfl | hkN
  · rw [hc k hk0 hkN, if_neg (by omega)]
  · rw [if_pos rfl]
  · rw [if_neg (by omega)]
    exact coeff_eq_zero_of_natDegree_lt ((secPoly_natDegree_le lam).trans_lt hkN)

lemma secPoly_coeff_N (lam : Fin N → ℂ) (hlam : ∀ j, lam j ≠ 0) :
    (secPoly lam).coeff N = ∏ j, -lam j := by
  rw [secPoly_prod_form lam hlam, coeff_C_mul]
  have hm : (∏ j : Fin N, (X - C (lam j)⁻¹)).Monic :=
    monic_prod_of_monic _ _ fun j _ => monic_X_sub_C _
  have hd : (∏ j : Fin N, (X - C (lam j)⁻¹)).natDegree = N := by
    rw [natDegree_prod_of_monic _ _ fun j _ => monic_X_sub_C _]
    simp
  have := hm.coeff_natDegree
  rw [hd] at this
  rw [this, mul_one]

lemma secPoly_coeff_N_ne_zero (lam : Fin N → ℂ) (hlam : ∀ j, lam j ≠ 0) :
    (secPoly lam).coeff N ≠ 0 := by
  rw [secPoly_coeff_N lam hlam]
  exact Finset.prod_ne_zero_iff.2 fun j _ => neg_ne_zero.2 (hlam j)

/-- Interior coefficients vanish ⇒ rotated clock. -/
lemma isRotatedClock_of_interior (hN : 1 ≤ N) (x : Fin N → ℝ)
    (hc : ∀ k, 1 ≤ k → k < N → (secPoly (phaseEig x)).coeff k = 0) : IsRotatedClock x := by
  set lam := phaseEig x with hlamdef
  have hlam : ∀ j, lam j ≠ 0 := phaseEig_ne_zero x
  set cN := (secPoly lam).coeff N with hcN
  have hcN0 : cN ≠ 0 := secPoly_coeff_N_ne_zero lam hlam
  have hsp := secPoly_eq_of_interior hN lam hc
  -- every `λ_j⁻¹` is a root, hence `λ_j^N = -c_N`
  have hpow : ∀ j, lam j ^ N = -cN := by
    intro j
    have h0 : (secPoly lam).eval (lam j)⁻¹ = 0 := by
      rw [secPoly_eval, secular]
      exact Finset.prod_eq_zero (Finset.mem_univ j) (by field_simp [hlam j]; ring)
    rw [hsp] at h0
    simp only [eval_add, eval_mul, eval_C, eval_pow, eval_X, eval_one, inv_pow] at h0
    have hj : lam j ^ N ≠ 0 := pow_ne_zero _ (hlam j)
    field_simp at h0
    linear_combination h0
  -- the roots are simple
  have hnodup : (secPoly lam).roots.Nodup := by
    have e : secPoly lam = C cN * (X ^ N - C (-cN⁻¹)) := by
      rw [hsp, mul_sub, ← C_mul, show cN * -cN⁻¹ = -1 by field_simp]
      simp only [C_neg, C_1]; ring
    rw [e, roots_C_mul _ hcN0]
    exact nodup_roots (separable_X_pow_sub_C _ (by exact_mod_cast (by omega : N ≠ 0))
      (neg_ne_zero.2 (inv_ne_zero hcN0)))
  rw [secPoly_roots lam hlam] at hnodup
  apply isRotatedClock_of_pairs hN x
  intro j k hjk
  constructor
  · exact (phaseEig_pow_eq_iff x N j k).1 (by rw [hpow, hpow])
  · intro hint
    have heq : lam j = lam k := by
      have := (phaseEig_pow_eq_iff x 1 j k).2 (by simpa using hint)
      simpa using this
    exact hjk (Multiset.inj_on_of_nodup_map hnodup j (Finset.mem_univ j) k (Finset.mem_univ k)
      (by rw [heq]))

/-- Rotated clock ⇒ `p(z) = 1 - (ζ z)^N`, hence interior coefficients vanish. -/
lemma interior_of_isRotatedClock (hN : 1 ≤ N) {x : Fin N → ℝ} (hx : IsRotatedClock x) :
    ∀ k, 1 ≤ k → k < N → (secPoly (phaseEig x)).coeff k = 0 := by
  obtain ⟨c, σ, hx⟩ := hx
  choose n hn using hx
  have hN0 : N ≠ 0 := by omega
  set ζ : ℂ := Complex.exp (2 * π * Complex.I * (c : ℂ)) with hζ
  set ω : ℂ := Complex.exp (2 * π * Complex.I / N) with hω
  have hprim : IsPrimitiveRoot ω N := Complex.isPrimitiveRoot_exp N hN0
  have heig : ∀ j, phaseEig x j = ζ * ω ^ ((σ j : Fin N) : ℕ) := by
    intro j
    rw [phaseEig, hn j, hζ, hω, ← Complex.exp_nat_mul, ← Complex.exp_add]
    have : 2 * (π : ℂ) * Complex.I * ((c + ((σ j : Fin N) : ℝ) / N + n j : ℝ) : ℂ) =
        (2 * π * Complex.I * c + ((σ j : Fin N) : ℕ) * (2 * π * Complex.I / N)) +
          (n j : ℂ) * (2 * π * Complex.I) := by
      push_cast; ring
    rw [this, Complex.exp_add _ ((n j : ℂ) * _), Complex.exp_int_mul_two_pi_mul_I, mul_one]
  have hsec : ∀ z, secular (phaseEig x) z = 1 - (z * ζ) ^ N := by
    intro z
    rw [secular]
    simp_rw [heig]
    rw [Equiv.prod_comp σ (fun m : Fin N => 1 - z * (ζ * ω ^ (m : ℕ))),
      Fin.prod_univ_eq_prod_range (fun i => 1 - z * (ζ * ω ^ i))]
    have h := congrArg (eval 1) (X_pow_sub_C_eq_prod hprim (α := z * ζ) (by omega) rfl)
    simp only [eval_sub, eval_pow, eval_X, eval_C, one_pow, eval_prod] at h
    rw [h]
    refine Finset.prod_congr rfl fun i _ => ?_
    ring
  have hpoly : secPoly (phaseEig x) = 1 - C (ζ ^ N) * X ^ N := by
    apply Polynomial.funext
    intro r
    rw [secPoly_eval, hsec]
    simp [mul_pow, mul_comm]
  intro k hk1 hkN
  rw [hpoly, coeff_sub, coeff_one, coeff_C_mul_X_pow, if_neg (by omega),
    if_neg (by omega), sub_zero]

theorem interior_coeff_zero_iff_rotated (hN : 1 ≤ N) (x : Fin N → ℝ) :
    (∀ k, 1 ≤ k → k < N → (secPoly (phaseEig x)).coeff k = 0) ↔ IsRotatedClock x :=
  ⟨isRotatedClock_of_interior hN x, interior_of_isRotatedClock hN⟩

/-- **Equality in the radial clock minimum (TRACE-091 §2.2).**  For `N ≥ 1` and
`0 < b < a < 1`, the normalized radial ratio equals the clock value iff the eigenvalues form a
rotated regular `N`-gon. -/
theorem radialRatio_eq_clock_iff_rotated (hN : 1 ≤ N) (x : Fin N → ℝ) {a b : ℝ}
    (hb0 : 0 < b) (hba : b < a) (ha1 : a < 1) :
    radialRatio (phaseEig x) a b = 1 + (a ^ N - b ^ N) ^ 2 / (1 - b ^ (2 * N)) ↔
      IsRotatedClock x := by
  rw [radialRatio_eq_clock_iff (phaseEig x) (norm_phaseEig x) hN hb0 hba ha1,
    interior_coeff_zero_iff_rotated hN x]

#print axioms norm_phaseEig
#print axioms phaseEig_ne_zero
#print axioms phaseEig_pow_eq_iff
#print axioms secPoly_prod_form
#print axioms secPoly_roots
#print axioms secPoly_eq_of_interior
#print axioms secPoly_coeff_N
#print axioms secPoly_coeff_N_ne_zero
#print axioms isRotatedClock_of_interior
#print axioms interior_of_isRotatedClock
#print axioms interior_coeff_zero_iff_rotated
#print axioms radialRatio_eq_clock_iff_rotated
end Bgs.Mathlib
