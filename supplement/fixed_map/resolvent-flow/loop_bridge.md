# Microscopic loop equations: a conditional route for the frozen map

Status: exact identities and a conditional all-order reduction. The
required mixed-loop estimate for the frozen quantum map is **unproved**.
This note neither proves BGS nor establishes priority for its elementary
identities. Research checkpoint: `resolvent-flow-20260920-mixed-hierarchy`.

The maintained model is U_N=exp(i tau N A_N) M_N, tau=10^-80, with the
original centered raw modular Weyl generator. No parameter average,
independent phase ensemble, or changed classical symbol is substituted.

## 1. External theorem and exact dictionary

Primary source: P. Bourgade and J. Huang, *Loop Equations Characterize
Random Matrix Statistics*, [arXiv:2607.07617v2](https://arxiv.org/abs/2607.07617v2),
9 September 2026. Theorem 1.9 characterizes convergence through approximate
mixed bulk loop equations. Its intensity is 1/pi. The proof's moment
bootstrap, equations (2.18)--(2.20), is relevant to the stronger correlation
conclusion below. These particular statements and their application were
checked; the entire 147-page proof was not independently verified here.

For arbitrary U_N with eigenangles theta_j, introduce one uniform origin
alpha in [0,2pi). This is just a spatial average of its fixed spectrum.
Define, off the real axis,

\[
s_N(w;\alpha)=\frac1N\sum_{j=1}^N
 \cot\left(\frac{\theta_j-\alpha}{2}-\frac wN\right).
\tag{1}
\]

It is a particle-generated Herglotz function. Its representing measure is

\[
\mu_N=\sum_{j=1}^N\sum_{\ell\in\mathbb Z}
 \delta_{N(\theta_j-\alpha)/2+\pi N\ell}.
\tag{2}
\]

Indeed, each summand in (1) has expansion 1/(x-w) at the corresponding
atom x. The upper half-plane is mapped to itself. The lattice sum of
1/(1+x^2) is finite. The linear Herglotz coefficient vanishes since
s_N(i eta) tends to i at fixed N as eta tends to infinity. The real
constant is Re s_N(i). The ordinary complex residue at an atom of mass m
is -m; the source's positive-residue wording uses the opposite sign.
Atom masses, rather than that wording, fix the convention here.

Uniform alpha makes (2) stationary with intensity 1/pi. Scaling positions
by 1/pi gives intensity one, exactly the usual unfolded quantum spectrum.
At each finite N all moments on compact sets away from the real line
exist, including when U_N has repeated eigenvalues.

For beta=2 define the full residual

\[
\begin{split}
\mathcal E_{p,N}(\mathbf w)
={}&\mathbb E_\alpha[(s_N(w_1)^2+1)
                 \prod_{j=2}^p s_N(w_j)]\\
&+\sum_{j=2}^p\mathbb E_\alpha\left[
 \partial_{w_j}\frac{s_N(w_1)-s_N(w_j)}{w_1-w_j}
 \prod_{\ell=2,\ell\ne j}^p s_N(w_\ell)\right].
\end{split}\tag{3}
\]

Coincident arguments use the holomorphic extension, equal to s_N''/2
in the differentiated divided difference. The sufficient hypothesis is,
for every p and compact K contained in C minus R,

\[
\sup_{\mathbf w\in K^p}
\frac{|\mathcal E_{p,N}(\mathbf w)|}
 {1+\mathbb E_\alpha\max_j|s_N(w_j)|^{p+1}}
\longrightarrow0.
\tag{H}
\]

The event Omega_N in the source is taken to be the entire probability
space. There is no discarded exceptional set. Under (H), the source
theorem applies to (1). **Condition (H) is not established for our U_N.**

## 2. Why this gives all compactly tested anchored correlations

Here the whole-space version of (H) is essential. Take p=2q-1, w_1=w,
q-2 further arguments equal to w, and q equal to its conjugate. The leading
term in (3) is E|s_N(w)|^(2q). Herglotz positivity bounds derivatives and
the required divided differences by C_K |s_N(w)|. The other terms have
strictly smaller degree, at most 2q-2 for beta=2. Young's inequality and
the relative o(1) in (H) therefore imply uniform moments of every fixed
order on compact sets. This reconstructs the moment step used in the
source, without assuming a preliminary local law for our spectrum.

From the Herglotz representation,

\[
\mu_N([-B,B])\le(1+B^2)\Im s_N(i)
                 \le(1+B^2)|s_N(i)|.
\tag{4}
\]

Thus all moments of each local particle count are uniformly bounded.
Weak point-process convergence from the external theorem upgrades to
convergence of every compactly tested factorial moment measure: the
factorial functional is continuous on integer-valued Radon measures in
the vague topology, and its absolute value is bounded by a fixed power
of a local particle count. The higher count moments provide uniform
integrability. Multiplicities at finite N cause no difficulty.

More explicitly, set y_j=N theta_j/(2pi) and t=N alpha/(2pi). The rescaled
configuration is xi_N=sum_{j,l} delta_{y_j+Nl-t}. Given continuous compactly
supported phi on R^(k-1), choose h in C_c(R) with integral one, and let
F(u)=h(u_k) phi(u_1-u_k,...,u_{k-1}-u_k). Integrating the uniform origin
and partitioning R into periods gives, for all sufficiently large N,

\[
\mathbb E\xi_N^{[k]}(F)=\frac1N
 \sum_{j_1,\ldots,j_k\ {m distinct}}
 \sum_{\ell\in\mathbb Z^{k-1}}
 \phi(y_{j_1}-y_{j_k}+N\ell_1,\ldots,
      y_{j_{k-1}}-y_{j_k}+N\ell_{k-1}).
\tag{5}
\]

Distinct lifts of one original label are excluded by the fixed compact
support once N is large. The limit of (5) is

\[
\int_{\mathbb R^{k-1}}\phi(z)
 \det[K(z_a-z_b)]_{a,b=1}^k\,dz,
\qquad K(v)=\frac{\sin\pi v}{\pi v},\quad z_k=0.
\tag{6}
\]

This is an all-order compact correlation criterion for the original
deterministic spectrum, conditional on (H). It does not assert pointwise
convergence of densities or convergence at every deterministic origin.
Finite deterministic anchored measures are discrete. An event Omega_N
of probability 1-o(1), without tail control on its complement, would not
be enough for this moment upgrade.

## 3. Every same-half-plane test is automatically satisfied

Write p_m=Tr U_N^m. For Im w>0, absolute Fourier convergence gives

\[
s_N(w)=i+\frac{2i}{N}\sum_{m\ge1}
 p_{-m}e^{im\alpha+2imw/N}.
\tag{7}
\]

All nonconstant origin frequencies are positive. The constant coefficient
of s_N^2+1 is zero, as is that of every derivative or divided difference.
Products of same-half-plane factors cannot introduce a zero frequency.
Therefore their expectation vanishes. The lower half-plane uses negative
frequencies and gives the same conclusion. Holomorphic extension covers
coincident arguments. This argument also annihilates the derivative term
for any beta>0, not merely beta=2.

Consequently an all-upper resolvent computation, however accurate, is not
evidence for (H): it passes for every unitary spectrum.

## 4. First mixed test and its exact CUE reference

For s>0 take w_1=is/2, w_2=-is/2, q=exp(-2s/N), and define

\[
L_N(s)=N^{-2}\sum_{m\ge1}q^m|p_m|^2,\qquad
C_N^0(s)=N^{-3}\sum_{a,b\ge1}q^{a+b}p_{-a}p_{-b}p_{a+b}.
\tag{8}
\]

Multiplying (7) and its lower-half-plane counterpart leaves only balanced
origin frequencies. The cubic first term of (3) is 8i(L_N+C_N^0).
The expected differentiated quotient is 2i/(w_1-w_2)^2=-2i/s^2. Hence

\[
\boxed{\mathcal E_{2,N}(is/2,-is/2)
 =8i\left(L_N(s)+C_N^0(s)-\frac1{4s^2}\right).}
\tag{9}
\]

C_N^0 need not be real. Equation (9) does not close at pair order: it
couples the Abel pair statistic to cubic traces on the same time scale.

For reference, the exact CUE trace formulas, reconstructed in the parent
checkpoint, give

\[
\begin{split}
\mathbb E_{\rm CUE}L_N&=\frac{q(1-q^N)}{N^2(1-q)^2},\\
\mathbb E_{\rm CUE}C_N^0&=\frac{q^{N+1}}{N^2(1-q)^2},\\
\mathbb E_{\rm CUE}(L_N+C_N^0)&=\frac1{4N^2\sinh^2(s/N)}.
\end{split}\tag{10}
\]

For the cubic identity, sum
N-(N-a)_+-(N-b)_++(N-a-b)_+ over a+b=m. The answer is N(m-N)_+:
for m<=N it is zero; for N<m<=2N evaluate the two finite arithmetic
progressions; for m>=2N each progression is N(N-1)/2. Summation in m
proves (10). In particular, the finite circular CUE residual in (9) has
mean O(N^-2), not exactly zero. The limiting pair and cubic references are
(1-e^-2s)/(4s^2) and e^-2s/(4s^2), respectively.

No infinite trace series needs truncation to evaluate (8). Set

\[
x_{\ell j}=q e^{i(\theta_\ell-\theta_j)},\quad
A_\ell=\sum_j\frac{x_{\ell j}}{1-x_{\ell j}},\quad
B_\ell=\sum_j\frac{x_{\ell j}}{(1-x_{\ell j})^2}.
\tag{11}
\]

Then L_N=N^-2 Re sum A_l, C_N^0=N^-3 sum A_l^2, and
L_N'=-2N^-3 Re sum B_l. These are exact geometric sums.

## 5. Brownian generator exposes the missing feedback

Take a Hermitian basis H_a orthonormal for Tr(H_a H_b)=delta_ab, and
D_H f(U)=d/dt f(exp(itH)U)|_{t=0}. The conventional unitary Brownian
generator is G=(2N)^-1 sum_a D_{H_a}^2. Matrix completeness gives
sum H_a X H_a=Tr(X)I and sum H_a^2=NI. Differentiating traces yields

\[
\begin{split}
G p_m&=-\frac m2p_m-\frac m{2N}
                  \sum_{a=1}^{m-1}p_a p_{m-a},\\
G|p_m|^2&=m^2-m|p_m|^2-
 \frac mN\Re\left(\bar p_m\sum_{a=1}^{m-1}p_a p_{m-a}\right).
\end{split}\tag{12}
\]

The positive cross-variation term is m^2, including for m>N. Absolute
convergence at q<1 permits summing differentiated series. With

\[
I_N=\frac{q(1+q)}{N^3(1-q)^3},\quad
C_N^1=N^{-4}\sum_{a,b\ge1}(a+b)q^{a+b}
             \Re(p_{-a}p_{-b}p_{a+b})
       =2N^{-4}\Re\sum_\ell A_\ell B_\ell,
\]

the generator in time T=N times physical Brownian time satisfies

\[
\frac1N G L_N= I_N+\frac12L_N'-C_N^1
 =\frac12\partial_s\left[L_N+\Re C_N^0
             -\frac{q}{N^2(1-q)^2}\right].
\tag{13}
\]

Thus even the infinitesimal Brownian comparison needs the real part of
the mixed loop defect. Calling the perturbation weak does not establish
its negligibility on microscopic observables. Nor does (13) control the
imaginary part of (9), much less the full hierarchy.

For the exact N-point clock, p_m=N when N divides m and otherwise zero.
Writing r=e^-2s gives L_N=r/(1-r), C_N^0=r^2/(1-r)^2. Hence

\[
\mathcal E_{2,N}=2i(\sinh^{-2}s-s^{-2})\ne0.
\tag{14}
\]

Its resolvent moments are bounded uniformly in N, so the normalized
condition (H) really fails. Meanwhile all same-half-plane tests pass.
Its Brownian drift has the nonzero limit

\[
\frac1{4s^3}-\frac{\cosh s}{4\sinh^3s}>0.
\tag{15}
\]

To check the sign, differentiate 3log(sinh(s)/s)-log(cosh(s)). After
multiplication by s sinh(s) cosh(s), the numerator is
h=s(3+2sinh^2(s))-3sinh(s)cosh(s). Its derivative is
4sinh(s)(s cosh(s)-sinh(s))>0 and h(0)=0. This is an abstract control,
not a counterexample for our perturbed Anosov map.

## 6. Attempt to obtain Brownian directions from the actual dynamics

Two direct replacements of deterministic transport by isotropic noise
fail as general mechanisms.

First, at an odd prime p, S=[[3,4],[2,3]] has order K dividing
p-(2/p). In the split case this follows from its reciprocal eigenvalues
in F_p; in the nonsplit case they lie in the norm-one subgroup of
F_(p^2). Its discriminant 32 is nonzero at odd p. Exact Weyl covariance
then makes M_p^K scalar. Consequently A_j=M_p^j A M_p^-j is K-periodic,
and every covariance assembled from these linear directions has rank
at most K<=p+1 on Hermitian matrices. After removing the scalar direction
the ambient dimension is p^2-1. For p>=3 the covariance cannot approach
a positive scalar multiple of the identity in relative operator norm:
its nullspace gives relative error at least one. Arbitrarily long
averaging of this unperturbed orbit does not remove that nullspace.

Second, replacing M by a unitary V with simple spectrum does not make its
transported directions immediately isotropic in eigenangles. In V's
eigenbasis, (V^j A V^-j)_{kk}=A_{kk}, independently of j. For any Gaussian
linear combination X=sum_j xi_j V^j A V^-j, first-order eigenangle
velocities are A_{kk} sum_j xi_j. Their covariance has rank at most one.
On the quotient by common rotation it still has rank at most one, while
isotropic unitary Brownian motion has rank N-1. This rules out that
particular instantaneous generator identification for N>=3. Simplicity
is an explicit hypothesis of this statement, not an established global
property of the frozen family.

Neither argument excludes bracket-generated diffusion at later times,
nonlinear interaction among kicked directions, or BGS itself. It identifies
the extra mathematical mechanism that a noise-based proof must supply.
Classical mixing and fixed-time Egorov alone have not supplied it here.

## 7. What was executed and what remains

`checks.py` evaluates (3) by direct cotangent quadrature, (8) by both
Fourier sums and the independent geometric sums (11), and (12)--(13)
by matrix finite differences over a full Hermitian basis. Integer and
rational computations check the CUE generating identities. Controls
include clocks, irregular fixed spectra, and the original raw matrices
with an auxiliary exponent 0.17. That exponent verifies identities;
it is not an experiment at the prescribed tau=10^-80.

The maximum mixed-loop identity error was 2.67e-15; same-half-plane
error 4.91e-15; Richardson-extrapolated generator error 4.11e-8.
These are floating consistency checks, not interval proofs. The algebraic
proofs above do not depend on floating accuracy. A fresh internal audit
checked sections 1--4 and the all-order correlation implication; this is
not external peer review or Lean certification.

The remaining obligation is (H), including mixed arguments and every
fixed order, for the original fixed family. Even its first mixed test
requires a Heisenberg-scale cubic estimate not obtained here. The
alternative pair target L_N(s)->(1-e^-2s)/(4s^2) from the parent checkpoint
also remains open. No commit or push is justified by this checkpoint.
