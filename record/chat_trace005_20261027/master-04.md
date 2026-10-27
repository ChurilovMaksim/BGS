если в (VIIId.4.2) увеличить порог $N$ так, чтобы каждый $|a_{0,r}+a_{1,r}/N+\rho_{r,N}|$ лежал между $1/2$ и 2. Нижняя граница использует также $|c_r|=1/2$. Поэтому наличие одной такой пары или малого семейства таких пар не даёт заметной нижней границы для нормированного $Y$. Другие ветвевые слагаемые могут иметь любой знак.

Тем самым опровергнут равномерный покомпонентный тезис «все невращательные и неотражательные ветвевые пары осциллируют с растущей частотой». Не доказано, что этот сектор имеет макроскопический вес; не доказано, что он даёт плато; не доказано нарушение закона Sine₂.

#### VIIId.4.2. SP5: вес всего сектора медленных координатных слов исчезает

Оценим вес, прежде чем приписывать построенным фазам спектральное значение. Пусть
$$
\mathcal W_{m,N}(L)=
 \{x:\operatorname{dist}_N(x_{j+1},x_j)\le L
                         \text{ для всех }j\},
$$
где $\operatorname{dist}_N$ — циклическое расстояние. Для $L<N/2$
$$
|\mathcal W_{m,N}(L)|\le N(2L+1)^{m-1}.
$$
Из принятой оценки FM-021, $\max|U_{xy}|^2\le C_0/N$, следует точное неравенство
$$
\sum_{x,y\in\mathcal W_{m,N}(L)}
          |a(x)\overline{a(y)}|
 \le N^2\left(\frac{C_0(2L+1)^2}{N}\right)^m.        \tag{VIIId.4.8}
$$
Действительно, каждое слово имеет не больше $N(2L+1)^{m-1}$ вариантов, а произведение двух амплитуд по модулю не больше $(C_0/N)^m$. Циклическое замыкание только уменьшает число вариантов.

Если $L_N=o(\sqrt N)$, то для любого фиксированного $c_0>0$ правая часть (VIIId.4.8) стремится к нулю равномерно по $c_0N\le m<2N$. Более того, её исходная $w$-взвешенная сумма, делённая на $N^2$, стремится к нулю: она ограничена
$$
2N\|w\|_\infty\,\rho_N^{c_0N},\qquad
 \rho_N=C_0(2L_N+1)^2/N\longrightarrow0.
$$
Никакая компенсация знаков для этого вывода не нужна.

Для слов SP4 при достаточно больших $N$ шаг $x$ не больше 2, а шаг $y$ не больше 4: используем $NL_1/m_N+1\to2\pi a/c+1<2$. Значит, весь построенный сектор входит в (VIIId.4.8) с $L=4$. Точные ветвевые слагаемые также удовлетворяют той же оценке с постоянной 16 после абсолютного суммирования всех ветвей: из (VIIId.4.2), $|c_r|=1/2$ каждое ребро имеет сумму модулей четырёх ветвей не больше $4/\sqrt N$.

**Следствие для проверяемого механизма.** Сам набор почти совпадающих фаз SP4 не может дать требуемую отрицательную поправку. При добавлении поперечных отклонений координат $o(N^{-1/2})$ шаги по-прежнему равны $o(\sqrt N)$, и (VIIId.4.8) всё ещё применимо. Первое пространство, для которого эта оценка перестаёт давать общий ответ, имеет поперечную ширину порядка $N^{-1/2}$ и шаги порядка $\sqrt N$. Это указание масштаба оставшегося расчёта; не доказательство ненулевого вклада на нём.

### VIIId.5. Самопроверка, статусы и продолжение

**ДОКАЗАНО:** SP1 — точный гессиан и малая ненулевая мода; SP2 — коллективное действие с остатком $C/m^2$; SP3 — контролируемое округление и исключение диэдральных совпадений; SP4 — почти совпадающие фазы некоторых точных ветвевых слагаемых исходной семьи при исходном $\tau$, с любым заданным $m_N/N\to c\in(0,2)$; SP5 — исчезающий вес всего сектора шагов $o(\sqrt N)$.

**OUTLINE:** после прямого локального пересуммирования остаётся отдельная коллективная интеграция по малым модам и суммирование по перестановкам. Полученное одномерное действие можно локально сделать квадратичным заменой координаты. Это не определяет меру интегрирования, поперечный определитель, комбинаторный вес или суммарную ошибку.

**НЕДОКАЗАНО:**

- U-SP1: оценить поперечную область ширины порядка $N^{-1/2}$ и полный вес остальных когерентных секторов после суммирования всех ветвей, перестановок, повторений и арифметических классов, с $o(N^2)$-ошибкой после исходного взвешивания.
- U-SP2: получить именно отрицательную поправку $-\delta_*$, а не положительный вклад или исчезновение отдельных классов.
- U-SP3: доказать достаточные тесты всех фиксированных порядков либо непосредственно ограниченный Laplace-закон.

Самое трудное место здесь — не вычисление гессиана. Оно состоит в весе коллективных конфигураций внутри полной знаковой суммы. Невырожденность каждого отдельного цикла и даже её экспоненциальная локальность не сохраняются после вычитания переставленных циклов. Вместе с тем решение этого локального препятствия ещё не дало бы необходимую компенсацию всех секторов.

Маршрут не объявляется исчерпанным. Простое перенесение щели отвергнуто; вклад одних медленных слов закрыт оценкой SP5. Пересуммирование с отдельной обработкой поперечных флуктуаций критической ширины остаётся открытым. Следующий содержательный шаг должен оценивать их полный вес и остаток, а не повторять вычисление уже известной фазы.

Конечные проверки: Wolfram независимо вывел (VIIId.1.2) для произвольной функции $S$ при $m=5,7,9,11$ и подтвердил ведущие коэффициенты (VIIId.1.4),(VIIId.2.2). Дополнительные нулевые моды при $m=9$ отдельно проверены Python. Ядро: 15.0.1, Linux x86-64. Первая отправка содержала синтаксическую ошибку; промежуточный вариант с вычислением предела выдал предупреждение, хотя вернул правильные выражения. Финальный вариант использует Taylor-коэффициент и завершился без сообщений. Сохранены точные входы и все три ответа.

Python отдельно проверяет Fourier-нормировки и знак гессиана, три нелинейные контрольные фазы, коэффициент $3/2$, ориентированный член $m^{-2}$ и невращательный характер округлённого слова. Контрольные фазы не подменяют исходный $S_r$; исходное положительное время покрыто аналитическим доказательством. Первый тест сырого коэффициента при $m=513$ использовал слишком строгий порог до устранения его ошибки $O(m^{-1})$; это диагностировано, финальная проверка использует явно приведённую экстраполяцию. Предел и SP1–SP4 доказываются текстом, а не результатами запуска.

Проверка доказательства выполнена автором отдельно после вывода: знаки двух циклов, множитель $2\pi N$, нечётность $m$, случай $3\mid m$, ненулевая мода $k=1$, ошибка округления, различие ветвевого и полного слова, накопление фазовой ошибки за $m$ шагов, подсчёт веса медленных слов и сохранение всех четырёх ветвей проверены явно. Независимого рецензирования не было. Новизна относительно литературы не устанавливалась.

Полные входы и результаты вычисления приведены ниже как воспроизводимый конечный протокол.

#### VIIId.5.1. Финальный символьный вход

```wolfram
ClearAll[f, x, q, b, a, m];
hessianChecks = Table[Module[{vars, u, phase, h, adj, target},
  vars = Array[x, mm];
  u[j_] := vars[[1 + Mod[j-1,mm]]];
  phase = Sum[f[u[j],u[j+1]] - f[u[j],u[j+2]], {j,mm}];
  h = Table[D[phase,vars[[j]],vars[[k]]],{j,mm},{k,mm}] /. Thread[vars -> q];
  adj[s_] := Table[Boole[Mod[k-j,mm] == s] + Boole[Mod[k-j,mm] == mm-s], {j,mm},{k,mm}];
  target = Derivative[1,1][f][q,q] (adj[1] - adj[2]);
  <|"m" -> mm, "hessianIdentity" -> TrueQ[Simplify[h == target]],
    "constantKernel" -> TrueQ[Simplify[h.ConstantArray[1,mm] == ConstantArray[0,mm]]]|>
],{mm,{5,7,9,11}}];
coefficientCheck = FullSimplify[
  -3/2 (f2 acc + f22 vel^2) + 3/2 ((f12+f22) vel^2 + f2 acc)
    == 3/2 f12 vel^2];
softLimit = Coefficient[Normal[Series[(Cos[2 Pi z]-Cos[4 Pi z])/2,{z,0,2}]],z,2];
lambdaLimit = 4 b softLimit;
<|"kernelVersion" -> $Version, "systemID" -> $SystemID, "hessians" -> hessianChecks, "integrationByPartsCoefficient" -> coefficientCheck,
  "quadraticProfileLimit" -> softLimit, "hessianEigenvalueLimit" -> lambdaLimit|>
```

#### VIIId.5.2. Все символьные вызовы, включая диагностические ошибки

```json
{
  "purpose": "Illustrative symbolic verification of SP1/SP2 only; not an asymptotic proof",
  "calls": [
    {
      "status": "syntax-error",
      "code": "\nClearAll[f, x, q, b, a, m, z];\nhessianChecks = Table[\n  vars = Array[x, mm];\n  cyc[j_] := 1 + Mod[j - 1, mm];\n  phase = Sum[f[vars[[j]], vars[[cyc[j + 1]]]]] - f[vars[[j]], vars[[cyc[j + 2]]]]], {j, mm}];\n  h = Table[D[phase, vars[[j]], vars[[k]]], {j, mm}, {k, mm}] /. Thread[vars -> q];\n  adj[s_] := Table[Boole[Mod[k-j,mm] == s] + Boole[Mod[k-j,mm] == mm-s], {j,mm}, {k,mm}];\n  target = Derivative[1,1][f][q,q] (adj[1] - adj[2]);\n  <|\"m\" -> mm, \"hessianIdentity\" -> TrueQ[Simplify[h == target]],\n    \"constantKernel\" -> TrueQ[Simplify[h.ConstantArray[1,mm] == ConstantArray[0,mm]]]|>,\n  {mm, {5,7,9,11}}];\ncoefficientCheck = FullSimplify[\n  -3/2 (f2 acc + f22 vel^2) + 3/2 ((f12+f22) vel^2 + f2 acc)\n     == 3/2 f12 vel^2];\nsoftLimit = Limit[m^2/2 (Cos[2 Pi/m] - Cos[4 Pi/m]), m -> Infinity];\nlambdaLimit = Limit[2 b m^2 (Cos[2 Pi/m] - Cos[4 Pi/m]), m -> Infinity];\n<|\"hessians\" -> hessianChecks, \"integrationByPartsCoefficient\" -> coefficientCheck,\n  \"quadraticProfileLimit\" -> softLimit, \"hessianEigenvalueLimit\" -> lambdaLimit|>\n",
      "result": {
        "content": [
          {
            "type": "text",
            "text": "ToExpression::sntx: Invalid syntax in or before \"phase = Sum[f[vars[[j] ...                     ^\".\"\\n\"\nGeneral::messages: Messages were generated which may indicate errors.\n\nOut[1]= $Failed"
          }
        ],
        "structuredContent": null,
        "isError": false
      }
    },
    {
      "status": "returned-result-with-warning",
      "code": "\nClearAll[f, x, q, b, a, m];\nhessianChecks = Table[Module[{vars, u, phase, h, adj, target},\n  vars = Array[x, mm];\n  u[j_] := vars[[1 + Mod[j-1,mm]]];\n  phase = Sum[f[u[j],u[j+1]] - f[u[j],u[j+2]], {j,mm}];\n  h = Table[D[phase,vars[[j]],vars[[k]]],{j,mm},{k,mm}] /. Thread[vars -> q];\n  adj[s_] := Table[Boole[Mod[k-j,mm] == s] + Boole[Mod[k-j,mm] == mm-s], {j,mm},{k,mm}];\n  target = Derivative[1,1][f][q,q] (adj[1] - adj[2]);\n  <|\"m\" -> mm, \"hessianIdentity\" -> TrueQ[Simplify[h == target]],\n    \"constantKernel\" -> TrueQ[Simplify[h.ConstantArray[1,mm] == ConstantArray[0,mm]]]|>\n],{mm,{5,7,9,11}}];\ncoefficientCheck = FullSimplify[\n  -3/2 (f2 acc + f22 vel^2) + 3/2 ((f12+f22) vel^2 + f2 acc)\n    == 3/2 f12 vel^2];\nsoftLimit = Limit[m^2/2 (Cos[2 Pi/m] - Cos[4 Pi/m]), m -> Infinity];\nlambdaLimit = Limit[2 b m^2 (Cos[2 Pi/m] - Cos[4 Pi/m]), m -> Infinity];\n<|\"hessians\" -> hessianChecks, \"integrationByPartsCoefficient\" -> coefficientCheck,\n  \"quadraticProfileLimit\" -> softLimit, \"hessianEigenvalueLimit\" -> lambdaLimit|>\n",
      "result": {
        "content": [
          {
            "type": "text",
            "text": "Infinity::indet: -- Message text not found -- (0*Infinity)\nGeneral::messages: Messages were generated which may indicate errors.\n\nOut[1]= <|\"hessians\" -> {<|\"m\" -> 5, \"hessianIdentity\" -> True, \"constantKernel\" -> True|>, <|\"m\" -> 7, \"hessianIdentity\" -> True, \"constantKernel\" -> True|>, <|\"m\" -> 9, \"hessianIdentity\" -> True, \"constantKernel\" -> True|>, <|\"m\" -> 11, \"hessianIdentity\" -> True, \"constantKernel\" -> True|>}, \"integrationByPartsCoefficient\" -> True, \"quadraticProfileLimit\" -> 3*Pi^2, \"hessianEigenvalueLimit\" -> 12*b*Pi^2|>"
          }
        ],
        "structuredContent": null,
        "isError": false
      }
    },
    {
      "status": "completed-without-reported-warning",
      "code": "\nClearAll[f, x, q, b, a, m];\nhessianChecks = Table[Module[{vars, u, phase, h, adj, target},\n  vars = Array[x, mm];\n  u[j_] := vars[[1 + Mod[j-1,mm]]];\n  phase = Sum[f[u[j],u[j+1]] - f[u[j],u[j+2]], {j,mm}];\n  h = Table[D[phase,vars[[j]],vars[[k]]],{j,mm},{k,mm}] /. Thread[vars -> q];\n  adj[s_] := Table[Boole[Mod[k-j,mm] == s] + Boole[Mod[k-j,mm] == mm-s], {j,mm},{k,mm}];\n  target = Derivative[1,1][f][q,q] (adj[1] - adj[2]);\n  <|\"m\" -> mm, \"hessianIdentity\" -> TrueQ[Simplify[h == target]],\n    \"constantKernel\" -> TrueQ[Simplify[h.ConstantArray[1,mm] == ConstantArray[0,mm]]]|>\n],{mm,{5,7,9,11}}];\ncoefficientCheck = FullSimplify[\n  -3/2 (f2 acc + f22 vel^2) + 3/2 ((f12+f22) vel^2 + f2 acc)\n    == 3/2 f12 vel^2];\nsoftLimit = Coefficient[Normal[Series[(Cos[2 Pi z]-Cos[4 Pi z])/2,{z,0,2}]],z,2];\nlambdaLimit = 4 b softLimit;\n<|\"kernelVersion\" -> $Version, \"systemID\" -> $SystemID, \"hessians\" -> hessianChecks, \"integrationByPartsCoefficient\" -> coefficientCheck,\n  \"quadraticProfileLimit\" -> softLimit, \"hessianEigenvalueLimit\" -> lambdaLimit|>\n",
      "result": {
        "content": [
          {
            "type": "text",
            "text": "Out[1]= <|\"kernelVersion\" -> \"15.0.1 for Linux x86 (64-bit) (July 2, 2026)\", \"systemID\" -> \"Linux-x86-64\", \"hessians\" -> {<|\"m\" -> 5, \"hessianIdentity\" -> True, \"constantKernel\" -> True|>, <|\"m\" -> 7, \"hessianIdentity\" -> True, \"constantKernel\" -> True|>, <|\"m\" -> 9, \"hessianIdentity\" -> True, \"constantKernel\" -> True|>, <|\"m\" -> 11, \"hessianIdentity\" -> True, \"constantKernel\" -> True|>}, \"integrationByPartsCoefficient\" -> True, \"quadraticProfileLimit\" -> 3*Pi^2, \"hessianEigenvalueLimit\" -> 12*b*Pi^2|>"
          }
        ],
        "structuredContent": null,
        "isError": false
      }
    }
  ],
  "interpretation": "The final exact Hessian identities are finite fixtures; the universal statements have separate proofs."
}
```

