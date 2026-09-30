# Fixed-map spectral statistics: exact reductions and the remaining estimate

**Claim IDs:** `BGS-FM-005`, `BGS-FM-006`, `BGS-FM-007`, `BGS-FM-008`, `BGS-FM-009`, `BGS-FM-010`, `BGS-FM-011`, `BGS-FM-012`, `BGS-RES-005`, `BGS-RES-006`, `BGS-RES-007`, `BGS-LOOP-001`, `BGS-TRACE-005`, `BGS-TRACE-007`, `BGS-TRACE-008`, `BGS-CUE-001`, `BGS-FLOW-001`, `BGS-FLOW-002`, `BGS-FLOW-003`, `BGS-FLOW-004`, `BGS-FLOW-005`, `BGS-FLOW-006`, `BGS-FLOW-007`, `BGS-FLOW-008`, `BGS-FLOW-009`, `BGS-FLOW-010`, `BGS-FM-013`, `BGS-BGS-001`

**Status, 29 September 2026.** The fixed-map BGS target is open. This chapter
consolidates the recovered research, states a conditional all-order criterion,
and proves what its first two mixed levels imply. The
[supplement](../supplement/fixed_map/README.md) contains full derivations,
programs, finite certificates and dated audits. External priority is not
claimed. Formalization covers only explicitly stated algebraic kernels.

## The unchanged target

For odd $N\ge3$, use raw modular Weyl operators

$$
(T_N(a,b)\psi)(x)=e_N\bigl(b(x+2^{-1}a)\bigr)\psi(x+a),
\qquad e_N(t)=\exp(2\pi i t/N),
$$

with modular inverses. Let $S=\left(\begin{smallmatrix}3&4\\2&3\end{smallmatrix}\right)$ and

$$
(M_N)_{xy}=N^{-1/2}e_N\bigl(-8^{-1}(3x^2-2xy+3y^2)\bigr),
\qquad U_N=\exp(i\tau N A_N)M_N,\quad \tau=10^{-80}.
$$

Here $A_N$ quantizes $f-1/10$ using $e^{2\pi i(kq+lp)}\mapsto T_N(l,k)$,
where

$$
\begin{split}
r(q)&=(1-\cos14\pi q)(1+\cos2\pi q),\\
f(q,p)&=\cos14\pi q+\frac{r(q)}{10}
 +\frac{r(q)\sin2\pi q}{100}
 +\frac{r(q)\cos(2\pi p-\alpha_0)}{100},\\
e^{i\alpha_0}&=(-3+4i)/5.
\end{split}
$$

Centering changes only a common spectral rotation. Neither an auxiliary
coupling average nor independent phases replace this fixed family.

Writing $p_m=\operatorname{Tr}U_N^m$, the pair target can be expressed as

$$
L_N(s):=N^{-2}\sum_{m\ge1}e^{-2sm/N}|p_m|^2
 \longrightarrow \frac{1-e^{-2s}}{4s^2},\qquad s>0.
$$

The [determinant-ratio reduction](../supplement/fixed_map/weighted-secular/determinant_boundary.md)
proves equivalence with all compact weighted pair tests, with an explicit
positive-definite tail bound. No estimate establishing this limit for the
displayed $U_N$ has been obtained. All-order universality needs more than
this pair target.

## An exact adjoint-resolvent form of the pair target

**Claim ID:** `BGS-RES-006`. This identity is finite-dimensional and holds
for every unitary $N\times N$ matrix, not just the frozen family. On the
Hilbert--Schmidt space $M_N(\mathbb C)$ define

$$
\mathcal U_N(X)=U_N XU_N^*,\qquad
\mathcal D_N=\frac{N^2}{4}\left(2I-\mathcal U_N-\mathcal U_N^*\right),\qquad
T_N(s)=\frac1N\operatorname{Tr}_{HS}(\mathcal D_N+s^2I)^{-1}.
$$

The map $\mathcal U_N$ is unitary on Hilbert--Schmidt space, so
$\mathcal D_N\ge0$. If $e^{i\theta_j}$ are the eigenvalues of $U_N$, the
matrix units in its eigenbasis diagonalize $\mathcal D_N$, with eigenvalues
$N^2\sin^2((\theta_j-\theta_k)/2)$. Summing the Poisson series with
$q=e^{-2s/N}$ gives the exact identity

$$
1+2L_N(s)=N\sinh(s/N)\cosh(s/N)\,T_N\!\left(N\sinh(s/N)\right).
$$

For every unitary spectrum and every $s>0$ one also has the uniform comparison

$$
0\le \frac{1+2L_N(s)}{s}-T_N(s)
\le \frac{2}{3N}\cosh(2s/N).                         \tag{R1}
$$

