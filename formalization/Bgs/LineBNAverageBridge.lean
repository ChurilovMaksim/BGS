/-
  Bgs/LineBNAverageBridge.lean — мост 175 к tsum-форме 163.

  В репозитории с 2026-10-31: формализация 175 условна
  (см. КОНСТАНТА и остаток ниже); состояние реестра не меняется.

  ЧЕСТНАЯ ФОРМУЛИРОВКА ЗАДАЧИ. Напрямую `NAverage.nAverage`
  НЕ инстанцируется, и вот три расхождения формы (а не технические
  мелочи):

  (1) Тип мод: у 175 мода — `n : ℤ` с конечным множеством `S : Finset ℤ`
  и `Phi : ℤ → ℂ`; у tsum-формы мода — кортеж `n : Fin m → ℤ`,
  сумма — по всем кортежам (`∑'`), а вес — `phiFun` (произведение
  по координатам). Конечную сумму по `ℤ` нельзя получить из `tsum`
  по кортежам без переписывания цепочки.

  (2) Фаза: у 175 фазовый множитель — `exp (2πi · (Q n / N))` с ЦЕЛЫМ
  `Q n`; у tsum — `e (Qnum / Dm / N)` с РАЦИОНАЛЬНЫМ `Qnum / Dm`.
  Целое `Q` не совпадает с `Qnum / Dm` (делимость `Dm ∣ Qnum`
  неверна в общем случае), так что `hSum` из 175 нельзя подставить
  буквально: цепочка переигрывается с рациональной фазой.

  (3) След `TrM`: у 175 `TrM : ℂ` — фиксированный параметр; в tsum
  `TrM_N = Tr (catMat N a ^ m)` зависит от `N` (но `‖TrM_N‖ = 1`
  при всех `N`, поэтому профиль `B` корректно определяется без `TrM`:
  `Btup ν = ‖Ztup ν‖ ^ 2`).

  ЧТО ДЕЛАЕТ ЭТОТ МОДУЛЬ. Он переигрывает цепочку 175 на кортежах
  с рациональной фазой, переиспользуя без изменений только
  модо-независимые леммы `NAverage` (окно, средние, `window_pow_le`,
  вторая компонента `window_error_decay`):

  * §0: положительность `pellX`, `gp m > 0`, `gp m ∣ (Dm m).toNat`
    (откуда фазовый мост вообще возможен: вычет `b % gp` корректно
    сводится по модулю `gp`, а обратный к `N` mod `Dm` даёт обратный
    mod `gp`).
  * §1: фазовый мост. `phaseTup` — это фаза 175 для кортежей
    (`exp (2πi · (−ν.val · yp · NmZ / gp))`); лемма
    `phase0Fun_eq_phaseTup` отождествляет её с нулевой фазой tsum
    при `ν = (b % gp : ZMod gp)`; лемма `nu_mul` даёт
    `ν * N = 1` в `ZMod gp` из `(N * b : ZMod Dm) = 1`.
  * §2: `tsum_with_inv` — переигровка §6–§7 tsum с ЗАРАНЕЕ выбранным
    обратным `b₀` (через `exists_inv_mod` + `trace_formula_kick_b`
    + `trace_tendsto` + `mode_sum_tendsto` для тождества и
    вычисление §7 для оценки): тождество, норма `1` и оценка (c)
    для одного и того же `b₀` со свойством обратного. Это нужно,
    потому что `trace_formula_tsum_error` возвращает `∃ b` БЕЗ
    свойства обратного, а фазовый мост требует именно его.
  * §3: кортежный профиль `Ztup`, его оценка `‖Ztup ν‖ ≤ s0 ^ m`
    (через `tsum_mode_prod_value` — это закрытие `hZ`!) и
    hence-форма `henceTup` (след = `TrM * (Ztup ν + R)`,
    `‖R‖ ≤ π·m·s2·s0^{m−1}/N` — это закрытие `hPhase` через (c)).
  * §4: поточечная оценка `pointwiseTup` (переигровка
    `pointwise_bound` с константой `C' = π·m·s2·s0^{m−1}`).
  * §5: главная теорема `nAverageTup` (переигровка `nAverage`)
    и следствие о затухании `nAverageTup_decay` (через
    `window_pow_le` и вторую компоненту `window_error_decay`).

  КОНСТАНТА: первый член ошибки моста —
  `(2·s0^m+1)·π·m·s2·s0^{m−1}/X`, а не `m·s2·s0^{2m−1}/X` из 175.
  Отношение — `π·(2 + s0^{-m}) ≈ 2π`. Граница 175 заявлена
  с `O`-нотацией, так что `O`-содержание закрыто, но ТОЧНОЕ
  неравенство `LineBNAverage` НЕ воспроизведено: для него нужна
  более острая фазовая оценка, чем (c). Это зафиксировано, а не
  заметено под ковёр.

  ЧТО ОСТАЁТСЯ ДЛЯ 175-full (честно, не доказано здесь):

  * `hEquidist` — равнораспределение вычетов `ν_N = N⁻¹ mod g'`
    при `N ∈ (X, 2X]`, `gcd(N, D_m) = 1`, против равномерного
    среднего, с ошибкой `D·min(s0^{2m}, Deff)/X`. Это аналитическое
    сердце: дискрепансия обратного отображения `N ↦ N⁻¹ mod g'`
    на интервале, оценка типа Вейля; член `min` — потому что
    дискрепансию можно оценивать либо тривиально через полную
    массу `s0^{2m}`, либо через эффективное число носителя `Deff`.
    Перестановкой сумм это не получается.
  * Случай `m = 1` (мост Гаусса требует `m ≥ 2`).
  * Аналитическая идентификация `kickMatInf` с реальным квантовым
    киком (входная установка, как у Expand/Tsum).
  * Технические гипотезы: непустота окна, `C' ≤ X` (окно достаточно
    велико), `D, Deff ≥ 0`.

  ЗАКРЫТО ЭТИМ МОСТОМ (в кортежной формулировке): `hTrace`
  (tsum-форма + фазовый мост), `hPhase` (через (c)), `hZ`
  (через тождество для произведения), тождества `s0`/`s2`
  (по определению — это tsum-суммы), `_hNu` (`ν` определён как
  обратный, свойство доказано).
-/

import Bgs.LineBNAverage
import Bgs.LineBTsum

open Filter
open Bgs.LineB.TraceFormula Bgs.LineB.Gauss Bgs.LineB.Expand Bgs.LineB.Derand

