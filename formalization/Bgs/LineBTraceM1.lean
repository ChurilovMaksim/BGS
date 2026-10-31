import Bgs.LineBTsum

/-!
# BGS Line B, the case `m = 1` of the trace formula (163)

No `sorry`, no `admit`, no `native_decide` anywhere in this file
(the words appear only in this header comment).

## What this module does

The chain `TraceFormula → Gauss → Expand → Tsum` proves Theorem 1(a) of 163
for `m ≥ 2`. This module closes the remaining case `m = 1`, in the same
notations as `trace_formula_tsum` (a general `ĝ : ℤ → ℂ` with
`∑ n² |ĝ n| < ∞`, `N ≥ 2`, `gcd (Dm 1, N) = 1`, `2 * a * (-4) = 1`):

* `trace_formula_kick_one` — the finite trace formula at `m = 1`;
* `trace_formula_tsum_one` — Theorem 1(a) at `m = 1` in `tsum` form;
* `trace_formula_tsum_error_one` — Theorem 1(c) at `m = 1`, with the
  `m = 1` specialization of the general bound, `π * s2 / N`.

## Where `m ≥ 2` was used, and what replaces it at `m = 1`

The only genuinely `m ≥ 2` steps of the chain are in the Gauss bridge:
`H_mul_Hinv` / `Hinv_mul_H` (which rest on the matrix identity `HXphi`,
whose residue analysis at `1` and `-1` needs `m ≥ 2`) and the lemmas built
on them (`transport`, `phase_ZMod`, `chi_phase`, `gauss_bridge`, `norm_TrM`).
Everything else is already `m`-generic: `hexpand` and `hg0def` (Expand),
`trace_formula_finite` (which takes `1 ≤ m`), the continuity/exhaustion
lemmas of Tsum, and `gauss_sum_zero_norm_sq` (which takes an abstract
`Hinv`).

At `m = 1` the Gauss step degenerates completely, and is proved here by
hand, with no new hypothesis:

* `H_1 = [4]` (the cyclic matrix `6I - C - Cᵀ` collapses: `6 - 1 - 1`),
  so the Gauss sum is the one-variable sum `∑_t χ(4a·t² + n₀·t)`.
* The square is completed by the shift `t ↦ t + n₀` — no division is
  needed, because `ht0 : 2 * a * (-4) = 1` gives `8a = -1`, hence
  `8a + 1 = 0` and the linear term vanishes, leaving the phase
  `χ((4a + 1)·n₀²)`.
* The phase identification `χ((4a + 1)·n₀²) = e(Qnum·aD/N)` is the
  `m = 1` instance of the general mechanism: `Qnum 1 n = 2·n₀²`,
  `Dm 1 = 4`, and `2·aD = 4a + 1` in `ZMod N` (both sides double to `1`:
  `4·aD = 1` by `haD`, `2·(4a + 1) = 8a + 2 = 1` by `ht0`; the factor `2`
  is cancelled using `2·aD` itself as its inverse).
* The norm `‖Gsum(0)‖ = √N` comes from the generic
  `gauss_sum_zero_norm_sq` with the explicit `1 × 1` inverse `[aD]`;
  `Hinv * H = 1` is the entry computation `aD * 4 = 1`.

No step below assumes anything that is false at `m = 1`: in particular
`‖TrM‖ = 1` is proved, not assumed, and the error bound is proved with
the exact `m = 1` constant.

## What is NOT proved here

* The equal-layers hypothesis `hfib` and the analytic identification of
  `kickMatInf` with the real quantum kick: as in the `m ≥ 2` chain, this
  module works with the Fourier datum `ĝ` directly.
-/

open Filter Topology
open Matrix
open Bgs.LineB.TraceFormula Bgs.LineB.Gauss Bgs.LineB.Expand Bgs.LineB.Derand
open Bgs.LineB.Tsum

namespace Bgs.LineB.TraceM1

/-! ### §0. The `m = 1` values -/

lemma pellX_one : pellX 1 = 3 := by decide
lemma pellY_one : pellY 1 = 1 := by decide
lemma pellX_zero : pellX 0 = 1 := rfl
lemma pellY_zero : pellY 0 = 0 := rfl

lemma Dm_one : Dm 1 = 4 := by decide
lemma Dm_one_toNat : (Dm 1).toNat = 4 := by rw [Dm_one]; rfl
lemma gp_one : gp 1 = 2 := by decide
lemma yp_one : yp 1 = 1 := by decide

lemma dist_one_zero : dist 1 0 0 = 0 := by decide

/-- The norm at `m = 1` is the square of the single mode. -/
lemma NmZ_one (n : Fin 1 → ℤ) : NmZ 1 n = (n 0) ^ 2 := by
  simp only [NmZ, Fin.sum_univ_one, Fin.val_zero, dist_one_zero, pellX_zero]
  ring

