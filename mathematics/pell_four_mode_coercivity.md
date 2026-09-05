---
title: "Sharp coercivity on the complete first Fourier box"
author: "WoW research programme"
date: "5 September 2026"
---

# A multiorbit result

The single-orbit theorem cannot simply be added across orbits: generated
frequencies can coincide and their coefficients interfere. This note handles
those coincidences exactly on the complete first Fourier box for the Pell
matrix $T=\left(\begin{smallmatrix}3&2\\4&3\end{smallmatrix}\right)$.
It is a finite-dimensional algebraic theorem, not positive BGS or a priority
claim. Its scope includes mixtures of distinct frequency orbits.

Write $b_v(x)=2\cos(2\pi v\cdot x)$, $\mathcal Cb_v=b_{Tv}$, and use the
same Green--Kubo form and $\Gamma(g)=\sigma^2(\{g,\mathcal Cg\}/(4\pi))$
as in the general single-orbit note. Every real, even, mean-zero trigonometric
polynomial with frequencies $\|v\|_\infty\leq1$ has the unique form
$$
 g=a b_{(0,1)}+b b_{(1,-1)}+c b_{(1,0)}+d b_{(1,1)},
             \qquad a,b,c,d\in\mathbb R.                    \tag{B1}
$$
Here $b$ without a subscript is a real coefficient. The frequencies $(1,-1)$
and $(1,1)$ share an orbit since $T(1,-1)=(1,1)$; the other two belong to
different signed orbits.

**Theorem.** On this whole four-dimensional space,
$$
             \boxed{\Gamma(g)\geq4\pi^2\|g\|_{L^2}^4.}      \tag{B2}
$$
The constant is sharp. Among nonzero symbols equality occurs exactly for a
scalar multiple of one of $b_{(0,1)},b_{(1,-1)},b_{(1,1)}$. In particular,
there is no nonzero second-order flat generator in this Fourier box.

# Exact quartic identity

Set $Q=\Gamma(g)/\pi^2$. Direct orbit reduction gives
$$
\begin{split}
 Q={}&16a^4+16b^4+64c^4+16d^4\\
 &+104a^2(b^2+d^2)+140a^2c^2+200c^2(b^2+d^2)\\
 &+608b^2d^2+8a^2bd+4bc^2d.
\end{split}                                               \tag{B3}
$$
The last two terms show why the four modes cannot be treated as independent.
Nevertheless the difference from the claimed bound is a sum of squares:
$$
\begin{split}
 Q-16(a^2+b^2+c^2+d^2)^2
 ={}&48c^4+108a^2c^2+68a^2(b^2+d^2)\\
 &+4(ab+ad)^2+166c^2(b^2+d^2)\\
 &+2(bc+cd)^2+576b^2d^2.
\end{split}                                               \tag{B4}
$$
Each summand is nonnegative. Cosine orthogonality gives
$\|g\|_2^2=2(a^2+b^2+c^2+d^2)$, proving (B2). Equality in (B4) first
forces $c=0$, then $bd=0$ and $a^2(b^2+d^2)=0$. The nonzero possibilities
are precisely the three asserted axes. Conversely those axes give equality
in (B3). Thus both sharpness and the complete equality set are established.

# Auditable orbit reduction behind the quartic

The basic differentiation identity is
$$
 \{b_u,b_w\}/(4\pi)=\pi\det(u,w)(b_{u-w}-b_{u+w}).
$$
Apply it to the sixteen ordered pairs of modes in (B1), replacing the second
frequency w by Tw. For each resulting frequency identify v and -v, then sum
along its T-orbit. The following table lists every nonzero orbit sum divided
by $\pi$; call these polynomials $P_{\mathcal O}$. Then
$Q=2\sum_{\mathcal O}P_{\mathcal O}^2$, whose expansion is (B3).

