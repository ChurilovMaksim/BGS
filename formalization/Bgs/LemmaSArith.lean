import Mathlib.RingTheory.Polynomial.Cyclotomic.Basic
import Mathlib.RingTheory.RootsOfUnity.Complex
import Mathlib.Analysis.SpecialFunctions.Log.Base
import Mathlib.Algebra.Ring.GeomSum

/-! Arithmetic identities and inequalities behind BGS-TRACE-352..354 (Lemma S on cross lines, the polymer gap
lemma, the Binet lattice generator η_s).  No sorry, no native_decide.

Convention (BGS-TRACE-342 / 348): ε = 1 + √2, ε̄ = 1 − √2, λ = ε², h_n = (ε^n + ε̄^n)/2 with h_0 = h_1 = 1,
h_{n+2} = 2 h_{n+1} + h_n (`hp`/`h` below use the same pair recursion as `Bgs.H6LemmaW.hpair`/`h`, restated so that this
module imports only Mathlib; `h_closed` proves the closed form).
Φ_n(x) := ∑_{k<n} x^k (for a prime n this is the cyclotomic polynomial, `Polynomial.cyclotomic_prime`).

What is certified here (and only this):
* `phi_eps`, `phi_neg_eps` : n odd ⟹ Φ_n(ε)Φ_n(ε̄) = h_n and Φ_n(−ε)Φ_n(−ε̄) = h_n  (N_{Q(√2)/Q} Φ_n(±ε) = h_n).
* `phi_lambda`             : n odd ⟹ Φ_n(λ)Φ_n(λ̄) = h_n².
* `prod_eta`, `prod_kernel` : p an odd prime, s = ±1 ⟹ ∏_{μ primitive p-th root of 1 in ℂ} (μ² − 2sμ − 1) = h_p and
                              ∏_μ (μ² − 6μ + 1) = h_p²  (the products over all conjugates; the identification with
                              the field norm of Q(ζ_p)/Q and the lattice/index statements are NOT formalized).
* `max_abs_add_sub`, `norm_le_ht`, `ht_sub_le`, `ht_add_le`, `lemmaS_core_sub`, `lemmaS_core_add`, `axis_bound`,
  `mul_le_max_sq` : the height/norm inequalities of Lemma S (the ideal-theoretic steps are NOT formalized).
* `polymer_norm_lt`, `polymer_gap`, `polymer_gap_of_norm`, `logb_const_lt`, `logb_const_gt` : |F(σε)|·|F(σε̄)| < A² ε^{K+2}/2 for
  |a_k| ≤ A, the resulting K > log_ε d − 2 log_ε A − log_ε(ε²/2), and 1.213 < log_ε(ε²/2) < 1.214
  (the divisibility step f ∉ (η₊η₋) ⟹ F(ε) ≠ 0 or F(−ε) ≠ 0 is NOT formalized). -/
namespace Bgs.LemmaSArith

open Finset Real Polynomial

/-- (h_n, h_{n+1}). -/
def hp : ℕ → ℕ × ℕ
  | 0 => (1, 1)
  | n + 1 => ((hp n).2, 2 * (hp n).2 + (hp n).1)

/-- h_n = (ε^n + ε̄^n)/2. -/
def h (n : ℕ) : ℕ := (hp n).1

lemma h_zero : h 0 = 1 := rfl
lemma h_one : h 1 = 1 := rfl
lemma h_rec (n : ℕ) : h (n + 2) = 2 * h (n + 1) + h n := rfl

/-- ε = 1 + √2. -/
noncomputable def e : ℝ := 1 + √2
/-- ε̄ = 1 − √2. -/
noncomputable def f : ℝ := 1 - √2

