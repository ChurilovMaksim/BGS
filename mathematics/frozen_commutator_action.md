# Classical commutator action with an explicit fixed-coupling remainder

**Claim ID:** `BGS-FM-015`

Date: 30 September 2026. Status: project proof and author self-review.
This closes the classical generating-function obligation in Section 39 of
the submitted note, in a specified mixed-coordinate chart. It does not
construct its quantum FIO kernel or prove an operator norm estimate.

## 1. The action and its exact coordinates

Use the physical symbol $g$ of [FM-001](fixed_model_symmetry_theorem.md),
$g_\delta(x)=g(x+\delta)$, and $X_h=(h_p,-h_q)$. Write
$$
\chi_{t,\delta}=T_{-\delta}\circ\Phi_g^t\circ T_\delta\circ\Phi_g^{-t}
=\Phi_{g_\delta}^t\circ\Phi_g^{-t}.
$$
All shifts are real. For $|t|\le10^{-8}$ the lifted graph has mixed
coordinates $(q,P)$, where $(Q,P)=\chi_{t,\delta}(q,p)$, and admits
a local real generating function
$$
S_{t,\delta}(q,P)=qP+s_{t,\delta}(q,P),\qquad
p=P+\partial_qs_{t,\delta},\quad Q=q+\partial_Ps_{t,\delta}. \tag{1}
$$
On a lift of the unit square choose its additive constant so that
$s_{t,\delta}(0,0)=t[g_\delta(0,0)-g(0,0)]$. Then
$$
s_{t,\delta}(q,P)=t[g_\delta(q,P)-g(q,P)]+E_{t,\delta}(q,P),
$$
and on the real unit square
$$
\|E_{t,\delta}\|_{C^{15}}\le10^{61}t^2,
\qquad
\max_{1\le j\le15}\|(2\pi)^{-j}\partial_q^jE_{t,\delta}\|_\infty
\le10^{49}t^2.                                             \tag{2}
$$
The $C^{15}$ norm here is the maximum over all partial derivatives of
total order at most 15, rather than their sum. Constants are deliberately
loose. Local charts and their constant choices suffice; no quantization,
global action holonomy or torus kernel phase is inferred from (1).

For $d_{\mathbb T}(\delta_q,0)\ge1/7$ and $0<|t|\le10^{-52}$,
the [finite-type theorem](frozen_phase_finite_type.md) gives
$$
\max_{1\le j\le14}|D_q^js_{t,\delta}|\ge |t|\kappa_0/2,
\quad
\max_{2\le j\le15}|D_q^j(s_{t,\delta}+\ell q)|
\ge |t|\kappa_0/2                                         \tag{3}
$$
for every real $\ell$. The actual Hamiltonian time
$t=\tau/(2\pi)$, $\tau=10^{-80}$, satisfies this explicit threshold.

## 2. Analytic bounds and flows

The exact Fourier expansion has
$\sum_{n,m}|\widehat g(n,m)|<2$, $|n|\le9$, $|m|\le1$,
$|n|+|m|\le10$. These bounds also hold for every real translate.
On the complex strip $|\Im q|,|\Im p|<R=1/100$ they imply
$$
|g|<4,\quad \|X_g\|_\infty\le B=300,
\quad \|DX_g\|_{\infty\to\infty}\le L=20000.                \tag{4}
$$
For example $|g|\le2e^{2\pi/10}<4$ and the largest row sum of the
Hamiltonian Hessian is bounded by $4(2\pi)^2\cdot9\cdot10<20000$.
These inequalities use the ordinary physical symbol, not the raw symbol.

Starting in the strip of width $3R/4$, the two flows for real
$|t|\le10^{-8}$ stay within width $R$: their total displacement is
at most $2B|t|\le6\cdot10^{-6}<R/4$. Local analytic ODE existence
and this a priori displacement extend them throughout the interval.
Integrating $X_h(x(u))-X_h(x)$ bounds each first-order flow remainder
by $BLt^2/2$. Composition therefore gives
$$
\|\chi_{t,\delta}(x)-x-t(X_{g_\delta}-X_g)(x)\|_\infty
\le3\cdot10^7t^2                                         \tag{5}
$$
on that strip. The bound follows from the two individual remainders and
the term $|t|L\|\Phi_g^{-t}(x)-x\|\le BLt^2$;
$2BL=1.2\cdot10^7<3\cdot10^7$. Displacement itself is at most $600|t|$.

## 3. Mixed-coordinate inversion and closedness

Let $d_p(q,p)=P(q,p)-p$. Cauchy's estimate between the strips of
width $3R/4$ and $R/2$ gives
$|\partial_pd_p|\le (4/R)600|t|=240000|t|<1/2$.
For $|\Im q|,|\Im P|<R/4$, solve
$p=P-d_p(q,p)$ by contraction on $|p-P|\le1200|t|$.
This ball stays in the width-$R/2$ strip; the map takes it into the
smaller ball of radius $600|t|$. Its fixed point is unique, analytic
in $(q,P)$, and $|p-P|\le600|t|$.

Symplecticity implies that
$$
\beta=(p(q,P)-P)dq+(Q(q,p(q,P))-q)dP
$$
is closed: in these coordinates $dp\wedge dq=dP\wedge dQ$ says
$\partial_Pp=\partial_qQ$, exactly the cross-derivative condition.
The Poincaré lemma on the lifted simply connected strip therefore gives
$ds=\beta$, proving (1). Reality follows from the real graph. A global
periodic primitive is not needed or asserted in this theorem.

The replacement of $p$ by $P$ in the first-order term costs at most
$|t|\cdot2L\cdot600|t|$. Together with (5) this proves
$$
\|\nabla_{q,P}E_{t,\delta}\|_\infty\le10^8t^2              \tag{6}
$$
throughout the width-$R/4$ strip, uniformly in every real translate.
The chosen constant makes $E(0,0)=0$; integrating (6) along a path
of length at most 2 gives $|E|\le2\cdot10^8t^2$ on the real square.

## 4. Derivative bounds and fixed time

For a multiindex of total order $j\ge1$, apply Cauchy's estimate to
one component of (6) on a polydisc of radius $R/8=1/800$ around a
real point. Its modulus is bounded by
$10^8(j-1)!800^{j-1}t^2$. For $1\le j\le15$ this is less than
$10^{61}t^2$. Dividing a pure $q$ derivative by $(2\pi)^j$ makes
the maximum less than $10^{49}t^2$ (already $\pi>3$ suffices).
This proves (2) with no fitted constants.

The elementary estimates in the finite-type proof give $\kappa_0>0.008$.
Thus $10^{49}|t|\le10^{-3}<\kappa_0/2$ at $|t|\le10^{-52}$.
Applying its perturbation inequalities proves (3). In particular the
smallness of the maintained coupling is now used in a checked inequality,
not as a substitute for a remainder estimate.

The verifier checks the Fourier mass and all rational arithmetic bounds
behind these constants. It does not verify analytic ODE existence or the
Poincaré lemma. Constructing a uniform torus FIO for the actual quantum
commutator, controlling its normalized Hilbert--Schmidt matrix elements,
and deriving a compression norm gap are distinct open obligations.
