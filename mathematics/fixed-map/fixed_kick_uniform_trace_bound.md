# Uniform original-family traces from continuity of the Gaussian scalar

**Claim:** BGS-TRACE-113. **Status:** analytic proof reconstructed and
self-reviewed on 21 October 2026; external classical input checked in its
published primary source. No external referee or formal verification.

Final dependency and cross-surface self-review: 22 October 2026.

## 1. The exact quantifiers

For the original odd-modulus family of
[TRACE-106](physical_kick_trace_decay.md), with unchanged $\tau=10^{-80}$,
there are $C<\infty$, $N_0<\infty$ and

$$
1<a<\sqrt\lambda,\qquad\lambda=3+2\sqrt2,
$$

such that

$$
|\operatorname{Tr}U_N^m|\le Ca^m
\quad\text{for every odd }N\ge N_0\text{ and every integer }m\ge1.
                                                               \tag{1}
$$

The threshold is independent of $m$. Neither the pressure gap nor $N_0$
is evaluated numerically. At $m\asymp N$ the right side is larger than
the unitarity bound $N$; (1) does not estimate the microscopic trace sum.

The full older route controls a per-edge modulus error by $O(h^2)$.
For (1) that quantitative expansion is unnecessary. Uniform continuity at
$h=0$ suffices once the positive classical pressure gap is fixed.

## 2. Exact quantum inputs and why their limits are legitimate

Set $h=(2\pi N)^{-1}$, $t_*=\tau/(2\pi)$ and
$\Psi=\phi_{-a}^{t_*}\circ L$,
$L=\left(\begin{smallmatrix}3&-4\\-2&3\end{smallmatrix}\right)$.
In this paragraph $a$ inside $\phi_{-a}$ is the ordinary-half Hamiltonian
symbol, whereas the constant $a$ in (1) is an exponential base.

The following complete source arguments have been read and reconstructed:

| Step | Source and exact scope |
|---|---|
| Odd comb, integer lattice character, metaplectic scalar | [Odd trace proof](../spectral_research/proofs/research_continuation_2026_10_20/odd_trace_and_algebraic_rigidity.md), §§2--5 |
| Normalized coherent frame and exact sector trace | Same source, §§6--8 |
| Exact analytic one-step amplitude and its real-$h$ limit | [Amplitude proof](../spectral_research/proofs/research_continuation_2026_10_20/exact_amplitude.md), §§1--8 |
| Contour, trace-class convergence and dominated splitting | [Gaussian proof](../spectral_research/proofs/research_continuation_2026_10_20/gaussian_cocycle_and_modulus.md), §§1--6 |
| Exact zero-order periodic normalization | Same source, §9; only its zero-order Gaussian identities are used |

Here are the substantive convergence checks. The real Weyl shifts preserve
horizontal analytic strips. After factoring the Hamilton--Jacobi phase,
the amplitude generator loses one derivative with bound $C/\delta$.
On a strip gap $\Delta=.001$, its $n$th time-ordered term is bounded by
$(eC|t|/\Delta)^n$, uniformly for real $h$, with $C=10^6$.
This ratio is below $.002719$ on $|t|\le10^{-12}$ and below
$4.4\cdot10^{-72}$ at $t_*$. Fixed-$h$ bounded-operator uniqueness
identifies the amplitude with the exact plane propagator; finite-jet
formal agreement alone would not do so. In particular $B_h\to
B_0=2\sqrt{F_{Qq}}$ uniformly with the required spatial derivatives.

For each fixed $m,N$ the operator word expansion has finite absolute
coefficient mass. Translated metaplectic coherent diagonals have Gaussian
integrals independent of the translation. Their lattice sums on a unit cell
are uniformly bounded in the Gaussian center. Thus all rearrangements in the
coherent sector identity are absolutely justified at that fixed $m,N$.
The Abel form follows word by word: its quadratic Hessian is
$-(6I-R-R^{-1})/4$, with spectrum in $[-2,-1]$, also for $m=1,2$.
Damped Gaussian integrals are bounded independently of every linear phase.
The resulting exact identity does not require a bound on word coefficient
mass uniform in $m$.

