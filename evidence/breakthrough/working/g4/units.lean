/-
  Bgs/LineBNAverageUnits.lean — среднее по единицам для 175 (исправленный таргет F_m).

  Проверен в тестовой копии 2026-11-01 (пересборка EXIT:0, стандартные аксиомы);
  в main импортируется из `Bgs.lean`. Существующие модули моста НЕ правятся:
  это аддитивный модуль рядом с ними.

  ЧЕСТНАЯ КАРТИНА. Источник (phase1_trace_formula.md §5, blob abdbfbc3):
  F_m — среднее ПО ЕДИНИЦАМ mod g' с нормировкой 1/φ(g'):
    (1/|𝒩_X|) Σ Ψ = (1/φ(g′)) Σ_{ν∈(Z/g′)^×} Ψ(Z_m(ν;η)) + O(...),
  а мост в main (LineBNAverage.nuAvg) усредняет по ВСЕМ вычетам с
  нормировкой 1/g' — неверный таргет (слова «units» в файлах моста нет).
  При m=1 это не косметика: hEquidist в форме моста ЛОЖНА
  (LineBNAverageM1.hEquidist_one_false: зазор 2 против оценки → 0).

  * §1: nuAvgUnits — среднее B по единицам (ZMod g')ˣ, нормировка 1/φ(g').
  * §2: при m=1 среднее по окну РАВНО nuAvgUnits (зазор 0): ν N = 1 на
    всём окне, а единицы mod 2 — только {1}, φ(2) = 1.
  * §3: nAverageM1_units — теорема среднего при m=1 с таргетом-единицами:
    только первый член ошибки (2·s0+1)·π·s2/X. Расхождение ≈2π с
    границей 175 (s2·s0/X) СОХРАНЯЕТСЯ — зафиксировано, не скрыто.
  * §4: nAverageTup_units — зеркало общего моста nAverageTup (m ≥ 2)
    с таргетом nuAvgUnits и гипотезой hEquidistUnits (равномерность ν_N
    по единицам). hEquidistUnits НЕ доказывается: это остаток
    (член D/X от неполных блоков + равномерность по единицам).

  No `sorry`, no `admit`, no `axiom`, no `native_decide` in this file.
-/

import Bgs.LineBNAverageBridge
import Bgs.LineBNAverageM1

open Bgs.LineB
open Bgs.LineB.TraceFormula Bgs.LineB.Derand Bgs.LineB.Tsum Bgs.LineB.Expand
open Bgs.LineB.NAverageBridge Bgs.LineB.NAverage Bgs.LineB.NAverageM1

namespace Bgs.LineB.NAverageUnits

/-! ### §1. Среднее по единицам. -/

