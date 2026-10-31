/-
# BGS-TRACE-157: коэффициент c₁ — Gamma-диагональ и нечётность по вычету

База: current main HEAD `347f1730…` (PR #56), запись `BGS-TRACE-157`,
`state: proved`, `formalization: []`, зависимости `[150, 151]`.
Источник: `mathematics/fixed-map/band_limited_kick_bridge.md`.

Граница дословно по содержанию:
`c₁ = (2/π) Im Σ φhat(ξ) conj φhat(ξ') E[G(ξ) conj G(ξ')] β(ξ)`,
`β = iηh₀ Σ v''(ξᵢ) − η² v'ᵀ H⁻¹ v'`.
(a) Пары `ξ' ∈ Γξ` дают нулевой вклад (оба ансамбля).
(e) `c₁(−N mod g'ₘ) = −c₁(N mod g'ₘ)`, откуда `c₁` в среднем по вычетам
равен 0 и не может равняться `−2m²` равномерно по `N`; для отдельных
вычетов и некоторых `η` значение `c₁ = −2m²` не исключено.

Что здесь доказано, а что — гипотеза (без выдуманных определений):

* Суммовая сторона (a): разложение суммы по парам на диагональную
  и внедиагональную части — конечное разбиение по фильтру;
  обращение диагональной части в нуль — из спаривания:
  инволюция без неподвижных точек (или с нулевыми значениями
  в неподвижных точках), меняющая знак слагаемого. Само существование
  такой инволюции для Gamma-пар — аналитический вход (территория
  151-full: действие Γ на `Fix_m`, веса `φhat`, среднее `E[G conj G']`),
  поэтому оно входит как гипотеза `hdiag`, а не теорема.
  Внутренняя структура слагаемого (`φhat`, вес `w = E[G conj G']`,
  `β`) зафиксирована как язык, а не выведена: `c1Term`.
* Производная сторона (e): чётность `Psi` (149: `Psi` чётна по
  `V → −V`) даёт нечётность производной; вместе с гипотезой
  коллапса-отрицания (`t*` при противоположных вычетах
  противоположны mod 1 — территория 151-full, как и `hcollapse`
  в модуле 150) это даёт `c₁(−N) = −c₁(N)`, среднее 0 по вычетам
  и невозможность равномерного значения `−2m²`.
* Мост между сторонами: равенство β-суммы и `Psi'(t*)/D` —
  аналитическое содержание самой 157 (совместно с 150); оно входит
  как гипотеза `hformula`, и все свойства (e) переносятся на
  суммовой коэффициент только условно на ней.
* НЕ формализовано и не claimed: «для отдельных вычетов и некоторых
  `η` значение `c₁ = −2m²` не исключено» — это отсутствие исключения,
  а не теорема; числовые проверки (`Γ`-диагональ `≤ 1e-12`,
  сумма по вычетам `0` с точностью `1e-11`) — данные verifier'ов
  `c1_tables.py` / `c1_validate.py`, в Lean не воспроизводятся.
  BGS-TRACE-005, BGS-BGS-001 и статистика собственных значений
  beyond второго момента — вне границы, как и в 150.

No sorry, no axiom, no native_decide, no decide.
-/

import Mathlib.Analysis.Calculus.Deriv.Basic
import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Analysis.Calculus.Deriv.Comp
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Ring.Periodic
import Mathlib.Data.Complex.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum.Basic

namespace Bgs.LineD.Coeff

/-! ### Суммовая сторона: разложение и обращение диагонали (a) -/

/-- Слагаемое β-суммы из границы 157: `φhat(ξ) · conj φhat(ξ') · w · β(ξ)`,
где `w` — абстрактное значение среднего `E[G(ξ) conj G(ξ')]`
(его аналитическое содержание — территория 151-full).
Индекс `i` пробегает пары `(ξ, ξ')`; `φhat'` — значение на `ξ'`. -/
noncomputable def c1Term (φhat φhat' w beta : ι → ℂ) (i : ι) : ℂ :=
  φhat i * star (φhat' i) * w i * beta i

/-- Коэффициент `c₁` как `(2/π) Im` суммы слагаемых. -/
noncomputable def c1Sum (φhat φhat' w beta : ι → ℂ) (s : Finset ι) : ℝ :=
  (2 / Real.pi) * (∑ i ∈ s, c1Term φhat φhat' w beta i).im

/-- Разложение суммы по парам на диагональную и внедиагональную части. -/
theorem sum_split {ι : Type*} [DecidableEq ι] (s : Finset ι)
    (diag : ι → Prop) [DecidablePred diag] [∀ i, Decidable (¬ diag i)]
    (f : ι → ℂ) :
    ∑ i ∈ s, f i
      = (∑ i ∈ s.filter diag, f i) + (∑ i ∈ s.filter (fun i => ¬ diag i), f i) :=
  (Finset.sum_filter_add_sum_filter_not s diag f).symm

/-- Механизм (a): диагональная сумма обращается в нуль при спаривании.
`σ` — инволюция на диагональном множестве, меняющая знак слагаемого;
в неподвижных точках слагаемое обязано быть нулём. Существование
такой `σ` для Gamma-пар — гипотеза (см. шапку), а не теорема. -/
theorem diag_sum_eq_zero {ι : Type*} [DecidableEq ι] (s : Finset ι)
    (diag : ι → Prop) [DecidablePred diag] [∀ i, Decidable (¬ diag i)]
    (f : ι → ℂ) (σ : ι → ι)
    (hmem : ∀ i ∈ s.filter diag, σ i ∈ s.filter diag)
    (hsign : ∀ i ∈ s.filter diag, f (σ i) = -f i)
    (hfixed : ∀ i ∈ s.filter diag, f i ≠ 0 → σ i ≠ i)
    (hinv : ∀ i ∈ s.filter diag, σ (σ i) = i) :
    ∑ i ∈ s.filter diag, f i = 0 := by
  refine Finset.sum_involution (fun i _ => σ i) ?_ ?_ ?_ ?_
  · intro i hi
    rw [hsign i hi]
    exact add_neg_cancel _
  · intro i hi
    exact hfixed i hi
  · exact hmem
  · exact hinv

/-- Итог (a) для коэффициента: при нулевой диагонали `c₁` равен
`(2/π) Im` внедиагональной суммы. -/
theorem c1Sum_eq_offDiag {ι : Type*} [DecidableEq ι] (s : Finset ι)
    (diag : ι → Prop) [DecidablePred diag] [∀ i, Decidable (¬ diag i)]
    (φhat φhat' w beta : ι → ℂ)
    (hdiag : ∑ i ∈ s.filter diag, c1Term φhat φhat' w beta i = 0) :
    c1Sum φhat φhat' w beta s
      = (2 / Real.pi)
        * (∑ i ∈ s.filter (fun i => ¬ diag i), c1Term φhat φhat' w beta i).im := by
  unfold c1Sum
  rw [sum_split s diag (c1Term φhat φhat' w beta), hdiag, zero_add]

/-! ### Производная сторона: чётность Psi ⇒ нечётность c₁ (e) -/

/-- Производная периодической функции инвариантна относительно
сдвига на период: доказано напрямую через `HasDerivAt.comp`,
так как леммы `Periodic.deriv` в Mathlib 4.33.1 нет (проверено
пробником). -/
lemma deriv_add_eq_of_forall_add_eq {f : ℝ → ℝ} {c : ℝ}
    (h : ∀ y, f (y + c) = f y) (hdiff : Differentiable ℝ f) (x : ℝ) :
    deriv f (x + c) = deriv f x := by
  have h1 : HasDerivAt f (deriv f (x + c)) (x + c) := (hdiff (x + c)).hasDerivAt
  have h2 : HasDerivAt (fun y => y + c) 1 x := by
    simpa using (hasDerivAt_id x).add_const c
  have h3 : HasDerivAt (f ∘ fun y => y + c) (deriv f (x + c) * 1) x :=
    h1.comp x h2
  have h4 : (f ∘ fun y => y + c) = f := funext fun y => h y
  rw [h4, mul_one] at h3
  exact h3.deriv.symm

/-- Производная периодической функции инвариантна относительно
целочисленного сдвига (период 1). -/
lemma deriv_add_int_of_periodic {Psi : ℝ → ℝ} (hper : Function.Periodic Psi 1)
    (hdiff : Differentiable ℝ Psi) (x : ℝ) (k : ℤ) :
    deriv Psi (x + k) = deriv Psi x := by
  apply deriv_add_eq_of_forall_add_eq _ hdiff
  intro y
  have h := hper.int_mul k y
  simpa using h

/-- Производная чётной функции нечётна: `Psi'(-x) = -Psi'(x)`.
Чётность `Psi` — из 149 (`V → −V` симметрия). -/
theorem deriv_neg_of_even {f : ℝ → ℝ} (heven : ∀ x, f (-x) = f x)
    (hdiff : Differentiable ℝ f) (x : ℝ) :
    deriv f (-x) = -deriv f x := by
  have h1 : HasDerivAt f (deriv f (-x)) (-x) := (hdiff (-x)).hasDerivAt
  have h2 : HasDerivAt (fun y : ℝ => -y) (-1) x := hasDerivAt_neg x
  have h3 : HasDerivAt (f ∘ fun y => -y) (deriv f (-x) * -1) x :=
    h1.comp x h2
  have h4 : (f ∘ fun y => -y) = f := funext fun y => heven y
  rw [h4] at h3
  have h5 : deriv f x = deriv f (-x) * -1 := h3.deriv
  linarith [h5]

/-- Коэффициент `c₁` в языке 150: `Psi'(t*)/D`. -/
noncomputable def c1Of (Psi : ℝ → ℝ) (tStar : ℕ → ℝ) (D : ℝ) (N : ℕ) : ℝ :=
  deriv Psi (tStar N) / D

/-- Нечётность `c₁` по вычету (e): при противоположных вычетах
(`N₁ + N₂ ≡ 0 mod g'`) значения `c₁` противоположны.
Гипотеза `hcollapseNeg` — коллапс-отрицание: противоположные
вычеты дают противоположные `t*` mod 1 (территория 151-full,
как `hcollapse` в модуле 150). -/
theorem c1_odd {Psi : ℝ → ℝ} {tStar : ℕ → ℝ} {D : ℝ} {g' : ℕ}
    (hper : Function.Periodic Psi 1) (heven : ∀ x, Psi (-x) = Psi x)
    (hdiff : Differentiable ℝ Psi)
    (hcollapseNeg : ∀ N₁ N₂ : ℕ, (N₁ + N₂) % g' = 0 →
      ∃ k : ℤ, tStar N₁ + tStar N₂ = (k : ℝ))
    {N₁ N₂ : ℕ} (h : (N₁ + N₂) % g' = 0) :
    c1Of Psi tStar D N₁ = -c1Of Psi tStar D N₂ := by
  obtain ⟨k, hk⟩ := hcollapseNeg N₁ N₂ h
  have hderiv : deriv Psi (tStar N₁) = -deriv Psi (tStar N₂) := by
    have h1 : tStar N₁ = -tStar N₂ + (k : ℝ) := by linarith [hk]
    rw [h1, deriv_add_int_of_periodic hper hdiff _ k,
      deriv_neg_of_even heven hdiff]
  unfold c1Of
  rw [hderiv]
  exact neg_div D _

/-! ### Среднее по вычетам и невозможность равномерного значения -/

/-- Вспомогательное: отражение вычета `r ↦ (g' − r) % g'` — инволюция
на `range g'`. -/
lemma neg_mod_inv {g' r : ℕ} (hr : r < g') :
    (g' - (g' - r) % g') % g' = r := by
  by_cases hr0 : r = 0
  · subst hr0
    simp [Nat.mod_self]
  · have h1 : g' - r < g' := by omega
    have h2 : (g' - r) % g' = g' - r := Nat.mod_eq_of_lt h1
    have h3 : g' - (g' - r) = r := by omega
    rw [h2, h3, Nat.mod_eq_of_lt hr]

/-- Сумма нечётной относительно отражения функции по вычетам равна 0
(спаривание `r ↔ (g' − r) % g'`, `Finset.sum_involution`). -/
theorem sum_range_eq_zero_of_neg {g' : ℕ} (hg' : 0 < g') (f : ℕ → ℝ)
    (hodd : ∀ r ∈ Finset.range g', f r + f ((g' - r) % g') = 0) :
    ∑ r ∈ Finset.range g', f r = 0 := by
  refine Finset.sum_involution (fun r _ => (g' - r) % g') ?_ ?_ ?_ ?_
  · intro r hr
    exact hodd r hr
  · intro r hr hne heq
    apply hne
    have h := hodd r hr
    rw [heq] at h
    have h2 : f r + f r = 0 := h
    linarith [h2]
  · intro r hr
    simp only [Finset.mem_range]
    exact Nat.mod_lt _ hg'
  · intro r hr
    simp only [Finset.mem_range] at hr
    exact neg_mod_inv hr

/-- Среднее `c₁` по вычетам равно 0 (e): сумма по всем вычетам
`mod g'` обращается в нуль. -/
theorem c1_avg_zero {Psi : ℝ → ℝ} {tStar : ℕ → ℝ} {D : ℝ} {g' : ℕ}
    (hg' : 0 < g')
    (hper : Function.Periodic Psi 1) (heven : ∀ x, Psi (-x) = Psi x)
    (hdiff : Differentiable ℝ Psi)
    (hcollapseNeg : ∀ N₁ N₂ : ℕ, (N₁ + N₂) % g' = 0 →
      ∃ k : ℤ, tStar N₁ + tStar N₂ = (k : ℝ)) :
    ∑ r ∈ Finset.range g', c1Of Psi tStar D r = 0 := by
  apply sum_range_eq_zero_of_neg hg'
  intro r hr
  simp only [Finset.mem_range] at hr
  have hmod : (r + (g' - r) % g') % g' = 0 := by
    have h1 : (g' - r) % g' ≡ (g' - r) [MOD g'] := Nat.mod_modEq _ _
    have h2 : (r + (g' - r) % g') ≡ (r + (g' - r)) [MOD g'] := h1.add_left r
    rw [Nat.add_sub_cancel' hr.le] at h2
    have h3 : g' ≡ 0 [MOD g'] := (Nat.modEq_zero_iff_dvd).mpr dvd_rfl
    have h4 := h2.trans h3
    have h5 : (r + (g' - r) % g') % g' = 0 % g' := h4
    rwa [Nat.zero_mod] at h5
  have hodd : c1Of Psi tStar D r = -c1Of Psi tStar D ((g' - r) % g') :=
    c1_odd hper heven hdiff hcollapseNeg hmod
  rw [hodd]
  exact neg_add_cancel _

/-- `c₁` не может равняться `−2m²` равномерно по всем вычетам (e):
иначе сумма по вычетам была бы `g' · (−2m²) ≠ 0`, вопреки среднему 0. -/
theorem c1_not_uniform {Psi : ℝ → ℝ} {tStar : ℕ → ℝ} {D : ℝ} {g' m : ℕ}
    (hg' : 1 ≤ g') (hm : 1 ≤ m)
    (hper : Function.Periodic Psi 1) (heven : ∀ x, Psi (-x) = Psi x)
    (hdiff : Differentiable ℝ Psi)
    (hcollapseNeg : ∀ N₁ N₂ : ℕ, (N₁ + N₂) % g' = 0 →
      ∃ k : ℤ, tStar N₁ + tStar N₂ = (k : ℝ)) :
    ¬ ∀ r ∈ Finset.range g', c1Of Psi tStar D r = -2 * (m : ℝ) ^ 2 := by
  intro hall
  have hsum : ∑ r ∈ Finset.range g', c1Of Psi tStar D r = 0 :=
    c1_avg_zero (show 0 < g' by omega) hper heven hdiff hcollapseNeg
  rw [Finset.sum_congr rfl (fun r hr => hall r hr)] at hsum
  rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul] at hsum
  have hm2 : (-2 * (m : ℝ) ^ 2) ≠ 0 := by
    intro hcon
    have hsq : (m : ℝ) ^ 2 = 0 := by linarith [hcon]
    rw [sq] at hsq
    have hm0 : (m : ℝ) = 0 := mul_self_eq_zero.mp hsq
    have hpos : (0 : ℝ) < (m : ℝ) := by exact_mod_cast hm
    linarith [hm0, hpos]
  have hg2 : (g' : ℝ) ≠ 0 := by exact_mod_cast (show g' ≠ 0 by omega)
  exact hg2 (mul_eq_zero.mp hsum |>.resolve_right hm2)

/-! ### Мост: перенос свойств (e) на суммовой коэффициент -/

/-- Если β-сумма при каждом вычете совпадает с производным
коэффициентом (аналитическое отождествление самой 157),
то нечётность, среднее 0 и неравномерность переносятся на неё. -/
theorem c1Sum_odd_of_formula {Psi : ℝ → ℝ} {tStar : ℕ → ℝ} {D : ℝ} {g' : ℕ}
    (S : ℕ → ℝ)
    (hper : Function.Periodic Psi 1) (heven : ∀ x, Psi (-x) = Psi x)
    (hdiff : Differentiable ℝ Psi)
    (hcollapseNeg : ∀ N₁ N₂ : ℕ, (N₁ + N₂) % g' = 0 →
      ∃ k : ℤ, tStar N₁ + tStar N₂ = (k : ℝ))
    (hformula : ∀ N : ℕ, S N = c1Of Psi tStar D N)
    {N₁ N₂ : ℕ} (h : (N₁ + N₂) % g' = 0) :
    S N₁ = -S N₂ := by
  rw [hformula N₁, hformula N₂]
  exact c1_odd hper heven hdiff hcollapseNeg h

theorem c1Sum_avg_zero_of_formula {Psi : ℝ → ℝ} {tStar : ℕ → ℝ} {D : ℝ} {g' : ℕ}
    (hg' : 0 < g')
    (S : ℕ → ℝ)
    (hper : Function.Periodic Psi 1) (heven : ∀ x, Psi (-x) = Psi x)
    (hdiff : Differentiable ℝ Psi)
    (hcollapseNeg : ∀ N₁ N₂ : ℕ, (N₁ + N₂) % g' = 0 →
      ∃ k : ℤ, tStar N₁ + tStar N₂ = (k : ℝ))
    (hformula : ∀ N : ℕ, S N = c1Of Psi tStar D N) :
    ∑ r ∈ Finset.range g', S r = 0 := by
  rw [Finset.sum_congr rfl (fun r _ => hformula r)]
  exact c1_avg_zero hg' hper heven hdiff hcollapseNeg

theorem c1Sum_not_uniform_of_formula {Psi : ℝ → ℝ} {tStar : ℕ → ℝ} {D : ℝ}
    {g' m : ℕ}
    (hg' : 1 ≤ g') (hm : 1 ≤ m)
    (S : ℕ → ℝ)
    (hper : Function.Periodic Psi 1) (heven : ∀ x, Psi (-x) = Psi x)
    (hdiff : Differentiable ℝ Psi)
    (hcollapseNeg : ∀ N₁ N₂ : ℕ, (N₁ + N₂) % g' = 0 →
      ∃ k : ℤ, tStar N₁ + tStar N₂ = (k : ℝ))
    (hformula : ∀ N : ℕ, S N = c1Of Psi tStar D N) :
    ¬ ∀ r ∈ Finset.range g', S r = -2 * (m : ℝ) ^ 2 := by
  intro hall
  apply c1_not_uniform hg' hm hper heven hdiff hcollapseNeg
  intro r hr
  rw [← hformula r]
  exact hall r hr

#print axioms Bgs.LineD.Coeff.diag_sum_eq_zero
#print axioms Bgs.LineD.Coeff.c1Sum_eq_offDiag
#print axioms Bgs.LineD.Coeff.deriv_neg_of_even
#print axioms Bgs.LineD.Coeff.c1_odd
#print axioms Bgs.LineD.Coeff.c1_avg_zero
#print axioms Bgs.LineD.Coeff.c1_not_uniform
#print axioms Bgs.LineD.Coeff.c1Sum_odd_of_formula
#print axioms Bgs.LineD.Coeff.c1Sum_avg_zero_of_formula
#print axioms Bgs.LineD.Coeff.c1Sum_not_uniform_of_formula

end Bgs.LineD.Coeff
