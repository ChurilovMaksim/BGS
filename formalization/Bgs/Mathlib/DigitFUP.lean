module
public import Mathlib
@[expose] public section

/-!
# Off-diagonal digit alphabets: the even-base saturation (BGS-FUP-001, §4)

Source: `mathematics/fixed-map/offdiagonal_digit_fup.md`.

For `M ≥ 2` and `N = M^k`, let `X_k ⊂ [0,N)²` be the set of pairs whose base-`M`
digits differ at every one of the `k` positions (`offDiag`).  The two-dimensional
unitary DFT is `(F f)(ξ, η) = N⁻¹ ∑_{x,y} e^{-2πi (xξ + yη)/N} f(x, y)` (`dft2`).

For **even `M ≥ 4`** the note proves that the compression `1_X F 1_X` has norm exactly
one at every scale, by an explicit unit vector.  We formalize the complete
construction:

* `digit_complement` — the digits of `N - 1 - x` are `M - 1 - r`;
* `digit_add_repunit_ne` — adding the repunit `d = 11…1₍M₎` modulo `N` changes every
  digit (carry analysis, valid for every `M ≥ 3`);
* `dft2_witness_eq_zero` — the transform of the witness is supported on the discrete
  line `η ≡ ξ + d (mod N)`;
* `even_offdiag_fup_saturated` — **main theorem**: there is `f` with `‖f‖₂ = 1`,
  supported in `X_k`, whose transform also has `‖F f‖₂ = 1` and is supported in `X_k`.
  Hence `‖1_X F 1_X‖ ≥ 1`; the reverse inequality is unitarity of `F`.
-/

open Complex BigOperators Finset

namespace Bgs.Mathlib

/-- The `i`-th base-`M` digit of `x`. -/
def digit (M i x : ℕ) : ℕ := x / M ^ i % M

/-- The base-`M` repunit `1 + M + ⋯ + M^{k-1} = (M^k - 1)/(M - 1)`. -/
def repunit (M k : ℕ) : ℕ := ∑ i ∈ range k, M ^ i

/-- Pairs whose first `k` base-`M` digits differ position-wise. -/
def offDiag (M k x y : ℕ) : Prop := ∀ i < k, digit M i x ≠ digit M i y

/-- The two-dimensional unitary DFT on `[0, N)²`. -/
noncomputable def dft2 (N : ℕ) (f : ℕ × ℕ → ℂ) (ξ η : ℕ) : ℂ :=
  (1 / (N : ℂ)) * ∑ x ∈ range N, ∑ y ∈ range N,
    Complex.exp (-(2 * Real.pi * Complex.I * ((x * ξ + y * η : ℕ) : ℂ) / N)) * f (x, y)

lemma digit_zero (M x : ℕ) : digit M 0 x = x % M := by simp [digit]

lemma digit_succ (M i x : ℕ) : digit M (i + 1) x = digit M i (x / M) := by
  simp [digit, Nat.div_div_eq_div_mul, pow_succ, mul_comm]

