/-
  Bgs/LineBNAverageM1.lean — случай `m = 1` для 175.

  Проверен в тестовой копии 2026-11-01 (пересборка EXIT:0, стандартные аксиомы);
  в main импортируется из `Bgs.lean`.

  ЧЕСТНАЯ КАРТИНА. Мост 175 (`LineBNAverageBridge`) требует `2 ≤ m`,
  потому что шаг Гаусса в tsum-форме 163 требует `m ≥ 2`. Для `m = 1`
  шаг Гаусса закрыт вручную в `LineBTraceM1`, поэтому цепочка
  переигрывается здесь с `m = 1`:

  * §1: hence-форма при `m = 1` (`tsum_with_inv_one`, `henceTup_one`,
    `traceHenceTup_one`): след = `TrM * (Ztup 1 ĝ ν + R)`,
    `‖R‖ ≤ π·s2/N` — ТОЧНАЯ специализация общей границы (c).
    Точечная оценка `pointwiseTup` при `m = 1` уже общая, первый
    член ошибки — `(2·s0+1)·π·s2/X` против `s2·s0/X` из 175:
    отношение `π·(2 + s0⁻¹) ≈ 2π` — расхождение в константе
    СОХРАНЯЕТСЯ при `m = 1`, не исчезает.
  * §2: на окне при `m = 1` вычет постоянен: `gp 1 = 2`,
    `Dm 1 = 4`, окно требует `gcd(N, 4) = 1`, т.е. `N` нечётно,
    поэтому `ν N = 1` для всех `N` окна.
  * §3: значения профиля при `m = 1` вычисляются явно:
    `Ztup 1 ĝ 0 = ∑' ĝ`, `Ztup 1 ĝ 1 = ∑' (-1)^k ĝ k`
    (так как `NmZ 1 n = (n 0)²`, `yp 1 = 1`, `gp 1 = 2`).
  * §4: теорема среднего при `m = 1` с ТОЧНЫМ зазором
    `|Btup 1 ĝ 1 - Btup 1 ĝ 0| / 2` вместо гипотезы `hEquidist`:
    среднее по окну равно `Btup 1 ĝ 1`, а `nuAvg` — среднее
    по ВСЕМ вычетам `(Btup 0 + Btup 1) / 2`.
  * §5: гипотеза `hEquidist` в форме моста при `m = 1` ЛОЖНА
    в общем случае: для `ĝ₀ = 1` на `{0, 1}` зазор равен `2`
    (константа, не убывающая с `X`), а правая часть
    `D·min(s0², Deff)/X → 0`. Конкретное опровержение:
    `X = 4`, `D = Deff = 1`, окно `{5, 7}`.
    Следствие: если граница 175 верна при `m = 1`, то её `F_1`
    — это среднее по ЕДИНИЦАМ (только `ν = 1`), а не по всем
    вычетам; `nuAvg` моста (по всем вычетам) с границей в этой
    точке НЕ совпадает. Определения здесь НЕ подгоняются:
    зафиксирован именно этот разрыв, а не «исправленный» `nuAvg`.
-/

import Bgs.LineBNAverageBridge
import Bgs.LineBTraceM1

open Filter Topology
open Bgs.LineB.TraceFormula Bgs.LineB.Gauss Bgs.LineB.Expand Bgs.LineB.Derand
open Bgs.LineB.Tsum
open Bgs.LineB.NAverageBridge Bgs.LineB.NAverage Bgs.LineB.TraceM1

namespace Bgs.LineB.NAverageM1

/-! ### §0. Числа при `m = 1`: `Dm 1 = 4`, `gp 1 = 2`, `yp 1 = 1`. -/

lemma dm_one : (Dm 1).toNat = 4 := by decide

lemma gp_one : gp 1 = 2 := by decide

lemma yp_one : yp 1 = 1 := by decide

/-- `NeZero (gp 1)` как инстанс модуля (нужен для `nuAvg` и `pointwiseTup`). -/
instance : NeZero (gp 1) := ⟨by decide⟩

/-! ### §1. Hence-форма при `m = 1` (переигровка §2–§3 моста). -/

