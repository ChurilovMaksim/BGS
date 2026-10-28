module
public import Mathlib
@[expose] public section

/-!
# Uniform two-state discrimination through pure loss: the scalar layer

Source: `mathematics/information-theory/pure_loss_discrimination.md`.

For `0 < u ≤ 1/16`, `0 < η ≤ 1`, `n ≥ 1` put `z = (1-η)^n`, `e = η^n`, `q = u e`,
`a = 1 - u + u z`, `b = u e`, `c² = u(1-u)e`, `s = a + b`, `r² = (a-b)² + 4c²`,
`d = ab - c²`, `h = 1 - z - e`, `δ = 1 - γ = 4c²/r²` and `L = -log(1 - δ)`.

Formalized here (every scalar step of the proof):

* `pl_d_eq`: `d = u² (η(1-η))^n`;  `pl_h_mem`: `0 ≤ h ≤ 1`;  `pl_s_bounds`: `1 - u ≤ s ≤ 1`;
  `pl_amb_ge`: `a - b ≥ 1 - 2u`;  `pl_r2_ge`: `r² ≥ (1-2u)²`.
* **Correction.** `pl_r2_eq`: `r² = 1 - 2uh + u²((1-z+e)² - 4e)`.  The source displays
  `r² = 1 - 2uh + u²(1-z+e)²`, which omits the term `-4u²e` (e.g. `u = 1/16`, `η = 1/2`,
  `n = 1` gives `r² = 1020/1024`, not `1028/1024`).  The downstream bounds are unaffected:
  they are proved below from the correct identity.
* `pl_delta_eq` (`1 - (a-b)²/r² = 4q(1-u)/r²`), `pl_delta_bounds` (`δ ≤ 5q` and
  `|δ - 4q| ≤ 16 u q`).
* `neg_log_one_sub_bounds`: `δ ≤ -log(1-δ) ≤ δ + δ²/(2(1-δ))` for `0 ≤ δ < 1`
  (via `sinh t ≥ t`), giving `pl_L_bounds` (`|L - 4q| ≤ 35 u q` and `L ≤ 8q`).
* `sqrt_one_sub_exp_lipschitz`: `|√(1-e^{-x}) - √(1-e^{-y})| ≤ √|x-y|` for `x, y ≥ 0`.
* Error budget with `t = B u η^n`: `pl_replacement_error` (`2B·2d/s < 5ut`),
  `pl_mean_shift` (`|B s L - 4t| ≤ 39 u t`), `pl_fluctuation` (`L √(B s (1-s)) ≤ 8 u √t`).

The trace-distance replacement identity and the binomial/Jensen step are not formalized.
-/

open Real

namespace Bgs.Mathlib

section PureLoss

variable {u η : ℝ} {n : ℕ}

/-- `z + e ≤ 1`: `(1-η)^n + η^n ≤ 1` for `0 ≤ η ≤ 1`, `n ≥ 1`. -/
lemma pow_add_pow_le_one (hη0 : 0 ≤ η) (hη1 : η ≤ 1) (hn : 1 ≤ n) :
    (1 - η) ^ n + η ^ n ≤ 1 := by
  have h1 : (1 - η) ^ n ≤ 1 - η := pow_le_of_le_one (by linarith) (by linarith) (by omega)
  have h2 : η ^ n ≤ η := pow_le_of_le_one hη0 hη1 (by omega)
  linarith

/-- `d = ab - c² = u² (η(1-η))^n`. -/
theorem pl_d_eq (u η : ℝ) (n : ℕ) :
    (1 - u + u * (1 - η) ^ n) * (u * η ^ n) - u * (1 - u) * η ^ n =
      u ^ 2 * (η * (1 - η)) ^ n := by
  rw [mul_pow]; ring

