module
public import Bgs.Mathlib.DigitFUP
@[expose] public section

/-!
# Off-diagonal digit alphabets: the binary exception (BGS-FUP-001, §4, `M = 2`)

Source: `mathematics/fixed-map/offdiagonal_digit_fup.md`, last paragraph of §4.

For `M = 2` and `N = 2^k` (`k ≥ 1`) the paired binary digits must be complementary, so
`X_k = {(x, N-1-x)}` is the discrete antidiagonal (`offDiag_two_iff`).  We prove that the
compression `1_{X_k} F_N 1_{X_k}` has norm **exactly** `√(2/N)`:

* `binary_offdiag_fup_bound` — for every `f` supported in `X_k`,
  `‖1_{X_k} F_N f‖² ≤ (2/N) ‖f‖²`;
* `binary_offdiag_fup_sharp` — there is a unit vector `f` supported in `X_k` with
  `‖1_{X_k} F_N f‖² = 2/N`.

The proof follows the note: restricted to the antidiagonal, the transform becomes, up to
unimodular factors, the one-dimensional DFT evaluated at the odd frequencies `2ξ + 1`,
each odd residue being hit exactly twice; Parseval finishes.
-/

open Complex BigOperators Finset

namespace Bgs.Mathlib

instance (M k x y : ℕ) : Decidable (offDiag M k x y) := by
  unfold offDiag; infer_instance

/-- The unnormalized one-dimensional DFT `ĝ(m) = ∑_{x<N} e^{-2πi x m / N} g(x)`. -/
noncomputable def dft1 (N : ℕ) (g : ℕ → ℂ) (m : ℕ) : ℂ :=
  ∑ x ∈ range N, Complex.exp (-(2 * Real.pi * Complex.I * ((x * m : ℕ) : ℂ) / N)) * g x

/-! ## Digits in base two -/

/-- Two numbers below `M^k` with the same first `k` digits are equal. -/
lemma eq_of_digit_eq {M : ℕ} (hM : 1 ≤ M) :
    ∀ (k x y : ℕ), x < M ^ k → y < M ^ k → (∀ i < k, digit M i x = digit M i y) → x = y := by
  intro k
  induction k with
  | zero => intro x y hx hy _; simp at hx hy; omega
  | succ k ih =>
    intro x y hx hy h
    have hMpos : 0 < M := hM
    have hxq : x / M < M ^ k := by
      rw [Nat.div_lt_iff_lt_mul hMpos]; rw [pow_succ] at hx; exact hx
    have hyq : y / M < M ^ k := by
      rw [Nat.div_lt_iff_lt_mul hMpos]; rw [pow_succ] at hy; exact hy
    have h0 : x % M = y % M := by
      have := h 0 (by omega); rwa [digit_zero, digit_zero] at this
    have hq : x / M = y / M := ih _ _ hxq hyq fun i hi => by
      have := h (i + 1) (by omega); rwa [digit_succ, digit_succ] at this
    rw [← Nat.mod_add_div x M, ← Nat.mod_add_div y M, h0, hq]

/-- In base two, `X_k` is the antidiagonal. -/
theorem offDiag_two_iff {k x y : ℕ} (hx : x < 2 ^ k) (hy : y < 2 ^ k) :
    offDiag 2 k x y ↔ y = 2 ^ k - 1 - x := by
  constructor
  · intro h
    apply eq_of_digit_eq (by norm_num) k y _ hy (by omega)
    intro i hi
    rw [digit_complement (by norm_num) k x hx i hi]
    have h1 := h i hi
    have h2 : digit 2 i x < 2 := Nat.mod_lt _ (by norm_num)
    have h3 : digit 2 i y < 2 := Nat.mod_lt _ (by norm_num)
    omega
  · rintro rfl
    exact offDiag_complement (by decide) (by norm_num) hx

/-! ## One-dimensional facts -/

lemma dft1_add_period {N : ℕ} (hN : 0 < N) (g : ℕ → ℂ) (m : ℕ) :
    dft1 N g (m + N) = dft1 N g m := by
  have hN0 : (N : ℂ) ≠ 0 := by exact_mod_cast hN.ne'
  rw [dft1, dft1]
  refine Finset.sum_congr rfl fun x _ => ?_
  congr 1
  have : -(2 * Real.pi * Complex.I * ((x * (m + N) : ℕ) : ℂ) / N) =
      -(2 * Real.pi * Complex.I * ((x * m : ℕ) : ℂ) / N) + ((-(x : ℤ) : ℤ) : ℂ) * (2 * Real.pi * Complex.I) := by
    push_cast; field_simp; ring
  rw [this, Complex.exp_add, Complex.exp_int_mul_two_pi_mul_I, mul_one]

