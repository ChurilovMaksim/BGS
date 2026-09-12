# Short quantum returns obstruct ergodic local spectral limits

**Status:** project proof with adversarial self-review. Finite computations are
separate evidence. The positivity mechanism has close published antecedents;
priority is unverified. Cat-map applications depend on the existing return-law
proofs, whose limited internal-review status is unchanged. BGS remains open.

## 1. Local processes and a uniform necessary condition

Let $U_D$ be a deterministic or random unitary of dimension $D\to\infty$.
Write its eigenphases, with multiplicities, as $\theta_j\in\mathbb R/\mathbb Z$
and $t_D(m)=D^{-1}\operatorname{Tr}U_D^m$.
For an independent uniform circle origin $X_D$, define the locally finite
counting measure
$$
 \Xi_D=\sum_{j=1}^D\sum_{\ell\in\mathbb Z}
                    \delta_{D(\theta_j-X_D+\ell)}.                 \tag{S1}
$$
This is stationary under real translations and has intensity one at each
finite dimension. Local-process convergence means convergence in law in the
vague topology, allowing multiplicities. Ergodicity means that every event
invariant under all real translations has probability zero or one.

**Theorem 1.** If $\Xi_D$ converges to a stationary ergodic process $\Xi$ of
intensity one, then for every integer $M_D\ge1$ with $M_D=o(D)$,
$$
             \mathbb E\max_{1\le m\le M_D}|t_D(m)|\longrightarrow0. \tag{S2}
$$
Consequently, for any $1\le K_D=o(D)$ the empirical eigenvalue law of
$U_D^{K_D}$ tends to Haar measure in probability. For deterministic spectra
this is ordinary weak convergence. No second-moment or pair-correlation
convergence hypothesis is imposed.

**Proof.** Choose a measurable maximizing integer $q_D\in[1,M_D]$, breaking
ties by the smallest index. It may depend on the spectrum. Put
$\zeta_D=\overline{t_D(q_D)}/|t_D(q_D)|$ when the denominator is nonzero,
and $\zeta_D=1$ otherwise. Introduce the mark
$$
                         Z_D=\zeta_D e^{2\pi i q_D X_D}.           \tag{S3}
$$
Conditionally on the spectrum this mark is Haar on the unit circle.
Joint tightness gives a subsequential limit $(\Xi,Z)$ along every subsequence.
Replacing $X_D$ by $X_D+a/D$ translates $\Xi_D$ by $-a$ and multiplies its
mark by $e^{2\pi i q_Da/D}$. The latter tends uniformly to one. The joint
limit is thus invariant under translations of $\Xi$ leaving $Z$ fixed.

Such an invariant coupling with an ergodic first marginal is a product
coupling. Indeed, for any bounded real $b(Z)$ the conditional expectation
$\mathbb E[b(Z)\mid\Xi]$ is invariant under translations, hence constant
almost surely. A countable determining family of $b$ proves independence.
In particular $\mathbb E[Z\langle\Xi,\psi\rangle]=0$ for integrable local
linear statistics, since $Z$ is Haar.

Choose $\psi\ge0$ continuous and compactly supported with $\int\psi>0$,
and use $\widehat\psi(\xi)=\int\psi(y)e^{-2\pi i\xi y}\,dy$.
Both $\mathbb E\langle\Xi_D,\psi\rangle$ and
$\mathbb E\langle\Xi,\psi\rangle$ equal $\int\psi$.
Nonnegative random variables converging in law with convergent means are
uniformly integrable: apply convergence to $y\wedge R$, subtract from the
means to control $(y-R)_+$, and then let $R\to\infty$.
This permits passage to the marked first moment; no corresponding assertion
about squared local counts is used.

An exact change of variables in the circle-origin integral gives
$$
 \mathbb E[Z_D\langle\Xi_D,\psi\rangle\mid U_D]
                     =|t_D(q_D)|\widehat\psi(q_D/D).             \tag{S4}