To see the sign and the error, set $a=s/N$ and
$y_{jk}=N^2\sin^2((\theta_j-\theta_k)/2)$. The ratio of the $(j,k)$ summand
in $(1+2L_N(s))/s$ to its summand in $T_N(s)$ is

$$
\frac{\sinh(2a)}{2a}\,\frac{y_{jk}+s^2}{y_{jk}+N^2\sinh^2a}.
$$

It lies between $1$ and $\sinh(2a)/(2a)$. Also
$T_N(s)\le N/s^2$, and
$\sinh x/x-1\le x^2\cosh(x)/6$ for $x\ge0$, which proves (R1).
Consequently, for each fixed $s>0$,

$$
L_N(s)\longrightarrow\frac{1-e^{-2s}}{4s^2}
\quad\Longleftrightarrow\quad
T_N(s)\longrightarrow\frac1s+\frac{1-e^{-2s}}{2s^3}.
$$

This is a reformulation of the same open pair limit. It gives no estimate
for $T_N(s)$ for the prescribed $U_N$ and no higher-order joint-trace
comparison. The detailed audit and the companion exact
[spectral-flow and control identities](frozen_spectral_flow_controls.md)
also rule out collapsing the actual iterated kicks into an unordered single
exponential; they do not estimate the ordered product at $m\asymp N$.

## A universal finite-dimensional Abel floor

**Claim ID:** `BGS-TRACE-007`. Every $N$-point unitary spectrum satisfies

$$
L_N(s)\ge \frac1{e^{2s}-1},\qquad s>0,                 \tag{R2}
$$

and the bound is attained by a rotated regular $N$-gon. Here is the precise
energy reduction. For $N=1$ the bound is equality directly. For $N\ge2$, put
$z_j=e^{i\theta_j}$ and

$$
f_q(r)=\frac{1-q^2}{(1-q)^2+qr},\qquad 0<q<1.
$$

