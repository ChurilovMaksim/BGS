# Слой формализации на Mathlib

39 модулей Aristotle адаптированы к существующему проекту BGS на Lean 4.33.1 и закреплённому Mathlib. Они дополняют 29 прежних модулей. Корневой Lake-проект из старого архива не переносится. Статусы математических утверждений не повышаются.

## Где лежат исходники

Исходники находятся в `formalization/Bgs/Mathlib/`; общий импорт — `formalization/Bgs/Mathlib.lean`. Сборка: `(cd formalization && lake build)`.

| Файл | Пространство имён | Содержание |
|---|---|---|
| `formalization/Bgs/Mathlib/CatMap.lean` | `Bgs.Mathlib` | кошачье отображение `S = [[3,4],[2,3]]` |
| `formalization/Bgs/Mathlib/PeriodicPoints.lean` | `Bgs.Mathlib` | FM-012: решётки периодических точек |
| `formalization/Bgs/Mathlib/AbelPoisson.lean` | `Bgs.Mathlib` | статистика Абеля `L_D(s)`, тождество Пуассона, TRACE-006 |
| `formalization/Bgs/Mathlib/ClockFloor.lean` | `Bgs.Mathlib` | TRACE-007/092 §1: универсальный «часовой» пол |
| `formalization/Bgs/Mathlib/CueReference.lean` | `Bgs.Mathlib` | эталон CUE и его предел |
| `formalization/Bgs/Mathlib/SineKernel.lean` | `Bgs.Mathlib` | ядро синуса, `ρ₂ = 1 − K²`, фурье-треугольник |
| `formalization/Bgs/Mathlib/CoherenceMemory.lean` | `Bgs.Mathlib` | TRACE-082: память когерентности и плато |
| `formalization/Bgs/Mathlib/PhaseChannel.lean` | `Bgs.Mathlib` | TRACE-053: элементарные оценки |
| `formalization/Bgs/Mathlib/HardyClock.lean` | `Bgs.Mathlib` | TRACE-091: веса Харди, препятствие к равенству Абеля, избыток CUE |
| `formalization/Bgs/Mathlib/TwoClock.lean` | `Bgs.Mathlib` | TRACE-008: момент Грама, двухчасовой фальсификатор |
| `formalization/Bgs/Mathlib/DigitFUP.lean` | `Bgs.Mathlib` | FUP-001: насыщение цифрового FUP для чётных оснований |
| `formalization/Bgs/Mathlib/MultiradiusRigidity.lean` | `Bgs.Mathlib` | RES-016: многорадиусная жёсткость полиномов (теорема 1(b), точность, §5) |
| `formalization/Bgs/Mathlib/TraceMobius.lean` | `Bgs.Mathlib` | TRACE-001: суммы по попарно различным индексам (k = 2, 3 и общая рекурсия) |
| `formalization/Bgs/Mathlib/ClockRigidity.lean` | `Bgs.Mathlib` | TRACE-092: точное разложение избытка и жёсткость равенства в часовом полу |
| `formalization/Bgs/Mathlib/DigitFUPBinary.lean` | `Bgs.Mathlib` | FUP-001: двоичный случай `M = 2`, точная норма `√(2/N)` |
| `formalization/Bgs/Mathlib/HardyIdentity.lean` | `Bgs.Mathlib` | TRACE-091: полное тождество Харди для радиального отношения, минимум |
| `formalization/Bgs/Mathlib/HardyRigidity.lean` | `Bgs.Mathlib` | TRACE-091: случай равенства ⇔ повёрнутые часы |
| `formalization/Bgs/Mathlib/TraceReconstruction.lean` | `Bgs.Mathlib` | TRACE-001 §4: короткие следы не определяют парную статистику |
| `formalization/Bgs/Mathlib/TraceMobiusGeneral.lean` | `Bgs.Mathlib` | TRACE-001, теорема 1 для всех `k` (циклическая форма) |
| `formalization/Bgs/Mathlib/FreshPhaseAverage.lean` | `Bgs.Mathlib` | TRACE-061: интеграл Пуассона и точные средние по свежей фазе |
| `formalization/Bgs/Mathlib/FlatChirp.lean` | `Bgs.Mathlib` | TRACE-081 §§2–3: квадратичная сумма Гаусса (O8), чирп `V_p`, след (O9), ядро `H`, `H⁶ = 1` |
| `formalization/Bgs/Mathlib/FlatTensor.lean` | `Bgs.Mathlib` | TRACE-081 §4, §7: тензорная конструкция `A_k = H^{⊗k} ⊗ V_p`, (O10), (O11), резонанс |
| `formalization/Bgs/Mathlib/FlatPerturb.lean` | `Bgs.Mathlib` | TRACE-081 §§5–7: малые фазы столбцов, (O1), (O2), (O5) |
| `formalization/Bgs/Mathlib/FirstReturnPulse.lean` | `Bgs.Mathlib` | TRACE-083, R1: интенсивности возврата `P(A^m)` |
| `formalization/Bgs/Mathlib/ClockCharacter.lean` | `Bgs.Mathlib` | TRACE-014: характерная оценка корней из единицы для часов (C2, C3, C6–C8) |
| `formalization/Bgs/Mathlib/FormFactorCurve.lean` | `Bgs.Mathlib` | TRACE-070: гармоническая мажоранта (3), (4) |
| `formalization/Bgs/Mathlib/TwoStepObstruction.lean` | `Bgs.Mathlib` | TRACE-074 §§1–2: поправка Хаусхолдера, предписания (7)–(9), компаньон (4) |
| `formalization/Bgs/Mathlib/ExactCumulants.lean` | `Bgs.Mathlib` | TRACE-069: точные четвёртые кумулянты CSE (3), (4), равномерная оценка; дисперсия CUE (7), (8) |
| `formalization/Bgs/Mathlib/TwoStepVariance.lean` | `Bgs.Mathlib` | TRACE-078: второй момент замороженного двухшагового приращения (комбинация, оценка `q_e`, координатные суммы 1, 2, 4, 6) |
| `formalization/Bgs/Mathlib/PairSumFactorization.lean` | `Bgs.Mathlib` | арифметика Кэли: факторизация парных сумм (теоремы 1, 2, 4) |
| `formalization/Bgs/Mathlib/UniformCluster.lean` | `Bgs.Mathlib` | лемма об однородном кластере: оценка (B1) |
| `formalization/Bgs/Mathlib/PureLoss.lean` | `Bgs.Mathlib` | различение двух состояний через чистые потери: скалярный слой (с исправлением тождества для `r²`) |
| `formalization/Bgs/Mathlib/QuadraticResponse.lean` | `Bgs.Mathlib` | пределы квадратичного отклика: all-pass тождество, определители орбит, сингулярность лаговой матрицы Грама |
| `formalization/Bgs/Mathlib/DeletedClock.lean` | `Bgs.Mathlib` | дополнение к TRACE-091: «удалённые часы» — точная статистика Абеля, строгий избыток, предел и асимптотика `1/N` |
| `formalization/Bgs/Mathlib/LocalJetObstruction.lean` | `Bgs.Mathlib.LocalJet` | BGS-RES-002: локальная полиномиальная кограница скобки `{G, G∘S}` |
| `formalization/Bgs/Mathlib/RadialTail.lean` | `Bgs.Mathlib.RadialTail` | радиальная замена `z = ψ/√(1+|ψ|²)`, интеграл по диску, вспомогательная оценка хвоста |
| `formalization/Bgs/Mathlib/AbsorptionBound.lean` | `Bgs.Mathlib.Absorption` | точная оценка вещественного поглощения (A1)–(A3), скалярные леммы коэрцитивности тела, явные константы `K = 5`, `c = 1/50` |
| `formalization/Bgs/Mathlib/HyperbolicEigenline.lean` | `Bgs.Mathlib` | иррациональность наклона собственных прямых гиперболических матриц `SL(2,ℤ)` (вход в аналитическую жёсткость скобки) |
| `formalization/Bgs/Mathlib/ResonanceComb.lean` | `Bgs.Mathlib.ResonanceComb` | скалярные входы теоремы о резонансной гребёнке Пелля: глобальное неравенство Тейлора для `e^{iy}`, гауссово отношение моментов |

