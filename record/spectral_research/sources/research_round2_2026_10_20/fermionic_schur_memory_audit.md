> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/fermionic_schur_memory_audit.md`. Embedded SHA256: `b8486c5c2cd59d6a60aea99dfc6c17152e379976d2fa537c4af90691d376567f`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/dephasing.md).

# Independent audit of the compressed adjoint-memory argument

20 October 2026. This is an independent read and derivation of the
entire file `adversarial_pair_schur_memory.md`, SHA-256
`a9811e26f0aaa15a3f94c61760da7f83446621057b65299c9107d2de1eab2c01`.

**Verdict: PASS.** The mathematical statements and their stated
scope are correct. The note proves an actual obstruction to a
particular operator-norm replacement, not a local-statistics
theorem or an obstruction to the required Hilbert--Schmidt bound.
No correction to the audited file is required.

## 1. Quantitative input and commutant dimension

The input is the all-time bound
`|p_m|<=C exp(a m)+2q_*^m`, where
`a=log(3+2sqrt(2))/2-1000tau^2>0`. The frozen quantitative-pressure
file has SHA-256
`d9efc87ad9c2977b1ae3ca78da26e5f974ce119a22585bcd87e2c76cab5a74b2`.

I checked the finite Gram argument directly. With
`L=floor((log N-2loglog N)/a)`, every off-diagonal row sum of
the Gram matrix of `1,zeta,...,zeta^(L-1)` in `L^2(mu_N)` is at
most

$$
 \frac2N\sum_{m=1}^{L-1}|p_m|=O((\log N)^{-2}).
$$

The geometrically decaying residual contributes only O(1/N).
If an atom has mass n_j/N, its normalized indicator has squared
inner product n_j/N with each vector. The Gram/Bessel inequality
therefore gives `L n_j/N<=1+epsilon_N`. Consequently

$$
 d_N=\sum_j n_j^2\le N\max_j n_j
 \le(a+o(1))N^2/\log N.
$$

This reasoning does not assume simple spectrum, a choice inside
a degenerate eigenspace, or a lower eigenphase spacing.

## 2. Removing every stationary matrix

The exact adjoint operator is unitary on the N^2-dimensional matrix
space. Thus the orthogonal complement of its fixed subspace E is
invariant and unitary. Projection of the N-dimensional space of
coordinate diagonal matrices onto E-perp has dimension at most
N-1, because its kernel contains the identity matrix. This proves
the claimed rank bound after the full commutant has been removed.

Let V denote that restricted unitary, P the indicated projection,
Q=I-P, and D=QVQ on Ran Q. For

$$
 K_t=\bigcap_{j=0}^t\ker(PV^j),
$$

rank subadditivity gives

$$
 \dim K_t\ge N^2-d_N-(t+1)(N-1).
$$

The condition j=0 puts K_t inside Ran Q. Induction gives
`D^j x=V^j x` for every x in K_t and every j<=t, since the next
condition makes each intervening projection Q act identically.
Hence `||D^t x||=||x||`. As D^t is a contraction, positivity of
`I-(D^t)^*D^t` implies that it annihilates K_t. This verifies not
only norm one but the asserted lower multiplicity of singular
value one and the Hilbert--Schmidt lower bound.

At `t<=floor(N-cN/log N)`, the dimension lower bound is
`(c-a+o(1))N^2/log N`, strictly positive for every fixed c>a.
The endpoint and the integer rounding are correct. If in a
particular dimension d_N=N, then t=N-2 still leaves dimension
at least N-1, also as claimed.

## 3. Exact Schur positivity

For the unitary block matrix `V=[[A,B],[C,D]]`, put
`R=(I-zD)^(-1)` and `F=A+zBRC`, for |z|<1. Block elimination
in `I-zV` gives the stated compressed resolvent
`(I-zF)^(-1)` with its exact power of z.

I independently checked the defect identity by applying V to
`(x,zRCx)`. Since `I+zDR=R`, its image is `(Fx,RCx)`.
Equality of input and output squared norms gives precisely

$$
 I-F^*F=(1-|z|^2)C^*R^*RC.
$$

Thus F is contractive, but the claimed strict decay for D^t is
incompatible with the isometric subspaces just proved. This is
a finite-dimensional obstruction for the actual U_N and remains
valid after all invariant matrices are removed. It does not
assert that D itself has spectral radius one or rule out decay
after the displayed finite time range.

## 4. Pair observable and scope

The adjoint eigenvalues are the ratios of the original eigenvalues,
so its mth trace is |p_m|^2. Absolute convergence of the geometric
resolvent expansions verifies

$$
 \|(I-r\mathcal C_N)^{-1}\|_{\rm HS}^2
 =\frac{N^2+2\sum_{m\ge1}r^m|p_m|^2}{1-r^2},
 \qquad 0<r<1.
$$

At r=exp(-2s/N), the requested bounded Abel statistic is equivalent
to an O_s(N^3) bound for this norm squared. Orthogonal decomposition
into E and E-perp gives exactly the fixed contribution
`d_N/(1-r)^2`; hence d_N=O(N) would be necessary. Removing this
contribution does not establish the required bound for the other
part. The file identifies that remaining quantity explicitly and
does not use it as an unproved hypothesis.

The isometric-subspace dimension lower bound has no contradiction
with a Hilbert--Schmidt resolvent of size O(N^3). It rules out the
stronger operator-norm decay proposed by this particular Schur
route. All scope qualifications in the audited note are appropriate.
