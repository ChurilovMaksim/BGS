module
public import Mathlib
@[expose] public section

/-!
# Second moment of the frozen two-step increment (BGS-TRACE-078)

Source: `mathematics/trace-bridge/two_step_increment_variance.md`.

Setting: `S` unitary of size `u`, `P = |S|²`, `K = P²`, `δ = max P ≤ 1/4`.

* `feedback_coeff_norm_le`: `|q_e| = |w_e/(1 - S_ee w_e)| ≤ 2` for `|w_e| = 1`, `|S_ee|² ≤ 1/4`.
* `increment_pointwise_le`: from the exact expansion (V2),
  `|Δ_e| ≤ r_e + 4|A_e| + 4|B_e| + 8|C_e| + 16|D_e| + 16 F_e`.
* `increment_second_moment_le`: the **combination** step — the six squared-sum bounds of the
  note imply `∑_e Δ_e² ≤ 2598 δ² [K_ij + (P³)_ij]` (hence (V1) with the constant `2600` after
  dividing by `u`).
* Coordinate squared-sum bounds proved for the actual unitary `S`:
  item 1 (`sum_r_sq_le`), item 2 (`sum_A_full_sq_le`, Parseval in the unitary rows),
  the omitted diagonal term and the combination `|a-b|² ≤ 2|a|²+2|b|²`
  (`A_split_bound`), item 4 (`C_cauchy_le`, `sum_C_sq_le`) and item 6 (`F_le`, `sum_F_sq_le`).

The exact Schur-feedback expansion (V2) itself is taken from the note (it is derived in the
companion TRACE-075 calculation); items 3 and 5 are not formalized separately, and enter the
combination step as hypotheses.
-/

open Finset Matrix

namespace Bgs.Mathlib

/-! ## Scalar layer -/

/-- `|q| ≤ 2` for `q = w/(1 - s w)`, `|w| = 1`, `|s|² ≤ 1/4`. -/
theorem feedback_coeff_norm_le {s w : ℂ} (hs : ‖s‖ ^ 2 ≤ 1 / 4) (hw : ‖w‖ = 1) :
    ‖w / (1 - s * w)‖ ≤ 2 := by
  have hs' : ‖s‖ ≤ 1 / 2 := by nlinarith [norm_nonneg s]
  have h1 : 1 / 2 ≤ ‖1 - s * w‖ := by
    have := norm_sub_norm_le (1 : ℂ) (s * w)
    rw [norm_one, norm_mul, hw, mul_one] at this
    linarith
  rw [norm_div, hw, div_le_iff₀ (by linarith)]
  linarith

/-- The real increment (V2):
`Δ = -r + 2 Re(qA) + |q|² B + 2 Re(q² C) + 2 Re(q |q|² D) + |q|⁴ F`. -/
noncomputable def incrementV2 (q A C D : ℂ) (r B F : ℝ) : ℝ :=
  -r + 2 * (q * A).re + ‖q‖ ^ 2 * B + 2 * (q ^ 2 * C).re + 2 * (q * (‖q‖ ^ 2 : ℝ) * D).re
    + ‖q‖ ^ 4 * F

theorem two_re_le (z : ℂ) : |2 * z.re| ≤ 2 * ‖z‖ := by
  rw [abs_mul, abs_two]; exact mul_le_mul_of_nonneg_left (Complex.abs_re_le_norm z) (by norm_num)

