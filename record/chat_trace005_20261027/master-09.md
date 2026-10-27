Эта формула позволяет проверить всю следующую таблицу подстановкой рациональных углов. При использовании Fourier-таблицы вместо (VIIIo.4.3) надо сохранить Weyl-сдвиг r(q+1/2).

### VIIIo.5. RV4–RV5: исчерпывающие препятствия и полный централизатор

Для компактной таблицы пишем z=(a,b)/8 и beta=(bq,bp)/8. Все указанные z принадлежат Fix S². Прямые значения из (VIIIo.4.3) равны:

| (a,b) | T((a,b)/8) |
|---|---|
| (0,0) | $19606/125$ |
| (0,1) | $-20-172\sqrt2/125$ |
| (0,7) | $-20+28\sqrt2/125$ |
| (0,2) | $784/5$ |
| (0,4) | $19594/125$ |
| (4,0) | $-24306/125$ |
| (4,4) | $-24894/125$ |
| (4,2), (4,6) | $-984/5$ |
| (2,1) | $(-3060+87\sqrt2)/500$ |
| (6,1) | $(-2540+87\sqrt2)/500$ |

Из неё следуют все нужные различия Delta=T(z)−T(K_0 z). В строках со знаком ± разрешены оба знака независимо; e=0,1 означает оба случая из (VIIIo.3.6).

| e | j | sigma | (bq,bp) | (a,b) | Delta |
|---|---|---|---|---|---|
| 1 | 0 | +1 | (0,0) | (0,1) | $-8\sqrt2/5$ |
| 1 | 0 | −1 | (0,0) | (2,1) | $-26/25$ |
| 0 | 0 | −1 | (0,0) | (0,1) | $-8\sqrt2/5$ |
| 0,1 | 0 | ±1 | (0,4) | (4,0) | $588/125$ |
| 0,1 | 0 | ±1 | (4,0) | (0,4) | $44488/125$ |
| 0,1 | 0 | ±1 | (4,4) | (0,0) | $356$ |
| 0,1 | 1 | ±1 | (0,0) или (0,4) | (0,2) | $1768/5$ |
| 0,1 | 1 | ±1 | (4,0) | (4,4) | $-356$ |
| 0,1 | 1 | ±1 | (4,4) | (0,0) | $356$ |

Таблица покрывает все 16 классов обращателей и все 15 нетождественных классов централизатора. Непокрытый класс e=0,j=0,sigma=+1,beta=0 — тождественное отображение, которое исключать нельзя. Различие в каждом покрытом классе имеет модуль не меньше 26/25. По (VIIIo.4.1)
$$
\left|\operatorname{Tr}DF_t^2(h_tz)
       -\operatorname{Tr}DF_t^2(h_tK_0z)\right|
 \ge\left(24\pi\frac{26}{25}-2\cdot10^{12}t\right)t
                         >70t.                               \tag{VIIIo.5.1}
$$
Здесь использованы pi>3 и t≤10⁻¹⁴; оценка действует на всём открытом по t интервале, включая исходный tau, без выбора подпоследовательности.

След производной F² постоянен вдоль каждой орбиты из Fix F²: матрицы в двух её точках сопряжены посредством DF. Поэтому вынесенные в (VIIIo.3.6) итерации F^k не меняют проверяемый след. Если H — C¹-диффеоморфизм и HF=FH, то в периодической точке дифференцирование равенства HF²=F²H делает DF²(z_t) и DF²(H z_t) сопряжёнными. Они должны иметь одинаковый след, что противоречит (VIIIo.5.1) во всех 15 запрещённых классах.

**RV5 доказана:** остаётся ровно топологический класс K=S^k, beta=0. По точному сопряжению соответствующее отображение равно h_tS^kh_t^{-1}=F_t^k. Каждая такая итерация гладкая и действительно коммутирует с F_t. Это доказывает (VIIIo.1.1) в обе стороны.

Если R — C¹-обращатель, дифференцирование RF²=F⁻²R делает DF²(z_t) сопряжённой с DF⁻²(Rz_t). В точке периода, делящего два, последняя матрица обратна DF²(Rz_t). Определитель равен 1, поэтому для матрицы размера два след обратной совпадает со следом самой матрицы. Опять потребовалось бы равенство двух следов из (VIIIo.5.1). Все 16 классов исключены. **RV4 доказана**, то есть верно (VIIIo.1.2), включая обращатели, сохраняющие ориентацию и не являющиеся инволюциями.

Следствия: F_t не C¹-сопряжено S; любой C¹-элемент конечного порядка, коммутирующий с F_t, тождествен; C¹-корня H^d=F_t при целом d≥2 не существует. Для последнего H автоматически коммутирует с F_t, значит H=F_t^k; тогда S^{kd}=S на гомологиях, что невозможно при d≥2. Топологические обращатели при этом существуют по RV1–RV2 и имеют вид h_tKh_t^{-1}. Утверждение об их отсутствии без условия C¹ было бы неверным.

### VIIIo.6. RV6: прямая параметрическая устойчивость квантовой парной энергии

Следующее утверждение относится непосредственно к квантовому U_N(t)=exp(itNA_N)M_N, а не к классическим производным. Как в PR1, положим
$$
\mathcal R_{N,t}(s)=\frac1{N^2}\sum_{j,k}
  P_{e^{-s/N}}(\vartheta_j(t)-\vartheta_k(t)),\quad
 P_r(\omega)=\frac{1-r^2}{1-2r\cos\omega+r^2}.
$$
Фазы vartheta здесь в радианах. **RV6.** Для всех допустимых нечётных N≥3, всех s>0 и вещественных t,t_0:
$$
\left|\partial_t\log\mathcal R_{N,t}(s)\right|
        \le\frac{2BN}{\sinh(s/N)}\le\frac{2BN^2}{s},
 \quad B=59/50,                                               \tag{VIIIo.6.1}
$$
$$
e^{-2BN^2|t-t_0|/s}\le
   \frac{\mathcal R_{N,t}(s)}{\mathcal R_{N,t_0}(s)}
                 \le e^{2BN^2|t-t_0|/s}.                     \tag{VIIIo.6.2}
$$
Кратности спектра не исключаются; конечная сумма энергии гладка по t независимо от возможности гладко выбрать отдельные собственные векторы. Это относительная устойчивость; из неё не следует ограниченность энергии по N.

