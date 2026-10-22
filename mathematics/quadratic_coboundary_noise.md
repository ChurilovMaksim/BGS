# Quadratic coboundary noise: covariance, ellipticity, and its transfer boundary

**Continuation, 29 September 2026.** [FLOW-004](quadratic_noise_coupling.md)
compares evolved noisy laws without occupancy;
[FLOW-005](quadratic_noise_reversibility.md) supplies a Haar-reversible drift;
[FLOW-006](quadratic_noise_trace_fluctuations.md) identifies the fixed-trace
anomaly; [FLOW-007](quadratic_noise_clock_limit.md) proves a scoped clock
local limit. These do not complete deterministic noise removal.


**Claim ID:** BGS-FLOW-003. **Status:** exact finite-dimensional project
derivation with deterministic finite checks and author self-review.
No priority claim; no fixed-map universality theorem. This note resolves a
fourth-order question left open by [BGS-FLOW-002](coboundary_spectral_flow_bound.md).
The noise constructed here is external and generally changes local statistics.

## 1. Exact covariance and its complete degeneracy criterion

Let $N\ge2$, let $U$ be any unitary matrix, and let $G$ be normalized GUE:
$\mathbb E G_{ab}G_{cd}=N^{-1}\delta_{ad}\delta_{bc}$.
Put

$$
H=\frac{i}{\sqrt2}[G,UGU^*],\qquad X=H-\mathbb EH,
\qquad m_r=\frac1N\operatorname{Tr}U^r.
$$

Both $H$ and $X$ are Hermitian and traceless. In an eigenbasis of $U$, write
$z_j=e^{i\theta_j}$. Repeated eigenvalues are allowed in this section.

**Theorem 1.** The mean and centered covariance are

$$
\mathbb EH=\frac{i}{\sqrt2}(m_1U^*-\overline{m_1}U),
$$

$$
\mathbb E X_{jk}X_{ab}
=\delta_{jb}\delta_{ka}v_{jk}
-\frac{2}{N^2}\delta_{jk}\delta_{ab}\sin^2(\theta_j-\theta_a),
\qquad
v_{jk}=\frac{1-\Re(m_2/(z_jz_k))}{N}.                    \tag{1}
$$

The product on the left has **no complex conjugation**; in particular
$\mathbb E|X_{jk}|^2=v_{jk}$ for $j\ne k$. For Hermitian $T,S$ this is
equivalently

$$
\begin{aligned}
\mathbb E\operatorname{Tr}(XT)\operatorname{Tr}(XS)
={}&\frac{\operatorname{Tr}(TS)}N
-\frac1N\Re\{m_2\operatorname{Tr}(U^*TU^*S)\}
-\frac{\operatorname{Tr}T\operatorname{Tr}S}{N^2}\\
&+\frac1{N^2}\Re\{\operatorname{Tr}(U^2T)
                  \overline{\operatorname{Tr}(U^2S)}\}.
\end{aligned}                                                       \tag{2}
$$

For every traceless Hermitian $T$,

$$
\frac{1-|m_2|}{N}\operatorname{Tr}T^2
\le \mathbb E(\operatorname{Tr}XT)^2
\le\frac{2+|m_2|}{N}\operatorname{Tr}T^2.                \tag{3}
$$

The covariance is positive definite on the real traceless Hermitian space
**if and only if** $|m_2|<1$. Its failure occurs exactly when the spectrum
of $U$ is contained in two antipodal points of the unit circle.

**Proof.** Direct expansion gives

$$
H_{jk}=\frac{i}{\sqrt2}\sum_l
\left(\frac{z_l}{z_k}-\frac{z_j}{z_l}\right)G_{jl}G_{lk}.
$$

The internal Gaussian contraction gives the stated mean. Of the two
remaining Wick contractions, one forces $j=b,k=a$ and contributes

$$
-\frac1{2N^2}\sum_l
\left(\frac{z_l^2}{z_jz_k}+\frac{z_jz_k}{z_l^2}-2\right)=v_{jk}.
$$

The other forces $j=k,a=b$ and contributes
$-2N^{-2}\sin^2(\theta_j-\theta_a)$. This proves (1). Contract with
$T_{kj}S_{ba}$ and use $2\sin^2 t=1-\cos2t$ to obtain (2).
Hilbert--Schmidt Cauchy--Schwarz gives
$|\operatorname{Tr}(U^*TU^*T)|\le\operatorname{Tr}T^2$ and
$|\operatorname{Tr}(U^2T)|^2\le N\operatorname{Tr}T^2$, proving (3).
Equality in the triangle inequality for $N^{-1}\sum_jz_j^2$ says
$|m_2|=1$ exactly when all $z_j^2$ agree. In that case every diagonal
entry of $H$ is zero in this eigenbasis, so a nonzero traceless diagonal
$T$ witnesses singularity. This also covers scalar $U$. Conversely (3)
is strictly positive when $|m_2|<1$. $\square$