$$
The substitution is $y=D(\theta_j-X_D+\ell)$; integer $q_D$ makes the
winding phase one. Since $q_D/D\to0$ uniformly, the expectation of the right
side is $(\int\psi)\mathbb E|t_D(q_D)|+o(1)$, whereas the left side tends
to zero. Every subsequence has such a further subsequence, proving (S2).
Apply (S2) to each fixed multiple of $K_D$ and approximate continuous circle
functions by trigonometric polynomials to obtain the Haar conclusion.

**Strengthening (all slowly varying tests).** Under the hypotheses of
Theorem 1, let
$$
 \mathfrak d_M(\nu,dx)=
 \sup_{\substack{f:\mathbb R/\mathbb Z\to\mathbb R\\
                 \|f\|_\infty\le1,\ \operatorname{Lip}(f)\le M}}
                \left|\int f\,d\nu-\int f\,dx\right|.
$$
For the empirical phase measure $\nu_D=D^{-1}\sum_j\delta_{\theta_j}$,
$$
             \mathbb E\mathfrak d_{M_D}(\nu_D,dx)\to0
                         \qquad(M_D=o(D),\ M_D\ge1).             \tag{S2a}
$$
Choose a spectrum-dependent real test $f_D$ within $D^{-1}$ of the supremum,
with sign giving a nonnegative discrepancy. Such a measurable choice exists
by taking the first suitable member of a countable dense subset of the
compact Lipschitz ball. Replace (S3) by the bounded real mark
$Z_D=f_D(X_D)-\int f_D\in[-2,2]$.
It has mean zero conditionally on the spectrum and changes by at most
$M_D|a|/D$ under a local translation. The same invariant-coupling and
uniform-integrability proof applies. The replacement for (S4) is
$$
 \mathbb E[Z_D\langle\Xi_D,\psi\rangle\mid U_D]
 =\left(\int\psi\right)\left(\int f_D\,d\nu_D-\int f_D\right)+E_D,
 \qquad |E_D|\le\frac{M_D}{D}\int |y|\psi(y)\,dy.
$$
The left side tends to zero, proving (S2a).

In particular, for every $0<w_D\le1$ with $Dw_D\to\infty$, the mesoscopic
empirical density $\rho_{D,w}(x)=w^{-1}\nu_D([x,x+w])$ satisfies
$$
                  \mathbb E\|\rho_{D,w_D}-1\|_{L^1}\to0.        \tag{S2b}
$$
Indeed, duality against any real $a$ with $|a|\le1$ converts this density
error to a phase-measure discrepancy tested by
$f_a(\theta)=w^{-1}\int_{\theta-w}^{\theta}a(x)dx$.
This test is bounded by one and has Lipschitz constant at most $2/w$.
Apply (S2a) with $M_D=2/w_D$. Thus an ergodic intensity-one local limit
forces uniform density in spatial $L^1$ on every window containing a
diverging number of mean spacings. No rate of mixing or quantitative rate
of local-process convergence was assumed.

## 2. The conditional intensity encoded by a return law

Suppose the spectra are deterministic, $K_D=o(D)$, and their $K_D$-folded
laws converge to a probability measure $\mu$. Suppose a local-process
subsequence converges with intensity one. Attach the unrotated mark
$Y_D=K_DX_D\bmod1$. Every joint limit $(\Xi,Y)$ is invariant under translating
$\Xi$ with $Y$ fixed, and $Y$ is uniform. The same first-moment argument for
all Fourier characters shows that $\mu$ must be absolutely continuous and
$$
 \mathbb E[\langle\Xi,\psi\rangle\mid Y=y]
             =\rho(y)\int\psi,\qquad d\mu(y)=\rho(y)\,dy.        \tag{S5}
$$
To verify the absolute continuity, the measure
$B\mapsto\mathbb E[\mathbf1_{Y\in B}\langle\Xi,\psi\rangle]$
is absolutely continuous with respect to the uniform law of $Y$. Its Fourier
coefficients equal those of $(\int\psi)\mu$ by (S4) without phase alignment.
Uniqueness of Fourier coefficients proves both assertions.
A nonconstant return density therefore forces nonergodicity of any local
limit preserving intensity one. A singular return law precludes such an
intensity-preserving limit. No conditional spacing law is identified by (S5).

