> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round5_2026_10_21/root_audit_cubic_character_pq_obstruction.md`. Embedded SHA256: `9cd22e7f5895b7ac705e396e2c193c9d733f27c7f897329584dbc293ec38087e`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/arithmetic.md).

# Independent audit: cubic-character auxiliary obstruction

Date: 2026-10-21. Auditor: `/root`.

Audited source: `arithmetic_cubic_character_pq_obstruction.md`, SHA256
`0b67c9c8d2f698046af49d0527eaf81169cd76d84112ffeebd6bfdeb79ac1625`.

**Outcome:** the stated auxiliary-family results are justified. These are
not a counterexample to the original family, and the source explicitly
maintains this distinction. No theorem about the original H_diag follows
from this auxiliary construction.

## 1. External theorem checked directly

I opened and read Todd Cochrane and Christopher Pinner's author-hosted
paper, *Using Stepanov's method for exponential sums involving rational
functions*, https://www.math.ksu.edu/~cochrane/research/stepmix.pdf,
especially its Theorems 1.1 and 1.2 and definitions (1.7), (1.10), (1.11).
The author's publication list independently links that file to
*Journal of Number Theory* **116** (2006), no. 2, 270–292:
https://www.math.ksu.edu/~cochrane/research/research09.html.
The publisher page returned HTTP 403; the mathematical theorem and the
publication identification were nevertheless available in the two
author-hosted primary sources. The PDF bears a later preparation date,
which does not change the theorem statement read here.

For a cubic character and the three simple roots of
R(X)=X(X-1)(X-3), a root of multiplicity one excludes every forbidden
perfect power, as required by (1.11), not just a third power. The
nonzero-frequency additive polynomial has degree one and no finite poles.
For the multiplicative correlation polynomial R(X)R(phi(X))^2, unequal
root sets of cardinality three leave at least one root of multiplicity
one. If the two root sets have intersection of size m, its distinct-root
count is 6-m, exactly m multiplicities are divisible by three, and the
total degree is nine. These are precisely the parameters used in the
source's application of Theorem 1.2. No missing singular-point terms are
present; the later replacement of the three zero values by one is
accounted for separately.

## 2. Construction and Fourier calculations reconstructed

Let p>5 be prime, p=1 mod 3, and let lambda_j equal the cubic character
of R(j) off its roots, with value one at its roots. Then
V=F* diag(lambda) F is unitary and V^3=I exactly.

For nonzero translation, a three-element subset of the prime field
cannot be invariant: every orbit of that translation has length p.
For reflection, its fixed element in {0,1,3} would have to be 0, 1,
or 3. The corresponding equality of twice the fixed element and the sum
of the other two respectively forces p to divide 4, 1, or 5. All are
excluded by p>5. Thus both correlation polynomials satisfy the theorem's
nondegeneracy hypothesis, including the zero-frequency reflection mode.

Writing V_xy=a_(y-x), direct finite Fourier orthogonality gives the
eigenvalues of its squared-entry and reversal matrices as

$$
 \gamma_r=p^{-1}\sum_j\lambda_j\overline{\lambda_{j+r}},
 \qquad
 \eta_r=p^{-1}\sum_j\lambda_j\overline{\lambda_{-r-j}}.
$$

I independently checked the signs: the first sum enforces j-k+r=0,
whereas the second enforces j+k+r=0. Both matrices are normal
circulants, so bounds on these eigenvalues are operator-norm bounds.
The zero mode of the first matrix is one and all other first modes,
and every second mode, have magnitude at most 4/sqrt(p)+7/p.
The trivial bound by one follows directly from these averages of
unit-modulus quantities. The entry bound 4/sqrt(p) follows from the
published additive estimate plus the three modified roots; p=7 is
covered by the trivial unitary entry bound.

## 3. Probability and moment conclusions reconstructed

The three spectral clusters have sizes n_0,n_1,n_2 summing to p, so
sum_a n_a(n_a-1)>=p^2/3-p. For a fixed compact window [-R_0,R_0],
the set of translated origins exposing a cluster has measure at most
6R_0/p. This proves convergence in probability in the vague topology
to the zero measure: any finite collection of compact supports lies
in such an interval. It does not contradict unit intensity because
the counts have no uniform-integrability bound.

For nonnegative b, retaining only pairs within the same cluster is a
valid lower bound. Positivity of the cross terms in its periodization
gives integral_0^1 b_p(t)^2 dt >= p^{-1} integral_R b^2. Hence
M_2 >= (p/6-1/2) integral b^2, while the CUE term is at most
(integral b)^2/2. This proves the divergent fixed-test moment and,
independently, the different bounded-observable local weak limit.

## 4. Simple-spectrum variant reconstructed

Replacing lambda_j by lambda_j exp(2 pi i sqrt(2) j/p^4) changes each
Fourier coefficient by at most d_p=2 pi sqrt(2) p^-3. Each correlation
average changes by at most 2d_p. There is no dimension factor because
the exact circulant eigenvalue formulas still apply.

Every pair of distinct eigenangles has an irrational difference of
the form a/3+sqrt(2)(j-k)/p^4. No positive integer multiple can be an
integer, so all powers have simple spectrum and none is scalar.
The exact diagonal form at times 3m gives the source's near-return
bound 6 pi sqrt(2) m p^-3. Cluster widths are O(p^-3), so their
scaled widths tend to zero. The source's periodized autocorrelation
identity for b then proves the same divergent moment, with the
within-cluster value integral b^2+o(1). The local weak limit remains
the zero measure by the same interval-covering argument.

## 5. Logical consequence and its limit

This construction rules out a general implication from small maximum
entries, mixing of P=|V|^2, decay of Q_xy=V_xy conjugate(V_yx),
spectral simplicity, and absence of exact scalar powers to H_diag.
It also rules out closing the original proof using those properties
alone. It neither changes the prescribed tau nor supplies a bad
subsequence of the prescribed U_N. The original first unproved
weighted signed trace estimate is unaffected.

This audit is a mathematical reconstruction, not a formal proof in
Lean, not external peer review, and not a claim of historical priority.
