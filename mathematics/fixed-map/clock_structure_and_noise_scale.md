# Exact clock structure factor and the scale of spectral noise removal

**Claim ID: BGS-FLOW-018. Status: project proof with independent internal review of the new implications.**
5 October 2026. The clock kernel and lattice-to-sine relaxation are prior
Forrester and Katori--Tanemura. The formulas below are derived from the
existing odd-dimensional kernel, with explicit signed compensation and
transport boundaries. No priority or deterministic BGS theorem is asserted.

## 1. Objects and finite-dimensional formula

Let $N=2M+1\ge3$, $C_N=\operatorname{diag}(e^{2\pi i j/N})$, and let
$V_t=B_tC_N$ for full normalized unitary Brownian motion, with the angle
generator D2 of [FLOW-015](../microscopic_noise_removal.md). Set $\tau=Nt$,
$p_m=\operatorname{Tr}V_t^m$, and $L_N=\{-M,\ldots,M\}$.
Use Fourier convention $\widehat g(\xi)=\int g(x)e^{-2\pi i x\xi}dx$.
Unfold the eigenangles with period $N$ and use an independent uniform
origin. Its stationary covariance spectral measure is

$$
\mathcal S_{N,t}=\frac1{N^2}\sum_{m\ne0}\mathbb E|p_m|^2\delta_{m/N}.
\tag{S1}
$$

Thus for any Schwartz $g$, the variance of the full-line linear statistic
$\int g\,d\Xi_{N,t}$ is $\int|\widehat g|^2d\mathcal S_{N,t}$.
This follows by Fourier expansion of the periodized $g$ and integration
over the origin; the $m=0$ coefficient is the deterministic mean $\int g$.

For $q\ne0$ define

$$
a_{q,N}(\tau)=e^{-\tau q^2/2}
\frac{\sinh(\tau q/2)}{N\sinh(\tau q/(2N))},\qquad
s_\tau(\xi)=1-\sum_{r\in\mathbb Z}(1-|\xi-r|)_+e^{-\tau r\xi}.
\tag{S2}
$$

The quotient is positive and even in $q$. Only two neighboring terms
contribute to the sum defining $s_\tau$, except at integer endpoints.
For every nonzero integer $m$ the exact identity is

$$
\mathbb E|p_m|^2=N\,s_\tau(m/N)
+\mathbf1_{N\mid m}N^2a_{m/N,N}(\tau)^2.
\tag{S3}
$$

In particular, $\mathbb E|p_m|^2=m(1-e^{-tm})$ for $1\le m<N$.
There is no Gaussian or independent-trace approximation in this formula.

**Derivation.** FLOW-007 (2) gives the kernel

$$
K(x,y)=\frac1{2\pi}\sum_{l\in L_N}\sum_{r\in\mathbb Z}
w_{l,r}e^{-ilx+i(l+rN)y},\quad
w_{l,r}=e^{-t((l+rN)^2-l^2)/(2N)}.
\tag{S4}
$$

Integrating its diagonal against $e^{imx}$ shows that $\mathbb Ep_m=0$
unless $m=qN$; in that case its magnitude is $Na_{q,N}$, by a finite
geometric sum. The determinantal second-moment identity, valid also for
this non-Hermitian biorthogonal kernel, is

$$
\mathbb E|p_m|^2=|\mathbb Ep_m|^2+N
-\iint e^{im(x-y)}K(x,y)K(y,x)dxdy.
$$

The two angular integrals in the last expression require $s=-r$ and
$l-k=m-rN$. The product of the two weights is exactly $e^{-trm}$;
there are $(N-|m-rN|)_+$ ordered pairs $(l,k)$. This proves S3.
All alias sums are absolutely convergent at fixed $N,t>0$.

## 2. Signed cancellation and an optimal pair rate

Let $\mathcal S_N^{\rm CUE}=N^{-1}\sum_{m\ne0}
\min(|m|/N,1)\delta_{m/N}$ be the exact Haar-CUE covariance measure.
Put $b_{q,\tau}(\xi)=(1-|\xi-q|)_+e^{-\tau q\xi}$ for $q\ne0$.
Its finite mesh mass has the exact value