/-- The `β`-term vanishes at `m = 1` (`y₀ = 0`). -/
lemma beta_one (n : Fin 1 → ℤ) : beta 1 n = 0 := by
  simp only [beta, Fin.sum_univ_one, Fin.val_zero, dist_one_zero, pellY_zero]
  ring

/-- The `Q`-numerator at `m = 1` is `2·n₀²`. -/
lemma Qnum_one (n : Fin 1 → ℤ) : Qnum 1 n = 2 * (n 0) ^ 2 := by
  unfold Qnum
  rw [pellY_one, NmZ_one, Dm_one, beta_one]
  ring

/-- The shift matrix at `m = 1` is `[1]` (in `ZMod 1`, `0 + 1 = 0`). -/
lemma shiftMat_one_entry : (Bgs.LineD.Defs.shiftMat 1 ℤ) 0 0 = 1 := by
  have h01 : (0 : ZMod 1) + 1 = 0 := Subsingleton.elim _ _
  simp [Bgs.LineD.Defs.shiftMat, h01]

/-- `H_1 = [4]`: the cyclic matrix `6I - C - Cᵀ` collapses at `m = 1`. -/
lemma Hmat_one_entry : (Bgs.LineD.Defs.Hmat 1 ℤ) 0 0 = 4 := by
  have hs := shiftMat_one_entry
  have hst : ((Bgs.LineD.Defs.shiftMat 1 ℤ)ᵀ) 0 0 = 1 := by
    rw [Matrix.transpose_apply]
    exact hs
  show ((6 : ℤ) • (1 : Matrix (ZMod 1) (ZMod 1) ℤ)
      - Bgs.LineD.Defs.shiftMat 1 ℤ - (Bgs.LineD.Defs.shiftMat 1 ℤ)ᵀ) 0 0 = 4
  rw [Matrix.sub_apply, Matrix.sub_apply, Matrix.smul_apply, Matrix.one_apply_eq,
    hs, hst]
  norm_num

/-- The `ZMod N` entry of `H_N` at `m = 1` is `4`. -/
lemma H_N_one_entry (N : ℕ) : (H_N 1 N) 0 0 = 4 := by
  unfold H_N
  rw [Matrix.map_apply, Hmat_one_entry, castHom_apply]
  norm_num

/-! ### §1. The Gauss sum at `m = 1` -/

/-- Functions `ZMod 1 → ZMod N` are just elements of `ZMod N`. -/
noncomputable def zmodOneFunEquiv (N : ℕ) : (ZMod 1 → ZMod N) ≃ ZMod N where
  toFun x := x 0
  invFun t := fun _ => t
  left_inv x := by
    funext i
    show (fun _ => x 0) i = x i
    rw [Subsingleton.elim i 0]
  right_inv _ := rfl

/-- The quadratic form at `m = 1` is `4·t²` (via the generic `quad_form_eq`:
the cycle sum has a single term `3t² - 2t² + 3t²`). -/
lemma Qform_one (N : ℕ) [NeZero N] (t : ZMod N) :
    Qform (H_N 1 N) (fun _ => t) = 4 * t ^ 2 := by
  show (fun _ => t) ⬝ᵥ (H_N 1 N *ᵥ (fun _ => t)) = 4 * t ^ 2
  rw [quad_form_eq 1 N (fun _ => t)]
  rw [Finset.sum_eq_single_of_mem 0 (Finset.mem_univ 0)]
  · show 3 * t ^ 2 - 2 * t * t + 3 * t ^ 2 = 4 * t ^ 2
    ring
  · intro b _ hb
    exact absurd (Subsingleton.elim b 0) hb

/-- The dot product over the singleton `ZMod 1`. -/
lemma dotProduct_one (N : ℕ) (w : ZMod 1 → ZMod N) (t : ZMod N) :
    w ⬝ᵥ (fun _ => t) = w 0 * t := by
  simp only [dotProduct]
  rw [Finset.sum_eq_single_of_mem 0 (Finset.mem_univ 0)]
  intro b _ hb
  exact absurd (Subsingleton.elim b 0) hb

/-- The Gauss sum at `m = 1`, reindexed as a sum over `ZMod N`. -/
lemma Gsum_one_eq (N : ℕ) [NeZero N] (a : ZMod N) (w : ZMod 1 → ZMod N) :
    Gsum (H_N 1 N) a w
      = ∑ t : ZMod N, chi N (a * (4 * t ^ 2) + w 0 * t) := by
  have h := (Equiv.sum_comp (zmodOneFunEquiv N).symm
    (fun x : ZMod 1 → ZMod N => chi N (a * Qform (H_N 1 N) x + w ⬝ᵥ x))).symm
  show (∑ x : ZMod 1 → ZMod N, chi N (a * Qform (H_N 1 N) x + w ⬝ᵥ x))
      = ∑ t : ZMod N, chi N (a * (4 * t ^ 2) + w 0 * t)
  rw [h]
  apply Finset.sum_congr rfl
  intro t _
  show chi N (a * Qform (H_N 1 N) (fun _ => t) + w ⬝ᵥ (fun _ => t)) = _
  rw [Qform_one, dotProduct_one]

