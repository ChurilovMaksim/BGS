# Clock relaxation under quadratic noise and the noise-removal boundary

**Claim ID: BGS-FLOW-007.** Project derivation and author self-review,
29 September 2026. The circular Dyson clock kernel is prior work of
Forrester; see [the exact-source review](../../literature/quadratic_noise_sources_20260929.md).
No priority or deterministic BGS claim is made.

## 1. Statement

Let $N=2M+1\ge3$, $C_N=\operatorname{diag}(e^{2\pi ij/N})_{j=0}^{N-1}$.
Start either the raw quadratic diffusion of
[FLOW-003](quadratic_coboundary_noise.md) or its
[reversible correction](quadratic_noise_reversibility.md) at $C_N$.
If $t_N\to0$ and $Nt_N\to\infty$, its unfolded point process viewed
from an independent uniform angle converges weakly to Sine$_2$.
For nonnegative $f\in C_c^1(\mathbb R)$ its averaged Laplace functional obeys

$$
|\mathbb E\Phi_{N,f}(U_t)-\Phi_{\rm Sine}(f)|
\le C_f[\sqrt t+(Nt)^{-1}+N^{-2}] \tag{1}
$$

for sufficiently large odd $N$, $Nt\ge1$, $0<t\le1/12$.
In particular $t=N^{-2/3}$ gives an $O_f(N^{-1/3})$ bound.
This is an auxiliary stochastic theorem from a special starting spectrum.
It does not assert convergence of its unbounded correlation moments.

## 2. Exact odd-dimensional Dyson kernel

Fix the full unitary Brownian angle generator as

$$
L_D=\frac1{2N}\sum_j\partial_j^2+
 \frac1{2N}\sum_j\sum_{k\ne j}
 \cot\frac{\theta_j-\theta_k}{2}\,\partial_j.
$$

Its scalar heat kernel relative to angle Lebesgue measure is
$q_t(x)=(2\pi)^{-1}\sum_{k\in\mathbb Z}e^{-tk^2/(2N)}e^{ikx}$.
The positive circular Vandermonde on an ordered chamber is proportional
to $h(\theta)=\det[e^{-il\theta_j}]_{l=-M}^M$ up to a constant phase.
It obeys $\partial_j\log h=\frac12\sum_{k\ne j}\cot((\theta_j-\theta_k)/2)$
and $\sum_j\partial_j^2h=-(\sum_l l^2)h$.
For odd $N$, a cyclic wrap has positive permutation sign. The determinant
of the periodic scalar heat kernels is consequently the absorbing chamber
kernel, and its Doob transform by $h$ has generator $L_D$.
Multiplication by $h(\theta)/h(a)$ and the scalar eigenvalue exponential
gives the transition density, a product of two determinants.

For $a_j=a_0+2\pi j/N$, finite Fourier inversion gives biorthogonal functions

$$
\phi_l(x)=e^{-ilx},\qquad
\psi_l(y)=\frac1{2\pi}\sum_{r\in\mathbb Z}
 e^{-t((l+rN)^2-l^2)/(2N)}e^{i(l+rN)y-irNa_0}.
$$

Each $\psi_l$ is a linear combination of $q_t(y-a_j)$, multiplied by
$e^{tl^2/(2N)}$. The identity
$\int_0^{2\pi}\phi_k\psi_l=\delta_{kl}$ follows since
$l+rN=k$, $|l|,|k|\le M$, forces $r=0,k=l$.
Integration of the determinant density therefore gives the exact kernel

$$
K_{N,t}(x,y)=\sum_{l=-M}^M\phi_l(x)\psi_l(y). \tag{2}
$$

This kernel need not be Hermitian. Positivity comes from the transition
density; inequalities requiring a Hermitian kernel are not used below.

## 3. Uniform local bound and passage to Laplace functionals

Set $x=\alpha+2\pi u/N$, $y=\alpha+2\pi v/N$, and
$\kappa=(2\pi/N)K_{N,t}$. The $r=0$ part is

$$
\kappa_0(u,v)=\frac{\sin\pi(v-u)}{N\sin(\pi(v-u)/N)}. \tag{3}
$$

