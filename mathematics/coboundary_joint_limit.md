# A simultaneous limit for uncentered Gaussian coboundary kicks

**Claim ID: BGS-FLOW-010.** Project proof and author self-review,
30 September 2026. No independent review, formal certificate, practical
simulation claim or priority determination.

## 1. Statement and boundary

Use precisely the uncentered chain (1) of
[FLOW-009](coboundary_mobius_diffusion.md), with independent normalized
GUE matrices, odd dimension $N\ge3$ and clock initial matrix $C_N$.
Write $h=\varepsilon^4/2$, $n=\lfloor t/h\rfloor$, and use the same
uniform-origin local Laplace functional $\Phi_{N,f}$.

There exist absolute constants $C,\varepsilon_0>0$ such that, for
$0\le f\in C_c^\infty(\mathbb R)$, $0<\varepsilon\le\varepsilon_0$,
$1/N\le t\le1/12$,

$$
\left|\mathbb E\Phi_{N,f}(U_n^\varepsilon)
                  -\Phi_{\mathrm{Sine}}(f)\right|
\le C_f\left[\sqrt t+\frac1{Nt}+\frac1{N^2}
                     +N^{20}e^{CNt}\varepsilon\right]. \tag{1}
$$

The exponent 20 is a loose bookkeeping bound, not an optimal exponent.
In particular, if $t_N\to0$, $Nt_N\to\infty$ and
$\varepsilon_N=e^{-N}$, the left side tends to zero in a **single joint
limit**. With $t_N=N^{-2/3}$ its order is $O_f(N^{-1/3})$.
Nonnegative $C_c^1$ tests have the joint limit, without the stated
smooth-test rate, by approximation in $L^1$.

This replaces the order-of-limits restriction for one explicit random
model. Its step count is of order $t_Ne^{4N}$ and is not computationally
practical. It does not prove a polynomial step-size regime, relaxation
from the deterministic frozen spectrum, or removal of external noise.
The BGS-TRACE-005 and BGS-BGS-001 obligations remain open.

## 2. Uniform Gaussian bounds and the fast coordinate

Here and below constants $C_k$ may depend on a fixed derivative or moment
order but not on $N$. Normalized GUE has
$\mathbb E\|G\|_{\rm op}^k\le C_k$.
One direct proof uses a $1/4$-net of the complex unit sphere, of cardinality
at most $9^{2N}$, and the real Gaussian variable $v^*Gv$, of variance
$1/N$. The quadratic-form net inequality gives
$\mathbb P(\|G\|_{\rm op}>r)\le
2\exp(2N\log9-Nr^2/8)$; for a sufficiently large absolute $r$,
integration proves the asserted uniform moments.

Put $x=m_1(U)$. For the actual step define
$\psi_U(G)=N^{-1}\operatorname{Tr}(e^{i\varepsilon(G-UGU^*)}U)$.
The linear coefficient is identically zero, since
$\operatorname{Tr}(G-UGU^*)U=0$. Differentiating the exponential by
Duhamel, the gradient consists of an averaged matrix
$A_s-U^*A_sU$, where $A_s=U+O_{\rm HS}
(\varepsilon\sqrt N\|G\|_{\rm op})$.
The contribution at $A_s=U$ cancels. Consequently

$$
\|D_G\psi_U\|_{\rm HS}\le
C\varepsilon^2\|G\|_{\rm op}/\sqrt N. \tag{2}
$$

