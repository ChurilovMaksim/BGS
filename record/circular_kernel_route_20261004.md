# Direct circular-kernel route: actual-start relaxation closed

This is an executed research route at base
`4982f8fc3d6303cc2cf7840e608f07d41ba2783e`.
The scoped stochastic result is [FLOW-014](../mathematics/circular_dyson_actual_start.md);
deterministic BGS remains open and priority is unestablished.
The exact arbitrary-start determinantal mechanism is **prior work**:
Kieburg, Li, Zhang and Forrester, arXiv:2012.11993v2, Proposition 12,
(2.4.10), Theorem 7(3), and Proposition 21, (3.2.2)--(3.2.3).
The source and application boundary are pinned in
[the source check](../literature/actual_start_dyson_sources_20261004.md).

## Exact finite target and recovered formula

Use the project's normalized full unitary Brownian motion with
$\mathbb EB_t=e^{-t/2}I$. Traceless Brownian motion has the same
uniform-origin observables, since the omitted scalar component supplies
only an independent common rotation. For odd $N=2L+1$, distinct initial
angles $\alpha_j$, and Haar angular measure $d\theta/(2\pi)$, put

$$
q_j(\phi)=\sum_{m\in\mathbb Z}e^{-tm^2/(2N)}e^{im(\phi-\alpha_j)},
\quad V_{\ell j}=e^{i\ell\alpha_j},\quad -L\le\ell\le L,
$$

$$
R_j(\theta)=\sum_{\ell=-L}^L(V^{-1})_{j\ell}
e^{t\ell^2/(2N)}e^{i\ell\theta},\qquad
K_{N,t}^{\alpha}(\theta,\phi)=\sum_{j=1}^NR_j(\theta)q_j(\phi).
\tag{K1}
$$

The source heat parameter is $t/(2N)$; using $t$ directly would change
the model. Direct Fourier integration, **without conjugating one factor**,
gives $\int R_jq_k=\delta_{jk}$, hence $K^2=K$ and $\int K(\theta,\theta)=N$.
The centered initial angles, rather than a clock, must be used in (K1).
The displayed finite formula assumes distinct angles. FLOW-014 handles
repeated initial levels through a gap-independent Laplace bound and
finite-N continuity, rather than an uncontrolled Vandermonde inverse.
The equivalent Lagrange polynomial is

$$
\sum_{\ell=-L}^L(V^{-1})_{j\ell}e^{i\ell\zeta}
=e^{iL\alpha_j-iL\zeta}
\prod_{k\ne j}\frac{e^{i\zeta}-e^{i\alpha_k}}
{e^{i\alpha_j}-e^{i\alpha_k}}.
\tag{K2}
$$

The backward heat factor in $R_j$ has the Gaussian representation
$\sqrt{N/(2\pi t)}\int_{\mathbb R}e^{-Ny^2/(2t)}
(\text{K2 at }\zeta=\theta+iy)\,dy$.
It is exact because the integrand is a finite Fourier polynomial.
Replacing the numerator by the complete product retains
$(e^{i\zeta}-e^{i\alpha_j})^{-1}$ as an amplitude.
Converting only its complete numerator to a sine product leaves an
$e^{i\zeta/2}$ prefactor while the exponential denominator is retained.
Converting that denominator as well cancels the prefactor: FLOW-014 (U7)
uses the exact complete sine-product quotient with
$2\sin((\zeta-\alpha_j)/2)$ in its denominator. Dropping a factor in a
partially converted formula would not be an exact identity.

At a clock, discrete Fourier inversion gives the existing FLOW-007 alias
kernel

$$
K_{N,t}(\theta,\phi)=
\sum_{\ell=-L}^{L}\sum_{r\in\mathbb Z}
e^{-t[(\ell+rN)^2-\ell^2]/(2N)}
e^{i\ell\theta-i(\ell+rN)\phi}.
\tag{K3}
$$

Finite controls compare (K1) and (K3), check the bilinear Gram matrix,
and verify the trace in both clock and warped initial configurations.
They do not simulate Brownian paths or certify a limiting kernel.

## Local input, closed global implication, and normalization checks

[FM-017](../mathematics/frozen_mesoscopic_regularity.md) supplies the
actual centered initial Herglotz bounds at a logarithmic scale. At
$t_N=\sqrt{4\log J_N/J_N}$ its local phase has two stationary points
near $\theta\pm it_N/2$, uniformly in the observation angle, with
controlled nonzero Hessians. Its real logarithmic potential also gives
an exponential uniform bound on the **unweighted** vertical phase tails.
This closes the local stationary-point and pure vertical-phase steps.
By itself it does not control the full kernel's amplitudes or contours.

The discriminating global step is now proved in FLOW-014. Summing the
interpolation residues first removes the individual $P'(\alpha_j)$
denominators. A period rectangle retains an extra residue $-Q_\phi(u)$;
rearrangement adds its full positive crossing term. The odd-N sine signs
cancel between numerator and denominator under every winding shift.
The resulting Gaussian prefactor is $N/t$.

A wider initial strip, beginning at $t/8$, is essential: controlling the
function only to the edge of a $t/4$ strip would not justify a uniform
Cauchy derivative bound at that edge. The corrected strip gives global
horizontal convexity and vertical concavity of the action. The real-axis
barrier is inherited from FM-017's potential estimate.
The remaining crossing singularity is $1/|u-z|$ in two real dimensions;
it is an ordinary absolutely integrable singularity, including when the
saddle and pole coincide. A uniform Gaussian-pole integral and period-cell
summation bound the remainder by $C_R\sqrt{N/t}$.

The crossing term, with every nonzero winding exponentially controlled,
gives the sine kernel after division by $N$ and unfolding by $N/(2\pi)$.
Hadamard and column-telescoping estimates control the entire Fredholm
series. Repeated initial levels pass through the uniform bounded Laplace
law by finite-N continuity. No initial minimum-gap assumption is added.

The general proof sharpens the actual time to $t_N=8g_N$,
$g_N=4\log J_N/J_N$, since then its $t_N/8$ strip is exactly the verified
initial scale. Balancing FLOW-012 with
$\varepsilon_N=N^{-9}/\sqrt{t_N}$ and
$n_N=\lfloor2t_N^3N^{36}\rfloor$ gives the original-chain Sine$_2$ law
with error $O_f(\sqrt{g_N})$. Its original starting matrix stays $U_N$.

The [independent internal audit](general_start_review_20261004.md) checks
the new analytic implications, without upgrading inherited proofs to
external referee certification. The separately bounded residue verifier
compares the formula against Fourier inversion on both sides of each
contour; finite quadrature is not the asymptotic proof.

## First remaining deterministic discriminator

Neither the initial logarithmic regularity nor the noisy sine law proves
$\Phi_{N,f}(U_N)-\mathbb E\Phi_{N,f}(U_{n_N}^{\varepsilon_N})\to0$.
The existing clock theorem already falsifies generic microscopic noise
removal from low traces and global density alone. Spectral rounding under
weak Egorov axioms is also a prior repository obstruction, not a new route.
The next successful argument must use additional actual-map information
or prove the signed Heisenberg hierarchy directly. Faster actual-start
relaxation, unbounded-correlation transfer for the chain, deterministic
noise removal and BGS remain open. No new finite-kernel priority or
general BGS conclusion is claimed.
