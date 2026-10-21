> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round3_2026_10_21/fixed_band_completion_countermodel.md`. Embedded SHA256: `ee6590231f03a40a36e2a6929145f6c9595a1c14d17e8096ff86621cd71d6fa8`.
> [Thematic guide](../../topics/closure.md).

# A deterministic countermodel to completion from one Fourier band

Date: 2026-10-21. Author: research continuation of `/root`.

## Scope and status

This theorem concerns a **different** family of diagonal unitary matrices.
It is not a counterexample to the specified kicked matrices `U_N`, and it
does not establish or refute their `H_diag`. It tests a proposed proof
mechanism: recovering arbitrary Fourier bands from all factorial orders
in one fixed band, positivity, exact finite-dimensional characteristic
polynomial identities, and the fact that a spectrum has exactly `N`
points. The countermodel obeys all those structural constraints.

The construction and estimates below are self-contained. No priority or
historical novelty is claimed. The probabilistic ensemble is an
intermediate existence construction for a deterministic sequence; it is
not introduced as an averaging operation on the original matrices.

## 1. The precise statement

Fix any finite `B>0`. There is a deterministic unitary family `W_N`, for
every odd `N`, with these properties.

1. For every fixed `k>=2` and every admissible test `b` in the original
   question with `supp bhat` contained in `[-B,B]`,

   `M^{W}_{k,N}(b)-M^{CUE}_{k,N}(b) -> 0`.

2. There is one fixed admissible test `b_+`, with larger compact Fourier
   support, and one fixed `epsilon>0`, such that for all sufficiently
   large odd `N`,

   `M^{W}_{2,N}(b_+)-M^{CUE}_{2,N}(b_+) >= epsilon`.

3. The random translates of the spectra of `W_N` converge in local law
   to a stationary, simple point process `mu_{omega,eta}` of intensity
   one, different from `Sine_2`.

An explicit finite-`N` ensemble used to select `W_N` matches the CUE
factorial statistics in the prescribed band **exactly**, at every order.

Choose an integer `omega>max(B+1,2)` and `0<eta<1`. The limiting
two-point factorial density is

$$
\rho^{\rm mod}_2(x,y)=
\left(1+\frac{\eta^2}{2}\cos(2\pi\omega(x-y))\right)
\left(1-\left(\frac{\sin\pi(x-y)}{\pi(x-y)}\right)^2\right).
\tag{1.1}
$$

In particular, this is a counterexample to a general one-band
completion theorem, even when the input sequence is deterministic and
the convergence is along all odd dimensions.

## 2. A normalized finite-dimensional ensemble

On the circle with Lebesgue measure, let `Pi_N` be the orthogonal
projection onto the span of `e_j(theta)=exp(2 pi i j theta)`,
`0<=j<N`. Its kernel is

$$
\Pi_N(\theta,\theta')=
\sum_{j=0}^{N-1}e^{2\pi i j(\theta-\theta')}.
$$

For `phi in [0,2pi)`, put

$$
a_{N,\phi}(\theta)
=1+\eta\cos(2\pi\omega N\theta+\phi).
\tag{2.1}
$$

Since `omega N>N-1`, the only Fourier coefficients of `a` that can
occur in `Pi_N a Pi_N` are its constant coefficient. Therefore

$$
\Pi_N M_{a_{N,\phi}}\Pi_N=\Pi_N.
\tag{2.2}
$$

The functions `sqrt(a) e_j` are consequently orthonormal. Their Gram
determinant gives the nonnegative symmetric probability density

$$
\frac1{N!}
\left|\det[e^{2\pi i j\theta_l}]_{j=0,\ldots,N-1;,l=1,\ldots,N}\right|^2
\prod_{l=1}^N a_{N,\phi}(\theta_l).
\tag{2.3}
$$

For completeness, normalization follows by expanding the determinant
and its conjugate. Integrating each coordinate produces its Gram
matrix entry; summing the two permutations gives `N! det G=N!`.
The same expansion with a factor `prod_l(1+t v(theta_l))` gives

$$
\mathbb E_{N,\phi}\prod_{l=1}^N(1+t v(\theta_l))
=\det_{\operatorname{Ran}\Pi_N}
\left(I+t\Pi_N M_{a_{N,\phi}v}\Pi_N\right).
\tag{2.4}
$$

Integrating out coordinates in (2.3) also gives factorial densities
`det[K_{N,phi}(theta_i,theta_j)]`, where

$$
K_{N,\phi}=M_{\sqrt a}\Pi_N M_{\sqrt a}.
\tag{2.5}
$$

Equation (2.2) proves `K^2=K`; this is a rank-`N` orthogonal projection.
Thus (2.3) is an exact `N`-point projection process, with no appeal to
an existence theorem for infinite determinantal processes.

We also choose `phi` uniformly. The resulting ensemble is invariant
under circle rotations: a rotation changes `phi` by a constant, and
the uniform law of `phi` is invariant. Its mean intensity is exactly
`N` on the circle, or one after unfolding by `N`.

## 3. Exact agreement throughout one prescribed band

For the original periodization

$$
b_N(\theta)=\sum_{l\in\mathbb Z}b(N(\theta+l)),
\qquad
\widehat{b_N}(m)=N^{-1}\widehat b(m/N),
$$

assume `supp bhat` is contained in `[-B,B]`. A matrix entry of
`Pi_N (a-1)b_N Pi_N` uses a Fourier coefficient of `b_N` at one of

$$
i-j+\omega N,\quad i-j-\omega N,
\qquad |i-j|\le N-1.
$$

Their absolute values exceed `BN`, since `omega>B+1`. Hence

$$
\Pi_N M_{a_{N,\phi}b_N}\Pi_N
=\Pi_N M_{b_N}\Pi_N
\quad\hbox{for every }N,\phi.
\tag{3.1}
$$

The same argument applies to any translated `b_N(theta-alpha)`.
The matrix on the right has entries `N^{-1} bhat((i-j)/N)` up to
transpose and diagonal unitary conjugation. Its elementary symmetric
functions are exactly the CUE benchmark in the question. Comparing
coefficients in (2.4), and then averaging in `alpha`, proves

$$
\mathbb E_{N,\phi}M_{k,N}(b)=M^{\rm CUE}_{k,N}(b)
\tag{3.2}
$$

for **every** `k`, including `k>N`, every `phi`, every `N`, and every
test in the fixed band. The generating polynomial identity is exact;
there is no small-`k` or low-order remainder.

## 4. Its actual local limit

Write `x=N theta`. A harmless kernel gauge removes the central
frequency of `Pi_N`. The rescaled kernel then is

$$
\widetilde K_{N,\phi}(x,y)=
\sqrt{a_\phi(x)a_\phi(y)}
\frac{\sin\pi(x-y)}{N\sin(\pi(x-y)/N)},
\qquad
a_\phi(x)=1+\eta\cos(2\pi\omega x+\phi).
\tag{4.1}
$$

The quotient at its removable zeros is interpreted by continuity.
On every fixed compact set this converges uniformly to

$$
K_\phi(x,y)=\sqrt{a_\phi(x)a_\phi(y)}
\frac{\sin\pi(x-y)}{\pi(x-y)}.
\tag{4.2}
$$

The factorial densities satisfy the uniform Hadamard bound

$$
0\le\rho_{k,N,\phi}(x_1,\ldots,x_k)\le(1+\eta)^k
\tag{4.3}
$$

on a lifted interval of length less than `N`. If `0<=h<=1` has fixed
compact support, the absolute value of the `k`th Fredholm expansion
term is at most `((1+eta) integral h)^k/k!`. Dominated convergence of
these expansions proves convergence of the local Laplace
functionals, first for each `phi` and then averaged over `phi`.
Tightness follows from the uniform bound on the expected number of
points in each compact interval. This constructs the limiting law
`mu_{omega,eta}` directly from (2.3).

For each `phi`, (4.2) is also an orthogonal projection on the line:
if `P` projects onto Fourier frequencies `[-1/2,1/2]`, then
`P a_phi P=P`, because `omega>1`. Hence
`sqrt(a_phi) P sqrt(a_phi)` squares to itself. This observation is
consistent with, but is not needed for, the existence argument above.

Translation by `s` changes the phase to `phi+2 pi omega s`.
The uniform phase mixture is stationary, of intensity one. Its
two-point density is obtained from the `2x2` determinant and

$$
\frac1{2\pi}\int_0^{2\pi}a_\phi(x)a_\phi(y)\,d\phi
=1+\frac{\eta^2}{2}\cos(2\pi\omega(x-y)).
$$

This proves (1.1). It differs from the sine density on an open set.
All local second moments are finite by (4.3), so the laws themselves
are different, not merely two unverified formal moment lists.

## 5. An explicit admissible test that detects the difference

Let `0<delta<1/4`. Choose any nonzero, real, even, nonnegative
`varphi in C_c^infty((-delta/2,delta/2))`; put
`g=F^{-1} varphi`, `w=|g|^2`, and

$$
c=\frac1{4\|w\|_\infty},\qquad
b_+(x)=c\,w(x)\bigl(1+\cos(2\pi\omega x)\bigr).
\tag{5.1}
$$

Then `b_+` is nonnegative Schwartz, has supremum at most `1/2`, and
has smooth compactly supported Fourier transform. The support is in
`[-omega-delta,omega+delta]`. Further,

$$
\widehat b_+(\omega)=\frac c2\widehat w(0)>0,
\qquad
|\widehat w(u)|\le\widehat w(0),
\qquad
\operatorname{supp}\widehat w\subset[-\delta,\delta].
\tag{5.2}
$$

For any real Schwartz `b`, (1.1) and the elementary Fourier identity
`F[(sin(pi x)/(pi x))^2](u)=(1-|u|)_+` give

$$
M^{\rm mod}_2(b)-M^{\rm sine}_2(b)
=\frac{\eta^2}{4}\left(
|\widehat b(\omega)|^2
-\int_{-1}^{1}(1-|u|)|\widehat b(\omega-u)|^2\,du
\right).
\tag{5.3}
$$

Here `M_2=1/2 integral b(x)b(y) rho_2(x,y) dx dy`, as in the
question. To check constants, the density correction has coefficient
`eta^2/2`; the unordered-pair factor contributes another `1/2`.
The first Fourier integral in (5.3) is `|bhat(omega)|^2`; convolution
with the triangle transform gives the second.

For (5.1), since `omega>2`, only the translated Fourier bump around
`omega` meets `omega-[-1,1]`. The integral in (5.3) is bounded above
by `2 delta |bhat_+(omega)|^2`. Consequently

$$
d_+:=M^{\rm mod}_2(b_+)-M^{\rm sine}_2(b_+)
\ge\frac{\eta^2}{4}(1-2\delta)
|\widehat b_+(\omega)|^2>0.
\tag{5.4}
$$

For a test supported in the original band, both terms in (5.3)
vanish. This is the two-point instance of the all-order identity
(3.2), not its proof.

## 6. Concentration of spatial factorial averages

This section makes the sequence in Section 1 deterministic. The
necessary estimate is only for this explicit auxiliary ensemble.

For a configuration on the circle of unfolded length `N`, let
`F_{k,b}(t)` be its local weighted unordered `k`-tuple statistic about
`t`. Then `M_{k,N}(b)=N^{-1} integral_0^N F_{k,b}(t) dt`.
First suppose `b` is bounded and supported in `[-R,R]`, with `N>8R`.

Conditional on `phi`, the modulus of the rescaled kernel satisfies

$$
|\widetilde K_{N,\phi}(x,y)|\le1+\eta,
\qquad
|\widetilde K_{N,\phi}(x,y)|
\le\frac{1+\eta}{2\operatorname{dist}_N(x-y,0)}
\tag{6.1}
$$

when the circular distance is nonzero. The latter follows from
`|sin(pi z/N)|>=2 dist_N(z,0)/N` for circular distance at most `N/2`.

When the two test windows about `t,s` are disjoint, their product
moment uses a `2k x 2k` determinant. Subtracting the two separate
`k x k` determinants leaves only permutations that cross between the
windows. Every such permutation crosses at least twice. If their
centres have circular distance `d>4R+1`, (6.1) therefore gives

$$
|\operatorname{Cov}_\phi(F_{k,b}(t),F_{k,b}(s))|
\le C_{k,b,R}(1+d)^{-2}.
\tag{6.2}
$$

Indeed there are at most `(2k)!` permutations, at least two factors
are bounded by `C/(d-2R)`, the others by `1+eta`, and the product of
the absolute test weights has a fixed integrable integral. No
independence of the disjoint windows is assumed.

For overlapping windows the same covariance is uniformly bounded:
expanding the square of `F` groups the coincident point indices into
at most `2k` distinct points, and (4.3) bounds every resulting
integral. Thus (6.2), with a larger constant, holds at all distances.

The conditional mean of the spatial average is independent of
`phi`. One way to see this is to rotate the configuration by
`phi/(2 pi omega N)` in (2.3); the spatial average itself is rotation
invariant. Integrating (6.2) and using the law of total variance yields

$$
\operatorname{Var}(M_{k,N}(b))\le C_{k,b,R}/N.
\tag{6.3}
$$

Exactly the same proof applies to fixed mixed factorial weights and
to any fixed power of a local weighted count, after expanding that
power by coincidences of indices.

The convergence in probability following from (6.3) extends to every
Schwartz test, to `w_0(x)=(1+x^2)^{-1}`, and to their fixed mixed
powers and compact truncations. Here is the
uniform tail justification. For such tests, the periodizations have
uniform bounded supremum for the tests used here and unchanged
`L^1` integral on the unfolded circle. Expanding a fixed polynomial
moment into distinct indices and applying (4.3) bounds it by a finite
polynomial in those `L^1` and supremum norms. If one factor is a tail
`b-b 1_{[-R,R]}`, at least one factor has `L^1` norm tending to zero;
the other factors stay bounded. Thus the `L^2` error of each fixed
local polynomial, and hence of its spatial average by Jensen, tends
to zero uniformly in `N` as `R->infinity`. For `w_0` this follows
also directly from its `O((1+|x|)^{-2})` bound. This proves

$$
M_{k,N}(b)-\mathbb E M_{k,N}(b)\longrightarrow0
\quad\hbox{in probability}
\tag{6.4}
$$

for the stated tests, and the analogous assertion for every fixed
ordinary moment of the periodized weighted count using `w_0`.

The ensemble expectations in (6.4) converge to those of `mu`, by
Section 4, the same tail bound, and (4.3). In particular all the
ordinary `w_0` count moments are uniformly finite. If

$$
Q_{p,N}:=\frac1N\int_0^N
\left(\sum_{j,l}w_0(x_j-t+lN)\right)^pdt,
$$

then `Q_{p,N}` converges in probability to a finite constant `q_p`.

For completeness, spatially averaged local Laplace functionals also
converge in probability to those of `mu`. Put `h=1-exp(-f)` for a
nonnegative compactly supported continuous `f`. Bonferroni bounds
the product between two consecutive finite sums of `M_{k,N}(h)`.
Each fixed term concentrates by (6.3); the difference between the
limiting consecutive sums is bounded by
`((1+eta) integral h)^J/J!`, which tends to zero. This proves the
claim without a separate mixing theorem for nonlinear observables.

## 7. Selecting one deterministic configuration in every dimension

Take a countable dense subset of the admissible band-`B` tests in
the norm

$$
\|b\|_{w_0}:=\sup_x(1+x^2)|b(x)|.
\tag{7.1}
$$

Such a subset exists because the Schwartz space is separable and
its inclusion into this normed space is continuous; equivalently,
use second countability of the Schwartz topology and then its image.
Include all positive integer factorial orders of these tests, the
test `b_+`, every `Q_p`, and a countable convergence-determining
collection of local Laplace functionals in one list of observables.

Every finite initial part of this list converges in probability to
the prescribed values. Hence there are increasing integers `N_q`
such that, for every odd `N>=N_q`, there is a configuration for which
the first `q` errors are less than `1/q` (using a harmless tolerance
adjustment for each fixed expected value). Set
`q(N)=max{q<=N: N_q<=N}`. Choose one such configuration for each
`N`; then `q(N)->infinity`. This is selection separately in every
dimension, with no subsequence or averaging in `N`.

If an explicit deterministic selection rule is desired, enumerate
the rational-angle configurations densely and choose the first one
meeting the finitely many strict inequalities. The observables are
continuous in the point positions, so a nonempty open good set
contains such a configuration. Small dimensions can be assigned
arbitrarily. Define `W_N` as the diagonal unitary with the selected
angles.

We check that passage from a countable set of tests to every test
does not assume moment convergence from weak convergence. The
selection enforces `limsup_N Q_{k,N}<infinity` for each fixed `k`.
If `||b-c||_{w_0}<=epsilon` and both `b,c` have `w_0` norm at most
`C`, telescoping products gives

$$
|M_{k,N}(b)-M_{k,N}(c)|
\le\frac{\epsilon C^{k-1}}{(k-1)!}\,Q_{k,N}.
\tag{7.2}
$$

The identical inequality holds for the limiting process with `q_k`.
The periodized pointwise inequalities needed here follow from
`|b-c|<=epsilon w_0`; then sum over unordered tuples and bound their
remaining factors by the `(k-1)`st power of the total `w_0` count.
Thus density and (7.2) extend convergence to every admissible test
in the band.

For that band the limiting factorial values equal the CUE limits
by (3.2); hence assertion 1 follows. For `b_+`, (5.4) gives

$$
M^W_{2,N}(b_+)-M^{\rm CUE}_{2,N}(b_+)\to d_+>0.
$$

Choosing `epsilon=d_+/2` proves assertion 2 along all sufficiently
large odd dimensions. The selected Laplace functionals and the
exact intensity-one identity for each random translate give
assertion 3. More explicitly, intensity implies tightness and
`L^1`-Lipschitz control of local Laplace functionals; a dense test
collection therefore determines every subsequential limit.

## 8. Consequence for the original proof search

All finite algebraic identities involving traces, partitions,
characteristic polynomial reciprocity, and exactly `N` unit-modulus
eigenvalues hold for `W_N`. All factorial orders in any prescribed
fixed band can hold simultaneously, while another fixed band
detects a nonzero pair discrepancy. Therefore a proof for the
specified kicked family must use information that distinguishes
its full phases from this construction. No combination of those
general finite-dimensional identities with one-band agreement
alone can supply the missing arbitrary-band conclusion.

This is a rigorous exclusion of a completion mechanism. It leaves
the exact original-family pair compensation estimate `(R)` and the
full `H_diag` open in this investigation.
