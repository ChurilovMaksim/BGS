# Mesoscopic initial regularity from the existing logarithmic trace window

**Claim ID: BGS-FM-017.** Corollary of the maintained FM-007 trace input,
4 October 2026. This is not a new logarithmic-time Egorov theorem or a
microscopic local law. The fixed operator and coupling are unchanged.

## 1. Finite estimate and actual initial spectrum

For a unitary $A$ of dimension $N$, write
$m_j=N^{-1}\operatorname{Tr}A^j$ and, for $|z|<1$,

$$
H_A(z)=N^{-1}\operatorname{Tr}[(A+z)(A-z)^{-1}].
$$

Suppose $|m_j|\le d$ for $1\le j\le J$. For every $g>0$,

$$
\sup_{|z|\le e^{-g}}|H_A(z)-1|
\le B(J,d,g):=\frac{2[d+e^{-(J+1)g}]}{1-e^{-g}}.
\tag{M1}
$$

Indeed the absolutely convergent series is
$H_A(z)=1+2\sum_{j\ge1}\overline m_jz^j$.
Bound the first $J$ coefficients by $d$ and the remaining ones by one.
No uncontrolled truncation of a boundary resolvent is used.

Let $A=U_N$ be the actual frozen odd-dimensional map at $\tau=10^{-80}$.
FM-007 (9) supplies $J_N=\lfloor c\log N\rfloor$ and
$d_N=C N^{-1/40}$, with fixed model-dependent $c,C>0$.
For $J_N\ge3$, put

$$
g_N=\frac{4\log J_N}{J_N}.
\tag{M2}
$$

Then $g_N\to0$, $Ng_N\to\infty$, and (M1) tends to zero uniformly
for all $|z|\le e^{-g_N}$. For instance, when $g_N\le1$,
$1-e^{-g_N}\ge g_N/2$, and its two contributions are bounded by
$4C N^{-1/40}/g_N$ and $4J_N^{-4}/g_N$.

The Poisson-smoothed angular density is
$\rho_{N,\eta}(\theta)=(2\pi)^{-1}\Re H_{U_N}(e^{-\eta+i\theta})$.
Consequently

$$
\sup_{\eta\ge g_N,\theta}
|2\pi\rho_{N,\eta}(\theta)-1|\longrightarrow0.
\tag{M3}
$$

This supplies a density bounded above and below at the stated logarithmic
scales. It says nothing about $\eta\asymp1/N$, individual gaps, or the
signed factorial hierarchy.

## 2. Exact reference centering and smooth control

FM-013 gives $|p_1|+|p_2|<20$ eventually. The FLOW-009 centering
$\Pi(U_N)=M_w(U_N)$ therefore has $|w|\le160/N$.
For $|w|\le1/2$, $M_w(\zeta)=(\zeta-w)/(1-\bar w\zeta)$ satisfies
$|M_w(\zeta)-\zeta|\le4|w|$ on the unit circle. Thus its angular
displacement is at most $2\pi|w|\le C/N$.
For every integer $j\ge1$,

$$
|m_j(\Pi U_N)-m_j(U_N)|\le Cj/N.
$$

Summing the series gives the finite stability bound

$$
\sup_{|z|\le e^{-g}}|H_{\Pi U_N}(z)-H_{U_N}(z)|
\le \frac{C e^{-g}}{N(1-e^{-g})^2}.
\tag{M4}
$$

In particular (M3) also holds for the **exact** initial matrix of
FLOW-012's reference Dyson process. The centering adds only
$O(1/(Ng_N^2))$, which vanishes.

For each fixed $r\ge0$ and $0<g\le1$, differentiating in the angular
variable gives, with a constant depending only on $r$,

$$
\sup_{\eta\ge g,\theta}
|\partial_\theta^r(H_{\Pi U_N}(e^{-\eta+i\theta})-1)|
\le C_r\left[
\frac{d_N+e^{-J_Ng/2}}{g^{r+1}}+
\frac1{Ng^{r+2}}\right].
\tag{M5}
$$

For the tail use $e^{-jg}\le e^{-J_Ng/2}e^{-jg/2}$ when $j>J_N$;
the sum of $j^re^{-jg/2}$ is at most $C_rg^{-(r+1)}$.
The centering term uses the sum of $j^{r+1}e^{-jg}$.
At $\widetilde g_N=J_N^{-1/2}$ the right side vanishes for every
fixed $r$. No assertion uniform in a growing derivative order is made.