/-- Completing the square at `m = 1`: the shift `t ↦ t + n₀` kills the
linear term because `8a = -1`, leaving the phase `χ((4a + 1)·n₀²)`. -/
lemma gsum_shift_one (N : ℕ) [NeZero N] (a : ZMod N) (ht0 : 2 * a * (-4) = 1)
    (n : Fin 1 → ℤ) :
    Gsum (H_N 1 N) a (nZN 1 N n)
      = chi N ((4 * a + 1) * ((n 0 : ℤ) : ZMod N) ^ 2)
        * Gsum (H_N 1 N) a 0 := by
  have h8 : (8 : ZMod N) * a + 1 = 0 := by linear_combination -ht0
  have hnZN : nZN 1 N n 0 = ((n 0 : ℤ) : ZMod N) := by
    have hz : zmodFinEquiv 1 (0 : ZMod 1) = 0 := Subsingleton.elim _ _
    simp [nZN, nZ, hz]
  rw [Gsum_one_eq, Gsum_one_eq, hnZN]
  simp only [Pi.zero_apply, zero_mul, add_zero]
  have hshift : (∑ t : ZMod N, chi N (a * (4 * t ^ 2) + ((n 0 : ℤ) : ZMod N) * t))
      = ∑ t : ZMod N,
        chi N (a * (4 * t ^ 2) + (4 * a + 1) * ((n 0 : ℤ) : ZMod N) ^ 2) := by
    have hre := (Equiv.sum_comp (Equiv.addRight ((n 0 : ℤ) : ZMod N))
      (fun t : ZMod N =>
        chi N (a * (4 * t ^ 2) + ((n 0 : ℤ) : ZMod N) * t))).symm
    rw [hre]
    apply Finset.sum_congr rfl
    intro t _
    show chi N (a * (4 * (t + ((n 0 : ℤ) : ZMod N)) ^ 2)
          + ((n 0 : ℤ) : ZMod N) * (t + ((n 0 : ℤ) : ZMod N)))
        = chi N (a * (4 * t ^ 2) + (4 * a + 1) * ((n 0 : ℤ) : ZMod N) ^ 2)
    congr 1
    linear_combination (((n 0 : ℤ) : ZMod N) * t) * h8
  rw [hshift]
  have hchi : ∀ t : ZMod N,
      chi N (a * (4 * t ^ 2) + (4 * a + 1) * ((n 0 : ℤ) : ZMod N) ^ 2)
        = chi N (a * (4 * t ^ 2))
          * chi N ((4 * a + 1) * ((n 0 : ℤ) : ZMod N) ^ 2) := by
    intro t
    exact chi_add _ _
  simp_rw [hchi, ← Finset.sum_mul]
  exact mul_comm _ _

/-! ### §2. Phase identification, `hGauss`, and the norm at `m = 1` -/

/-- `2·aD = 4a + 1` in `ZMod N`: both sides double to `1`
(`4·aD = 1` by `haD`, `2·(4a + 1) = 8a + 2 = 1` by `ht0`), and the
factor `2` is cancelled using `2·aD` itself as the inverse of `2`
(since `2·(2·aD) = 4·aD = 1`). -/
lemma two_aD_eq (N : ℕ) [NeZero N] (a : ZMod N) (aDℕ : ℕ)
    (haD : (((Dm 1).toNat * aDℕ : ℕ) : ZMod N) = 1) (ht0 : 2 * a * (-4) = 1) :
    2 * (aDℕ : ZMod N) = 4 * a + 1 := by
  have haD' : (4 : ZMod N) * (aDℕ : ZMod N) = 1 := by
    have h := haD
    rw [Dm_one_toNat] at h
    push_cast at h
    exact h
  have h1 : (2 : ZMod N) * (2 * (aDℕ : ZMod N)) = 1 := by
    linear_combination haD'
  have h2 : (2 : ZMod N) * (4 * a + 1) = 1 := by
    linear_combination -ht0
  have hu : (2 * (aDℕ : ZMod N)) * 2 = 1 := by
    rw [mul_comm]
    exact h1
  calc 2 * (aDℕ : ZMod N)
      = (2 * (aDℕ : ZMod N)) * (2 * (4 * a + 1)) := by rw [h2, mul_one]
    _ = ((2 * (aDℕ : ZMod N)) * 2) * (4 * a + 1) := by ring
    _ = 4 * a + 1 := by rw [hu, one_mul]