/-- Pointwise bound from (V2) with `|q| ≤ 2`. -/
theorem increment_pointwise_le {q A C D : ℂ} {r B F : ℝ} (hq : ‖q‖ ≤ 2) (hr : 0 ≤ r)
    (hF : 0 ≤ F) :
    |incrementV2 q A C D r B F| ≤ r + 4 * ‖A‖ + 4 * |B| + 8 * ‖C‖ + 16 * ‖D‖ + 16 * F := by
  have hq0 := norm_nonneg q
  have hA : |2 * (q * A).re| ≤ 4 * ‖A‖ := by
    refine (two_re_le _).trans ?_
    rw [norm_mul]; nlinarith [norm_nonneg A]
  have hC : |2 * (q ^ 2 * C).re| ≤ 8 * ‖C‖ := by
    refine (two_re_le _).trans ?_
    rw [norm_mul, norm_pow]
    have : ‖q‖ ^ 2 ≤ 4 := by nlinarith
    nlinarith [norm_nonneg C]
  have hD : |2 * (q * (‖q‖ ^ 2 : ℝ) * D).re| ≤ 16 * ‖D‖ := by
    refine (two_re_le _).trans ?_
    rw [norm_mul, norm_mul, Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg (by positivity)]
    have : ‖q‖ * ‖q‖ ^ 2 ≤ 8 := by
      have : ‖q‖ ^ 2 ≤ 4 := by nlinarith
      nlinarith
    nlinarith [norm_nonneg D]
  have hB : |‖q‖ ^ 2 * B| ≤ 4 * |B| := by
    rw [abs_mul, abs_of_nonneg (by positivity)]
    have : ‖q‖ ^ 2 ≤ 4 := by nlinarith
    nlinarith [abs_nonneg B]
  have hFF : |‖q‖ ^ 4 * F| ≤ 16 * F := by
    rw [abs_mul, abs_of_nonneg (by positivity), abs_of_nonneg hF]
    have : ‖q‖ ^ 4 ≤ 16 := by
      have : ‖q‖ ^ 2 ≤ 4 := by nlinarith
      nlinarith
    nlinarith
  unfold incrementV2
  have hr' : |-r| = r := by rw [abs_neg, abs_of_nonneg hr]
  calc _ ≤ |-r| + |2 * (q * A).re| + |‖q‖ ^ 2 * B| + |2 * (q ^ 2 * C).re|
        + |2 * (q * (‖q‖ ^ 2 : ℝ) * D).re| + |‖q‖ ^ 4 * F| := by
        refine (abs_add_le _ _).trans ?_
        gcongr
        refine (abs_add_le _ _).trans ?_
        gcongr
        refine (abs_add_le _ _).trans ?_
        gcongr
        refine (abs_add_le _ _).trans ?_
        gcongr
        exact abs_add_le _ _
    _ ≤ _ := by linarith

/-- Cauchy for six terms: `(a+b+c+d+e+f)² ≤ 6(a²+b²+c²+d²+e²+f²)`. -/
theorem six_sq_le (a b c d e f : ℝ) :
    (a + b + c + d + e + f) ^ 2 ≤ 6 * (a ^ 2 + b ^ 2 + c ^ 2 + d ^ 2 + e ^ 2 + f ^ 2) := by
  nlinarith [sq_nonneg (a - b), sq_nonneg (a - c), sq_nonneg (a - d), sq_nonneg (a - e),
    sq_nonneg (a - f), sq_nonneg (b - c), sq_nonneg (b - d), sq_nonneg (b - e), sq_nonneg (b - f),
    sq_nonneg (c - d), sq_nonneg (c - e), sq_nonneg (c - f), sq_nonneg (d - e), sq_nonneg (d - f),
    sq_nonneg (e - f)]