This is strictly completely monotone on $[0,4]$. The regular $N$-gon is a
sharp configuration on $S^1$: it is a circular $(N-1)$-design and has
$\lfloor N/2\rfloor$ distinct inner products between different vertices.
Cohn--Kumar, Theorem 1.2 in
[*Universally optimal distribution of points on spheres*](https://arxiv.org/abs/math/0607446v2),
therefore minimizes $\sum_{j\ne k}f_q(|z_j-z_k|^2)$. The diagonal terms of
the full ordered sum are configuration-independent. If eigenangles
coincide, perturb them to distinct angles and pass to the limit; $f_q$ is
continuous at zero. Since

$$
\frac{1-q^2}{|1-qe^{it}|^2}
=\sum_{m\in\mathbb Z}q^{|m|}e^{imt},
$$

the minimized full sum is $N^2+2\sum_{m\ge1}q^m|p_m|^2$. For the regular
polygon $p_m=N$ exactly when $N\mid m$, and is zero otherwise. Taking
$q=e^{-2s/N}$ yields (R2).

The CUE benchmark is strictly above this floor:

$$
\frac{1-e^{-2s}}{4s^2}-\frac1{e^{2s}-1}
=\frac{e^{-s}(\sinh^2s-s^2)}{2s^2\sinh s}>0.
$$

Thus (R2) is a sharp universal lower bound but does not identify the frozen
model's limit or give a uniform excess over the clock value.

## Smooth resolvent transfer for the seven-cut *full* propagator

**Claim ID:** `BGS-RES-007`. Let $U_N$ and $V_N$ be the original and
seven-cut **full** propagators of [`BGS-FM-007`](frozen_seven_cut_reduction.md).
For an arbitrary unitary $W$ write $L_{W,N}$ and $T_{W,N}$ for the pair
Abel and adjoint-resolvent functions above. For every compact
$K\subset(0,\infty)$ and every integer $r\ge0$, there are constants
$C_{K,r},N_{K,r}$ such that, for odd $N\ge N_{K,r}$,

$$
\sup_{s\in K}|\partial_s^r(L_{U,N}(s)-L_{V,N}(s))|
 \le C_{K,r}\frac{\tau}{\log N},                         \tag{R3}
$$

$$
\sup_{s\in K}|\partial_s^r(T_{U,N}(s)-T_{V,N}(s))|
 \le C_{K,r}\left(\frac{\tau}{\log N}+\frac1N\right). \tag{R4}
$$

Thus $T_{U,N}-T_{V,N}\to0$ in $C^\infty_{\rm loc}(0,\infty)$.
This is equivalence of any possible scalar-resolvent limits, not
convergence of either resolvent to the CUE value.

**Proof.** Formula (13) of `BGS-FM-007` expresses $L_{W,N}$ as
$\frac12 C_{2,N}^W(h_s)$ plus terms independent of $W$, where
$h_s(x)=s/(s^2+\pi^2x^2)$. All Abel series and their fixed-order
$s$ derivatives converge absolutely on $K$ at each $N$. For every $r$,
the derivatives $\partial_s^r h_s$ and their $x$ derivatives have
uniformly summable unit-interval suprema as $s$ runs over $K$;
the $x$ derivative is $O_{K,r}(|x|^{-3})$ at infinity. Apply the
phase-coupling estimate (7) there to these differentiated tests.
Its coupled total displacement is $O(\tau)$, and the seven-cut
occupancy is $O(N/\log N)$. The spectrum-independent terms cancel,
giving (R3) uniformly on $K$.

It remains to pass from the Abel functions to the resolvents **with
derivatives**, since (R1) alone bounds only their values. Set
$y_{jk}=N^2\sin^2((\theta_j-\theta_k)/2)$,
$c_N(s)=\sinh(2s/N)/(2s/N)$, and
$b_N(s)=N^2\sinh^2(s/N)$. The exact identity preceding (R1) gives

$$
R_{W,N}(s):=\frac{1+2L_{W,N}(s)}s-T_{W,N}(s)
=\frac1N\sum_{j,k=1}^N\left[
 \frac{c_N(s)}{y_{jk}+b_N(s)}-\frac1{y_{jk}+s^2}\right]. \tag{R5}
$$

On a fixed small complex neighborhood of $K$ in $\Re s>0$ and for all
sufficiently large $N$, the expansions
$c_N(s)=1+O_K(N^{-2})$ and $b_N(s)=s^2+O_K(N^{-2})$
hold uniformly. Both denominators have modulus at least
$c_K(1+y_{jk})$ there. Hence each bracket in (R5) is bounded by
$C_KN^{-2}/(1+y_{jk})$. The $N^2$ terms and the exterior $1/N$
give $\sup |R_{W,N}|\le C_K/N$ uniformly over **every** unitary $W$.
Cauchy's derivative estimates on a slightly smaller neighborhood yield
$\sup_{s\in K}|\partial_s^rR_{W,N}(s)|\le C_{K,r}/N$.
Subtract (R5) for $U_N,V_N$ and use (R3), together with the bounded
derivatives of $1/s$ on $K$, to obtain (R4). $\square$

The proof exploits the already established full-propagator phase coupling;
it neither decomposes $V_N$ into independent spectra nor evaluates
its scalar resolvent at Heisenberg times. The all-order mixed-resolvent
obligation `BGS-TRACE-005` therefore remains open. The separate
[`BGS-TRACE-008` two-clock example](two_clock_gram_falsifier.md)
also proves that the necessary Gram moment $4/3$, simple phases,
macroscopic Haar convergence, uniformly bounded unfolded unit occupancy
and nonvanishing traces cannot replace that obligation.

## What the recovered work establishes

For the actual frozen kick, the [exact Jacobi-chain decomposition](frozen_kick_rank_boundary.md)
has $\gcd(N,7)$ irreducible blocks for every odd dimension. With the cited
Hermite--Lindemann input, it implies
$\operatorname{rank}(U_N-zM_N)\ge N-\gcd(N,7)$ for every complex $z$ and
every nonzero algebraic coupling. Its approximate-rank bound applies only
before eigenphase wrapping, $|\tau N|(79/50)\le\pi$; it supplies no fixed-strength
asymptotic control. Separately, the [full-lag classical gap](frozen_full_lag_resonance.md)
proves a uniform translated Riesz bound for the exact physical symbol under
the *linear* cat map, including small weighted-Fourier perturbations. It
does not treat transport by the nonlinear kicked map. The
[nonlinear bracket pressure theorem](nonlinear_bracket_pressure.md) shows
that this same $\lambda^{-r}$ normalization cannot have a uniform upper
bound for the **actual** nonlinear map: its individual bracket norms grow
at a strictly larger exponential rate. This result is classical and uses
thermodynamic-formalism inputs; none of these results bounds the
Heisenberg-scale joint traces needed for `BGS-TRACE-005`.

An [exact seven-cut reduction](frozen_seven_cut_reduction.md) now gives
$\|U_N-e^{i\tau N A_N^{\rm cut}}M_N\|_1\le28\pi^2\tau/(25N)$
for the same fixed coupling. The two **full** propagators have equivalent
fixed-order sine-kernel targets. Their pair and full Abel statistics differ
by $O_s(\tau/\log N)$ without assuming a CUE limit. The seven paths
belong only to the generator: every proper union of paths exchanges
Hilbert–Schmidt mass $d(N-d)/N$ with its complement under the full
propagator. Thus `BGS-TRACE-005` can be attacked for either full
propagator, with no claim of independent seven-block spectra. The
[all-minor and simple-spectrum theorem](frozen_algebraic_spectral_simplicity.md)
removes exact level multiplicity when $7\nmid N$, while the
[integer commutator-cube certificate](frozen_common_antireversor_certificate.md)
excludes a common antiunitary reversal of $(A_N,M_N)$ except at $N=7$.
These results are qualitative and do not estimate near-degenerate spacings.
The [arithmetic trace identity and rigidity theorem](frozen_arithmetic_trace_rigidity.md)
also proves exact nonvanishing of every $\operatorname{Tr}U_N^m$
on the odd sequence and classifies scalar powers. The
[effective gap floor](frozen_effective_gap_floor.md) makes spectral
simplicity quantitative for $7\nmid N$, but its bound is far below
the mean spacing $N^{-1}$. Neither result supplies an upper bound for
Heisenberg-time traces or the open Abel limit.

Exact algebraic arguments exclude scalar-algebraic returns for the stated
frozen family except its explicitly treated raw $N=7$ exception. They do not
give microscopic eigenvalue separation. The new qualitative simplicity
theorem covers all odd $7\nmid N$, whereas the older *quantitative*
finite-size certificates cover only specified dimensions. Structured ergodic comparison
controls unfolded RMS motion of subprincipal perturbations under its stated
Egorov and ergodicity hypotheses; transferring factorial correlations also
needs local occupation moments.

The block-memory analysis distinguishes closed quantum propagation from
reset evolution. Mixing of the positive reset chain does not imply decay
of coherent quantum memory. Actual weighted principal-minor computations
show cancellation within and across frequency windows. They do not justify
independent-phase substitution. A rotated deleted clock has exactly the
CUE characteristic-polynomial covariance and nevertheless regular spacings;
covariance alone therefore does not determine pair statistics.

Full statements, assumptions and proofs are in the topic-indexed supplement.
The [shadow-tube analysis](shadow_tube_history_bridge.md), recovered from the
remote branch, likewise keeps its geometric equidistribution assumption
separate from its proved symbolic filling bound. Both local and remote
research lines are retained.

## A conditional route to every compact correlation order

For eigenangles $\theta_j$ in radians and a uniform common origin
$\alpha\in[0,2\pi)$, put

$$
s_N(w)=\frac1N\sum_j\cot\left(\frac{\theta_j-\alpha}{2}-\frac wN\right).
$$

This Herglotz function has unit-mass particles at
$N(\theta_j-\alpha)/2+\pi N\ell$, and intensity $1/\pi$.
Define, using holomorphic extension at coincident arguments,

$$
\begin{split}
\mathcal E_{p,N}(\mathbf w)={}&
\mathbb E[(s_N(w_1)^2+1)\prod_{j=2}^p s_N(w_j)]\\
&+\sum_{j=2}^p\mathbb E\left[
\partial_{w_j}\frac{s_N(w_1)-s_N(w_j)}{w_1-w_j}
\prod_{\ell=2,\ell\ne j}^p s_N(w_\ell)\right].
\end{split}
$$

Theorem 1.9 of Bourgade--Huang,
[*Loop Equations Characterize Random Matrix Statistics*, arXiv:2607.07617v2](https://arxiv.org/abs/2607.07617v2),
provides the external convergence theorem. Our sufficient model hypothesis is

$$
\sup_{\mathbf w\in K^p}
\frac{|\mathcal E_{p,N}(\mathbf w)|}
 {1+\mathbb E\max_j|s_N(w_j)|^{p+1}}\longrightarrow0
$$

for every fixed $p$ and every compact $K\subset\mathbb C\setminus\mathbb R$.
The event in that theorem is the whole origin probability space. Its moment
bootstrap then bounds all local particle-count moments, since
$\mu_N([-B,B])\le(1+B^2)|s_N(i)|$. Uniform integrability upgrades weak
point-process convergence to all compact factorial correlation tests.
Dividing positions by $\pi$ and integrating the origin gives exactly the
usual deterministic anchored statistic, with normalization $1/N$.
The [detailed bridge](../supplement/fixed_map/resolvent-flow/loop_bridge.md)
checks these steps. This is a conditional implication; the model hypothesis
is unproved. It does not assert pointwise correlation densities.

## The first two mixed equations

For arguments in the same half-plane every loop residual vanishes for
every unitary spectrum. Indeed, the nonconstant Fourier frequencies in the
uniform origin all have the same strict sign. Such tests cannot verify
universality.

Fix $s>0$, $w=is/2$, $v=-is/2$, $q=e^{-2s/N}$, and define

$$
C_N=N^{-3}\sum_{a,b\ge1}q^{a+b}p_{-a}p_{-b}p_{a+b}.
$$

Absolute Fourier convergence gives the exact mixed identity

$$
\mathcal E_{2,N}(w,v)=8i\left(L_N+C_N-\frac1{4s^2}\right).
$$

The cubic quantity $C_N$ need not be real. Finite circular CUE satisfies
$\mathbb E(L_N+C_N)=1/(4N^2\sinh^2(s/N))$, so the limiting straight-line
equation has a finite-size correction even in the reference ensemble.

Put $Z=s_N(w)$, $M_r=\mathbb E|Z|^r$,
$e_2=L_N+\Re C_N-1/(4s^2)$, and $e_3=\mathcal E_{3,N}(w,v,v)$.
Then

$$
e_3=M_4-1-\frac2{s^2}(M_2+1)\in\mathbb R.
$$

To prove this, write $T=s_N(v)=\bar Z$. Same-half-plane identities give
$\mathbb ET^2=-1$ and $\mathbb E(T'T)=0$. Each differentiated quotient,
multiplied by $T$, has expectation $-(M_2+1)/s^2$. There are two such
terms; the leading expectation is $M_4-1$.

For $P=(Z/i-1)/2$ and $Q=\mathbb E|P|^4$, Fourier orthogonality yields
$M_2=1+4L_N$ and $M_4=1+16L_N+32\Re C_N+16Q$. Eliminating $C_N$ gives

$$
Q=\left(1+\frac1{2s^2}\right)L_N-\frac1{4s^2}
       +\frac{e_3}{16}-2e_2.
$$

Consequently $Q\ge L_N^2$ implies

$$
L_N^2-\left(1+\frac1{2s^2}\right)L_N+\frac1{4s^2}
 \le\frac{e_3}{16}-2e_2.
$$

These conclusions require no probabilistic independence. If
$|e_3|\le\delta_N(1+M_4)$ with $\delta_N\to0$, Jensen gives, for
$x=M_2$ and $t=s^{-2}$,

$$
(1-\delta_N)x^2-2tx-(1+\delta_N+2t)\le0.
$$

Thus $M_2,M_4$ are bounded and $e_3\to0$. A normalized vanishing $p=2$
residual now also vanishes without normalization. Every subsequential
limit $\ell$ of $L_N(s)$ lies in

$$
\frac12+\frac1{4s^2}-\frac12\sqrt{1+\frac1{4s^4}}
 \le\ell\le\frac1{2s^2}.
$$

The interval has positive width. These low-order bounds do not identify
the CUE value or prove convergence; no realizable non-CUE process satisfying
the two vanishing residuals is asserted either. Establishing those residual
hypotheses for the actual map remains a dynamical problem.

## Why a direct noise replacement does not close the estimate

There is also an exact identity for depolarizing noise. Let
$\mathcal P_N(X)=\operatorname{Tr}(X)I/N$ and
$\Phi_{\eta,N}=e^{-\eta}\mathcal U_N+(1-e^{-\eta})\mathcal P_N$ for
$\eta\ge0$. The scalar matrices have eigenvalue $1$ under $\Phi_{\eta,N}$;
on traceless matrices it acts as $e^{-\eta}\mathcal U_N$. Therefore

$$
\operatorname{Tr}_{HS}\Phi_{\eta,N}^m
=1+e^{-m\eta}(|p_m|^2-1).
$$

For
$L_{\eta,N}(s)=N^{-2}\sum_{m\ge1}e^{-2sm/N}\operatorname{Tr}_{HS}\Phi_{\eta,N}^m$,
this gives

$$
L_{\eta,N}(s)=L_N(s+N\eta/2)+\rho_N(s,\eta),\qquad
\rho_N(s,\eta)=\frac1{N^2}\sum_{m\ge1}e^{-2sm/N}(1-e^{-m\eta}),
$$

with $0\le\rho_N(s,\eta)\le(2Ns)^{-1}$. Noise shifts the unknown
parameter from $s$ to $s+N\eta/2$; this identity alone does not recover the
fixed-$s$ pair limit or control Heisenberg-time traces.

For the unitary Brownian generator $G=(2N)^{-1}\sum_a D_{H_a}^2$, with
$\operatorname{Tr}(H_aH_b)=\delta_{ab}$, matrix completeness gives

$$
G|p_m|^2=m^2-m|p_m|^2-
 \frac mN\Re\left(\bar p_m\sum_{a=1}^{m-1}p_a p_{m-a}\right).
$$

Hence exactly

$$
\frac1N GL_N(s)=\frac12\partial_s
 \left[L_N(s)+\Re C_N(s)-\frac{q}{N^2(1-q)^2}\right].
$$

The unknown mixed defect reappears in the attempt to remove noise. For an
exact clock it is nonzero. Moreover, transport directions $V^jAV^{-j}$
have identical diagonal entries in a simple eigenbasis of $V$; Gaussian
linear combinations therefore give rank at most one for instantaneous
eigenphase covariance. Nonlinear bracket effects are not excluded.

A separate elementary obstruction concerns global entropy. On the unfolded
circle of length $N$, let $d_N$ be RMS matching distance to a deterministic
configuration, minimized over permutations and common rotation. Labeled
CUE density is at most $1/N!$ by Hadamard's inequality. A rotation mesh
and a union of Euclidean balls therefore give

$$
Q_N(d_N\le\delta)\le
 \min\left\{1,\left\lceil\frac N\delta\right\rceil
                   (\sqrt{8\pi e}\,\delta)^N\right\}.
$$

Binary relative-entropy contraction shows that $d_N\to0$ in $P_N$
probability forces $D(P_N\Vert Q_N)/N\to\infty$. Thus global entropy
$o(N)$ and microscopic RMS preservation cannot both justify the proposed
comparison. This does not exclude local entropy methods or universality.
The [full proof](../supplement/fixed_map/resolvent-flow/entropy_obstruction.md)
includes the torus-volume and labeling factors.

## The singular reference boundary and a coboundary control

The [Haar-CUE reference proof](cue_singular_energy.md) (BGS-CUE-001)
evaluates an unregularized object beyond the fixed-positive-$s$
pair Abel statistic: if $F_{N,2}=\sum_{j\ne k}
|e^{i\theta_j}-e^{i\theta_k}|^{-2}$, then
$\mathbb EF_{N,2}=N(N^2-1)/6$ while its variance
is infinite. Centered $N^{-8/3}F_{N,2}$ has a
spectrally positive $3/2$-stable law, derived from the
published Haar-CUE small-gap Poisson limit and a
project determinantal tail bound. The same proof covers
inverse chord powers $3/2<p<3$.
Moving one eigenphase by $O(N^{-1})$ can preserve
weak local process limits while making the normalized
unregularized inverse-gap energy diverge. Therefore
neither a weak local limit nor the exact positive-$s$
adjoint-resolvent identity permits taking the singular
boundary without an additional gap/uniform-integrability
estimate. None has been established for the maintained
fixed propagator.

The [finite coboundary spectral-flow theorem](coboundary_spectral_flow_bound.md)
(BGS-FLOW-001) controls RMS unfolded phase motion by an
adjoint Birkhoff average of $H=iN[G,UGU^*]$, with
explicit higher-order commutator errors and a sharp
abstract clock example. Its needed logarithmic-time
average and nested-commutator bounds remain unproved
for the frozen family. The related infinitesimal
calculation (BGS-FLOW-002) shows that Gaussian
coboundary kicks produce a sine drift and no radial
Dyson diffusion. The second-order three-exponential
normal form itself was previously proved in
[the Pell coboundary note](pell_coboundary_resonance.md).
These observations leave the mixed Heisenberg-time
trace obligation unchanged.

## Audited periodic-point control from the 27 September upload

The [all-time annihilator theorem](frozen_periodic_point_annihilator.md)
(`BGS-FM-012`) writes
$C^m=\left(\begin{smallmatrix}x_m&2y_m\\y_m&x_m\end{smallmatrix}\right)$
for $C=\left(\begin{smallmatrix}1&2\\1&1\end{smallmatrix}\right)$,
$C^2=S$, and proves

$$
(S^m-I)^T\mathbb Z^2=
\begin{cases}2x_m\mathbb Z^2,&m\text{ odd},\\
2y_m\mathbb Z\times4y_m\mathbb Z,&m\text{ even}.
\end{cases}
$$

Thus the physical ordinary symbol averages exactly $-1/10,-1/20,0$
over the linear-cat fixed-point sets at times $1,2,\ge3$. This unweighted
identity does not estimate an oscillatory Birkhoff sum or quantum trace.
The [submission audit](../record/cue_upload_review_20260927.md) rejects
the proposed upgrade from pair-only TG-mean estimates to all-order CUE.
It also corrects the submitted ordinary-symbol translation, bispectrum
Fourier sign, distinct-index convention and Abel cutoff accuracy.
These controls do not change the Heisenberg-scale joint-trace obligation.

## Quadratic noise and its deterministic-transfer boundary

The [quadratic-noise theorem](quadratic_coboundary_noise.md)
(`BGS-FLOW-003`) goes beyond the second-order radial obstruction. For
normalized GUE $G$, put $X=i[G,UGU^*]/\sqrt2-\mathbb E(i[G,UGU^*]/\sqrt2)$
and $m_2=\operatorname{Tr}U^2/N$. Its exact covariance obeys

$$
\frac{1-|m_2|}{N}\operatorname{Tr}T^2
\le\mathbb E(\operatorname{Tr}XT)^2
\le\frac{2+|m_2|}{N}\operatorname{Tr}T^2
$$

for every traceless Hermitian $T$. It is nonsingular precisely when the
spectrum is not contained in two antipodal points. Inverting the square
root of its covariance yields the infinitesimal traceless Dyson generator.
The raw noise is different: for $N\ge4$,
$\int\mathcal L_X|\operatorname{Tr}U^2|^2\,d\mathrm{Haar}=4+2/N^2$.

For a compactly supported smooth local pair statistic, microscopic-time
generators differ by at most
$C_{R,\phi}|m_2|M^2(1+\log N)+2N^{-2}\sup|x^2\phi''|$
if every mean-spacing arc contains at most $M$ phases. That occupancy
bound and its propagation are not proved for the frozen map. A quadratic
noise built from $d$ Gaussian directions has covariance rank at most
$d(d+1)/2$; finitely many smooth directions and logarithmically many
frozen-frame time translates do not yield full instantaneous radial rank.
None of these results supplies deterministic noise removal or the required
all-order Heisenberg trace comparison.

## Quantitative quadratic-noise dynamics: a scoped continuation

The [coupling theorem](quadratic_noise_coupling.md) (`BGS-FLOW-004`)
compares the raw diffusion $U_t$ with traceless unitary Brownian motion
$V_t$ from the same matrix. For $0\le t\le1$,

$$
N\mathbb E\|U_t-V_t\|_{\rm HS}^2
\le10e^3t(1+|\operatorname{Tr}U_0|^2+|\operatorname{Tr}U_0^2|^2).
$$

Symmetry of the covariance square root cancels the relative Itô
commutator. Every-even-moment estimates strengthen this to
$N\|U_{t_N}-V_{t_N}\|_{\rm op}\to0$ in probability when the initial
first two traces are bounded and $t_N\log N\to0$. A separate integrated
translation estimate gives phase-averaged local Laplace and finite-count
comparison for every $t_N\to0$ with bounded initial low traces, without
an occupancy assumption. It does not give unbounded correlation moments.

The [reversible correction](quadratic_noise_reversibility.md)
(`BGS-FLOW-005`) is the commuting traceless Hermitian drift

$$
A=-\operatorname{Im}[(m_2+m_1^2/2)U^{*2}+(m_2\bar m_1/2)U^*],
\qquad m_j=N^{-1}\operatorname{Tr}U^j.
$$

Adding $D_A$ puts the generator in Haar divergence form. Moreover
$A=-(4N)^{-1}\operatorname{grad}(|p_2|^2+N^{-1}\operatorname{Re}(p_2\bar p_1^2))$.
For $N\ge4K$, initial $|p_1|,|p_2|\le K/2$, and $t\le1/12$,
Girsanov and an explicit exit estimate give

$$
d_{\rm TV}(P_X^{[0,t]},P_R^{[0,t]})
\le\min(1,2K\sqrt t+16e^{-K^2/(768t)}).
$$

This compares full path laws with the same covariance, not path laws
with Dyson covariance. Haar reversibility does not imply ergodicity;
scalar matrices are absorbing.

The [fixed-trace theorem](quadratic_noise_trace_fluctuations.md)
(`BGS-FLOW-006`) assumes every fixed initial trace is uniformly bounded
and the selected initial traces converge. For fixed $K,T$, it proves
joint path convergence to independent circular complex OU processes
with variance coefficient $b_k^2=k^2(1+\mathbf1_{k=2}/2)$ and rates

$$
a_X(k)=k/2-\mathbf1_{k=2}/2,\qquad
a_R(k)=k/2+\mathbf1_{k=2}/2.
$$

Uniform maximal trace moments justify the limit. From zero initial
traces the raw second-trace variance is $6(1-e^{-t})$, whereas Dyson
has $2(1-e^{-2t})$. Their difference prohibits microscopic operator
coupling at fixed positive time. The reversible limit has variance
$2(1-e^{-3t})$, with Haar-compatible stationary value two; no finite-$N$
stationary convergence or growing-order theorem is implied.

For the odd clock start, the [local-limit theorem](quadratic_noise_clock_limit.md)
(`BGS-FLOW-007`) uses the established circular Dyson clock kernel of
Forrester, with a rederived odd-$N$ normalization and explicit alias
bound. Both quadratic diffusions converge after phase averaging to
Sine$_2$ at $t_N\to0$, $Nt_N\to\infty$, with Laplace error
$O_f(\sqrt t+(Nt)^{-1}+N^{-2})$. The initial clock has exactly one point
per unit interval while Sine$_2$ has a positive hole probability.
Thus low traces and bounded occupancy cannot justify generic noise removal.

The [fixed-time model input](quadratic_noise_fixed_time_input.md)
(`BGS-FM-013`) is **conditional**. Its parity repair is exact, but the
full regularized trace and quantization/remainder identification for
Faure's plane estimate remain to be checked. No even-dimensional torus
theorem is silently applied to odd dimensions. These auxiliary results
leave `BGS-TRACE-005` and `BGS-BGS-001` open. The
[research audit](../record/quadratic_noise_review_20260929.md) separates
proofs, finite controls, prior work and the conditional application.

## From finite coboundary kicks to a spectral diffusion

The [fourth-order calculation](coboundary_fourth_order_drift.md)
(`BGS-FLOW-008`) distinguishes the actual step
$U\mapsto e^{i\varepsilon(G-UGU^*)}U$ from the raw quadratic diffusion.
In its conjugated logarithm, the expected second-degree Hermitian field
is $J=-\operatorname{Im}(m_1U^*)$; a further fourth-degree drift remains
even after frozen subtraction of $J$. Thus covariance alone cannot
identify the limit. Both logarithmic mean terms vanish at $m_1=0$.

The [Möbius reduction](coboundary_mobius_diffusion.md)
(`BGS-FLOW-009`) uses
$\Pi(U)=(U-wI)(I-\bar wU)^{-1}$, with the small $w$ chosen to set
$\operatorname{Tr}\Pi(U)=0$. The faster field $J$ lies on common
Möbius orbits. Phase-averaged local Laplace functionals change by
$O_f(|m_1|)$ under centering, without an occupancy assumption.
At fixed dimension, killed trace moments control the fast mode and
identify the stopped spectral quotient limit at step $\varepsilon^4/2$
with generator $\overline Lf=L_X(f\circ\Pi)$ on the centered slice.
The projected diffusion has an explicit additional Itô drift of operator
norm at most $80/N^2$ for $|m_2|\le1/2$; it admits a dimension-uniform
short-time comparison with Dyson motion.

Consequently, for independent normalized GUE kicks and odd clock start,
if $t_N\to0$ and $Nt_N\to\infty$,

$$
\lim_{N\to\infty,\ N\ {\rm odd}}\limsup_{\varepsilon\downarrow0}
\left|\mathbb E\Phi_{N,f}
 (U^\varepsilon_{\lfloor2t_N/\varepsilon^4\rfloor})
-\Phi_{\rm Sine}(f)\right|=0.
$$

The chain contains no centering drift or covariance whitening. This proof
first fixes dimension; the following extension supplies an explicit joint
regime. No convergence of the original matrix paths is asserted. The initial clock remains
a counterexample to generic noise removal. This auxiliary theorem does not
establish the deterministic map's Heisenberg joint-trace estimate. The
[continuation audit](../record/coboundary_mobius_review_20260929.md) records
the proof obligations, exact algebra and finite projection checks.

## A dimension-quantitative joint regime for the random chain

The [uniform-step theorem](coboundary_joint_limit.md) (`BGS-FLOW-010`)
strengthens the fast-coordinate estimate to
$\mathbb E[|m_1|;j<\sigma]\le C(\varepsilon/N+\varepsilon^4)$.
Its full quartic mean and absolute sixth-order remainder are retained.
Smooth localization gives backward derivative growth $e^{CNt}$;
a discrete second-trace Lyapunov estimate controls exits directly.
For smooth nonnegative compactly supported tests, the original chain obeys

$$
\left|\mathbb E\Phi_{N,f}
 (U^\varepsilon_{\lfloor2t/\varepsilon^4\rfloor})
-\Phi_{\rm Sine}(f)\right|
\le C_f[\sqrt t+(Nt)^{-1}+N^{-2}+N^{20}e^{CNt}\varepsilon],
\qquad 1/N\le t\le1/12.
$$

Hence $\varepsilon_N=e^{-N}$, $t_N\to0$ and $Nt_N\to\infty$ give
a simultaneous local weak limit. At $t_N=N^{-2/3}$ the smooth-test rate
is $O_f(N^{-1/3})$. Nonnegative $C_c^1$ tests follow by approximation,
without this rate. The exponential step count is not practical, and no
polynomial-step theorem or deterministic noise removal follows. The
[author audit](../record/coboundary_joint_review_20260930.md) separates
the analytic proof from exact algebra and finite Frechet-gradient checks.

## Verification and remaining work

The recovered supplement includes exact arithmetic replay, an independent
C++ verifier, independent matrix assemblies and numerical identity checks.
The new quartic relation was checked in 27 finite cases and by a separate
internal algebra audit. Its source code and proof are retained. Auxiliary
kick strengths in these tests do not resolve $\tau=10^{-80}$.

The Lean module `CueLoopKernels` states the cubic positive-part identity
and a cleared-denominator elimination kernel over integers. These are a
small algebraic layer; they do not formalize the analytic loop criterion.
Current compilation results are recorded in the publication review.

The remaining task is a model-specific Heisenberg-scale cancellation
estimate for the actual mixed resolvent products, or an equally strong
direct trace comparison. No noise approximation, source theorem or finite
computation in this chapter supplies that missing estimate.
