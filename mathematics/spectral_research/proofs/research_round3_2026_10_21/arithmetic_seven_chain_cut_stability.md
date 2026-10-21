> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round3_2026_10_21/arithmetic_seven_chain_cut_stability.md`. Embedded SHA256: `d6ddc0695d91441729852ea5fc89d6318a1297b22eb4837cd5d3e0c930c3d349`.
> [Thematic guide](../../topics/closure.md).

# Seven-chain cutting at every odd dimension: exact spectral stability

Date: 21 October 2026. Original-family arithmetic branch.

## 0. Target, result, and evidence boundary

The proposed discriminator was the exact decomposition of the Hamiltonian into
seven Jacobi chains when `7 | N`. Could this produce a distinct infinite
subsequence of spectral statistics after multiplication by the full matrix
`M_N`? The argument below does not produce such a counterexample. It proves
instead that a seven-chain Hamiltonian can be obtained at **every** sufficiently
large odd dimension by a spectrally negligible modification, with explicit
norms and quantitative stability of the complete pair statistics.

Write `U_N^c` for the matrix constructed in Section 1. It uses the original
fixed `tau = 10^(-80)` and the original `M_N`. The results are:

1. `A_N^c` is the direct sum of seven paths of lengths `floor(N/7)` or
   `ceil(N/7)`, and `A_N^c = A_N` whenever `7 | N`.
2. `||U_N-U_N^c||_1 <= (28 pi^2/25) tau/N`, with a simultaneous matching of
   eigenphases satisfying both a total displacement bound and a uniform
   microscopic displacement bound.
3. For each nonnegative compactly supported `C^1` test function `f`, the
   difference of the two local Laplace functionals is at most
   `(14 pi/25)(tau/N)||f'||_1`. Consequently the two families have the same
   possible local weak limits.
4. Using only the independently checked short-time trace bound from the frozen
   base report, for every fixed admissible `b`,
   `|Delta^U_(2,N)(b)-Delta^c_(2,N)(b)| = O_b(tau/log N)`.
   The **entire** Abel pair statistic, including its infinite tail, changes by
   `O_s(tau/log N)` for each fixed `s > 0`.
5. The full `H_diag` condition holds for one of these two families if and only
   if it holds for the other. This equivalence uses the assumed `H_diag` of the
   source family to supply uniform integrability; it is not an unconditional
   claim that all higher factorial moment differences tend to zero.

These statements do not determine the pair limit, prove `H_diag`, or refute it.
In particular, the cut matrix still contains the dense metaplectic factor.
The result excludes the *mere presence of seven exact chain boundaries* as a
distinction available only on `7 | N`; it does not exclude other arithmetic
correlations on that subsequence.

### Frozen sources

| Source | SHA-256 |
|---|---|
| `Spectral_partial_results_2026-10-20.md` | `b8c5e2071d49394270006853ee8316f3900e84f1a7ae9b03e58e5c4eaf29a7cc` |
| `research_round2_2026_10_20/fermionic_pseudoorbit_cutoff.md` | `03173e53d1a10e2c1afad517c48943a5330d43fc4059b80fc0e37d5b1598a9eb` |
| `research_continuation_2026_10_20/gaussian_cocycle_and_modulus.md` | `c1a863e613a327acb5fe43ff1093c4a8fe51b37ebd5dcee9fddf0ae0a91986f1` |
| `research_round3_2026_10_21/audit_trace_foundation_independent.md` | `8cc14d6dbcae730a9a0b0a139f23fc285ce2a6a9772a1f58109f50c2b12614ac` |
| `research_round2_2026_10_20/arithmetic_oldspace_escape.md` | `596d44605310cc898fa75e23df4aa811189a1764fed21ce8b9f5d07ae734813a` |
| `research_round2_2026_10_20/arithmetic_seven_chain_discriminant_checkpoint.md` | `eee2b4caa27349a81e5cf3113d53ff1f88164e44b748c2eb99754f6e07fc6a8f` |
| `research_round2_2026_10_20/arithmetic_seven_chain_mod5_obstruction.md` | `5e19c3d9569a98f8583b10f6b044b876d5009b47d41c57f61d4554bfd77e2acc` |
| `research_round2_2026_10_20/adversarial_all_odd_eigenline_audit.md` | `8b2143715121d41735b9d2c2baa586623effce0c524dcb8cdade7b4ece542fb5` |