#### VIIId.5.3. Конечные Python-результаты

```json
{
  "assertion_tested": "Finite Fourier/Hessian normalizations; nonlinear continuum phase fixture; nonrotation witness after rounding.",
  "coefficient_domain": "complex128, float64; exact symbolic identities separately checked with Wolfram",
  "software": [
    {
      "name": "Python",
      "version": "3.12.14"
    },
    {
      "name": "NumPy",
      "version": "2.3.5"
    },
    {
      "name": "SciPy",
      "version": "1.17.0"
    }
  ],
  "eigen_checks": [
    {
      "m": 5,
      "max_fourier_error": 3.855927796350635e-16,
      "nullity": 1,
      "m_squared_soft_eigenvalue": 13.975424859373685
    },
    {
      "m": 7,
      "max_fourier_error": 1.6401643046719713e-15,
      "nullity": 1,
      "m_squared_soft_eigenvalue": 20.727263027468673
    },
    {
      "m": 9,
      "max_fourier_error": 3.0161768325659466e-15,
      "nullity": 3,
      "m_squared_soft_eigenvalue": 23.99204875080793
    },
    {
      "m": 11,
      "max_fourier_error": 5.925149092659698e-15,
      "nullity": 1,
      "m_squared_soft_eigenvalue": 25.76323044967233
    }
  ],
  "continuum_checks": [
    {
      "epsilon": 0.0,
      "eta": 0.058823529411764705,
      "energy": 0.010738129588385222,
      "quadrature_reported_error": 1.1921962496998982e-16,
      "rows": [
        {
          "m": 9,
          "phase": 0.001252961550528326,
          "m_phase": 0.011276653954754934,
          "target": 0.016107194382577832,
          "m_squared_remainder": -0.04347486385040609,
          "next_coefficient": 0.0009141729766759523
        },
        {
          "m": 33,
          "phase": 0.0004758598421509492,
          "m_phase": 0.015703374790981325,
          "target": 0.016107194382577832,
          "m_squared_remainder": -0.0133260465226848,
          "next_coefficient": 0.0009141729766759523
        },
        {
          "m": 129,
          "phase": 0.00012469552942549083,
          "m_phase": 0.016085723295888317,
          "target": 0.016107194382577832,
          "m_squared_remainder": -0.002769770182947223,
          "next_coefficient": 0.0009141729766759523
        },
        {
          "m": 513,
          "phase": 3.139799206114229e-05,
          "m_phase": 0.016107169927365998,
          "target": 0.016107194382577832,
          "m_squared_remainder": -1.2545523672989577e-05,
          "next_coefficient": 0.0009141729766759523
        }
      ],
      "extrapolated_second_coefficient": 0.0009137096353019482
    },
    {
      "epsilon": 0.003,
      "eta": 0.058823529411764705,
      "energy": 0.012509983146334157,
      "quadrature_reported_error": 1.389011856077145e-16,
      "rows": [
        {
          "m": 9,
          "phase": 0.001478608095859786,
          "m_phase": 0.013307472862738074,
          "target": 0.018764974719501237,
          "m_squared_remainder": -0.049117516710868454,
          "next_coefficient": 0.003805373202019673
        },
        {
          "m": 33,
          "phase": 0.0005568301566997813,
          "m_phase": 0.018375395171092785,
          "target": 0.018764974719501237,
          "m_squared_remainder": -0.012856125097478913,
          "next_coefficient": 0.003805373202019673
        },
        {
          "m": 129,
          "phase": 0.00014543592037647308,
          "m_phase": 0.018761233728565026,
          "target": 0.018764974719501237,
          "m_squared_remainder": -0.00048258783077100985,
          "next_coefficient": 0.003805373202019673
        },
        {
          "m": 513,
          "phase": 3.6589264528633364e-05,
          "m_phase": 0.018770292703188914,
          "target": 0.018764974719501237,
          "m_squared_remainder": 0.0027281256317793433,
          "next_coefficient": 0.003805373202019673
        }
      ],
      "extrapolated_second_coefficient": 0.003806724685604852
    },
    {
      "epsilon": -0.003,
      "eta": 0.058823529411764705,
      "energy": 0.008966276030436288,
      "quadrature_reported_error": 1.1286686963017764e-16,
      "rows": [
        {
          "m": 9,
          "phase": 0.001027315005196866,
          "m_phase": 0.009245835046771794,
          "target": 0.013449414045654431,
          "m_squared_remainder": -0.037832210989943736,
          "next_coefficient": -0.0019770272486677684
        },
        {
          "m": 33,
          "phase": 0.00039488952760211704,
          "m_phase": 0.013031354410869863,
          "target": 0.013449414045654431,
          "m_squared_remainder": -0.013795967947890803,
          "next_coefficient": -0.0019770272486677684
        },
        {
          "m": 129,
          "phase": 0.00010395513847450861,
          "m_phase": 0.013410212863211611,
          "target": 0.013449414045654431,
          "m_squared_remainder": -0.005056952535123886,
          "next_coefficient": -0.0019770272486677684
        },
        {
          "m": 513,
          "phase": 2.620671959365122e-05,
          "m_phase": 0.013444047151543076,
          "target": 0.013449414045654431,
          "m_squared_remainder": -0.0027532166791253226,
          "next_coefficient": -0.0019770272486677684
        }
      ],
      "extrapolated_second_coefficient": -0.001979305415000805
    }
  ],
  "rounding_fixture": {
    "m": 101,
    "N": 100003,
    "original_first_harmonic": 0.010000428453586284,
    "permuted_first_harmonic": 2.7631778155337104e-07
  },
  "non_claims": [
    "The nonlinear fixture is not the original U_N or its phase S_t.",
    "No finite computation at actual tau=10^-80.",
    "No contribution estimate for the full coherent sum.",
    "No proof or refutation of Sine_2 or of the full pair moment."
  ],
  "development_note": "A first raw m=513 coefficient test used an unjustified 2e-4 tolerance before removing its O(1/m) term and failed. The final test uses the displayed Richardson extrapolation; the mathematical claim was not changed.",
  "script_sha256": "3894f303b51817710f52ecf0abf903d5fc340605e9a8b0f6afb2aecba17cc015"
}
```

#### VIIId.5.4. Протокол запуска

```json
{
  "schema_version": 2,
  "claim_id": "TRACE005-PAIRED-SOFT-MODES-20261026",
  "repository": {
    "commit": "unavailable; standalone research artifacts",
    "dirty": true,
    "dirty_semantics": "New unversioned files in shared workspace; Git status not inspected"
  },
  "command": [
    "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python3",
    "/workspace/scratch/980ff7770509/output/trace005_soft_modes_verify.py",
    "--output",
    "/workspace/scratch/980ff7770509/output/trace005_soft_modes_checks.json"
  ],
  "environment": {
    "software": [
      {
        "name": "Python",
        "version": "3.12.14"
      },
      {
        "name": "NumPy",
        "version": "2.3.5"
      },
      {
        "name": "SciPy",
        "version": "1.17.0"
      }
    ],
    "hardware": "x86_64"
  },
  "mathematics": {
    "assertion_tested": "Finite Fourier/Hessian normalizations; nonlinear continuum phase fixture; nonrotation witness after rounding.",
    "coefficient_domain": "complex128, float64; exact symbolic identities separately checked with Wolfram",
    "conventions": "Cyclic steps +1,+2; phase S(q_j,q_j+1)-S(q_j,q_j+2); Fourier exp(2*pi*i*k*j/m)",
    "inputs": [
      "Fixed polynomial/trigonometric phase fixture and rounded cosine profile, as defined in script"
    ],
    "bounds": {
      "hessian_m": [
        5,
        7,
        9,
        11
      ],
      "continuum_m": [
        9,
        33,
        129,
        513
      ],
      "epsilon": [
        0,
        0.003,
        -0.003
      ],
      "rounding_m": 101,
      "rounding_N": 100003,
      "coefficient_tolerance": 2e-05
    },
    "non_claims": [
      "The nonlinear fixture is not the original U_N or its phase S_t.",
      "No finite computation at actual tau=10^-80.",
      "No contribution estimate for the full coherent sum.",
      "No proof or refutation of Sine_2 or of the full pair moment."
    ]
  },
  "randomness": {
    "used": false,
    "generator": "",
    "seed": null
  },
  "run": {
    "started_at": "2026-10-26T06:17:46.997700+00:00",
    "runtime_seconds": 5.051177997000195,
    "status": "completed",
    "exit_status": 0,
    "resource_limits": {
      "wall_seconds": 30,
      "memory_bytes": null,
      "cpu_seconds": null,
      "max_cores": null,
      "max_threads": null
    }
  },
  "outputs": [
    {
      "path": "output/trace005_soft_modes_checks.json",
      "sha256": "938a3758fc1336ad94a887eb417579d3ca56c6254ea63aeb5f8e5eaa767b85f0",
      "kind": "result"
    }
  ],
  "checks": [
    "All Fourier modes in four dimensions, including m divisible by 3",
    "Wrong-sign and wrong-factor negative fixtures",
    "Three nonlinear phases with independent quadrature and third-order coefficient",
    "Fourier nonrotation witness after rounding"
  ],
  "result": "Finite assertions passed; SP1-SP4 are separately proved in text.",
  "residual_risks": [
    "Floating fixtures are not interval certified",
    "Self-review only",
    "No microscopic moment estimate or full local law",
    "No Git revision available"
  ],
  "input_artifacts": [
    {
      "path": "output/trace005_soft_modes_verify.py",
      "sha256": "3894f303b51817710f52ecf0abf903d5fc340605e9a8b0f6afb2aecba17cc015",
      "sha256_after": "3894f303b51817710f52ecf0abf903d5fc340605e9a8b0f6afb2aecba17cc015"
    }
  ],
  "declared_results": [
    "output/trace005_soft_modes_checks.json"
  ]
}
```

Команда воспроизведения после сохранения скрипта из приложения XI.9:

```bash
python3 trace005_soft_modes_verify.py --output trace005_soft_modes_checks.json
```


## VIIIe. Критическое гауссово взвешивание и его точные ограничения

### VIIIe.1. Определения и точное утверждение CG1

Пусть
$$
D_N=\sum_{\ell\in\mathbb Z}e^{-\ell^2N/2},\qquad
 g_N(n)=D_N^{-1}\sum_{\ell\in\mathbb Z}
               e^{-(n+\ell N)^2/(2N)} .
$$
Это $N$-периодический вещественный вес, $g_N(0)=1$. Положим
$$
B_N(t)_{xy}=g_N(x-y)U_N(t)_{xy},\qquad
                         0\le t\le\eta=10^{-6}.       \tag{VIIIe.1.1}
$$
Используем точные четыре ветви и нормировку I1:
$$
U_N(t)_{xy}=\frac1{\sqrt N}\sum_{r=0}^3
 c_{\nu_N,r}(y)a_r(x/N,y/N,t)e^{2\pi iNS_r(x/N,y/N,t)}
                  +R_N(x,y,t),                       \tag{VIIIe.1.2}
$$
где аргументы фаз являются двумя координатами ядра,
$$
|R_N(x,y,t)|\le E N^{-3/2},\quad E=10^{60},\quad
 a_r=a_{0,r}>0,\quad a_r^2=4b_r,\quad b_r=S_{r,12},
$$
$$
\frac15<b_r<\frac13,\qquad |b_r-1/4|\le700t,           \tag{VIIIe.1.3}
$$
$$
|S_{r,1}(q,q,t)+q/2-r/4|\le22t,\quad
 |S_{r,2}(q,q,t)+q/2|\le11t.                           \tag{VIIIe.1.4}
$$
Все эти свойства, кроме более удобной числовой версии $|b_r-1/4|\le700t$, уже доказаны в I1. Для неё из вариационного уравнения
$$
|J_r-1|\le\tfrac74(e^{1300t}-1)\le2600t,\quad
 J_r\ge0.998,\quad b_r=(4J_r)^{-1}
$$
получаем $|b_r-1/4|<652t<700t$. Оценки действуют также в локальных подъёмах координат через край тора. Точное начальное разложение применимо к любым целым представителям индексов; эволюция на четырёхкратном накрытии сохраняет его равенство исходному ядру.

Пусть $H\ge1$ ограничивает все $C^3$-нормы $S_r$ и $C^1$-нормы $a_r$ на $[-1,2]^2$, $0\le t\le\eta$, всех четырёх ветвей. Эти нормы конечны по уже доказанному аналитическому построению, не зависят от $N,m$. Можно увеличить $H$, чтобы включить соседние локальные подъёмы. Введём
$$
\rho(b)=\left(1+\frac1{4\pi^2b^2}\right)^{-1/4},
 \qquad \rho_0=\rho(1/4)
       =\left(1+\frac4{\pi^2}\right)^{-1/4}<0.919.
$$

**CG1.** Существует явно контролируемая константа $C$, не зависящая от $N,t,m$, такая, что
$$
\boxed{\|B_N(t)\|\le\rho_0+5000t+C N^{-1/5}.}          \tag{VIIIe.1.5}
$$
Например, приведённые ниже мажоранты допускают
$$
C=10^{20}(1+E+H)^{10}.           \tag{VIIIe.1.6}
$$
Неравенство $\rho_0<0.919$ также имеет рациональную проверку: для границы $p_U>\pi$ из CG4 выполнено $(919/1000)^4(1+4/p_U^2)>1$. Оценка равномерна по всем нечётным $N\ge3$, $0\le t\le\eta$. Её правая часть может быть больше 1; утверждение о строгом сжатии используется только при достаточно малом фиксированном времени. В частности, при исходном $t=\tau=10^{-80}$, для всех достаточно больших нечётных $N$
$$
\|B_N(\tau)\|\le0.95.        \tag{VIIIe.1.7}
$$
Достаточно увеличить $N$ до $(100C)^5$. Это не эффективный вычислительный порог, но он конечен и не зависит от длины слова.