/-- The `m = 1` phase identification: the Gauss phase `χ((4a + 1)·n₀²)`
is the `e`-phase `e(Qnum·aD/N)` of `trace_formula_finite`. -/
lemma chi_phase_one (N : ℕ) [NeZero N] (a : ZMod N) (aDℕ : ℕ)
    (haD : (((Dm 1).toNat * aDℕ : ℕ) : ZMod N) = 1) (ht0 : 2 * a * (-4) = 1)
    (n : Fin 1 → ℤ) :
    chi N ((4 * a + 1) * ((n 0 : ℤ) : ZMod N) ^ 2)
      = e ((Qnum 1 n : ℚ) * (aDℕ : ℚ) / (N : ℚ) : ℝ) := by
  rw [Qnum_one]
  have hcast : (4 * a + 1) * ((n 0 : ℤ) : ZMod N) ^ 2
      = ((2 * (n 0) ^ 2 * aDℕ : ℤ) : ZMod N) := by
    push_cast
    rw [← two_aD_eq N a aDℕ haD ht0]
    ring
  rw [hcast, chi_int]
  congr 1
  push_cast
  ring

/-- `hGauss` at `m = 1`: the trace expansion with the `e`-phases. -/
lemma hGauss_one (N : ℕ) [NeZero N] (ĝ : ℤ → ℂ) (supp : Finset ℤ)
    (a : ZMod N) (aDℕ : ℕ)
    (haD : (((Dm 1).toNat * aDℕ : ℕ) : ZMod N) = 1) (ht0 : 2 * a * (-4) = 1) :
    Matrix.trace ((kickMat N ĝ supp * catMat N a) ^ 1)
      = Matrix.trace (catMat N a ^ 1)
        * ∑ n ∈ modeSet 1 supp, phiFun 1 ĝ n
          * e ((Qnum 1 n : ℚ) * (aDℕ : ℚ) / (N : ℚ) : ℝ) := by
  have hex := hexpand 1 N ĝ supp a
  have hg0 := hg0def 1 N a
  rw [hex, hg0]
  have hsum : (∑ n ∈ modeSet 1 supp, phiFun 1 ĝ n
        * Gsum (H_N 1 N) a (nZN 1 N n))
      = Gsum (H_N 1 N) a 0
        * ∑ n ∈ modeSet 1 supp, phiFun 1 ĝ n
          * e ((Qnum 1 n : ℚ) * (aDℕ : ℚ) / (N : ℚ) : ℝ) := by
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro n _
    rw [gsum_shift_one N a ht0 n, chi_phase_one N a aDℕ haD ht0 n]
    ring
  rw [hsum]
  ring

/-- The norm of the zero-term Gauss sum at `m = 1` is `√N`, from the
generic `gauss_sum_zero_norm_sq` with the explicit `1 × 1` inverse `[aD]`. -/
lemma norm_G0_one (N : ℕ) [NeZero N] (a : ZMod N) (aDℕ : ℕ)
    (haD : (((Dm 1).toNat * aDℕ : ℕ) : ZMod N) = 1) (ht0 : 2 * a * (-4) = 1) :
    ‖Gsum (H_N 1 N) a 0‖ = Real.sqrt (N : ℝ) := by
  have hHinv : (Matrix.of fun _ _ => (aDℕ : ZMod N)) * (H_N 1 N) = 1 := by
    ext i j
    rw [Subsingleton.elim i 0, Subsingleton.elim j 0]
    simp only [Matrix.mul_apply]
    rw [Finset.sum_eq_single_of_mem 0 (Finset.mem_univ 0)]
    · show (aDℕ : ZMod N) * (H_N 1 N) 0 0 = 1
      rw [H_N_one_entry]
      have h := haD
      rw [Dm_one_toNat] at h
      push_cast at h
      rw [mul_comm]
      exact h
    · intro b _ hb
      exact absurd (Subsingleton.elim b 0) hb
  rw [← Real.sqrt_sq (norm_nonneg _)]
  congr 1
  rw [gauss_sum_zero_norm_sq (H_N_symm 1 N) hHinv a ⟨-4, ht0⟩, ZMod.card]
  simp

/-- The normalized zero-term sum has norm `1` at `m = 1`. -/
lemma norm_TrM_one (N : ℕ) [NeZero N] (a : ZMod N) (aDℕ : ℕ)
    (haD : (((Dm 1).toNat * aDℕ : ℕ) : ZMod N) = 1) (ht0 : 2 * a * (-4) = 1) :
    ‖(((Real.sqrt ((N : ℝ) ^ 1) : ℂ)))⁻¹ * Gsum (H_N 1 N) a 0‖ = 1 := by
  have hpos : 0 < Real.sqrt (N : ℝ) :=
    Real.sqrt_pos.mpr (by exact_mod_cast NeZero.pos N)
  rw [pow_one, norm_mul, norm_G0_one N a aDℕ haD ht0, ← Complex.ofReal_inv,
    Complex.norm_real, Real.norm_eq_abs, abs_of_pos (inv_pos.mpr hpos),
    inv_mul_cancel₀ (ne_of_gt hpos)]

