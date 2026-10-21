> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/root_gram_permutation_identity.md`. Embedded SHA256: `ca635dab171d81b673aec7136b2123ab9f2b82deac8a8a9b82a436d961520375`.
> [Thematic guide](../../topics/closure.md).

# Permutation correlations, positive Gram operators, and fermionic coefficients

Research continuation, 20 October 2026. This is a self-contained algebraic
and analytic lemma for the endpoint integrals arising in the current
three-cell calculation. It does not assume that arbitrary orbit families
admit that endpoint reduction. In particular, it does not prove
`H_diag`, a lower bound for the complete off-diagonal sum, or a universal
law for the actual endpoint measures.

## 1. The positive operator

Let mu and nu be Borel probability measures on the real line. Compact
support is sufficient for every application here, but is not needed for
the identities in Sections 1--3. For real t define

$$
 (F_t f)(b)=\int e^{it ab} f(a)\,d\mu(a),\qquad
 F_t:L^2(\mu)\longrightarrow L^2(\nu).
 \tag{1.1}
$$

This is a Hilbert--Schmidt operator: its kernel has modulus one and

$$
 \|F_t\|_{\rm HS}^2=\iint 1\,d\mu\,d\nu=1.
 \tag{1.2}
$$

The operator

$$
 K_t=F_tF_t^*,\qquad
 K_t(b,b')=\int e^{it a(b-b')}\,d\mu(a)
 \tag{1.3}
$$

is positive and trace class, with trace one. To verify these assertions
without a kernel-diagonal inference, for an orthonormal basis `(e_j)` of
`L^2(nu)` use

$$
 \langle e_j,K_te_j\rangle=\|F_t^*e_j\|^2,\qquad
 \sum_j\|F_t^*e_j\|^2=\|F_t\|_{\rm HS}^2=1.
 \tag{1.4}
$$

Thus its eigenvalues `(lambda_j(t))`, including multiplicity, are
nonnegative, sum to one, and satisfy `lambda_j<=1`. In particular

$$
 0<\operatorname{Tr}(K_t^r)=\sum_j\lambda_j(t)^r\le1
 \quad\text{for every integer }r\ge1.
 \tag{1.5}
$$

Strict positivity follows because at least one eigenvalue is positive.
There is no assertion of a positive lower bound uniform over all t or
over all choices of the measures.

For `r>=2` the cyclic integral formula is

$$
 \operatorname{Tr}(K_t^r)=
 \int\prod_{j=1}^r K_t(b_j,b_{j+1})\,
                      d\nu(b_1)\cdots d\nu(b_r),
 \qquad b_{r+1}=b_1.
 \tag{1.6}
$$

One direct justification is to compose the bounded kernels by Fubini.
They are Hilbert--Schmidt on probability spaces, and for two
Hilbert--Schmidt kernels the trace of their product is the integral of
their two kernels in reversed variables. Approximation of both kernels
in `L^2(nu times nu)` by finite-rank kernels proves this last formula by
Cauchy--Schwarz. Apply it to `K_t` and `K_t^(r-1)`; their composed kernels
are bounded by one. Formula (1.6) follows. For `r=1` use (1.4).

## 2. The complete correlation of two permutations

Let `a_1,...,a_n` be independent with common law mu, and let
`b_1,...,b_n` be independent with common law nu, independent also of
all the a variables. For a permutation sigma of `{1,...,n}` put

$$
 Z_\sigma=\exp\left(it\sum_{j=1}^n a_j b_{\sigma(j)}\right).
 \tag{2.1}
$$

For every two permutations sigma and pi,

$$
 \boxed{\quad
 \mathbb E[Z_\sigma\overline{Z_\pi}]
 =\prod_{c\in\operatorname{Cycles}(\pi^{-1}\sigma)}
                    \operatorname{Tr}(K_t^{|c|}).
 \quad}
 \tag{2.2}
$$

**Proof.** Integrate each independent a variable first. The result is

$$
 \int\prod_{j=1}^n K_t(b_{\sigma(j)},b_{\pi(j)})\,d\nu^n(b).
 \tag{2.3}
$$

Relabel the b variables by pi. This leaves their joint law unchanged
and decomposes the product into the disjoint cycles of
`pi^(-1) sigma`. The variables belonging to different cycles are
independent. A cycle of length r contributes (1.6), with a possible
reversal of its orientation. Reversal conjugates a real positive trace
and hence does not change it. A fixed point contributes one. This
proves (2.2).

Every quantity in (2.2) is positive and real. Individual samples
`Re(Z_sigma conjugate Z_pi)` can nevertheless be negative.
Positivity is a statement about this precisely specified independent
endpoint integral.

For the two different cyclic orders of three labelled cells, the
relative permutation is a three-cycle. Consequently

$$
 \int \exp\left(it\sum_{j=1}^3
     a_j(b_{j+1}-b_{j-1})\right)d\mu^3(a)d\nu^3(b)
 =\operatorname{Tr}(K_t^3)>0,
 \tag{2.4}
$$

where indices are read modulo three. Either overall sign in the
exponent gives the same value.

## 3. Exact fermionic summation

Let `E=(e^(it a_i b_j))_(1<=i,j<=n)`. Then

$$
 \boxed{\quad
 \mathbb E|\det E|^2=(n!)^2 e_n(K_t).
 \quad}
 \tag{3.1}
$$

Here `e_n(K_t)` is the sum of the products of n different eigenvalues
of the positive trace-class operator K_t. It is absolutely convergent,
with

$$
 0\le e_n(K_t)\le\frac1{n!}.
 \tag{3.2}
$$

For completeness, expand the two determinants in (3.1) and use (2.2).
For each relative permutation rho there are n! pairs `(sigma,pi)`.
Their signs multiply to `sgn(rho)`. Thus the left side is

$$
 n!\sum_{\rho\in S_n}\operatorname{sgn}(\rho)
              \prod_{c\in\operatorname{Cycles}(\rho)}p_{|c|},
 \qquad p_r=\operatorname{Tr}(K_t^r).
 \tag{3.3}
$$

The coefficient identity

$$
 \frac1{n!}\sum_{\rho\in S_n}\operatorname{sgn}(\rho)
                 \prod_c p_{|c|}=e_n(K_t)
 \tag{3.4}
$$

can be proved directly by grouping permutations according to their
numbers `m_r` of r-cycles. There are
`n! / product_r(r^(m_r) m_r!)` such permutations, and their sign is
`product_r (-1)^((r-1)m_r)`. Therefore their generating function is

$$
 \exp\left(\sum_{r\ge1}\frac{(-1)^{r-1}p_r}{r}z^r\right)
 =\prod_j(1+z\lambda_j(t)).
 \tag{3.5}
$$

Both sides converge absolutely for `|z|<1`, because `p_r<=1` and
`sum lambda_j=1`; coefficient comparison proves (3.4). Equations
(3.3)--(3.4) give (3.1). Inequality (3.2) follows by expanding
`(sum_j lambda_j)^n` and retaining terms with pairwise different
indices.

Without the determinant signs the same proof gives

$$
 \mathbb E|\operatorname{per}E|^2=(n!)^2h_n(K_t),
 \tag{3.6}
$$

where `h_n` is the complete homogeneous symmetric function, defined by
`sum_n h_n z^n=product_j(1-z lambda_j)^(-1)` for `|z|<1`.
Thus the different cycle signs have a precise algebraic role; they
cannot be replaced by the positivity of one collection of orbit pairs.

## 4. Uniformity on compact frequency intervals

As t tends to s, dominated convergence in (1.1) gives
`||F_t-F_s||_HS -> 0`. Factoring the difference of the two positive
operators yields

$$
 \|K_t-K_s\|_1
 \le(\|F_t\|_{\rm HS}+\|F_s\|_{\rm HS})
                   \|F_t-F_s\|_{\rm HS}
 =2\|F_t-F_s\|_{\rm HS}.
 \tag{4.1}
$$

This product bound follows from the Hilbert--Schmidt Cauchy--Schwarz
inequality; it can also be checked first for finite matrices and then
by finite-rank approximation. Since `||K_t||<=1`, telescoping powers
gives

$$
 |\operatorname{Tr}K_t^r-\operatorname{Tr}K_s^r|
 \le r\|K_t-K_s\|_1.
 \tag{4.2}
$$

Consequently, for any fixed probability measures and any compact real
interval J,

$$
 \min_{t\in J}\operatorname{Tr}(K_t^3)>0.
 \tag{4.3}
$$

This is an existence bound, not an explicit numerical lower bound.
If `|a|<=A` and `|b|<=B`, then
`||F_t-F_s||_HS<=AB|t-s|`, providing an explicit continuity modulus.

At t=0 the operator is rank one and all its positive power traces are
one. Formula (3.1) then gives zero for n>=2, as the matrix E is a matrix
of ones. This also checks the distinction between positive individual
permutation correlations and a signed determinant cancellation.

## 5. The sine-kernel case: an exact implication with stated hypotheses

Suppose, in addition, that mu and nu are the uniform probability
measures on intervals of positive lengths A and B. Their interval
centres only introduce a diagonal unitary conjugation in (1.3).
After removing this conjugation, its kernel is

$$
 K_t(b,b')=
 \frac{\sin(tA(b-b')/2)}{tA(b-b')/2}.
 \tag{5.1}
$$

For t nonzero put `L=|t|AB/(2pi)` and rescale
`x=|t|A(b-centre(nu))/(2pi)`. The probability measure `db/B`
becomes `dx/L` on the interval of length L. The unitary change from
`L^2(dx/L)` to `L^2(dx)` therefore identifies K_t with

$$
 \frac1L\mathsf S_L,\qquad
 \mathsf S_L(x,y)=\frac{\sin\pi(x-y)}{\pi(x-y)},
 \quad x,y\text{ in an interval of length }L.
 \tag{5.2}
$$

In particular

$$
 \operatorname{Tr}K_t^r=L^{-r}\operatorname{Tr}\mathsf S_L^r,
 \qquad e_n(K_t)=L^{-n}e_n(\mathsf S_L).
 \tag{5.3}
$$

This elementary exact bridge explains why a sine kernel can arise
inside an encounter integral. It does **not** identify the actual
homoclinic endpoint measures of the prescribed nonlinear map with
uniform interval measures. That identification requires a separate
geometric proof and has not been used as a hypothesis in any claimed
theorem here.

## 6. Application boundary for the spectral-statistics problem

The three-cell orbit calculation must separately establish:

1. a quadratic expansion of its exact deck-corrected action with a
   uniform error whose product with N tends to zero;
2. convergence of its actual weighted six endpoint variables to a
   product of three copies of each of two probability measures;
3. the weighted orbit count, including exclusion of extra markers,
   primitive periods, and the conversion from words to geometric
   orbits;
4. the uniform quantum amplitude comparison.

Once those statements are proved, (2.4) evaluates the resulting
complete signed three-cell endpoint integral. The identity alone
supplies none of them. Even after that evaluation, it says nothing
about pairs outside the specified family. Their total signed
contribution remains the first unresolved spectral-statistics issue.

No independent random phases are added to the quantum family in this
lemma's application. The independent variables describe the limiting
weighted endpoint distribution proved from the deterministic coding;
that limiting distribution must not be substituted without its error
estimate.