/-- **Combination.** If `|q_e| ≤ 2`, `r_e, F_e ≥ 0`, `0 ≤ δ ≤ 1/4` and the six squared sums obey
the bounds of items 1–6 of the note, then `∑_e Δ_e² ≤ 2598 δ² (K + P₃)`. -/
theorem increment_second_moment_le {ι : Type*} (E : Finset ι) (q A C D : ι → ℂ)
    (r B F : ι → ℝ) {δ K P3 : ℝ} (hδ0 : 0 ≤ δ) (hδ : δ ≤ 1 / 4) (hK : 0 ≤ K) (hP3 : 0 ≤ P3)
    (hq : ∀ e ∈ E, ‖q e‖ ≤ 2) (hr : ∀ e ∈ E, 0 ≤ r e) (hF : ∀ e ∈ E, 0 ≤ F e)
    (h1 : ∑ e ∈ E, r e ^ 2 ≤ δ ^ 2 * K)
    (h2 : ∑ e ∈ E, ‖A e‖ ^ 2 ≤ 10 * δ ^ 2 * K)
    (h3 : ∑ e ∈ E, B e ^ 2 ≤ 6 * δ ^ 2 * P3 + 12 * δ ^ 2 * K)
    (h4 : ∑ e ∈ E, ‖C e‖ ^ 2 ≤ δ ^ 2 * K)
    (h5 : ∑ e ∈ E, ‖D e‖ ^ 2 ≤ 4 * δ ^ 3 * P3)
    (h6 : ∑ e ∈ E, F e ^ 2 ≤ δ ^ 4 * K) :
    ∑ e ∈ E, incrementV2 (q e) (A e) (C e) (D e) (r e) (B e) (F e) ^ 2
      ≤ 2598 * δ ^ 2 * (K + P3) := by
  have hpt : ∀ e ∈ E, incrementV2 (q e) (A e) (C e) (D e) (r e) (B e) (F e) ^ 2 ≤
      6 * (r e ^ 2 + 16 * ‖A e‖ ^ 2 + 16 * B e ^ 2 + 64 * ‖C e‖ ^ 2 + 256 * ‖D e‖ ^ 2
        + 256 * F e ^ 2) := by
    intro e he
    have hb := increment_pointwise_le (A := A e) (C := C e) (D := D e) (B := B e) (hq e he)
      (hr e he) (hF e he)
    have hsq : incrementV2 (q e) (A e) (C e) (D e) (r e) (B e) (F e) ^ 2 ≤
        (r e + 4 * ‖A e‖ + 4 * |B e| + 8 * ‖C e‖ + 16 * ‖D e‖ + 16 * F e) ^ 2 := by
      rw [← sq_abs]
      exact pow_le_pow_left₀ (abs_nonneg _) hb 2
    refine hsq.trans ((six_sq_le _ _ _ _ _ _).trans (le_of_eq ?_))
    simp only [mul_pow, sq_abs]; ring
  refine (sum_le_sum hpt).trans ?_
  rw [← mul_sum]
  simp only [sum_add_distrib, ← mul_sum]
  have hδ2 : δ ^ 2 ≤ 1 / 16 := by nlinarith
  have e1 : 256 * δ ^ 4 * K ≤ 16 * δ ^ 2 * K := by
    have : δ ^ 4 = δ ^ 2 * δ ^ 2 := by ring
    rw [this]; nlinarith [mul_nonneg (sq_nonneg δ) hK]
  have e2 : 1024 * δ ^ 3 * P3 ≤ 256 * δ ^ 2 * P3 := by
    have : δ ^ 3 = δ ^ 2 * δ := by ring
    rw [this]; nlinarith [mul_nonneg (sq_nonneg δ) hP3]
  nlinarith [mul_nonneg (sq_nonneg δ) hK, mul_nonneg (sq_nonneg δ) hP3]

/-! ## Coordinate squared sums for a unitary `S` -/

section Coordinates

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- Intensities `P_kl = |S_kl|²`. -/
noncomputable def intensity (S : Matrix n n ℂ) (k l : n) : ℝ := ‖S k l‖ ^ 2

/-- `K_ij = (P²)_ij`. -/
noncomputable def intensitySq (S : Matrix n n ℂ) (i j : n) : ℝ :=
  ∑ k, intensity S i k * intensity S k j

omit [Fintype n] [DecidableEq n] in
theorem intensity_nonneg (S : Matrix n n ℂ) (k l : n) : 0 ≤ intensity S k l := by
  unfold intensity; positivity

