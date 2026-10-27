Компоненты здесь в координатном порядке единственной открытой цепочки и после удаления фазы; их модули не меняются от этого унитарного сопряжения.

Если $d=7$ и $n\ge3$, произведение связей любой отдельной цепочки $B$ удовлетворяет
$$
\mathcal B_B\ge
              \frac{n^{14}}{(800\cdot16^6)^{\,n-1}}.                \tag{VIIIi.3.6}
$$
В самом деле, каждое $b_x\le4/200=1/50$, а вне этой цепочки ровно $6(n-1)$ ненулевых связей. Разделим $\mathcal B_{\rm tot}$ из (VIIIi.2.1) на их верхнюю оценку. Следовательно, **внутри каждой цепочки**
$$
g_B\ge\frac{118}{25}
             \frac{n^{14}}{(1888\cdot16^6)^{\,n-1}},\qquad
 |v(0)|,\ |v(n-1)|\ge
             \frac{n^{14}}{(1888\cdot16^6)^{\,n-1}}.                \tag{VIIIi.3.7}
$$
При $N=7$ цепочки имеют длину 1, и промежуток внутри них не определён; (VIIIi.3.7) к этому случаю не применяется. Формулы (VIIIi.3.6)–(VIIIi.3.7) не разделяют уровни разных блоков. Простота всего $A_N$ при $7\mid N$ здесь не доказана.

### VIIIi.4. AQ3: целая нормировка и все архимедовы сопряжения

Далее снова $7\nmid N$. Положим
$$
K=\mathbb Q(i,\zeta_N,\sqrt N),\quad D_K=[K:\mathbb Q]\le4N,
 \quad B=4000A_N,\quad C=\sqrt N\,M_N.
                                                                    \tag{VIIIi.4.1}
$$
Буква $C$ здесь обозначает матрицу; биномиальные числа ниже обозначаются $c_k$. Оценка степени следует из уравнения $\zeta_N^N=1$ и двух квадратных присоединений $i,\sqrt N$; неприводимость циклотомического многочлена не требуется.

**Лемма AQ3.** Все элементы $B,C$ — алгебраические целые в $K$. Для любого вложения $\sigma:K\hookrightarrow\mathbb C$
$$
(A_N)^\sigma\ \text{эрмитова},\quad
           \|(A_N)^\sigma\|\le R,\quad
           (M_N)^\sigma\ \text{унитарна}.                           \tag{VIIIi.4.2}
$$
В частности, все корни $p^\sigma(z)$, где $p(z)=\det(zI-B)$, вещественны и принадлежат $[-4720,4720]$.

**Доказательство.** Fourier-коэффициенты исходного $f-1/10$ лежат в $\mathbb Q(i)$; умножение на 4000 делает их гауссовыми целыми. Это проверяется напрямую: коэффициенты $r$ имеют знаменатели, делящие 4; синус вносит множитель $1/(2i)$, косинус по $p$ — $a_\star^{\pm1}/2$, где $a_\star^{\pm1}=(-3\pm4i)/5$. Множители $1/10$, $1/100$ дают общий знаменатель, делящий 4000. Матрицы $T_N$ имеют элементами нули и корни единицы. Элементы $C$ — корни единицы из явного ядра $M_N$. Корни единицы и гауссовы целые алгебраически целые, суммы и произведения таких чисел целы. Последнее следует, например, из конечного модуля, порождённого степенями конечного набора целых образующих, и определительного приёма.

Вложение задаёт $\zeta_N\mapsto\zeta_N^u$, $\gcd(u,N)=1$, $i\mapsto\pm i$, $\sqrt N\mapsto\pm\sqrt N$, с возможными совместными ограничениями. Комплексное сопряжение коммутирует с ним на этих образующих, а значит, на $K$. Применение $\sigma$ к $A_N^*=A_N$ поэтому сохраняет эрмитовость. Каждая $T_N^\sigma$ остаётся унитарной; модули сопряжённых коэффициентов из $\mathbb Q(i)$ сохраняются. Оценка (VIIIi.3.4) даёт $\|A_N^\sigma\|\le R$.

Наконец,
$$
(M_N^\sigma)_{xy}=\frac{\pm1}{\sqrt N}
       \zeta_N^{-u\bar{8}(3x^2-2xy+3y^2)}.