lemma s2sq : √2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
lemma s2pos : 0 < √2 := Real.sqrt_pos.2 (by norm_num)
lemma s2gt1 : 1 < √2 := by nlinarith [s2sq, s2pos]
lemma s2lt : √2 < 3 / 2 := by nlinarith [s2sq, s2pos]
lemma ef : e * f = -1 := by unfold e f; nlinarith [s2sq]
lemma e_add_f : e + f = 2 := by unfold e f; ring
lemma e_sq : e ^ 2 = 2 * e + 1 := by unfold e; nlinarith [s2sq]
lemma f_sq : f ^ 2 = 2 * f + 1 := by unfold f; nlinarith [s2sq]
lemma e_pos : 0 < e := by unfold e; linarith [s2pos]
lemma one_lt_e : 1 < e := by unfold e; linarith [s2pos]
lemma abs_f : |f| = √2 - 1 := by
  unfold f; rw [abs_of_neg (by linarith [s2gt1])]; ring

/-- Closed form: h_n = (ε^n + ε̄^n)/2. -/
theorem h_closed (n : ℕ) : (h n : ℝ) = (e ^ n + f ^ n) / 2 := by
  have key : ∀ n, (h n : ℝ) = (e ^ n + f ^ n) / 2 ∧ (h (n + 1) : ℝ) = (e ^ (n + 1) + f ^ (n + 1)) / 2 := by
    intro n
    induction n with
    | zero =>
      refine ⟨by simp [h_zero], ?_⟩
      rw [h_one]; have := e_add_f; push_cast; linarith
    | succ k ih =>
      refine ⟨ih.2, ?_⟩
      rw [h_rec]; push_cast; rw [ih.1, ih.2]
      have he : e ^ (k + 2) = 2 * e ^ (k + 1) + e ^ k := by
        rw [show k + 2 = k + 1 + 1 by ring, pow_succ, pow_succ]; linear_combination e ^ k * e_sq
      have hf : f ^ (k + 2) = 2 * f ^ (k + 1) + f ^ k := by
        rw [show k + 2 = k + 1 + 1 by ring, pow_succ, pow_succ]; linear_combination f ^ k * f_sq
      rw [show k + 1 + 1 = k + 2 by ring, he, hf]; ring
  exact (key n).1

/-- Φ_n(x) = ∑_{k<n} x^k. -/
def Phi {R : Type*} [CommRing R] (n : ℕ) (x : R) : R := ∑ i ∈ range n, x ^ i

lemma Phi_mul {R : Type*} [CommRing R] (n : ℕ) (x : R) : Phi n x * (x - 1) = x ^ n - 1 := geom_sum_mul x n

lemma ef_pow (n : ℕ) : e ^ n * f ^ n = (-1) ^ n := by rw [← mul_pow, ef]

/-- N_{Q(√2)/Q}(Φ_n(ε)) = h_n for odd n. -/
theorem phi_eps {n : ℕ} (hn : Odd n) : Phi n e * Phi n f = h n := by
  have k1 := Phi_mul n e
  have k2 := Phi_mul n f
  have hP : (e - 1) * (f - 1) = -2 := by unfold e f; nlinarith [s2sq]
  have hR : (e ^ n - 1) * (f ^ n - 1) = -2 * (h n : ℝ) := by
    rw [h_closed]; have := ef_pow n; rw [hn.neg_one_pow] at this; linear_combination this
  have key : (Phi n e * Phi n f) * ((e - 1) * (f - 1)) = (e ^ n - 1) * (f ^ n - 1) := by
    rw [← k1, ← k2]; ring
  linear_combination (-1 / 2 : ℝ) * key + (Phi n e * Phi n f / 2) * hP - (1 / 2 : ℝ) * hR

/-- N_{Q(√2)/Q}(Φ_n(−ε)) = h_n for odd n. -/
theorem phi_neg_eps {n : ℕ} (hn : Odd n) : Phi n (-e) * Phi n (-f) = h n := by
  have k1 := Phi_mul n (-e)
  have k2 := Phi_mul n (-f)
  have hP : (-e - 1) * (-f - 1) = 2 := by unfold e f; nlinarith [s2sq]
  have hR : ((-e) ^ n - 1) * ((-f) ^ n - 1) = 2 * (h n : ℝ) := by
    rw [hn.neg_pow, hn.neg_pow, h_closed]; have := ef_pow n; rw [hn.neg_one_pow] at this
    linear_combination this
  have key : (Phi n (-e) * Phi n (-f)) * ((-e - 1) * (-f - 1)) = ((-e) ^ n - 1) * ((-f) ^ n - 1) := by
    rw [← k1, ← k2]; ring
  linear_combination (1 / 2 : ℝ) * key - (Phi n (-e) * Phi n (-f) / 2) * hP + (1 / 2 : ℝ) * hR