$$
\frac1N\sum_{m\in\mathbb Z}b_{q,\tau}(m/N)=a_{q,N}(\tau)^2.
\tag{S5}
$$

Indeed set $d=m-qN$. The left side is
$N^{-2}e^{-\tau q^2}\sum_d(N-|d|)_+e^{-tqd}$, the square of the
geometric sum in S2. The $m=0$ term is zero even when $|q|=1$.
Consequently $\nu_{q,N,\tau}=a_{q,N}^{-2}N^{-1}
\sum_m b_{q,\tau}(m/N)\delta_{m/N}$ is a probability measure, and

$$
\mathcal S_{N,t}-\mathcal S_N^{\rm CUE}
=\sum_{q\ne0}a_{q,N}^2(\delta_q-\nu_{q,N,\tau}).
\tag{S6}
$$

This is a signed compensation identity; every summand has zero total
mass. For $\tau\ge1$, uniformly in odd $N$ and $t=\tau/N$,

$$
\|\mathcal S_{N,t}-\mathcal S_N^{\rm CUE}\|_{\rm TV}
\le\frac8{\tau^2}.
\tag{S7}
$$

Here the norm is the total mass of the variation, without a factor $1/2$.
Use $N\sinh(x/N)\ge x$ and

$$
0<a_{q,N}\le a_q(\tau):=
\frac{e^{-\tau q(q-1)/2}(1-e^{-\tau q})}{\tau q},\quad q\ge1.
$$

The variation in S6 is at most $4\sum_{q\ge1}a_{q,N}^2
\le4\tau^{-2}\sum_{q\ge1}q^{-2}\le8\tau^{-2}$.
Thus the entire signed pair comparison for every bounded Fourier weight
$W$ is bounded by $8\|W\|_\infty/(Nt)^2$. The diagonal counterterm is
the same for both laws, so this also compares their factorial pair tests.
The $O((Nt)^{-1})$ pointwise kernel bound is not sharp for this
origin-averaged signed pair quantity.

The rate is optimal. If $N\to\infty$, $\tau_N\to\infty$ and
$t_N=\tau_N/N\to0$, then against every compact continuous weight,

$$
\tau_N^2(\mathcal S_{N,t_N}-\mathcal S_N^{\rm CUE})
\ \longrightarrow\ \delta_1+\delta_{-1}-2\delta_0.
\tag{S8}
$$

For $q=\pm1$, $\tau^2a_{q,N}^2\to1$ because
$t/(2\sinh(t/2))\to1$. Their negative mesh measures concentrate at zero.
For example, on $\xi\ge\delta>0$,
$b_{1,\tau}(\xi)\le e^{-\tau\delta/2}b_{1,\tau/2}(\xi)$;
S5 bounds the rescaled tail by $4e^{-\tau\delta/2}$.
All $|q|\ge2$ have rescaled total mass bounded by
$\sum_{q\ge2}q^{-2}e^{-\tau q(q-1)}\to0$.
These prove S8. A fixed smooth $W$ supported near 1 with $W(1)=1$
gives a nonzero limiting coefficient, proving optimality for local
Schwartz pair tests as well.

## 3. Critical-time local law, with all fixed moments

If $Nt_N\to\tau\in(0,\infty)$, the origin-averaged local process
converges to a stationary law $Q_\tau$. Conditional on a uniform phase
$\eta\in[0,1)$ its factorial densities are determinants of

$$
\mathcal K_\tau^\eta(u,v)=\sum_{r\in\mathbb Z}
e^{2\pi ir(v+\eta)}\int_{-1/2}^{1/2}
e^{-\tau(r^2+2rs)/2}e^{2\pi is(v-u)}ds.
\tag{S9}
$$

The unconditional law is a phase mixture; it is not asserted to have
one determinantal kernel. Its intensity is one. Every fixed compact
continuous or Schwartz factorial test converges, and every fixed-window
ordinary count moment is uniformly bounded.