/-- Среднее по единицам mod g' с нормировкой 1/φ(g') — таргет F_m
    источника (phase1 §5). Сумма — по типу единиц (ZMod g')ˣ. -/
noncomputable def nuAvgUnits {g' : ℕ} [NeZero g'] (B : ZMod g' → ℝ) : ℝ :=
  (∑ u : (ZMod g')ˣ, B (u : ZMod g')) / (Nat.totient g' : ℝ)

/-! ### §2. При m = 1: среднее по окну равно среднему по единицам. -/

/-- Единицы mod 2 — только {1}. -/
lemma units_zmod_two : (Finset.univ : Finset (ZMod 2)ˣ) = {1} := by decide

/-- Среднее по единицам при g' = 2 — просто значение в 1
    (φ(2) = 1, единственная единица — 1). -/
lemma nuAvgUnits_two (B : ZMod 2 → ℝ) : nuAvgUnits B = B 1 := by
  unfold nuAvgUnits
  rw [units_zmod_two, Finset.sum_singleton]
  have htot : Nat.totient 2 = 1 := by decide
  rw [htot]
  simp

/-- Среднее по единицам при m = 1 — значение в 1 (gp 1 = 2). -/
lemma nuAvgUnits_one (ĝ : ℤ → ℂ) :
    nuAvgUnits (Btup 1 ĝ) = Btup 1 ĝ 1 :=
  nuAvgUnits_two (Btup 1 ĝ)

/-- Среднее по окну при m = 1 равно среднему по единицам:
    ν N = 1 на всём окне, а единицы mod 2 — только 1. -/
theorem winAvg_units_one (ĝ : ℤ → ℂ) (ν : ℕ → ZMod (gp 1)) (X : ℝ)
    (hν : ∀ N ∈ window X (Dm 1).toNat, (ν N) * (N : ZMod (gp 1)) = 1)
    (hW : (window X (Dm 1).toNat).Nonempty) :
    winAvg (window X (Dm 1).toNat) (fun N => Btup 1 ĝ (ν N))
      = nuAvgUnits (Btup 1 ĝ) := by
  rw [nuAvgUnits_one]
  have hconst : ∀ N ∈ window X (Dm 1).toNat, Btup 1 ĝ (ν N) = Btup 1 ĝ 1 := by
    intro N hN
    rw [window_nu_eq_one hN (hν N hN)]
  have hcard : ((window X (Dm 1).toNat).card : ℝ) ≠ 0 := by
    exact_mod_cast (Finset.card_pos.mpr hW).ne'
  unfold winAvg
  rw [Finset.sum_congr rfl (fun N hN => hconst N hN), Finset.sum_const,
    nsmul_eq_mul, mul_div_cancel_left₀ _ hcard]

/-! ### §3. Теорема среднего при m = 1 с таргетом-единицами. -/

/-- Средняя теорема 175 при `m = 1` с исправленным таргетом:
    зазор между средним по окну и средним по единицам равен 0,
    остаётся только первый член ошибки `(2·s0+1)·π·s2/X`.
    Расхождение `≈2π` с границей 175 (`s2·s0/X`) сохраняется. -/
theorem nAverageM1_units (ĝ : ℤ → ℂ) (a : ∀ N : ℕ, ZMod N) (TrU : ℕ → ℂ) (X : ℝ)
    (hX1 : 1 < X)
    (hs2 : Summable fun k : ℤ => (k : ℝ) ^ 2 * ‖ĝ k‖)
    (ha : ∀ N ∈ window X (Dm 1).toNat, 2 * (a N) * (-4) = 1)
    (hTrU : ∀ N ∈ window X (Dm 1).toNat, ∀ [NeZero N],
      TrU N = ((kickMatInf N ĝ * catMat N (a N)) ^ 1).trace)
    (hW : (window X (Dm 1).toNat).Nonempty)
    (hC'le : Real.pi * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖) ≤ X) :
    |winAvg (window X (Dm 1).toNat) (fun N => ‖TrU N‖ ^ 2)
      - nuAvgUnits (Btup 1 ĝ)|
      ≤ ((2 * (∑' k : ℤ, ‖ĝ k‖) + 1)
          * (Real.pi * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖))) / X := by
  obtain ⟨ν, R, hν, hTr⟩ := traceHenceTup_one ĝ a TrU X hX1 hs2 ha hTrU
  have hs0 : Summable fun k : ℤ => ‖ĝ k‖ := summable_norm_of_summable_sq ĝ hs2
  set s0 : ℝ := ∑' k : ℤ, ‖ĝ k‖ with hs0def
  set s2 : ℝ := ∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖ with hs2def
  set C' : ℝ := Real.pi * s2 with hC'def
  have hs0nn : 0 ≤ s0 := tsum_nonneg (fun k => norm_nonneg _)
  have hs2nn : 0 ≤ s2 := tsum_nonneg (fun k => mul_nonneg (sq_nonneg _) (norm_nonneg _))
  have hC'0 : 0 ≤ C' := by rw [hC'def]; exact mul_nonneg Real.pi_nonneg hs2nn
  have hXpos : 0 < X := lt_trans zero_lt_one hX1
  have hmem : ∀ N ∈ window X (Dm 1).toNat, X < N := by
    intro N hN
    exact (mem_window (le_of_lt hXpos) hN).1
  have hpt : ∀ N ∈ window X (Dm 1).toNat,
      |‖TrU N‖ ^ 2 - Btup 1 ĝ (ν N)|
        ≤ ((2 * s0 + 1) * C') / (N : ℝ) := by
    intro N hN
    have h := pointwiseTup 1 ĝ hXpos hs0nn hC'0 hC'le
      (fun ν => Ztup_norm_le 1 ĝ hs0 ν) hTr hmem N hN
    simpa only [pow_one] using h
  have havg1 : |winAvg (window X (Dm 1).toNat) (fun N => ‖TrU N‖ ^ 2)
        - winAvg (window X (Dm 1).toNat) (fun N => Btup 1 ĝ (ν N))|
      ≤ winAvg (window X (Dm 1).toNat) (fun N => ((2 * s0 + 1) * C') / (N : ℝ)) := by
    apply le_trans (avg_sub_abs_le _ _ _ hW)
    exact avg_mono _ _ _ hW (fun N hN => hpt N hN)
  have hK0 : 0 ≤ (2 * s0 + 1) * C' :=
    mul_nonneg (by linarith) hC'0
  have havg2 : winAvg (window X (Dm 1).toNat) (fun N => ((2 * s0 + 1) * C') / (N : ℝ))
      ≤ ((2 * s0 + 1) * C') / X := by
    apply avg_le_of_forall_le _ _ _ hW
    intro N hN
    have hNX : X < (N : ℝ) := hmem N hN
    have h1 : (1 : ℝ) / (N : ℝ) ≤ 1 / X := one_div_le_one_div_of_le hXpos (le_of_lt hNX)
    calc ((2 * s0 + 1) * C') / (N : ℝ)
        = ((2 * s0 + 1) * C') * (1 / (N : ℝ)) := div_eq_mul_one_div _ _
      _ ≤ ((2 * s0 + 1) * C') * (1 / X) := mul_le_mul_of_nonneg_left h1 hK0
      _ = ((2 * s0 + 1) * C') / X := (div_eq_mul_one_div _ _).symm
  have hgap : |winAvg (window X (Dm 1).toNat) (fun N => Btup 1 ĝ (ν N))
        - nuAvgUnits (Btup 1 ĝ)| = 0 := by
    rw [winAvg_units_one ĝ ν X hν hW, sub_self, abs_zero]
  have havg : |winAvg (window X (Dm 1).toNat) (fun N => ‖TrU N‖ ^ 2)
        - winAvg (window X (Dm 1).toNat) (fun N => Btup 1 ĝ (ν N))|
      + |winAvg (window X (Dm 1).toNat) (fun N => Btup 1 ĝ (ν N))
        - nuAvgUnits (Btup 1 ĝ)|
      ≤ ((2 * s0 + 1) * C') / X + 0 :=
    add_le_add (le_trans havg1 havg2) (le_of_eq hgap)
  have hfin := le_trans (abs_sub_le _ _ _) havg
  rw [hC'def] at hfin
  simpa only [add_zero] using hfin

/-! ### §4. Общий мост с таргетом-единицами (m ≥ 2, условно). -/

/-- Зеркало `nAverageTup` с исправленным таргетом: среднее по единицам
    вместо среднего по всем вычетам. Гипотеза `hEquidistUnits` —
    равномерность `ν_N` по единицам — НЕ доказывается здесь: это
    остаток 175-full (член D/X от неполных блоков + равномерность
    по единицам). Первый член ошибки — тот же, что у моста. -/
theorem nAverageTup_units (m : ℕ) [NeZero m] [NeZero (gp m)] (ĝ : ℤ → ℂ)
    (a : ∀ N : ℕ, ZMod N) (TrU : ℕ → ℂ) (X : ℝ) (D Deff : ℝ)
    (hm : 2 ≤ m) (hX1 : 1 < X)
    (hs2 : Summable fun k : ℤ => (k : ℝ) ^ 2 * ‖ĝ k‖)
    (ha : ∀ N ∈ NAverage.window X (Dm m).toNat, 2 * (a N) * (-4) = 1)
    (hTrU : ∀ N ∈ NAverage.window X (Dm m).toNat, ∀ [NeZero N],
      TrU N = ((Tsum.kickMatInf N ĝ * catMat N (a N)) ^ m).trace)
    (hW : (NAverage.window X (Dm m).toNat).Nonempty)
    (hC'le : Real.pi * (m : ℝ) * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖)
      * (∑' k : ℤ, ‖ĝ k‖) ^ (m - 1) ≤ X)
    (hEquidistUnits : ∀ ν : ℕ → ZMod (gp m),
      (∀ N ∈ NAverage.window X (Dm m).toNat, (ν N) * (N : ZMod (gp m)) = 1) →
      |NAverage.winAvg (NAverage.window X (Dm m).toNat) (fun N => Btup m ĝ (ν N))
        - nuAvgUnits (Btup m ĝ)|
        ≤ (D : ℝ) * min ((∑' k : ℤ, ‖ĝ k‖) ^ (2 * m)) Deff / X) :
    |NAverage.winAvg (NAverage.window X (Dm m).toNat)
        (fun N => ‖TrU N‖ ^ 2) - nuAvgUnits (Btup m ĝ)|
      ≤ ((2 * (∑' k : ℤ, ‖ĝ k‖) ^ m + 1)
          * (Real.pi * (m : ℝ) * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖)
            * (∑' k : ℤ, ‖ĝ k‖) ^ (m - 1))) / X
        + (D : ℝ) * min ((∑' k : ℤ, ‖ĝ k‖) ^ (2 * m)) Deff / X := by
  have hgp : 0 < gp m := Nat.pos_of_ne_zero (NeZero.ne _)
  obtain ⟨ν, R, hν, hTr⟩ := traceHenceTup m ĝ a TrU X hm hX1 hs2 ha hTrU
  have hs0 : Summable fun k : ℤ => ‖ĝ k‖ := Tsum.summable_norm_of_summable_sq ĝ hs2
  set s0 : ℝ := ∑' k : ℤ, ‖ĝ k‖ with hs0def
  set s2 : ℝ := ∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖ with hs2def
  set C' : ℝ := Real.pi * (m : ℝ) * s2 * s0 ^ (m - 1) with hC'def
  have hs0nn : 0 ≤ s0 := tsum_nonneg (fun k => norm_nonneg _)
  have hs2nn : 0 ≤ s2 := tsum_nonneg
    (fun k => mul_nonneg (sq_nonneg _) (norm_nonneg _))
  have hC'0 : 0 ≤ C' := by
    rw [hC'def]
    apply mul_nonneg
    apply mul_nonneg
    apply mul_nonneg
    · exact Real.pi_nonneg
    · exact_mod_cast Nat.zero_le m
    · exact hs2nn
    · exact pow_nonneg hs0nn _
  have hXpos : 0 < X := lt_trans zero_lt_one hX1
  have hmem : ∀ N ∈ NAverage.window X (Dm m).toNat, X < N := by
    intro N hN
    exact (NAverage.mem_window (le_of_lt hXpos) hN).1
  have hpt : ∀ N ∈ NAverage.window X (Dm m).toNat,
      |‖TrU N‖ ^ 2 - Btup m ĝ (ν N)|
        ≤ ((2 * s0 ^ m + 1) * C') / (N : ℝ) :=
    pointwiseTup m ĝ hXpos hs0nn hC'0 hC'le
      (fun ν => Ztup_norm_le m ĝ hs0 ν) hTr hmem
  have havg1 : |NAverage.winAvg (NAverage.window X (Dm m).toNat)
        (fun N => ‖TrU N‖ ^ 2)
      - NAverage.winAvg (NAverage.window X (Dm m).toNat)
        (fun N => Btup m ĝ (ν N))|
      ≤ NAverage.winAvg (NAverage.window X (Dm m).toNat)
        (fun N => ((2 * s0 ^ m + 1) * C') / (N : ℝ)) := by
    apply le_trans (NAverage.avg_sub_abs_le _ _ _ hW)
    exact NAverage.avg_mono _ _ _ hW (fun N hN => hpt N hN)
  have hK0 : 0 ≤ (2 * s0 ^ m + 1) * C' := by
    apply mul_nonneg
    · linarith [pow_nonneg hs0nn m]
    · exact hC'0
  have havg2 : NAverage.winAvg (NAverage.window X (Dm m).toNat)
        (fun N => ((2 * s0 ^ m + 1) * C') / (N : ℝ))
      ≤ ((2 * s0 ^ m + 1) * C') / X := by
    apply NAverage.avg_le_of_forall_le _ _ _ hW
    intro N hN
    have hNX : X < (N : ℝ) := hmem N hN
    have h1 : (1 : ℝ) / (N : ℝ) ≤ 1 / X :=
      one_div_le_one_div_of_le hXpos (le_of_lt hNX)
    calc ((2 * s0 ^ m + 1) * C') / (N : ℝ)
        = ((2 * s0 ^ m + 1) * C') * (1 / (N : ℝ)) := div_eq_mul_one_div _ _
      _ ≤ ((2 * s0 ^ m + 1) * C') * (1 / X) :=
        mul_le_mul_of_nonneg_left h1 hK0
      _ = ((2 * s0 ^ m + 1) * C') / X := (div_eq_mul_one_div _ _).symm
  have havg : |NAverage.winAvg (NAverage.window X (Dm m).toNat)
        (fun N => ‖TrU N‖ ^ 2)
      - NAverage.winAvg (NAverage.window X (Dm m).toNat)
        (fun N => Btup m ĝ (ν N))|
      + |NAverage.winAvg (NAverage.window X (Dm m).toNat)
        (fun N => Btup m ĝ (ν N)) - nuAvgUnits (Btup m ĝ)|
      ≤ ((2 * s0 ^ m + 1) * C') / X
        + (D : ℝ) * min (s0 ^ (2 * m)) Deff / X :=
    add_le_add (le_trans havg1 havg2) (hEquidistUnits ν hν)
  have hfin := le_trans (abs_sub_le _ _ _) havg
  rw [hC'def] at hfin
  exact hfin

/- Axiom audit for all main theorems of this module. -/
#print axioms Bgs.LineB.NAverageUnits.nuAvgUnits_two
#print axioms Bgs.LineB.NAverageUnits.nuAvgUnits_one
#print axioms Bgs.LineB.NAverageUnits.winAvg_units_one
#print axioms Bgs.LineB.NAverageUnits.nAverageM1_units
#print axioms Bgs.LineB.NAverageUnits.nAverageTup_units

end Bgs.LineB.NAverageUnits
