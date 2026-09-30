# К полной CUE-универсальности на масштабе Гейзенберга для фиксированного нелинейного квантового cat map

## Точные редукции, новые finite-type оценки, FUP-механизм и оставшиеся барьеры

**Статус заметки:** исследовательский препринт / рабочая статья.  
**Дата:** 30 сентября 2026.  
**Модель:** фиксированная, детерминированная, без усреднения по параметру и без искусственного шума.  
**Ключевой параметр:** \(\tau=10^{-80}\) фиксирован навсегда.

> **Главное утверждение о статусе.** Полная микроскопическая CUE-универсальность для данной конкретной последовательности \(U_N\) в этой заметке **не доказана**. Ниже строго отделены:
>
> 1. точные алгебраические тождества;
> 2. результаты, доказанные непосредственно для конкретного символа \(g\);
> 3. теоремы из литературы, которые можно использовать как чёрные ящики;
> 4. условные мосты, которые ещё требуется доказать;
> 5. эвристика, которая пока не имеет права называться доказательством.
>
> При этом получена существенно более узкая и конструктивная схема атаки: реальная задача сводится к двум конкретным теоремам — **microlocal open-baker reduction для doubled seven-cut dynamics** и **переход от полученного off-diagonal spectral gap к Heisenberg-time trace correlations**.

---

## 1. Постановка

Пусть \(N\ge 3\) нечётно и

\[
\mathcal H_N=\ell^2(\mathbb Z/N\mathbb Z),\qquad e_N(t)=e^{2\pi i t/N},
\]

а \(h=2^{-1}\pmod N\).

Линейная часть задаётся матрицей

\[
S=
\begin{pmatrix}
3&4\\
2&3
\end{pmatrix},
\qquad
\operatorname{spec}(S)=\{3+2\sqrt2,\,3-2\sqrt2\},
\]

и её метаплектической квантизацией

\[
(M_N)_{xy}
=
N^{-1/2}
e_N\!\left(
-8^{-1}(3x^2-2xy+3y^2)
\right).
\]

Далее

\[
r(q)=(1-\cos 14\pi q)(1+\cos 2\pi q),
\]

\[
e^{i\alpha}=\frac{-3+4i}{5},
\]

\[
v(q)
=
\cos 14\pi q+\frac{r(q)}{10}
+\frac{r(q)\sin 2\pi q}{100}
-\frac1{10},
\]

\[
b_N(x)=
e^{-i\alpha}\frac{r((x+h)/N)}{200},
\]

а \(A_N\) — циклическая эрмитова Jacobi-матрица

\[
(A_N\psi)(x)
=
v(x/N)\psi(x)
+b_N(x)\psi(x+1)
+\overline{b_N(x-1)}\psi(x-1).
\]

Фиксируем

\[
\boxed{\tau=10^{-80}}
\]

и определяем

\[
\boxed{
U_N=e^{i\tau N A_N}M_N.
}
\]

Его обычный midpoint/Weyl-символ равен

\[
\boxed{
g(q,p)
=
v(q)
+
\frac{r(q+\tfrac12)}{100}\cos(2\pi p-\alpha).
}
\]

Критически важно: здесь именно \(r(q+\tfrac12)\), а не \(r(q)\).

Пусть

\[
U_N\psi_{j,N}
=
e^{2\pi i\theta_{j,N}}\psi_{j,N},
\qquad
p_m(N)=\operatorname{Tr}U_N^m.
\]

Цель — доказать микроскопическую CUE-универсальность на полном масштабе Гейзенберга \(m=\Theta(N)\).

---

## 2. Целевой all-\(k\) результат

Для фиксированного \(k\ge2\) положим

\[
D_N(m_1,\dots,m_k)
=
\sum_{\substack{j_1,\dots,j_k\\\text{попарно различны}}}
e^{2\pi i\sum_{a=1}^k m_a\theta_{j_a,N}}.
\]

Эквивалентно, по Möbius-инверсии на решётке разбиений,

\[
D_N(m)
=
\sum_{\pi\in\Pi_k}
\mu(\pi)
\prod_{B\in\pi}
p_{\sum_{a\in B}m_a},
\]

где

\[
\mu(\pi)
=
\prod_{B\in\pi}
(-1)^{|B|-1}(|B|-1)!.
\]

При условии

\[
m_k=-\sum_{a=1}^{k-1}m_a
\]

нужен предел

\[
\boxed{
N^{-k}
\sum_{m\in\mathbb Z^{k-1}}
W(m/N)
\left[
D_N(m)
-
\mathbb E_{\mathrm{CUE}}
D_N^{\mathrm{CUE}}(m)
\right]
\to0
}
\]

для каждого фиксированного \(k\) и каждого
\(W\in C_c^\infty(\mathbb R^{k-1})\).

Это эквивалентно all-\(k\) микроскопическим корреляциям sine-kernel/CUE после стандартного Fourier bridge.

---

## 3. Pair target и Abel target

Для пары CUE benchmark:

\[
B_N(0)=N^2,
\qquad
B_N(m)=\min(|m|,N),\quad m\ne0.
\]

Желаемый weighted pair theorem:

\[
\boxed{
N^{-2}
\sum_{m\in\mathbb Z}
w(m/N)
\left(
|p_m|^2-B_N(m)
\right)
\to0.
}
\]

Абелевская версия:

\[
L_N(s)
=
N^{-2}
\sum_{m\ge1}
e^{-2sm/N}|p_m|^2.
\]

CUE-предел:

\[
\boxed{
L_N(s)\to
L(s)
=
\frac{1-e^{-2s}}{4s^2}.
}
\]

Поскольку

\[
\frac{1-e^{-2s}}{4s^2}
=
\int_0^\infty
e^{-2sx}\min(x,1)\,dx,
\]

вся pair-задача естественно является задачей о сходимости положительных мер

\[
\mu_N
=
\frac1{N^2}
\sum_{m\ge1}
|p_m|^2\delta_{m/N}.
\]

---

# Часть I. Точные тождества

## 4. Abel \(\Rightarrow\) полный weighted pair theorem

Если для каждого \(s>0\)

\[
L_N(s)\to
\int_0^\infty e^{-2sx}\min(x,1)\,dx,
\]

то

\[
\mu_N
\overset{v}{\longrightarrow}
\min(x,1)\,dx
\]

на \((0,\infty)\).

Причина: \(\mu_N\) положительны, Laplace transforms определяют меру однозначно, а локальная tightness получается из одного фиксированного \(s_0>0\):

\[
\mu_N([0,R])
\le
e^{2s_0R}
L_N(s_0).
\]

Следовательно, для всякой
\(w\in C_c(\mathbb R)\)

\[
\frac1{N^2}\sum_{m\ge1}
w(m/N)|p_m|^2
\to
\int_0^\infty
w(x)\min(x,1)\,dx.
\]

После симметризации \(m\leftrightarrow -m\) это даёт полный weighted pair theorem.

### Важная техническая деталь

Для перехода от pointwise convergence \(L_N(s)\to L(s)\) к локально равномерной сходимости по \(s\) не нужен Dini theorem по индексу \(N\). Достаточно монотонности каждого \(L_N\) по \(s\), непрерывности предела и стандартного compact monotone interpolation argument.

---

## 5. Точная resolvent-формула для adjoint dynamics

Определим оператор на Hilbert–Schmidt пространстве

\[
\mathcal U_N(X)=U_NXU_N^*
\]

и

\[
\mathcal D_N
=
\frac{N^2}{4}
(2I-\mathcal U_N-\mathcal U_N^*).
\]

Положим

\[
T_N(s)
=
\frac1N
\operatorname{Tr}_{HS}
(\mathcal D_N+s^2I)^{-1}.
\]

Если