/-- Tsum-форма + оценка (c) при `m = 1` для ЗАРАНЕЕ выбранного
обратного `b₀` (зеркало `tsum_with_inv`, с леммами `TraceM1`). -/
lemma tsum_with_inv_one (N : ℕ) [NeZero N] (ĝ : ℤ → ℂ)
    (a : ZMod N) (hcop : (Dm 1).toNat.Coprime N) (hN : 2 ≤ N)
    (ht0 : 2 * a * (-4) = 1) (hs2 : Summable fun k : ℤ => (k : ℝ) ^ 2 * ‖ĝ k‖) :
    ∃ b : ℕ, ((N * b : ℕ) : ZMod (Dm 1).toNat) = 1 ∧
      ((kickMatInf N ĝ * catMat N a) ^ 1).trace
        = (catMat N a ^ 1).trace
          * ∑' n : Fin 1 → ℤ, phiFun 1 ĝ n * phaseFun 1 N b n ∧
      ‖(catMat N a ^ 1).trace‖ = 1 ∧
      ‖((kickMatInf N ĝ * catMat N a) ^ 1).trace
        - (catMat N a ^ 1).trace
          * ∑' n : Fin 1 → ℤ, phiFun 1 ĝ n * phase0Fun 1 N b n‖
        ≤ Real.pi * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖) / (N : ℝ) := by
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
  have hTr : ((kickMatInf N ĝ * catMat N a) ^ 1).trace
      = (catMat N a ^ 1).trace
        * ∑' n : Fin 1 → ℤ, phiFun 1 ĝ n * phaseFun 1 N b₀ n :=
    (tendsto_nhds_unique (by rw [hEq]; exact hL2') hL1).symm
  refine ⟨b₀, hb₀, hTr, (hS ∅).2, ?_⟩
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
  rw [hTr, ← mul_sub, hdiff, norm_mul, (hS ∅).2, one_mul]
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

/-- Hence-форма при `m = 1` (зеркало `henceTup`): след =
`TrM * (Ztup 1 ĝ ν + R)`, `ν * N = 1` в `ZMod (gp 1)`,
`‖R‖ ≤ π·s2/N`. -/
lemma henceTup_one (N : ℕ) [NeZero N] (ĝ : ℤ → ℂ)
    (a : ZMod N) (hcop : (Dm 1).toNat.Coprime N) (hN : 2 ≤ N)
    (ht0 : 2 * a * (-4) = 1) (hs2 : Summable fun k : ℤ => (k : ℝ) ^ 2 * ‖ĝ k‖) :
    ∃ ν : ZMod (gp 1), ∃ R : ℂ,
      (ν * (N : ZMod (gp 1)) = 1) ∧
      (∃ TrM : ℂ, ((kickMatInf N ĝ * catMat N a) ^ 1).trace
        = TrM * (Ztup 1 ĝ ν + R) ∧ ‖TrM‖ = 1 ∧
        ‖R‖ ≤ Real.pi * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖) / (N : ℝ)) := by
  have hgp : 0 < gp 1 := gp_pos (by norm_num)
  have hdvd : gp 1 ∣ (Dm 1).toNat := gp_dvd_Dm (by norm_num)
  have hs0 := summable_norm_of_summable_sq ĝ hs2
  obtain ⟨b₀, hb₀, hTr, hNorm, hErr⟩ := tsum_with_inv_one N ĝ a hcop hN ht0 hs2
  have hsumQ := summable_mode_one ĝ hs0 N b₀
  have hsum0 := summable_mode0_one ĝ hs0 N b₀
  have hsplit : (∑' n : Fin 1 → ℤ, phiFun 1 ĝ n * phase0Fun 1 N b₀ n)
      + (∑' n : Fin 1 → ℤ, (phiFun 1 ĝ n * phaseFun 1 N b₀ n
        - phiFun 1 ĝ n * phase0Fun 1 N b₀ n))
      = ∑' n : Fin 1 → ℤ, phiFun 1 ĝ n * phaseFun 1 N b₀ n := by
    rw [← Summable.tsum_add hsum0 (hsumQ.sub hsum0)]
    apply tsum_congr
    intro n
    ring
  have hZ : Ztup 1 ĝ (((b₀ % gp 1 : ℕ) : ZMod (gp 1)))
      = ∑' n : Fin 1 → ℤ, phiFun 1 ĝ n * phase0Fun 1 N b₀ n := by
    unfold Ztup
    apply tsum_congr
    intro n
    rw [phase0Fun_eq_phaseTup 1 N b₀ n hgp]
  refine ⟨((b₀ % gp 1 : ℕ) : ZMod (gp 1)),
    ∑' n : Fin 1 → ℤ, (phiFun 1 ĝ n * phaseFun 1 N b₀ n
      - phiFun 1 ĝ n * phase0Fun 1 N b₀ n),
    nu_mul 1 N b₀ hgp hdvd hb₀, (catMat N a ^ 1).trace, ?_, hNorm, ?_⟩
  · rw [hTr, ← hsplit, ← hZ]
  · have hRval : (catMat N a ^ 1).trace
        * (∑' n : Fin 1 → ℤ, (phiFun 1 ĝ n * phaseFun 1 N b₀ n
          - phiFun 1 ĝ n * phase0Fun 1 N b₀ n))
        = ((kickMatInf N ĝ * catMat N a) ^ 1).trace
          - (catMat N a ^ 1).trace
            * (∑' n : Fin 1 → ℤ, phiFun 1 ĝ n * phase0Fun 1 N b₀ n) := by
      rw [hTr, ← hsplit]
      rw [mul_add, add_sub_cancel_left]
    have hnormR : ‖∑' n : Fin 1 → ℤ, (phiFun 1 ĝ n * phaseFun 1 N b₀ n
        - phiFun 1 ĝ n * phase0Fun 1 N b₀ n)‖
        = ‖((kickMatInf N ĝ * catMat N a) ^ 1).trace
          - (catMat N a ^ 1).trace
            * (∑' n : Fin 1 → ℤ, phiFun 1 ĝ n * phase0Fun 1 N b₀ n)‖ := by
      rw [← hRval, norm_mul, hNorm, one_mul]
    rw [hnormR]
    exact hErr

/-- Hence-форма на всём окне при `m = 1` (зеркало `traceHenceTup`). -/
theorem traceHenceTup_one (ĝ : ℤ → ℂ) (a : ∀ N : ℕ, ZMod N)
    (TrU : ℕ → ℂ) (X : ℝ) (hX1 : 1 < X)
    (hs2 : Summable fun k : ℤ => (k : ℝ) ^ 2 * ‖ĝ k‖)
    (ha : ∀ N ∈ window X (Dm 1).toNat, 2 * (a N) * (-4) = 1)
    (hTrU : ∀ N ∈ window X (Dm 1).toNat, ∀ [NeZero N],
      TrU N = ((kickMatInf N ĝ * catMat N (a N)) ^ 1).trace) :
    ∃ ν : ℕ → ZMod (gp 1), ∃ R : ℕ → ℂ,
      (∀ N ∈ window X (Dm 1).toNat, (ν N) * (N : ZMod (gp 1)) = 1) ∧
      (∀ N ∈ window X (Dm 1).toNat, ∃ TrM : ℂ,
        TrU N = TrM * (Ztup 1 ĝ (ν N) + R N) ∧ ‖TrM‖ = 1 ∧
        ‖R N‖ ≤ Real.pi * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖) / (N : ℝ)) := by
  have hper : ∀ N : ℕ, ∃ ν₀ : ZMod (gp 1), ∃ R₀ : ℂ, ∃ TrM₀ : ℂ,
      N ∈ window X (Dm 1).toNat →
      (ν₀ * (N : ZMod (gp 1)) = 1) ∧
      TrU N = TrM₀ * (Ztup 1 ĝ ν₀ + R₀) ∧ ‖TrM₀‖ = 1 ∧
      ‖R₀‖ ≤ Real.pi * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖) / (N : ℝ) := by
    intro N
    by_cases hN : N ∈ window X (Dm 1).toNat
    · have hmem := mem_window (le_of_lt (lt_trans zero_lt_one hX1)) hN
      have hN2 : 2 ≤ N := by
        have h1 : (1 : ℝ) < (N : ℝ) := lt_trans hX1 hmem.1
        have h2 : 1 < N := by exact_mod_cast h1
        omega
      haveI : NeZero N := ⟨by omega⟩
      have hcop : (Dm 1).toNat.Coprime N := hmem.2.2.symm
      obtain ⟨ν₀, R₀, hν₀, TrM₀, hTr₀, hNorm₀, hR₀⟩ :=
        henceTup_one N ĝ (a N) hcop hN2 (ha N hN) hs2
      rw [hTrU N hN]
      exact ⟨ν₀, R₀, TrM₀, fun _ => ⟨hν₀, hTr₀, hNorm₀, hR₀⟩⟩
    · exact ⟨0, 0, 0, fun h => absurd h hN⟩
  choose ν R TrM h using hper
  exact ⟨ν, R, fun N hN => (h N hN).1,
    fun N hN => ⟨TrM N, (h N hN).2.1, (h N hN).2.2.1, (h N hN).2.2.2⟩⟩