/-- `hMod` at `m = 1`: the un-kicked trace has norm `1`. -/
lemma hMod_one (N : ℕ) [NeZero N] (a : ZMod N) (aDℕ : ℕ)
    (haD : (((Dm 1).toNat * aDℕ : ℕ) : ZMod N) = 1) (ht0 : 2 * a * (-4) = 1) :
    ‖Matrix.trace (catMat N a ^ 1)‖ = 1 := by
  rw [hg0def 1 N a]
  exact norm_TrM_one N a aDℕ haD ht0

/-- The finite trace formula at `m = 1` with a fixed inverse `b₀` of `N`
mod `Dm 1` (the form the `tsum` limit step needs). -/
theorem trace_formula_finite_one (N : ℕ) [NeZero N] (ĝ : ℤ → ℂ)
    (supp : Finset ℤ) (a : ZMod N) (hcop : Nat.Coprime (Dm 1).toNat N)
    (hN : 2 ≤ N) (ht0 : 2 * a * (-4) = 1) (b₀ : ℕ)
    (hb₀ : ((N * b₀ : ℕ) : ZMod (Dm 1).toNat) = 1) :
    Matrix.trace ((kickMat N ĝ supp * catMat N a) ^ 1)
      = Matrix.trace (catMat N a ^ 1)
        * ∑ n ∈ modeSet 1 supp, phiFun 1 ĝ n * phaseFun 1 N b₀ n
      ∧ ‖Matrix.trace (catMat N a ^ 1)‖ = 1 := by
  obtain ⟨aDℕ, haD⟩ := exists_inv_mod (Dm 1).toNat N hcop
  have hG := hGauss_one N ĝ supp a aDℕ haD ht0
  have hM := hMod_one N a aDℕ haD ht0
  exact trace_formula_finite 1 N le_rfl hN hcop aDℕ b₀ haD hb₀ (phiFun 1 ĝ)
    (Matrix.trace (catMat N a ^ 1))
    (Matrix.trace ((kickMat N ĝ supp * catMat N a) ^ 1))
    (modeSet 1 supp) hG hM

/-- The finite trace formula at `m = 1` (Theorem 1(a) of 163 for
trigonometric-polynomial kicks), plus `‖TrM‖ = 1`. -/
theorem trace_formula_kick_one (N : ℕ) [NeZero N] (ĝ : ℤ → ℂ)
    (supp : Finset ℤ) (a : ZMod N) (hcop : Nat.Coprime (Dm 1).toNat N)
    (hN : 2 ≤ N) (ht0 : 2 * a * (-4) = 1) :
    ∃ b : ℕ, Matrix.trace ((kickMat N ĝ supp * catMat N a) ^ 1)
      = Matrix.trace (catMat N a ^ 1)
        * ∑ n ∈ modeSet 1 supp, phiFun 1 ĝ n * phaseFun 1 N b n
      ∧ ‖Matrix.trace (catMat N a ^ 1)‖ = 1 := by
  obtain ⟨b₀, hb₀⟩ := exists_inv_mod N (Dm 1).toNat (Nat.Coprime.symm hcop)
  exact ⟨b₀, trace_formula_finite_one N ĝ supp a hcop hN ht0 b₀ hb₀⟩

/-! ### §3. The `tsum` trace formula at `m = 1` -/

/-- Mode terms are summable at `m = 1` (the proof of `summable_mode`
with `1 ≤ 1` in place of `2 ≤ m`). -/
lemma summable_mode_one (ĝ : ℤ → ℂ) (hs0 : Summable fun k : ℤ => ‖ĝ k‖)
    (N b : ℕ) :
    Summable fun n : Fin 1 → ℤ => phiFun 1 ĝ n * phaseFun 1 N b n := by
  apply Summable.of_norm
  have h := mode_norm_summable ĝ hs0 1 le_rfl
  have heq : (fun n : Fin 1 → ℤ => ‖phiFun 1 ĝ n * phaseFun 1 N b n‖)
      = (fun n => ∏ j : Fin 1, ‖ĝ (n j)‖) := by
    funext n
    exact norm_phiFun_mul_phase 1 ĝ N b n
  rw [heq]
  exact h

/-- Zero-phase mode terms are summable at `m = 1`. -/
lemma summable_mode0_one (ĝ : ℤ → ℂ) (hs0 : Summable fun k : ℤ => ‖ĝ k‖)
    (N b : ℕ) :
    Summable fun n : Fin 1 → ℤ => phiFun 1 ĝ n * phase0Fun 1 N b n := by
  apply Summable.of_norm
  have h := mode_norm_summable ĝ hs0 1 le_rfl
  have heq : (fun n : Fin 1 → ℤ => ‖phiFun 1 ĝ n * phase0Fun 1 N b n‖)
      = (fun n => ∏ j : Fin 1, ‖ĝ (n j)‖) := by
    funext n
    exact norm_phiFun_mul_phase0 1 ĝ N b n
  rw [heq]
  exact h

