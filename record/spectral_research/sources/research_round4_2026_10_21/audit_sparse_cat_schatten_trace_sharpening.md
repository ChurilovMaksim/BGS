> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round4_2026_10_21/audit_sparse_cat_schatten_trace_sharpening.md`. Embedded SHA256: `bdc1401fb3476afde3739a71de71e1196faaa5ffda0b1a51e9c656301b9f42ee`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit: the uniform absolute trace bound for sparse cat histories

21 October 2026. Auditor: `/root/audit_uniform_word_r4`.

## 1. Frozen source and verdict

Audited source: `dual_sparse_cat_schatten_trace_sharpening.md`, SHA-256
`784f41271c57c3655215239153fafcd66dc9ecebdcab5eb462d6f25b451bc92d`.
The entire source was read, its hash checked, and no source was modified.

**Verdict: Theorem F+ is proved as written.** In particular, for the same
exact word sums $B_{n,N}$ and the same fixed $\delta>0$ as in Theorem F,
$$
\sum_{n\ge1}|\operatorname{Tr}B_{n,N}|\le K_*
$$
holds uniformly over all sufficiently large odd N. The exact signed pair
correction for any bounded array of weights is consequently $O(N^{-2})$.
The stated two-Hilbert--Schmidt intermediate estimate is also correct.

The prerequisite Theorem F was separately audited in
`audit_all_odd_sparse_cat_history_removal.md`, SHA-256
`f46c404d78344f4bfa71c0c657abd9119afc78d4fb90a79b6452fdf7cf8989e0`.
That audit reconstructed the exact echo orientation, fixed-box orbit
escape, all run constants, entropy bound, and the dimension $M=N^2-1$.
The present audit examines the new Schatten inequality and early-time
integer count rather than relying on the author's status for those steps.

The theorem bounds the sum of absolute traces. It must not be reported as
a uniform bound on $\sum_n\|B_{n,N}\|_{S_1}$ over all times: the early
powers $D^n$ are handled by their fixed-label traces, not by such a
trace-norm estimate. The displayed theorem itself makes the correct claim.

## 2. The trace Holder proof is valid for noncommuting factors

Let $X_1,\ldots,X_p$ initially be invertible square matrices of common
dimension M. Singular-value decomposition gives
$$
\|\bigwedge^kX\|=\prod_{i=1}^k s_i(X),
$$
where singular values are ordered decreasingly: the exterior powers of the
unitary factors remain unitary and the diagonal exterior factor has all
k-fold products. Multiplicativity of exterior powers and submultiplicativity
of the operator norm therefore give
$$
\sum_{i\le k}\log s_i(X_1\cdots X_p)
\le\sum_{i\le k}\sum_{a=1}^p\log s_i(X_a).
$$
At k=M there is equality, because both sides are logarithms of the absolute
determinant of the product. The right-hand logarithmic list is decreasing,
since it is a sum of decreasing lists.

For any decreasing finite list x and real t,
$\sum_i(x_i-t)_+=\max_{0\le k\le M}(\sum_{i\le k}x_i-kt)$.
Applying the preceding prefix inequalities proves the positive-part
inequality (2.3) in the source. For bounds a and b enclosing both lists,
the identity
$$
e^x=e^a+e^a(x-a)+\int_a^b e^t(x-t)_+\,dt
$$
is exact. Indeed the integral is over $[a,x]$ and equals
$e^x-(x-a+1)e^a$. Summing this identity, the linear terms cancel by
equality of the total logarithmic sums, and the integral terms are ordered
by the positive-part inequality. Thus
$$
\sum_i s_i(X_1\cdots X_p)
\le\sum_i\prod_{a=1}^p s_i(X_a).
$$
Scalar Holder, applied to these p nonnegative lists, gives the product of
their $\ell^p$ norms. The source supplies a direct proof of this scalar
step by normalization and the arithmetic-geometric mean inequality.
Finally, an SVD of the product gives
$|\operatorname{Tr}Y|\le\sum_i s_i(Y)$, since the diagonal entries of
the intervening unitary matrix have modulus at most one. Therefore
$$
|\operatorname{Tr}(X_1\cdots X_p)|\le\prod_{a=1}^p\|X_a\|_{S_p}.
$$
This argument actually proves the corresponding trace-norm inequality
for the product as well; it never assumes that the factors commute or
are positive.

Invertible matrices are dense: for example, replace every zero singular
value in an SVD by a small positive number. Singular values vary continuously.
For clarity, the finite-dimensional min-max formula needed here follows
directly from an orthonormal eigenbasis: for decreasing eigenvalues of a
Hermitian A,
$$
\lambda_k(A)=\min_{\dim L=M-k+1}\max_{x\in L,\|x\|=1}\langle x,Ax\rangle.
$$
The subspace spanned by eigenvectors k through M gives one inequality; any
subspace of that dimension intersects the span of the first k eigenvectors
nontrivially, giving the other. Perturbing A in operator norm changes each
Rayleigh quotient by at most that norm, hence changes every eigenvalue by
at most that norm. Apply this to $X^*X$ and take square roots. This
justifies passage from invertible factors to arbitrary matrices in the
proof above.

## 3. Ideal inequality and charging the designated factors

For arbitrary X and Y,
$$
XYY^*X^*\preceq\|Y\|^2XX^*.
$$
The same min-max argument orders the eigenvalues, so
$s_i(XY)\le\|Y\|s_i(X)$ for every i. Summing their pth powers proves
$\|XY\|_{S_p}\le\|X\|_{S_p}\|Y\|$; the left version follows by
adjoints.

In a trace, cyclically start at one designated D factor and group each of
the p designated D factors with the intervening product that follows it.
There are p resulting blocks. Applying the trace Holder inequality to those
blocks and then the ideal inequality charges each designated D once in
$S_p$, with the operator norms of all intervening products. This precisely
justifies selecting 33 D factors anywhere in a noncommuting word. There is
no sum over possible selections and hence no additional binomial factor.

## 4. Exact constant in the unnormalized Schatten bound

The weighted permutation D has singular values $|d_v|$. With p=33 and
the uniform echo bound from Theorem F,
$$
\|D\|_{S_{33}}^{33}
\le2^{32}C_0^{33}\left[
\sum_{w\in\Lambda_N}(1+|w|_N)^{-33/16}+M/N^{33}\right].
$$
The centered shell of sup norm j has 8j points and Euclidean norm at least
j. Hence its complete sum is bounded by
$$
8\sum_{j\ge1}j(1+j)^{-33/16}
\le8\sum_{j\ge1}j^{-17/16}
\le8\left(1+\int_1^\infty x^{-17/16}\,dx\right)=136.
$$
The integral is exactly sixteen. The remaining term $M/N^{33}$ is at
most one. Therefore $A_p=137\,2^{32}C_0^{33}$ is a valid bound, with
no factor of N or M. This unnormalized bound is the reason the final
normalized error reaches $N^{-2}$.

## 5. The number of designated factors and the remaining runs

The actual definition in Theorem F gives $L\ge3$, so
$\kappa=(\log2)/L<1/3$ and
$\delta=\kappa^2/32<1/288<1/33$. For every n at least 33 and every
selected j,
$$
n-j\ge n-\lfloor\delta n\rfloor>(1-1/33)n\ge32.
$$
The integer n-j is consequently at least 33. The strict inequality is
enough at the endpoint n=33 and handles all integer rounding.

Before designating factors, a word with j R letters has j+1 possibly empty
D runs. Each of the 33 chosen D factors introduces at most one additional
residual run. Thus there are at most j+34 residual D runs, with total length
n-j-33. If cyclic regrouping merges endpoint runs this only reduces the
count. An empty run has norm one, which is at most the uniform prefactor
two used for a general D run.

The trace Holder inequality, $\|D\|_{S_{33}}^{33}\le A_p$,
$\|D^m\|\le2e^{-\kappa m}$, and $\|R_N\|\le2$ now yield
$$
|\operatorname{Tr}(\text{word})|
\le2^{j+34}2^j A_p e^{-\kappa(n-j-33)}
=2^{34}e^{33\kappa}A_p e^{-\kappa n}(4e^\kappa)^j.
$$
Every factor and every residual run has been charged. No operator-norm
contraction of D itself, or commutativity between D and R, is assumed.

The independently checked entropy inequality of Theorem F gives
$H(\delta)+\delta\log(4e^\kappa)<\kappa/4$, with the exact same fixed
delta. Summing the word estimate over placements and allowed j therefore
gives
$$
|\operatorname{Tr}B_{n,N}|
\le2^{34}e^{33\kappa}A_p e^{-3\kappa n/4},\qquad n\ge33.
$$
Enlarging the geometric sum from n at least 33 to n at least one proves
the late part of $K_*$ with denominator $e^{3\kappa/4}-1$.

## 6. The exact early-time bound over arbitrary composite moduli

For $1\le n\le32$, $\delta n<1$, so $B_{n,N}=D^n$ exactly.
Each diagonal entry of this weighted permutation is either zero or the
product of weights along a label fixed by $S^n$. As every weight has
modulus at most one,
$$
|\operatorname{Tr}D^n|
\le\#\ker(S^n-I:(\mathbb Z/N\mathbb Z)^2\to(\mathbb Z/N\mathbb Z)^2).
$$
Including the zero vector in this upper bound only enlarges it.

For a nonsingular integer matrix A, the map
$$
[x]\in\ker(A\bmod N)\longmapsto Ax/N\pmod{A\mathbb Z^2}
$$
is well-defined, since Ax/N is integral and changing x by Nz changes its
image by Az. It is injective: equality of two target classes gives
$A(x_1-x_2)=NAz$, so nonsingularity implies $x_1-x_2=Nz$.
This proves that the kernel cardinality is at most the index of
$A\mathbb Z^2$ in $\mathbb Z^2$, for every N without a coprimality
assumption.

The source's direct calculation of that index is correct. For first column
$(a,c)^t\ne0$, choose $g=\gcd(a,c)>0$ and Bezout coefficients
$ua+vc=g$. The displayed integer row matrix has determinant one and
turns A into $\left(\begin{smallmatrix}g&b'\\0&d'\end{smallmatrix}\right)$
with $gd'=\det A\ne0$. In its quotient, reduce the second coordinate
modulo $|d'|$ using the second column, then reduce the first modulo g
using the first column. Uniqueness follows because the difference of two
such representatives has second coordinate of modulus less than
$|d'|$, forcing the second-column coefficient to vanish; the first
coefficient then also vanishes. There are exactly $g|d'|=|\det A|$
classes. The unimodular row operation preserves the index.

Thus the bound $\#\ker(A\bmod N)\le|\det A|$ is fully proved here,
including composite N. For $A=S^n-I$, the eigenvalues $\lambda^n-1$
and $\lambda^{-n}-1$ are nonzero, and
$$
|\det(S^n-I)|=\lambda^n+\lambda^{-n}-2.
$$
This gives precisely the finite constant $T_0$ after summing n from
one to 32. There is no appeal to uniformity of a long-time asymptotic
formula at these early times.

## 7. Total bound, two-HS check, and exact scope

Adding the early fixed-label count and the late geometric estimate proves
$\sum_{n\ge1}|\operatorname{Tr}B_{n,N}|\le K_*$ with the stated
constant, uniformly for all odd $N\ge N_0$. The trace here is an
ordinary trace on dimension $M=N^2-1$. Division by the original pair
normalization $N^2$ gives exactly $WK_*/N^2$ for bounded weights.
No replacement of M by N in a Schatten norm has occurred.

The shorter intermediate argument also checks correctly. For n at least
two, $\delta<1/2$ guarantees at least two D factors. Trace Cauchy--Schwarz
charges two Hilbert--Schmidt norms, leaving at most j+3 D runs and the
factor $8e^{2\kappa}\sigma_D^2$. At n=1, $B=D$ has trace zero:
$\det(S-I)=-4$ is invertible modulo every odd N, so its only fixed
label is the excluded zero. Inserting
$\sigma_D^2\le20C_0^2N^{-1/8}$ gives exactly the constant 160 in
(6.1). This is consistent with, but weaker than, Theorem F+.

For real pair weights the correction is real; absolute convergence and the
bound do not require that fact. Abel windows at any fixed positive s are
covered by the same bounded-weight estimate, and finite Fourier windows
need no additional restriction. These are bounds on the correction,
not a statement that the original uncorrected Abel tail is uniformly small.

The first missing step for the original problem remains the signed estimate
of the retained histories with more than $\delta n$ non-cat steps,
followed by the higher-order factorial-moment estimates. The stronger
$N^{-2}$ error for the removed sector does not supply either estimate.