This is a covariance criterion, not a criterion for quantum chaos. A clock
spectrum satisfies it, and its original spacings are completely rigid.

## 2. Explicit covariance operator and a corrected noise

Let $\mathcal H_0$ denote the real traceless Hermitian space with scalar
product $\operatorname{Tr}(TS)$. The covariance operator, extended to all
Hermitian matrices, is

$$
\begin{aligned}
\mathcal C_U(T)={}&\frac TN
-\frac{m_2U^*TU^*+\overline{m_2}UTU}{2N}
-\frac{\operatorname{Tr}T}{N^2}I\\
&+\frac{\operatorname{Tr}(U^2T)U^{*2}
        +\operatorname{Tr}(U^{*2}T)U^2}{2N^2}.
\end{aligned}                                                       \tag{4}
$$

It annihilates $I$ and preserves $\mathcal H_0$. If $|m_2|<1$, define

$$
Y=(N\mathcal C_U|_{\mathcal H_0})^{-1/2}X.              \tag{5}
$$

Then $\mathbb EY=0$ and, for $T,S\in\mathcal H_0$,
$\mathbb E\operatorname{Tr}(YT)\operatorname{Tr}(YS)=N^{-1}\operatorname{Tr}(TS)$.
The norm of the linear map in (5) is at most $(1-|m_2|)^{-1/2}$.
These assertions follow by diagonalizing the positive real self-adjoint
operator (4); they do not require $X$ or $Y$ to be Gaussian.

Consequently, for a smooth function on the unitary group, the fixed-$N$
one-step operator

$$
\lim_{\varepsilon\to0}
\frac{\mathbb E f(e^{i\varepsilon Y}U)-f(U)}{\varepsilon^2}
$$

is exactly the generator with traceless GUE increments. Indeed, expand
$f(e^{i\varepsilon Y}U)$ to second order at fixed $U$. The first-order
term has mean zero and the second-order term depends only on the covariance.
All moments of $Y$ are finite, so the Taylor remainder is integrable.
This is a **local infinitesimal statement**, with the noise sampled at the
current $U$; no derivative of the sampling law enters that Taylor expansion.
It is not a claim of uniform-in-$N$ diffusion convergence or noise removal.
The determinant is preserved; the corresponding group diffusion is on its
fixed-determinant coset, rather than allowing an independent common phase.

When $m_2=0$, (4) on $\mathcal H_0$ becomes $I/N$ plus an operator of
rank at most two, supported by $\Re U^2$ and $\Im U^2$. If also $m_4=0$,
these two Hermitian matrices are orthogonal with squared norm $N/2$.
The map (5) then multiplies their components by $\sqrt{2/3}$ and leaves
their orthogonal complement unchanged. This is an explicit correction,
not an assertion that the uncorrected process has the same equilibrium.

## 3. Radial generator and a microscopic pair comparison

Assume now that the eigenvalues are distinct. For an arbitrary fixed
Hermitian kick $T$, differentiating the eigenvalue equation for
$e^{i\varepsilon T}U$ gives

$$
\theta_j'(0)=T_{jj},\qquad
\theta_j''(0)=\sum_{k\ne j}|T_{jk}|^2
                         \cot\frac{\theta_j-\theta_k}{2}.
$$

Thus the uncorrected centered noise $X$ has generator

$$
\mathcal L_XF=
\frac12\sum_{jk}\Sigma_{jk}\partial_{jk}F+
\frac12\sum_j\sum_{k\ne j}v_{jk}
       \cot\frac{\theta_j-\theta_k}{2}\,\partial_jF,
\quad
\Sigma_{jk}=\delta_{jk}v_{jj}-\frac{2}{N^2}\sin^2(\theta_j-\theta_k).
                                                               \tag{6}
$$

In particular $\Sigma\mathbf1=0$. Let $\mathcal L_D$ denote circular
Dyson motion with diagonal covariance $I/N$ and drift
$(2N)^{-1}\sum_{k\ne j}\cot((\theta_j-\theta_k)/2)$.
At a spectrum with $m_2=0$,