\[
s_N
=
N\,\operatorname{arsinh}(s/N),
\]

то **точно**

\[
\boxed{
T_N(s)
=
\frac{N}{s\sqrt{N^2+s^2}}
\left(
1+2L_N(s_N)
\right).
}
\]

### Доказательство

Собственные значения \(\mathcal U_N\) равны

\[
e^{2\pi i(\theta_j-\theta_k)}.
\]

Поэтому

\[
\mathcal D_N
\quad\text{имеет собственные значения}\quad
N^2\sin^2\pi(\theta_j-\theta_k).
\]

Используем

\[
\frac{1}{s^2+N^2\sin^2\pi x}
=
\frac{1}{s\sqrt{N^2+s^2}}
\left[
1+
2\sum_{m\ge1}
e^{-2m\operatorname{arsinh}(s/N)}
\cos 2\pi mx
\right].
\]

Суммирование по \(j,k\) даёт

\[
\sum_{j,k}
e^{2\pi i m(\theta_j-\theta_k)}
=
|p_m|^2,
\]

что и завершает вывод.

### Следствие

Pair Abel theorem и convergence resolvent \(T_N(s)\) — не просто аналогичные утверждения, а **точно эквивалентные** после микроскопической репараметризации \(s\mapsto s_N\).

---

## 6. Первый mixed cubic benchmark

Для \(a,b\ge1\)

\[
\boxed{
\mathbb E_{\mathrm{CUE}}
\left[
p_{-a}p_{-b}p_{a+b}
\right]
=
N-(N-a)_+-(N-b)_++(N-a-b)_+.
}
\]

Кроме того,

\[
D_N(-a,-b,a+b)
=
p_{-a}p_{-b}p_{a+b}
-|p_a|^2-|p_b|^2-|p_{a+b}|^2+2N.
\]

Лапласовский benchmark

\[
C_N(s)
=
N^{-3}
\sum_{a,b\ge1}
e^{-2s(a+b)/N}
p_{-a}p_{-b}p_{a+b}
\]

должен удовлетворять

\[
\boxed{
C_N(s)\to
\frac{e^{-2s}}{4s^2}.
}
\]

Более общий двухпараметрический CUE-предел:

\[
\frac{e^{-2t}-e^{-2s}}
{8st(s-t)},
\qquad s\ne t.
\]

На диагонали \(t=s\):

\[
\frac{e^{-2s}}{4s^2}.
\]

Это минимальная действительно higher-order проверка, которую не может заменить pair correlation.

---

## 7. Exact all-\(k\) CUE Fourier benchmark

CUE \(k\)-point density:

\[
\rho_{k,N}(x_1,\dots,x_k)
=
\det\!\bigl[K_N(x_a-x_b)\bigr]_{a,b=1}^k,
\]

\[
K_N(x)=\sum_{r=0}^{N-1}e^{2\pi irx}.
\]

Раскрывая determinant по перестановкам,

\[
\rho_{k,N}
=
\sum_{\sigma\in S_k}
\operatorname{sgn}(\sigma)
\prod_{a=1}^k
K_N(x_a-x_{\sigma(a)}).
\]

Интегрирование против

\[
e^{2\pi i\sum_a m_ax_a}
\]

показывает, что каждая cycle \(C\) перестановки вносит вклад только если

\[
\sum_{a\in C}m_a=0.
\]

Для ориентированного cycle

\[
C=(a_1\,a_2\,\dots\,a_\ell)
\]

введём частичные суммы

\[
s_0=0,
\qquad
s_j=
m_{a_1}+\cdots+m_{a_j},
\quad 1\le j\le \ell.
\]

При условии \(s_\ell=0\) положим

\[
\operatorname{rng}_C^\sigma(m)
=
\max_{0\le j<\ell}s_j
-
\min_{0\le j<\ell}s_j.
\]

Тогда

\[
\boxed{
\mathbb E_{\mathrm{CUE}}D_N(m)
=
\sum_{\sigma\in S_k}
\operatorname{sgn}(\sigma)
\prod_{C\in\mathrm{Cyc}(\sigma)}
\mathbf 1_{\sum_{a\in C}m_a=0}
\left(
N-\operatorname{rng}_C^\sigma(m)
\right)_+.
}
\]

Это точная конечномерная формула.

### Геометрическая структура резонансов

Если никакая собственная непустая подсовокупность индексов не имеет нулевой суммы,

\[
\sum_{a\in I}m_a\ne0
\quad
\forall\,\varnothing\ne I\subsetneq\{1,\dots,k\},
\]

то выживают только \(k\)-cycles.

Все lower-cycle terms живут на гиперплоскостях

\[
\sum_{a\in I}m_a=0.
\]

Это чрезвычайно важно: те же гиперплоскости появляются как «плохие временные резонансы» в multi-Fejér подходе.

---

## 8. Determinant identity для distinct-index observables

В eigenbasis \(U_N\) имеем

\[
\det\left(
I+\sum_{a=1}^k t_aU_N^{m_a}
\right)
=
\prod_{j=1}^N
\left(
1+\sum_{a=1}^k
t_ae^{2\pi i m_a\theta_j}
\right).
\]

Коэффициент \(t_1\cdots t_k\) выбирает \(k\) различных eigenindices. Поэтому

\[
\boxed{
D_N(m_1,\dots,m_k)
=
\left.
\partial_{t_1}\cdots\partial_{t_k}
\det\left(
I+\sum_{a=1}^k t_aU_N^{m_a}
\right)
\right|_{t=0}.
}
\]

Это удобный вход для Riemann–Siegel/self-inversive spectral determinant методов.

---

## 9. Tensor/operator representation all-\(k\)

Для разбиения \(\pi\in\Pi_k\) каждому блоку \(B\in\pi\) сопоставляется tensor factor.

При \(m_k=-\sum_{a<k}m_a\) можно определить commuting operators

\[
R_{a,\pi}
=
U_N^{(B(a))}
\left(
U_N^{(B(k))}
\right)^{-1},
\qquad
a=1,\dots,k-1,
\]

так что

\[
\boxed{
\operatorname{Tr}
\prod_{a<k}
R_{a,\pi}^{m_a}
=
\prod_{B\in\pi}
p_{\sum_{a\in B}m_a}.
}
\]

Тем самым all-\(k\) корреляции превращаются в joint spectral problem для commuting phase-difference operators.

---

# Часть II. Точный символ и его специальные свойства

## 10. Факторизация \(r\)

Имеем

\[
r(q)
=
(\sin6\pi q+\sin8\pi q)^2,
\]

а после half-shift

\[
\boxed{
r(q+\tfrac12)
=
(\sin6\pi q-\sin8\pi q)^2.
}
\]

Также

\[
r(q+\tfrac12)
=
1-\cos2\pi q
-\frac12\cos12\pi q
+\cos14\pi q
-\frac12\cos16\pi q.
\]

---

## 11. Полный Fourier support символа

Диагональная часть:

\[
\begin{aligned}
v(q)
={}&
\frac1{10}\cos2\pi q
-\frac1{20}\cos12\pi q
+\frac9{10}\cos14\pi q
-\frac1{20}\cos16\pi q\\
&+\frac1{100}\sin2\pi q
+\frac1{200}\sin4\pi q
+\frac1{400}\sin10\pi q
+\frac1{200}\sin12\pi q\\
&-\frac1{200}\sin16\pi q
-\frac1{400}\sin18\pi q.
\end{aligned}
\]

Отсюда \(m=0\) Fourier support содержит

\[
n=\pm1,\pm2,\pm5,\pm6,\pm7,\pm8,\pm9,
\]

то есть 14 мод.

Hopping part имеет \(p\)-частоты \(m=\pm1\) и \(q\)-частоты