theorem pl_h_mem (hη0 : 0 ≤ η) (hη1 : η ≤ 1) (hn : 1 ≤ n) :
    0 ≤ 1 - (1 - η) ^ n - η ^ n ∧ 1 - (1 - η) ^ n - η ^ n ≤ 1 := by
  have := pow_add_pow_le_one hη0 hη1 hn
  have h1 : 0 ≤ (1 - η) ^ n := pow_nonneg (by linarith) n
  have h2 : 0 ≤ η ^ n := pow_nonneg hη0 n
  constructor <;> linarith

/-- `s = 1 - u h ∈ [1 - u, 1]`. -/
theorem pl_s_bounds (hu : 0 ≤ u) (hη0 : 0 ≤ η) (hη1 : η ≤ 1) (hn : 1 ≤ n) :
    1 - u ≤ (1 - u + u * (1 - η) ^ n) + u * η ^ n ∧
      (1 - u + u * (1 - η) ^ n) + u * η ^ n ≤ 1 := by
  have := pow_add_pow_le_one hη0 hη1 hn
  have h1 : 0 ≤ (1 - η) ^ n := pow_nonneg (by linarith) n
  have h2 : 0 ≤ η ^ n := pow_nonneg hη0 n
  constructor <;> nlinarith

/-- `a - b ≥ 1 - 2u`. -/
theorem pl_amb_ge (hu : 0 ≤ u) (hη0 : 0 ≤ η) (hη1 : η ≤ 1) :
    1 - 2 * u ≤ (1 - u + u * (1 - η) ^ n) - u * η ^ n := by
  have h1 : 0 ≤ (1 - η) ^ n := pow_nonneg (by linarith) n
  have h2 : η ^ n ≤ 1 := pow_le_one₀ hη0 hη1
  nlinarith

/-- **Corrected identity** `r² = 1 - 2uh + u²((1-z+e)² - 4e)`. -/
theorem pl_r2_eq (u η : ℝ) (n : ℕ) :
    ((1 - u + u * (1 - η) ^ n) - u * η ^ n) ^ 2 + 4 * (u * (1 - u) * η ^ n) =
      1 - 2 * u * (1 - (1 - η) ^ n - η ^ n) +
        u ^ 2 * ((1 - (1 - η) ^ n + η ^ n) ^ 2 - 4 * η ^ n) := by
  ring

/-- The identity displayed in the source, `r² = 1 - 2uh + u²(1-z+e)²`, is false in general. -/
theorem pl_r2_source_formula_false :
    ¬ ∀ (u η : ℝ) (n : ℕ), 0 < u → u ≤ 1 / 16 → 0 < η → η ≤ 1 → 1 ≤ n →
      ((1 - u + u * (1 - η) ^ n) - u * η ^ n) ^ 2 + 4 * (u * (1 - u) * η ^ n) =
        1 - 2 * u * (1 - (1 - η) ^ n - η ^ n) + u ^ 2 * (1 - (1 - η) ^ n + η ^ n) ^ 2 := by
  intro h
  have := h (1 / 16) (1 / 2) 1 (by norm_num) (by norm_num) (by norm_num) (by norm_num) le_rfl
  norm_num at this

/-- `r² ≥ (1 - 2u)²` (for `u ≤ 1/2`). -/
theorem pl_r2_ge (hu : 0 ≤ u) (hu2 : u ≤ 1 / 2) (hη0 : 0 ≤ η) (hη1 : η ≤ 1) :
    (1 - 2 * u) ^ 2 ≤
      ((1 - u + u * (1 - η) ^ n) - u * η ^ n) ^ 2 + 4 * (u * (1 - u) * η ^ n) := by
  have h := pl_amb_ge (n := n) hu hη0 hη1
  have h2 : 0 ≤ η ^ n := pow_nonneg hη0 n
  have h3 : 0 ≤ 4 * (u * (1 - u) * η ^ n) := by
    have : 0 ≤ 1 - u := by linarith
    positivity
  have h4 : 0 ≤ 1 - 2 * u := by linarith
  nlinarith