## 3. A viable slower comparison scale and its exact boundary

Take $t_N=\sqrt{g_N}$, $\varepsilon_N=N^{-10}$ and
$n_N=\lfloor2t_NN^{40}\rfloor$. Eventually $1/N\le t_N\le1/12$.
FLOW-012 gives, for every fixed nonnegative compact smooth $f$,

$$
|\mathbb E\Phi_{N,f}(U_{n_N}^{\varepsilon_N})
-\mathbb E\Phi_{N,f}(D_{t_N}[\Pi U_N])|
\le C_f g_N^{1/4}+o(1)\longrightarrow0.
\tag{M6}
$$

The initial Poisson regularity scale obeys $g_N/t_N\to0$.
This is a concrete hypothesis and time separation for a circular
relaxation route, not proof of that route within this claim.
The separate [FLOW-014 argument](circular_dyson_actual_start.md) supplies
the required full kernel analysis, also at the sharper $t_N=8g_N$.
Real-line Dyson theorems are not invoked by replacing cotangents by
reciprocals. Nor does (M6) compare the final noisy spectrum with the
deterministic initial spectrum.

At the faster $t_N=N^{-2/3}$, even the **whole FM-007-type logarithmic
trace bound** is insufficient as an abstract hypothesis. Apply FLOW-013's
construction to this schedule: $Q_N\asymp N^{1/10}$ exceeds every
$c\log N$, and its balanced-multiplicity proof gives
$|p_j|\le2\pi j+O(j/N^3)$ for all $1\le j<Q_N$.
Hence $|p_j|\le C N^{39/40}$ throughout $1\le j\le c\log N$,
while its Dyson local limit at $N^{-2/3}$ is empty.
This does not identify the actual frozen spectrum with that falsifier.

## 4. Local stationary points for a direct heat-kernel route

There is a further analytic consequence at the slower $t=t_N=\sqrt{g_N}$.
Let $A=\Pi U_N$ have angles $\alpha_j$ and, locally off the real axis,
define the phase

$$
\mathcal S_N(\zeta;\theta)=\frac{(\zeta-\theta)^2}{2t}
+\frac1N\sum_{j=1}^N\log\!\left[2\sin\frac{\zeta-\alpha_j}{2}\right].
\tag{M7}
$$

Any local analytic branches give the same derivatives. This is a phase
calculation, not an assertion that its local expansion evaluates a
full correlation integral. Set

$$
E_N=B(J_N,d_N,t/4)+\frac{C e^{-t/4}}{N(1-e^{-t/4})^2}\to0.
$$

For every real $\theta$, each disk of radius $t/8$ about
$\theta\pm it/2$ contains a unique stationary point $\zeta_\pm$.
Uniformly in $\theta$,

$$
|\zeta_\pm-(\theta\pm it/2)|\le tE_N/2,
\qquad |t\mathcal S_N''(\zeta_\pm;\theta)-1|\le8E_N.
\tag{M8}
$$

To prove this, put $F_N(\zeta)=H_A(e^{i\zeta})$. The cotangent identity
gives $\mathcal S_N'=(\zeta-\theta)/t-iF_N(\zeta)/2$.
In the upper strip $\Im\zeta\ge t/4$, (M1),(M4) imply
$|F_N-1|\le E_N$; in the lower strip $\Im\zeta\le-t/4$, reflection
$F_N(\bar\zeta)=-\overline{F_N(\zeta)}$ gives $|F_N+1|\le E_N$.
Every point in either disk has a radius-$t/16$ analytic neighborhood
inside the corresponding strip. Cauchy's derivative estimate there is
$|F_N'|\le16E_N/t$.
For sufficiently large $N$, $E_N<1/16$; the map
$\zeta\mapsto\theta+itF_N(\zeta)/2$ maps each closed disk into itself
and contracts it by at most $8E_N<1/2$. Its fixed point proves both
the uniqueness inside that disk and (M8).
Zeros of the sine factors lie on the real axis, so the required local
logarithms exist, including for repeated eigenvalues.

