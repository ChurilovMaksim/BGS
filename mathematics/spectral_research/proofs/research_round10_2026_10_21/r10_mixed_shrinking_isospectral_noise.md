> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round10_2026_10_21/r10_mixed_shrinking_isospectral_noise.md`. Embedded SHA256: `5c9265843ce9ad7037ca35b0b601bfed4cca9bd87a44d15405a30f68d22683fb`.
> [Thematic guide](../../topics/closure.md).

# Shrinking isospectral Weyl noise: exact diffusion and exact loss of the long-time statistic

21 October 2026. Branch `/root/r10_mixed`.

## 0. Result and scope

This note constructs a fully explicit **auxiliary** ensemble around the
bare matrix `M_N` from the question. Every sample has exactly the same
spectrum as `M_N`. The noise tends to zero on the classical scale and
on every fixed Weyl observable. Nevertheless its averaged one-step
adjoint has spectral radius tending to zero on trace-zero matrices,
and its operator traces are `1+o(1)` uniformly at every positive time.

The powers of a single sample instead retain exact cat-map scalar
returns. On an explicit sequence of odd dimensions, a fixed admissible
pair statistic diverges and the local point measure converges in
probability to the empty measure. Replacing the actual repeated-sample
average by powers of the averaged adjoint therefore changes the
microscopic statistic even under this vanishing noise.

This is stronger in its smooth-observable scope than full Haar
conjugacy averaging, but it does **not** replace the prescribed
`U_N=e^{i10^{-80}NA_N}M_N`. It is not an original-family counterexample
and not a refutation of any theorem about a different, specifically
Hamiltonian ensemble. Its purpose is to test whether a shrinking
diffusion and its spectral gap by themselves justify the missing
mixed-determinant step. No priority claim is made.

## 1. Exact covariance for the specified `M_N`

Use the exact modular Weyl operators from the question, and write
`v=(a,b)`, `k=(c,d)` and

$$
 \sigma(v,k)=ad-bc.
$$

Direct multiplication of the two shift-and-phase operators gives

$$
 T_N(v)T_N(k)=e_N(2^{-1}\sigma(v,k))T_N(v+k),
 \qquad
 T_N(v)T_N(k)T_N(v)^*=e_N(\sigma(v,k))T_N(k).
 \tag{1.1}
$$

In particular the `N^2` matrices `N^{-1/2}T_N(k)` are an
orthonormal basis for Hilbert--Schmidt matrix space. The trace of
`T_N(k)` vanishes unless `k=0`: a nonzero shift has zero diagonal,
and a nonconstant diagonal character sums to zero. The same facts
applied to `T_N(k)^*T_N(l)` prove orthogonality.

For the exact matrix `M_N` in the question, set

$$
 S=\begin{pmatrix}3&4\\2&3\end{pmatrix}.
$$

Then for every odd `N`, including composite sizes,

$$
 \boxed{M_NT_N(k)M_N^*=T_N(Sk).}
 \tag{1.2}
$$

Here is the kernel verification, which also fixes the signs.
Let

$$
 Q(x,z)=-8^{-1}(3x^2-2xz+3z^2).
$$

The kernel of `M_NT_N(a,b)`, after changing the summation variable
from `y` to `z=y+a`, has exponent

$$
 Q(x,z)-4^{-1}ax+(3\cdot4^{-1}a+b)z
       -3\cdot8^{-1}a^2-2^{-1}ab.
$$

The kernel of `T_N(c,d)M_N` has exponent

$$
 Q(x,z)+(d-3\cdot4^{-1}c)x+4^{-1}cz
       -3\cdot8^{-1}c^2+2^{-1}cd.
$$

They are equal upon substituting `c=3a+4b`, `d=2a+3b`, including
their constant terms. All inverses in this computation are modular
ones, so the argument works for every odd `N`. Unitarity then gives
(1.2).

One further modular fact will be decisive:

$$
 \det(S-I)=-4.
 \tag{1.3}
$$

Thus `S-I` is invertible modulo every odd `N`.

## 2. A concrete shrinking probability distribution

Fix any number `0 < alpha < 2`. Define

$$
 \epsilon_N=N^{-\alpha},\qquad s_N=\epsilon_N N^2=N^{2-\alpha}.
$$

For each coordinate `i=1,2`, let `P_i^+`, `P_i^-` be independent
Poisson random variables of mean `s_N/2`, and reduce

$$
 v_i=P_i^+-P_i^-\pmod N.
$$

Let `nu_N` be the resulting probability measure on `(Z/NZ)^2`.
The elementary Poisson generating function gives its exact Fourier
transform:

$$
 \sum_v\nu_N(v)e_N(v\cdot q)
  =\exp[-s_N\ell_N(q)],\qquad
 \ell_N(q)=2-\cos(2\pi q_1/N)-\cos(2\pi q_2/N).
 \tag{2.1}
$$

Define the isospectral ensemble

$$
 Y_{N,v}=T_N(v)M_NT_N(v)^*.
 \tag{2.2}
$$

Each sample in (2.2) is exactly unitarily conjugate to `M_N`.
In particular it has the same full determinant ratios, all
factorial statistics, and all local Laplace observables.

The noise shrinks on the torus. Before reduction, each coordinate
has variance `s_N`; centered reduction can only decrease its
distance to zero. If `dist_T` denotes Euclidean torus distance,

$$
 \mathbb E\operatorname{dist}_{\mathbb T^2}(v/N,0)^2
 \le 2s_N/N^2=2\epsilon_N\longrightarrow0.
 \tag{2.3}
$$

Thus the translations converge to zero in probability. The
following fixed-observable calculation is a more directly quantum
version of the same statement.

## 3. The averaged adjoint and its fixed-frequency limit

Let

$$
 \mathcal A_N=\mathbb E_{v\sim\nu_N}\operatorname{Ad}(Y_{N,v}).
$$

Combining (1.1)--(1.2) gives

$$
 \operatorname{Ad}(Y_{N,v})T_N(k)
 =e_N\bigl(\sigma(v,(S-I)k)\bigr)T_N(Sk).
$$

The function `ell_N` is invariant under interchanging the
coordinates and changing their signs. Consequently (2.1) yields
the exact weighted-permutation formula

$$
 \boxed{
 \mathcal A_NT_N(k)=d_N(k)T_N(Sk),\qquad
 d_N(k)=\exp[-s_N\ell_N((S-I)k)].}
 \tag{3.1}
$$

The scalar subspace is fixed, and the trace-zero subspace is
invariant. All weights lie in `(0,1]`.

For any fixed integer label `k`, put `q=(S-I)k` before modular
reduction. Since `1-cos t <= t^2/2`,

$$
 0\le1-d_N(k)
 \le s_N\ell_N(q)
 \le2\pi^2\epsilon_N|q|^2\longrightarrow0.
 \tag{3.2}
$$

Thus the averaged operator retains the exact cat correspondence
on every fixed Fourier label. Moreover, writing
`||X||_{2,N}^2=N^{-1}Tr(X^*X)`, the actual sample fluctuation obeys

$$
 \begin{aligned}
 &\mathbb E\left\|
 \operatorname{Ad}(Y_{N,v})T_N(k)
       -\operatorname{Ad}(M_N)T_N(k)\right\|_{2,N}^2\\
 &\hspace{15mm}=2(1-d_N(k))
 \le4\pi^2\epsilon_N|(S-I)k|^2\longrightarrow0.
 \end{aligned}
 \tag{3.3}
$$

Any fixed trigonometric polynomial is a finite sum of these modes,
so the same convergence holds for it by the triangle inequality in
`L^2(nu_N;HS)`. This is an exact fixed-smooth-observable
correspondence, not a claim inferred only from a classical picture.

## 4. A uniform trace estimate at every time

Fix

$$
 \rho=\frac1{16},\qquad
 c_0=1-\cos(2\pi\rho)=1-\cos(\pi/8)>0.
$$

Represent each residue coordinate by its unique centered integer
between `-(N-1)/2` and `(N-1)/2`. A centered vector is called
small in this proof if its coordinate maximum is at most `rho N`.

### Lemma 4.1: every nonzero periodic orbit has a nonsmall vector

Suppose `q != 0` modulo `N` and `S^m q=q` modulo `N`, with
`m >= 1`. Then some centered vector among
`q,Sq,...,S^(m-1)q` has a coordinate of absolute value greater
than `rho N`.

**Proof.** If all vectors were small, multiplication by `S` would
keep each coordinate of the unreduced next vector below
`7rho N<N/2`, since the largest row absolute sum of `S` is
seven. Therefore there could be no modular wraparound in any of
these transitions, including the last. The centered initial vector
would satisfy `S^m q=q` over the integers. The two real eigenvalues
of `S` are

$$
 \lambda=3+2\sqrt2>1,\qquad\lambda^{-1}=3-2\sqrt2,
$$

so `S^m-I` is invertible over the reals. This forces `q=0`, a
contradiction. $\square$

On any nonsmall centered vector, monotonicity of `1-cos t` for
`0 <= t <= pi` gives `ell_N(q) >= c_0`. Now expand the operator
trace of (3.1) in the orthonormal Weyl basis. Only labels with
`S^m k=k` contribute. The zero label contributes one. For any
nonzero contributing label, `q=(S-I)k` is nonzero by (1.3), is
also periodic, and satisfies `S^j q=(S-I)S^j k`. Lemma 4.1 gives
at least one factor in its weight product bounded by `exp(-c_0s_N)`.
All the other factors are at most one. Hence

$$
 \boxed{
 0\le\operatorname{Tr}_{\rm HS}(\mathcal A_N^m)-1
 \le(N^2-1)e^{-c_0s_N}
 \quad\text{for every integer }m\ge1.}
 \tag{4.1}
$$

This estimate is uniform over unbounded times. No semiclassical
expansion or fixed-time restriction occurs in its proof.

## 5. Spectral radius and the qualification about singular values

There is also a quantitative bound on powers in operator norm.
Put

$$
 J_N=\left\lceil\frac{\log(4N)}{\log\lambda}\right\rceil,
 \qquad L_N=2J_N+1.
$$

Every block of `L_N` consecutive vectors in a nonzero orbit of
`S` modulo `N` contains a nonsmall vector. To prove this, suppose
all centered vectors `v_0,...,v_(2J_N)` in a block were small.
As in Lemma 4.1, they would obey `v_j=S^j v_0` exactly over the
integers. Write a real vector as

$$
 (a,b)=u(\sqrt2,1)+s(\sqrt2,-1),\qquad
 u=\frac{a}{2\sqrt2}+\frac b2,\quad
 s=\frac{a}{2\sqrt2}-\frac b2.
$$

For a small vector, both `|u|` and `|s|` are at most `rho N`.
At the middle of the block the unstable coordinate is bounded by
`rho N lambda^(-J_N)` using the final endpoint, and the stable
coordinate has the same bound using the initial endpoint. Thus

$$
 \|v_{J_N}\|_\infty
 \le 2\sqrt2\rho N\lambda^{-J_N}
 \le\rho/\sqrt2<1.
$$

An integer vector with coordinate maximum less than one is zero.
This contradicts invertibility of `S` modulo `N` and the nonzero
initial label.

Applying this block fact to `q=(S-I)k` in (3.1), with `k != 0`,
proves

$$
 \left\|\mathcal A_N^{L_N}|_{\operatorname{Tr}=0}\right\|
 \le e^{-c_0s_N},\qquad
 r\left(\mathcal A_N|_{\operatorname{Tr}=0}\right)
 \le e^{-c_0s_N/L_N}\longrightarrow0.
 \tag{5.1}
$$

The norm here is the Hilbert--Schmidt operator norm; a weighted
permutation has norm equal to its largest weight, which justifies
the first inequality. The radius limit uses `alpha<2` and
`L_N=O(log N)`.

This is a spectral-radius statement, **not** a uniform lower bound
for the singular values of `I-A_N`. The latter would require a
separate proof for this nonnormal operator. The estimate actually
obtained from the displayed blocks is

$$
 \left\|(I-\mathcal A_N)^{-1}|_{\operatorname{Tr}=0}\right\|
 \le \sum_{m\ge0}e^{-c_0s_N\lfloor m/L_N\rfloor}
 =\frac{L_N}{1-e^{-c_0s_N}}=O(\log N).
 \tag{5.2}
$$

Keeping this qualification is essential. The separate Haar
conjugacy example in the companion note gives an exact one-step
orthogonal projection, but does not have the fixed-smooth-observable
correspondence (3.3). No claim that these two different examples
satisfy all of each other's conditions is being made.

## 6. The resampled microscopic statistic vanishes

For any fixed bounded `w` supported in `[0,B]`, define the
operator statistic produced by independent resampling at every
step as

$$
 F_N^{\rm resampled}(w)=\frac1{N^2}\sum_{m\ge1}
          w(m/N)\operatorname{Tr}_{\rm HS}(\mathcal A_N^m).
$$

Equation (4.1) gives, directly for the complete weighted sum,

$$
 \boxed{
 |F_N^{\rm resampled}(w)|
 \le B\|w\|_\infty
       \left(\frac1N+Ne^{-c_0N^{2-\alpha}}\right)
 \longrightarrow0.}
 \tag{6.1}
$$

The endpoint rounding only reduces the displayed bound. In
contrast, the CUE form factor for a nonzero nonnegative continuous
`w` has the strictly positive limit

$$
 \frac1{N^2}\sum_{m\ge1}w(m/N)\min(m,N)
 \longrightarrow\int_0^B w(u)\min(u,1)\,du.
 \tag{6.2}
$$

The Haar identity behind (6.2) is proved in the companion twirl
note. The limit itself is just a Riemann sum.

## 7. The actual ensemble has exact scalar returns on explicit odd dimensions

Define integers `a_r,n_r` by

$$
 S^r=\begin{pmatrix}a_r&4n_r\\2n_r&a_r\end{pmatrix},\qquad
 n_r=\frac{\lambda^r-\lambda^{-r}}{4\sqrt2}.
$$

The integral recurrence

$$
 n_0=0,\quad n_1=1,\quad n_{r+1}=6n_r-n_{r-1}
$$

verifies integrality directly. It also shows that `n_r` is odd
when `r` is odd. Taking determinants gives

$$
 a_r^2-8n_r^2=1.
$$

Choose odd `r >= 3` and dimension `N_r=n_r`. Then

$$
 S^r\equiv a_r I\pmod{N_r},\qquad
 S^{2r}\equiv I\pmod{N_r}.
$$

By exact covariance (1.2), `M_(N_r)^(2r)` commutes with every
Weyl operator. A matrix commuting with `T(0,1)` is diagonal,
because that diagonal unitary has distinct eigenvalues. Commuting
also with the cyclic shift `T(1,0)` makes all diagonal entries
equal. Therefore

$$
 \boxed{M_{N_r}^{2r}=\gamma_r I,\qquad |\gamma_r|=1.}
 \tag{7.1}
$$

No knowledge of the scalar phase is needed. Every conjugate
`Y_(N_r,v)` has the same return, and hence for each positive
multiple `m` of `2r`,

$$
 |\operatorname{Tr}Y_{N_r,v}^{m}|^2=N_r^2.
 \tag{7.2}
$$

This is the same sample raised to a power. In fact, for every `m`,

$$
 \mathbb E_v\operatorname{Ad}(Y_{N,v})^mT_N(k)
 =\exp[-s_N\ell_N((S^m-I)k)]T_N(S^mk),
 \tag{7.3a}
$$

by applying the calculation of Section 3 to `M_N^m`. The
independently resampled expression is instead

$$
 \mathcal A_N^mT_N(k)
 =\exp\!\left[-s_N\sum_{j=0}^{m-1}
        \ell_N((S-I)S^jk)\right]T_N(S^mk).
 \tag{7.3b}
$$

The label in (7.3a) is the telescoping sum
`(S^m-I)k=sum_j (S-I)S^jk`. On a periodic label it vanishes
exactly, so the same-sample average has weight one. Equation
(7.3b) sums separate nonnegative penalties and suppresses that
same periodic label by at least `exp(-c_0s_N)`. Thus the lost
coherence is visible before taking the operator trace. In
particular exact covariance proves the finite identity

$$
 |\operatorname{Tr}M_N^m|^2
 =\#\ker(S^m-I:(\mathbb Z/N\mathbb Z)^2\to
                  (\mathbb Z/N\mathbb Z)^2).
 \tag{7.3c}
$$

Equivalently,

$$
 \boxed{
 \operatorname{Tr}_{\rm HS}
      \bigl(\mathbb E_v\operatorname{Ad}(Y_{N,v})^m\bigr)
 =|\operatorname{Tr}M_N^m|^2,}
 \tag{7.3}
$$

because the trace is invariant under conjugacy. Equations
(4.1) and (7.3) are the two different operations at issue.

### A fixed admissible pair test

Use the single test from Section 4 of the companion note:

$$
 \phi_0(\xi)=e^{-1/(1-16\xi^2)}\mathbf1_{|\xi|<1/4},\qquad
 b_0=|\mathcal F^{-1}\phi_0|^2/[2(\int\phi_0)^2],\qquad
 w_0=|\widehat b_0|^2.
$$

Its verified properties are `0 <= b_0 <= 1/2`, Schwartz decay,
and `bhat_0` smooth with support `[-1/2,1/2]`, positive on its
interior. In particular

$$
 c_1:=\min_{0\le u\le1/4}w_0(u)>0.
$$

The positive terms from (7.2) give

$$
 \begin{aligned}
 F_{N_r}^{\rm actual}(w_0)
 &:=\frac1{N_r^2}\sum_{m\ge1}
                 w_0(m/N_r)|\operatorname{Tr}M_{N_r}^m|^2\\
 &\ge c_1\left\lfloor\frac{N_r}{8r}\right\rfloor
 \longrightarrow+\infty.
 \end{aligned}
 \tag{7.4}
$$

The last limit follows from the explicit exponential formula for
`N_r`. The CUE comparison is bounded by (6.2). Consequently the
exact pair identity proves

$$
 \Delta_{2,N_r}^{M}(b_0)\longrightarrow+\infty.
 \tag{7.5}
$$

Every sample in (2.2) has this same statistic. Thus the failure of
replacement in (6.1) is quantitative and involves an actual fixed
admissible microscopic test, not only an operator spectrum.

### A bounded local observable also changes

Equation (7.1) implies that the spectrum has at most `2r` distinct
angles at dimension `N_r`. For any fixed compact interval `I`,
and sufficiently large `N_r`, the event that the local point
measure places any point in `I` is contained in a union of at most
`2r` origin intervals, each of length `|I|/N_r`. Therefore

$$
 \mathbb P_{\rm origin}\{\Xi_{N_r}(I)>0\}
 \le\frac{2r|I|}{N_r}\longrightarrow0.
 \tag{7.6}
$$

The point processes converge vaguely in probability to the empty
measure along this subsequence. In particular every compactly
supported nonnegative Laplace test has limit one. This does not
contradict intensity one at finite `N`: mass is carried by rare
clusters, and the counts are not uniformly integrable.

## 8. Consequence for the attempted noise-removal route

This construction has all of the following properties simultaneously:

1. the ensemble is exactly isospectral for every odd dimension;
2. its perturbation tends to zero on the torus and on every fixed
   polynomial Weyl observable;
3. the averaged adjoint is an exact quantized discrete diffusion
   followed by a hyperbolic Weyl permutation;
4. its trace-zero spectral radius tends to zero;
5. its averaged-operator traces satisfy (4.1) uniformly at every
   time, and its resampled weighted statistic tends to zero;
6. its actual pair statistic diverges on a specified odd subsequence.

The distinction between the sample power in (7.3) and the averaged
power in (4.1) cannot be removed by invoking only properties 1--4.
Even verifying the very strong operator trace estimate (4.1) for a
regularized one-step operator is insufficient without a comparison
to the original same-sample mixed source.

The first missing assertion for the original fixed-kick family
remains the Round 10 checkpoint estimate

$$
 N^{-2}\sum_{1\le m<2N}|\widehat b_*(m/N)|^2
 \bigl(|\operatorname{Tr}U_N^m|^2-\min(m,N)\bigr)\to0.
$$

No estimate for it is proved here. The present family uses `M_N`
and explicit auxiliary conjugations, and therefore meets neither
the main nor the alternative original-family success criterion.

## 9. Relation to the checked supersymmetry source

The primary text checked was M. R. Zirnbauer, *Pair Correlations of
Quantum Chaotic Maps from Supersymmetry*,
[arXiv:chao-dyn/9812023v1](https://arxiv.org/pdf/chao-dyn/9812023).
Sections 3 and 8 use independent Gaussian coefficients of variance
`2 epsilon(h)` in a left multiplier
`exp(i sum xi_k Q_N(x_k)/h)`, with a finite family of smooth
Hamiltonians and an ellipticity requirement. The proposed scaling
is `epsilon(h)=h^alpha`, `0<alpha<1`. Section 8 explicitly notes
the need to treat powers of the adjoint after the Hessian. The
conclusion on pages 26--27 lists further work required for a
mathematically rigorous proof of the ensemble assertion.

Our Weyl translations are a different ensemble: discrete torus
translations are not being presented as that finite family of
global smooth Hamiltonian flows. Thus this note does not refute a
rigorous theorem from that source, or assert that its full mixed
average equals the independently resampled dynamics. It supplies
an exact test of an otherwise tempting replacement.

The fixed continuous-symbol stability proved in Round 9 concerns
generators `exp(iQ_N(v)/N)`, with a fixed bounded limiting symbol.
Writing `h=(2pi N)^(-1)`, the coefficient of `Q_N(v)` is of
order `h`. Expressed as `exp(i xi Q_N(v)/h)`, its coefficient is
therefore `xi=O(h^2)`, or variance scale `O(h^4)`. This arithmetic
scale comparison does not supply a stability theorem at the
Gaussian scale `h^(alpha/2)` above. The source supplies no direct
original-family estimate to fill that gap.

## 10. Provenance

The exact matrix and Weyl definitions in the question are the only
inputs for Sections 1--8, apart from the explicitly reproved finite
pair/CUE identity in the companion note. No earlier semiclassical
trace bound or classical pressure assertion is assumed. The source
in Section 9 was read in its raw original PDF, especially printed
pages 5--6, 19--27, on 21 October 2026.

The working target was checked against
`research_round10_2026_10_21/round10_target_checkpoint.md`, SHA-256
`a35e09d5678b1f718f7deaa1c726afa5c692886010eb41f748e8f9f1624378f0`.
The frozen master remains SHA-256
`e338400f1f360b680ea74c739283b296c9c67eb4e598c2067b136f9f29773777`.
Only a new file in the assigned `r10_mixed_*` write scope was created.