/-- `δ = 1 - (a-b)²/r² = 4q(1-u)/r²`, `q = u η^n`. -/
theorem pl_delta_eq {r2 : ℝ}
    (hr2 : r2 = ((1 - u + u * (1 - η) ^ n) - u * η ^ n) ^ 2 + 4 * (u * (1 - u) * η ^ n))
    (hr2pos : 0 < r2) :
    1 - ((1 - u + u * (1 - η) ^ n) - u * η ^ n) ^ 2 / r2 = 4 * (u * η ^ n) * (1 - u) / r2 := by
  field_simp
  rw [hr2]; ring

/-- Auxiliary: `|r² - (1 - u)| ≤ u + 4u²`. -/
lemma pl_r2_near (hu : 0 ≤ u) (hη0 : 0 ≤ η) (hη1 : η ≤ 1) (hn : 1 ≤ n) :
    |((1 - u + u * (1 - η) ^ n) - u * η ^ n) ^ 2 + 4 * (u * (1 - u) * η ^ n) - (1 - u)| ≤
      u + 4 * u ^ 2 := by
  rw [pl_r2_eq]
  obtain ⟨hh0, hh1⟩ := pl_h_mem hη0 hη1 hn
  have hz0 : 0 ≤ (1 - η) ^ n := pow_nonneg (by linarith) n
  have he0 : 0 ≤ η ^ n := pow_nonneg hη0 n
  have hze := pow_add_pow_le_one hη0 hη1 hn
  set z := (1 - η) ^ n
  set e := η ^ n
  have hw1 : (1 - z + e) ^ 2 ≤ 4 := by nlinarith
  rw [abs_le]
  constructor <;> nlinarith [sq_nonneg u]

/-- `δ ≤ 5q` and `|δ - 4q| ≤ 16 u q`. -/
theorem pl_delta_bounds (hu : 0 < u) (hu16 : u ≤ 1 / 16) (hη0 : 0 ≤ η) (hη1 : η ≤ 1)
    (hn : 1 ≤ n) {r2 : ℝ}
    (hr2 : r2 = ((1 - u + u * (1 - η) ^ n) - u * η ^ n) ^ 2 + 4 * (u * (1 - u) * η ^ n)) :
    4 * (u * η ^ n) * (1 - u) / r2 ≤ 5 * (u * η ^ n) ∧
      |4 * (u * η ^ n) * (1 - u) / r2 - 4 * (u * η ^ n)| ≤ 16 * u * (u * η ^ n) := by
  have hge := pl_r2_ge (n := n) hu.le (by linarith) hη0 hη1
  rw [← hr2] at hge
  have hnear := pl_r2_near hu.le hη0 hη1 hn
  rw [← hr2] at hnear
  have hr2pos : 0 < r2 := lt_of_lt_of_le (by nlinarith) hge
  have hq : 0 ≤ u * η ^ n := mul_nonneg hu.le (pow_nonneg hη0 n)
  have hr2lo : (7 / 8) ^ 2 ≤ r2 := le_trans (by nlinarith) hge
  constructor
  · rw [div_le_iff₀ hr2pos]
    nlinarith
  · have : 4 * (u * η ^ n) * (1 - u) / r2 - 4 * (u * η ^ n) =
        4 * (u * η ^ n) * ((1 - u) - r2) / r2 := by field_simp
    rw [this, abs_div, abs_mul, abs_of_pos hr2pos, abs_of_nonneg (by positivity : 0 ≤ 4 * (u * η ^ n)),
      div_le_iff₀ hr2pos]
    rw [abs_sub_comm] at hnear
    have h1 : 4 * (u * η ^ n) * |1 - u - r2| ≤ 4 * (u * η ^ n) * (u + 4 * u ^ 2) :=
      mul_le_mul_of_nonneg_left hnear (by positivity)
    nlinarith [mul_nonneg (mul_nonneg hq hu.le) (show 0 ≤ 4 * r2 - 1 - 4 * u by nlinarith)]