lemma repunit_succ (M k : ℕ) : repunit M (k + 1) = 1 + M * repunit M k := by
  rw [repunit, Finset.sum_range_succ', repunit, Finset.mul_sum]
  simp [pow_succ, mul_comm, add_comm]

/-- Digits of the complement `M^k - 1 - x`. -/
theorem digit_complement {M : ℕ} (hM : 1 ≤ M) :
    ∀ (k x : ℕ), x < M ^ k → ∀ i < k, digit M i (M ^ k - 1 - x) = M - 1 - digit M i x := by
  intro k
  induction k with
  | zero => intro x _ i hi; omega
  | succ k ih =>
    intro x hx i hi
    have hMpos : 0 < M := hM
    have hx0 : x % M < M := Nat.mod_lt _ hMpos
    have hxq : x / M < M ^ k := by
      rw [Nat.div_lt_iff_lt_mul hMpos]; rw [pow_succ] at hx; exact hx
    have hdecomp : M ^ (k + 1) - 1 - x = (M - 1 - x % M) + M * (M ^ k - 1 - x / M) := by
      have hx' := Nat.mod_add_div x M
      have hpk : 1 ≤ M ^ k := Nat.one_le_pow _ _ hMpos
      have hpk1 : 1 ≤ M ^ (k + 1) := Nat.one_le_pow _ _ hMpos
      zify [show x ≤ M ^ (k + 1) - 1 by omega, hpk1,
        show x % M ≤ M - 1 by omega, show 1 ≤ M by omega, show x / M ≤ M ^ k - 1 by omega,
        hpk]
      have hx'' : (x : ℤ) = x % M + M * (x / M) := by exact_mod_cast hx'.symm
      rw [pow_succ]
      linear_combination -hx''
    have hmod : (M ^ (k + 1) - 1 - x) % M = M - 1 - x % M := by
      rw [hdecomp, Nat.add_mul_mod_self_left, Nat.mod_eq_of_lt (by omega)]
    have hdiv : (M ^ (k + 1) - 1 - x) / M = M ^ k - 1 - x / M := by
      rw [hdecomp, Nat.add_mul_div_left _ _ hMpos, Nat.div_eq_of_lt (by omega), zero_add]
    rcases i with _ | j
    · rw [digit_zero, digit_zero, hmod]
    · rw [digit_succ, digit_succ, hdiv]
      exact ih _ hxq j (by omega)

/-- Adding the repunit (plus an incoming carry `c ≤ 1`) modulo `M^k` changes every
digit, for every base `M ≥ 3`. -/
theorem digit_add_repunit_ne {M : ℕ} (hM : 3 ≤ M) :
    ∀ (k ξ c : ℕ), ξ < M ^ k → c ≤ 1 → ∀ i < k,
      digit M i ((ξ + repunit M k + c) % M ^ k) ≠ digit M i ξ := by
  intro k
  induction k with
  | zero => intro ξ c _ _ i hi; omega
  | succ k ih =>
    intro ξ c hξ hc i hi
    have hMpos : 0 < M := by omega
    have hξ0 : ξ % M < M := Nat.mod_lt _ hMpos
    have hξq : ξ / M < M ^ k := by
      rw [Nat.div_lt_iff_lt_mul hMpos]; rw [pow_succ] at hξ; exact hξ
    set a := ξ % M + 1 + c with ha
    have hz : ξ + repunit M (k + 1) + c = a + M * (ξ / M + repunit M k) := by
      rw [repunit_succ, ha]
      have := Nat.mod_add_div ξ M
      nlinarith
    have hzmod : (ξ + repunit M (k + 1) + c) % M = a % M := by
      rw [hz, Nat.add_mul_mod_self_left]
    have hzdiv : (ξ + repunit M (k + 1) + c) / M = ξ / M + repunit M k + a / M := by
      rw [hz, Nat.add_mul_div_left _ _ hMpos]; ring
    have hw := Nat.mod_mul (a := M) (b := M ^ k) (x := ξ + repunit M (k + 1) + c)
    rw [← pow_succ'] at hw
    have ha_div : a / M ≤ 1 := by
      rw [Nat.div_le_iff_le_mul_add_pred hMpos]; omega
    rcases i with _ | j
    · rw [digit_zero, digit_zero, hw, Nat.add_mul_mod_self_left, Nat.mod_mod, hzmod]
      by_cases hlt : a < M
      · rw [Nat.mod_eq_of_lt hlt]; omega
      · rw [Nat.mod_eq_sub_mod (by omega), Nat.mod_eq_of_lt (by omega)]; omega
    · rw [digit_succ, digit_succ, hw, Nat.add_mul_div_left _ _ hMpos,
        Nat.div_eq_of_lt (Nat.mod_lt _ hMpos), zero_add, hzdiv]
      exact ih _ _ hξq ha_div j (by omega)

/-- For even `M`, a pair `(x, M^k - 1 - x)` lies in `X_k`. -/
theorem offDiag_complement {M : ℕ} (hMe : Even M) (hM : 1 ≤ M) {k x : ℕ} (hx : x < M ^ k) :
    offDiag M k x (M ^ k - 1 - x) := by
  intro i hi
  rw [digit_complement hM k x hx i hi]
  have : digit M i x < M := Nat.mod_lt _ (by omega)
  obtain ⟨t, ht⟩ := hMe
  omega

/-- The explicit witness `f(x, y) = N^{-1/2} 1_{y = N-1-x} e^{2πi d y / N}`. -/
noncomputable def fupWitness (M k : ℕ) (p : ℕ × ℕ) : ℂ :=
  if p.1 < M ^ k ∧ p.2 = M ^ k - 1 - p.1 then
    (1 / Real.sqrt (M ^ k : ℕ)) *
      Complex.exp (2 * Real.pi * Complex.I * ((repunit M k * p.2 : ℕ) : ℂ) / (M ^ k : ℕ))
  else 0

/-- Root-of-unity sums: `∑_{x<N} (e^{2πi m/N})^x` is `N` if `N ∣ m` and `0` otherwise. -/
lemma geom_exp_sum {N : ℕ} (hN : 0 < N) (m : ℤ) :
    ∑ x ∈ range N, Complex.exp (2 * Real.pi * Complex.I * m / N) ^ x =
      if (N : ℤ) ∣ m then (N : ℂ) else 0 := by
  have hN0 : (N : ℂ) ≠ 0 := by exact_mod_cast hN.ne'
  set w := Complex.exp (2 * Real.pi * Complex.I * m / N) with hw
  have hwN : w ^ N = 1 := by
    rw [hw, ← Complex.exp_nat_mul, Complex.exp_eq_one_iff]
    exact ⟨m, by field_simp⟩
  have hw1 : w = 1 ↔ (N : ℤ) ∣ m := by
    rw [hw, Complex.exp_eq_one_iff]
    constructor
    · rintro ⟨n, hn⟩
      refine ⟨n, ?_⟩
      have hpi : (2 * Real.pi * Complex.I : ℂ) ≠ 0 := by
        simp [Real.pi_ne_zero, Complex.I_ne_zero]
      field_simp at hn
      exact_mod_cast hn
    · rintro ⟨n, rfl⟩
      exact ⟨n, by push_cast; field_simp⟩
  split_ifs with h
  · rw [hw1.2 h]; simp
  · have hne : w ≠ 1 := fun h' => h (hw1.1 h')
    rw [geom_sum_eq hne, hwN, sub_self, zero_div]

/-- The transform of the witness: an explicit phase times a root-of-unity sum. -/
lemma dft2_fupWitness (M k ξ η : ℕ) (hN : 0 < M ^ k) :
    dft2 (M ^ k) (fupWitness M k) ξ η =
      (1 / (M ^ k : ℕ)) * (1 / Real.sqrt (M ^ k : ℕ)) *
        Complex.exp (2 * Real.pi * Complex.I *
          (((M ^ k : ℕ) : ℂ) - 1) * ((repunit M k : ℂ) - η) / (M ^ k : ℕ)) *
        ∑ x ∈ range (M ^ k), Complex.exp (2 * Real.pi * Complex.I *
          (((η : ℤ) - ξ - repunit M k : ℤ) : ℂ) / (M ^ k : ℕ)) ^ x := by
  set N := M ^ k with hNdef
  have hN0 : (N : ℂ) ≠ 0 := by exact_mod_cast hN.ne'
  rw [dft2, Finset.mul_sum, Finset.mul_sum]
  refine Finset.sum_congr rfl fun x hx => ?_
  have hxN : x < N := Finset.mem_range.1 hx
  rw [mul_assoc (1 / (N : ℂ)), mul_assoc (1 / (N : ℂ))]
  congr 1
  rw [Finset.sum_eq_single (N - 1 - x)]
  · have hf : fupWitness M k (x, N - 1 - x) = (1 / Real.sqrt (N : ℕ)) *
        Complex.exp (2 * Real.pi * Complex.I * ((repunit M k * (N - 1 - x) : ℕ) : ℂ) / (N : ℕ)) := by
      rw [fupWitness, if_pos (show x < M ^ k ∧ N - 1 - x = M ^ k - 1 - x from ⟨hxN, rfl⟩)]
    rw [hf, ← Complex.exp_nat_mul]
    have hcast : ((N - 1 - x : ℕ) : ℂ) = (N : ℂ) - 1 - x := by
      rw [Nat.cast_sub (by omega), Nat.cast_sub (by omega)]; simp
    have e : ∀ a b c : ℂ, Complex.exp a * (b * Complex.exp c) = b * Complex.exp (a + c) := by
      intro a b c; rw [Complex.exp_add]; ring
    rw [e]
    conv_rhs => rw [mul_assoc, ← Complex.exp_add]
    congr 2
    push_cast
    rw [hcast]
    field_simp
    ring
  · intro y _ hy
    rw [fupWitness, if_neg (by rintro ⟨_, h⟩; exact hy h), mul_zero]
  · intro h; exfalso; exact h (Finset.mem_range.2 (by omega))

theorem dft2_fupWitness_ne_zero {M k ξ η : ℕ} (hN : 0 < M ^ k)
    (h : dft2 (M ^ k) (fupWitness M k) ξ η ≠ 0) :
    ((M ^ k : ℕ) : ℤ) ∣ ((η : ℤ) - ξ - repunit M k) := by
  rw [dft2_fupWitness M k ξ η hN, geom_exp_sum hN] at h
  by_contra hc
  rw [if_neg hc, mul_zero] at h
  exact h rfl

theorem norm_sq_dft2_fupWitness (M k ξ η : ℕ) (hN : 0 < M ^ k) :
    ‖dft2 (M ^ k) (fupWitness M k) ξ η‖ ^ 2 =
      if ((M ^ k : ℕ) : ℤ) ∣ ((η : ℤ) - ξ - repunit M k) then 1 / ((M ^ k : ℕ) : ℝ) else 0 := by
  rw [dft2_fupWitness M k ξ η hN, geom_exp_sum hN]
  have hNr : (0 : ℝ) < ((M ^ k : ℕ) : ℝ) := by exact_mod_cast hN
  split_ifs with h
  · have hexp : ‖Complex.exp (2 * Real.pi * Complex.I *
          (((M ^ k : ℕ) : ℂ) - 1) * ((repunit M k : ℂ) - η) / (M ^ k : ℕ))‖ = 1 := by
      have : (2 * Real.pi * Complex.I * (((M ^ k : ℕ) : ℂ) - 1) * ((repunit M k : ℂ) - η) /
          (M ^ k : ℕ)) = ((2 * Real.pi * (((M ^ k : ℕ) : ℝ) - 1) * ((repunit M k : ℝ) - η) /
          (M ^ k : ℕ) : ℝ) : ℂ) * Complex.I := by push_cast; ring
      rw [this, Complex.norm_exp_ofReal_mul_I]
    rw [norm_mul, norm_mul, norm_mul, hexp, Complex.norm_natCast, norm_div, norm_one,
      Complex.norm_natCast, norm_div, norm_one, Complex.norm_real, Real.norm_eq_abs,
      abs_of_pos (Real.sqrt_pos.2 hNr)]
    field_simp
    rw [Real.sq_sqrt hNr.le]
  · simp

/-- **Main theorem (BGS-FUP-001, even bases).**  For even `M ≥ 4` and every `k`, there is a
unit vector supported in `X_k` whose unitary DFT is again a unit vector supported in
`X_k`.  Consequently `‖1_{X_k} F_N 1_{X_k}‖ = 1` at every scale. -/
theorem even_offdiag_fup_saturated {M : ℕ} (hMe : Even M) (hM : 3 ≤ M) (k : ℕ) :
    ∃ f : ℕ × ℕ → ℂ,
      (∀ x y, f (x, y) ≠ 0 → x < M ^ k ∧ y < M ^ k ∧ offDiag M k x y) ∧
      ∑ x ∈ range (M ^ k), ∑ y ∈ range (M ^ k), ‖f (x, y)‖ ^ 2 = 1 ∧
      (∀ ξ < M ^ k, ∀ η < M ^ k, dft2 (M ^ k) f ξ η ≠ 0 → offDiag M k ξ η) ∧
      ∑ ξ ∈ range (M ^ k), ∑ η ∈ range (M ^ k), ‖dft2 (M ^ k) f ξ η‖ ^ 2 = 1 := by
  have hM1 : 1 ≤ M := by omega
  have hN : 0 < M ^ k := pow_pos (by omega) k
  have hNr : (0 : ℝ) < ((M ^ k : ℕ) : ℝ) := by exact_mod_cast hN
  -- the unique frequency partner of `ξ`
  have hpartner : ∀ ξ η : ℕ, η < M ^ k →
      (((M ^ k : ℕ) : ℤ) ∣ ((η : ℤ) - ξ - repunit M k) ↔ η = (ξ + repunit M k) % M ^ k) := by
    intro ξ η hη
    constructor
    · intro h
      have hmod : ξ + repunit M k ≡ η [MOD M ^ k] := by
        rw [Nat.modEq_iff_dvd]; push_cast; rwa [show (η : ℤ) - (ξ + repunit M k) =
          (η : ℤ) - ξ - repunit M k by ring]
      rw [hmod, Nat.mod_eq_of_lt hη]
    · rintro rfl
      have hmod : ξ + repunit M k ≡ (ξ + repunit M k) % M ^ k [MOD M ^ k] :=
        (Nat.mod_modEq _ _).symm
      rw [Nat.modEq_iff_dvd] at hmod
      push_cast at hmod
      rwa [show (((ξ + repunit M k) % M ^ k : ℕ) : ℤ) - ξ - repunit M k =
        (((ξ + repunit M k) % M ^ k : ℕ) : ℤ) - (ξ + repunit M k) by ring]
  refine ⟨fupWitness M k, ?_, ?_, ?_, ?_⟩
  · intro x y h
    rw [fupWitness] at h
    split_ifs at h with hc
    · obtain ⟨hx, hy⟩ := hc
      simp only at hx hy
      subst hy
      exact ⟨hx, by omega, offDiag_complement hMe hM1 hx⟩
    · exact absurd rfl h
  · have hrow : ∀ x ∈ range (M ^ k),
        ∑ y ∈ range (M ^ k), ‖fupWitness M k (x, y)‖ ^ 2 = 1 / ((M ^ k : ℕ) : ℝ) := by
      intro x hx
      have hxN := Finset.mem_range.1 hx
      rw [Finset.sum_eq_single (M ^ k - 1 - x)]
      · rw [fupWitness, if_pos ⟨hxN, rfl⟩, norm_mul]
        have hexp : ‖Complex.exp (2 * Real.pi * Complex.I *
            ((repunit M k * (M ^ k - 1 - x) : ℕ) : ℂ) / (M ^ k : ℕ))‖ = 1 := by
          have : 2 * Real.pi * Complex.I * ((repunit M k * (M ^ k - 1 - x) : ℕ) : ℂ) /
              (M ^ k : ℕ) = ((2 * Real.pi * ((repunit M k * (M ^ k - 1 - x) : ℕ) : ℝ) /
              (M ^ k : ℕ) : ℝ) : ℂ) * Complex.I := by push_cast; ring
          rw [this, Complex.norm_exp_ofReal_mul_I]
        rw [hexp, mul_one, norm_div, norm_one, Complex.norm_real, Real.norm_eq_abs,
          abs_of_pos (Real.sqrt_pos.2 hNr), div_pow, Real.sq_sqrt hNr.le, one_pow]
      · intro y _ hy
        rw [fupWitness, if_neg (by rintro ⟨_, h⟩; exact hy h)]; simp
      · intro h; exfalso; exact h (Finset.mem_range.2 (by omega))
    rw [Finset.sum_congr rfl hrow, Finset.sum_const, Finset.card_range, nsmul_eq_mul]
    field_simp
  · intro ξ hξ η hη h
    have hdvd := dft2_fupWitness_ne_zero hN h
    rw [hpartner ξ η hη] at hdvd
    intro i hi heq
    have := digit_add_repunit_ne hM k ξ 0 hξ (Nat.zero_le _) i hi
    rw [add_zero, ← hdvd] at this
    exact this heq.symm
  · have hrow : ∀ ξ ∈ range (M ^ k),
        ∑ η ∈ range (M ^ k), ‖dft2 (M ^ k) (fupWitness M k) ξ η‖ ^ 2 = 1 / ((M ^ k : ℕ) : ℝ) := by
      intro ξ _
      simp_rw [norm_sq_dft2_fupWitness M k ξ _ hN]
      rw [Finset.sum_eq_single ((ξ + repunit M k) % M ^ k)]
      · rw [if_pos ((hpartner ξ _ (Nat.mod_lt _ hN)).2 rfl)]
      · intro η hη hne
        rw [if_neg (fun h => hne ((hpartner ξ η (Finset.mem_range.1 hη)).1 h))]
      · intro h; exfalso; exact h (Finset.mem_range.2 (Nat.mod_lt _ hN))
    rw [Finset.sum_congr rfl hrow, Finset.sum_const, Finset.card_range, nsmul_eq_mul]
    field_simp

#print axioms digit_zero
#print axioms digit_succ
#print axioms repunit_succ
#print axioms digit_complement
#print axioms digit_add_repunit_ne
#print axioms offDiag_complement
#print axioms geom_exp_sum
#print axioms dft2_fupWitness
#print axioms dft2_fupWitness_ne_zero
#print axioms norm_sq_dft2_fupWitness
#print axioms even_offdiag_fup_saturated
end Bgs.Mathlib