Сборка: `(cd formalization && lake build)` из корня BGS. Все модули собраны без ошибок;
`sorry` нет; `#print axioms` для ключевых теорем даёт только стандартные
аксиомы `propext`, `Classical.choice`, `Quot.sound`. Новых аксиом нет.

## Соответствие утверждениям реестра

Обозначения: `T_m = Σ_j e^{2πi m x_j}`,
`L_D(s) = D⁻² Σ_{m≥1} e^{−2sm/D} |T_m|²`.

| Утверждение | Теорема Lean | Что доказано формально |
|---|---|---|
| BGS-TRACE-007, BGS-TRACE-092 §1 | `abelL_ge_clock` | для любого `N ≥ 1`, любого спектра `x : Fin N → ℝ` и `s > 0`: `L_N(s) ≥ 1/(e^{2s} − 1)` (через явный положительный сертификат G + H) |
| BGS-TRACE-007 (равенство) | `abelL_clock` | для часового спектра `x_j = j/D`: `L_D(s) = 1/(e^{2s} − 1)` |
| — (общий инструмент) | `abelL_poisson_identity`, `poisson_hasSum` | тождество Пуассона для `L_D(s)` |
| BGS-TRACE-006, предл. 1 | `abelL_cluster_lower_bound` | нижняя оценка Абеля для спектра, сгруппированного в `M` кластеров |
| BGS-TRACE-006, предл. 2 | `cluster_trace_factorization`, `cluster_trace_eq_zero` | факторизация и обнуление следа для кластерного спектра |
| BGS-TRACE-082, M1 | `return_memory_recurrence`, `coherent_part_formula` | точная рекуррентность памяти возврата для произвольного идемпотента `D` и линейного `T` |
| BGS-TRACE-082, M2 | `coherence_plateau_hs`, `coherence_plateau_opNorm` | для унитарной `U`, `N ≥ 2`, `r < N`: индуцированная норма `HS → HS` оператора `E^r` равна 1 (не фробениусова норма супероператора) |
| BGS-TRACE-053 (входные леммы) | `stochastic_pow_entry_le`, `degree_two_coeff_le`, `unistochastic_pow_entry_le` | элементарные оценки элементов степеней (уни)стохастических матриц |
| BGS-FM-012 | `fix_count_odd`, `fix_count_even` | `det(S^m − 1) = −4x_m²` (нечётные `m`) и `−8y_m²` (чётные `m`) |
| BGS-FM-012 | `annihilator_odd`, `annihilator_even` | описание решётки-аннигилятора `(S^m − 1)ᵀℤ²` |
| BGS-FM-012 | `ell_values`, `ell_ge_fourteen` | `ℓ₁..ℓ₆ = 2, 4, 14, 24, 82, 140`; `ℓ_m ≥ 14` при `m ≥ 3` |
| кошачье отображение | `catS_trace_pow_real` и др. | `tr S^n = λⁿ + λ⁻ⁿ`, `λ = 3 + 2√2`; `det S = 1`; сохранение формы Пелля |
| эталон CUE | `cueL_closed_form`, `cueL_tendsto` | замкнутая форма и предел `L_N(s) → (1 − e^{−2s})/(4s²)` |
| ядро синуса | `sineKernel_sq_eq_fourier_triangle` | `∫_{−1}^{1} (1 − |t|) cos(2πxt) dt = K(x)²` |
| BGS-TRACE-091 | `hardyWeight_zero`, `hardyWeight_N`, `hardyWeight_second_difference` | граничные значения и вторая разность весов Харди `w_m` |
| BGS-TRACE-091 | `hardyWeight_pos` | при `0 < b < a < 1` все внутренние веса `w_m > 0` |
| BGS-TRACE-091 | `abel_equality_obstruction` | препятствие к равенству: при `0<r<1`, `0<k<N`: `r^{−2k} + r^{−2(N−k)} < 1 + r^{−2N}` |
| BGS-TRACE-091, (13) | `cue_hardy_excess_pos` | предельный избыток CUE в (13) строго положителен |
| BGS-TRACE-008, (4) | `gramMoment_formula` | `(1/N) tr(G²) = 1 + (2/N³) Σ_{m=1}^{N−1} (N − m) |T_m|²` (формула (4) момента Грама) |
| BGS-TRACE-008 | `cueGramMoment_eq` | эталон CUE: `4/3 − 1/(3N²)` |
| BGS-TRACE-008, (3) | `gramMoment_twoGon`, `exists_twoGon_cue_gram` | для двухугольника момент равен `1 + cos²(φ/2)`; существует двухугольник с моментом CUE |
| BGS-TRACE-008, (8), (10) | `abelL_twoGon`, `twoClockB_closed_form` | точная абелева статистика двухугольника и замкнутая форма `B(s)` |
| BGS-TRACE-008 | `twoClockB_le`, `twoClockB_ne_cue` | `B(s) ≤ e^{−s}/(1 − e^{−s})` и отличие `B` от эталона CUE (при `s = 8`) — фальсификатор |
| BGS-FUP-001 | `digit_complement`, `digit_add_repunit_ne`, `offDiag_complement` | комбинаторика цифр, вне-диагональное множество `X_k` и его симметрия |
| BGS-FUP-001 (чётные `M ≥ 4`) | `even_offdiag_fup_saturated` | существует единичный вектор с носителем в `X_k`, чьё ДПФ — тоже единичный вектор с носителем в `X_k`; норма сжатия равна 1 |
| BGS-RES-016, лемма | `real_sparse_pos_roots_card_le`, `sparse_pos_roots_card_le` | правило знаков Декарта: число положительных корней разреженного многочлена |
| BGS-RES-016, теорема 1(b) | `multiradius_rigidity` | число плоских радиусов `|S| + 1 ≤ rank` (ранг коэффициентов) |
| BGS-RES-016 | `flat_at_rank_radii_orthogonal`, `orthogonal_isFlat` | если число плоских радиусов ≥ ранга, коэффициенты попарно ортогональны; ортогональность ⇒ плоскость на любом радиусе |
| BGS-RES-016 (точность) | `sharpExample_attains_bound` | пример `P = (2(1+z), √5 z(1−z), z²(1+z))`: плоские радиусы ровно `{1, 2}`, ранг 3 |
| BGS-RES-016, §5 | `two_radius_quadrature_rigidity` | двухрадиусная квадратура: плоскость `|A|²+|B|²` на двух различных радиусах ⇒ ортогональность коэффициентов |
| BGS-TRACE-001 | `distinct_sum_two`, `distinct_sum_three` | разложение сумм по попарно различным индексам для `k = 2, 3` (инклюзия–исключение) |
| BGS-TRACE-001 | `distinct_sum_cons` | общая рекурсия, порождающая формулу Мёбиуса по разбиениям |
| BGS-TRACE-092, (2) | `abelL_excess_decomposition` | точное разложение `L_N(s) − 1/(e^{2s}−1)` в сумму неотрицательных слагаемых (сертификат G + H) |
| BGS-TRACE-092 (жёсткость) | `abelL_eq_clock_iff`, `abelL_gt_clock`, `Hfun_eq_zero_iff` | при `N ≥ 1`, `s > 0`: равенство в часовом полу ⇔ спектр — повёрнутые часы (`IsRotatedClock`); иначе строгое неравенство |
| BGS-FUP-001 (`M = 2`) | `offDiag_two_iff`, `binary_offdiag_fup_bound` | описание вне-диагонального множества при `M = 2`; норма сжатия `≤ √(2/N)` |
| BGS-FUP-001 (`M = 2`, точность) | `binary_offdiag_fup_sharp` | норма сжатия равна ровно `√(2/N)` (достигается) |
| BGS-TRACE-091, (5) | `radialRatio_hardy_identity` | полное спектральное тождество: радиальное отношение = часовая константа + неотрицательный остаток Харди `hardyRem` |
| BGS-TRACE-091 | `radialRatio_ge_clock`, `radialRatio_eq_clock_iff` | `Z_U ≥ Z_cl`; равенство ⇔ все внутренние коэффициенты векового многочлена равны нулю |
| BGS-TRACE-091 (жёсткость) | `interior_coeff_zero_iff_rotated`, `radialRatio_eq_clock_iff_rotated` | внутренние коэффициенты равны нулю ⇔ собственные фазы — повёрнутые часы; итог: равенство ⇔ повёрнутые часы |
| BGS-TRACE-001, §4 | `short_traces_do_not_determine_pair_statistic` | явная пара спектров (часы и «удвоенные» фазы) с совпадающими следами в коротком окне, но разной парной статистикой |
| BGS-TRACE-001, теорема 1 | `distinctSum_cycle_formula` | факториальное тождество следов для любого `k`: сумма по попарно различным индексам = сумма по перестановкам `sign(σ)` × произведение следов по циклам |
| BGS-TRACE-061, (2) | `poisson_moment`, `freshDenom_factor`, `freshZeta_norm_lt_one`, `fresh_phase_moment` | факторизация `d(w) = (r+s+Δ)/2·|1−ζw|²`, `|ζ| < 1`; `E_w w^k/d(w) = ζ̄^k/Δ` для всех `k ≥ 0` (при `|γ|² < rs`) |
| BGS-TRACE-061, (3)/(4) | `fresh_phase_conj_moment`, `fresh_phase_conjugated_average` | `E_w w̄/d(w) = ζ/Δ`; поэлементное среднее `R₀ − (a−w̄b)(a−w̄b)*/d(w)` равно `R₀ − (aa*+bb*−ζ̄ab*−ζba*)/Δ` |
| BGS-TRACE-061, (6)/(7) | `fresh_phase_leverage_average`, `fresh_phase_leverage_identity` | `E_w δ/d(w) = δ/Δ`; при `X = I`: `δ/Δ = ½√(1−|γ|²)` |
| BGS-TRACE-081, (O8), (O9) | `chirp_sum_normSq`, `chirpV_trace_pow_normSq` | для нечётного простого `p`, `a ≠ 0`: `|∑_b e^{2πi(ab²+db)/p}|² = p`; `|Tr V_p^q|² = p` при `p ∤ q` |
| BGS-TRACE-081, §3 | `coreH_unitary`, `coreH_pow_six`, `reversal_coreH` | ядро `H` унитарно и плоско, `H⁶ = 1`, матрица обращения `B(H)` |
| BGS-TRACE-081, (O10), (O11) | `flatA_unitary`, `flatA_entry_normSq`, `flatA_trace_pow_div_le` | `A_k` унитарна и плоска; `|Tr A_k^q|/N ≤ p^{-1/2}` при `p ∤ q` |
| BGS-TRACE-081, резонанс | `flatA_pow_resonance`, `flatA_trace_resonance` | `A_k^{(4^k−4)p} = 1` |
| BGS-TRACE-081, (O1) | `flatU_entry_normSq`, `norm_reversalB_flatU` | для любых фаз столбцов `U_k` плоская и `‖B(U_k)‖ = 2^{−k}` |
| BGS-TRACE-081, (O2), (O5) | `flatU_trace_pow_le`, `flatU_form_factor_ge` | `|Tr U_k^q|/N ≤ p^{−1/2} + qε`; в резонансе `|Tr U_k^t|²/N ≥ N(1 − tε)²` |
| BGS-TRACE-083, R1 | `intensity_flatA_pow`, `intensity_flatA_pow_odd`, `intensity_flatA_pow_even` | точные интенсивности возврата `|(A_k^m)_{ij}|²` |
| BGS-TRACE-014 | `clock_alternant_ratio`, `clock_trace_pow_eq_zero`, `clock_two_copy_max`, `lattice_points_in_window` | C6: отношение альтернантов; следы часов; C2/C3/C7; подсчёт решёточных точек (C8) |
| BGS-TRACE-070, (3), (4) | `harmonic_half_sum_le`, `harmonic_half_sum_le_log_dist` | `∑_{j=d}^{N−1}(j+½)^{−1} ≤ 2 + log(N/(d+1))` и интегрируемая мажоранта |
| BGS-TRACE-074, (5)–(9) | `householder_unitary`, `twoStep_prescriptions`, `twoStep_P2_entry` | детерминированная двухшаговая конструкция с совместимыми предписаниями |
| BGS-TRACE-074, (4) | `doublyStochastic_power_entry`, `doublyStochastic_power_entry_delta` | положительный компаньон для дважды стохастических степеней |
| BGS-TRACE-069, (3) | `cseKappa_formula_short`, `cseKappa_formula_middle`, `cseKappa_formula_plateau` | точная формула `κ₂₂` CSE во всех трёх диапазонах (из сумм (2) и группировки (1)) |
| BGS-TRACE-069, (4) | `cseKappa_diag`, `cseKappa_two_mul_sub_one` | `κ₂₂(N,N) = −(N/4)H₁(N) − (N²/8)H₂(N)`; плато уже при `n = 2N − 1` |
| BGS-TRACE-069, оценка | `cseKappa_le`, `hHarm_one_le_log`, `cseM2_le` | `κ₂₂ ≤ N H₁(N)/8`; `H₁(N) ≤ 2 + log(2N−1)`; `m₂ ≤ N[2 + ½log(2N−1)]` |
| BGS-TRACE-069, (7), (8) | `cueVar_short`, `cueVar_middle`, `cueVar_long`, `cueVar_le`, `cueVar_comparison` | дисперсия CUE по трём диапазонам, `≤ N² − N`, арифметическая форма (8) |
| BGS-TRACE-078, (V1) | `increment_second_moment_le` | шаг комбинации: `∑_e Δ_e² ≤ 2598 δ²[K_ij + (P³)_ij]` из шести оценок квадратичных сумм |
| BGS-TRACE-078 | `feedback_coeff_norm_le`, `increment_pointwise_le` | `|q_e| ≤ 2`; поточечная оценка из (V2) |
| BGS-TRACE-078, пункты 1, 2, 4, 6 | `sum_r_sq_le`, `sum_A_full_sq_le`, `A_split_bound`, `sum_C_sq_le`, `sum_F_sq_le` | координатные квадратичные суммы для унитарной `S` (Парсеваль, Коши) |
| арифметика Кэли, теоремы 1, 2, 4 | `pair_sum_resultant_factorization`, `pair_sum_resultant_factorization_poly`, `pair_sum_order_three_iff`, `pair_sum_const_sq` | факторизация результанта парных сумм, порядок нуля, форма через корни |
| лемма об однородном кластере, (B1) | `cyclic_form_bounds`, `diagDominant_inv_decay`, `cluster_B1` | `−2I ≤ H₀ ≤ −I`, оценки обратной матрицы с диагональным преобладанием, (B1) |
| чистые потери, скалярный слой | `pl_r2_eq`, `pl_r2_source_formula_false`, `pl_delta_bounds`, `pl_L_bounds`, `pl_mean_shift`, `pl_fluctuation` | исправленное тождество для `r²` (см. ниже) и все скалярные оценки бюджета ошибок |
| пределы квадратичного отклика | `allpass_identity`, `orbit_determinants`, `lag_gram_singular`, `coercive_far_from_singular` | all-pass тождество, определители орбит, сингулярность циклической лаговой матрицы Грама |
| удалённые часы (TRACE-091) | `traceT_deleted`, `abelL_deleted` | `Tr V_N^m = N` при `(N+1) ∣ m`, иначе `−1`; точная формула `L_N^del(s) = 1/(N²(e^{2s/N}−1)) + (1−1/N²)/(e^{2s(1+1/N)}−1)` |
| удалённые часы (TRACE-091) | `deleted_not_rotatedClock`, `abelL_deleted_gt_clock` | при `N ≥ 2` спектр не является повёрнутыми часами, избыток Харди строго положителен |
| удалённые часы (TRACE-091) | `abelL_deleted_tendsto`, `abelL_deleted_excess_asymptotic`, `deleted_coeff_pos` | тем не менее `L_N^del(s) → 1/(e^{2s}−1)`; точнее `N(L_N^del(s) − 1/(e^{2s}−1)) → 1/(2s) − s/(2 sinh² s) > 0` |
| BGS-RES-002 | `Gfun_nonneg`, `Gfun_eq_zero_iff` | `G ≥ 0`, начало координат — строгий изолированный минимум |
| BGS-RES-002, (2) | `bracket_expansion`, `bracket_coeff_three`, `monomial_coboundary` | `{G, G∘S}` — однородный многочлен степени 6 с явными коэффициентами; резонансный коэффициент `c₃ = 16(λ²−λ⁻²)(2a²−λ²−λ⁻²)` обращается в нуль ровно при (2) |
| BGS-RES-002, (3) | `bracket_is_coboundary`, `bracket_ne_zero`, `project_a` | при (2) скобка равна `V − V∘S` для явного многочлена `V`; коэффициент при `u⁶` равен `8a(λ²−λ⁴) ≠ 0`; для `λ = 3+2√2` `a = √17` |
| радиальная замена | `one_sub_normSq_radial`, `radial_inverse`, `log_one_add_normSq_radial` | `1 − |z|² = 1/(1+|ψ|²)`, `ψ = z/√(1−|z|²)`, `log(1+|ψ|²) = −log(1−|z|²)` |
| радиальная замена | `disk_weight_integral` | `∫_{|z|<1} (1−|z|²)^a d²z = π/(1+a)` для `a ≥ 0` |
| радиальная замена, хвост | `centered_disk_tail_bound`, `absorbed_tail_bound` | для любого `S` с `e^{−S} ≤ e^{−cH}` на `Ω_N`: `∫_{Ω_N, H≥L} e^{−S} ≤ e^{−cL/2}[π/(1+c/2)]^{N−1}`; с поглощением — множитель `e^{s/2}` |
| вещественное поглощение, (A1) | `absorption_scalar_identity`, `absorption_scalar_bound`, `det_one_sub_smul_eq_prod`, `absorption_det_bound`, `absorption_det_bound_of_contraction` | `|det(I−αA)| ≥ ((1+α)/2)^d |det(I−A)|` при спектральном радиусе `≤ 1` (без нормальности), в частности для любого сжатия |
| вещественное поглощение | `absorption_det_sharp`, `absorption_complex_counterexample` | равенство при `A = −I`; контрпример `A = −3i/4`, `α = i/2` к комплексному обобщению |
| вещественное поглощение, (A3) | `log_half_one_add_exp_neg`, `absorption_log_term_ge` | `M log((1+e^{−s/N})/2) = −Ms/(2N) + M log cosh(s/(2N)) ≥ −Ms/(2N)` |
| коэрцитивность тела | `logcosh_div_ge`, `neg_log_one_sub_tanh_sq`, `actual_constants` | `log cosh(s/K) ≥ K⁻² log cosh s` (`K ≥ 1`); `−log(1−tanh² r) = 2 log cosh r`; `K = 5`, `c = 1/50`, `4(1+2·10⁻⁶⁶)² < 5` |
| аналитическая жёсткость скобки | `hyperbolic_eigenvalue_irrational`, `hyperbolic_eigenline_irrational`, `catS_eigenline_irrational` | собственные значения иррациональны; собственная прямая гиперболической `S ∈ SL(2,ℤ)` имеет иррациональный наклон |
| резонансная гребёнка Пелля | `exp_I_taylor_bound`, `gaussian_moment_ratio`, `gaussian_moment_ratio_tendsto` | `|e^{iux} − ∑_{l<n}(iux)^l/l!| ≤ |ux|^n/n!`; `A^{2r}(2r−1)!!/(2r)! = A^{2r}/(2^r r!) → 0` |