$$
\mathcal L_X-\mathcal L_D
=-\frac1{2N^2}\left(\sum_j\partial_j\right)^2
+\frac1{2N^2}\sum_{jk}\cos(2\theta_j-2\theta_k)\partial_{jk}.
                                                               \tag{7}
$$

The first term removes the common phase. The second comprises two smooth
collective directions. For $\phi\in C_c^2(\mathbb R)$ supported in
$[-R,R]$, $N>2R$, define the ordered-pair statistic

$$
F_{N,\phi}=\frac1N\sum_{j\ne k}\sum_{\ell\in\mathbb Z}
\phi(x_{jk,\ell}),\qquad
x_{jk,\ell}=\frac N{2\pi}(\theta_j-\theta_k+2\pi\ell).
$$

Its common-phase derivative vanishes, and differentiating each summand
twice in (7) gives exactly

$$
(\mathcal L_X-\mathcal L_D)F_{N,\phi}
=\frac1{4\pi^2N}\sum_{j\ne k,\ell}
(1-\cos(2\theta_j-2\theta_k))\phi''(x_{jk,\ell}).       \tag{8}
$$

At most one translate contributes for each ordered pair, and
$1-\cos(4\pi x/N)\le8\pi^2x^2/N^2$. Therefore

$$
\left|(\mathcal L_X-\mathcal L_D)F_{N,\phi}\right|
\le\frac{2(N-1)}{N^2}\sup_x|x^2\phi''(x)|.             \tag{9}
$$

No occupancy bound is needed. Nevertheless (9) holds at $m_2=0$, a set
not proved invariant under $\mathcal L_X$. It is neither a comparison
of semigroups nor a local law. For small nonzero $m_2$, (1) gives relative
off-diagonal variance error at most $|m_2|$, but the singular cotangent
drift and derivatives of microscopic observables prevent silently
upgrading this to a uniform dynamic comparison. An additional occupancy
assumption does permit the following pointwise extension.

**Theorem 2 (conditional microscopic generator comparison).** Suppose every
arc of angular length $2\pi/N$ contains at most $M$ eigenphases, the
spectrum is simple, and $N>2R+2$. Then, with a constant depending only
on $R$ and the first two derivatives of $\phi$,

$$
\frac1N\left|(\mathcal L_X-\mathcal L_D)F_{N,\phi}\right|
\le C_{R,\phi}|m_2|M^2(1+\log N)
+\frac{2}{N^2}\sup_x|x^2\phi''(x)|.                    \tag{9a}
$$

No positive lower bound on the smallest gap is assumed. The factor $1/N$
on the left is the generator scaling at microscopic noise time.

**Proof.** Replace $\phi$ by its even part without changing $F$ and let
$g_j=\partial_jF$. Periodizing the test function, differentiation gives
$g_j=\pi^{-1}\sum_l\phi'(x_{jl})$, including the zero self term. Here and
below each expression includes the unique possible periodized translate.
The occupancy bound yields
$|g_j|\le C_{R,\phi}M$ and
$|\partial_{jj}F|\le C_{R,\phi}NM$.
If the circular distance $d_{jk}$ is at most $1/N$, compare the two sums
term by term. The union of their supports lies in an arc of length
$O((R+1)/N)$, hence has $O((R+1)M)$ points. The mean value theorem gives
$|g_j-g_k|\le C_{R,\phi}MN d_{jk}$; for larger distances use the bound
on $g$ itself. Thus for all $j,k$,

$$
|g_j-g_k|\le C_{R,\phi}M\min\{Nd_{jk},1\}.
$$

Set $a_{jk}=\Re(m_2/(z_jz_k))=a_{kj}$. The part of the drift difference
not already in (7) is

$$
-\frac1{4N}\sum_{j\ne k}a_{jk}
\cot\frac{\theta_j-\theta_k}{2}(g_j-g_k).
$$

The preceding estimate cancels its pole for small $d_{jk}$. Grouping other
points into arcs of length $2\pi/N$ around each $j$ gives a harmonic sum:

$$
\sum_{k\ne j}\left|\cot\frac{\theta_j-\theta_k}{2}\right|
\min\{Nd_{jk},1\}\le C MN(1+\log N).
$$

Use $|a_{jk}|\le|m_2|$ and sum in $j$ to bound the drift difference by
$C_{R,\phi}|m_2|NM^2(1+\log N)$. The additional diagonal Hessian term
is $-(2N)^{-1}\sum_j a_{jj}\partial_{jj}F$, bounded by
$C_{R,\phi}|m_2|NM$. The remaining terms are exactly (7) and obey (9).
Divide by $N$, absorb $M\ge1$ into $M^2$, and obtain (9a). $\square$