\[
n=0,\pm1,\pm6,\pm7,\pm8,
\]

то есть ещё 18 мод.

Итого:

\[
\boxed{
|\operatorname{supp}\widehat g|=32.
}
\]

---

## 12. Несколько критических точных Fourier coefficients

Прямое символическое вычисление даёт

\[
\widehat g(1,0)
=
\frac1{20}-\frac{i}{200},
\]

\[
\widehat g(-1,0)
=
\frac1{20}+\frac{i}{200},
\]

поэтому

\[
\boxed{
|\widehat g(\pm1,0)|
=
\frac{\sqrt{101}}{200}.
}
\]

Для чистой \(p\)-гармоники

\[
\widehat g(0,1)
=
-\frac3{1000}-\frac{i}{250},
\]

\[
\widehat g(0,-1)
=
-\frac3{1000}+\frac{i}{250},
\]

и

\[
\boxed{
|\widehat g(0,\pm1)|=\frac1{200}.
}
\]

Смешанные первые гармоники:

\[
\widehat g(\pm1,1)
=
\frac3{2000}+\frac{i}{500},
\]

\[
\widehat g(\pm1,-1)
=
\frac3{2000}-\frac{i}{500},
\]

следовательно

\[
\boxed{
|\widehat g(\pm1,\pm1)|=\frac1{400}.
}
\]

---

## 13. У символа нет нетривиальной translation symmetry

Предположим

\[
g(q+a,p+b)=g(q,p)
\quad\forall(q,p)\in\mathbb T^2.
\]

Из ненулевой моды \((1,0)\) следует

\[
e^{2\pi ia}=1,
\]

то есть

\[
a=0\pmod1.
\]

Из ненулевой моды \((0,1)\) затем следует

\[
e^{2\pi ib}=1,
\]

то есть

\[
b=0\pmod1.
\]

Итак,

\[
\boxed{
g(\cdot+\delta)=g
\Longrightarrow
\delta=0\in\mathbb T^2.
}
\]

Это простой, но важный arithmetic-symmetry obstruction: nonlinear kick не имеет скрытой torus-translation symmetry.

---

## 14. Новая uniform finite-type lemma для off-diagonal \(q\)-shifts

Определим

\[
\Delta_\delta g(q,p)
=
g(q+\delta_q,p+\delta_p)-g(q,p).
\]

Пусть

\[
\delta_q\in[1/7,6/7]\pmod1.
\]

Рассмотрим \(q\)-Fourier mode \(n=-1\).

Его \(m=0\) часть имеет модуль

\[
\frac{\sqrt{101}}{200}
\left|
e^{-2\pi i\delta_q}-1
\right|
\ge
\frac{\sqrt{101}}{100}\sin\frac{\pi}{7}.
\]

Две \(m=\pm1\) поправки имеют суммарный worst-case модуль не более

\[
2\cdot
\frac1{400}
\cdot2
=
\frac1{100}.
\]

Поэтому коэффициент \(n=-1\), рассматриваемый как функция \(p\), удовлетворяет точной нижней оценке

\[
\boxed{
|C_{-1}(p;\delta)|
\ge
c_0
:=
\frac{\sqrt{101}\sin(\pi/7)-1}{100}
}
\]

для всех \(p,\delta_p\).

Численно

\[
c_0\approx0.03360477612158.
\]

Теперь положим

\[
\mathcal D_q
=
\frac1{2\pi}\partial_q
\]

и

\[
P(z)
=
z^2(z-i)
\prod_{n\in\{2,5,6,7,8,9\}}
\left(
1+\frac{z^2}{n^2}
\right).
\]

Этот polynomial annihilator убивает все \(q\)-частоты символа, кроме \(n=-1\).

Действительно,

\[
P(in)=0
\]

для

\[
n=0,1,\pm2,\pm5,\pm6,\pm7,\pm8,\pm9,
\]

а

\[
|P(-i)|
=
\frac43.
\]

Следовательно,

\[
\boxed{
|P(\mathcal D_q)\Delta_\delta g(q,p)|
\ge
\frac43c_0
}
\]

uniformly.

Если

\[
P(z)=\sum_{j=2}^{15}p_jz^j,
\]

то exact coefficient \(\ell^1\)-norm равен

\[
\sum_{j=2}^{15}|p_j|
=
\frac{6409325}{2286144}
\approx2.8035526196.
\]

Отсюда pointwise

\[
\boxed{
\max_{2\le j\le15}
\left|
\mathcal D_q^j
\Delta_\delta g(q,p)
\right|
\ge
\kappa_0,
}
\]

где

\[
\kappa_0
=
\frac{\frac43c_0}
{6409325/2286144}
\approx
0.01598199650.
\]

### Интерпретация

Любой phase difference между двумя состояниями, разделёнными в \(q\) хотя бы на один seven-strip,

\[
d_{\mathbb T}(\delta_q,0)\ge\frac17,
\]

имеет **uniform finite type не выше 15**.

По стандартным finite-type van der Corput / sublevel estimates это даёт polynomial oscillatory cancellation порядка не хуже

\[
\lambda^{-1/15}
\]

для одномерных \(q\)-интегралов с этой фазой и uniform smooth amplitude.

### Критическая оговорка

Для полного quantum kick

\[
K_N=e^{i\tau NA_N}
\]

нельзя просто заменить

\[
K_NT_\delta K_N^{-1}
\]

на умножение фазой

\[
e^{i\tau N\Delta_\delta g}.
\]

Точно имеем лишь

\[
T_\delta^{-1}A_NT_\delta
=
\operatorname{Op}_N(g(\cdot+\delta)),
\]

а

\[
e^{i\tau N A_\delta}
e^{-i\tau NA}
\ne
e^{i\tau N(A_\delta-A)}
\]

из-за commutators.

Поэтому доказанная выше finite-type lemma является **строгим результатом о leading Hamilton–Jacobi action difference**, но ещё не полной one-kick quantum FUP lemma.

Для завершения нужно построить generating function полного canonical commutator loop и показать

\[
\Phi_{\tau,\delta}
=
\tau\Delta_\delta g
+
O_{C^{15}}(\tau^2).
\]

Поскольку \(\tau=10^{-80}\), любой явный \(O(\tau^2)\) bound с разумной константой сохраняет lower bound

\[
\max_{j\le15}
|\partial_q^j\Phi_{\tau,\delta}|
\gtrsim
\tau\kappa_0.
\]

Это один из наиболее конкретных новых технических пунктов для завершения FUP-моста.

---

# Часть III. Weyl-lattice representation

## 15. Exact Weyl representation \(A_N\)

Для достаточно больших нечётных \(N\)

\[
A_N
=
\operatorname{Op}_N(g)
=
\sum_{\kappa\in\Lambda}
\widehat g(\kappa)T_\kappa,
\]

где

\[
|\Lambda|=32.
\]

Weyl multiplication:

\[
T_\kappa T_\nu
=
e_N(h\omega(\kappa,\nu))
T_{\kappa+\nu}
\]

с convention-dependent знаком.

Поэтому

\[
\boxed{
N[A_N,T_\nu]
=
N
\sum_{\kappa\in\Lambda}
\widehat g(\kappa)
\left[
e_N(h\omega(\kappa,\nu))
-
e_N(-h\omega(\kappa,\nu))
\right]
T_{\nu+\kappa}.
}
\]

Таким образом, \(N\,\mathrm{ad}_{A_N}\) — finite-range оператор на Weyl lattice с 32 соседями.

Metaplectic Egorov точно даёт

\[
\operatorname{Ad}_{M_N}T_\nu
=
T_{S\nu}
\]

с возможной заменой \(S\) на \(S^{-1}\) в зависимости от convention.

Следовательно,