theorem row_sum_intensity {S : Matrix n n ℂ} (h : S * Sᴴ = 1) (k : n) :
    ∑ l, intensity S k l = 1 := by
  have := congrFun (congrFun h k) k
  simp [Matrix.mul_apply, Complex.mul_conj'] at this
  exact_mod_cast this

theorem col_sum_intensity {S : Matrix n n ℂ} (h : Sᴴ * S = 1) (l : n) :
    ∑ k, intensity S k l = 1 := by
  have := congrFun (congrFun h l) l
  simp [Matrix.mul_apply, Complex.conj_mul'] at this
  exact_mod_cast this

/-- Parseval in the unitary rows: `∑_e |∑_k S_ek v_k|² = ∑_k |v_k|²`. -/
theorem parseval_unitary {S : Matrix n n ℂ} (h : Sᴴ * S = 1) (v : n → ℂ) :
    ∑ e, ‖∑ k, S e k * v k‖ ^ 2 = ∑ k, ‖v k‖ ^ 2 := by
  have key : star (S *ᵥ v) ⬝ᵥ (S *ᵥ v) = star v ⬝ᵥ v := by
    rw [star_mulVec, dotProduct_mulVec, vecMul_vecMul, h, vecMul_one]
  have e1 : ∀ x : n → ℂ, star x ⬝ᵥ x = ((∑ k, ‖x k‖ ^ 2 : ℝ) : ℂ) := by
    intro x; simp [dotProduct, Complex.conj_mul']
  rw [e1, e1] at key
  have := Complex.ofReal_injective key
  simpa [mulVec, dotProduct] using this

theorem K_le_delta {S : Matrix n n ℂ} (h : S * Sᴴ = 1) {δ : ℝ}
    (hδ : ∀ k l, intensity S k l ≤ δ) (i j : n) : intensitySq S i j ≤ δ := by
  unfold intensitySq
  calc ∑ k, intensity S i k * intensity S k j ≤ ∑ k, intensity S i k * δ :=
        sum_le_sum fun k _ => mul_le_mul_of_nonneg_left (hδ k j) (intensity_nonneg S i k)
    _ = δ := by rw [← sum_mul, row_sum_intensity h, one_mul]

omit [DecidableEq n] in
/-- **Item 1**: `∑_e r_e² ≤ δ² K_ij`, `r_e = P_ie P_ej`. -/
theorem sum_r_sq_le (S : Matrix n n ℂ) {δ : ℝ} (hδ : ∀ k l, intensity S k l ≤ δ) (i j : n) :
    ∑ e, (intensity S i e * intensity S e j) ^ 2 ≤ δ ^ 2 * intensitySq S i j := by
  unfold intensitySq
  rw [mul_sum]
  refine sum_le_sum fun e _ => ?_
  have a := intensity_nonneg S i e
  have b := intensity_nonneg S e j
  have := hδ i e
  have := hδ e j
  have : (intensity S i e * intensity S e j) ^ 2 =
      (intensity S i e * intensity S e j) * (intensity S i e * intensity S e j) := by ring
  rw [this]
  have hp : intensity S i e * intensity S e j ≤ δ * δ := mul_le_mul (by assumption)
    (by assumption) b (by linarith)
  nlinarith [mul_nonneg a b]

/-- **Item 2** (full coordinate sum, first component): by Parseval in the unitary rows,
`∑_e |S_ie ∑_k P_kj S_ek conj(S_ik)|² ≤ δ² K_ij`. -/
theorem sum_A_full_sq_le {S : Matrix n n ℂ} (h : Sᴴ * S = 1) {δ : ℝ}
    (hδ : ∀ k l, intensity S k l ≤ δ) (i j : n) :
    ∑ e, ‖S i e * ∑ k, (intensity S k j : ℂ) * S e k * star (S i k)‖ ^ 2
      ≤ δ ^ 2 * intensitySq S i j := by
  have hδ0 : 0 ≤ δ := (intensity_nonneg S i i).trans (hδ i i)
  set v : n → ℂ := fun k => (intensity S k j : ℂ) * star (S i k) with hv
  have hpar := parseval_unitary h v
  have step1 : ∀ e, ‖S i e * ∑ k, (intensity S k j : ℂ) * S e k * star (S i k)‖ ^ 2
      ≤ δ * ‖∑ k, S e k * v k‖ ^ 2 := by
    intro e
    rw [norm_mul, mul_pow]
    have : ∑ k, (intensity S k j : ℂ) * S e k * star (S i k) = ∑ k, S e k * v k := by
      refine sum_congr rfl fun k _ => ?_; simp only [hv]; ring
    rw [this]
    exact mul_le_mul_of_nonneg_right (hδ i e) (by positivity)
  refine (sum_le_sum fun e _ => step1 e).trans ?_
  rw [← mul_sum, hpar]
  have step2 : ∑ k, ‖v k‖ ^ 2 ≤ δ * intensitySq S i j := by
    unfold intensitySq
    rw [mul_sum]
    refine sum_le_sum fun k _ => ?_
    simp only [hv, norm_mul, Complex.norm_real, Real.norm_eq_abs, norm_star,
      abs_of_nonneg (intensity_nonneg S k j), mul_pow]
    have h1 : ‖S i k‖ ^ 2 = intensity S i k := rfl
    rw [h1]
    have a := intensity_nonneg S i k
    have b := intensity_nonneg S k j
    have := hδ k j
    nlinarith [mul_nonneg a b]
  calc δ * ∑ k, ‖v k‖ ^ 2 ≤ δ * (δ * intensitySq S i j) := mul_le_mul_of_nonneg_left step2 hδ0
    _ = δ ^ 2 * intensitySq S i j := by ring

/-- **Item 2**, omitted diagonal term and combination: if the full sums satisfy
`∑‖A_full‖² ≤ 4δ²K` and the omitted diagonal term has squared sum `≤ 4δ³K`, then `∑|A_e|² ≤ (8 + 8δ) δ² K ≤ 10 δ² K` for `δ ≤ 1/4`. -/
theorem A_split_bound {ι : Type*} (E : Finset ι) (Afull Aom : ι → ℂ) {δ K : ℝ}
    (hδ : δ ≤ 1 / 4) (hK : 0 ≤ K)
    (hfull : ∑ e ∈ E, ‖Afull e‖ ^ 2 ≤ 4 * δ ^ 2 * K)
    (hom : ∑ e ∈ E, ‖Aom e‖ ^ 2 ≤ 4 * δ ^ 3 * K) :
    ∑ e ∈ E, ‖Afull e - Aom e‖ ^ 2 ≤ 10 * δ ^ 2 * K := by
  have hpt : ∀ e ∈ E, ‖Afull e - Aom e‖ ^ 2 ≤ 2 * ‖Afull e‖ ^ 2 + 2 * ‖Aom e‖ ^ 2 := by
    intro e _
    have := norm_sub_le (Afull e) (Aom e)
    nlinarith [norm_nonneg (Afull e - Aom e), norm_nonneg (Afull e), norm_nonneg (Aom e),
      sq_nonneg (‖Afull e‖ - ‖Aom e‖)]
  refine (sum_le_sum hpt).trans ?_
  rw [sum_add_distrib, ← mul_sum, ← mul_sum]
  have : δ ^ 3 = δ ^ 2 * δ := by ring
  have h3 : 8 * δ ^ 3 * K ≤ 2 * δ ^ 2 * K := by
    rw [this]; nlinarith [mul_nonneg (sq_nonneg δ) hK]
  nlinarith

/-- Cauchy–Schwarz for finite complex sums: `|∑ a_k b_k|² ≤ (∑|a_k|²)(∑|b_k|²)`. -/
theorem norm_sum_mul_sq_le {ι : Type*} (T : Finset ι) (a b : ι → ℂ) :
    ‖∑ k ∈ T, a k * b k‖ ^ 2 ≤ (∑ k ∈ T, ‖a k‖ ^ 2) * (∑ k ∈ T, ‖b k‖ ^ 2) := by
  have h1 : ‖∑ k ∈ T, a k * b k‖ ≤ ∑ k ∈ T, ‖a k‖ * ‖b k‖ :=
    (norm_sum_le _ _).trans (le_of_eq (sum_congr rfl fun k _ => norm_mul _ _))
  have cs : (∑ k ∈ T, ‖a k‖ * ‖b k‖) ^ 2 ≤ (∑ k ∈ T, ‖a k‖ ^ 2) * (∑ k ∈ T, ‖b k‖ ^ 2) :=
    sum_mul_sq_le_sq_mul_sq T _ _
  calc ‖∑ k ∈ T, a k * b k‖ ^ 2 ≤ (∑ k ∈ T, ‖a k‖ * ‖b k‖) ^ 2 :=
        pow_le_pow_left₀ (norm_nonneg _) h1 2
    _ ≤ _ := cs

/-- `C_e = ∑_{k ∈ T} α_k β_k` with `α_k = S_ie S_ek conj(S_ik)`, `β_k = S_ke S_ej conj(S_kj)`. -/
noncomputable def coeffC (S : Matrix n n ℂ) (T : Finset n) (i j e : n) : ℂ :=
  ∑ k ∈ T, (S i e * S e k * star (S i k)) * (S k e * S e j * star (S k j))

/-- **Item 4**, Cauchy step: `|C_e|² ≤ r_e δ K_ij` for any index set `T`. -/
theorem C_cauchy_le {S : Matrix n n ℂ} (h : S * Sᴴ = 1) {δ : ℝ}
    (hδ : ∀ k l, intensity S k l ≤ δ) (T : Finset n) (i j e : n) :
    ‖coeffC S T i j e‖ ^ 2 ≤ intensity S i e * intensity S e j * δ * intensitySq S i j := by
  have hfac : coeffC S T i j e =
      (S i e * S e j) * ∑ k ∈ T, (S e k * S k e) * (star (S i k) * star (S k j)) := by
    unfold coeffC; rw [mul_sum]; refine sum_congr rfl fun k _ => ?_; ring
  rw [hfac, norm_mul, mul_pow]
  have cs := norm_sum_mul_sq_le T (fun k => S e k * S k e) (fun k => star (S i k) * star (S k j))
  have ha : ∑ k ∈ T, ‖S e k * S k e‖ ^ 2 ≤ δ := by
    calc ∑ k ∈ T, ‖S e k * S k e‖ ^ 2 = ∑ k ∈ T, intensity S e k * intensity S k e := by
          refine sum_congr rfl fun k _ => ?_; rw [norm_mul, mul_pow]; rfl
      _ ≤ ∑ k, intensity S e k * intensity S k e :=
          sum_le_sum_of_subset_of_nonneg (subset_univ T) fun k _ _ =>
            mul_nonneg (intensity_nonneg S e k) (intensity_nonneg S k e)
      _ ≤ ∑ k, intensity S e k * δ :=
          sum_le_sum fun k _ => mul_le_mul_of_nonneg_left (hδ k e) (intensity_nonneg S e k)
      _ = δ := by rw [← sum_mul, row_sum_intensity h, one_mul]
  have hb : ∑ k ∈ T, ‖star (S i k) * star (S k j)‖ ^ 2 ≤ intensitySq S i j := by
    calc ∑ k ∈ T, ‖star (S i k) * star (S k j)‖ ^ 2
          = ∑ k ∈ T, intensity S i k * intensity S k j := by
          refine sum_congr rfl fun k _ => ?_; rw [norm_mul, norm_star, norm_star, mul_pow]; rfl
      _ ≤ intensitySq S i j :=
          sum_le_sum_of_subset_of_nonneg (subset_univ T) fun k _ _ =>
            mul_nonneg (intensity_nonneg S i k) (intensity_nonneg S k j)
  have hie : ‖S i e * S e j‖ ^ 2 = intensity S i e * intensity S e j := by
    rw [norm_mul, mul_pow]; rfl
  rw [hie]
  have hr0 : 0 ≤ intensity S i e * intensity S e j :=
    mul_nonneg (intensity_nonneg S i e) (intensity_nonneg S e j)
  have hb0 : 0 ≤ ∑ k ∈ T, ‖star (S i k) * star (S k j)‖ ^ 2 := by positivity
  have hδ0 : 0 ≤ δ := (intensity_nonneg S i i).trans (hδ i i)
  calc intensity S i e * intensity S e j * ‖∑ k ∈ T, S e k * S k e * (star (S i k) * star (S k j))‖ ^ 2
        ≤ intensity S i e * intensity S e j *
          ((∑ k ∈ T, ‖S e k * S k e‖ ^ 2) * (∑ k ∈ T, ‖star (S i k) * star (S k j)‖ ^ 2)) :=
        mul_le_mul_of_nonneg_left cs hr0
    _ ≤ intensity S i e * intensity S e j * (δ * intensitySq S i j) := by
        apply mul_le_mul_of_nonneg_left _ hr0
        exact mul_le_mul ha hb hb0 hδ0
    _ = _ := by ring

/-- **Item 4**: `∑_e |C_e|² ≤ δ K_ij² ≤ δ² K_ij` (with `T_e = {k ≠ e}` or any other index sets). -/
theorem sum_C_sq_le {S : Matrix n n ℂ} (h : S * Sᴴ = 1) {δ : ℝ}
    (hδ : ∀ k l, intensity S k l ≤ δ) (T : n → Finset n) (i j : n) :
    ∑ e, ‖coeffC S (T e) i j e‖ ^ 2 ≤ δ ^ 2 * intensitySq S i j := by
  have hδ0 : 0 ≤ δ := (intensity_nonneg S i i).trans (hδ i i)
  have hK0 : 0 ≤ intensitySq S i j :=
    sum_nonneg fun k _ => mul_nonneg (intensity_nonneg S i k) (intensity_nonneg S k j)
  refine (sum_le_sum fun e _ => C_cauchy_le h hδ (T e) i j e).trans ?_
  rw [← sum_mul, ← sum_mul]
  have hKd := K_le_delta h hδ i j
  have : ∑ e, intensity S i e * intensity S e j = intensitySq S i j := rfl
  rw [this]
  nlinarith [mul_nonneg hK0 hδ0]

/-- **Item 6**: `F_e = r_e ∑_{k ∈ T} P_ek P_ke ≤ δ r_e`. -/
theorem F_le {S : Matrix n n ℂ} (h : S * Sᴴ = 1) {δ : ℝ}
    (hδ : ∀ k l, intensity S k l ≤ δ) (T : Finset n) (i j e : n) :
    intensity S i e * intensity S e j * ∑ k ∈ T, intensity S e k * intensity S k e
      ≤ δ * (intensity S i e * intensity S e j) := by
  have hr0 : 0 ≤ intensity S i e * intensity S e j :=
    mul_nonneg (intensity_nonneg S i e) (intensity_nonneg S e j)
  have : ∑ k ∈ T, intensity S e k * intensity S k e ≤ δ :=
    calc ∑ k ∈ T, intensity S e k * intensity S k e ≤ ∑ k, intensity S e k * intensity S k e :=
          sum_le_sum_of_subset_of_nonneg (subset_univ T) fun k _ _ =>
            mul_nonneg (intensity_nonneg S e k) (intensity_nonneg S k e)
      _ ≤ ∑ k, intensity S e k * δ :=
          sum_le_sum fun k _ => mul_le_mul_of_nonneg_left (hδ k e) (intensity_nonneg S e k)
      _ = δ := by rw [← sum_mul, row_sum_intensity h, one_mul]
  nlinarith

/-- **Item 6**: `∑_e F_e² ≤ δ⁴ K_ij`. -/
theorem sum_F_sq_le {S : Matrix n n ℂ} (h : S * Sᴴ = 1) {δ : ℝ}
    (hδ : ∀ k l, intensity S k l ≤ δ) (T : n → Finset n) (i j : n) :
    ∑ e, (intensity S i e * intensity S e j * ∑ k ∈ T e, intensity S e k * intensity S k e) ^ 2
      ≤ δ ^ 4 * intensitySq S i j := by
  have hδ0 : 0 ≤ δ := (intensity_nonneg S i i).trans (hδ i i)
  have hpt : ∀ e ∈ (univ : Finset n),
      (intensity S i e * intensity S e j * ∑ k ∈ T e, intensity S e k * intensity S k e) ^ 2
        ≤ δ ^ 2 * (intensity S i e * intensity S e j) ^ 2 := by
    intro e _
    have h0 : 0 ≤ intensity S i e * intensity S e j * ∑ k ∈ T e, intensity S e k * intensity S k e :=
      mul_nonneg (mul_nonneg (intensity_nonneg S i e) (intensity_nonneg S e j))
        (sum_nonneg fun k _ => mul_nonneg (intensity_nonneg S e k) (intensity_nonneg S k e))
    have := F_le h hδ (T e) i j e
    rw [show δ ^ 2 * (intensity S i e * intensity S e j) ^ 2 =
      (δ * (intensity S i e * intensity S e j)) ^ 2 by ring]
    exact pow_le_pow_left₀ h0 this 2
  refine (sum_le_sum hpt).trans ?_
  rw [← mul_sum]
  have := sum_r_sq_le S hδ i j
  calc δ ^ 2 * ∑ e, (intensity S i e * intensity S e j) ^ 2 ≤ δ ^ 2 * (δ ^ 2 * intensitySq S i j) :=
        mul_le_mul_of_nonneg_left this (by positivity)
    _ = δ ^ 4 * intensitySq S i j := by ring

end Coordinates

#print axioms feedback_coeff_norm_le
#print axioms two_re_le
#print axioms increment_pointwise_le
#print axioms six_sq_le
#print axioms increment_second_moment_le
#print axioms intensity_nonneg
#print axioms row_sum_intensity
#print axioms col_sum_intensity
#print axioms parseval_unitary
#print axioms K_le_delta
#print axioms sum_r_sq_le
#print axioms sum_A_full_sq_le
#print axioms A_split_bound
#print axioms norm_sum_mul_sq_le
#print axioms C_cauchy_le
#print axioms sum_C_sq_le
#print axioms F_le
#print axioms sum_F_sq_le
end Bgs.Mathlib