In particular, if the previous project bound $m_2=O(N^{-1/40})$ holds,
the right side tends to zero for bounded $M$, or more generally for
$M=o(N^{1/80}/\sqrt{\log N})$. Such microscopic occupancy is **not
proved for the frozen family here**. This pointwise generator estimate
also needs propagation of occupancy, comparison of evolved test functions,
and deterministic noise removal before it can yield local universality.

## 4. An exact obstruction: uncorrected noise does not preserve Haar

Write $p_r=\operatorname{Tr}U^r$. Direct substitution in (6) yields

$$
\mathcal L_Xp_2=-\frac{p_2}{2}-\frac{p_1^2}{N}
+\frac{p_2|p_1|^2+\overline{p_2}(p_1p_3+p_2^2)}{2N^2},
                                                               \tag{10}
$$

$$
\Gamma_X(p_2,\overline{p_2})
=6-\frac{8|p_2|^2}{N^2}+\frac{2|p_4|^2}{N^2},         \tag{11}
$$

where $\Gamma(F,G)=\mathcal L(FG)-F\mathcal LG-G\mathcal LF$.
For completeness, (11) follows by contracting
$4z_j^2\overline{z_k^2}$ with $\Sigma_{jk}$. To derive (10), symmetrize
the drift sum in $j,k$ and use
$\cot((\theta_j-\theta_k)/2)=i(z_j+z_k)/(z_j-z_k)$; the differences
$z_j^2-z_k^2$ cancel the apparent poles.

For Haar $U(N)$ and $N\ge4$, the required elementary power-sum integrals are

$$
\begin{gathered}
\mathbb E|p_2|^2=2,\quad \mathbb E|p_2|^4=8,\quad
\mathbb E|p_4|^2=4,\quad \mathbb E|p_2p_1|^2=2,\\
\mathbb E\overline{p_2}p_1^2=0,\qquad
\mathbb E\overline{p_2}^{\,2}p_1p_3=0.
\end{gathered}
$$

One derivation is the power-sum expansion
$p_\lambda=\sum_{\mu\vdash d}\chi^\mu(\lambda)s_\mu$.
For $d\le N$, all the partitions occur; Haar orthogonality of the unitary
characters $s_\mu$ and column orthogonality of the symmetric-group
characters give
$\langle p_\lambda,p_\nu\rangle=\delta_{\lambda\nu}
\prod_r r^{a_r}a_r!$, where $a_r$ counts parts of size $r$.
This proves precisely the displayed moments, with maximal degree four.
These are standard finite representation identities, not a new Haar theorem.
An independent exact Laurent integration at $N=4$ is included in the verifier.

Combining (10)--(11) gives the nonzero stationarity defect

$$
\boxed{\displaystyle
\int\mathcal L_X|p_2|^2\,d\mathrm{Haar}=4+\frac2{N^2}>0
\quad(N\ge4).}                                           \tag{12}
$$

Thus the raw centered quadratic noise cannot simply be declared a
Haar-preserving Dyson process. The correction (5) removes this covariance
defect but introduces an explicit state-dependent modification of the noise.
The Haar statement concerns the smooth matrix generator; eigenvalue
collision coordinates cause no problem for the polynomial observable.
Failure of exact Haar stationarity does not itself exclude asymptotic
local CUE statistics for some stationary law of the uncorrected process.

## 5. Why this is fourth order for the original coboundary kick

Let $B=UGU^*$ and $V(t)=e^{it(G-B)}U$. The previously proved project normal
form is

$$
e^{-itG}V(t)e^{itG}=W(t)U,\quad
W(t)=e^{-itG}e^{it(G-B)}e^{itB}
=I-\tfrac12t^2[G,B]+O_G(t^3)
=I+\frac{it^2}{\sqrt2}H+O_G(t^3).
$$

At fixed $N$ and simple $U$, label the eigenphase branches from $t=0$.
Then $\Delta\theta_j=t^2H_{jj}/\sqrt2+O_G(t^3)$, and

$$
\lim_{t\to0}t^{-4}\operatorname{Cov}(\Delta\theta_j,\Delta\theta_k)
=\tfrac12\Sigma_{jk}.                                  \tag{13}
$$

The expansion also holds in $L^2(G)$: restrict first to a bounded $G$ set
where the fixed spectral gap gives analytic perturbation bounds, and then
use Gaussian tails and the norm bound on unitary spectral motion. One may
take a cutoff growing like a sufficiently large multiple of
$\sqrt{\log(1/|t|)}$, keeping $t\|G\|$ small; its omitted polynomial
moments are smaller than any prescribed power of $t$.
In particular,

