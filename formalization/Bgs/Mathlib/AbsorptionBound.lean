module
public import Mathlib
@[expose] public section

/-!
# Exact real scalar absorption bound and bosonic-body scalar lemmas
(`mathematics/trace-bridge/real_absorption_body_coercivity.md`,
`mathematics/trace-bridge/matrix_block_body_coercivity.md`,
`mathematics/trace-bridge/actual_body_coercivity_constants.md`)

* `absorption_scalar_identity`:
  `4|1−αλ|² − (1+α)²|1−λ|² = (1−α)[(1+3α)(1−|λ|²) + 2(1−α)(1+Re λ)]`.
* `absorption_scalar_bound`: `|1−αλ| ≥ ((1+α)/2)|1−λ|` for `|λ| ≤ 1`, `0 ≤ α ≤ 1`.
* `det_one_sub_smul_eq_prod`: `det(I − αA) = ∏_j (1 − αλ_j)` over the eigenvalues
  (roots of the characteristic polynomial, with algebraic multiplicity).
* `absorption_det_bound` **(A1)**: if every eigenvalue of `A ∈ M_d(ℂ)` has `|λ| ≤ 1` and
  `0 ≤ α ≤ 1`, then `|det(I−αA)| ≥ ((1+α)/2)^d |det(I−A)|`; no normality is needed.
  `absorption_det_bound_of_contraction`: the same for every Euclidean contraction.
* `absorption_det_sharp`: equality for `A = −I`.
* `log_half_one_add_exp_neg`, `absorption_log_term_ge` **(A3)**:
  `M log((1+e^{−s/N})/2) = −Ms/(2N) + M log cosh(s/(2N)) ≥ −Ms/(2N)`
  (with `M = Nk` this is `−ks/2 + Nk log cosh(s/(2N)) ≥ −ks/2`).
* `absorption_complex_counterexample`: for `A = −3i/4`, `α = i/2` the bound with `|α|` fails.
* `logcosh_div_ge`: `log cosh(s/K) ≥ K⁻² log cosh s` for `K ≥ 1` (the Jensen step).
* `neg_log_one_sub_tanh_sq`: `−log(1 − tanh² r) = 2 log cosh r` (`H = 2 ∑ Φ(W_j)`).
* `actual_constants`: `K = 1 + √(5−1)/(1−1/2) = 5`, `c = 1/(2K²) = 1/50`, and
  `4(1 + 2·10⁻⁶⁶)² < 5`.
-/

open Real Complex Polynomial

namespace Bgs.Mathlib

namespace Absorption

/-! ## The scalar inequality -/

theorem absorption_scalar_identity (α : ℝ) (μ : ℂ) :
    4 * ‖1 - (α : ℂ) * μ‖ ^ 2 - (1 + α) ^ 2 * ‖1 - μ‖ ^ 2 =
      (1 - α) * ((1 + 3 * α) * (1 - ‖μ‖ ^ 2) + 2 * (1 - α) * (1 + μ.re)) := by
  simp only [← Complex.normSq_eq_norm_sq, Complex.normSq_apply]
  simp only [Complex.sub_re, Complex.one_re, Complex.mul_re, Complex.ofReal_re,
    Complex.ofReal_im, Complex.sub_im, Complex.one_im, Complex.mul_im]
  ring

theorem absorption_scalar_bound {α : ℝ} (h0 : 0 ≤ α) (h1 : α ≤ 1) {μ : ℂ} (hμ : ‖μ‖ ≤ 1) :
    (1 + α) / 2 * ‖1 - μ‖ ≤ ‖1 - (α : ℂ) * μ‖ := by
  have hid := absorption_scalar_identity α μ
  have hre : -1 ≤ μ.re := by
    have := Complex.abs_re_le_norm μ
    have := neg_abs_le μ.re
    linarith
  have hsq : 0 ≤ 1 - ‖μ‖ ^ 2 := by nlinarith [norm_nonneg μ]
  have hrhs : 0 ≤ (1 - α) * ((1 + 3 * α) * (1 - ‖μ‖ ^ 2) + 2 * (1 - α) * (1 + μ.re)) := by
    apply mul_nonneg (by linarith)
    apply add_nonneg
    · exact mul_nonneg (by linarith) hsq
    · exact mul_nonneg (mul_nonneg (by norm_num) (by linarith)) (by linarith)
  have hle : ((1 + α) / 2 * ‖1 - μ‖) ^ 2 ≤ ‖1 - (α : ℂ) * μ‖ ^ 2 := by nlinarith
  exact (pow_le_pow_iff_left₀ (by positivity) (norm_nonneg _) two_ne_zero).1 hle

