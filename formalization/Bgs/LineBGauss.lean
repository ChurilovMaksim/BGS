import Bgs.LineBTraceFormula
-- NOTE: no `import Mathlib` here on purpose: the probe file `ProbeGauss2.lean`
-- (importing only `Bgs.LineBTraceFormula`) resolved every §2 name below, and a
-- full-Mathlib import costs ~25 min per build on this VM versus ~2 min without
-- it. If a later section needs a name outside this import closure, add the
-- single targeted Mathlib import for it (never the whole of Mathlib).

/-!
# Line B: the Gauss step for the trace formula (163)

This module closes the `hGauss` hypothesis of
`Bgs.LineB.TraceFormula.trace_formula_finite` (the Gauss step of
`phase1_trace_formula.md` §3), up to one explicit expansion hypothesis
`hExpand` (see `trace_formula_via_gauss`): the trace of the product is
the finite Gauss-sum expression. The operator-theoretic expansion itself
(Fourier series of the kick, absolute convergence, sum swap) is not
formalized here; everything after it — completing the square, the
phase identification via `HXphi`/`quadId`, and the norm `‖G(0)‖` —
is proved.

Contents:
- §1: the additive character `χ_N` on `ZMod N` and its basic lemmas.
- §2: finite quadratic Gauss sums and completing the square.
- §3: the norm `‖G(0)‖² = N^m` by the double-sum trick (no CRT needed).
- §4: specialization to `Hmat`, phase identification, and the bridge
  to `trace_formula_finite`.

No `sorry`, no `axiom`, no `native_decide` anywhere in this file.
-/

namespace Bgs
namespace LineB
namespace Gauss

open Bgs.LineB.TraceFormula
open Matrix

/-! ### §1. The additive character -/

/-- The additive character `χ_N(u) = e(u/N)` on `ZMod N`,
with `e` the exponential phase of `LineBTraceFormula`. -/
noncomputable def chi (N : ℕ) (u : ZMod N) : ℂ :=
  e ((((u.val : ℚ) / (N : ℚ) : ℚ) : ℝ))

/-- `e` is additive in its argument. -/
lemma e_add' (s t : ℝ) : e (s + t) = e s * e t := by
  -- NOTE: the cast must stay around `s + t` as a whole: `↑s + ↑t` is not
  -- definitionally equal to `↑(s + t)`, so the `show` pattern needs `((s + t : ℝ) : ℂ)`.
  show Complex.exp (2 * Real.pi * Complex.I * ((s + t : ℝ) : ℂ))
    = Complex.exp (2 * Real.pi * Complex.I * s)
      * Complex.exp (2 * Real.pi * Complex.I * t)
  rw [show 2 * Real.pi * Complex.I * ((s + t : ℝ) : ℂ)
    = 2 * Real.pi * Complex.I * s + 2 * Real.pi * Complex.I * t by push_cast; ring]
  exact Complex.exp_add _ _

/-- `e` at `0` is `1`. -/
lemma e_zero' : e 0 = 1 := by
  show Complex.exp (2 * Real.pi * Complex.I * (0 : ℝ)) = 1
  simp

/-- `e` at an integer is `1`. -/
lemma e_int' (k : ℤ) : e (k : ℝ) = 1 := by
  show Complex.exp (2 * Real.pi * Complex.I * (k : ℝ)) = 1
  rw [show 2 * Real.pi * Complex.I * (k : ℝ)
    = (k : ℂ) * (2 * Real.pi * Complex.I) by push_cast; ring]
  exact Complex.exp_int_mul_two_pi_mul_I k