/-- `δ ≤ -log(1 - δ) ≤ δ + δ²/(2(1-δ))` for `0 ≤ δ < 1` (from `sinh t ≥ t`). -/
theorem neg_log_one_sub_bounds {δ : ℝ} (h0 : 0 ≤ δ) (h1 : δ < 1) :
    δ ≤ -log (1 - δ) ∧ -log (1 - δ) ≤ δ + δ ^ 2 / (2 * (1 - δ)) := by
  have hpos : 0 < 1 - δ := by linarith
  constructor
  · have := Real.log_le_sub_one_of_pos hpos; linarith
  · set t := -log (1 - δ)
    have ht : 0 ≤ t := by
      have : log (1 - δ) ≤ 0 := Real.log_nonpos hpos.le (by linarith)
      simp only [t]; linarith
    have hs := Real.self_le_sinh_iff.mpr ht
    rw [Real.sinh_eq] at hs
    have he1 : Real.exp t = 1 / (1 - δ) := by
      simp only [t]; rw [Real.exp_neg, Real.exp_log hpos, one_div]
    have he2 : Real.exp (-t) = 1 - δ := by
      simp only [t, neg_neg]; rw [Real.exp_log hpos]
    rw [he1, he2] at hs
    have : (1 / (1 - δ) - (1 - δ)) / 2 = δ + δ ^ 2 / (2 * (1 - δ)) := by
      field_simp; ring
    linarith

/-- `|L - 4q| ≤ 35 u q` and `L ≤ 8q`, for `L = -log(1-δ)`, `δ = 4q(1-u)/r²`. -/
theorem pl_L_bounds (hu : 0 < u) (hu16 : u ≤ 1 / 16) (hη0 : 0 ≤ η) (hη1 : η ≤ 1)
    (hn : 1 ≤ n) {r2 : ℝ}
    (hr2 : r2 = ((1 - u + u * (1 - η) ^ n) - u * η ^ n) ^ 2 + 4 * (u * (1 - u) * η ^ n)) :
    |-log (1 - 4 * (u * η ^ n) * (1 - u) / r2) - 4 * (u * η ^ n)| ≤ 35 * u * (u * η ^ n) ∧
      -log (1 - 4 * (u * η ^ n) * (1 - u) / r2) ≤ 8 * (u * η ^ n) := by
  obtain ⟨hd5, hd16⟩ := pl_delta_bounds hu hu16 hη0 hη1 hn hr2
  set q := u * η ^ n
  set δ := 4 * q * (1 - u) / r2
  have hq0 : 0 ≤ q := mul_nonneg hu.le (pow_nonneg hη0 n)
  have hq1 : q ≤ u := by
    have : η ^ n ≤ 1 := pow_le_one₀ hη0 hη1
    simp only [q]; nlinarith
  have hge := pl_r2_ge (n := n) hu.le (by linarith) hη0 hη1
  rw [← hr2] at hge
  have hr2pos : 0 < r2 := lt_of_lt_of_le (by nlinarith) hge
  have hδ0 : 0 ≤ δ := by
    simp only [δ]; apply div_nonneg _ hr2pos.le
    have : 0 ≤ 1 - u := by linarith
    positivity
  have hδ516 : δ ≤ 5 / 16 := by nlinarith
  obtain ⟨hL1, hL2⟩ := neg_log_one_sub_bounds hδ0 (by linarith)
  have hsq : δ ^ 2 / (2 * (1 - δ)) ≤ 25 * q ^ 2 * (8 / 11) := by
    rw [div_le_iff₀ (by linarith)]
    have : δ ^ 2 ≤ 25 * q ^ 2 := by nlinarith
    nlinarith
  have hqq : q ^ 2 ≤ u * q := by nlinarith
  constructor
  · rw [abs_le] at hd16 ⊢
    constructor <;> nlinarith
  · nlinarith [abs_le.mp hd16]