The oldspace, mixed-minor, mod-5, all-odd eigenline, and affine-reversal/CRT
arguments were inspected before pursuing this route. They are not premises of
the cutting proof. Sections 1–3 and 7 below depend only on the matrix
definitions. Sections 4–6 additionally use the already established trace bound
specified explicitly in (4.1), not a quantum universality assertion. The input
provenance makes that dependence visible.

## 1. Exact cuts and Schatten norm constants

Put `h_N=(N+1)/2`, the stated modular inverse of two represented as an integer.
The finite Fourier definition gives exactly

$$
(A_N)_{xx}=V(x/N),\qquad
(A_N)_{x,x+1}=w_x=\frac{e^{-i\alpha_0}}{200}
r((x+h_N)/N),                                      \tag{1.1}
$$

with the opposite entries their conjugates, where

$$
V(q)=\cos14\pi q+\frac{r(q)}{10}
 +\frac{r(q)\sin2\pi q}{100}-\frac1{10}.
$$

To verify (1.1), the `l=0` Fourier modes act diagonally. For `l=1`, their sum is
`e^(-i alpha_0) r((x+h_N)/N)/200` times the shift by one; the `l=-1` part is its
adjoint. This retains the modular half exactly.

For `j=0,...,7`, let `y_j` be the integer nearest to `Nj/7`, with `y_0=0` and
`y_7=N`. There is no rounding tie. Delete from `A_N` the seven undirected edges

$$
\{x_j,x_j+1\},\qquad x_j=y_j-h_N\pmod N,
\quad j=0,\ldots,6,                                  \tag{1.2}
$$

to define `A_N^c`. The edge `j=0` is already zero. The resulting intervals are

$$
I_j=\{h_N+y_j,\ldots,h_N+y_{j+1}-1\}\pmod N,
\quad j=0,\ldots,6.                                  \tag{1.3}
$$

Indeed, `2h_N=1 mod N`, so the left boundary edge of `I_j` is exactly `x_j`.
The lengths `y_(j+1)-y_j` equal `floor(N/7)` or `ceil(N/7)`. The zero set of
`r` on a grid of odd denominator consists precisely of the grid points
`j/7`: its other possible zero `q=1/2` is absent. It follows that the paths
in (1.3) have strictly positive internal hopping magnitudes. For `7 | N`
the seven deleted edges were all zero to begin with.

Suppose first `7` does not divide `N`. The six rounding errors

$$
e_j=y_j-Nj/7,\quad j=1,\ldots,6,
$$

are, as a multiset, exactly

$$
\{-3/7,-2/7,-1/7,1/7,2/7,3/7\}.
$$

This is because multiplication by `N mod 7` permutes the six nonzero residue
classes. Thus

$$
\sum_{j=1}^6e_j^2=4/7,\qquad \max_j e_j^2=9/49.      \tag{1.4}
$$

Using `1-cos t <= t^2/2` and `1+cos t <= 2` gives

$$
r(y_j/N)\le\frac{196\pi^2e_j^2}{N^2},\qquad
|w_{x_j}|\le\frac{49\pi^2e_j^2}{50N^2}.             \tag{1.5}
$$

For `N>=21`, the distinct cut edges have disjoint vertex pairs. Hence
`Delta A_N=A_N-A_N^c` is a direct sum of at most six off-diagonal Hermitian
two-by-two matrices. Each has eigenvalues `+|w|,-|w|`. Equations (1.4)–(1.5)
therefore prove

$$
\boxed{
\|\Delta A_N\|_1\le\frac{28\pi^2}{25N^2},\qquad
\|\Delta A_N\|\le\frac{9\pi^2}{50N^2},\qquad
\operatorname{rank}\Delta A_N\le12.
}                                                     \tag{1.6}
$$

For `7 | N` the difference is zero, so (1.6) holds for all odd `N>=21`.

Define, with the unchanged fixed kick,

$$
U_N^c=e^{i\tau N A_N^c}M_N.                           \tag{1.7}
$$

The Duhamel integral for the difference of two Hermitian exponentials, and
unitary invariance of the two norms, give

$$
\boxed{
\|U_N-U_N^c\|_1\le C_1\frac\tau N,
\qquad
\|U_N-U_N^c\|\le C_\infty\frac\tau N,
\quad
C_1=\frac{28\pi^2}{25},\quad C_\infty=\frac{9\pi^2}{50}.
}                                                     \tag{1.8}
$$

