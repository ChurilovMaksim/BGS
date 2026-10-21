> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round4_2026_10_21/dual_sparse_cat_schatten_trace_sharpening.md`. Embedded SHA256: `784f41271c57c3655215239153fafcd66dc9ecebdcab5eb462d6f25b451bc92d`.
> [Thematic guide](../../topics/dephasing.md).

# Uniform trace-class removal of sparse cat histories

21 October 2026. Supplement to Theorem F in
`dual_all_odd_sparse_cat_history_removal.md`, SHA-256
`ebe8550d0a1598d0d90b1ecf66d1640b23b9e9151f7b67eac0eadf89707a62dd`.
That frozen source is not changed here. The notation, fixed family, and
all-odd threshold N0 are exactly those of Theorem F.

The stronger trace conclusion below was independently noticed by the author
and the separate auditor after Theorem F was frozen. It sharpens the total
normalized removed contribution from O(N^(-1/16)) to O(N^(-2)). It does not
estimate the complementary dense histories or establish H_diag.

## 1. Statement and inputs

On the M=N^2-1 dimensional traceless Weyl space, write

$$
C=\operatorname{Ad}_{U_N}|_{\Lambda_N}=D+R_N,\qquad
D e_v=d_v e_{Sv},\qquad
S=\begin{pmatrix}3&2\\4&3\end{pmatrix}.
$$

For all odd N at least N0, the frozen Theorem F proves

$$
|d_v|\le1,\qquad
|d_v|\le C_0(1+|Sv|_N)^{-1/16}+C_0/N,
\tag{1.1}
$$
$$
\|D^m\|\le2e^{-\kappa m}\quad(m\ge0),\qquad
\|R_N\|\le2.
\tag{1.2}
$$

Here C0 and kappa are positive constants independent of N. Its exact choices
have L at least 3 and kappa=(log 2)/L, so

$$
\kappa<1/3,\qquad
\delta=\kappa^2/32<1/288<1/33.
\tag{1.3}
$$

Indeed R0 is at least one, so the positive logarithmic term in its definition
of L has ceiling at least one, giving L at least three; log 2 is less than one.
Let B_(n,N) be the same exact word sum as in Theorem F: words of length n in
D and R_N having at most floor(delta n) copies of R_N. Thus the collection of
paths being removed is unchanged.

Define the fixed constants

$$
p=33,\qquad A_p=137\,2^{32}C_0^{33},\qquad
\eta=e^{-3\kappa/4},\qquad \lambda=3+2\sqrt2,
$$
$$
T_0=\sum_{n=1}^{32}(\lambda^n+\lambda^{-n}-2),
$$
$$
\boxed{K_* = T_0+
\frac{2^{34}e^{33\kappa}A_p}{e^{3\kappa/4}-1}.}
\tag{1.4}
$$

**Theorem F+.** For every odd N at least N0,

$$
\boxed{\sum_{n=1}^{\infty}|\operatorname{Tr}B_{n,N}|\le K_*.}
\tag{1.5}
$$

Consequently, for every array with sup_(n,N)|w_(n,N)| at most W,

$$
\boxed{\left|\frac1{N^2}\sum_{n\ge1}
w_{n,N}\operatorname{Tr}B_{n,N}\right|\le\frac{WK_*}{N^2}.}
\tag{1.6}
$$

The correction series is absolutely convergent; the same bound holds for every
finite truncation, every Heisenberg window n at most BN, and every infinite
Abel window. All constants are fixed for the original tau=10^(-80), with no
change of tau, parameter average, or prime-modulus restriction.

## 2. Finite-dimensional trace Holder inequality, with proof

We give the finite-dimensional matrix inequality used below to avoid inserting
an unproved estimate into the argument. For an M by M complex matrix X, denote
its decreasing singular values by s_i(X), and write

$$
\|X\|_{S_p}=\left(\sum_{i=1}^M s_i(X)^p\right)^{1/p}.
$$

For a positive integer p and matrices X_1,...,X_p,

$$
|\operatorname{Tr}(X_1\cdots X_p)|
\le\prod_{a=1}^p\|X_a\|_{S_p}.
\tag{2.1}
$$

To prove this, first suppose all X_a are invertible. The kth exterior power
satisfies

$$
\|\mathop{\bigwedge}\nolimits^k X\|
=\prod_{i=1}^k s_i(X),
$$

because a singular-value decomposition induces unitary exterior factors and
diagonal entries equal to products of k singular values. Exterior powers
preserve products, and the operator norm is submultiplicative. Therefore,

$$
\sum_{i=1}^k\log s_i(X_1\cdots X_p)
\le\sum_{i=1}^k\sum_{a=1}^p\log s_i(X_a)
\tag{2.2}
$$

for every k, with equality at k=M by multiplicativity of the determinant.
Put x_i=log s_i(X_1...X_p) and y_i=sum_a log s_i(X_a). Both lists decrease.
For every real t,

$$
\sum_i(x_i-t)_+
=\max_{0\le k\le M}\left(\sum_{i=1}^k x_i-kt\right)
\le\sum_i(y_i-t)_+.
\tag{2.3}
$$

Choose real a and b enclosing both finite lists. On [a,b],

$$
e^x=e^a+e^a(x-a)+\int_a^b e^t(x-t)_+\,dt.
$$

Sum this identity and use (2.3), together with equality of the total sums in
(2.2). This proves

$$
\sum_i s_i(X_1\cdots X_p)
\le\sum_i\prod_{a=1}^p s_i(X_a).
\tag{2.4}
$$

The right side is at most the right side of (2.1) by the scalar Holder
inequality. For completeness, after dividing each list by its l^p norm, this
last assertion is the arithmetic-geometric mean inequality
product_a t_a at most (1/p)sum_a t_a^p, summed over i. A singular-value
decomposition Y=V diag(s_i(Y)) W^* gives
|Tr Y| at most sum_i s_i(Y), since each diagonal entry of W^*V has modulus
at most one. This finishes (2.1) for invertible factors. Approximate each
factor by invertible matrices and pass to the limit. Singular values are
continuous: the eigenvalues of X^*X obey the finite-dimensional min-max
formula, and perturbing its entries perturbs every Rayleigh quotient uniformly
on the unit sphere. This justifies the limiting step.

We also need the ideal inequality

$$
\|XY\|_{S_p}\le\|X\|_{S_p}\|Y\|.
\tag{2.5}
$$

Indeed (XY)(XY)^* is at most ||Y||^2 XX^* as positive semidefinite matrices.
The same min-max formula orders their eigenvalues, so
s_i(XY) is at most ||Y||s_i(X), and summing pth powers proves (2.5).
The analogous left ideal inequality follows by taking adjoints.

Finally, in a cyclic trace of an arbitrary word, choose p designated factors
D and group all the intervening factors into p intervening products. Apply
(2.1) to those p blocks and (2.5) inside each block. Thus the p copies of D
can be charged in S_p and every other factor in operator norm, regardless of
their locations, order, or commutators. This is the precise form used below.

## 3. A uniform, unnormalized Schatten-33 bound

D is a weighted permutation, so its singular values are exactly the |d_v|.
With p=33, (1.1) and (a+b)^p at most 2^(p-1)(a^p+b^p) give

$$
\|D\|_{S_p}^p
\le2^{32}C_0^{33}\left[
\sum_{w\in\Lambda_N}(1+|w|_N)^{-33/16}
 +\frac{M}{N^{33}}\right].
\tag{3.1}
$$

The nonzero centered shell of infinity norm j contains 8j labels; its
Euclidean norm is at least j. Extending the finite sum to all positive j,

$$
\sum_{w\in\Lambda_N}(1+|w|_N)^{-33/16}
\le8\sum_{j\ge1}j(1+j)^{-33/16}
\le8\sum_{j\ge1}j^{-17/16}
\le8\left(1+\int_1^\infty x^{-17/16}\,dx\right)=136.
\tag{3.2}
$$

Also M/N^33 is at most one for N at least one. Therefore

$$
\boxed{\|D\|_{S_{33}}^{33}\le A_p=137\,2^{32}C_0^{33}.}
\tag{3.3}
$$

This bound has no factor of M or N. The summability threshold p>32 is exactly
the dimension-two shell condition p/16>2 for the already proved echo decay.

## 4. Long words: trace-ideal bound and the fixed-density entropy sum

For n at least 33 and j at most floor(delta n), (1.3) gives

$$
n-j\ge n-\lfloor\delta n\rfloor>(1-1/33)n\ge32.
$$

The left side is an integer, so there are at least 33 copies of D. Choose 33
of them for (2.1). Removing those designated factors leaves at most
j+34 possibly empty D runs. Their total length is n-j-33. Applying (1.2) to
each remaining D run and to each of the j copies of R_N gives

$$
\begin{aligned}
|\operatorname{Tr}(\mathrm{word})|
&\le A_p\,2^{j+34}2^j e^{-\kappa(n-j-33)}\\
&=2^{34}e^{33\kappa}A_p\,e^{-\kappa n}(4e^\kappa)^j.
\end{aligned}
\tag{4.1}
$$

To check the run count, before selecting factors there are j+1 D runs.
Each chosen D can split one run into at most two residual runs, increasing
the count by at most one. Adjacent chosen factors are allowed, and their
empty residual runs are included; using ||D^0||=1 at most 2 is harmless.
Thus j+34 is a valid bound. The trace Holder lemma permits all remaining
factors to be charged by the product of these operator bounds.

The frozen Theorem F proves, with the very same fixed delta,

$$
H(\delta)+\delta\log(4e^\kappa)<\kappa/4,
\qquad
\sum_{j\le\lfloor\delta n\rfloor}\binom nj\le e^{nH(\delta)}.
\tag{4.2}
$$

These are elementary inequalities, independent of N and of any dynamical
claim. Explicitly, H(delta) is at most delta log(e/delta), and substituting
delta=kappa^2/32 bounds the left side of the first inequality by
(kappa^2/32)[log 128+1+kappa+2 log(1/kappa)]<kappa/4. The second follows by
putting x=delta/(1-delta)<1 in the binomial expansion of (1+x)^n.

Summing (4.1) over placements and j therefore gives

$$
\boxed{|\operatorname{Tr}B_{n,N}|
\le2^{34}e^{33\kappa}A_p\,\eta^n\quad(n\ge33).}
\tag{4.3}
$$

In particular,

$$
\sum_{n\ge33}|\operatorname{Tr}B_{n,N}|
\le\frac{2^{34}e^{33\kappa}A_p}{e^{3\kappa/4}-1}.
\tag{4.4}
$$

We enlarged the geometric sum to n at least one in (4.4), which only
increases its upper bound.

## 5. Early times: an exact finite lattice count

For 1 at most n at most 32, (1.3) implies floor(delta n)=0. Hence
B_(n,N)=D^n exactly. Since D is a weighted permutation and all its weights
have modulus at most one,

$$
|\operatorname{Tr}D^n|
\le\#\{v\in\Lambda_N:(S^n-I)v=0\pmod N\}.
\tag{5.1}
$$

For any nonsingular two by two integer matrix A,

$$
\#\ker(A:(\mathbb Z/N)^2\longrightarrow(\mathbb Z/N)^2)
\le|\det A|.
\tag{5.2}
$$

Here is a proof covering arbitrary composite N. For a kernel class represented
by x in Z^2, map it to Ax/N modulo A Z^2. The quotient Ax/N is integral.
Changing the representative by Nz changes this image by Az, so the map is
well-defined. If two images agree modulo A Z^2, nonsingularity of A implies
their representatives agree modulo N Z^2. The map is therefore injective
into Z^2/A Z^2.

The latter quotient has |det A| elements, as can be checked directly. If
(a,c)^T is its first column, put g=gcd(a,c)>0 and choose integers u,v with
ua+vc=g. The unimodular row operation

$$
\begin{pmatrix}u&v\\-c/g&a/g\end{pmatrix}
$$

sends A to an integer triangular matrix with diagonal entries g,d', where
gd'=det A. Every class has a unique representative whose second coordinate
is in {0,...,|d'|-1} and whose first coordinate is in {0,...,g-1}: first
reduce the second coordinate using the second column, and then the first
using the first column. This gives g|d'|=|det A| classes. The first column
of a nonsingular matrix cannot be zero; negative entries do not affect this
argument. This proves (5.2) without a prime or divisor assumption.

The eigenvalues of S are lambda and lambda^(-1). Therefore S^n-I is
nonsingular for every positive n, and

$$
|\det(S^n-I)|=\lambda^n+\lambda^{-n}-2.
\tag{5.3}
$$

Combining (5.1)--(5.3) gives

$$
\sum_{n=1}^{32}|\operatorname{Tr}B_{n,N}|\le T_0.
\tag{5.4}
$$

Equations (4.4) and (5.4) prove (1.5), and the triangle inequality proves
(1.6). No estimate from one time range is extended to another without the
exact early-time count.

## 6. The two-HS strengthening, as a shorter intermediate proof

There is a simpler intermediate gain that does not use Schatten exponents
above two. Theorem F gives

$$
\sigma_D^2:=\frac{\|D\|_{\rm HS}^2}{M}
\le20C_0^2N^{-1/8}.
$$

For n at least two and j at most floor(delta n), there are at least two D
factors since delta<1/2. Select those two in Hilbert--Schmidt norm and use
the cyclic trace Cauchy--Schwarz inequality. At most j+3 remaining D runs
give

$$
\frac{|\operatorname{Tr}(\mathrm{word})|}{M}
\le8e^{2\kappa}\sigma_D^2 e^{-\kappa n}(4e^\kappa)^j.
$$

Summing by (4.2) produces a geometric bound with N^(-1/8). At n=1 the trace
vanishes exactly: det(S-I)=-4 is invertible modulo every odd N, so S has no
fixed nonzero label. Hence the entire correction already obeys

$$
\frac1{N^2}\sum_{n\ge1}|\operatorname{Tr}B_{n,N}|
\le\frac{160e^{2\kappa}C_0^2}{e^{3\kappa/4}-1}N^{-1/8}.
\tag{6.1}
$$

This shorter proof supplies an independent check of the trace-ideal strategy.
The stronger O(N^(-2)) statement in Section 1 uses full summability of the
weighted permutation's singular values together with the exact early count.

## 7. What this sharpens, and the unresolved step

The exact pair identity remains

$$
\operatorname{Tr}C^n=|\operatorname{Tr}U_N^n|^2-1.
$$

Thus removing the same fixed-density sparse histories from the complete
signed pair functional now has error O(N^(-2)), uniformly for bounded weights.
The replacement formula in Section 8 of Theorem F is unchanged; only its
proved error is sharpened. The result is an absolute bound on the entire
removed trace series, so it also controls cancellation-sensitive weight sums.

The first still-unproved estimate is exactly the dense-history expression
in Section 9 of Theorem F. These arguments do not estimate the signed sum of
histories with more than delta n non-cat steps, and they do not prove
higher-order factorial-moment comparison. The normalized O(N^(-2)) estimate
for the removed class cannot be substituted for that missing calculation.
