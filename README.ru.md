# BGS — арифметический квантовый хаос и спектральная универсальность

<p align="center">
  <a href="README.md">English</a> · <strong>Русский</strong>
</p>

<p align="center">
  <strong>Долгосрочная математическая исследовательская программа по гипотезе Бохигаса–Джаннони–Шмита, явным хаотическим квантовым отображениям и механизму возникновения универсальной микроскопической спектральной статистики из детерминированной динамики.</strong>
</p>

> **Текущий научный статус — 23 сентября 2026 года.**  
> Микроскопическая BGS-задача при фиксированной силе возмущения для поддерживаемой frozen-модели остаётся **ОТКРЫТОЙ**. Репозиторий содержит точные редукции, проектные доказательства в явно указанных областях применимости, применения внешних теорем с проверкой гипотез, конечные сертификаты, формальные алгебраические ядра, численные диагностики и явные контрпримеры к недостаточным стратегиям доказательства. Ни один из этих результатов не объявляется полным доказательством BGS без недостающей модельно-специфической оценки на масштабе времени Гейзенберга.

<p align="center">
  <img src="assets/readme/bgs_overview.svg" alt="Постановка BGS: классическая хаотическая динамика, квантовый спектр со средним расстоянием порядка 1/N и универсальная локальная статистика случайных матриц после правильного учёта симметрий." width="100%">
</p>

## Аннотация

Гипотеза **Бохигаса–Джаннони–Шмита (BGS)** утверждает, что квантовая система с хаотическим классическим пределом после устранения обычных симметрий и корректного unfolding должна иметь ту же **локальную спектральную статистику**, что и соответствующий ансамбль случайных матриц. Ключевое слово здесь — «локальную»: среднее расстояние между уровнями имеет порядок $1/N$, поэтому микроскопический предел исследует корреляции собственных значений на масштабе, уменьшающемся вместе с ростом размерности гильбертова пространства.

Этот репозиторий развивает строгую исследовательскую программу вокруг именно этого перехода. Основная лаборатория — явное нелинейное возмущение гиперболического квантового cat map,

$$
U_N=\exp(i\tau N A_N)\,M_N,
\qquad
\tau=10^{-80},
$$

где $\tau$ фиксировано при $N\to\infty$. Программа уже закрывает детерминированный переход от микроскопических корреляционных функционалов к взвешенным произведениям квантовых следов, устанавливает ряд структурных теорем для frozen-модели, доказывает арифметические законы возврата и crossover-режимы, получает точные конечнополевые/Cayley-редукции, развивает резонансно-кохомологические препятствия и строит явные falsifier-конструкции для нескольких заманчивых, но недостаточных путей.

Главный нерешённый вход для фиксированной модели теперь изолирован очень чётко:

$$
\boxed{\text{модельно-специфическое mixed/joint-trace cancellation при }m=\Theta(N)}
$$

для фактического desymmetrized frozen propagator. Это стабильное утверждение **BGS-TRACE-005**. Его доказательство вместе с уже закрытым детерминированным мостом и точными гипотезами о симметрии/unfolding закрыло бы поддерживаемую fixed-map цель **BGS-BGS-001**.

---

## Содержание

