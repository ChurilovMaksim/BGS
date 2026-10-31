import Bgs.LineBDerand
import Bgs.LineDDefs
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Analysis.Calculus.Deriv.MeanValue
import Mathlib.Analysis.SpecialFunctions.Exponential
import Mathlib.Analysis.Normed.Algebra.Exponential
import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Complex.Basic
import Mathlib.NumberTheory.Real.Irrational
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-!
  Bgs/LineBTraceFormula.lean — the exact Pell-norm trace formula for the
  fixed diagonal kick (TRACE-163, Theorem 1 / Theorem 3 / Theorem 2),
  as far as it closes from definitions and finite algebra.

  What this module proves (no sorry / axiom / native_decide)
  ------------------------------------------------------------
  * §1 Pell toolkit, general m: x_d² − 8y_d² = 1, λ^d = x_d + 2√2·y_d,
    the recurrence 6a_d = a_{d−1} + a_{d+1}, the subtraction laws,
    the φ-symbol φ_m(d) = y_m·x_d − (x_m−1)·y_d with φ_m(d) = φ_m(m−d)
    and φ_m(m) = y_m, and 2y_m/D_m = y′_m/g′_m.
  * §2 The matrix identity H_m · X_φ = D_m • 1 over ℤ (Lemma Q, matrix
    form), with X_φ the circulant φ-matrix. This is the general-m
    version of the kernel-checked `lemmaQ_m` in `Bgs.LineB.Derand`
    (which covers m ≤ 10, 12 only).
  * §3 The quadratic identity (Lemma Q, quadratic form):
    2·Σ_{i,j} n_i n_j φ_m(|i−j|) = 2y_m·Nm(α_n) + D_m·β(n),
    with Nm(α_n) = Σ_{i,j} n_i n_j x_{|i−j|} and
    β(n) = −2·Σ_{i<j} n_i n_j y_{j−i}, plus the exact phase data
    Q(n) = (y′_m/g′_m)·Nm(α_n) + β(n) and 0 ≤ Q(n) ≤ ‖n‖²/2.
  * §4 Reciprocity: the Gauss phase e(r·D̄/N) collapses to
    e(Q(n)/N)·e(−ν·y′_m·Nm(α_n)/g′_m), ν = N⁻¹ mod g′_m.
  * §5 Theorem 1 assembled from the Gauss-sum hypothesis `hGauss`
    (the trace expansion + multidimensional Gauss sum, which needs
    CRT/Gauss-sum infrastructure not present in this module):
    the exact formula (a), |Tr M^m| = 1 (b, from `hGauss`), and the
    finite-sum error bound (c) with the explicit constant
    π·m·s2·s0^{m−1}/N. The passage from finite sums to the absolutely
    convergent sum over ℤ^m is NOT proved here (see `hMoment`).
  * §6 Proposition R, abstract kernel form: for a finite abelian group
    V with a quadratic form 𝒬, the kernel levels are {0, |Rad|/D}
    and the zero pattern is independent of the odd unit ν.
  * §7 Theorem 2, complete-block form: the average over a full block
    of admissible N equals the ν-average exactly (equal fibres,
    hypothesis `hFib`); the incomplete-block D/X term of the source
    is NOT proved here (it is the `hEquidist` hypothesis of the
    175 module).

  What is deliberately NOT claimed
  ---------------------------------
  * The Gauss-sum step itself (trace expansion, completing the square
    mod N, |G(0)| = N^{m/2} by CRT): hypothesis `hGauss`.
  * The identification det(H_m) = D_m (only tables in Derand/150);
    this module uses D_m := 2(x_m − 1) throughout.
  * The Smith identification V ≅ ℤ/d₁ × ℤ/d₂, |V| = D_m,
    Rad = V[4], |Rad| = gcd(4,d₁)·gcd(4,d₂): the kernel theorem is
    abstract; the V-specific values are parameters/hypotheses.
  * The 2m law (needs ND_m + cyclotomic distinctness + the stabilizer
    count), Theorem 5 (physical-τ window), time reversal (TRACE-131,
    cited not re-claimed), pointwise self-averaging (FALSE, not
    claimed), BGS-005/BGS-001, anything at τ = m/N = O(1).
-/

namespace Bgs
namespace LineB
namespace TraceFormula

open Bgs.LineB.Derand
open Matrix
open scoped BigOperators

/-! ### §1. Pell toolkit -/

/-- The fundamental unit λ = 3 + 2√2 of ℤ[√2]. -/
noncomputable def lam : ℝ := 3 + 2 * Real.sqrt 2

/-- The Galois conjugate λ⁻¹ = 3 − 2√2. -/
noncomputable def lamInv : ℝ := 3 - 2 * Real.sqrt 2

lemma sqrt2_sq : (Real.sqrt 2 : ℝ) ^ 2 = 2 := Real.sq_sqrt (by norm_num)

lemma lam_mul_lamInv : lam * lamInv = 1 := by
  unfold lam lamInv
  linear_combination (-4 : ℝ) * sqrt2_sq

lemma lam_add_lamInv : lam + lamInv = 6 := by
  unfold lam lamInv; ring

lemma lam_ne_zero : lam ≠ 0 := by
  intro h
  have h0 : lam * lamInv = 0 := by rw [h]; ring
  rw [lam_mul_lamInv] at h0
  exact one_ne_zero h0

/-- Joint positivity: x_n > 0 and y_n ≥ 0 (proved together, since the
    recurrences mix the two sequences). -/
lemma pell_pos (n : ℕ) : 0 < pellX n ∧ 0 ≤ pellY n := by
  induction n with
  | zero => exact ⟨by decide, by decide⟩
  | succ k ih =>
    have hx : pellX (k + 1) = 3 * pellX k + 8 * pellY k := rfl
    have hy : pellY (k + 1) = pellX k + 3 * pellY k := rfl
    rw [hx, hy]
    exact ⟨by linarith [ih.1, ih.2], by linarith [ih.1, ih.2]⟩

lemma pellX_pos (n : ℕ) : 0 < pellX n := (pell_pos n).1

lemma pellY_nonneg (n : ℕ) : 0 ≤ pellY n := (pell_pos n).2

/-- x_m ≥ 3 for m ≥ 1 (monotonicity of the Pell sequence). -/
lemma pellX_ge_three (m : ℕ) (hm : 1 ≤ m) : 3 ≤ pellX m := by
  have hmono : Monotone pellX := by
    apply monotone_nat_of_le_succ
    intro n
    have hx : pellX (n + 1) = 3 * pellX n + 8 * pellY n := rfl
    have hX := pellX_pos n
    have hY := pellY_nonneg n
    rw [hx]; linarith
  have h1 : pellX 1 = 3 := rfl
  calc 3 = pellX 1 := h1.symm
    _ ≤ pellX m := hmono hm

lemma pell_norm (n : ℕ) : pellX n ^ 2 - 8 * pellY n ^ 2 = 1 := by
  induction n with
  | zero => decide
  | succ k ih =>
    have hx : pellX (k + 1) = 3 * pellX k + 8 * pellY k := rfl
    have hy : pellY (k + 1) = pellX k + 3 * pellY k := rfl
    rw [hx, hy]
    linear_combination ih

/-- λ^d = x_d + 2√2·y_d. -/
lemma lam_pow (d : ℕ) :
    lam ^ d = (pellX d : ℝ) + 2 * Real.sqrt 2 * (pellY d : ℝ) := by
  induction d with
  | zero =>
    have e1 : pellX 0 = 1 := rfl
    have e2 : pellY 0 = 0 := rfl
    rw [e1, e2]
    simp [lam]
  | succ k ih =>
    have hx : pellX (k + 1) = 3 * pellX k + 8 * pellY k := rfl
    have hy : pellY (k + 1) = pellX k + 3 * pellY k := rfl
    rw [pow_succ, ih, hx, hy]
    unfold lam
    push_cast
    linear_combination (4 * (pellY k : ℝ)) * sqrt2_sq

/-- λ̄^d = x_d − 2√2·y_d. -/
lemma lamInv_pow (d : ℕ) :
    lamInv ^ d = (pellX d : ℝ) - 2 * Real.sqrt 2 * (pellY d : ℝ) := by
  induction d with
  | zero =>
    have e1 : pellX 0 = 1 := rfl
    have e2 : pellY 0 = 0 := rfl
    rw [e1, e2]
    simp [lamInv]
  | succ k ih =>
    have hx : pellX (k + 1) = 3 * pellX k + 8 * pellY k := rfl
    have hy : pellY (k + 1) = pellX k + 3 * pellY k := rfl
    rw [pow_succ, ih, hx, hy]
    unfold lamInv
    push_cast
    linear_combination (4 * (pellY k : ℝ)) * sqrt2_sq

/-- λ^d + λ̄^d = 2x_d. -/
lemma lam_add_lamInv_pow (d : ℕ) : lam ^ d + lamInv ^ d = 2 * (pellX d : ℝ) := by
  rw [lam_pow, lamInv_pow]; ring

/-- λ^{−d} = λ̄^d (as a real power identity via zpow). -/
lemma lam_zpow_neg (d : ℕ) : lam ^ (-(d : ℤ)) = lamInv ^ d := by
  have h : lam ^ d * lamInv ^ d = 1 := by
    rw [← mul_pow, lam_mul_lamInv, one_pow]
  rw [_root_.zpow_neg, zpow_natCast, eq_inv_of_mul_eq_one_left h, inv_inv]

