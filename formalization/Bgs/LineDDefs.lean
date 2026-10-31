/-
BGS-TRACE-151 / BGS-TRACE-149: общие определения инфраструктурного блока.
Тестовая копия; в репозиторий не пушится, реестр не тронут.

Boundary (claims.json, 347f, дословно по содержанию):
- 151: Fix_m = {ξ : H_m ξ ∈ ℤ^m} (периодические решения
  q_{j+1} + q_{j-1} = 6 q_j mod 1); Psi_m(s/D) — сумма по парам
  ξ, ξ' ∈ Fix_m с весами phihat_s и omega_k (J0/гауссовы);
  |phihat_s|² ∈ {0, |V[4]|/D_m}; носитель не зависит от s;
  D_eff = 49, 72, 1681, 4900, 57121 (m = 3..7).
- 149: U = exp(i eta V_theta) M_N, M_N — cat-матрица S = [[3,4],[2,3]];
  H_m = 6I - C - C^T, D_m = det H_m = Tr S^m - 2, X_m = D_m H_m^{-1};
  для нечётного N с gcd(N, D_m) = 1 и любого theta:
  Tr U^m = Tr M_N^m ∑_n Ghat_theta(n) e(t_N 2 n^T X_m n),
  t_N = (D_m^{-1} mod N)/N, |Tr M_N^m| = 1;
  отсюда E_theta|Tr U^m|² = Psi_m(t_N), Psi_m C^∞ (не claimed
  вещественно-аналитическая), чётная, 1-периодическая, не зависит от N.

Что здесь ОПРЕДЕЛЕНО (без выдуманных объектов):
- shiftMat C (циклический сдвиг; индексы — ZMod m, поэтому сдвиг —
  это просто +1, без ручной арифметики Fin);
- Hmat H_m = 6I - C - Cᵀ над любым полукольцом;
- Dm m = det H_m (над ℤ); Xmat m = adjugate H_m (над ℤ),
  поэтому H_m * X_m = D_m • 1 и X_m * H_m = D_m • 1 — это и есть
  содержание "X_m = D_m H_m^{-1}" без деления;
- Dm m > 0 для m ≥ 1 — через положительную определённость H_m
  над ℝ: xᵀ H_m x = 4‖x‖² + ∑ (x_i - x_{i+1})².
  (Тождество det H_m = Tr S^m - 2 в общем m здесь НЕ доказывается:
  это отдельный пробел, см. отчёт; таблицы det для малых m —
  в LineDOrbitPair, по мере вычислимости decide.)

ЧЕСТНАЯ ГРАНИЦА МОДУЛЯ:
- Fix_m, Psi_m (парами), мост 149 — в LineDOrbitPair / LineDBridge.
- No sorry, no axiom, no native_decide, no decide (decide только
  в пробниках таблиц, не здесь).
-/

import Mathlib.Analysis.Matrix.PosDef
import Mathlib.LinearAlgebra.Matrix.Adjugate
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases

namespace Bgs.LineD.Defs

open Matrix
open scoped BigOperators

/-! ### Циклический сдвиг и матрица H_m -/

/-- Циклический сдвиг: (C x)_i = x_{i+1}. Индексы — ZMod m. -/
def shiftMat (m : ℕ) (α : Type*) [Zero α] [One α] : Matrix (ZMod m) (ZMod m) α :=
  Matrix.of fun i j => if j = i + 1 then 1 else 0

/-- H_m = 6I - C - Cᵀ. -/
def Hmat (m : ℕ) (α : Type*) [Ring α] : Matrix (ZMod m) (ZMod m) α :=
  (6 : α) • (1 : Matrix (ZMod m) (ZMod m) α) - shiftMat m α - (shiftMat m α)ᵀ

/-- D_m = det H_m (над ℤ). -/
def Dm (m : ℕ) [NeZero m] : ℤ := (Hmat m ℤ).det

/-- X_m = adjugate H_m (над ℤ): целочисленная версия D_m H_m^{-1}. -/
def Xmat (m : ℕ) [NeZero m] : Matrix (ZMod m) (ZMod m) ℤ := (Hmat m ℤ).adjugate

theorem Hmat_mul_Xmat (m : ℕ) [NeZero m] :
    Hmat m ℤ * Xmat m = Dm m • (1 : Matrix (ZMod m) (ZMod m) ℤ) :=
  Matrix.mul_adjugate _

theorem Xmat_mul_Hmat (m : ℕ) [NeZero m] :
    Xmat m * Hmat m ℤ = Dm m • (1 : Matrix (ZMod m) (ZMod m) ℤ) :=
  Matrix.adjugate_mul _

/-- H_m симметрична. -/
theorem Hmat_transpose (m : ℕ) (α : Type*) [CommRing α] :
    (Hmat m α)ᵀ = Hmat m α := by
  simp only [Hmat, Matrix.transpose_sub, Matrix.transpose_smul, Matrix.transpose_one,
    Matrix.transpose_transpose]
  rw [sub_right_comm]