**Proof.** In S4 the unfolded sum over $l$ is a midpoint Riemann sum
over $[-1/2,1/2]$. For $\tau$ in any compact subset of $(0,\infty)$,
the aliases have the uniform summable majorant
$e^{-\tau |r|(|r|-1)/2}$ for $|r|\ge1$. Midpoint errors for all derivatives
on a compact window are dominated by the same majorant times a fixed
polynomial in $r$. Thus the kernels converge locally uniformly, uniformly
in $\eta$. The determinant/Fredholm majorants of FLOW-007 give the
Laplace limit and bounded factorial moments of every fixed order.
Tightness follows from intensity one; these Laplace limits identify the
law. Positive factorial majorants and the Stirling identity supply ordinary
moments. Spatial tiling and these moments give the Schwartz extension.
No infinite-dimensional SDE construction is needed for this limit proof.

Taking limits in S1--S3 gives its covariance spectral measure

$$
\mathcal S_\tau=s_\tau(\xi)d\xi+\sum_{q\ne0}a_q(\tau)^2\delta_q.
\tag{S10}
$$

The mesh convergence follows first for compact Fourier weights and then
for Schwartz weights by the uniform moment tails. In particular,
$s_\tau(\xi)=|\xi|(1-e^{-\tau|\xi|})$ on $0<|\xi|<1$.
The nonzero atoms distinguish $Q_\tau$ from Sine$_2$ at every finite
$\tau$. S9 is the known lattice relaxation kernel, up to transposition,
with Katori--Tanemura time $\tau/(4\pi^2)$.

## 4. Small noise, contractivity and robustness

Use ordered angle lifts in the convex chamber
$\theta_1<\cdots<\theta_N<\theta_1+2\pi$. Their SDE has independent
noises $N^{-1/2}dW_j$ and drift
$b_j=(2N)^{-1}\sum_{k\ne j}\cot((\theta_j-\theta_k)/2)$.
The clock lift $a_j=2\pi j/N$ has $b(a)=0$.
For $\Delta_j=\theta_j-a_j$ the monotonicity of cotangent on each
chamber pair interval and of $x\mapsto x^{2r-1}$ gives

$$
\sum_j\Delta_j^{2r-1}(b_j(\theta)-b_j(a))\le0.
$$

Apply Ito to $N^{-1}\sum_j\Delta_j^{2r}$, localize before a collision
and at large common translations, and use the noncolliding Dyson law.
Induction and Fatou yield

$$
\mathbb E\frac1N\sum_j
\left|\frac N{2\pi}\Delta_j(t)\right|^{2r}
\le(2r-1)!!\left(\frac{Nt}{4\pi^2}\right)^r.
\tag{S11}
$$

The induction uses derivative bound $r(2r-1)N^{-1}$ times the moment
of order $2r-2$. For localization the same bound is applied to stopped
moments; removing the stops preserves the upper bound. Full Brownian
common translation is included in S11. Shortest circular displacements
are no larger than these lift displacements.
FLOW-016 with the deterministic clock reference now implies that if
$Nt_N\to0$, all fixed local factorial tests converge to those of
$\mathbb Z+\operatorname{Unif}[0,1)$, and all fixed count moments stay
bounded. When $Nt\le1$, S11 and the same packing inequality also give
uniform moment bounds. When $Nt\ge1$, FLOW-007's bounded kernel gives
them directly, including the regime $Nt\to\infty$.

Two simple initial spectra with ordered lifts in this chamber can be
coupled with the same particle noises. Their difference $d_j$ has no
martingale term. Pairwise monotonicity gives, for every $p\ge1$,

$$
\frac d{dt}\sum_j|d_j|^p\le0.
\tag{S12}
$$

For $p=1$ use a convex smooth approximation; for $p>1$ use
$\operatorname{sgn}(x)|x|^{p-1}$ and pair the two drift positions.
Interpolation between the two ordered lifts stays in the chamber;
cotangent is decreasing separately on $(-2\pi,0)$ and $(0,2\pi)$.
Localization and continuity remove the stops. It is a standard
monotone-drift coupling, not matrix Brownian coupling with identical
matrix entries.

Consequently, if simple spectra $A_N$ admit ordered lifts matched to
the clock with
$N^{-1}\sum_j|N(\theta_j-a_j)/(2\pi)|^{2r}\to0$ for every fixed $r$,
then their Dyson laws have the same local limits and all fixed moments
as the clock laws in each of the three regimes. FLOW-016 applies since
the reference moments above are uniform and the coupled costs do not
increase. Their original local law is the clock law as well.
The one-phase perturbed clock D11 of FLOW-015 satisfies these hypotheses
and has every positive trace nonzero.

