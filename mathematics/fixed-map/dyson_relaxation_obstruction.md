# A low-trace obstruction to prescribed-time Dyson relaxation

**Claim ID: BGS-FLOW-013.** Project derivation, 4 October 2026.
Base: `4982f8fc3d6303cc2cf7840e608f07d41ba2783e`.
The construction is an abstract initial spectrum, not the frozen quantum
map and not a counterexample to a naturally quantified BGS conjecture.

## 1. Exact quantifiers

For **every prescribed** sequence $t_N\to0$ along odd dimensions,
there are simple deterministic unitary spectra $A_N$ such that:

1. Their empirical measures converge weakly to uniform circle measure.
2. For every fixed positive $j$, $|\operatorname{Tr}A_N^j|=O_j(1)$;
   eventually $|p_1|+|p_2|<20$.
3. Every positive power trace is nonzero, at every dimension of the construction.
4. Normalized circular Dyson Brownian motion from $A_N$, and from
   $\Pi(A_N)$, converges from a uniform origin locally in probability to
   the **empty point process** at time $t_N$.

If also $Nt_N\to\infty$, the original uncentered coboundary chain with
$\varepsilon_N=N^{-10}$ and
$n_N=\lfloor2t_NN^{40}\rfloor$ has the same empty weak local limit,
by FLOW-012. All these uniformly rooted processes nevertheless have
exactly unit mean intensity at every finite $N$. The failure is lack of
uniform integrability, not a change in the unfolding convention.

The initial family may depend on the prescribed times. This does not
rule out a slower, family-dependent relaxation schedule for each given
globally equidistributed family. It refutes the universal implication
from the listed low-trace hypotheses to a specified $t_N$.

## 2. An elementary finite spectral-concentration bound

Let $A$ have all its eigenangles within circular distance $\delta$ of a
set of $Q$ angles $\Gamma$. Let $V_t=B_tA$, where normalized full or
traceless unitary Brownian motion $B_t$ starts at $I$. Then

$$
\mathbb E N^{-1}\|V_t-A\|_{\rm HS}^2\le t.
\tag{R1}
$$

Indeed the full process solves $dB=i\,dH B-B\,dt/2$ with covariance
$\mathbb E(dH)_{ab}(dH)_{cd}=dt\,\delta_{ad}\delta_{bc}/N$.
Thus $\mathbb EB_t=e^{-t/2}I$ and the left side is
$2(1-e^{-t/2})\le t$. For traceless noise replace the exponent by
$-(1-N^{-2})t/2$, obtaining the same bound.

There is a permutation matching eigenvalues of two unitary matrices
with summed squared chord distances at most their matrix HS distance
squared. To see this directly, overlap squares of their orthonormal
eigenbases form a doubly stochastic matrix $P$, and
$\sum_{jk}P_{jk}|\lambda_j-\zeta_k|^2=\|V-A\|_{\rm HS}^2$.
Decompose $P$ into permutation matrices and select one whose cost is
at most this average. The decomposition follows by a positive-support
Hall matching, subtraction of its smallest matched weight, and induction
on the number of positive entries. This argument includes repeated eigenvalues.

Circular angle distance is at most $\pi/2$ times chord distance.
Consequently, if $M_b(V_t)$ counts eigenangles farther than $b>0$ from
$\Gamma$, then

$$
\mathbb E\frac{M_b(V_t)}N
\le \frac{2\delta^2+(\pi^2/2)t}{b^2}.
\tag{R2}
$$

Let $I\subset[-R,R]$ be a fixed bounded interval in unfolded units,
and let $X_{N,t}(I)$ count its points from an independent uniform origin.
A point within $b$ of $\Gamma$ can be observed in $I$ only if that origin
lies within $b+2\pi R/N$ of one of the $Q$ centers. For the remaining
points, uniform-origin averaging gives expected count
$|I|\mathbb E M_b/N$. Hence, for $N>2R$,

$$
\mathbb P(X_{N,t}(I)>0)
\le \frac Q\pi\left(b+\frac{2\pi R}N\right)
+|I|\frac{2\delta^2+(\pi^2/2)t}{b^2}.
\tag{R3}
$$

No operator-norm Brownian bound, local density assumption, spectral-gap
lower bound, or numerical simulation is used in (R3).

## 3. Globally uniform clusters with uniformly bounded fixed traces

For all sufficiently large odd $N$, choose the largest odd integer

$$
3\le Q_N\le\min(N^{1/10},t_N^{-1/6}).
\tag{R4}
$$

It tends to infinity; a finite initial segment can be filled arbitrarily.
Write $N=LQ+r$, $0\le r<Q$. Put $L$ particles at every $Q$th root.
If $r>0$, put one additional particle at roots with indices
$k_l=\lfloor lQ/r\rfloor$, $0\le l<r$. These indices are distinct.
At each root split its particles with the angles