/-- (C x)_i = x_{i+1}. -/
theorem shift_mulVec (m : ℕ) [NeZero m] (α : Type*) [Semiring α] (x : ZMod m → α) :
    shiftMat m α *ᵥ x = fun i => x (i + 1) := by
  ext i
  simp only [Matrix.mulVec_apply_eq_sum, shiftMat, Matrix.of_apply]
  rw [Finset.sum_eq_single (i + 1)]
  · simp
  · intro b _ hb
    simp [hb]
  · intro h
    exact absurd (Finset.mem_univ _) h

/-- (Cᵀ x)_i = x_{i-1}. -/
theorem shift_transpose_mulVec (m : ℕ) [NeZero m] (α : Type*) [Semiring α] (x : ZMod m → α) :
    (shiftMat m α)ᵀ *ᵥ x = fun i => x (i - 1) := by
  ext i
  simp only [Matrix.mulVec_apply_eq_sum, Matrix.transpose_apply, shiftMat, Matrix.of_apply]
  rw [Finset.sum_eq_single (i - 1)]
  · rw [sub_add_cancel]
    simp
  · intro b _ hb
    have hne : i ≠ b + 1 := by
      intro h
      apply hb
      rw [eq_sub_iff_add_eq]
      exact h.symm
    simp [hne]
  · intro h
    exact absurd (Finset.mem_univ _) h

/-! ### Переиндексация циклических сумм -/

theorem sum_addOne (m : ℕ) [NeZero m] (f : ZMod m → ℝ) :
    ∑ i, f (i + 1) = ∑ i, f i :=
  Equiv.sum_comp (Equiv.addRight (1 : ZMod m)) f

theorem sum_subOne (m : ℕ) [NeZero m] (f : ZMod m → ℝ) :
    ∑ i, f (i - 1) = ∑ i, f i := by
  have h := Equiv.sum_comp (Equiv.addRight (-1 : ZMod m)) f
  simp only [sub_eq_add_neg] at *
  exact h

/-! ### Положительная определённость H_m над ℝ -/

/-- Квадратичная форма H_m: xᵀ H x = 4‖x‖² + ∑ (x_i - x_{i+1})². -/
theorem Hmat_dotProduct (m : ℕ) [NeZero m] (x : ZMod m → ℝ) :
    x ⬝ᵥ (Hmat m ℝ) *ᵥ x
      = 4 * (∑ i, x i * x i) + ∑ i, (x i - x (i + 1)) * (x i - x (i + 1)) := by
  have hC : (shiftMat m ℝ) *ᵥ x = fun i => x (i + 1) := shift_mulVec m ℝ x
  have hCT : (shiftMat m ℝ)ᵀ *ᵥ x = fun i => x (i - 1) := shift_transpose_mulVec m ℝ x
  have hH : (Hmat m ℝ) *ᵥ x
      = (6 : ℝ) • x - (fun i => x (i + 1)) - (fun i => x (i - 1)) := by
    simp only [Hmat, Matrix.sub_mulVec, smul_mulVec, Matrix.one_mulVec, hC, hCT]
  rw [hH]
  simp only [dotProduct, Pi.sub_apply, Pi.smul_apply, smul_eq_mul]
  have hS : ∑ i, x i * x (i - 1) = ∑ i, x i * x (i + 1) := by
    have h1 : ∑ i, x i * x (i - 1) = ∑ i, x (i - 1) * x i := by
      apply Finset.sum_congr rfl
      intro i _
      rw [mul_comm]
    rw [h1]
    have h2 : ∑ i, x (i - 1) * x i = ∑ i, x (i - 1) * x ((i - 1) + 1) := by
      apply Finset.sum_congr rfl
      intro i _
      rw [sub_add_cancel]
    rw [h2]
    exact sum_subOne m (fun j => x j * x (j + 1))
  have hSq : ∑ i, (x i - x (i + 1)) * (x i - x (i + 1))
      = 2 * (∑ i, x i * x i) - 2 * (∑ i, x i * x (i + 1)) := by
    have hexp : ∀ i : ZMod m,
        (x i - x (i + 1)) * (x i - x (i + 1))
          = x i * x i - 2 * (x i * x (i + 1)) + x (i + 1) * x (i + 1) := by
      intro i
      ring
    rw [Finset.sum_congr rfl (fun i _ => hexp i)]
    rw [Finset.sum_add_distrib, Finset.sum_sub_distrib, ← Finset.mul_sum]
    have hSA : ∑ i, x (i + 1) * x (i + 1) = ∑ i, x i * x i :=
      sum_addOne m (fun j => x j * x j)
    rw [hSA]
    ring
  have hexpand : ∑ i, x i * ((6 : ℝ) * x i - x (i + 1) - x (i - 1))
      = 6 * (∑ i, x i * x i) - (∑ i, x i * x (i + 1)) - (∑ i, x i * x (i - 1)) := by
    have hterm : ∀ i : ZMod m,
        x i * ((6 : ℝ) * x i - x (i + 1) - x (i - 1))
          = 6 * (x i * x i) - x i * x (i + 1) - x i * x (i - 1) := by
      intro i
      ring
    rw [Finset.sum_congr rfl (fun i _ => hterm i)]
    rw [Finset.sum_sub_distrib, Finset.sum_sub_distrib, ← Finset.mul_sum]
  rw [hexpand, hS, hSq]
  ring