No commutativity of the Hamiltonians is used.

## 2. A simultaneous matching of eigenphases

Consider the unitary path

$$
A_N(t)=A_N-t\Delta A_N,\qquad
U_N(t)=e^{i\tau N A_N(t)}M_N,\quad 0\le t\le1.
$$

Its Hermitian instantaneous generator is

$$
G_N(t)=-iU_N'(t)U_N(t)^*
=-\tau N\int_0^1
 e^{iu\tau N A_N(t)}\Delta A_N e^{-iu\tau N A_N(t)}\,du.
                                                               \tag{2.1}
$$

Consequently

$$
\|G_N(t)\|_1\le C_1\tau/N,\qquad
\|G_N(t)\|\le C_\infty\tau/N.                         \tag{2.2}
$$

Here is the finite-dimensional phase-path fact needed to use both bounds at
once. For a `C^1` path of unitary matrices, continuous real eigenangle lifts can
be chosen absolutely continuous, and almost everywhere their derivatives are
the diagonal expectations of `G=-iU'U^*` in a suitable orthonormal eigenbasis.
In particular

$$
\sum_j|\varphi_j'(t)|\le\|G(t)\|_1,\qquad
\max_j|\varphi_j'(t)|\le\|G(t)\|.                     \tag{2.3}
$$

For completeness, this fact does not require a simultaneous optimal matching
theorem. Near any given time choose a point of the unit circle outside the
finite spectrum, and a branch of the matrix logarithm on the remaining arc.
The resulting Hermitian matrix of angles is `C^1`. Its sorted eigenvalues are
locally Lipschitz by the min–max principle and so absolutely continuous.
Their labels and integer multiples of `2pi` can be matched on finitely many
successive overlapping time intervals covering `[0,1]`.

To compute their first derivatives at a spectral cluster with eigenvalue
`lambda`, compress the first-order expansion of `U(t+epsilon)` to that
eigenspace. Smooth spectral projections and a local orthonormal frame are
available from the finite resolvent contour integral; the off-cluster block
can be eliminated to first order because its spectral gap is nonzero.
The compressed first-order term is
`i lambda epsilon PGP`. Therefore the first derivatives of the angles in
the cluster are the eigenvalues of the Hermitian compression `PGP`.
Diagonalize that compression separately in each cluster. At the almost every
time at which the Lipschitz angle labels are differentiable this proves the
asserted diagonal-expectation formula. Finally, for every unit vector `v`,
`|<v,Gv>| <= <v,|G|v>`. Summing this inequality in the chosen basis proves
the trace-norm bound in (2.3); the operator-norm bound is immediate. This also
handles multiple eigenvalues and crossings.

Integrating (2.2)–(2.3), and writing the endpoint phases in turns rather than
radians, gives one matching and real displacements `delta theta_j` such that

$$
\boxed{
\sum_{j=1}^N|\delta\theta_j|
 \le\frac{14\pi\tau}{25N},\qquad
\max_j |N\delta\theta_j|
 \le D:=\frac{9\pi\tau}{100}.
}                                                     \tag{2.4}
$$

All quantities in (2.4) refer to that same matching. The phase lifts may cross
an integer; periodicization of every statistic makes this immaterial.

## 3. Unconditional local Laplace stability

Use the same uniform `alpha` for both spectra and the matching in (2.4).
For `f>=0`, `f in C_c^1(R)`, the function `exp(-x)` is 1-Lipschitz on the
nonnegative half-line. Therefore the absolute difference of the two Laplace
functionals is at most the expectation of

$$
\sum_{j,\ell}
\left|f(N(\theta_j-\alpha+\ell))
-f(N(\theta_j+\delta\theta_j-\alpha+\ell))\right|.
$$

For one label `j`, integrating over `alpha` and summing the periods gives
exactly

$$
\frac1N\|f-f(\,\cdot+N\delta\theta_j)\|_1
\le |\delta\theta_j|\,\|f'\|_1.
$$

Thus

$$
\boxed{
\left|\mathbb E e^{-\langle f,\Xi_N^U\rangle}
      -\mathbb E e^{-\langle f,\Xi_N^c\rangle}\right|
\le\frac{14\pi\tau}{25N}\|f'\|_1.
}                                                     \tag{3.1}
$$