## 5. Uniform vertical tails of the unweighted phase

Write the branch-independent real potential and action as

$$
q_N(\theta,y)=\frac1N\sum_j\log\left|2\sin
\frac{\theta+iy-\alpha_j}{2}\right|,
\qquad a_N(\theta,y)=-\frac{y^2}{2t}+q_N(\theta,y).
$$

At real zeros set $q_N=-\infty$. For $y>0$, the exact determinant
identity and its absolutely convergent series give

$$
q_N(\theta,y)=\frac y2-
\Re\sum_{j\ge1}\frac{\overline{m_j(A)}}j e^{-jy+ij\theta},
\qquad q_N(\theta,-y)=q_N(\theta,y).
$$

For $g=g_N$, $d=d_N$, $J=J_N$, set

$$
v_N=d\log\frac1{1-e^{-g}}+
\frac{e^{-(J+1)g}}{(J+1)(1-e^{-g})}
+\frac{C e^{-g}}{N(1-e^{-g})}.
\tag{M9}
$$

The last term retains the exact centering. Splitting the series at $J$
and using $|m_j(\Pi U_N)-m_j(U_N)|\le Cj/N$ proves
$|q_N(\theta,y)-|y|/2|\le v_N$ for $|y|\ge g$, uniformly in $\theta$.
At the stated $g$, $v_N=O(d_N\log J+J^{-4}/\log J+J/(N\log J))$,
so $v_N/t\to0$ for $t=\sqrt g$.

The real part of the Herglotz transform is positive in the disk.
Hence $\partial_y q_N(\theta,y)=\Re F_N(\theta+iy)/2>0$ for $y>0$,
and $q_N(\theta,y)\le q_N(\theta,g)\le g/2+v_N$ for $|y|\le g$.
This includes boundary zeros by their limiting value; no lower gap is used.
Eventually $g\le t/8$ and $v_N\le t/512$. Then

$$
\sup_{|y|\le t/4}
[a_N(\theta,y)-a_N(\theta,t/2)]\le-t/64,
\tag{M10a}
$$

$$
a_N(\theta,y)-a_N(\theta,t/2)
\le-\frac{(|y|-t/2)^2}{4t},
\quad |y|\ge t/4,\quad \bigl||y|-t/2\bigr|\ge t/8.
\tag{M10b}
$$

Indeed for $g\le|y|\le t/4$, the action is at most
$|y|/2-y^2/(2t)+v_N\le3t/32+v_N$.
For $|y|\le g$ it is at most $g/2+v_N\le t/16+v_N$.
The reference action is at least $t/8-v_N$, proving (M10a).
For $|y|\ge t/4$, subtraction gives
$-(|y|-t/2)^2/(2t)+2v_N$; the stated lower distance and
$v_N\le t/512$ give (M10b).

Let $T_N=\{y:||y|-t/2|\ge t/8\}$ be the complement of the two
stationary neighborhoods on the vertical line. Integrating (M10), for
some absolute $c,C>0$, gives

$$
\int_{T_N}e^{N a_N(\theta,y)}\,dy
\le C\sqrt{t/N}\,
e^{N a_N(\theta,t/2)-cNt}.
\tag{M11}
$$

The central part has length $t/2$ and its barrier is $Nt/64$.
The two remaining Gaussian tails have distance at least $t/8$;
their rescaled integrals are bounded by $C\sqrt{t/N}e^{-cNt}$.
Since $Nt\to\infty$, the central prefactor is absorbed by decreasing $c$.
All bounds are uniform in $\theta$ and allow repeated levels.

(M11) controls an **unweighted phase integral only**. It is not a bound
on the complete resummed kernel, its initial-gap denominators, a joint
contour's crossing poles or a Fredholm series. The
[kernel route record](../record/circular_kernel_route_20261004.md)
credits the prior arbitrary-start formula. Complete contour/amplitude
control and microscopic Fredholm convergence are separate obligations
from (M11), closed in FLOW-014. Deterministic noise removal remains open.

The elementary Poisson transform and phase estimates are project
corollaries; FM-007 owns the logarithmic trace input. Priority is not asserted.
Actual-start circular relaxation, deterministic noise removal,
BGS-TRACE-005 and BGS-BGS-001 remain open.