/-- N_{Q(√2)/Q}(Φ_n(λ)) = h_n² for odd n (λ = ε²). -/
theorem phi_lambda {n : ℕ} (hn : Odd n) : Phi n (e ^ 2) * Phi n (f ^ 2) = (h n : ℝ) ^ 2 := by
  have k1 := Phi_mul n (e ^ 2)
  have k2 := Phi_mul n (f ^ 2)
  have hP : (e ^ 2 - 1) * (f ^ 2 - 1) = -4 := by unfold e f; nlinarith [s2sq]
  have hR : ((e ^ 2) ^ n - 1) * ((f ^ 2) ^ n - 1) = -4 * (h n : ℝ) ^ 2 := by
    rw [h_closed, ← pow_mul, ← pow_mul, mul_comm 2 n, pow_mul, pow_mul]
    have := ef_pow n; rw [hn.neg_one_pow] at this
    linear_combination (e ^ n * f ^ n + 1) * this
  have key : (Phi n (e ^ 2) * Phi n (f ^ 2)) * ((e ^ 2 - 1) * (f ^ 2 - 1)) =
      ((e ^ 2) ^ n - 1) * ((f ^ 2) ^ n - 1) := by
    rw [← k1, ← k2]; ring
  linear_combination (-1 / 4 : ℝ) * key + (Phi n (e ^ 2) * Phi n (f ^ 2) / 4) * hP - (1 / 4 : ℝ) * hR

/-! ### Products over the primitive p-th roots of unity in ℂ -/

lemma eval_cyc {p : ℕ} [hp : Fact p.Prime] (x : ℂ) :
    ∏ μ ∈ primitiveRoots p ℂ, (x - μ) = Phi p x := by
  have hζ := Complex.isPrimitiveRoot_exp p hp.out.ne_zero
  have h1 := congrArg (Polynomial.eval x) (cyclotomic_eq_prod_X_sub_primitiveRoots hζ)
  rw [cyclotomic_prime, eval_prod] at h1
  simp only [eval_sub, eval_X, eval_C, eval_finsetSum, eval_pow] at h1
  rw [← h1]; rfl

lemma Phi_ofReal (n : ℕ) (x : ℝ) : ((Phi n x : ℝ) : ℂ) = Phi n (x : ℂ) := by
  unfold Phi; push_cast; rfl

/-- ∏_μ η_s(μ) = h_p, η_s(ω) = ω² − 2sω − 1, μ over the primitive p-th roots of unity, s = ±1. -/
theorem prod_eta {p : ℕ} [hp : Fact p.Prime] (hp2 : p ≠ 2) (s : ℂ) (hs : s = 1 ∨ s = -1) :
    ∏ μ ∈ primitiveRoots p ℂ, (μ ^ 2 - 2 * s * μ - 1) = (h p : ℂ) := by
  have hpo : Odd p := hp.out.odd_of_ne_two hp2
  have hE : ((e : ℝ) : ℂ) * ((f : ℝ) : ℂ) = -1 := by exact_mod_cast ef
  have hS : ((e : ℝ) : ℂ) + ((f : ℝ) : ℂ) = 2 := by exact_mod_cast e_add_f
  have hs2 : s ^ 2 = 1 := by rcases hs with rfl | rfl <;> norm_num
  have fac : ∀ μ : ℂ, μ ^ 2 - 2 * s * μ - 1 = (s * (e : ℂ) - μ) * (s * (f : ℂ) - μ) := by
    intro μ; linear_combination (-((e : ℂ) * (f : ℂ))) * hs2 - hE + (s * μ) * hS
  simp_rw [fac]
  rw [prod_mul_distrib, eval_cyc, eval_cyc]
  rcases hs with rfl | rfl
  · simp only [one_mul]; rw [← Phi_ofReal, ← Phi_ofReal]; exact_mod_cast phi_eps hpo
  · simp only [neg_one_mul]
    rw [show -((e : ℝ) : ℂ) = ((-e : ℝ) : ℂ) by push_cast; rfl,
        show -((f : ℝ) : ℂ) = ((-f : ℝ) : ℂ) by push_cast; rfl, ← Phi_ofReal, ← Phi_ofReal]
    exact_mod_cast phi_neg_eps hpo