\[
\boxed{
\mathcal U_N
=
e^{i\tau N\,\mathrm{ad}_{A_N}}
P_{S,N},
}
\]

где \(P_{S,N}\) — permutation/metaplectic transport Weyl indices.

Это точная finite-dimensional reformulation pair dynamics.

---

## 16. Interaction picture

Положим

\[
K_N=e^{i\tau NA_N}.
\]

Тогда

\[
U_N^m
=
K_{0,N}K_{1,N}\cdots K_{m-1,N}M_N^m,
\]

где

\[
K_{j,N}
=
M_N^jK_NM_N^{-j}
=
e^{i\tau N A_{j,N}},
\]

\[
A_{j,N}
=
\sum_{\kappa\in\Lambda}
\widehat g(\kappa)
T_{S^j\kappa}
\]

с convention-dependent \(S^{\pm j}\).

Это показывает, что nonlinear kick во времени возбуждает экспоненциально растущие hyperbolic Fourier directions.

---

# Часть IV. Smooth-sector theorem

## 17. Fejér suppression микроскопических phase-difference invariants

Пусть \(a\in C^\infty(\mathbb T^2)\) имеет нулевое среднее и

\[
A_N=\operatorname{Op}_N(a).
\]

Определим

\[
Q_{N,C}(a)
=
\frac1N
\sum_{\|\theta_j-\theta_k\|\le C/N}
|\langle\psi_j,A_N\psi_k\rangle|^2.
\]

Берём Fejér kernel

\[
F_M(t)
=
\sum_{|n|<M}
\left(
1-\frac{|n|}{M}
\right)e^{2\pi int},
\]

\[
M=\lfloor c\log N\rfloor.
\]

При

\[
|t|\le C/N
\]

и \(M\ll N\)

\[
F_M(t)\gtrsim M.
\]

Поэтому

\[
Q_{N,C}(a)
\lesssim
\frac1M
\sum_{|n|<M}
\left(
1-\frac{|n|}{M}
\right)
\frac1N
\operatorname{Tr}
\left(
A_N^*U_N^nA_NU_N^{-n}
\right).
\]

Если использовать log-time Egorov и exponential mixing Anosov map для smooth observables, то

\[
\frac1N
\operatorname{Tr}
\left(
A_N^*U_N^nA_NU_N^{-n}
\right)
=
\int
\overline a\,
a\circ f^n
+
o(1)
\]

равномерно для

\[
|n|\le c\log N.
\]

Экспоненциальное mixing и mean-zero дают summable correlation tail, следовательно

\[
\boxed{
Q_{N,C}(a)
=
O_a\!\left(
\frac1{\log N}
\right).
}
\]

### Что это действительно доказывает

Микроскопические phase-difference near-invariants не могут иметь существенную массу в любом **фиксированном smooth observable sector**.

### Чего это не доказывает

Это не bound на число eigenvalue pairs.

Остаётся rough/Planck-scale Hilbert–Schmidt sector — именно там может скрываться obstruction к CUE.

---

# Часть V. Hidden arithmetic failure modes

## 18. Fixed point и Hessian

Точное вычисление:

\[
g(0,0)=\frac9{10},
\]

\[
\nabla g(0,0)=0,
\]

\[
\boxed{
D^2g(0,0)
=
\begin{pmatrix}
-\frac{19606}{125}\pi^2 & 0\\
0&0
\end{pmatrix}.
}
\]

Обозначим

\[
H
=
-\frac{19606}{125}\pi^2
\ne0.
\]

Точка \(0\) остаётся fixed point Hamiltonian kick.

Для classical kick time \(t\ne0\), соответствующего quantum exponential convention,

\[
D\phi_g^t(0)
=
\begin{pmatrix}
1&0\\
-tH&1
\end{pmatrix}
\]

с возможной заменой \(t\mapsto -t\).

При композиции с \(S\)

\[
\operatorname{Tr}D(\phi_g^t\circ S)(0)
=
6-4tH,
\]

или с противоположным знаком времени

\[
6+4tH.
\]

В любом случае для \(t\ne0\)

\[
\operatorname{Tr}Df(0)\ne6.
\]

Поскольку \(C^1\)-conjugacy сохраняет eigenvalues derivative на соответствующих periodic points, perturbed map не может быть \(C^1\)-conjugate к исходному linear cat map.

Это исключает один из наиболее опасных сценариев: «нелинейная» модель на самом деле является скрытой гладкой арифметической conjugate linear model.

---

# Часть VI. Natural quantization и обход Ehrenfest barrier

## 19. Faure–Tsujii: all-time trace formula существует для natural quantization

Для symplectic Anosov diffeomorphism Faure–Tsujii строят prequantum transfer operator и выделяют finite-dimensional outer spectral band.

Спектральное ограничение на этот outer band определяет natural quantum operator

\[
F_\hbar^{\mathrm{nat}}.
\]

Для изолированного outer band их Gutzwiller formula имеет ошибку

\[
\boxed{
\left|
\operatorname{Tr}(F_\hbar^n)
-
\sum_{x=f^nx}
\frac{
e^{D_n(x)}
e^{iS_{n,x}/\hbar}
}{
\sqrt{|\det(I-Df_x^n)|}
}
\right|
\le
C_\varepsilon
N^d
(r_1^++\varepsilon)^n,
}
\]

где

\[
r_1^+<1.
\]

Ключевой момент:

\[
\boxed{
\text{оценка действует для всех }n\ge1.
}
\]

Если

\[
n=cN,
\]

то remainder

\[
N^d(r_1^++\varepsilon)^{cN}
\]

экспоненциально мал.

### Значение

Ehrenfest barrier не является фундаментальным запретом для всех quantizations Anosov map.

Он является барьером стандартного semiclassical propagation, но natural/prequantum construction способен дать all-time periodic-orbit trace formula.

---

## 20. Почему это ещё не решает нашу задачу

Наш оператор

\[
U_N=e^{i\tau NA_N}M_N
\]

— конкретная Weyl/metaplectic quantization.

Natural operator Faure–Tsujii — другой объект.

Их сравнение с geometric/Toeplitz quantization в опубликованной теории даёт лишь small semiclassical error порядка

\[
O(\hbar^\delta)
\]

в operator norm после подходящей идентификации и correction of potential.

Для Heisenberg times этого недостаточно.

Если

\[
\|U_N-V_N\|
\lesssim N^{-\delta},
\]

то при \(m\sim N\)

\[
\|U_N^m-V_N^m\|
\lesssim
N^{1-\delta},
\]

что не является малым при малом \(\delta\).

---

## 21. Нужный all-orders bridge theorem

Достаточно доказать:

> **Bridge theorem \(B_K\).** Для каждого \(K>0\) существуют unitary/isomorphic identifications \(B_N\) и подходящая natural/Toeplitz quantization \(\mathcal F_N\) той же classical map такие, что
>
> \[
> \boxed{
> \|
> B_N^{-1}U_NB_N-\mathcal F_N
> \|
> \le
> C_KN^{-K}.
> }
> \]

Тогда для

\[
m\le CN
\]

\[
\|U_N^m-\mathcal F_N^m\|
\le
CmN^{-K}
=
O(N^{1-K}),
\]

и

\[
\left|
\operatorname{Tr}U_N^m
-
\operatorname{Tr}\mathcal F_N^m
\right|
\le
N\|U_N^m-\mathcal F_N^m\|
=
O(N^{2-K}).
\]

Для fixed all-\(k\) observable worst-case error после summation over \(O(N^{k-1})\) frequencies и нормировки \(N^{-k}\) имеет порядок не хуже

\[
O(N^{k-K}).
\]

Следовательно, arbitrary-order matching автоматически достаточно для любого фиксированного \(k\): выбираем

\[
K>k.
\]

---