For completeness the Gaussian centered-moment inequality needed here
does not require a dimension-dependent Lipschitz constant. If $G'$ is
independent, integrate the derivative of
$\psi(\cos s\,G+\sin s\,G')$, $0\le s\le\pi/2$.
Its Gaussian velocity is independent of its position and has covariance
$I/N$ in the real Hermitian Hilbert space. Conditional Gaussian moments,
Minkowski and Jensen give

$$
\|\psi(G)-\mathbb E\psi(G)\|_{L^k}
\le C_kN^{-1/2}\|D\psi(G)\|_{L^k({\rm HS})}.
$$

Apply this to real and imaginary parts of (2). Uniformly in every $U$,

$$
\|\psi_U-\mathbb E\psi_U\|_{L^k}
\le C_k\varepsilon^2/N. \tag{3}
$$

The uniform sixth-order Taylor remainder for the normalized trace follows
directly from the original single exponential: its $j$th derivative is
bounded by $(2\|G\|_{\rm op})^j$ and odd expected orders vanish.
FLOW-008 and the first-trace drift in FLOW-004 therefore yield

$$
\mathbb E\psi_U=x-\frac{\varepsilon^2}{2}
                       (x-\bar x q)
                 +\varepsilon^4 P_4(x,q,r)+O(\varepsilon^6),
\quad q=m_2,\ r=m_3,
\qquad
P_4=\frac{x}{8}-\frac{q\bar x}{6}
 +\frac{|q|^2x-|x|^2x+\bar x^2r}{24}. \tag{4}
$$

To check the fourth coefficient independently, it is
$N^{-1}\operatorname{Tr}((\mathbb EL_4)U)
+L_Xm_1/2-N^{-1}\operatorname{Tr}(J^2U)/2$.
Substituting FLOW-008 and FLOW-004 gives the displayed $P_4$;
equivalently it is $\mathbb E\operatorname{Tr}((G-UGU^*)^4U)/(24N)$.
In particular $|P_4|\le C|x|$. Thus the constants in (4) are uniform.
The sixth remainder is retained as an absolute error; no divisibility
of all higher coefficients by $m_1$ is assumed.

When $|m_2|\le3/4$, (4) contracts $|x|$ by $1-c\varepsilon^2$,
up to $C\varepsilon^6$, for an absolute small $\varepsilon_0$.
Expand $|\mathbb E\psi_U+\xi|^{2p}$ with
$\mathbb E\xi=0$, use (3), and absorb each remaining term with Young's
inequality. This gives

$$
\mathbb E(|m_1(U_{j+1})|^{2p}\mid U_j)
\le(1-c_p\varepsilon^2)|m_1(U_j)|^{2p}
 +C_p\left(\frac{\varepsilon^{2p+2}}{N^{2p}}
                         +\varepsilon^{8p+2}\right). \tag{5}
$$

For the noise terms of degree $k\ge2$, the absorption remainder is at
most $C_p\varepsilon^{2p+2}/N^{2p}$; the deterministic forcing
$C\varepsilon^6$ has equilibrium size $\varepsilon^4$, giving the
second term. Killing at any of the exits below and starting at $m_1=0$
therefore gives

$$
\mathbb E[|m_1(U_j)|^{2p};j<\sigma]
\le C_p\left[(\varepsilon/N)^{2p}+\varepsilon^{8p}\right]. \tag{6}
$$

The uniform first-moment scale is
$\rho=\varepsilon/N+\varepsilon^4$. For $T\le1$, a union bound over
at most $2T\varepsilon^{-4}+1$ steps, using the conditional estimate at
the last pre-exit point, bounds an exit through
$|m_1|=a=1/1024$ by

$$
C(T+1)(\varepsilon^2/N^6+\varepsilon^{20}). \tag{7}
$$

## 3. A dimension-controlled weak expansion

Work in the same centering chart as FLOW-009. Stop when the centered
$|m_2|$ reaches $q_*=2/5$, or $|m_1|$ reaches $a$.
Before stopping, the original $|m_2|$ is below $3/4$.
For a smooth conjugation- and rotation-invariant function $F$ on the
centered slice, let $\widetilde F=F\circ\Pi$ in this chart.
The fast coefficient $D_J\widetilde F$ is exactly zero.
Denote by $\|F\|_k$ the ambient real Hilbert--Schmidt $C^k$ norm of a
smooth extension near the slice, including its sup norm.

Uniformly on a slightly larger chart, the inverse trace equation has
$\|D^j w\|\le C_j/\sqrt N$ for $j\ge1$, and
$\|D^j\Pi\|_{\rm HS}\le C_j$ for fixed $j\ge1$.
Indeed $D^j m_1$ after the polar-unitary extension is bounded by
$C_j/\sqrt N$; the real inverse of $w\mapsto w-m_2\bar w$
is uniformly bounded, and repeated implicit differentiation gives the
first estimate. In differentiating $\Pi$, each apparently large factor
$\|U^r\|_{\rm HS}=\sqrt N$ is paired with a derivative of $w$.
Also $\|U-\Pi U\|_{\rm HS}\le C\sqrt N|m_1|$.

The quartic coefficient at a centered point is
$\overline LF=L_X(F\circ\Pi)$ by FLOW-008. Its coefficients and their
first derivatives have at most polynomial dimension cost. Taylor through
degree five with integral sixth remainder gives the explicit coarse bound

$$
\mathbb E[\widetilde F(U_{j+1})-\widetilde F(U_j)\mid U_j]
=h\overline LF(\Pi U_j)+\mathcal R_j,
\quad
|\mathcal R_j|\le ChN^4\|F\|_6
                            (|m_1(U_j)|+\varepsilon^2). \tag{8}
$$

Here the spectral-equivalent step $W_\varepsilon U$ is used, not the
rapidly moving eigenvector representative. Every derivative of its
matrix path costs at most $C_j\sqrt N\|G\|_{\rm op}^j$.
In a sixth derivative of the composite, at most six such factors give
$N^3$; uniform Gaussian moments and parity remove the fifth expected
coefficient. The covariance generator and its derivative cost at most
$CN\|F\|_3$; multiplying the chart displacement gives
$CN^{3/2}|m_1|\|F\|_3$. The fourth logarithmic drift and frozen
mean-square term obey smaller bounds. $N^4$ covers both contributions.
Only derivatives through order six are used in (8).

Smooth cutoffs extend the test outside the chart without changing (8)
there. A single jump out of the larger chart is harmless: from the
unitary product and its zero first derivative,
$\|W_\varepsilon-I\|_{\rm op}\le C\varepsilon^2\|G\|_{\rm op}^2$.
The Gaussian net bound makes the probability of a fixed-size jump over
$O(T\varepsilon^{-4})$ steps at most $C_K\varepsilon^K$ for every fixed
$K$, uniformly in $N\ge3$, after decreasing $\varepsilon_0$.

## 4. Quantitative localization without a boundary limit theorem

Use a nonnegative smooth extension of $F_2=|p_2|^2$ which agrees with it
on the larger centered chart and is bounded by $CN^2$ with
$\|F_2\|_6\le CN^2$. Such cutoffs may depend on normalized traces,
whose derivatives are bounded, and on the polar-unitary chart.
Equation (12) of FLOW-009 implies
$\overline L F_2\le C$: the negative quadratic drift absorbs the
$300|p_2|/N$ error, and the bracket is at most 64.
Apply (8) up to the discrete stopping time, sum (6), and use positivity:

$$
\mathbb EF_2(\Pi U_{n\wedge\sigma})
\le Ct+CtN^6(\rho+\varepsilon^2).
$$

This expression denotes the chosen extension if the final point leaves
its chart. On a centered-second-trace exit with no large jump it is at
least $N^2q_*^2$. Include (7) and the large-jump event to obtain

$$
\mathbb P(\sigma\le n)
\le C\left[t/N^2+(t+1)N^4\varepsilon\right]. \tag{9}
$$

This argument uses neither regular exit values nor convergence of
stopping-time functionals. It bounds the exit directly in the discrete
chain. Gaussian tails and all cutoff errors are included in the loose
last term.

## 5. Uniform backward-semigroup estimates

Localize the projected diffusion of FLOW-009 by multiplying its noise
by a smooth $\chi(|m_2|^2)$ and its Itô drift by $\chi^2$, with $\chi=1$
for $|m_2|\le9/20$ and $\chi=0$ for $|m_2|\ge3/5$.
This gives generator $\chi^2\overline L$, preserving the centered
unitary slice. It has a smooth bounded ambient extension. For example,
use the polar map on $\|V^*V-I\|_{\rm HS}<\delta$, compose with $\Pi$,
and cut off both this distance and $|m_1|$ before their chart boundaries.
All fixed-order derivatives of these extensions are dimension-uniform.

On this localized region $N\mathcal C_Y|_{\mathcal H_0}$, on the real
traceless Hermitian space, has spectrum in a fixed compact subinterval
of $(0,\infty)$ and fixed-order operator derivatives bounded
by $C_j$. This follows term by term from (4) of FLOW-003; each trace
rank term has two factors of Hilbert--Schmidt size $\sqrt N$ and
normalization $N^{-2}$. The square-root resolvent integral then gives
$\|D^j\mathcal C_Y^{1/2}\|\le C_jN^{-1/2}$.

In real ambient coordinates write the extended equation as
$dY=b(Y)dt+\sigma(Y)dW$. The number of noise coordinates is at most
$N^2$. Through order six its coefficients satisfy

$$
\|D^j\sigma\|_{\rm noise\ HS}\le C_j\sqrt N,
\qquad \|D^j b\|_{\rm HS}\le C_jN. \tag{10}
$$

For the drift it suffices to contract the bounded derivatives of $\Pi$
against $\sum_a\|K_a\|_{\rm HS}^2\le CN$; derivatives through order
eight of $\Pi$ are available from the same implicit equation.
These are multilinear derivative norms on unit ambient directions;
they do not sum over ambient coordinate tuples.

Differentiating the Itô equation in up to six fixed initial directions,
applying Itô's formula to even moments, and inducting on the derivative
order proves

$$
\|S_sF\|_6\le C e^{CNs}\|F\|_6,\qquad 0\le s\le1. \tag{11}
$$

For the first derivative the moment differential inequality has
coefficient $C(\|Db\|+\|D\sigma\|^2)\le CN$.
At each higher derivative order, the new equation has the same linear
part and products of lower derivative variations as forcing. Hölder,
the required higher even moments and Gronwall give an exponent $C_kNs$;
there are only six orders. Factors $Ns$ from the forcing integrals are
absorbed by increasing $C_k$, not by an exponential in $N^2$.
This proves (11) without a spectral-gap or dimension-uniform elliptic
regularity assertion. The generator also obeys
$\|\overline LF\|_k\le CN\|F\|_{k+2}$, for $k\le4$.

Take $g(s,Y)=S_{t-s}F(Y)$. On the pre-exit region it solves
$\partial_sg+\overline Lg=0$ and is invariant under conjugation and
common rotation. Therefore $g(s,\Pi U)$ has no fast term.
Apply (8), the backward equation and (11) at each discrete time,
including the time increment. The latter contributes at most
$Ch^2N^2 e^{CNt}\|F\|_6$, using $\overline L^2g$.
Summation up to $n\wedge\sigma$, (6), and (9) yield, for $0\le F\le1$,

$$
\left|\mathbb E F(\Pi U_n)-S_tF(C_N)\right|
\le C\left[t/N^2+N^4\varepsilon
                 +tN^4e^{CNt}\|F\|_6\varepsilon\right]. \tag{12}
$$

One compares the stopped backward expression with the terminal test;
their difference is at most twice the exit probability, because both
take values in $[0,1]$. The final time interval shorter than $h$ is
bounded by $ChN e^{CNt}\|F\|_6$ and fits the last term.
This avoids derivatives of a killed boundary semigroup altogether.

## 6. Microscopic tests and completion of the proof

For smooth compactly supported $f$, periodize
$f(N\theta/(2\pi))$. Its Fourier coefficients $a_k$ satisfy
$\sum_k |k|^j|a_k|\le C_{f,j}N^j$, $0\le j\le6$.
On the unitary group, $j$ derivatives of $\operatorname{Tr}U^k$
are bounded coarsely by $C_jN(1+|k|)^j$; the polar extension has the
same bound. Thus the trace of the periodized test has derivative norm
at most $C_{f,j}N^{j+1}$.
It is nonnegative, so differentiating its exponential and integrating
over the observation angle gives

$$
0\le\Phi_{N,f}\le1,\qquad \|\Phi_{N,f}\|_6\le C_fN^{12}. \tag{13}
$$

Each product of derivatives in order $j$ has total order $j$ and at
most $j$ factors, explaining $N^{2j}$. This is a bound on a smooth
matrix class function even at eigenvalue collisions; no inverse gap
occurs. Centering and extension do not add dimension powers.

Use (13) in (12); its weak-error power is at most $N^{16}$.
Equation (5) of FLOW-009 and (6) remove terminal centering at cost
$C_f\rho$ before exit. The localized diffusion agrees with the original
projected diffusion until $|m_2|=9/20$; (13) of FLOW-009 bounds its exit
probability by $Ct/N^2$. FLOW-009's projected-to-Dyson comparison and
FLOW-007's credited odd-clock Dyson theorem give the other three
terms in (1). $N^{20}$ covers the exit, time-rounding and extension
budgets with four spare powers. This proves (1).

For $\varepsilon_N=e^{-N}$ and $t_N\to0$,
$N^{20}\exp(CNt_N-N)\to0$ since eventually $Ct_N<1/2$.
At $t_N=N^{-2/3}$ the two principal errors are $N^{-1/3}$.
Finally uniform-origin averaging gives exactly unit mean intensity,
so $|\Phi_{N,f}-\Phi_{N,g}|\le\|f-g\|_1$ for every spectrum.
Nonnegative smooth approximation proves the $C_c^1$ joint limit.

## 7. Research consequence

The small fast coordinate has scale $\varepsilon/N+\varepsilon^4$,
rather than an unspecified dimension-dependent $O_N(\varepsilon)$.
Together with controlled derivatives on the Möbius slice this closes
an explicit simultaneous regime for the original random kicks.
It leaves a concrete quantitative question: replace the exponentially
small step by an economical polynomial step without the coarse
$e^{CNt}$ stability cost. More fundamentally, the initial clock has
rigid spacings and this chain changes them to Sine$_2$. The argument
therefore supplies no deterministic noise-removal estimate for the
frozen quantum map.