/-- `e` at a negated argument is the inverse. -/
lemma e_neg' (t : ℝ) : e (-t) = (e t)⁻¹ := by
  have h := e_add' t (-t)
  rw [add_neg_cancel, e_zero'] at h
  -- `h : 1 = e t * e (-t)`; the lemma wants the product in the other order.
  have h2 : e (-t) * e t = 1 := by
    rw [mul_comm]
    exact h.symm
  exact eq_inv_of_mul_eq_one_left h2

/-- Complex conjugation of `e`: `conj (e t) = e (-t)` for real `t`.
(`Complex.conj_exp` does not exist in Mathlib 4.33.1, so this goes through
`Complex.exp_mul_I` and `cos`/`sin` of the real argument.) -/
lemma e_conj' (t : ℝ) : starRingEnd ℂ (e t) = e (-t) := by
  show starRingEnd ℂ (Complex.exp (2 * Real.pi * Complex.I * t))
    = Complex.exp (2 * Real.pi * Complex.I * ((-t : ℝ) : ℂ))
  have ht : (2 * Real.pi * Complex.I * (t : ℂ))
      = ((2 * Real.pi * t : ℝ) : ℂ) * Complex.I := by
    push_cast
    ring
  have ht' : (2 * Real.pi * Complex.I * ((-t : ℝ) : ℂ))
      = ((2 * Real.pi * (-t) : ℝ) : ℂ) * Complex.I := by
    push_cast
    ring
  rw [ht, ht', Complex.exp_mul_I, Complex.exp_mul_I]
  -- The negation sits inside a product (`2 * π * (-t)`), so `cos_neg`/`sin_neg`
  -- cannot fire until it is pulled out as a top-level negation.
  have harg : (2 * Real.pi * (-t) : ℝ) = -(2 * Real.pi * t) := by ring
  rw [harg]
  -- NOTE: `Complex.ofReal_neg` must NOT be in this simp set: it would pull the
  -- negation out of the cast (`↑(-X) ↦ -↑X`) before `← Complex.ofReal_cos`
  -- can fire, leaving `Complex.cos (-↑X)` with `cos_neg` unable to match.
  -- So: first `ofReal_cos/sin` + `cos_neg/sin_neg`, then `ofReal_neg` alone.
  simp only [← Complex.ofReal_cos, ← Complex.ofReal_sin, map_add, map_mul,
    Complex.conj_ofReal, Complex.conj_I, Real.cos_neg, Real.sin_neg]
  simp only [Complex.ofReal_neg]
  ring

/-- `χ_N` is a character: `χ(u + v) = χ(u) * χ(v)`. -/
lemma chi_add {N : ℕ} [NeZero N] (u v : ZMod N) :
    chi N (u + v) = chi N u * chi N v := by
  have hNQ : (N : ℚ) ≠ 0 := by exact_mod_cast NeZero.ne N
  have hval : (u + v).val = (u.val + v.val) % N := ZMod.val_add u v
  have hdiv : u.val + v.val = N * ((u.val + v.val) / N) + (u.val + v.val) % N :=
    (Nat.div_add_mod (u.val + v.val) N).symm
  have hQ : (((u + v).val : ℚ) / (N : ℚ))
      = ((u.val : ℚ) / (N : ℚ)) + ((v.val : ℚ) / (N : ℚ))
        - (((u.val + v.val) / N : ℕ) : ℚ) := by
    have h2 : (((u.val + v.val : ℕ) : ℚ))
        = (N : ℚ) * (((u.val + v.val) / N : ℕ) : ℚ)
          + ((((u.val + v.val) % N : ℕ)) : ℚ) := by
      exact_mod_cast hdiv
    rw [← hval] at h2
    have h3 : (((u + v).val : ℚ))
        = (((u.val + v.val : ℕ) : ℚ))
          - (N : ℚ) * (((u.val + v.val) / N : ℕ) : ℚ) := by
      rw [h2]
      ring
    rw [h3, Nat.cast_add, sub_div, mul_div_cancel_left₀ _ hNQ, add_div]
  have hneg : e (-((((u.val + v.val) / N : ℕ)) : ℝ)) = 1 := by
    -- `e_int'` forces the negation to elaborate in ℤ (its argument type is ℤ),
    -- avoiding the ascription trap where `(-x : ℝ)` elaborates the negation at ℝ.
    have h := e_int' (-(((u.val + v.val) / N : ℕ) : ℤ))
    rwa [Int.cast_neg, Int.cast_natCast] at h
  show e ((((u + v).val : ℚ) / (N : ℚ) : ℚ) : ℝ)
    = e ((((u.val : ℚ) / (N : ℚ) : ℚ) : ℝ))
      * e ((((v.val : ℚ) / (N : ℚ) : ℚ) : ℝ))
  rw [hQ]
  -- NOTE: no `push_cast` here: it rewrites Nat-division casts into Rat-division
  -- form, which breaks the `hneg` match below. The explicit `Rat.cast_*` simp set
  -- normalizes both sides consistently instead.
  simp only [Rat.cast_add, Rat.cast_sub, Rat.cast_div, Rat.cast_natCast]
  rw [sub_eq_add_neg, e_add', hneg, mul_one, e_add']

/-- `χ_N(0) = 1`. -/
lemma chi_zero {N : ℕ} : chi N 0 = 1 := by
  show e ((((0 : ZMod N).val : ℚ) / (N : ℚ) : ℚ) : ℝ) = 1
  simp [e_zero']

/-- `χ_N` of an integer cast equals `e` of the rational phase. -/
lemma chi_int {N : ℕ} [NeZero N] (k : ℤ) :
    chi N ((k : ℤ) : ZMod N) = e (((k : ℚ) / (N : ℚ) : ℚ) : ℝ) := by
  have hNQ : (N : ℚ) ≠ 0 := by exact_mod_cast NeZero.ne N
  -- NOTE: `Int.emod_modEq` / `Int.ediv_add_emod` do not exist in Lean 4.33.1;
  -- the div/mod identity is `Int.mul_ediv_add_emod : b * (a / b) + a % b = a`.
  have hmod : ((k : ℤ) : ZMod N) = (((k % (N : ℤ) : ℤ)) : ZMod N) := by
    rw [ZMod.intCast_eq_intCast_iff, Int.modEq_iff_dvd]
    refine ⟨-(k / (N : ℤ)), ?_⟩
    have hid := Int.mul_ediv_add_emod k (N : ℤ)
    calc k % (N : ℤ) - k
        = ((N : ℤ) * (k / (N : ℤ)) + k % (N : ℤ)) - (N : ℤ) * (k / (N : ℤ)) - k := by
          ring
      _ = k - (N : ℤ) * (k / (N : ℤ)) - k := by rw [hid]
      _ = (N : ℤ) * -(k / (N : ℤ)) := by rw [mul_neg]; ring
  -- NOTE: `((k % (N : ℤ) : ℚ))` does NOT mean what it looks like: the outer
  -- `: ℚ` ascription makes `%` elaborate at ℚ (Euclidean-domain mod on a field,
  -- which is 0 for nonzero divisor), not as integer mod cast to ℚ. The double
  -- ascription `(((k % (N : ℤ)) : ℤ) : ℚ)` forces `%` to elaborate in ℤ first.
  have hvalQ : (((((k % (N : ℤ) : ℤ)) : ZMod N).val : ℚ))
      = ((((k % (N : ℤ)) : ℤ) : ℚ)) := by
    have h1 : ((((k % (N : ℤ) : ℤ)) : ZMod N).val : ℤ)
        = k % (N : ℤ) := by
      rw [ZMod.val_intCast, Int.emod_emod_of_dvd k (dvd_refl _)]
    have h2 := congrArg (fun z : ℤ => (z : ℚ)) h1
    rwa [Int.cast_natCast] at h2
  have hediv : (k : ℚ)
      = (N : ℚ) * ((k / (N : ℤ) : ℤ) : ℚ) + (((k % (N : ℤ)) : ℤ) : ℚ) := by
    have hid := Int.mul_ediv_add_emod k (N : ℤ)
    have h2 := congrArg (fun z : ℤ => (z : ℚ)) hid
    -- No `push_cast` here: it would rewrite the integer mod cast into
    -- Euclidean mod on ℚ (see the note at `hvalQ`).
    rw [Int.cast_add, Int.cast_mul, Int.cast_natCast] at h2
    exact h2.symm
  have hrat : ((k : ℚ) / (N : ℚ))
      = ((((k % (N : ℤ)) : ℤ) : ℚ) / (N : ℚ)) + ((k / (N : ℤ) : ℤ) : ℚ) := by
    rw [hediv]
    field_simp
    ring
  show e (((( ((k : ℤ) : ZMod N).val : ℚ) / (N : ℚ) : ℚ) : ℝ))
    = e ((((k : ℚ) / (N : ℚ) : ℚ) : ℝ))
  rw [hmod]
  have hval : (((((k % (N : ℤ) : ℤ)) : ZMod N).val : ℚ) / (N : ℚ))
      = ((((k % (N : ℤ)) : ℤ) : ℚ) / (N : ℚ)) := by
    rw [hvalQ]
  rw [hval, hrat]
  push_cast
  rw [e_add', e_int', mul_one]

/-- `χ_N(u) ≠ 1` for `u ≠ 0`: the character is nontrivial. -/
lemma chi_ne_one {N : ℕ} [NeZero N] {u : ZMod N} (hu : u ≠ 0) :
    chi N u ≠ 1 := by
  intro h
  have hval0 : u.val ≠ 0 := by
    intro hv
    apply hu
    have h1 := ZMod.natCast_zmod_val u
    rw [hv] at h1
    simpa using h1.symm
  have hlt : u.val < N := ZMod.val_lt u
  have hpos : 0 < u.val := Nat.pos_of_ne_zero hval0
  obtain ⟨k, hk⟩ := (e_eq_one_iff _).mp h
  have hQ : ((u.val : ℚ) / (N : ℚ)) = (k : ℚ) := by
    exact_mod_cast hk
  have hNq : (0 : ℚ) < (N : ℚ) :=
    by exact_mod_cast Nat.pos_of_ne_zero (NeZero.ne N)
  have hvalq : (0 : ℚ) < (u.val : ℚ) := by exact_mod_cast hpos
  have h1 : (0 : ℚ) < (k : ℚ) := by
    rw [← hQ]
    exact div_pos hvalq hNq
  have h2 : (k : ℚ) < 1 := by
    rw [← hQ, div_lt_one hNq]
    exact_mod_cast hlt
  have hk1 : (1 : ℤ) ≤ k := by exact_mod_cast h1
  have hk2 : k < 1 := by exact_mod_cast h2
  omega

section GaussSums

variable {ι : Type*} [Fintype ι] [DecidableEq ι] {N : ℕ} [NeZero N]

/-- Quadratic form of a matrix over `ZMod N`: `Q_H(x) = x ⬝ᵥ (H *ᵥ x)`. -/
noncomputable def Qform (H : Matrix ι ι (ZMod N)) (x : ι → ZMod N) : ZMod N :=
  x ⬝ᵥ (H *ᵥ x)

/-- Finite Gauss sum with linear term `n`:
`G_H(a, n) = ∑_x χ(a * Q_H(x) + n ⬝ᵥ x)`. -/
noncomputable def Gsum (H : Matrix ι ι (ZMod N)) (a : ZMod N) (n : ι → ZMod N) : ℂ :=
  ∑ x, chi N (a * Qform H x + n ⬝ᵥ x)

/-- Cross term under a symmetric matrix: `t ⬝ᵥ (H *ᵥ y) = (H *ᵥ t) ⬝ᵥ y`.
Proved by direct double-sum manipulation (the `vecMul` route would need
the same symmetry argument anyway). -/
lemma dotProduct_mulVec_symm {H : Matrix ι ι (ZMod N)} (hH : Hᵀ = H)
    (t y : ι → ZMod N) : t ⬝ᵥ (H *ᵥ y) = (H *ᵥ t) ⬝ᵥ y := by
  simp only [dotProduct, Matrix.mulVec, Finset.mul_sum, Finset.sum_mul]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro j _
  apply Finset.sum_congr rfl
  intro i _
  have hij : H j i = H i j := by
    have h1 := congrFun (congrFun hH j) i
    rw [Matrix.transpose_apply] at h1
    exact h1.symm
  rw [hij]
  ring

/-- The shift vector `t = t0 • (Hinv *ᵥ n)` satisfies `H *ᵥ t = t0 • n`. -/
lemma mulVec_shift {H Hinv : Matrix ι ι (ZMod N)} (hHinv : H * Hinv = 1)
    (t0 : ZMod N) (n : ι → ZMod N) :
    H *ᵥ (t0 • (Hinv *ᵥ n)) = t0 • n := by
  rw [mulVec_smul]
  congr 1
  rw [mulVec_mulVec, hHinv, one_mulVec]

/-- The shift vector dotted with `n` is `t0` times the inverse form. -/
lemma dotProduct_shift_self {Hinv : Matrix ι ι (ZMod N)}
    (t0 : ZMod N) (n : ι → ZMod N) :
    (t0 • (Hinv *ᵥ n)) ⬝ᵥ n = t0 * (n ⬝ᵥ (Hinv *ᵥ n)) := by
  rw [smul_dotProduct]
  simp only [smul_eq_mul]
  rw [dotProduct_comm]

/-- The quadratic form of the shift vector. -/
lemma Qform_shift {H Hinv : Matrix ι ι (ZMod N)} (hHinv : H * Hinv = 1)
    (t0 : ZMod N) (n : ι → ZMod N) :
    Qform H (t0 • (Hinv *ᵥ n)) = t0 ^ 2 * (n ⬝ᵥ (Hinv *ᵥ n)) := by
  show (t0 • (Hinv *ᵥ n)) ⬝ᵥ (H *ᵥ (t0 • (Hinv *ᵥ n)))
      = t0 ^ 2 * (n ⬝ᵥ (Hinv *ᵥ n))
  rw [mulVec_shift hHinv, dotProduct_smul]
  simp only [smul_eq_mul]
  rw [dotProduct_shift_self]
  ring

/-- Pointwise completing the square: the phase at `y - t` equals the phase
at `y` plus the constant `(a * t0 ^ 2 - t0) * (n ⬝ᵥ (Hinv *ᵥ n))`; the
linear term in `y` cancels exactly because `2 * a * t0 = 1`. -/
lemma phase_shift {H Hinv : Matrix ι ι (ZMod N)} (hH : Hᵀ = H)
    (a t0 : ZMod N) (ht0 : 2 * a * t0 = 1) (n t : ι → ZMod N)
    (hHt : H *ᵥ t = t0 • n) (htn : t ⬝ᵥ n = t0 * (n ⬝ᵥ (Hinv *ᵥ n)))
    (hQt : Qform H t = t0 ^ 2 * (n ⬝ᵥ (Hinv *ᵥ n))) (y : ι → ZMod N) :
    a * Qform H (y - t) + n ⬝ᵥ (y - t)
      = a * Qform H y + (a * t0 ^ 2 - t0) * (n ⬝ᵥ (Hinv *ᵥ n)) := by
  have hByt : y ⬝ᵥ (H *ᵥ t) = t0 * (n ⬝ᵥ y) := by
    rw [hHt, dotProduct_smul, dotProduct_comm]
    simp only [smul_eq_mul]
  have hBty : t ⬝ᵥ (H *ᵥ y) = t0 * (n ⬝ᵥ y) := by
    rw [dotProduct_mulVec_symm hH, hHt, smul_dotProduct]
    simp only [smul_eq_mul]
  have hQ : Qform H (y - t)
      = Qform H y - t0 * (n ⬝ᵥ y) - t0 * (n ⬝ᵥ y) + Qform H t := by
    show (y - t) ⬝ᵥ (H *ᵥ (y - t))
        = y ⬝ᵥ (H *ᵥ y) - t0 * (n ⬝ᵥ y) - t0 * (n ⬝ᵥ y) + t ⬝ᵥ (H *ᵥ t)
    rw [mulVec_sub, sub_dotProduct, dotProduct_sub, dotProduct_sub, hByt, hBty]
    ring
  have hndot : n ⬝ᵥ (y - t) = n ⬝ᵥ y - t0 * (n ⬝ᵥ (Hinv *ᵥ n)) := by
    rw [dotProduct_sub, dotProduct_comm n t, htn]
  have key : a * (t0 * (n ⬝ᵥ y)) + a * (t0 * (n ⬝ᵥ y)) = n ⬝ᵥ y := by
    have hring : a * (t0 * (n ⬝ᵥ y)) + a * (t0 * (n ⬝ᵥ y))
        = (2 * a * t0) * (n ⬝ᵥ y) := by ring
    rw [hring, ht0, one_mul]
  rw [hQ, hQt, hndot]
  calc a * (Qform H y - t0 * (n ⬝ᵥ y) - t0 * (n ⬝ᵥ y)
          + t0 ^ 2 * (n ⬝ᵥ (Hinv *ᵥ n)))
          + (n ⬝ᵥ y - t0 * (n ⬝ᵥ (Hinv *ᵥ n)))
      = a * Qform H y + (a * t0 ^ 2 - t0) * (n ⬝ᵥ (Hinv *ᵥ n))
          + (n ⬝ᵥ y - (a * (t0 * (n ⬝ᵥ y)) + a * (t0 * (n ⬝ᵥ y)))) := by ring
    _ = a * Qform H y + (a * t0 ^ 2 - t0) * (n ⬝ᵥ (Hinv *ᵥ n)) := by
        rw [key, sub_self, add_zero]

/-- Translation of the function space by `t` (used to reindex Gauss sums). -/
def transEquiv (t : ι → ZMod N) : (ι → ZMod N) ≃ (ι → ZMod N) where
  toFun y := y - t
  invFun x := x + t
  left_inv y := sub_add_cancel y t
  right_inv x := add_sub_cancel_right x t

lemma transEquiv_apply (t y : ι → ZMod N) : (transEquiv t) y = y - t := rfl

/-- Completing the square for finite Gauss sums (source §3, first step):
`G(a, n) = χ((a * t0 ^ 2 - t0) * (n ⬝ᵥ (Hinv *ᵥ n))) * G(a, 0)`,
whenever `H` is symmetric, `H * Hinv = 1`, and `2 * a * t0 = 1`. -/
theorem gauss_sum_shift {H Hinv : Matrix ι ι (ZMod N)} (hH : Hᵀ = H)
    (hHinv : H * Hinv = 1) (a t0 : ZMod N) (ht0 : 2 * a * t0 = 1)
    (n : ι → ZMod N) :
    Gsum H a n
      = chi N ((a * t0 ^ 2 - t0) * (n ⬝ᵥ (Hinv *ᵥ n))) * Gsum H a 0 := by
  have hHt : H *ᵥ (t0 • (Hinv *ᵥ n)) = t0 • n := mulVec_shift hHinv t0 n
  have htn : (t0 • (Hinv *ᵥ n)) ⬝ᵥ n = t0 * (n ⬝ᵥ (Hinv *ᵥ n)) :=
    dotProduct_shift_self t0 n
  have hQt : Qform H (t0 • (Hinv *ᵥ n)) = t0 ^ 2 * (n ⬝ᵥ (Hinv *ᵥ n)) :=
    Qform_shift hHinv t0 n
  have hreindex : (∑ y, chi N (a * Qform H (y - t0 • (Hinv *ᵥ n))
        + n ⬝ᵥ (y - t0 • (Hinv *ᵥ n)))) = Gsum H a n := by
    unfold Gsum
    exact Equiv.sum_comp (transEquiv (t0 • (Hinv *ᵥ n)))
      (fun x => chi N (a * Qform H x + n ⬝ᵥ x))
  have hsum : Gsum H a n = ∑ y, chi N (a * Qform H y
      + (a * t0 ^ 2 - t0) * (n ⬝ᵥ (Hinv *ᵥ n))) := by
    rw [← hreindex]
    apply Finset.sum_congr rfl
    intro y _
    rw [phase_shift hH a t0 ht0 n (t0 • (Hinv *ᵥ n)) hHt htn hQt y]
  have hG0 : Gsum H a 0 = ∑ y, chi N (a * Qform H y) := by
    unfold Gsum
    apply Finset.sum_congr rfl
    intro y _
    rw [zero_dotProduct, add_zero]
  have step1 : (∑ y, chi N (a * Qform H y
        + (a * t0 ^ 2 - t0) * (n ⬝ᵥ (Hinv *ᵥ n))))
      = (∑ y, chi N (a * Qform H y))
        * chi N ((a * t0 ^ 2 - t0) * (n ⬝ᵥ (Hinv *ᵥ n))) := by
    rw [Finset.sum_mul]
    apply Finset.sum_congr rfl
    intro y _
    rw [chi_add]
  rw [hsum, hG0, step1, mul_comm]

end GaussSums

/- §3: Norm of the zero-linear-term Gauss sum, without CRT.
The double-sum trick replaces the source's CRT + prime-power diagonalization
(source §3: "diagonalize over Z/p^kZ ... then multiply over p^k by CRT").
Survival only at `u = 0` comes from character orthogonality (`sum_chi_dotProduct`)
plus two-sided invertibility of `H`. -/

section NormComputation

variable {ι : Type*} [Fintype ι] [DecidableEq ι] {N : ℕ} [NeZero N]

/-- Conjugation of the character: `conj (χ u) = χ (-u)`. -/
lemma chi_conj (u : ZMod N) : starRingEnd ℂ (chi N u) = chi N (-u) := by
  show starRingEnd ℂ (e ((((u.val : ℚ) / (N : ℚ) : ℚ) : ℝ)))
      = e (((((-u).val : ℚ) / (N : ℚ) : ℚ) : ℝ))
  rw [e_conj']
  by_cases hu : u = 0
  · subst hu
    simp
  · have hval : (-u).val = N - u.val := by
      haveI : NeZero u := ⟨hu⟩
      exact ZMod.val_neg_of_ne_zero u
    rw [hval]
    have hNq : (N : ℚ) ≠ 0 := by exact_mod_cast NeZero.ne N
    have hlt : u.val < N := ZMod.val_lt u
    have hcast : (((N - u.val : ℕ) : ℚ) / (N : ℚ))
        = 1 - ((u.val : ℚ) / (N : ℚ)) := by
      rw [Nat.cast_sub (le_of_lt hlt), sub_div, div_self hNq]
    rw [hcast]
    have harg : (((1 - ((u.val : ℚ) / (N : ℚ)) : ℚ) : ℝ))
        = 1 - (((u.val : ℚ) / (N : ℚ) : ℚ) : ℝ) := by
      push_cast
      ring
    -- Robust finale: `e_int'` does not match `e 1` syntactically, so prove
    -- `e 1 = 1` explicitly via `Int.cast_one` first.
    rw [harg, show (1 : ℝ) - (((u.val : ℚ) / (N : ℚ) : ℚ) : ℝ)
      = (-(((u.val : ℚ) / (N : ℚ) : ℚ) : ℝ)) + 1 by ring, e_add']
    have he1 : e (1 : ℝ) = 1 := by
      have h := e_int' 1
      rwa [Int.cast_one] at h
    rw [he1, mul_one]

/-- Translation of the function space by `t`, in the `+t` direction.
(`Equiv.addRight` is NOT used here: checking `⇑(addRight t) v = v + t` by
defeq times out on `isDefEq`; this plain structure instance unfolds by
`rfl`, exactly like `transEquiv` in §2.) -/
def addEquiv (t : ι → ZMod N) : (ι → ZMod N) ≃ (ι → ZMod N) where
  toFun v := v + t
  invFun v := v - t
  left_inv v := add_sub_cancel_right v t
  right_inv v := sub_add_cancel v t

lemma addEquiv_apply (t v : ι → ZMod N) : (addEquiv t) v = v + t := rfl

/-- Character orthogonality on the function space: the sum of `χ(w ⬝ᵥ v)`
over all `v` is `N ^ card ι` if `w = 0`, else `0`. No factorization over
coordinates is needed: if `w i ≠ 0`, translating `v ↦ v + Pi.single i 1`
multiplies the sum by `χ(w i) ≠ 1`. -/
lemma sum_chi_dotProduct (w : ι → ZMod N) :
    (∑ v, chi N (w ⬝ᵥ v)) = if w = 0 then (N : ℂ) ^ Fintype.card ι else 0 := by
  by_cases hw : w = 0
  · subst hw
    rw [if_pos rfl]
    simp only [zero_dotProduct, chi_zero, Finset.sum_const, Finset.card_univ,
      nsmul_eq_mul, mul_one]
    rw [Fintype.card_pi]
    simp [ZMod.card]
  · rw [if_neg hw]
    obtain ⟨i, hi⟩ : ∃ i, w i ≠ 0 := by
      by_contra h
      push_neg at h
      exact hw (funext h)
    have hdot : ∀ v, w ⬝ᵥ (v + Pi.single (M := fun _ : ι => ZMod N) i (1 : ZMod N)) = w ⬝ᵥ v + w i := by
      intro v
      rw [dotProduct_add]
      congr 1
      -- `w ⬝ᵥ Pi.single i 1 = w i` by a single-term sum. (Do NOT use
      -- `simp [dotProduct, ...]` here: unfolding `dotProduct` in `simp` times
      -- out on `whnf`; and do NOT use `show` with a fresh `Pi.single`: its
      -- family `M` cannot be inferred. `rw [dotProduct]` keeps the goal's
      -- already-elaborated `Pi.single`.)
      rw [dotProduct]
      rw [Finset.sum_eq_single i]
      · rw [Pi.single_eq_same, mul_one]
      · intro j _ hji
        rw [Pi.single_eq_of_ne hji, mul_zero]
      · intro hi
        exact absurd (Finset.mem_univ i) hi
    have h1 : (∑ v, chi N (w ⬝ᵥ v))
        = ∑ v, chi N (w ⬝ᵥ (v + Pi.single (M := fun _ : ι => ZMod N) i (1 : ZMod N))) := by
      have h := Equiv.sum_comp (addEquiv (Pi.single (M := fun _ : ι => ZMod N) i (1 : ZMod N)))
        (fun v => chi N (w ⬝ᵥ v))
      rw [← h]
      apply Finset.sum_congr rfl
      intro v _
      rw [addEquiv_apply]
    have h2 : chi N (w i) * (∑ v, chi N (w ⬝ᵥ v))
        = ∑ v, chi N (w ⬝ᵥ (v + Pi.single (M := fun _ : ι => ZMod N) i (1 : ZMod N))) := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro v _
      rw [hdot v, chi_add, mul_comm]
    have hkey : (∑ v, chi N (w ⬝ᵥ v))
        = chi N (w i) * (∑ v, chi N (w ⬝ᵥ v)) := h1.trans h2.symm
    have hchi : chi N (w i) ≠ 1 := chi_ne_one hi
    have hzero : (1 - chi N (w i)) * (∑ v, chi N (w ⬝ᵥ v)) = 0 := by
      rw [sub_mul, one_mul, ← hkey, sub_self]
    exact (mul_eq_zero.mp hzero).resolve_left (sub_ne_zero.mpr (Ne.symm hchi))

/-- Quadratic expansion: `Q(u + y) = Q(u) + 2 * (u ⬝ᵥ (H *ᵥ y)) + Q(y)`. -/
lemma Qform_add {H : Matrix ι ι (ZMod N)} (hH : Hᵀ = H) (u y : ι → ZMod N) :
    Qform H (u + y) = Qform H u + 2 * (u ⬝ᵥ (H *ᵥ y)) + Qform H y := by
  show (u + y) ⬝ᵥ (H *ᵥ (u + y))
      = u ⬝ᵥ (H *ᵥ u) + 2 * (u ⬝ᵥ (H *ᵥ y)) + y ⬝ᵥ (H *ᵥ y)
  rw [mulVec_add, add_dotProduct, dotProduct_add, dotProduct_add]
  have hcross : y ⬝ᵥ (H *ᵥ u) = u ⬝ᵥ (H *ᵥ y) := by
    rw [dotProduct_comm, dotProduct_mulVec_symm hH]
  rw [hcross]
  ring

/-- The squared norm of the zero-linear-term Gauss sum, without CRT:
`‖G(a, 0)‖² = N ^ card ι`, whenever `2 * a` is a unit (so the character
sum in the double-sum trick survives only at `u = 0`) and `H` has a
left inverse (`Hinv * H = 1` gives injectivity of `H *ᵥ ·`; the
other direction `H * Hinv = 1` is not needed here). -/
theorem gauss_sum_zero_norm_sq {H Hinv : Matrix ι ι (ZMod N)} (hH : Hᵀ = H)
    (hHinv' : Hinv * H = 1) (a : ZMod N)
    (h2a : ∃ b, 2 * a * b = 1) :
    ‖Gsum H a 0‖ ^ 2 = (N : ℝ) ^ Fintype.card ι := by
  have hG0 : Gsum H a 0 = ∑ x, chi N (a * Qform H x) := by
    unfold Gsum
    apply Finset.sum_congr rfl
    intro x _
    rw [zero_dotProduct, add_zero]
  have hconj : starRingEnd ℂ (Gsum H a 0)
      = ∑ y, chi N (-(a * Qform H y)) := by
    rw [hG0, map_sum]
    apply Finset.sum_congr rfl
    intro y _
    rw [chi_conj]
  have h3a : Gsum H a 0 * starRingEnd ℂ (Gsum H a 0)
      = ∑ x, ∑ y, chi N (a * (Qform H x - Qform H y)) := by
    rw [hconj, hG0, Finset.sum_mul_sum]
    apply Finset.sum_congr rfl
    intro x _
    apply Finset.sum_congr rfl
    intro y _
    rw [← chi_add]
    congr 1
    ring
  have h3b : (∑ x, ∑ y, chi N (a * (Qform H x - Qform H y)))
      = ∑ u, ∑ y, chi N (a * (Qform H (u + y) - Qform H y)) := by
    let e : (ι → ZMod N) × (ι → ZMod N) ≃ (ι → ZMod N) × (ι → ZMod N) :=
      { toFun := fun p => (p.1 + p.2, p.2)
        invFun := fun p => (p.1 - p.2, p.2)
        left_inv := fun p => by
          obtain ⟨a, b⟩ := p
          exact Prod.ext (add_sub_cancel_right a b) rfl
        right_inv := fun p => by
          obtain ⟨a, b⟩ := p
          exact Prod.ext (sub_add_cancel a b) rfl }
    calc (∑ x, ∑ y, chi N (a * (Qform H x - Qform H y)))
        = ∑ p ∈ (Finset.univ : Finset ((ι → ZMod N) × (ι → ZMod N))),
            chi N (a * (Qform H p.1 - Qform H p.2)) :=
          (Finset.sum_product' Finset.univ Finset.univ
            (fun x y => chi N (a * (Qform H x - Qform H y)))).symm
      _ = ∑ p ∈ (Finset.univ : Finset ((ι → ZMod N) × (ι → ZMod N))),
            chi N (a * (Qform H (p.1 + p.2) - Qform H p.2)) :=
          (Equiv.sum_comp e _).symm
      _ = ∑ u, ∑ y, chi N (a * (Qform H (u + y) - Qform H y)) :=
          Finset.sum_product' Finset.univ Finset.univ
            (fun u y => chi N (a * (Qform H (u + y) - Qform H y)))
  have h3c : ∀ u y, chi N (a * (Qform H (u + y) - Qform H y))
      = chi N (a * Qform H u) * chi N (((2 * a) • (H *ᵥ u)) ⬝ᵥ y) := by
    intro u y
    have hQ : Qform H (u + y) - Qform H y
        = Qform H u + 2 * (u ⬝ᵥ (H *ᵥ y)) := by
      rw [Qform_add hH]
      ring
    have hdot : ((2 * a) • (H *ᵥ u)) ⬝ᵥ y = 2 * a * (u ⬝ᵥ (H *ᵥ y)) := by
      rw [smul_dotProduct]
      simp only [smul_eq_mul]
      rw [← dotProduct_mulVec_symm hH]
    rw [hQ, hdot, ← chi_add]
    congr 1
    ring
  have h3d : (∑ u, ∑ y, chi N (a * Qform H u) * chi N (((2 * a) • (H *ᵥ u)) ⬝ᵥ y))
      = ∑ u, chi N (a * Qform H u)
        * (∑ y, chi N (((2 * a) • (H *ᵥ u)) ⬝ᵥ y)) := by
    apply Finset.sum_congr rfl
    intro u _
    rw [Finset.mul_sum]
  have hsurv : ∀ u : ι → ZMod N, (2 * a) • (H *ᵥ u) = 0 ↔ u = 0 := by
    intro u
    constructor
    · intro hu
      have hHu : H *ᵥ u = 0 := by
        obtain ⟨b, hb⟩ := h2a
        funext i
        have hi := congrFun hu i
        simp only [Pi.smul_apply, smul_eq_mul, Pi.zero_apply] at hi
        calc (H *ᵥ u) i = (b * (2 * a)) * (H *ᵥ u) i := by
                rw [mul_comm b (2 * a), hb, one_mul]
          _ = b * (2 * a * (H *ᵥ u) i) := by rw [mul_assoc]
          _ = 0 := by rw [hi, mul_zero]
      have h3 : Hinv *ᵥ (H *ᵥ u) = 0 := by rw [hHu, mulVec_zero]
      rw [mulVec_mulVec, hHinv', one_mulVec] at h3
      exact h3
    · intro hu
      rw [hu, mulVec_zero, smul_zero]
  have h3f : (∑ u, chi N (a * Qform H u)
        * (∑ y, chi N (((2 * a) • (H *ᵥ u)) ⬝ᵥ y)))
      = (N : ℂ) ^ Fintype.card ι := by
    have hinner : ∀ u, (∑ y, chi N (((2 * a) • (H *ᵥ u)) ⬝ᵥ y))
        = if u = 0 then (N : ℂ) ^ Fintype.card ι else 0 := by
      intro u
      rw [sum_chi_dotProduct]
      by_cases hu : u = 0
      · rw [if_pos hu, if_pos ((hsurv u).mpr hu)]
      · rw [if_neg hu, if_neg (fun h => hu ((hsurv u).mp h))]
    have hsum : (∑ u, chi N (a * Qform H u)
          * (∑ y, chi N (((2 * a) • (H *ᵥ u)) ⬝ᵥ y)))
        = ∑ u, chi N (a * Qform H u)
          * (if u = 0 then (N : ℂ) ^ Fintype.card ι else 0) := by
      apply Finset.sum_congr rfl
      intro u _
      rw [hinner u]
    rw [hsum, Finset.sum_eq_single (0 : ι → ZMod N)]
    · simp [Qform, mulVec_zero, chi_zero]
    · intro u _ hu0
      rw [if_neg hu0, mul_zero]
    · intro h0
      exact absurd (Finset.mem_univ (0 : ι → ZMod N)) h0
  have hnorm : Gsum H a 0 * starRingEnd ℂ (Gsum H a 0)
      = (((N : ℝ) ^ Fintype.card ι : ℝ) : ℂ) := by
    calc Gsum H a 0 * starRingEnd ℂ (Gsum H a 0)
        = ∑ x, ∑ y, chi N (a * (Qform H x - Qform H y)) := h3a
      _ = ∑ u, ∑ y, chi N (a * (Qform H (u + y) - Qform H y)) := h3b
      _ = ∑ u, ∑ y, chi N (a * Qform H u) * chi N (((2 * a) • (H *ᵥ u)) ⬝ᵥ y) := by
          apply Finset.sum_congr rfl
          intro u _
          apply Finset.sum_congr rfl
          intro y _
          exact h3c u y
      _ = ∑ u, chi N (a * Qform H u)
          * (∑ y, chi N (((2 * a) • (H *ᵥ u)) ⬝ᵥ y)) := h3d
      _ = (N : ℂ) ^ Fintype.card ι := h3f
      _ = (((N : ℝ) ^ Fintype.card ι : ℝ) : ℂ) := by
          push_cast
          ring
  have h1 : (Complex.normSq (Gsum H a 0) : ℂ)
      = (((N : ℝ) ^ Fintype.card ι : ℝ) : ℂ) := by
    rw [← Complex.mul_conj]
    exact hnorm
  have h2 : Complex.normSq (Gsum H a 0) = (N : ℝ) ^ Fintype.card ι :=
    Complex.ofReal_inj.mp h1
  rw [Complex.normSq_eq_norm_sq] at h2
  exact h2

end NormComputation

/- §4: Specialization to the frozen-map matrix and the bridge to
`trace_formula_finite` (source §3). The matrices are moved from ℤ to
`ZMod N` via `castHom`; the inverse of `Dm` mod `N` comes from coprimality
(`exists_inv_mod`, as in `trace_formula_finite` itself). The bridge
eliminates `hGauss` and closes `hMod` via the §3 norm; the only remaining
hypothesis for finite-sum Theorem 1(a) is `hExpand` (the trace expansion),
which is operator-theoretic and out of scope here. -/

/-- The cast ring hom used to move matrices from ℤ to `ZMod N`. -/
abbrev castHom (N : ℕ) : ℤ →+* ZMod N := Int.castRingHom (ZMod N)

/-- Applying `castHom` is the plain integer cast (by `rfl`: the abbrev
unfolds to `Int.castRingHom`, whose `toFun` is `Int.cast`). Used to convert
between the `((z : ℤ) : ZMod N)` form of statements and the `⇑(castHom N) z`
form that `map_sum`/`map_mul` rewrite. -/
lemma castHom_apply (N : ℕ) (z : ℤ) : ⇑(castHom N) z = ((z : ℤ) : ZMod N) := rfl

section Specialization

open Bgs.LineB.Derand

-- NOTE: every lemma below takes `m`, `N` and the hypotheses it needs as
-- EXPLICIT binders. Section `variable`s are deliberately NOT used: for a
-- named declaration, a section variable is only in scope in the proof if it
-- occurs in the statement (probes 10-12: `example` works, `lemma` fails),
-- and `H_N`/`Xphi_N` written without arguments get fresh metavariables
-- instead of the section `m`/`N`.

/-- The frozen-map matrix over `ZMod N` and its adjugate counterpart. -/
def H_N (m N : ℕ) : Matrix (ZMod m) (ZMod m) (ZMod N) :=
  (Bgs.LineD.Defs.Hmat m ℤ).map ⇑(castHom N)

def Xphi_N (m N : ℕ) : Matrix (ZMod m) (ZMod m) (ZMod N) :=
  (Xphi m).map ⇑(castHom N)

/-- The lattice vector attached to `n : Fin m → ℤ`. -/
def nZ (m : ℕ) [NeZero m] (n : Fin m → ℤ) : ZMod m → ℤ := fun r => n (zmodFinEquiv m r)

lemma nZ_apply (m : ℕ) [NeZero m] (n : Fin m → ℤ) (r : ZMod m) : nZ m n r = n (zmodFinEquiv m r) := rfl

/-- The same vector, cast to `ZMod N`. -/
def nZN (m N : ℕ) [NeZero m] (n : Fin m → ℤ) : ZMod m → ZMod N :=
  fun r => ((nZ m n r : ℤ) : ZMod N)

lemma nZN_apply (m N : ℕ) [NeZero m] [NeZero N] (n : Fin m → ℤ) (r : ZMod m) :
    nZN m N n r = ((nZ m n r : ℤ) : ZMod N) := rfl

/-- `Xphi` is symmetric: transposition swaps the two arguments of `phi`,
and `phi_symm` handles the wraparound. -/
lemma Xphi_transpose (m : ℕ) [NeZero m] : (Xphi m)ᵀ = Xphi m := by
  ext i j
  rw [Matrix.transpose_apply]
  show phi m (i - j).val = phi m (j - i).val
  by_cases h : j - i = 0
  · have h' : i - j = 0 := by rw [← neg_sub, h, neg_zero]
    rw [h, h']
  · have hval : (i - j).val = m - (j - i).val := by
      have h1 : i - j = -(j - i) := (neg_sub j i).symm
      rw [h1]
      haveI : NeZero (j - i) := ⟨h⟩
      exact ZMod.val_neg_of_ne_zero (j - i)
    rw [hval]
    exact (phi_symm m _ (le_of_lt (ZMod.val_lt _))).symm

/-- Positivity of the Pell pair, by simultaneous induction. -/
lemma pell_nonneg : ∀ k : ℕ, 1 ≤ pellX k ∧ 0 ≤ pellY k := by
  intro k
  induction k with
  | zero => exact ⟨le_refl 1, le_refl 0⟩
  | succ k ih =>
    show 1 ≤ 3 * pellX k + 8 * pellY k ∧ 0 ≤ pellX k + 3 * pellY k
    constructor <;> linarith [ih.1, ih.2]

lemma Dm_nonneg (m : ℕ) : 0 ≤ Dm m := by
  have h := (pell_nonneg m).1
  show 0 ≤ 2 * (pellX m - 1)
  linarith

/-- An inverse of `8` mod `N` exists for odd `N` (source Theorem 1 setup). -/
lemma exists_inv8 (N : ℕ) [NeZero N] (hNodd : Odd N) : ∃ i8n : ℕ, ((8 * i8n : ℕ) : ZMod N) = 1 := by
  have h2N : Nat.Coprime 2 N := by
    rw [Nat.prime_two.coprime_iff_not_dvd, ← even_iff_two_dvd]
    exact Nat.not_even_iff_odd.mpr hNodd
  have h8N : Nat.Coprime 8 N := by
    have h : (8 : ℕ) = 2 ^ 3 := rfl
    rw [h]
    exact (Nat.coprime_pow_left_iff (by norm_num : 0 < 3) 2 N).mpr h2N
  exact exists_inv_mod 8 N h8N

/-- From an inverse of `8` mod `N`, the two numerical identities the
Gauss specialization needs: `2 * (-i8) * (-4) = 1` (the completing-the-
square condition) and the coefficient identity `(-i8) * (-4)^2 - (-4) = 2`
(source §3: `4a = -2̄`, so `-(4a)⁻¹ = 2`). -/
lemma i8_props (N : ℕ) [NeZero N] (i8n : ℕ) (hi8n : ((8 * i8n : ℕ) : ZMod N) = 1) :
    2 * (-(((i8n : ℕ)) : ZMod N)) * (-4) = 1
    ∧ (-(((i8n : ℕ)) : ZMod N)) * (-4) ^ 2 - (-4) = 2 := by
  have hi8 : (8 : ZMod N) * (((i8n : ℕ)) : ZMod N) = 1 := by
    have h := hi8n
    rw [Nat.cast_mul] at h
    simpa using h
  constructor
  · have h1 : 2 * (-(((i8n : ℕ)) : ZMod N)) * (-4)
        = 8 * (((i8n : ℕ)) : ZMod N) := by ring
    rw [h1, hi8]
  · have h16 : (16 : ZMod N) * (((i8n : ℕ)) : ZMod N) = 2 := by
      have h1 : (16 : ZMod N) * (((i8n : ℕ)) : ZMod N)
          = 2 * (8 * (((i8n : ℕ)) : ZMod N)) := by ring
      rw [h1, hi8, mul_one]
    have h2 : (-(((i8n : ℕ)) : ZMod N)) * (-4) ^ 2 - (-4)
        = -((16 : ZMod N) * (((i8n : ℕ)) : ZMod N)) + 4 := by ring
    rw [h2, h16]
    ring

lemma H_N_symm (m N : ℕ) [NeZero m] [NeZero N] : (H_N m N)ᵀ = H_N m N := by
  show ((Bgs.LineD.Defs.Hmat m ℤ).map ⇑(castHom N))ᵀ
      = (Bgs.LineD.Defs.Hmat m ℤ).map ⇑(castHom N)
  rw [← transpose_map, Bgs.LineD.Defs.Hmat_transpose]

lemma Hinv_N_symm (m N : ℕ) [NeZero m] [NeZero N] (aDℕ : ℕ) :
    (((aDℕ : ZMod N)) • Xphi_N m N)ᵀ = ((aDℕ : ZMod N)) • Xphi_N m N := by
  show (((aDℕ : ZMod N)) • (Xphi m).map ⇑(castHom N))ᵀ
      = ((aDℕ : ZMod N)) • (Xphi m).map ⇑(castHom N)
  rw [Matrix.transpose_smul, ← transpose_map, Xphi_transpose]

lemma H_mul_Hinv (m N : ℕ) [NeZero m] [NeZero N] (hm : 2 ≤ m) (aDℕ : ℕ)
    (haD : (((Dm m).toNat * aDℕ : ℕ) : ZMod N) = 1) :
    H_N m N * (((aDℕ : ZMod N)) • Xphi_N m N) = 1 := by
  show (Bgs.LineD.Defs.Hmat m ℤ).map ⇑(castHom N)
      * (((aDℕ : ZMod N)) • (Xphi m).map ⇑(castHom N)) = 1
  rw [Matrix.mul_smul, ← Matrix.map_mul, HXphi m hm]
  have hmapsmul : ((Dm m • (1 : Matrix (ZMod m) (ZMod m) ℤ)).map
        ⇑(castHom N))
      = (Dm m : ℤ) • (((1 : Matrix (ZMod m) (ZMod m) ℤ).map
        ⇑(castHom N))) :=
    Matrix.map_smul ⇑(castHom N) (Dm m)
      (fun a => map_zsmul (castHom N) (Dm m) a)
      (1 : Matrix (ZMod m) (ZMod m) ℤ)
  rw [hmapsmul, Matrix.map_one ⇑(castHom N) (map_zero (castHom N))
    (map_one (castHom N))]
  have hDm1 : (Dm m : ℤ) • (1 : Matrix (ZMod m) (ZMod m) (ZMod N))
      = ((Dm m : ℤ) : ZMod N) • (1 : Matrix (ZMod m) (ZMod m) (ZMod N)) := by
    ext i j
    simp only [Matrix.smul_apply, zsmul_eq_mul, smul_eq_mul]
  rw [hDm1, smul_smul]
  have haD' : (aDℕ : ZMod N) * ((Dm m : ℤ) : ZMod N) = 1 := by
    have h1 : (((Dm m).toNat : ℕ) : ZMod N) = ((Dm m : ℤ) : ZMod N) := by
      rw [← Int.cast_natCast, Int.toNat_of_nonneg (Dm_nonneg m)]
    rw [← h1, ← Nat.cast_mul, mul_comm]
    exact haD
  rw [haD', one_smul]

lemma Hinv_mul_H (m N : ℕ) [NeZero m] [NeZero N] (hm : 2 ≤ m) (aDℕ : ℕ)
    (haD : (((Dm m).toNat * aDℕ : ℕ) : ZMod N) = 1) :
    (((aDℕ : ZMod N)) • Xphi_N m N) * H_N m N = 1 := by
  have h := congrArg Matrix.transpose (H_mul_Hinv m N hm aDℕ haD)
  rw [Matrix.transpose_mul, H_N_symm m N, Hinv_N_symm m N aDℕ,
    Matrix.transpose_one] at h
  exact h

/-- Transport of the quadratic form to `Qnum` (mirrors Step A of
`Q_bound_ge_two` in `LineBTraceFormula`, but over ℤ). -/
lemma transport (m : ℕ) [NeZero m] (hm : 2 ≤ m) (n : Fin m → ℤ) :
    2 * (nZ m n ⬝ᵥ (Xphi m *ᵥ nZ m n)) = Qnum m n := by
  have hdot : nZ m n ⬝ᵥ (Xphi m *ᵥ nZ m n)
      = ∑ i, ∑ j, (nZ m n i * nZ m n j) * φbar m (j - i) := by
    rw [dotProduct]
    simp only [Matrix.mulVec_apply_eq_sum]
    apply Finset.sum_congr rfl
    intro i _
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro j _
    show nZ m n i * (φbar m (j - i) * nZ m n j) = (nZ m n i * nZ m n j) * φbar m (j - i)
    ring
  rw [hdot, zmod_sum_eq_fin_sum m hm (nZ m n)]
  have hcast2 : (∑ i : Fin m, ∑ j : Fin m,
        (nZ m n (((i.val : ℕ)) : ZMod m) * nZ m n (((j.val : ℕ)) : ZMod m))
          * phi m (dist m i.val j.val))
      = ∑ i, ∑ j, (n i * n j) * phi m (dist m (i : ℕ) (j : ℕ)) := by
    apply Finset.sum_congr rfl
    intro i _
    apply Finset.sum_congr rfl
    intro j _
    simp only [nZ_apply, zmodFinEquiv_cast]
  rw [hcast2]
  exact quadId m n

/-- Scalar multiplication commutes with `mulVec` (no `Matrix.smul_mulVec_assoc`
in Mathlib 4.33.1). -/
lemma smul_mulVec' (m N : ℕ) [NeZero m] [NeZero N] (a : ZMod N) (M : Matrix (ZMod m) (ZMod m) (ZMod N))
    (v : ZMod m → ZMod N) : (a • M) *ᵥ v = a • (M *ᵥ v) := by
  ext i
  simp only [Matrix.mulVec_apply_eq_sum, Matrix.smul_apply, Pi.smul_apply,
    smul_eq_mul, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro j _
  ring

/-- `map` commutes with `mulVec` (no `Matrix.map_mulVec` in 4.33.1). -/
lemma map_mulVec' (m N : ℕ) [NeZero m] [NeZero N] (M : Matrix (ZMod m) (ZMod m) ℤ) (v : ZMod m → ℤ) :
    (M.map ⇑(castHom N)) *ᵥ (fun r => ((v r) : ZMod N))
      = fun i => (((M *ᵥ v) i : ℤ) : ZMod N) := by
  ext i
  simp only [← castHom_apply, Matrix.mulVec_apply_eq_sum, Matrix.map_apply]
  rw [map_sum]
  apply Finset.sum_congr rfl
  intro j _
  rw [map_mul]

/-- `map` commutes with `dotProduct` (no `Matrix.map_dotProduct` in 4.33.1). -/
lemma map_dotProduct' (m N : ℕ) [NeZero m] [NeZero N] (v w : ZMod m → ℤ) :
    (fun r => ((v r) : ZMod N)) ⬝ᵥ (fun r => ((w r) : ZMod N))
      = ((v ⬝ᵥ w : ℤ) : ZMod N) := by
  simp only [← castHom_apply, dotProduct]
  rw [map_sum]
  apply Finset.sum_congr rfl
  intro j _
  rw [map_mul]

/-- Phase identification: twice the `Hinv_N`-quadratic form of `nZN n` is
`aD` times the cast of `Qnum` (never dividing by `2`). -/
lemma phase_ZMod (m N : ℕ) [NeZero m] [NeZero N] (hm : 2 ≤ m)
    (n : Fin m → ℤ) (aDℕ : ℕ) :
    2 * (nZN m N n ⬝ᵥ ((((aDℕ : ZMod N)) • Xphi_N m N) *ᵥ nZN m N n))
      = ((aDℕ : ZMod N)) * (((Qnum m n : ℤ)) : ZMod N) := by
  have h1 : ((((aDℕ : ZMod N)) • Xphi_N m N) *ᵥ nZN m N n)
      = ((aDℕ : ZMod N)) • (Xphi_N m N *ᵥ nZN m N n) := smul_mulVec' m N _ _ _
  have h2 : Xphi_N m N *ᵥ nZN m N n
      = fun i => (((Xphi m *ᵥ nZ m n) i : ℤ) : ZMod N) := by
    show (Xphi m).map ⇑(castHom N) *ᵥ nZN m N n
        = fun i => (((Xphi m *ᵥ nZ m n) i : ℤ) : ZMod N)
    rw [show nZN m N n = fun r => (((nZ m n r : ℤ)) : ZMod N)
      from funext (nZN_apply m N n)]
    exact map_mulVec' m N (Xphi m) (nZ m n)
  have h4 : nZN m N n ⬝ᵥ (fun i => (((Xphi m *ᵥ nZ m n) i : ℤ) : ZMod N))
      = (((nZ m n ⬝ᵥ (Xphi m *ᵥ nZ m n) : ℤ)) : ZMod N) := by
    have h := map_dotProduct' m N (nZ m n) (Xphi m *ᵥ nZ m n)
    rwa [← funext (nZN_apply m N n)] at h
  rw [h1, dotProduct_smul, smul_eq_mul, h2, h4]
  have htr := transport m hm n
  have hf2 : ⇑(castHom N) (2 : ℤ) = 2 := by simp
  rw [← htr]
  simp only [← castHom_apply]
  rw [map_mul, hf2]
  ring

/-- The phase of the specialized Gauss sum is `e` of the rational phase
`Qnum * aD / N` (compare `trace_formula_finite`'s `hGauss`). -/
lemma chi_phase (m N : ℕ) [NeZero m] [NeZero N] (hm : 2 ≤ m)
    (n : Fin m → ℤ) (aDℕ : ℕ) :
    chi N (2 * (nZN m N n ⬝ᵥ ((((aDℕ : ZMod N)) • Xphi_N m N) *ᵥ nZN m N n)))
      = e ((Qnum m n : ℚ) * (aDℕ : ℚ) / (N : ℚ) : ℝ) := by
  rw [phase_ZMod m N hm n aDℕ]
  have hcast : ((aDℕ : ZMod N)) * (((Qnum m n : ℤ)) : ZMod N)
      = ((((aDℕ : ℤ) * Qnum m n : ℤ)) : ZMod N) := by
    rw [Int.cast_mul, Int.cast_natCast]
  rw [hcast, chi_int]
  congr 1
  push_cast
  ring

/-- Specialized Gauss sum (source §3, Theorem 1(a) phase): with `a` the
kick coefficient (`-i8` in the source) and `t0 = -4`, completing the square
gives the `Qnum`-phase times the zero-term sum. -/
lemma gauss_special (m N : ℕ) [NeZero m] [NeZero N] (hm : 2 ≤ m)
    (n : Fin m → ℤ) (aDℕ : ℕ)
    (haD : (((Dm m).toNat * aDℕ : ℕ) : ZMod N) = 1)
    (a : ZMod N) (ht0 : 2 * a * (-4) = 1)
    (hcoef : a * (-4) ^ 2 - (-4) = 2) :
    Gsum (H_N m N) a (nZN m N n)
      = e ((Qnum m n : ℚ) * (aDℕ : ℚ) / (N : ℚ) : ℝ)
        * Gsum (H_N m N) a 0 := by
  rw [gauss_sum_shift (H_N_symm m N) (H_mul_Hinv m N hm aDℕ haD) a (-4) ht0
    (nZN m N n), hcoef, chi_phase m N hm n aDℕ]

/-- The bridge: the finite sum over `S` factors through the zero-term sum
with exactly the `hGauss` phases of `trace_formula_finite`. -/
lemma gauss_bridge (m N : ℕ) [NeZero m] [NeZero N] (hm : 2 ≤ m)
    (Φ : (Fin m → ℤ) → ℂ) (S : Finset (Fin m → ℤ))
    (aDℕ : ℕ) (haD : (((Dm m).toNat * aDℕ : ℕ) : ZMod N) = 1)
    (a : ZMod N) (ht0 : 2 * a * (-4) = 1)
    (hcoef : a * (-4) ^ 2 - (-4) = 2) :
    (∑ n ∈ S, Φ n * Gsum (H_N m N) a (nZN m N n))
      = Gsum (H_N m N) a 0
        * ∑ n ∈ S, Φ n * e ((Qnum m n : ℚ) * (aDℕ : ℚ) / (N : ℚ) : ℝ) := by
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro n _
  rw [gauss_special m N hm n aDℕ haD a ht0 hcoef]
  ring

/-- Norm of the specialized zero-term sum (source §3, Theorem 1(b) input:
`|Tr M^m| = 1` comes from `|G(0)| = N^{m/2}`). -/
lemma norm_G0 (m N : ℕ) [NeZero m] [NeZero N] (hm : 2 ≤ m) (aDℕ : ℕ)
    (haD : (((Dm m).toNat * aDℕ : ℕ) : ZMod N) = 1)
    (a : ZMod N) (ht0 : 2 * a * (-4) = 1) :
    ‖Gsum (H_N m N) a 0‖ = Real.sqrt ((N : ℝ) ^ m) := by
  rw [← Real.sqrt_sq (norm_nonneg _)]
  congr 1
  rw [gauss_sum_zero_norm_sq (H_N_symm m N) (Hinv_mul_H m N hm aDℕ haD) a
    ⟨-4, ht0⟩, ZMod.card]

/-- The normalized zero-term sum has norm `1`: this is `hMod` of
`trace_formula_finite`, proved rather than assumed. -/
lemma norm_TrM (m N : ℕ) [NeZero m] [NeZero N] (hm : 2 ≤ m) (aDℕ : ℕ)
    (haD : (((Dm m).toNat * aDℕ : ℕ) : ZMod N) = 1)
    (a : ZMod N) (ht0 : 2 * a * (-4) = 1) :
    ‖(((Real.sqrt ((N : ℝ) ^ m) : ℂ)))⁻¹ * Gsum (H_N m N) a 0‖ = 1 := by
  have hpos : 0 < Real.sqrt ((N : ℝ) ^ m) :=
    Real.sqrt_pos.mpr (pow_pos (by exact_mod_cast NeZero.pos N) m)
  rw [norm_mul, norm_G0 m N hm aDℕ haD a ht0, ← Complex.ofReal_inv,
    Complex.norm_real, Real.norm_eq_abs, abs_of_pos (inv_pos.mpr hpos),
    inv_mul_cancel₀ (ne_of_gt hpos)]

/-- The wrapper: given the trace expansion `hExpand` (the only remaining
hypothesis — Fourier series of the kick, absolute convergence, sum swap,
matrix-element computation) and the Gauss-sum data `(a, ht0, hcoef)`, the
finite-sum Theorem 1(a) phases and the norm follow. The inverse `b` of `N`
mod `Dm` is packaged existentially, as in `trace_formula_finite`. -/
theorem trace_formula_via_gauss (m N : ℕ) [NeZero m] [NeZero N] (hm : 2 ≤ m)
    (hcop : Nat.Coprime (Dm m).toNat N)
    (Φ : (Fin m → ℤ) → ℂ) (S : Finset (Fin m → ℤ))
    (Tr TrM : ℂ) (hN : 2 ≤ N)
    (a : ZMod N) (ht0 : 2 * a * (-4) = 1)
    (hcoef : a * (-4) ^ 2 - (-4) = 2)
    (hExpand : Tr = (((Real.sqrt ((N : ℝ) ^ m) : ℂ)))⁻¹
      * ∑ n ∈ S, Φ n * Gsum (H_N m N) a (nZN m N n))
    (hG0def : TrM = (((Real.sqrt ((N : ℝ) ^ m) : ℂ)))⁻¹ * Gsum (H_N m N) a 0) :
    ∃ b : ℕ, Tr = TrM * ∑ n ∈ S, Φ n * (e ((Qnum m n : ℚ) / (Dm m : ℚ)
      / (N : ℚ) : ℝ) * e (-((b % gp m : ℕ) : ℚ) * (yp m : ℚ)
      * (NmZ m n : ℚ) / (gp m : ℚ) : ℝ)) ∧ ‖TrM‖ = 1 := by
  obtain ⟨aDℕ, haD⟩ := exists_inv_mod (Dm m).toNat N hcop
  obtain ⟨bℕ, hbℕ⟩ := exists_inv_mod N (Dm m).toNat (Nat.Coprime.symm hcop)
  have hGauss : Tr = TrM * ∑ n ∈ S, Φ n
      * e ((Qnum m n : ℚ) * (aDℕ : ℚ) / (N : ℚ) : ℝ) := by
    rw [hExpand, hG0def, gauss_bridge m N hm Φ S aDℕ haD a ht0 hcoef, mul_assoc]
  have hMod : ‖TrM‖ = 1 := by rw [hG0def]; exact norm_TrM m N hm aDℕ haD a ht0
  exact ⟨bℕ, trace_formula_finite m N (by omega) hN hcop aDℕ bℕ haD hbℕ
    Φ TrM Tr S hGauss hMod⟩

end Specialization

/- Axiom audit for all main theorems of this module. -/
#print axioms Bgs.LineB.Gauss.e_add'
#print axioms Bgs.LineB.Gauss.e_zero'
#print axioms Bgs.LineB.Gauss.e_int'
#print axioms Bgs.LineB.Gauss.e_neg'
#print axioms Bgs.LineB.Gauss.e_conj'
#print axioms Bgs.LineB.Gauss.chi_add
#print axioms Bgs.LineB.Gauss.chi_zero
#print axioms Bgs.LineB.Gauss.chi_int
#print axioms Bgs.LineB.Gauss.chi_ne_one
#print axioms Bgs.LineB.Gauss.dotProduct_mulVec_symm
#print axioms Bgs.LineB.Gauss.mulVec_shift
#print axioms Bgs.LineB.Gauss.dotProduct_shift_self
#print axioms Bgs.LineB.Gauss.Qform_shift
#print axioms Bgs.LineB.Gauss.phase_shift
#print axioms Bgs.LineB.Gauss.transEquiv_apply
#print axioms Bgs.LineB.Gauss.gauss_sum_shift
#print axioms Bgs.LineB.Gauss.chi_conj
#print axioms Bgs.LineB.Gauss.addEquiv_apply
#print axioms Bgs.LineB.Gauss.sum_chi_dotProduct
#print axioms Bgs.LineB.Gauss.Qform_add
#print axioms Bgs.LineB.Gauss.gauss_sum_zero_norm_sq
#print axioms Bgs.LineB.Gauss.castHom_apply
#print axioms Bgs.LineB.Gauss.nZ_apply
#print axioms Bgs.LineB.Gauss.nZN_apply
#print axioms Bgs.LineB.Gauss.Xphi_transpose
#print axioms Bgs.LineB.Gauss.pell_nonneg
#print axioms Bgs.LineB.Gauss.Dm_nonneg
#print axioms Bgs.LineB.Gauss.exists_inv8
#print axioms Bgs.LineB.Gauss.i8_props
#print axioms Bgs.LineB.Gauss.H_N_symm
#print axioms Bgs.LineB.Gauss.Hinv_N_symm
#print axioms Bgs.LineB.Gauss.H_mul_Hinv
#print axioms Bgs.LineB.Gauss.Hinv_mul_H
#print axioms Bgs.LineB.Gauss.transport
#print axioms Bgs.LineB.Gauss.smul_mulVec'
#print axioms Bgs.LineB.Gauss.map_mulVec'
#print axioms Bgs.LineB.Gauss.map_dotProduct'
#print axioms Bgs.LineB.Gauss.phase_ZMod
#print axioms Bgs.LineB.Gauss.chi_phase
#print axioms Bgs.LineB.Gauss.gauss_special
#print axioms Bgs.LineB.Gauss.gauss_bridge
#print axioms Bgs.LineB.Gauss.norm_G0
#print axioms Bgs.LineB.Gauss.norm_TrM
#print axioms Bgs.LineB.Gauss.trace_formula_via_gauss
end Gauss
end LineB
end Bgs