/-- Parseval for the unnormalized DFT. -/
lemma dft1_parseval {N : ℕ} (hN : 0 < N) (g : ℕ → ℂ) :
    ∑ m ∈ range N, ‖dft1 N g m‖ ^ 2 = N * ∑ x ∈ range N, ‖g x‖ ^ 2 := by
  have hN0 : (N : ℂ) ≠ 0 := by exact_mod_cast hN.ne'
  apply Complex.ofReal_injective
  push_cast
  simp_rw [← Complex.mul_conj']
  have key : ∀ x y m : ℕ, Complex.exp (-(2 * Real.pi * Complex.I * ((x * m : ℕ) : ℂ) / N)) *
      (starRingEnd ℂ) (Complex.exp (-(2 * Real.pi * Complex.I * ((y * m : ℕ) : ℂ) / N))) =
      Complex.exp (2 * Real.pi * Complex.I * (((y : ℤ) - x : ℤ) : ℂ) / N) ^ m := by
    intro x y m
    rw [← Complex.exp_conj, ← Complex.exp_add, ← Complex.exp_nat_mul]
    congr 1
    simp only [map_neg, map_div₀, map_mul, Complex.conj_ofReal, Complex.conj_I, map_natCast,
      map_ofNat]
    push_cast; ring
  have hexp : ∑ m ∈ range N, dft1 N g m * (starRingEnd ℂ) (dft1 N g m) =
      ∑ x ∈ range N, ∑ y ∈ range N, g x * (starRingEnd ℂ) (g y) *
        ∑ m ∈ range N, Complex.exp (2 * Real.pi * Complex.I * (((y : ℤ) - x : ℤ) : ℂ) / N) ^ m := by
    simp_rw [dft1, map_sum, Finset.sum_mul_sum, Finset.mul_sum]
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl fun x _ => ?_
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl fun y _ => ?_
    refine Finset.sum_congr rfl fun m _ => ?_
    rw [map_mul, ← key x y m]
    ring
  rw [hexp]
  have hinner : ∀ x ∈ range N, ∑ y ∈ range N, g x * (starRingEnd ℂ) (g y) *
      ∑ m ∈ range N, Complex.exp (2 * Real.pi * Complex.I * (((y : ℤ) - x : ℤ) : ℂ) / N) ^ m =
      N * (g x * (starRingEnd ℂ) (g x)) := by
    intro x hx
    simp_rw [geom_exp_sum hN]
    rw [Finset.sum_eq_single x]
    · simp; ring
    · intro y hy hyx
      rw [if_neg, mul_zero]
      rintro ⟨t, ht⟩
      have hx' := Finset.mem_range.1 hx; have hy' := Finset.mem_range.1 hy
      have : t = 0 := by
        by_contra ht0
        rcases lt_or_gt_of_ne ht0 with h | h
        · have : (N : ℤ) * t ≤ -(N : ℤ) := by nlinarith
          omega
        · have : (N : ℤ) ≤ (N : ℤ) * t := by nlinarith
          omega
      subst this
      omega
    · intro h; exact absurd hx h
  rw [Finset.sum_congr rfl hinner, ← Finset.mul_sum]

/-- The odd frequencies `2ξ + 1`, `ξ < N = 2h`, hit each odd residue exactly twice. -/
lemma sum_odd_freq {h : ℕ} (hh : 0 < h) (g : ℕ → ℂ) :
    ∑ ξ ∈ range (2 * h), ‖dft1 (2 * h) g (2 * ξ + 1)‖ ^ 2 =
      2 * ∑ m ∈ (range (2 * h)).filter Odd, ‖dft1 (2 * h) g m‖ ^ 2 := by
  have himg : (range (2 * h)).filter Odd = (range h).image (fun ξ => 2 * ξ + 1) := by
    ext m
    simp only [Finset.mem_filter, Finset.mem_range, Finset.mem_image]
    constructor
    · rintro ⟨hm, ξ, rfl⟩; exact ⟨ξ, by omega, rfl⟩
    · rintro ⟨ξ, hξ, rfl⟩; exact ⟨by omega, ξ, rfl⟩
  rw [himg, Finset.sum_image (fun a _ b _ hab => by omega),
    show 2 * h = h + h by ring, Finset.sum_range_add]
  have : ∀ ξ, ‖dft1 (h + h) g (2 * (h + ξ) + 1)‖ ^ 2 = ‖dft1 (h + h) g (2 * ξ + 1)‖ ^ 2 := by
    intro ξ
    rw [show 2 * (h + ξ) + 1 = (2 * ξ + 1) + (h + h) by ring, dft1_add_period (by omega)]
  simp_rw [this]
  ring

/-! ## Reduction of the two-dimensional transform -/

/-- On the antidiagonal, the 2D transform of an antidiagonal function is (up to a phase)
the 1D transform at the odd frequency `2ξ + 1`. -/
lemma norm_dft2_antidiag {N : ℕ} (hN : 0 < N) (f : ℕ × ℕ → ℂ)
    (hf : ∀ x y, f (x, y) ≠ 0 → x < N ∧ y = N - 1 - x) {ξ : ℕ} (hξ : ξ < N) :
    ‖dft2 N f ξ (N - 1 - ξ)‖ = (1 / (N : ℝ)) * ‖dft1 N (fun x => f (x, N - 1 - x)) (2 * ξ + 1)‖ := by
  have hN0 : (N : ℂ) ≠ 0 := by exact_mod_cast hN.ne'
  set c : ℂ := Complex.exp (-(2 * Real.pi * Complex.I * (((N - 1 : ℕ) : ℂ) * ((N - 1 - ξ : ℕ) : ℂ)) / N))
    with hc
  have hcn : ‖c‖ = 1 := by
    have : -(2 * Real.pi * Complex.I * (((N - 1 : ℕ) : ℂ) * ((N - 1 - ξ : ℕ) : ℂ)) / N) =
        ((-(2 * Real.pi * (((N - 1 : ℕ) : ℝ) * ((N - 1 - ξ : ℕ) : ℝ)) / N)) : ℝ) * Complex.I := by
      push_cast; ring
    rw [hc, this, Complex.norm_exp_ofReal_mul_I]
  have hred : dft2 N f ξ (N - 1 - ξ) = (1 / (N : ℂ)) * c * dft1 N (fun x => f (x, N - 1 - x)) (2 * ξ + 1) := by
    rw [dft2, dft1, mul_assoc (1 / (N : ℂ)) c]
    congr 1
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl fun x hx => ?_
    have hxN := Finset.mem_range.1 hx
    rw [Finset.sum_eq_single (N - 1 - x)]
    · rw [← mul_assoc]
      congr 1
      rw [hc, ← Complex.exp_add]
      have hx1 : ((N - 1 - x : ℕ) : ℂ) = (N : ℂ) - 1 - x := by
        rw [Nat.cast_sub (by omega), Nat.cast_sub (by omega)]; simp
      have hξ1 : ((N - 1 - ξ : ℕ) : ℂ) = (N : ℂ) - 1 - ξ := by
        rw [Nat.cast_sub (by omega), Nat.cast_sub (by omega)]; simp
      have hN1 : ((N - 1 : ℕ) : ℂ) = (N : ℂ) - 1 := by
        rw [Nat.cast_sub (by omega)]; simp
      have : -(2 * Real.pi * Complex.I * ((x * ξ + (N - 1 - x) * (N - 1 - ξ) : ℕ) : ℂ) / N) =
          -(2 * Real.pi * Complex.I * (((N - 1 : ℕ) : ℂ) * ((N - 1 - ξ : ℕ) : ℂ)) / N) +
          -(2 * Real.pi * Complex.I * ((x * (2 * ξ + 1) : ℕ) : ℂ) / N) +
          ((x : ℤ) : ℂ) * (2 * Real.pi * Complex.I) := by
        rw [Nat.cast_add, Nat.cast_mul, Nat.cast_mul, Nat.cast_mul, hx1, hξ1, hN1]
        push_cast
        field_simp
        ring
      rw [this, Complex.exp_add _ (((x : ℤ) : ℂ) * _), Complex.exp_int_mul_two_pi_mul_I, mul_one]
    · intro y _ hy
      have : f (x, y) = 0 := by
        by_contra h
        exact hy (hf x y h).2
      rw [this, mul_zero]
    · intro h; exfalso; exact h (Finset.mem_range.2 (by omega))
  rw [hred, norm_mul, norm_mul, hcn, mul_one, norm_div, norm_one, Complex.norm_natCast]

/-- The squared norm of `1_{X_k} F f`, written as a sum over the antidiagonal. -/
lemma compression_sq_eq {k : ℕ} (hk : 1 ≤ k) (f : ℕ × ℕ → ℂ)
    (hf : ∀ x y, f (x, y) ≠ 0 → x < 2 ^ k ∧ y < 2 ^ k ∧ offDiag 2 k x y) :
    ∑ ξ ∈ range (2 ^ k), ∑ η ∈ range (2 ^ k),
        (if offDiag 2 k ξ η then ‖dft2 (2 ^ k) f ξ η‖ ^ 2 else 0) =
      (2 / ((2 ^ k : ℕ) : ℝ) ^ 2) * ∑ m ∈ (range (2 ^ k)).filter Odd,
        ‖dft1 (2 ^ k) (fun x => f (x, 2 ^ k - 1 - x)) m‖ ^ 2 := by
  have hN : 0 < 2 ^ k := by positivity
  have hNr : (0 : ℝ) < ((2 ^ k : ℕ) : ℝ) := by exact_mod_cast hN
  have hf' : ∀ x y, f (x, y) ≠ 0 → x < 2 ^ k ∧ y = 2 ^ k - 1 - x := by
    intro x y h
    obtain ⟨hx, hy, ho⟩ := hf x y h
    exact ⟨hx, (offDiag_two_iff hx hy).1 ho⟩
  have hrow : ∀ ξ ∈ range (2 ^ k), ∑ η ∈ range (2 ^ k),
      (if offDiag 2 k ξ η then ‖dft2 (2 ^ k) f ξ η‖ ^ 2 else 0) =
      (1 / ((2 ^ k : ℕ) : ℝ) ^ 2) *
        ‖dft1 (2 ^ k) (fun x => f (x, 2 ^ k - 1 - x)) (2 * ξ + 1)‖ ^ 2 := by
    intro ξ hξ
    have hξ' := Finset.mem_range.1 hξ
    rw [Finset.sum_eq_single (2 ^ k - 1 - ξ)]
    · rw [if_pos ((offDiag_two_iff hξ' (by omega)).2 rfl),
        norm_dft2_antidiag hN f hf' hξ']
      push_cast
      ring
    · intro η hη hne
      rw [if_neg]
      intro ho
      exact hne ((offDiag_two_iff hξ' (Finset.mem_range.1 hη)).1 ho)
    · intro h; exfalso; exact h (Finset.mem_range.2 (by omega))
  rw [Finset.sum_congr rfl hrow, ← Finset.mul_sum]
  obtain ⟨j, rfl⟩ : ∃ j, k = j + 1 := ⟨k - 1, by omega⟩
  have h2 : 2 ^ (j + 1) = 2 * 2 ^ j := by ring
  rw [h2, sum_odd_freq (by positivity)]
  push_cast
  ring

lemma norm_sq_antidiag {k : ℕ} (f : ℕ × ℕ → ℂ)
    (hf : ∀ x y, f (x, y) ≠ 0 → x < 2 ^ k ∧ y < 2 ^ k ∧ offDiag 2 k x y) :
    ∑ x ∈ range (2 ^ k), ∑ y ∈ range (2 ^ k), ‖f (x, y)‖ ^ 2 =
      ∑ x ∈ range (2 ^ k), ‖f (x, 2 ^ k - 1 - x)‖ ^ 2 := by
  refine Finset.sum_congr rfl fun x hx => ?_
  have hx' := Finset.mem_range.1 hx
  rw [Finset.sum_eq_single (2 ^ k - 1 - x)]
  · intro y hy hne
    have : f (x, y) = 0 := by
      by_contra h
      obtain ⟨_, hy', ho⟩ := hf x y h
      exact hne ((offDiag_two_iff hx' hy').1 ho)
    rw [this, norm_zero]; ring
  · intro h; exfalso; exact h (Finset.mem_range.2 (by omega))

/-! ## Main theorems -/

/-- **Binary FUP upper bound.**  For `N = 2^k`, `k ≥ 1`, and every `f` supported in `X_k`,
`‖1_{X_k} F_N f‖² ≤ (2/N) ‖f‖²`. -/
theorem binary_offdiag_fup_bound {k : ℕ} (hk : 1 ≤ k) (f : ℕ × ℕ → ℂ)
    (hf : ∀ x y, f (x, y) ≠ 0 → x < 2 ^ k ∧ y < 2 ^ k ∧ offDiag 2 k x y) :
    ∑ ξ ∈ range (2 ^ k), ∑ η ∈ range (2 ^ k),
        (if offDiag 2 k ξ η then ‖dft2 (2 ^ k) f ξ η‖ ^ 2 else 0) ≤
      (2 / ((2 ^ k : ℕ) : ℝ)) * ∑ x ∈ range (2 ^ k), ∑ y ∈ range (2 ^ k), ‖f (x, y)‖ ^ 2 := by
  have hN : 0 < 2 ^ k := by positivity
  have hNr : (0 : ℝ) < ((2 ^ k : ℕ) : ℝ) := by exact_mod_cast hN
  rw [compression_sq_eq hk f hf, norm_sq_antidiag f hf]
  set g : ℕ → ℂ := fun x => f (x, 2 ^ k - 1 - x)
  have hsub : ∑ m ∈ (range (2 ^ k)).filter Odd, ‖dft1 (2 ^ k) g m‖ ^ 2 ≤
      ∑ m ∈ range (2 ^ k), ‖dft1 (2 ^ k) g m‖ ^ 2 :=
    Finset.sum_le_sum_of_subset_of_nonneg (Finset.filter_subset _ _) (fun _ _ _ => by positivity)
  rw [dft1_parseval hN] at hsub
  have h2 : (0 : ℝ) ≤ 2 / ((2 ^ k : ℕ) : ℝ) ^ 2 := by positivity
  calc (2 / ((2 ^ k : ℕ) : ℝ) ^ 2) * ∑ m ∈ (range (2 ^ k)).filter Odd, ‖dft1 (2 ^ k) g m‖ ^ 2
      ≤ (2 / ((2 ^ k : ℕ) : ℝ) ^ 2) * (((2 ^ k : ℕ) : ℝ) * ∑ x ∈ range (2 ^ k), ‖g x‖ ^ 2) :=
        mul_le_mul_of_nonneg_left (by exact_mod_cast hsub) h2
    _ = _ := by simp only [g]; field_simp

/-- **Binary FUP sharpness.**  There is a unit vector supported in `X_k` with
`‖1_{X_k} F_N f‖² = 2/N`.  Together with `binary_offdiag_fup_bound`, the compression norm is
exactly `√(2/N)`. -/
theorem binary_offdiag_fup_sharp {k : ℕ} (hk : 1 ≤ k) :
    ∃ f : ℕ × ℕ → ℂ,
      (∀ x y, f (x, y) ≠ 0 → x < 2 ^ k ∧ y < 2 ^ k ∧ offDiag 2 k x y) ∧
      ∑ x ∈ range (2 ^ k), ∑ y ∈ range (2 ^ k), ‖f (x, y)‖ ^ 2 = 1 ∧
      ∑ ξ ∈ range (2 ^ k), ∑ η ∈ range (2 ^ k),
        (if offDiag 2 k ξ η then ‖dft2 (2 ^ k) f ξ η‖ ^ 2 else 0) = 2 / ((2 ^ k : ℕ) : ℝ) := by
  have hN : 0 < 2 ^ k := by positivity
  have hNr : (0 : ℝ) < ((2 ^ k : ℕ) : ℝ) := by exact_mod_cast hN
  set N := 2 ^ k with hNdef
  set g : ℕ → ℂ := fun x => (1 / Real.sqrt (N : ℕ)) *
    Complex.exp (2 * Real.pi * Complex.I * (x : ℂ) / (N : ℕ)) with hg
  set f : ℕ × ℕ → ℂ := fun p => if p.1 < N ∧ p.2 = N - 1 - p.1 then g p.1 else 0 with hfdef
  have hgnorm : ∀ x, ‖g x‖ ^ 2 = 1 / (N : ℝ) := by
    intro x
    have : 2 * Real.pi * Complex.I * (x : ℂ) / (N : ℕ) =
        ((2 * Real.pi * x / (N : ℕ) : ℝ) : ℂ) * Complex.I := by push_cast; ring
    rw [hg]; simp only
    rw [this, norm_mul, Complex.norm_exp_ofReal_mul_I, mul_one, norm_div, norm_one,
      Complex.norm_real, Real.norm_eq_abs, abs_of_pos (Real.sqrt_pos.2 hNr), div_pow,
      Real.sq_sqrt hNr.le, one_pow]
  have hsupp : ∀ x y, f (x, y) ≠ 0 → x < N ∧ y < N ∧ offDiag 2 k x y := by
    intro x y h
    simp only [hfdef] at h
    split_ifs at h with hc
    · obtain ⟨hx, hy⟩ := hc
      have hy' : y < N := by omega
      exact ⟨hx, hy', (offDiag_two_iff hx hy').2 hy⟩
    · exact absurd rfl h
  have hfg : (fun x => f (x, N - 1 - x)) = fun x => if x < N then g x else 0 := by
    funext x; simp only [hfdef, and_true]
  have hdft : ∀ m, dft1 N (fun x => f (x, N - 1 - x)) m = dft1 N g m := by
    intro m
    rw [hfg, dft1, dft1]
    refine Finset.sum_congr rfl fun x hx => ?_
    rw [if_pos (Finset.mem_range.1 hx)]
  have heven : ∀ m, ¬ Odd m → dft1 N g m = 0 := by
    intro m hm
    have e : dft1 N g m = (1 / Real.sqrt (N : ℕ)) * ∑ x ∈ range N,
        Complex.exp (2 * Real.pi * Complex.I * ((1 - m : ℤ) : ℂ) / N) ^ x := by
      rw [dft1, Finset.mul_sum]
      refine Finset.sum_congr rfl fun x _ => ?_
      rw [hg]; simp only
      rw [← Complex.exp_nat_mul, mul_left_comm, ← Complex.exp_add]
      congr 2
      push_cast; ring
    rw [e, geom_exp_sum hN, if_neg, mul_zero]
    rintro ⟨t, ht⟩
    apply hm
    have hk' : (2 : ℤ) ∣ (N : ℤ) := by
      rw [hNdef]; push_cast
      exact dvd_pow_self 2 (by omega)
    have : (2 : ℤ) ∣ 1 - (m : ℤ) := hk'.trans ⟨t, ht⟩
    rcases Nat.even_or_odd m with he | ho
    · obtain ⟨r, hr⟩ := he; obtain ⟨u, hu⟩ := this
      exfalso; omega
    · exact ho
  refine ⟨f, hsupp, ?_, ?_⟩
  · rw [norm_sq_antidiag f hsupp, ← hNdef]
    have : ∀ x ∈ range N, ‖f (x, N - 1 - x)‖ ^ 2 = 1 / (N : ℝ) := by
      intro x hx
      have := congrFun hfg x
      rw [this, if_pos (Finset.mem_range.1 hx), hgnorm]
    rw [Finset.sum_congr rfl this, Finset.sum_const, Finset.card_range, nsmul_eq_mul]
    field_simp
  · rw [compression_sq_eq hk f hsupp, ← hNdef]
    simp_rw [hdft]
    have hall : ∑ m ∈ (range N).filter Odd, ‖dft1 N g m‖ ^ 2 =
        ∑ m ∈ range N, ‖dft1 N g m‖ ^ 2 := by
      apply Finset.sum_filter_of_ne
      intro m _ hne
      by_contra hodd
      exact hne (by rw [heven m hodd]; simp)
    rw [hall, dft1_parseval hN]
    simp_rw [hgnorm]
    rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul]
    field_simp

#print axioms eq_of_digit_eq
#print axioms offDiag_two_iff
#print axioms dft1_add_period
#print axioms dft1_parseval
#print axioms sum_odd_freq
#print axioms norm_dft2_antidiag
#print axioms compression_sq_eq
#print axioms norm_sq_antidiag
#print axioms binary_offdiag_fup_bound
#print axioms binary_offdiag_fup_sharp
end Bgs.Mathlib