/-- The finite mode sums tend to the `tsum` over all modes at `m = 1`. -/
lemma mode_sum_tendsto_one (ĝ : ℤ → ℂ) (hs0 : Summable fun k : ℤ => ‖ĝ k‖)
    (N b : ℕ) :
    Tendsto (fun S : Finset ℤ => ∑ n ∈ modeSet 1 S, phiFun 1 ĝ n * phaseFun 1 N b n)
      atTop (nhds (∑' n : Fin 1 → ℤ, phiFun 1 ĝ n * phaseFun 1 N b n)) :=
  (summable_mode_one ĝ hs0 N b).hasSum.comp (modeSet_tendsto_atTop 1)

/-- Summability of the squared-coordinate term at `m = 1`. -/
lemma summable_sq_coord_one (ĝ : ℤ → ℂ) (j : Fin 1)
    (hs0 : Summable fun k : ℤ => ‖ĝ k‖)
    (hs2 : Summable fun k : ℤ => (k : ℝ) ^ 2 * ‖ĝ k‖) :
    Summable fun n : Fin 1 → ℤ => ((n j : ℝ)) ^ 2 * ∏ r : Fin 1, ‖ĝ (n r)‖ := by
  have h := summable_mode_prod_nonneg 1 le_rfl (sqFamily ĝ j)
    (fun r k => sqFamily_nonneg ĝ j r k) (fun r => sqFamily_summable ĝ j r hs0 hs2)
  have heq : (fun n : Fin 1 → ℤ => ∏ r : Fin 1, sqFamily ĝ j r (n r))
      = (fun n => ((n j : ℝ)) ^ 2 * ∏ r : Fin 1, ‖ĝ (n r)‖) :=
    funext fun n => sqFamily_prod ĝ j n
  rw [heq] at h
  exact h

/-- The squared-coordinate `tsum` at `m = 1` is `s2`
(the `m = 1` case of `s2 * s0 ^ (m - 1)`). -/
lemma sq_tsum_one (ĝ : ℤ → ℂ) (j : Fin 1)
    (hs0 : Summable fun k : ℤ => ‖ĝ k‖)
    (hs2 : Summable fun k : ℤ => (k : ℝ) ^ 2 * ‖ĝ k‖) :
    ∑' n : Fin 1 → ℤ, ((n j : ℝ)) ^ 2 * ∏ r : Fin 1, ‖ĝ (n r)‖
      = (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖) := by
  have hval := tsum_mode_prod_value 1 le_rfl (sqFamily ĝ j)
    (fun r k => sqFamily_nonneg ĝ j r k) (fun r => sqFamily_summable ĝ j r hs0 hs2)
  have heq : (fun n : Fin 1 → ℤ => ∏ r : Fin 1, sqFamily ĝ j r (n r))
      = (fun n => ((n j : ℝ)) ^ 2 * ∏ r : Fin 1, ‖ĝ (n r)‖) :=
    funext fun n => sqFamily_prod ĝ j n
  rw [heq] at hval
  rw [hval, sqFamily_tsum_prod]
  simp

/-- The weighted mode sum at `m = 1` is `s2`
(the `m = 1` case of `m * s2 * s0 ^ (m - 1)`). -/
lemma weighted_mode_tsum_one (ĝ : ℤ → ℂ)
    (hs0 : Summable fun k : ℤ => ‖ĝ k‖)
    (hs2 : Summable fun k : ℤ => (k : ℝ) ^ 2 * ‖ĝ k‖) :
    ∑' n : Fin 1 → ℤ, (∏ j : Fin 1, ‖ĝ (n j)‖) * (∑ j, ((n j : ℝ)) ^ 2)
      = (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖) := by
  rw [prod_mul_sq_sum ĝ 1,
    Summable.tsum_finsetSum (s := Finset.univ)
      (f := fun j (n : Fin 1 → ℤ) => ((n j : ℝ)) ^ 2 * ∏ r : Fin 1, ‖ĝ (n r)‖)
      (fun j _ => summable_sq_coord_one ĝ j hs0 hs2)]
  rw [show (∑ j : Fin 1, ∑' n : Fin 1 → ℤ, ((n j : ℝ)) ^ 2 * ∏ r : Fin 1, ‖ĝ (n r)‖)
      = ∑ j : Fin 1, (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖) from
      Finset.sum_congr rfl (fun j _ => sq_tsum_one ĝ j hs0 hs2)]
  rw [Fin.sum_univ_one]

/-- Theorem 1(a) of 163 at `m = 1` in `tsum` form, plus `‖TrM‖ = 1`.
Proved by taking limits in the finite identity with a fixed `b₀`, exactly
as in `trace_formula_tsum`. -/
theorem trace_formula_tsum_one (N : ℕ) [NeZero N] (ĝ : ℤ → ℂ)
    (a : ZMod N) (hcop : Nat.Coprime (Dm 1).toNat N) (hN : 2 ≤ N)
    (ht0 : 2 * a * (-4) = 1) (hs2 : Summable fun k : ℤ => (k : ℝ) ^ 2 * ‖ĝ k‖) :
    ∃ b : ℕ, ((kickMatInf N ĝ * catMat N a) ^ 1).trace
      = (catMat N a ^ 1).trace
        * ∑' n : Fin 1 → ℤ, phiFun 1 ĝ n * phaseFun 1 N b n
      ∧ ‖(catMat N a ^ 1).trace‖ = 1 := by
  have hs0 := summable_norm_of_summable_sq ĝ hs2
  obtain ⟨b₀, hb₀⟩ := exists_inv_mod N (Dm 1).toNat (Nat.Coprime.symm hcop)
  have hS : ∀ S : Finset ℤ,
      ((kickMat N ĝ S * catMat N a) ^ 1).trace
        = (catMat N a ^ 1).trace
          * ∑ n ∈ modeSet 1 S, phiFun 1 ĝ n * phaseFun 1 N b₀ n
        ∧ ‖(catMat N a ^ 1).trace‖ = 1 :=
    fun S => trace_formula_finite_one N ĝ S a hcop hN ht0 b₀ hb₀
  have hL1 := trace_tendsto ĝ hs0 N a 1
  have hL2 := mode_sum_tendsto_one ĝ hs0 N b₀
  have hL2' : Tendsto (fun S : Finset ℤ => (catMat N a ^ 1).trace
      * ∑ n ∈ modeSet 1 S, phiFun 1 ĝ n * phaseFun 1 N b₀ n)
      atTop (nhds ((catMat N a ^ 1).trace
        * ∑' n : Fin 1 → ℤ, phiFun 1 ĝ n * phaseFun 1 N b₀ n)) :=
    hL2.const_mul _
  have hEq : (fun S : Finset ℤ => ((kickMat N ĝ S * catMat N a) ^ 1).trace)
      = (fun S : Finset ℤ => (catMat N a ^ 1).trace
        * ∑ n ∈ modeSet 1 S, phiFun 1 ĝ n * phaseFun 1 N b₀ n) :=
    funext fun S => (hS S).1
  refine ⟨b₀, ?_, (hS ∅).2⟩
  exact (tendsto_nhds_unique (by rw [hEq]; exact hL2') hL1).symm

/-- Theorem 1(c) of 163 at `m = 1`: the trace with the `Q`-phases differs
from the trace with zero phases by at most `π * s2 / N` — the `m = 1`
specialization of `π * m * s2 * s0 ^ (m - 1) / N`. -/
theorem trace_formula_tsum_error_one (N : ℕ) [NeZero N] (ĝ : ℤ → ℂ)
    (a : ZMod N) (hcop : Nat.Coprime (Dm 1).toNat N) (hN : 2 ≤ N)
    (ht0 : 2 * a * (-4) = 1) (hs2 : Summable fun k : ℤ => (k : ℝ) ^ 2 * ‖ĝ k‖) :
    ∃ b : ℕ, ((kickMatInf N ĝ * catMat N a) ^ 1).trace
      = (catMat N a ^ 1).trace
        * ∑' n : Fin 1 → ℤ, phiFun 1 ĝ n * phaseFun 1 N b n
      ∧ ‖(catMat N a ^ 1).trace‖ = 1
      ∧ ‖((kickMatInf N ĝ * catMat N a) ^ 1).trace
        - (catMat N a ^ 1).trace
          * ∑' n : Fin 1 → ℤ, phiFun 1 ĝ n * phase0Fun 1 N b n‖
        ≤ Real.pi * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖) / (N : ℝ) := by
  have hs0 := summable_norm_of_summable_sq ĝ hs2
  obtain ⟨b₀, hTr, hNorm⟩ := trace_formula_tsum_one N ĝ a hcop hN ht0 hs2
  refine ⟨b₀, hTr, hNorm, ?_⟩
  have hsumQ := summable_mode_one ĝ hs0 N b₀
  have hsum0 := summable_mode0_one ĝ hs0 N b₀
  have hdiff : (∑' n : Fin 1 → ℤ, phiFun 1 ĝ n * phaseFun 1 N b₀ n)
      - (∑' n : Fin 1 → ℤ, phiFun 1 ĝ n * phase0Fun 1 N b₀ n)
      = ∑' n : Fin 1 → ℤ, (phiFun 1 ĝ n * phaseFun 1 N b₀ n
        - phiFun 1 ĝ n * phase0Fun 1 N b₀ n) :=
    (Summable.tsum_sub hsumQ hsum0).symm
  have hbound : Summable fun n : Fin 1 → ℤ =>
      (Real.pi / (N : ℝ)) * ((∏ j : Fin 1, ‖ĝ (n j)‖) * (∑ j, ((n j : ℝ)) ^ 2)) := by
    apply Summable.mul_left
    rw [prod_mul_sq_sum ĝ 1]
    exact summable_finset_sum (s := Finset.univ)
      (f := fun j (n : Fin 1 → ℤ) => ((n j : ℝ)) ^ 2 * ∏ r : Fin 1, ‖ĝ (n r)‖)
      (fun j _ => summable_sq_coord_one ĝ j hs0 hs2)
  have hnormdiff : Summable fun n : Fin 1 → ℤ =>
      ‖phiFun 1 ĝ n * phaseFun 1 N b₀ n - phiFun 1 ĝ n * phase0Fun 1 N b₀ n‖ := by
    refine Summable.of_nonneg_of_le (fun n => norm_nonneg _)
      (fun n => diff_term_bound 1 N le_rfl hN ĝ b₀ n) hbound
  rw [hTr, ← mul_sub, hdiff, norm_mul, hNorm, one_mul]
  calc ‖∑' n : Fin 1 → ℤ, (phiFun 1 ĝ n * phaseFun 1 N b₀ n
        - phiFun 1 ĝ n * phase0Fun 1 N b₀ n)‖
      ≤ ∑' n : Fin 1 → ℤ, ‖phiFun 1 ĝ n * phaseFun 1 N b₀ n
        - phiFun 1 ĝ n * phase0Fun 1 N b₀ n‖ :=
        norm_tsum_le_tsum_norm hnormdiff
    _ ≤ ∑' n : Fin 1 → ℤ, (Real.pi / (N : ℝ))
        * ((∏ j : Fin 1, ‖ĝ (n j)‖) * (∑ j, ((n j : ℝ)) ^ 2)) :=
        Summable.tsum_le_tsum (fun n => diff_term_bound 1 N le_rfl hN ĝ b₀ n)
          hnormdiff hbound
    _ = (Real.pi / (N : ℝ)) * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖) := by
        rw [tsum_mul_left, weighted_mode_tsum_one ĝ hs0 hs2]
    _ = Real.pi * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖) / (N : ℝ) := by
        rw [div_mul_eq_mul_div]

/- Axiom audit for all theorems of this module. -/
#print axioms Bgs.LineB.TraceM1.pellX_one
#print axioms Bgs.LineB.TraceM1.pellY_one
#print axioms Bgs.LineB.TraceM1.pellX_zero
#print axioms Bgs.LineB.TraceM1.pellY_zero
#print axioms Bgs.LineB.TraceM1.Dm_one
#print axioms Bgs.LineB.TraceM1.Dm_one_toNat
#print axioms Bgs.LineB.TraceM1.gp_one
#print axioms Bgs.LineB.TraceM1.yp_one
#print axioms Bgs.LineB.TraceM1.dist_one_zero
#print axioms Bgs.LineB.TraceM1.NmZ_one
#print axioms Bgs.LineB.TraceM1.beta_one
#print axioms Bgs.LineB.TraceM1.Qnum_one
#print axioms Bgs.LineB.TraceM1.shiftMat_one_entry
#print axioms Bgs.LineB.TraceM1.Hmat_one_entry
#print axioms Bgs.LineB.TraceM1.H_N_one_entry
#print axioms Bgs.LineB.TraceM1.Qform_one
#print axioms Bgs.LineB.TraceM1.dotProduct_one
#print axioms Bgs.LineB.TraceM1.Gsum_one_eq
#print axioms Bgs.LineB.TraceM1.gsum_shift_one
#print axioms Bgs.LineB.TraceM1.two_aD_eq
#print axioms Bgs.LineB.TraceM1.chi_phase_one
#print axioms Bgs.LineB.TraceM1.hGauss_one
#print axioms Bgs.LineB.TraceM1.norm_G0_one
#print axioms Bgs.LineB.TraceM1.norm_TrM_one
#print axioms Bgs.LineB.TraceM1.hMod_one
#print axioms Bgs.LineB.TraceM1.trace_formula_finite_one
#print axioms Bgs.LineB.TraceM1.trace_formula_kick_one
#print axioms Bgs.LineB.TraceM1.summable_mode_one
#print axioms Bgs.LineB.TraceM1.summable_mode0_one
#print axioms Bgs.LineB.TraceM1.mode_sum_tendsto_one
#print axioms Bgs.LineB.TraceM1.summable_sq_coord_one
#print axioms Bgs.LineB.TraceM1.sq_tsum_one
#print axioms Bgs.LineB.TraceM1.weighted_mode_tsum_one
#print axioms Bgs.LineB.TraceM1.trace_formula_tsum_one
#print axioms Bgs.LineB.TraceM1.trace_formula_tsum_error_one

end Bgs.LineB.TraceM1