$$
Скалярное произведение различных строк — фаза, умноженная на $N^{-1}\sum_y\zeta_N^{u\bar{4}(x-x')y}=0$; при совпадающих строках оно равно 1. Здесь $u\bar{4}$ обратим по нечётному модулю. Это доказывает унитарность. Число 4720 равно $4000R$. $\square$

В частности, каждый сопряжённый главный минор, определённый через спектральные проекторы ниже, будет иметь модуль не больше 1. Это существенно сильнее грубой оценки произвольного полинома в корнях характеристического многочлена.

### VIIIi.5. AQ4: симметрическое произведение миноров вместо поля разложения

Приведём само доказательство (VIIIi.1.2), включая исключение скрытого множителя $N!$ из степени поля.

Пусть $b_j=4000a_j$, $p(z)=\prod_j(z-b_j)$, и $L$ — поле разложения $p$ над $K$. Спектральные проекторы задаются **рациональной алгебраической**, а не содержащей комплексное сопряжение формулой
$$
P_j=\frac{\operatorname{adj}(b_jI-B)}{p'(b_j)}.
                                                                    \tag{VIIIi.5.1}
$$
Корни $b_j$ алгебраически целы, поскольку $p$ моничен с целыми алгебраическими коэффициентами. Числа $p'(b_j)$ ненулевые по AP1. Поле $L$ может иметь большую степень; мы не оцениваем в нём норму каждого $d_S$ отдельно.

В собственном базисе $B$ точно
$$
\det\!\left(I+M_N\sum_{j=1}^N z_jP_j\right)
                           =\sum_{S}d_S\prod_{j\in S}z_j.           \tag{VIIIi.5.2}
$$
Действительно, сопряжение переводит $\sum_jz_jP_j$ в диагональную матрицу $\operatorname{diag}z_j$; разложение определителя $I+\widehat M\operatorname{diag}z_j$ по выбранным столбцам даёт именно главные миноры. Это также доказывает алгебраичность $d_S\in L$ без выбора алгебраически нормированных собственных векторов.

Зафиксируем $k$, $1\le k\le N$, и положим
$$
c_k=\binom Nk,\quad r_k=\binom{N-1}{k-1},\quad
                     G_k=\prod_{|S|=k}d_S.
$$
Рассмотрим целые алгебраические числители
$$
F_S=(\sqrt N)^k\!\left(\prod_{j\in S}p'(b_j)\right)d_S.              \tag{VIIIi.5.3}
$$
Их целостность следует из (VIIIi.5.2): это коэффициент при $\prod_{j\in S}z_j$ в
$$
\det\!\left(I+C\sum_{j\in S}z_j\operatorname{adj}(b_jI-B)\right).
$$
Здесь все матричные элементы целы алгебраически, поэтому коэффициент цел. Многочлен определителя многолинеен по указанным весам ранга 1; в нужном коэффициенте каждый знаменатель $p'(b_j)$ появляется ровно один раз.

Каждый корень $b_j$ входит ровно в $r_k$ множеств размера $k$. Следовательно,
$$
Z_k:=\prod_{|S|=k}F_S
    =(\sqrt N)^{k c_k}
       \left(\prod_{j=1}^Np'(b_j)\right)^{r_k}G_k.                  \tag{VIIIi.5.4}
$$
Произведение всех $p'(b_j)$ равно, с точностью до знака, дискриминанту
$$
\delta=\prod_{j<h}(b_j-b_h)^2\in K\setminus\{0\}.
$$
Все автоморфизмы $L/K$ переставляют корни, спектральные проекторы и множества $S$, сохраняя $B,C$. Поэтому $G_k,Z_k$ лежат в $K$. Здесь достаточно следующего элементарного свойства поля разложения в характеристике 0: все сопряжения элемента над $K$ продолжаются до вложений поля разложения, а его нормальность делает их автоморфизмами; элемент, неподвижный относительно всех таких автоморфизмов, имеет минимальный многочлен степени 1. Продолжение строится последовательно выбором корня минимального многочлена каждого присоединяемого элемента. Это обосновывает использованную симметрию без предположения, что степень $L$ мала.

По AP4 каждый $d_S\ne0$. Поэтому $Z_k\ne0$; это **ненулевое алгебраическое целое в $K$**.

Для любого $\sigma:K\hookrightarrow\mathbb C$ продолжим $\sigma$ до вложения $L$ в $\mathbb C$. Корни переходят в различные вещественные собственные значения $B^\sigma$, а (VIIIi.5.1) — в его ортогональные проекторы. Матрица $M_N^\sigma$ унитарна по AQ3. Поэтому
$$
|d_S^\sigma|\le1,\qquad |G_k^\sigma|\le1.
$$
Первое не зависит от нормировок векторов: соответствующий главный блок унитарной матрицы — сжатие нормы не больше 1, а модуль его определителя не больше 1.

Расстояние любых двух корней $p^\sigma$ не больше $9440=2\cdot4720$. Из (VIIIi.5.4), $r_k=kc_k/N$ получаем
$$
|Z_k^\sigma|
   \le N^{k c_k/2}\,9440^{\,N(N-1)r_k}
   =\exp\{L_k\},\quad
 L_k=kc_k[\tfrac12\log N+(N-1)\log9440].                            \tag{VIIIi.5.5}
$$
Норма $Z_k$ из $K$ в $\mathbb Q$ — ненулевое целое число. Действительно, произведение сопряжений рационально и алгебраически цело; рациональное алгебраическое целое — целое, что видно из монического уравнения и сокращённого знаменателя. Поэтому
$$
1\le|\operatorname{Nm}_{K/\mathbb Q}Z_k|
          \le |Z_k| e^{(D_K-1)L_k},\qquad
                        |Z_k|\ge e^{-(D_K-1)L_k}.                 \tag{VIIIi.5.6}
$$
Модуль множителя перед $G_k$ в (VIIIi.5.4) не больше $e^{L_k}$. Значит,
$$
|G_k|\ge e^{-D_KL_k}.
$$
Все $|d_S|\le1$, поэтому произведение $|G_k|$ не превосходит каждого своего множителя. Следовательно,
$$
|d_S|\ge e^{-D_K L_k}
        \ge e^{-4Nk c_k[\frac12\log N+(N-1)\log9440]},
$$
что доказывает первую оценку (VIIIi.1.2).

Для второй используем $\log9440<10$ и $\log N\le N$:
$$
\tfrac12\log N+(N-1)\log9440\le\tfrac{21}{2}N.
$$
Отсюда показатель не больше $42kN^2c_k$. Наконец, $k\le N$, $c_k\le2^N$ дают (VIIIi.1.3). Все константы действуют одновременно по всем допустимым $N,k,S$. $\square$

Таким образом, ненулевость AP4 и новая оценка нормы используются в разных местах. Без AP4 норма $Z_k$ могла бы быть нулевой, и никакой нижней оценки из целостности не следовало бы.

### VIIIi.6. AQ5: полностью явный комплексный спектральный свидетель

Докажем (VIIIi.1.4)–(VIIIi.1.5), усилив конечномерный аргумент AP5 и раскрыв его зависимость от $N$.

Пусть $H_s=e^{sA_N}M_N$, $s\ge0$, и $e_k(H_s)$ — элементарные симметрические функции собственных значений. Обозначим
$$
\ell_k=\sum_{j=N-k+1}^{N}a_j,\quad
 d_k=d_{\{N-k+1,\ldots,N\}},\quad
 c=\max_k\binom Nk,\quad d_*=\min_{0\le k\le N}|d_k|,\quad g=g_N.
$$
Это конечномерные величины, зависящие от $N$. Они не совпадают с тестовой константой $\delta_*$ исходной задачи. Разложение по главным минорам даёт точно
$$
e_k(H_s)=\sum_{|S|=k}d_S e^{s\sum_{j\in S}a_j}
              =d_ke^{s\ell_k}+R_k,\qquad
 |R_k|\le c\,e^{s(\ell_k-g)},                                      \tag{VIIIi.6.1}
$$
где при $k=0,N$ остаток равен нулю. Действительно, наибольшая сумма $k$ уровней уникальна; замена хотя бы одного верхнего уровня уменьшает сумму не меньше чем на $g$. Также по всем $k$
$$
|e_k(H_s)|\le c e^{s\ell_k}.              \tag{VIIIi.6.2}
$$

Потребуем
$$
s\ge \frac3g\log\frac{8(N+1)c}{d_*}.              \tag{VIIIi.6.3}
$$
Тогда главный член в (VIIIi.6.1) имеет модуль не меньше $(d_*/2)e^{s\ell_k}$.

Рассмотрим характеристический многочлен
$$
P_s(z)=\sum_{k=0}^N(-1)^k e_k(H_s)z^{N-k}.
$$
На окружности $|z|=e^{s\theta}$ положим $\Phi_k=\ell_k+(N-k)\theta$. Если $\theta$ находится между двумя соседними $a_j$, наибольшая $\Phi_k$ единственна; её индекс $k_0=N-\#\{a_j<\theta\}$. Для
$$
\theta=a_j-g/3\quad\text{или}\quad a_j+g/3
$$
расстояние от $\theta$ до любого уровня $a_h$ не меньше $g/3$. Поскольку
$\Phi_{k+1}-\Phi_k=a_{N-k}-\theta$, каждый другой член уступает главному не меньше $sg/3$ в экспоненте. Из (VIIIi.6.1)–(VIIIi.6.3)
$$
\sum_{k\ne k_0}
  \frac{|e_k(H_s)|\,|z|^{N-k}}{|e_{k_0}(H_s)|\,|z|^{N-k_0}}
          \le \frac{2(N+1)c}{d_*}\,e^{-sg/3}\le\frac14.             \tag{VIIIi.6.4}
$$
Значит, при гомотопии, линейно включающей все остальные мономы, на этой окружности нет нулей. Число корней внутри сохраняется и равно степени главного монома $N-k_0$. Это можно увидеть непосредственно: интеграл изменения аргумента по окружности — целое число, непрерывно зависящее от параметра гомотопии, и потому постоянно. Для полинома он равен числу корней внутри, поскольку каждый множитель $z-\lambda$ даёт 1 или 0 в зависимости от положения корня. При $\theta=a_j-g/3$ внутри $j-1$ корней, при $\theta=a_j+g/3$ — $j$. Поэтому в каждом из $N$ непересекающихся кольцевых интервалов (VIIIi.1.5) ровно один корень с учётом кратности. Они простые, и все модули различны.

Осталось проверить, что наше полностью явное $s_N$ удовлетворяет (VIIIi.6.3). По AQ2 и AQ4
$$
\frac3g\le\frac{75}{118}\frac{1888^{\,N-1}}{N^2},\qquad
           d_*\ge e^{-42N^3 2^N},\qquad c\le2^N.
$$
Для $N\ge3$, $\log[8(N+1)c]\le3N$, поэтому
$$
\log\frac{8(N+1)c}{d_*}\le43N^3 2^N.
$$
Отсюда правая часть (VIIIi.6.3) не больше
$$
\frac{3225}{118}N\,1888^{\,N-1}2^N
       =\frac{3225}{118\cdot1888}\,N\,3776^N
       <N\,3776^N=s_N.
$$
Здесь $3225<118\cdot1888$; никаких скрытых зависящих от $N$ констант нет. Это доказывает AQ5. $\square$

Дополнительно из (VIIIi.1.5), для соседних упорядоченных по модулю корней
$$
\log|\lambda_{j+1}(s)|-\log|\lambda_j(s)|>sg_N/3.
$$
Это оценка только на указанном комплексном луче $t=-is/N$, а не расстояния между собственными фазами исходного $U_N(\tau)$.

### VIIIi.7. Где именно количественный перенос на исходное время остановился

Новые оценки устраняют две неявные конечномерные константы AP5: $g_N$ и нижнюю границу на главные миноры. Однако следующий шаг был бы другим утверждением.

В исходном собственном базисе $A_N$, при вещественном $\tau$, секулярные коэффициенты равны
$$
e_k(U_N(\tau))
          =\sum_{|S|=k}d_S e^{\,i\tau N\sum_{j\in S}a_j}.            \tag{VIIIi.7.1}
$$
Все экспоненты в (VIIIi.7.1) имеют модуль 1. Никакого экспоненциального превосходства максимальной суммы уровней, использованного в (VIIIi.6.1), здесь нет. Арифметическая лемма E3 исключает некоторые точные нули, но не оценивает абсолютную величину суммы (VIIIi.7.1).

Даже сам достаточный порог (VIIIi.6.3) не может иметь порядок $\tau N$ в пределе. Действительно, из $\|A_N\|\le R$
$$
g_N\le\frac{2R}{N-1},\qquad
 c\ge\frac{2^N}{N+1},\qquad d_*\le1.
$$
Поэтому величина именно этого достаточного порога удовлетворяет
$$
\frac3{g_N}\log\frac{8(N+1)c}{d_*}
       \ge \frac{3(N-1)}{2R}\,[N\log2+\log8].                      \tag{VIIIi.7.2}
$$
Она по крайней мере квадратична по $N$, тогда как $\tau N$ линейна. (VIIIi.7.2) не является нижней оценкой на минимально возможное время появления простого спектра; она лишь точно показывает, что данный аргумент доминирующего монома не приближается к нужному режиму даже при улучшении его неизвестных констант.

На временах $m\asymp N$ в следах появляются фазы масштаба $\tau N m$. Нижняя оценка на **минимальный** промежуток генератора (VIIIi.1.1) не даёт нижней оценки на все разности сумм $m$ его уровней и не обеспечивает компенсацию коэффициентов соответствующей экспоненциальной суммы. Кроме того, по принципу Дирихле существует соседняя пара с $g_N\le2R/(N-1)$, так что попытка равномерно осциллировать все элементарные разные фазы уже на одном шаге также не следует из новых результатов.

**Полученная математическая информация:** связь циклотомического произведения с концевым кофактором даёт экспоненциальную, а не произведение худших степенных оценок, границу на промежутки генератора. Симметризация миноров устраняет степень поля разложения из оценки и даёт явные количественные границы при фиксированном размере минора. **Новой оценки исходной смешанной следовой суммы не получено.**

#### VIIIi.7.1. AQ6: почему E3 не оценивает величину по одним модулям коэффициентов

Зафиксируем буквально $\tau=10^{-80}$. Для каждого целого $L\ge0$ положим
$$
q_L=\sum_{r=0}^{L}\frac{(i\tau)^r}{r!}\in\mathbb Q(i),\qquad
                         F_L(t)=e^{it}-q_L.
$$
Множество частот $\{0,i\}$ не зависит от $L$; модули обоих коэффициентов не больше 3. Тем не менее
$$
0<|F_L(\tau)|
               \le e^\tau\frac{\tau^{L+1}}{(L+1)!}\longrightarrow0.
                                                                    \tag{VIIIi.7.3}
$$
Ненулевость следует из E1: $e^{i\tau}$ трансцендентно, а $q_L$ алгебраично. Верхняя оценка получается суммированием хвоста абсолютно сходящегося ряда экспоненты, используя $(L+1+j)!\ge(L+1)!\,j!$. Также $|q_L|\le e^\tau<3$. Это самостоятельное точное утверждение по каждому $L$, а не численная иллюстрация.

У рациональных коэффициентов $q_L$ растут знаменатели: общим знаменателем можно взять $(10^{80})^L L!$. Поэтому AQ6 не исключает эффективных оценок с дополнительным контролем арифметической высоты. Он исключает только попытку получить их из E3, фиксированных частот и верхних архимедовых оценок коэффициентов. В исходной модели такие коэффициенты зависят от $N$; переход к их экспоненциальным значениям не сохраняет целочисленную норму, использованную в (VIIIi.5.6). AQ6 не является контрпримером к исходному спектральному закону.

### VIIIi.8. Живые маршруты, доказанные части и открытые обязательства

| Маршрут | Выполненный новый шаг | Статус и точная граница |
|---|---|---|
| Количественная арифметика генератора | Точное произведение связей по всем нечётным N; явные промежутки и концевые компоненты | AQ1–AQ2 доказаны; для $7\mid N$ промежутки лишь внутри цепочек |
| Количественная арифметика сжатий | Нормы симметрических произведений в поле степени не больше $4N$ | AQ3–AQ4 доказаны при $7\nmid N$; не оценена сумма их разных фаз |
| Комплексный свидетель и перенос к исходной оси | Явный луч и раздельные кольца собственных значений; проверено его ограничение | AQ5 доказана; на вещественной оси механизм (VIIIi.6.4) не действует |
| Продолжение к размерностям, кратным 7 | Общие произведения и промежутки внутри блоков получены | Полная простота и нужные смешанные миноры остаются открытыми; известный нулевой граничный минор при N=49 не пересчитывался |

**ДОКАЗАНО:**

- AQ1: точное произведение всех ненулевых связей, включая все нечётные составные размерности.
- AQ2: кофакторная оценка промежутков и концов, затем (VIIIi.1.1), (VIIIi.3.5), (VIIIi.3.7).
- AQ3: целая нормировка $4000A_N,\sqrt N M_N$ и контроль всех сопряжений.
- AQ4: оценки каждого главного сжатия (VIIIi.1.2)–(VIIIi.1.3), с использованием прежней ненулевости AP4.
- AQ5: явный количественный комплексный свидетель (VIIIi.1.4)–(VIIIi.1.5).
- AQ6: точный двухчастотный пример (VIIIi.7.3), отделяющий качественную трансцендентность от нижней оценки величины при контроле только модулей коэффициентов.

**OUTLINE:**

- AQ1 $\Rightarrow$ AQ2 — завершённый переход.
- AP4 + AQ3 + симметризация $\Rightarrow$ AQ4 — завершённый переход.
- AQ2 + AQ4 + счёт корней $\Rightarrow$ AQ5 — завершённый переход.
- AQ5 + E3 сохраняют прежний качественный вывод AP6 для исходного алгебраического времени; нового микроскопического следствия в этом outline нет.

**НЕДОКАЗАНО:**

- U-Q1: количественная знаковая компенсация исходных смешанных фаз при $m/N$ в фиксированном интервале; в частности, исходная взвешенная сумма $Y\to-\delta_*$.
- U-Q2: оценки, достаточные для всех фиксированных порядков из исходного PDF, либо непосредственная оценка ограниченного Laplace-функционала.
- U-Q3: полный аналог AP4–AP6 для бесконечной подпоследовательности $7\mid N$; промежутки между разными цепочками и смешанные сжатия.
- U-Q4: равномерные расстояния между собственными фазами самого $U_N(\tau)$ и их коллективная статистика. Даже такая нижняя оценка сама по себе не была бы полным критерием Sine₂.

Трудным местом остаётся не конечномерная ненулевость: теперь у неё есть явные границы. Трудность — коллективная сумма очень многих комплексных слагаемых на вещественной оси. Исчезновение одного точного резонанса не оценивает сумму близких резонансов, а оценка в мнимом времени опирается на рост модулей, отсутствующий в унитарном режиме.

Продолжать арифметический маршрут к исходному закону имеет смысл только с новым механизмом контроля **всей** суммы (VIIIi.7.1) или соответствующих смешанных следов. Увеличение комплексного свидетеля и повторение проверки ненулевости не меняют U-Q1. Маршрут для семи цепочек остаётся открытым: для него изменился вход (теперь известны общие произведения и внутренние промежутки), но нулевой граничный Fourier-минор всё ещё требует иной организации смешанных членов.

### VIIIi.9. Область проверки и ограничения

Доказательства выше получены текстом, а не конечным перебором. Отдельно использованы точные hosted-вычисления Wolfram для проверки коэффициентных знаменателей, десяти циклотомических произведений, пяти общих кофакторных тождеств и симметрического очищения знаменателей на независимой трёхмерной модели.

Трёхмерная модель проверяет алгебраический механизм AQ4, а не является подменой исходных $A_N,M_N$. В ней также проверены ортонормированность собственного базиса, непосредственное совпадение миноров из этого базиса с проекторной формулой, целостность числителей и обязательный отрицательный случай с нулевым произведением. Ошибочные и промежуточные вычислительные входы сохранены отдельно и не считаются подтверждением.

Самопроверка выполнена тем же исполнителем. Независимого рецензирования, формальной верификации и проверки научной новизны не было. Полный исходный предел остаётся открытым.

### VIIIi.10. Полные символьные входы и сохранённые ответы

Всего шесть hosted-вызовов. Два являются текущими корректными проверками; три диагностических входа не используются как подтверждение; один корректный промежуточный вход заменён усиленным. Для всех конечных выводов область проверки указана буквально. Новый локальный v2-manifest не заявляется.

#### VIIIi.10.1. cyclotomic_products

Точная конечная проверка пройдена; текущий вход.

```wolfram
ClearAll[z,p,a,r,f,coef,nn,dd,quot,ker,bs,ds,mat];
a=(-3+4 I)/5;
r=(1-(z^7+z^-7)/2)(1+(z+z^-1)/2);
f=Expand[(z^7+z^-7)/2+r/10+r(z-z^-1)/(200 I)+r(p/a+a/p)/200-1/10];
coef=Flatten[Table[Coefficient[Coefficient[Expand[f z^9 p],z,k+9],p,l+1],{k,-9,9},{l,-1,1}]];
den=Apply[LCM,Flatten[({Denominator[Re[#]],Denominator[Im[#]]}& /@ coef)]];
products=Table[
 dd=GCD[nn,7];quot=Cancel[(z^nn-1)/(z^dd-1)];
 With[{got=Factor[Resultant[quot,1-z^7,z]^2 Resultant[quot,1+z,z]^2/(4^(nn-dd) Resultant[quot,z,z]^8)]},
 <|"N"->nn,"chains"->dd,"exactNonzeroBondProduct"->got,"identity"->TrueQ[got==(nn/dd)^(2dd)/4^(nn-dd)]|>],
 {nn,{3,5,7,9,15,21,25,35,49,63}}];
cof=Table[
 bs=Array[b,nn-1];ds=Array[d,nn];
 mat=Table[Which[j==k,z-ds[[j]],j==k+1,-bs[[k]],k==j+1,-bs[[j]],True,0],{j,nn},{k,nn}];
 TrueQ[Expand[(-1)^(nn+1)Det[mat[[Range[nn-1],Range[2,nn]]]]-Times@@bs]==0],
 {nn,2,6}];
<|"kernelVersion"->$Version,"FourierDenominatorLCM"->den,
"constant4000ClearsCoefficients"->And@@(IntegerQ /@ Flatten[({4000 Re[#],4000 Im[#]}& /@coef)]),
"sourceNormCertificate"->(11/10+4/100+4/100==59/50),
"bondProducts"->products,"cofactorIdentitiesN2Through6"->cof|>
```

Сохранённый ответ:

```json
{
  "content": [
    {
      "type": "text",
      "text": "Out[1]= <|\"kernelVersion\" -> \"15.0.1 for Linux x86 (64-bit) (July 2, 2026)\", \"FourierDenominatorLCM\" -> 4000, \"constant4000ClearsCoefficients\" -> True, \"sourceNormCertificate\" -> True, \"bondProducts\" -> {<|\"N\" -> 3, \"chains\" -> 1, \"exactNonzeroBondProduct\" -> 9/16, \"identity\" -> True|>, <|\"N\" -> 5, \"chains\" -> 1, \"exactNonzeroBondProduct\" -> 25/256, \"identity\" -> True|>, <|\"N\" -> 7, \"chains\" -> 7, \"exactNonzeroBondProduct\" -> 1, \"identity\" -> True|>, <|\"N\" -> 9, \"chains\" -> 1, \"exactNonzeroBondProduct\" -> 81/65536, \"identity\" -> True|>, <|\"N\" -> 15, \"chains\" -> 1, \"exactNonzeroBondProduct\" -> 225/268435456, \"identity\" -> True|>, <|\"N\" -> 21, \"chains\" -> 7, \"exactNonzeroBondProduct\" -> 4782969/268435456, \"identity\" -> True|>, <|\"N\" -> 25, \"chains\" -> 1, \"exactNonzeroBondProduct\" -> 625/281474976710656, \"identity\" -> True|>, <|\"N\" -> 35, \"chains\" -> 7, \"exactNonzeroBondProduct\" -> 6103515625/72057594037927936, \"identity\" -> True|>, <|\"N\" -> 49, \"chains\" -> 7, \"exactNonzeroBondProduct\" -> 678223072849/19342813113834066795298816, \"identity\" -> True|>, <|\"N\" -> 63, \"chains\" -> 7, \"exactNonzeroBondProduct\" -> 22876792454961/5192296858534827628530496329220096, \"identity\" -> True|>}, \"cofactorIdentitiesN2Through6\" -> {True, True, True, True, True}|>"
    }
  ],
  "structuredContent": null,
  "isError": false
}
```

#### VIIIi.10.2. minor_initial

Отвергнутый вход: несвязанный итератор в чистой функции; диагностические Part/Fold-сообщения.

```wolfram
ClearAll[z,y,xx,bvals,pp,pders,proj,raw,subset,coeff,fc,dc,pr,zz,hh];
dim=3;bm={{0,1,0},{1,0,1},{0,1,0}};
bvals={-Sqrt[2],0,Sqrt[2]};pp=Expand[Det[z IdentityMatrix[dim]-bm]];
pders=(D[pp,z]/.z->#)& /@ bvals;
proj=Table[FullSimplify[Apply[Dot,Prepend[Table[If[j==l,Nothing,(bm-bvals[[l]]IdentityMatrix[dim])/(bvals[[j]]-bvals[[l]])],{l,dim}],IdentityMatrix[dim]]]],{j,dim}];
wv={1,2,3};mm=IdentityMatrix[dim]-Outer[Times,wv,wv]/7;cc=7;
xx=Array[x,dim];raw=Table[FullSimplify[pders[[j]]proj[[j]]],{j,dim}];
coeff[expr_,ss_]:=Fold[Coefficient[#1,xx[[#2]],1]&,Expand[expr],ss];
records=Table[
 subset=Subsets[Range[dim],{kk}];hh=Binomial[dim,kk];rr=Binomial[dim-1,kk-1];
 dc=FullSimplify[coeff[Det[IdentityMatrix[dim]+mm.Sum[xx[[j]]proj[[j]],{j,ss}]],ss]]& /@ subset;
 fc=FullSimplify[coeff[Det[IdentityMatrix[dim]+cc mm.Sum[xx[[j]]raw[[j]],{j,ss}]],ss]]& /@ subset;
 pr=FullSimplify[Times@@dc];zz=FullSimplify[Times@@fc];
 <|"k"->kk,"compressedPrincipalMinors"->dc,"theirProduct"->pr,
 "integralSymmetricProduct"->zz,
 "exactDenominatorIdentity"->TrueQ[FullSimplify[zz==cc^(kk hh)(Times@@pders)^rr pr]],
 "allNumeratorsAlgebraicIntegers"->And@@Table[With[{mp=MinimalPolynomial[v,y]},And[Coefficient[mp,y,Exponent[mp,y]]==1,And@@(IntegerQ /@ CoefficientList[mp,y])]],{v,fc}]|>,
 {kk,1,dim}];
zeroMM=RotateLeft[IdentityMatrix[3]];
negative=Product[zeroMM[[j,j]],{j,3}];
<|"kernelVersion"->$Version,"projectorResolution"->TrueQ[FullSimplify[Total[proj]==IdentityMatrix[3]]],
"simpleDiscriminant"->Discriminant[pp,z],"unitaryM"->TrueQ[mm.Transpose[mm]==IdentityMatrix[3]],
"records"->records,"negativeMissingNonzeroHypothesis"->TrueQ[negative==0]|>
```

Сохранённый ответ:

```json
{
  "content": [
    {
      "type": "text",
      "text": "Part::pkspec1: The expression j cannot be used as a part specification.\nPart::pkspec1: The expression j cannot be used as a part specification.\nPart::pkspec1: The expression j cannot be used as a part specification.\nGeneral::stop: Further output of Part::pkspec1 will be suppressed during this calculation.\nGeneral::stop: Further output of Part::pkspec1 will be suppressed during this calculation.\nFold::normal: Nonatomic expression expected at position 3 in Fold[Coefficient[#1, xx[[#2]], 1] & , 1 + 3*{{6/ ... }}}[[j]]*{x[1], x[2], x[3]}[[j]], {j, ss}], ss].\nFold::normal: Nonatomic expression expected at position 3 in Fold[Coefficient[#1, xx[[#2]], 1] & , 1 + 3*{{6/ ... }}}[[j]]*{x[1], x[2], x[3]}[[j]], {j, ss}], ss].\nFold::normal: Nonatomic expression expected at position 3 in Fold[Coefficient[#1, xx[[#2]], 1] & , 1 + 3*{{6/ ... }}}[[j]]*{x[1], x[2], x[3]}[[j]], {j, ss}], ss].\nFold::normal: Nonatomic expression expected at position 3 in Fold[Coefficient[#1, xx[[#2]], 1] & , 1 + 3*{{6/ ... }}}[[j]]*{x[1], x[2], x[3]}[[j]], {j, ss}], ss].\nFold::normal: Nonatomic expression expected at position 3 in Fold[Coefficient[#1, xx[[#2]], 1] & , 1 + 3*{{6/ ... }}}[[j]]*{x[1], x[2], x[3]}[[j]], {j, ss}], ss].\nGeneral::stop: Further output of Fold::normal will be suppressed during this calculation.\nGeneral::messages: Messages were generated which may indicate errors.\n\nOut[1]= <|\"kernelVersion\" -> \"15.0.1 for Linux x86 (64-bit) (July 2, 2026)\", \"projectorResolution\" -> True, \"simpleDiscriminant\" -> 32, \"unitaryM\" -> True, \"records\" -> {<|\"k\" -> 1, \"compressedPrincipalMinors\" -> {Fold[Coefficient[#1, xx[[#2]], 1] & , 1 + 3*{{6/7, -2/7, -3/7}, {-2/7, 3/7, -6/7}, {-3/7, -6/7, -2/7}} . Sum[{{{1/4, -1/2*1/Sqrt[2], 1/4}, {-1/2*1/Sqrt[2], 1/2, -1/2*1/Sqrt[2]}, {1/4, -1/2*1/Sqrt[2], 1/4}}, {{1/2, 0, -1/2}, {0, 0, 0}, {-1/2, 0, 1/2}}, {{1/4, 1/(2*Sqrt[2]), 1/4}, {1/(2*Sqrt[2]), 1/2, 1/(2*Sqrt[2])}, {1/4, 1/(2*Sqrt[2]), 1/4}}}[[j]]*{x[1], x[2], x[3]}[[j]], {j, ss}], ss], Fold[Coefficient[#1, xx[[#2]], 1] & , 1 + 3*{{6/7, -2/7, -3/7}, {-2/7, 3/7, -6/7}, {-3/7, -6/7, -2/7}} . Sum[{{{1/4, -1/2*1/Sqrt[2], 1/4}, {-1/2*1/Sqrt[2], 1/2, -1/2*1/Sqrt[2]}, {1/4, -1/2*1/Sqrt[2], 1/4}}, {{1/2, 0, -1/2}, {0, 0, 0}, {-1/2, 0, 1/2}}, {{1/4, 1/(2*Sqrt[2]), 1/4}, {1/(2*Sqrt[2]), 1/2, 1/(2*Sqrt[2])}, {1/4, 1/(2*Sqrt[2]), 1/4}}}[[j]]*{x[1], x[2], x[3]}[[j]], {j, ss}], ss], Fold[Coefficient[#1, xx[[#2]], 1] & , 1 + 3*{{6/7, -2/7, -3/7}, {-2/7, 3/7, -6/7}, {-3/7, -6/7, -2/7}} . Sum[{{{1/4, -1/2*1/Sqrt[2], 1/4}, {-1/2*1/Sqrt[2], 1/2, -1/2*1/Sqrt[2]}, {1/4, -1/2*1/Sqrt[2], 1/4}}, {{1/2, 0, -1/2}, {0, 0, 0}, {-1/2, 0, 1/2}}, {{1/4, 1/(2*Sqrt[2]), 1/4}, {1/(2*Sqrt[2]), 1/2, 1/(2*Sqrt[2])}, {1/4, 1/(2*Sqrt[2]), 1/4}}}[[j]]*{x[1], x[2], x[3]}[[j]], {j, ss}], ss]}, \"theirProduct\" -> Fold[Coefficient[#1, xx[[#2]], 1] & , 1 + 3*{{6/7, -2/7, -3/7}, {-2/7, 3/7, -6/7}, {-3/7, -6/7, -2/7}} . Sum[{{{1/4, -1/2*1/Sqrt[2], 1/4}, {-1/2*1/Sqrt[2], 1/2, -1/2*1/Sqrt[2]}, {1/4, -1/2*1/Sqrt[2], 1/4}}, {{1/2, 0, -1/2}, {0, 0, 0}, {-1/2, 0, 1/2}}, {{1/4, 1/(2*Sqrt[2]), 1/4}, {1/(2*Sqrt[2]), 1/2, 1/(2*Sqrt[2])}, {1/4, 1/(2*Sqrt[2]), 1/4}}}[[j]]*{x[1], x[2], x[3]}[[j]], {j, ss}], ss]^3, \"integralSymmetricProduct\" -> Fold[Coefficient[#1, xx[[#2]], 1] & , 1 + 21*{{6/7, -2/7, -3/7}, {-2/7, 3/7, -6/7}, {-3/7, -6/7, -2/7}} . Sum[{{{1, -Sqrt[2], 1}, {-Sqrt[2], 2, -Sqrt[2]}, {1, -Sqrt[2], 1}}, {{-1, 0, 1}, {0, 0, 0}, {1, 0, -1}}, {{1, Sqrt[2], 1}, {Sqrt[2], 2, Sqrt[2]}, {1, Sqrt[2], 1}}}[[j]]*{x[1], x[2], x[3]}[[j]], {j, ss}], ss]^3, \"exactDenominatorIdentity\" -> False, \"allNumeratorsAlgebraicIntegers\" -> False|>, <|\"k\" -> 2, \"compressedPrincipalMinors\" -> {Fold[Coefficient[#1, xx[[#2]], 1] & , 1 + 3*{{6/7, -2/7, -3/7}, {-2/7, 3/7, -6/7}, {-3/7, -6/7, -2/7}} . Sum[{{{1/4, -1/2*1/Sqrt[2], 1/4}, {-1/2*1/Sqrt[2], 1/2, -1/2*1/Sqrt[2]}, {1/4, -1/2*1/Sqrt[2], 1/4}}, {{1/2, 0, -1/2}, {0, 0, 0}, {-1/2, 0, 1/2}}, {{1/4, 1/(2*Sqrt[2]), 1/4}, {1/(2*Sqrt[2]), 1/2, 1/(2*Sqrt[2])}, {1/4, 1/(2*Sqrt[2]), 1/4}}}[[j]]*{x[1], x[2], x[3]}[[j]], {j, ss}], ss], Fold[Coefficient[#1, xx[[#2]], 1] & , 1 + 3*{{6/7, -2/7, -3/7}, {-2/7, 3/7, -6/7}, {-3/7, -6/7, -2/7}} . Sum[{{{1/4, -1/2*1/Sqrt[2], 1/4}, {-1/2*1/Sqrt[2], 1/2, -1/2*1/Sqrt[2]}, {1/4, -1/2*1/Sqrt[2], 1/4}}, {{1/2, 0, -1/2}, {0, 0, 0}, {-1/2, 0, 1/2}}, {{1/4, 1/(2*Sqrt[2]), 1/4}, {1/(2*Sqrt[2]), 1/2, 1/(2*Sqrt[2])}, {1/4, 1/(2*Sqrt[2]), 1/4}}}[[j]]*{x[1], x[2], x[3]}[[j]], {j, ss}], ss], Fold[Coefficient[#1, xx[[#2]], 1] & , 1 + 3*{{6/7, -2/7, -3/7}, {-2/7, 3/7, -6/7}, {-3/7, -6/7, -2/7}} . Sum[{{{1/4, -1/2*1/Sqrt[2], 1/4}, {-1/2*1/Sqrt[2], 1/2, -1/2*1/Sqrt[2]}, {1/4, -1/2*1/Sqrt[2], 1/4}}, {{1/2, 0, -1/2}, {0, 0, 0}, {-1/2, 0, 1/2}}, {{1/4, 1/(2*Sqrt[2]), 1/4}, {1/(2*Sqrt[2]), 1/2, 1/(2*Sqrt[2])}, {1/4, 1/(2*Sqrt[2]), 1/4}}}[[j]]*{x[1], x[2], x[3]}[[j]], {j, ss}], ss]}, \"theirProduct\" -> Fold[Coefficient[#1, xx[[#2]], 1] & , 1 + 3*{{6/7, -2/7, -3/7}, {-2/7, 3/7, -6/7}, {-3/7, -6/7, -2/7}} . Sum[{{{1/4, -1/2*1/Sqrt[2], 1/4}, {-1/2*1/Sqrt[2], 1/2, -1/2*1/Sqrt[2]}, {1/4, -1/2*1/Sqrt[2], 1/4}}, {{1/2, 0, -1/2}, {0, 0, 0}, {-1/2, 0, 1/2}}, {{1/4, 1/(2*Sqrt[2]), 1/4}, {1/(2*Sqrt[2]), 1/2, 1/(2*Sqrt[2])}, {1/4, 1/(2*Sqrt[2]), 1/4}}}[[j]]*{x[1], x[2], x[3]}[[j]], {j, ss}], ss]^3, \"integralSymmetricProduct\" -> Fold[Coefficient[#1, xx[[#2]], 1] & , 1 + 21*{{6/7, -2/7, -3/7}, {-2/7, 3/7, -6/7}, {-3/7, -6/7, -2/7}} . Sum[{{{1, -Sqrt[2], 1}, {-Sqrt[2], 2, -Sqrt[2]}, {1, -Sqrt[2], 1}}, {{-1, 0, 1}, {0, 0, 0}, {1, 0, -1}}, {{1, Sqrt[2], 1}, {Sqrt[2], 2, Sqrt[2]}, {1, Sqrt[2], 1}}}[[j]]*{x[1], x[2], x[3]}[[j]], {j, ss}], ss]^3, \"exactDenominatorIdentity\" -> False, \"allNumeratorsAlgebraicIntegers\" -> False|>, <|\"k\" -> 3, \"compressedPrincipalMinors\" -> {Fold[Coefficient[#1, xx[[#2]], 1] & , 1 + 3*{{6/7, -2/7, -3/7}, {-2/7, 3/7, -6/7}, {-3/7, -6/7, -2/7}} . Sum[{{{1/4, -1/2*1/Sqrt[2], 1/4}, {-1/2*1/Sqrt[2], 1/2, -1/2*1/Sqrt[2]}, {1/4, -1/2*1/Sqrt[2], 1/4}}, {{1/2, 0, -1/2}, {0, 0, 0}, {-1/2, 0, 1/2}}, {{1/4, 1/(2*Sqrt[2]), 1/4}, {1/(2*Sqrt[2]), 1/2, 1/(2*Sqrt[2])}, {1/4, 1/(2*Sqrt[2]), 1/4}}}[[j]]*{x[1], x[2], x[3]}[[j]], {j, ss}], ss]}, \"theirProduct\" -> Fold[Coefficient[#1, xx[[#2]], 1] & , 1 + 3*{{6/7, -2/7, -3/7}, {-2/7, 3/7, -6/7}, {-3/7, -6/7, -2/7}} . Sum[{{{1/4, -1/2*1/Sqrt[2], 1/4}, {-1/2*1/Sqrt[2], 1/2, -1/2*1/Sqrt[2]}, {1/4, -1/2*1/Sqrt[2], 1/4}}, {{1/2, 0, -1/2}, {0, 0, 0}, {-1/2, 0, 1/2}}, {{1/4, 1/(2*Sqrt[2]), 1/4}, {1/(2*Sqrt[2]), 1/2, 1/(2*Sqrt[2])}, {1/4, 1/(2*Sqrt[2]), 1/4}}}[[j]]*{x[1], x[2], x[3]}[[j]], {j, ss}], ss], \"integralSymmetricProduct\" -> Fold[Coefficient[#1, xx[[#2]], 1] & , 1 + 21*{{6/7, -2/7, -3/7}, {-2/7, 3/7, -6/7}, {-3/7, -6/7, -2/7}} . Sum[{{{1, -Sqrt[2], 1}, {-Sqrt[2], 2, -Sqrt[2]}, {1, -Sqrt[2], 1}}, {{-1, 0, 1}, {0, 0, 0}, {1, 0, -1}}, {{1, Sqrt[2], 1}, {Sqrt[2], 2, Sqrt[2]}, {1, Sqrt[2], 1}}}[[j]]*{x[1], x[2], x[3]}[[j]], {j, ss}], ss], \"exactDenominatorIdentity\" -> False, \"allNumeratorsAlgebraicIntegers\" -> False|>}, \"negativeMissingNonzeroHypothesis\" -> True|>"
    }
  ],
  "structuredContent": null,
  "isError": false
}
```

#### VIIIi.10.3. minor_corrected

Отвергнутый вход: скаляр ошибочно записан через Dot; нулевые коэффициенты противоречат независимому ненулевому следу.

```wolfram
ClearAll[z,y,xx,bvals,pp,pders,proj,raw,extract,dc,fc,pr,zz,hh];
dim=3;bm={{0,1,0},{1,0,1},{0,1,0}};
bvals={-Sqrt[2],0,Sqrt[2]};pp=Expand[Det[z IdentityMatrix[dim]-bm]];
pders=(D[pp,z]/.z->#)& /@ bvals;
proj=Table[FullSimplify[Apply[Dot,Prepend[Table[If[j==l,Nothing,(bm-bvals[[l]]IdentityMatrix[dim])/(bvals[[j]]-bvals[[l]])],{l,dim}],IdentityMatrix[dim]]]],{j,dim}];
wv={1,2,3};mm=IdentityMatrix[dim]-Outer[Times,wv,wv]/7;cc=7;
xx=Array[x,dim];raw=Table[FullSimplify[pders[[j]]proj[[j]]],{j,dim}];
extract[ss_,arr_,mult_]:=Module[{pol,sel},
 sel=Total[Table[xx[[j]]arr[[j]],{j,ss}]];
 pol=Expand[Det[IdentityMatrix[dim]+mult.mm.sel]];
 FullSimplify[Fold[Coefficient[#1,xx[[#2]],1]&,pol,ss]]
];
records=Table[
 sub=Subsets[Range[dim],{kk}];hh=Binomial[dim,kk];rr=Binomial[dim-1,kk-1];
 dc=Table[extract[ss,proj,1],{ss,sub}];
 fc=Table[extract[ss,raw,cc],{ss,sub}];
 pr=FullSimplify[Times@@dc];zz=FullSimplify[Times@@fc];
 <|"k"->kk,"compressedPrincipalMinors"->dc,"theirProduct"->pr,
 "integralSymmetricProduct"->zz,
 "exactDenominatorIdentity"->TrueQ[FullSimplify[zz==cc^(kk hh)(Times@@pders)^rr pr]],
 "allNumeratorsAlgebraicIntegers"->And@@Table[With[{mp=MinimalPolynomial[v,y]},And[Coefficient[mp,y,Exponent[mp,y]]==1,And@@(IntegerQ /@ CoefficientList[mp,y])]],{v,fc}]|>,
 {kk,1,dim}];
zeroMM=RotateLeft[IdentityMatrix[3]];
negative=Product[zeroMM[[j,j]],{j,3}];
<|"kernelVersion"->$Version,"projectorResolution"->TrueQ[FullSimplify[Total[proj]==IdentityMatrix[3]]],
"simpleDiscriminant"->Discriminant[pp,z],"unitaryM"->TrueQ[mm.Transpose[mm]==IdentityMatrix[3]],
"records"->records,"negativeMissingNonzeroHypothesis"->TrueQ[negative==0]|>
```

Сохранённый ответ:

```json
{
  "content": [
    {
      "type": "text",
      "text": "Out[1]= <|\"kernelVersion\" -> \"15.0.1 for Linux x86 (64-bit) (July 2, 2026)\", \"projectorResolution\" -> True, \"simpleDiscriminant\" -> 32, \"unitaryM\" -> True, \"records\" -> {<|\"k\" -> 1, \"compressedPrincipalMinors\" -> {0, 0, 0}, \"theirProduct\" -> 0, \"integralSymmetricProduct\" -> 0, \"exactDenominatorIdentity\" -> True, \"allNumeratorsAlgebraicIntegers\" -> True|>, <|\"k\" -> 2, \"compressedPrincipalMinors\" -> {0, 0, 0}, \"theirProduct\" -> 0, \"integralSymmetricProduct\" -> 0, \"exactDenominatorIdentity\" -> True, \"allNumeratorsAlgebraicIntegers\" -> True|>, <|\"k\" -> 3, \"compressedPrincipalMinors\" -> {0}, \"theirProduct\" -> 0, \"integralSymmetricProduct\" -> 0, \"exactDenominatorIdentity\" -> True, \"allNumeratorsAlgebraicIntegers\" -> True|>}, \"negativeMissingNonzeroHypothesis\" -> True|>"
    }
  ],
  "structuredContent": null,
  "isError": false
}
```

#### VIIIi.10.4. minor_hardened

Исправленные значения; заменён итоговой проверкой в независимом собственном базисе.

```wolfram
ClearAll[z,y,xx,bvals,pp,pders,proj,raw,extract,dc,fc,pr,zz,hh];
dim=3;bm={{0,1,0},{1,0,1},{0,1,0}};
bvals={-Sqrt[2],0,Sqrt[2]};pp=Expand[Det[z IdentityMatrix[dim]-bm]];
pders=(D[pp,z]/.z->#)& /@ bvals;
proj=Table[FullSimplify[Apply[Dot,Prepend[Table[If[j==l,Nothing,(bm-bvals[[l]]IdentityMatrix[dim])/(bvals[[j]]-bvals[[l]])],{l,dim}],IdentityMatrix[dim]]]],{j,dim}];
wv={1,2,3};mm=IdentityMatrix[dim]-Outer[Times,wv,wv]/7;cc=7;
xx=Array[x,dim];raw=Table[FullSimplify[pders[[j]]proj[[j]]],{j,dim}];
extract[ss_,arr_,mult_]:=Module[{pol,sel},
 sel=Total[Table[xx[[j]]arr[[j]],{j,ss}]];
 pol=Expand[Det[IdentityMatrix[dim]+mult*(mm.sel)]];
 FullSimplify[Fold[Coefficient[#1,xx[[#2]],1]&,pol,ss]]
];
records=Table[
 sub=Subsets[Range[dim],{kk}];hh=Binomial[dim,kk];rr=Binomial[dim-1,kk-1];
 dc=Table[extract[ss,proj,1],{ss,sub}];
 fc=Table[extract[ss,raw,cc],{ss,sub}];
 pr=FullSimplify[Times@@dc];zz=FullSimplify[Times@@fc];
 <|"k"->kk,"compressedPrincipalMinors"->dc,"theirProduct"->pr,
 "integralSymmetricProduct"->zz,
 "exactDenominatorIdentity"->TrueQ[FullSimplify[zz==cc^(kk hh)(Times@@pders)^rr pr]],
 "allNumeratorsAlgebraicIntegers"->And@@Table[With[{mp=MinimalPolynomial[v,y]},And[Coefficient[mp,y,Exponent[mp,y]]==1,And@@(IntegerQ /@ CoefficientList[mp,y])]],{v,fc}]|>,
 {kk,1,dim}];
zeroMM=RotateLeft[IdentityMatrix[3]];
negative=Product[zeroMM[[j,j]],{j,3}];
<|"kernelVersion"->$Version,"projectorResolution"->TrueQ[FullSimplify[Total[proj]==IdentityMatrix[3]]],
"simpleDiscriminant"->Discriminant[pp,z],"unitaryM"->TrueQ[mm.Transpose[mm]==IdentityMatrix[3]],
"records"->records,"firstPolynomial"->FullSimplify[Det[IdentityMatrix[3]+xx[[1]]*(mm.proj[[1]])]],"firstTrace"->FullSimplify[Tr[mm.proj[[1]]]],"negativeMissingNonzeroHypothesis"->TrueQ[negative==0]|>
```

Сохранённый ответ:

```json
{
  "content": [
    {
      "type": "text",
      "text": "Out[1]= <|\"kernelVersion\" -> \"15.0.1 for Linux x86 (64-bit) (July 2, 2026)\", \"projectorResolution\" -> True, \"simpleDiscriminant\" -> 32, \"unitaryM\" -> True, \"records\" -> {<|\"k\" -> 1, \"compressedPrincipalMinors\" -> {(1 + 4*Sqrt[2])/7, 5/7, (1 - 4*Sqrt[2])/7}, \"theirProduct\" -> -155/343, \"integralSymmetricProduct\" -> 4960, \"exactDenominatorIdentity\" -> True, \"allNumeratorsAlgebraicIntegers\" -> True|>, <|\"k\" -> 2, \"compressedPrincipalMinors\" -> {(-1 + 4*Sqrt[2])/7, -5/7, (-1 - 4*Sqrt[2])/7}, \"theirProduct\" -> 155/343, \"integralSymmetricProduct\" -> 54440960, \"exactDenominatorIdentity\" -> True, \"allNumeratorsAlgebraicIntegers\" -> True|>, <|\"k\" -> 3, \"compressedPrincipalMinors\" -> {-1}, \"theirProduct\" -> -1, \"integralSymmetricProduct\" -> 10976, \"exactDenominatorIdentity\" -> True, \"allNumeratorsAlgebraicIntegers\" -> True|>}, \"firstPolynomial\" -> (7 + x[1] + 4*Sqrt[2]*x[1])/7, \"firstTrace\" -> (1 + 4*Sqrt[2])/7, \"negativeMissingNonzeroHypothesis\" -> True|>"
    }
  ],
  "structuredContent": null,
  "isError": false
}
```

#### VIIIi.10.5. minor_final

Проверки дали True, но сравнение вызвало внутренние сообщения о точности; заменён строго алгебраическим сравнением.

```wolfram
ClearAll[z,y,xx,bvals,pp,pders,proj,raw,extract,dc,fc,pr,zz,hh];
dim=3;bm={{0,1,0},{1,0,1},{0,1,0}};
bvals={-Sqrt[2],0,Sqrt[2]};pp=Expand[Det[z IdentityMatrix[dim]-bm]];
pders=(D[pp,z]/.z->#)& /@ bvals;
proj=Table[FullSimplify[Apply[Dot,Prepend[Table[If[j==l,Nothing,(bm-bvals[[l]]IdentityMatrix[dim])/(bvals[[j]]-bvals[[l]])],{l,dim}],IdentityMatrix[dim]]]],{j,dim}];
wv={1,2,3};mm=IdentityMatrix[dim]-Outer[Times,wv,wv]/7;cc=7;
qq=Transpose[{{1,-Sqrt[2],1}/2,{1,0,-1}/Sqrt[2],{1,Sqrt[2],1}/2}];
qmm=FullSimplify[Transpose[qq].mm.qq];
xx=Array[x,dim];raw=Table[FullSimplify[pders[[j]]proj[[j]]],{j,dim}];
extract[ss_,arr_,mult_]:=Module[{pol,sel},
 sel=Total[Table[xx[[j]]arr[[j]],{j,ss}]];
 pol=Expand[Det[IdentityMatrix[dim]+mult*(mm.sel)]];
 FullSimplify[Fold[Coefficient[#1,xx[[#2]],1]&,pol,ss]]
];
records=Table[
 sub=Subsets[Range[dim],{kk}];hh=Binomial[dim,kk];rr=Binomial[dim-1,kk-1];
 dc=Table[extract[ss,proj,1],{ss,sub}];
 fc=Table[extract[ss,raw,cc],{ss,sub}];
 pr=FullSimplify[Times@@dc];zz=FullSimplify[Times@@fc];
 <|"k"->kk,"compressedPrincipalMinors"->dc,"theirProduct"->pr,
 "integralSymmetricProduct"->zz,
 "exactDenominatorIdentity"->TrueQ[FullSimplify[zz==cc^(kk hh)(Times@@pders)^rr pr]],
 "independentEigenbasisCheck"->TrueQ[FullSimplify[dc==Table[Det[qmm[[ss,ss]]],{ss,sub}]]],
 "nonzeroAllComputedMinors"->And@@(TrueQ[FullSimplify[#!=0]]& /@dc),
 "allNumeratorsAlgebraicIntegers"->And@@Table[With[{mp=MinimalPolynomial[v,y]},And[Coefficient[mp,y,Exponent[mp,y]]==1,And@@(IntegerQ /@ CoefficientList[mp,y])]],{v,fc}]|>,
 {kk,1,dim}];
zeroMM=RotateLeft[IdentityMatrix[3]];
negative=Product[zeroMM[[j,j]],{j,3}];
<|"kernelVersion"->$Version,"eigenbasisOrthonormal"->TrueQ[FullSimplify[Transpose[qq].qq==IdentityMatrix[3]]],
"eigenbasisDiagonalization"->TrueQ[FullSimplify[Transpose[qq].bm.qq==DiagonalMatrix[bvals]]],
"projectorResolution"->TrueQ[FullSimplify[Total[proj]==IdentityMatrix[3]]],
"simpleDiscriminant"->Discriminant[pp,z],"unitaryM"->TrueQ[mm.Transpose[mm]==IdentityMatrix[3]],
"records"->records,"firstPolynomial"->FullSimplify[Det[IdentityMatrix[3]+xx[[1]]*(mm.proj[[1]])]],"firstTrace"->FullSimplify[Tr[mm.proj[[1]]]],"negativeMissingNonzeroHypothesis"->TrueQ[negative==0]|>
```

Сохранённый ответ:

```json
{
  "content": [
    {
      "type": "text",
      "text": "N::meprec: Internal precision limit $MaxExtraPrecision = 50. reached while evaluating 1/7 - (4*Sqrt[2])/7 + (-1 + 4*Sqrt[2])/7.\nN::meprec: Internal precision limit $MaxExtraPrecision = 50. reached while evaluating 1/7 + (4*Sqrt[2])/7 + (-1 - 4*Sqrt[2])/7.\nGeneral::messages: Messages were generated which may indicate errors.\n\nOut[1]= <|\"kernelVersion\" -> \"15.0.1 for Linux x86 (64-bit) (July 2, 2026)\", \"eigenbasisOrthonormal\" -> True, \"eigenbasisDiagonalization\" -> True, \"projectorResolution\" -> True, \"simpleDiscriminant\" -> 32, \"unitaryM\" -> True, \"records\" -> {<|\"k\" -> 1, \"compressedPrincipalMinors\" -> {(1 + 4*Sqrt[2])/7, 5/7, (1 - 4*Sqrt[2])/7}, \"theirProduct\" -> -155/343, \"integralSymmetricProduct\" -> 4960, \"exactDenominatorIdentity\" -> True, \"independentEigenbasisCheck\" -> True, \"nonzeroAllComputedMinors\" -> True, \"allNumeratorsAlgebraicIntegers\" -> True|>, <|\"k\" -> 2, \"compressedPrincipalMinors\" -> {(-1 + 4*Sqrt[2])/7, -5/7, (-1 - 4*Sqrt[2])/7}, \"theirProduct\" -> 155/343, \"integralSymmetricProduct\" -> 54440960, \"exactDenominatorIdentity\" -> True, \"independentEigenbasisCheck\" -> True, \"nonzeroAllComputedMinors\" -> True, \"allNumeratorsAlgebraicIntegers\" -> True|>, <|\"k\" -> 3, \"compressedPrincipalMinors\" -> {-1}, \"theirProduct\" -> -1, \"integralSymmetricProduct\" -> 10976, \"exactDenominatorIdentity\" -> True, \"independentEigenbasisCheck\" -> True, \"nonzeroAllComputedMinors\" -> True, \"allNumeratorsAlgebraicIntegers\" -> True|>}, \"firstPolynomial\" -> (7 + x[1] + 4*Sqrt[2]*x[1])/7, \"firstTrace\" -> (1 + 4*Sqrt[2])/7, \"negativeMissingNonzeroHypothesis\" -> True|>"
    }
  ],
  "structuredContent": null,
  "isError": false
}
```

#### VIIIi.10.6. minor_exact

Точная конечная проверка пройдена; RootReduce и независимый собственный базис, без диагностических сообщений.

```wolfram
ClearAll[z,y,xx,bvals,pp,pders,proj,raw,extract,dc,fc,pr,zz,hh];
dim=3;bm={{0,1,0},{1,0,1},{0,1,0}};
bvals={-Sqrt[2],0,Sqrt[2]};pp=Expand[Det[z IdentityMatrix[dim]-bm]];
pders=(D[pp,z]/.z->#)& /@ bvals;
proj=Table[FullSimplify[Apply[Dot,Prepend[Table[If[j==l,Nothing,(bm-bvals[[l]]IdentityMatrix[dim])/(bvals[[j]]-bvals[[l]])],{l,dim}],IdentityMatrix[dim]]]],{j,dim}];
wv={1,2,3};mm=IdentityMatrix[dim]-Outer[Times,wv,wv]/7;cc=7;
qq=Transpose[{{1,-Sqrt[2],1}/2,{1,0,-1}/Sqrt[2],{1,Sqrt[2],1}/2}];
qmm=FullSimplify[Transpose[qq].mm.qq];
xx=Array[x,dim];raw=Table[FullSimplify[pders[[j]]proj[[j]]],{j,dim}];
extract[ss_,arr_,mult_]:=Module[{pol,sel},
 sel=Total[Table[xx[[j]]arr[[j]],{j,ss}]];
 pol=Expand[Det[IdentityMatrix[dim]+mult*(mm.sel)]];
 FullSimplify[Fold[Coefficient[#1,xx[[#2]],1]&,pol,ss]]
];
records=Table[
 sub=Subsets[Range[dim],{kk}];hh=Binomial[dim,kk];rr=Binomial[dim-1,kk-1];
 dc=Table[extract[ss,proj,1],{ss,sub}];
 fc=Table[extract[ss,raw,cc],{ss,sub}];
 pr=FullSimplify[Times@@dc];zz=FullSimplify[Times@@fc];
 <|"k"->kk,"compressedPrincipalMinors"->dc,"theirProduct"->pr,
 "integralSymmetricProduct"->zz,
 "exactDenominatorIdentity"->TrueQ[FullSimplify[zz==cc^(kk hh)(Times@@pders)^rr pr]],
 "independentEigenbasisCheck"->And@@(SameQ[RootReduce[#],0]& /@(dc-Table[Det[qmm[[ss,ss]]],{ss,sub}])),
 "nonzeroAllComputedMinors"->And@@(UnsameQ[RootReduce[#],0]& /@dc),
 "allNumeratorsAlgebraicIntegers"->And@@Table[With[{mp=MinimalPolynomial[v,y]},And[Coefficient[mp,y,Exponent[mp,y]]==1,And@@(IntegerQ /@ CoefficientList[mp,y])]],{v,fc}]|>,
 {kk,1,dim}];
zeroMM=RotateLeft[IdentityMatrix[3]];
negative=Product[zeroMM[[j,j]],{j,3}];
<|"kernelVersion"->$Version,"eigenbasisOrthonormal"->TrueQ[FullSimplify[Transpose[qq].qq==IdentityMatrix[3]]],
"eigenbasisDiagonalization"->TrueQ[FullSimplify[Transpose[qq].bm.qq==DiagonalMatrix[bvals]]],
"projectorResolution"->TrueQ[FullSimplify[Total[proj]==IdentityMatrix[3]]],
"simpleDiscriminant"->Discriminant[pp,z],"unitaryM"->TrueQ[mm.Transpose[mm]==IdentityMatrix[3]],
"records"->records,"firstPolynomial"->FullSimplify[Det[IdentityMatrix[3]+xx[[1]]*(mm.proj[[1]])]],"firstTrace"->FullSimplify[Tr[mm.proj[[1]]]],"negativeMissingNonzeroHypothesis"->TrueQ[negative==0]|>
```

Сохранённый ответ:

```json
{
  "content": [
    {
      "type": "text",
      "text": "Out[1]= <|\"kernelVersion\" -> \"15.0.1 for Linux x86 (64-bit) (July 2, 2026)\", \"eigenbasisOrthonormal\" -> True, \"eigenbasisDiagonalization\" -> True, \"projectorResolution\" -> True, \"simpleDiscriminant\" -> 32, \"unitaryM\" -> True, \"records\" -> {<|\"k\" -> 1, \"compressedPrincipalMinors\" -> {(1 + 4*Sqrt[2])/7, 5/7, (1 - 4*Sqrt[2])/7}, \"theirProduct\" -> -155/343, \"integralSymmetricProduct\" -> 4960, \"exactDenominatorIdentity\" -> True, \"independentEigenbasisCheck\" -> True, \"nonzeroAllComputedMinors\" -> True, \"allNumeratorsAlgebraicIntegers\" -> True|>, <|\"k\" -> 2, \"compressedPrincipalMinors\" -> {(-1 + 4*Sqrt[2])/7, -5/7, (-1 - 4*Sqrt[2])/7}, \"theirProduct\" -> 155/343, \"integralSymmetricProduct\" -> 54440960, \"exactDenominatorIdentity\" -> True, \"independentEigenbasisCheck\" -> True, \"nonzeroAllComputedMinors\" -> True, \"allNumeratorsAlgebraicIntegers\" -> True|>, <|\"k\" -> 3, \"compressedPrincipalMinors\" -> {-1}, \"theirProduct\" -> -1, \"integralSymmetricProduct\" -> 10976, \"exactDenominatorIdentity\" -> True, \"independentEigenbasisCheck\" -> True, \"nonzeroAllComputedMinors\" -> True, \"allNumeratorsAlgebraicIntegers\" -> True|>}, \"firstPolynomial\" -> (7 + x[1] + 4*Sqrt[2]*x[1])/7, \"firstTrace\" -> (1 + 4*Sqrt[2])/7, \"negativeMissingNonzeroHypothesis\" -> True|>"
    }
  ],
  "structuredContent": null,
  "isError": false
}
```

### VIIIi.11. Отдельный проход самопроверки

Проверяемое утверждение — AQ1–AQ6 в их записанной области, с зависимостью AQ4–AQ5 от AP4. Основной Sine₂-вывод в проверяемую теорему не включён. Первичный вердикт для AQ1–AQ6: **proved as written** по выполненному проходу самопроверки. Независимой проверки нет.

| Обязательство | Проверка | Итог |
|---|---|---|
| QA-01 (AQ1) | исходное T-правило и множитель 200; удаляются именно нулевые рёбра | Пройдено |
| QA-02 (AQ1) | кратность отображения z -> z^7 для d=1 и d=7 | Пройдено |
| QA-03 (AQ1) | знаки, произведение корней, нечётность N и пустой случай N=7 | Пройдено |
| QA-04 (AQ2) | концевой кофактор, его знак и крайний общий случай L=2 | Пройдено |
| QA-05 (AQ2) | присоединённая матрица в простой точке и нормировка собственных векторов | Пройдено |
| QA-06 (AQ2) | константы R=59/50, D0=59/25, 800 и 1888 | Пройдено |
| QA-07 (AQ2) | семь цепочек: число чужих связей и предел внутриблочного вывода | Пройдено |
| QA-08 (AQ3) | целость коэффициентов 4000A и элементов sqrt(N)M из исходных формул | Пройдено |
| QA-09 (AQ3) | вложения K; комплексное сопряжение коммутирует на образующих | Пройдено |
| QA-10 (AQ3) | эрмитовость, норма и унитарность всех сопряжённых матриц | Пройдено |
| QA-11 (AQ4) | спектральные проекторы выражены алгебраически, без сопряжения собственных векторов | Пройдено |
| QA-12 (AQ4) | коэффициентная формула для каждого d_S и степень каждого знаменателя | Пройдено |
| QA-13 (AQ4) | целость F_S и симметричность произведения по всем S | Пройдено |
| QA-14 (AQ4) | целое число r_k=k binom(N,k)/N и отсутствие оценки в поле степени N! | Пройдено |
| QA-15 (AQ4) | ненулевая целая норма: обязательность AP4, а не одна целость | Пройдено |
| QA-16 (AQ4) | вложения поля разложения; каждый сопряжённый минор есть сжатие унитарной матрицы | Пройдено |
| QA-17 (AQ4) | оценки дискриминанта, произведения, отдельного множителя и константы 42 | Пройдено |
| QA-18 (AQ4) | кванторы по k,S,N и пустой минор; случай k=N | Пройдено |
| QA-19 (AQ5) | потеря не меньше g при замене верхнего подмножества уровней | Пройдено |
| QA-20 (AQ5) | главный коэффициент и сумма остальных на двух окружностях у каждого уровня | Пройдено |
| QA-21 (AQ5) | счёт корней, простота и раздельность модулей без предельного обмена | Пройдено |
| QA-22 (AQ5) | все численные константы и неравенство для каждого N>=3 | Пройдено |
| QA-23 (AQ5) | знак t=-is/N и вспомогательный, не физический характер этого параметра | Пройдено |
| QA-24 (AQ6) | фиксированное рациональное tau, E1, хвост ряда и общий знаменатель | Пройдено |
| QA-25 (TRANSFER) | достаточный порог доминирующего монома не отождествлён с необходимым временем | Пройдено |
| QA-26 (COMPUTATION) | отвергнуты ошибочные нули; итог проверен независимым собственным базисом | Пройдено |
| QA-27 (GOAL) | расстояния между фазами самого U_N(tau) и Heisenberg-сумма | Не доказано этим результатом |
| QA-28 (SEVEN) | полная простота при 7|N и смешанные блоковые миноры | Не доказано этим результатом |

Итог исходной цели этим вердиктом не меняется. В U-Q1 и U-Q3 остаются точные незакрытые утверждения. Алгебраические входы, области конечных вычислений и ошибочные промежуточные входы не смешаны с доказательствами по всем N.


## VIIIj. Дисперсия, собственные векторы и Ward-тождества памяти

### VIIIj.1. Точные новые утверждения

Во всём разделе $U_N=e^{i\tau NA_N}M_N$, $\tau=10^{-80}$, без изменения определения. Логарифмы натуральные. Положим
$$
\Gamma=(64/3)^{8/9},\qquad
 L_N=1+\left\lfloor\frac{\log N}{8\log(64/3)}\right\rfloor .
$$
**LD2.** Для каждого нечётного $N\ge3$, каждого целого $m\ge1$ и всех координат
$$
\boxed{\quad |(U_N^m)_{xy}|^2
           \le \min\{1,\ 10^{21}\Gamma^m N^{-2/9}\}.\quad}          \tag{VIIIj.1.1}
$$
Утверждение равномерно по всем записанным параметрам. Малость правой части утверждается только в соответствующем диапазоне $m$; при $m\asymp N$ эта оценка тривиальна.

**LD3.** Для каждого нормированного собственного вектора $\psi$ исходного $U_N$, включая любой выбор внутри вырожденного собственного подпространства,
$$
\boxed{\quad
 \max_x|\psi(x)|^2
  \le \mu_N:=
     \min\{1,\ L_N^{-1}+10^{11}N^{-1/18}\}.
 \quad}                                                          \tag{VIIIj.1.2}
$$
В частности, для всех нечётных $N\ge e^{1000}$
$$
\max_x|\psi(x)|^2\le\frac{33}{\log N},
       \qquad \sum_x|\psi(x)|^4\le\frac{33}{\log N}.                 \tag{VIIIj.1.3}
$$
В (VIIIj.1.1)–(VIIIj.1.3) нет ограничения $7\nmid N$.

Используем HS-норму $\|X\|_{\mathrm{HS}}^2=\operatorname{Tr}(X^*X)$. Обозначим через $E$ ортогональную проекцию на диагональные матрицы в этой норме и через
$$
\mathscr T_N(X)=U_NXU_N^*,\qquad
        D_N=(I-E)\mathscr T_N(I-E)|_{\mathrm{off}}
$$
внедиагональную когерентную память. Она действует на пространстве размерности $n=N(N-1)$. Сингулярные числа ниже нумеруются **по возрастанию**.

**LD4.** Для каждого нечётного $N\ge e^{1000}$
$$
\boxed{\quad
 s_{(N-1)/2}^{\uparrow}(I-D_N)\le\frac{11}{\sqrt{\log N}}.
 \quad}                                                          \tag{VIIIj.1.4}
$$
Значит, не меньше $(N-1)/2$ независимых сингулярных направлений имеют такой малый остаток. Если $I-D_N$ обратима, то
$$
\boxed{\quad
          \|(I-D_N)^{-1}\|
                    \ge\sqrt{\frac{\log N-33}{33}}.
          \quad}                                                 \tag{VIIIj.1.5}
$$
Если она необратима, существует точная невидимая неподвижная мода. Малые сингулярные числа не отождествляются с расстояниями собственных значений $D_N$ до 1.

**LD5.** Для любой унитарной матрицы $U$ размера $N$, любого её ортонормированного собственного базиса $V=(v_1,\ldots,v_N)$, $\lambda_1,\ldots,\lambda_N$ с кратностями, положим
$\mathsf H_{xj}=|v_j(x)|^2$. Для той же памяти $D$
$$
\boxed{\quad
   \det(I-D)
     =|\det\mathsf H|^2
          \prod_{j<k}|\lambda_j-\lambda_k|^2 .
 \quad}                                                          \tag{VIIIj.1.6}
$$
Таким образом, в одной точной формуле встречаются собственные фазы, собственные векторы и когерентная память. Она доказывается ниже, а не принимается как внешняя формула.

LD6 проверяет попытку получить Sine₂ из этих структурных результатов: уже имеющаяся другая семья SC3 усиливается так, чтобы она одновременно имела все трансцендентные попарные отношения, сильную делокализацию и регулярные тождества LD5, сохраняя решётчатый локальный предел. Это отрицательный тест общего механизма, не опровержение исходной семьи.

### VIIIj.2. LD1: положительная локализация, классическое покрытие и все диагональные alias-члены

#### VIIIj.2.1. Используемый внутренний Egorov-вход

В доказанной H3 исходный Weyl-символ есть
$$
g(q,p)=d(q)+\frac{r(q+1/2)}{100}\cos(2\pi p-\alpha_0),\qquad
 F=S\circ\Phi_\tau,\quad S=\begin{pmatrix}3&4\\2&3\end{pmatrix}.
$$
Здесь $\Phi_\tau$ — поток поля $(g_p,-g_q)/(2\pi)$. Полусдвиг сохранён. Для всех целых меток $v$, всех нечётных $N$, всех $m\ge1$
$$
\|U_N^mW_N(v)U_N^{-m}
      -\operatorname{Op}_N(E_v\circ F^m)\|
       \le \frac{10^{20}\tau}{N^2}(1+|v|_1)^8\,16^{8m},            \tag{VIIIj.2.1}
$$
$$
H_3(E_v\circ F^m)
       :=\sum_b|b|_1^3|(E_v\circ F^m)_b|
       \le10^{15}(1+|v|_1)^8\,16^{8m}.                            \tag{VIIIj.2.2}
$$
H3 доказывает эти оценки коммутатором Weyl и интегральным остатком Дюамеля, включая все оборачивания меток. Мы применяем их к конечному Fourier-полиному, поэтому новых перестановок бесконечных рядов нет.

По H3 производная $F$ всюду имеет покомпонентную нижнюю границу
$$
DF\ge\begin{pmatrix}5/2&7/2\\3/2&5/2\end{pmatrix}
                                      \ge\frac34 S.              \tag{VIIIj.2.3}
$$
Все матрицы здесь с положительными элементами. В H3 также построен подъём $F(z+\ell)=F(z)+S\ell$.

#### VIIIj.2.2. Одномерное классическое покрытие

Пусть $Q_m(q,p)=(F^m(q,p))_1$ на подъёме, $\beta_m=(S^m)_{12}>0$. Перемножение положительных матриц в (VIIIj.2.3) даёт
$$
\partial_p Q_m(q,p)\ge(3/4)^m\beta_m,\qquad
                Q_m(q,p+1)=Q_m(q,p)+\beta_m.                      \tag{VIIIj.2.4}
$$
Неравенство произведений следует индукцией: умножение неотрицательных матриц сохраняет покомпонентный порядок. Оно применимо и когда матрицы вычислены в разных точках орбиты.

Для любого неотрицательного периодического $h$ и любого $s\in\mathbb R$, замена переменной $u=Q_m(q,p)$, монотонная по (VIIIj.2.4), даёт
$$
\int_0^1h(Q_m(q,p)-s)\,dp
     \le (4/3)^m\int_0^1h(u)\,du.                                 \tag{VIIIj.2.5}
$$
Действительно, длина нового интервала ровно целое $\beta_m$, поэтому интеграл периодического $h$ по нему равен $\beta_m\int_0^1h$. Множитель $\beta_m$ сокращается с нижней оценкой производной. Оценка равномерна по $q,s$, всем $m\ge1$.

#### VIIIj.2.3. Положительный оператор локализации

Для целого $L\ge1$
$$
h_L(t)=\frac1{L^2}\left|\sum_{j=0}^{L-1}e^{2\pi ijt}\right|^2
       =\sum_{|k|<L}c_{k,L}e^{2\pi ikt},\quad
 c_{k,L}=\frac{L-|k|}{L^2}.
$$
Точно
$$
h_L\ge0,\quad h_L(0)=1,\quad \int_0^1h_L=L^{-1},\quad
                          \sum_kc_{k,L}=1.                       \tag{VIIIj.2.6}
$$
Матрица $\operatorname{Op}_N(h_L(q-s))$ диагональна, с элементами $h_L(x/N-s)$. При $s=y/N$ она не меньше проектора $|e_y\rangle\langle e_y|$ в порядке самосопряжённых матриц. Поэтому
$$
|(U_N^m)_{xy}|^2
  \le \langle e_x,U_N^m
      \operatorname{Op}_N(h_L(q-y/N))U_N^{-m}e_x\rangle.             \tag{VIIIj.2.7}
$$
Этот шаг использует положительность исходного локализатора, не положительность квантования произвольного гладкого символа.

Суммируя (VIIIj.2.1) с коэффициентами $c_{k,L}e^{-2\pi iky/N}$, получаем операторную ошибку не больше
$$
\frac{10^{20}\tau}{N^2}L^8 16^{8m}.                 \tag{VIIIj.2.8}
$$
Использовано $1+|k|\le L$ для всех присутствующих меток и (VIIIj.2.6).

#### VIIIj.2.4. Диагональный элемент квантованного символа

Для гладкого $a(q,p)=\sum_{k,l}a_{kl}E_{(k,l)}$, буквально из $W_N(k,l)=(-1)^{kl}T_N(l,k)$ при нечётном $N$
$$
\langle e_x,W_N(k,l)e_x\rangle
   =\begin{cases}
       (-1)^{kr}e^{2\pi ikx/N},&l=Nr,\quad r\in\mathbb Z,\\
       0,&N\nmid l.
     \end{cases}                                                 \tag{VIIIj.2.9}
$$
При $l=Nr$ фаза $e_N(k\bar{2}\,l)$ равна 1, а $(-1)^{kNr}=(-1)^{kr}$. Следовательно,
$$
\langle e_x,\operatorname{Op}_N(a)e_x\rangle
          =\int_0^1a(x/N,p)\,dp+\mathcal A_x(a),
 \quad |\mathcal A_x(a)|\le N^{-3}H_3(a).                           \tag{VIIIj.2.10}
$$
Здесь $\mathcal A_x$ содержит **все** $r\ne0$. Сумма их модулей не больше $\sum_{|l|\ge N,k}|a_{kl}|\le N^{-3}H_3(a)$. Fourier-метки по $q$ не отсекаются; их сумма в главном члене — ровно значение интеграла при $q=x/N$.

Для $a=h_L(Q_m-y/N)$, из (VIIIj.2.2), (VIIIj.2.6)
$$
H_3(a)\le10^{15}L^8 16^{8m}.
$$
Подставляем (VIIIj.2.5), (VIIIj.2.8), (VIIIj.2.10) в (VIIIj.2.7):
$$
\boxed{\quad
 |(U_N^m)_{xy}|^2
 \le\frac{(4/3)^m}{L}
   +\left(\frac{10^{20}\tau}{N^2}
                    +\frac{10^{15}}{N^3}\right)L^8 16^{8m}.
 \quad}                                                          \tag{VIIIj.2.11}
$$
Она верна для каждого целого $L\ge1$, каждого $m\ge1$, каждого нечётного $N\ge3$, всех $x,y$. Замены суммы интегралом без alias-остатка здесь нет. LD1 доказана.

### VIIIj.3. LD2: оптимизация с одновременным контролем времени

Положим
$$
L_* =N^{2/9}(4/3)^{m/9}16^{-8m/9}.
$$
Две величины точно совпадают:
$$
\frac{(4/3)^m}{L_*}
     =N^{-2/9}\Gamma^m,\qquad
              N^{-2}16^{8m}L_*^8=N^{-2/9}\Gamma^m.                 \tag{VIIIj.3.1}
$$
Если $L_*\ge2$, берём $L=\lfloor L_*\rfloor$. Тогда $L\ge L_*/2$, $L^8\le L_*^8$. При исходном $\tau$ и $N\ge3$,
$$
\tau+10^{-5}/N<1.
$$
Поэтому (VIIIj.2.11)–(VIIIj.3.1) дают
$$
|(U_N^m)_{xy}|^2
       \le(2+10^{20})N^{-2/9}\Gamma^m
       \le10^{21}N^{-2/9}\Gamma^m.
$$
Если $L_*<2$, то $N^{-2/9}\Gamma^m=(4/3)^m/L_*>1/2$, и та же правая часть больше 1; достаточно унитарной оценки $|(U_N^m)_{xy}|^2\le1$. Это доказывает (VIIIj.1.1) по всем $m$, без неявного предположения о размере оптимального окна.

При
$$
1\le m\le \frac{\log N}{8\log(64/3)}
$$
получаем более простой вид
$$
\max_{x,y}|(U_N^m)_{xy}|^2
                              \le10^{21}N^{-1/9},\qquad
             \max_{x,y}|(U_N^m)_{xy}|
                              \le10^{11}N^{-1/18}.                \tag{VIIIj.3.2}
$$
Обратные степени имеют ту же максимальную оценку, поскольку $U_N^{-m}=(U_N^m)^*$. Время 0 в (VIIIj.1.1)–(VIIIj.3.2) не включено.

Это новый контроль **всех матричных элементов степеней**, а не только следа. Его диапазон остаётся логарифмическим. Ни одной оценки малости при $m\asymp N$ из него не заявляется.

### VIIIj.4. LD3: каждый собственный вектор исходной семьи делокализован

Фиксируем координату $x$, положим $L=L_N$ и рассмотрим $L$ единичных векторов
$$
\phi_j=U_N^j e_x,\qquad0\le j<L.
$$
Их Gram-матрица $G$ имеет диагональ 1. По (VIIIj.3.2) все внедиагональные элементы по модулю не больше
$\delta_N=10^{11}N^{-1/18}$. Для $L=1$ внедиагональных элементов нет. Поэтому
$$
\|G\|\le1+(L-1)\delta_N.               \tag{VIIIj.4.1}
$$
Например, (VIIIj.4.1) следует из
$\sum_{i\ne j}|a_i||a_j|\le(L-1)\sum_i|a_i|^2$ в квадратичной форме $G$.

Если $U_N\psi=\lambda\psi$, $\|\psi\|=1$, то
$$
\sum_{j=0}^{L-1}|\langle\phi_j,\psi\rangle|^2
                         =L|\psi(x)|^2.
$$
Ненулевые собственные значения оператора рамки
$\sum_j|\phi_j\rangle\langle\phi_j|$ и Gram-матрицы $G$ совпадают: это два произведения прямоугольной матрицы её столбцов с сопряжённой. Следовательно,
$$
L|\psi(x)|^2\le\|G\|,\qquad
                       |\psi(x)|^2\le L^{-1}+\delta_N.
$$
Вместе с тривиальной верхней границей 1 это (VIIIj.1.2).

Чтобы получить явную простую (VIIIj.1.3), заметим
$$
L_N>\frac{\log N}{8\log(64/3)},\qquad \log(64/3)<4.
$$
Пусть $t=\log N\ge1000$. Функция $t e^{-t/18}$ убывает при $t\ge1000$, а
$10^{11}\cdot1000\,e^{-1000/18}<1$: достаточно $\log10<3$ и $1000/18>42$. Значит, $\delta_N\le1/\log N$. Отсюда
$$
L_N^{-1}+\delta_N\le33/\log N.
$$
Наконец, $\sum_x|\psi(x)|^4\le(\max_x|\psi(x)|^2)\sum_x|\psi(x)|^2$. LD3 доказана.

Доказательство не выбирает собственный базис и не предполагает простоту спектра. Оно действует для каждого вектора любого собственного подпространства, а значит, включает размерности, кратные 7. Оно не является утверждением о Haar-распределении собственных векторов.

### VIIIj.5. LD4: не меньше половины N мягких когерентных направлений

В полном пространстве матриц, в ортогональных HS-координатах «диагональ / внедиагональ», запишем
$$
\mathscr T_N=\begin{pmatrix}P_N&B_N\\C_N&D_N\end{pmatrix}.
$$
На диагональных матрицах нулевого следа верхний блок равен $P_N-J_N$; $D_N$ буквально совпадает с памятью прежних частей. Унитарность сопряжения даёт $\|C_N\|\le1$.

#### VIIIj.5.1. Отдельный собственный проектор

Пусть $P_\psi=|\psi\rangle\langle\psi|$,
$$
X=P_\psi-I/N=x+y,\qquad x=EX,\quad y=(I-E)X.
$$
Точно $\mathscr T_NX=X$, поэтому
$$
(I-D_N)y=C_Nx,\quad
 \|x\|_{\mathrm{HS}}^2=\sum_x|\psi(x)|^4-1/N,\quad
 \|y\|_{\mathrm{HS}}^2=1-\sum_x|\psi(x)|^4.                         \tag{VIIIj.5.1}
$$
Для $N\ge e^{1000}$ вектор $y$ ненулевой по (VIIIj.1.3). Его нормировка и $\|C_N\|\le1$ дают
$$
s_{\min}(I-D_N)
    \le \sqrt{\frac{\sum|\psi|^4-1/N}{1-\sum|\psi|^4}}
    \le\sqrt{\frac{33}{\log N-33}}.                               \tag{VIIIj.5.2}
$$
Если $I-D_N$ обратима, норма обратной равна обратному минимальному сингулярному числу, откуда (VIIIj.1.5). Если числитель первой дроби нулевой, (VIIIj.5.1) непосредственно даёт ненулевой $y$ в ядре $I-D_N$. Это не вывод о собственных значениях из сингулярных чисел.

#### VIIIj.5.2. Одновременно не меньше половины N направлений

Выберем любой ортонормированный собственный базис и его проекторы $P_1,\ldots,P_N$. Пусть
$$
\mathcal R=\left\{\sum_{j=1}^Nh_jP_j:\sum_jh_j=0\right\},\qquad
                              \dim\mathcal R=d=N-1.
$$
Все элементы $\mathcal R$ неподвижны. След квадрата сингулярных чисел ограничения $E|_{\mathcal R}$ точно равен
$$
t_{\mathcal R}
    =\sum_{j=1}^N\|EP_j\|_{\mathrm{HS}}^2-1
    =\sum_{j=1}^N\sum_x|v_j(x)|^4-1
                    \le \frac{33N}{\log N}-1.                    \tag{VIIIj.5.3}
$$
Вычитаемая 1 — вклад нормированного тождественного оператора $I/\sqrt N$, который лежит в диагональном пространстве.

Положим $\eta=99/\log N<1$. Из $N/(N-1)\le3/2$ при $N\ge3$ и (VIIIj.5.3)
$$
t_{\mathcal R}\le d\eta/2.
$$
Не больше $d/2$ собственных значений положительной матрицы
$(E|_{\mathcal R})^*(E|_{\mathcal R})$ могут превышать $\eta$: их сумма равна $t_{\mathcal R}$. Значит, существует подпространство $\mathcal R_0$ размерности не меньше $d/2$, на котором
$$
\|EX\|^2\le\eta\|X\|^2.
$$
Отображение $X\mapsto y=(I-E)X$ на $\mathcal R_0$ инъективно; $\|y\|^2\ge(1-\eta)\|X\|^2$. Для каждого такого $X$, как в (VIIIj.5.1), $(I-D_N)y=C_NEX$. На образе размерности не меньше $d/2$
$$
\|(I-D_N)y\|\le\sqrt{\frac{\eta}{1-\eta}}\,\|y\|.
$$
Вариационное определение сингулярных чисел даёт
$$
s_{d/2}^{\uparrow}(I-D_N)
       \le\sqrt{\frac{99}{\log N-99}}
       \le\frac{11}{\sqrt{\log N}}\quad(\log N\ge1000).
$$
Последнее неравенство эквивалентно $22\log N\ge11979$. При нечётном $N$, $d$ чётно, поэтому индекс $d/2=(N-1)/2$ целый. Это (VIIIj.1.4). LD4 доказана.

Итак, в исходной координатной памяти присутствует растущее число почти неподвижных сингулярных направлений. Их существование получено из реальных собственных проекторов и новой делокализации. Оно не оценивает суммарный след их степеней и не утверждает, что они дают необходимую константу $-\delta_*$.

### VIIIj.6. LD5: точная Ward-формула и спектральный якобиан

Здесь $U$ — любая унитарная матрица, $N\ge2$; все равенства конечномерные. Используем полный диагональный блок $P$, а не только $P-J$:
$$
\operatorname{Ad}_U=\begin{pmatrix}P&B\\C&D\end{pmatrix}.
$$
Определим передаточную матрицу
$$
\mathscr F(z)=P+zB(I-zD)^{-1}C,\qquad |z|<1.        \tag{VIIIj.6.1}
$$
Обратная существует при $|z|<1$, поскольку $D$ — сжатие. Для таких $z$ формула Schur-комплемента даёт
$$
\det(I-z\operatorname{Ad}_U)
             =\det(I-zD)\det(I-z\mathscr F(z)).                    \tag{VIIIj.6.2}
$$
Это тождество рациональных функций, продолжающееся в каждую точку, где записанные обратные существуют.

#### VIIIj.6.1. Регулярная точка z=1

Если $U$ имеет простой спектр, её неподвижное пространство состоит ровно из $\sum_jh_jP_j$. Проекция на диагональ в этих ортонормированных координатах задаётся $\mathsf H=(|v_j(x)|^2)$.

При простом спектре $I-D$ обратима **тогда и только тогда**, когда $\mathsf H$ обратима. В одну сторону: ненулевой $h$ с $\mathsf Hh=0$ даёт ненулевую неподвижную внедиагональную матрицу, то есть вектор ядра $I-D$. В другую: если $Dy=y$ для ненулевого внедиагонального $y$, из унитарности
$\|\operatorname{Ad}_Uy\|^2=\|By\|^2+\|Dy\|^2=\|y\|^2$ следует $By=0$. Тогда $y$ неподвижна и, при простом спектре, соответствует ненулевому $h$ с $\mathsf Hh=0$.

Если спектр вырожден, размерность неподвижного пространства равна $\sum_\lambda r_\lambda^2>N$; проекция в N-мерную диагональ имеет ядро. Значит, $I-D$ необратима. В итоге
$$
I-D\ \text{обратима}\quad\Longleftrightarrow\quad
       U\ \text{имеет простой спектр и }\det\mathsf H\ne0.          \tag{VIIIj.6.3}
$$

В регулярном случае положим $Y=(I-D)^{-1}C$. Каждому диагональному $x$ соответствует единственная неподвижная матрица с блоками $(x,Yx)$. Поэтому
$$
\mathscr F(1)=I_N.
$$
Неподвижная матрица одновременно неподвижна для $(\operatorname{Ad}_U)^*$. Её нижнее уравнение даёт $B^*=(I-D^*)Y$, то есть $B(I-D)^{-1}=Y^*$. Дифференцируя (VIIIj.6.1),
$$
\boxed{\quad
 \mathscr F'(1)=B(I-D)^{-2}C=Y^*Y,\qquad
             I_N+\mathscr F'(1)=(\mathsf H\mathsf H^*)^{-1}.
 \quad}                                                          \tag{VIIIj.6.4}
$$
Второе равенство проверяется нормой: коэффициенты неподвижной матрицы в собственных проекторах равны $\mathsf H^{-1}x$, и её HS-норма в квадрате равна одновременно
$\|\mathsf H^{-1}x\|^2$ и $\|x\|^2+\|Yx\|^2$.

#### VIIIj.6.2. Детерминантная формула по всем случаям

При простом спектре собственные значения $\operatorname{Ad}_U$ равны $\lambda_j\overline{\lambda_k}$; ровно N из них равны 1. Поэтому
$$
\lim_{z\to1}\frac{\det(I-z\operatorname{Ad}_U)}{(1-z)^N}
      =\prod_{j\ne k}(1-\lambda_j\overline{\lambda_k})
      =\prod_{j<k}|\lambda_j-\lambda_k|^2.                         \tag{VIIIj.6.5}
$$
Каждая пара $j,k$ даёт $(1-\lambda_j\bar\lambda_k)(1-\lambda_k\bar\lambda_j)
=|\lambda_j-\lambda_k|^2$.

В регулярном случае $\mathscr F(1)=I$ и
$$
I-z\mathscr F(z)
       =(1-z)(I+\mathscr F'(1))+O((z-1)^2).
$$
Подставляя (VIIIj.6.4)–(VIIIj.6.5) в (VIIIj.6.2), получаем (VIIIj.1.6).

Чтобы снять условие регулярности, параметризуем $U=V\operatorname{diag}(\lambda_j)V^*$. Простые наборы $(\lambda_j)$ плотны на N-мерном торе. Матрицы $V$ с $\det(|V_{xj}|^2)\ne0$ также плотны: фиксируем эрмитов логарифм $K$ с $e^{iK}=V$, и рассмотрим путь $V_s=e^{i(1-s)K}$. При $s=0$ это $V$, при $s=1$ — $I$, где определитель равен 1. Функция $\det(|(V_s)_{xj}|^2)$ вещественно-аналитична и не тождественно нулевая; её нули изолированы. Значит, регулярные $V_s$ подходят сколь угодно близко к $V$. Существование K следует из спектрального разложения V и выбора аргументов её собственных значений.

Обе стороны (VIIIj.1.6) непрерывны по $V,\lambda_j$. Поэтому тождество переходит к произвольным, в том числе вырожденным, наборам. При вырождении произведение промежутков равно 0, а слева действительно есть невидимая неподвижная мода по (VIIIj.6.3). LD5 доказана.

#### VIIIj.6.3. Что это даёт именно исходной памяти

Для исходных $U_N$, $N\ge e^{1000}$, получена безусловная альтернатива:

1. $I-D_N$ необратима и существует точная невидимая неподвижная мода; либо
2. выполняются (VIIIj.6.4), а кроме (VIIIj.1.5) есть нижняя граница
$$
\operatorname{Tr}\mathscr F_N'(1)
                     \ge (N-1)\left(\frac{\log N}{66}-1\right).
                                                                    \tag{VIIIj.6.6}
$$

Для доказательства (VIIIj.6.6) ограничим $\mathsf H$ на $\mathbf1^\perp$, обозначив результат $\mathsf H^0$. Стохастичность по строкам и столбцам сохраняет это пространство, а единичная мода даёт нулевую производную $\mathscr F'$. По (VIIIj.5.3)
$$
t=\operatorname{Tr}(\mathsf H^0\mathsf H^{0*})
      =\sum_j\sum_x|v_j(x)|^4-1\le33N/\log N-1.
$$
В регулярном случае $t>0$. Для положительных чисел $\sigma_i^2$, $1\le i\le N-1$, неравенство Коши даёт $\sum_i\sigma_i^{-2}\ge(N-1)^2/\sum_i\sigma_i^2$. Поэтому
$$
\operatorname{Tr}\mathscr F'(1)
       \ge (N-1)^2/t-(N-1)
       \ge(N-1)\left(\frac{\log N}{66}-1\right),
$$
где использовано $(N-1)/N\ge1/2$. Это доказывает (VIIIj.6.6). Никакая из ветвей не объявляется установленной для каждой отдельной исходной размерности; сама альтернатива и оценки (VIIIj.1.4)–(VIIIj.1.5) безусловны.

Для $7\nmid N$ простота AP6 позволяет при желании устранить первую ветвь **выбором наблюдаемого базиса**, не изменяя спектр U: в сколь угодно малой окрестности исходного базиса существует детерминированное унитарное R с обратимой матрицей $|(R^*V)_{xj}|^2$. Это та же аналитическая плотность. При $\|R-I\|\le\epsilon_N\to0$
$$
\|P_{R^*UR}-P_U\|
 \le\|\operatorname{Ad}_{R^*UR}-\operatorname{Ad}_U\|
 \le4\epsilon_N.
$$
Следовательно, сильный предельный интенсивностный вход сохраняется. При $\epsilon_N\le N^{-2}$ также сохраняется порядок $O(1/\log N)$ координатной делокализации. Никакого усреднения по R или изменения собственных фаз здесь нет. Это выбор базиса анализа, а не замена исходной семьи другой спектральной семьёй.

### VIIIj.7. LD6: почему новые тождества ещё не дают Sine₂

Проверим конкретный универсальный вывод из предыдущих разделов: достаточно ли сильного интенсивностного смешивания, отражённой щели, простого спектра, всех трансцендентных попарных отношений, делокализации собственных векторов и регулярной Ward-формулы? Ответ отрицателен. Строим другой пример, используя уже доказанный SC3. Это проверка общего утверждения, **не подпоследовательность исходных U_N**.

#### VIIIj.7.1. Исходные внутренние данные SC3

Для каждого простого $p\ge5$ SC3 строит симметричную метаплектическую $R_p$ с простым спектром
$$
\lambda_j=e^{2\pi ij/(p+1)},\qquad1\le j\le p,
$$
и сопряжение $K_p=V_pR_pV_p^*$, $V_p=e^{i\epsilon H_r}$,
$\epsilon=10^{-80}$, $H_r=T_p(r,0)+T_p(-r,0)$, такое, что
$$
\|P_{K_p}-J_p\|\le9\epsilon,\quad
 \max|K_p(x,y)|\le e^{4\epsilon}/\sqrt p,\quad
                  \|B_{K_p}\|\le1-\epsilon^2/480.                 \tag{VIIIj.7.1}
$$
Здесь $B_U(x,y)=U_{xy}\overline{U_{yx}}$ — отражённая матрица из исходных частей, не блок B в (VIIIj.6.1). Все перечисленные входы уже доказаны в SC3; не заменяем их численным предположением.

Дополнительное следствие того же конечнополевого построения: $R_p^m$ имеет плоские элементы при
$$
1\le m<(p+1)/2.                             \tag{VIIIj.7.2}
$$
Действительно, классический торус порождён элементом u порядка $p+1$. Верхний правый элемент его m-й степени равен 0 только при $u^m=\pm1$: нормированный элемент тогда лежит в $\mathbb F_p$ и имеет норму 1, то есть равен $\pm1$. В диапазоне (VIIIj.7.2) это невозможно. Из Weyl-ковариантности $R_p^m Z=T_p(\beta_m,a_m)R_p^m$, $\beta_m\ne0$, следует равенство модулей элементов столбца при сдвиге строки на $\beta_m$. По простоте p такой сдвиг обходит все строки, и унитарность даёт модуль $p^{-1/2}$.

Центральное время $m=(p+1)/2$ исключено существенно: оно соответствует $-I$ и вообще не даёт плоской матрицы. В конечной проверке оно является обязательным отрицательным тестом.

Сумма модулей коэффициентов $V_p$ в степенях сдвига не больше $e^{2\epsilon}$; это следует из ряда экспоненты и суммы модулей коэффициентов $H_r$, равной 2. Поэтому
$$
\max|(K_p^m)_{xy}|\le e^{4\epsilon}/\sqrt p
                              <2/\sqrt p
       \quad(1\le m<(p+1)/2).
$$
Gram-доказательство раздела 4 с $L=(p+1)/2$ теперь даёт
$$
\max_{j,x}|v_j(x)|^2
                      \le \frac2{p+1}+\frac2{\sqrt p}
                      \le\frac3{\sqrt p}.                         \tag{VIIIj.7.3}
$$
Таким образом, уже у другого семейства собственные векторы делокализованы сильнее, чем нужно для (VIIIj.1.3).

#### VIIIj.7.2. Все отношения трансцендентны, локальный предел остаётся решёткой

Изменим **каждое** собственное значение, сохраняя собственные векторы:
$$
\widetilde\lambda_j
                  =\lambda_j e^{ij/p^6},\qquad1\le j\le p.
$$
Положим $\widetilde K_p=V_{\rm eig}\operatorname{diag}(\widetilde\lambda_j)V_{\rm eig}^*$, где $V_{\rm eig}$ — собственный базис $K_p$. Точно
$$
\|\widetilde K_p-K_p\|\le p^{-5},\qquad
 \|\widetilde K_p-K_p\|_{\mathrm{HS}}\le p^{-9/2}.                  \tag{VIIIj.7.4}
$$
Для $j\ne k$, отношение $\widetilde\lambda_j/\widetilde\lambda_k$ — ненулевой алгебраический корень единицы, умноженный на $e^{i(j-k)/p^6}$. По внутренней E1 оно трансцендентно. Значит, спектр прост, и ни один положительный проектный период невозможен.

Максимальное смещение развёрнутой собственной фазы не больше $p^{-4}/(2\pi)$, поэтому локальный процесс имеет тот же случайно сдвинутый решётчатый предел, что и исходный спектр с одним отсутствующим $(p+1)$-м корнем. Доказательство решётчатого предела дано в SC2–SC3: дефект отсутствующего узла имеет частоту $1/p$, остальные промежутки после развёртки стремятся к 1. Смещение, равномерно стремящееся к нулю, сохраняет ограниченные непрерывные локальные тесты: в каждом ограниченном окне число узлов этой почти решётки ограничено, и непрерывный тест меняется не больше его модуля непрерывности, умноженного на это число. Отношения трансцендентны, но это не меняет предела.

Интенсивностная оценка сохраняется:
$$
\|P_{\widetilde K_p}-P_{K_p}\|\le2p^{-5}.
$$
Это сжатие разности двух унитарных сопряжений. Для отражённой матрицы из (VIIIj.7.1), обозначая $\Delta=\widetilde K_p-K_p$, имеем
$$
\|B_{\widetilde K_p}-B_{K_p}\|
 \le\|B_{\widetilde K_p}-B_{K_p}\|_{\mathrm{HS}}
 \le2\max|K_p|\,\|\Delta\|_{\mathrm{HS}}+\|\Delta\|_{\mathrm{HS}}^2
 \le4p^{-5}+p^{-9}.                                               \tag{VIIIj.7.5}
$$
Квадратичный член ограничен $\|\Delta\|_{\mathrm{HS}}^2$ покоординатным неравенством и Коши. Поэтому фиксированная отражённая щель сохраняется для всех достаточно больших p.

При необходимости вторые моменты всех секулярных коэффициентов из SC3 также сохраняются. В формальном кольце рядов по z до степени p
$$
\log\prod_{j=1}^p
  \frac{1+z\lambda_je^{ij/p^6}}{1+z\lambda_j}
   =\sum_{r=1}^p a_rz^r\pmod{z^{p+1}},
 \qquad |a_r|\le\sum_{j=1}^p j/p^6\le p^{-4}.
$$
Здесь $|e^{iru}-1|\le r|u|$. Сумма модулей коэффициентов логарифма не больше $p^{-3}$; после экспоненцирования сумма модулей ненулевых коэффициентов разности с 1 не больше $e^{p^{-3}}-1\le2p^{-3}$. У базового многочлена коэффициенты $e_k=(-1)^k$. Следовательно, по всем $0\le k\le p$
$$
|e_k(\widetilde K_p)-(-1)^k|\le2p^{-3}.
$$
Общий случайный фазовый сдвиг по-прежнему точно убирает разные степени k,l; диагональные вторые моменты отличаются от 1 не больше $5p^{-3}$. Никаких независимых фаз не вводится в этот пример.

#### VIIIj.7.3. Регулярность Ward без изменения спектра

Выберем детерминированную унитарную $Z_p$ со
$\|Z_p-I\|\le p^{-6}$, делающую матрицу модулей собственных векторов обратимой; её существование доказано аналитической плотностью в разделе 6. Положим
$$
W_p=Z_p^*\widetilde K_pZ_p.
$$
Все спектральные утверждения, включая решётчатый предел, трансцендентность отношений и секулярные коэффициенты, сохраняются точно. Собственные векторы по (VIIIj.7.3) удовлетворяют
$$
\max|v_j^{\,W_p}(x)|^2\le4/\sqrt p
$$
для всех достаточно больших p. Интенсивностная норма меняется не больше $4p^{-6}$. Поэлементная оценка остаётся $O(p^{-1/2})$.

Для отражённой матрицы после последнего сопряжения $\|\Delta_{\rm rot}\|_{\mathrm{HS}}\le2p^{-11/2}$, а $\max|\widetilde K_p|\le3/\sqrt p$. Как в (VIIIj.7.5), изменение нормы не больше $12p^{-6}+4p^{-11}$. Вместе с (VIIIj.7.1), (VIIIj.7.5), например при всех простых $p\ge10^{40}$,
$$
\|B_{W_p}\|\le1-\epsilon^2/960,\qquad
             \limsup\|P_{W_p}-J_p\|\le9\epsilon<10^{-64}.
$$
Резольвента в (VIIIj.6.3) регулярна, и все равенства Ward и детерминантное тождество выполняются.

Итак, даже после добавления новых условий общий вывод Sine₂ ложен. Этот результат сформулирован только для **другой семьи на простых размерностях**. Он не является контрпримером к исходным матрицам и не решает исходный парный тест. Его роль — отклонить непроверенный переход от LD2–LD5 и общих интенсивностных входов к требуемой микроскопической статистике.

### VIIIj.8. Где остановилась попытка оценить исходную отрицательную поправку

Получены две точные структуры для исходного оператора:

- все собственные векторы теряют координатную локализацию;
- его память имеет много мягких направлений, а детерминант памяти связан с полным спектральным якобианом.

Но нужная сумма следов ещё не оценена. При $|z|<1$
$$
\log\det(I-z\operatorname{Ad}_{U_N})
                    =-\sum_{m\ge1}\frac{z^m}{m}
                                   |\operatorname{Tr}U_N^m|^2.    \tag{VIIIj.8.1}
$$
Ряд абсолютно сходится для каждого фиксированного N, поскольку
$|\operatorname{Tr}U_N^m|^2\le N^2$. (VIIIj.6.2) сохраняет все его коэффициенты и все знаки.

Тождества (VIIIj.6.4) задают значение и первую производную в z=1. Чтобы получить оценки коэффициентов порядка N этим контурным методом, нужны оценки на контурах, приближающихся к единичной окружности: при фиксированном $r<1$ множитель $r^{-m}$ в формуле Коши растёт экспоненциально по N. Нужного знакового контроля полного выражения, например в слое $1-|z|\asymp1/N$, здесь не получено. Конечный Taylor-полином около 1 также не контролируется без оценок высших производных; они содержат степени $(I-zD_N)^{-1}$.

Элементарная нормовая верхняя оценка, конечно, имеется:
$$
\|(I-zD_N)^{-1}\|\le(1-|z|)^{-1},
                              \qquad |z|<1.                       \tag{VIIIj.8.2}
$$
Она следует из сходящегося в норме геометрического ряда и $\|D_N\|\le1$. В слое $1-|z|\asymp1/N$ это оценка порядка N. Она выполняется также для контрсемейства LD6, поэтому вместе с доказанными Ward-тождествами и остальными перечисленными условиями не даёт нужной спектральной компенсации. Открытым оставлен более точный контроль полной знаковой величины, а не существование любой верхней оценки резольвенты.

LD4 показывает, что ограниченная равномерно по N резольвента в точке 1 невозможна. Это не запрет на следовую компенсацию и не утверждение о невозможности всего резольвентного метода. LD6 отдельно показывает, что сами Ward-тождества, делокализация и качественная арифметика нужной компенсации не определяют.

**ДОКАЗАНО:** LD1 — положительная локализация с полным диагональным alias-остатком; LD2 — все элементы степеней на явном диапазоне; LD3 — каждый исходный собственный вектор, все нечётные N; LD4 — множество мягких направлений и нижняя резольвентная оценка; LD5 — Ward-формулы и точный спектральный якобиан; LD6 — отрицательная проверка универсального вывода на усиленном другом семействе.

**OUTLINE:** LD1 $\Rightarrow$ LD2 $\Rightarrow$ LD3 $\Rightarrow$ LD4 — завершённая цепочка. Неподвижное пространство $\Rightarrow$ LD5 — завершённое конечномерное доказательство. LD5 $\Rightarrow$ Sine₂ не установлено; общий вывод из одних перечисленных свойств исключён LD6.

**НЕДОКАЗАНО:**

- U-LD-1: для исходной семьи количественно оценить полную знаковую сумму на $1\le m<2N$ и получить именно $-\delta_*$ для Y-сектора.
- U-LD-2: на резольвентном маршруте получить N-зависимый контроль полного выражения (VIIIj.6.2) около единичной окружности, достаточный для исходной временной нормировки. Ограничение нормы памяти нулём или постоянной заменой не обосновано.
- U-LD-3: закрыть все фиксированные порядки достаточного критерия либо ограниченный Laplace-закон.
- U-LD-4: если продолжать через регулярную Ward-формулу в первоначальном координатном базисе, установить для исходных размерностей обратимость $\mathsf H_N$ или работать с её точным сингулярным разложением. Малое изменение наблюдаемого базиса устраняет конечномерную нерегулярность при простом спектре, но не U-LD-1.

Маршрут через геометрию классической карты остаётся открытым: теперь он контролирует собственные векторы, но не исходные локальные собственные фазы. Маршрут через резольвенту тоже открыт; новым входом служат точные Ward-формулы и неизбежные мягкие направления. Повторение ограниченной резольвенты или подстановка только значения z=1 без контроля слоя $1/N$ не продолжит доказательство.

Самое трудное место не подменено более слабым условием: на Heisenberg-времени требуется коллективная фазовая оценка. Все полученные здесь малые ошибки выписаны со своим диапазоном и не переносятся на $m\asymp N$. Полный исходный закон по-прежнему не доказан и не опровергнут.

### VIIIj.9. Полные текущие вычисления и восстановление записей

Всего выполнено семь hosted-вызовов: четыре первоначальных и три повторных. При заключительной проверке отчёта обнаружено, что временно сохранённые полные объекты первых вызовов не удержались в записях. Их входы восстановлены из протокола диалога, исходные наблюдавшиеся итоги помечены отдельно. Три корректных проверки повторены; их полные входы и фактически возвращённые ответы записаны непосредственно при повторе. Отсутствующий исходный MCP-объект не реконструируется и не объявляется сохранённым. Это исправление вычислительного приложения; доказательства LD1–LD6 от него не меняются.

Текущие подтверждающие вызовы: ward_reproduced, alias_reproduced, torus_reproduced. Первоначальный вход с предупреждением не используется как подтверждение. Никакого нового локального v2-manifest не заявляется.

#### VIIIj.9.1. ward_initial

Статус: superseded by fully retained reproduction.

Вход совпадает с программой ward_reproduced ниже; его восстановленный SHA-256: a8c51e3010965136f629c82fef478a25362e86e3afcec1b70a2b48036b71a90b.

Запись по протоколу первоначального вызова:

```json
{
  "id": "ward_initial",
  "status": "superseded by fully retained reproduction",
  "code_ref": "ward_reproduced",
  "record_provenance": "original tool transcript; full MCP payload did not persist in transient execution state",
  "observed_summary": "all Ward and determinant assertions true; memory determinants 196/3125 and 264257536/497067025; dark and degenerate zero fixtures true",
  "restored_input_sha256": "a8c51e3010965136f629c82fef478a25362e86e3afcec1b70a2b48036b71a90b"
}
```

#### VIIIj.9.2. alias_initial

Статус: superseded by fully retained reproduction.

Вход совпадает с программой alias_reproduced ниже; его восстановленный SHA-256: 19571eecae7e3d1ee6463cd308b72d176f0a38857f4f4eb1cc7e4d40b7fcf320.

Запись по протоколу первоначального вызова:

```json
{
  "id": "alias_initial",
  "status": "superseded by fully retained reproduction",
  "code_ref": "alias_reproduced",
  "record_provenance": "original tool transcript; full MCP payload did not persist in transient execution state",
  "observed_summary": "five Fejer cases, 1568 alias entries and all cone/exponent/constant assertions true",
  "restored_input_sha256": "19571eecae7e3d1ee6463cd308b72d176f0a38857f4f4eb1cc7e4d40b7fcf320"
}
```

#### VIIIj.9.3. torus_initial

Статус: diagnostic; not used as current confirmation.

```wolfram
ClearAll[z,red,bar,mt,power,pp,aa,bb,dd];
fixtures=Table[
 {pp,dd,aa,bb}=spec;BB=Mod[dd bb,pp];iv=PowerMod[2BB,-1,pp];
 phi=Sum[z^j,{j,0,pp-1}];red[v_]:=PolynomialRemainder[Expand[v],phi,z];
 bar[v_]:=red[Sum[Coefficient[v,z,j]z^Mod[-j,pp],{j,0,pp-2}]];
 mt=Table[z^Mod[-iv(aa*x^2-2x*y+aa*y^2),pp],{x,0,pp-1},{y,0,pp-1}];
 mt=Map[red,mt,{2}];power=IdentityMatrix[pp];
 good={};central=False;
 Do[
 power=Map[red,power.mt,{2}];
 equal=Flatten[Table[TrueQ[red[power[[x,y]]bar[power[[x,y]]]-pp^(m-1)]==0],{x,pp},{y,pp}]];
 If[m<(pp+1)/2,AppendTo[good,And@@equal],central=Not[And@@equal]],
 {m,1,(pp+1)/2}];
 <|"p"->pp,"nonresidue"->dd,"a"->aa,"b"->bb,
 "normOne"->Mod[aa^2-dd bb^2,pp]==1,
 "noncentralTimes"->Range[(pp-1)/2],"allPowersFlatBeforeCentralTime"->And@@good,
 "centralTimeCorrectlyNotFlat"->central|>,
 {spec,{{5,2,3,2},{7,3,2,1},{11,2,3,2}}}];
<|"kernelVersion"->$Version,"torusPowerFixtures"->fixtures|>
```

Запись по протоколу первоначального вызова:

```json
{
  "id": "torus_initial",
  "status": "diagnostic; not used as current confirmation",
  "record_provenance": "input restored verbatim from tool transcript; initial full MCP payload unavailable",
  "observed_diagnostic_text": "Symbol::undefined2: Warning: Global symbols \"BB, BB\" are undefined.\nGeneral::messages: Messages were generated which may indicate errors.",
  "observed_summary": "all finite assertions true but parser warning; superseded by cleared-symbol exact repetition",
  "code_sha256": "e9f8b0c9770352ee28bbfa7493c21e9fc9af9511226fa3d4214c554e2fe85cfd"
}
```

#### VIIIj.9.4. torus_corrected_initial

Статус: superseded by fully retained reproduction.

Вход совпадает с программой torus_reproduced ниже; его восстановленный SHA-256: 6e045f5d0c2832db14a3d5f33542f7e793a823254e9da954c3ad4b6cd0c677e4.

Запись по протоколу первоначального вызова:

```json
{
  "id": "torus_corrected_initial",
  "status": "superseded by fully retained reproduction",
  "code_ref": "torus_reproduced",
  "record_provenance": "original tool transcript; full MCP payload did not persist in transient execution state",
  "observed_summary": "p5,7,11 noncentral flat powers and expected nonflat central times all true without diagnostics",
  "restored_input_sha256": "6e045f5d0c2832db14a3d5f33542f7e793a823254e9da954c3ad4b6cd0c677e4"
}
```

#### VIIIj.9.5. ward_reproduced

Статус: passed exact finite assertions.

```wolfram
ClearAll[make,amp,raw,seq,dim,inds,dd,xx,yy,aa,bb,zz];
make[v_,lam_]:=Module[{n,u,off,p,bl,cl,mem,h,dis,detm,r,ff,fp,ys},
 n=Length[lam];u=FullSimplify[v.DiagonalMatrix[lam].ConjugateTranspose[v]];
 off=Select[Tuples[Range[n],2],#[[1]]!=#[[2]]&];
 p=Table[Expand[u[[x,a]]Conjugate[u[[x,a]]]],{x,n},{a,n}];
 bl=Table[u[[x,off[[j,1]]]]Conjugate[u[[x,off[[j,2]]]]],{x,n},{j,Length[off]}];
 cl=Table[u[[off[[j,1]],a]]Conjugate[u[[off[[j,2]],a]]],{j,Length[off]},{a,n}];
 mem=Table[u[[off[[i,1]],off[[j,1]]]]Conjugate[u[[off[[i,2]],off[[j,2]]]]],{i,Length[off]},{j,Length[off]}];
 h=Map[Expand[# Conjugate[#]]&,v,{2}];
 dis=FullSimplify[Times@@Flatten[Table[If[j<k,{(lam[[j]]-lam[[k]])Conjugate[lam[[j]]-lam[[k]]]},Nothing],{j,n},{k,n}]]];
 detm=Factor[Det[IdentityMatrix[Length[off]]-mem]];
 If[detm!=0,
  r=Inverse[IdentityMatrix[Length[off]]-mem];ys=r.cl;
  ff=FullSimplify[p+bl.r.cl];fp=FullSimplify[bl.r.r.cl];
  <|"N"->n,"memoryDeterminant"->detm,"overlapDeterminantSquared"->Factor[Det[h]^2],
   "spectralVandermondeSquared"->dis,"determinantIdentity"->TrueQ[FullSimplify[detm==Det[h]^2 dis]],
   "wardF1"->TrueQ[ff==IdentityMatrix[n]],
   "wardDerivative"->TrueQ[FullSimplify[fp==ConjugateTranspose[ys].ys]],
   "overlapInverseIdentity"->TrueQ[FullSimplify[IdentityMatrix[n]+fp==Inverse[h.Transpose[h]]]]|>,
  <|"N"->n,"memoryDeterminant"->detm,"overlapDeterminantSquared"->Factor[Det[h]^2],
    "spectralVandermondeSquared"->dis,"determinantIdentity"->TrueQ[FullSimplify[detm==Det[h]^2 dis]],
    "inverseWardNotEvaluatedAtSingularPoint"->True|>]
];
q2={{3,-4},{4,3}}/5;
w={1,2,3};q3=IdentityMatrix[3]-Outer[Times,w,w]/7;
q4={{1,1,1,1},{1,-1,1,-1},{1,1,-1,-1},{1,-1,-1,1}}/2;
l2={1,(3+4I)/5};l3={1,(-3+4I)/5,(5+12I)/13};
l4={1,(-3+4I)/5,(5+12I)/13,(8+15I)/17};
<|"kernelVersion"->$Version,"rationalWardFixtures"->{make[q2,l2],make[q3,l3]},
 "simpleDarkFixture"->make[q4,l4],"degenerateSpectrumFixture"->make[q3,{1,1,(-3+4I)/5}]|>
```

Полный ответ текущего повтора:

```json
{
  "content": [
    {
      "type": "text",
      "text": "Out[1]= <|\"kernelVersion\" -> \"15.0.1 for Linux x86 (64-bit) (July 2, 2026)\", \"rationalWardFixtures\" -> {<|\"N\" -> 2, \"memoryDeterminant\" -> 196/3125, \"overlapDeterminantSquared\" -> 49/625, \"spectralVandermondeSquared\" -> 4/5, \"determinantIdentity\" -> True, \"wardF1\" -> True, \"wardDerivative\" -> True, \"overlapInverseIdentity\" -> True|>, <|\"N\" -> 3, \"memoryDeterminant\" -> 264257536/497067025, \"overlapDeterminantSquared\" -> 16129/117649, \"spectralVandermondeSquared\" -> 16384/4225, \"determinantIdentity\" -> True, \"wardF1\" -> True, \"wardDerivative\" -> True, \"overlapInverseIdentity\" -> True|>}, \"simpleDarkFixture\" -> <|\"N\" -> 4, \"memoryDeterminant\" -> 0, \"overlapDeterminantSquared\" -> 0, \"spectralVandermondeSquared\" -> 57802752/1349232625, \"determinantIdentity\" -> True, \"inverseWardNotEvaluatedAtSingularPoint\" -> True|>, \"degenerateSpectrumFixture\" -> <|\"N\" -> 3, \"memoryDeterminant\" -> 0, \"overlapDeterminantSquared\" -> 16129/117649, \"spectralVandermondeSquared\" -> 0, \"determinantIdentity\" -> True, \"inverseWardNotEvaluatedAtSingularPoint\" -> True|>|>"
    }
  ],
  "structuredContent": null,
  "isError": false
}
```

#### VIIIj.9.6. alias_reproduced

Статус: passed exact finite assertions.

```wolfram
ClearAll[z,nn,k,l,x,half,h,hh,aa,ff];
fejer=Table[
 h=Sum[(ll-Abs[k])z^k/ll^2,{k,1-ll,ll-1}];
 aa=Sum[z^j,{j,0,ll-1}]/ll;
 <|"L"->ll,"LaurentSquareIdentity"->TrueQ[Expand[h-aa(aa/.z->1/z)]==0],
   "weightsSumOne"->TrueQ[(h/.z->1)==1],"constantCoefficient"->Coefficient[Expand[h],z,0]|>,
 {ll,{1,2,3,5,8}}];
alias=Table[
 half=PowerMod[2,-1,nn];
 tests=Flatten[Table[
   With[{actual=If[Mod[l,nn]==0,(-1)^(k*l)z^Mod[k*(x+half*l),nn],0],
         predicted=If[Mod[l,nn]==0,(-1)^(k*(l/nn))z^Mod[k*x,nn],0]},
   TrueQ[Expand[actual-predicted]==0]],
 {k,-3,3},{l,{-2nn,-nn,-1,0,1,nn,2nn}},{x,0,nn-1}]];
 <|"N"->nn,"entriesCompared"->Length[tests],"allDiagonalAliasPhasesExact"->And@@tests|>,
 {nn,{3,5,9,15}}];
ss={{3,4},{2,3}};lower={{5/2,7/2},{3/2,5/2}};
opt=With[{ls=nn^(2/9)(4/3)^(mm/9)16^(-8mm/9),target=nn^(-2/9)(64/3)^(8mm/9)},
 {FullSimplify[(4/3)^mm/ls==target,Assumptions->nn>0&&mm>=0],
  FullSimplify[nn^-2 16^(8mm)ls^8==target,Assumptions->nn>0&&mm>=0]}];
<|"kernelVersion"->$Version,"fejerIdentities"->fejer,"aliasFixtures"->alias,
 "coneEntrywiseLower"->And@@Flatten[MapThread[GreaterEqual,{lower,(3/4)ss},2]],
 "optimizedExponents"->opt,"constantCertificate"->{10^20+2<10^21,10^21<10^22,99*1000<121*(1000-99)},
 "negativeAliasFixture"->(-1)^(1*5)==-1|>
```

Полный ответ текущего повтора:

```json
{
  "content": [
    {
      "type": "text",