## Границы доверия (честно)

* Форм-фактор CUE `min(m, N)` в `CueReference.lean` взят как **определение**;
  мера Хаара и вывод форм-фактора из неё не формализованы.
* Предложения TRACE-006/007/082 формализованы в той форме, что указана в
  таблице; аналитические следствия из других разделов не формализованы.
* **BGS-BGS-001 (сама гипотеза BGS) и BGS-TRACE-005 остаются открытыми.**
  Ничто в этом слое их не доказывает.

## Проверенная версия и происхождение

Полная сборка адаптированного графа завершилась успешно: 8776 Lake jobs,
без ошибок и предупреждений. Для всех 589 публичных теорем/лемм нового слоя
проверены `#print axioms`: только `propext`, `Classical.choice`, `Quot.sound`
либо отсутствие аксиом. Это не меняет отдельную границу доверия прежних
сертификатов `native_decide`.

[Машиночитаемый протокол](../evidence/formalization/aristotle_20261027/receipt.json)
содержит хеш исходного архива, судьбу всех 52 изменённых входных файлов,
исходные и адаптированные хеши 39 модулей, полный список 589 проверенных имён
и их аксиом. После смены среды исходники восстановлены по этим хешам;
повторная проверка ядром не выдаётся за новый запуск.

Исходный архив был основан на старом `main`. Его `STATUS.md`, `CHANGELOG.md`,
реестр errata и README не заменяют актуальные файлы целиком: внесены только
содержательные дополнения. Технический `RequestProject/Main.lean` и сообщение
о лимите времени не добавляются; второй Lake-проект не создаётся.

Исправление ERR-060: в тождестве для `r²` необходим член `−4u²e`.
При `u = 1/16`, `η = 1/2`, `n = 1` прямое вычисление даёт `255/256`,
а старое отображение давало `257/256`. Lean-модуль `PureLoss` проверяет
скалярное тождество и оценки; полный аргумент о канале и тензорных степенях
остаётся аналитическим доказательством.