| Orbit representative | $P_{\mathcal O}$ | Orbit representative | $P_{\mathcal O}$ |
|---|---|---|---|
| $(-6,-6)$ | $-12bd$ | $(-4,-8)$ | $12bd$ |
| $(-4,-4)$ | $-4c^2$ | $(-4,-3)$ | $-7bc$ |
| $(-4,3)$ | $-7cd$ | $(-3,-3)$ | $-6ac$ |
| $(-3,-2)$ | $-5ab$ | $(-3,2)$ | $-5ad$ |
| $(-2,-5)$ | $7bc$ | $(-2,-4)$ | $2a^2+4c^2$ |
| $(-2,-2)$ | $-2a^2$ | $(-2,-1)$ | $-bc$ |
| $(-2,0)$ | $-2b^2-2d^2$ | $(-2,1)$ | $-cd$ |
| $(-2,5)$ | $7cd$ | $(-1,-4)$ | $5ab$ |
| $(-1,-3)$ | $3ac$ | $(-1,-2)$ | $ab+ad$ |
| $(-1,0)$ | $-ab-ad$ | $(-1,3)$ | $3ac$ |
| $(-1,4)$ | $5ad$ | $(0,-2)$ | $2b^2+2d^2$ |
| $(0,-1)$ | $bc+cd$ |  |  |

Representatives are selected by minimizing $E(v)=2v_1^2+v_2^2$ along the
signed T-orbit, with a lexicographic tie rule. This procedure is exact:
writing $v_2+\sqrt2v_1$ and its conjugate shows that
$E(T^jv)=A\lambda^{2j}+B\lambda^{-2j}$ with A,B strictly positive for
nonzero integral v. It is strictly convex as a function of real j. Integer
neighbour descent therefore reaches its global integer minimum, with at most
two adjacent ties. This also gives a finite way to check that the displayed
representatives are distinct orbit classes. No unexplained bound on orbit
search depth is imported into the proof.

The maintained Python script constructs this table in the original integral
coordinates and verifies (B3)--(B4) coefficient by coefficient over the
integers. The independent C++ quadratic-ring implementation agrees at all
80 nonzero coefficient vectors in $\{-1,0,1\}^4$. The finite evaluations are
cross-checks; the coefficientwise identities and orbit reduction establish
the theorem for arbitrary real coefficients.

# An exact obstruction to extending the same constant

The constant in (B2) cannot hold on every larger Fourier box. Define a
sixteen-mode polynomial $g_*$ by the following nonzero cosine coefficients:

| Frequency | Coefficient | Frequency | Coefficient |
|---|---:|---|---:|
| $(0,1)$ | $-5$ | $(0,2)$ | $-7$ |
| $(0,3)$ | $4$ | $(1,-3)$ | $1$ |
| $(1,-2)$ | $5$ | $(1,-1)$ | $-10$ |
| $(1,1)$ | $10$ | $(1,2)$ | $-5$ |
| $(1,3)$ | $-1$ | $(2,-2)$ | $2$ |
| $(2,-1)$ | $2$ | $(2,0)$ | $-6$ |
| $(2,1)$ | $2$ | $(2,2)$ | $2$ |
| $(3,-1)$ | $1$ | $(3,1)$ | $-1$ |

All frequencies lie in the radius-three box. Exact integer Poisson and orbit
reduction gives
$$
 \sum_v c_v^2=396,\qquad
 \frac{\Gamma(g_*)}{\pi^2}=1890144,\qquad
 \boxed{\frac{\Gamma(g_*)}{\|g_*\|_2^4}
                  =\frac{6563}{2178}\pi^2<4\pi^2.}         \tag{B5}
$$
The complete 106 nonzero integer orbit sums are recorded by the checker; their
squared sum times two is 1890144. Original-coordinate Python and independent
quadratic-ring C++ both obtain this exact integer. Thus (B5) is an exact
finite arithmetic witness, not a fitted floating-point minimum. It does not
claim to be the optimal radius-three polynomial or a zero of Gamma.

# Broader experiments are not promoted to the theorem

A radius-two search found the radius-one minimum in twelve local numerical
optimizations, but that is not a proof of the corresponding global inequality.
A restricted diagonal-dominance sum-of-squares search there was infeasible;
this does not disprove a more general SOS certificate or the inequality.
The radius-three numerical search was used to find the integer witness (B5),
which was then independently verified in exact arithmetic. No numerical
stationary point is labelled a global optimizer.

Likewise, infeasibility of a linear identity or diagonal-dominance certificate
at a given radius does not prove that a nonzero zero of Gamma exists. The
arbitrary multi-orbit nondegeneracy and sharp-minimum problems remain distinct
from the completed four-mode theorem and exact counterexample (B5).