Both random point measures have exactly unit intensity. Their masses on each
compact set are consequently tight by Markov's inequality, and a compact
exhaustion gives tightness of their laws in the vague topology. Equation (3.1)
and the local Laplace characterization then show that they have the same
subsequential weak limits. In particular, local convergence to `Sine_2` is
equivalent for these two families. No trace estimate or factorial moment
assumption was used in this section.

## 4. The checked trace input and its two positivity consequences

For Sections 4–6 only, use the following quantitative result proved in the
frozen sources:

$$
|p_{m,N}|=|\operatorname{Tr}U_N^m|\le3a^m,
\qquad a=(1+\sqrt2)\,1.0002,                         \tag{4.1}
$$

for every positive `m` and all odd `N` beyond one fixed threshold. This is the
consequence of equations (1) and (14) of the frozen fermionic note; only its
restriction to `m <= log N/log a` is needed here. Its derivation uses the exact
orbit trace formula: fewer than `lambda^m` periodic points, outside amplitude
`lambda^(-m/2)`, each scalar graph factor bounded by `1.0002`, and residual
at most `2(0.421)^m`, with `lambda=(1+sqrt2)^2`. Taking absolute values gives
`a^m+2(0.421)^m <= 3a^m`. The raw trace foundation and its normalization were
independently reconstructed in the source listed in Section 0. Nothing about
long-time cancellation is included in (4.1).

Let

$$
L=L_N=\lfloor\log N/\log a\rfloor,
\quad
F_L(t)=\frac1L\left|\sum_{j=0}^{L-1}e^{2\pi ijt}\right|^2
=\sum_{|m|<L}(1-|m|/L)e^{2\pi imt}.                 \tag{4.2}
$$

We work at sufficiently large `N` that `L>=2`.

### 4.1 Uniform bound on the number of phases in a short arc

For every `alpha`, (4.1) gives

$$
\sum_jF_L(\theta_j-\alpha)
\le N+6\sum_{m=1}^{L-1}a^m
\le\left(1+\frac6{a-1}\right)N.                      \tag{4.3}
$$

For `|t|<=1/(2L)` modulo one, the sine formula for `F_L`, together with
`sin u >= 2u/pi` on `[0,pi/2]`, shows

$$
F_L(t)\ge4L/\pi^2.
$$

Every circular arc of length `1/L` therefore contains at most

$$
\boxed{
C_{\rm arc}\frac NL\quad\hbox{eigenphases, with multiplicities},
\qquad C_{\rm arc}=\frac{\pi^2}{4}\left(1+\frac6{a-1}\right).
}                                                     \tag{4.4}
$$

An immediate useful extension is this: for any fixed nonnegative function
`beta(x) <= C_beta(1+|x|)^(-r)`, with `r>1`, define
`beta_N(t)=sum_ell beta(N(t+ell))`. Then

$$
\boxed{
\sup_\alpha\sum_j\beta_N(\theta_j-\alpha)
 \le C'_\beta\frac NL.
}                                                     \tag{4.5}
$$

To prove (4.5), place all periodically lifted microscopic coordinates into
the real intervals `[vQ,(v+1)Q)`, where `Q=N/L>=1` and `v` is an integer.
By (4.4), each interval contains at most `C_arc Q` points. The sum over `v`
of the suprema of `beta` on these intervals is at most
`2 C_beta(1+sum_(n>=1)(1+nQ)^(-r))`, uniformly bounded for `Q>=1`.
Multiplying these two bounds proves the assertion. In particular, it applies
to any Schwartz envelope, whether or not that envelope is smooth.

### 4.2 Sliding Fejer windows for squared traces, including the zero mode

For completeness there is a separate positive-energy consequence of (4.1).
Set `a_m=|p_(m,N)|^2`, including `a_0=N^2`, and
`W_L(m)=(1-|m|/L)_+`. For any integer `v`,

$$
\begin{aligned}
0\le\sum_mW_L(m-v)a_m
&=\sum_{i,j}e^{2\pi iv(\theta_i-\theta_j)}
                F_L(\theta_i-\theta_j)\\
&\le\sum_{i,j}F_L(\theta_i-\theta_j)
=\sum_mW_L(m)a_m.                                   \tag{4.6}
\end{aligned}
$$

The middle expression is real and nonnegative because it equals the left
side. Its upper bound follows from the triangle inequality and `F_L>=0`.
The centered sum is, with the zero mode kept explicitly,