namespace Bgs.LineB.NAverageBridge

/-! ### §0. Pell facts: `gp` is positive and divides `Dm`. -/

/-- Joint positivity: `pellX` is positive, `pellY` nonnegative. -/
lemma pellX_pos_pellY_nonneg : ∀ n : ℕ, 0 < pellX n ∧ 0 ≤ pellY n := by
  intro n
  induction n with
  | zero =>
    constructor
    · show 0 < (1 : ℤ)
      norm_num
    · show (0 : ℤ) ≤ 0
      norm_num
  | succ n ih =>
    obtain ⟨hx, hy⟩ := ih
    constructor
    · show 0 < 3 * pellX n + 8 * pellY n
      linarith
    · show 0 ≤ pellX n + 3 * pellY n
      linarith

/-- `pellX` is strictly increasing. -/
lemma pellX_strictMono : StrictMono pellX := by
  apply strictMono_nat_of_lt_succ
  intro n
  have h := pellX_pos_pellY_nonneg n
  show pellX n < 3 * pellX n + 8 * pellY n
  linarith

/-- `pellX 1 = 3` (used for the `m ≥ 1` lower bound). -/
lemma pellX_one : pellX 1 = 3 := by
  show 3 * pellX 0 + 8 * pellY 0 = 3
  show (3 : ℤ) * 1 + 8 * 0 = 3
  norm_num

/-- For `m ≥ 1`, `pellX m ≥ 3`, hence `pellX m - 1 > 0`. -/
lemma pellX_sub_one_pos {m : ℕ} (hm : 1 ≤ m) : 0 < pellX m - 1 := by
  have h3 : 3 ≤ pellX m := by
    have hmono := pellX_strictMono.monotone hm
    rw [pellX_one] at hmono
    exact hmono
  omega

/-- `gp m > 0` for `m ≥ 1`: `gp` is a positive quotient. -/
lemma gp_pos {m : ℕ} (hm : 1 ≤ m) : 0 < gp m := by
  have hX : 0 < (pellX m - 1).toNat := by
    have h := pellX_sub_one_pos hm
    omega
  show 0 < (pellX m - 1).toNat / Nat.gcd (pellX m - 1).toNat (pellY m).toNat
  exact Nat.div_pos (Nat.le_of_dvd hX (Nat.gcd_dvd_left _ _))
    (Nat.gcd_pos_of_pos_left _ hX)

/-- `gp m ∣ (Dm m).toNat`: `gp` divides `pellX - 1`, hence `Dm = 2(pellX-1)`. -/
lemma gp_dvd_Dm {m : ℕ} (hm : 1 ≤ m) : gp m ∣ (Dm m).toNat := by
  have hX : 0 ≤ pellX m - 1 := le_of_lt (pellX_sub_one_pos hm)
  have hDm : (Dm m).toNat = 2 * (pellX m - 1).toNat := by
    have h1 : Dm m = ((2 * (pellX m - 1).toNat : ℕ) : ℤ) := by
      show 2 * (pellX m - 1) = ((2 * (pellX m - 1).toNat : ℕ) : ℤ)
      push_cast
      rw [Int.toNat_of_nonneg hX]
    rw [h1, Int.toNat_natCast]
  have hdiv : gp m * Nat.gcd (pellX m - 1).toNat (pellY m).toNat
      = (pellX m - 1).toNat :=
    Nat.div_mul_cancel (Nat.gcd_dvd_left _ _)
  have hgp_dvd : gp m ∣ (pellX m - 1).toNat := ⟨Nat.gcd _ _, hdiv.symm⟩
  rw [hDm]
  exact hgp_dvd.mul_left 2

/-! ### §1. The phase bridge: tsum zero-phase = 175-phase at `ν = b % gp`. -/

/-- The 175-phase for tuple modes: `exp (2πi · (−ν.val · yp · NmZ / gp))`,
    i.e. `NAverage.phase` with `Nm := NmZ m`, `yp := yp m`, `n : Fin m → ℤ`. -/
noncomputable def phaseTup (m : ℕ) [NeZero m] (ν : ZMod (gp m)) (n : Fin m → ℤ) : ℂ :=
  e (((-(ν.val : ℝ)) * (yp m : ℝ) * (NmZ m n : ℝ)) / (gp m : ℝ))

/-- The tuple phase has norm `1` (it is `e` of a real number). -/
lemma phaseTup_norm_one (m : ℕ) [NeZero m] (ν : ZMod (gp m)) (n : Fin m → ℤ) :
    ‖phaseTup m ν n‖ = 1 := by
  unfold phaseTup
  exact e_norm_one _

/-- The tsum zero-phase at `b` is the 175-phase at `ν = (b % gp : ZMod gp)`.
    This is the phase bridge: the only way `b` enters `phase0Fun` is via `b % gp`. -/
lemma phase0Fun_eq_phaseTup (m N : ℕ) [NeZero m] (b : ℕ) (n : Fin m → ℤ)
    (hgp : 0 < gp m) :
    Tsum.phase0Fun m N b n = phaseTup m (((b % gp m : ℕ) : ZMod (gp m))) n := by
  haveI : NeZero (gp m) := ⟨hgp.ne'⟩
  have hval : (((b % gp m : ℕ) : ZMod (gp m))).val = b % gp m := by
    rw [ZMod.val_natCast]
    exact Nat.mod_eq_of_lt (Nat.mod_lt _ hgp)
  unfold Tsum.phase0Fun phaseTup e
  rw [hval]
  congr 1

/-- If `b` inverts `N` mod `Dm`, then `ν = (b % gp : ZMod gp)` inverts `N` mod `gp`.
    This uses `gp ∣ Dm`: reduction mod `gp` of an inverse mod `Dm` is the inverse mod `gp`. -/
lemma nu_mul (m N b : ℕ) [NeZero m] (hgp : 0 < gp m)
    (hdvd : gp m ∣ (Dm m).toNat)
    (hb : ((N * b : ℕ) : ZMod (Dm m).toNat) = 1) :
    (((b % gp m : ℕ) : ZMod (gp m))) * (N : ZMod (gp m)) = 1 := by
  haveI : NeZero (gp m) := ⟨hgp.ne'⟩
  have h1 : ((b % gp m : ℕ) : ZMod (gp m)) = (b : ZMod (gp m)) :=
    ZMod.natCast_mod b (gp m)
  rw [h1, ← Nat.cast_mul]
  have hmod : N * b ≡ 1 [MOD (Dm m).toNat] := by
    rw [← ZMod.natCast_eq_natCast_iff]
    simpa using hb
  have hmod' : N * b ≡ 1 [MOD gp m] := hmod.of_dvd hdvd
  rw [mul_comm] at hmod'
  simpa using (ZMod.natCast_eq_natCast_iff _ _ _).mpr hmod'