### VIIIe.2. Доказательство CG1 без многомерной стационарной фазы

#### VIIIe.2.1. Гауссовы суммы и принцип нормировки

Для $\operatorname{Re}a>0$
$$
\int_{\mathbb R}e^{-au^2-2\pi i\xi u}\,du
       =\sqrt{\frac\pi a}\,e^{-\pi^2\xi^2/a}.         \tag{VIIIe.2.1}
$$
Доказательство не использует внешнюю формулу: интегрирование по частям даёт дифференциальное уравнение по $\xi$; значение при нуле для положительного вещественного $a$ вычисляется возведением интеграла в квадрат и полярными координатами. Голоморфность обеих сторон в правой полуплоскости, из доминированного дифференцирования под интегралом, продолжает равенство на указанные $a$.

Разложение периодизации гауссианы в ряд Fourier следует непосредственно из вычисления её коэффициентов по (VIIIe.2.1). Ряды и преобразованные ряды абсолютно сходятся. В частности, для $h=4/\sqrt N$, $1/5\le b\le1/3$, оператор свёртки на $\ell^2(\mathbb Z)$ с ядром
$$
k_{b,N}(j)=h\sqrt b\,
                  e^{-(1/2+i\pi b)(hj)^2}
$$
имеет Fourier-множитель
$$
\sqrt{\frac{\pi b}{1/2+i\pi b}}\,
 \sum_{\ell\in\mathbb Z}
 \exp\left\{-\frac{(\omega+2\pi\ell)^2}
                 {4(1/2+i\pi b)h^2}\right\},
 \quad -\pi\le\omega\le\pi .
$$
Член ближайшего изображения по модулю не больше $\rho(b)$.
Для остальных $|\omega+2\pi\ell|\ge(2|\ell|-1)\pi$ и
$$
\operatorname{Re}\frac1{4(1/2+i\pi b)}
 =\frac{1/2}{4(1/4+\pi^2b^2)}>\frac1{12}.
$$
Следовательно, при $N\ge100$
$$
\|k_{b,N}*\|\le\rho(b)(1+4e^{-N/100}).               \tag{VIIIe.2.2}
$$
Норма свёртки здесь равна супремуму модуля Fourier-множителя: равенство Парсеваля сначала проверяется на конечных последовательностях, затем по плотности. Верхняя оценка достаточна для дальнейшего доказательства; изображения не отбрасываются.

#### VIIIe.2.2. Все четыре арифметические ветви дают унитарные рамки

Положим $C_\nu=(c_{\nu,r}(s))_{0\le r,s<4}$, где $\nu$ нечётно. Тогда $C_\nu$ унитарна. Действительно,
$$
c_{\nu,r}(s)=\frac14\sum_{x=0}^3
 e^{-2\pi i\nu(3x^2-2xs+3s^2)/8}e^{-2\pi irx/4}.
$$
Первая Fourier-матрица с нормировкой $1/2$ унитарна. Вторая матрица с элементами
$\tfrac12 e^{-2\pi i\nu(3x^2-2xs+3s^2)/8}$ также унитарна: скалярное произведение двух её столбцов содержит
$\sum_{x=0}^3 e^{2\pi i\nu x(s-t)/4}=0$ при $s\ne t$.
Их произведение равно $C_\nu$.

Для фиксированной точки $q_0$ определим две $4\times4$ матрицы
$$
F_{sr}=\tfrac12 e^{2\pi isS_{r,1}(q_0,q_0,t)},\qquad
 C_{rs}=c_{\nu,r}(s)e^{2\pi isS_{r,2}(q_0,q_0,t)}.
$$
При $t=0$ они унитарны: первая есть четырёхточечная Fourier-матрица с диагональной фазой, вторая — $C_\nu$ с диагональной фазой. Из (VIIIe.1.4), $|e^{iu}-e^{iv}|\le|u-v|$ и оценки нормы $4\times4$ матрицы через четыре максимальных модуля элемента получаем
$$
\|F\|\le1+1000t,\qquad
                  \|C\|\le1+500t.                   \tag{VIIIe.2.3}
$$
Эти оценки равномерны по $\nu=1,3,5,7$, положению точки и времени. Термин «рамка» здесь означает только эти конечномерные матрицы; никакая новая вероятностная модель не вводится.

#### VIIIe.2.3. Локальная квадратичная модель на промежуточном масштабе

Возьмём $J=\lceil N^{2/5}\rceil$, $\delta=J^{-1}$. Сначала вход поддержан в $|q-q_0|\le\delta$. Маска $g_N$ делает выход за пределы $|q-q_0|\le2\delta$ по норме не больше константы, умноженной на $e^{-N/(8J^2)}$. Это получается суммированием гауссовых хвостов по строкам и столбцам и неравенством
$$
\|K\|\le
 \sqrt{\left(\sup_x\sum_y|K_{xy}|\right)
             \left(\sup_y\sum_x|K_{xy}|\right)}.       \tag{VIIIe.2.4}
$$
Само (VIIIe.2.4) следует из взвешенного неравенства Коши–Буняковского для каждой строки.

В этом локальном квадрате заменяем $S_r$ её Taylor-полиномом степени 2 около $(q_0,q_0)$, а $a_r$ — значением в центре. При увеличении квадрата до $3\delta$ остаток фазы не больше $36H\delta^3$, следовательно ошибка экспоненты не больше $72\pi HN\delta^3$. Амплитудная ошибка не больше $6H\delta$.
Сумма модулей гауссовой маски по одной строке не больше $4\sqrt N$; поэтому (VIIIe.2.4) ограничивает операторную ошибку этих замен числом
$$
10^5H(N/J^3+J^{-1}).            \tag{VIIIe.2.5}
$$
Остаток $R_N$ из (VIIIe.1.2), умноженный на маску, даёт ещё не больше $4E/N$.

Группируем локальные целые индексы по остаткам:
$x=4j+s,\ y=4k+u$, $s,u=0,1,2,3$.
Замена $g_N(4j+s-4k-u)$ на $e^{-16(j-k)^2/(2N)}$ имеет операторную ошибку $O(N^{-1/2})$ с абсолютной константой: по теореме о среднем сдвиг не больше 3 умножается на производную гауссианы, сумма модулей которой после нормировки ограничена константой. Образы периодизации на локальном квадрате дают экспоненциально малую добавку.

В Taylor-полиноме фазы остаточные зависимости от $s,u$, кроме
$sS_{r,1}(q_0,q_0)+uS_{r,2}(q_0,q_0)$, дают по норме не больше
$10^5H(J^{-1}+N^{-1/2})$. Это следует из $|s|,|u|\le3$: смешанные с локальными координатами члены имеют фазу $O(H/J)$, а чисто остаточные — $O(H/N)$.

После этих замен локальная матрица имеет вид
$$
F\,\operatorname{diag}(D_r)\,C, \tag{VIIIe.2.6}
$$
где ядро $D_r$ равно $2a_r(q_0,q_0)/\sqrt N$, умноженному на гауссиану и экспоненту квадратичного полинома в $4j/N,4k/N$. Все ряды можно продолжить нулём за пределы локального окна; ограничения на вход и выход не увеличивают норму.

Левое и правое умножение на диагональные унитарные матрицы превращают квадратичную фазу $D_r$ в
$-\pi b_r[4(j-k)/\sqrt N]^2$. Равенство $a_r/2=\sqrt{b_r}$ показывает, что оставшаяся свёртка — точно $k_{b_r,N}$ из (VIIIe.2.2). Поэтому
$$
\|D_r\|\le\rho(b_r)(1+4e^{-N/100}).                  \tag{VIIIe.2.7}
$$
Именно равенство амплитуды и смешанной производной фазы обеспечивает правильную константу. Один модуль элемента $N^{-1/2}$ такого вывода не дал бы.

Все локальные ошибки (VIIIe.2.5)–(VIIIe.2.7), включая хвосты, ограничены
$$
10^8(1+E+H)^2\bigl(N/J^3+J^{-1}+N^{-1/2}
                                +e^{-N/(8J^2)}\bigr)              \tag{VIIIe.2.8}
$$
для достаточно больших $N$, равномерно по номеру окна. Для меньших $N$ итоговая грубая константа (VIIIe.1.6) покрывает оценку $\|B_N\|\le1$, доказанную ниже.

#### VIIIe.2.4. Суммирование окон без потери их числа