$$
\sum_mW_L(m)a_m
\le N^2+18\sum_{m=1}^{L-1}a^{2m}\le C_0N^2,\qquad
C_0=1+\frac{18}{1-a^{-2}}.                           \tag{4.7}
$$

Every interval of `floor(L/2)` consecutive integer times consequently has
sum of squared traces at most `2C_0N^2`. Covering `1<=m<=BN` yields

$$
N^{-2}\sum_{1\le m\le BN}|p_{m,N}|^2=O_B(N/L).
                                                               \tag{4.8}
$$

For the full exponential weight, use the same consecutive blocks. On block
`v`, the weight is bounded by `exp(-2s v floor(L/2)/N)`. Summing this geometric
series, with no discarded tail, proves

$$
N^{-2}\sum_{m\ge1}e^{-2sm/N}|p_{m,N}|^2=O_s(N/L),\quad s>0.
                                                               \tag{4.9}
$$

These are growth bounds, not the desired `O(1)` form-factor asymptotics.

## 5. Unconditional stability of every admissible pair statistic

Fix an admissible `b` from the question. Use the phase matching (2.4), put
`d_j=N delta theta_j`, and define the nonnegative, rapidly decreasing envelope

$$
\beta(x)=\sup_{|u|\le D}b(x+u)
        +\sup_{|u|\le D}|b'(x+u)|.                   \tag{5.1}
$$

At a fixed `alpha`, write

$$
x_j=b_N(\theta_j-\alpha),\quad
y_j=b_N(\theta_j+\delta\theta_j-\alpha),\quad
Z=\sum_j\beta_N(\theta_j-\alpha),\quad
W=\sum_j|x_j-y_j|.
$$

Each `x_j,y_j` is bounded by its corresponding summand in `Z`. Translation
in `L^1(R)`, followed by integration over `alpha`, gives

$$
\mathbb EW\le\|b'\|_1\sum_j|\delta\theta_j|
\le\frac{14\pi\tau}{25N}\|b'\|_1.                   \tag{5.2}
$$

Telescoping the pair products gives

$$
|e_2(x)-e_2(y)|\le WZ.
$$

Applying (4.5) to (5.1) and then (5.2) proves

$$
\boxed{
|M^U_{2,N}(b)-M^c_{2,N}(b)|
=|\Delta^U_{2,N}(b)-\Delta^c_{2,N}(b)|
=O_b(\tau/\log N).
}                                                     \tag{5.3}
$$

This does not assume bounded pair moments or `H_diag` for either family.

In the Fourier form, (5.3) is precisely a stability estimate on the **entire
weighted sum**

$$
\frac1{N^2}\sum_{m\ge1}|\widehat b(m/N)|^2
\left(|\operatorname{Tr}U_N^m|^2
     -|\operatorname{Tr}(U_N^c)^m|^2\right)
=O_b(\tau/\log N).                                  \tag{5.4}
$$

The `m=0` terms and the subtracted `N` terms agree and cancel. The two signs
of nonzero `m` cancel the `1/2` in the second factorial moment. This verifies
the normalization in (5.4).

There is also a simpler, weaker Fourier check: telescoping powers in (1.8)
gives `|p_m-q_m| <= C_1 tau m/N`. For any fixed nonnegative compactly supported
weight `w`, the triangle inequality in the weighted sequence Hilbert space
therefore yields

$$
\left|\sqrt{N^{-2}\sum_{m\ge1}w(m/N)|p_m|^2}
      -\sqrt{N^{-2}\sum_{m\ge1}w(m/N)|q_m|^2}\right|
\le\frac{C_1\tau}{N^2}
       \left(\sum_{m\ge1}m^2w(m/N)\right)^{1/2}
=O_w(\tau/\sqrt N).                                  \tag{5.5}
$$

Combining (5.5) with (4.8) gives an unconditional `O_w(tau/sqrt(log N))`
stability estimate even for a bounded nonnegative band weight with no smooth
inverse Fourier transform. Formula (5.3) is stronger for the actual
admissible factorial statistics.

## 6. Complete Abel statistic: the infinite tail is included

For fixed `s>0`, set

$$
\mathcal F_{s,N}(U)=N^{-2}\sum_{m\ge1}
e^{-2sm/N}|\operatorname{Tr}U^m|^2,
\quad
c_s(x)=\frac{s}{s^2+\pi^2x^2}.
$$

