> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round4_2026_10_21/dual_audit_no_exact_scalar_powers.md`. Embedded SHA256: `ef22c0fc94e21398246e4dca3ed54f6cffabf63c053b073793bc394bb3c623d8`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit: no exact scalar powers of the prescribed family

Audit date: 21 October 2026. Auditor: the Weyl-dual research branch.

## 1. Frozen object and verdict

The object audited is `counter_no_exact_scalar_powers.md`, SHA256

`b443bef206df2c6a7764ade3bec61c9a27acd29429ee5889048e7e6e483718a3`.

**Verdict: Theorem 1 and the exceptional-dimension assertion are proved as
written.** In particular the proof covers every odd integer $N\ge3$ other
than $7$, including the small dimensions with Fourier aliases and all
composite dimensions. It proves
$$
 (e^{is_0NA_N}M_N)^n\notin\mathbb CI
 \quad(n\ge1,
 \ s_0\in\overline{\mathbb Q}\setminus\{0\},\ N\ne7).
$$
It does not establish a uniform lower bound for proximity to scalar matrices
and gives no proof or disproof of the requested spectral-statistics limit.

The argument below reconstructs the critical steps independently. The frozen
source was not modified. No numerical spectral evidence enters the verdict.

## 2. Original modular convention and covariance

For $W(k,l)=T(l,k)$, the original finite Weyl matrices are orthonormal for
$\langle X,Y\rangle=N^{-1}\operatorname{Tr}(X^*Y)$. Indeed a nonzero shift
has zero diagonal; a zero shift and nonzero modulation has character sum
zero. The latter assertion holds for nonunit modulations as well: for
$b\ne0\pmod N$, the geometric ratio $e_N(b)\ne1$ has $N$-th power one.
This proves orthogonality on every odd composite modulus, with no field
assumption. There are $N^2$ matrices, so they span all matrices.

The rows of $M_N$ are orthogonal because their inner product contains
$N^{-1}\sum_y e_N(4^{-1}(x-x')y)$. The factor $4^{-1}$ is a unit for odd
$N$, so this is zero exactly when $x\ne x'$. Hence $M_N$ is invertible.

Directly expanding the two matrix products after removing the common kernel
$N^{-1/2}e_N(-8^{-1}(3x^2-2xy+3y^2))$ gives the exponents
$$
 -\frac{ax}{4}+\left(\frac{3a}{4}+b\right)y
 -\frac{3a^2}{8}-\frac{ab}{2}
$$
and
$$
 \left(b'-\frac{3a'}4\right)x+\frac{a'y}4
 +\frac{a'b'}2-\frac{3(a')^2}8.
$$
Every denominator in these expressions denotes the indicated modular
inverse. Substitution of $a'=3a+4b$, $b'=2a+3b$ matches the linear terms,
while the constant in the second expression is
$$
 \frac{a'(4b'-3a')}{8}
 =-\frac{a(3a+4b)}8.
$$
It equals the first constant exactly. Thus no lift-dependent sign or scalar
phase has been omitted:
$$
 M_NW(v)M_N^{-1}=W(Sv),\qquad
 S=\begin{pmatrix}3&2\\4&3\end{pmatrix}.
$$

It follows that $M_N^n$ is scalar if and only if $S^n=I\pmod N$. For the
forward implication use the distinctness of the Weyl basis elements. For the
reverse implication, $M_N^n$ commutes with a basis of the full matrix
algebra, hence with every matrix and is scalar. Since $\det S=1$, its
action on labels is a permutation. If $S^n=I$, every orbit length divides
$n$. This argument is valid over the residue ring; diagonalization of
$S$ is unnecessary.

## 3. Fourier imbalance and arbitrary aliases

Writing $C_j=\cos(2\pi jq)$ and $S_j=\sin(2\pi jq)$, expansion gives
$$
 r=1+C_1-C_7-\tfrac12C_8-\tfrac12C_6,
$$
and
$$
 f-\tfrac1{10}=\tfrac9{10}C_7+\tfrac1{10}C_1-\tfrac1{20}C_8
 -\tfrac1{20}C_6+\tfrac1{100}rS_1
 +\tfrac1{100}r\cos(2\pi p-\alpha_0).
$$
The sine product is
$$
 rS_1=S_1+\tfrac12S_2-\tfrac12S_8+\tfrac12S_6
 -\tfrac14S_9+\tfrac14S_5.
$$
In particular it has no pure $q$-frequency $\pm7$. The last term has
$p$-frequency $\pm1$, so the original coefficients satisfy
$c_{(7,0)}=c_{(-7,0)}=9/20$.

The Fourier coefficient norm is submultiplicative by the convolution
formula and the triangle inequality. Here $\|r\|_{\mathcal F,1}=4$, and
each nonconstant sine or cosine, including the phase-shifted one, has norm
one. Consequently the sum of absolute values of every original coefficient
except the two marked ones is bounded by
$$
 \frac1{10}+\frac1{20}+\frac1{20}+\frac4{100}+\frac4{100}
 =\frac7{25}.
$$
The estimate is deliberately an upper bound; cancellation among unmarked
frequencies is not required.

Let $\widetilde c_v=\sum_{\kappa\bmod N=v}c_\kappa$. The specified
quantization is exactly $A_N=\sum_v\widetilde c_vW(v)$; no extra signs
occur on passing to residue labels. For odd $N\ge3$, the label
$v_0=(7\bmod N,0)$ vanishes only for $N=7$. When it is nonzero its
entire $S$-orbit $\mathcal O$ is disjoint from zero. The orbit sum of
the aggregated coefficients includes $9/20$ from $(7,0)$. It may also
include the other positive coefficient $9/20$. Every remaining included
coefficient is part of a set of total absolute mass at most $7/25$.
Therefore
$$
 \operatorname{Re}\sum_{v\in\mathcal O}\widetilde c_v
 \ge\frac9{20}-\frac7{25}=\frac{17}{100}.
$$
This proof already includes every possible alias, even several unmarked
frequencies falling on a marked residue. It does not require the original
support to inject into the residue group. An assumption such as $N\ge19$
would be unnecessary. The bound also remains valid if some unmarked
coefficients aggregate to the scalar label, since that label is outside the
orbit being summed.

## 4. External theorem and the algebraic hypotheses

The precise external result used is the distinct-exponent
Lindemann--Weierstrass theorem, as stated in Cheng-Chao Huang, *Explicit
Bounds for Linear Forms in the Exponentials of Algebraic Numbers*, ISSAC
2022, Theorem 1.1, DOI
[10.1145/3476446.3536170](https://doi.org/10.1145/3476446.3536170).
The auditor independently opened the
[versioned author PDF, arXiv:2112.05004v2](https://arxiv.org/pdf/2112.05004v2)
on 21 October 2026 and read Theorem 1.1 on printed page 1. The same page
contains the ISSAC publication metadata and DOI. The theorem applies to
distinct algebraic exponents and nonzero algebraic coefficients; their
linear combination of exponentials cannot be zero. The paper's algebraic
numbers are complex numbers, as its Section 2.1 also explicitly confirms.

Here the required hypothesis check is as follows.

1. All entries of $A_N$ and $M_N$ are algebraic: their phases are roots
   of unity, $N^{-1/2}$ is algebraic, and
   $e^{\pm i\alpha_0}=(-3\pm4i)/5$. Algebraicity of $\alpha_0$ itself
   is neither asserted nor needed.
2. Each eigenvalue of the Hermitian algebraic matrix $A_N$ is algebraic,
   being a root of its characteristic polynomial over
   $\overline{\mathbb Q}$. Hermiticity gives diagonalizability, regardless
   of multiplicities. For the set of distinct eigenvalues, the Lagrange
   polynomial
   $\prod_{\mu\ne\lambda}(A_N-\mu I)/(\lambda-\mu)$ is its spectral
   projector and has algebraic entries. Empty products also cause no
   difficulty.
3. Expanding $(e^{isNA_N}M_N)^n$ using these projectors produces a finite
   exponential polynomial in each matrix entry. Coefficients are algebraic
   matrices; slopes are $iN(\lambda_1+\cdots+\lambda_n)$, hence algebraic.
   Equal slopes must first be combined, and zero resulting coefficients
   discarded, as the source expressly does.
4. Multiplication of distinct slopes by a nonzero algebraic $s_0$ keeps
   them distinct and algebraic. The remaining coefficients are nonzero
   algebraic numbers. A zero slope is permitted. No rational linear
   independence of the slopes is necessary: that would be a different
   formulation of transcendence than the linear statement applied here.

It follows that a scalar exponential polynomial of this form which vanishes
at $s_0$ is identically zero. If $U_N(s_0)^n$ is scalar, apply this result
to its off-diagonal entries and to the difference of each diagonal entry
from the first. The unknown scalar at $s_0$ need not be algebraic and is
never used as a coefficient. We therefore obtain
$$
 U_N(s)^n=\zeta(s)I\quad\text{for every complex }s,
$$
where $\zeta$ is entire. The source does not rely on unitarity for complex
$s$; only Hermiticity of $A_N$ and invertibility of $M_N$ are used.

## 5. Derivative and orbit count

At $s=0$ the scalar identity gives $M_N^n\in\mathbb CI$, and hence
$S^n=I\pmod N$. If $L$ is the orbit length of $v_0$, then $L\mid n$.
The ordinary product rule gives, with the factors in their correct order,
$$
 \left.\frac d{ds}U_N(s)^n\right|_{s=0}
 =iN\left(\sum_{j=0}^{n-1}M_N^jA_NM_N^{-j}\right)M_N^n.
$$
The derivative is scalar. Dividing by the nonzero scalar $iNM_N^n$ shows
that the parenthesized matrix $B_n$ must be scalar.

Exact covariance expresses its Weyl coefficient at $v_0$ as
$$
 \frac1N\operatorname{Tr}(W(v_0)^*B_n)
 =\sum_{j=0}^{n-1}\widetilde c_{S^{-j}v_0}
 =\frac nL\sum_{v\in\mathcal O}\widetilde c_v.
$$
The last equality counts a full finite cycle exactly $n/L$ times. The
real part is at least $17n/(100L)>0$, contradicting the vanishing of every
nonzero Weyl coefficient of a scalar matrix. This proves the entire stated
quantifier range, with no subsequence or parameter averaging.

## 6. Genuine exception at dimension seven

For $N=7$, a shift of the original integer Fourier frequency $k$ by
seven leaves $T_7(l,k)$ exactly unchanged for each fixed $l$. Thus in the
linear Fourier quantization of $(1-C_7)G(q,p)$, the three shifted copies
cancel within each fixed $p$-frequency block. This is a statement about
coefficient aggregation, not an assertion that quantization preserves
products. Applying it to the three terms containing $r$ gives
$A_7=(9/10)I$.

Ordinary integer multiplication yields
$$
 S^3=\begin{pmatrix}99&70\\140&99\end{pmatrix}=I\pmod7.
$$
The covariance converse proves $M_7^3$ scalar, and multiplication by the
scalar exponential proves $U_7(s)^3$ scalar for every complex $s$. This
also checks that the exclusion of $7$ in the main theorem is substantive.

## 7. Scope of the result

For the original rational $\tau=10^{-80}$, the theorem excludes all exact
projective returns in every allowed dimension except the finite exception
$7$. The argument makes no transfer from a derivative at zero to a
quantitative estimate at $\tau$. In particular, the positive distance from
scalar matrices for each individual $(N,n)$ may have no useful lower bound
as both parameters grow. Close spectral clustering, small gaps, and
near-returns at times of order $N$ remain uncontrolled.

Accordingly the first outstanding spectral estimate is still the signed,
weighted trace comparison at times proportional to $N$, followed by its
all-orders counterpart. Neither the Lindemann--Weierstrass step nor the
Fourier imbalance supplies that estimate. The frozen source draws this
distinction correctly.