/-- `|√(1-e^{-x}) - √(1-e^{-y})| ≤ √|x - y|` for `x, y ≥ 0`. -/
theorem sqrt_one_sub_exp_lipschitz {x y : ℝ} (hx : 0 ≤ x) (hy : 0 ≤ y) :
    |Real.sqrt (1 - Real.exp (-x)) - Real.sqrt (1 - Real.exp (-y))| ≤ Real.sqrt |x - y| := by
  wlog hxy : y ≤ x generalizing x y
  · rw [abs_sub_comm, abs_sub_comm x y]; exact this hy hx (le_of_not_ge hxy)
  have hA : 0 ≤ 1 - Real.exp (-y) := by
    have : Real.exp (-y) ≤ 1 := Real.exp_le_one_iff.mpr (by linarith)
    linarith
  have hmono : Real.exp (-x) ≤ Real.exp (-y) := Real.exp_le_exp.mpr (by linarith)
  have hle : Real.sqrt (1 - Real.exp (-y)) ≤ Real.sqrt (1 - Real.exp (-x)) :=
    Real.sqrt_le_sqrt (by linarith)
  rw [abs_of_nonneg (by linarith), abs_of_nonneg (by linarith)]
  -- `√A - √B ≤ √(A - B)` for `A ≥ B ≥ 0`
  have key : Real.sqrt (1 - Real.exp (-x)) ≤
      Real.sqrt (1 - Real.exp (-y)) + Real.sqrt (Real.exp (-y) - Real.exp (-x)) := by
    rw [Real.sqrt_le_left (by positivity)]
    have h1 := Real.sq_sqrt hA
    have h2 := Real.sq_sqrt (show 0 ≤ Real.exp (-y) - Real.exp (-x) by linarith)
    nlinarith [Real.sqrt_nonneg (1 - Real.exp (-y)),
      Real.sqrt_nonneg (Real.exp (-y) - Real.exp (-x)),
      mul_nonneg (Real.sqrt_nonneg (1 - Real.exp (-y)))
        (Real.sqrt_nonneg (Real.exp (-y) - Real.exp (-x)))]
  have hdiff : Real.exp (-y) - Real.exp (-x) ≤ x - y := by
    have h1 : Real.exp (-y) - Real.exp (-x) = Real.exp (-y) * (1 - Real.exp (-(x - y))) := by
      rw [mul_sub, mul_one, ← Real.exp_add]; ring_nf
    have h2 : 1 - Real.exp (-(x - y)) ≤ x - y := by
      have := Real.add_one_le_exp (-(x - y)); linarith
    have h3 : Real.exp (-y) ≤ 1 := Real.exp_le_one_iff.mpr (by linarith)
    have h4 : 0 ≤ 1 - Real.exp (-(x - y)) := by
      have : Real.exp (-(x - y)) ≤ 1 := Real.exp_le_one_iff.mpr (by linarith)
      linarith
    rw [h1]; nlinarith [Real.exp_pos (-y)]
  have := Real.sqrt_le_sqrt hdiff
  linarith

/-! ### The error budget, with `t = B u η^n` -/

/-- Replacement error: `2B ℓ ≤ 2B · 2d/s ≤ 4 B u² η^n/(1-u) < 5 u t` (for `t > 0`). -/
theorem pl_replacement_error (hu : 0 < u) (hu16 : u ≤ 1 / 16) (hη0 : 0 < η) (hη1 : η ≤ 1)
    {B : ℝ} (hB : 0 < B) :
    2 * B * (2 * (u ^ 2 * (η * (1 - η)) ^ n) / (1 - u)) < 5 * u * (B * u * η ^ n) := by
  have hpow : (η * (1 - η)) ^ n ≤ η ^ n := by
    rw [mul_pow]
    have : (1 - η) ^ n ≤ 1 := pow_le_one₀ (by linarith) (by linarith)
    have : 0 ≤ η ^ n := pow_nonneg hη0.le n
    nlinarith [pow_nonneg (show (0:ℝ) ≤ 1 - η by linarith) n]
  have he : 0 < η ^ n := pow_pos hη0 n
  rw [show 2 * B * (2 * (u ^ 2 * (η * (1 - η)) ^ n) / (1 - u)) =
      4 * B * u ^ 2 * (η * (1 - η)) ^ n / (1 - u) by ring]
  rw [div_lt_iff₀ (by linarith)]
  have h1 : 4 * B * u ^ 2 * (η * (1 - η)) ^ n ≤ 4 * B * u ^ 2 * η ^ n :=
    mul_le_mul_of_nonneg_left hpow (by positivity)
  have h2 : 4 * B * u ^ 2 * η ^ n < 5 * u * (B * u * η ^ n) * (1 - u) := by
    have : 0 < B * u ^ 2 * η ^ n := by positivity
    nlinarith
  linarith