An elementary integral gives

$$
\widehat c_s(\xi)=e^{-2s|\xi|},\qquad \int c_s=1.
$$

The absolutely convergent periodicization
`c_(s,N)(t)=sum_ell c_s(N(t+ell))` has Fourier coefficients
`N^(-1)exp(-2s|m|/N)`. Consequently the following is exact:

$$
\mathcal F_{s,N}(U)
=\frac1{2N}\sum_{i,j}c_{s,N}(\theta_i-\theta_j)-\frac12.
                                                               \tag{6.1}
$$

This identity involves the entire positive-time sum. The constant `-1/2`
comes from the zero Fourier mode `|p_0|^2=N^2`.

Since `|d_i-d_j|<=2D`, use the even nonnegative envelope

$$
\eta_s(x)=\sup_{|u|\le2D}|c_s'(x+u)|
\le C_s(1+|x|)^{-3}.                                 \tag{6.2}
$$

The mean value inequality, (6.1), and evenness give

$$
\begin{aligned}
|\mathcal F_{s,N}(U_N)-\mathcal F_{s,N}(U_N^c)|
&\le\frac1{2N}\sum_{i,j}(|d_i|+|d_j|)
                    \eta_{s,N}(\theta_i-\theta_j)\\
&\le\frac1N\left(\sum_i|d_i|\right)
     \sup_\alpha\sum_j\eta_{s,N}(\theta_j-\alpha).
\end{aligned}
$$

Now (2.4) gives `sum |d_i| <=14 pi tau/25`, and (4.5) applies to (6.2).
Therefore

$$
\boxed{
|\mathcal F_{s,N}(U_N)-\mathcal F_{s,N}(U_N^c)|
=O_s(\tau/\log N),\qquad s>0\text{ fixed}.
}                                                     \tag{6.3}
$$

No infinite tail was dropped or controlled by a formal pointwise limit.
Equations (6.1)–(6.3) treat it directly through an integrable derivative
envelope. Thus the proposed Abel limit, if established for either family,
would transfer to the other. Its value is not established here.

## 7. Full `H_diag` equivalence, with the moment premise explicit

This section uses (2.4) and the definition of `H_diag`, but does not use (4.1).
We prove

$$
\boxed{H_{\rm diag}(U_N)\quad\Longleftrightarrow\quad
        H_{\rm diag}(U_N^c).}                         \tag{7.1}
$$

The requirement of all fixed orders in `H_diag` is used, not omitted.

### 7.1 Positive band-limited majorant

Every nonnegative rapidly decreasing function `beta` has a nonnegative
Schwartz majorant `B` whose Fourier transform is smooth and compactly
supported. Here is a construction. Take a nonzero nonnegative smooth compactly
supported function `phi`, let `g` be its inverse Fourier transform, and use
`K=|g|^2`. It is nonnegative Schwartz, has smooth compactly supported Fourier
transform, and satisfies `K>=c>0` on `[-r,r]` for some `r,c>0`, because
`g(0)=int phi>0`. Set

$$
a_n=c^{-1}\sup_{|x-nr|\le r}\beta(x),\qquad
B(x)=\sum_{n\in\mathbb Z}a_nK(x-nr).                 \tag{7.2}
$$

The coefficients decay faster than any power. Every derivative series in
(7.2) converges with all Schwartz seminorms. For a point `x`, choose the
nearest lattice site `nr`; its one summand is at least `beta(x)`. Thus `B`
is the required majorant. Also

$$
\widehat B(\xi)=\widehat K(\xi)
\sum_na_ne^{-2\pi inr\xi}\in C_c^\infty.
$$

Choose `C>||B||_infinity`; then `b_0=B/C` is an admissible test function.
The zero function case is immediate and can be omitted from this construction.

### 7.2 Uniform moments supplied by the source `H_diag`

Assume `H_diag` for the original family, and fix the target test `b` and an
integer `k>=2`. Apply (7.2) to the envelope (5.1). For sufficiently large `N`,
`0<=b_(0,N)<=1`: the closest periodic copy is bounded by `sup b_0<1`, and the
sum of all other copies is `O(N^(-2))`, uniformly in their center.

Let

$$
X_N=\sum_jb_{0,N}(\theta_j-\alpha),\qquad Z_N=CX_N.
$$