/-! ### §2. На окне при `m = 1` вычет постоянен: `ν N = 1`. -/

/-- Взаимная простота из принадлежности к окну. -/
lemma window_coprime_one {X : ℝ} {N : ℕ} (hN : N ∈ window X (Dm 1).toNat) :
    Nat.Coprime N (Dm 1).toNat := by
  rw [window, Finset.mem_filter] at hN
  exact hN.2

/-- При `m = 1` каждое `N` окна равно `1` в `ZMod (gp 1)`:
окно требует `gcd(N, 4) = 1`, значит `N` нечётно. -/
lemma window_cast_eq_one {X : ℝ} {N : ℕ} (hN : N ∈ window X (Dm 1).toNat) :
    (N : ZMod (gp 1)) = 1 := by
  have hcop := window_coprime_one hN
  rw [dm_one] at hcop
  have hodd : Odd N := by
    by_contra h
    rw [Nat.not_odd_iff_even] at h
    obtain ⟨j, hj⟩ := h
    have h1 : Nat.gcd N 4 = 1 := hcop
    have h2 : (2 : ℕ) ∣ Nat.gcd N 4 := Nat.dvd_gcd ⟨j, by omega⟩ ⟨2, rfl⟩
    rw [h1] at h2
    exact (by norm_num : ¬ (2 : ℕ) ∣ 1) h2
  have hmod : N ≡ 1 [MOD gp 1] := by
    rw [gp_one]
    show N ≡ 1 [MOD 2]
    rw [Nat.ModEq]
    simp [Nat.odd_iff.mp hodd]
  simpa using (ZMod.natCast_eq_natCast_iff N 1 (gp 1)).mpr hmod

