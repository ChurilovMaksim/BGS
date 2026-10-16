# Сверка последнего чата «Решение гипотезы BGS» с main

Дата: 16 октября 2026. Исходный main:
`e20825f15b62c403ddb52ef345aa48e339eda21d` от 14 октября.
Тип проверки: авторская повторная проверка и новые конечные вычисления.
Независимое внешнее рецензирование и новая аналитическая Lean-формализация
не проводились.

Проверен полный сохранённый свод от 15 октября: 103 раздела, 16 исходных
записок и 90 записей реестра. Все исходные тексты сохранены в
[историческом документе](history/2026/chat_20261015/BGS_complete_research_2026-10-15.md).
[Машинная карта переноса](chat_integration_20261016.json) связывает новые
канонические доказательства с исходными SHA-256;
[полный реестр 90 записей](chat_claim_inventory_20261016.json) сохраняет
исходные статусы, исправления и адреса. Историческое «подтверждено» не
равнозначно новой сертификации в этом проходе.

## Что внесено в поддерживаемый корпус

| Семейство | Каноническое содержание | Граница проверки |
|---|---|---|
| FM-032 | Циклическая аддитивная когомология, чётность cat-периода, начальные скорости фаз | Простые p>99; линейный отклик не переносится на растущую физическую силу |
| FM-033 | Нормированная одношаговая Weyl-overlap оценка всех масштабов | Условно на количественные входы G1–G3; конечные проверки не заменяют их аналитический аудит |
| TRACE-084 | Критерий через мезоскопическую дисперсию числа уровней блока | Только достаточный маршрут удаления выбранного сектора |
| TRACE-085 | Root lifting, потеря меток корней и исправление необходимости (R) | Абстрактные спектры, включая доказательство детерминированного существования; не физический U_N |
| TRACE-086 | Полная H_diag даёт Sine₂, все фиксированные локальные моменты и UI | Доказана импликация; сама физическая H_diag не доказана |
| CUE-002 | Полная CUE-ковариация всех положительных степеней и производная по coupling | Эталонный ансамбль и точное конечное тождество |
| TRACE-087 | Параметрическая полоса O(N²), количественное снятие усреднения | Нужная физическая интегральная оценка остаётся открытой |
| TRACE-088 | Точная rooted BEST-нормировка, экспоненциальная равнорёберная масса и компенсация | Dense-mixing входы; компенсация определена лишь до O(N²) |
| TRACE-089 | Факториально взвешенное удаление редких конфигураций и sinh(c²/2)/(c²/2) | Фиксированное конечное c=m/sqrt(N); не времена порядка N |
| TRACE-090 | Полные bounded radial ratios, mixed-критерий слабого процесса и квадратура | Требуемые физические mixed-пределы открыты; слабый закон не даёт UI |
| TRACE-091 | Clock-минимум и явные положительные остатки Харди | Любой унитарный спектр; CUE требует положительного, ещё не вычисленного excess |

В [отдельном контроле](../mathematics/deleted_clock_hardy_boundary_20261015.md)
сохранено точное разложение deleted-clock excess порядка 1/N. Остальные
исходные алгебраические, арифметические, классические и квантовые результаты
доступны в разделах 10–47 исторического документа с сохранёнными
ограничениями: фиксированные частоты, малый параметр, внешние динамические
входы, конечные диапазоны и явно отозванные сильные утверждения. Они не
переименованы в новые безусловные теоремы.

## Исправления

1. Удаление отдельного резонансного сектора (R) не является необходимой
   последней леммой BGS. Root lifting сохраняет полный локальный процесс,
   хотя положительная энергия следов может лежать на редких временах.
   Компенсация происходит между знаковыми отклонениями секторов.
2. В Hardy/Blaschke-разложении p — характеристический полином унитарной
   матрицы. Одной самообратимости коэффициентов недостаточно; например,
   1+3z+z² имеет корни вне единичной окружности.
3. Дискретная Toeplitz-компрессия является положительной контракцией через
   Fourier-изометрию при числе узлов M>=N. Проверщик теперь отвергает
   недопустимую сетку; аналитическая ошибка aliasing рассматривается отдельно.