1. [Гипотеза BGS с нуля](#гипотеза-bgs-с-нуля)
2. [Что означает микроскопическая универсальность](#что-означает-микроскопическая-универсальность)
3. [Почему возникает время Гейзенберга](#почему-возникает-время-гейзенберга)
4. [Поддерживаемая фиксированная модель](#поддерживаемая-фиксированная-модель)
5. [Точный мост от следов к локальной статистике](#точный-мост-от-следов-к-локальной-статистике)
6. [Что уже установлено](#что-уже-установлено)
7. [Что уже исключено](#что-уже-исключено)
8. [Главный открытый фронтир](#главный-открытый-фронтир)
9. [Что даст успешное закрытие](#что-даст-успешное-закрытие)
10. [Избранные научные графики](#избранные-научные-графики)
11. [Репозиторий, проверяемость и публикации](#репозиторий-проверяемость-и-публикации)

---

# Гипотеза BGS с нуля

## Классический хаос

Детерминированная гамильтонова система или симплектическое отображение может быть сильно хаотическим: близкие траектории экспоненциально расходятся, существуют устойчивые и неустойчивые направления, периодические орбиты быстро пролиферируют, а долгосрочные классические наблюдаемые демонстрируют mixing-подобное поведение. Для отображений гиперболичность особенно удобна, потому что можно изучать итерации одного фиксированного преобразования.

Классическая часть этой программы начинается с гиперболического автоморфизма тора и малого нелинейного kick. В поддерживаемом диапазоне возмущения соответствующая frozen-классическая карта остаётся аналитической и Anosov.

Но классический хаос сам по себе ещё ничего не говорит о микроскопическом квантовом спектре.

## Квантование

Для $N$-мерного квантового отображения одношаговая эволюция задаётся унитарным оператором $U_N$. Его собственные значения лежат на единичной окружности:

$$
U_N\psi_j=e^{i\theta_j}\psi_j,
\qquad
j=1,\ldots,N.
$$

Таким образом, спектральные данные — это собственные фазы

$$
0\le \theta_1,\ldots,\theta_N<2\pi.
$$

На глобальном масштабе очень разные спектры могут выглядеть похожими. BGS интересует противоположный режим — масштаб **одного среднего расстояния между уровнями**.

## Историческое происхождение

Программа названа в честь работы 1984 года О. Бохигаса, М. Джаннони и К. Шмита, которые обнаружили random-matrix-подобные флуктуации уровней в хаотическом квантовом биллиарде и сформулировали принцип универсальности, теперь связанный с BGS:

> хаотическая классическая динамика должна после правильного учёта симметрий и unfolding приводить к универсальной локальной квантовой спектральной статистике типа случайных матриц.

Исходная работа:

O. Bohigas, M. J. Giannoni, C. Schmit, *Characterization of Chaotic Quantum Spectra and Universality of Level Fluctuation Laws*, Physical Review Letters **52** (1984), 1–4, DOI: [10.1103/PhysRevLett.52.1](https://doi.org/10.1103/PhysRevLett.52.1).

Современная математическая задача — не построить ещё одну убедительную гистограмму, а доказать предел универсальности для детерминированного семейства, точно зафиксировав ансамбль, symmetry block, unfolding, масштаб времени и класс тестовых функций.

---

# Что означает микроскопическая универсальность

## Unfolding и средний шаг

На единичной окружности среднее угловое расстояние между собственными фазами имеет порядок $2\pi/N$. После unfolding к единичной средней плотности исследуются локальные координаты вида

$$
x_j=\frac{N}{2\pi}(\theta_j-\theta_0),
$$

с точной центрировкой согласно выбранной конвенции.

Микроскопическая наблюдаемая поэтому видит интервалы длины $O(1/N)$ в исходной фазовой переменной. Это принципиально сильнее теоремы о глобальной плотности.

## Парные и высшие корреляции

Типичный парный функционал имеет вид

$$
\frac1N
\sum_{j\ne k}
\phi\!\left(
\frac{N}{2\pi}(\theta_j-\theta_k)
\right),
$$

где $\phi$ — достаточно регулярная тестовая функция.

Высшие $k$-точечные корреляции спрашивают, сходятся ли конфигурации различных unfolded eigenphases к соответствующему random-matrix point process.

Целевой ансамбль определяется симметрией. В unitary class естественным локальным эталоном является sine-kernel/CUE-семейство; при наличии подходящей antiunitary symmetry возникает orthogonal class. Корректная теорема обязана определить класс симметрии из оператора, а не выбрать его постфактум по удачной численной картинке.

## Глобальное сходство недостаточно

Следующие свойства строго слабее микроскопической BGS:

- сходимость глобальной эмпирической спектральной меры;
- Gaussian или semicircle limits для отдельных наблюдаемых;
- конечное число моментов;
- визуально убедительная spacing histogram при умеренных $N$;
- закон возврата на логарифмическом времени;
- кластеризация или расходимость Abel-transform;
- short-time trace estimate.

В репозитории есть точные конструкции, демонстрирующие несколько таких логических разрывов.

---

# Почему возникает время Гейзенберга

Ключевой механизм — Fourier duality.

Для поддерживаемой нормировки парного функционала имеется точное тождество

$$
C_{2,N}(U;\phi)
=
\frac{1}{N^2}
\sum_{m\in\mathbb Z}
\widehat{\phi}(m/N)
\left(
|\operatorname{Tr}U^m|^2-N
\right).
$$

Если $\widehat{\phi}$ поддержана в фиксированном компактном интервале, то $\widehat{\phi}(m/N)$ использует моды

$$
|m|\le cN.
$$

То есть даже compactly supported microscopic Fourier test требует информации о степенях порядка $N$.

Для Haar-unitary матриц $V_N\in U(N)$ точный эталон имеет вид

$$
\mathbb E\left|\operatorname{Tr}V_N^m\right|^2
=
\min(|m|,N).
$$

Следовательно, fixed-map задача состоит не в том, чтобы просто доказать «малость следов». Нужна **правильная взвешенная совместная статистика** на всём Heisenberg window.

<p align="center">
  <img src="assets/readme/bgs_scales.svg" alt="Иерархия временных масштабов от фиксированного времени через логарифмические и сублинейные степени к масштабу Гейзенберга m пропорционально N." width="100%">
</p>

Именно поэтому fixed-time semiclassics, возвратные законы при $m=O(\log N)$ и даже широкая информация при $m=o(N)$ сами по себе не дают BGS.

---

# Поддерживаемая фиксированная модель

Основная лаборатория:

$$
U_N=\exp(i\tau N A_N)\,M_N,
\qquad
\tau=10^{-80},
$$

где $M_N$ — квантование гиперболического cat map

$$
S=
\begin{pmatrix}
3&4\\
2&3
\end{pmatrix},
$$

а $A_N$ — поддерживаемое Weyl-квантование явного нелинейного символа.

Сразу важны две особенности.

### 1. Классическое возмущение очень мало, но фиксировано

Параметр $\tau$ **не** стремится к нулю при $N\to\infty$. Поэтому в квантовом экспоненциальном множителе стоит $\tau N$, и large-$N$ режим не является равномерно perturbative.

Это отделяет целевую задачу от shrinking-kick режимов типа

$$
\tau_N N\to0.
$$

Теорема для семейства с исчезающей силой kick может быть чрезвычайно полезной, но она не становится автоматически теоремой для frozen model.

### 2. Арифметические возвраты сосуществуют с нелинейной динамикой

Исходный cat map имеет сильную арифметическую структуру. Pell-подпоследовательности дают точные или почти точные возвраты и тем самым создают естественную лабораторию для проверки того, контролируют ли глобальные recurrence signatures микроскопическую статистику.

Одна из главных тем проекта — отделить реальные арифметические препятствия от эффектов, которые исчезают до достижения микроскопического масштаба.

---

# Точный мост от следов к локальной статистике

Детерминированная спектральная редукция — одна из наиболее завершённых частей программы.

Для distinct-index $k$-точечных сумм partition-lattice Möbius inversion точно выражает микроскопические factorial statistics через произведения следов

$$
\operatorname{Tr}U_N^{m_1},
\ldots,
\operatorname{Tr}U_N^{m_r},
$$

с линейными ограничениями на Fourier modes.

Поддерживаемый trace bridge имеет четыре базовых слоя.

### BGS-TRACE-001 — точная partition–Möbius формула

Спектральные суммы по различным индексам переводятся в произведения следов конечномерным комбинаторным тождеством.

### BGS-TRACE-002 — микроскопическое Fourier-представление

После unfolding компактная поддержка rescaled Fourier transform требует степеней вплоть до порядка $N$.

### BGS-TRACE-003 — достаточность сравнения на масштабе Гейзенберга

Если правильно взвешенные joint traces детерминированного propagator совпадают с соответствующими joint traces целевого random-matrix ensemble на любой фиксированной компактной Fourier support, то band-limited microscopic correlations сходятся.

### BGS-TRACE-004 — переход к Schwartz tests

При поддерживаемых positivity/normalization hypotheses сходимость на **каждой** компактной Fourier bandwidth продолжается на Schwartz correlation tests.

Слово «каждой» существенно. Одной фиксированной bandwidth недостаточно; в репозитории построен точный контрпример.

<p align="center">
  <img src="assets/readme/bgs_proof_architecture.svg" alt="Архитектура доказательной программы BGS для фиксированной модели: установленные структурные результаты и trace bridge, открытый Heisenberg-scale input и конечная микроскопическая цель." width="100%">
</p>

---

# Что уже установлено

Программу лучше читать как несколько семейств теорем с явно отделёнными границами применимости.

## 1. Структура fixed map

**BGS-FM-001 — теорема о классических симметриях frozen model.**  
В поддерживаемом малом диапазоне coupling классическая карта аналитична и Anosov; обычный $C^1$ centralizer сводится к степеням карты, отсутствует $C^1$ reversor, исключены соответствующие affine $C^1$ conjugacies.

**Граница:** это не исключает $N$-зависимые quantum commutants и не доказывает Heisenberg-time cancellation.

**BGS-FM-002 — full-symbol Gaussian crossover на odd-Pell подпоследовательности.**  
Нормированное period average полного kick symbol имеет Gaussian fixed-moment limit с точной дисперсией

$$
\sigma^2=\frac{1650797}{4000000}=0.41269925.
$$

Если scaled kick parameter удовлетворяет $\epsilon_K\sqrt K\to t$, нормированные recurrence traces имеют явный Gaussian crossover. Необходимое условие для CUE pair behaviour:

$$
|\epsilon_K|\sqrt K\to\infty.
$$

**Граница:** frozen regime $\epsilon_K=\tau N_K$ в конечном счёте выходит за доказанное bounded crossover window.

**BGS-FM-003 — точные moment controls и transfer bounds.**  
Finite-spectrum inequalities и repeated-clock falsifiers показывают, что несколько low-order или one-orientation loop tests могут выполняться для спектров, далёких от CUE.

**BGS-FM-004 — three-orientation mixed-resolvent barrier.**  
При явных residual-decay hypotheses получается количественный lower barrier для Abel pair statistic. Теорема условна, потому что эти residuals не контролируются для frozen propagator.

**BGS-FM-005 — точная frozen-kick rank boundary.**  
Для нечётных $N$ multiplicity собственных значений frozen generator не превосходит $\gcd(N,7)$, а значит

$$
\operatorname{rank}(U_N-zM_N)\ge N-\gcd(N,7)
$$

в точной заявленной области.

**Граница:** rank obstruction не является теоремой о локальной спектральной универсальности.

## 2. Резонансы и когомология

Резонансная ветка спрашивает, может ли малая variance объясняться классическим coboundary или скрытой дегенерацией.

**BGS-RES-001** доказывает sharp Fourier-line coercivity в указанных Sobolev classes.

**BGS-RES-002** строит локальный polynomial coboundary obstruction и показывает, что чисто локальные fixed-point jets не могут решить глобальную torus problem.

**BGS-RES-004** доказывает smooth finite-orbit lag independence для конечных объединений signed frequency orbits.

**BGS-RES-005** даёт full-lag uniform classical Riesz gap для фактического frozen physical symbol под linear cat transport, устойчивый в указанном weighted-Wiener perturbation ball.

**Открыто BGS-RES-003:** every-observable analytic nondegeneracy остаётся нерешённой.

Эти результаты существенно сужают пространство простых классических дегенераций, но всё ещё не дают quantum Heisenberg-time estimate.

## 3. Арифметика и Cayley energy

Арифметическая ветка переводит fourth-moment задачи в finite-field additive-energy problems.

**BGS-CAYLEY-001** даёт pair-key/fourth-moment reduction.

**BGS-CAYLEY-002** переводит mixed term в Cayley additive energy.

**BGS-CAYLEY-003** и **004** дают pointwise $K^{8/3}$-scale bounds в явных subgroup/curve regimes с проверенными отображениями гипотез внешних теорем.

Sharp centered target:

$$
E_+(A)
=
\frac{(K-1)^4}{p}
+
O\!\left(K^{2+o(1)}\right),
$$

записан как **BGS-CAYLEY-005 — OPEN**.

Существенная коррекция в этой ветке носила концептуальный характер: требование устранить все exceptional collisions слишком сильное и является неправильной целью. Большие exceptional primes могут сосуществовать лишь с константным excess energy. Правильная цель — centered energy control.

## 4. Return laws и Pell regimes

Проект доказывает глобальные spectral/observable laws на явных арифметических подпоследовательностях.

**BGS-RET-001** — harmonic return law для фактического kicked Pell propagator при фиксированной multiplicity и логарифмическом return time.

**BGS-RET-002** — harmonic-scale global transition для compressed observables в fixed Pell cat map.

Это строгие результаты, но их временной масштаб не является Heisenberg time.

## 5. Clustered Abel statistics и falsifiers

**BGS-TRACE-006** даёт два взаимодополняющих утверждения.

Во-первых, достаточно узкая кластеризация спектра заставляет расходиться Abel-type statistic.

Во-вторых, существуют явные **простые спектры** с такой же clustering/Abel divergence, но их positive-time form factor стремится к нулю равномерно на каждом окне

$$
m\in[aN,bN],
\qquad
0<a<b.
$$

Следовательно, кластеризация сама по себе не может быть недостающим механизмом BGS.

---

# Что уже исключено

В этом репозитории отрицательные результаты рассматриваются как полноценный научный результат. Несколько естественных стратегий уже доказанно недостаточны.

### Конечные моменты недостаточны

Два спектра могут совпадать по длинному начальному диапазону следов и при этом иметь различную microscopic pair statistic.

### Одной Fourier bandwidth недостаточно

Совпадение на одной фиксированной compact support не влечёт full Schwartz convergence. Bandlimit должен проходить через exhaustion по всем компактам.

### One-sided или same-half-plane loop equations недостаточны

Некоторые loop residuals тождественно исчезают для любого спектра; локальную информацию несут только действительно mixed orientations.

### Low-order loop identities недостаточны

Явные repeated-clock spectra могут удовлетворять существенным конечным наборам тождеств, не приближаясь к CUE point process.

### Global return laws недостаточны

Логарифмические или harmonic return distributions могут быть вычислены точно, в то время как microscopic spectrum остаётся неопределённым.

### Finite random-matrix resemblance недостаточно

Численные гистограммы полезны как diagnostics и falsification tools, но не являются asymptotic local theorem.

### Classical nondegeneracy недостаточна

Даже сильный classical Riesz gap не превращается автоматически в quantum trace cancellation при $m=\Theta(N)$.

Постоянный журнал исправлений находится в [record/retractions.md](record/retractions.md), а компактный reader-facing индекс — в [ERRATA.md](ERRATA.md).

---

# Главный открытый фронтир

Прямой bottleneck fixed-map программы — **BGS-TRACE-005**:

> доказать правильно desymmetrized weighted Heisenberg-scale joint-trace comparison или аналитически эквивалентную mixed-resolvent hierarchy для фактического frozen propagator, равномерно на каждой компактной Fourier support.

Для парного функционала желаемое утверждение схематически имеет вид

$$
\frac{1}{N^2}
\sum_{m\in\mathbb Z}
w(m/N)
\left[
|\operatorname{Tr}U_N^m|^2
-
\mathbb E_{\mathrm{RMT}}
|\operatorname{Tr}V_N^m|^2
\right]
\longrightarrow0,
$$

для подходящего класса compactly supported weights $w$ и **правильного** random-matrix symmetry class.

Высшие корреляции требуют соответствующих constrained products

$$
\prod_{\nu=1}^r \operatorname{Tr}U_N^{m_\nu}
$$

с Fourier-mode relations, возникающими из partition structure.

Сейчас поддерживаются два эквивалентных исследовательских языка:

1. **прямое joint-trace comparison**;
2. **mixed resolvent / loop hierarchy**, достаточно сильная для получения той же локальной статистики.

Второй язык условно формализован в **BGS-LOOP-001**. Model-specific residual decay остаётся открытой.

---

# Что даст успешное закрытие

Если BGS-TRACE-005 будет доказано в требуемом объёме, в репозитории уже имеется большая часть детерминированной машины для перехода к микроскопическим корреляциям. После этого останется завершить точную работу с symmetry block, unfolding и point-process hypotheses для цели BGS-BGS-001.

Успешная fixed-map theorem даст:

- строгий local random-matrix law для явного детерминированного нелинейного хаотического квантового отображения;
- прозрачный механизм связи долгосрочной детерминированной квантовой динамики с локальной спектральной универсальностью;
- модель, где арифметические возвраты, нелинейные возмущения, классические резонансы и квантовые trace statistics отслеживаются в одной системе;
- воспроизводимый framework для отделения настоящего механизма универсальности от ложных численных или глобальных признаков.

Это **не** будет автоматически доказательством BGS для всех хаотических гамильтонианов и всех типов квантования. Проект принципиально различает глубокую модельную теорему и полную универсальную гипотезу.

---

# Избранные научные графики

Ниже — поддерживаемые project figures. Подписи явно указывают их фактический evidentiary role.

<p align="center">
  <img src="assets/figures/correlation_bandwidth.svg" alt="Clock/dimer counterexample: одна фиксированная Fourier bandwidth не определяет microscopic pair law." width="48%">
  <img src="assets/figures/pell_harmonic_returns.svg" alt="Аналитические second-return limits для kicked Pell cat-map harmonic regime." width="48%">
</p>

**Слева — точный контрпример.** Две спектральные конфигурации могут совпадать на заданной low-frequency band и иметь разные microscopic pair statistics. Именно поэтому BGS-TRACE-004 требует каждую компактную bandwidth, а не одну фиксированную support.

**Справа — аналитический закон возврата.** Для kicked Pell family строго контролируется logarithmic-time return regime. Это теорема о return statistics, а не microscopic BGS theorem.

<p align="center">
  <img src="assets/figures/cayley_trace_gaussian.svg" alt="Конечные распределения Cayley traces по сравнению с Gaussian reference." width="72%">
</p>

**Finite Cayley trace illustration.** Этот график численный/диагностический. Асимптотическая теорема имеет собственный точно указанный арифметический режим; ни finite plot, ни глобальный Gaussian law не влекут локальную спектральную универсальность.

---

# Связь с общей картиной BGS

Репозиторий намеренно консервативен в вопросе области применимости.

Quantum graphs, специальные arithmetic maps, semiclassical trace expansions, random band/unitary ensembles и другие модельные классы дают строгие BGS-type результаты или очень сильные аналоги в специальных условиях. Но такие теоремы не переносятся автоматически на поддерживаемое fixed nonlinear cat-map family.

Аналогично, classical Anosov dynamics, quantum ergodicity, eigenfunction equidistribution и matrix-element statistics тесно связаны с quantum chaos, но логически отличаются от microscopic eigenphase spacing.

Поддерживаемый [литературный обзор](literature/bibliography.md) разделяет:

- результаты, реально используемые как theorem inputs;
- соседнюю литературу для контекста;
- model-specific universality theorems, которые напрямую здесь не применимы;
- claims, для которых гипотезы внешних теорем проверены отдельно.

---

# Репозиторий, проверяемость и публикации

Научное изложение выше — основная входная точка. Остальная структура нужна для того, чтобы каждое серьёзное утверждение можно было проверить.

## Рекомендуемый порядок чтения

1. [Текущие результаты](mathematics/results.md) — индекс теорем и точные области действия.
2. [Открытые обязательства](mathematics/open_questions.md) — нерешённый фронтир.
3. [Trace-to-local-statistics bridge](mathematics/trace_to_local_statistics_bridge.md).
4. [Fixed-map frontier](mathematics/fixed_map_resolvent_frontier.md).
5. [Core claim registry](record/claim_registry.md).
6. [Scientific dependency graph](record/scientific_dependency_graph.md).
7. [Unified manuscript](manuscript/BGS_unified.tex).
8. [Literature map](literature/bibliography.md).
9. [Retractions and corrections](record/retractions.md).

## Иерархия источников истины

Текущий статус контролируется [record/claim_ledger.md](record/claim_ledger.md).

Machine-readable [record/claims.json](record/claims.json) задаёт stable core IDs и cross-layer links, но не может усилить claim ledger. Поддерживаемые математические доказательства находятся в [mathematics/](mathematics/README.md). Внешние load-bearing theorems зафиксированы в [literature/external_dependencies.json](literature/external_dependencies.json).

Formalization, computations, evidence files, README prose и manuscript подчинены текущему claim ledger.

Краткая схема находится в [SOURCE_OF_TRUTH.md](SOURCE_OF_TRUTH.md).

## Воспроизводимость

Сначала запускаются дешёвые fail-closed проверки:

~~~sh
python computations/verification/scientific_registry_audit.py
python computations/verification/repository_audit.py
~~~

Затем maintained Python/C++ verification surface:

~~~sh
python -m pip install -r requirements.txt

cmake -S . -B build/cmake -DCMAKE_BUILD_TYPE=Release
cmake --build build/cmake --parallel

python computations/maintenance/verify_workspace.py \
  --build build/cmake \
  --logs build/verification-logs \
  --output build/workspace-verification.json
~~~

Lean project:

~~~sh
(cd formalization && lake build)
~~~

Generated manuscript sections и canonical manuscript:

~~~sh
python computations/maintenance/sync_return_sections.py --check
python computations/maintenance/sync_finite_orbit_section.py --check
python computations/maintenance/sync_fixed_map_section.py --check
python computations/maintenance/build_unified_manuscript.py \
  --output-dir build/unified-paper
~~~

Полный execution contract: [REPRODUCE_unified.md](REPRODUCE_unified.md) и [environment/runtime-manifest.json](environment/runtime-manifest.json).

## Карта репозитория

| Раздел | Назначение |
|---|---|
| [mathematics/](mathematics/README.md) | Авторитетные формулировки, доказательства, редукции, контрпримеры, открытые вопросы |
| [manuscript/](manuscript/README.md) | Каноническая объединённая исследовательская рукопись |
| [papers/](papers/README.md) | Сфокусированные publication candidate scopes без дублирования proof authority |
| [literature/](literature/bibliography.md) | Граница литературы и theorem-level external dependencies |
| [formalization/](formalization/README.md) | Lean 4 algebraic/finite kernels и явная trust boundary |
| [computations/](computations/README.md) | Exact verification, independent implementations, regressions, diagnostics |
| [evidence/](evidence/provenance.md) | Продвинутые finite certificates, numerical/reference data, execution provenance |
| [record/](record/README.md) | Claim authority, audits, corrections, research history, governance |
| [supplement/fixed_map/](supplement/fixed_map/README.md) | Детальные fixed-map derivations и replayable evidence |
| [assets/](assets/) | Поддерживаемые project figures и README diagrams |

## Публикации и review

Долгосрочная программа собрана в [manuscript/BGS_unified.tex](manuscript/BGS_unified.tex). Сфокусированные paper scopes находятся в [papers/](papers/README.md).

- Citation metadata: [CITATION.cff](CITATION.cff)
- Contribution protocol: [CONTRIBUTING.md](CONTRIBUTING.md)
- Referee protocol: [REVIEWING.md](REVIEWING.md)
- Research roadmap: [ROADMAP.md](ROADMAP.md)
- Release policy: [RELEASES.md](RELEASES.md)

## Авторство и область заявлений

Maintainer и автор рукописи: **Maksim Churilov**.

Этот репозиторий не утверждает:

- доказательство общей гипотезы BGS для всех хаотических систем;
- внешний priority claim на весь корпус;
- независимую referee validation каждой проектной теоремы;
- что numerical resemblance является доказательством;
- что formalized finite kernels покрывают аналитическую BGS-задачу.

Цель проекта — максимально продвинуть конкретную задачу микроскопической универсальности, сохраняя явной границу между доказательством, внешним theorem input, formal/finite verification, numerical evidence, conditional reduction и открытым обязательством.