/-- Обратный вычет на окне при `m = 1` — всегда `1`. -/
lemma window_nu_eq_one {X : ℝ} {N : ℕ} (hN : N ∈ window X (Dm 1).toNat)
    {ν : ZMod (gp 1)} (hν : ν * (N : ZMod (gp 1)) = 1) : ν = 1 := by
  rw [window_cast_eq_one hN, mul_one] at hν
  exact hν

/-! ### §3. Значения профиля при `m = 1`. -/

/-- `NmZ 1 n = (n 0)²`: двойная сумма по `Fin 1` — один член,
`pellX 0 = 1`. -/
lemma NmZ_one (n : Fin 1 → ℤ) : NmZ 1 n = (n 0) ^ 2 := by
  unfold NmZ
  rw [Fin.sum_univ_one, Fin.sum_univ_one]
  change n 0 * n 0 * pellX (dist 1 0 0) = n 0 ^ 2
  rw [show dist 1 (0 : ℕ) (0 : ℕ) = 0 by decide, show pellX 0 = 1 by decide]
  ring

/-- `phiFun 1 ĝ n = ĝ (n 0)`: произведение по одноэлементному `ZMod 1`. -/
lemma phiFun_one (ĝ : ℤ → ℂ) (n : Fin 1 → ℤ) : phiFun 1 ĝ n = ĝ (n 0) := by
  unfold phiFun
  have huniv : (Finset.univ : Finset (ZMod 1)) = {0} := by decide
  rw [huniv, Finset.prod_singleton]
  congr 1