/-- Coefficient uniqueness for a + 2√2·b (irrationality of √2). -/
lemma sqrt2_coeff_inj {a b a' b' : ℤ}
    (h : (a : ℝ) + 2 * Real.sqrt 2 * (b : ℝ) = (a' : ℝ) + 2 * Real.sqrt 2 * (b' : ℝ)) :
    a = a' ∧ b = b' := by
  have hbb : b = b' := by
    by_contra hne
    have hbR : (b : ℝ) ≠ (b' : ℝ) := by exact_mod_cast hne
    have hden : (2 : ℝ) * ((b : ℝ) - (b' : ℝ)) ≠ 0 :=
      mul_ne_zero (by norm_num) (sub_ne_zero.mpr hbR)
    have h2 : Real.sqrt 2 = ((a' - a : ℤ) : ℝ) / (2 * ((b : ℝ) - (b' : ℝ))) := by
      rw [eq_div_iff hden]
      push_cast
      linarith [h]
    have h2' : Real.sqrt 2 = ((a' - a : ℤ) : ℝ) / ((2 * (b - b') : ℤ) : ℝ) := by
      rw [h2]
      norm_cast
    exact (irrational_iff_ne_rational _).mp irrational_sqrt_two (a' - a) (2 * (b - b'))
      (by omega) h2'
  subst hbb
  have haa : (a : ℝ) = (a' : ℝ) := by linarith
  exact ⟨by exact_mod_cast haa, rfl⟩

/-- The Pell recurrence 6x_d = x_{d−1} + x_{d+1}, via λ + λ̄ = 6. -/
lemma pell_rec (d : ℕ) (hd : 1 ≤ d) :
    6 * pellX d = pellX (d - 1) + pellX (d + 1) ∧
    6 * pellY d = pellY (d - 1) + pellY (d + 1) := by
  obtain ⟨k, rfl⟩ : ∃ k, d = k + 1 := ⟨d - 1, by omega⟩
  have hlam : 6 * lam ^ (k + 1) = lam ^ (k + 2) + lam ^ k := by
    have h1 : lam ^ (k + 2) = lam ^ (k + 1) * lam := by rw [pow_succ]
    have h2 : lam ^ (k + 1) = lam ^ k * lam := by rw [pow_succ]
    have h3 : lam ^ k = lam ^ (k + 1) * lamInv := by
      rw [h2, mul_assoc, lam_mul_lamInv, mul_one]
    rw [h1, h3]
    have h6 : lam + lamInv = 6 := lam_add_lamInv
    linear_combination (-(lam ^ (k + 1))) * h6
  rw [lam_pow, lam_pow, lam_pow] at hlam
  have hform : ((6 * pellX (k + 1) : ℤ) : ℝ) + 2 * Real.sqrt 2 * ((6 * pellY (k + 1) : ℤ) : ℝ)
      = (((pellX k + pellX (k + 2) : ℤ)) : ℝ)
        + 2 * Real.sqrt 2 * (((pellY k + pellY (k + 2) : ℤ)) : ℝ) := by
    push_cast
    linear_combination hlam
  have hcoeff := sqrt2_coeff_inj hform
  have hx : 6 * pellX (k + 1) = pellX k + pellX (k + 2) := hcoeff.1
  have hy : 6 * pellY (k + 1) = pellY k + pellY (k + 2) := hcoeff.2
  have e1 : k + 1 - 1 = k := by omega
  have e2 : k + 1 + 1 = k + 2 := by omega
  rw [e1, e2]
  exact ⟨hx, hy⟩

/-- Subtraction law for y: y_{m−d} = y_m·x_d − x_m·y_d (d ≤ m). -/
lemma pellY_sub (m d : ℕ) (hd : d ≤ m) :
    pellY (m - d) = pellY m * pellX d - pellX m * pellY d := by
  have hpow : lam ^ (m - d) = lam ^ m * lamInv ^ d := by
    have h1 : lam ^ m = lam ^ (m - d) * lam ^ d := by
      rw [← pow_add]
      congr 1
      omega
    have h2 : lam ^ (m - d) * lam ^ d * lamInv ^ d = lam ^ (m - d) := by
      rw [mul_assoc, ← mul_pow, lam_mul_lamInv, one_pow, mul_one]
    calc lam ^ (m - d) = lam ^ (m - d) * lam ^ d * lamInv ^ d := h2.symm
      _ = lam ^ m * lamInv ^ d := by rw [h1]
  rw [lam_pow, lam_pow, lamInv_pow] at hpow
  have hform : ((pellX (m - d) : ℤ) : ℝ) + 2 * Real.sqrt 2 * ((pellY (m - d) : ℤ) : ℝ)
      = (((pellX m * pellX d - 8 * pellY m * pellY d : ℤ)) : ℝ)
        + 2 * Real.sqrt 2 * (((pellY m * pellX d - pellX m * pellY d : ℤ)) : ℝ) := by
    push_cast
    linear_combination hpow - 4 * (pellY m : ℝ) * (pellY d : ℝ) * sqrt2_sq
  exact (sqrt2_coeff_inj hform).2

/-- Subtraction law for x: x_{m−d} = x_m·x_d − 8·y_m·y_d (d ≤ m). -/
lemma pellX_sub (m d : ℕ) (hd : d ≤ m) :
    pellX (m - d) = pellX m * pellX d - 8 * pellY m * pellY d := by
  have hpow : lam ^ (m - d) = lam ^ m * lamInv ^ d := by
    have h1 : lam ^ m = lam ^ (m - d) * lam ^ d := by
      rw [← pow_add]
      congr 1
      omega
    have h2 : lam ^ (m - d) * lam ^ d * lamInv ^ d = lam ^ (m - d) := by
      rw [mul_assoc, ← mul_pow, lam_mul_lamInv, one_pow, mul_one]
    calc lam ^ (m - d) = lam ^ (m - d) * lam ^ d * lamInv ^ d := h2.symm
      _ = lam ^ m * lamInv ^ d := by rw [h1]
  rw [lam_pow, lam_pow, lamInv_pow] at hpow
  have hform : ((pellX (m - d) : ℤ) : ℝ) + 2 * Real.sqrt 2 * ((pellY (m - d) : ℤ) : ℝ)
      = (((pellX m * pellX d - 8 * pellY m * pellY d : ℤ)) : ℝ)
        + 2 * Real.sqrt 2 * (((pellY m * pellX d - pellX m * pellY d : ℤ)) : ℝ) := by
    push_cast
    linear_combination hpow - 4 * (pellY m : ℝ) * (pellY d : ℝ) * sqrt2_sq
  exact (sqrt2_coeff_inj hform).1

/-- The φ-symbol: φ_m(d) = y_m·x_d − (x_m−1)·y_d. At d = 0 it is y_m;
    it is the circulant symbol of X_m (Lemma Q). -/
def phi (m d : ℕ) : ℤ := pellY m * pellX d - (pellX m - 1) * pellY d

lemma phi_zero (m : ℕ) : phi m 0 = pellY m := by
  have e1 : pellX 0 = 1 := rfl
  have e2 : pellY 0 = 0 := rfl
  unfold phi
  rw [e1, e2]
  ring

lemma phi_m (m : ℕ) : phi m m = pellY m := by
  unfold phi; ring

lemma phi_symm (m d : ℕ) (hd : d ≤ m) : phi m d = phi m (m - d) := by
  unfold phi
  rw [pellX_sub m d hd, pellY_sub m d hd]
  have hnorm := pell_norm m
  linear_combination (-(pellY d : ℤ)) * hnorm

lemma phi_rec (m d : ℕ) (hd : 1 ≤ d) :
    6 * phi m d = phi m (d - 1) + phi m (d + 1) := by
  have hr := pell_rec d hd
  unfold phi
  linear_combination (pellY m) * hr.1 - (pellX m - 1) * hr.2

/-- y_{m−1} = 3y_m − x_m (used for the diagonal of H·X). -/
lemma pellY_pred (m : ℕ) (hm : 1 ≤ m) : pellY (m - 1) = 3 * pellY m - pellX m := by
  obtain ⟨k, rfl⟩ : ∃ k, m = k + 1 := ⟨m - 1, by omega⟩
  have hx : pellX (k + 1) = 3 * pellX k + 8 * pellY k := rfl
  have hy : pellY (k + 1) = pellX k + 3 * pellY k := rfl
  have e : k + 1 - 1 = k := by omega
  rw [e, hy, hx]
  ring

lemma phi_one (m : ℕ) (hm : 1 ≤ m) : phi m 1 = 1 + pellY (m - 1) := by
  have hx1 : pellX 1 = 3 := rfl
  have hy1 : pellY 1 = 1 := rfl
  unfold phi
  rw [hx1, hy1, pellY_pred m hm]
  ring

/-- 2y_m/D_m = y′_m/g′_m (both sides are the reduced fraction). -/
lemma two_y_over_D (m : ℕ) (hm : 1 ≤ m) :
    (2 * (pellY m : ℚ)) / (Dm m : ℚ) = (yp m : ℚ) / (gp m : ℚ) := by
  have h3 := pellX_ge_three m hm
  have hY := pellY_nonneg m
  set A := (pellX m - 1).toNat with hAdef
  set B := (pellY m).toNat with hBdef
  set g := Nat.gcd A B with hgdef
  have hApos : 0 < A := by omega
  have hAint : (A : ℤ) = pellX m - 1 := Int.toNat_of_nonneg (by linarith)
  have hBint : (B : ℤ) = pellY m := Int.toNat_of_nonneg hY
  have hBpos : 0 < B := by
    have hnorm := pell_norm m
    have h1 : (1 : ℤ) ≤ pellY m := by nlinarith [h3, hY]
    omega
  have hgA : g ∣ A := Nat.gcd_dvd_left A B
  have hgB : g ∣ B := Nat.gcd_dvd_right A B
  have hgpos : 0 < g := Nat.gcd_pos_of_pos_left B hApos
  have hyp : yp m = B / g := by
    unfold yp
    rw [← hAdef, ← hBdef, ← hgdef]
  have hgp : gp m = A / g := by
    unfold gp
    rw [← hAdef, ← hBdef, ← hgdef]
  have hgp0 : gp m ≠ 0 := by
    rw [hgp]
    have hle : g ≤ A := by rw [hgdef]; exact Nat.gcd_le_left B hApos
    have := Nat.div_pos hle hgpos
    omega
  have key : yp m * A = gp m * B := by
    rw [hyp, hgp]
    have e2 : A = (A / g) * g := (Nat.div_mul_cancel hgA).symm
    calc (B / g) * A = (B / g) * ((A / g) * g) := by conv_lhs => rw [e2]
      _ = ((B / g) * g) * (A / g) := by ring
      _ = B * (A / g) := by rw [Nat.div_mul_cancel hgB]
      _ = (A / g) * B := by rw [mul_comm]
  have hDm : Dm m = 2 * (pellX m - 1) := rfl
  have hDne : (Dm m : ℚ) ≠ 0 := by
    rw [hDm]
    have hpos : (0 : ℤ) < 2 * (pellX m - 1) := by linarith
    exact_mod_cast (ne_of_gt hpos)
  have hgpne : (gp m : ℚ) ≠ 0 := by exact_mod_cast hgp0
  rw [div_eq_div_iff hDne hgpne]
  have keyQ : (yp m : ℚ) * (A : ℚ) = (gp m : ℚ) * (B : ℚ) := by exact_mod_cast key
  have hAQ : (A : ℚ) = ((pellX m - 1 : ℤ) : ℚ) := by exact_mod_cast hAint
  have hBQ : (B : ℚ) = (pellY m : ℚ) := by exact_mod_cast hBint
  rw [hAQ, hBQ] at keyQ
  push_cast at keyQ
  rw [hDm]
  push_cast
  linear_combination (-2) * keyQ

/-- g′_m divides D_m. -/
lemma gp_dvd_D (m : ℕ) (hm : 1 ≤ m) : gp m ∣ (Dm m).toNat := by
  have hDm : Dm m = 2 * (pellX m - 1) := rfl
  have hA : ((pellX m - 1).toNat : ℤ) = pellX m - 1 := by
    apply Int.toNat_of_nonneg
    have h3 := pellX_ge_three m hm
    linarith
  have hdiv : gp m ∣ (pellX m - 1).toNat := by
    unfold gp
    refine ⟨(pellX m - 1).toNat.gcd (pellY m).toNat, ?_⟩
    exact (Nat.div_mul_cancel (Nat.gcd_dvd_left _ _)).symm
  have h2 : (Dm m).toNat = 2 * (pellX m - 1).toNat := by
    have hnn : (0 : ℤ) ≤ pellX m - 1 := by
      have h3 := pellX_ge_three m hm
      linarith
    have h2nat : Int.toNat (2 : ℤ) = 2 := by decide
    rw [hDm, Int.toNat_mul (by norm_num : (0 : ℤ) ≤ 2) hnn, h2nat]
  rw [h2]
  exact dvd_trans hdiv (Nat.dvd_mul_left _ _)

/-! ### §2. The matrix identity H_m · X_φ = D_m · I over ℤ -/

/-- The Pell-symbol matrix: X_φ[i][j] = φ_m((j − i) mod m). -/
def Xphi (m : ℕ) : Matrix (ZMod m) (ZMod m) ℤ :=
  Matrix.of fun i j => phi m (j - i).val

/-- φ̄_m(r) = φ_m(r.val): the symbol read at a residue. -/
def φbar (m : ℕ) (r : ZMod m) : ℤ := phi m r.val

lemma φbar_zero (m : ℕ) : φbar m 0 = pellY m := by
  simp [φbar, phi_zero]

lemma φbar_one (m : ℕ) [NeZero m] (hm : 2 ≤ m) : φbar m 1 = phi m 1 := by
  have h : (1 : ZMod m) = ((1 : ℕ) : ZMod m) := by simp
  rw [φbar, h, ZMod.val_natCast_of_lt (by omega : (1 : ℕ) < m)]

lemma φbar_neg_one (m : ℕ) [NeZero m] (hm : 2 ≤ m) :
    φbar m (-1) = phi m 1 := by
  have hcast : ((-1 : ZMod m)) = (((m - 1 : ℕ)) : ZMod m) := by
    have h1 : (((m - 1 : ℕ)) : ZMod m) + 1 = 0 := by
      have hc : ((((m - 1 + 1 : ℕ))) : ZMod m) = (((m - 1 : ℕ)) : ZMod m) + 1 := by
        rw [Nat.cast_add, Nat.cast_one]
      rw [← hc, Nat.sub_add_cancel (show 1 ≤ m by omega)]
      exact ZMod.natCast_self m
    exact (eq_neg_of_add_eq_zero_left h1).symm
  have hval : ((-1 : ZMod m)).val = m - 1 := by
    rw [hcast, ZMod.val_natCast_of_lt (by omega : m - 1 < m)]
  rw [φbar, hval]
  have hs := phi_symm m (m - 1) (by omega)
  rw [Nat.sub_sub_self (show 1 ≤ m by omega)] at hs
  exact hs

lemma φbar_sub (m : ℕ) [NeZero m] (r : ZMod m) (hr : r ≠ 0) :
    φbar m (r - 1) = phi m (r.val - 1) := by
  have hd : 1 ≤ r.val := by
    have h0 : r.val ≠ 0 := by
      intro h
      apply hr
      rw [← ZMod.natCast_zmod_val r, h]
      simp
    omega
  have hcast : r - 1 = (((r.val - 1 : ℕ)) : ZMod m) := by
    have h1 : r = ((r.val : ℕ) : ZMod m) := (ZMod.natCast_zmod_val r).symm
    have hc : ((((r.val - 1 : ℕ))) : ZMod m) = ((r.val : ℕ) : ZMod m) - 1 := by
      rw [Nat.cast_sub hd, Nat.cast_one]
    conv_lhs => rw [h1]
    exact hc.symm
  rw [φbar, hcast, ZMod.val_natCast_of_lt (by
    have := ZMod.val_lt r
    omega : r.val - 1 < m)]

lemma φbar_add (m : ℕ) [NeZero m] (r : ZMod m) (hr : r ≠ 0) :
    φbar m (r + 1) = phi m (r.val + 1) := by
  have hd : 1 ≤ r.val := by
    have h0 : r.val ≠ 0 := by
      intro h
      apply hr
      rw [← ZMod.natCast_zmod_val r, h]
      simp
    omega
  have hlt : r.val < m := ZMod.val_lt r
  by_cases hc : r.val + 1 < m
  · have hcast : r + 1 = (((r.val + 1 : ℕ)) : ZMod m) := by
      have h1 : r = ((r.val : ℕ) : ZMod m) := (ZMod.natCast_zmod_val r).symm
      have hc : ((((r.val + 1 : ℕ))) : ZMod m) = ((r.val : ℕ) : ZMod m) + 1 := by
        rw [Nat.cast_add, Nat.cast_one]
      conv_lhs => rw [h1]
      exact hc.symm
    rw [φbar, hcast, ZMod.val_natCast_of_lt hc]
  · have hdm : r.val + 1 = m := by omega
    have hcast : r + 1 = 0 := by
      have h1 : r = ((r.val : ℕ) : ZMod m) := (ZMod.natCast_zmod_val r).symm
      have hc : ((((r.val + 1 : ℕ))) : ZMod m) = ((r.val : ℕ) : ZMod m) + 1 := by
        rw [Nat.cast_add, Nat.cast_one]
      rw [h1, ← hc, hdm]
      exact ZMod.natCast_self m
    rw [hcast, φbar_zero, hdm]
    exact (phi_m m).symm

/-- The symbol recurrence, read at residues: 6φ̄(r) − φ̄(r−1) − φ̄(r+1)
    is D_m at r = 0 and 0 elsewhere. This is Lemma Q, step 2, in matrix form. -/
lemma phiBar_rec (m : ℕ) [NeZero m] (hm : 2 ≤ m) (r : ZMod m) :
    6 * φbar m r - φbar m (r - 1) - φbar m (r + 1)
      = if r = 0 then Dm m else 0 := by
  by_cases hr : r = 0
  · subst hr
    rw [if_pos rfl]
    simp only [zero_sub, zero_add]
    rw [φbar_zero, φbar_neg_one m hm, φbar_one m hm]
    have h1 := phi_one m (by omega : 1 ≤ m)
    have hp := pellY_pred m (by omega : 1 ≤ m)
    have hDm : Dm m = 2 * (pellX m - 1) := rfl
    rw [hDm]
    linarith
  · rw [if_neg hr, φbar_sub m r hr, φbar_add m r hr]
    have hrec := phi_rec m r.val (by
      have h0 : r.val ≠ 0 := by
        intro h
        apply hr
        rw [← ZMod.natCast_zmod_val r, h]
        simp
      omega)
    have hφ : φbar m r = phi m r.val := rfl
    rw [hφ]
    linarith

/-- Lemma Q, step 2, as a matrix identity over ℤ. -/
theorem HXphi (m : ℕ) [NeZero m] (hm : 2 ≤ m) :
    Bgs.LineD.Defs.Hmat m ℤ * Xphi m
      = Dm m • (1 : Matrix (ZMod m) (ZMod m) ℤ) := by
  ext i j
  have key : (Bgs.LineD.Defs.Hmat m ℤ * Xphi m) i j
      = 6 * Xphi m i j - Xphi m (i + 1) j - Xphi m (i - 1) j := by
    rw [Matrix.mul_apply]
    have hH : ∀ k, Bgs.LineD.Defs.Hmat m ℤ i k
        = (if i = k then (6 : ℤ) else 0) - (if k = i + 1 then (1 : ℤ) else 0)
          - (if i = k + 1 then (1 : ℤ) else 0) := by
      intro k
      have eC : Bgs.LineD.Defs.shiftMat m ℤ i k = if k = i + 1 then 1 else 0 := rfl
      have eCT : (Bgs.LineD.Defs.shiftMat m ℤ)ᵀ i k = if i = k + 1 then 1 else 0 := rfl
      have e1 : ((6 : ℤ) • (1 : Matrix (ZMod m) (ZMod m) ℤ)) i k
          = if i = k then 6 else 0 := by
        rw [Matrix.smul_apply, Matrix.one_apply]
        split_ifs <;> simp
      simp only [Bgs.LineD.Defs.Hmat, Matrix.sub_apply, e1, eC, eCT]
    simp only [hH, sub_mul]
    rw [Finset.sum_sub_distrib, Finset.sum_sub_distrib]
    have s1 : ∑ k, (if i = k then (6 : ℤ) else 0) * Xphi m k j
        = 6 * Xphi m i j := by
      rw [Finset.sum_eq_single i]
      · simp
      · intro k _ hki
        simp [show i ≠ k from fun h => hki h.symm]
      · simp
    have s2 : ∑ k, (if k = i + 1 then (1 : ℤ) else 0) * Xphi m k j
        = Xphi m (i + 1) j := by
      rw [Finset.sum_eq_single (i + 1)]
      · simp
      · intro k _ hki
        simp [hki]
      · simp
    have s3 : ∑ k, (if i = k + 1 then (1 : ℤ) else 0) * Xphi m k j
        = Xphi m (i - 1) j := by
      rw [Finset.sum_eq_single (i - 1)]
      · simp [sub_add_cancel]
      · intro k _ hki
        have hne : i ≠ k + 1 := by
          intro h
          apply hki
          rw [eq_sub_iff_add_eq]
          exact h.symm
        simp [hne]
      · simp
    rw [s1, s2, s3]
  rw [key]
  have e1 : j - (i + 1) = (j - i) - 1 := by abel
  have e2 : j - (i - 1) = (j - i) + 1 := by abel
  have hX1 : Xphi m i j = φbar m (j - i) := rfl
  have hX2 : Xphi m (i + 1) j = φbar m ((j - i) - 1) := by
    show phi m (j - (i + 1)).val = phi m ((j - i) - 1).val
    rw [e1]
  have hX3 : Xphi m (i - 1) j = φbar m ((j - i) + 1) := by
    show phi m (j - (i - 1)).val = phi m ((j - i) + 1).val
    rw [e2]
  rw [hX1, hX2, hX3, phiBar_rec m hm (j - i)]
  by_cases hij : i = j
  · subst hij
    simp [sub_self]
  · have hji : j - i ≠ 0 := sub_ne_zero.mpr (Ne.symm hij)
    rw [if_neg hji]
    simp [Matrix.smul_apply, hij]

/-! ### §3. Norms and the quadratic identity -/

/-- α_n = Σ_j n_j λ^j (real embedding of the Pell-ring element). -/
noncomputable def alpha (m : ℕ) (n : Fin m → ℤ) : ℝ :=
  ∑ j, (n j : ℝ) * lam ^ (j : ℕ)

/-- ᾱ_n = Σ_j n_j λ̄^j (Galois conjugate). -/
noncomputable def alphaBar (m : ℕ) (n : Fin m → ℤ) : ℝ :=
  ∑ j, (n j : ℝ) * lamInv ^ (j : ℕ)

/-- Nm(α_n) as a real number: α_n · ᾱ_n. -/
noncomputable def NmR (m : ℕ) (n : Fin m → ℤ) : ℝ := alpha m n * alphaBar m n

/-- Nm(α_n) as an integer: Σ_{i,j} n_i n_j x_{|i−j|}. -/
def NmZ (m : ℕ) (n : Fin m → ℤ) : ℤ :=
  ∑ i, ∑ j, (n i * n j) * pellX (dist m (i : ℕ) (j : ℕ))

/-- β(n) = −Σ_{i,j} n_i n_j y_{|i−j|} (full double sum; it equals the
    source's −2Σ_{i<j} n_i n_j y_{j−i} since diagonal terms vanish, y_0 = 0,
    and off-diagonal terms pair by symmetry of dist — see `beta_pair`). -/
def beta (m : ℕ) (n : Fin m → ℤ) : ℤ :=
  -∑ i, ∑ j, (n i * n j) * pellY (dist m (i : ℕ) (j : ℕ))

/-- r(n) = 2y_m·Nm(α_n) + D_m·β(n), the numerator of Q(n). -/
def Qnum (m : ℕ) (n : Fin m → ℤ) : ℤ :=
  2 * pellY m * NmZ m n + Dm m * beta m n

lemma dist_symm (m i j : ℕ) : dist m i j = dist m j i := by
  show (if i ≤ j then j - i else i - j) = (if j ≤ i then i - j else j - i)
  split_ifs with h1 h2 h2 <;> omega

lemma dist_self (m i : ℕ) : dist m i i = 0 := by
  show (if i ≤ i then i - i else i - i) = 0
  simp

/-- Pairing of λ-powers: λ^i λ̄^j + λ^j λ̄^i = 2x_{|i−j|}. -/
lemma pair_pow (m i j : ℕ) :
    lam ^ i * lamInv ^ j + lam ^ j * lamInv ^ i
      = 2 * (pellX (dist m i j) : ℝ) := by
  rcases le_total i j with h | h
  · have hd : dist m i j = j - i := by
      show (if i ≤ j then j - i else i - j) = j - i
      simp [h]
    have e1 : lam ^ i * lamInv ^ j = lamInv ^ (j - i) := by
      have hj : j = (j - i) + i := (Nat.sub_add_cancel h).symm
      conv_lhs => rw [hj]
      rw [pow_add]
      have hr : lam ^ i * (lamInv ^ (j - i) * lamInv ^ i)
          = lamInv ^ (j - i) * (lam ^ i * lamInv ^ i) := by ring
      rw [hr, ← mul_pow, lam_mul_lamInv, one_pow, mul_one]
    have e2 : lam ^ j * lamInv ^ i = lam ^ (j - i) := by
      have hj : j = (j - i) + i := (Nat.sub_add_cancel h).symm
      conv_lhs => rw [hj]
      rw [pow_add]
      have hr : (lam ^ (j - i) * lam ^ i) * lamInv ^ i
          = lam ^ (j - i) * (lam ^ i * lamInv ^ i) := by ring
      rw [hr, ← mul_pow, lam_mul_lamInv, one_pow, mul_one]
    rw [hd, e1, e2, add_comm]
    exact lam_add_lamInv_pow (j - i)
  · have hd : dist m i j = i - j := by
      show (if i ≤ j then j - i else i - j) = i - j
      split_ifs with h2 <;> omega
    have e1 : lam ^ i * lamInv ^ j = lam ^ (i - j) := by
      have hi : i = (i - j) + j := (Nat.sub_add_cancel h).symm
      conv_lhs => rw [hi]
      rw [pow_add]
      have hr : (lam ^ (i - j) * lam ^ j) * lamInv ^ j
          = lam ^ (i - j) * (lam ^ j * lamInv ^ j) := by ring
      rw [hr, ← mul_pow, lam_mul_lamInv, one_pow, mul_one]
    have e2 : lam ^ j * lamInv ^ i = lamInv ^ (i - j) := by
      have hi : i = (i - j) + j := (Nat.sub_add_cancel h).symm
      conv_lhs => rw [hi]
      rw [pow_add]
      have hr : lam ^ j * (lamInv ^ (i - j) * lamInv ^ j)
          = lamInv ^ (i - j) * (lam ^ j * lamInv ^ j) := by ring
      rw [hr, ← mul_pow, lam_mul_lamInv, one_pow, mul_one]
    rw [hd, e1, e2]
    exact lam_add_lamInv_pow (i - j)

/-- Nm(α_n) computed in ℝ equals the integer norm sum. -/
lemma Nm_eq (m : ℕ) (n : Fin m → ℤ) : NmR m n = (NmZ m n : ℝ) := by
  set h : Fin m → Fin m → ℝ :=
    fun i j => (n i : ℝ) * (n j : ℝ) * (lam ^ (i : ℕ) * lamInv ^ (j : ℕ)) with hh
  have hexpand : NmR m n = ∑ i, ∑ j, h i j := by
    rw [NmR, alpha, alphaBar, Finset.sum_mul_sum]
    apply Finset.sum_congr rfl
    intro i _
    apply Finset.sum_congr rfl
    intro j _
    simp only [hh]
    ring
  have hswap : (∑ i, ∑ j, h j i) = ∑ i, ∑ j, h i j := by
    rw [← Finset.sum_product', ← Finset.sum_product']
    exact Equiv.sum_comp (Equiv.prodComm (Fin m) (Fin m)) (fun p => h p.1 p.2)
  have hpair : ∀ i j, h i j + h j i
      = 2 * ((n i : ℝ) * (n j : ℝ) * (pellX (dist m (i : ℕ) (j : ℕ)) : ℝ)) := by
    intro i j
    have hp := pair_pow m (i : ℕ) (j : ℕ)
    simp only [hh]
    linear_combination ((n i : ℝ) * (n j : ℝ)) * hp
  have hS : (∑ i, ∑ j, h i j) + (∑ i, ∑ j, h j i) = 2 * (NmZ m n : ℝ) := by
    have hsum : (∑ i, ∑ j, (h i j + h j i))
        = ∑ i, ∑ j, 2 * ((n i : ℝ) * (n j : ℝ)
          * (pellX (dist m (i : ℕ) (j : ℕ)) : ℝ)) := by
      apply Finset.sum_congr rfl
      intro i _
      apply Finset.sum_congr rfl
      intro j _
      exact hpair i j
    simp only [← Finset.sum_add_distrib]
    rw [hsum]
    simp only [← Finset.mul_sum]
    congr 1
    rw [NmZ]
    push_cast
    apply Finset.sum_congr rfl
    intro i _
    apply Finset.sum_congr rfl
    intro j _
    ring
  have h2 : 2 * NmR m n = 2 * (NmZ m n : ℝ) := by
    rw [hexpand, two_mul]
    nth_rewrite 2 [← hswap]
    exact hS
  linarith

/-- The quadratic identity of Lemma Q: 2nᵀH⁻¹n, computed as a φ-sum,
    equals r(n) = 2y_m·Nm(α_n) + D_m·β(n). -/
lemma quadId (m : ℕ) (n : Fin m → ℤ) :
    2 * (∑ i, ∑ j, (n i * n j) * phi m (dist m (i : ℕ) (j : ℕ)))
      = Qnum m n := by
  have expand : (∑ i, ∑ j, (n i * n j) * phi m (dist m (i : ℕ) (j : ℕ)))
      = (∑ i, ∑ j, (n i * n j) * (pellY m * pellX (dist m (i : ℕ) (j : ℕ))))
        - (∑ i, ∑ j, (n i * n j) * ((pellX m - 1) * pellY (dist m (i : ℕ) (j : ℕ)))) := by
    simp only [← Finset.sum_sub_distrib]
    apply Finset.sum_congr rfl
    intro i _
    apply Finset.sum_congr rfl
    intro j _
    rw [phi]
    ring
  have fac1 : (∑ i, ∑ j, (n i * n j) * (pellY m * pellX (dist m (i : ℕ) (j : ℕ))))
      = pellY m * NmZ m n := by
    rw [NmZ, Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro i _
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro j _
    ring
  have fac2 : (∑ i, ∑ j, (n i * n j) * ((pellX m - 1) * pellY (dist m (i : ℕ) (j : ℕ))))
      = (pellX m - 1) * (-beta m n) := by
    rw [beta, neg_neg, Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro i _
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro j _
    ring
  rw [expand, fac1, fac2, Qnum]
  have hDm : Dm m = 2 * (pellX m - 1) := rfl
  rw [hDm]
  ring

/-- Q(n) = r(n)/D_m, in the source's reduced form. -/
lemma Q_eq (m : ℕ) (hm : 1 ≤ m) (n : Fin m → ℤ) :
    (Qnum m n : ℚ) / (Dm m : ℚ)
      = (yp m : ℚ) / (gp m : ℚ) * (NmZ m n : ℚ) + (beta m n : ℚ) := by
  have h3 := pellX_ge_three m hm
  have hDm : Dm m = 2 * (pellX m - 1) := rfl
  have hDne : (Dm m : ℚ) ≠ 0 := by
    rw [hDm]
    have hpos : (0 : ℤ) < 2 * (pellX m - 1) := by linarith
    exact_mod_cast (ne_of_gt hpos)
  have h2y := two_y_over_D m hm
  have h2y' : (yp m : ℚ) / (gp m : ℚ) * (Dm m : ℚ) = 2 * (pellY m : ℚ) := by
    rw [← h2y]
    exact div_mul_cancel₀ _ hDne
  rw [Qnum, div_eq_iff hDne]
  push_cast
  linear_combination (-(NmZ m n : ℚ)) * h2y'

/-! ### §4. Bounds for Q(n) via the matrix form -/

/-- X_φ over ℝ (entrywise cast of the integer matrix). -/
def XphiR (m : ℕ) : Matrix (ZMod m) (ZMod m) ℝ :=
  (Xphi m).map (Int.castRingHom ℝ)

/-- H_m⁻¹ over ℝ, for m ≥ 2: (1/D_m) • X_φ. -/
noncomputable def Hinv (m : ℕ) [NeZero m] (_hm : 2 ≤ m) :
    Matrix (ZMod m) (ZMod m) ℝ :=
  ((Dm m : ℝ))⁻¹ • XphiR m

lemma Dm_real_ne_zero (m : ℕ) (hm : 1 ≤ m) : (Dm m : ℝ) ≠ 0 := by
  have h3 := pellX_ge_three m hm
  have hDm : Dm m = 2 * (pellX m - 1) := rfl
  rw [hDm]
  have hpos : (0 : ℤ) < 2 * (pellX m - 1) := by linarith
  exact_mod_cast (ne_of_gt hpos)

lemma XphiR_apply (m : ℕ) (i j : ZMod m) :
    XphiR m i j = (φbar m (j - i) : ℝ) := by
  simp [XphiR, Xphi, φbar, Matrix.map_apply]

lemma Hmat_entry (m : ℕ) (α : Type*) [Ring α] (i j : ZMod m) :
    Bgs.LineD.Defs.Hmat m α i j
      = (if i = j then (6 : α) else 0) - (if j = i + 1 then (1 : α) else 0)
        - (if i = j + 1 then (1 : α) else 0) := by
  have eC : Bgs.LineD.Defs.shiftMat m α i j = if j = i + 1 then 1 else 0 := rfl
  have eCT : (Bgs.LineD.Defs.shiftMat m α)ᵀ i j = if i = j + 1 then 1 else 0 := rfl
  have e1 : ((6 : α) • (1 : Matrix (ZMod m) (ZMod m) α)) i j
      = if i = j then 6 else 0 := by
    rw [Matrix.smul_apply, Matrix.one_apply]
    split_ifs <;> simp
  simp only [Bgs.LineD.Defs.Hmat, Matrix.sub_apply, e1, eC, eCT]

lemma Hmat_map (m : ℕ) :
    (Bgs.LineD.Defs.Hmat m ℤ).map (Int.castRingHom ℝ)
      = Bgs.LineD.Defs.Hmat m ℝ := by
  ext i j
  rw [Matrix.map_apply, Hmat_entry m ℤ, Hmat_entry m ℝ]
  split_ifs <;> norm_num

/-- H_m · H_m⁻¹ = I over ℝ (from the integer identity HXphi, cast). -/
lemma Hmat_mul_Hinv (m : ℕ) [NeZero m] (hm : 2 ≤ m) :
    Bgs.LineD.Defs.Hmat m ℝ * Hinv m hm = 1 := by
  have hcast : (Bgs.LineD.Defs.Hmat m ℤ * Xphi m).map (Int.castRingHom ℝ)
      = (Dm m • (1 : Matrix (ZMod m) (ZMod m) ℤ)).map (Int.castRingHom ℝ) :=
    congrArg (fun M : Matrix (ZMod m) (ZMod m) ℤ => M.map (Int.castRingHom ℝ))
      (HXphi m hm)
  rw [Matrix.map_mul, Hmat_map] at hcast
  have hX : (Xphi m).map (Int.castRingHom ℝ) = XphiR m := rfl
  rw [hX] at hcast
  have hD : ((Dm m • (1 : Matrix (ZMod m) (ZMod m) ℤ)).map (Int.castRingHom ℝ))
      = (Dm m : ℝ) • (1 : Matrix (ZMod m) (ZMod m) ℝ) := by
    ext i j
    rw [Matrix.map_apply]
    by_cases hij : i = j
    · subst hij
      simp [Matrix.smul_apply]
    · simp [Matrix.smul_apply, hij]
  rw [hD] at hcast
  unfold Hinv
  rw [Matrix.mul_smul, hcast, smul_smul, inv_mul_cancel₀
    (Dm_real_ne_zero m (by omega : 1 ≤ m)), one_smul]

/-- H_m is symmetric over ℝ. -/
lemma Hmat_symm (m : ℕ) :
    (Bgs.LineD.Defs.Hmat m ℝ)ᵀ = Bgs.LineD.Defs.Hmat m ℝ := by
  simp only [Bgs.LineD.Defs.Hmat, Matrix.transpose_sub, Matrix.transpose_smul,
    Matrix.transpose_one, Matrix.transpose_transpose]
  exact sub_right_comm _ _ _

/-- (H_m u)_i = 6u_i − u_{i+1} − u_{i−1}. -/
lemma Hmat_mulVec_apply (m : ℕ) [NeZero m] (u : ZMod m → ℝ) (i : ZMod m) :
    (Bgs.LineD.Defs.Hmat m ℝ *ᵥ u) i = 6 * u i - u (i + 1) - u (i - 1) := by
  have hC := Bgs.LineD.Defs.shift_mulVec m ℝ u
  have hCT := Bgs.LineD.Defs.shift_transpose_mulVec m ℝ u
  have hH : (Bgs.LineD.Defs.Hmat m ℝ) *ᵥ u
      = (6 : ℝ) • u - (fun i => u (i + 1)) - (fun i => u (i - 1)) := by
    simp only [Bgs.LineD.Defs.Hmat, Matrix.sub_mulVec, Matrix.smul_mulVec,
      Matrix.one_mulVec, hC, hCT]
  rw [hH]
  simp [Pi.sub_apply, Pi.smul_apply, smul_eq_mul]

/-- The quadratic form nᵀH⁻¹n is nonnegative (H⁻¹ is positive via H). -/
lemma quad_nonneg (m : ℕ) [NeZero m] (hm : 2 ≤ m) (n : ZMod m → ℝ) :
    0 ≤ n ⬝ᵥ (Hinv m hm *ᵥ n) := by
  have hHu : Bgs.LineD.Defs.Hmat m ℝ *ᵥ (Hinv m hm *ᵥ n) = n := by
    rw [Matrix.mulVec_mulVec, Hmat_mul_Hinv, Matrix.one_mulVec]
  have hdot := Bgs.LineD.Defs.Hmat_dotProduct m (Hinv m hm *ᵥ n)
  rw [hHu] at hdot
  rw [dotProduct_comm, hdot]
  apply add_nonneg
  · exact mul_nonneg (by norm_num)
      (Finset.sum_nonneg fun i _ => mul_self_nonneg _)
  · exact Finset.sum_nonneg fun i _ => mul_self_nonneg _

/-- The Fin m ≃ ZMod m equivalence (val / Nat cast). -/
def zmodFinEquiv (m : ℕ) [NeZero m] : ZMod m ≃ Fin m where
  toFun r := ⟨r.val, ZMod.val_lt r⟩
  invFun j := ((j.val : ℕ) : ZMod m)
  left_inv r := by
    show ((r.val : ℕ) : ZMod m) = r
    exact ZMod.natCast_zmod_val r
  right_inv j := Fin.ext (ZMod.val_natCast_of_lt j.isLt)

/-- φ̄ at a difference of Nat casts is φ at the linear distance. -/
lemma φbar_cast_sub (m : ℕ) [NeZero m] (_hm : 2 ≤ m) (i j : ℕ)
    (hi : i < m) (hj : j < m) :
    φbar m ((((j : ℕ)) : ZMod m) - (((i : ℕ)) : ZMod m))
      = phi m (dist m i j) := by
  by_cases hle : i ≤ j
  · have hd : dist m i j = j - i := by
      show (if i ≤ j then j - i else i - j) = j - i
      simp [hle]
    have hcast : (((j : ℕ)) : ZMod m) - (((i : ℕ)) : ZMod m)
        = (((j - i : ℕ)) : ZMod m) := by
      rw [Nat.cast_sub hle]
    rw [hd, φbar, hcast, ZMod.val_natCast_of_lt (by omega : j - i < m)]
  · have hlt : j < i := by omega
    have hd : dist m i j = i - j := by
      show (if i ≤ j then j - i else i - j) = i - j
      split_ifs <;> omega
    have hcast : (((j : ℕ)) : ZMod m) - (((i : ℕ)) : ZMod m)
        = -((((i - j : ℕ)) : ZMod m)) := by
      have h1 : (((i : ℕ)) : ZMod m) - (((j : ℕ)) : ZMod m)
          = (((i - j : ℕ)) : ZMod m) := by
        rw [Nat.cast_sub (le_of_lt hlt)]
      rw [← h1]
      abel
    have hneg : -(((i - j : ℕ)) : ZMod m) = (((m - (i - j) : ℕ)) : ZMod m) := by
      have h2 : (((i - j : ℕ)) : ZMod m) + (((m - (i - j) : ℕ)) : ZMod m) = 0 := by
        rw [← Nat.cast_add, Nat.add_sub_cancel' (by omega : i - j ≤ m)]
        exact ZMod.natCast_self m
      exact (eq_neg_of_add_eq_zero_right h2).symm
    rw [hd, φbar, hcast, hneg, ZMod.val_natCast_of_lt (by omega : m - (i - j) < m)]
    have hs := phi_symm m (i - j) (by omega)
    exact hs.symm

/-- Transport: the ZMod φ̄-sum equals the Fin φ-sum. -/
lemma zmod_sum_eq_fin_sum (m : ℕ) [NeZero m] (hm : 2 ≤ m) (n : ZMod m → ℤ) :
    (∑ i, ∑ j, (n i * n j) * φbar m (j - i))
      = ∑ i : Fin m, ∑ j : Fin m,
        (n (((i.val : ℕ)) : ZMod m) * n (((j.val : ℕ)) : ZMod m))
          * phi m (dist m i.val j.val) := by
  have step : ∀ i : ZMod m,
      (∑ j, (n i * n j) * φbar m (j - i))
        = ∑ j : Fin m, (n i * n (((j.val : ℕ)) : ZMod m))
          * phi m (dist m i.val j.val) := by
    intro i
    have e := (Equiv.sum_comp (zmodFinEquiv m).symm
      (fun j : ZMod m => (n i * n j) * φbar m (j - i))).symm
    rw [e]
    apply Finset.sum_congr rfl
    intro j _
    show (n i * n (((j.val : ℕ)) : ZMod m))
          * φbar m ((((j.val : ℕ)) : ZMod m) - i)
        = (n i * n (((j.val : ℕ)) : ZMod m)) * phi m (dist m i.val j.val)
    have hdiff : ((((j.val : ℕ)) : ZMod m) - i)
        = ((((j.val : ℕ)) : ZMod m) - (((i.val : ℕ)) : ZMod m)) := by
      rw [ZMod.natCast_zmod_val i]
    rw [hdiff, φbar_cast_sub m hm i.val j.val (ZMod.val_lt i) j.isLt]
  rw [Finset.sum_congr rfl (fun i _ => step i)]
  have e := (Equiv.sum_comp (zmodFinEquiv m).symm
    (fun i : ZMod m => ∑ j : Fin m, (n i * n (((j.val : ℕ)) : ZMod m))
      * phi m (dist m i.val j.val))).symm
  rw [e]
  apply Finset.sum_congr rfl
  intro i _
  show (∑ j : Fin m, (n (((i.val : ℕ)) : ZMod m) * n (((j.val : ℕ)) : ZMod m))
      * phi m (dist m (((((i.val : ℕ)) : ZMod m)).val) j.val))
    = ∑ j : Fin m, (n (((i.val : ℕ)) : ZMod m) * n (((j.val : ℕ)) : ZMod m))
      * phi m (dist m i.val j.val)
  rw [ZMod.val_natCast_of_lt i.isLt]

lemma Hinv_mulVec_apply (m : ℕ) [NeZero m] (hm : 2 ≤ m) (n : ZMod m → ℝ)
    (i : ZMod m) :
    (Hinv m hm *ᵥ n) i = ((Dm m : ℝ))⁻¹ * ∑ j, (φbar m (j - i) : ℝ) * n j := by
  unfold Hinv
  rw [smul_mulVec]
  simp only [Pi.smul_apply, smul_eq_mul, Matrix.mulVec_apply_eq_sum, XphiR_apply]

lemma zmodFinEquiv_cast (m : ℕ) [NeZero m] (i : Fin m) :
    zmodFinEquiv m (((i.val : ℕ)) : ZMod m) = i := by
  apply Fin.ext
  show (((((i.val : ℕ)) : ZMod m)).val) = i.val
  exact ZMod.val_natCast_of_lt i.isLt

/-- The m = 1 case of the Q-bounds, by direct computation. -/
lemma Q_bound_one (n : Fin 1 → ℤ) :
    0 ≤ (Qnum 1 n : ℝ) / (Dm 1 : ℝ)
      ∧ (Qnum 1 n : ℝ) / (Dm 1 : ℝ) ≤ (∑ i, (n i : ℝ) ^ 2) / 2 := by
  have hNmZ : NmZ 1 n = (n 0) ^ 2 := by
    simp only [NmZ, Fin.sum_univ_one]
    have e1 : Derand.dist 1 (0 : Fin 1).val (0 : Fin 1).val = 0 := rfl
    rw [e1]
    have e2 : pellX 0 = 1 := rfl
    rw [e2]
    ring
  have hbeta : beta 1 n = 0 := by
    simp only [beta, Fin.sum_univ_one]
    have e1 : Derand.dist 1 (0 : Fin 1).val (0 : Fin 1).val = 0 := rfl
    rw [e1]
    have e3 : pellY 0 = 0 := rfl
    rw [e3]
    simp
  have hQ : Qnum 1 n = 2 * (n 0) ^ 2 := by
    have e4 : pellY 1 = 1 := rfl
    have e5 : Dm 1 = 4 := rfl
    simp only [Qnum, hNmZ, hbeta, e4, e5]
    ring
  have hDm : Dm 1 = 4 := rfl
  have hnorm : (∑ i, (n i : ℝ) ^ 2) = (n 0 : ℝ) ^ 2 := Fin.sum_univ_one _
  rw [hQ, hDm, hnorm]
  push_cast
  constructor
  · exact div_nonneg (by positivity) (by norm_num)
  · exact le_of_eq (by ring)

/-- The Q-bounds, m ≥ 2, via the matrix form. -/
lemma Q_bound_ge_two (m : ℕ) [NeZero m] (hm : 2 ≤ m) (n : Fin m → ℤ) :
    0 ≤ (Qnum m n : ℝ) / (Dm m : ℝ)
      ∧ (Qnum m n : ℝ) / (Dm m : ℝ) ≤ (∑ i, (n i : ℝ) ^ 2) / 2 := by
  have hDne : (Dm m : ℝ) ≠ 0 := Dm_real_ne_zero m (by omega : 1 ≤ m)
  set nZ : ZMod m → ℤ := fun r => n (zmodFinEquiv m r) with hnZ
  set nR : ZMod m → ℝ := fun r => (nZ r : ℝ) with hnR
  -- Step A: the quadratic form equals Qnum / (2D).
  have hform : nR ⬝ᵥ (Hinv m hm *ᵥ nR)
      = ((Dm m : ℝ))⁻¹ * ((Qnum m n : ℝ) / 2) := by
    have hdot : nR ⬝ᵥ (Hinv m hm *ᵥ nR)
        = ((Dm m : ℝ))⁻¹ * ∑ i, ∑ j, (nR i * nR j) * (φbar m (j - i) : ℝ) := by
      rw [dotProduct]
      simp only [Hinv_mulVec_apply]
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro i _
      simp only [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro j _
      ring
    rw [hdot]
    congr 1
    have hS : (∑ i, ∑ j, (nR i * nR j) * (φbar m (j - i) : ℝ))
        = ((Qnum m n : ℝ) / 2) := by
      have hcast : (∑ i, ∑ j, (nR i * nR j) * (φbar m (j - i) : ℝ))
          = ((∑ i, ∑ j, (nZ i * nZ j) * φbar m (j - i) : ℤ) : ℝ) := by
        push_cast
        apply Finset.sum_congr rfl
        intro i _
        apply Finset.sum_congr rfl
        intro j _
        simp [hnR]
      rw [hcast, zmod_sum_eq_fin_sum m hm nZ]
      have hcast2 : (∑ i : Fin m, ∑ j : Fin m,
            (nZ (((i.val : ℕ)) : ZMod m) * nZ (((j.val : ℕ)) : ZMod m))
              * phi m (dist m i.val j.val))
          = ∑ i, ∑ j, (n i * n j) * phi m (dist m (i : ℕ) (j : ℕ)) := by
        apply Finset.sum_congr rfl
        intro i _
        apply Finset.sum_congr rfl
        intro j _
        simp only [hnZ, zmodFinEquiv_cast]
      rw [hcast2]
      have hq := quadId m n
      have hqR : ((2 * (∑ i, ∑ j, (n i * n j) * phi m (dist m (i : ℕ) (j : ℕ))) : ℤ) : ℝ)
          = (Qnum m n : ℝ) := by exact_mod_cast hq
      push_cast at hqR
      push_cast
      linarith
    exact hS
  -- Step B: Q = 2 * (quadratic form).
  have hQ : (Qnum m n : ℝ) / (Dm m : ℝ) = 2 * (nR ⬝ᵥ (Hinv m hm *ᵥ nR)) := by
    rw [hform]
    field_simp
  -- Step C: lower bound.
  have hpos : 0 ≤ nR ⬝ᵥ (Hinv m hm *ᵥ nR) := quad_nonneg m hm nR
  -- Step D: upper bound via the H-expansion.
  set u := Hinv m hm *ᵥ nR with hu
  have hHu : Bgs.LineD.Defs.Hmat m ℝ *ᵥ u = nR := by
    rw [hu, Matrix.mulVec_mulVec, Hmat_mul_Hinv, Matrix.one_mulVec]
  have hquad : nR ⬝ᵥ u = u ⬝ᵥ (Bgs.LineD.Defs.Hmat m ℝ *ᵥ u) := by
    rw [hHu, dotProduct_comm]
  have hdotH := Bgs.LineD.Defs.Hmat_dotProduct m u
  -- d_i = u_{i+1} - u_i
  set d : ZMod m → ℝ := fun i => u (i + 1) - u i with hd
  have hHapply : ∀ i, (Bgs.LineD.Defs.Hmat m ℝ *ᵥ u) i = 4 * u i - d i + d (i - 1) := by
    intro i
    rw [Hmat_mulVec_apply]
    have e1 : u (i + 1) = u i + d i := by simp [hd]
    have e2 : u (i - 1) = u i - d (i - 1) := by
      have : d (i - 1) = u ((i - 1) + 1) - u (i - 1) := rfl
      rw [sub_add_cancel] at this
      linarith
    rw [e1, e2]
    ring
  have hnorm2 : (∑ i, ((Bgs.LineD.Defs.Hmat m ℝ *ᵥ u) i) ^ 2)
      = 16 * (∑ i, (u i) ^ 2) + (∑ i, (d (i - 1) - d i) ^ 2)
        + 8 * (∑ i, u i * (d (i - 1) - d i)) := by
    have hexp : ∀ i, ((Bgs.LineD.Defs.Hmat m ℝ *ᵥ u) i) ^ 2
        = 16 * (u i) ^ 2 + (d (i - 1) - d i) ^ 2 + 8 * (u i * (d (i - 1) - d i)) := by
      intro i
      rw [hHapply]
      ring
    rw [Finset.sum_congr rfl (fun i _ => hexp i), Finset.sum_add_distrib,
      Finset.sum_add_distrib, ← Finset.mul_sum, ← Finset.mul_sum]
  have hshift : (∑ i, u i * d (i - 1)) = ∑ i, u (i + 1) * d i := by
    have e := Bgs.LineD.Defs.sum_subOne m (fun j => u (j + 1) * d j)
    -- e : ∑ i, (fun j => u (j+1) * d j) (i - 1) = ∑ i, u (i+1) * d i
    have econgr : (∑ i, (fun j => u (j + 1) * d j) (i - 1)) = ∑ i, u i * d (i - 1) := by
      apply Finset.sum_congr rfl
      intro i _
      show u ((i - 1) + 1) * d (i - 1) = u i * d (i - 1)
      rw [sub_add_cancel]
    rw [econgr] at e
    exact e
  have hsumd : (∑ i, u i * (d (i - 1) - d i)) = ∑ i, (d i) ^ 2 := by
    have h1 : (∑ i, u i * (d (i - 1) - d i))
        = (∑ i, u i * d (i - 1)) - (∑ i, u i * d i) := by
      rw [← Finset.sum_sub_distrib]
      apply Finset.sum_congr rfl
      intro i _
      ring
    rw [h1, hshift, ← Finset.sum_sub_distrib]
    apply Finset.sum_congr rfl
    intro i _
    have : u (i + 1) * d i - u i * d i = (d i) ^ 2 := by simp [hd]; ring
    exact this
  have hdotH2 : u ⬝ᵥ (Bgs.LineD.Defs.Hmat m ℝ *ᵥ u)
      = 4 * (∑ i, (u i) ^ 2) + ∑ i, (d i) ^ 2 := by
    rw [hdotH]
    have e1 : (∑ i, u i * u i) = ∑ i, (u i) ^ 2 := by
      apply Finset.sum_congr rfl
      intro i _
      ring
    have e2 : (∑ i, (u i - u (i + 1)) * (u i - u (i + 1))) = ∑ i, (d i) ^ 2 := by
      apply Finset.sum_congr rfl
      intro i _
      have h : u i - u (i + 1) = -(d i) := by simp [hd]
      rw [h]
      ring
    rw [e1, e2]
  have hnormnR : (∑ i, (nR i) ^ 2) = ∑ i, (n i : ℝ) ^ 2 := by
    have e := (Equiv.sum_comp (zmodFinEquiv m).symm (fun r : ZMod m => (nR r) ^ 2)).symm
    rw [e]
    apply Finset.sum_congr rfl
    intro i _
    show ((nZ (((i.val : ℕ)) : ZMod m) : ℝ)) ^ 2 = (n i : ℝ) ^ 2
    rw [hnZ]
    simp [zmodFinEquiv_cast]
  have hkey : (∑ i, ((Bgs.LineD.Defs.Hmat m ℝ *ᵥ u) i) ^ 2)
      - 4 * (u ⬝ᵥ (Bgs.LineD.Defs.Hmat m ℝ *ᵥ u))
      = (∑ i, (d (i - 1) - d i) ^ 2) + 4 * (∑ i, (d i) ^ 2) := by
    rw [hnorm2, hdotH2, hsumd]
    ring
  have hnonneg : 0 ≤ (∑ i, (d (i - 1) - d i) ^ 2) + 4 * (∑ i, (d i) ^ 2) := by
    apply add_nonneg
    · exact Finset.sum_nonneg fun i _ => sq_nonneg _
    · exact mul_nonneg (by norm_num) (Finset.sum_nonneg fun i _ => sq_nonneg _)
  have hnormHu : (∑ i, ((Bgs.LineD.Defs.Hmat m ℝ *ᵥ u) i) ^ 2) = ∑ i, (n i : ℝ) ^ 2 := by
    have hpt : ∀ i, ((Bgs.LineD.Defs.Hmat m ℝ *ᵥ u) i) ^ 2 = (nR i) ^ 2 := by
      intro i
      rw [hHu]
    rw [Finset.sum_congr rfl (fun i _ => hpt i), hnormnR]
  have hub : 2 * (u ⬝ᵥ (Bgs.LineD.Defs.Hmat m ℝ *ᵥ u)) ≤ (∑ i, (n i : ℝ) ^ 2) / 2 := by
    have hle : 4 * (u ⬝ᵥ (Bgs.LineD.Defs.Hmat m ℝ *ᵥ u)) ≤ ∑ i, (n i : ℝ) ^ 2 := by
      rw [← hnormHu]
      linarith [hnonneg, hkey]
    linarith
  rw [hQ, hquad]
  exact ⟨by linarith, hub⟩

/-- The Q-bounds for all m ≥ 1: 0 ≤ Q(n) ≤ ‖n‖²/2. -/
lemma Q_bound (m : ℕ) (hm : 1 ≤ m) (n : Fin m → ℤ) :
    0 ≤ (Qnum m n : ℝ) / (Dm m : ℝ)
      ∧ (Qnum m n : ℝ) / (Dm m : ℝ) ≤ (∑ i, (n i : ℝ) ^ 2) / 2 := by
  rcases eq_or_lt_of_le hm with h1 | h2
  · subst h1
    exact Q_bound_one n
  · haveI : NeZero m := ⟨by omega⟩
    exact Q_bound_ge_two m h2 n

/- §5. The phase factor e(t) = exp (2πi t) and reciprocity. -/

/-- The phase factor `e(t) = exp (2πi t)`. -/
noncomputable def e (t : ℝ) : ℂ := Complex.exp (2 * Real.pi * Complex.I * t)

lemma e_add (s t : ℝ) : e (s + t) = e s * e t := by
  unfold e
  rw [Complex.ofReal_add, mul_add, Complex.exp_add]

lemma e_int (k : ℤ) : e (k : ℝ) = 1 := by
  unfold e
  rw [show 2 * Real.pi * Complex.I * ((k : ℝ) : ℂ)
      = (k : ℂ) * (2 * Real.pi * Complex.I) by push_cast; ring]
  exact Complex.exp_int_mul_two_pi_mul_I k

/-- Reciprocity of modular inverses (source §3): if `a` inverts `d` mod `n` and
    `b` inverts `n` mod `d`, then `a·d + b·n - 1` is divisible by `d·n`.
    In particular `a/n + b/d - 1/(dn)` is an integer. -/
lemma reciprocity (d n : ℕ) (hcop : Nat.Coprime d n)
    (a b : ℕ) (ha : ((d * a : ℕ) : ZMod n) = 1) (hb : ((n * b : ℕ) : ZMod d) = 1) :
    ∃ t : ℤ, (a : ℤ) * (d : ℤ) + (b : ℤ) * (n : ℤ) - 1
      = (d : ℤ) * (n : ℤ) * t := by
  have hDd : (d : ℤ) ∣ (a : ℤ) * (d : ℤ) + (b : ℤ) * (n : ℤ) - 1 := by
    rw [← ZMod.intCast_zmod_eq_zero_iff_dvd]
    have hb' : (b : ZMod d) * (n : ZMod d) = 1 := by
      have h := hb
      rw [Nat.cast_mul, mul_comm] at h
      exact h
    rw [Int.cast_sub, Int.cast_add, Int.cast_mul, Int.cast_mul, Int.cast_one,
      Int.cast_natCast, Int.cast_natCast, Int.cast_natCast, Int.cast_natCast,
      ZMod.natCast_self, mul_zero, zero_add, hb']
    simp
  have hNd : (n : ℤ) ∣ (a : ℤ) * (d : ℤ) + (b : ℤ) * (n : ℤ) - 1 := by
    rw [← ZMod.intCast_zmod_eq_zero_iff_dvd]
    have ha' : (a : ZMod n) * (d : ZMod n) = 1 := by
      have h := ha
      rw [Nat.cast_mul, mul_comm] at h
      exact h
    rw [Int.cast_sub, Int.cast_add, Int.cast_mul, Int.cast_mul, Int.cast_one,
      Int.cast_natCast, Int.cast_natCast, Int.cast_natCast, Int.cast_natCast,
      ZMod.natCast_self, mul_zero, add_zero, ha']
    simp
  have hcopZ : IsCoprime (d : ℤ) (n : ℤ) := hcop.isCoprime
  exact hcopZ.mul_dvd hDd hNd

/-- The phase identity of Theorem 1(a) (source §3): the modular-inverse phase
    `r·a/n` splits into the rational phase `r/(dn)` and the residue phase
    `-ν·y'·Nm/g'`, up to an integer (which `e` kills). Here `r = 2y·Nm + d·β`
    is the numerator of `Q` (see `quadId`), `2y/d = y'/g'` is the reduced Pell
    ratio (see `two_y_over_D`), and `ν = b % g'`. -/
lemma phase_identity (d n g' yp' : ℕ) (hd : 1 ≤ d) (hn : 2 ≤ n)
    (hcop : Nat.Coprime d n) (hgpos : 0 < g')
    (a b : ℕ) (ha : ((d * a : ℕ) : ZMod n) = 1) (hb : ((n * b : ℕ) : ZMod d) = 1)
    (y Nm β : ℤ) (r : ℤ) (hr : r = 2 * y * Nm + (d : ℤ) * β)
    (h2y : (2 * (y : ℚ)) / (d : ℚ) = (yp' : ℚ) / (g' : ℚ)) :
    e ((r : ℚ) * (a : ℚ) / (n : ℚ) : ℝ)
      = e ((r : ℚ) / (d : ℚ) / (n : ℚ) : ℝ)
        * e (-((b % g' : ℕ) : ℚ) * (yp' : ℚ) * (Nm : ℚ) / (g' : ℚ) : ℝ) := by
  obtain ⟨t, ht⟩ := reciprocity d n hcop a b ha hb
  set s := b / g' with hs
  set ν := b % g' with hν
  have hdQ : (d : ℚ) ≠ 0 := by exact_mod_cast (ne_of_gt (by omega : 0 < d))
  have hnQ : (n : ℚ) ≠ 0 := by exact_mod_cast (ne_of_gt (by omega : 0 < n))
  have hgQ : (g' : ℚ) ≠ 0 := by exact_mod_cast (ne_of_gt hgpos)
  have H1 : (a : ℚ) * (d : ℚ) + (b : ℚ) * (n : ℚ) - 1
      = (d : ℚ) * (n : ℚ) * (t : ℚ) := by
    exact_mod_cast ht
  have H2 : 2 * (y : ℚ) * (g' : ℚ) = (yp' : ℚ) * (d : ℚ) := by
    rw [div_eq_div_iff hdQ hgQ] at h2y
    linear_combination h2y
  have H3 : (r : ℚ) = 2 * (y : ℚ) * (Nm : ℚ) + (d : ℚ) * (β : ℚ) := by
    exact_mod_cast hr
  have H4 : (b : ℚ) = (g' : ℚ) * (s : ℚ) + (ν : ℚ) := by
    have h := Nat.div_add_mod b g'
    rw [← hs, ← hν] at h
    have hQ : ((g' * s + ν : ℕ) : ℚ) = (b : ℚ) := by exact_mod_cast h
    push_cast at hQ
    linarith [hQ]
  have hW : (r : ℚ) * (a : ℚ) / (n : ℚ) - (r : ℚ) / (d : ℚ) / (n : ℚ)
      - ((-(ν : ℚ)) * (yp' : ℚ) * (Nm : ℚ) / (g' : ℚ))
      = (r : ℚ) * (t : ℚ) - (yp' : ℚ) * (Nm : ℚ) * (s : ℚ)
        - (β : ℚ) * (b : ℚ) := by
    field_simp
    linear_combination (r : ℚ) * (g' : ℚ) * H1
      - ((g' : ℚ) * (b : ℚ) * (n : ℚ)) * H3
      - (2 * (y : ℚ) * (Nm : ℚ) * (g' : ℚ) * (n : ℚ)) * H4
      - ((Nm : ℚ) * (n : ℚ) * (g' : ℚ) * (s : ℚ)
        + (Nm : ℚ) * (n : ℚ) * (ν : ℚ)) * H2
  have hsum : (r : ℚ) * (a : ℚ) / (n : ℚ)
      = (r : ℚ) / (d : ℚ) / (n : ℚ)
        + ((-(ν : ℚ)) * (yp' : ℚ) * (Nm : ℚ) / (g' : ℚ))
        + ((r * t - (yp' : ℤ) * Nm * (s : ℤ) - β * (b : ℤ) : ℤ) : ℚ) := by
    have hWQ : ((r * t - (yp' : ℤ) * Nm * (s : ℤ) - β * (b : ℤ) : ℤ) : ℚ)
        = (r : ℚ) * (t : ℚ) - (yp' : ℚ) * (Nm : ℚ) * (s : ℚ)
          - (β : ℚ) * (b : ℚ) := by
      push_cast
      ring
    rw [hWQ]
    linarith [hW]
  have hR : ((r : ℚ) * (a : ℚ) / (n : ℚ) : ℝ)
      = ((r : ℚ) / (d : ℚ) / (n : ℚ) : ℝ)
        + ((-(ν : ℚ)) * (yp' : ℚ) * (Nm : ℚ) / (g' : ℚ) : ℝ)
        + ((r * t - (yp' : ℤ) * Nm * (s : ℤ) - β * (b : ℤ) : ℤ) : ℝ) := by
    exact_mod_cast hsum
  rw [hR, e_add, e_add, e_int, mul_one]

/-- |sin x| ≤ |x|, via the mean value theorem. (Not in Mathlib 4.33.1.) -/
lemma abs_sin_le_abs (x : ℝ) : |Real.sin x| ≤ |x| := by
  have hpos : ∀ y : ℝ, 0 ≤ y → |Real.sin y| ≤ y := by
    intro y hy
    rcases eq_or_lt_of_le hy with h0 | hpos
    · subst h0
      simp
    · obtain ⟨c, _, hceq⟩ := exists_hasDerivAt_eq_slope Real.sin Real.cos hpos
        Real.continuous_sin.continuousOn (fun z _ => Real.hasDerivAt_sin z)
      rw [Real.sin_zero, sub_zero, sub_zero] at hceq
      have hsin : Real.sin y = Real.cos c * y := by
        rw [eq_div_iff (ne_of_gt hpos)] at hceq
        exact hceq.symm
      rw [hsin, abs_mul, abs_of_nonneg hy]
      calc |Real.cos c| * y ≤ 1 * y :=
            mul_le_mul_of_nonneg_right (Real.abs_cos_le_one c) hy
        _ = y := one_mul y
  rcases le_total 0 x with hx | hx
  · rw [abs_of_nonneg hx]
    exact hpos x hx
  · rw [abs_of_nonpos hx]
    have h := hpos (-x) (by linarith)
    rwa [Real.sin_neg, abs_neg] at h

/-- The modulus of `exp (θ·i) - 1` is `2|sin (θ/2)|`. -/
lemma exp_I_sub_one_abs (θ : ℝ) :
    ‖Complex.exp ((θ : ℂ) * Complex.I) - 1‖
      = 2 * |Real.sin (θ / 2)| := by
  have hfac : Complex.exp ((θ : ℂ) * Complex.I) - 1
      = Complex.exp (((θ / 2 : ℝ) : ℂ) * Complex.I)
        * (Complex.exp (((θ / 2 : ℝ) : ℂ) * Complex.I)
          - Complex.exp (((-(θ / 2) : ℝ) : ℂ) * Complex.I)) := by
    rw [mul_sub, ← Complex.exp_add, ← Complex.exp_add]
    congr 1
    · congr 1
      push_cast
      ring
    · rw [show (((θ / 2 : ℝ) : ℂ) * Complex.I + ((-(θ / 2) : ℝ) : ℂ) * Complex.I) = 0
          by push_cast; ring]
      exact Complex.exp_zero.symm
  have hdiff : Complex.exp (((θ / 2 : ℝ) : ℂ) * Complex.I)
      - Complex.exp (((-(θ / 2) : ℝ) : ℂ) * Complex.I)
      = ((2 * Real.sin (θ / 2) : ℝ) : ℂ) * Complex.I := by
    apply Complex.ext
    · rw [Complex.sub_re, Complex.exp_ofReal_mul_I_re, Complex.exp_ofReal_mul_I_re,
        Complex.mul_I_re, Complex.ofReal_im, neg_zero, Real.cos_neg, sub_self]
    · rw [Complex.sub_im, Complex.exp_ofReal_mul_I_im, Complex.exp_ofReal_mul_I_im,
        Complex.mul_I_im, Complex.ofReal_re, Real.sin_neg]
      ring
  rw [hfac, norm_mul, hdiff, Complex.norm_exp_ofReal_mul_I, norm_mul,
    Complex.norm_I, Complex.norm_real, mul_one, one_mul, Real.norm_eq_abs, abs_mul,
    abs_of_nonneg (show (0 : ℝ) ≤ 2 by norm_num)]

/-- The phase estimate of Theorem 1(c) (source §3): |e(t) - 1| ≤ 2π|t|. -/
lemma e_sub_one_le (t : ℝ) : ‖e t - 1‖ ≤ 2 * Real.pi * |t| := by
  have hθ : e t = Complex.exp (((2 * Real.pi * t : ℝ) : ℂ) * Complex.I) := by
    unfold e
    congr 1
    push_cast
    ring
  rw [hθ, exp_I_sub_one_abs]
  have h2 : (2 * Real.pi * t) / 2 = Real.pi * t := by ring
  rw [h2]
  have hs := abs_sin_le_abs (Real.pi * t)
  rw [abs_mul, abs_of_nonneg Real.pi_nonneg] at hs
  linarith [hs]

/- §6. Theorem 1 as a finite-sum theorem, from the Gauss-sum hypothesis. -/

/-- Inverses mod `n` exist for units: if `gcd (d, n) = 1`, some `a` inverts
    `d` mod `n`. (Used to instantiate `a` and `b` in `trace_formula_finite`.) -/
lemma exists_inv_mod (d n : ℕ) (hcop : Nat.Coprime d n) :
    ∃ a : ℕ, ((d * a : ℕ) : ZMod n) = 1 := by
  rcases Nat.eq_zero_or_pos n with hn | hn
  · subst hn
    rw [Nat.coprime_zero_right] at hcop
    subst hcop
    refine ⟨1, ?_⟩
    show ((1 : ℕ) : ℤ) = 1
    simp
  · haveI : NeZero n := ⟨by omega⟩
    refine ⟨(ZMod.unitOfCoprime d hcop)⁻¹.val.val, ?_⟩
    rw [Nat.cast_mul, ZMod.natCast_zmod_val, ← ZMod.coe_unitOfCoprime d hcop,
      ← Units.val_mul]
    simp

/-- Theorem 1(a) + (b) of the source (§3), finite-sum form: assuming the
    Gauss-sum step `hGauss` (the trace equals `TrM` times the Fourier sum
    with the modular phase `r·a/N`, where `a` inverts `D_m` mod `N`) and
    `|TrM| = 1`, the trace equals `TrM` times the sum with the rational
    phase `Q(n)/N` and the residue phase `-ν·y′·Nm/g′`, where `ν = b % g′`
    for `b` inverting `N` mod `D_m`. The Gauss-sum step itself (Fourier
    expansion, Gaussian evaluation, CRT) is the hypothesis `hGauss`; the
    reciprocity step — the new content of the source — is proved here via
    `phase_identity`, `quadId` and `two_y_over_D`. The passage from finite
    sums to the absolutely convergent sum over `ℤ^m` is NOT proved here. -/
lemma trace_formula_finite (m N : ℕ) (hm : 1 ≤ m) (hN : 2 ≤ N)
    (hcop : Nat.Coprime (Dm m).toNat N)
    (a b : ℕ) (ha : (((Dm m).toNat * a : ℕ) : ZMod N) = 1)
    (hb : ((N * b : ℕ) : ZMod (Dm m).toNat) = 1)
    (Φ : (Fin m → ℤ) → ℂ) (TrM Tr : ℂ)
    (S : Finset (Fin m → ℤ))
    (hGauss : Tr = TrM * ∑ n ∈ S, Φ n * e ((Qnum m n : ℚ) * (a : ℚ) / (N : ℚ) : ℝ))
    (hMod : ‖TrM‖ = 1) :
    Tr = TrM * ∑ n ∈ S, Φ n * (e ((Qnum m n : ℚ) / (Dm m : ℚ) / (N : ℚ) : ℝ)
      * e (-((b % gp m : ℕ) : ℚ) * (yp m : ℚ) * (NmZ m n : ℚ) / (gp m : ℚ) : ℝ))
      ∧ ‖TrM‖ = 1 := by
  have hDmnn : 0 ≤ Dm m := by
    have h := pellX_pos m
    show 0 ≤ 2 * (pellX m - 1)
    linarith
  have hDmZ : (((Dm m).toNat : ℕ) : ℤ) = Dm m := Int.toNat_of_nonneg hDmnn
  have hDmQ : (((Dm m).toNat : ℕ) : ℚ) = (Dm m : ℚ) := by exact_mod_cast hDmZ
  have hDm4 : 4 ≤ Dm m := by
    have h := pellX_ge_three m hm
    show 4 ≤ 2 * (pellX m - 1)
    linarith
  have hDpos : 1 ≤ (Dm m).toNat := by omega
  have hgppos : 0 < gp m := Nat.pos_of_dvd_of_pos (gp_dvd_D m hm) (by omega)
  refine ⟨?_, hMod⟩
  rw [hGauss]
  congr 1
  apply Finset.sum_congr rfl
  intro n _
  have hr : Qnum m n
      = 2 * (pellY m : ℤ) * (NmZ m n) + (((Dm m).toNat : ℕ) : ℤ) * (beta m n) := by
    show 2 * pellY m * NmZ m n + Dm m * beta m n
      = 2 * (pellY m : ℤ) * (NmZ m n) + (((Dm m).toNat : ℕ) : ℤ) * (beta m n)
    rw [hDmZ]
  have h2yQ : (2 * (pellY m : ℚ)) / (((Dm m).toNat : ℕ) : ℚ)
      = (yp m : ℚ) / (gp m : ℚ) := by
    rw [hDmQ]
    exact two_y_over_D m hm
  rw [phase_identity (Dm m).toNat N (gp m) (yp m) hDpos hN hcop hgppos a b ha hb
    (pellY m) (NmZ m n) (beta m n) (Qnum m n) hr h2yQ, hDmQ]

/-- |e(t)| = 1. -/
lemma e_norm_one (t : ℝ) : ‖e t‖ = 1 := by
  have hθ : e t = Complex.exp (((2 * Real.pi * t : ℝ) : ℂ) * Complex.I) := by
    unfold e
    congr 1
    push_cast
    ring
  rw [hθ, Complex.norm_exp_ofReal_mul_I]

/-- Key moment factorization: on a product set, the weighted second moment
    splits into one `k²`-factor and `m - 1` plain factors. -/
lemma moment_key (T : Finset ℤ) (f : ℤ → ℝ) (m : ℕ) (j : Fin m) :
    ∑ n ∈ Fintype.piFinset (fun _ : Fin m => T), (∏ i, f (n i)) * ((n j : ℝ)) ^ 2
    = (∑ k ∈ T, ((k : ℝ)) ^ 2 * f k) * (∑ k ∈ T, f k) ^ (m - 1) := by
  classical
  set g : Fin m → ℤ → ℝ := fun i k => if i = j then ((k : ℝ)) ^ 2 * f k else f k with hg
  have hprod : ∀ n : Fin m → ℤ,
      (∏ i, g i (n i)) = (∏ i, f (n i)) * ((n j : ℝ)) ^ 2 := by
    intro n
    rw [Finset.prod_eq_mul_prod_sdiff_singleton_of_mem (Finset.mem_univ j) _]
    have hj : g j (n j) = ((n j : ℝ)) ^ 2 * f (n j) := by simp [hg]
    have hrest : ∏ i ∈ Finset.univ \ {j}, g i (n i)
        = ∏ i ∈ Finset.univ \ {j}, f (n i) := by
      apply Finset.prod_congr rfl
      intro i hi
      have hij : i ≠ j := by simpa using (Finset.mem_sdiff.mp hi).2
      simp [hg, hij]
    rw [hj, hrest, Finset.prod_eq_mul_prod_sdiff_singleton_of_mem (Finset.mem_univ j) _]
    ring
  have hsum : (∑ n ∈ Fintype.piFinset (fun _ : Fin m => T),
        (∏ i, f (n i)) * ((n j : ℝ)) ^ 2)
      = ∑ n ∈ Fintype.piFinset (fun _ : Fin m => T), ∏ i, g i (n i) := by
    apply Finset.sum_congr rfl
    intro n _
    exact (hprod n).symm
  rw [hsum, Finset.sum_prod_piFinset,
    Finset.prod_eq_mul_prod_sdiff_singleton_of_mem (Finset.mem_univ j) _]
  have hgj : (∑ k ∈ T, g j k) = ∑ k ∈ T, ((k : ℝ)) ^ 2 * f k := by
    apply Finset.sum_congr rfl
    intro k _
    simp [hg]
  rw [hgj]
  have hgrest : ∏ i ∈ Finset.univ \ {j}, (∑ k ∈ T, g i k)
      = ∏ i ∈ Finset.univ \ {j}, (∑ k ∈ T, f k) := by
    apply Finset.prod_congr rfl
    intro i hi
    have hij : i ≠ j := by simpa using (Finset.mem_sdiff.mp hi).2
    apply Finset.sum_congr rfl
    intro k _
    simp [hg, hij]
  rw [hgrest, Finset.prod_const, Finset.card_sdiff, Finset.inter_univ,
    Finset.card_univ, Fintype.card_fin, Finset.card_singleton]

/-- The moment identity: on a product set, the weighted second moment is
    `m · s2 · s0^(m-1)`. -/
lemma moment_prod (T : Finset ℤ) (f : ℤ → ℝ) (m : ℕ) :
    ∑ n ∈ Fintype.piFinset (fun _ : Fin m => T), (∏ j, f (n j)) * (∑ j, ((n j : ℝ)) ^ 2)
    = (m : ℝ) * (∑ k ∈ T, ((k : ℝ)) ^ 2 * f k) * (∑ k ∈ T, f k) ^ (m - 1) := by
  classical
  have hswap : (∑ n ∈ Fintype.piFinset (fun _ : Fin m => T),
        (∏ j, f (n j)) * (∑ j, ((n j : ℝ)) ^ 2))
      = ∑ j : Fin m, ∑ n ∈ Fintype.piFinset (fun _ : Fin m => T),
        (∏ i, f (n i)) * ((n j : ℝ)) ^ 2 := by
    have hbody : ∀ n : Fin m → ℤ, (∏ j, f (n j)) * (∑ j, ((n j : ℝ)) ^ 2)
        = ∑ j, (∏ i, f (n i)) * ((n j : ℝ)) ^ 2 := by
      intro n
      rw [Finset.mul_sum]
    rw [Finset.sum_congr rfl (fun n _ => hbody n), Finset.sum_comm]
  rw [hswap]
  simp only [moment_key]
  rw [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
  ring

/-- Theorem 1(c) of the source (§3), finite-sum form: replacing the rational
    phase `e(Q(n)/N)` by `1` in the Fourier sum costs at most
    `π·m·s2·s0^(m-1)/N`, where `s0, s2` are the weight moments on the finite
    support `T`. Here `Φ` is bounded by the product weight `∏ f` and `Ψ`
    is any unit-modulus phase (the residue phase in the application). -/
lemma trace_error_finite (m N : ℕ) (hm : 1 ≤ m) (hN : 1 ≤ N)
    (Φ : (Fin m → ℤ) → ℂ) (Ψ : (Fin m → ℤ) → ℂ) (f : ℤ → ℝ)
    (hΨ : ∀ n, ‖Ψ n‖ = 1)
    (hf : ∀ n, ‖Φ n‖ ≤ ∏ j, f (n j))
    (T : Finset ℤ) (S : Finset (Fin m → ℤ))
    (hS : S = Fintype.piFinset (fun _ : Fin m => T)) :
    ‖∑ n ∈ S, Φ n * (e ((Qnum m n : ℚ) / (Dm m : ℚ) / (N : ℚ) : ℝ) * Ψ n)
      - ∑ n ∈ S, Φ n * Ψ n‖
      ≤ Real.pi * (m : ℝ) * (∑ k ∈ T, ((k : ℝ)) ^ 2 * f k)
        * (∑ k ∈ T, f k) ^ (m - 1) / (N : ℝ) := by
  have hNpos : (0 : ℝ) < (N : ℝ) := by exact_mod_cast hN
  subst hS
  rw [← Finset.sum_sub_distrib]
  calc ‖∑ n ∈ Fintype.piFinset (fun _ : Fin m => T),
        (Φ n * (e ((Qnum m n : ℚ) / (Dm m : ℚ) / (N : ℚ) : ℝ) * Ψ n) - Φ n * Ψ n)‖
      ≤ ∑ n ∈ Fintype.piFinset (fun _ : Fin m => T),
        ‖Φ n * (e ((Qnum m n : ℚ) / (Dm m : ℚ) / (N : ℚ) : ℝ) * Ψ n) - Φ n * Ψ n‖ :=
        norm_sum_le _ _
    _ ≤ ∑ n ∈ Fintype.piFinset (fun _ : Fin m => T),
        (∏ j, f (n j)) * (Real.pi * (∑ j, ((n j : ℝ)) ^ 2) / (N : ℝ)) := by
        apply Finset.sum_le_sum
        intro n _
        have heq : Φ n * (e ((Qnum m n : ℚ) / (Dm m : ℚ) / (N : ℚ) : ℝ) * Ψ n)
            - Φ n * Ψ n
            = (Φ n * Ψ n) * (e ((Qnum m n : ℚ) / (Dm m : ℚ) / (N : ℚ) : ℝ) - 1) := by
          ring
        rw [heq, norm_mul, norm_mul, hΨ n, mul_one]
        have hQ := Q_bound m hm n
        have hphase := e_sub_one_le
          (((Qnum m n : ℚ) / (Dm m : ℚ) / (N : ℚ) : ℚ) : ℝ)
        have ht : (((Qnum m n : ℚ) / (Dm m : ℚ) / (N : ℚ) : ℚ) : ℝ)
            = (Qnum m n : ℝ) / (Dm m : ℝ) / (N : ℝ) := by
          rw [Rat.cast_div, Rat.cast_div, Rat.cast_intCast, Rat.cast_intCast,
            Rat.cast_natCast]
        rw [ht] at hphase
        have hNpos : (0 : ℝ) < (N : ℝ) := by exact_mod_cast hN
        have hDmposR : (0 : ℝ) < (Dm m : ℝ) := by
          have h4 : 4 ≤ Dm m := by
            have h := pellX_ge_three m hm
            show 4 ≤ 2 * (pellX m - 1)
            linarith
          exact_mod_cast (by linarith : 0 < Dm m)
        have hQnum : (0 : ℝ) ≤ (Qnum m n : ℝ) := by
          have h1 : (Qnum m n : ℝ)
              = ((Qnum m n : ℝ) / (Dm m : ℝ)) * (Dm m : ℝ) :=
            (div_mul_cancel₀ _ (ne_of_gt hDmposR)).symm
          rw [h1]
          exact mul_nonneg hQ.1 (le_of_lt hDmposR)
        have hNQ : (0 : ℝ) ≤ (Qnum m n : ℝ) / (Dm m : ℝ) / (N : ℝ) :=
          div_nonneg (div_nonneg hQnum (le_of_lt hDmposR)) (le_of_lt hNpos)
        rw [abs_of_nonneg hNQ] at hphase
        have hle : 2 * Real.pi * ((Qnum m n : ℝ) / (Dm m : ℝ) / (N : ℝ))
            ≤ Real.pi * (∑ j, ((n j : ℝ)) ^ 2) / (N : ℝ) := by
          have h2Q : 2 * ((Qnum m n : ℝ) / (Dm m : ℝ)) ≤ ∑ j, ((n j : ℝ)) ^ 2 := by
            linarith [hQ.2]
          have hform : 2 * Real.pi * ((Qnum m n : ℝ) / (Dm m : ℝ) / (N : ℝ))
              = Real.pi * (2 * ((Qnum m n : ℝ) / (Dm m : ℝ))) / (N : ℝ) := by
            field_simp
          rw [hform]
          exact div_le_div_of_nonneg_right
            (mul_le_mul_of_nonneg_left h2Q (le_of_lt Real.pi_pos)) (le_of_lt hNpos)
        calc ‖Φ n‖ * ‖e ((Qnum m n : ℚ) / (Dm m : ℚ) / (N : ℚ) : ℝ) - 1‖
            ≤ (∏ j, f (n j)) * (2 * Real.pi * ((Qnum m n : ℝ) / (Dm m : ℝ) / (N : ℝ))) :=
              mul_le_mul (hf n) hphase (norm_nonneg _)
                (le_trans (norm_nonneg _) (hf n))
          _ ≤ (∏ j, f (n j)) * (Real.pi * (∑ j, ((n j : ℝ)) ^ 2) / (N : ℝ)) :=
              mul_le_mul_of_nonneg_left hle (le_trans (norm_nonneg _) (hf n))
    _ = Real.pi * (m : ℝ) * (∑ k ∈ T, ((k : ℝ)) ^ 2 * f k)
        * (∑ k ∈ T, f k) ^ (m - 1) / (N : ℝ) := by
        have hNne : (N : ℝ) ≠ 0 := ne_of_gt hNpos
        calc ∑ n ∈ Fintype.piFinset (fun _ : Fin m => T),
              (∏ j, f (n j)) * (Real.pi * (∑ j, ((n j : ℝ)) ^ 2) / (N : ℝ))
            = (Real.pi / (N : ℝ)) * ∑ n ∈ Fintype.piFinset (fun _ : Fin m => T),
              (∏ j, f (n j)) * (∑ j, ((n j : ℝ)) ^ 2) := by
              rw [Finset.mul_sum]
              apply Finset.sum_congr rfl
              intro n _
              ring
          _ = (Real.pi / (N : ℝ)) * ((m : ℝ) * (∑ k ∈ T, ((k : ℝ)) ^ 2 * f k)
              * (∑ k ∈ T, f k) ^ (m - 1)) := by
              rw [moment_prod]
          _ = Real.pi * (m : ℝ) * (∑ k ∈ T, ((k : ℝ)) ^ 2 * f k)
              * (∑ k ∈ T, f k) ^ (m - 1) / (N : ℝ) := by
              field_simp

/-- Theorem 1(c) as a ratio estimate (source §3): `Tr / TrM` equals the
    residue-phase sum `Z` up to `π·m·s2·s0^(m-1)/N`. -/
lemma trace_ratio_error (m N : ℕ) (hm : 1 ≤ m) (hN : 2 ≤ N)
    (hcop : Nat.Coprime (Dm m).toNat N)
    (a b : ℕ) (ha : (((Dm m).toNat * a : ℕ) : ZMod N) = 1)
    (hb : ((N * b : ℕ) : ZMod (Dm m).toNat) = 1)
    (Φ : (Fin m → ℤ) → ℂ) (TrM Tr : ℂ) (hTrM : TrM ≠ 0)
    (S : Finset (Fin m → ℤ))
    (hGauss : Tr = TrM * ∑ n ∈ S, Φ n * e ((Qnum m n : ℚ) * (a : ℚ) / (N : ℚ) : ℝ))
    (hMod : ‖TrM‖ = 1)
    (f : ℤ → ℝ) (hf : ∀ n, ‖Φ n‖ ≤ ∏ j, f (n j))
    (T : Finset ℤ) (hS : S = Fintype.piFinset (fun _ : Fin m => T)) :
    ‖Tr / TrM - ∑ n ∈ S, Φ n
      * e (-((b % gp m : ℕ) : ℚ) * (yp m : ℚ) * (NmZ m n : ℚ) / (gp m : ℚ) : ℝ)‖
      ≤ Real.pi * (m : ℝ) * (∑ k ∈ T, ((k : ℝ)) ^ 2 * f k)
        * (∑ k ∈ T, f k) ^ (m - 1) / (N : ℝ) := by
  obtain ⟨hform, -⟩ := trace_formula_finite m N hm hN hcop a b ha hb Φ TrM Tr S
    hGauss hMod
  have hdiv : Tr / TrM = ∑ n ∈ S, Φ n * (e ((Qnum m n : ℚ) / (Dm m : ℚ) / (N : ℚ) : ℝ)
      * e (-((b % gp m : ℕ) : ℚ) * (yp m : ℚ) * (NmZ m n : ℚ) / (gp m : ℚ) : ℝ)) := by
    rw [hform, mul_div_cancel_left₀ _ hTrM]
  rw [hdiv]
  exact trace_error_finite m N hm (by omega) Φ
    (fun n => e (-((b % gp m : ℕ) : ℚ) * (yp m : ℚ) * (NmZ m n : ℚ) / (gp m : ℚ) : ℝ))
    f (fun n => e_norm_one _) hf T S hS

/- §7. The abstract kernel form (Theorem 3 / Prop R of the source).
    V is an abstract finite abelian group (standing in for V = ℤ^m/Hℤ^m),
    𝒬 : V → ℚ the quadratic form, ℬ its polarization, χ a unit-modulus
    character (standing in for the pairing with ξ). The Smith identification
    V ≅ ℤ/d₁ × ℤ/d₂, Rad = V[4] and |V| = D are NOT proved here. -/

/-- Orthogonality of characters: a nontrivial character sums to zero. -/
lemma char_sum_eq_zero_of_exists_ne_one {V : Type*} [AddCommGroup V] [Fintype V]
    (χ : V → ℂ) (hχ : ∀ β γ, χ (β + γ) = χ β * χ γ)
    (β₀ : V) (hβ₀ : χ β₀ ≠ 1) : ∑ β, χ β = 0 := by
  have h2 : ∑ β, χ (Equiv.addLeft β₀ β) = ∑ β, χ β :=
    Equiv.sum_comp (Equiv.addLeft β₀) χ
  have h1 : ∑ β, χ β = χ β₀ * ∑ β, χ β := by
    rw [Finset.mul_sum, ← h2]
    exact Finset.sum_congr rfl (fun β _ => hχ β₀ β)
  have h3 : (1 - χ β₀) * ∑ β, χ β = 0 := by linear_combination h1
  exact (mul_eq_zero.mp h3).resolve_left (sub_ne_zero.mpr (Ne.symm hβ₀))

/-- `e(t) = 1` iff `t` is an integer. -/
lemma e_eq_one_iff (t : ℝ) : e t = 1 ↔ ∃ k : ℤ, t = (k : ℝ) := by
  constructor
  · intro h
    unfold e at h
    obtain ⟨n, hn⟩ := (Complex.exp_eq_one_iff).mp h
    have h2pi : (2 * (Real.pi : ℂ) * Complex.I) ≠ 0 := by
      apply mul_ne_zero
      · apply mul_ne_zero
        · norm_num
        · exact_mod_cast ne_of_gt Real.pi_pos
      · exact Complex.I_ne_zero
    have hcan : (2 * (Real.pi : ℂ) * Complex.I) * (t : ℂ)
        = (2 * (Real.pi : ℂ) * Complex.I) * (n : ℂ) := by
      calc (2 * (Real.pi : ℂ) * Complex.I) * (t : ℂ)
          = 2 * (Real.pi : ℂ) * Complex.I * (t : ℂ) := by ring
        _ = (n : ℂ) * (2 * (Real.pi : ℂ) * Complex.I) := hn
        _ = (2 * (Real.pi : ℂ) * Complex.I) * (n : ℂ) := by ring
    have ht := mul_left_cancel₀ h2pi hcan
    refine ⟨n, ?_⟩
    exact_mod_cast ht
  · rintro ⟨k, rfl⟩
    exact e_int k

/-- Conjugation negates the phase: `conj (e t) = e (-t)`. -/
lemma e_conj (t : ℝ) : star (e t) = e (-t) := by
  have hθ : ∀ s : ℝ, e s = Complex.exp (((2 * Real.pi * s : ℝ) : ℂ) * Complex.I) := by
    intro s
    unfold e
    congr 1
    push_cast
    ring
  rw [hθ t, hθ (-t), Complex.exp_eq_exp_ℂ, NormedSpace.star_exp,
    ← Complex.exp_eq_exp_ℂ]
  congr 1
  simp

/-- `e 0 = 1`. -/
lemma e_zero : e 0 = 1 := by
  unfold e
  simp

/-- The twisted phase `ψ_ν(β) = e(-ν·𝒬(β))`. -/
noncomputable def psi {V : Type*} (Q : V → ℚ) (ν : ℚ) (β : V) : ℂ :=
  e (-((ν : ℝ) * (Q β : ℝ)))

/-- The kernel-square identity (source §4, proof of Prop R): the squared
    modulus of the kernel sum splits over the radical set `Rad` (the set of
    `γ` with `ν·ℬ(·,γ)` integral). `Rad` is taken as a parameter with its
    two defining properties as hypotheses. -/
lemma kernel_sq {V : Type*} [AddCommGroup V] [Fintype V] [DecidableEq V]
    (Q : V → ℚ) (B : V → V → ℚ)
    (hBilin1 : ∀ β₁ β₂ γ, B (β₁ + β₂) γ = B β₁ γ + B β₂ γ)
    (hQuad : ∀ β γ, Q (β + γ) = Q β + Q γ + B β γ)
    (ν : ℚ) (χ : V → ℂ)
    (hχ : ∀ β γ, χ (β + γ) = χ β * χ γ)
    (hχnorm : ∀ β, ‖χ β‖ = 1)
    (Rad : Finset V)
    (hRadIn : ∀ γ ∈ Rad, ∀ β, ∃ k : ℤ, (ν * B β γ : ℚ) = k)
    (hRadOut : ∀ γ ∉ Rad, ∃ β₀, ¬ ∃ k : ℤ, (ν * B β₀ γ : ℚ) = k) :
    (∑ β, psi Q ν β * (χ β)⁻¹) * star (∑ β, psi Q ν β * (χ β)⁻¹)
    = (Fintype.card V : ℂ) * ∑ γ ∈ Rad, χ γ * e (((ν : ℝ) * (Q γ : ℝ))) := by
  classical
  have hχne : ∀ β, χ β ≠ 0 := by
    intro β h0
    have hn := hχnorm β
    rw [h0, norm_zero] at hn
    exact zero_ne_one hn
  have hχconj : ∀ γ, star (χ γ) = (χ γ)⁻¹ := by
    intro γ
    have h1 : star (χ γ) * χ γ = 1 := by
      have h := Complex.normSq_eq_conj_mul_self (z := χ γ)
      rw [Complex.normSq_eq_norm_sq, hχnorm γ] at h
      simp only [one_pow, Complex.ofReal_one] at h
      rw [Complex.star_def]
      exact h.symm
    exact eq_inv_of_mul_eq_one_left h1
  have hstar : ∀ β, star (psi Q ν β * (χ β)⁻¹)
      = e (((ν : ℝ) * (Q β : ℝ))) * χ β := by
    intro β
    show star (e (-((ν : ℝ) * (Q β : ℝ))) * (χ β)⁻¹) = _
    rw [star_mul, e_conj, star_inv₀, hχconj β, inv_inv, neg_neg, mul_comm]
  have hterm : ∀ β δ, (psi Q ν β * (χ β)⁻¹)
      * (e (((ν : ℝ) * (Q (β + δ) : ℝ))) * χ (β + δ))
      = χ δ * e (((ν : ℝ) * (Q δ : ℝ))) * e (((ν : ℝ) * (B β δ : ℝ))) := by
    intro β δ
    have hQ : ((ν : ℝ) * (Q (β + δ) : ℝ))
        = ((ν : ℝ) * (Q β : ℝ)) + ((ν : ℝ) * (Q δ : ℝ))
          + ((ν : ℝ) * (B β δ : ℝ)) := by
      have h := hQuad β δ
      have h2 : (ν * Q (β + δ) : ℚ) = ν * Q β + ν * Q δ + ν * B β δ := by
        rw [h]
        ring
      exact_mod_cast h2
    show (e (-((ν : ℝ) * (Q β : ℝ))) * (χ β)⁻¹)
        * (e (((ν : ℝ) * (Q (β + δ) : ℝ))) * χ (β + δ)) = _
    rw [hQ, e_add, e_add, hχ β δ]
    have hcan : e (-((ν : ℝ) * (Q β : ℝ))) * e (((ν : ℝ) * (Q β : ℝ))) = 1 := by
      rw [← e_add, neg_add_cancel]
      exact e_zero
    have hχcan : (χ β)⁻¹ * χ β = 1 := inv_mul_cancel₀ (hχne β)
    linear_combination (χ δ * e (((ν : ℝ) * (Q δ : ℝ)))
        * e (((ν : ℝ) * (B β δ : ℝ)))) * hcan
      + (χ δ * e (((ν : ℝ) * (Q δ : ℝ))) * e (((ν : ℝ) * (B β δ : ℝ)))
        * (e (-((ν : ℝ) * (Q β : ℝ))) * e (((ν : ℝ) * (Q β : ℝ))))) * hχcan
  have hreindex : ∀ β, (∑ γ, (psi Q ν β * (χ β)⁻¹)
        * (e (((ν : ℝ) * (Q γ : ℝ))) * χ γ))
      = ∑ δ, (psi Q ν β * (χ β)⁻¹)
        * (e (((ν : ℝ) * (Q (β + δ) : ℝ))) * χ (β + δ)) := by
    intro β
    exact (Equiv.sum_comp (Equiv.addLeft β) _).symm
  have hinner : ∀ δ, (∑ β, (psi Q ν β * (χ β)⁻¹)
        * (e (((ν : ℝ) * (Q (β + δ) : ℝ))) * χ (β + δ)))
      = χ δ * e (((ν : ℝ) * (Q δ : ℝ)))
        * (∑ β, e (((ν : ℝ) * (B β δ : ℝ)))) := by
    intro δ
    rw [Finset.sum_congr rfl (fun β _ => hterm β δ), Finset.mul_sum]
  have hInner : ∀ δ, (∑ β, e (((ν : ℝ) * (B β δ : ℝ))))
      = if δ ∈ Rad then (Fintype.card V : ℂ) else 0 := by
    intro δ
    by_cases hδ : δ ∈ Rad
    · rw [if_pos hδ]
      have h1 : ∀ β, e (((ν : ℝ) * (B β δ : ℝ))) = 1 := by
        intro β
        obtain ⟨k, hk⟩ := hRadIn δ hδ β
        have hkR : ((ν : ℝ) * (B β δ : ℝ)) = ((k : ℤ) : ℝ) := by exact_mod_cast hk
        rw [hkR]
        exact e_int k
      rw [Finset.sum_congr rfl (fun β _ => h1 β), Finset.sum_const, Finset.card_univ,
        nsmul_eq_mul, mul_one]
    · rw [if_neg hδ]
      obtain ⟨β₀, hβ₀⟩ := hRadOut δ hδ
      refine char_sum_eq_zero_of_exists_ne_one
        (fun β => e (((ν : ℝ) * (B β δ : ℝ)))) ?_ β₀ ?_
      · intro β₁ β₂
        have hB : ((ν : ℝ) * (B (β₁ + β₂) δ : ℝ))
            = ((ν : ℝ) * (B β₁ δ : ℝ)) + ((ν : ℝ) * (B β₂ δ : ℝ)) := by
          have h := hBilin1 β₁ β₂ δ
          have h2 : (ν * B (β₁ + β₂) δ : ℚ) = ν * B β₁ δ + ν * B β₂ δ := by
            rw [h]
            ring
          exact_mod_cast h2
        rw [hB, e_add]
      · intro hcon
        apply hβ₀
        obtain ⟨k, hk⟩ := (e_eq_one_iff _).mp hcon
        refine ⟨k, ?_⟩
        exact_mod_cast hk
  rw [star_sum]
  simp only [hstar]
  rw [Fintype.sum_mul_sum]
  simp only [hreindex]
  rw [Finset.sum_comm]
  simp only [hinner]
  have hG : ∀ δ ∈ Finset.univ, δ ∉ Rad → χ δ * e (((ν : ℝ) * (Q δ : ℝ)))
      * (∑ β, e (((ν : ℝ) * (B β δ : ℝ)))) = 0 := by
    intro δ _ hδ
    rw [hInner δ, if_neg hδ, mul_zero]
  rw [← Finset.sum_subset (Finset.subset_univ Rad) hG]
  rw [Finset.sum_congr rfl (fun δ hδ => by rw [hInner δ, if_pos hδ]),
    ← Finset.sum_mul]
  rw [mul_comm (∑ γ ∈ Rad, χ γ * e (((ν : ℝ) * (Q γ : ℝ)))) (Fintype.card V : ℂ)]

/-- Vanishing of the bilinear form on `0` (used for the radical subgroup). -/
lemma B_apply_zero {V : Type*} [AddCommGroup V] (B : V → V → ℚ)
    (hBilin2 : ∀ β γ₁ γ₂, B β (γ₁ + γ₂) = B β γ₁ + B β γ₂) (β : V) :
    B β 0 = 0 := by
  have h := hBilin2 β 0 0
  rw [add_zero] at h
  have h2 : B β 0 + 0 = B β 0 + B β 0 := by rw [add_zero]; exact h
  exact (add_left_cancel h2).symm

/-- The radical subgroup: `γ` with `ν·ℬ(·,γ)` integral (source §4:
    `Rad = V[4]`, the radical of the bilinear form). -/
def RadSub {V : Type*} [AddCommGroup V] (B : V → V → ℚ)
    (hBilin2 : ∀ β γ₁ γ₂, B β (γ₁ + γ₂) = B β γ₁ + B β γ₂) (ν : ℚ) :
    AddSubgroup V where
  carrier := {γ | ∀ β, ∃ k : ℤ, (ν * B β γ : ℚ) = k}
  zero_mem' := by
    intro β
    refine ⟨0, ?_⟩
    rw [B_apply_zero B hBilin2 β]
    simp
  add_mem' := by
    intro γ₁ γ₂ h₁ h₂ β
    obtain ⟨k₁, hk₁⟩ := h₁ β
    obtain ⟨k₂, hk₂⟩ := h₂ β
    refine ⟨k₁ + k₂, ?_⟩
    rw [hBilin2, mul_add, hk₁, hk₂]
    push_cast
    ring
  neg_mem' := by
    intro γ hγ β
    obtain ⟨k, hk⟩ := hγ β
    refine ⟨-k, ?_⟩
    have h := hBilin2 β γ (-γ)
    rw [add_neg_cancel, B_apply_zero B hBilin2 β] at h
    have hneg : B β (-γ) = -B β γ := eq_neg_of_add_eq_zero_right h.symm
    rw [hneg, mul_neg, hk]
    push_cast
    ring

/-- Membership in the radical subgroup, unfolded. -/
lemma mem_RadSub {V : Type*} [AddCommGroup V] (B : V → V → ℚ)
    (hBilin2 : ∀ β γ₁ γ₂, B β (γ₁ + γ₂) = B β γ₁ + B β γ₂) (ν : ℚ)
    (γ : V) :
    γ ∈ RadSub B hBilin2 ν ↔ ∀ β, ∃ k : ℤ, (ν * B β γ : ℚ) = k :=
  Iff.rfl

/-- Proposition R (source §4): the squared modulus of the normalized kernel
    `k = S / card V` is either `0` or `Rad.card / card V`, i.e. `1 / D_eff`
    with `D_eff = card V / Rad.card`. The `Rad` finset is the radical set;
    its subgroup structure is `RadSub` (the source identifies it with `V[4]`,
    which needs Smith normal form and is NOT proved here). -/
lemma propR {V : Type*} [AddCommGroup V] [Fintype V] [DecidableEq V]
    (Q : V → ℚ) (B : V → V → ℚ)
    (hBilin1 : ∀ β₁ β₂ γ, B (β₁ + β₂) γ = B β₁ γ + B β₂ γ)
    (hBilin2 : ∀ β γ₁ γ₂, B β (γ₁ + γ₂) = B β γ₁ + B β γ₂)
    (hQuad : ∀ β γ, Q (β + γ) = Q β + Q γ + B β γ)
    (ν : ℚ) (χ : V → ℂ)
    (hχ : ∀ β γ, χ (β + γ) = χ β * χ γ)
    (hχnorm : ∀ β, ‖χ β‖ = 1)
    (Rad : Finset V)
    (hRadIn : ∀ γ ∈ Rad, ∀ β, ∃ k : ℤ, (ν * B β γ : ℚ) = k)
    (hRadOut : ∀ γ ∉ Rad, ∃ β₀, ¬ ∃ k : ℤ, (ν * B β₀ γ : ℚ) = k) :
    ‖(∑ β, psi Q ν β * (χ β)⁻¹) / (Fintype.card V : ℂ)‖^2 = 0 ∨
    ‖(∑ β, psi Q ν β * (χ β)⁻¹) / (Fintype.card V : ℂ)‖^2
      = (Rad.card : ℝ) / (Fintype.card V : ℝ) := by
  classical
  have hker := kernel_sq Q B hBilin1 hQuad ν χ hχ hχnorm Rad hRadIn hRadOut
  have hRadSub : ∀ γ, γ ∈ Rad ↔ γ ∈ RadSub B hBilin2 ν := by
    intro γ
    rw [mem_RadSub]
    constructor
    · intro hγ
      exact hRadIn γ hγ
    · intro hp
      by_contra hγ
      obtain ⟨β₀, hβ₀⟩ := hRadOut γ hγ
      exact hβ₀ (hp β₀)
  have hcard : Fintype.card ↥(RadSub B hBilin2 ν) = Rad.card := by
    rw [← Fintype.card_coe Rad]
    exact Fintype.card_congr (Equiv.subtypeEquiv (Equiv.refl V) hRadSub).symm
  have hbridge : (∑ δ : ↥(RadSub B hBilin2 ν), χ ↑δ * e (((ν : ℝ) * (Q ↑δ : ℝ))))
      = ∑ γ ∈ Rad, χ γ * e (((ν : ℝ) * (Q γ : ℝ))) := by
    have h1 : (∑ δ : ↥(RadSub B hBilin2 ν), χ ↑δ * e (((ν : ℝ) * (Q ↑δ : ℝ))))
        = ∑ γ : {x // x ∈ Rad}, χ ↑(Equiv.subtypeEquiv (Equiv.refl V) hRadSub γ)
          * e (((ν : ℝ) * (Q ↑(Equiv.subtypeEquiv (Equiv.refl V) hRadSub γ) : ℝ))) := by
      exact (Equiv.sum_comp (Equiv.subtypeEquiv (Equiv.refl V) hRadSub) _).symm
    rw [h1]
    exact Finset.sum_coe_sort Rad (fun γ => χ γ * e (((ν : ℝ) * (Q γ : ℝ))))
  have hχRmul : ∀ δ₁ δ₂ : ↥(RadSub B hBilin2 ν),
      χ ↑(δ₁ + δ₂) * e (((ν : ℝ) * (Q ↑(δ₁ + δ₂) : ℝ)))
      = (χ ↑δ₁ * e (((ν : ℝ) * (Q ↑δ₁ : ℝ))))
        * (χ ↑δ₂ * e (((ν : ℝ) * (Q ↑δ₂ : ℝ)))) := by
    intro δ₁ δ₂
    have hcoe : ((δ₁ + δ₂ : ↥(RadSub B hBilin2 ν)) : V) = ↑δ₁ + ↑δ₂ := rfl
    rw [hcoe, hχ ↑δ₁ ↑δ₂]
    have hQ : ((ν : ℝ) * (Q (↑δ₁ + ↑δ₂) : ℝ))
        = ((ν : ℝ) * (Q ↑δ₁ : ℝ)) + ((ν : ℝ) * (Q ↑δ₂ : ℝ))
          + ((ν : ℝ) * (B ↑δ₁ ↑δ₂ : ℝ)) := by
      have h := hQuad ↑δ₁ ↑δ₂
      have h2 : (ν * Q (↑δ₁ + ↑δ₂) : ℚ) = ν * Q ↑δ₁ + ν * Q ↑δ₂ + ν * B ↑δ₁ ↑δ₂ := by
        rw [h]; ring
      exact_mod_cast h2
    rw [hQ, e_add, e_add]
    have hδ₂ : ∀ β, ∃ k : ℤ, (ν * B β ↑δ₂ : ℚ) = k :=
      (mem_RadSub B hBilin2 ν _).mp δ₂.2
    obtain ⟨k, hk⟩ := hδ₂ ↑δ₁
    have hkR : ((ν : ℝ) * (B ↑δ₁ ↑δ₂ : ℝ)) = ((k : ℤ) : ℝ) := by exact_mod_cast hk
    rw [hkR, e_int k, mul_one]
    ring
  haveI : Nonempty V := ⟨0⟩
  have hVpos : 0 < Fintype.card V := Fintype.card_pos
  have hVR : (Fintype.card V : ℝ) ≠ 0 := by exact_mod_cast hVpos.ne'
  have hnormSq : ∀ z : ℂ, (‖z‖^2 : ℂ) = z * star z := by
    intro z
    have h := Complex.mul_conj z
    rw [Complex.normSq_eq_norm_sq] at h
    rw [Complex.star_def, ← Complex.ofReal_pow]
    exact h.symm
  by_cases htriv : ∀ δ : ↥(RadSub B hBilin2 ν),
      χ ↑δ * e (((ν : ℝ) * (Q ↑δ : ℝ))) = 1
  · right
    have hsum : (∑ δ : ↥(RadSub B hBilin2 ν), χ ↑δ * e (((ν : ℝ) * (Q ↑δ : ℝ))))
        = (Rad.card : ℂ) := by
      rw [Finset.sum_congr rfl (fun δ _ => htriv δ), Finset.sum_const, Finset.card_univ,
        nsmul_eq_mul, mul_one, hcard]
    have hSkSq : ‖∑ β, psi Q ν β * (χ β)⁻¹‖^2
        = (Fintype.card V : ℝ) * (Rad.card : ℝ) := by
      have h0 : (‖∑ β, psi Q ν β * (χ β)⁻¹‖^2 : ℂ)
          = (((Fintype.card V : ℝ) * (Rad.card : ℝ)) : ℂ) := by
        rw [hnormSq, hker, ← hbridge, hsum]
        push_cast
        ring
      exact_mod_cast h0
    rw [norm_div, div_pow, Complex.norm_natCast, hSkSq]
    field_simp
  · left
    push_neg at htriv
    obtain ⟨δ₀, hδ₀⟩ := htriv
    have hsum0 : (∑ δ : ↥(RadSub B hBilin2 ν), χ ↑δ * e (((ν : ℝ) * (Q ↑δ : ℝ)))) = 0 :=
      char_sum_eq_zero_of_exists_ne_one _ hχRmul δ₀ hδ₀
    have hSk0 : (∑ β, psi Q ν β * (χ β)⁻¹) = 0 := by
      have h0 : (‖∑ β, psi Q ν β * (χ β)⁻¹‖^2 : ℂ) = 0 := by
        rw [hnormSq, hker, ← hbridge, hsum0, mul_zero]
      have h1 : ‖∑ β, psi Q ν β * (χ β)⁻¹‖^2 = 0 := by exact_mod_cast h0
      have h2 : ‖∑ β, psi Q ν β * (χ β)⁻¹‖ = 0 :=
        (pow_eq_zero_iff (show (2 : ℕ) ≠ 0 by norm_num)).mp h1
      exact norm_eq_zero.mp h2
    simp [hSk0]

/-- `ν`-independence of the radical character (source §4): on the radical,
    `2·𝒬` is integral, and for odd `ν` the phase `e(ν·𝒬)` equals `e(𝒬)`,
    so the zero pattern of the kernel does not depend on the unit `ν`.
    The hypothesis `hQ2` is the source's `2·𝒬(γ) = ℬ(γ,γ) ∈ ℤ` on `Rad`. -/
lemma nu_indep {V : Type*} [AddCommGroup V]
    (Q : V → ℚ) (B : V → V → ℚ)
    (ν ν' : ℚ)
    (hνodd : ∃ a : ℤ, ν = 2 * a + 1) (hν'odd : ∃ a : ℤ, ν' = 2 * a + 1)
    (hQ2 : ∀ δ, (∀ β, ∃ k : ℤ, (ν * B β δ : ℚ) = k) → ∃ k : ℤ, 2 * Q δ = k)
    (δ : V) (hδ : ∀ β, ∃ k : ℤ, (ν * B β δ : ℚ) = k) :
    e (((ν : ℝ) * (Q δ : ℝ))) = e (((ν' : ℝ) * (Q δ : ℝ))) := by
  obtain ⟨k2, hk2⟩ := hQ2 δ hδ
  obtain ⟨a, ha⟩ := hνodd
  obtain ⟨a', ha'⟩ := hν'odd
  have hdiff : ((ν' : ℝ) * (Q δ : ℝ)) - ((ν : ℝ) * (Q δ : ℝ))
      = (((a' - a) * k2 : ℤ) : ℝ) := by
    have hQ : (ν' - ν) * Q δ = (a' - a) * (2 * Q δ) := by
      rw [ha, ha']; ring
    have hQ2' : (ν' - ν) * Q δ = (a' - a) * k2 := by rw [hQ, hk2]
    have hcast : (((ν' - ν) * Q δ : ℚ) : ℝ)
        = ((ν' : ℝ) * (Q δ : ℝ)) - ((ν : ℝ) * (Q δ : ℝ)) := by
      push_cast; ring
    rw [← hcast, hQ2']
    push_cast; ring
  have hsplit : ((ν' : ℝ) * (Q δ : ℝ))
      = ((ν : ℝ) * (Q δ : ℝ)) + (((a' - a) * k2 : ℤ) : ℝ) := by
    linarith [hdiff]
  rw [hsplit, e_add, e_int, mul_one]

/- §8. Theorem 2: the `N`-average equals the `ν`-average on a full block. -/

/-- The fiber identity behind Theorem 2 (source §5): if the residue map
    `νmap : 𝒩 → (ZMod g')ˣ` has equal fibers over all units, then the
    `𝒩`-sum of any `Ψ` is the fiber size times the `ν`-sum. The cardinality
    of `(ZMod g')ˣ` is Euler's `φ(g')`. -/
lemma avg_eq_avg_units {g' : ℕ} [NeZero g'] (𝒩 : Finset ℕ) (νmap : ℕ → (ZMod g')ˣ)
    (hfib : ∀ u₁ u₂ : (ZMod g')ˣ,
      (𝒩.filter (fun N => νmap N = u₁)).card
      = (𝒩.filter (fun N => νmap N = u₂)).card)
    (Ψ : (ZMod g')ˣ → ℂ) :
    (∑ N ∈ 𝒩, Ψ (νmap N)) * (Fintype.card (ZMod g')ˣ : ℂ)
    = (𝒩.card : ℂ) * ∑ u : (ZMod g')ˣ, Ψ u := by
  classical
  by_cases h𝒩 : 𝒩.Nonempty
  · obtain ⟨N₀, hN₀⟩ := h𝒩
    set c := (𝒩.filter (fun N => νmap N = νmap N₀)).card with hc
    have hfibc : ∀ u, (𝒩.filter (fun N => νmap N = u)).card = c :=
      fun u => hfib u (νmap N₀)
    have hdecomp : (∑ N ∈ 𝒩, Ψ (νmap N))
        = ∑ u : (ZMod g')ˣ, ((𝒩.filter (fun N => νmap N = u)).card : ℂ) * Ψ u := by
      have h := Finset.sum_fiberwise_of_maps_to (s := 𝒩) (t := Finset.univ)
        (fun N _ => Finset.mem_univ (νmap N)) (f := fun N => Ψ (νmap N))
      rw [← h]
      apply Finset.sum_congr rfl
      intro u _
      rw [Finset.sum_congr rfl (fun N hN => by rw [(Finset.mem_filter.mp hN).2]),
        Finset.sum_const, nsmul_eq_mul]
    have hcard : 𝒩.card = c * Fintype.card (ZMod g')ˣ := by
      have h := Finset.card_eq_sum_card_fiberwise (s := 𝒩) (t := Finset.univ)
        (f := νmap) (fun N _ => Finset.mem_univ _)
      rw [h]
      rw [Finset.sum_congr rfl (fun u _ => hfibc u), Finset.sum_const, Finset.card_univ,
        nsmul_eq_mul, Nat.cast_id, mul_comm]
    have hcardC : (𝒩.card : ℂ)
        = (c : ℂ) * (Fintype.card (ZMod g')ˣ : ℂ) := by exact_mod_cast hcard
    rw [hdecomp, Finset.sum_congr rfl (fun u _ => by rw [hfibc u]), ← Finset.mul_sum,
      hcardC]
    ring
  · rw [Finset.not_nonempty_iff_eq_empty.mp h𝒩]
    simp

/-- Theorem 2, averaged error (source §5): on a full block `𝒩` of `N ≥ X`,
    if each `A N` is within `E / N` of `Z (νmap N)`, then the `𝒩`-average of
    `A` is within `E / X` of the `ν`-average of `Z`. Combined with
    `trace_ratio_error` (Theorem 1(c), `E = π·m·s2·s0^(m-1)`), this is the
    source's Theorem 2 up to the incomplete-block `D / X` term, which is NOT
    proved here (it is the `hEquidist` hypothesis of the 175 module). -/
lemma theorem2_avg_error {g' : ℕ} [NeZero g'] (𝒩 : Finset ℕ) (νmap : ℕ → (ZMod g')ˣ)
    (hfib : ∀ u₁ u₂ : (ZMod g')ˣ,
      (𝒩.filter (fun N => νmap N = u₁)).card
      = (𝒩.filter (fun N => νmap N = u₂)).card)
    (h𝒩 : 𝒩.Nonempty)
    (Z : (ZMod g')ˣ → ℂ) (A : ℕ → ℂ) (E X : ℝ) (hX : 0 < X) (hE : 0 ≤ E)
    (hN : ∀ N ∈ 𝒩, X ≤ (N : ℝ))
    (herr : ∀ N ∈ 𝒩, ‖A N - Z (νmap N)‖ ≤ E / (N : ℝ)) :
    ‖(∑ N ∈ 𝒩, A N) / (𝒩.card : ℂ)
      - (∑ u, Z u) / (Fintype.card (ZMod g')ˣ : ℂ)‖ ≤ E / X := by
  classical
  have hcard𝒩 : (𝒩.card : ℝ) ≠ 0 := by
    have hpos : 0 < 𝒩.card := Finset.card_pos.mpr h𝒩
    exact_mod_cast hpos.ne'
  have hcardU : (Fintype.card (ZMod g')ˣ : ℝ) ≠ 0 := by
    haveI : Nonempty (ZMod g')ˣ := ⟨1⟩
    have hpos : 0 < Fintype.card (ZMod g')ˣ := Fintype.card_pos
    exact_mod_cast hpos.ne'
  have havg := avg_eq_avg_units 𝒩 νmap hfib Z
  have hdiff : (∑ N ∈ 𝒩, A N) / (𝒩.card : ℂ)
      - (∑ u, Z u) / (Fintype.card (ZMod g')ˣ : ℂ)
      = (∑ N ∈ 𝒩, (A N - Z (νmap N))) / (𝒩.card : ℂ) := by
    rw [Finset.sum_sub_distrib]
    have hc𝒩 : (𝒩.card : ℂ) ≠ 0 := by exact_mod_cast hcard𝒩
    have hcU : (Fintype.card (ZMod g')ˣ : ℂ) ≠ 0 := by exact_mod_cast hcardU
    field_simp
    linear_combination havg
  rw [hdiff, norm_div, Complex.norm_natCast]
  calc ‖∑ N ∈ 𝒩, (A N - Z (νmap N))‖ / (𝒩.card : ℝ)
      ≤ (∑ N ∈ 𝒩, ‖A N - Z (νmap N)‖) / (𝒩.card : ℝ) := by
        apply div_le_div_of_nonneg_right _ (Nat.cast_nonneg _)
        exact norm_sum_le _ _
    _ ≤ (∑ N ∈ 𝒩, E / (N : ℝ)) / (𝒩.card : ℝ) := by
        apply div_le_div_of_nonneg_right _ (Nat.cast_nonneg _)
        exact Finset.sum_le_sum (fun N hN => herr N hN)
    _ ≤ (∑ N ∈ 𝒩, E / X) / (𝒩.card : ℝ) := by
        apply div_le_div_of_nonneg_right _ (Nat.cast_nonneg _)
        apply Finset.sum_le_sum
        intro N hNm
        apply div_le_div_of_nonneg_left hE hX (hN N hNm)
    _ = E / X := by
        rw [Finset.sum_const, nsmul_eq_mul]
        field_simp

/- Axiom audit for the main theorems (all must be the standard three only). -/
#print axioms pell_norm
#print axioms lam_pow
#print axioms phi_symm
#print axioms two_y_over_D
#print axioms gp_dvd_D
#print axioms HXphi
#print axioms quadId
#print axioms Q_eq
#print axioms Hmat_mul_Hinv
#print axioms quad_nonneg
#print axioms Q_bound
#print axioms reciprocity
#print axioms phase_identity
#print axioms e_sub_one_le
#print axioms exists_inv_mod
#print axioms trace_formula_finite
#print axioms moment_prod
#print axioms trace_error_finite
#print axioms trace_ratio_error
#print axioms char_sum_eq_zero_of_exists_ne_one
#print axioms e_eq_one_iff
#print axioms e_conj
#print axioms kernel_sq
#print axioms B_apply_zero
#print axioms propR
#print axioms nu_indep
#print axioms avg_eq_avg_units
#print axioms theorem2_avg_error

end TraceFormula
end LineB
end Bgs