Доказательство без предположения простоты. На HS-пространстве Q=Ad_U и H=ad_A эрмитов, норма H не больше 2B. Точно Q'=iNHQ. Абсолютно сходящийся Laurent-ряд P_r и его производной разрешает почленное дифференцирование следа. Цикличность следа даёт
$$
\partial_t\mathcal R_{N,t}(s)
              =\frac N{N^2}\operatorname{Tr}_{\mathrm{HS}}
                         [H P'_r(Q)].                        \tag{VIIIo.6.3}
$$
Здесь P'_r(Q) — самосопряжённый оператор со значениями производной по углу на спектре Q. Нормировка N⁻² сохраняется. Для omega∈R
$$
\frac{|P'_r(\omega)|}{P_r(\omega)}
 =\frac{2r|\sin\omega|}{1+r^2-2r\cos\omega}
                         \le\frac{2r}{1-r^2}.                \tag{VIIIo.6.4}
$$
После возведения в квадрат нужное неравенство сводится к точному сертификату
$$
(1+r^2-2rc)^2-(1-r^2)^2(1-c^2)
                        =[2r-(1+r^2)c]^2\ge0,
 \qquad c=\cos\omega.
$$
Следовательно, модуль (VIIIo.6.3) не больше 2BN·2r/(1−r²), умноженного на энергию. При r=exp(−s/N) это первая граница (VIIIo.6.1); sinh x≥x даёт вторую. Интегрирование логарифмической производной доказывает (VIIIo.6.2).

Степень N² в общем случае ограниченных генераторов улучшить нельзя. Это утверждение об общем классе, не о точной исходной семье. Для нечётного N=2n+1 возьмём два диагональных блока кратностей n,n+1, генератор +B и −B и начальный фазовый зазор omega=s/N. Тогда при t=0
$$
E_N=a_N P_r(0)+b_N P_r(s/N),\quad
 a_N=\frac{n^2+(n+1)^2}{N^2},\quad
 b_N=\frac{2n(n+1)}{N^2},
$$
$$
E_N'=2BNb_N P'_r(s/N),\quad
 \frac{E_N}{N}\to\frac3{2s},\quad
 \frac{\partial_t\log E_N}{BN^2}\to-\frac2{3s}.              \tag{VIIIo.6.5}
$$
Для (VIIIo.6.5) достаточно рядов exp(−sx)=1−sx+O_s(x²), sin(sx)=sx+O_s(x³), cos(sx)=1−s²x²/2+O_s(x⁴) при x=1/N: знаменатель P равен 2s²x²+O_s(x³), а числитель 2sx+O_s(x²). Константы остатков равномерны по x в фиксированном малом интервале при каждом фиксированном s>0; равномерность по s→0 или s→∞ не утверждается.

В частности, для фиксированного s окна o(N⁻²) дают относительное изменение o(1) по (VIIIo.6.2). Эта оценка не позволяет переносить линейные резонансы t=0 в фиксированную конечную точку tau по всем N: показатель tau N² не мал. Она также не даёт фазовой статистики при tau. Двухблочная модель из (VIIIo.6.5) не объявляется контрпримером к исходной задаче.

### VIIIo.7. Что закрыто, а что осталось

**ДОКАЗАНО:**

- RV1: точное топологическое сопряжение, построенное ограниченным Green-оператором, с явной оценкой 600t.
- RV2: все топологические классы централизатора и обращателей, включая ориентацию +1 и неинволютивные обращения.
- RV3: первая вариация следа периода, делящего два, и остаток 10¹²t², равномерный по всему указанному интервалу t.
- RV4–RV5: отсутствие всех C¹-обращателей, полный C¹-централизатор из одних итераций, отсутствие C¹-сопряжения с S и собственных гладких корней.
- RV6: относительная устойчивость настоящей невзвешенной парной энергии, без условия простоты; порядок N² резок в общем классе ограниченных генераторов.

**OUTLINE:**

- Маршрут скрытой классической гладкой симметрии доведён до окончательного отрицательного ответа для обращения и до полной классификации централизатора. Для этого частного геометрического вопроса U-списка нет.
- Топологическое сопряжение существует, но его нельзя использовать как гладкое каноническое сопряжение для прямого переноса линейного квантового спектра. Это конкретное препятствие данной конструкции, не запрет иных методов квантового сравнения.
- RV6 точно указывает масштаб, на котором имеющийся общий нормовый контроль замораживает параметр. Утверждение о правильном значении энергии в таком окне не получено.

**НЕДОКАЗАНО:**

- U-RV1: локальный закон положительного HS-оператора из PR2 именно для исходного U_N(tau); даже O(1) вместо нынешней верхней оценки O(N/log N) не доказано.
- U-RV2: исходная Heisenberg-компенсация Y с пределом −delta_* и все фиксированные высшие порядки.
- U-RV3: какой-либо корректный вывод квантового Sine₂ из вычисленного гладкого централизатора. Такой общей импликации здесь нет и она не предполагается.

Самый трудный шаг основной задачи не изменился: устранение геометрических симметрий не вычисляет когерентную сумму на m порядка N. Предыдущие интенсивностные, арифметические и классические оценки не определяют её квантовый член порядка 1/N. Здесь закрыта полноценная структурная подзадача о конкретном фиксированном отображении, однако назвать её решением спектрального предела было бы логической ошибкой. Произвольная антиунитарная операция, определённая в собственном базисе конечной унитарной матрицы, также не исключается этим геометрическим результатом.

### VIIIo.8. Полные вычислительные записи и воспроизведение

Теорема RV1–RV5 следует из полного доказательства, включая классификацию всех гомеоморфизмов после сопряжения и единый остаток. Вычисления проверяют только явно конечный алгебраический дискриминатор и константы. Исторически первая локальная заготовка потребовала отсутствующий SymPy; после этого вычисление переписано на стандартные рациональные типы Python. Эти неудавшиеся запуски не являются подтверждением каких-либо лемм. Ни малые квантовые N, ни спектр при другом tau здесь не тестировались.

Текущий локальный скрипт исполнялся без сторонних библиотек. Его манифест v2 содержит наблюдавшиеся до и после хеши, точную команду, версию Python, время, stdout и пустой stderr, объявленный до исполнения результат. Статус completed и нулевой код означают выполнение конечных проверок. Манифест проверен текущим validate_manifest.py с --root проекта. Манифест сообщает отсутствие доступной Git-ревизии; это самостоятельное вычисление, а не изменение репозитория.

Проверены все 32 точки Fix S² и все 196 точек Fix S³, по 16 классов обращателей; при m=2 также 16 классов централизатора. Проверка делимости обратной целой решётки гарантирует, что выбранные сетки покрывают все соответствующие точки. Неравенство в циклотомическом поле проверяется точным ненулевым вектором рациональных коэффициентов. Приближённые вещественные значения используются только для выбора одного из уже точно ненулевых свидетелей; они не определяют наличие препятствия. Все обращающие классы имеют несовпадение; у централизатора при m=2 единственный класс без несовпадения — тождественный.

Полный воспроизводимый код; команда: python3 output/trace005_periodic_symmetry_verify.py.

```python
"""Exact finite discriminator, not an asymptotic spectral test.

Contract: for m=2,3 and all 16 affine reversal classes modulo S iterates,
plus all 16 centralizer classes at m=2,
compute the first parameter derivative of Tr DF_t^m at labeled S-periodic
points, using the literal Weyl symbol. Arithmetic is in Q(zeta_D).
Nonzero differences obstruct a C1 reverser only after the accompanying
uniform remainder and conjugacy arguments have been proved.
Command: python3 output/trace005_periodic_symmetry_verify.py
"""
from fractions import Fraction as Q
from pathlib import Path
from math import lcm,pi
from cmath import exp
import json

ROOT=Path(__file__).resolve().parents[1]
S=((3,4),(2,3))
horizontal={1:(Q(1,20),Q(-1,200)),2:(Q(0),Q(-1,400)),
5:(Q(0),Q(-1,800)),6:(Q(-1,40),Q(-1,400)),
7:(Q(9,20),Q(0)),8:(Q(-1,40),Q(1,400)),9:(Q(0),Q(1,800))}
coeff={}
for k,(a,b) in horizontal.items():
    coeff[k,0]=(a,b); coeff[-k,0]=(a,-b)
r={0:Q(1),1:Q(1,2),-1:Q(1,2),6:Q(-1,4),-6:Q(-1,4),
   7:Q(-1,2),-7:Q(-1,2),8:Q(-1,4),-8:Q(-1,4)}
for k,v in r.items():
    c=v*(1 if k%2==0 else -1)/1000
    coeff[k,1]=(-3*c,-4*c)
    coeff[k,-1]=(-3*c,4*c)

def run(m,d,mode='reverse'):
    D=lcm(d,4)
    ph={8:[1,0,0,0,1],28:[1,0,-1,0,1,0,-1,0,1,0,-1,0,1]}[D]
    ph=list(map(Q,ph));deg=len(ph)-1
    def reduce(a):
        a=list(a)+[Q(0)]*max(0,deg-len(a))
        for j in range(len(a)-1,deg-1,-1):
            c=a[j]
            if c:
                for k in range(deg): a[j-deg+k]-=c*ph[k]
        return tuple(a[:deg])
    powers=[]
    for j in range(D):
        a=[Q(0)]*D;a[j]=Q(1);powers.append(reduce(a))
    def value(z):
        result=[Q(0)]*deg; a,b=z
        for j in range(m):
            for (k,l),(u,v) in coeff.items():
                exponent=((k*a+l*b)*(D//d))%D
                factor=2*k*k-l*l
                for power,c in ((exponent,u),(exponent+D//4,v)):
                    for i,t in enumerate(powers[power%D]): result[i]+=factor*c*t
            a,b=(3*a+4*b)%d,(2*a+3*b)%d
        return tuple(result)
    A=((1,0),(0,1))
    for _ in range(m):
        A=tuple(tuple(sum(A[i][k]*S[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    A=tuple(tuple(A[i][j]-(i==j) for j in range(2)) for i in range(2))
    determinant=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    assert all((d*x)%determinant==0 for row in A for x in row), 'grid must cover inverse-lattice points'
    points=[(a,b) for a in range(d) for b in range(d)
            if (A[0][0]*a+A[0][1]*b)%d==0
            and (A[1][0]*a+A[1][1]*b)%d==0]
    assert len(points)==abs(determinant)
    values={z:value(z) for z in points}
    classes=[]
    for parity in (0,1):
      for sign in (1,-1):
        for tq in (0,d//2):
            for tp in (0,d//2):
                mismatches=[]
                for z in points:
                    eta=-1 if mode=='reverse' else 1
                    target=((sign*(z[0]+2*parity*eta*z[1])+tq)%d,
                            (sign*(parity*z[0]+eta*z[1])+tp)%d)
                    delta=tuple(a-b for a,b in zip(values[z],values[target]))
                    if any(delta):
                        zz=sum(float(c)*exp(2j*pi*i/D) for i,c in enumerate(delta))
                        mismatches.append({'z':z,'target':target,
                            'delta_basis':[str(t) for t in delta],
                            'delta_numeric_real':zz.real,'delta_numeric_imag':zz.imag})
                classes.append({'parity':parity,'sign':sign,'translation_grid':[tq,tp],
                                'mismatch_count':len(mismatches),
                                'witness':max(mismatches,key=lambda z:abs(z['delta_numeric_real'])) if mismatches else None})
    return {'m':m,'mode':mode,'grid_denominator':d,'field_order':D,'phi_ascending':list(map(str,ph)),
            'point_count':len(points),'expected_point_count':abs(A[0][0]*A[1][1]-A[0][1]*A[1][0]),
            'classes':classes,'all_sixteen_classes_distinguished':all(c['witness'] for c in classes)}

result={'assertion_tested':__doc__,'results':[run(2,8),run(3,14),run(2,8,'centralize')],
        'non_claim':'No quantum local limit is tested or proved; remainders and topological labeling are not tested by this script.'}
target=ROOT/'work/trace005_periodic_symmetry_result.json'
target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
assert all(c['witness'] for a in result['results'][:2] for c in a['classes'])
assert sum(c['witness'] is None for c in result['results'][2]['classes'])==1
print(json.dumps(result,ensure_ascii=False,indent=2))
```

Полный текущий манифест:

```json
{
  "schema_version": 2,
  "claim_id": "TRACE005-RV3-RV5-finite-discriminator",
  "repository": {
    "commit": "unavailable: git rev-parse HEAD returned not a repository (exit 128)",
    "dirty": false,
    "dirty_applicability": "not applicable: no usable git repository"
  },
  "command": [
    "python3",
    "output/trace005_periodic_symmetry_verify.py"
  ],
  "environment": {
    "software": [
      {
        "name": "Python",
        "version": "3.12.14"
      }
    ],
    "hardware": "x86_64; Linux"
  },
  "mathematics": {
    "assertion_tested": "Exact first variations of period traces in 16 affine classes: all reversal classes for m=2,3, and centralizer classes for m=2; only identity centralizer class survives at m=2.",
    "coefficient_domain": "Q[zeta_8] and Q[zeta_28], rational polynomial reduction; floating values only order already certified nonzero witnesses",
    "conventions": "Weyl symbol g including r(q+1/2); S=[[3,4],[2,3]]; derivative coefficient T_m=sum (2k^2-l^2)g_kl exp(2pi i v.S^j z).",
    "inputs": [
      "literal Fourier coefficients in source"
    ],
    "bounds": {
      "m": [
        2,
        3
      ],
      "grid_denominators": [
        8,
        14
      ],
      "affine_classes_per_mode": 16,
      "fixed_point_counts": [
        32,
        196
      ]
    },
    "non_claims": [
      "No all-N quantum spectral asymptotic tested",
      "No C1 rigidity or uniform t remainder supplied by finite computation",
      "No numerical eigenphase computation at tau"
    ]
  },
  "randomness": {
    "used": false,
    "generator": "none",
    "seed": null
  },
  "run": {
    "started_at": "2026-10-27T09:02:57.110579+00:00",
    "runtime_seconds": 1.146775209000225,
    "exit_status": 0,
    "status": "completed",
    "resource_limits": {
      "memory_bytes": null,
      "cpu_seconds": null,
      "max_cores": null,
      "max_threads": null
    },
    "wall_timeout_seconds": 60
  },
  "outputs": [
    {
      "path": "work/trace005_periodic_symmetry_stdout.json",
      "sha256": "c54633c0c3466298909e865daa5cf309175de6323f1f6d9a69a0bb512376d246",
      "kind": "log"
    },
    {
      "path": "work/trace005_periodic_symmetry_stderr.txt",
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "kind": "log"
    },
    {
      "path": "work/trace005_periodic_symmetry_result.json",
      "sha256": "c54633c0c3466298909e865daa5cf309175de6323f1f6d9a69a0bb512376d246",
      "kind": "result"
    }
  ],
  "checks": [
    "exact grid inverse-lattice divisibility",
    "fixed point count equals determinant",
    "all 16 reversal classes at both periods differ",
    "exactly one centralizer class has no mismatch"
  ],
  "result": "Finite assertion verified in stated exact arithmetic range; theorem proof remains the written argument.",
  "residual_risks": [
    "Exact arithmetic code and handwritten coefficients require mathematical audit; direct trigonometric hosted calls provide a separate representation."
  ],
  "input_artifacts": [
    {
      "path": "output/trace005_periodic_symmetry_verify.py",
      "sha256": "6df7b0754037e73f9c4f5d6fb85171a23f79a8929fa51890c955af24758d5df0",
      "sha256_after": "6df7b0754037e73f9c4f5d6fb85171a23f79a8929fa51890c955af24758d5df0"
    }
  ],
  "execution_artifacts": [
    "output/trace005_periodic_symmetry_verify.py"
  ],
  "declared_results": [
    "work/trace005_periodic_symmetry_result.json"
  ]
}
```

Полный текущий локальный результат:

```json
{
  "assertion_tested": "Exact finite discriminator, not an asymptotic spectral test.\n\nContract: for m=2,3 and all 16 affine reversal classes modulo S iterates,\nplus all 16 centralizer classes at m=2,\ncompute the first parameter derivative of Tr DF_t^m at labeled S-periodic\npoints, using the literal Weyl symbol. Arithmetic is in Q(zeta_D).\nNonzero differences obstruct a C1 reverser only after the accompanying\nuniform remainder and conjugacy arguments have been proved.\nCommand: python3 output/trace005_periodic_symmetry_verify.py\n",
  "results": [
    {
      "m": 2,
      "mode": "reverse",
      "grid_denominator": 8,
      "field_order": 8,
      "phi_ascending": [
        "1",
        "0",
        "0",
        "0",
        "1"
      ],
      "point_count": 32,
      "expected_point_count": 32,
      "classes": [
        {
          "parity": 0,
          "sign": 1,
          "translation_grid": [
            0,
            0
          ],
          "mismatch_count": 12,
          "witness": {
            "z": [
              0,
              1
            ],
            "target": [
              0,
              7
            ],
            "delta_basis": [
              "0",
              "-8/5",
              "0",
              "8/5"
            ],
            "delta_numeric_real": -2.262741699796952,
            "delta_numeric_imag": 2.220446049250313e-16
          }
        },
        {
          "parity": 0,
          "sign": 1,
          "translation_grid": [
            0,
            4
          ],
          "mismatch_count": 20,
          "witness": {
            "z": [
              4,
              0
            ],
            "target": [
              4,
              4
            ],
            "delta_basis": [
              "588/125",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": 4.704,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 0,
          "sign": 1,
          "translation_grid": [
            4,
            0
          ],
          "mismatch_count": 28,
          "witness": {
            "z": [
              0,
              4
            ],
            "target": [
              4,
              4
            ],
            "delta_basis": [
              "44488/125",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": 355.904,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 0,
          "sign": 1,
          "translation_grid": [
            4,
            4
          ],
          "mismatch_count": 16,
          "witness": {
            "z": [
              0,
              0
            ],
            "target": [
              4,
              4
            ],
            "delta_basis": [
              "356",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": 356.0,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 0,
          "sign": -1,
          "translation_grid": [
            0,
            0
          ],
          "mismatch_count": 8,
          "witness": {
            "z": [
              2,
              1
            ],
            "target": [
              6,
              1
            ],
            "delta_basis": [
              "-26/25",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": -1.04,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 0,
          "sign": -1,
          "translation_grid": [
            0,
            4
          ],
          "mismatch_count": 24,
          "witness": {
            "z": [
              4,
              0
            ],
            "target": [
              4,
              4
            ],
            "delta_basis": [
              "588/125",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": 4.704,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 0,
          "sign": -1,
          "translation_grid": [
            4,
            0
          ],
          "mismatch_count": 16,
          "witness": {
            "z": [
              0,
              4
            ],
            "target": [
              4,
              4
            ],
            "delta_basis": [
              "44488/125",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": 355.904,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 0,
          "sign": -1,
          "translation_grid": [
            4,
            4
          ],
          "mismatch_count": 28,
          "witness": {
            "z": [
              0,
              0
            ],
            "target": [
              4,
              4
            ],
            "delta_basis": [
              "356",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": 356.0,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 1,
          "sign": 1,
          "translation_grid": [
            0,
            0
          ],
          "mismatch_count": 30,
          "witness": {
            "z": [
              0,
              2
            ],
            "target": [
              4,
              6
            ],
            "delta_basis": [
              "1768/5",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": 353.6,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 1,
          "sign": 1,
          "translation_grid": [
            0,
            4
          ],
          "mismatch_count": 30,
          "witness": {
            "z": [
              0,
              2
            ],
            "target": [
              4,
              2
            ],
            "delta_basis": [
              "1768/5",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": 353.6,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 1,
          "sign": 1,
          "translation_grid": [
            4,
            0
          ],
          "mismatch_count": 28,
          "witness": {
            "z": [
              4,
              4
            ],
            "target": [
              0,
              0
            ],
            "delta_basis": [
              "-356",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": -356.0,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 1,
          "sign": 1,
          "translation_grid": [
            4,
            4
          ],
          "mismatch_count": 28,
          "witness": {
            "z": [
              0,
              0
            ],
            "target": [
              4,
              4
            ],
            "delta_basis": [
              "356",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": 356.0,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 1,
          "sign": -1,
          "translation_grid": [
            0,
            0
          ],
          "mismatch_count": 30,
          "witness": {
            "z": [
              0,
              2
            ],
            "target": [
              4,
              2
            ],
            "delta_basis": [
              "1768/5",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": 353.6,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 1,
          "sign": -1,
          "translation_grid": [
            0,
            4
          ],
          "mismatch_count": 30,
          "witness": {
            "z": [
              0,
              2
            ],
            "target": [
              4,
              6
            ],
            "delta_basis": [
              "1768/5",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": 353.6,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 1,
          "sign": -1,
          "translation_grid": [
            4,
            0
          ],
          "mismatch_count": 28,
          "witness": {
            "z": [
              4,
              4
            ],
            "target": [
              0,
              0
            ],
            "delta_basis": [
              "-356",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": -356.0,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 1,
          "sign": -1,
          "translation_grid": [
            4,
            4
          ],
          "mismatch_count": 28,
          "witness": {
            "z": [
              0,
              0
            ],
            "target": [
              4,
              4
            ],
            "delta_basis": [
              "356",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": 356.0,
            "delta_numeric_imag": 0.0
          }
        }
      ],
      "all_sixteen_classes_distinguished": true
    },
    {
      "m": 3,
      "mode": "reverse",
      "grid_denominator": 14,
      "field_order": 28,
      "phi_ascending": [
        "1",
        "0",
        "-1",
        "0",
        "1",
        "0",
        "-1",
        "0",
        "1",
        "0",
        "-1",
        "0",
        "1"
      ],
      "point_count": 196,
      "expected_point_count": 196,
      "classes": [
        {
          "parity": 0,
          "sign": 1,
          "translation_grid": [
            0,
            0
          ],
          "mismatch_count": 120,
          "witness": {
            "z": [
              3,
              3
            ],
            "target": [
              3,
              11
            ],
            "delta_basis": [
              "0",
              "-392/125",
              "0",
              "196/125",
              "0",
              "-294/125",
              "0",
              "196/125",
              "0",
              "-98/125",
              "0",
              "196/125"
            ],
            "delta_numeric_real": -3.73770363553853,
            "delta_numeric_imag": 4.440892098500626e-16
          }
        },
        {
          "parity": 0,
          "sign": 1,
          "translation_grid": [
            0,
            7
          ],
          "mismatch_count": 196,
          "witness": {
            "z": [
              7,
              0
            ],
            "target": [
              7,
              7
            ],
            "delta_basis": [
              "882/125",
              "0",
              "0",
              "0",
              "0",
              "0",
              "0",
              "0",
              "0",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": 7.056,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 0,
          "sign": 1,
          "translation_grid": [
            7,
            0
          ],
          "mismatch_count": 196,
          "witness": {
            "z": [
              0,
              7
            ],
            "target": [
              7,
              7
            ],
            "delta_basis": [
              "66732/125",
              "0",
              "0",
              "0",
              "0",
              "0",
              "0",
              "0",
              "0",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": 533.856,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 0,
          "sign": 1,
          "translation_grid": [
            7,
            7
          ],
          "mismatch_count": 196,
          "witness": {
            "z": [
              0,
              2
            ],
            "target": [
              7,
              5
            ],
            "delta_basis": [
              "66297/125",
              "0",
              "0",
              "97/125",
              "391/500",
              "194/125",
              "103/250",
              "0",
              "-103/250",
              "-194/125",
              "-391/500",
              "-97/125"
            ],
            "delta_numeric_real": 534.0946728866982,
            "delta_numeric_imag": -3.885780586188048e-16
          }
        },
        {
          "parity": 0,
          "sign": -1,
          "translation_grid": [
            0,
            0
          ],
          "mismatch_count": 120,
          "witness": {
            "z": [
              1,
              0
            ],
            "target": [
              13,
              0
            ],
            "delta_basis": [
              "0",
              "102/25",
              "0",
              "-147/100",
              "0",
              "21/5",
              "0",
              "-51/25",
              "0",
              "-3/25",
              "0",
              "-261/100"
            ],
            "delta_numeric_real": 6.743371524703244,
            "delta_numeric_imag": -6.661338147750939e-16
          }
        },
        {
          "parity": 0,
          "sign": -1,
          "translation_grid": [
            0,
            7
          ],
          "mismatch_count": 196,
          "witness": {
            "z": [
              1,
              0
            ],
            "target": [
              13,
              7
            ],
            "delta_basis": [
              "0",
              "102/25",
              "0",
              "-147/100",
              "147/250",
              "21/5",
              "147/125",
              "-51/25",
              "-147/125",
              "-3/25",
              "-147/250",
              "-261/100"
            ],
            "delta_numeric_real": 7.999964768354367,
            "delta_numeric_imag": -6.661338147750939e-16
          }
        },
        {
          "parity": 0,
          "sign": -1,
          "translation_grid": [
            7,
            0
          ],
          "mismatch_count": 196,
          "witness": {
            "z": [
              8,
              7
            ],
            "target": [
              13,
              7
            ],
            "delta_basis": [
              "66272/125",
              "4",
              "0",
              "-49/25",
              "97/100",
              "77/25",
              "-53/250",
              "-2",
              "53/250",
              "23/25",
              "-97/100",
              "-51/25"
            ],
            "delta_numeric_real": 536.1906683834272,
            "delta_numeric_imag": -1.1102230246251565e-15
          }
        },
        {
          "parity": 0,
          "sign": -1,
          "translation_grid": [
            7,
            7
          ],
          "mismatch_count": 196,
          "witness": {
            "z": [
              8,
              7
            ],
            "target": [
              13,
              0
            ],
            "delta_basis": [
              "66272/125",
              "4",
              "0",
              "-49/25",
              "191/500",
              "77/25",
              "-347/250",
              "-2",
              "347/250",
              "23/25",
              "-191/500",
              "-51/25"
            ],
            "delta_numeric_real": 534.934075139776,
            "delta_numeric_imag": -8.881784197001252e-16
          }
        },
        {
          "parity": 1,
          "sign": 1,
          "translation_grid": [
            0,
            0
          ],
          "mismatch_count": 194,
          "witness": {
            "z": [
              1,
              4
            ],
            "target": [
              7,
              11
            ],
            "delta_basis": [
              "2697/125",
              "-677/500",
              "0",
              "2541/1000",
              "4119/250",
              "343/1000",
              "-2991/250",
              "677/1000",
              "2991/250",
              "-1697/1000",
              "-4119/250",
              "-1187/1000"
            ],
            "delta_numeric_real": 39.276493244488734,
            "delta_numeric_imag": -2.3314683517128287e-15
          }
        },
        {
          "parity": 1,
          "sign": 1,
          "translation_grid": [
            0,
            7
          ],
          "mismatch_count": 194,
          "witness": {
            "z": [
              1,
              3
            ],
            "target": [
              9,
              5
            ],
            "delta_basis": [
              "102/5",
              "-677/500",
              "0",
              "2541/1000",
              "153/10",
              "343/1000",
              "-51/5",
              "677/1000",
              "51/5",
              "-1697/1000",
              "-153/10",
              "-1187/1000"
            ],
            "delta_numeric_real": 37.41909908551487,
            "delta_numeric_imag": -2.3314683517128287e-15
          }
        },
        {
          "parity": 1,
          "sign": 1,
          "translation_grid": [
            7,
            0
          ],
          "mismatch_count": 196,
          "witness": {
            "z": [
              8,
              3
            ],
            "target": [
              9,
              5
            ],
            "delta_basis": [
              "137591/250",
              "-147/500",
              "0",
              "931/1000",
              "1886/125",
              "833/1000",
              "-5479/500",
              "147/1000",
              "5479/500",
              "-1127/1000",
              "-1886/125",
              "-637/1000"
            ],
            "delta_numeric_real": 566.0913545593013,
            "delta_numeric_imag": -1.3877787807814457e-15
          }
        },
        {
          "parity": 1,
          "sign": 1,
          "translation_grid": [
            7,
            7
          ],
          "mismatch_count": 196,
          "witness": {
            "z": [
              8,
              4
            ],
            "target": [
              7,
              11
            ],
            "delta_basis": [
              "137303/250",
              "-147/500",
              "0",
              "931/1000",
              "2036/125",
              "833/1000",
              "-5203/500",
              "147/1000",
              "5203/500",
              "-1127/1000",
              "-2036/125",
              "-637/1000"
            ],
            "delta_numeric_real": 566.6813931948499,
            "delta_numeric_imag": -1.3877787807814457e-15
          }
        },
        {
          "parity": 1,
          "sign": -1,
          "translation_grid": [
            0,
            0
          ],
          "mismatch_count": 194,
          "witness": {
            "z": [
              5,
              5
            ],
            "target": [
              5,
              0
            ],
            "delta_basis": [
              "-2697/125",
              "677/500",
              "0",
              "-2541/1000",
              "-4119/250",
              "-343/1000",
              "2991/250",
              "-677/1000",
              "-2991/250",
              "1697/1000",
              "4119/250",
              "1187/1000"
            ],
            "delta_numeric_real": -39.276493244488734,
            "delta_numeric_imag": 2.3314683517128287e-15
          }
        },
        {
          "parity": 1,
          "sign": -1,
          "translation_grid": [
            0,
            7
          ],
          "mismatch_count": 194,
          "witness": {
            "z": [
              1,
              4
            ],
            "target": [
              7,
              10
            ],
            "delta_basis": [
              "102/5",
              "-677/500",
              "0",
              "2541/1000",
              "153/10",
              "343/1000",
              "-51/5",
              "677/1000",
              "51/5",
              "-1697/1000",
              "-153/10",
              "-1187/1000"
            ],
            "delta_numeric_real": 37.41909908551487,
            "delta_numeric_imag": -2.3314683517128287e-15
          }
        },
        {
          "parity": 1,
          "sign": -1,
          "translation_grid": [
            7,
            0
          ],
          "mismatch_count": 196,
          "witness": {
            "z": [
              5,
              5
            ],
            "target": [
              12,
              0
            ],
            "delta_basis": [
              "-137303/250",
              "147/500",
              "0",
              "-931/1000",
              "-2036/125",
              "-833/1000",
              "5203/500",
              "-147/1000",
              "-5203/500",
              "1127/1000",
              "2036/125",
              "637/1000"
            ],
            "delta_numeric_real": -566.6813931948499,
            "delta_numeric_imag": 1.3877787807814457e-15
          }
        },
        {
          "parity": 1,
          "sign": -1,
          "translation_grid": [
            7,
            7
          ],
          "mismatch_count": 196,
          "witness": {
            "z": [
              5,
              5
            ],
            "target": [
              12,
              7
            ],
            "delta_basis": [
              "-137591/250",
              "147/500",
              "0",
              "-931/1000",
              "-1886/125",
              "-833/1000",
              "5479/500",
              "-147/1000",
              "-5479/500",
              "1127/1000",
              "1886/125",
              "637/1000"
            ],
            "delta_numeric_real": -566.0913545593013,
            "delta_numeric_imag": 1.3877787807814457e-15
          }
        }
      ],
      "all_sixteen_classes_distinguished": true
    },
    {
      "m": 2,
      "mode": "centralize",
      "grid_denominator": 8,
      "field_order": 8,
      "phi_ascending": [
        "1",
        "0",
        "0",
        "0",
        "1"
      ],
      "point_count": 32,
      "expected_point_count": 32,
      "classes": [
        {
          "parity": 0,
          "sign": 1,
          "translation_grid": [
            0,
            0
          ],
          "mismatch_count": 0,
          "witness": null
        },
        {
          "parity": 0,
          "sign": 1,
          "translation_grid": [
            0,
            4
          ],
          "mismatch_count": 24,
          "witness": {
            "z": [
              4,
              0
            ],
            "target": [
              4,
              4
            ],
            "delta_basis": [
              "588/125",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": 4.704,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 0,
          "sign": 1,
          "translation_grid": [
            4,
            0
          ],
          "mismatch_count": 24,
          "witness": {
            "z": [
              0,
              4
            ],
            "target": [
              4,
              4
            ],
            "delta_basis": [
              "44488/125",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": 355.904,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 0,
          "sign": 1,
          "translation_grid": [
            4,
            4
          ],
          "mismatch_count": 28,
          "witness": {
            "z": [
              0,
              0
            ],
            "target": [
              4,
              4
            ],
            "delta_basis": [
              "356",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": 356.0,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 0,
          "sign": -1,
          "translation_grid": [
            0,
            0
          ],
          "mismatch_count": 20,
          "witness": {
            "z": [
              0,
              1
            ],
            "target": [
              0,
              7
            ],
            "delta_basis": [
              "0",
              "-8/5",
              "0",
              "8/5"
            ],
            "delta_numeric_real": -2.262741699796952,
            "delta_numeric_imag": 2.220446049250313e-16
          }
        },
        {
          "parity": 0,
          "sign": -1,
          "translation_grid": [
            0,
            4
          ],
          "mismatch_count": 20,
          "witness": {
            "z": [
              4,
              0
            ],
            "target": [
              4,
              4
            ],
            "delta_basis": [
              "588/125",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": 4.704,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 0,
          "sign": -1,
          "translation_grid": [
            4,
            0
          ],
          "mismatch_count": 20,
          "witness": {
            "z": [
              0,
              4
            ],
            "target": [
              4,
              4
            ],
            "delta_basis": [
              "44488/125",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": 355.904,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 0,
          "sign": -1,
          "translation_grid": [
            4,
            4
          ],
          "mismatch_count": 16,
          "witness": {
            "z": [
              0,
              0
            ],
            "target": [
              4,
              4
            ],
            "delta_basis": [
              "356",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": 356.0,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 1,
          "sign": 1,
          "translation_grid": [
            0,
            0
          ],
          "mismatch_count": 30,
          "witness": {
            "z": [
              0,
              2
            ],
            "target": [
              4,
              2
            ],
            "delta_basis": [
              "1768/5",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": 353.6,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 1,
          "sign": 1,
          "translation_grid": [
            0,
            4
          ],
          "mismatch_count": 30,
          "witness": {
            "z": [
              0,
              2
            ],
            "target": [
              4,
              6
            ],
            "delta_basis": [
              "1768/5",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": 353.6,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 1,
          "sign": 1,
          "translation_grid": [
            4,
            0
          ],
          "mismatch_count": 28,
          "witness": {
            "z": [
              4,
              4
            ],
            "target": [
              0,
              0
            ],
            "delta_basis": [
              "-356",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": -356.0,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 1,
          "sign": 1,
          "translation_grid": [
            4,
            4
          ],
          "mismatch_count": 28,
          "witness": {
            "z": [
              0,
              0
            ],
            "target": [
              4,
              4
            ],
            "delta_basis": [
              "356",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": 356.0,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 1,
          "sign": -1,
          "translation_grid": [
            0,
            0
          ],
          "mismatch_count": 30,
          "witness": {
            "z": [
              0,
              2
            ],
            "target": [
              4,
              6
            ],
            "delta_basis": [
              "1768/5",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": 353.6,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 1,
          "sign": -1,
          "translation_grid": [
            0,
            4
          ],
          "mismatch_count": 30,
          "witness": {
            "z": [
              0,
              2
            ],
            "target": [
              4,
              2
            ],
            "delta_basis": [
              "1768/5",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": 353.6,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 1,
          "sign": -1,
          "translation_grid": [
            4,
            0
          ],
          "mismatch_count": 28,
          "witness": {
            "z": [
              4,
              4
            ],
            "target": [
              0,
              0
            ],
            "delta_basis": [
              "-356",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": -356.0,
            "delta_numeric_imag": 0.0
          }
        },
        {
          "parity": 1,
          "sign": -1,
          "translation_grid": [
            4,
            4
          ],
          "mismatch_count": 28,
          "witness": {
            "z": [
              0,
              0
            ],
            "target": [
              4,
              4
            ],
            "delta_basis": [
              "356",
              "0",
              "0",
              "0"
            ],
            "delta_numeric_real": 356.0,
            "delta_numeric_imag": 0.0
          }
        }
      ],
      "all_sixteen_classes_distinguished": false
    }
  ],
  "non_claim": "No quantum local limit is tested or proved; remainders and topological labeling are not tested by this script."
}
```

Далее сохранены все пять hosted-вызовов Wolfram с полными входами и MCP-ответами. Версия ядра: 15.0.1 for Linux x86 (64-bit), July 2, 2026. Первый независимо вычисляет 16 обращающих свидетелей прямым дифференцированием символа. Второй проверяет 16 коммутирующих классов, 11 значений T и константы. Третий содержит синтаксическую ошибку и не имеет математического результата. Четвёртый подтверждает формулы, но сопровождается предупреждениями Power::infy при прямом пределе; он также оставлен диагностическим. Пятый заменяет этот предельный шаг чистым сокращением рациональных Taylor-многочленов до подстановки нуля. Текущими чистыми подтверждениями считаются первый, второй и пятый вызовы.

#### VIIIo.8.1. period_two_all_reverser_classes: current_valid

```wolfram
ClearAll[q,p,g,r,rr,h,tm,z,s,cc,jj];
s={{3,4},{2,3}};cc={{1,2},{1,1}};jj={{1,0},{0,-1}};
r[q_]:=(1-Cos[14 Pi q])(1+Cos[2 Pi q]);
rr[q_]:=(1+Cos[14 Pi q])(1-Cos[2 Pi q]);
g=Cos[14 Pi q]+r[q]/10+r[q]Sin[2 Pi q]/100-1/10+rr[q](-3 Cos[2 Pi p]+4 Sin[2 Pi p])/500;
h=Expand[(D[g,{p,2}]-2 D[g,{q,2}])/(4 Pi^2)];
tm[z_]:=FullSimplify[TrigExpand[(h/.Thread[{q,p}->z])+(h/.Thread[{q,p}->Mod[s.z,1]])]];
witnesses={
{0,1,{0,0},{0,1},-8 Sqrt[2]/5},
{0,1,{0,4},{4,0},588/125},
{0,1,{4,0},{0,4},44488/125},
{0,1,{4,4},{0,0},356},
{0,-1,{0,0},{2,1},-26/25},
{0,-1,{0,4},{4,0},588/125},
{0,-1,{4,0},{0,4},44488/125},
{0,-1,{4,4},{0,0},356},
{1,1,{0,0},{0,2},1768/5},
{1,1,{0,4},{0,2},1768/5},
{1,1,{4,0},{4,4},-356},
{1,1,{4,4},{0,0},356},
{1,-1,{0,0},{0,2},1768/5},
{1,-1,{0,4},{0,2},1768/5},
{1,-1,{4,0},{4,4},-356},
{1,-1,{4,4},{0,0},356}};
checks=Map[Function[w,Module[{z=w[[4]]/8,b=w[[3]]/8,bmat=w[[2]]MatrixPower[cc,w[[1]]].jj,target,delta},
target=Mod[bmat.z+b,1];delta=FullSimplify[tm[z]-tm[target]];
<|"parity"->w[[1]],"sign"->w[[2]],"betaGrid"->w[[3]],"zGrid"->w[[4]],"targetGrid"->8 target,
"delta"->delta,"exactExpected"->TrueQ[delta==w[[5]]],
"periodic"->And@@(IntegerQ/@((s.s-IdentityMatrix[2]).z)),
"bound"->TrueQ[FullSimplify[Abs[delta]>=26/25]]|>]] ,witnesses];
<|"checks"->checks,"allExact"->And@@Lookup[checks,"exactExpected"],"allBounds"->And@@Lookup[checks,"bound"],
"C2equalsS"->(cc.cc==s),"reversingMatrices"->And@@Table[MatrixPower[cc,j].jj.s==Inverse[s].MatrixPower[cc,j].jj,{j,0,1}],
"linearTraceIdentity"->Simplify[Tr[MatrixPower[s,2].{{D[g,q,p],D[g,{p,2}]},{-D[g,{q,2}],-D[g,p,q]}}/(2 Pi)]-24 Pi h]==0,
"kernelVersion"->$Version|>
```

Полный возвращённый объект:

```json
{
  "content": [
    {
      "type": "text",
      "text": "Out[1]= <|\"checks\" -> {<|\"parity\" -> 0, \"sign\" -> 1, \"betaGrid\" -> {0, 0}, \"zGrid\" -> {0, 1}, \"targetGrid\" -> {0, 7}, \"delta\" -> (-8*Sqrt[2])/5, \"exactExpected\" -> True, \"periodic\" -> True, \"bound\" -> True|>, <|\"parity\" -> 0, \"sign\" -> 1, \"betaGrid\" -> {0, 4}, \"zGrid\" -> {4, 0}, \"targetGrid\" -> {4, 4}, \"delta\" -> 588/125, \"exactExpected\" -> True, \"periodic\" -> True, \"bound\" -> True|>, <|\"parity\" -> 0, \"sign\" -> 1, \"betaGrid\" -> {4, 0}, \"zGrid\" -> {0, 4}, \"targetGrid\" -> {4, 4}, \"delta\" -> 44488/125, \"exactExpected\" -> True, \"periodic\" -> True, \"bound\" -> True|>, <|\"parity\" -> 0, \"sign\" -> 1, \"betaGrid\" -> {4, 4}, \"zGrid\" -> {0, 0}, \"targetGrid\" -> {4, 4}, \"delta\" -> 356, \"exactExpected\" -> True, \"periodic\" -> True, \"bound\" -> True|>, <|\"parity\" -> 0, \"sign\" -> -1, \"betaGrid\" -> {0, 0}, \"zGrid\" -> {2, 1}, \"targetGrid\" -> {6, 1}, \"delta\" -> -26/25, \"exactExpected\" -> True, \"periodic\" -> True, \"bound\" -> True|>, <|\"parity\" -> 0, \"sign\" -> -1, \"betaGrid\" -> {0, 4}, \"zGrid\" -> {4, 0}, \"targetGrid\" -> {4, 4}, \"delta\" -> 588/125, \"exactExpected\" -> True, \"periodic\" -> True, \"bound\" -> True|>, <|\"parity\" -> 0, \"sign\" -> -1, \"betaGrid\" -> {4, 0}, \"zGrid\" -> {0, 4}, \"targetGrid\" -> {4, 4}, \"delta\" -> 44488/125, \"exactExpected\" -> True, \"periodic\" -> True, \"bound\" -> True|>, <|\"parity\" -> 0, \"sign\" -> -1, \"betaGrid\" -> {4, 4}, \"zGrid\" -> {0, 0}, \"targetGrid\" -> {4, 4}, \"delta\" -> 356, \"exactExpected\" -> True, \"periodic\" -> True, \"bound\" -> True|>, <|\"parity\" -> 1, \"sign\" -> 1, \"betaGrid\" -> {0, 0}, \"zGrid\" -> {0, 2}, \"targetGrid\" -> {4, 6}, \"delta\" -> 1768/5, \"exactExpected\" -> True, \"periodic\" -> True, \"bound\" -> True|>, <|\"parity\" -> 1, \"sign\" -> 1, \"betaGrid\" -> {0, 4}, \"zGrid\" -> {0, 2}, \"targetGrid\" -> {4, 2}, \"delta\" -> 1768/5, \"exactExpected\" -> True, \"periodic\" -> True, \"bound\" -> True|>, <|\"parity\" -> 1, \"sign\" -> 1, \"betaGrid\" -> {4, 0}, \"zGrid\" -> {4, 4}, \"targetGrid\" -> {0, 0}, \"delta\" -> -356, \"exactExpected\" -> True, \"periodic\" -> True, \"bound\" -> True|>, <|\"parity\" -> 1, \"sign\" -> 1, \"betaGrid\" -> {4, 4}, \"zGrid\" -> {0, 0}, \"targetGrid\" -> {4, 4}, \"delta\" -> 356, \"exactExpected\" -> True, \"periodic\" -> True, \"bound\" -> True|>, <|\"parity\" -> 1, \"sign\" -> -1, \"betaGrid\" -> {0, 0}, \"zGrid\" -> {0, 2}, \"targetGrid\" -> {4, 2}, \"delta\" -> 1768/5, \"exactExpected\" -> True, \"periodic\" -> True, \"bound\" -> True|>, <|\"parity\" -> 1, \"sign\" -> -1, \"betaGrid\" -> {0, 4}, \"zGrid\" -> {0, 2}, \"targetGrid\" -> {4, 6}, \"delta\" -> 1768/5, \"exactExpected\" -> True, \"periodic\" -> True, \"bound\" -> True|>, <|\"parity\" -> 1, \"sign\" -> -1, \"betaGrid\" -> {4, 0}, \"zGrid\" -> {4, 4}, \"targetGrid\" -> {0, 0}, \"delta\" -> -356, \"exactExpected\" -> True, \"periodic\" -> True, \"bound\" -> True|>, <|\"parity\" -> 1, \"sign\" -> -1, \"betaGrid\" -> {4, 4}, \"zGrid\" -> {0, 0}, \"targetGrid\" -> {4, 4}, \"delta\" -> 356, \"exactExpected\" -> True, \"periodic\" -> True, \"bound\" -> True|>}, \"allExact\" -> True, \"allBounds\" -> True, \"C2equalsS\" -> True, \"reversingMatrices\" -> True, \"linearTraceIdentity\" -> True, \"kernelVersion\" -> \"15.0.1 for Linux x86 (64-bit) (July 2, 2026)\"|>"
    }
  ],
  "structuredContent": null,
  "isError": false
}
```

#### VIIIo.8.2. cyclic_centralizer_and_uniform_constants: current_valid

```wolfram
ClearAll[q,p,g,r,rr,h,tm,s,cc,jj];
s={{3,4},{2,3}};cc={{1,2},{1,1}};jj={{1,0},{0,-1}};
r[q_]:=(1-Cos[14 Pi q])(1+Cos[2 Pi q]);
rr[q_]:=(1+Cos[14 Pi q])(1-Cos[2 Pi q]);
g=Cos[14 Pi q]+r[q]/10+r[q]Sin[2 Pi q]/100-1/10+rr[q](-3 Cos[2 Pi p]+4 Sin[2 Pi p])/500;
h=Expand[(D[g,{p,2}]-2 D[g,{q,2}])/(4 Pi^2)];
tm[z_]:=FullSimplify[TrigExpand[(h/.Thread[{q,p}->z])+(h/.Thread[{q,p}->Mod[s.z,1]])]];
points={{0,0},{0,1},{0,7},{0,2},{0,4},{4,0},{4,4},{4,2},{4,6},{2,1},{6,1}};
values=Map[<|"gridPoint"->#,"T"->tm[#/8]|>&,points];
checks=Flatten[Table[Module[{beta={bq,bp}/8,z,expect,target,delta},
Which[j==0&&bq==0&&bp==0&&sgn==1,z={0,0};expect=0,
j==0&&bq==0&&bp==0&&sgn==-1,z={0,1};expect=-8 Sqrt[2]/5,
j==0&&bq==0&&bp==4,z={4,0};expect=588/125,
j==0&&bq==4&&bp==0,z={0,4};expect=44488/125,
j==0&&bq==4&&bp==4,z={0,0};expect=356,
j==1&&bq==0,z={0,2};expect=1768/5,
j==1&&bq==4&&bp==0,z={4,4};expect=-356,
j==1&&bq==4&&bp==4,z={0,0};expect=356];
target=Mod[sgn MatrixPower[cc,j].(z/8)+beta,1];delta=FullSimplify[tm[z/8]-tm[target]];
<|"parity"->j,"sign"->sgn,"betaGrid"->{bq,bp},"zGrid"->z,"targetGrid"->8 target,
"delta"->delta,"exactExpected"->TrueQ[delta==expect]|>],
{j,0,1},{sgn,{1,-1}},{bq,{0,4}},{bp,{0,4}}],3];
projectors={(IdentityMatrix[2]+(s-3 IdentityMatrix[2])/(2 Sqrt[2]))/2,
(IdentityMatrix[2]-(s-3 IdentityMatrix[2])/(2 Sqrt[2]))/2};
<|"periodTwoValues"->values,"centralizerChecks"->checks,"allExact"->And@@Lookup[checks,"exactExpected"],
"greenBound"->FullSimplify[2/(3+2 Sqrt[2]-1)+2/(1-1/(3+2 Sqrt[2]))],
"projectorNormBounds"->((Max[Total[Abs[#]]&/@#]<2)&/@projectors),
"derivativeConstants"->Table[(59/50)*9*72^j<{20,1000,100000,10000000}[[j+1]],{j,0,3}],
"traceRemainderConstant"->(2*(14*10^9+7001^2)<10^12),
"gapConstant"->(72*26/25-2/100>70),
"kernelVersion"->$Version|>
```

Полный возвращённый объект:

```json
{
  "content": [
    {
      "type": "text",
      "text": "Out[1]= <|\"periodTwoValues\" -> {<|\"gridPoint\" -> {0, 0}, \"T\" -> 19606/125|>, <|\"gridPoint\" -> {0, 1}, \"T\" -> -20 - (172*Sqrt[2])/125|>, <|\"gridPoint\" -> {0, 7}, \"T\" -> -20 + (28*Sqrt[2])/125|>, <|\"gridPoint\" -> {0, 2}, \"T\" -> 784/5|>, <|\"gridPoint\" -> {0, 4}, \"T\" -> 19594/125|>, <|\"gridPoint\" -> {4, 0}, \"T\" -> -24306/125|>, <|\"gridPoint\" -> {4, 4}, \"T\" -> -24894/125|>, <|\"gridPoint\" -> {4, 2}, \"T\" -> -984/5|>, <|\"gridPoint\" -> {4, 6}, \"T\" -> -984/5|>, <|\"gridPoint\" -> {2, 1}, \"T\" -> (3*(-1020 + 29*Sqrt[2]))/500|>, <|\"gridPoint\" -> {6, 1}, \"T\" -> (-2540 + 87*Sqrt[2])/500|>}, \"centralizerChecks\" -> {<|\"parity\" -> 0, \"sign\" -> 1, \"betaGrid\" -> {0, 0}, \"zGrid\" -> {0, 0}, \"targetGrid\" -> {0, 0}, \"delta\" -> 0, \"exactExpected\" -> True|>, <|\"parity\" -> 0, \"sign\" -> 1, \"betaGrid\" -> {0, 4}, \"zGrid\" -> {4, 0}, \"targetGrid\" -> {4, 4}, \"delta\" -> 588/125, \"exactExpected\" -> True|>, <|\"parity\" -> 0, \"sign\" -> 1, \"betaGrid\" -> {4, 0}, \"zGrid\" -> {0, 4}, \"targetGrid\" -> {4, 4}, \"delta\" -> 44488/125, \"exactExpected\" -> True|>, <|\"parity\" -> 0, \"sign\" -> 1, \"betaGrid\" -> {4, 4}, \"zGrid\" -> {0, 0}, \"targetGrid\" -> {4, 4}, \"delta\" -> 356, \"exactExpected\" -> True|>, <|\"parity\" -> 0, \"sign\" -> -1, \"betaGrid\" -> {0, 0}, \"zGrid\" -> {0, 1}, \"targetGrid\" -> {0, 7}, \"delta\" -> (-8*Sqrt[2])/5, \"exactExpected\" -> True|>, <|\"parity\" -> 0, \"sign\" -> -1, \"betaGrid\" -> {0, 4}, \"zGrid\" -> {4, 0}, \"targetGrid\" -> {4, 4}, \"delta\" -> 588/125, \"exactExpected\" -> True|>, <|\"parity\" -> 0, \"sign\" -> -1, \"betaGrid\" -> {4, 0}, \"zGrid\" -> {0, 4}, \"targetGrid\" -> {4, 4}, \"delta\" -> 44488/125, \"exactExpected\" -> True|>, <|\"parity\" -> 0, \"sign\" -> -1, \"betaGrid\" -> {4, 4}, \"zGrid\" -> {0, 0}, \"targetGrid\" -> {4, 4}, \"delta\" -> 356, \"exactExpected\" -> True|>, <|\"parity\" -> 1, \"sign\" -> 1, \"betaGrid\" -> {0, 0}, \"zGrid\" -> {0, 2}, \"targetGrid\" -> {4, 2}, \"delta\" -> 1768/5, \"exactExpected\" -> True|>, <|\"parity\" -> 1, \"sign\" -> 1, \"betaGrid\" -> {0, 4}, \"zGrid\" -> {0, 2}, \"targetGrid\" -> {4, 6}, \"delta\" -> 1768/5, \"exactExpected\" -> True|>, <|\"parity\" -> 1, \"sign\" -> 1, \"betaGrid\" -> {4, 0}, \"zGrid\" -> {4, 4}, \"targetGrid\" -> {0, 0}, \"delta\" -> -356, \"exactExpected\" -> True|>, <|\"parity\" -> 1, \"sign\" -> 1, \"betaGrid\" -> {4, 4}, \"zGrid\" -> {0, 0}, \"targetGrid\" -> {4, 4}, \"delta\" -> 356, \"exactExpected\" -> True|>, <|\"parity\" -> 1, \"sign\" -> -1, \"betaGrid\" -> {0, 0}, \"zGrid\" -> {0, 2}, \"targetGrid\" -> {4, 6}, \"delta\" -> 1768/5, \"exactExpected\" -> True|>, <|\"parity\" -> 1, \"sign\" -> -1, \"betaGrid\" -> {0, 4}, \"zGrid\" -> {0, 2}, \"targetGrid\" -> {4, 2}, \"delta\" -> 1768/5, \"exactExpected\" -> True|>, <|\"parity\" -> 1, \"sign\" -> -1, \"betaGrid\" -> {4, 0}, \"zGrid\" -> {4, 4}, \"targetGrid\" -> {0, 0}, \"delta\" -> -356, \"exactExpected\" -> True|>, <|\"parity\" -> 1, \"sign\" -> -1, \"betaGrid\" -> {4, 4}, \"zGrid\" -> {0, 0}, \"targetGrid\" -> {4, 4}, \"delta\" -> 356, \"exactExpected\" -> True|>}, \"allExact\" -> True, \"greenBound\" -> 2*Sqrt[2], \"projectorNormBounds\" -> {True, True}, \"derivativeConstants\" -> {True, True, True, True}, \"traceRemainderConstant\" -> True, \"gapConstant\" -> True, \"kernelVersion\" -> \"15.0.1 for Linux x86 (64-bit) (July 2, 2026)\"|>"
    }
  ],
  "structuredContent": null,
  "isError": false
}
```

#### VIIIo.8.3. poisson_parameter_stability_certificate: diagnostic_superseded

```wolfram
ClearAll[r,c,w,s,x];
den=1+r^2-2r c;
cert=Expand[den^2-(1-r^2)^2(1-c^2)];
p0=(1+r)/(1-r);
pw=(1-r^2)/(1-2r Cos[w]+r^2);
pwprime=D[pw,w];
ans=<|"poissonDerivativeCertificate"->Factor[cert],
"certificateEqualsSquare"->TrueQ[Factor[cert-(2r-(1+r^2)c)^2]==0],
"maximizer"->FullSimplify[(2r Sqrt[1-c^2]/den)/.(c->2r/(1+r^2)),0<r<1],
"energyScale"->Limit[(p0+pw)/.(r->Exp[-s x],w->s x),x->0,Direction->"FromAbove"],
"scaledEnergy"->Limit[(x(p0+pw)/2)/.(r->Exp[-s x],w->s x),x->0,Direction->"FromAbove",Assumptions->s>0],
"scaledLogDerivative"->Limit[((2 pwprime)/(p0+pw))*x/.(r->Exp[-s x],w->s x),x->0,Direction->"FromAbove",Assumptions->s>0],
"kernelVersion"->$Version|>;
ans
```

Полный возвращённый объект:

```json
{
  "content": [
    {
      "type": "text",
      "text": "ToExpression::sntx: Invalid syntax in or before \"\\\"energyScale\\\"->Limit ...                     ^\".\"\\n\"\nGeneral::messages: Messages were generated which may indicate errors.\n\nOut[1]= $Failed"
    }
  ],
  "structuredContent": null,
  "isError": false
}
```

#### VIIIo.8.4. poisson_parameter_stability_corrected: diagnostic_superseded

```wolfram
ClearAll[r,c,w,s,x];
den=1+r^2-2r c;
cert=Expand[den^2-(1-r^2)^2(1-c^2)];
p0=(1+r)/(1-r);
pw=(1-r^2)/(1-2r Cos[w]+r^2);
pwprime=D[pw,w];
<|"poissonDerivativeCertificate"->Factor[cert],
"certificateEqualsSquare"->TrueQ[Factor[cert-(2r-(1+r^2)c)^2]==0],
"maximizer"->FullSimplify[(2r Sqrt[1-c^2]/den)/.(c->2r/(1+r^2)),0<r<1],
"scaledEnergy"->Limit[(x(p0+pw)/2)/.{r->Exp[-s x],w->s x},x->0,Direction->"FromAbove",Assumptions->s>0],
"scaledLogDerivative"->Limit[(2 x pwprime/(p0+pw))/.{r->Exp[-s x],w->s x},x->0,Direction->"FromAbove",Assumptions->s>0],
"kernelVersion"->$Version|>
```

Полный возвращённый объект:

```json
{
  "content": [
    {
      "type": "text",
      "text": "Power::infy: -- Message text not found -- (1/0)\nPower::infy: -- Message text not found -- (1/0)\nInfinity::indet: -- Message text not found -- (0*ComplexInfinity)\nPower::infy: -- Message text not found -- (1/0)\nPower::infy: -- Message text not found -- (1/0)\nInfinity::indet: -- Message text not found -- (0*ComplexInfinity)\nGeneral::messages: Messages were generated which may indicate errors.\n\nOut[1]= <|\"poissonDerivativeCertificate\" -> (c - 2*r + c*r^2)^2, \"certificateEqualsSquare\" -> True, \"maximizer\" -> (-2*r)/(-1 + r^2), \"scaledEnergy\" -> 3/(2*s), \"scaledLogDerivative\" -> -2/(3*s), \"kernelVersion\" -> \"15.0.1 for Linux x86 (64-bit) (July 2, 2026)\"|>"
    }
  ],
  "structuredContent": null,
  "isError": false
}
```

#### VIIIo.8.5. poisson_parameter_stability_clean_cancellation: current_valid

```wolfram
ClearAll[s,x,c,r];
rr=1-s x+(s x)^2/2-(s x)^3/6+(s x)^4/24;
co=1-(s x)^2/2+(s x)^4/24;
si=s x-(s x)^3/6;
dd=Expand[1-2 rr co+rr^2];
pp0=(1+rr)/(1-rr);
pp=(1-rr^2)/dd;
dp=-2 rr si (1-rr^2)/dd^2;
ee=Cancel[Together[x(pp0+pp)/2]];
ll=Cancel[Together[2x dp/(pp0+pp)]];
<|"scaledEnergyFiniteCancellation"->(ee/.x->0),
"scaledLogDerivativeFiniteCancellation"->(ll/.x->0),
"bothExpected"->TrueQ[Simplify[(ee/.x->0)==3/(2s)&&(ll/.x->0)==-2/(3s),s>0]],
"denominatorLeadingOrder"->Coefficient[dd,x,2],
"noLimitsInvoked"->True,"kernelVersion"->$Version|>
```

Полный возвращённый объект:

```json
{
  "content": [
    {
      "type": "text",
      "text": "Out[1]= <|\"scaledEnergyFiniteCancellation\" -> 3/(2*s), \"scaledLogDerivativeFiniteCancellation\" -> -2/(3*s), \"bothExpected\" -> True, \"denominatorLeadingOrder\" -> 2*s^2, \"noLimitsInvoked\" -> True, \"kernelVersion\" -> \"15.0.1 for Linux x86 (64-bit) (July 2, 2026)\"|>"
    }
  ],
  "structuredContent": null,
  "isError": false
}
```

### VIIIo.9. Отдельный проход самопроверки

Самопроверка выполнена автором после вывода и чтения сырых записей. Независимый рецензент и формальный доказатель не использовались. Проверены 34 обязательства в заявленной области; три главных спектральных обязательства оставлены открытыми.

| ID | Блок | Обязательство | Статус |
|---|---|---|---|
| RV-AUDIT-01 | RV1 | Реальный Weyl-символ, включая сдвиг r(q+1/2), B=59/50 и поддержку |v|_1<=9 | Проверено |
| RV-AUDIT-02 | RV1 | Индуцированные max-нормы производных X, оценки 20,1000,1e5,1e7 без переноса из иного символа | Проверено |
| RV-AUDIT-03 | RV1 | Полный вещественный поток, обратимость и сохранение площади | Проверено |
| RV-AUDIT-04 | RV1 | Оценки epsilon и её производной на всём 0<=t<=1e-14 | Проверено |
| RV-AUDIT-05 | RV1 | Двусторонняя Green-формула, оба индекса и единственность ограниченного решения | Проверено |
| RV-AUDIT-06 | RV1 | Норма Green меньше 3 и коэффициент сжатия 42000t | Проверено |
| RV-AUDIT-07 | RV1 | Непрерывное периодическое решение, точное сопряжение и сдвиг <=600t | Проверено |
| RV-AUDIT-08 | RV1 | Построение непрерывного k из полных поднятых орбит и обе композиции hk=kh=Id | Проверено |
| RV-AUDIT-09 | RV2 | Подъём произвольного гомеоморфизма, целая гомологическая матрица и постоянная целая поправка | Проверено |
| RV-AUDIT-10 | RV2 | Ограниченность обеих гиперболических компонент, отсутствие неаффинных кандидатов после сопряжения | Проверено |
| RV-AUDIT-11 | RV2 | Все четыре допустимых сдвига и обе ориентации | Проверено |
| RV-AUDIT-12 | RV2 | Все целые обратимые коммутирующие и обращающие матрицы; нормы плюс и минус единица | Проверено |
| RV-AUDIT-13 | RV2 | Полнота единиц Z[sqrt2] элементарным приведением в [1,1+sqrt2) | Проверено |
| RV-AUDIT-14 | RV2 | Факторизация C^2=S и ровно 16 классов каждого типа после вынесения итераций | Проверено |
| RV-AUDIT-15 | RV3 | Используются точки периода, делящего два, включая неподвижные, а не только строгого периода два | Проверено |
| RV-AUDIT-16 | RV3 | Вариационное уравнение Y, точная вторая производная и равномерный Taylor-остаток | Проверено |
| RV-AUDIT-17 | RV3 | Замена точки h_tz на z стоит O(t^2) без дифференцирования h_t | Проверено |
| RV-AUDIT-18 | RV3 | Порядок матричного произведения, след линейного члена 24pi T и константа 34 | Проверено |
| RV-AUDIT-19 | RV3 | Явная формула H через r,R и их производные и прямые значения на 11 рациональных точках | Проверено |
| RV-AUDIT-20 | RV4-RV5 | Таблица покрывает 16 обращателей и 15 неединичных коммутирующих классов | Проверено |
| RV-AUDIT-21 | RV4-RV5 | Тождественный класс централизатора сохранён; нет ошибочного исключения итераций | Проверено |
| RV-AUDIT-22 | RV4-RV5 | Отделённый разрыв следов >70t на всём 0<t<=1e-14, в частности при исходном tau | Проверено |
| RV-AUDIT-23 | RV4 | Для обращателя используется обратная монодромия; след обратной равен следу только после det=1 и размера два | Проверено |
| RV-AUDIT-24 | RV5 | След монодромии инвариантен вдоль орбиты; вынесенная итерация не меняет препятствие | Проверено |
| RV-AUDIT-25 | RV4-RV5 | Полная C1-классификация не требует сохранения площади или R^2=Id; топологические обращатели остаются | Проверено |
| RV-AUDIT-26 | RV5 | Корни, конечный порядок и отсутствие C1-сопряжения следуют с учётом бесконечного порядка S | Проверено |
| RV-AUDIT-27 | RV6 | Производная Q=iN ad_A Q и знак угловой производной Poisson-керна | Проверено |
| RV-AUDIT-28 | RV6 | Цикличное дифференцирование абсолютно сходящегося Laurent-ряда работает и в вырождениях | Проверено |
| RV-AUDIT-29 | RV6 | Точный квадратный сертификат производной, нормировка N^-2 и относительная оценка с коэффициентом 2B | Проверено |
| RV-AUDIT-30 | RV6 | Интегральная граница логарифма не превращена в априорную ограниченность R_N | Проверено |
| RV-AUDIT-31 | RV6 | Общая двухблочная модель резкости N^2 отделена от исходной семьи; нечётные кратности и фиксированное s | Проверено |
| RV-AUDIT-32 | COMPUTATION | Пять полных hosted-записей, три чистые текущие и две диагностические; предупреждения не скрыты | Проверено |
| RV-AUDIT-33 | COMPUTATION | Локальный точный скрипт: до/после хеши, объявленный результат, stderr, диапазон и валидированный v2-manifest | Проверено |
| RV-AUDIT-34 | REVIEW | Самопроверка не объявлена независимым рецензированием; литературная новизна не проверялась | Проверено |
| RV-AUDIT-35 | GOAL | Критическая невзвешенная положительная резольвента исходного U при фиксированном tau | Не закрыто |
| RV-AUDIT-36 | GOAL | Исходная Y-компенсация -delta_star, все высшие порядки и полный Sine2 | Не закрыто |
| RV-AUDIT-37 | GOAL | Корректный мост от C1-классификации к квантовой локальной статистике; такой мост не дан | Не закрыто |

Итог самопроверки: полная C¹-классификация относится именно к исходному классическому F_t, а не к общим антиунитарным операциям и не к коммутанту произвольной конечной унитарной матрицы. Указанный t-интервал покрыт явным остатком, а не продолжением формальной первой производной. Устойчивость RV6 относится к исходной невзвешенной энергии, однако не оценивает её значение. Основной спектральный предел остаётся недоказанным и неопровергнутым.


## VIIIp. Квантовая точность, устойчивость локального закона и парный перенос

### VIIIp.1. Цель и выбор маршрутов

Заданное семейство не меняется:
$$
U_N=e^{i\tau N A_N}M_N,\qquad\tau=10^{-80},\qquad
                          N\longrightarrow\infty\text{ по нечётным }N.
$$
Единственная случайность — общий равномерный сдвиг alpha∈[0,1). Для произвольной унитарной U размера N, с фазами в оборотах theta_j, обозначим соответствующий периодический процесс через Xi_{U,N,alpha} и положим
$$
\mathscr L_{U,N}(f)=\mathbb E_\alpha
      \exp\{-\langle f,\Xi_{U,N,\alpha}\rangle\},
 \quad f\in C_c^\infty(\mathbb R),\quad f\ge0.
$$
Парные наблюдаемые:
$$
\mathcal R_{U,N}(s)=\frac1{N^2}\sum_{j,k}
        P_{e^{-s/N}}(2\pi(\theta_j-\theta_k)),\quad
 P_r(\omega)=\frac{1-r^2}{1-2r\cos\omega+r^2},\quad s>0,
$$
$$
\mathcal T_{U,N}(w)=\frac1{N^2}\sum_{m\ge1}
                       w(m/N)|\operatorname{Tr}U^m|^2.        \tag{VIIIp.1.1}
$$
Здесь w вещественна, чётна и принадлежит C²_c(R); исходный вес удовлетворяет более сильному C∞-условию. Разность двух парных отклонений от CUE при одинаковом N равна разности двух T: эталон min(m,N) сокращается точно.

| Маршрут | Первый проверяемый вопрос | Итог |
|---|---|---|
| Конечномерные унитарные тождества и двойственность | Передаёт ли малая ошибка матрицы всю локальную статистику? | QS1 и QS4 дают точный достаточный и резкий общий масштаб; одна унитарность и самодвойственность секулярного многочлена значения предела не определяют |
| Положительный HS-оператор | Можно ли сравнить критические резольвенты без выбора собственных векторов? | QS2–QS3 дают положительное сравнение и перенос парного теста для исходной семьи с явной ошибкой |
| Достаточность фиксированной классической динамики | Исключают ли новый C¹-результат, интенсивности и короткие следы другой локальный предел? | QS5–QS6 дают строго отрицательный ответ для перечисленного набора входов, сохраняя именно F_tau, а не линейный предел t=0 |

Новый шаг по сравнению с прежним движущимся t_N: в QS5 классическая конечная точка остаётся буквально той же F_tau. Меняется квантовая матрица; это отмечается во всех выводах.

### VIIIp.2. QS1: ограниченные Laplace-тесты без сопоставления собственных фаз

**QS1.** Для любых унитарных U,V размера N при epsilon=norm(V−U)<2 положим
$$
\eta=2\arcsin(\epsilon/2).
$$
Тогда для каждого неотрицательного f∈C∞_c(R)
$$
\boxed{\quad
 |\mathscr L_{V,N}(f)-\mathscr L_{U,N}(f)|
                      \le\frac{N\eta}{2\pi}\|f'\|_{L^1(\mathbb R)}.
 \quad}                                                       \tag{VIIIp.2.1}
$$
Следовательно, если norm(V_N−U_N)=o(1/N), оба процесса имеют одни и те же слабые локальные пределы. Равномерная интегрируемость парных моментов не требуется.

Доказательство. Спектр VU* не содержит −1. По конечномерному спектральному разложению существует эрмитова H с e^{iH}=VU*, norm H=eta. Рассмотрим U_t=e^{itH}U, 0≤t≤1. Фазы отдельными ветвями не выбираются. Периодизация
$$
F_N(\omega)=\sum_{\ell\in\mathbb Z}
                   f\bigl(N(\omega/(2\pi)+\ell)\bigr)
$$
неотрицательна и гладка. Её Fourier-ряд и ряд производной абсолютно сходятся при каждом N. Цикличность следа даёт для любого целого m
$$
\partial_t\operatorname{Tr}U_t^m
                    =im\operatorname{Tr}(H U_t^m),
$$
включая отрицательные степени. Поэтому при Z_t=e^{-2pi i alpha}U_t
$$
\partial_t\operatorname{Tr}F_N(Z_t)
                         =\operatorname{Tr}[H F_N'(Z_t)].     \tag{VIIIp.2.2}
$$
Штрих здесь означает производную по углу omega в радианах. Если B самосопряжён, то abs Tr(HB)≤norm H·Tr abs(B): диагонализируем B и оцениваем каждый диагональный элемент H его нормой. Интегрирование по alpha даёт точно
$$
\int_0^1\operatorname{Tr}|F_N'(e^{-2\pi i\alpha}U_t)|\,d\alpha
 =\frac N{2\pi}\int_0^{2\pi}|F_N'(\omega)|\,d\omega
 \le\frac N{2\pi}\|f'\|_1.                                 \tag{VIIIp.2.3}
$$
Последняя оценка следует раскрытием периодизации, треугольным неравенством и заменой переменной. Поскольку Tr F_N≥0, модуль производной exp(−Tr F_N) не больше модуля (VIIIp.2.2). Интегрирование по t доказывает (VIIIp.2.1).

У всех процессов среднее число точек на интервале равно его длине. Это даёт равномерную тесноту на компактах через неравенство Маркова. Laplace-функционалы для неотрицательных гладких компактных тестов определяют закон; непрерывные компактные тесты получаются равномерным приближением, ошибка которого контролируется тем же первым моментом. Таким образом, исчезающая правая часть (VIIIp.2.1) передаёт любой слабый предел. Это ограниченный функционал, а не моментный перенос с неявным UI.

Все наблюдаемые (VIIIp.1.1) и L инвариантны при умножении U на общий скаляр единичного модуля. Поэтому во всех результатах можно вместо epsilon использовать inf norm(V−zU), где abs(z)=1; минимум достигается на окружности. Меняется лишь общий сдвиг alpha, его закон сохраняется.

### VIIIp.3. QS2: положительное сравнение всей парной резольвенты

**QS2.** При тех же U,V, eta для каждого s>0
$$
e^{-2\eta/\sinh(s/N)}\le
      \frac{\mathcal R_{V,N}(s)}{\mathcal R_{U,N}(s)}
                      \le e^{2\eta/\sinh(s/N)}.               \tag{VIIIp.3.1}
$$
В частности, при epsilon≤1 показатель не больше 4N epsilon/s. Относительное сравнение не предполагает ограниченности R по N и само по себе её не доказывает.

На HS-пространстве Q_t=Ad_{U_t}, G=ad_H=HX−XH. Оператор G самосопряжён, norm G≤2eta, Q_t'=iGQ_t. Абсолютно сходящийся Laurent-ряд P_r позволяет применить (VIIIp.2.2) на HS-пространстве:
$$
\partial_t\mathcal R_{U_t,N}(s)
           =N^{-2}\operatorname{Tr}_{\mathrm{HS}}[G P_r'(Q_t)].
$$
Точный положительный сертификат
$$
(1+r^2-2rc)^2-(1-r^2)^2(1-c^2)
                         =[2r-(1+r^2)c]^2
$$
при c=cos omega доказывает
$$
|P_r'(\omega)|\le\frac{2r}{1-r^2}P_r(\omega)
                =\frac1{\sinh(s/N)}P_r(\omega).
$$
Следовательно, abs partial_t log R≤2eta/sinh(s/N). Интегрирование по t даёт (VIIIp.3.1). Использованы только унитарность и положительность; кратности не исключаются.

Есть независимая формулировка без логарифма и геодезической. Обозначим Q=Ad_U, Qtilde=Ad_V, B=I−rQ, Btilde=I−rQtilde и
$$
a=\frac{2r\epsilon}{1-r}.
$$
При a<1 имеем неравенства положительных форм
$$
(1-a)^2B^*B\le\widetilde B^*\widetilde B\le(1+a)^2B^*B,
$$
$$
(1+a)^{-2}\mathcal R_{U,N}(s)
 \le\mathcal R_{V,N}(s)\le(1-a)^{-2}\mathcal R_{U,N}(s).      \tag{VIIIp.3.2}
$$
Действительно, norm(Qtilde−Q)≤2epsilon в HS-норме оператора. Пишем Btilde=(I+E)B, norm E≤a, используя norm B^{-1}≤(1−r)^{-1}. Это даёт сравнение форм, затем их обратных и следов. По PR1 энергия равна (1−r²)N^{-2}Tr(B*B)^{-1}. Таким образом, потеря фактора 1/(1−r), порядка N на критическом масштабе, видна непосредственно в положительном операторе; она не устраняется сменой координат.

### VIIIp.4. QS3: перенос исходного парного теста через ошибку порядка 1/N²

Для вещественной чётной w∈C²_c(R) определим конечную константу
$$
C_w=4\pi\|t w(t)\|_{L^1}
                      +\pi^{-1}\|(t w(t))''\|_{L^1}.         \tag{VIIIp.4.1}
$$
**QS3.** Для произвольных U,V размера N при epsilon<2:
$$
\boxed{\quad
 |\mathcal T_{V,N}(w)-\mathcal T_{U,N}(w)|
 \le\frac{C_wN\eta}{2}
   e^{2\eta/\sinh(2\pi/N)}\mathcal R_{U,N}(2\pi).
 \quad}                                                       \tag{VIIIp.4.2}
$$
Это абсолютный перенос парного момента с явно указанным контролирующим положительным моментом; одной слабой сходимости для него не используется.

Пусть
$$
\phi(x)=\int_{\mathbb R}w(t)e^{2\pi itx}\,dt.
$$
При abs(x)≤1 интегральная формула производной даёт abs(phi')≤2pi norm(tw)_1. При abs(x)≥1 интегрируем дважды по частям; граничные члены равны нулю, поскольку tw∈C²_c. Тогда
$$
|\phi'(x)|\le\frac{\|(tw)''\|_1}{2\pi x^2},\qquad
             |\phi'(x)|\le\frac{C_w}{1+x^2}
                       =\pi C_w f_{2\pi}(x),
 \quad f_s(x)=\frac{2s}{s^2+4\pi^2x^2}.                     \tag{VIIIp.4.3}
$$
Такая же оценка без производной обеспечивает суммируемость периодизации phi. Сравнение Fourier-коэффициентов и обратное Fourier-преобразование дают
$$
h_N(\omega):=\sum_{m\ge1}w(m/N)\cos(m\omega)
   =\frac12\left[N\sum_{\ell\in\mathbb Z}
                \phi(N(\omega/(2\pi)+\ell))-w(0)\right].     \tag{VIIIp.4.4}
$$
Ряды периодизации и их производные равномерно сходятся при каждом N, так что почленное дифференцирование допустимо. По положительной периодизации Poisson-керна из PR3:
$$
|h_N'(\omega)|\le\frac{N^2}{4\pi}
    \sum_\ell|\phi'(N(\omega/(2\pi)+\ell))|
                         \le\frac{C_wN}{4}P_{e^{-2\pi/N}}(\omega).
                                                               \tag{VIIIp.4.5}
$$
На HS-пространстве T=N^{-2}Tr h_N(Q). Дифференцирование вдоль того же U_t, norm ad_H≤2eta и (VIIIp.4.5) дают
$$
|\partial_t\mathcal T_{U_t,N}(w)|
                    \le\frac{C_wN\eta}{2}\mathcal R_{U_t,N}(2\pi).
$$
Применяем (VIIIp.3.1) и интегрируем t∈[0,1]. Получена (VIIIp.4.2). Нормировки N, 2pi и диагональные члены в (VIIIp.4.4) сохранены; производная постоянного w(0) равна нулю.

Теперь U_N — буквально исходная семья при фиксированном tau. Из PR5 по всем нечётным N≥exp(1000)
$$
\mathcal R_{U_N,N}(2\pi)
                        \le1+\frac{250N}{\pi\log N}.         \tag{VIIIp.4.6}
$$
Пусть V_N — любая унитарная аппроксимация и norm(V_N−U_N)≤K/N² при фиксированном K≥0. Для нечётных
$$
N\ge\max\{e^{1000},2K+1\}
$$
из eta≤2epsilon и (VIIIp.4.2)–(VIIIp.4.6) следует явная граница
$$
\boxed{\quad
 |\mathcal T_{V_N,N}(w)-\mathcal T_{U_N,N}(w)|
            \le e C_w K\left(\frac1N+\frac{250}{\pi\log N}\right)
                           \longrightarrow0.
 \quad}                                                       \tag{VIIIp.4.7}
$$
В частности, исходное парное отклонение от min(m,N) сохраняется с ошибкой O_w,K(1/log N). Более общая достаточная ошибка — o(log N/N²). Одновременно QS1 переносит полный слабый процесс. Никакой сходимости высших неограниченных факториальных моментов из (VIIIp.4.7) не утверждается.

Условие точной унитарности аппроксимации тоже можно снять, сохранив исчезающую, хотя менее сильную ошибку. Пусть B_N — произвольная матрица, norm(B_N−U_N)≤epsilon_N. Для неё T_B означает тот же конечный следовый полином из (VIIIp.1.1), без утверждения о фазовом точечном процессе. Пусть поддержка w лежит в [-R,R], W=sup abs(w),
$$
A_w=W e^{2\pi R},\qquad D_w=W(R+1)^3.
$$
Телескопирование даёт равномерно при 1≤m≤RN
$$
|\operatorname{Tr}B_N^m-\operatorname{Tr}U_N^m|/N
                         \le m\epsilon_N e^{RN\epsilon_N}.
$$
Следовательно, квадрат взвешенного расстояния следов удовлетворяет
$$
Z_N:=N^{-2}\sum_{m\ge1}|w(m/N)|
       |\operatorname{Tr}B_N^m-\operatorname{Tr}U_N^m|^2
                 \le D_w\epsilon_N^2N^3e^{2RN\epsilon_N}.    \tag{VIIIp.4.8}
$$
Поскольку abs(w(t))≤A_w exp(−2pi t) при t≥0, (VIIIp.4.6) даёт
$$
\mathcal T_{U_N,N}(|w|)
     \le\frac{A_w}{2}(\mathcal R_{U_N,N}(2\pi)-1)
                         \le\frac{125A_w N}{\pi\log N}.
$$
В выражении T(|w|) используется непосредственно конечная сумма (VIIIp.1.1); гладкость модуля веса для этой оценки не нужна. Неравенство Коши–Шварца для последовательностей следов теперь доказывает
$$
|\mathcal T_{B_N,N}(w)-\mathcal T_{U_N,N}(w)|
 \le2\epsilon_N N^2 e^{RN\epsilon_N}
       \sqrt{\frac{125A_wD_w}{\pi\log N}}
            +D_w\epsilon_N^2N^3e^{2RN\epsilon_N}.             \tag{VIIIp.4.9}
$$
В частности, при epsilon_N≤K/N² это O_w,K(1/sqrt(log N)+1/N), равномерно по всем нечётным N→∞. Достаточна даже epsilon_N=o(sqrt(log N)/N²). Это прямой перенос конечного парного теста к неунитарному параметриксу; нормировки и весь диапазон m порядка N учтены явно.

Для переноса самого слабого процесса можно вместо B взять его унитарную полярную часть V=B(B*B)^{-1/2}. При epsilon<1 все сингулярные числа B лежат между 1−epsilon и 1+epsilon, поскольку этот интервал ограничивает norm(Bx) для каждого единичного x. Поэтому B обратима, V унитарна и
$$
\|V-B\|\le\epsilon,\qquad
                \|V-U\|\le2\epsilon.                        \tag{VIIIp.4.10}
$$
QS1 и (VIIIp.4.7) применимы к V. Никакого фазового процесса для неунитарной B без этой операции не вводится.

Это новый конкретный инструмент для исходной семьи: достаточно контролировать любую предлагаемую параметрикс-матрицу с ошибкой O(1/N²), чтобы её конечный следовый парный тест имел ту же асимптотику. Наивная универсальная граница O(N² epsilon) при такой ошибке даёт лишь O(1); исчезающий остаток здесь получается из уже доказанной коротковременной информации и положительной энергии. Но удобная аппроксимация с доказанным CUE-пределом ещё не построена, так что (VIIIp.4.7) и (VIIIp.4.9) не решают сам тест.

### VIIIp.5. QS4: два общих масштаба действительно различны

Первый масштаб o(1/N) в QS1 нельзя заменить общим O(1/N). Для нечётного N=2n+1 зададим две диагональные унитарные матрицы масштабированными фазами
$$
x_j=j,\qquad y_j=j+\tfrac14(-1)^j,\quad0\le j<N.
$$
Их операторное расстояние равно 2sin(pi/(4N))=O(1/N). Первый процесс — равномерно сдвинутая решётка. У второго на окружности длины N есть n промежутков 1/2, n промежутков 3/2 и один промежуток 1. Единственный дефект виден в фиксированном окне с вероятностью O(1/N); предел — стационарно сдвинутый периодический узор периода два с промежутками 1/2,3/2.

В интервале длины 3/4 вероятность двух точек у первого процесса нулевая, а у второго точно
$$
\frac{n(3/4-1/2)}{N}
                           =\frac{N-1}{8N}\longrightarrow\frac18.
$$
Это различие ограниченного события, а не только неограниченного момента. Для любого меньшего фиксированного сдвига 0<a<1/2 та же конструкция работает с промежутками 1±2a; поэтому речь не о пороге размера константы.

Универсальный абсолютный парный перенос имеет более строгий масштаб. Телескопическая оценка степеней даёт
$$
|\operatorname{Tr}U^m-\operatorname{Tr}V^m|\le Nm\epsilon,
 \quad
 |\mathcal T_{V,N}(w)-\mathcal T_{U,N}(w)|
                         \le2\epsilon\sum_{m\ge1}m|w(m/N)|
                         =O_w(N^2\epsilon).                 \tag{VIIIp.5.1}
$$
Масштаб o(1/N²) в этой общей абсолютной границе нельзя заменить O(1/N²) без контроля положительного момента. Для N=2n+1 возьмём два диагональных блока кратностей n,n+1, с фазами в радианах 0 и 1/N. Вторую семью получим, увеличив фазу второго блока на c/N², где c>0 фиксировано и рационально. Операторное расстояние не больше c/N², и
$$
\mathcal T_{V,N}(w)-\mathcal T_{U,N}(w)
 \longrightarrow-\frac c2\int_0^\infty t w(t)\sin t\,dt.      \tag{VIIIp.5.2}
$$
Для исходного неотрицательного w с поддержкой [-2,2] интеграл строго положителен. Доказательство: коэффициент косинусной перекрёстной части равен
$$
b_N=2n(n+1)/N^2=(1-N^{-2})/2.
$$
При t=m/N аргумент меняется с t на t+ct/N. По Taylor-формуле
$$
\cos(t+ct/N)-\cos t=-ct\sin t/N+O_{c,w}(N^{-2})
$$
равномерно на фиксированной поддержке w. Число членов O_w(N), поэтому суммарный остаток O_c,w(1/N), а основной член — сумма Римана в (VIIIp.5.2). В обоих семействах слабый процесс пустой: весь спектр лежит в ограниченном числе кластеров ширины O(1/N), встречающихся после общего сдвига с вероятностью O(1/N). Таким образом, один слабый предел не передаёт парный момент автоматически.

В этом примере вырождения можно снять сколь угодно малыми различными фазовыми сдвигами o(N⁻²); (VIIIp.5.1) сохраняет (VIIIp.5.2). Для полностью явного снятия достаточно добавить к j-й фазе N⁻⁴·2⁻ʲ. Все ненулевые попарные фазовые разности становятся различными рациональными числами: внутри блоков используется уникальность двоичных разностей, а между блоками центральный сдвиг порядка 1/N отделён от поправок порядка 1/N⁴. По E1 все нетривиальные спектральные отношения трансцендентны. Эти две семьи не являются исходной моделью; они доказывают только резкость универсального переноса.

Контрольный вес w_0(t)=(1−t²/4)^4 при abs(t)<2, нуль вне этого интервала, принадлежит C³_c и подходит под QS3. Для него
$$
\int_0^2w_0=256/315,\quad \|tw_0\|_1=4/5,\quad
 \|(tw_0)''\|_1=118/27,\quad
              C_{w_0}=16\pi/5+118/(27\pi).
$$
Предел (VIIIp.5.2) при c=1 равен приблизительно −0.1264881489717176. Это проверка другого удобного веса, не пересчёт исходной delta_*.

### VIIIp.6. QS5: тот же фиксированный классический предел может иметь пустую локальную статистику

**QS5.** Существует другая детерминированная унитарная семья V_N по всем нечётным N≥3 со следующими свойствами:

- norm(V_N−U_N)≤4N⁻³⁄⁴, где U_N — исходная матрица при буквально фиксированном tau.
- Можно выбрать один и тот же полный ортонормированный собственный базис для U_N и V_N. Все матричные элементы фиксированных наблюдаемых в этом базисе сохраняются.
- Спектр V_N прост; все нетривиальные спектральные отношения трансцендентны и попарно различны; проектных периодов нет.
- Сохраняются исходный главный классический предел F_tau, предельный классический корреляционный профиль и геометрические свойства F_tau из RV4–RV5.
- Сохраняются сильная интенсивностная граница limsup norm(P−J)≤10⁻⁶⁴, плоскость max abs(V_xy)²=O(1/N), коротковременная H1 с теми же степенями и суммируемость вращательного сектора.
- При этом Xi_{V_N,N,alpha} слабо стремится к пустому процессу, а исходный положительный парный момент для этой другой семьи расходится вверх.

Полная точная формула U_N=exp(i tau N A_N)M_N при замене на V_N **не сохраняется**, что ниже отдельно проверено по определителю. Заявленная точность квантового Egorov O(N⁻²) и специальные точечные оценки SG6 для V_N не доказаны; параметрическая дифференциальная система для V_N не построена. Теорема опровергает достаточность только перечисленных сохранённых данных; она не опровергает исходный Sine₂.

Конструкция. Выберем ортонормированный собственный базис U_N, в нём собственные значения lambda_j. Положим
$$
L_N=\lceil N^{3/4}\rceil,\quad \zeta_N=e^{2\pi i/L_N},
 \quad\gamma_N=N^{-4},\quad 1\le j\le N.
$$
Выберем ближайший к lambda_j корень zeta_N^{k_j}, разрешая ничью фиксированным меньшим индексом. Зададим в том же базисе
$$
V_N^0=\operatorname{diag}(\zeta_N^{k_j}),\qquad
 V_N=\operatorname{diag}(\zeta_N^{k_j}e^{i\gamma_N2^{-j}}).
                                                               \tag{VIIIp.6.1}
$$
Если исходный спектр кратен, внутри его пространств можно фиксировать базис последовательной ортогонализацией проекций стандартных координатных векторов. Дополнительной случайности в (VIIIp.6.1) нет. Матрицы U_N и V_N коммутируют; при простом исходном спектре V_N есть конечномерная функция U_N.

По ближайшему углу
$$
\|V_N-U_N\|\le\pi/L_N+N^{-4}\le4/L_N\le4N^{-3/4}.
                                                               \tag{VIIIp.6.2}
$$
Числа 2⁻ʲ−2⁻ᵏ при j≠k попарно различны для упорядоченных пар: для положительной разности её несократимый двоичный знаменатель определяет больший индекс, затем числитель — меньший. Отрицательные разности отличаются знаком. Поэтому отношение двух различных собственных значений V_N имеет вид алгебраического корня единицы, умноженного на exp(iq), где q ненулево и рационально. По E1 это трансцендентное число. Равенство двух таких отношений также потребовало бы exp(iq) быть алгебраическим при ненулевом рациональном q; значит оно возможно лишь для одной и той же упорядоченной пары. Это доказывает все качественные спектральные утверждения, включая отсутствие проектных периодов.

Отдельно проверим, что конструкция действительно меняет точную исходную матрицу при всех нечётных N≥19. У A_N нулевой постоянный Fourier-коэффициент, а все ненулевые метки имеют abs(k)≤9, abs(l)≤1 и потому в этих размерах не дают нулевой метки по модулю N. Следовательно, Tr A_N=0. Тогда det U_N=det M_N алгебраичен, поскольку элементы M_N алгебраичны. В то же время
$$
\det V_N=\zeta_N^{\sum_jk_j}
                \exp\{i\gamma_N(1-2^{-N})\}
$$
трансцендентен по E1. Значит V_N не равно исходному U_N и не удовлетворяет той же точной экспоненциальной формуле. Сам по себе определитель не различает локальные процессы: общий скалярный поворот для них несуществен. Ни проективная, ни микроскопическая эквивалентность V_N и U_N здесь также не доказаны, поэтому QS5 не даёт контрпример к буквально поставленной спектральной задаче.

Все точки V_N находятся в N⁻⁴-окрестностях не более чем L_N центров на окружности. При общем сдвиге вероятность увидеть хотя бы одну точку в фиксированном масштабированном окне [-R,R] не больше
$$
L_N\left(\frac{2R}{N}+\frac{N^{-4}}\pi\right)
                           \longrightarrow0.                \tag{VIIIp.6.3}
$$
Следовательно, весь процесс слабо стремится к пустому. Его средняя интенсивность при каждом конечном N всё ещё равна 1: масса первого момента теряется на редких больших кластерах. Это прямое различие ограниченных Laplace-функционалов с Sine₂, а не вывод из положительной расходимости парного момента.

У V_N^0 все степени, кратные L_N, равны I. Поэтому при s>0
$$
\mathcal R_{V_N^0,N}(s)\ge\coth\frac{sL_N}{2N}.
$$
Телескопическая оценка из (VIIIp.5.1), применённая к полной Poisson-сумме, даёт
$$
|\mathcal R_{V_N,N}(s)-\mathcal R_{V_N^0,N}(s)|
                \le4N^{-4}\frac{e^{-s/N}}{(1-e^{-s/N})^2}
                \le\frac4{s^2N^2}.
$$
Итак,
$$
\mathcal R_{V_N,N}(s)\ge\frac{2N}{sL_N}-\frac4{s^2N^2}
                         \longrightarrow\infty.             \tag{VIIIp.6.4}
$$
Для оригинального w при m=kL_N<2N собственные значения V_N^m имеют аргументы по модулю не больше 2N gamma_N. Тогда
$$
N^{-2}|\operatorname{Tr}V_N^m|^2\ge1-4N^{-6}.
$$
Положительность остальных временных членов и сумма Римана с шагом L_N/N дают
$$
\liminf_{N\to\infty}\frac{L_N}{N}
 \left[\mathcal T_{V_N,N}(w)
  -\frac1{N^2}\sum_{m\ge1}w(m/N)\min(m,N)\right]
                     \ge\int_0^2w(t)\,dt>0.                 \tag{VIIIp.6.5}
$$
Эталонная сумма ограничена и после умножения на L_N/N исчезает. Это нижняя граница; точное равенство в (VIIIp.6.5) не утверждается.

### VIIIp.7. QS6: проверка сохранённых динамических и интенсивностных входов

Пусть B_N ограничена в операторной норме. Для каждого целого m
$$
\|V_N^m B_NV_N^{-m}-U_N^m B_NU_N^{-m}\|
                      \le2|m|\|B_N\|\|V_N-U_N\|.             \tag{VIIIp.7.1}
$$
При фиксированных m и Fourier-метке v правая часть исчезает. Исходный Egorov поэтому даёт для V_N тот же предел Op(E_v composed with F_tau^m); меняется лишь точность на O_m(N⁻³⁄⁴). Для B_N=A_N сравнение нормированных HS-корреляций даёт тот же фиксированный классический профиль C_m(tau) и H_tau. Никакой переход от фиксированного m к m порядка N здесь не выполняется. Полный гладкий централизатор и отсутствие C¹-обращателей — свойства самого F_tau, так что они буквально те же.

Для координатных интенсивностей
$$
\|P(V)-P(U)\|_{2\to2}\le2\|V-U\|.     \tag{VIIIp.7.2}
$$
Действительно, вложение в диагональные матрицы — HS-изометрия, а взятие диагонали — ортогональное сжатие. Сжатие Ad_U на это подпространство равно матрице abs(U_xy)². Разность двух сопряжений имеет HS-операторную норму не больше 2norm(V−U), что доказывает (VIIIp.7.2). Поэтому сильный limsup FM сохраняется. Кроме того,
$$
\max_{x,y}|V_N(x,y)|\le\max_{x,y}|U_N(x,y)|+4N^{-3/4},
$$
так что плоскость порядка 1/N сохраняется с фиксированной константой и даже с той же верхней асимптотической константой, если она задана.

Короткие следы: для N≥33 и всех m≥1 из H1 и (VIIIp.6.2)
$$
\frac{|\operatorname{Tr}V_N^m|^2}{N^2}
 \le2\cdot10^{20}16^{8m}N^{-2/5}+32m^2N^{-3/2}
                  \le3\cdot10^{20}16^{8m}N^{-2/5}.             \tag{VIIIp.7.3}
$$
Использованы m²≤16^{8m} и N⁻³⁄²≤N⁻²⁄⁵. Так сохранены тот же логарифмический диапазон и те же степени убывания, с изменением лишь фиксированной константы.

Для вращательного сектора приведём общий достаточный аргумент. Пусть P интенсивностная матрица унитарного размера N, q=max P_xy≤C_0/N, norm(P−J)≤rho<1, а N достаточно велико для q≤1/4. Если d(x) — наименьший период замкнутого слова длины m, то
$$
D_m=\sum_x d(x)|a(x)|^2
          =m\operatorname{Tr}P^m-R_m,\quad R_m\ge0.
$$
При словах периода d, собственного делителя m, их вес ограничивается следом d-й степени поэлементной степени P^{circ(m/d)}. Её сумма каждой строки не больше q^{m/d−1}. Следовательно,
$$
R_m\le m\sum_{d\mid m,\ d<m}Nq^{m-d}
                   \le m^2Nq^{\lceil m/2\rceil},\quad m\ge2.
$$
Суммирование чётных и нечётных m даёт
$$
\sum_{m\ge2}R_m\le8N\sum_{r\ge1}r^2q^r
 =8Nq\frac{1+q}{(1-q)^3}\le24C_0.                            \tag{VIIIp.7.4}
$$
Пусть E=P−J. Из двойной стохастичности EJ=JE=0. При m≥2
$$
|\operatorname{Tr}E^m|\le\rho^{m-2}\|E\|_{\mathrm{HS}}^2
                                      \le C_0\rho^{m-2},
$$
где использованы HS-неравенство для произведения и sum P_xy²≤Nq. При m=1 abs Tr E≤C_0+1. Вместе с (VIIIp.7.4)
$$
\sum_{m\ge1}|D_m-m|
                  \le25C_0+1+\frac{2C_0}{(1-\rho)^2}.       \tag{VIIIp.7.5}
$$
Для V_N по (VIIIp.7.2) и плоскости можно взять фиксированные C_0 и rho=1/2 при всех достаточно больших N, получая не больше 33C_0+1. Значит сильная суммируемость вращательного сектора тоже сохраняется. Однако её знаковое когерентное дополнение у V_N не имеет нужного предела −delta_*: (VIIIp.6.5) показывает совсем другой парный тест.

Все перечисленные сохранения проверены в точных нормах и режимах. Исходная формула экспоненциального кика нарушается по приведённому определительному инварианту. Для V_N не доказаны точная конечномерная корреляция CW1 и специальные квантовые оценки SG3/SG6; семейство с производной iNA_N V_N не построено. Называть V_N семейством, удовлетворяющим всем прежним входам, было бы неверно.

### VIIIp.8. Статусы и следующий незакрытый шаг