Построим периодическое разбиение единицы:
$\chi_j(q)=\cos(\pi J(q-j/J)/2)$ при расстоянии до $j/J$ не больше $1/J$, нуль вне этого интервала. На каждом промежутке между центрами ровно две функции являются косинусом и синусом одного угла, поэтому
$$
\sum_j\chi_j^2=1,\qquad
 \sum_j|\chi_j(q)-\chi_j(q')|^2
                 \le(\pi J/2)^2\operatorname{dist}(q,q')^2.
                                                               \tag{VIIIe.2.9}
$$
Для последней оценки отображение $q\mapsto(\chi_j(q))_j$ имеет скорость $\pi J/2$ в $\ell^2$ на каждом промежутке; интегрирование вдоль короткой дуги доказывает (VIIIe.2.9), включая точки излома.

Положим $Q_N=B_N^*B_N$. Для достаточно больших $N$ из (VIIIe.1.2) следует $|U_{xy}|\le5/\sqrt N$. Суммируя произведение двух гауссиан по промежуточному индексу, получаем
$$
|(Q_N)_{yz}|\le
   \frac{2000}{\sqrt N}
      e^{-\operatorname{dist}_N(y,z)^2/(8N)}.         \tag{VIIIe.2.10}
$$
Например, $g_N(n)\le3e^{-\operatorname{dist}_N(n,0)^2/(2N)}$.
Для суммы произведений используем одновременно
$d(x,y)^2+d(x,z)^2\ge d(y,z)^2/2$ и
$d(x,y)^2+d(x,z)^2\ge d(x,y)^2$, затем складываем половины этих оценок. Оставшаяся гауссова сумма не больше $5\sqrt N$; константа 2000 больше $25\cdot9\cdot5$.

Ядро
$Q_N-\sum_j\chi_jQ_N\chi_j$ равно
$\tfrac12(Q_N)_{yz}\sum_j(\chi_j(y/N)-\chi_j(z/N))^2$.
Из (VIIIe.2.9),(VIIIe.2.10),(VIIIe.2.4), суммирования второго момента гауссианы
$\sum_d d^2 e^{-d^2/(8N)}\le100N^{3/2}$ следует
$$
\left\|Q_N-\sum_j\chi_jQ_N\chi_j\right\|
                                      \le10^6J^2/N. \tag{VIIIe.2.11}
$$
Поскольку $Q_N$ положителен, локальная оценка (VIIIe.2.6) применяется к каждому $\chi_jf$, а $\sum\|\chi_jf\|^2=\|f\|^2$. Число окон не появляется как множитель ошибки.

Локальные подъёмы через край тора не меняют этого аргумента. В каждом окне выбираются целые представители индексов в одном интервале длины меньше $N$, и используется точная четырёхветвевая формула на накрытии. Все четыре $\nu_N$ и все остатки индексов по модулю 4 уже включены в (VIIIe.2.3). Образ нулевого продолжения в каждом классе остатков изометричен; никакой делимости $N$ на 4 не требуется.

Из (VIIIe.2.3),(VIIIe.2.7),(VIIIe.2.8),(VIIIe.2.11), $J\asymp N^{2/5}$, получаем
$$
\|B_N(t)\|\le
 (1+1000t)(1+500t)\max_{r,q}\rho(b_r(q,q,t))
                                  +C N^{-1/5}.      \tag{VIIIe.2.12}
$$
В (VIIIe.2.8) экспоненциальный хвост также ограничен константой, умноженной на $N^{-1/5}$. Например,
$N^{1/5}e^{-N/(8J^2)}$ ограничен абсолютной константой, так как $J\le2N^{2/5}$.

Для $1/5\le b\le1/3$
$$
0\le\rho'(b)=\frac{\rho(b)}{2b(1+4\pi^2b^2)}<3.
$$
По (VIIIe.1.3), $\rho(b_r)\le\rho_0+2100t$; по (VIIIe.2.3) произведение норм рамок не больше $1+1501t$ при $t\le\eta$. Поскольку $\rho(b)\le1$, правая часть (VIIIe.2.12) не больше
$\rho_0+3601t+CN^{-1/5}$, что сильнее (VIIIe.1.5).
Выбор (VIIIe.1.6) заведомо покрывает константы (VIIIe.2.5),(VIIIe.2.8),(VIIIe.2.11), гауссовы хвосты, взятие квадратного корня после (VIIIe.2.11) и начальный диапазон $N$, где отдельные оценки ещё не использовались.

Наконец, $\|B_N\|\le1$ для каждого $N$: Fourier-коэффициенты $g_N$ неотрицательны по (VIIIe.2.1), а их сумма равна $g_N(0)=1$. Поэтому $B_N$ есть точная выпуклая комбинация матриц $Z^\ell U_N Z^{-\ell}$, где $Z_{xx}=e_N(x)$. Это только алгебраическое тождество для заданного веса, не рандомизация исходной задачи.

### VIIIe.3. CG2: весь гауссово взвешенный знаковый сектор оценён

Теперь $t=\tau$, все константы фиксированы. Для слова $x$ положим
$$
a_B(x)=a_U(x)\prod_{j=0}^{m-1}g_N(x_j-x_{j+1}).
$$
Это точное произведение элементов $B_N$. Определим $D^B,Y^B$ той же конечной группировкой, что в исходной задаче. Тогда
$$
|\operatorname{Tr}B_N^m|^2=D^B_{m,N}+Y^B_{m,N}
$$
точно; $D^B\ge0$, но $Y^B$ имеет знаки.

Пусть $\max|U_{xy}|^2\le C_0/N$, как в FM-021. Из
$\sum_n g_N(n)^2\le\sum_n g_N(n)\le4\sqrt N$ получаем
$$
\|B_N\|_{\mathrm{HS}}^2\le4C_0\sqrt N.
$$
При $m\ge2$, неравенство для следа произведения и норма $0.95$ дают
$$
|\operatorname{Tr}B_N^m|
 \le\|B_N\|_{\mathrm{HS}}^2\,0.95^{m-2}.
$$
Для $m=1$, поскольку $g_N(0)=1$,
$$
|\operatorname{Tr}B_N|^2
   =|\operatorname{Tr}U_N|^2\le C_0N.
$$
Следовательно, для любого фиксированного ограниченного веса $w\ge0$
$$
\frac1{N^2}\sum_{1\le m<2N}w(m/N)|\operatorname{Tr}B_N^m|^2
 \le\frac{\|w\|_\infty}{N}
       \left(C_0+\frac{16C_0^2}{1-0.95^2}\right).     \tag{VIIIe.3.1}
$$

С другой стороны, для $P_B=|B_N|^2$ сумма строки не больше
$r_N=4C_0/\sqrt N$, а $\operatorname{Tr}P_B\le C_0$.
Вращательная часть удовлетворяет
$$
0\le D^B_{m,N}\le m\operatorname{Tr}P_B^m.
$$
При $r_N\le1/2$
$$
\sum_{m\ge1}D^B_{m,N}\le C_0+128C_0^2.
$$
Совместно с (VIIIe.3.1) это доказывает
$$
\boxed{\left|
 \frac1{N^2}\sum_{1\le m<2N}w(m/N)Y^B_{m,N}
 \right|\le \frac{C_w}{N}\longrightarrow0.}           \tag{VIIIe.3.2}
$$
Можно взять
$$
C_w=\|w\|_\infty\left(
 2C_0+128C_0^2+\frac{16C_0^2}{1-0.95^2}\right).
$$
Оценки равномерны по всем временам в сумме, включая $m\asymp N$.
Сам вес $w$ остаётся исходным, если подставить $w=|\widehat b_*|^2$.

**Различие целей существенно.** В (VIIIe.3.2) стоит $Y^B$, а не исходный $Y$. Предел 0 здесь не заменяет требуемый исходный $-\delta_*$. Умножение на гауссов вес каждого из $m$ рёбер существенно меняет длинное слово; оно не является ошибкой порядка $o(1)$ для всей исходной суммы.

### VIIIe.4. CG3: вес нельзя снять малым операторным возмущением

Для исходной семьи при $\tau$
$$
\|U_N-B_N\|_{\mathrm{HS}}^2
   =\sum_{x,y}|U_{xy}|^2(1-g_N(x-y))^2
   \ge N-2C_0\sum_ng_N(n)
   \ge N-8C_0\sqrt N.
$$
Здесь использована унитарность $U_N$, затем FM-021. Поэтому
$$
\boxed{\liminf_{N\ \mathrm{odd}}\|U_N-B_N\|\ge1.}    \tag{VIIIe.4.1}
$$
Неравенство $\|A\|_{\mathrm{HS}}\le\sqrt N\|A\|$ доказывается суммированием норм $Ae_j$. Никакой информации о неизвестных собственных фазах для (VIIIe.4.1) не требуется.

Таким образом, строгая оценка (VIIIe.3.2) не переносится на $Y$ непрерывностью по операторной норме. Это конкретное препятствие для проверенного механизма снятия веса, а не запрет всех возможных методов.

#### VIIIe.4.1. CG4: жёсткое отсечение может увеличить норму уже при нулевом времени

Этот отдельный результат относится к $M_N=U_N(0)$, не подменяет исходное $\tau$. Положим
$$
H_N(x,y)=\mathbf1_{\operatorname{dist}_N(x,y)\le
                                  \lfloor2\sqrt N\rfloor}\,M_N(x,y).
$$
Тогда
$$
\liminf\|H_N\|>1.001.       \tag{VIIIe.4.2}
$$
Значит, из точечного неравенства $0\le h\le1$ нельзя заключать, что шурово взвешивание унитарной матрицы сжимает норму.

Приведём точное доказательство. Для произвольной циклической маски $h(n)$ пусть
$$
p_\ell=\frac1N\sum_nh(n)e_N(-\ell n),\quad
 V=T_N(-4,2).
$$
Из точной метаплектической формулы
$$
M_N^*Z^\ell M_N Z^{-\ell}
      =e_N(2\ell^2)V^\ell
$$
следует
$$
\|h\odot M_N\|
   =\max_{k\bmod N}\left|\sum_{\ell\bmod N}
                    p_\ell e_N(2\ell^2+k\ell)\right|. \tag{VIIIe.4.3}
$$
Оператор $V$ имеет все $N$ корней единицы как собственные значения по одному разу: $V^N=I$, а $\operatorname{Tr}V^j=0$ при $1\le j<N$, поскольку $-4$ обратимо по нечётному модулю. Конечное Fourier-обращение кратностей завершает это утверждение.

Действие $M_N^*Z^\ell M_N$ можно проверить непосредственно суммой по промежуточному индексу; оно равно $T_N(-4\ell,3\ell)$. Weyl-произведение с $Z^{-\ell}$ даёт фазу $e_N(2\ell^2)$. Таким образом, (VIIIe.4.3) не использует предположения о случайных фазах.

Завершение квадрата в сумме по $\ell$ даёт при $k=0$
$$
\sum_\ell p_\ell e_N(2\ell^2)
 =\frac{G_N}{N}\sum_{|n|\le\lfloor2\sqrt N\rfloor}
                           e_N(-\bar{8} n^2),\quad
 G_N=\sum_\ell e_N(2\ell^2),\quad |G_N|=\sqrt N.
$$
Последняя норма следует раскрытием квадрата: внутренний характер имеет коэффициент $4v$, поэтому ненулевая сумма возникает только при $v=0$.

Запишем $8\bar{8}=1+\nu_NN$, $\nu_N\in\{1,3,5,7\}$. Группируя по остаткам $n\bmod8$, получаем равномерную риманову оценку
$$
\frac1{\sqrt N}\sum_{|n|\le\lfloor2\sqrt N\rfloor}
 e_N(-\bar{8}n^2)
 =\frac12e^{-\pi i\nu_N/4}
      \int_{-2}^2e^{-\pi iu^2/4}\,du+O(200N^{-1/2}).
$$
Здесь среднее восьми арифметических коэффициентов равно
$\frac18\sum_{s=0}^7e^{-\pi i\nu_Ns^2/4}
=\frac12e^{-\pi i\nu_N/4}$. Для остатка достаточно оценить производную медленной функции модулем $\pi$ и два крайних неполных интервала каждого класса; константа 200 больше полученной суммы. Все четыре $\nu_N$ сохранены.

Следовательно, нижняя граница нормы в (VIIIe.4.3) стремится к
$$
\left|\int_0^2 e^{-\pi iu^2/4}\,du\right|
 \ge \int_0^2\sin(\pi u^2/4)\,du.
$$
Для $0\le x\le\pi<4$ знак остатка синусного ряда даёт
$\sin x\ge x-x^3/6+x^5/120-x^7/5040$. Действительно, начиная с члена $x^9/9!$, модули чередующегося хвоста строго убывают. После интегрирования
$$
\int_0^2\sin(\pi u^2/4)\,du
 \ge \frac{2\pi}{3}-\frac{\pi^3}{21}
                +\frac{\pi^5}{660}-\frac{\pi^7}{37800}>1.001.       \tag{VIIIe.4.4}
$$

Последнее строгое сравнение допускает полностью рациональный сертификат.
Пусть $A_n(z)=\sum_{j=0}^{n-1}(-1)^jz^{2j+1}/(2j+1)$, и
$$
p_L=16A_{10}(1/5)-4(A_2(1/239)+1/(5\cdot239^5)),
$$
$$
p_U=16(A_{10}(1/5)+1/(21\cdot5^{21}))-4A_2(1/239).
$$
Тогда $p_L<\pi<p_U$. Формула
$\pi=16\arctan(1/5)-4\arctan(1/239)$
получается из тангенса разности: $\tan(4\arctan(1/5))=120/119$, а последующая разность с $\arctan(1/239)$ имеет тангенс 1 и лежит в $(0,\pi/2)$: положительность следует из $\arctan(1/5)>1/5-1/(3\cdot5^3)$, а сверху угол меньше $4/5<\pi/2$. Последнее также следует из $\arctan1>1/2$. Остатки рядов арктангенса дают указанные рациональные границы. Прямая рациональная арифметика проверяет
$$
2p_L/3-p_U^3/21+p_L^5/660-p_U^7/37800
             >1001/1000 .
$$
Полный рациональный пересчёт приведён в скрипте. Это завершает (VIIIe.4.2); конечное приближение нормы не используется как доказательство предела.

### VIIIe.5. Статусы, проверка и оставшийся шаг

**ДОКАЗАНО:** CG1 — строгая норма гауссово взвешенного оператора при исходном $\tau$, с равномерным остатком; CG2 — $O(N^{-1})$-оценка полного взвешенного знакового сектора; CG3 — отсутствие операторной близости к исходному $U_N$; CG4 — увеличение нормы при жёстком отсечении для $t=0$.

**OUTLINE:** операторный расчёт закрывает точно определённый гауссово взвешенный сектор критической ширины. Сумма без этого веса не выражена через него с контролируемой ошибкой. Положительный и ограниченный вес не допускает монотонного сравнения модулей когерентных сумм; CG4 даёт конкретную проверку такого различия.

**НЕДОКАЗАНО:**

- U-CG1: снять вес в полном когерентном тесте либо получить контролируемую совокупность секторов, которая точно восстанавливает исходную сумму.
- U-CG2: оценить исходный неотражённый $Y$ с пределом $-\delta_*$, сохранив все слова и ветви.
- U-CG3: закрыть достаточную иерархию всех фиксированных порядков или ограниченный Laplace-тест.

Новый результат не объявляется принципиальным решением BGS. Самое трудное место остаётся в суммарном весе и знаковой компенсации исходных конфигураций. Одношаговая нормовая оценка здесь обходится без блокера X1 потому, что предварительно введён существенный вес; удаление именно этого веса и осталось недоказанным.

Доказательства проверены автором отдельно после вывода. Особо проверены: нормировка $a_r/2=\sqrt{b_r}$, четыре остаточных канала, изменение модулей 4 при нечётном $N$, отсутствие потери числа локальных окон, степень $N^{-1/5}$, применимость оценки ко всем степеням только для $B_N$, различие $Y^B$ и $Y$, знак исходной поправки $-\delta_*$, а также область $t=0$ отдельного жёсткого контрпримера. Независимого рецензирования не было; новизна в литературе не проверялась.

Вычисления проверяют конечные тождества и нормировки. Они не проверяют Sine₂ при доступном $N$. В контрольных положительных временах используется $t=10^{-6}$ для проверки определений; это не численная проверка исходного $10^{-80}$. Ранние два Wolfram-вызова вернули результаты с диагностическими сообщениями; заключительный расчёт точных рамок в $\mathbb Q(\zeta_8)$ и рационального сертификата не содержит сообщений. Все входы и ответы сохранены. Первичная квадратура оставляла стандартный относительный допуск SciPy, что привело к провалу сравнения на уровне 10⁻¹²; после диагностики явно заданы оба допуска 10⁻¹³. Аналитическая формула и утверждение не менялись.

#### VIIIe.5.1. Финальный точный Wolfram-вход

```wolfram
ClearAll[z,nu,r,s,x,b,xi];
red[p_]:=PolynomialRemainder[Expand[p],z^4+1,z];
frames=Table[
 c=Table[red[Sum[z^Mod[-nu(3 x^2-2 x s+3 s^2)-2 r x,8],{x,0,3}]/4],
 {r,0,3},{s,0,3}];
 cstar=Map[red[#/.z->z^7]&,Transpose[c],{2}];
 <|"nu"->nu,"unitaryInQZeta8"->(Map[red,cstar.c-IdentityMatrix[4],{2}]==ConstantArray[0,{4,4}])|>,
 {nu,{1,3,5,7}}];
partial[z0_,n_]:=Sum[(-1)^j z0^(2 j+1)/(2 j+1),{j,0,n-1}];
pL=16 partial[1/5,10]-4 (partial[1/239,2]+1/(5*239^5));
pU=16 (partial[1/5,10]+1/(21*5^21))-4 partial[1/239,2];
sinLower=2 pL/3-pU^3/21+pL^5/660-pU^7/37800;
normIdentity=Together[(Pi*b)^2/(1/4+Pi^2*b^2) - 1/(1+1/(4 Pi^2*b^2))]===0;
<|"kernelVersion"->$Version,"frames"->frames,"gaussianFourthPowerIdentity"->normIdentity,
 "rhoQuarter"->N[(1+4/Pi^2)^(-1/4),30],
 "rationalLowerExceeds1001over1000"->TrueQ[sinLower>1001/1000],
 "rationalLower"->N[sinLower,30]|>
```

#### VIIIe.5.2. Полный символьный протокол

```json
{
  "purpose": "Finite symbolic normalization checks only; analytical CG1-CG4 proofs are in the report.",
  "calls": [
    {
      "status": "returned-results-with-precision-warnings",
      "code": "\nClearAll[nu,r,s,x,u,b,xi,pL,pU];\nframes=Table[\n c=Table[FullSimplify[Sum[\n Exp[-2 Pi I nu (3 x^2-2 x s+3 s^2)/8] Exp[-2 Pi I r x/4],\n {x,0,3}]/4],{r,0,3},{s,0,3}];\n <|\"nu\"->nu,\"unitary\"->TrueQ[FullSimplify[ConjugateTranspose[c].c==IdentityMatrix[4]]]|>,\n {nu,{1,3,5,7}}];\ngauss=Integrate[Sqrt[b] Exp[-(1/2+I Pi b)u^2-2 Pi I xi u],\n {u,-Infinity,Infinity},Assumptions->b>0 && Element[xi,Reals]];\ngaussAtZero=FullSimplify[Abs[gauss/.xi->0],Assumptions->b>0];\npartial[z_,n_]:=Sum[(-1)^j z^(2 j+1)/(2 j+1),{j,0,n-1}];\npL=16 partial[1/5,10]-4 (partial[1/239,2]+1/(5*239^5));\npU=16 (partial[1/5,10]+1/(21*5^21))-4 partial[1/239,2];\nsinLower=2 pL/3-pU^3/21+pL^5/660-pU^7/37800;\n<|\"kernelVersion\"->$Version,\"frames\"->frames,\n \"gaussianMultiplier\"->gauss,\"normAtZero\"->gaussAtZero,\n \"rhoQuarter\"->N[(1+4/Pi^2)^(-1/4),30],\n \"piIntervalContainsPi\"->TrueQ[pL<Pi<pU],\n \"sinIntegralRationalLowerExceeds1001over1000\"->TrueQ[sinLower>1001/1000],\n \"sinIntegralRationalLower\"->N[sinLower,30],\n \"hardCenterLimit\"->N[Abs[Integrate[Exp[-I Pi u^2/4],{u,0,2}]],30]|>\n",
      "result": {
        "content": [
          {
            "type": "text",
            "text": "N::meprec: Internal precision limit $MaxExtraPrecision = 50. reached while evaluating -1/2 + ((1/2 - I/2)*(-1)^(1/4))/Sqrt[2].\nN::meprec: Internal precision limit $MaxExtraPrecision = 50. reached while evaluating -1/2 + ((1/2 - I/2)*(-1)^(1/4))/Sqrt[2].\nN::meprec: Internal precision limit $MaxExtraPrecision = 50. reached while evaluating -1/2 + ((1/2 - I/2)*(-1)^(1/4))/Sqrt[2].\nN::meprec: Internal precision limit $MaxExtraPrecision = 50. reached while evaluating -1/2 + ((1/2 - I/2)*(-1)^(1/4))/Sqrt[2].\nN::meprec: Internal precision limit $MaxExtraPrecision = 50. reached while evaluating -1/2 + ((1/2 - I/2)*(-1)^(1/4))/Sqrt[2].\nN::meprec: Internal precision limit $MaxExtraPrecision = 50. reached while evaluating -1/2 + ((1/2 - I/2)*(-1)^(1/4))/Sqrt[2].\nN::meprec: Internal precision limit $MaxExtraPrecision = 50. reached while evaluating -1/2 + ((1/2 - I/2)*(-1)^(1/4))/Sqrt[2].\nN::meprec: Internal precision limit $MaxExtraPrecision = 50. reached while evaluating -1/2 + ((1/2 - I/2)*(-1)^(1/4))/Sqrt[2].\nN::meprec: Internal precision limit $MaxExtraPrecision = 50. reached while evaluating -1/2 - ((1/2 + I/2)*(-1)^(3/4))/Sqrt[2].\nN::meprec: Internal precision limit $MaxExtraPrecision = 50. reached while evaluating -1/2 - ((1/2 + I/2)*(-1)^(3/4))/Sqrt[2].\nN::meprec: Internal precision limit $MaxExtraPrecision = 50. reached while evaluating -1/2 - ((1/2 + I/2)*(-1)^(3/4))/Sqrt[2].\nGeneral::messages: Messages were generated which may indicate errors.\n\nOut[1]= <|\"kernelVersion\" -> \"15.0.1 for Linux x86 (64-bit) (July 2, 2026)\", \"frames\" -> {<|\"nu\" -> 1, \"unitary\" -> True|>, <|\"nu\" -> 3, \"unitary\" -> True|>, <|\"nu\" -> 5, \"unitary\" -> True|>, <|\"nu\" -> 7, \"unitary\" -> True|>}, \"gaussianMultiplier\" -> E^(((2*I)*Pi^2*xi^2)/(-I + 2*b*Pi))/Sqrt[I + 1/(2*b*Pi)], \"normAtZero\" -> 1/Sqrt[Abs[I + 1/(2*b*Pi)]], \"rhoQuarter\" -> 0.9184571890234016835679272660031121097908670747713381976803`30., \"piIntervalContainsPi\" -> True, \"sinIntegralRationalLowerExceeds1001over1000\" -> True, \"sinIntegralRationalLower\" -> 1.0016699884888372700002230190023576379035691344012303308901`30., \"hardCenterLimit\" -> 1.2565688534853226622040487794805698692119377149433196079244`30.|>"
          }
        ],
        "structuredContent": null,
        "isError": false
      }
    },
    {
      "status": "returned-results-with-root-reduction-warnings",
      "code": "\nClearAll[nu,r,s,x,u,b,xi,pL,pU];\nframes=Table[\n c=Table[RootReduce[Sum[\n Exp[-2 Pi I nu (3 x^2-2 x s+3 s^2)/8] Exp[-2 Pi I r x/4],\n {x,0,3}]/4],{r,0,3},{s,0,3}];\n <|\"nu\"->nu,\"unitary\"->TrueQ[Map[RootReduce,ConjugateTranspose[c].c-IdentityMatrix[4],{2}]==ConstantArray[0,{4,4}]]|>,\n {nu,{1,3,5,7}}];\ngauss=Integrate[Sqrt[b] Exp[-(1/2+I Pi b)u^2-2 Pi I xi u],\n {u,-Infinity,Infinity},Assumptions->b>0 && Element[xi,Reals]];\ngaussAtZero=(1+1/(4 Pi^2 b^2))^(-1/4);\npartial[z_,n_]:=Sum[(-1)^j z^(2 j+1)/(2 j+1),{j,0,n-1}];\npL=16 partial[1/5,10]-4 (partial[1/239,2]+1/(5*239^5));\npU=16 (partial[1/5,10]+1/(21*5^21))-4 partial[1/239,2];\nsinLower=2 pL/3-pU^3/21+pL^5/660-pU^7/37800;\n<|\"kernelVersion\"->$Version,\"frames\"->frames,\n \"gaussianMultiplier\"->gauss,\"normAtZero\"->gaussAtZero,\n \"rhoQuarter\"->N[(1+4/Pi^2)^(-1/4),30],\n \"piIntervalContainsPi\"->TrueQ[pL<Pi<pU],\n \"sinIntegralRationalLowerExceeds1001over1000\"->TrueQ[sinLower>1001/1000],\n \"sinIntegralRationalLower\"->N[sinLower,30],\n \"hardCenterLimit\"->N[Abs[Integrate[Exp[-I Pi u^2/4],{u,0,2}]],30]|>\n",
      "result": {
        "content": [
          {
            "type": "text",
            "text": "MinValue::lpsub: -- Message text not found -- \nMaxValue::lpsub: -- Message text not found -- \nMinValue::lpsub: -- Message text not found -- \nMinValue::lpsub: -- Message text not found -- \nMaxValue::lpsub: -- Message text not found -- \nMinValue::lpsub: -- Message text not found -- \nMinValue::lpsub: -- Message text not found -- \nMaxValue::lpsub: -- Message text not found -- \nMinValue::lpsub: -- Message text not found -- \nMinValue::lpsub: -- Message text not found -- \nMaxValue::lpsub: -- Message text not found -- \nGeneral::messages: Messages were generated which may indicate errors.\n\nOut[1]= <|\"kernelVersion\" -> \"15.0.1 for Linux x86 (64-bit) (July 2, 2026)\", \"frames\" -> {<|\"nu\" -> 1, \"unitary\" -> True|>, <|\"nu\" -> 3, \"unitary\" -> True|>, <|\"nu\" -> 5, \"unitary\" -> True|>, <|\"nu\" -> 7, \"unitary\" -> True|>}, \"gaussianMultiplier\" -> E^(((2*I)*Pi^2*xi^2)/(-I + 2*b*Pi))/Sqrt[I + 1/(2*b*Pi)], \"normAtZero\" -> (1 + 1/(4*b^2*Pi^2))^(-1/4), \"rhoQuarter\" -> 0.9184571890234016835679272660031121097908670747713381976803`30., \"piIntervalContainsPi\" -> True, \"sinIntegralRationalLowerExceeds1001over1000\" -> True, \"sinIntegralRationalLower\" -> 1.0016699884888372700002230190023576379035691344012303308901`30., \"hardCenterLimit\" -> 1.2565688534853226622040487794805698692119377149433196079244`30.|>"
          }
        ],
        "structuredContent": null,
        "isError": false
      }
    },
    {
      "status": "completed-without-reported-messages",
      "code": "\nClearAll[z,nu,r,s,x,b,xi];\nred[p_]:=PolynomialRemainder[Expand[p],z^4+1,z];\nframes=Table[\n c=Table[red[Sum[z^Mod[-nu(3 x^2-2 x s+3 s^2)-2 r x,8],{x,0,3}]/4],\n {r,0,3},{s,0,3}];\n cstar=Map[red[#/.z->z^7]&,Transpose[c],{2}];\n <|\"nu\"->nu,\"unitaryInQZeta8\"->(Map[red,cstar.c-IdentityMatrix[4],{2}]==ConstantArray[0,{4,4}])|>,\n {nu,{1,3,5,7}}];\npartial[z0_,n_]:=Sum[(-1)^j z0^(2 j+1)/(2 j+1),{j,0,n-1}];\npL=16 partial[1/5,10]-4 (partial[1/239,2]+1/(5*239^5));\npU=16 (partial[1/5,10]+1/(21*5^21))-4 partial[1/239,2];\nsinLower=2 pL/3-pU^3/21+pL^5/660-pU^7/37800;\nnormIdentity=Together[(Pi*b)^2/(1/4+Pi^2*b^2) - 1/(1+1/(4 Pi^2*b^2))]===0;\n<|\"kernelVersion\"->$Version,\"frames\"->frames,\"gaussianFourthPowerIdentity\"->normIdentity,\n \"rhoQuarter\"->N[(1+4/Pi^2)^(-1/4),30],\n \"rationalLowerExceeds1001over1000\"->TrueQ[sinLower>1001/1000],\n \"rationalLower\"->N[sinLower,30]|>\n",
      "result": {
        "content": [
          {
            "type": "text",
            "text": "Out[1]= <|\"kernelVersion\" -> \"15.0.1 for Linux x86 (64-bit) (July 2, 2026)\", \"frames\" -> {<|\"nu\" -> 1, \"unitaryInQZeta8\" -> True|>, <|\"nu\" -> 3, \"unitaryInQZeta8\" -> True|>, <|\"nu\" -> 5, \"unitaryInQZeta8\" -> True|>, <|\"nu\" -> 7, \"unitaryInQZeta8\" -> True|>}, \"gaussianFourthPowerIdentity\" -> True, \"rhoQuarter\" -> 0.9184571890234016835679272660031121097908670747713381976803`30., \"rationalLowerExceeds1001over1000\" -> True, \"rationalLower\" -> 1.0016699884888372700002230190023576379035691344012303308901`30.|>"
          }
        ],
        "structuredContent": null,
        "isError": false
      }
    }
  ]
}
```

#### VIIIe.5.3. Конечные Python-результаты

```json
{
  "assertion_tested": "Exact Q(zeta_8) frame unitarity and rational sine certificate; finite Weyl identity; Gaussian/hard filter norms; constant-coefficient integral normalization; finite original matrix definitions at auxiliary time.",
  "software": [
    {
      "name": "Python",
      "version": "3.12.14"
    },
    {
      "name": "NumPy",
      "version": "2.3.5"
    },
    {
      "name": "SciPy",
      "version": "1.17.0"
    }
  ],
  "exact_frames": [
    {
      "nu": 1,
      "exact_unitarity": true
    },
    {
      "nu": 3,
      "exact_unitarity": true
    },
    {
      "nu": 5,
      "exact_unitarity": true
    },
    {
      "nu": 7,
      "exact_unitarity": true
    }
  ],
  "rational_certificate": {
    "pi_lower": "135971713047870654998930719127948/43281140504482774600982666015625",
    "pi_upper": "59510387181559814171646183368/18942744570509433746337890625",
    "sine_lower": "13515073147129850941350036736725939301073911552649964863931561684919034467575872095630345575666962526609087895132265157511642297456387139902455261508133508052812869006227306268509269748378942138916576514823967336/13492540759376524467826703539814856458444108846181796100586238055014969386560577910517040118099684122128862643424852137710239908848978765275566507929071336015739423838254336385222842409348231740295886993408203125",
    "sine_lower_float": 1.0016699884888374
  },
  "matrix_checks": [
    {
      "N": 9,
      "nu": 7,
      "weyl_identity_error": 2.1897020778056683e-15,
      "direct_norm": 0.8679919073557477,
      "weyl_norm": 0.8679919073557477
    },
    {
      "N": 11,
      "nu": 5,
      "weyl_identity_error": 1.2268151741436226e-15,
      "direct_norm": 0.8823270221092536,
      "weyl_norm": 0.8823270221092536
    },
    {
      "N": 13,
      "nu": 3,
      "weyl_identity_error": 1.4146460637222681e-15,
      "direct_norm": 0.8981103413995575,
      "weyl_norm": 0.8981103413995576
    },
    {
      "N": 15,
      "nu": 1,
      "weyl_identity_error": 2.575741344239586e-15,
      "direct_norm": 0.9089065000716207,
      "weyl_norm": 0.908906500071621
    }
  ],
  "scale_checks": [
    {
      "N": 63,
      "kappa": 0.5,
      "gaussian_norm": 0.6045865923418172,
      "gaussian_limit": 0.6045865662484434,
      "hard_kappa2_norm": 1.2680248950611668,
      "hard_kappa2_center": 1.1928321168237084
    },
    {
      "N": 63,
      "kappa": 1.0,
      "gaussian_norm": 0.918457188978541,
      "gaussian_limit": 0.9184571890234017,
      "hard_kappa2_norm": 1.2680248950611668,
      "hard_kappa2_center": 1.1928321168237084
    },
    {
      "N": 63,
      "kappa": 2.0,
      "gaussian_norm": 0.993324340772085,
      "gaussian_limit": 0.9937658135352574,
      "hard_kappa2_norm": 1.2680248950611668,
      "hard_kappa2_center": 1.1928321168237084
    },
    {
      "N": 63,
      "kappa": 4.0,
      "gaussian_norm": 0.9997431355117465,
      "gaussian_limit": 0.9996046052781503,
      "hard_kappa2_norm": 1.2680248950611668,
      "hard_kappa2_center": 1.1928321168237084
    },
    {
      "N": 255,
      "kappa": 0.5,
      "gaussian_norm": 0.6045865662484434,
      "gaussian_limit": 0.6045865662484434,
      "hard_kappa2_norm": 1.2794625696257649,
      "hard_kappa2_center": 1.2362901108692064
    },
    {
      "N": 255,
      "kappa": 1.0,
      "gaussian_norm": 0.9184571890234017,
      "gaussian_limit": 0.9184571890234017,
      "hard_kappa2_norm": 1.2794625696257649,
      "hard_kappa2_center": 1.2362901108692064
    },
    {
      "N": 255,
      "kappa": 2.0,
      "gaussian_norm": 0.9937658135352433,
      "gaussian_limit": 0.9937658135352574,
      "hard_kappa2_norm": 1.2794625696257649,
      "hard_kappa2_center": 1.2362901108692064
    },
    {
      "N": 255,
      "kappa": 4.0,
      "gaussian_norm": 0.9995785992053025,
      "gaussian_limit": 0.9996046052781503,
      "hard_kappa2_norm": 1.2794625696257649,
      "hard_kappa2_center": 1.2362901108692064
    },
    {
      "N": 1023,
      "kappa": 0.5,
      "gaussian_norm": 0.6045865662484434,
      "gaussian_limit": 0.6045865662484434,
      "hard_kappa2_norm": 1.2717549215923891,
      "hard_kappa2_center": 1.2491835392374824
    },
    {
      "N": 1023,
      "kappa": 1.0,
      "gaussian_norm": 0.9184571890234016,
      "gaussian_limit": 0.9184571890234017,
      "hard_kappa2_norm": 1.2717549215923891,
      "hard_kappa2_center": 1.2491835392374824
    },
    {
      "N": 1023,
      "kappa": 2.0,
      "gaussian_norm": 0.9937658135352576,
      "gaussian_limit": 0.9937658135352574,
      "hard_kappa2_norm": 1.2717549215923891,
      "hard_kappa2_center": 1.2491835392374824
    },
    {
      "N": 1023,
      "kappa": 4.0,
      "gaussian_norm": 0.9996046052781323,
      "gaussian_limit": 0.9996046052781503,
      "hard_kappa2_norm": 1.2717549215923891,
      "hard_kappa2_center": 1.2491835392374824
    },
    {
      "N": 4095,
      "kappa": 0.5,
      "gaussian_norm": 0.6045865662484434,
      "gaussian_limit": 0.6045865662484434,
      "hard_kappa2_norm": 1.265044772228524,
      "hard_kappa2_center": 1.2535673960463156
    },
    {
      "N": 4095,
      "kappa": 1.0,
      "gaussian_norm": 0.9184571890234017,
      "gaussian_limit": 0.9184571890234017,
      "hard_kappa2_norm": 1.265044772228524,
      "hard_kappa2_center": 1.2535673960463156
    },
    {
      "N": 4095,
      "kappa": 2.0,
      "gaussian_norm": 0.9937658135352574,
      "gaussian_limit": 0.9937658135352574,
      "hard_kappa2_norm": 1.265044772228524,
      "hard_kappa2_center": 1.2535673960463156
    },
    {
      "N": 4095,
      "kappa": 4.0,
      "gaussian_norm": 0.9996046052781504,
      "gaussian_limit": 0.9996046052781503,
      "hard_kappa2_norm": 1.265044772228524,
      "hard_kappa2_center": 1.2535673960463156
    },
    {
      "N": 16383,
      "kappa": 0.5,
      "gaussian_norm": 0.6045865662484435,
      "gaussian_limit": 0.6045865662484434,
      "hard_kappa2_norm": 1.2610175395784877,
      "hard_kappa2_center": 1.2552424210265178
    },
    {
      "N": 16383,
      "kappa": 1.0,
      "gaussian_norm": 0.9184571890234016,
      "gaussian_limit": 0.9184571890234017,
      "hard_kappa2_norm": 1.2610175395784877,
      "hard_kappa2_center": 1.2552424210265178
    },
    {
      "N": 16383,
      "kappa": 2.0,
      "gaussian_norm": 0.993765813535257,
      "gaussian_limit": 0.9937658135352574,
      "hard_kappa2_norm": 1.2610175395784877,
      "hard_kappa2_center": 1.2552424210265178
    },
    {
      "N": 16383,
      "kappa": 4.0,
      "gaussian_norm": 0.9996046052781501,
      "gaussian_limit": 0.9996046052781503,
      "hard_kappa2_norm": 1.2610175395784877,
      "hard_kappa2_center": 1.2552424210265178
    }
  ],
  "normal_form_checks": [
    {
      "b": 0.2,
      "xi": 0.0,
      "quadrature_error": 1.2412670766236366e-16
    },
    {
      "b": 0.2,
      "xi": 0.25,
      "quadrature_error": 1.6653345369377348e-16
    },
    {
      "b": 0.2,
      "xi": 0.5,
      "quadrature_error": 1.0838898772828417e-16
    },
    {
      "b": 0.25,
      "xi": 0.0,
      "quadrature_error": 1.5700924586837752e-16
    },
    {
      "b": 0.25,
      "xi": 0.25,
      "quadrature_error": 0.0
    },
    {
      "b": 0.25,
      "xi": 0.5,
      "quadrature_error": 4.85722573273506e-17
    },
    {
      "b": 0.3333333333333333,
      "xi": 0.0,
      "quadrature_error": 4.002966042486721e-16
    },
    {
      "b": 0.3333333333333333,
      "xi": 0.25,
      "quadrature_error": 1.3877787807814457e-17
    },
    {
      "b": 0.3333333333333333,
      "xi": 0.5,
      "quadrature_error": 1.1188630228279524e-16
    }
  ],
  "positive_time_checks": [
    {
      "N": 19,
      "auxiliary_time": 1e-06,
      "filtered_norm": 0.91747579521598
    },
    {
      "N": 21,
      "auxiliary_time": 1e-06,
      "filtered_norm": 0.9184534840758235
    },
    {
      "N": 31,
      "auxiliary_time": 1e-06,
      "filtered_norm": 0.9184788674018355
    }
  ],
  "non_claims": [
    "No computation tests original tau=10^-80 at asymptotic N.",
    "Finite norms do not prove a norm limit.",
    "CG1-CG4 have separate analytical proofs.",
    "The Gaussian weighted sum is not the original coherent sum.",
    "Sine_2 and the original pair moment remain unresolved."
  ],
  "development_note": "An initial quadrature check failed its 1e-12 comparison because SciPy's default relative tolerance was left active; diagnostics showed reported quadrature errors above that threshold. Final quadrature explicitly sets both tolerances to 1e-13.",
  "script_sha256": "cf38ff629a931511c4ecaf2a0d5583c5445df90cccecec6b8605ad8a9d7fa707"
}
```

#### VIIIe.5.4. Протокол запуска

```json
{
  "schema_version": 2,
  "claim_id": "TRACE005-CRITICAL-GAUSSIAN-20261026",
  "repository": {
    "commit": "unavailable; standalone research artifacts",
    "dirty": true,
    "dirty_semantics": "New unversioned files; no Git status inspected"
  },
  "command": [
    "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python3",
    "/workspace/scratch/980ff7770509/output/trace005_critical_gaussian_verify.py",
    "--output",
    "/workspace/scratch/980ff7770509/output/trace005_critical_gaussian_checks.json"
  ],
  "environment": {
    "software": [
      {
        "name": "Python",
        "version": "3.12.14"
      },
      {
        "name": "NumPy",
        "version": "2.3.5"
      },
      {
        "name": "SciPy",
        "version": "1.17.0"
      }
    ],
    "hardware": "x86_64"
  },
  "mathematics": {
    "assertion_tested": "Exact Q(zeta_8) frame unitarity and rational sine certificate; finite Weyl identity; Gaussian/hard filter norms; constant-coefficient integral normalization; finite original matrix definitions at auxiliary time.",
    "coefficient_domain": "Q(zeta_8), rational arithmetic, and separately complex128/float64",
    "conventions": "Original T_N and cat M_N; cyclic masks; auxiliary positive time 1e-6",
    "inputs": [
      "Exact finite frames, rational Machin bounds, original finite cat and kick definitions specified in the script"
    ],
    "bounds": {
      "frame_nu": [
        1,
        3,
        5,
        7
      ],
      "weyl_N": [
        9,
        11,
        13,
        15
      ],
      "gaussian_N": [
        63,
        255,
        1023,
        4095,
        16383
      ],
      "kappa": [
        0.5,
        1,
        2,
        4
      ],
      "hard_kappa": 2,
      "normal_form_b": [
        0.2,
        0.25,
        0.3333333333333333
      ],
      "normal_form_xi": [
        0,
        0.25,
        0.5
      ],
      "positive_time_N": [
        19,
        21,
        31
      ],
      "auxiliary_time": 1e-06
    },
    "non_claims": [
      "No computation tests original tau=10^-80 at asymptotic N.",
      "Finite norms do not prove a norm limit.",
      "CG1-CG4 have separate analytical proofs.",
      "The Gaussian weighted sum is not the original coherent sum.",
      "Sine_2 and the original pair moment remain unresolved."
    ]
  },
  "randomness": {
    "used": false,
    "generator": "",
    "seed": null
  },
  "run": {
    "started_at": "2026-10-26T07:15:44.134613+00:00",
    "runtime_seconds": 1.5037941159998809,
    "status": "completed",
    "exit_status": 0,
    "resource_limits": {
      "wall_seconds": 30,
      "memory_bytes": null,
      "cpu_seconds": null,
      "max_cores": null,
      "max_threads": null
    }
  },
  "outputs": [
    {
      "path": "output/trace005_critical_gaussian_checks.json",
      "sha256": "d31d8a0356c4cb6819cd003f9005b020a7a06271fa62fbe9c499960f0eeb4193",
      "kind": "result"
    }
  ],
  "checks": [
    "All four exact arithmetic frames",
    "Rational lower bound for hard-cut norm witness",
    "Direct matrix and Weyl identity with both signs of ell",
    "Exact finite mask spectral reduction versus SVD",
    "Gaussian alias inequality and large-N finite normalization",
    "Nine independent Gaussian quadratures",
    "Three auxiliary positive-time original matrix fixtures"
  ],
  "result": "Finite assertions passed; CG1-CG4 separately proved in text.",
  "residual_risks": [
    "Floating checks are not interval certified",
    "Self-review only",
    "Gaussian weighted sum differs from original coherent sum",
    "No proof or refutation of the main local law"
  ],
  "input_artifacts": [
    {
      "path": "output/trace005_critical_gaussian_verify.py",
      "sha256": "cf38ff629a931511c4ecaf2a0d5583c5445df90cccecec6b8605ad8a9d7fa707",
      "sha256_after": "cf38ff629a931511c4ecaf2a0d5583c5445df90cccecec6b8605ad8a9d7fa707"
    }
  ],
  "declared_results": [
    "output/trace005_critical_gaussian_checks.json"
  ]
}
```

Полный Python-скрипт помещён в приложение XI.10. Команда воспроизведения:

```bash
python3 trace005_critical_gaussian_verify.py --output trace005_critical_gaussian_checks.json
```


## VIIIf. Точное восстановление окон: исходный смешанный предел не оценён

### VIIIf.1. Точное разбиение и совместные нормы

Пусть $U$ — любая унитарная $N\times N$ матрица,
$g:\mathbb Z_N\to[0,\infty)$ — ненулевой вещественный вес. Положим
$$
S=\sum_{n\bmod N}g(n),\quad H=\sum_{n\bmod N}g(n)^2,\quad
 B_\ell(x,y)=g(x-y-\ell)U_{xy},\quad \ell\bmod N.
$$
Все суммы в этом разделе конечны. Тогда точно
$$
\sum_\ell B_\ell=SU,\qquad
 \sum_\ell B_\ell^*B_\ell=HI,\qquad
 \sum_\ell B_\ell B_\ell^*=HI.                         \tag{VIIIf.1.1}
$$

Первое равенство получается суммированием веса при фиксированных $x,y$.
Для второго его элемент $(y,z)$ равен
$$
\sum_x\overline{U_{xy}}U_{xz}
 \sum_\ell g(x-y-\ell)g(x-z-\ell).
$$
Внутренняя сумма зависит только от $y-z$, а не от $x$. Унитарность оставляет только $y=z$, где внутренняя сумма равна $H$. Третье равенство доказывается аналогично по строкам. Ни независимость фаз, ни усреднение исходной модели не используются.

Для истории меток $\boldsymbol\ell=(\ell_1,\ldots,\ell_m)$ зададим
$W_{\boldsymbol\ell}=B_{\ell_1}\cdots B_{\ell_m}$, $m\ge1$.
Не меняя порядок множителей, имеем
$$
\sum_{\boldsymbol\ell}W_{\boldsymbol\ell}=S^mU^m,
$$
$$
\sum_{\boldsymbol\ell}W_{\boldsymbol\ell}^*
       W_{\boldsymbol\ell}
 =\sum_{\boldsymbol\ell}W_{\boldsymbol\ell}
       W_{\boldsymbol\ell}^*=H^mI.                   \tag{VIIIf.1.2}
$$
Вторая строка получается последовательным применением (VIIIf.1.1) к внутреннему множителю. Это тождества для всех $m$, в том числе $m\asymp N$.

#### VIIIf.1.1. Смешанные истории необходимы уже для нормы

Обозначим $\eta=H/S^2$. Из (VIIIf.1.2)
$$
S^{-2m}\sum_{\boldsymbol\ell}
       \|W_{\boldsymbol\ell}\|_{\mathrm{HS}}^2=N\eta^m,
$$
тогда как полная когерентная сумма даёт
$$
S^{-2m}\left\|\sum_{\boldsymbol\ell}
               W_{\boldsymbol\ell}\right\|_{\mathrm{HS}}^2=N.
$$
Следовательно, сумма всех смешанных скалярных произведений точно равна
$$
\boxed{S^{-2m}
 \sum_{\boldsymbol\ell\ne\boldsymbol k}
   \operatorname{Tr}(W_{\boldsymbol k}^*W_{\boldsymbol\ell})
       =N(1-\eta^m).}                                \tag{VIIIf.1.3}
$$
Отдельные слагаемые комплексны; их полная сумма в (VIIIf.1.3) вещественна.
Это утверждение относится к норме Гильберта–Шмидта. Оно не заменяет
$\operatorname{Tr}W_{\boldsymbol\ell}
 \overline{\operatorname{Tr}W_{\boldsymbol k}}$,
которое входит в спектральный тест.

Для конкретного гауссова $g_N$ из CG1,
$$
0\le g_N\le1,\quad
 S_N=D_N^{-1}\sum_{r\in\mathbb Z}e^{-r^2/(2N)},\quad D_N<2
 \quad(N\ge3).
$$
Здесь $g_N\le1$ следует из его неотрицательных Fourier-коэффициентов и $g_N(0)=1$. Формула периодизации гауссианы даёт
$\sum_re^{-r^2/(2N)}\ge\sqrt{2\pi N}$.
Кроме того,
$$
D_N\le1+\frac{2e^{-N/2}}{1-e^{-3N/2}}<2.
$$
Последнее можно проверить без десятичных приближений:
$e^{3/2}>4$, откуда при $N\ge3$ добавка меньше $32/63$.
Поэтому $S_N>\sqrt N$, $H_N\le S_N$, и
$$
0<\eta_N<N^{-1/2}.          \tag{VIIIf.1.4}
$$
При $m\ge cN$, $c>0$ фиксировано, доля одинаковых историй в первой нормовой сумме не больше $N^{-cN/2}$; смешанная часть составляет $1-\eta_N^m$ полной нормы. Это равномерная, а не фиксированная по времени оценка.

#### VIIIf.1.2. Что получилось именно для спектрального следа

Положим
$$
I_{m,N}^{\mathrm{win}}=S_N^{-2m}
      \sum_{\boldsymbol\ell}
           |\operatorname{Tr}W_{\boldsymbol\ell}|^2.
$$
Неравенство $|\operatorname{Tr}A|^2\le N\|A\|_{\mathrm{HS}}^2$ даёт
$$
0\le I_{m,N}^{\mathrm{win}}\le N^2\eta_N^m.
$$
Следовательно,
$$
\boxed{\frac1{N^2}\sum_{1\le m<2N}w(m/N)I_{m,N}^{\mathrm{win}}
 \le\|w\|_\infty\frac{\eta_N}{1-\eta_N}
 \le\frac{3\|w\|_\infty}{\sqrt N}.}                  \tag{VIIIf.1.5}
$$
Здесь $w\ge0$ — исходный фиксированный вес или любой ограниченный неотрицательный вес.

Определим полную смешанную следовую сумму
$$
C_{m,N}^{\mathrm{win}}=S_N^{-2m}
 \sum_{\boldsymbol\ell\ne\boldsymbol k}
 \operatorname{Tr}W_{\boldsymbol\ell}\,
                   \overline{\operatorname{Tr}W_{\boldsymbol k}}.
$$
Тогда
$$
|\operatorname{Tr}U_N^m|^2
       = I_{m,N}^{\mathrm{win}}+C_{m,N}^{\mathrm{win}}               \tag{VIIIf.1.6}
$$
точно. Нормовая оценка (VIIIf.1.3) не оценивает $C_{m,N}^{\mathrm{win}}$.
Величина $I^{\mathrm{win}}$ также не является исходным вращательным
$D_{m,N}\simeq m$; это другое разбиение пар.

После (VIIIf.1.5) для парного критерия требуется
$$
\frac1{N^2}\sum_{1\le m<2N}w(m/N)C_{m,N}^{\mathrm{win}}
 \longrightarrow K_w,\qquad
 K_w=\int_0^2w(t)\min(t,1)\,dt>0.                    \tag{VIIIf.1.7}
$$
Это только точный словарь новой группировки. Оценка левой стороны не получена. Положительный знак $K_w$ не противоречит исходной отрицательной поправке $-\delta_*$: разные части вычитаются в разных разбиениях. Исходное обязательство для $Y$ по-прежнему равно $-\delta_*$.

Эквивалентность с исходным парным тестом здесь использует только (VIIIf.1.5) и обычную риманову сумму. Для исходного гладкого $w$ ошибка последней не больше
$$
\left|\frac1{N^2}\sum_{1\le m<2N}w(m/N)\min(m,N)-K_w\right|
 \le\frac{2\|w'\|_\infty+\|w\|_\infty}{N}.
$$
Действительно, полная вариация функции $w(t)\min(t,1)$ на $[0,2]$ не больше числителя. Ошибка правой римановой суммы по каждой ячейке ограничена её длиной, умноженной на интеграл модуля производной по ячейке. Оценка не зависит от $m$.

Добавление всех циклических вращений историй меток также не даёт главного члена. По цикличности следа их положительный вклад не больше $m I_{m,N}^{\mathrm{win}}$; его взвешенная сумма после деления на $N^2$ ограничена
$$
\|w\|_\infty\sum_{m\ge1}m\eta_N^m
 =\|w\|_\infty\frac{\eta_N}{(1-\eta_N)^2}
 \le\frac{6\|w\|_\infty}{\sqrt N}.
$$
Это вращения историй меток окон, а не исходных координатных слов. Нужная смешанная сумма остаётся вне этих положительных вкладов.

**ДОКАЗАНО:** (VIIIf.1.1)–(VIIIf.1.6), сходимость одинаковых историй к нулю после нормировки, необходимость существенных смешанных вкладов для нормы.
**OUTLINE:** исходный парный тест выражен через (VIIIf.1.7).
**НЕДОКАЗАНО:** сама (VIIIf.1.7); она не стала проще от точного разбиения.

### VIIIf.2. Fourier-проверка: реконструкция возвращает унитарный канал

Для $Z_{xx}=e_N(x)$ и
$$
p_t=\frac1N\sum_ng_N(n)e_N(-tn)
$$
точно
$$
B_\ell=\sum_{t\bmod N}p_t e_N(-t\ell)\,Z^tU_NZ^{-t}.
$$
Поэтому Fourier-преобразование меток окон даёт
$$
\boxed{\frac1{\sqrt N}\sum_\ell e_N(t\ell)B_\ell
       =\sqrt N\,p_t\,Z^tU_NZ^{-t}.}                 \tag{VIIIf.2.1}
$$
При $t=0$ правая часть равна $S_NU_N/\sqrt N$, то есть полное восстановление оставляет исходный унитарный канал. Для гауссова веса все $p_t>0$, поэтому после удаления скалярного множителя каждый канал справа унитарен. Равенство Парсеваля также даёт
$$
H_N=N\sum_t p_t^2.
$$

Таким образом, оценка нормы отдельного $B_\ell$ и даже полная система тождеств (VIIIf.1.1) не дают сжатия восстановленного канала. В (VIIIf.2.1) не вводится разрешённая или запрещённая случайность: это конечная смена базиса в уже заданной сумме. Не получена оценка следов этого канала при $m\asymp N$.

### VIIIf.3. Проверка силы предлагаемого критерия на нулевом параметре

Можно ли всё же вывести универсальность из совместного набора свойств: точное восстановление, тождества (VIIIf.1.1), равномерное сжатие всех сдвинутых окон? Уже семейство $M_N=U_N(0)$ опровергает такой общий вывод. Это повторное использование контрольного нулевого параметра для проверки нового критерия, а не контрпример исходному $\tau=10^{-80}$.

Из точной формулы CG4 для произвольной циклической маски следует
$$
\|g_N(\,\cdot-\ell)\odot M_N\|
  =\max_k\left|\sum_t p_t e_N(2t^2+(k-\ell)t)\right|
  =\|g_N\odot M_N\| .
$$
По CG1 при $t=0$ для всех достаточно больших нечётных $N$ эти нормы меньше 0.95, одновременно для всех $\ell$. Тождества (VIIIf.1.1) выполнены автоматически.

Для полноты воспроизведём бесконечную арифметическую подпоследовательность.
Пусть
$$
(3+2\sqrt2)^j=a_j+b_j\sqrt2,\qquad
 N_j=b_j/2,\quad j=3,5,7,\ldots .
$$
Рекурсии
$$
a_{j+1}=3a_j+4b_j,\qquad b_{j+1}=2a_j+3b_j
$$
показывают, что $a_j$ нечётно, $b_j$ чётно и $N_j\equiv j\pmod2$.
Кроме того, $N_{j+1}=a_j+3N_j\ge3N_j$, поэтому $j/N_j\to0$.
Для $S=\left(\begin{smallmatrix}3&4\\2&3\end{smallmatrix}\right)$
$$
S^j=\begin{pmatrix}a_j&2b_j\\b_j&a_j\end{pmatrix}
       \equiv a_jI\pmod{N_j},\qquad
 a_j^2-2b_j^2=1.
$$
Следовательно, $S^{2j}\equiv I\pmod{N_j}$.
Точная Egorov-формула для $M_N$ даёт
$$
M_{N_j}^{2j}=\zeta_jI.         \tag{VIIIf.3.1}
$$
Действительно, эта степень коммутирует со всеми $T_N$. Коммутирование с диагональным $Z$ делает её диагональной, а коммутирование с циклическим сдвигом — скалярной.

У $M_{N_j}$ не больше $2j$ различных собственных фаз. При общем сдвиге вероятность попадания хотя бы одной из них в фиксированное микроскопическое окно длины $L$ не больше $2jL/N_j\to0$. Поэтому вдоль этой подпоследовательности слабый локальный предел пуст, а не Sine₂.

Также для кратных $2j$, $|\operatorname{Tr}M_{N_j}^m|^2=N_j^2$.
Выберем $c_w=\min_{1/4\le t\le1/2}w(t)>0$. В этом интервале не меньше $N_j/(8j)-2$ таких кратных. Отсюда
$$
\Delta_{2,N_j}(b_*)\ge
 c_w\bigl(N_j/(8j)-2\bigr)-2\|w\|_\infty
                                   \longrightarrow+\infty .
$$
Положительное отклонение момента само по себе не используется как критерий опровержения слабого закона: пустой слабый предел доказан отдельно.

**ДОКАЗАНО:** перечисленные свойства окон совместимы с пустым локальным пределом и огромными исходными следами.
**OUTLINE:** их можно использовать как технические входы при дополнительной оценке смешанных фаз.
**НЕДОКАЗАНО:** такая дополнительная оценка для исходного положительного $\tau$. Простой вывод из нормовых свойств исключён этим контрольным примером; вся оконная программа не исключена.

### VIIIf.4. Проверка второго маршрута: монотонность сглаженного следа

Положительность Fourier-коэффициентов маски обеспечивает сжатие матричной нормы. Она не обеспечивает монотонность $|\operatorname{Tr}B^m|^2$.

Пусть $\omega^2+\omega+1=0$, $|\omega|=1$, и
$$
U=\begin{pmatrix}
 (1+\omega)/2&(1-\omega)/2&0\\
 (1-\omega)/2&(1+\omega)/2&0\\
 0&0&\omega^2
 \end{pmatrix}.
$$
Это унитарная матрица: первые два собственных значения равны $1,\omega$,
третье — $\omega^2$. В частности, $\operatorname{Tr}U^2=0$.

Для $0\le q\le1$ возьмём циклическую маску $h_q=(1,q,q)$ и положим $B_q=h_q\odot U$. Её Fourier-коэффициенты равны
$$
\frac{1+2q}{3},\qquad\frac{1-q}{3},\qquad\frac{1-q}{3},
$$
то есть неотрицательны и суммируются в 1. Поэтому $\|B_q\|\le1$.
Но точное вычисление даёт
$$
\operatorname{Tr}B_q^2=\frac{3\omega}{2}(1-q^2),\qquad
 |\operatorname{Tr}B_q^2|^2=\frac94(1-q^2)^2.          \tag{VIIIf.4.1}
$$
Усиление сглаживания, то есть уменьшение $q$ от 1, увеличивает этот спектральный момент от нуля. В частности, универсальная монотонная оценка, которая позволила бы снять вес из оценки сглаженных следов, неверна.

Обратное направление монотонности также не является универсальным. Для той же матрицы
$$
\operatorname{Tr}B_q^3=\tfrac34(1+3q^2),
$$
и его квадрат модуля уменьшается при уменьшении $q$. Даже при том же порядке $m=2$ матрица, переставляющая первые две координаты и фиксирующая третью, даёт
$\operatorname{Tr}B_q^2=1+2q^2$, что имеет противоположную монотонность по сравнению с (VIIIf.4.1).

Это конечный контрпример к общему шагу доказательства. Он не принадлежит исходной семье и не опровергает специальную, пока не доказанную оценку конкретной исходной $w$-суммы.

**ДОКАЗАНО:** (VIIIf.4.1) и отрицательный ответ на сформулированный общий тезис монотонности.
**OUTLINE:** специальная монотонность или иной контроль исходного семейства потребовали бы отдельного аргумента.
**НЕДОКАЗАНО:** такой аргумент для TRACE-005 не найден.

### VIIIf.5. Самопроверка и действующий итог

Действующая цель не изменена: исходный $U_N=e^{i10^{-80}NA_N}M_N$, все нечётные $N$, общий сдвиг как единственная случайность. Нужны исходный когерентный предел $-\delta_*$ и затем достаточные тесты всех порядков либо прямой ограниченный Laplace-закон.

Точное восстановление веса выполнено. Количественная оценка исходной смешанной следовой суммы (VIIIf.1.7) не получена. Поэтому этот этап не объявляется продвижением в доказательстве основного парного предела: получены тождества и проверки того, почему два простых продолжения CG1 не закрывают цель.

Самопроверка проведена отдельно после вывода:

- в (VIIIf.1.2) сохранён порядок некоммутирующих множителей;
- в (VIIIf.1.3) стоит $\operatorname{Tr}(W^*W)$, а не произведение двух следов;
- в (VIIIf.1.5) использована только положительная сумма одинаковых историй;
- $I^{\mathrm{win}}$ не отождествляется с исходным вращательным вкладом;
- все Fourier-метки и все сдвиги окон сохранены в (VIIIf.2.1);
- размер $N_j$ нечётен, период (VIIIf.3.1) проектный, а коэффициент момента учитывает только кратные периода;
- параметр $t=0$ в контрольном примере не заменяет исходного положительного времени;
- конечный трёхмерный пример исключает общий шаг, а не исходный локальный закон.

Независимого рецензирования и формальной верификации не было. Внешние математические источники не привлекались; новизна не устанавливалась. Wolfram проверил конечный рациональный пример разбиения на окна, точный трёхмерный контрпример и четыре целых размера Пелля. Общие утверждения доказаны выше; конечные проверки не доказывают требуемую асимптотику. Для удалённых символьных вызовов сохранены полные входы, ответы и сообщённая версия ядра; отдельный локальный вычислительный манифест v2 не заявляется.

Продолжение остаётся открытым ровно в оценке смешанной следовой суммы исходного оператора. Простая замена её суммой одинаковых историй, нормовое сжатие восстановленного канала и универсальное монотонное снятие веса не обоснованы. Первые два шага проверены точными тождествами, последний опровергнут конкретной матрицей. Это не утверждение о невозможности других методов.

#### VIIIf.5.1. Точный символьный вход и ответ

```wolfram
ClearAll[w,q,x,y,ell];
nn=3; v={1,2,3};
uu=IdentityMatrix[nn]-2 Outer[Times,v,v]/(v.v);
gg={1,1/2,1/2}; ss=Total[gg]; hh=gg.gg;
bb=Table[Table[gg[[1+Mod[x-y-ell,nn]]] uu[[x+1,y+1]],
 {x,0,nn-1},{y,0,nn-1}],{ell,0,nn-1}];