## 3. A finite positive-Fourier pair inequality

For Schwartz $\phi$ define the ordered factorial statistic
$$
 C_D(U;\phi)=D^{-1}\sum_{j\ne l}\sum_{n\in\mathbb Z}
                      \phi(D(\theta_j-\theta_l+n)).              \tag{S6}
$$
Put $\phi_L(x)=e^{-\pi x^2/L^2}$ for $L>0$. Poisson summation gives exactly
$$
 C_D(U;\phi_L)=L\sum_{m\in\mathbb Z}e^{-\pi L^2m^2/D^2}|t_D(m)|^2
                         -\sum_{n\in\mathbb Z}e^{-\pi D^2n^2/L^2}.
                                                                  \tag{S7}
$$
All sums converge absolutely. For any distinct positive integers $q_1,\ldots,q_R$,
$$
 C_D(U;\phi_L)\ge
 L\left(1+2\sum_{r=1}^R e^{-\pi L^2q_r^2/D^2}|t_D(q_r)|^2\right)
                         -\sum_{n\in\mathbb Z}e^{-\pi D^2n^2/L^2}.
                                                                  \tag{S8}
$$
The subtracted sum is the diagonal term; at fixed $L$ it tends to one.
Dropping that term is false even in dimension one. Positivity also permits
any probability average over spectra.

If $K_D=o(D)$ and $t_D(rK_D)\to a_r$ for every fixed $r$, first taking the
limit at finite $R$, then increasing $R$, gives
$$
 \liminf_D C_D(U;\phi_L)\ge
                   L\left(1+2\sum_{r\ge1}|a_r|^2\right)-1.       \tag{S9}
$$
An infinite sum means divergence to positive infinity. There is no exchange
of an uncontrolled infinite sum and a limit. If the folded law has an $L^2$
density $\rho$, the parenthesis is $\int\rho^2$ by Parseval.
For random spectra, $L^2$ trace convergence implies the averaged version;
convergence in probability implies each finite-$R$ lower bound in probability.

**Corollary 2.** If $C_D(U;\phi)\to\int\phi\rho_2$ for all Schwartz tests,
where $\rho_2$ is bounded and $\rho_2(x)\to1$ at infinity, then every
sublinear-frequency maximum in (S2) tends to zero for deterministic spectra.
Indeed, a retained modulus $a>0$ would imply
$\int\phi_L\rho_2\ge L(1+2a^2)-1$ for every fixed $L$. But dominated
convergence after $x=Ly$ gives $L^{-1}\int\phi_L\rho_2\to1$ as $L\to\infty$.
This is a separate argument from Theorem 1; weak process convergence was not
silently promoted to convergence of pair moments.

For the Poisson target $C_{\rm P}(\phi_L)=L$. For the sine-kernel target
$\rho_{2,\rm sine}(x)=1-(\sin(\pi x)/(\pi x))^2$,
$$
 C_{\rm sine}(\phi_L)=L-\operatorname{erf}(\sqrt\pi L)
                         +\frac{1-e^{-\pi L^2}}{\pi L},
 \qquad0\le C_{\rm sine}(\phi_L)-L+1\le\frac1{\pi L}.            \tag{S10}
$$
The transform of the squared sinc is $(1-|\xi|)_+$; integration gives the
formula. The bound follows from
$\operatorname{erfc}(x)\le e^{-x^2}/(\sqrt\pi x)$, obtained by bounding
$\int_x^\infty e^{-u^2}du$ by $x^{-1}\int_x^\infty u e^{-u^2}du$.

Under convergence to these respective Gaussian pair targets, (S8) implies,
for every fixed $\delta>0$,
$$
 \limsup_D\sum_{1\le m\le\delta D}|t_D(m)|^2\le
 \begin{cases}\sqrt{\pi e/2}\,\delta,&\text{Poisson},\\
                 (e/2)\,\delta^2,&\text{sine kernel}.
 \end{cases}                                                     \tag{S11}