/-- Two inverses of `N` mod `Dm` agree mod `gp`: the phase residue `b % gp`
    depends only on `N`, not on the chosen inverse. -/
lemma phase_congr (m N b₁ b₂ : ℕ) [NeZero m]
    (hdvd : gp m ∣ (Dm m).toNat) (hcop : (Dm m).toNat.Coprime N)
    (h1 : ((N * b₁ : ℕ) : ZMod (Dm m).toNat) = 1)
    (h2 : ((N * b₂ : ℕ) : ZMod (Dm m).toNat) = 1) :
    b₁ % gp m = b₂ % gp m := by
  have hcopg : Nat.Coprime N (gp m) := hcop.symm.coprime_dvd_right hdvd
  have e1 : N * b₁ ≡ 1 [MOD (Dm m).toNat] := by
    rw [← ZMod.natCast_eq_natCast_iff]
    simpa using h1
  have e2 : N * b₂ ≡ 1 [MOD (Dm m).toNat] := by
    rw [← ZMod.natCast_eq_natCast_iff]
    simpa using h2
  have e1' : N * b₁ ≡ 1 [MOD gp m] := e1.of_dvd hdvd
  have e2' : N * b₂ ≡ 1 [MOD gp m] := e2.of_dvd hdvd
  have e : N * b₁ ≡ N * b₂ [MOD gp m] := e1'.trans e2'.symm
  have e3 : b₁ ≡ b₂ [MOD gp m] := e.cancel_left_of_coprime hcopg.symm
  exact e3

/-! ### §2. The tsum formula + error bound for a CHOSEN inverse `b₀`.

    `trace_formula_tsum_error` returns `∃ b` without the inverse property,
    so it cannot feed the phase bridge. We replay its §6–§7 with a `b₀`
    chosen first via `exists_inv_mod`. -/