## 22. Почему all-orders matching не автоматичен

Работы Laurent Charles дают мощный symbolic calculus для Toeplitz/Fourier integral operators с metaplectic correction, principal/subprincipal symbols и unitary identifications.

Но они не утверждают без дополнительных условий, что **любые** две quantizations одной canonical map на \(\mathbb T^2\) automatically conjugate modulo \(O(N^{-\infty})\).

На несвязно-простой фазовой области возникают global obstructions.

Zelditch показывает, что quantizability symplectic map на torus зависит от сохранения holonomy prequantum connection.

Следовательно, all-orders bridge должен проверить:

1. principal canonical relation;
2. Maslov/metaplectic data;
3. subprincipal cocycle;
4. prequantum holonomy;
5. flat line-bundle class;
6. periodic-orbit/Livšic obstructions на каждом рекурсивном order.

Это конкретная, конечная по структуре задача, а не абстрактная «semiclassical equivalence».

---

# Часть VII. Seven-cut и FUP

## 23. Seven-cut reduction

Имеется seven-cut full propagator \(V_N\), для которого уже установлена trace-norm близость

\[
\boxed{
\|U_N-V_N\|_1
\le
\frac{28\pi^2}{25}
\frac{\tau}{N}.
}
\]

По условию задачи fixed-order microscopic laws для \(U_N\) и \(V_N\) эквивалентны.

В tensor square возникают \(7^2=49\) branch pairs.

Диагональные:

\[
(r,r),\qquad r=0,\dots,6.
\]

Off-diagonal alphabet:

\[
\boxed{
A_7
=
\{(r,s)\in\mathbb Z_7^2:r\ne s\}.
}
\]

В нём 42 symbols.

Каждая строка содержит ровно 6 symbols, каждая колонка — ровно 6.

Поэтому:

\[
\boxed{
A_7\text{ не имеет полной строки и не имеет полной колонки.}
}
\]

---

## 24. Почему это замечательно совпадает с FUP 2026

Jin–Zhang–Zhang, *Anisotropic 2D FUP and quantum open baker's map* (arXiv:2606.23160, 2026), доказывают:

- discrete anisotropic FUP;
- essential spectral gap для 2D anisotropic open baker;
- reduction «FUP \(\Rightarrow\) spectral gap».

В частности, для open baker alphabet \(A\) spectral gap существует, если \(A\) не имеет полной строки **или** не имеет полной колонки.

Наш идеальный off-diagonal alphabet \(A_7\) удовлетворяет условию с большим запасом.

Следовательно:

> **Если doubled seven-cut off-diagonal propagator можно microlocally привести к open-baker normal form с alphabet \(A_7\), то polynomial FUP/spectral gap уже обеспечен существующей теоремой.**

Это, вероятно, самый сильный конкретный structural breakthrough всей текущей работы.

---

## 25. Изотропный Cohen criterion также проходит

Для isotropic discrete 2D Cantor sets Cohen доказал sharp criterion:

\[
\|1_Y\mathcal F1_X\|
\le
CN^{-\beta}
\]

если и только если limiting Cantor sets не содержат пару взаимно ортогональных affine lines.

Для первого seven-grid drawing complement diagonal:

\[
r\ne s.
\]

Любая полная torus line, лежащая в этом drawing, должна иметь direction

\[
(1,1),
\]

поскольку для любого другого direction функция \(q_2-q_1\) меняется вдоль линии и обязательно попадает в diagonal strip.

Limiting set действительно содержит некоторые линии direction \((1,1)\); например offset \(1/2\) устойчив under multiplication by 7 modulo 1.

Но direction

\[
(1,-1)
\]

не содержится.

Поэтому self-pair \(X=Y\) не содержит **orthogonal pair** lines.

Итак, и sharp isotropic Cohen criterion также предсказывает FUP для ideal seven-alphabet model.

---

## 26. Что отсутствует в FUP-мосте

Реальный doubled operator

\[
U_N\otimes\overline{U_N}
\]

не является буквально standard baker matrix.

Необходимо доказать один из двух вариантов.

### Вариант A. Exact/discrete normal form

После seven-cut localization, metaplectic changes of variables и \(L\sim c\log N\) iterations:

\[
\boxed{
\mathcal B_{N,L}
=
E_N
B_{N,L}^{\mathrm{baker}}
F_N
+
O(N^{-\infty})
}
\]

в operator norm, где

- \(E_N,F_N\) uniformly bounded/invertible microlocal FIOs;
- \(B_{N,L}^{\mathrm{baker}}\) — open baker с alphabet \(A_7\) или finite union таких blocks.

Тогда discrete FUP 2026 переносится напрямую.

### Вариант B. Robust continuous FUP

Показать, что stable/unstable projections реального trapped survivor set имеют anisotropic line-porosity, удовлетворяющую continuous FUP hypotheses Jin–Zhang–Zhang или line-porosity Cohen.

Далее локально linearize canonical phase и применить FIO version FUP через metaplectic normal forms и almost orthogonality.

Этот путь менее арифметичен и вероятно устойчив к nonlinear kick.

---

# Часть VIII. Новая геометрия obstruction channels

## 27. Что являются «плохими линиями» в Hilbert–Schmidt picture

В Weyl basis affine line-type concentration соответствует coherent families Weyl translations \(T_\nu\).

Для чистого linear cat map

\[
T_\nu
\mapsto
T_{S\nu}.
\]

Именно поэтому arithmetic line channels могут сохраняться и мешать FUP.

Nonlinear kick действует через

\[
e^{i\tau N\,\mathrm{ad}_{A_N}}.
\]

Из раздела 14 видно, что symbol-level action difference между two macro-separated \(q\)-channels имеет uniform finite type.

То есть nonlinear kick разрушает exact affine degeneracy уже на первом classical action order.

---

## 28. Half-translation как worst-case test

Для

\[
\delta_q=\frac12
\]

phase difference

\[
\Delta(q,p)
=
g(q+\tfrac12,p)-g(q,p)
\]

имеет clean critical manifolds

\[
q=0,\qquad q=\frac12.
\]

На них transverse Hessian равномерно невырожден.

Точное вычисление:

\[
\partial_q^2\Delta(0,p)
\in
\left[
\frac{8744}{25}\pi^2,
\frac{8936}{25}\pi^2
\right],
\]

\[
\partial_q^2\Delta(\tfrac12,p)
\in
\left[
-\frac{8936}{25}\pi^2,
-\frac{8744}{25}\pi^2
\right].
\]

То есть это Morse–Bott, а не flat phase.

Для соответствующего scalar oscillatory integral stationary phase давал бы

\[
O((N\tau)^{-1/2}).
\]

Это ещё один сильный индикатор того, что nonlinear kick действительно уничтожает exact arithmetic line obstruction.

Снова: перенос этого statement на полный operator exponential требует FIO construction.

---

# Часть IX. Почему quantum-graph route не закрывает задачу

Строгие universality results для quantum graphs обычно используют одно или несколько из:

- energy averaging;
- phase averaging;
- incommensurate bond lengths;
- graph ensemble.

Здесь запрещены все такие механизмы.

\(U_N\) — одна фиксированная матрица при одном fixed \(\tau\).

Поэтому quantum-graph analogy полезна структурно, но не предоставляет готового deterministic microscopic theorem.

---

# Часть X. Long-time periodic-orbit bottleneck

## 29. Даже all-time trace formula не даёт CUE автоматически

Предположим all-orders bridge к natural quantization доказан.

Тогда при \(m\sim N\)

\[
p_m
=
\sum_{x\in\operatorname{Fix}(f^m)}
A_m(x)
e^{iS_m(x)/\hbar}
+
O(N^{-\infty}).
\]

Для pair form factor:

\[
|p_m|^2
=
\sum_{x,y\in\operatorname{Fix}(f^m)}
A_m(x)\overline{A_m(y)}
e^{i(S_m(x)-S_m(y))/\hbar}
+\cdots.
\]

Diagonal \(x=y\) должен дать classical sum-rule contribution.

Но остаётся доказать cancellation:

\[
\boxed{
\frac1{N^2}
\sum_m
w(m/N)
\sum_{\substack{x,y\in\operatorname{Fix}(f^m)\\x\ne y}}
A_m(x)\overline{A_m(y)}
e^{i(S_m(x)-S_m(y))/\hbar}
=o(1).
}
\]

Это genuinely hard Heisenberg-scale dynamical exponential-sum theorem.

---

## 30. Twisted transfer operator formulation

Pair problem естественно живёт на product dynamics

\[
F=f\times f
\]

с phase cocycle

\[
\Psi(x,y)
=
S(x)-S(y).
\]

Off-diagonal часть соответствует complement diagonal.

Нужен spectral gap для high-frequency twisted transfer operator вида

\[
\mathcal L_{\lambda}u
=
\sum_{Fz=w}
a(z)
e^{i\lambda\Psi(z)}
u(z),
\qquad
\lambda\asymp N.
\]

Вероятные инструменты:

- Dolgopyat non-integrability;
- anisotropic Banach spaces;
- FUP;
- open-system escape;
- dynamical determinants.

Special explicit symbol \(g\) полезен именно здесь: finite-type lemma даёт concrete transversality/non-flatness constant.

---

# Часть XI. Riemann–Siegel и времена \(m\gtrsim N\)

Finite-dimensional unitarity даёт exact self-inversive identity для characteristic polynomial.

Поэтому spectral determinant можно переписать в exact Riemann–Siegel-lookalike form, где pseudo-orbits длиннее \(N/2\) не являются независимыми.

Работы Braun–Haake показывают, как это организует semiclassical expansion.

Но это не заменяет rigorous control коротких pseudo-orbit sums.

Корректная архитектура выглядит так:

1. prove trace/pseudo-orbit control до \(N/2\);
2. use exact Riemann–Siegel duality для complementary long sector;
3. prove off-diagonal cancellations uniformly after the required smoothing.

---

# Часть XII. Multi-\(k\) geometry

## 31. Partition lattice как partial diagonals

В product phase space \(f^k\) каждому set partition \(\pi\) соответствует partial diagonal:

\[
x_a=x_b
\quad
\text{если }a,b\text{ лежат в одном block }\pi.
\]

Möbius combination

\[
\sum_{\pi}\mu(\pi)\cdots
\]

алгебраически вычитает contributions lower-dimensional collision strata.

Это совпадает с CUE Fourier formula, где lower-cycle terms живут на resonance hyperplanes

\[
\sum_{a\in I}m_a=0.
\]

И совпадает с multi-Fejér geometry, где slow-mixing tuples имеют partial time-sum collisions.

Это не случайность, а сильный structural indication:

\[
\boxed{
\text{partition Möbius inversion}
\leftrightarrow
\text{partial diagonal renormalization}
\leftrightarrow
\text{CUE cycle decomposition}.
}
\]

---

## 32. Multi-Fejér program

На \(k\)-fold tensor space определим

\[
R_a
=
U_N^{(a)}
(U_N^{(k)})^{-1},
\qquad
a=1,\dots,k-1.
\]

Их joint eigenphases:

\[
\theta_{j_a}-\theta_{j_k}.
\]

Product Fejér kernel с

\[
M=c\log N
\]

detects joint microscopic window.

Для smooth tensor observable \(A\), orthogonal к partial diagonals, ожидается bound

\[
\frac{
\|\Pi_{N,C}^{(k-1)}A\|_{HS}^2
}{
N^k
}
\lesssim
\frac1{M^{k-1}}
\sum_{|n_a|<M}
|\mathrm{Corr}(n_1,\dots,n_{k-1})|
+o(1).
\]

Away from hyperplanes

\[
\sum_{a\in I}n_a=0
\]

higher mixing должен давать exponential decay.

Количество lattice points, лежащих на конечном наборе таких hyperplanes в box \(M^{k-1}\), равно

\[
O(M^{k-2}).
\]

Поэтому формально

\[
O(M^{-1})
=
O((\log N)^{-1}).
\]

### Что ещё требуется для строгой версии

Нужно либо:

- получить quantitative higher-order exponential mixing с uniform constants для фиксированного \(k\);
- либо вывести нужную оценку напрямую из Markov/Ruelle spectral gap.

Пока эта часть должна считаться programmatic, а не законченной теоремой.

---

# Часть XIII. Что уже исключено

## 33. Недостаточные критерии

Следующие свойства сами по себе не дают CUE:

- simple spectrum;
- отсутствие нулевых traces;
- macroscopic Haar equidistribution;
- bounded occupancy;
- finite collection Gram moments;
- pair Abel equality;
- log-time trace bounds;
- classical Anosov chaos;
- отсутствие centralizer/reversor;
- tiny gap floor.

Даже полный pair theorem не имплицирует all-\(k\).

---

## 34. Запрещённые shortcuts

Для исходной задачи нельзя использовать:

- \(\tau_N\to0\);
- averaging по \(\tau\);
- random phases;
- random kicks;
- ensemble averaging;
- искусственные independent blocks;
- artificial noise с последующим недоказанным removal;
- редкую subsequence вместо всех \(N\);
- numerical evidence как proof.

---

# Часть XIV. Точная цепочка, которая решила бы задачу

Ниже сформулирован минимальный proof architecture.

## Теорема A. Microlocal doubled seven-cut normal form

Для

\[
L=\lfloor c\log N\rfloor
\]

построить decomposition doubled propagator на diagonal и off-diagonal channels и доказать, что off-diagonal \(L\)-block после uniformly bounded FIO conjugations является smooth perturbation open baker с alphabet

\[
A_7=\{r\ne s\}.
\]

Ошибка:

\[
O(N^{-K})
\]

для произвольного \(K\) или хотя бы достаточно большая polynomial power.

---

## Теорема B. Off-diagonal FUP spectral gap

Используя Jin–Zhang–Zhang 2026 / Cohen / Han–Schlag и finite-type transversality nonlinear kick, доказать

\[
\boxed{
\|\mathcal B_{N,\mathrm{off}}^{L}\|
\le
CN^{-\beta}
}
\]

для некоторого

\[
\beta>0.
\]

---

## Теорема C. Renewal/return decomposition

Показать, что Heisenberg-time Hilbert–Schmidt trace

\[
\operatorname{Tr}_{HS}\mathcal U_N^m
=
|p_m|^2
\]

можно разложить на:

1. universal diagonal return term;
2. words, содержащие off-diagonal blocks;
3. negligible boundary/cut errors.

Теорема B должна подавить пункт 2 после summation по \(m\sim N\).

Тогда получить

\[
N^{-2}
\sum_m
w(m/N)
|p_m|^2
\to
\int
w(x)\min(|x|,1)\,dx.
\]

Это решает pair theorem.

---

## Теорема D. All-\(k\) partition-FUP

На \(k\)-fold product space провести аналогичное open-channel decomposition relative to всех partial diagonals.

После Möbius subtraction lower-partition channels должны cancel exactly.

На fully off-diagonal sector доказать FUP/spectral gap.

Тогда CUE cycle formula раздела 7 должна появиться как единственный surviving combinatorial contribution.

---

## Теорема E. Heisenberg-time completion

Для contributions, доходящих до spectral determinant scale, использовать exact Riemann–Siegel finite-\(N\) duality.

После этого получить для каждого fixed \(k\)

\[
N^{-k}
\sum
W(m/N)
\left[
D_N(m)-\mathbb E_{\mathrm{CUE}}D_N(m)
\right]
\to0.
\]