/-- Mean shift: `|B s L - 4t| ≤ 39 u t` from `|L - 4q| ≤ 35 u q`, `1 - u ≤ s ≤ 1`. -/
theorem pl_mean_shift {B s L q : ℝ} (hB : 0 ≤ B) (hu : 0 ≤ u) (hu1 : u ≤ 1) (hq : 0 ≤ q)
    (hs1 : 1 - u ≤ s) (hs2 : s ≤ 1) (hL : |L - 4 * q| ≤ 35 * u * q) :
    |B * s * L - 4 * (B * q)| ≤ 39 * u * (B * q) := by
  have hs0 : 0 ≤ s := by linarith
  have hid : B * s * L - 4 * (B * q) = B * s * (L - 4 * q) + 4 * (B * q) * (s - 1) := by ring
  rw [hid]
  calc |B * s * (L - 4 * q) + 4 * (B * q) * (s - 1)|
      ≤ |B * s * (L - 4 * q)| + |4 * (B * q) * (s - 1)| := abs_add_le _ _
    _ ≤ B * 1 * (35 * u * q) + 4 * (B * q) * u := by
        gcongr
        · rw [abs_mul, abs_of_nonneg (by positivity)]
          exact mul_le_mul (by nlinarith) hL (abs_nonneg _) (by positivity)
        · rw [abs_mul, abs_of_nonneg (by positivity)]
          gcongr
          rw [abs_le]; constructor <;> linarith
    _ = 39 * u * (B * q) := by ring

/-- Fluctuation: `L √(B s (1-s)) ≤ 8 u √t` with `L ≤ 8q`, `q = u η^n`, `t = B q`, `0 ≤ 1-s ≤ u`. -/
theorem pl_fluctuation (hu : 0 ≤ u) (hu1 : u ≤ 1) (hη0 : 0 ≤ η) (hη1 : η ≤ 1) {B s L : ℝ} (hB : 0 ≤ B)
    (hs1 : 1 - u ≤ s) (hs2 : s ≤ 1) (hL : L ≤ 8 * (u * η ^ n)) :
    L * Real.sqrt (B * s * (1 - s)) ≤ 8 * u * Real.sqrt (B * (u * η ^ n)) := by
  have he0 : 0 ≤ η ^ n := pow_nonneg hη0 n
  have he1 : η ^ n ≤ 1 := pow_le_one₀ hη0 hη1
  have hs0 : 0 ≤ s := by linarith
  calc L * Real.sqrt (B * s * (1 - s)) ≤ 8 * (u * η ^ n) * Real.sqrt (B * u) := by
        apply mul_le_mul hL _ (Real.sqrt_nonneg _) (by positivity)
        apply Real.sqrt_le_sqrt
        have : s * (1 - s) ≤ u := by nlinarith
        nlinarith
    _ = 8 * u * (η ^ n * Real.sqrt (B * u)) := by ring
    _ ≤ 8 * u * Real.sqrt (B * (u * η ^ n)) := by
        gcongr
        rw [show B * (u * η ^ n) = (B * u) * η ^ n by ring, Real.sqrt_mul' _ he0]
        rw [mul_comm]
        gcongr
        rw [Real.le_sqrt he0 he0]
        nlinarith

end PureLoss

end Bgs.Mathlib