For any positive integer `p`, group the terms in `X_N^p` according to the
partition of repeated eigenvalue labels. Since each factor is in `[0,1]`,
its positive integer powers are no greater than itself. Hence

$$
\mathbb EX_N^p\le
\sum_{j=1}^p\left\{\!\begin{matrix}p\\j\end{matrix}\!\right\}
j!\,M^U_{j,N}(b_0).                                  \tag{7.3}
$$

The braces denote the number of partitions of `p` labeled positions into
`j` nonempty blocks. The first moment on the right is exactly `int b_0`.
For every other fixed `j`, source `H_diag` and the exact CUE bound
`M^CUE_(j,N)(b_0)<= (int b_0)^j/j!` bound that moment uniformly in large `N`.
Thus

$$
\sup_{N\text{ sufficiently large}}\mathbb EZ_N^p<\infty
\quad\text{for each fixed }p.                        \tag{7.4}
$$

### 7.3 Transfer of factorial moments

Use `x_j,y_j,W` as in Section 5, but now use `B_N` for the envelope defining
`Z_N`. The derivative portion of (5.1) and (2.4) give

$$
W\le D Z_N,
\qquad \mathbb EW\le\frac{14\pi\tau}{25N}\|b'\|_1. \tag{7.5}
$$

Telescoping each product in the elementary symmetric polynomial yields

$$
|e_k(x)-e_k(y)|\le\frac{WZ_N^{k-1}}{(k-1)!}.          \tag{7.6}
$$

For a fixed integer `p>k` and `R>=1`, split according to `Z_N<=R`. Equations
(7.4)–(7.5) imply

$$
\mathbb E(WZ_N^{k-1})
\le R^{k-1}\mathbb EW
  +D R^{-(p-k)}\mathbb EZ_N^p
\le C_{b,p}\left(N^{-1}R^{k-1}+R^{-(p-k)}\right).
                                                               \tag{7.7}
$$

Taking `R=N^(1/(p-1))` proves

$$
|M^U_{k,N}(b)-M^c_{k,N}(b)|
=O_{b,p}\left(N^{-(p-k)/(p-1)}\right)\longrightarrow0.
                                                               \tag{7.8}
$$

Each selected `p` is finite, so only finitely many source `H_diag` moments are
used for this individual bound. The shared CUE comparison and (7.8) give
`H_diag` for the cut family. Reversing the phase path and constructing the
same sort of majorant centered at its endpoint proves the converse. This
completes (7.1).

Without source `H_diag`, equations (7.4) and (7.8) have not been asserted. A
small phase displacement in total variation does not by itself control an
arbitrarily high unbounded factorial statistic in spectra with large clusters.
The unconditional second-order transfer in Section 5 uses the separate
quantitative local count bound, which does not supply (7.4).

## 8. What the executed attempt resolved, and what remains

The literal arithmetic proposal was to obtain an infinite subsequence with a
fixed discrepancy by using the exact seven-chain decomposition at multiples
of seven. The operation in (1.2) supplies that same number of exact chains at
all other large odd dimensions with vanishing local-law error. The norm
constants, matching, full pair-statistic transfer, infinite-tail control, and
moment-integrability step above are explicit. This is the substantive outcome
of this attempt.

The dense factor `M_N` remains. For example, at `N=7n` and the coordinate chain
projections `P_s`, all its blocks satisfy

$$
\|P_tU_NP_s\|_{\rm HS}^2
=\|P_tM_NP_s\|_{\rm HS}^2=n^2/N>0.
$$

The first equality follows because the left kick is block unitary; the second
uses the constant modulus `N^(-1/2)` of every entry. Thus the chains are not
seven spectral sectors of `U_N`. This elementary observation is included to
delimit the new theorem and is not counted as progress on `H_diag` itself.

After cutting, the unresolved second-order estimate is still, for each fixed
admissible `b`,

$$
\frac1{N^2}\sum_{m\ge1}|\widehat b(m/N)|^2
\left(|\operatorname{Tr}(U_N^c)^m|^2-\min(m,N)\right)
\longrightarrow0.                                   \tag{8.1}
$$

By (5.4), proving or refuting (8.1) is equivalent to doing so for the original
pair criterion. No nonzero limiting discrepancy is obtained here. At higher
orders, the complete weighted trace products in the question remain
uncontrolled; (7.1) transfers that problem but does not solve it.