---

# Часть XV. Альтернативная цепочка через natural quantization

Вторая возможная архитектура:

1. all-orders bridge
   \[
   U_N
   \sim
   F_N^{\mathrm{nat}}
   \mod O(N^{-\infty});
   \]

2. Faure–Tsujii all-time trace formula;

3. rewrite correlation sums as twisted product transfer operators;

4. prove Dolgopyat/FUP high-frequency spectral gap off all partial diagonals;

5. identify surviving diagonal/cycle saddles with exact CUE Fourier benchmark;

6. use Riemann–Siegel completion.

Эта цепочка conceptually cleaner для periodic-orbit theory, но all-orders quantization bridge — сам по себе серьёзная задача.

---

# Часть XVI. Что считать реальным прорывом текущей работы

На данный момент наиболее существенны следующие пункты.

### 1. Ehrenfest barrier перестал быть абсолютным

Natural quantization Faure–Tsujii даёт all-time trace formula с exponentially decaying-in-time remainder.

Значит основная проблема не «невозможно дойти до \(m\sim N\)», а «как связать наш конкретный \(U_N\) с all-time quantization и как доказать cancellation exponentially many orbits».

### 2. Seven-cut off-diagonal alphabet попадает точно под FUP 2026

\[
A_7=\{r\ne s\}
\]

не имеет полной строки и колонки.

Именно такой combinatorial condition даёт spectral gap для 2D open baker в theorem Jin–Zhang–Zhang 2026.

### 3. Nonlinear kick имеет явную uniform finite-type transversality

Для любого macro-separated seven-strip \(q\)-shift:

\[
\max_{2\le j\le15}
|\mathcal D_q^j\Delta_\delta g|
\ge
0.01598\ldots
\]

uniformly.

Это конкретное количественное разрушение affine arithmetic channel.

### 4. Hidden smooth conjugacy к linear cat исключена

Fixed-point multiplier меняется при любом ненулевом kick time.

### 5. All-\(k\) CUE benchmark полностью организуется partitions/cycles

Это даёт точную combinatorial target geometry для product-space FUP.

---

# Часть XVII. Самокритика и места, где нельзя перепрыгнуть доказательство

## 35. Нельзя объявлять one-kick FUP из \(\Delta g\)

Ошибка была бы в тождестве

\[
e^{i\tau N A_\delta}
e^{-i\tau NA}
\stackrel{\text{false}}=
e^{i\tau N(A_\delta-A)}.
\]

Это неверно.

Нужен настоящий Hamilton–Jacobi/FIO expansion.

---

## 36. Нельзя считать Toeplitz/natural equivalence all-orders автоматически

Из опубликованного \(O(\hbar^\delta)\) comparison не следует Heisenberg-time transfer.

Нужно рекурсивно решить symbol matching и global holonomy/Livšic obstructions.

---

## 37. Нельзя заменить fixed-map theorem semiclassical diagrammatics

Müller–Novaes дают глубокое all-orders cancellation в unitary-class semiclassical diagrammatics, но это не uniform rigorous estimate для одной фиксированной карты.

Их combinatorics следует использовать как target, не как proof.

---

## 38. Нельзя переносить quantum-graph universality без averaging theorem

Energy/phase averaging — существенная часть известных graph proofs.

---

# Часть XVIII. Конкретный список следующих доказательств

## 39. FIO finite-type completion

Построить classical commutator map

\[
\chi_{\tau,\delta}
=
T_{-\delta}
\circ
\phi_g^\tau
\circ
T_\delta
\circ
\phi_g^{-\tau}.
\]

Его generating action должна удовлетворять

\[
\Phi_{\tau,\delta}
=
\tau\Delta_\delta g
+
O_{C^{15}}(\tau^2).
\]

Требуется explicit bound

\[
\|O(\tau^2)\|_{C^{15}}
\le
C_*
\tau^2
\]

с

\[
C_*\tau
<
\kappa_0/2.
\]

При \(\tau=10^{-80}\) допустим даже

\[
C_*<10^{78}.
\]

Для нашего trigonometric polynomial symbol ожидаемые constants на много порядков меньше.

После этого finite-type oscillatory estimate становится строгим для полного canonical commutator.

---

## 40. Torus FIO quantization lemma

Доказать uniform kernel representation

\[
T_\mu^*
K_NT_\delta K_N^*
T_\nu
\]

как finite sum oscillatory integrals с phase \(\Phi_{\tau,\delta,\mu,\nu}\) и amplitudes uniform in \(N\).

Finite type \(\le15\) должно дать

\[
|\langle T_\mu,K_NT_\delta K_N^*\rangle_{HS}|
\le
C_\tau N^{-\eta},
\]

для некоторого

\[
\eta>0.
\]

Наивный finite-type exponent:

\[
\eta\approx\frac1{15},
\]

хотя после clean stationary phase на generic channels он должен быть лучше.

---

## 41. Log-block propagation of the line gap

Показать, что \(L=c\log N\) последовательных hyperbolic/FIO steps превращают one-step polynomial line leakage в open-system spectral gap.

Именно здесь следует использовать FUP, а не перемножать individual matrix-element bounds вручную.

---

## 42. Seven-cut FUP normal form

Нужно построить explicit symbolic coding branch pairs и доказать anisotropic porosity survivor sets.

Для alphabet \(A_7\) combinatorics уже оптимальна:

\[
\text{no full row},
\qquad
\text{no full column}.
\]

---

## 43. Pair renewal identity

Нужна точная operator identity, которая связывает

\[
\operatorname{Tr}_{HS}\mathcal U_N^m
\]

с sums over first-return words к diagonal channel.

Идеальная форма должна быть аналогом renewal equation:

\[
\mathcal U^m
=
\text{diagonal returns}
+
\sum
\text{off-diagonal excursions}.
\]

FUP gap подавляет long excursions.

Universal diagonal combinatorics должна породить

\[
\min(m,N).
\]

Это, вероятно, самый прямой путь к pair theorem, не требующий полного periodic-orbit enumeration.

---

## 44. Higher-\(k\) renewal/partition identity

Для каждого partition \(\pi\):

- partial diagonal sector;
- excursion operator away from that sector;
- Möbius cancellation между nested partitions.

Цель — получить finite-\(N\) cycle expansion, асимптотически совпадающий с exact CUE formula раздела 7.

---

# Часть XIX. Литературные опоры

Ниже только те источники, роль которых была проверена по содержанию.

1. **F. Faure, M. Tsujii**,  
   *Prequantum transfer operator for symplectic Anosov diffeomorphism*,  
   arXiv:1206.0282.  
   Band structure, natural quantum operator, exact Egorov-type framework, all-time Gutzwiller trace formula with exponentially small-in-time remainder.

2. **A. Cohen**,  
   *Fractal uncertainty for discrete two-dimensional Cantor sets*,  
   arXiv:2206.14131.  
   Sharp 2D discrete FUP criterion: единственные obstructions — orthogonal affine lines.

3. **A. Cohen**,  
   *Fractal uncertainty in higher dimensions*,  
   arXiv:2305.05022.  
   Higher-dimensional line-porosity FUP.

4. **R. Han, W. Schlag**,  
   *A higher dimensional Bourgain–Dyatlov fractal uncertainty principle*,  
   arXiv:1805.04994, Analysis & PDE 13 (2020).  
   FUP для Fourier supports, покрываемых products of 1D regular sets; устойчивость к controlled diffeomorphic distortion.

5. **L. Jin, A. Zhang, H. Zhang**,  
   *Anisotropic 2D FUP and quantum open baker's map*,  
   arXiv:2606.23160 (2026).  
   Anisotropic discrete/continuous FUP и spectral gap open baker. Особенно важно условие отсутствия full row/full column.