/-- ∏_μ (μ² − 6μ + 1) = h_p² (the full-level kernel element ζ² − 6ζ + 1). -/
theorem prod_kernel {p : ℕ} [hp : Fact p.Prime] (hp2 : p ≠ 2) :
    ∏ μ ∈ primitiveRoots p ℂ, (μ ^ 2 - 6 * μ + 1) = (h p : ℂ) ^ 2 := by
  have hpo : Odd p := hp.out.odd_of_ne_two hp2
  have hE : ((e ^ 2 : ℝ) : ℂ) * ((f ^ 2 : ℝ) : ℂ) = 1 := by
    have : e ^ 2 * f ^ 2 = 1 := by rw [← mul_pow, ef]; norm_num
    exact_mod_cast this
  have hS : ((e ^ 2 : ℝ) : ℂ) + ((f ^ 2 : ℝ) : ℂ) = 6 := by
    have : e ^ 2 + f ^ 2 = 6 := by rw [e_sq, f_sq]; linarith [e_add_f]
    exact_mod_cast this
  have fac : ∀ μ : ℂ, μ ^ 2 - 6 * μ + 1 = (((e ^ 2 : ℝ) : ℂ) - μ) * (((f ^ 2 : ℝ) : ℂ) - μ) := by
    intro μ; linear_combination μ * hS - hE
  simp_rw [fac]
  rw [prod_mul_distrib, eval_cyc, eval_cyc, ← Phi_ofReal, ← Phi_ofReal]
  exact_mod_cast phi_lambda hpo

/-! ### Lemma S: heights and norms in Z[√2] -/

