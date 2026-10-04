# Fixed-time bounded traces for the unchanged odd-dimensional map

**Claim ID: BGS-FM-013. Status: PROJECT PROOF + AUTHOR SELF-REVIEW.**
4 October 2026. This closes the bounded-trace input previously recorded
conditionally in [the source adaptation](quadratic_noise_fixed_time_input.md).
The method is standard fixed-time semiclassical wave-packet propagation;
no priority for that method, full trace expansion, external referee approval,
or Heisenberg-time estimate is asserted.

## 1. Statement and the prior result

Keep exactly the full odd-dimensional family

$$
U_N=e^{i\tau N A_N}M_N,
\quad \tau=10^{-80},\quad h=(2\pi N)^{-1},\quad
\kappa=\tau/(2\pi),\quad A_N=\operatorname{Op}_N(g),
$$

with the physical midpoint symbol and matrix convention of
[FM-001](fixed_model_symmetry_theorem.md). Its classical map is
$F=\Phi_g^{-\kappa}\circ S_0^{-1}$, $S_0=\left(\begin{smallmatrix}3&4\\2&3\end{smallmatrix}\right)$.
In particular, the momentum-dependent part of $g$ contains $r(q+1/2)$.

**Theorem.** For every fixed nonzero integer $j$ there are $C_j,N_j$
such that

$$
|\operatorname{Tr}U_N^j|\le C_j\qquad(N\ge N_j,\ N\text{ odd}). \tag{1}
$$

The constants and thresholds are not effective here and are not uniform
in $j$. In particular, no estimate is supplied for $j\asymp N$.
The earlier [FM-007 proof](frozen_seven_cut_reduction.md), (9)--(12),
already gives $O(N^{39/40})$ through a sufficiently short logarithmic
time window. Thus qualitative normalized fixed-time trace vanishing,
macroscopic phase equidistribution, and starting-noise ellipticity were
already available. The improvement in (1) is the bounded unnormalized
trace input; it does not extend that logarithmic window.

## 2. Exact finite-dimensional coherent frame

For $z=(q,p)\in[0,1]^2$, $x=0,\ldots,N-1$, define

$$
\psi_{z,N}(x)=\left(\frac2N\right)^{1/4}
\sum_{k\in\mathbb Z}
e^{-\pi N(x/N-q-k)^2}
e^{2\pi iNp(x/N-q-k)}.                                      \tag{2}
$$

All sums converge absolutely. The projectors are periodic in $q,p$:
the $p\mapsto p+1$ change is a common scalar. Direct integration gives

$$
N\int_{[0,1]^2}|\psi_{z,N}\rangle\langle\psi_{z,N}|\,dz=I_N.   \tag{3}
$$

Indeed the $p$ integral kills every term except
$x-y-N(k-l)=0$, hence $x=y,k=l$. The remaining $q$ integral is
$\int_{\mathbb R}e^{-2\pi Nt^2}dt=(2N)^{-1/2}$, which, multiplied
by the squared prefactor in (2), is $1/N$. Poisson summation also gives
$\|\psi_{z,N}\|^2=1+O(e^{-cN})$ uniformly in $z$, but exact
normalization is unnecessary for (3). For any matrix $B$,

$$
\operatorname{Tr}B=N\int\langle\psi_{z,N},B\psi_{z,N}\rangle dz. \tag{4}
$$

These identities hold at odd $N$; there is no import of an even-dimensional
trace formula or a distributional infinite operator trace.

## 3. Packet propagation, including the odd-N identification

Here are details of the analytic input, rather than treating one-step
Egorov as an all-order localization theorem. Set

$$
(\mathcal P_N f)(x)=N^{-1/2}\sum_{k\in\mathbb Z}f(x/N+k).
$$

For the normalized plane Gaussian
$f_{z,h}(t)=(\pi h)^{-1/4}e^{-(t-q)^2/(2h)}e^{ip(t-q)/h}$,
$\mathcal P_N f_{z,h}=\psi_{z,N}$. Ordinary plane Weyl quantization
of $e^{2\pi i(bq+ap)}$ intertwines exactly with
$W_N(a,b)=(-1)^{ab}T_N(a,b)$ under $\mathcal P_N$:

$$
(W_N(a,b)v)(x)=e^{2\pi ib(x+a/2)/N}v(x+a\bmod N).             \tag{5}
$$

Both multiplication and the shift follow directly from the sampling sum.
For odd $N$, $2^{-1}=(N+1)/2$ modulo $N$, so the factor $(-1)^{ab}$
is essential in (5). Consequently
$\mathcal P_N\operatorname{Op}_h(g)=A_N\mathcal P_N$ exactly.

The physical lattice translations act on $\mathcal P_N$ with character
$(-1)^{Nn_1n_2}$. Since $S_0^{\pm1}\equiv I\pmod2$, their plane
metaplectic lifts preserve this character. This descent can be checked on the dual combs
$\sum_k\delta(t-x/N-k)$: invariance under integer position translation
and multiplication by $e^{2\pi iNt}$ characterizes their N-dimensional
span. The preserved lattice character therefore makes the descent
well-defined. Poisson summation for the plane Fourier transform gives
the normalized finite Fourier transform; quadratic phase multipliers
give the corresponding unitary finite chirps (with the intermediate
boundary character retained). Their metaplectic compositions therefore
give a unitary descent. The induced finite operator has the same Weyl
conjugation as $M_N$, hence equals it up to a unit scalar: the finite
clock and shift matrices have scalar commutant.
Choose that scalar once to obtain
$\mathcal P_N\mu\,f=M_N\mathcal P_N f$ for the lift whose packet
center is $S_0^{-1}z$. This identifies the actual quantization, not a
different matrix with only approximate Egorov. Projective phases have
no effect on the bounds below.

For completeness, a finite-order packet construction is sufficient.
During the kick use the plane Hamiltonian $H=-g$ for time $\kappa$.
Its trajectory has center $z(t)=\Phi_g^{-t}z(0)$. Remove the trajectory
translation and action and rescale both coordinates by $\sqrt h$.
Let $H_r(t)$ denote the homogeneous degree-$r$ Taylor polynomial of
$H$ at $z(t)$ in these rescaled variables. The constant and linear
terms are canceled by the action and trajectory equations. The remaining
Schrodinger equation has quadratic term $\operatorname{Op}_1(H_2)$
and higher terms $h^{r/2}\operatorname{Op}_1(H_{r+2})$, $r\ge1$.
For a truncation order $L$, solve the triangular equations

$$
i\partial_t a_\ell=operatorname{Op}_1(H_2)a_\ell+
\sum_{r=1}^{\ell}\operatorname{Op}_1(H_{r+2})a_{\ell-r},
\qquad 0\le\ell\le L.                                      \tag{6}
$$

Initially $a_0$ is a Gaussian and $a_\ell=0$ for $\ell>0$.
For a polynomial-Gaussian input the same construction applies termwise.
The quadratic propagator is metaplectic. At any fixed time it takes a
polynomial times a Gaussian to another such packet; the positive Gaussian
width remains bounded above and below on a fixed compact time interval.
Duhamel in (6) thus gives polynomial-Gaussian envelopes with bounded
Schwartz seminorms. The bounds are uniform in initial $z$, since the
symbol is periodic and the trajectories and derivatives for fixed $j$
remain in a bounded set of lifts.

The Taylor remainder has the required operator meaning here. The symbol
$g$ is a finite Fourier polynomial. Each Fourier mode, after translating
and rescaling, is an exponential of a linear combination of position
and momentum multiplied by $\sqrt h$. Taylor's formula with integral
remainder for that exponential on Schwartz functions bounds the omitted
degree-$r$ term by $C h^{r/2}$ in every fixed Schwartz seminorm, using
finitely many higher seminorms of the input. No unbounded polynomial
operator is estimated on the whole Hilbert space. In the original
$ih\partial_t$ equation, the ansatz
$\sum_{\ell=0}^L h^{\ell/2}a_\ell$ therefore has residual
$O(h^{(L+3)/2})$ in the packet norm and the needed weighted seminorms.