## 5. An explicit test and the original chain

Fix nonzero $\widehat g\in C_c^\infty((a,b))$ with $0<a<b<1$.
The clock linear statistic is identically zero by periodization, whereas
for $Nt_N\to\tau\in(0,\infty)$ its noisy variance tends to

$$
\int_a^b|\widehat g(\xi)|^2\xi(1-e^{-\tau\xi})d\xi
\ge a(1-e^{-\tau a})\|\widehat g\|_2^2>0.
\tag{S13}
$$

For $Nt_N\to\infty$ it tends to
$\int_a^b\xi|\widehat g(\xi)|^2d\xi>0$. Thus on the clock and the
matched families of Section 4, preservation of every fixed local test
under Dyson noise holds precisely when $Nt_N\to0$; if this fails,
a subsequence has $Nt_N$ bounded away from zero and S3 gives a positive
lower bound for the same test. This is a noise-removal obstruction for
these spectra, not a counterexample to chaotic BGS.

There is an original-chain corollary. Start C1 of FLOW-017 at $C_N$,
assume $1/N\le t_N\to0$, $t_N^2\log N\to0$ and its single
superpolynomial step-size condition C2. If $Nt_N\to\tau\in[1,\infty)$,
the original uncentered chain has the all-fixed-order limit $Q_\tau$;
if $Nt_N\to\infty$, it has Sine$_2$ with all fixed moments.
Use FLOW-017's general polynomial-test comparison C10, which does not
use its separate Sine reference assumption. The centered initial clock
is exactly $C_N$. FLOW-016's projected-to-Dyson Schatten costs vanish;
the reference moments required for its packing step are supplied here
by Sections 3--4 instead of FLOW-014. C11 and positive majorants then
transfer all fixed factorial orders. No quenched $L^2$ or small-time
chain statement below $1/N$ is added by this corollary.

## 6. Actual-map boundary and provenance

There is a resolvent/Abel consequence for this same control. Put
$L_N(s;V)=N^{-2}\sum_{m\ge1}e^{-2sm/N}|\operatorname{Tr}V^m|^2$,
$s>0$, and $H_N(x)=N^{-1}\sum_{l\in L_N}e^{xl}
=\sinh(Nx/2)/(N\sinh(x/2))$, with $H_N(0)=1$.
The positive half of S6 gives the absolutely convergent identity

$$
\mathbb EL_N(s;V_t)-L_N^{\rm CUE}(s)
=\sum_{q\ge1}e^{-\tau q^2-2sq}
\left[H_N(tq)^2-H_N(tq+2s/N)^2\right]<0,
\tag{S14}
$$

where $L_N^{\rm CUE}(s)=
e^{-2s/N}(1-e^{-2s})/[N^2(1-e^{-2s/N})^2]$.
Pairing $l$ and $-l$ shows that $H_N$ is strictly increasing on
$(0,\infty)$ for $N\ge3$, proving the sign; S5 justifies the summation.
The universal floor TRACE-007 supplies the lower bound
$1/(e^{2s}-1)\le\mathbb EL_N(s;V_t)$.
At the joint regime of S8 its exact leading discrepancy is
$(e^{-2s}-1)/\tau^2+o(\tau^{-2})$; apply S8 to
$\tfrac12e^{-2s|\xi|}$. Extending from compact weights is justified
by its boundedness and the vanishing rescaled $|q|\ge2$ tails.
No monotonicity in time is asserted by this sandwich.

The prescribed frozen $U_N$ has not been matched to a clock by vanishing
unfolded costs. S6 relies on the exactly equispaced start and its Fourier
selection rule; it is not an identity for arbitrary starts. The actual
signed defects C16--C17 and D4 remain unestimated. This result isolates
one rigorous cancellation mechanism and its sharp noise scale; it does
not establish deterministic BGS or priority.

The [source check](../../literature/critical_noise_sources_20261005.md)
distinguishes the prior kernels from the new project derivation and
records a visually checked source-formula inconsistency. The companion
verifier supplies finite exact generator, mesh-mass and angular-selection
controls and numerical kernel diagnostics; none certifies an asymptotic
limit, stochastic trajectory, analytic Lean proof or world novelty.