lemma tsum_with_inv (m N : ℕ) [NeZero m] [NeZero N] (ĝ : ℤ → ℂ)
    (a : ZMod N) (hm : 2 ≤ m) (hcop : (Dm m).toNat.Coprime N) (hN : 2 ≤ N)
    (ht0 : 2 * a * (-4) = 1) (hs2 : Summable fun k : ℤ => (k : ℝ) ^ 2 * ‖ĝ k‖)
    (hdvd : gp m ∣ (Dm m).toNat) :
    ∃ b : ℕ, ((N * b : ℕ) : ZMod (Dm m).toNat) = 1 ∧
      ((Tsum.kickMatInf N ĝ * catMat N a) ^ m).trace
        = (catMat N a ^ m).trace
          * ∑' n : Fin m → ℤ, phiFun m ĝ n * Tsum.phaseFun m N b n ∧
      ‖(catMat N a ^ m).trace‖ = 1 ∧
      ‖((Tsum.kickMatInf N ĝ * catMat N a) ^ m).trace
        - (catMat N a ^ m).trace
          * ∑' n : Fin m → ℤ, phiFun m ĝ n * Tsum.phase0Fun m N b n‖
        ≤ Real.pi * (m : ℝ) * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖)
          * (∑' k : ℤ, ‖ĝ k‖) ^ (m - 1) / (N : ℝ) := by
  have hs0 := Tsum.summable_norm_of_summable_sq ĝ hs2
  obtain ⟨b₀, hb₀⟩ := exists_inv_mod N (Dm m).toNat (Nat.Coprime.symm hcop)
  have hS : ∀ S : Finset ℤ,
      ((kickMat N ĝ S * catMat N a) ^ m).trace
        = (catMat N a ^ m).trace
          * ∑ n ∈ modeSet m S, phiFun m ĝ n * Tsum.phaseFun m N b₀ n
        ∧ ‖(catMat N a ^ m).trace‖ = 1 :=
    fun S => Tsum.trace_formula_kick_b m N ĝ S a hm hcop hN ht0 b₀ hb₀
  have hL1 := Tsum.trace_tendsto ĝ hs0 N a m
  have hL2 := Tsum.mode_sum_tendsto ĝ hs0 m hm N b₀
  have hL2' : Tendsto (fun S : Finset ℤ => (catMat N a ^ m).trace
      * ∑ n ∈ modeSet m S, phiFun m ĝ n * Tsum.phaseFun m N b₀ n)
      atTop (nhds ((catMat N a ^ m).trace
        * ∑' n : Fin m → ℤ, phiFun m ĝ n * Tsum.phaseFun m N b₀ n)) :=
    hL2.const_mul _
  have hEq : (fun S : Finset ℤ => ((kickMat N ĝ S * catMat N a) ^ m).trace)
      = (fun S : Finset ℤ => (catMat N a ^ m).trace
        * ∑ n ∈ modeSet m S, phiFun m ĝ n * Tsum.phaseFun m N b₀ n) :=
    funext fun S => (hS S).1
  have hTr : ((Tsum.kickMatInf N ĝ * catMat N a) ^ m).trace
      = (catMat N a ^ m).trace
        * ∑' n : Fin m → ℤ, phiFun m ĝ n * Tsum.phaseFun m N b₀ n :=
    (tendsto_nhds_unique (by rw [hEq]; exact hL2') hL1).symm
  refine ⟨b₀, hb₀, hTr, (hS ∅).2, ?_⟩
  have hsumQ := Tsum.summable_mode ĝ hs0 m hm N b₀
  have hsum0 := Tsum.summable_mode0 ĝ hs0 m hm N b₀
  have hdiff : (∑' n : Fin m → ℤ, phiFun m ĝ n * Tsum.phaseFun m N b₀ n)
      - (∑' n : Fin m → ℤ, phiFun m ĝ n * Tsum.phase0Fun m N b₀ n)
      = ∑' n : Fin m → ℤ, (phiFun m ĝ n * Tsum.phaseFun m N b₀ n
        - phiFun m ĝ n * Tsum.phase0Fun m N b₀ n) :=
    (Summable.tsum_sub hsumQ hsum0).symm
  have hsum : ∀ j : Fin m, Summable fun n : Fin m → ℤ =>
      ((n j : ℝ)) ^ 2 * ∏ r : Fin m, ‖ĝ (n r)‖ := by
    intro j
    have h := Tsum.summable_mode_prod_nonneg m (by omega) (Tsum.sqFamily ĝ j)
      (fun r k => Tsum.sqFamily_nonneg ĝ j r k)
      (fun r => Tsum.sqFamily_summable ĝ j r hs0 hs2)
    have heq : (fun n : Fin m → ℤ => ∏ r : Fin m, Tsum.sqFamily ĝ j r (n r))
        = (fun n => ((n j : ℝ)) ^ 2 * ∏ r : Fin m, ‖ĝ (n r)‖) :=
      funext fun n => Tsum.sqFamily_prod ĝ j n
    rw [heq] at h
    exact h
  have hbound : Summable fun n : Fin m → ℤ =>
      (Real.pi / (N : ℝ)) * ((∏ j : Fin m, ‖ĝ (n j)‖) * (∑ j, ((n j : ℝ)) ^ 2)) := by
    apply Summable.mul_left
    rw [Tsum.prod_mul_sq_sum ĝ m]
    exact Tsum.summable_finset_sum (s := Finset.univ)
      (f := fun j (n : Fin m → ℤ) => ((n j : ℝ)) ^ 2 * ∏ r : Fin m, ‖ĝ (n r)‖)
      (fun j _ => hsum j)
  have hnormdiff : Summable fun n : Fin m → ℤ =>
      ‖phiFun m ĝ n * Tsum.phaseFun m N b₀ n
        - phiFun m ĝ n * Tsum.phase0Fun m N b₀ n‖ := by
    refine Summable.of_nonneg_of_le (fun n => norm_nonneg _)
      (fun n => Tsum.diff_term_bound m N (by omega) hN ĝ b₀ n) hbound
  rw [hTr, ← mul_sub, hdiff, norm_mul, (hS ∅).2, one_mul]
  calc ‖∑' n : Fin m → ℤ, (phiFun m ĝ n * Tsum.phaseFun m N b₀ n
        - phiFun m ĝ n * Tsum.phase0Fun m N b₀ n)‖
      ≤ ∑' n : Fin m → ℤ, ‖phiFun m ĝ n * Tsum.phaseFun m N b₀ n
        - phiFun m ĝ n * Tsum.phase0Fun m N b₀ n‖ :=
        norm_tsum_le_tsum_norm hnormdiff
    _ ≤ ∑' n : Fin m → ℤ, (Real.pi / (N : ℝ))
        * ((∏ j : Fin m, ‖ĝ (n j)‖) * (∑ j, ((n j : ℝ)) ^ 2)) :=
        Summable.tsum_le_tsum (fun n => Tsum.diff_term_bound m N (by omega) hN ĝ b₀ n)
          hnormdiff hbound
    _ = (Real.pi / (N : ℝ)) * ((m : ℝ) * ((∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖)
        * (∑' k : ℤ, ‖ĝ k‖) ^ (m - 1))) := by
        rw [tsum_mul_left, Tsum.weighted_mode_tsum m hm ĝ hs0 hs2]
    _ = Real.pi * (m : ℝ) * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖)
        * (∑' k : ℤ, ‖ĝ k‖) ^ (m - 1) / (N : ℝ) := by
        rw [div_mul_eq_mul_div]
        ring

/-! ### §3. The tuple profile, its `ℓ¹` bound, and the hence form. -/

/-- The ν-profile for tuple modes: `Ztup ν = ∑' n, phiFun n * phaseTup ν n`.
    This is `NAverage.Zfun` with `S` replaced by all of `Fin m → ℤ`,
    `Phi := phiFun`, `Nm := NmZ m`, `yp := yp m`. -/
noncomputable def Ztup (m : ℕ) [NeZero m] (ĝ : ℤ → ℂ) (ν : ZMod (gp m)) : ℂ :=
  ∑' n : Fin m → ℤ, phiFun m ĝ n * phaseTup m ν n

/-- The squared profile for tuple modes: `Btup ν = ‖Ztup ν‖ ^ 2`.
    This is `NAverage.Bprof` with the `‖TrM‖ ^ 2` factor dropped,
    which is legitimate because `‖TrM_N‖ = 1` for every `N`. -/
noncomputable def Btup (m : ℕ) [NeZero m] (ĝ : ℤ → ℂ) (ν : ZMod (gp m)) : ℝ :=
  ‖Ztup m ĝ ν‖ ^ 2

/-- The `ℓ¹` bound for the tuple profile: `‖Ztup ν‖ ≤ s0 ^ m`.
    This closes `hZ` (the tsum product identity replaces the finite
    `ℓ¹` estimate). -/
lemma Ztup_norm_le (m : ℕ) [NeZero m] (ĝ : ℤ → ℂ)
    (hs0 : Summable fun k : ℤ => ‖ĝ k‖) (ν : ZMod (gp m)) :
    ‖Ztup m ĝ ν‖ ≤ (∑' k : ℤ, ‖ĝ k‖) ^ m := by
  have hnorm : ∀ n : Fin m → ℤ,
      ‖phiFun m ĝ n * phaseTup m ν n‖ = ∏ j : Fin m, ‖ĝ (n j)‖ := by
    intro n
    rw [norm_mul, phaseTup_norm_one, mul_one, Tsum.norm_phiFun]
  have hsumm : Summable fun n : Fin m → ℤ =>
      ‖phiFun m ĝ n * phaseTup m ν n‖ := by
    rw [show (fun n => ‖phiFun m ĝ n * phaseTup m ν n‖)
        = (fun n => ∏ j : Fin m, ‖ĝ (n j)‖) from funext hnorm]
    exact Tsum.mode_norm_summable ĝ hs0 m (by have h0 : m ≠ 0 := NeZero.ne m; omega)
  unfold Ztup
  calc ‖∑' n : Fin m → ℤ, phiFun m ĝ n * phaseTup m ν n‖
      ≤ ∑' n : Fin m → ℤ, ‖phiFun m ĝ n * phaseTup m ν n‖ :=
        norm_tsum_le_tsum_norm hsumm
    _ = ∑' n : Fin m → ℤ, ∏ j : Fin m, ‖ĝ (n j)‖ := tsum_congr hnorm
    _ = ∏ j : Fin m, ∑' k : ℤ, ‖ĝ k‖ :=
        Tsum.tsum_mode_prod_value m (by have h0 : m ≠ 0 := NeZero.ne m; omega)
          (fun j k => ‖ĝ k‖) (fun j k => norm_nonneg _) (fun j => hs0)
    _ = (∑' k : ℤ, ‖ĝ k‖) ^ m := by
        rw [Finset.prod_const, Finset.card_univ, Fintype.card_fin]

/-- The hence form for tuple modes: the trace is `TrM * (Ztup ν + R)`
    with `ν * N = 1` in `ZMod gp` and `‖R‖ ≤ π·m·s2·s0^{m−1}/N`.
    This closes `hTrace` (in tsum form) and `hPhase` (via theorem 1(c)). -/
lemma henceTup (m N : ℕ) [NeZero m] [NeZero N] (ĝ : ℤ → ℂ)
    (a : ZMod N) (hm : 2 ≤ m) (hcop : (Dm m).toNat.Coprime N) (hN : 2 ≤ N)
    (ht0 : 2 * a * (-4) = 1) (hs2 : Summable fun k : ℤ => (k : ℝ) ^ 2 * ‖ĝ k‖)
    (hgp : 0 < gp m) (hdvd : gp m ∣ (Dm m).toNat) :
    ∃ ν : ZMod (gp m), ∃ R : ℂ,
      (ν * (N : ZMod (gp m)) = 1) ∧
      (∃ TrM : ℂ, ((Tsum.kickMatInf N ĝ * catMat N a) ^ m).trace
        = TrM * (Ztup m ĝ ν + R) ∧ ‖TrM‖ = 1 ∧
        ‖R‖ ≤ Real.pi * (m : ℝ) * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖)
          * (∑' k : ℤ, ‖ĝ k‖) ^ (m - 1) / (N : ℝ)) := by
  haveI : NeZero (gp m) := ⟨hgp.ne'⟩
  have hs0 := Tsum.summable_norm_of_summable_sq ĝ hs2
  obtain ⟨b₀, hb₀, hTr, hNorm, hErr⟩ :=
    tsum_with_inv m N ĝ a hm hcop hN ht0 hs2 hdvd
  have hsumQ := Tsum.summable_mode ĝ hs0 m hm N b₀
  have hsum0 := Tsum.summable_mode0 ĝ hs0 m hm N b₀
  have hsplit : (∑' n : Fin m → ℤ, phiFun m ĝ n * Tsum.phase0Fun m N b₀ n)
      + (∑' n : Fin m → ℤ, (phiFun m ĝ n * Tsum.phaseFun m N b₀ n
        - phiFun m ĝ n * Tsum.phase0Fun m N b₀ n))
      = ∑' n : Fin m → ℤ, phiFun m ĝ n * Tsum.phaseFun m N b₀ n := by
    rw [← Summable.tsum_add hsum0 (hsumQ.sub hsum0)]
    apply tsum_congr
    intro n
    show phiFun m ĝ n * Tsum.phase0Fun m N b₀ n
        + (phiFun m ĝ n * Tsum.phaseFun m N b₀ n
          - phiFun m ĝ n * Tsum.phase0Fun m N b₀ n)
        = phiFun m ĝ n * Tsum.phaseFun m N b₀ n
    ring
  have hZ : Ztup m ĝ (((b₀ % gp m : ℕ) : ZMod (gp m)))
      = ∑' n : Fin m → ℤ, phiFun m ĝ n * Tsum.phase0Fun m N b₀ n := by
    unfold Ztup
    apply tsum_congr
    intro n
    rw [phase0Fun_eq_phaseTup m N b₀ n hgp]
  refine ⟨((b₀ % gp m : ℕ) : ZMod (gp m)),
    ∑' n : Fin m → ℤ, (phiFun m ĝ n * Tsum.phaseFun m N b₀ n
      - phiFun m ĝ n * Tsum.phase0Fun m N b₀ n),
    nu_mul m N b₀ hgp hdvd hb₀, (catMat N a ^ m).trace, ?_, hNorm, ?_⟩
  · rw [hTr, ← hsplit, ← hZ]
  · have hRval : (catMat N a ^ m).trace
        * (∑' n : Fin m → ℤ, (phiFun m ĝ n * Tsum.phaseFun m N b₀ n
          - phiFun m ĝ n * Tsum.phase0Fun m N b₀ n))
        = ((Tsum.kickMatInf N ĝ * catMat N a) ^ m).trace
          - (catMat N a ^ m).trace
            * (∑' n : Fin m → ℤ, phiFun m ĝ n * Tsum.phase0Fun m N b₀ n) := by
      rw [hTr, ← hsplit]
      rw [mul_add, add_sub_cancel_left]
    have hnormR : ‖∑' n : Fin m → ℤ, (phiFun m ĝ n * Tsum.phaseFun m N b₀ n
        - phiFun m ĝ n * Tsum.phase0Fun m N b₀ n)‖
        = ‖((Tsum.kickMatInf N ĝ * catMat N a) ^ m).trace
          - (catMat N a ^ m).trace
            * (∑' n : Fin m → ℤ, phiFun m ĝ n * Tsum.phase0Fun m N b₀ n)‖ := by
      rw [← hRval, norm_mul, hNorm, one_mul]
    rw [hnormR]
    exact hErr

/-! ### §4. The pointwise bound for tuple modes (replay of `pointwise_bound`). -/

/-- Squared pointwise bound: `|‖TrU N‖² − Btup (ν N)| ≤ (2·s0^m+1)·C'/N`.
    The constant is `(2·s0^m+1)·C'` with `C' = π·m·s2·s0^{m−1}` from (c);
    this is where the `≈2π` constant factor vs 175's exact term comes from. -/
theorem pointwiseTup (m : ℕ) [NeZero m] [NeZero (gp m)] (ĝ : ℤ → ℂ)
    {TrU : ℕ → ℂ} {ν : ℕ → ZMod (gp m)} {R : ℕ → ℂ} {W : Finset ℕ}
    {X s0 : ℝ} {C' : ℝ}
    (hX : 0 < X) (hs0 : 0 ≤ s0) (hC'0 : 0 ≤ C') (hC'le : C' ≤ X)
    (hZ : ∀ ν : ZMod (gp m), ‖Ztup m ĝ ν‖ ≤ s0 ^ m)
    (hTrace : ∀ N ∈ W, ∃ TrM : ℂ, TrU N = TrM * (Ztup m ĝ (ν N) + R N) ∧
      ‖TrM‖ = 1 ∧ ‖R N‖ ≤ C' / (N : ℝ))
    (hW : ∀ N ∈ W, X < N) :
    ∀ N ∈ W, |‖TrU N‖ ^ 2 - Btup m ĝ (ν N)|
      ≤ ((2 * s0 ^ m + 1) * C') / (N : ℝ) := by
  intro N hN
  obtain ⟨TrM, hTr, hNorm, hR⟩ := hTrace N hN
  have hNpos : (0 : ℝ) < N := lt_trans hX (hW N hN)
  have hNne : (N : ℝ) ≠ 0 := ne_of_gt hNpos
  set z := ‖Ztup m ĝ (ν N)‖ with hz_def
  set r := ‖R N‖ with hr_def
  set w := ‖Ztup m ĝ (ν N) + R N‖ with hw_def
  have hz0 : 0 ≤ z := norm_nonneg _
  have hr0 : 0 ≤ r := norm_nonneg _
  have hw0 : 0 ≤ w := norm_nonneg _
  have hzle : z ≤ s0 ^ m := hZ _
  have hs0m : 0 ≤ s0 ^ m := pow_nonneg hs0 _
  have hRle : r ≤ C' / (N : ℝ) := hR
  have hCN : C' / (N : ℝ) ≤ 1 := by
    rw [div_le_one hNpos]
    exact le_trans hC'le (le_of_lt (hW N hN))
  have hr1 : r ≤ 1 := le_trans hRle hCN
  have hCN0 : 0 ≤ C' / (N : ℝ) := div_nonneg hC'0 (le_of_lt hNpos)
  have hw_le : w ≤ z + r := norm_add_le _ _
  have hw_ge : z - r ≤ w := by
    have h := norm_sub_norm_le (Ztup m ĝ (ν N)) (-(R N))
    rw [sub_neg_eq_add, norm_neg] at h
    exact h
  have habs : |w ^ 2 - z ^ 2| ≤ 2 * z * r + r ^ 2 := by
    rw [sq_sub_sq, abs_mul]
    have hwz : |w - z| ≤ r := by
      rw [abs_le]
      constructor <;> linarith [hw_le, hw_ge]
    have hwz2 : |w + z| ≤ 2 * z + r := by
      rw [abs_le]
      constructor
      · have : -(w + z) ≤ 0 := by linarith [hw0, hz0]
        linarith [this]
      · linarith [hw_le]
    calc |w + z| * |w - z| ≤ (2 * z + r) * r :=
          mul_le_mul hwz2 hwz (abs_nonneg _) (by linarith [hz0, hr0])
      _ = 2 * z * r + r ^ 2 := by ring
  have hnorm : ‖TrU N‖ = w := by
    rw [hTr, norm_mul, hNorm, one_mul]
  have hB : Btup m ĝ (ν N) = z ^ 2 := by
    show ‖Ztup m ĝ (ν N)‖ ^ 2 = z ^ 2
    rw [← hz_def]
  have hA : ‖TrU N‖ ^ 2 - Btup m ĝ (ν N) = w ^ 2 - z ^ 2 := by
    rw [hnorm, hB]
  rw [hA]
  calc |w ^ 2 - z ^ 2| ≤ 2 * z * r + r ^ 2 := habs
    _ ≤ 2 * s0 ^ m * (C' / (N : ℝ)) + (C' / (N : ℝ)) ^ 2 := by
        have h1 : 2 * z * r ≤ 2 * s0 ^ m * (C' / (N : ℝ)) := by
          have := mul_le_mul hzle hRle hr0 hs0m
          linarith [this]
        have h2 : r ^ 2 ≤ (C' / (N : ℝ)) ^ 2 :=
          pow_le_pow_left₀ hr0 hRle 2
        linarith [h1, h2]
    _ ≤ (2 * s0 ^ m + 1) * (C' / (N : ℝ)) := by
        have hsq : (C' / (N : ℝ)) ^ 2 ≤ C' / (N : ℝ) := by
          rw [pow_two]
          calc (C' / (N : ℝ)) * (C' / (N : ℝ)) ≤ (C' / (N : ℝ)) * 1 :=
                mul_le_mul_of_nonneg_left hCN hCN0
            _ = C' / (N : ℝ) := mul_one _
        linarith [hsq]
    _ = ((2 * s0 ^ m + 1) * C') / (N : ℝ) := by
        rw [mul_div_assoc]

/-! ### §5. The window average and the decay corollary.

    The kicked trace is taken as an ABSTRACT function `TrU` with the
    hypothesis `hTrU` that it agrees with the tsum trace on the window.
    This is forced, not a choice: the trace `((kickMatInf * catMat)^m).trace`
    needs a `Fintype (ZMod N)` instance, i.e. `NeZero N`, which cannot be
    synthesized for a bound `N` in a theorem statement. On the window
    `N ≥ 2`, so the instance exists there; stating the theorems for an
    abstract agreeing `TrU` is exactly the window content. -/

/-- The hence form over the whole window, with `ν` and `R` as functions.
    `ν N` is genuinely the inverse residue: `(ν N) * N = 1` in `ZMod gp`. -/
theorem traceHenceTup (m : ℕ) [NeZero m] (ĝ : ℤ → ℂ) (a : ∀ N : ℕ, ZMod N)
    (TrU : ℕ → ℂ) (X : ℝ) (hm : 2 ≤ m) (hX1 : 1 < X)
    (hs2 : Summable fun k : ℤ => (k : ℝ) ^ 2 * ‖ĝ k‖)
    (ha : ∀ N ∈ NAverage.window X (Dm m).toNat, 2 * (a N) * (-4) = 1)
    (hTrU : ∀ N ∈ NAverage.window X (Dm m).toNat, ∀ [NeZero N],
      TrU N = ((Tsum.kickMatInf N ĝ * catMat N (a N)) ^ m).trace) :
    ∃ ν : ℕ → ZMod (gp m), ∃ R : ℕ → ℂ,
      (∀ N ∈ NAverage.window X (Dm m).toNat, (ν N) * (N : ZMod (gp m)) = 1) ∧
      (∀ N ∈ NAverage.window X (Dm m).toNat, ∃ TrM : ℂ,
        TrU N = TrM * (Ztup m ĝ (ν N) + R N) ∧ ‖TrM‖ = 1 ∧
        ‖R N‖ ≤ Real.pi * (m : ℝ) * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖)
          * (∑' k : ℤ, ‖ĝ k‖) ^ (m - 1) / (N : ℝ)) := by
  have hgp : 0 < gp m := gp_pos (by omega)
  have hdvd : gp m ∣ (Dm m).toNat := gp_dvd_Dm (by omega)
  have hper : ∀ N : ℕ, ∃ ν₀ : ZMod (gp m), ∃ R₀ : ℂ, ∃ TrM₀ : ℂ,
      N ∈ NAverage.window X (Dm m).toNat →
      (ν₀ * (N : ZMod (gp m)) = 1) ∧
      TrU N = TrM₀ * (Ztup m ĝ ν₀ + R₀) ∧ ‖TrM₀‖ = 1 ∧
      ‖R₀‖ ≤ Real.pi * (m : ℝ) * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖)
        * (∑' k : ℤ, ‖ĝ k‖) ^ (m - 1) / (N : ℝ) := by
    intro N
    by_cases hN : N ∈ NAverage.window X (Dm m).toNat
    · have hmem := NAverage.mem_window (le_of_lt (lt_trans zero_lt_one hX1)) hN
      have hN2 : 2 ≤ N := by
        have h1 : (1 : ℝ) < (N : ℝ) := lt_trans hX1 hmem.1
        have h2 : 1 < N := by exact_mod_cast h1
        omega
      haveI : NeZero N := ⟨by omega⟩
      have hcop : (Dm m).toNat.Coprime N := hmem.2.2.symm
      obtain ⟨ν₀, R₀, hν₀, TrM₀, hTr₀, hNorm₀, hR₀⟩ :=
        henceTup m N ĝ (a N) hm hcop hN2 (ha N hN) hs2 hgp hdvd
      rw [hTrU N hN]
      exact ⟨ν₀, R₀, TrM₀, fun _ => ⟨hν₀, hTr₀, hNorm₀, hR₀⟩⟩
    · exact ⟨0, 0, 0, fun h => absurd h hN⟩
  choose ν R TrM h using hper
  exact ⟨ν, R, fun N hN => (h N hN).1,
    fun N hN => ⟨TrM N, (h N hN).2.1, (h N hN).2.2.1, (h N hN).2.2.2⟩⟩

/-- The main averaging theorem for tuple modes (replay of `nAverage`).
    The equidistribution hypothesis is stated for every inverse-residue
    sequence `ν` — this is the single sequence `ν_N = N⁻¹ mod g'`,
    since the inverse is unique on the window (`gcd(N, gp) = 1` there).
    The first error term carries the `(2·s0^m+1)·π` factor from (c);
    see the header for the constant discussion. -/
theorem nAverageTup (m : ℕ) [NeZero m] [NeZero (gp m)] (ĝ : ℤ → ℂ)
    (a : ∀ N : ℕ, ZMod N) (TrU : ℕ → ℂ) (X : ℝ) (D Deff : ℝ)
    (hm : 2 ≤ m) (hX1 : 1 < X)
    (hs2 : Summable fun k : ℤ => (k : ℝ) ^ 2 * ‖ĝ k‖)
    (ha : ∀ N ∈ NAverage.window X (Dm m).toNat, 2 * (a N) * (-4) = 1)
    (hTrU : ∀ N ∈ NAverage.window X (Dm m).toNat, ∀ [NeZero N],
      TrU N = ((Tsum.kickMatInf N ĝ * catMat N (a N)) ^ m).trace)
    (hW : (NAverage.window X (Dm m).toNat).Nonempty)
    (hC'le : Real.pi * (m : ℝ) * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖)
      * (∑' k : ℤ, ‖ĝ k‖) ^ (m - 1) ≤ X)
    (hEquidist : ∀ ν : ℕ → ZMod (gp m),
      (∀ N ∈ NAverage.window X (Dm m).toNat, (ν N) * (N : ZMod (gp m)) = 1) →
      |NAverage.winAvg (NAverage.window X (Dm m).toNat) (fun N => Btup m ĝ (ν N))
        - NAverage.nuAvg (Btup m ĝ)|
        ≤ (D : ℝ) * min ((∑' k : ℤ, ‖ĝ k‖) ^ (2 * m)) Deff / X) :
    |NAverage.winAvg (NAverage.window X (Dm m).toNat)
        (fun N => ‖TrU N‖ ^ 2) - NAverage.nuAvg (Btup m ĝ)|
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
        (fun N => Btup m ĝ (ν N)) - NAverage.nuAvg (Btup m ĝ)|
      ≤ ((2 * s0 ^ m + 1) * C') / X
        + (D : ℝ) * min (s0 ^ (2 * m)) Deff / X :=
    add_le_add (le_trans havg1 havg2) (hEquidist ν hν)
  have hfin := le_trans (abs_sub_le _ _ _) havg
  rw [hC'def] at hfin
  exact hfin

/-- Decay form: under the logarithmic window, both error terms decay
    like `X^{-ε}`. The second term is `window_error_decay` verbatim;
    the first term is the bridge constant pushed through `window_pow_le`. -/
theorem nAverageTup_decay (m : ℕ) [NeZero m] [NeZero (gp m)] (ĝ : ℤ → ℂ)
    (a : ∀ N : ℕ, ZMod N) (TrU : ℕ → ℂ) (X ε : ℝ) (D Deff : ℝ)
    (hm : 2 ≤ m) (hX1 : 1 < X) (hε0 : 0 < ε) (hε1 : ε < 1)
    (hs2 : Summable fun k : ℤ => (k : ℝ) ^ 2 * ‖ĝ k‖)
    (hs0pos : 0 < ∑' k : ℤ, ‖ĝ k‖)
    (ha : ∀ N ∈ NAverage.window X (Dm m).toNat, 2 * (a N) * (-4) = 1)
    (hTrU : ∀ N ∈ NAverage.window X (Dm m).toNat, ∀ [NeZero N],
      TrU N = ((Tsum.kickMatInf N ĝ * catMat N (a N)) ^ m).trace)
    (hW : (NAverage.window X (Dm m).toNat).Nonempty)
    (hC'le : Real.pi * (m : ℝ) * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖)
      * (∑' k : ℤ, ‖ĝ k‖) ^ (m - 1) ≤ X)
    (hD0 : 0 ≤ D) (hDeff0 : 0 ≤ Deff)
    (hWin : (m : ℝ) ≤ (1 - ε) * NAverage.cEta (∑' k : ℤ, ‖ĝ k‖) * Real.log X)
    (hEquidist : ∀ ν : ℕ → ZMod (gp m),
      (∀ N ∈ NAverage.window X (Dm m).toNat, (ν N) * (N : ZMod (gp m)) = 1) →
      |NAverage.winAvg (NAverage.window X (Dm m).toNat) (fun N => Btup m ĝ (ν N))
        - NAverage.nuAvg (Btup m ĝ)|
        ≤ (D : ℝ) * min ((∑' k : ℤ, ‖ĝ k‖) ^ (2 * m)) Deff / X) :
    |NAverage.winAvg (NAverage.window X (Dm m).toNat)
        (fun N => ‖TrU N‖ ^ 2) - NAverage.nuAvg (Btup m ĝ)|
      ≤ ((Real.pi * (2 * (∑' k : ℤ, ‖ĝ k‖) ^ m + 1) * (m : ℝ)
          * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖))
          / (∑' k : ℤ, ‖ĝ k‖) ^ (m + 1)) * X ^ (-ε)
        + D * X ^ (-ε) := by
  have hmain := nAverageTup m ĝ a TrU X D Deff hm hX1 hs2 ha hTrU hW hC'le hEquidist
  have hs0 : Summable fun k : ℤ => ‖ĝ k‖ := Tsum.summable_norm_of_summable_sq ĝ hs2
  have hs2nn : 0 ≤ ∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖ := tsum_nonneg
    (fun k => mul_nonneg (sq_nonneg _) (norm_nonneg _))
  have hpow : (∑' k : ℤ, ‖ĝ k‖) ^ (2 * m) ≤ X ^ ((1 : ℝ) - ε) :=
    NAverage.window_pow_le hX1 hε0 hε1 hs0pos hWin
  have hXpos : (0 : ℝ) < X := lt_trans zero_lt_one hX1
  have hrw : X ^ ((1 : ℝ) - ε) / X = X ^ (-ε) := by
    have h1 : X ^ ((1 : ℝ) - ε) = X * X ^ (-ε) := by
      have h2 : ((1 : ℝ) - ε) = 1 + (-ε) := by ring
      rw [h2, Real.rpow_add hXpos]
      simp
    rw [h1]
    field_simp
  have hT2 : (D : ℝ) * min ((∑' k : ℤ, ‖ĝ k‖) ^ (2 * m)) Deff / X
      ≤ D * X ^ (-ε) :=
    (NAverage.window_error_decay hX1 hε0 hε1 hs0pos hs2nn (by omega) hD0 hDeff0
      hWin).2
  have hT1 : ((2 * (∑' k : ℤ, ‖ĝ k‖) ^ m + 1)
        * (Real.pi * (m : ℝ) * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖)
          * (∑' k : ℤ, ‖ĝ k‖) ^ (m - 1))) / X
      ≤ ((Real.pi * (2 * (∑' k : ℤ, ‖ĝ k‖) ^ m + 1) * (m : ℝ)
          * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖))
          / (∑' k : ℤ, ‖ĝ k‖) ^ (m + 1)) * X ^ (-ε) := by
    have hs0pow : (0 : ℝ) < (∑' k : ℤ, ‖ĝ k‖) ^ (m + 1) :=
      pow_pos hs0pos _
    have hstep : (∑' k : ℤ, ‖ĝ k‖) ^ (m - 1)
        ≤ X ^ ((1 : ℝ) - ε) / (∑' k : ℤ, ‖ĝ k‖) ^ (m + 1) := by
      rw [le_div_iff₀ hs0pow]
      have hsplit : (∑' k : ℤ, ‖ĝ k‖) ^ (2 * m)
          = (∑' k : ℤ, ‖ĝ k‖) ^ (m - 1) * (∑' k : ℤ, ‖ĝ k‖) ^ (m + 1) := by
        rw [← pow_add]
        congr 1
        omega
      rw [← hsplit]
      exact hpow
    have hstep2 : (Real.pi * (m : ℝ) * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖))
        * (∑' k : ℤ, ‖ĝ k‖) ^ (m - 1)
        ≤ (Real.pi * (m : ℝ) * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖))
        * (X ^ ((1 : ℝ) - ε) / (∑' k : ℤ, ‖ĝ k‖) ^ (m + 1)) :=
      mul_le_mul_of_nonneg_left hstep (by
        apply mul_nonneg
        apply mul_nonneg Real.pi_nonneg (by exact_mod_cast Nat.zero_le m)
        exact hs2nn)
    calc ((2 * (∑' k : ℤ, ‖ĝ k‖) ^ m + 1)
          * (Real.pi * (m : ℝ) * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖)
            * (∑' k : ℤ, ‖ĝ k‖) ^ (m - 1))) / X
        ≤ ((2 * (∑' k : ℤ, ‖ĝ k‖) ^ m + 1)
          * (Real.pi * (m : ℝ) * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖)
            * (X ^ ((1 : ℝ) - ε) / (∑' k : ℤ, ‖ĝ k‖) ^ (m + 1)))) / X := by
          rw [div_eq_mul_inv, div_eq_mul_inv]
          apply mul_le_mul_of_nonneg_right _ (inv_nonneg.mpr (le_of_lt hXpos))
          exact mul_le_mul_of_nonneg_left hstep2
            (by linarith [pow_nonneg (le_of_lt hs0pos) m])
      _ = ((Real.pi * (2 * (∑' k : ℤ, ‖ĝ k‖) ^ m + 1) * (m : ℝ)
          * (∑' k : ℤ, (k : ℝ) ^ 2 * ‖ĝ k‖))
          / (∑' k : ℤ, ‖ĝ k‖) ^ (m + 1)) * X ^ (-ε) := by
          rw [← hrw]
          ring
  exact le_trans hmain (add_le_add hT1 hT2)

/- Axiom audit for all main theorems of this module. -/
#print axioms Bgs.LineB.NAverageBridge.pellX_pos_pellY_nonneg
#print axioms Bgs.LineB.NAverageBridge.gp_pos
#print axioms Bgs.LineB.NAverageBridge.gp_dvd_Dm
#print axioms Bgs.LineB.NAverageBridge.phaseTup_norm_one
#print axioms Bgs.LineB.NAverageBridge.phase0Fun_eq_phaseTup
#print axioms Bgs.LineB.NAverageBridge.nu_mul
#print axioms Bgs.LineB.NAverageBridge.phase_congr
#print axioms Bgs.LineB.NAverageBridge.tsum_with_inv
#print axioms Bgs.LineB.NAverageBridge.Ztup_norm_le
#print axioms Bgs.LineB.NAverageBridge.henceTup
#print axioms Bgs.LineB.NAverageBridge.pointwiseTup
#print axioms Bgs.LineB.NAverageBridge.traceHenceTup
#print axioms Bgs.LineB.NAverageBridge.nAverageTup
#print axioms Bgs.LineB.NAverageBridge.nAverageTup_decay

end Bgs.LineB.NAverageBridge