Sampling preserves this residual estimate. For any uniformly Schwartz
envelope $b$, Cauchy--Schwarz on the sampling sum and the mesh
$1/(N\sqrt h)$ give a uniform bound on
$\|\mathcal P_N[h^{-1/4}b((t-q_0)/\sqrt h)e^{ip_0(t-q_0)/h}]\|$.
For example a fixed bound on $\sup_y(1+|y|)^2|b(y)|$ suffices;
the sum of the corresponding decaying mesh weights is $O(N\sqrt h)$.
This also applies to the remainder, uniformly in packet center and phase.
Equation (5), followed by finite-dimensional unitary Duhamel, then gives
an error $O(h^{(L+1)/2})$. There is no application of an unbounded
sampling map to an arbitrary small $L^2(\mathbb R)$ error.

Alternate these kick approximations with the exact metaplectic action
for the $j$ cat steps. For fixed positive $j$ and $L=5$ one obtains a
finite sum of polynomial-Gaussian packets centered at $F^jz$, plus
an error $O_j(h^3)$ in the finite-dimensional norm, uniformly in $z$.
All coefficients are bounded for this fixed $j$. This is the usual
fixed-time packet argument, reconstructed for the finite Fourier symbol
and the odd-N sampling convention. General coherent-state/FIO covariance
is prior; see Guillemin--Uribe--Wang, Theorem 1.1 and Section 5.3,
[source mapping](../literature/expansion_wavepacket_sources_20261004.md).
Their theorem is corroborating background, not a substituted torus trace
identity.

## 4. Overlap and trace bound

Poisson summation of two periodized polynomial-Gaussian packets gives,
uniformly in their centers, the overlap bound

$$
|\langle\psi_{z,N},U_N^j\psi_{z,N}\rangle|
\le C_{j,M}\left(1+\frac{\operatorname{dist}(F^jz,z)}{\sqrt h}\right)^{-M}
+C_jh^3                                                      \tag{7}
$$

for every fixed $M$. To see the phase-space, rather than position-only,
decay: each product Gaussian sum has spatial-center decay, while its
Fourier transform has momentum-center decay. Poisson summation sums
these bounds over the integer position and momentum shifts. The resulting
lattice Gaussian is bounded by $C e^{-c_j\operatorname{dist}^2/h}$;
the finite polynomial factors can be absorbed into a weaker Gaussian
or any fixed power in (7). Constants depend on the fixed covariance
matrices and degrees, which were bounded in Section 3. The remainder
in (7) follows from the uniform norm bound for (2).

By FM-001, $F$ is Anosov. For fixed $j>0$, every fixed point of $F^j$
is nondegenerate: $DF^j-I$ is invertible by stable/unstable hyperbolicity.
The fixed points are isolated and finite by compactness. The inverse
function theorem near each, and positive separation elsewhere, imply

$$
|\{z:\operatorname{dist}(F^jz,z)\le r\}|\le C_jr^2
\quad(0<r<r_j).                                             \tag{8}
$$

For $M>2$, a dyadic decomposition of (8) gives

$$
\int\left(1+\operatorname{dist}(F^jz,z)/\sqrt h\right)^{-M}dz
=O_j(h).
$$

Insert (7) into the exact trace identity (4):
$|\operatorname{Tr}U_N^j|\le C_jNh+C_jNh^3=O_j(1)$, since
$Nh=1/(2\pi)$. Negative powers follow by unitarity and complex conjugation.
This proves (1) without evaluating a regularized plane trace.

## 5. Closed inputs and what remains open

For each fixed finite list of powers, the initial unnormalized traces
are now uniformly bounded; subsequences with convergent initial traces
exist. Convergence of those traces along all odd $N$ is not proved.
FLOW-004/005 can use some finite bound on $|p_1|+|p_2|$ for sufficiently
large $N$; this proof does not supply the numerical choice $K=20$.
The sharp limsup constants in the historical FM-013 source adaptation,
or the complete action-phase trace formula, remain conditional there.

The exact FLOW-003 inequality now has $|m_2|=O(N^{-1})$, so its actual
starting covariance has spectral bounds $1-O(N^{-1})$ and
$2+O(N^{-1})$ after the stated normalization, and whitening norm
$1+O(N^{-1})$. Earlier ellipticity was already implied by FM-007.
Neither bounded fixed traces nor this strengthened covariance rate
removes external randomness or controls resonant Heisenberg traces.
**BGS-TRACE-005 and BGS-BGS-001 remain OPEN.**