4. В мезоскопическом проверщике начальный правый предел включает правый
   конец дуги: 0<phi<=ell. Старая строгая граница могла дать отрицательное
   среднее числа уровней.
5. Отдельная UI-гипотеза излишня под полной all-order H_diag. Это не
   утверждение для одной парной статистики или одних bounded ratios.
6. Строгая конечная положительность остатка Харди не задаёт его предельную
   норму. Исчезновение всех фиксированных Taylor-коэффициентов также не
   контролирует энергию растущих степеней.

Эти изменения отражены в claim ledger, errata, графе зависимостей,
теоремном указателе, тематической навигации, RU/EN README и активной рукописи.

## Воспроизводимость и пределы выполненной работы

Контроль целостности исходного архива прошёл для 268 файлов и 16 включённых
исходных текстов. Для новой интеграции выполнены 15 конечных прогонов:
алгебраическая ревизия, фильтры, циклическая когомология, мезоскопический
критерий, контроль отвергнутого решения, root lifting, all-order closure,
scaled overlap, CUE covariance, de-averaging, equal-edge, collision,
bounded radial ratios, Hardy identities и deleted-clock control.
Точные Hardy-проверки используют уравнение Штейна для бесконечной нормы,
а не усечение ряда: 24 радиальных/абелевых случая и 24 комплексных
перекрёстных тождества. Численная часть проверяет 23 спектра. Все proxy
couplings явно отличаются от буквального 10^-80.

Команда из корня репозитория:

```bash
python3 computations/verification/chat_20261015/run_checks.py --output build/chat-replay
```

Требования Python заданы в requirements.txt. Каждый запуск работает во
временном каталоге, сохраняет код возврата, команду, хеш исходника и выходы.
[Новые результаты исполнения](../evidence/executions/20261016/chat-integration/receipt.json)
отделены от исторических журналов. Доступен закреплённый снимок исходников;
полное клонирование не удалось. Проверка реестра использует реальные
локальные тексты математического раздела и пути полного удалённого Git-tree.
Она не объявляется полным pytest, новым lake build или сборкой PDF.

## Граница доступа к последнему чату

Это сверка сохранённого математического корпуса, а не буквальная выгрузка
всех реплик. Более поздние сообщения доступны только в выдержках.
Для сообщения о гауссовом относительном сравнении равнорёберной суммы при
m=o(N^(3/4)) не получены точная формулировка, остаток, доказательство и код.
Упомянутые там количества слов, таблиц и Wick-сопоставлений не считаются
воспроизведёнными. Результат записан как непроверенное дополнение в карте
переноса и не повышен до доказанного. Восстановленные условия унитарности,
M>=N и точные дисперсии проверены отдельно.

**TRACE-005 и BGS-BGS-001 остаются открытыми.** Внесённые конечные тождества,
условные редукции, контрольные спектры и перепроверка кода не подменяют
модельно-зависимое знаковое сокращение на гейзенберговом масштабе.

## Полная карта исходных записей