$$
\theta_{k,s}^{\rm alg}=2\pi k/Q+2\pi s/N^5,
\quad 0\le s<n_k,\qquad
\delta_N\le(2\pi+1)N^{-4}.
\tag{R5}
$$

All these eigenvalues are algebraic roots of unity and are distinct.
Finally multiply the eigenvalue at $(k,s)=(0,0)$ by $e^{i\eta_N}$,
$\eta_N=N^{-4}$. It remains within the stated cluster radius and cannot
equal another algebraic eigenvalue.

For fixed $j<Q$, the $L$ complete polygons have zero $j$th trace.
For the extra particles, compare $k_l/Q$ with $l/r$. If $r>j$ the
$r$-clock trace is zero, and the comparison error is at most
$2\pi jr/Q\le2\pi j$. If $r\le j$ their entire contribution is at
most $r\le j$. Splitting and the one exceptional rotation add at most
$2\pi j/N^3+j/N^4$. Therefore

$$
|p_j(A_N)|\le2\pi j+2\pi j/N^3+j/N^4,
\qquad j<Q.
\tag{R6}
$$

In particular the eventual first-two sum is at most $6\pi+o(1)<20$.
The empirical measure converges to uniform measure: the complete
polygons do, the extra mass is at most $Q/N$, and splitting tends to zero.

For **every** integer $j\ge1$, write the trace before the exceptional
rotation as an algebraic number $a_j$. Afterwards it is
$a_j-1+e^{ij\eta_N}$. The last exponential is transcendental, since
$ij\eta_N$ is a nonzero algebraic number. Thus the trace is nonzero.
This uses the already checked Popescu Corollary 3.2
([EXT-POPESCU-2023](../../literature/external_dependencies.json)); it supplies
no quantitative lower gap or trace bound. The finite initial segment
can use an ordinary $N$-clock with this same one-eigenvalue rotation,
preserving simplicity and all-power nonvanishing.

## 4. Empty noisy limit and the chain consequence

Apply (R3) with $Q=Q_N$ and $b=Q_N^{-2}$. By (R4), $t_N\le Q_N^{-6}$.
The resulting bound is

$$
\mathbb P(X_{N,t_N}(I)>0)
\le C_I\left[Q_N^{-1}+Q_N/N+Q_N^{-2}+Q_N^4N^{-8}\right]\to0.
\tag{R7}
$$

Möbius centering moves every angle by at most $C_K/N$, using
$|w|\le8K/N$ and $K=20$. Apply the same proof to $\Pi(A_N)$ with
$\delta_N$ replaced by $\delta_N+C_K/N$; the additional term is
$C_KQ_N^4/N^2\to0$. A countable increasing collection of compact
windows identifies convergence locally in probability to the empty process.

For the chain, FLOW-012 (G2) with $\varepsilon=N^{-10}$ has error at
most $C_f[\sqrt{t_N}+N^{-1}+N^{-6}+N^{-11}+t_N/N+t_NN^{-10}]\to0$.
For every nonnegative compact smooth $f$, (R7) gives the reference
Laplace limit one; the same holds for the original chain. Uniform-origin
unit intensity gives tightness, and these Laplace limits identify the
empty weak point-process limit. Equivalently, smooth tests positive on
a fixed interval show that its nonempty probability tends to zero.

Sine$_2$ has unit intensity and positive probability of a point in a
nonempty interval, so its Laplace functional is strictly less than one
for suitable $f$. This distinguishes the limits.

The fixed map is not realized by this construction. What fails is using
its known fixed-time trace bounds, global equidistribution, simplicity,
or nonzero traces **alone** to import the clock's relaxation time.
This does not contradict [FLOW-014](circular_dyson_actual_start.md): that
result uses the actual frozen spectrum's growing logarithmic trace window,
not only the fixed-power bounds above, and proves the Dyson-reference
local Sine$_2$ Laplace limit from $\Pi U_N$ at $t_N=8g_N$,
$g_N=4\log J_N/J_N$, $J_N=\lfloor c\log N\rfloor$. Its comparison
also gives the original uncentered chain a weak uniform-origin local limit
on the stated polynomial schedule. [FLOW-017](coboundary_all_order_limit.md)
adds all fixed factorial orders and one-chain $L^2$ origin averages on a
superpolynomial schedule at the same time. Faster actual-start relaxation
at $N^{-2/3}$ and deterministic noise removal remain open, as do
BGS-TRACE-005 and BGS-BGS-001. Prior intensity-loss obstructions are
recorded in [the return note](../returns/return_trace_obstruction.md).