6. **S. Dyatlov, M. Zworski**,  
   *Fractal uncertainty for transfer operators*,  
   arXiv:1710.05430.  
   FUP как spectral-gap mechanism для nonlinear transfer-operator dynamics.

7. **L. Charles**,  
   *Semi-Classical Properties of Geometric Quantization with Metaplectic Correction*,  
   arXiv:math/0602168.  
   Fourier integral/Toeplitz symbolic calculus, principal/subprincipal symbols, unitary semiclassical identifications.

8. **S. Zelditch**,  
   *Quantum maps and automorphisms*,  
   arXiv:math/0307175.  
   Toeplitz quantum maps, holonomy obstruction, quantizability on non-simply-connected phase spaces, torus examples.

9. **P. Braun, F. Haake**,  
   *Chaotic maps and flows: exact Riemann–Siegel lookalike for spectral fluctuations*,  
   arXiv:1206.4222.  
   Exact finite-dimensional self-inversive/Riemann–Siegel mechanism; semiclassical correlation analysis.

10. **S. Müller, M. Novaes**,  
    *Full perturbative calculation of spectral correlation functions for chaotic systems in the unitary symmetry class*,  
    arXiv:1807.10186.  
    All-orders semiclassical unitary-class cancellation within diagrammatic framework.

---

# Часть XX. Итог

Полная задача пока не закрыта, но область неопределённости резко сузилась.

Раньше главный барьер выглядел как неопределённое:

> «нужно каким-то образом контролировать квантовую систему до времени \(N\)».

После проведённого анализа он разделился на конкретные теоремы:

\[
\boxed{
\text{doubled seven-cut FIO}
\longrightarrow
\text{open-baker/anisotropic-FUP normal form}
}
\]

и затем

\[
\boxed{
\text{off-diagonal spectral gap}
\longrightarrow
\text{Heisenberg-time trace renewal}
\longrightarrow
\text{CUE}.
}
\]

Для первого перехода уже имеются:

- ideal alphabet \(A_7\), удовлетворяющий sharp FUP hypotheses;
- explicit 2026 open-baker spectral-gap theorem;
- отсутствие translation symmetry;
- uniform finite-type \(15\) transversality конкретного nonlinear symbol;
- Anosov hyperbolicity;
- seven-cut decomposition.

Для второго перехода уже имеются:

- exact Hilbert–Schmidt encoding
  \[
  \operatorname{Tr}_{HS}\mathcal U_N^m=|p_m|^2;
  \]
- exact Abel-resolvent identity;
- exact CUE all-\(k\) Fourier benchmark;
- partition/Möbius geometry;
- Riemann–Siegel finite-\(N\) completion mechanism.

Самый важный недоказанный объект теперь можно сформулировать без расплывчатости:

> **Нужно построить rigorous first-return / excursion expansion doubled seven-cut propagator relative to the diagonal symbolic channel и доказать polynomial FUP spectral gap для каждого off-diagonal excursion block.**

Если этот pair-level theorem будет доказан, weighted CUE pair law выглядит достижимой без новой «магии» на масштабе \(N\).

Для полного all-\(k\) остаётся сделать его partition-valued version; точная CUE cycle formula уже показывает, какой combinatorial answer должен появиться.

---

## Приложение A. Полный список ненулевых Fourier coefficients \(g\)

При convention

\[
\widehat g(n,m)
=
\int_0^1\int_0^1
g(q,p)e^{-2\pi i(nq+mp)}\,dq\,dp
\]

ненулевые коэффициенты:

### \(m=0\)

\[
\widehat g(-9,0)=-\frac{i}{800},
\]

\[
\widehat g(-8,0)=-\frac1{40}-\frac{i}{400},
\]

\[
\widehat g(-7,0)=\frac9{20},
\]

\[
\widehat g(-6,0)=-\frac1{40}+\frac{i}{400},
\]

\[
\widehat g(-5,0)=\frac{i}{800},
\]

\[
\widehat g(-2,0)=\frac{i}{400},
\]

\[
\widehat g(-1,0)=\frac1{20}+\frac{i}{200},
\]

\[
\widehat g(1,0)=\frac1{20}-\frac{i}{200},
\]

\[
\widehat g(2,0)=-\frac{i}{400},
\]

\[
\widehat g(5,0)=-\frac{i}{800},
\]

\[
\widehat g(6,0)=-\frac1{40}-\frac{i}{400},
\]

\[
\widehat g(7,0)=\frac9{20},
\]

\[
\widehat g(8,0)=-\frac1{40}+\frac{i}{400},
\]

\[
\widehat g(9,0)=\frac{i}{800}.
\]

### \(m=1\)

\[
\widehat g(-8,1)=\frac3{4000}+\frac{i}{1000},
\]

\[
\widehat g(-7,1)=-\frac3{2000}-\frac{i}{500},
\]

\[
\widehat g(-6,1)=\frac3{4000}+\frac{i}{1000},
\]

\[
\widehat g(-1,1)=\frac3{2000}+\frac{i}{500},
\]

\[
\widehat g(0,1)=-\frac3{1000}-\frac{i}{250},
\]

\[
\widehat g(1,1)=\frac3{2000}+\frac{i}{500},
\]

\[
\widehat g(6,1)=\frac3{4000}+\frac{i}{1000},
\]

\[
\widehat g(7,1)=-\frac3{2000}-\frac{i}{500},
\]

\[
\widehat g(8,1)=\frac3{4000}+\frac{i}{1000}.
\]

### \(m=-1\)

\[
\widehat g(-8,-1)=\frac3{4000}-\frac{i}{1000},
\]

\[
\widehat g(-7,-1)=-\frac3{2000}+\frac{i}{500},
\]

\[
\widehat g(-6,-1)=\frac3{4000}-\frac{i}{1000},
\]

\[
\widehat g(-1,-1)=\frac3{2000}-\frac{i}{500},
\]

\[
\widehat g(0,-1)=-\frac3{1000}+\frac{i}{250},
\]

\[
\widehat g(1,-1)=\frac3{2000}-\frac{i}{500},
\]

\[
\widehat g(6,-1)=\frac3{4000}-\frac{i}{1000},
\]

\[
\widehat g(7,-1)=-\frac3{2000}+\frac{i}{500},
\]

\[
\widehat g(8,-1)=\frac3{4000}-\frac{i}{1000}.
\]

Итого \(14+9+9=32\) мод.

---

## Приложение B. Минимальный checklist перед заявлением полного доказательства

Полное решение можно объявлять только после строгой проверки всех пунктов:

- [ ] FIO normal form полного kick, а не только leading phase.
- [ ] Uniform finite-type/nonrefocusing estimate с явными constants при \(\tau=10^{-80}\).
- [ ] Microlocal reduction doubled seven-cut off-diagonal block к классу, покрытому доказанным FUP.
- [ ] Operator norm spectral gap uniform in \(N\).
- [ ] First-return/renewal identity для HS trace.
- [ ] Контроль cut-boundary errors после \(m=\Theta(N)\) summation.
- [ ] Получение полного pair benchmark \(\min(m,N)\), включая \(m>N\).
- [ ] Riemann–Siegel completion без semiclassical averaging.
- [ ] Partition-valued extension для fixed arbitrary \(k\).
- [ ] Uniform control resonance hyperplanes.
- [ ] Exact identification surviving cycle terms с CUE formula.
- [ ] No hidden averaging/randomization anywhere.
- [ ] All estimates valid для всей sequence odd \(N\) в требуемом диапазоне, а не только subsequence.

До выполнения этого checklist результат следует описывать как **rigorous partial progress + sharply formulated reduction**, а не как доказанную BGS/CUE universality.