/-- H_m положительно определена над ℝ. -/
theorem Hmat_posDef (m : ℕ) [NeZero m] : (Hmat m ℝ).PosDef := by
  refine ⟨?_, ?_⟩
  · show (Hmat m ℝ)ᴴ = Hmat m ℝ
    rw [Matrix.conjTranspose_eq_transpose_of_trivial, Hmat_transpose]
  · intro x hx
    -- Переводим двойную сумму Finsupp в обычную двойную сумму по univ.
    have houter : x.sum (fun i xi => x.sum (fun j xj => star xi * Hmat m ℝ i j * xj))
        = ∑ i, x.sum (fun j xj => star (x i) * Hmat m ℝ i j * xj) := by
      apply Finsupp.sum_fintype
      intro i
      simp
    have hinner : ∀ i, x.sum (fun j xj => star (x i) * Hmat m ℝ i j * xj)
        = ∑ j, star (x i) * Hmat m ℝ i j * x j := by
      intro i
      apply Finsupp.sum_fintype
      intro j
      simp
    rw [houter]
    simp only [hinner]
    simp only [star_trivial]
    have hdot : (∑ i, ∑ j, x i * Hmat m ℝ i j * x j)
        = (fun i => x i) ⬝ᵥ (Hmat m ℝ) *ᵥ (fun i => x i) := by
      simp only [dotProduct, Matrix.mulVec_apply_eq_sum]
      apply Finset.sum_congr rfl
      intro i _
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro j _
      rw [mul_assoc]
    rw [hdot, Hmat_dotProduct m (fun i => x i)]
    have hx2 : (0 : ℝ) < ∑ i, x i * x i := by
      obtain ⟨i, hi⟩ : ∃ i, x i ≠ 0 := by
        by_contra h
        apply hx
        ext j
        by_contra hj
        exact h ⟨j, by simpa using hj⟩
      have h0 : ∀ j ∈ (Finset.univ : Finset (ZMod m)), (0 : ℝ) ≤ x j * x j :=
        fun j _ => mul_self_nonneg _
      have h1 : ∃ j ∈ (Finset.univ : Finset (ZMod m)), (0 : ℝ) < x j * x j :=
        ⟨i, Finset.mem_univ i, mul_self_pos.mpr hi⟩
      exact Finset.sum_pos' h0 h1
    have hnn : (0 : ℝ) ≤ ∑ i, (x i - x (i + 1)) * (x i - x (i + 1)) := by
      apply Finset.sum_nonneg
      intro j _
      exact mul_self_nonneg _
    linarith

/-- Каст H_m из ℤ в ℝ — та же матрица. -/
theorem Hmat_map_cast (m : ℕ) :
    (Hmat m ℤ).map (Int.castRingHom ℝ) = Hmat m ℝ := by
  ext i j
  simp only [Hmat, Matrix.map_apply, Matrix.sub_apply, Matrix.smul_apply, Matrix.one_apply,
    Matrix.transpose_apply, shiftMat, Matrix.of_apply]
  split_ifs <;> norm_num

/-- D_m > 0 при m ≥ 1. -/
theorem Dm_pos (m : ℕ) [NeZero m] : 0 < Dm m := by
  have hdet : (0 : ℝ) < (Hmat m ℝ).det := (Hmat_posDef m).det_pos
  have hcast : ((Dm m : ℤ) : ℝ) = (Hmat m ℝ).det := by
    show ((Hmat m ℤ).det : ℝ) = (Hmat m ℝ).det
    rw [← Hmat_map_cast m]
    exact RingHom.map_det (Int.castRingHom ℝ) (Hmat m ℤ)
  have : (0 : ℝ) < (Dm m : ℝ) := by rw [hcast]; exact hdet
  exact_mod_cast this

#print axioms Bgs.LineD.Defs.Hmat_mul_Xmat
#print axioms Bgs.LineD.Defs.Xmat_mul_Hmat
#print axioms Bgs.LineD.Defs.Hmat_transpose
#print axioms Bgs.LineD.Defs.Dm_pos

end Bgs.LineD.Defs