/-- `(-1)` в чётной/нечётной степени: из равенства вычетов mod 2. -/
lemma neg_one_zpow_of_modEq_two {a b : ℤ} (h : a ≡ b [ZMOD 2]) :
    (-1 : ℂ) ^ a = (-1 : ℂ) ^ b := by
  have h2 : a % 2 = b % 2 := h
  rcases Int.even_or_odd a with ha | ha
  · have hb : Even b := by
      rw [Int.even_iff] at ha ⊢
      rw [← h2, ha]
    rw [ha.neg_one_zpow, hb.neg_one_zpow]
  · have hb : Odd b := by
      rw [Int.odd_iff] at ha ⊢
      rw [← h2, ha]
    rw [ha.neg_one_zpow, hb.neg_one_zpow]

/-- Фаза при `m = 1`, `ν = 1`: `e(-k²/2) = (-1)^k`. -/
lemma exp_neg_sq_half (k : ℤ) : e (-(k : ℝ) ^ 2 / 2) = (-1 : ℂ) ^ k := by
  have hmod : -k ^ 2 ≡ k [ZMOD 2] := by
    rw [Int.modEq_iff_dvd]
    rcases Int.even_or_odd k with ⟨j, hj⟩ | ⟨j, hj⟩
    · exact ⟨j * (2 * j + 1), by rw [hj]; ring⟩
    · exact ⟨(2 * j + 1) * (j + 1), by rw [hj]; ring⟩
  have hexp : 2 * Real.pi * Complex.I * (((-(k : ℝ) ^ 2 / 2 : ℝ)) : ℂ)
      = ((-k ^ 2 : ℤ) : ℂ) * (Real.pi * Complex.I) := by
    push_cast
    ring
  unfold e
  rw [hexp, Complex.exp_int_mul, Complex.exp_pi_mul_I]
  exact neg_one_zpow_of_modEq_two hmod

/-- Значения вычетов `ZMod (gp 1)` как натуральных представителей. -/
lemma val_zero_gp1 : (0 : ZMod (gp 1)).val = 0 := by decide

lemma val_one_gp1 : (1 : ZMod (gp 1)).val = 1 := by decide