$$
For Poisson minimize $e^{\pi L^2\delta^2}/(2L)$ at
$L^2=(2\pi\delta^2)^{-1}$. For the sine kernel minimize
$e^{\pi L^2\delta^2}/(2\pi L^2)$ at $L^2=(\pi\delta^2)^{-1}$.
The same argument applies to averaged pair convergence and squared traces.
These are necessary budgets, not sufficient criteria.

## 4. Consequences for the cat-map programme

Use the hypotheses and convention of
[the general return theorem](general_cat_return_laws.md): a fixed hyperbolic
matrix, a fixed real mean-zero Gevrey symbol, and its explicit arithmetic
subsequence with $K\asymp\log N$. Take $D=N$, or $D=(N-1)/2$ on the odd
space for an even symbol. These are the stated sectors, not an assertion
that every possible arithmetic symmetry has been removed.

For $\epsilon_K\to0$, positive $\sigma_A^2(f)$, and
$K\epsilon_K^2\to v<\infty$, the existing return theorem gives
$$
             t_D(rK)\longrightarrow e^{-r^2v\sigma_A^2(f)/2}
                          \quad(r\text{ fixed}).                 \tag{S12}
$$
Its small-amplitude condition holds eventually for each fixed $r$.
Thus Theorem 1 excludes any ergodic stationary intensity-one local limit.
For $v>0$, (S9) gives the explicit pair obstruction
$$
 \liminf C_D(U_{\epsilon_K,f};\phi_L)
   \ge L\Theta(v\sigma_A^2(f))-1,
 \qquad\Theta(a)=\sum_{r\in\mathbb Z}e^{-ar^2}>1.                \tag{S13}
$$
Already $L>e^{v\sigma_A^2(f)}/2$ separates the bound using only $r=1$
from both Poisson and sine-kernel pair targets.
A necessary condition for either an ergodic intensity-one local limit or the
decorrelating pair limits in Corollary 2 is therefore
$$
                          K\epsilon_K^2\longrightarrow\infty.   \tag{S14}
$$
Otherwise take a subsequence with a finite limit $v$ and apply (S12).
With $\hbar_N=(2\pi N)^{-1}$ and $\kappa_K=\hbar_N\epsilon_K$, this is
$|\kappa_K|N\sqrt K\to\infty$ within the stated shrinking-quantum-kick
regime. It is not a sufficient threshold or a theorem about fixed nonzero
classical strength.

For $v=0$, all return moments tend to one and (S9) diverges for each $L$.
In fact the local process tends to the empty process. Fix $0<\eta<1/2$
and let $b_D(\eta)$ be the fraction of folded phases outside distance $\eta$
from zero. The probability that a window of unfolded length $L$ meets a
level is bounded by
$$
                          2\eta+KL/D+L b_D(\eta).                \tag{S15}
$$
Good levels lie in $K$ arcs of total length $2\eta$; enlarge them by the
window length. Bad levels contribute at most their expected window count.
Since the folded law tends to a point mass, first let $D\to\infty$, then
$\eta\downarrow0$. The finite mean density one is lost in this weak limit.
For zero $\sigma_A^2(f)$ and $\epsilon_K\to0$, the existing operator-norm
return estimate gives the same point-mass return and empty local limit.

In the sampled-harmonic family of
[pell_harmonic_returns.md](pell_harmonic_returns.md), the $L^2$ limit
$t_D(K)\to e^{-\tau^2/2}$ holds for every $\beta\in[0,1/2]$ and fixed $\tau$.
The harmonic-averaged local process therefore has no ergodic intensity-one
limit. Averaged Poisson and sine-kernel pair limits are excluded; a fixed
$L>e^{\tau^2}/2$ also gives a positive pair-test gap in probability. This
includes the free-unitary-Brownian return endpoint.