/-! ## Determinants as products over eigenvalues -/

lemma norm_multiset_prod_map (s : Multiset ℂ) (f : ℂ → ℂ) :
    ‖(s.map f).prod‖ = (s.map (fun x => ‖f x‖)).prod := by
  have := map_multiset_prod (normHom : ℂ →*₀ ℝ) (s.map f)
  simpa [Multiset.map_map] using this

variable {d : ℕ}

theorem det_one_sub_smul_eq_prod (A : Matrix (Fin d) (Fin d) ℂ) (α : ℂ) :
    (1 - α • A).det = (A.charpoly.roots.map (fun μ => 1 - α * μ)).prod := by
  have hsplit : A.charpoly = (A.charpoly.roots.map (fun a => X - C a)).prod :=
    (IsAlgClosed.splits _).eq_prod_roots_of_monic (Matrix.charpoly_monic A)
  have hcard : A.charpoly.roots.card = d := by
    rw [(splits_iff_card_roots).1 (IsAlgClosed.splits _), Matrix.charpoly_natDegree_eq_dim,
      Fintype.card_fin]
  by_cases hα : α = 0
  · subst hα; simp
  · have hmat : (1 : Matrix (Fin d) (Fin d) ℂ) - α • A = α • (Matrix.scalar (Fin d) α⁻¹ - A) := by
      rw [smul_sub, Matrix.scalar_apply, ← Matrix.smul_one_eq_diagonal, smul_smul,
        mul_inv_cancel₀ hα, one_smul]
    rw [hmat, Matrix.det_smul, Fintype.card_fin, ← Matrix.eval_charpoly]
    conv_lhs => rw [hsplit]
    rw [Polynomial.eval_multiset_prod, Multiset.map_map]
    have hpow : α ^ d = (A.charpoly.roots.map (fun _ => α)).prod := by
      rw [Multiset.map_const', Multiset.prod_replicate, hcard]
    rw [hpow, ← Multiset.prod_map_mul]
    congr 1
    apply Multiset.map_congr rfl
    intro μ _
    simp only [Function.comp, eval_sub, eval_X, eval_C]
    field_simp

/-- **(A1)** The exact real scalar absorption bound. -/
theorem absorption_det_bound (A : Matrix (Fin d) (Fin d) ℂ)
    (hA : ∀ μ ∈ A.charpoly.roots, ‖μ‖ ≤ 1) {α : ℝ} (h0 : 0 ≤ α) (h1 : α ≤ 1) :
    ((1 + α) / 2) ^ d * ‖(1 - A).det‖ ≤ ‖(1 - (α : ℂ) • A).det‖ := by
  have hcard : A.charpoly.roots.card = d := by
    rw [(splits_iff_card_roots).1 (IsAlgClosed.splits _), Matrix.charpoly_natDegree_eq_dim,
      Fintype.card_fin]
  have e1 := det_one_sub_smul_eq_prod A 1
  simp only [one_smul, one_mul] at e1
  rw [e1, det_one_sub_smul_eq_prod, norm_multiset_prod_map, norm_multiset_prod_map]
  have hpow : ((1 + α) / 2) ^ d = (A.charpoly.roots.map (fun _ => (1 + α) / 2)).prod := by
    rw [Multiset.map_const', Multiset.prod_replicate, hcard]
  rw [hpow, ← Multiset.prod_map_mul]
  apply Multiset.prod_map_le_prod_map₀
  · intro μ _; positivity
  · intro μ hμ; exact absorption_scalar_bound h0 h1 (hA μ hμ)

/-- Every Euclidean contraction has all its eigenvalues in the closed unit disk. -/
theorem eigenvalue_norm_le_of_contraction (A : Matrix (Fin d) (Fin d) ℂ)
    (hA : ∀ v : Fin d → ℂ, ∑ i, ‖A.mulVec v i‖ ^ 2 ≤ ∑ i, ‖v i‖ ^ 2) :
    ∀ μ ∈ A.charpoly.roots, ‖μ‖ ≤ 1 := by
  intro μ hμ
  have hroot : A.charpoly.IsRoot μ := (Polynomial.mem_roots (Matrix.charpoly_monic A).ne_zero).1 hμ
  rw [Polynomial.IsRoot, Matrix.eval_charpoly] at hroot
  obtain ⟨v, hv, hAv⟩ := Matrix.exists_mulVec_eq_zero_iff.2 hroot
  have heig : A.mulVec v = μ • v := by
    rw [Matrix.sub_mulVec, Matrix.scalar_apply, ← Matrix.smul_one_eq_diagonal,
      Matrix.smul_mulVec, Matrix.one_mulVec, sub_eq_zero] at hAv
    exact hAv.symm
  have h := hA v
  rw [heig] at h
  simp only [Pi.smul_apply, smul_eq_mul, norm_mul, mul_pow] at h
  rw [← Finset.mul_sum] at h
  have hpos : 0 < ∑ i, ‖v i‖ ^ 2 := by
    obtain ⟨i, hi⟩ := Function.ne_iff.1 hv
    have hi' : 0 < ‖v i‖ := norm_pos_iff.2 hi
    exact lt_of_lt_of_le (by positivity : 0 < ‖v i‖ ^ 2)
      (Finset.single_le_sum (f := fun j => ‖v j‖ ^ 2) (fun j _ => by positivity)
        (Finset.mem_univ i))
  have : ‖μ‖ ^ 2 ≤ 1 := by
    by_contra hc; have hc' := not_le.1 hc; nlinarith
  nlinarith [norm_nonneg μ]

/-- **(A1)** for every (not necessarily normal) contraction. -/
theorem absorption_det_bound_of_contraction (A : Matrix (Fin d) (Fin d) ℂ)
    (hA : ∀ v : Fin d → ℂ, ∑ i, ‖A.mulVec v i‖ ^ 2 ≤ ∑ i, ‖v i‖ ^ 2)
    {α : ℝ} (h0 : 0 ≤ α) (h1 : α ≤ 1) :
    ((1 + α) / 2) ^ d * ‖(1 - A).det‖ ≤ ‖(1 - (α : ℂ) • A).det‖ :=
  absorption_det_bound A (eigenvalue_norm_le_of_contraction A hA) h0 h1

/-- Sharpness: `A = −I` attains equality in (A1). -/
theorem absorption_det_sharp (α : ℝ) (h0 : 0 ≤ α) :
    ((1 + α) / 2) ^ d * ‖(1 - (-1 : Matrix (Fin d) (Fin d) ℂ)).det‖ =
      ‖(1 - (α : ℂ) • (-1 : Matrix (Fin d) (Fin d) ℂ)).det‖ := by
  have e1 : (1 : Matrix (Fin d) (Fin d) ℂ) - -1 = (2 : ℂ) • 1 := by
    rw [sub_neg_eq_add, two_smul]
  have e2 : (1 : Matrix (Fin d) (Fin d) ℂ) - (α : ℂ) • -1 = ((1 + α : ℝ) : ℂ) • 1 := by
    rw [smul_neg, sub_neg_eq_add]
    ext i j
    simp only [Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply, smul_eq_mul]
    split_ifs <;> push_cast <;> ring
  rw [e1, e2, Matrix.det_smul, Matrix.det_smul]
  simp only [Matrix.det_one, mul_one, Fintype.card_fin, norm_pow, Complex.norm_real,
    Real.norm_eq_abs, abs_of_nonneg (by linarith : (0 : ℝ) ≤ 1 + α)]
  rw [show ‖(2 : ℂ)‖ = 2 by simp, ← mul_pow]
  congr 1; ring

/-! ## The logarithmic absorption term (A2)–(A3) -/

theorem half_one_add_exp_neg (t : ℝ) :
    (1 + Real.exp (-t)) / 2 = Real.exp (-t / 2) * Real.cosh (t / 2) := by
  rw [Real.cosh_eq, mul_div_assoc', mul_add, ← Real.exp_add, ← Real.exp_add,
    show -t / 2 + t / 2 = 0 by ring, show -t / 2 + -(t / 2) = -t by ring, Real.exp_zero]

theorem log_half_one_add_exp_neg (t : ℝ) :
    Real.log ((1 + Real.exp (-t)) / 2) = -t / 2 + Real.log (Real.cosh (t / 2)) := by
  rw [half_one_add_exp_neg, Real.log_mul (Real.exp_pos _).ne' (Real.cosh_pos _).ne',
    Real.log_exp]

/-- **(A3)**: `M log((1+e^{−s/N})/2) = −Ms/(2N) + M log cosh(s/(2N)) ≥ −Ms/(2N)`. -/
theorem absorption_log_term_ge (M N s : ℝ) (hM : 0 ≤ M) :
    M * Real.log ((1 + Real.exp (-(s / N))) / 2) =
        -(M * s / (2 * N)) + M * Real.log (Real.cosh (s / (2 * N))) ∧
      -(M * s / (2 * N)) ≤ M * Real.log ((1 + Real.exp (-(s / N))) / 2) := by
  have h := log_half_one_add_exp_neg (s / N)
  have e : s / N / 2 = s / (2 * N) := by rw [div_div, mul_comm]
  rw [e] at h
  have hval : M * Real.log ((1 + Real.exp (-(s / N))) / 2) =
      -(M * s / (2 * N)) + M * Real.log (Real.cosh (s / (2 * N))) := by
    rw [h]; rw [show -(s / N) / 2 = -(s / (2 * N)) by rw [neg_div, e]]; ring
  refine ⟨hval, ?_⟩
  rw [hval]
  have : 0 ≤ Real.log (Real.cosh (s / (2 * N))) := Real.log_nonneg (Real.one_le_cosh _)
  nlinarith

/-- The constant does not extend to complex `α` via `|α|`. -/
theorem absorption_complex_counterexample :
    ‖1 - (Complex.I / 2) * (-3 * Complex.I / 4)‖ = 5 / 8 ∧
      (1 + ‖Complex.I / 2‖) * ‖1 - (-3 * Complex.I / 4)‖ / 2 = 15 / 16 ∧
      ‖1 - (Complex.I / 2) * (-3 * Complex.I / 4)‖ <
        (1 + ‖Complex.I / 2‖) * ‖1 - (-3 * Complex.I / 4)‖ / 2 := by
  have h1 : (1 : ℂ) - (Complex.I / 2) * (-3 * Complex.I / 4) = ((5 / 8 : ℝ) : ℂ) := by
    have := Complex.I_sq; push_cast; linear_combination (3 / 8 : ℂ) * this
  have h2 : ‖Complex.I / 2‖ = 1 / 2 := by simp
  have h3 : ‖(1 : ℂ) - (-3 * Complex.I / 4)‖ = 5 / 4 := by
    rw [show (1 : ℂ) - (-3 * Complex.I / 4) = ⟨1, 3 / 4⟩ by
      apply Complex.ext <;> norm_num]
    rw [Complex.norm_def, Complex.normSq_mk]
    rw [show (1 : ℝ) * 1 + 3 / 4 * (3 / 4) = (5 / 4) ^ 2 by norm_num]
    exact Real.sqrt_sq (by norm_num)
  refine ⟨?_, ?_, ?_⟩
  · rw [h1, Complex.norm_real, Real.norm_eq_abs, abs_of_pos (by norm_num)]
  · rw [h2, h3]; norm_num
  · rw [h1, h2, h3, Complex.norm_real, Real.norm_eq_abs, abs_of_pos (by norm_num)]; norm_num

/-! ## Scalar lemmas of the bare-body coercivity argument -/

/-- `t tanh t ≤ 2 log cosh t` for `t ≥ 0`. -/
lemma mul_tanh_le_two_logcosh {t : ℝ} (ht : 0 ≤ t) :
    t * Real.tanh t ≤ 2 * Real.log (Real.cosh t) := by
  -- `g(t) = 2 log cosh t − t tanh t` is monotone with `g(0) = 0`
  let g : ℝ → ℝ := fun t => 2 * Real.log (Real.cosh t) - t * (Real.sinh t / Real.cosh t)
  have hg : ∀ x, HasDerivAt g ((Real.sinh x * Real.cosh x - x) / Real.cosh x ^ 2) x := by
    intro x
    have hc : Real.cosh x ≠ 0 := (Real.cosh_pos x).ne'
    have h1 := ((Real.hasDerivAt_cosh x).log hc).const_mul 2
    have h2 := (hasDerivAt_id x).mul ((Real.hasDerivAt_sinh x).div (Real.hasDerivAt_cosh x) hc)
    convert! h1.sub h2 using 1
    simp only [id, Pi.div_apply]
    field_simp
    rw [show Real.cosh x ^ 2 = Real.sinh x ^ 2 + 1 by rw [Real.cosh_sq]]
    ring
  have hmono : MonotoneOn g (Set.Ici 0) := by
    apply monotoneOn_of_deriv_nonneg (convex_Ici 0)
    · exact fun x _ => (hg x).continuousAt.continuousWithinAt
    · exact fun x _ => (hg x).differentiableAt.differentiableWithinAt
    · intro x hx
      rw [interior_Ici] at hx
      rw [(hg x).deriv]
      apply div_nonneg _ (by positivity)
      have : x ≤ Real.sinh x * Real.cosh x := by
        have h2x := Real.self_le_sinh_iff.2 (by linarith [hx.out] : 0 ≤ 2 * x)
        rw [Real.sinh_two_mul] at h2x; linarith
      linarith
  have := hmono (Set.mem_Ici.2 le_rfl) (Set.mem_Ici.2 ht) ht
  simp only [g, Real.cosh_zero, Real.log_one, Real.sinh_zero, zero_div, mul_zero, sub_zero] at this
  rw [Real.tanh_eq_sinh_div_cosh]
  linarith

/-- `tanh t / t` is antitone on `(0, ∞)`. -/
lemma tanh_div_antitone {x y : ℝ} (hx : 0 < x) (hy : 0 < y) (hxy : x ≤ y) :
    Real.tanh y / y ≤ Real.tanh x / x := by
  have hd : ∀ t, 0 < t → HasDerivAt (fun t => Real.sinh t / (t * Real.cosh t))
      ((t - Real.sinh t * Real.cosh t) / (t * Real.cosh t) ^ 2) t := by
    intro t ht
    have hc : t * Real.cosh t ≠ 0 := (mul_pos ht (Real.cosh_pos t)).ne'
    have := (Real.hasDerivAt_sinh t).div ((hasDerivAt_id t).mul (Real.hasDerivAt_cosh t)) hc
    convert! this using 1
    simp only [id, Pi.mul_apply]
    field_simp
    rw [show Real.cosh t ^ 2 = Real.sinh t ^ 2 + 1 by rw [Real.cosh_sq]]
    ring
  have hanti : AntitoneOn (fun t => Real.sinh t / (t * Real.cosh t)) (Set.Ioi 0) := by
    apply antitoneOn_of_deriv_nonpos (convex_Ioi 0)
    · exact fun t ht => (hd t ht).continuousAt.continuousWithinAt
    · intro t ht
      rw [interior_Ioi] at ht
      exact (hd t ht).differentiableAt.differentiableWithinAt
    · intro t ht
      rw [interior_Ioi] at ht
      have ht0 : 0 < t := ht
      rw [(hd t ht0).deriv]
      apply div_nonpos_of_nonpos_of_nonneg _ (by positivity)
      have h2t := Real.self_le_sinh_iff.2 (by linarith : 0 ≤ 2 * t)
      rw [Real.sinh_two_mul] at h2t; linarith
  have := hanti hx hy hxy
  simp only at this
  rw [Real.tanh_eq_sinh_div_cosh, Real.tanh_eq_sinh_div_cosh, div_div, div_div,
    mul_comm (Real.cosh y), mul_comm (Real.cosh x)]
  exact this

/-- `log cosh t / t²` is antitone on `(0,∞)`; in the form used in the argument:
`log cosh(s/K) ≥ K⁻² log cosh s` for `K ≥ 1`. -/
theorem logcosh_div_ge {K : ℝ} (hK : 1 ≤ K) (s : ℝ) :
    Real.log (Real.cosh s) / K ^ 2 ≤ Real.log (Real.cosh (s / K)) := by
  -- reduce to `s ≥ 0` by evenness
  wlog hs : 0 ≤ s generalizing s
  · have := this (-s) (by linarith)
    rwa [Real.cosh_neg, neg_div, Real.cosh_neg] at this
  have hK0 : 0 < K := by linarith
  -- `φ(u) = K² log cosh(u/K) − log cosh u` is antitone… we show it is ≥ 0 via monotonicity
  let φ : ℝ → ℝ := fun u => K ^ 2 * Real.log (Real.cosh (u / K)) - Real.log (Real.cosh u)
  have hφ : ∀ u, HasDerivAt φ (K * Real.tanh (u / K) - Real.tanh u) u := by
    intro u
    have h1 := (((hasDerivAt_id u).div_const K).cosh.log (Real.cosh_pos _).ne').const_mul (K ^ 2)
    have h2 := (Real.hasDerivAt_cosh u).log (Real.cosh_pos u).ne'
    convert! h1.sub h2 using 1
    simp only [id, Real.tanh_eq_sinh_div_cosh]
    field_simp
  have hmono : MonotoneOn φ (Set.Ici 0) := by
    apply monotoneOn_of_deriv_nonneg (convex_Ici 0)
    · exact fun x _ => (hφ x).continuousAt.continuousWithinAt
    · exact fun x _ => (hφ x).differentiableAt.differentiableWithinAt
    · intro u hu
      rw [interior_Ici] at hu
      have hu0 : 0 < u := hu
      rw [(hφ u).deriv, sub_nonneg]
      -- `tanh u ≤ K tanh(u/K)`: `tanh(x)/x` is antitone (concavity of `tanh` on `[0,∞)`)
      have := tanh_div_antitone (by positivity : (0:ℝ) < u / K) hu0 (div_le_self hu0.le hK)
      rw [div_div_eq_mul_div, div_le_div_iff₀ hu0 hu0] at this
      nlinarith
  have := hmono (Set.mem_Ici.2 le_rfl) (Set.mem_Ici.2 hs) hs
  simp only [φ, zero_div, Real.cosh_zero, Real.log_one, mul_zero, sub_zero] at this
  rw [div_le_iff₀ (by positivity)]
  linarith

/-- `−log(1 − tanh² r) = 2 log cosh r`. -/
theorem neg_log_one_sub_tanh_sq (r : ℝ) :
    -Real.log (1 - Real.tanh r ^ 2) = 2 * Real.log (Real.cosh r) := by
  have hc : Real.cosh r ≠ 0 := (Real.cosh_pos r).ne'
  have : 1 - Real.tanh r ^ 2 = (Real.cosh r ^ 2)⁻¹ := by
    rw [Real.tanh_eq_sinh_div_cosh]
    field_simp
    rw [Real.cosh_sq]; ring
  rw [this, Real.log_inv, neg_neg, Real.log_pow]; push_cast; ring

/-- The explicit eventual constants for the actual family. -/
theorem actual_constants :
    (1 + Real.sqrt (5 - 1) / (1 - 1 / 2) = (5 : ℝ)) ∧
      (1 / (2 * (5 : ℝ) ^ 2) = 1 / 50) ∧
      (4 * (1 + 2 * (10 : ℝ) ^ (-66 : ℤ)) ^ 2 < 5) := by
  refine ⟨?_, by norm_num, ?_⟩
  · rw [show (5 : ℝ) - 1 = 2 ^ 2 by norm_num, Real.sqrt_sq (by norm_num)]; norm_num
  · have h : (10 : ℝ) ^ (-66 : ℤ) ≤ 1 / 100 := by
      rw [zpow_neg]; norm_num
    have h0 : 0 < (10 : ℝ) ^ (-66 : ℤ) := by positivity
    generalize (10 : ℝ) ^ (-66 : ℤ) = x at h h0 ⊢
    nlinarith

end Absorption

end Bgs.Mathlib