$$
\lim_{t\to0}t^{-4}\mathbb E\frac1N\sum_j
\left[\frac N{2\pi}(\Delta\theta_j-\mathbb E\Delta\theta_j)\right]^2
=\frac{N}{8\pi^2}(1-|m_2|^2).                           \tag{14}
$$

Here we used $\operatorname{Tr}\Sigma=1-|m_2|^2$.
The old second-order absence of radial diffusion and the present
fourth-order phase variance are compatible. Equation (14) suggests a
scale $Nt^4\asymp1$, but is a **fixed-$N$ derivative**, not an estimate
uniform up to that scale. Higher-order drift terms in the original $V(t)$
have not been removed. Its complete fourth-order generator is therefore
not identified with (6) or (5).

## 6. Smooth-noise realization and the exact rank obstruction

Suppose instead that $G=\sum_{a=1}^d\xi_aG_a$ for fixed Hermitian $G_a$
and independent real standard Gaussians. Then $H$ is a quadratic polynomial
with symmetric matrix coefficients

$$
A_{ab}=\frac{i}{2\sqrt2}
\big([G_a,UG_bU^*]+[G_b,UG_aU^*]\big).
$$

Hence $X$ lies in their real span and

$$
\operatorname{rank}\operatorname{Cov}(X)\le d(d+1)/2.      \tag{15}
$$

Full matrix ellipticity requires $d(d+1)/2\ge N^2-1$; full radial
ellipticity modulo a common phase requires $d(d+1)/2\ge N-1$.
If $d=O(K^2)$ for a two-dimensional Fourier cutoff $K$, these necessitate,
respectively, $K\gtrsim N^{1/2}$ and $K\gtrsim N^{1/4}$.
They are necessary conditions only, not sufficient mixing estimates.

Taking exact time translates at a **frozen** $U$ does not fix the radial
rank deficit: for $G_r=U^{-r}GU^r$,

$$
H(G_r,U)=U^{-r}H(G,U)U^r,
$$

whose diagonal in the $U$ eigenbasis is unchanged. Independently sampled
translated copies have the same radial covariance range. Allowing mixed
quadratic terms among different translates enlarges the input span and
must be counted anew in $d$; allowing an evolving $U$ is also a different
problem. Equation (15) does not exclude bracket-generated diffusion or
Hörmander mechanisms over multiple evolving steps.

Even allowing all mixed terms among $L+1$ translates of $d_0$ original
directions leaves $d\le d_0(L+1)$. Thus a fixed $d_0$ and
$L=O(\log N)$ give instantaneous radial covariance rank $O(\log^2N)$,
strictly smaller than $N-1$ eventually. Full instantaneous radial rank
requires $d_0(L+1)\gtrsim\sqrt N$. This is a precise obstruction to
that particular frozen-frame logarithmic-time construction, not to
all time-dependent constructions.

## 7. Relation to the maintained map and the still-missing implication

The previously maintained [fixed-time trace estimate](frozen_seven_cut_reduction.md)
$|\operatorname{Tr}U_N^2|\le C N^{39/40}$ would give
$|m_2|=O(N^{-1/40})$ in (3) for the actual frozen family. This is an
application of that earlier project bound, not a new audit of its proof.
The covariance theorem itself needs no dynamical assumption.
The [4 October direct packet proof](fixed_time_wavepacket_trace_bound.md)
now gives $|\operatorname{Tr}U_N^2|=O(1)$, strengthening that application
to $|m_2|=O(N^{-1})$. This improves the covariance rate, not the already
available ellipticity or deterministic noise removal.

What is now available is an explicit nondegenerate quadratic noise and
an exact way to correct its covariance. What remains unavailable is a
quantitative comparison between the deterministic original spectrum and
this noisy spectrum at a microscopic relaxation time, with the needed
initial regularity and all-order control. A clock has $m_2=0$ for $N\ge3$
and satisfies the same ellipticity criterion, so this missing transfer
cannot follow from (3) alone. The verifier also exhibits a smooth local
pair observable whose Dyson derivative at a clock is of order $N$.

No finite computation here establishes a large-$N$ limit. No Lean
compilation or external referee audit is claimed. The exact proof and
finite computational scope are recorded in the
[research checkpoint](../archive/record/quadratic_noise_program_20260928.md).
BGS-TRACE-005 and BGS-BGS-001 remain open.