Center the phase on an edge and deform each real coordinate to
$z_s(y)=sy-i\psi(sy)$, $s=\sqrt h$, with smooth odd saturation,
$\psi(u)=u$ near zero and $0\le\psi'\le1$. If
$D=u'\psi(u')+u\psi(u)$, the real exponent is at most $-D/(4h)$.
For a finite-dimensional sector, entire Gaussian regularization first
justifies the deformation; this bound then removes the regulator by dominated
convergence. The saturated tails decay linearly in $|y|/s$, not quadratically.
They are $O(e^{-c/h})$ in every fixed weighted derivative norm needed here.

The edge operators $K_h(x)$ are trace class. With
$H=1-\partial_y^2+y^2$ one has the explicit criterion

$$
\|K\|_1\le\frac{\pi^2}{24}\|H_{y'}H_y k\|_{L^2(\mathbb R^2)}.
                                                               \tag{2}
$$

It proves uniform convergence $K_h(x)\to K_0(x)$ in trace norm.
All these operators are within $10^{-4}$ of the fixed Gaussian operator
whose eigenvalues are $1,\rho,\rho^2,\ldots$, $\rho=3-2\sqrt2$,
once $h<h_0$ for one threshold independent of $x$ and $m$.

The normalized past/future graph transforms contract by less than $.172$.
They give, on one fixed Hilbert space,

$$
K_h(x)=\gamma_h(x)v_h(\Psi x)\ell_h(x)+\mathcal B_h(x),
\quad\ell_h(x)v_h(x)=1,
$$
$$
\mathcal B_h(x)v_h(x)=0,\quad
\ell_h(\Psi x)\mathcal B_h(x)=0,
\quad\|\mathcal B_h\|<.174,\quad\|\mathcal B_h\|_1<.209. \tag{3}
$$

The two zero identities make every mixed product vanish exactly. The graph
transforms use the full past and future, not a finite-time boundary condition.
The centered deck identities make (3) a torus cocycle without a missing chart
phase. The exact trace therefore is

$$
\operatorname{Tr}U_N^m
=\zeta_N^m\sum_{x\in\operatorname{Fix}\Psi^m}
\omega_{m,N}(x)\lambda^{-m/2}\Gamma_h(x,m)+E_{m,N},
\quad |E_{m,N}|\le2(.421)^m,                     \tag{4}
$$

where $|\omega|=1$ and $\Gamma_h=\prod_{j=0}^{m-1}\gamma_h(\Psi^jx)$.
The residual bound follows from (3) and
$\#\operatorname{Fix}\Psi^m<\lambda^m$, derived by strict concavity
of the cyclic action. It holds simultaneously for every $m$.

## 3. The only modulus fact needed

Uniform contraction stability and $K_h\to K_0$ imply
$\gamma_h\to\gamma_0$ uniformly, with $\gamma_0(x)>0$ bounded away
from zero. Define

$$
\varepsilon(h)=\sup_x|\log|\gamma_h(x)|-\log\gamma_0(x)|\longrightarrow0.
                                                               \tag{5}
$$

For a periodic orbit of period dividing $m$, let $\Lambda_m(x)>1$
be its unstable multiplier. The Gaussian cyclic integral and the discrete
Hill determinant identity give

$$
\lambda^{-m/2}\operatorname{Tr}\prod K_0(\Psi^jx)
=\frac{\Lambda_m(x)^{-1/2}}{1-\Lambda_m(x)^{-1}}.
$$

Repeat this orbit $r$ times in the exact Gaussian identity. Equation (3)
bounds the residual by $.209(.174)^{rm-1}$, while
$\Gamma_0\ge(1-.0002)^m>0$. Taking positive $r$th roots and letting
$r\to\infty$ proves

$$
\lambda^{-m/2}\Gamma_0(x,m)=\Lambda_m(x)^{-1/2}.
$$

Consequently, directly from (5),

$$
\lambda^{-m/2}|\Gamma_h(x,m)|
\le e^{m\varepsilon(h)}\Lambda_m(x)^{-1/2}.         \tag{6}
$$

No parity expansion, imaginary first coefficient, or rate for (5) enters (6).

## 4. Actual classical pressure gap

The small analytic perturbation has invariant stable/unstable cones and
preserves area. It is topologically conjugate to $L$: write
$\Psi(x)=Lx+v(x)$, with $\|v\|<10^{-78}$ and derivative less than
$10^{-70}$. The bounded Green inverse of
$u(Lx)-Lu(x)=g(x)$ is the sum of the forward unstable and backward stable
geometric series. Applying it to $g=v(x+u(x))$ is a contraction.
It constructs $H(x)=x+u(x)$ with $\Psi H=HL$. Degree one gives
surjectivity. If $Hx=Hy$, all $L^n x,L^n y$ stay within $2\|u\|$;
linear expansivity gives $x=y$. Thus $H$ is a homeomorphism.
It follows that the map is transitive, expansive, has dense periodic points
and entropy $H_0=\log\lambda$.

Let $\varphi=\log J^u_\Psi$ and $P_*=P_\Psi(-\varphi/2)$.
The [checked Bowen--Ruelle input](../../literature/bowen_ruelle_trace_closure_20261021.md)
applies to the smooth constant-roof mapping torus. It supplies the equilibrium
and volume facts needed below, without a mixing-flow assumption.
The endpoint pressures are $P(0)=H_0$ and $P(-\varphi)=0$, with smooth
area the geometric equilibrium state. If $P_*=H_0/2$, a midpoint
equilibrium would maximize both endpoint functionals. Uniqueness would make
smooth area the measure of maximal entropy.

This is impossible at the actual fixed point $x_0=(0,0)$:

$$
\operatorname{Tr}D\Psi(x_0)
=6+\frac{39212\pi}{125}\tau>6,
\qquad\Lambda_0>\lambda.
$$

On its period-one suspension orbit, the zero-potential Gibbs lower bound
and the smooth-volume upper bound would give, for all integers $m\ge1$,
$c\lambda^{-m}\le\operatorname{vol}B_m(x_0,\delta)
\le C\Lambda_0^{-m}$, a contradiction. Hence

$$
\Delta=H_0/2-P_*>0.                              \tag{7}
$$

The fixed points of $\Psi^m$ are separated at a fixed expansivity scale.
The separated-set definition of pressure therefore gives, for each $\eta>0$,

$$
\sum_{x\in\operatorname{Fix}\Psi^m}\Lambda_m(x)^{-1/2}
\le C_\eta e^{(P_*+\eta)m},\qquad m\ge1.          \tag{8}
$$

Only an upper bound is used; no periodic-orbit equidistribution or rate is
silently inserted into (8).

## 5. One threshold for all iterates

Take $\eta=\Delta/4$ and use (5) to choose $h_1$ so that
$\varepsilon(h)\le\Delta/4$ for $0<h<h_1$.
Equations (4), (6) and (8) give

$$
|\operatorname{Tr}U_N^m|
\le C_\eta e^{(H_0/2-\Delta/2)m}+2(.421)^m.
$$

Choose any $a$ strictly between
$\max\{1,e^{H_0/2-\Delta/2}\}$ and $e^{H_0/2}$.
This proves (1), with one $N_0$ chosen from $h<\min(h_0,h_1)$.
The lower Pell spectral-distance bound in TRACE-110 is consequently an
unconditional corollary at its stated global scale. This does not give a
local spacing law, a physical counterexample, or signed cancellation at
times proportional to $N$.