/-- Профиль при `m = 1` в явном виде. -/
lemma Ztup_one_eq (ĝ : ℤ → ℂ) (ν : ZMod (gp 1)) :
    Ztup 1 ĝ ν = ∑' k : ℤ, ĝ k * e (-(ν.val : ℝ) * (k : ℝ) ^ 2 / 2) := by
  unfold Ztup
  have key : (∑' n : Fin 1 → ℤ, phiFun 1 ĝ n * phaseTup 1 ν n)
      = ∑' k : ℤ, phiFun 1 ĝ (fun _ => k) * phaseTup 1 ν (fun _ => k) := by
    exact (Equiv.tsum_eq
      { toFun := fun k _ => k
        invFun := fun n => n 0
        left_inv := fun _ => rfl
        right_inv := fun n => funext fun i => congrArg n (Subsingleton.elim (0 : Fin 1) i) }
      (fun n : Fin 1 → ℤ => phiFun 1 ĝ n * phaseTup 1 ν n)).symm
  rw [key]
  apply tsum_congr
  intro k
  have hphi : phiFun 1 ĝ (fun _ => k) = ĝ k := by rw [phiFun_one]
  have hph : phaseTup 1 ν (fun _ => k) = e (-(ν.val : ℝ) * (k : ℝ) ^ 2 / 2) := by
    have hgp1R : ((gp 1 : ℕ) : ℝ) = 2 := by rw [gp_one]; norm_num
    have hNk : NmZ 1 (fun _ => k) = (k : ℤ) ^ 2 := by simpa using NmZ_one (fun _ => k)
    unfold phaseTup
    rw [yp_one, hNk, hgp1R]
    congr 1
    push_cast
    ring
  rw [hphi, hph]

/-- Профиль при `ν = 0`: обычная сумма `∑' ĝ`. -/
lemma Ztup_one_zero (ĝ : ℤ → ℂ) : Ztup 1 ĝ 0 = ∑' k : ℤ, ĝ k := by
  rw [Ztup_one_eq]
  apply tsum_congr
  intro k
  rw [val_zero_gp1]
  simp [e]

/-- Профиль при `ν = 1`: знакочередующаяся сумма. -/
lemma Ztup_one_one (ĝ : ℤ → ℂ) :
    Ztup 1 ĝ 1 = ∑' k : ℤ, ĝ k * (-1 : ℂ) ^ k := by
  rw [Ztup_one_eq]
  apply tsum_congr
  intro k
  rw [val_one_gp1]
  simp only [Nat.cast_one]
  have harg : -(1 : ℝ) * (k : ℝ) ^ 2 / 2 = -(k : ℝ) ^ 2 / 2 := by ring
  rw [harg, exp_neg_sq_half]

/-- `nuAvg` при `m = 1`: среднее по двум вычетам. -/
lemma nuAvg_one_eq (ĝ : ℤ → ℂ) :
    nuAvg (Btup 1 ĝ) = (Btup 1 ĝ 0 + Btup 1 ĝ 1) / 2 := by
  unfold nuAvg
  have hgp1R : ((gp 1 : ℕ) : ℝ) = 2 := by rw [gp_one]; norm_num
  have hsum : (∑ ν : ZMod (gp 1), Btup 1 ĝ ν) = Btup 1 ĝ 0 + Btup 1 ĝ 1 := by
    have huniv : (Finset.univ : Finset (ZMod (gp 1))) = {0, 1} := by
      ext ν
      simp only [Finset.mem_univ, Finset.mem_insert, Finset.mem_singleton, true_iff]
      have hlt : ν.val < gp 1 := ZMod.val_lt ν
      have hν : ν = ((ν.val : ℕ) : ZMod (gp 1)) := (ZMod.natCast_zmod_val ν).symm
      have h01 : ν.val = 0 ∨ ν.val = 1 := by
        have hgp : gp 1 = 2 := gp_one
        omega
      rcases h01 with h | h
      · left
        rw [hν, h]
        simp
      · right
        rw [hν, h]
        simp
    rw [huniv, Finset.sum_insert (by decide), Finset.sum_singleton]
  rw [hsum, hgp1R]

/-! ### §4. Теорема среднего при `m = 1` с точным зазором. -/

/-- Средняя теорема 175 при `m = 1`: первый член ошибки —
`(2·s0+1)·π·s2/X` (расхождение `≈2π` с `s2·s0/X` из 175
сохраняется), второй член — ТОЧНЫЙ зазор `|B1 - B0|/2`,
а не убывающая оценка: среднее по окну равно `Btup 1 ĝ 1`,
а `nuAvg` — среднее по всем вычетам. Никакой гипотезы
`hEquidist` здесь нет — и §5 показывает, что её и не может
быть в этой форме. -/
theorem nAverageM1 (ĝ : ℤ → ℂ) (a : ∀ N : ℕ, ZMod N) (TrU : ℕ → ℂ) (X : ℝ)
    (hX1 : 1 < X)
    (hs2 : Summable fun k : ℤ => (k : ℝ) ^ 2 * ‖ĝ k‖)
    (ha : ∀ N ∈ window X (Dm 1).toNat, 2 * (a N) * (-4) = 1)
    (hTrU : ∀ N ∈ window X (Dm 1).toNat, ∀ [NeZero N],
      TrU N = ((kickMatInf N ĝ * catMat N (a N)) ^ 1).trace)
    (hW : (window X (Dm 1).toNat).Nonempty)
    (hC'le : Real.pi * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖) ≤ X) :
    |winAvg (window X (Dm 1).toNat) (fun N => ‖TrU N‖ ^ 2)
      - nuAvg (Btup 1 ĝ)|
      ≤ ((2 * (∑' k : ℤ, ‖ĝ k‖) + 1)
          * (Real.pi * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖))) / X
        + |Btup 1 ĝ 1 - Btup 1 ĝ 0| / 2 := by
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
  have hwinBtup : winAvg (window X (Dm 1).toNat) (fun N => Btup 1 ĝ (ν N))
      = Btup 1 ĝ 1 := by
    have hconst : ∀ N ∈ window X (Dm 1).toNat, Btup 1 ĝ (ν N) = Btup 1 ĝ 1 := by
      intro N hN
      rw [window_nu_eq_one hN (hν N hN)]
    have hcard : ((window X (Dm 1).toNat).card : ℝ) ≠ 0 := by
      exact_mod_cast (Finset.card_pos.mpr hW).ne'
    unfold winAvg
    rw [Finset.sum_congr rfl (fun N hN => hconst N hN), Finset.sum_const,
      nsmul_eq_mul, mul_div_cancel_left₀ _ hcard]
  have hgap : |winAvg (window X (Dm 1).toNat) (fun N => Btup 1 ĝ (ν N))
        - nuAvg (Btup 1 ĝ)|
      = |Btup 1 ĝ 1 - Btup 1 ĝ 0| / 2 := by
    rw [hwinBtup, nuAvg_one_eq]
    have hrw : Btup 1 ĝ 1 - (Btup 1 ĝ 0 + Btup 1 ĝ 1) / 2
        = (Btup 1 ĝ 1 - Btup 1 ĝ 0) / 2 := by ring
    rw [hrw, abs_div, abs_of_nonneg (show (0 : ℝ) ≤ 2 by norm_num)]
  have havg : |winAvg (window X (Dm 1).toNat) (fun N => ‖TrU N‖ ^ 2)
        - winAvg (window X (Dm 1).toNat) (fun N => Btup 1 ĝ (ν N))|
      + |winAvg (window X (Dm 1).toNat) (fun N => Btup 1 ĝ (ν N)) - nuAvg (Btup 1 ĝ)|
      ≤ ((2 * s0 + 1) * C') / X + |Btup 1 ĝ 1 - Btup 1 ĝ 0| / 2 :=
    add_le_add (le_trans havg1 havg2) (le_of_eq hgap)
  have hfin := le_trans (abs_sub_le _ _ _) havg
  rw [hC'def] at hfin
  exact hfin

/-! ### §5. `hEquidist` при `m = 1` ложна в форме моста. -/

/-- Контрпример: `ĝ₀ = 1` на `{0, 1}`, `0` иначе. -/
noncomputable def g₀ : ℤ → ℂ := fun k => if k = 0 ∨ k = 1 then 1 else 0

lemma g₀_support (k : ℤ) (hk : k ∉ ({0, 1} : Finset ℤ)) : g₀ k = 0 := by
  simp only [Finset.mem_insert, Finset.mem_singleton, not_or] at hk
  unfold g₀
  rw [if_neg (not_or.mpr hk)]

lemma sum_g₀ : ∑' k : ℤ, g₀ k = 2 := by
  rw [tsum_eq_sum g₀_support, Finset.sum_insert (by decide), Finset.sum_singleton]
  norm_num [g₀]

lemma sum_norm_g₀ : ∑' k : ℤ, ‖g₀ k‖ = 2 := by
  have heq : (fun k : ℤ => ‖g₀ k‖) = fun k => if k = 0 ∨ k = 1 then (1 : ℝ) else 0 := by
    funext k
    unfold g₀
    by_cases h : k = 0 ∨ k = 1 <;> simp [h]
  rw [heq, tsum_eq_sum (s := ({0, 1} : Finset ℤ)) (by
    intro k hk
    simp only [Finset.mem_insert, Finset.mem_singleton, not_or] at hk
    rw [if_neg (not_or.mpr hk)])]
  rw [Finset.sum_insert (by decide), Finset.sum_singleton]
  norm_num

lemma sum_alt_g₀ : ∑' k : ℤ, g₀ k * (-1 : ℂ) ^ k = 0 := by
  rw [tsum_eq_sum (s := ({0, 1} : Finset ℤ)) (by
    intro k hk
    rw [g₀_support k hk, zero_mul])]
  rw [Finset.sum_insert (by decide), Finset.sum_singleton]
  simp [g₀]

lemma Btup_g₀_zero : Btup 1 g₀ 0 = 4 := by
  unfold Btup
  rw [Ztup_one_zero, sum_g₀]
  norm_num

lemma Btup_g₀_one : Btup 1 g₀ 1 = 0 := by
  unfold Btup
  rw [Ztup_one_one, sum_alt_g₀]
  simp

lemma nuAvg_g₀ : nuAvg (Btup 1 g₀) = 2 := by
  rw [nuAvg_one_eq, Btup_g₀_zero, Btup_g₀_one]
  norm_num

/-- `5` лежит в окне при `X = 4` (окно `(4, 8]`, `gcd(N, 4) = 1`). -/
lemma window_four_mem : (5 : ℕ) ∈ window (4 : ℝ) (Dm 1).toNat := by
  rw [dm_one]
  unfold window
  rw [Finset.mem_filter, Finset.mem_Ioc]
  have h4 : ⌊(4 : ℝ)⌋₊ = 4 := Nat.floor_natCast 4
  have h8 : ⌊2 * (4 : ℝ)⌋₊ = 8 := by
    rw [show (2 : ℝ) * (4 : ℝ) = (8 : ℝ) by norm_num]
    exact Nat.floor_natCast 8
  rw [h4, h8]
  exact ⟨⟨by norm_num, by norm_num⟩, by decide⟩

/-- Гипотеза `hEquidist` моста при `m = 1` (для всех `X, D, Deff`
и всех обратных вычетов) ЛОЖНА: при `X = 4`, `D = Deff = 1`,
`ν ≡ 1` левая часть равна `2`, а правая — `1/4`. -/
theorem hEquidist_one_false :
    ¬ ∀ (X D Deff : ℝ), 0 ≤ D → 0 ≤ Deff → (window X (Dm 1).toNat).Nonempty →
      ∀ ν : ℕ → ZMod (gp 1),
        (∀ N ∈ window X (Dm 1).toNat, ν N * (N : ZMod (gp 1)) = 1) →
        |winAvg (window X (Dm 1).toNat) (fun N => Btup 1 g₀ (ν N))
          - nuAvg (Btup 1 g₀)|
          ≤ D * min ((∑' k : ℤ, ‖g₀ k‖) ^ (2 * 1)) Deff / X := by
  intro h
  have hW : (window (4 : ℝ) (Dm 1).toNat).Nonempty := ⟨5, window_four_mem⟩
  have hνinv : ∀ N ∈ window (4 : ℝ) (Dm 1).toNat,
      (fun _ => (1 : ZMod (gp 1))) N * (N : ZMod (gp 1)) = 1 := by
    intro N hN
    show (1 : ZMod (gp 1)) * (N : ZMod (gp 1)) = 1
    rw [one_mul]
    exact window_cast_eq_one hN
  have hbound := h 4 1 1 zero_le_one zero_le_one hW (fun _ => 1) hνinv
  have hwin : winAvg (window (4 : ℝ) (Dm 1).toNat)
      (fun N => Btup 1 g₀ ((fun _ => (1 : ZMod (gp 1))) N)) = 0 := by
    unfold winAvg
    rw [Finset.sum_eq_zero (fun N _ => by simp [Btup_g₀_one]), zero_div]
  rw [hwin, nuAvg_g₀, sum_norm_g₀] at hbound
  have hmin : min ((2 : ℝ) ^ (2 * 1)) (1 : ℝ) = 1 := by
    rw [show (2 : ℝ) ^ (2 * 1) = 4 by norm_num]
    exact min_eq_right (by norm_num)
  rw [hmin] at hbound
  norm_num at hbound

/- Axiom audit for all main theorems of this module. -/
#print axioms Bgs.LineB.NAverageM1.tsum_with_inv_one
#print axioms Bgs.LineB.NAverageM1.henceTup_one
#print axioms Bgs.LineB.NAverageM1.traceHenceTup_one
#print axioms Bgs.LineB.NAverageM1.window_cast_eq_one
#print axioms Bgs.LineB.NAverageM1.window_nu_eq_one
#print axioms Bgs.LineB.NAverageM1.NmZ_one
#print axioms Bgs.LineB.NAverageM1.phiFun_one
#print axioms Bgs.LineB.NAverageM1.neg_one_zpow_of_modEq_two
#print axioms Bgs.LineB.NAverageM1.exp_neg_sq_half
#print axioms Bgs.LineB.NAverageM1.Ztup_one_eq
#print axioms Bgs.LineB.NAverageM1.Ztup_one_zero
#print axioms Bgs.LineB.NAverageM1.Ztup_one_one
#print axioms Bgs.LineB.NAverageM1.nuAvg_one_eq
#print axioms Bgs.LineB.NAverageM1.nAverageM1
#print axioms Bgs.LineB.NAverageM1.hEquidist_one_false

end Bgs.LineB.NAverageM1