Pairing $r$ and $-r$ and summing over $l$ bounds the absolute remainder,
uniformly in all phases, by

$$
R_{N,t}=\frac1N\sum_{r\ge1}
e^{-Nt r(r-1)/2}\frac{1-e^{-Nrt}}{\sinh(rt/2)}
\le\frac2{Nt}\left[1+\frac1{2(e^{Nt}-1)}\right]
\le\frac3{Nt},\quad Nt\ge1. \tag{4}
$$

Use $\sinh(rt/2)\ge rt/2$, $r(r-1)/2\ge r-1$, and $1/r\le1/2$
for $r\ge2$. On any fixed compact window, (3) differs from the sine
kernel by $O(N^{-2})$. Thus the kernel error is
$O((Nt)^{-1}+N^{-2})$.

If its entries are bounded by $C$, each correlation determinant is
bounded in absolute value by $k^{k/2}C^k$ (Hadamard). The Fredholm
expansion on a compact interval $I$ is absolutely and uniformly
summable, since $\sum_k k^{k/2}(C|I|)^k/k!<\infty$.
Multilinearity gives the same summable majorant with one additional
factor $k$ for differences. Consequently the Dyson Laplace error is
$C_f[(Nt)^{-1}+N^{-2}]$. This argument is valid for the possibly
non-Hermitian kernel (2).

The reference process in [FLOW-004](quadratic_noise_coupling.md) is
traceless Brownian motion. Multiplication by an independent scalar
$e^{ib_t/N}$ gives full unitary Brownian motion. A uniform observation
angle removes this common translation exactly, so the same averaged
Laplace bound applies to the traceless process.

## 4. Transfer to the two quadratic diffusions

At the clock, $p_1=p_2=0$. FLOW-004 bounds the raw-to-Dyson averaged
Laplace error by $\|f'\|_1\sqrt{10e^3t}/4$, proving (1) for the raw law.
For the reversible law, use FLOW-005 with $K=1$, $N\ge4$:
the endpoint total variation is at most
$2\sqrt t+16e^{-1/(768t)}=O(\sqrt t)$ on $0<t\le1/12$.
This proves (1) for it as well. Tightness follows from unit mean local
intensity after phase averaging, and the Laplace limits identify Sine$_2$.

## 5. Why this cannot remove the added noise

The initial unfolded clock is $\mathbb Z+\operatorname{Unif}[0,1)$;
every unit interval contains exactly one point almost surely. Moreover
$p_j=0$ for all $1\le j<N$ and the local occupancies are bounded.
Sine$_2$ has a strictly positive probability of a hole in $[0,1]$:
its restricted sine-kernel operator is a positive compact contraction
of trace one and has no eigenvalue one. Such an eigenvector would yield
a nonzero function both compactly supported and bandlimited, excluded
by analyticity of the inverse Fourier transform. Its norm is therefore
strictly less than one, and its summable eigenvalues give
$\det(I-K_{[0,1]})>0$.

The weak limit has no points at the interval endpoints, so its interval
count law is the limit of the noisy counts. Their total-variation
distance from the initial clock count has a positive limiting lower
bound, this hole probability. Thus vanishing low traces and bounded
local occupancy cannot by themselves justify deterministic noise removal.
This is not a counterexample to BGS for chaotic systems.

There is also a separate elementary obstruction to conjugation-based
arguments. The fields $Y_G(U)=i[G,U]$ and all their Lie brackets annihilate
class functions, even for smooth state-dependent $G$. They cannot
generate radial Dyson motion. The quadratic fields $i[G,UGU^*]U$ are
different. In the BCH expansion of exact conjugation,

$$
e^{i\varepsilon G}Ue^{-i\varepsilon G}U^*
=\exp\left(i\varepsilon(G-UGU^*)+
 \frac{\varepsilon^2}{2}[G,UGU^*]+O(\varepsilon^3)\right),
$$

the commutator correction is essential to isospectrality.

## Verification scope

The companion clock verifier compares (2) with an independently assembled
heat/Gram kernel, checks finite truncation bounds, and computes an
illustrative sine-hole quadrature. These complex128 calculations do not
prove the infinite-dimensional limit. The proof is the argument above;
the Dyson clock mechanism is credited to the established literature.
