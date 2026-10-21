> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/fermionic_resolvent_frame.md`. Embedded SHA256: `61409d8899fe3966a752830e7c1f32069337a9b7ecd3cd4c2d6c8c05258bc9b0`.
> [Thematic guide](../../topics/dephasing.md).


# Positive resolvent and finite Krylov frame bounds

Research continuation, 20 October 2026. This note proves an exact positive
identity and a bound for the full, infinite exponentially weighted trace
sum of the actual family. The proved bound is of order `N^3/log N` for
the unnormalized sum, rather than the required `N^2`. Its limitation is
made quantitative. No contour is moved across the unit circle, and no
inverse determinant is bounded by an orbit-diagonal approximation.

## 1. Frozen inputs and scope

The actual matrices are the fixed-parameter matrices in the question,
with `tau=10^-80` and all sufficiently large odd `N`. Write

$$
p_m=\operatorname{Tr}U_N^m,\qquad p_0=N,\qquad c_m=p_m/N,
\qquad c_{-m}=\overline{c_m}.
$$

The direct actual-family input used below is

$$
|p_m|\le C a^m\quad(m\ge1),\qquad
a=\sqrt{3+2\sqrt2}\,(1.0002)>1,\quad C=3.
\tag{1.1}
$$

It follows from the all-time trace and amplitude estimates in the
previous package. Its explicit verification and the corresponding
unitarity minimum are recorded in
`fermionic_pseudoorbit_cutoff.md`, SHA-256
`03173e53d1a10e2c1afad517c48943a5330d43fc4059b80fc0e37d5b1598a9eb`.
The Gaussian modulus source is
`../research_continuation_2026_10_20/gaussian_cocycle_and_modulus.md`,
SHA-256
`c1a863e613a327acb5fe43ff1093c4a8fe51b37ebd5dcee9fddf0ae0a91986f1`.

The counterexample comparison in Section 6 uses only the already proved
model in Part II of `fermionic_root_trace_audit.md`, SHA-256
`449aa3d72f26a6b3b195395f5ef714ecebcd3a42071718b569f8d7658c0712eb`.
That model is not the matrix family of the question. In particular it
is not asserted to satisfy the newer all-fixed-iterate sector theorem
for the original family.

Every identity in Sections 2--4 is proved below for an arbitrary finite
unitary matrix, including matrices with repeated eigenvalues.

## 2. A contractive rational function inside the unit disk

Let `zeta_j`, `1<=j<=N`, be the eigenvalues, with multiplicity, and set

$$
D(z)=\prod_{j=1}^N(1-z\zeta_j),\qquad
F(z)=\frac1N\sum_{j=1}^N\frac{1+z\zeta_j}{1-z\zeta_j}.
\tag{2.1}
$$

For `|z|<1`, every denominator is nonzero. Direct multiplication by its
conjugate gives

$$
\operatorname{Re}F(z)
=\frac{1-|z|^2}{N}\sum_{j=1}^N\frac1{|1-z\zeta_j|^2}>0.
\tag{2.2}
$$

The absolutely convergent geometric series gives

$$
F(z)=1+2\sum_{m\ge1}c_mz^m
=1-\frac{2zD'(z)}{ND(z)}.
\tag{2.3}
$$

Consequently `F+1` has positive real part, and

$$
w(z):=\frac{F(z)-1}{F(z)+1}
=\frac{-zD'(z)}{ND(z)-zD'(z)}
\tag{2.4}
$$

is holomorphic with `|w(z)|<1` and `w(0)=0`. The inequality follows
directly from `|F+1|^2-|F-1|^2=4 Re F>0`; no theorem about Schur
functions or orthogonal polynomials is needed.

For `0<r<1`, define

$$
S_N(r):=\sum_{m\ge1}r^{2m}|c_m|^2.
\tag{2.5}
$$

All the series here converge absolutely because `|c_m|<=1`. Angular
Parseval and (2.3)--(2.4) prove the exact identity

$$
\boxed{S_N(r)=\frac14\int_0^{2\pi}|F(re^{it})-1|^2\frac{dt}{2\pi}
=\int_0^{2\pi}\frac{|w(re^{it})|^2}{|1-w(re^{it})|^2}\frac{dt}{2\pi}.}
\tag{2.6}
$$

Since `F(0)=1`, its absolutely convergent Fourier series also yields

$$
\boxed{\int_0^{2\pi}
\frac{1-|w(re^{it})|^2}{|1-w(re^{it})|^2}\frac{dt}{2\pi}=1.}
\tag{2.7}
$$

Thus the positive probability measure

$$
d\nu_{N,r}(t)=\operatorname{Re}F(re^{it})\frac{dt}{2\pi}
$$

satisfies

$$
S_N(r)=\int\frac{|w|^2}{1-|w|^2}\,d\nu_{N,r}.
\tag{2.8}
$$

Equations (2.6)--(2.8) locate the issue precisely: contractivity by itself
does not bound its harmonic-measure-weighted approach to the unit circle.
For example a bound `sup_(|z|=r)|w(z)|<=rho<1` would imply
`S_N(r)<=rho^2/(1-rho^2)`, but no such uniform bound is assumed or claimed.

### 2.1 Cofactor positivity and the exact numerator

Let `D_j(z)=D(z)/(1-z zeta_j)`, with repeated factors still indexed
separately. Put `A(z)=ND(z)-zD'(z)` and `B(z)=-zD'(z)`. Then

$$
\boxed{|A(z)|^2-|B(z)|^2
=N(1-|z|^2)\sum_{j=1}^N|D_j(z)|^2.}
\tag{2.9}
$$

Indeed (2.2)--(2.3) imply

`N^2 |D|^2 Re F = N(1-|z|^2) sum_j |D_j|^2`,

while the left side equals
`N^2|D|^2-2N Re(zD' conjugate(D))=|A|^2-|B|^2`.
The apparently favorable numerator in (2.9) is therefore the complete
sum of squared cofactors. Dropping mixed primitive-orbit terms in either
`D'` or those cofactors would be an extra estimate, not positivity.

## 3. A finite frame removes the determinant denominator completely

Define the positive Toeplitz Gram matrix

$$
G_L=(c_{k-j})_{0\le j,k<L},\qquad L\ge1.
\tag{3.1}
$$

Here positivity follows from

$$
\sum_{j,k}\overline{v_j}v_kc_{k-j}
=\frac1N\sum_{\ell=1}^N
\left|\sum_{k=0}^{L-1}v_k\zeta_\ell^k\right|^2.
\tag{3.2}
$$

### Theorem 3.1: exact positive frame inequality

For every `N,L` and `0<r<1`,

$$
\boxed{
(1-r^{2L})(1+S_N(r))
+\sum_{n=1}^{L-1}(1-r^{2(L-n)})|c_n|^2
\le\lambda_{\max}(G_L).
}
\tag{3.3}
$$

**Proof.** Use the finite probability space with measure
`mu=N^-1 sum_j delta_(zeta_j)` on the unit circle. Its Hilbert space is
`H=L^2(mu)`. Let `v_j(zeta)=zeta^j`, and let
`T:C^L -> H` send the j-th coordinate vector to `v_j`. Then
`T^*T=G_L`. The elementary singular-value bound for a finite matrix
implies

$$
\sum_{j=0}^{L-1}|\langle v_j,f\rangle_H|^2
\le\lambda_{\max}(G_L)\|f\|_H^2
\quad(f\in H).
\tag{3.4}
$$

This also follows directly by diagonalizing the positive matrix
`TT^*`; its positive eigenvalues are those of `T^*T`, since the maps
`T` and `T^*` give inverse correspondences up to the nonzero eigenvalue.

Take `f_z(zeta)=(1-z zeta)^-1`, `z=r exp(it)`, and integrate (3.4) in t.
The geometric series and its absolute convergence imply

$$
\int|\langle v_j,f_{re^{it}}\rangle_H|^2\frac{dt}{2\pi}
=\sum_{m\ge0}r^{2m}|c_{m-j}|^2,
\qquad
\int\|f_{re^{it}}\|_H^2\frac{dt}{2\pi}
=\frac1{1-r^2}.
\tag{3.5}
$$

In the first sum separate `m>=j` from `0<=m<j`. The first part summed
over j is

$$
\frac{1-r^{2L}}{1-r^2}(1+S_N(r)).
$$

For the second part set `n=j-m`; using `|c_(-n)|=|c_n|`, its total is

$$
\sum_{n=1}^{L-1}|c_n|^2
\sum_{j=n}^{L-1}r^{2(j-n)}
=\frac1{1-r^2}
\sum_{n=1}^{L-1}(1-r^{2(L-n)})|c_n|^2.
$$

Multiplying the integrated inequality (3.4) by `1-r^2` proves (3.3).
This proof is finite dimensional apart from absolutely convergent
geometric series. In particular it accounts for every `m>=1` in (2.5),
including the entire infinite tail. QED.

## 4. What the actual all-time trace bound proves

For a Hermitian Toeplitz matrix in (3.1), the sum of absolute values in
each row of `G_L-I` is at most

$$
\epsilon_{N,L}:=\frac2N\sum_{m=1}^{L-1}|p_m|.
$$

The operator norm is at most this maximum row sum. One proof is to bound
`|v^*(G_L-I)v|` using `2|v_j v_k|<=|v_j|^2+|v_k|^2`; the row and column
sums coincide because the matrix is Hermitian. Hence (1.1) gives

$$
\lambda_{\max}(G_L)\le1+\epsilon_{N,L},\qquad
\epsilon_{N,L}\le\frac{2C a^L}{N(a-1)}.
\tag{4.1}
$$

For large N choose

$$
L_N=\left\lfloor\frac{\log N-2\log\log N}{\log a}\right\rfloor.
\tag{4.2}
$$

Then `L_N>=1`, `epsilon_(N,L_N)=O((log N)^-2)`, and
`L_N/log N -> 1/log a`. Dropping only the explicit nonnegative finite
sum in (3.3), and setting `r_N=exp(-s/N)`, gives for every fixed `s>0`

$$
\boxed{
\frac1{N^2}\sum_{m\ge1}e^{-2sm/N}|p_m|^2
\le\frac{1+O((\log N)^{-2})}{1-e^{-2sL_N/N}}-1.
}
\tag{4.3}
$$

In particular, for the actual family and all sufficiently large odd N,

$$
\boxed{
\limsup_{N\to\infty\atop N\ {\rm odd}}
\frac{\log N}{N}
\left[\frac1{N^2}\sum_{m\ge1}e^{-2sm/N}|p_m|^2\right]
\le\frac{\log a}{2s}.
}
\tag{4.4}
$$

Equivalently the unnormalized sum is `O_s(N^3/log N)`. This is a
logarithmic improvement on the direct unitarity bound `O_s(N^3)`.
It is not the desired `O_s(N^2)` bound, and it is not the claimed CUE
asymptotic.

The same proof works with any fixed constants `C>0`, `a>1` for which
`|p_m|<=C a^m` holds for all m at one N threshold. Thus a genuinely
smaller actual growth exponent improves the constant in (4.4), but
does not by itself replace its `N/log N` scale by a bounded one.

## 5. Where the coefficient cancellation fails to enter

For the actual dynamical determinant write

$$
\mathcal Z_N(z)=D_N(z)e^{G_N^{\rm err}(z)}
=\sum_{n\ge0}q_{n,N}z^n.
$$

The superscript avoids confusing the scalar analytic error with the
matrix `G_L`. The frozen pseudo-orbit theorem proves, for example,
`|q_(N+u,N)|<=exp(-c u)` when `u>=N^(1/50)`. It also proves that its
positive complete primitive-subset diagonal tends to `C_F(Psi)>0`,
and consequently the full different-subset sum tends to `-C_F(Psi)`
beyond that cutoff.

These facts bound the coefficients of a holomorphic function. The
resolvent identities (2.6) and (2.9) concern its logarithmic derivative,
with the complete inverse and cofactor expressions. The frame identity
(3.3) avoids all divisions, but its Gram entries are the power traces
themselves. It does not identify them with the diagonal pseudo-orbit
coefficients.

For comparison, the next Gram quadratic statistic has the exact form

$$
\operatorname{Tr}G_L^2
=L+2\sum_{m=1}^{L-1}(L-m)\frac{|p_m|^2}{N^2}.
\tag{5.1}
$$

This follows by counting the `L-m` entries on each of the two m-th
off-diagonals. At `L` proportional to N, estimating (5.1) is already
a positive weighted power-trace problem. No bound on its right side
at the desired scale follows from the known coefficient cutoff.
Using such a bound inside the frame argument without an independent
proof would put the unresolved pair estimate into the premise.

Nor is a uniform bound on `lambda_max(G_N)` asserted as a necessary
condition for the desired averaged pair statistic. The distinction
between a maximum frame norm and an averaged quadratic statistic is
preserved here.

## 6. Quantitatively sharp limitation of the old coefficient data

The already constructed, different family `U_tilde=B_N M_N B_N^*`
has the exact bare-cat spectrum and the fixed analytic conjugate map.
Its previously proved inputs include all the primitive diagonal
constants and post-N coefficient cancellations just described. They
also include

$$
|\operatorname{Tr}\widetilde U_N^m|\le\lambda^{m/2},\qquad
\lambda=3+2\sqrt2,
\tag{6.1}
$$

and, on the odd sequence

$$
r_j=21(2j+1),\qquad
N_{r_j}=\frac{\lambda^{r_j}-\lambda^{-r_j}}{4\sqrt2},
$$

the exact return `U_tilde_(N_r)^(2r)` is a scalar unitary.
These statements are frozen in the file cited in Section 1; the
construction is not repeated here.

There is a further exact-scale consequence. Applying (4.4) with
`a=sqrt(lambda)` gives

$$
\limsup_j\frac{\log N_{r_j}}{N_{r_j}}
\widetilde S_{N_{r_j}}(e^{-s/N_{r_j}})
\le\frac{\log\lambda}{4s}.
\tag{6.2}
$$

Every positive multiple of `2r` is also a scalar return, so positivity
of the sum gives

$$
\widetilde S_{N_r}(e^{-s/N_r})
\ge\sum_{\ell\ge1}e^{-4sr\ell/N_r}
=\frac1{e^{4sr/N_r}-1}.
\tag{6.3}
$$

Since `log N_r/r -> log lambda` and `r/N_r ->0`, the lower and upper
bounds match:

$$
\boxed{
\widetilde S_{N_{r_j}}(e^{-s/N_{r_j}})
\sim\frac{\log\lambda}{4s}\,
\frac{N_{r_j}}{\log N_{r_j}}\qquad(s>0\text{ fixed}).
}
\tag{6.4}
$$

Thus the order supplied by the positive frame argument is sharp for
the previously available exponential trace growth and primitive
coefficient data. This is a numerical-order obstruction to a missing
positivity inference, not merely a large upper bound on an inverse
determinant.

The comparison has a specific scope. It does not refute the original
problem. It does not assert compatibility with the original family's
newer all-fixed-iterate sector covariance or a strict unstable-pressure
gap; the conjugate cat has constant periodic unstable multipliers and
has zero such pressure gap.

## 7. Precise status of the next estimate

For the original family it remains unproved here that

$$
\sup_{N\ {
m odd}}\frac1{N^2}
\sum_{m\ge1}e^{-2sm/N}|p_m|^2<\infty
$$

for even one fixed `s>0`. Equations (2.6)--(2.9) supply an exact
contractive representation, and (3.3)--(4.4) give its actual unconditional
consequence from the presently used trace bound. To improve that
consequence by positivity, one must control more of the original
matrix's long-time Gram data or the equivalent weighted Schur
concentration. The complete primitive diagonal and the post-degree
cancellation do not provide that control by themselves.

The related primary paper of S. Nonnenmacher and M. R. Zirnbauer,
*Det-Det correlations for quantum maps: Dual pair and saddle-point
analyses*, J. Math. Phys. **43** (2002), 2214--2240,
DOI `10.1063/1.1462417`, gives exact character representations for a
determinant correlation, and explicitly discusses the additional
semiclassical difficulty. No saddle-point or averaging claim from
that work is used as a bound for the fixed matrices here.



---