If $\|\widetilde U_D-U_D\|_{\rm op}=\eta_D$ and $K_D\eta_D\to0$, telescoping
unitary powers gives, for every fixed positive integer $r$,
$$
 |D^{-1}\operatorname{Tr}\widetilde U_D^{rK_D}-t_D(rK_D)|
                            \le rK_D\eta_D\longrightarrow0.     \tag{S16}
$$
The exclusions persist under these $o(1/K_D)$ perturbations, which may be
larger than the mean spacing. Equality of classical principal maps alone
is not asserted to imply the required norm estimate.

## 5. Sharp boundaries and unfolding

A $D$-point clock has $t_D(D)=1$, while its local process is the uniformly
shifted integer lattice: stationary, ergodic under real translations, and
intensity one. Thus $o(D)$ cannot be replaced by $O(D)$ in Theorem 1.
The clock also has $t_D(m)=0$ for $1\le m<D$, and its coprime powers permute
the spectrum. Necessary short-return conditions are therefore not sufficient
for Poisson or sine-kernel statistics.

Ergodicity is essential. For $D=Kn$, $n\to\infty$, place
$$
 \theta_{b,j}=K^{-1}(b+j/(2n)),\qquad
                 0\le b<K,\quad0\le j<n.                        \tag{S17}
$$
Here $K$ can grow. Each unfolded length-$n$ cell is half filled by a
spacing-$1/2$ lattice and half empty. The local limit is an equal mixture of
that stationary lattice and the empty process, with intensity one but without
ergodicity. Boundary windows have probability $O(L/n)$. The folded law has
density $2\mathbf1_{[0,1/2]}$, and $|t_D(K)|\to2/\pi$.
The Gaussian pair limit is
$\sum_{j\ne0}e^{-\pi j^2/(4L^2)}=2L-1+O(Le^{-4\pi L^2})$.
This realizes (S5) and the leading density-square bound sharply.
Intensity preservation is also essential: coincident spectra have unit
return moments but an empty local limit of intensity zero.

Global mean-spacing unfolding is part of the statement. For $v>0$ the wrapped
Gaussian return density $\rho$ is smooth and strictly positive. Its CDF lift
$F(y)=\int_0^y\rho(u)du$ satisfies $F(y+1)=F(y)+1$, and
$$
                         H_K(\theta)=K^{-1}F(K\theta)            \tag{S18}
$$
is an increasing degree-one circle map. Its Lipschitz constant and inverse
Lipschitz constant are bounded independently of $K$. The transformed folded
law is Haar, so this density-dependent unfolding removes this particular
obstruction. It does not prove local universality after the change.

## 6. Prior work, checks, and the remaining gap

Aistleitner, Lachmann and Pausinger,
[*Pair correlations and equidistribution*](https://arxiv.org/abs/1612.05495),
Theorems 1–2, establish the Poissonian implication to equidistribution and a
density-square lower bound. Steinerberger,
[*Poissonian Pair Correlation in Higher Dimensions*](https://arxiv.org/abs/1812.10458),
Theorem 2, uses a positive Fourier kernel for quantitative low-frequency
exponential-sum bounds. Those principles are prior work. Priority for the
marked first-moment formulation here and its specific cat-map applications
has not been established.

The sine process satisfies the ergodicity hypothesis by Soshnikov,
[*Determinantal random point fields*](https://arxiv.org/abs/math/0002099),
Theorem 7. Its kernel is the Fourier projection onto $[-1/2,1/2]$, a
translation-invariant, locally trace-class positive contraction in the stated
Hermitian setting. The Poisson process is mixing by independence on disjoint
bounded sets. Other ensemble targets require their own ergodicity input for
Theorem 1, or the explicit pair-density hypotheses of Corollary 2.

The companion Python verifier checks exact quarter-circle Fourier and marked
convolution identities, then independently compares floating Gaussian pair
and trace formulas. It also checks the sine integral and scope counterexamples.
These finite checks do not prove process convergence or the cat-map return laws.
See [the scoped research review](../record/return_obstruction_review_20260912.md).
The positive BGS target still requires fixed-classical-strength,
Heisenberg-time desymmetrized joint-trace estimates.