ww=Flatten[Table[bb[[j]].bb[[k]],{j,nn},{k,nn}],1];
diag=Total[(Tr[Transpose[#].#]&)/@ww];
coherent=Tr[Transpose[Total[ww]].Total[ww]];
red[p_]:=PolynomialRemainder[Expand[p],w^2+w+1,w];
star[a_]:=Map[red[#/.w->w^2]&,Transpose[a],{2}];
uc={{(1+w)/2,(1-w)/2,0},{(1-w)/2,(1+w)/2,0},{0,0,w^2}};
bc=Table[If[j==k,1,q]uc[[j,k]],{j,3},{k,3}];
p2=red[Tr[bc.bc]];
square=Factor[red[p2*(p2/.w->w^2)]];
<|"kernelVersion"->$Version,
"reconstruction"->TrueQ[Total[bb]==ss uu],
"leftFrame"->TrueQ[Total[(Transpose[#].#&)/@bb]==hh IdentityMatrix[nn]],
"rightFrame"->TrueQ[Total[(#.Transpose[#]&)/@bb]==hh IdentityMatrix[nn]],
"twoStepReconstruction"->TrueQ[Total[ww]==ss^2 uu.uu],
"twoStepFrame"->TrueQ[Total[(Transpose[#].#&)/@ww]==hh^2 IdentityMatrix[nn]],
"twoStepDiagonalHS"->diag,"twoStepCoherentHS"->coherent,
"normalizedCrossHS"->(coherent-diag)/(nn ss^4),
"clockUnitary"->TrueQ[Map[red,star[uc].uc-IdentityMatrix[3],{2}]==ConstantArray[0,{3,3}]],
"clockTrace2AtNoFilter"->red[Tr[uc.uc]],
"clockFilteredTrace2"->p2,"clockFilteredTrace2Squared"->square|>
```

```json
{
  "content": [
    {
      "type": "text",
      "text": "Out[1]= <|\"kernelVersion\" -> \"15.0.1 for Linux x86 (64-bit) (July 2, 2026)\", \"reconstruction\" -> True, \"leftFrame\" -> True, \"rightFrame\" -> True, \"twoStepReconstruction\" -> True, \"twoStepFrame\" -> True, \"twoStepDiagonalHS\" -> 27/4, \"twoStepCoherentHS\" -> 48, \"normalizedCrossHS\" -> 55/64, \"clockUnitary\" -> True, \"clockTrace2AtNoFilter\" -> 0, \"clockFilteredTrace2\" -> (3/2 - (3*q^2)/2)*w, \"clockFilteredTrace2Squared\" -> (9*(-1 + q)^2*(1 + q)^2)/4|>"
    }
  ],
  "structuredContent": null,
  "isError": false
}
```

#### VIIIf.5.2. Точный символьный вход и ответ

```wolfram
ClearAll[a,b,j,ss];
ss={{3,4},{2,3}};
table=Table[
 pow=MatrixPower[ss,j];
 nn=pow[[2,1]]/2;
 <|"j"->j,"N"->nn,"oddN"->OddQ[nn],
   "scalarAtJ"->TrueQ[Mod[pow,nn]==Mod[pow[[1,1]],nn] IdentityMatrix[2]],
   "returnAt2J"->TrueQ[Mod[MatrixPower[ss,2j],nn]==IdentityMatrix[2]]|>,
 {j,{3,5,7,9}}];
<|"kernelVersion"->$Version,"exactPellFixtures"->table|>
```

```json
{
  "content": [
    {
      "type": "text",
      "text": "Out[1]= <|\"kernelVersion\" -> \"15.0.1 for Linux x86 (64-bit) (July 2, 2026)\", \"exactPellFixtures\" -> {<|\"j\" -> 3, \"N\" -> 35, \"oddN\" -> True, \"scalarAtJ\" -> True, \"returnAt2J\" -> True|>, <|\"j\" -> 5, \"N\" -> 1189, \"oddN\" -> True, \"scalarAtJ\" -> True, \"returnAt2J\" -> True|>, <|\"j\" -> 7, \"N\" -> 40391, \"oddN\" -> True, \"scalarAtJ\" -> True, \"returnAt2J\" -> True|>, <|\"j\" -> 9, \"N\" -> 1372105, \"oddN\" -> True, \"scalarAtJ\" -> True, \"returnAt2J\" -> True|>}|>"
    }
  ],
  "structuredContent": null,
  "isError": false
}
```

#### VIIIf.5.3. Точный символьный вход и ответ

```wolfram
ClearAll[w,q];
red[p_]:=PolynomialRemainder[Expand[p],w^2+w+1,w];
uc={{(1+w)/2,(1-w)/2,0},{(1-w)/2,(1+w)/2,0},{0,0,w^2}};
bc=Table[If[j==k,1,q]uc[[j,k]],{j,3},{k,3}];
us={{0,1,0},{1,0,0},{0,0,1}};
bs=Table[If[j==k,1,q]us[[j,k]],{j,3},{k,3}];
<|"kernelVersion"->$Version,
"sameClockFilteredTrace3"->Factor[red[Tr[MatrixPower[bc,3]]]],
"swapFilteredTrace2"->Tr[bs.bs]|>
```

```json
{
  "content": [
    {
      "type": "text",
      "text": "Out[1]= <|\"kernelVersion\" -> \"15.0.1 for Linux x86 (64-bit) (July 2, 2026)\", \"sameClockFilteredTrace3\" -> (3*(1 + 3*q^2))/4, \"swapFilteredTrace2\" -> 1 + 2*q^2|>"
    }
  ],
  "structuredContent": null,
  "isError": false
}
```


## VIIIg. Временные интенсивности и проверка секулярного механизма

### VIIIg.1. OF1: точное ограничение на временные интенсивности

Пусть $U$ — произвольная унитарная матрица размера $N\ge2$. Различаем
$$
P^{[t]}(x,y)=|(U^t)_{xy}|^2,\qquad P=P^{[1]},\qquad
 J(x,y)=1/N.
$$
В общем случае $P^{[t]}\ne P^t$. Все нормы Гильберта–Шмидта ниже ненормированы; $\|X\|_{\mathrm{HS}}^2=\sum_{x,y}|X_{xy}|^2$.

**Теорема OF1.** Для каждого целого $L\ge1$
$$
\sum_{t=1}^{L-1}(L-t)\|P^{[t]}-J\|_{\mathrm{HS}}^2
 \ge \frac{L(N-1)}2\left(\frac{L}{N+1}-1\right).       \tag{VIIIg.1.1}
$$
При отрицательной правой части сохраняется очевидная нижняя граница 0. В частности, при $L=2N$
$$
\boxed{\frac1{N^2}\sum_{t=1}^{2N-1}(2N-t)
       \|P^{[t]}-J\|_{\mathrm{HS}}^2
       \ge \frac{(N-1)^2}{N(N+1)}.}                  \tag{VIIIg.1.2}
$$
Ни усреднение по матрицам, ни случайные фазы здесь не вводятся. Оценки равномерны по всем унитарным $U$, всем $N$ и указанным временам.

**Доказательство.** Работаем в комплексном пространстве матриц с нулевым следом с HS-скалярным произведением. Его размерность $n=N^2-1$. Пусть $\mathcal E$ — подпространство диагональных матриц с нулевым следом, $d=\dim\mathcal E=N-1$, а $\Pi$ — ортогональный проектор на него. Обозначим
$$
\mathcal T(X)=UXU^*,\qquad
 \Pi_j=\mathcal T^j\Pi\mathcal T^{-j},\qquad
 F_L=\sum_{j=0}^{L-1}\Pi_j.
$$
Оператор $\mathcal T$ унитарен, поэтому каждый $\Pi_j$ — ортогональный проектор ранга $d$. Сжатие $\Pi\mathcal T^t\Pi$ на диагональное подпространство есть $P^{[t]}$ на $\mathbf1^\perp$. На всём $\mathbb C^N$ его продолжение нулём равно $P^{[t]}-J$. Следовательно,
$$
\operatorname{Tr}(\Pi_i\Pi_j)
   =\|\Pi\mathcal T^{j-i}\Pi\|_{\mathrm{HS}}^2
   =\|P^{[|j-i|]}-J\|_{\mathrm{HS}}^2\quad(i\ne j). \tag{VIIIg.1.3}
$$
Для отрицательных времён используется $P^{[-t]}=(P^{[t]})^T$, что сохраняет HS-норму. Поэтому
$$
\operatorname{Tr}F_L=Ld,\qquad
 \operatorname{Tr}F_L^2=Ld+
       2\sum_{t=1}^{L-1}(L-t)\|P^{[t]}-J\|_{\mathrm{HS}}^2.
$$
Если $\mu_1,\ldots,\mu_n\ge0$ — собственные значения $F_L$, то
$(\sum\mu_j)^2\le n\sum\mu_j^2$. Подставляя $d/n=1/(N+1)$, получаем (VIIIg.1.1). Формула (VIIIg.1.2) — её точная специализация. □

Механизм оценки — ограниченная размерность пространства наблюдаемых: $L$ перенесённых диагональных подпространств имеют суммарную размерность $L(N-1)$, тогда как доступная размерность равна $N^2-1$. Порог их возможной взаимной ортогональности равен $N+1$. Это даёт точный временной масштаб, но само по себе не задаёт статистику собственных фаз.

### VIIIg.2. OF2: применение к исходному фиксированному параметру

**Теорема OF2.** Пусть $\rho_N=\|P_N-J_N\|<1$, где норма операторная. Положим
$$
\mathcal R_N=\frac1{N^2}\sum_{t=1}^{2N-1}(2N-t)
     \|P_N^{[t]}-P_N^t\|_{\mathrm{HS}}^2,
 \quad a_N=\frac{N-1}{\sqrt{N(N+1)}},
 \quad b_N=\sqrt{\frac{2(N-1)}N}\,
                 \frac{\rho_N}{\sqrt{1-\rho_N^2}}.
$$
Тогда точно
$$
\mathcal R_N\ge(a_N-b_N)_+^2.  \tag{VIIIg.2.1}
$$
В частности, для исходных $U_N=e^{i\tau NA_N}M_N$, $\tau=10^{-80}$, по разрешённому входу FM-021,
$$
\boxed{\liminf_{\substack{N\to\infty\\N\ \mathrm{odd}}}\mathcal R_N
 \ge \left(1-\frac{\sqrt2\,10^{-64}}{\sqrt{1-10^{-128}}}\right)^2
 \ge 1-3\cdot10^{-64}.}                            \tag{VIIIg.2.2}
$$
Это утверждение о настоящих степенях исходной матрицы при исходном параметре. Его вес $2N-t$ и его наблюдаемая $\|P_N^{[t]}-P_N^t\|_{\mathrm{HS}}^2$ отличаются от спектрального теста с весом $w(t/N)$.

**Доказательство.** Дважды стохастическая $P$ удовлетворяет $PJ=JP=J$, поэтому $P^t-J=(P-J)^t$. На $\mathbf1^\perp$ размерность равна $N-1$, и
$$
\|P^t-J\|_{\mathrm{HS}}^2\le(N-1)\rho^{2t}.
$$
Отсюда
$$
\frac1{N^2}\sum_{t=1}^{2N-1}(2N-t)\|P^t-J\|_{\mathrm{HS}}^2
 \le\frac{2(N-1)}N\frac{\rho^2}{1-\rho^2}=b_N^2.    \tag{VIIIg.2.3}
$$
Применяем обратное неравенство треугольника в прямой сумме HS-пространств с весами $(2N-t)/N^2$, используя (VIIIg.1.2). Получается (VIIIg.2.1). Если $\limsup\rho_N\le r<1$, предельная нижняя оценка равна $(1-\sqrt2r/\sqrt{1-r^2})_+^2$. Подставляем $r=10^{-64}$. Для $0\le r\le1/3$ имеем $\sqrt2r/\sqrt{1-r^2}\le3r/2$, откуда последнее неравенство (VIIIg.2.2). □

Таким образом, замена всей временной последовательности интенсивностей исходной квантовой динамики степенями её одношагового интенсивностного канала теряет вклад с явной ненулевой нижней границей (VIIIg.2.2). Утверждения о $P_N^t$ из прежних частей сохраняются. Они относятся к другому оператору, чем $|U_N^t|^2$.

### VIIIg.3. OF3: что означало бы точное исчезновение всех ранних возвратов

**Теорема OF3.** Если для некоторой унитарной $U$ размера $N\ge2$
$$
P^{[t]}=J\quad(1\le t\le N),           \tag{VIIIg.3.1}
$$
то $U$ имеет простой спектр и существует $|\lambda_0|=1$, для которого
$$
\operatorname{spec}U=\{\lambda_0 e^{2\pi i j/(N+1)}:1\le j\le N\}.
                                                               \tag{VIIIg.3.2}
$$
В частности, $U^{N+1}=\lambda_0^{N+1}I$. При нечётном $N$, не являющемся квадратом, условие (VIIIg.3.1) вообще невозможно.

**Доказательство спектральной жёсткости.** Из (VIIIg.1.3) следует, что $\mathcal E_j=\mathcal T^j\mathcal E$, $0\le j\le N$, взаимно ортогональны. Сумма их размерностей равна $N^2-1$, поэтому это полное ортогональное разложение пространства матриц с нулевым следом. Унитарность $\mathcal T$ даёт $\mathcal T\mathcal E_N=\mathcal E_0$: образ последнего подпространства ортогонален $\mathcal E_1,\ldots,\mathcal E_N$.

Следовательно, $V=U^{N+1}$ сопряжением сохраняет все диагональные матрицы. Оно переставляет их минимальные проекторы $E_{xx}$; значит, $V$ — мономиальная матрица. Пусть её перестановка имеет $c$ циклов. На $\mathcal E$ неподвижное подпространство $\operatorname{Ad}_V$ имеет размерность $c-1$.

При циклическом ортогональном разложении выше любой неподвижный $X$ оператора $\mathcal T$ единственным образом имеет вид
$$
X=\sum_{j=0}^{N}\mathcal T^j x,
 \qquad x\in\mathcal E,\quad\mathcal T^{N+1}x=x.
$$
Это проверяется сравнением компонент по $\mathcal E_j$. Поэтому $\dim\ker(\mathcal T-I)=c-1$. С другой стороны, если кратности собственных значений $U$ равны $m_j$, размерность коммутанта с нулевым следом равна $\sum_jm_j^2-1\ge N-1$. Получаем $c=N$ и $\sum_jm_j^2=N$. Значит, перестановка тождественна, а все кратности равны 1.

Теперь $V$ диагональна и коммутирует с $U$. Из $P^{[1]}=J$ все элементы $U$ ненулевые, поэтому $(V_{xx}-V_{yy})U_{xy}=0$ требует скалярности $V$. Среди $N+1$ корней этого скаляра $U$ имеет ровно $N$ различных; обозначив отсутствующий корень через $\lambda_0$, получаем (VIIIg.3.2).

Если $N$ нечётно, положим $H=(U/\lambda_0)^{(N+1)/2}$. По (VIIIg.3.2) это эрмитова унитарная матрица со следом $-1$, а по (VIIIg.3.1) все её элементы имеют модуль $N^{-1/2}$. Диагональные элементы вещественны, значит, равны $\pm N^{-1/2}$. Их сумма $-1$ требует, чтобы $\sqrt N$ была целой. Это исключает все нечётные неквадраты. □

Имеется и количественное тождество устойчивости без спектрального вывода. Для
$$
S_N=\sum_{t=1}^{N}(N+1-t)\|P^{[t]}-J\|_{\mathrm{HS}}^2
$$
точно
$$
\|F_{N+1}-I\|_{\mathrm{HS}}^2=2S_N,
 \qquad N-\|P^{[N+1]}\|_{\mathrm{HS}}^2\le4S_N.      \tag{VIIIg.3.3}
$$
Действительно, первое равенство следует из доказательства OF1, а
$\mathcal T F_{N+1}\mathcal T^{-1}-F_{N+1}=\Pi_{N+1}-\Pi_0$.
По неравенству треугольника квадрат нормы правой части не больше $8S_N$. Он же равен $2(N-\|P^{[N+1]}\|_{\mathrm{HS}}^2)$, что доказывает вторую оценку.

Для исходного $\tau$ точная скалярность $U_N^{N+1}$ исключена E4 при $N\ge19$. Это даёт только строгую ненулевость $S_N$, а не равномерный количественный зазор. Утверждение OF3 нельзя обратить: один лишь спектр (VIIIg.3.2) ещё не обеспечивает плоскость всех первых $N$ степеней.

### VIIIg.4. SC1: точное конечномерное сокращение в характеристическом многочлене

Пусть $e_k=e_k(U)$, $e_0=1$, $e_k=0$ при $k>N$. Введём формальные ряды
$$
E(z)=\det(I+zU)=\sum_{k=0}^{N}e_kz^k,\qquad
 H(z)=E(-z)^{-1}=\sum_{k\ge0}h_kz^k,
$$
и явно определённые крюковые многочлены
$$
q_{a,b}=\sum_{j=0}^{b}(-1)^j h_{a+j}e_{b-j},
                   \qquad a\ge1,\ b\ge0.            \tag{VIIIg.4.1}
$$
Здесь используется только арифметика формальных рядов; сходимость при $|z|=1$ не нужна.

**Лемма SC1.** Для любого $m\ge1$
$$
q_{a,b}=0\ (b\ge N),\qquad
 \boxed{\operatorname{Tr}U^m=
       \sum_{b=0}^{\min(m-1,N-1)}(-1)^bq_{m-b,b}.}   \tag{VIIIg.4.2}
$$

**Доказательство.** При $b\ge N$ правая часть (VIIIg.4.1) равна
$(-1)^b\sum_{k=0}^{N}(-1)^ke_kh_{a+b-k}=0$ по $E(-z)H(z)=1$, так как $a+b>0$. Если в сумме по $b$ временно оставить все $0\le b<m$, коэффициент при $e_kh_{m-k}$ равен $(-1)^k(m-k)$. Это коэффициент $z^{m-1}$ в $E(-z)H'(z)$. Дифференцируя формальное произведение по собственным значениям, получаем
$$
E(-z)H'(z)=\sum_{m\ge1}\operatorname{Tr}U^m z^{m-1}.
$$
Теперь удаляем тождественно нулевые $b\ge N$. □

Число оставшихся слагаемых равно $\min(m,N)$, но квадрат модуля следа содержит все их смешанные произведения. Число слагаемых не оценивает эти произведения. Полученная формула сохраняет точное конечномерное обрезание и не имеет растущего Taylor-остатка; недостаёт фазовой оценки для исходной матрицы.

### VIIIg.5. SC2: даже все секулярные вторые моменты не определяют локальный закон

**Лемма о Haar-эталоне.** Если $V$ имеет закон Haar $U(N)$, то
$$
\mathbb E e_k(V)\overline{e_l(V)}=\delta_{kl}
                         \quad(0\le k,l\le N).      \tag{VIIIg.5.1}
$$
Это утверждение здесь можно доказать без формулы интегрирования по собственным значениям. Разложим $e_k$ в сумму главных миноров. Инвариантность Haar при умножении слева на произвольную диагональную унитарную матрицу убивает перекрёстные произведения миноров с разными наборами строк. Для фиксированного набора строк $I$, $|I|=k$, формула Коши–Бине и ортонормированность строк дают
$\sum_{|J|=k}|\det V_{I,J}|^2=1$.
Инвариантность при перестановке столбцов делает все $\binom Nk$ средних одинаковыми. Поэтому средний квадрат каждого главного минора равен $\binom Nk^{-1}$; сумма по $I$ равна 1. При $k\ne l$ общий фазовый множитель даёт ноль. Это доказывает (VIIIg.5.1), включая $k=0,N$.