| ID | Исходное утверждение | Исходный статус | Текущий адрес |
|---|---|---|---|
| A01 | Определение неизменённого оператора и midpoint/raw-словарь | ПОДТВЕРЖДЕНО | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A02 | 32 Fourier-моды, центрирование и эрмитовость | ПОДТВЕРЖДЕНО | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A03 | Точная норма Tr(A_N^2)/N=66033/160000 | ПОДТВЕРЖДЕНО | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A04 | Лаговая ковариация g и гауссова дисперсия 1650797/4000000 | ПОДТВЕРЖДЕНО | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A05 | Гиперболичность и полная C1-классификация симметрий | ИМПОРТИРОВАНО С ГРАНИЦЕЙ | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A06 | Фазовая независимость фиксированных аналитических наблюдаемых на сетке | ПОДТВЕРЖДЁН АРГУМЕНТ | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A07 | Полиномиальная скорость каждого фиксированного фазового Fourier-мода | ПОДТВЕРЖДЁН АРГУМЕНТ | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A08 | Точные cat-возвраты и d_p\|p-(2/p) | ПОДТВЕРЖДЕНО | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A09 | Нижняя граница d_p>2 log p/log lambda | ПОДТВЕРЖДЕНО | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A10 | Неограниченность p/d_p по Чеботарёву | ПОДТВЕРЖДЁН АРГУМЕНТ С ВНЕШНЕЙ ТЕОРЕМОЙ | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A11 | Плотность один для d_p>p^(1/2-epsilon) | ПОДТВЕРЖДЕНО | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A12 | Четырёхоператорное Weyl-тождество для одномерного кика | ПОДТВЕРЖДЕНО | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A13 | Бесселевы оценки O(p^-1/6), затем O(log p/sqrt p) | ПОДТВЕРЖДЁН АРГУМЕНТ | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A14 | Средняя косинусная OTOC до времени p с O(1/log p) | ПОДТВЕРЖДЁН АРГУМЕНТ | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A15 | Матрица H_m: det, ранг и трёхдиагональная обратная | ПОДТВЕРЖДЁН АРГУМЕНТ | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A16 | Локальная формула диагонального кика в полном cat-периоде | ПОДТВЕРЖДЁН АРГУМЕНТ | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A17 | Фазово-пространственная формула полного двумерного кика | ПОДТВЕРЖДЕНО | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A18 | Унитарность полного передаточного оператора | ПОДТВЕРЖДЕНО | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A19 | Ранг полной симплектической формы и её Fourier-преобразование | ПОДТВЕРЖДЕНО | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A20 | Метаплектические примеры с плоскими Weyl-коэффициентами | ПОДТВЕРЖДЁН АРГУМЕНТ | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A21 | Расстояние полного Q_N от Clifford-нормализатора >= const*tau | ПОДТВЕРЖДЁН АРГУМЕНТ | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A22 | Аналитическое некоммутативное телескопирование V M V* M* | ПОДТВЕРЖДЕНО | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A23 | Низкие OTOC/высокая Weyl-энтропия не исключают возвраты | ПОДТВЕРЖДЕНО | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A24 | Классический bracket h={g,g o S}: 726 мод и дисперсия | ПОДТВЕРЖДЕНО | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A25 | Два точных периодических сертификата bracket | ПОДТВЕРЖДЕНО | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A26 | Ненулевой периодический сертификат при физическом kappa | ВОССТАНОВЛЕН ОСТАТОК | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A27 | Положительная асимптотическая дисперсия h_kappa | УСЛОВНО НА СТАНДАРТНЫЙ ДИНАМИЧЕСКИЙ ВХОД | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A28 | Нелаттисность h_0 и почти всех малых kappa | ПОДТВЕРЖДЁН АРГУМЕНТ | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A29 | Явные нижние границы 10^-21/(1+\|t\|) и диапазон 10^17 | НЕ ПОВЫШАЕТСЯ ДО ПОЛНОЙ СЕРТИФИКАЦИИ | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A30 | Q-линейная независимость четырёх геометрических лог-мультипликаторов | ПОДТВЕРЖДЁН АРГУМЕНТ | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A31 | Ruelle-декорреляция/LLT для фиксированных частот | УСЛОВНО НА ТОЧНУЮ ТЕОРЕМУ ПЕРЕНОСА | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A32 | Продукт Anosov с арифметическим фактором не имеет нужного предела | ИСПРАВЛЕНО ОБОСНОВАНИЕ СЛАБОГО ПРЕДЕЛА | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A33 | Классический предел Weyl-энергии как распределения смещения | ПОДТВЕРЖДЁН АРГУМЕНТ | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A34 | Абсолютная непрерывность предельной chord-меры | ПОДТВЕРЖДЁН АРГУМЕНТ | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A35 | Глобально ненулевая матрица Hess g | ПОДТВЕРЖДЕНО | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A36 | H3/H8 Hilbert–Schmidt Egorov и окно N^(2/3-eps) | ПОДТВЕРЖДЁН АРГУМЕНТ | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A37 | Скалярный конечный тип 2 и \|c_N(v)\|=O_tau(N^-1/7) | ПОДТВЕРЖДЁН АРГУМЕНТ | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A38 | Weyl-adjoint disperal O(\|v\|^-1/17) плюс Egorov-ошибки | ПОДТВЕРЖДЁН АРГУМЕНТ | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A39 | Масса любой конечнополевой прямой O_tau(p^-1/129) | УСЛОВНО НА КОЛИЧЕСТВЕННЫЙ OVERLAP-ВХОД | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A40 | Орбитальная Parseval-формула для усреднённых OTOC | ПОДТВЕРЖДЕНО | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A41 | Оценка split-orbit OTOC через Клоостермана | УСЛОВНО НА ВНЕШНИЙ WEIL-ВХОД | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A42 | Кограничный дефект \|\|P A\|\|, нечётный/чётный коэффициент | ПОДТВЕРЖДЕНО | [quantum_cyclic_cohomology_20261015](../mathematics/quantum_cyclic_cohomology_20261015.md) |
| A43 | Норма минимальной аддитивной первообразной Theta(sqrt d) | ПОДТВЕРЖДЁН АРГУМЕНТ | [quantum_cyclic_cohomology_20261015](../mathematics/quantum_cyclic_cohomology_20261015.md) |
| A44 | Фазовые скорости, Haar-сравнение и максимальный inert-order коэффициент | ПОДТВЕРЖДЕНО | [quantum_cyclic_cohomology_20261015](../mathematics/quantum_cyclic_cohomology_20261015.md) |
| A45 | p^(3/4-delta) как достаточный порог на плотности один | ПОДТВЕРЖДЕНО КАК ИМПЛИКАЦИЯ | [quantum_cyclic_cohomology_20261015](../mathematics/quantum_cyclic_cohomology_20261015.md) |
| A46 | Алгебраическая простота, transcendence и p-adic total minors | НЕ ПЕРЕСЕРТИФИЦИРОВАНО ПОЛНОСТЬЮ | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A47 | Полное доказательство другого агента | ОТКЛОНЕНО | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A48 | Равномерное det-Hessian=(linear det)*(1+O(tau)) при m->infty | ОТКЛОНЕНО В ТАКОМ ВИДЕ | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A49 | Линейная и квадратичная pre-asymptotic lower bounds E_p | ПОДТВЕРЖДЕНО | [resonant_mesoscopic_criterion_20261015](../mathematics/resonant_mesoscopic_criterion_20261015.md) |
| A50 | Критерий через дисперсию числа фаз блока | ПОДТВЕРЖДЕНО С ИСПРАВЛЕННЫМ КОДОМ | [resonant_mesoscopic_criterion_20261015](../mathematics/resonant_mesoscopic_criterion_20261015.md) |
| A51 | Пакетный контрпример: max нормированного следа ->0, энергия >0 | ПОДТВЕРЖДЕНО | [resonant_mesoscopic_criterion_20261015](../mathematics/resonant_mesoscopic_criterion_20261015.md) |
| A52 | WKB-перенос резонансной энергии и полного теста | ТОЛЬКО УСЛОВНАЯ ИМПЛИКАЦИЯ | [resonant_mesoscopic_criterion_20261015](../mathematics/resonant_mesoscopic_criterion_20261015.md) |
| A53 | Гауссов quantum echo почти до log N/log lambda | ПОДТВЕРЖДЁН АРГУМЕНТ В ДРУГОМ МАСШТАБЕ | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A54 | (R) как необходимая последняя лемма BGS | ОТОЗВАНО | [root_lifting_sector_boundary_20261015](../mathematics/root_lifting_sector_boundary_20261015.md) |
| A55 | Root-lift, детерминированный выбор базы, generic splitting | ПОДТВЕРЖДЁН АРГУМЕНТ | [root_lifting_sector_boundary_20261015](../mathematics/root_lifting_sector_boundary_20261015.md) |
| A56 | U=Z R_d(C), Z^d=I | ИСПРАВЛЕНА НОРМИРОВКА | [root_lifting_sector_boundary_20261015](../mathematics/root_lifting_sector_boundary_20261015.md) |
| A57 | Новый результат: одинаковый полный C, разные локальные законы корней | ДОКАЗАНО НИЖЕ | [root_lifting_sector_boundary_20261015](../mathematics/root_lifting_sector_boundary_20261015.md) |
| A58 | Новый результат: точное локальное сведение к смеси помеченных секторов | ДОКАЗАНО НИЖЕ | [root_lifting_sector_boundary_20261015](../mathematics/root_lifting_sector_boundary_20261015.md) |
| A59 | Общая BGS / Sine2 для исходного фиксированного семейства | НЕ ДОКАЗАНО | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| A60 | Практические численные проверки как доказательство асимптотики | НЕ ДОПУСКАЕТСЯ | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| B01 | Полная H_diag даёт weak Sine₂, все фиксированные локальные моменты и UI | ДОКАЗАНА УСЛОВНАЯ ИМПЛИКАЦИЯ | [all_order_process_closure_20261015](../mathematics/all_order_process_closure_20261015.md) |
| B02 | Одношаговый полный Weyl-overlap с показателем 1/65 | АНАЛИТИЧЕСКИЙ АРГУМЕНТ С УКАЗАННЫМ ВХОДОМ | [scaled_weyl_overlap_20261015](../mathematics/scaled_weyl_overlap_20261015.md) |
| B03 | Абсолютное среднее OTOC вдоль каждой cat-орбиты для всех простых | СЛЕДСТВИЕ ПРЕДЫДУЩЕЙ ОЦЕНКИ | [scaled_weyl_overlap_20261015](../mathematics/scaled_weyl_overlap_20261015.md) |
| B04 | Сжатая арифметическая алгебра: (D^131/N)^(1/65) | СЛЕДСТВИЕ С РАЗМЕРНОСТНОЙ ПОТЕРЕЙ | [scaled_weyl_overlap_20261015](../mathematics/scaled_weyl_overlap_20261015.md) |
| B05 | Точная производная полного J по coupling | ТОЧНОЕ ТОЖДЕСТВО | [full_pair_cue_covariance_20261015](../mathematics/full_pair_cue_covariance_20261015.md) |
| B06 | Полная CUE-ковариация всех положительных trace powers | ЭТАЛОННЫЙ РАСЧЁТ | [full_pair_cue_covariance_20261015](../mathematics/full_pair_cue_covariance_20261015.md) |
| B07 | Прямые вычисления полного J при контрольных 0.03,0.30 | КОНЕЧНЫЕ ДИАГНОСТИКИ | [full_pair_cue_covariance_20261015](../mathematics/full_pair_cue_covariance_20261015.md) |
| B08 | Точная полоса O(N²) по параметру для J и фиксированных factorial-коэффициентов | ДОКАЗАНО АЛГЕБРАИЧЕСКИ | [parameter_deaveraging_20261015](../mathematics/parameter_deaveraging_20261015.md) |
| B09 | Количественное снятие параметрического усреднения | ДОКАЗАНА УСЛОВНАЯ ИМПЛИКАЦИЯ | [parameter_deaveraging_20261015](../mathematics/parameter_deaveraging_20261015.md) |
| B10 | Шестой CUE-момент O(N^-3) в произвольной фиксированной полосе | ЭТАЛОННЫЙ АРГУМЕНТ | [parameter_deaveraging_20261015](../mathematics/parameter_deaveraging_20261015.md) |
| B11 | Физический шестой момент как sinc-Gram-форма | ТОЧНАЯ РЕДУКЦИЯ, ОЦЕНКА ОТКРЫТА | [parameter_deaveraging_20261015](../mathematics/parameter_deaveraging_20261015.md) |
| B12 | Точный rooted BEST-подсчёт полного равнорёберного семейства | ДОКАЗАНО | [equal_edge_occupation_20261015](../mathematics/equal_edge_occupation_20261015.md) |
| B13 | Экспоненциальная равнорёберная масса при m~N | ДОКАЗАНО ПРИ DENSE-MIXING | [equal_edge_occupation_20261015](../mathematics/equal_edge_occupation_20261015.md) |
| B14 | Экспоненциальная компенсация до остатка O(N²) | ТОЧНОЕ СЛЕДСТВИЕ УНИТАРНОСТИ | [equal_edge_occupation_20261015](../mathematics/equal_edge_occupation_20261015.md) |
| B15 | Факториально взвешенное удаление тройных посещений при m=O(sqrt N) | ДОКАЗАНО | [collision_crossover_20261015](../mathematics/collision_crossover_20261015.md) |
| B16 | Полный sqrt-time crossover sinh(c²/2)/(c²/2) | ДОКАЗАНО В УКАЗАННОМ КЛАССЕ | [collision_crossover_20261015](../mathematics/collision_crossover_20261015.md) |
| B17 | Знаковое determinant-сокращение всех переключений | ТОЧНОЕ ТОЖДЕСТВО | [collision_crossover_20261015](../mathematics/collision_crossover_20261015.md) |
| B18 | Контрактивное radial ratio и положительный K | ТОЧНЫЕ СПЕКТРАЛЬНЫЕ ТОЖДЕСТВА | [bounded_radial_ratios_20261015](../mathematics/bounded_radial_ratios_20261015.md) |
| B19 | Mixed bounded ratios характеризуют weak Sine₂ | ДОКАЗАНА ЭКВИВАЛЕНТНОСТЬ | [bounded_radial_ratios_20261015](../mathematics/bounded_radial_ratios_20261015.md) |
| B20 | CUE radial mean и shifted Toeplitz-эталоны | ЭТАЛОННЫЕ ТОЖДЕСТВА | [bounded_radial_ratios_20261015](../mathematics/bounded_radial_ratios_20261015.md) |
| B21 | Размерностно-равномерная угловая квадратура для bounded ratios | ДОКАЗАНА ОЦЕНКА ОШИБКИ | [bounded_radial_ratios_20261015](../mathematics/bounded_radial_ratios_20261015.md) |
| B22 | Вторая радиальная производная равна 1+2L_N | ТОЧНОЕ ТОЖДЕСТВО | [bounded_radial_ratios_20261015](../mathematics/bounded_radial_ratios_20261015.md) |
| B23 | Минимум radial ratio на clock и положительный Hardy-остаток | КОНЕЧНОМЕРНАЯ ТЕОРЕМА | [hardy_spectral_remainder_20261015](../mathematics/hardy_spectral_remainder_20261015.md) |
| B24 | Положительно полуопределённое kernel-усиление Hardy | ТОЧНОЕ GRAM-ТОЖДЕСТВО | [hardy_spectral_remainder_20261015](../mathematics/hardy_spectral_remainder_20261015.md) |
| B25 | Abel floor как квадрат Hardy-нормы | ТОЧНОЕ ТОЖДЕСТВО | [hardy_spectral_remainder_20261015](../mathematics/hardy_spectral_remainder_20261015.md) |
| B26 | Исчезновение фиксированных Taylor-коэффициентов Hardy-остатка | СЛЕДСТВИЕ КОРОТКИХ СЛЕДОВ | [hardy_spectral_remainder_20261015](../mathematics/hardy_spectral_remainder_20261015.md) |
| B27 | Trace-norm stability полного bounded ratio | ДОКАЗАННАЯ ОЦЕНКА | [hardy_spectral_remainder_20261015](../mathematics/hardy_spectral_remainder_20261015.md) |
| B28 | Deleted-clock положительный excess с явным порядком1/N | ДОКАЗАНО В ТЕКУЩЕМ ПРОХОДЕ | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| B29 | Завершение сильной fixed-model BGS и общей BGS | НЕ ДОКАЗАНО | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
| B30 | Повторный запуск и архивирование источников | ПРОЦЕДУРА ВОСПРОИЗВОДИМОСТИ | [BGS_complete_research_2026-10-15](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md) |