/-- Height of a + b√2: |a| + √2|b| (= max(|ρ|, |ρ'|), `max_abs_add_sub`). -/
noncomputable def ht (a b : ℤ) : ℝ := |(a : ℝ)| + √2 * |(b : ℝ)|

lemma max_abs_add_sub (x y : ℝ) : max |x + y| |x - y| = |x| + |y| := by
  apply le_antisymm (max_le (abs_add_le x y) (abs_sub x y))
  rcases le_total 0 x with hx | hx <;> rcases le_total 0 y with hy | hy
  · exact le_max_of_le_left (by rw [abs_of_nonneg hx, abs_of_nonneg hy]; exact le_abs_self _)
  · exact le_max_of_le_right (by rw [abs_of_nonneg hx, abs_of_nonpos hy]; exact le_abs_self _)
  · exact le_max_of_le_right (by rw [abs_of_nonpos hx, abs_of_nonneg hy]; exact neg_le_abs _ |>.trans_eq' (by ring))
  · exact le_max_of_le_left (by rw [abs_of_nonpos hx, abs_of_nonpos hy]; exact neg_le_abs _ |>.trans_eq' (by ring))

/-- max(|a + b√2|, |a − b√2|) = |a| + √2|b|. -/
theorem ht_eq_max (a b : ℤ) : max |(a : ℝ) + b * √2| |(a : ℝ) - b * √2| = ht a b := by
  rw [max_abs_add_sub, abs_mul, abs_of_pos s2pos, ht, mul_comm]

/-- |N(a + b√2)| ≤ height². -/
theorem norm_le_ht (a b : ℤ) : |((a ^ 2 - 2 * b ^ 2 : ℤ) : ℝ)| ≤ ht a b ^ 2 := by
  unfold ht; push_cast
  have ha := sq_abs (a : ℝ); have hb := sq_abs (b : ℝ)
  have h1 := abs_nonneg (a : ℝ); have h2 := abs_nonneg (b : ℝ)
  rw [abs_le]; constructor <;> nlinarith [s2sq, s2pos, mul_nonneg h1 h2, mul_nonneg (mul_nonneg h1 h2) s2pos.le]

theorem ht_nonneg (a b : ℤ) : 0 ≤ ht a b := by
  unfold ht; have := s2pos; positivity

theorem ht_sub_le (a b c d : ℤ) : ht (a - c) (b - d) ≤ ht a b + ht c d := by
  unfold ht; push_cast
  have := abs_sub (a : ℝ) c; have := abs_sub (b : ℝ) d; nlinarith [s2pos]

theorem ht_add_le (a b c d : ℤ) : ht (a + c) (b + d) ≤ ht a b + ht c d := by
  unfold ht; push_cast
  have := abs_add_le (a : ℝ) c; have := abs_add_le (b : ℝ) d; nlinarith [s2pos]

/-- A nonzero element whose norm is divisible by d has height² ≥ d (axis sub-line: G ≥ √min(d₊,d₋)). -/
theorem axis_bound {a b : ℤ} {d : ℕ} (hne : a ^ 2 - 2 * b ^ 2 ≠ 0) (hd : (d : ℤ) ∣ a ^ 2 - 2 * b ^ 2) :
    (d : ℝ) ≤ ht a b ^ 2 := by
  have h1 : (d : ℤ) ≤ |a ^ 2 - 2 * b ^ 2| := Int.le_of_dvd (abs_pos.2 hne) ((dvd_abs _ _).2 hd)
  have h2 : (d : ℝ) ≤ |((a ^ 2 - 2 * b ^ 2 : ℤ) : ℝ)| := by
    rw [← Int.cast_abs]; exact_mod_cast h1
  exact h2.trans (norm_le_ht a b)

/-- Lemma S core (difference side): if N(ρ₂ − ρ₁) ≠ 0 and d ∣ N(ρ₂ − ρ₁) then d ≤ (G(ρ₁) + G(ρ₂))². -/
theorem lemmaS_core_sub {a1 b1 a2 b2 : ℤ} {d : ℕ} (hne : (a2 - a1) ^ 2 - 2 * (b2 - b1) ^ 2 ≠ 0)
    (hd : (d : ℤ) ∣ (a2 - a1) ^ 2 - 2 * (b2 - b1) ^ 2) : (d : ℝ) ≤ (ht a1 b1 + ht a2 b2) ^ 2 := by
  refine (axis_bound hne hd).trans ?_
  have := ht_sub_le a2 b2 a1 b1
  have := ht_nonneg (a2 - a1) (b2 - b1)
  nlinarith

/-- Lemma S core (sum side): if N(ρ₂ + ρ₁) ≠ 0 and d ∣ N(ρ₂ + ρ₁) then d ≤ (G(ρ₁) + G(ρ₂))². -/
theorem lemmaS_core_add {a1 b1 a2 b2 : ℤ} {d : ℕ} (hne : (a2 + a1) ^ 2 - 2 * (b2 + b1) ^ 2 ≠ 0)
    (hd : (d : ℤ) ∣ (a2 + a1) ^ 2 - 2 * (b2 + b1) ^ 2) : (d : ℝ) ≤ (ht a1 b1 + ht a2 b2) ^ 2 := by
  refine (axis_bound hne hd).trans ?_
  have := ht_add_le a2 b2 a1 b1
  have := ht_nonneg (a2 + a1) (b2 + b1)
  nlinarith

/-- d₊ d₋ = h ⟹ h ≤ max(d₊, d₋)² (so max(d₊,d₋) ≥ √h; needs d₊d₋ = h_p, i.e. squarefree h_p, H6). -/
theorem mul_le_max_sq (dp dm : ℕ) : dp * dm ≤ (max dp dm) ^ 2 := by
  rcases le_total dp dm with h | h
  · rw [max_eq_right h, sq]; exact Nat.mul_le_mul_right _ h
  · rw [max_eq_left h, sq]; exact Nat.mul_le_mul_left _ h

/-! ### Polymer gap lemma: the explicit constant -/

lemma geom_e_lt (K : ℕ) : Phi (K + 1) e < e ^ (K + 1) / √2 := by
  have k := Phi_mul (K + 1) e
  have he1 : e - 1 = √2 := by unfold e; ring
  rw [he1] at k
  rw [lt_div_iff₀ s2pos, k]; linarith

lemma geom_f_lt (K : ℕ) : Phi (K + 1) |f| < 1 / (2 - √2) := by
  have k := Phi_mul (K + 1) |f|
  rw [abs_f] at k ⊢
  have hpos : 0 < 2 - √2 := by linarith [s2lt]
  have hq : 0 ≤ √2 - 1 := by linarith [s2gt1]
  have hpow : 0 < (√2 - 1) ^ (K + 1) := pow_pos (by linarith [s2gt1]) _
  rw [lt_div_iff₀ hpos]
  have : Phi (K + 1) (√2 - 1) * (2 - √2) = 1 - (√2 - 1) ^ (K + 1) := by linear_combination -k
  linarith

/-- |∑ a_k x^k| ≤ A ∑ |x|^k when |a_k| ≤ A. -/
lemma abs_poly_le (K : ℕ) (a : ℕ → ℤ) (A : ℝ) (ha : ∀ k, |(a k : ℝ)| ≤ A) (x : ℝ) :
    |∑ k ∈ range (K + 1), (a k : ℝ) * x ^ k| ≤ A * Phi (K + 1) |x| := by
  unfold Phi; rw [mul_sum]
  refine (abs_sum_le_sum_abs _ _).trans (sum_le_sum fun k _ => ?_)
  rw [abs_mul, abs_pow]; exact mul_le_mul_of_nonneg_right (ha k) (by positivity)

/-- For |a_k| ≤ A (A > 0), σ = ±1 and F = ∑_{k ≤ K} a_k x^k: |F(σε)|·|F(σε̄)| < A² ε^{K+2}/2. -/
theorem polymer_norm_lt (K : ℕ) (a : ℕ → ℤ) (A : ℝ) (hA : 0 < A) (ha : ∀ k, |(a k : ℝ)| ≤ A)
    (σ : ℝ) (hσ : σ = 1 ∨ σ = -1) :
    |∑ k ∈ range (K + 1), (a k : ℝ) * (σ * e) ^ k| * |∑ k ∈ range (K + 1), (a k : ℝ) * (σ * f) ^ k|
      < A ^ 2 * e ^ (K + 2) / 2 := by
  have hσ1 : |σ| = 1 := by rcases hσ with rfl | rfl <;> norm_num
  have h1 := abs_poly_le K a A ha (σ * e)
  have h2 := abs_poly_le K a A ha (σ * f)
  rw [abs_mul, hσ1, one_mul, abs_of_pos e_pos] at h1
  rw [abs_mul, hσ1, one_mul] at h2
  have g1 := geom_e_lt K
  have g2 := geom_f_lt K
  have p1 : 0 ≤ Phi (K + 1) e := by unfold Phi; exact sum_nonneg fun i _ => pow_nonneg e_pos.le _
  have p2 : 0 < Phi (K + 1) |f| := by
    unfold Phi; rw [sum_range_succ']; simp only [pow_zero]
    exact add_pos_of_nonneg_of_pos (sum_nonneg fun i _ => pow_nonneg (abs_nonneg _) _) one_pos
  have hpos : 0 < 2 - √2 := by linarith [s2lt]
  have hk : √2 * (2 - √2) * e = 2 := by unfold e; linear_combination (1 - √2) * s2sq
  have hid : e ^ (K + 1) / √2 * (1 / (2 - √2)) = e ^ (K + 2) / 2 := by
    rw [div_mul_div_comm, mul_one, div_eq_div_iff (mul_pos s2pos hpos).ne' (by norm_num), pow_succ e (K + 1)]
    linear_combination (-(e ^ (K + 1))) * hk
  calc _ ≤ (A * Phi (K + 1) e) * (A * Phi (K + 1) |f|) :=
        mul_le_mul h1 h2 (abs_nonneg _) (by positivity)
    _ = A ^ 2 * (Phi (K + 1) e * Phi (K + 1) |f|) := by ring
    _ < A ^ 2 * (e ^ (K + 1) / √2 * (1 / (2 - √2))) := by
        apply mul_lt_mul_of_pos_left _ (by positivity)
        calc Phi (K + 1) e * Phi (K + 1) |f| ≤ (e ^ (K + 1) / √2) * Phi (K + 1) |f| :=
              mul_le_mul_of_nonneg_right g1.le p2.le
          _ < (e ^ (K + 1) / √2) * (1 / (2 - √2)) :=
              mul_lt_mul_of_pos_left g2 (by have := e_pos; positivity)
    _ = A ^ 2 * e ^ (K + 2) / 2 := by rw [hid]; ring

/-- The gap: d ≥ 1 and d < A² ε^{K+2}/2 imply K > log_ε d − 2 log_ε A − log_ε(ε²/2). -/
theorem polymer_gap (K d : ℕ) (A : ℝ) (hA : 0 < A) (hd : 1 ≤ d) (hlt : (d : ℝ) < A ^ 2 * e ^ (K + 2) / 2) :
    logb e d - 2 * logb e A - logb e (e ^ 2 / 2) < K := by
  have hL : 0 < Real.log e := Real.log_pos one_lt_e
  have hd0 : (0 : ℝ) < d := by exact_mod_cast hd
  have key := Real.log_lt_log hd0 hlt
  have hA2 : A ^ 2 ≠ 0 := (pow_pos hA 2).ne'
  have hE2 : e ^ (K + 2) ≠ 0 := (pow_pos e_pos _).ne'
  rw [Real.log_div (mul_ne_zero hA2 hE2) (by norm_num), Real.log_mul hA2 hE2,
    Real.log_pow, Real.log_pow] at key
  have h2 : Real.log (e ^ 2 / 2) = 2 * Real.log e - Real.log 2 := by
    rw [Real.log_div (pow_pos e_pos 2).ne' (by norm_num), Real.log_pow]; push_cast; ring
  simp only [Real.logb]
  rw [h2]
  have : (Real.log d - 2 * Real.log A - (2 * Real.log e - Real.log 2)) / Real.log e < K := by
    rw [div_lt_iff₀ hL]; push_cast at key; nlinarith
  calc _ = (Real.log d - 2 * Real.log A - (2 * Real.log e - Real.log 2)) / Real.log e := by
        field_simp
    _ < K := this

/-- Polymer gap, combined: if d ≥ 1 divides the norm N F(σε) = F(σε)·F(σε̄), so that d ≤ |F(σε)|·|F(σε̄)|,
and |a_k| ≤ A with A > 0, then K > log_ε d − 2 log_ε A − log_ε(ε²/2). -/
theorem polymer_gap_of_norm (K d : ℕ) (a : ℕ → ℤ) (A : ℝ) (hA : 0 < A) (ha : ∀ k, |(a k : ℝ)| ≤ A)
    (σ : ℝ) (hσ : σ = 1 ∨ σ = -1) (hd : 1 ≤ d)
    (hle : (d : ℝ) ≤ |∑ k ∈ range (K + 1), (a k : ℝ) * (σ * e) ^ k| *
      |∑ k ∈ range (K + 1), (a k : ℝ) * (σ * f) ^ k|) :
    logb e d - 2 * logb e A - logb e (e ^ 2 / 2) < K :=
  polymer_gap K d A hA hd (hle.trans_lt (polymer_norm_lt K a A hA ha σ hσ))

lemma h103 : 2 * h 103 + 1 < 2 ^ 131 := by decide +kernel
lemma h59 : 2 ^ 75 < 2 * h 59 := by decide +kernel

lemma f_pow_odd_neg {n : ℕ} (hn : Odd n) : f ^ n < 0 ∧ -1 < f ^ n := by
  have hf : f < 0 := by unfold f; linarith [s2gt1]
  have hf1 : -1 < f := by unfold f; linarith [s2lt]
  refine ⟨hn.pow_neg hf, ?_⟩
  have : |f| < 1 := by rw [abs_lt]; constructor <;> linarith
  have h1 : |f ^ n| < 1 := by rw [abs_pow]; exact pow_lt_one₀ (abs_nonneg _) this (by obtain ⟨k, rfl⟩ := hn; omega)
  exact (abs_lt.1 h1).1

/-- log_ε(ε²/2) < 1.214 (it is 1.21355...). -/
theorem logb_const_lt : logb e (e ^ 2 / 2) < 1.214 := by
  have hL : 0 < Real.log e := Real.log_pos one_lt_e
  have hc := h_closed 103
  obtain ⟨-, hneg⟩ := f_pow_odd_neg (n := 103) ⟨51, rfl⟩
  have hlt : e ^ 103 < 2 ^ 131 := by
    have : ((2 * h 103 + 1 : ℕ) : ℝ) < ((2 ^ 131 : ℕ) : ℝ) := by exact_mod_cast h103
    push_cast at this; linarith
  have hlog : 103 * Real.log e < 131 * Real.log 2 := by
    have := Real.log_lt_log (by have := e_pos; positivity) hlt
    rwa [Real.log_pow, Real.log_pow] at this
  have h2 : Real.log (e ^ 2 / 2) = 2 * Real.log e - Real.log 2 := by
    rw [Real.log_div (by have := e_pos; positivity) (by norm_num), Real.log_pow]; push_cast; ring
  have hl2 : 0 < Real.log 2 := Real.log_pos (by norm_num)
  rw [Real.logb, h2, div_lt_iff₀ hL]; nlinarith

/-- 1.213 < log_ε(ε²/2). -/
theorem logb_const_gt : 1.213 < logb e (e ^ 2 / 2) := by
  have hL : 0 < Real.log e := Real.log_pos one_lt_e
  have hc := h_closed 59
  obtain ⟨hneg, -⟩ := f_pow_odd_neg (n := 59) ⟨29, rfl⟩
  have hgt : 2 ^ 75 < e ^ 59 := by
    have : ((2 ^ 75 : ℕ) : ℝ) < ((2 * h 59 : ℕ) : ℝ) := by exact_mod_cast h59
    push_cast at this; linarith
  have hlog : 75 * Real.log 2 < 59 * Real.log e := by
    have := Real.log_lt_log (by positivity) hgt
    rwa [Real.log_pow, Real.log_pow] at this
  have h2 : Real.log (e ^ 2 / 2) = 2 * Real.log e - Real.log 2 := by
    rw [Real.log_div (by have := e_pos; positivity) (by norm_num), Real.log_pow]; push_cast; ring
  rw [Real.logb, h2, lt_div_iff₀ hL]; nlinarith

end Bgs.LemmaSArith

#print axioms Bgs.LemmaSArith.h_closed
#print axioms Bgs.LemmaSArith.phi_eps
#print axioms Bgs.LemmaSArith.phi_neg_eps
#print axioms Bgs.LemmaSArith.phi_lambda
#print axioms Bgs.LemmaSArith.prod_eta
#print axioms Bgs.LemmaSArith.prod_kernel
#print axioms Bgs.LemmaSArith.ht_eq_max
#print axioms Bgs.LemmaSArith.norm_le_ht
#print axioms Bgs.LemmaSArith.axis_bound
#print axioms Bgs.LemmaSArith.lemmaS_core_sub
#print axioms Bgs.LemmaSArith.lemmaS_core_add
#print axioms Bgs.LemmaSArith.mul_le_max_sq
#print axioms Bgs.LemmaSArith.polymer_norm_lt
#print axioms Bgs.LemmaSArith.polymer_gap
#print axioms Bgs.LemmaSArith.polymer_gap_of_norm
#print axioms Bgs.LemmaSArith.logb_const_lt
#print axioms Bgs.LemmaSArith.logb_const_gt
