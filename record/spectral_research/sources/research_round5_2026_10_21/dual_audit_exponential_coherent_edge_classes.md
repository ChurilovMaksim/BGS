> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round5_2026_10_21/dual_audit_exponential_coherent_edge_classes.md`. Embedded SHA256: `598579babb15dfa66582c5d8f66d6b287dea556312aa52e606eda555df0a04d0`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit: exponentially large coherent directed-edge classes

Auditor: /root/weyl_dual_heisenberg_20261021. Date: 21 October 2026.

Frozen source audited:
root_exponential_coherent_edge_classes.md, SHA256
001fd27ca128f1a00417838e0f4b07d7ad19f291e8c2c5fbb593e614d2ec29e0.
The source hash was independently recomputed before this audit was fixed.
The source has not been edited.

**Verdict:** Sections 1--6 prove the stated exponential lower bound and
the forced negative complementary bound, subject exactly to the finite
unitary/mixing hypotheses (1.1). The application to the original family
uses the previously proved physical-kernel and oscillatory estimates.
No additional independence or spectral-universality hypothesis appears
in the proof. These statements do not prove or refute H_diag.

This audit reconstructs the analytic and combinatorial parts separately.
Agreement with another agent or a previous review is not used as evidence.

## 1. The hypotheses and their elementary consequences

Let U be unitary, P_uv=|U_uv|^2, and J_uv=1/N. Unitarity makes P
doubly stochastic. Set A=P-J. The hypotheses are max P<=C/N and
||A||_op<=1/2, for fixed C>=1.

The row and column square bounds in source (2.1) both follow from

$$
\sum_y(P_{vy}-1/N)^2=\sum_yP_{vy}^2-1/N
\le (C-1)/N.
$$

The column calculation is identical. Thus for k>=2,

$$
|(A^k)_{vv}|
\le \|e_v^*A\|_2\,\|A\|_{\rm op}^{k-2}\,\|Ae_v\|_2
\le (C-1)N^{-1}2^{-(k-2)}.
$$

The k=1 bound |A_vv|<=C/N is valid for C>=1. Also
||A||_HS^2<=C-1, and Hilbert--Schmidt Cauchy--Schwarz gives

$$
|\operatorname{Tr}A^n|
\le\|A\|_{\rm HS}\|A^{n-1}\|_{\rm HS}
\le(C-1)2^{-(n-2)}\qquad(n\ge2).
$$

Since AJ=JA=0, P^n=J+A^n for n>=1. Therefore T_n=Tr P^n
satisfies source (2.3). None of these steps assumes normality of A.

## 2. Exact visit generating function and its uniform approximation

For D_z=I+(z-1)e_ve_v^*, the entry of D_zP starting at v is
multiplied by z. A cyclic word has one departing edge at each of
its recorded positions, so

$$
\operatorname{Tr}(D_zP)^n
=\sum_x\prod_jP_{x_jx_{j+1}}\,
 z^{\#\{j:x_j=v\}}.
$$

This identity counts rooted cyclic words, including periodic words
with their actual trace multiplicity. No stationary-chain probability
law is substituted for this closed-path sum.

Put eta=z-1 and
R_v(lambda)=sum_{k>=1}lambda^{-k}(A^k)_vv. For |lambda|>=3/4
the direct geometric calculations yield

$$
|R_v|\le \frac{4C}{3N}+\frac{16(C-1)}{3N}
\le\frac{20C}{3N},
$$

$$
|R_v'|\le\frac{16C}{9N}+\frac{256(C-1)}{9N}
\le\frac{31C}{N}.
$$

The coefficient 256/9 comes from
sum_{k>=2}k 2^{-(k-2)}(4/3)^{k+1}; it has been independently
summed. The estimates are uniform in v.

The determinant identity is also exact. For lambda outside the
spectrum of P, the rank-one determinant multiplier for
D_zP=P+eta e_ve_v^*P is

$$
1-\eta e_v^*P(\lambda I-P)^{-1}e_v
=1-\frac\eta{N(\lambda-1)}-\eta R_v(\lambda).
$$

Multiplying by
det(lambda I-P)=(lambda-1)det_{1^perp}(lambda I-A)
gives source (2.8), and analytic continuation removes the apparent
singularity at lambda=1. On |lambda|>=3/4 the determinant factor
on 1^perp is nonzero because ||A||<=1/2.

For |z|<=2, |eta|<=3. If N>=80C then |eta R_v|<=1/4.
Every zero outside the disk of radius 3/4 must consequently satisfy

$$
\lambda=1+\frac\eta{N(1-\eta R_v(\lambda))},
\qquad |\lambda-1|\le4/N.
$$

The right side maps the closed radius-6/N disk around one into
its radius-4/N subdisk. Once N is sufficiently large this disk
lies in |lambda|>=3/4. Its derivative is bounded by

$$
\frac{9\cdot31C}{N^2}(4/3)^2
=\frac{496C}{N^2}<1/2.
$$

The derivative bound implies a Lipschitz bound on this convex complex
disk, so the elementary contraction theorem gives a unique fixed point.
Conversely that fixed point is a determinant zero. At it, the derivative
of the bracket in source (2.8) is
(1-eta R_v)(1-F'(lambda)), where F is the fixed-point map;
it is nonzero. Hence there is exactly one algebraically simple
eigenvalue outside radius 3/4, and all others have modulus at most 3/4.

The explicit estimates in source (2.10) are correct:

$$
|\lambda-1-\eta/N|\le80C/N^2,
\qquad |\log\lambda-\eta/N|\le96C/N^2
$$

for all sufficiently large N. The second follows from |lambda-1|<=4/N
and the Taylor remainder for log(1+w). Raising to n<=BN gives a
uniform O_{B,C}(1/N) error against exp((n/N)eta). The other eigenvalue
powers contribute at most N(3/4)^n. The trace-of-powers identity used
here holds for algebraic eigenvalues with multiplicity, even when the
matrix is not diagonalizable.

On cN<=n<=BN that exponential residual is O_{c,B}(1/N). Thus
the generating-function estimate (2.5), uniform on the complete
complex disk |z|<=2, is proved. Cauchy's coefficient formula on
the circle |z|=2 yields source (2.11) for each fixed visit count m.
This argument verifies uniformity in the vertex v, the scaled time,
and the complex variable used to extract the coefficient.

## 3. The weighted mean of good vertices

Summing the m=3 coefficient over v gives
N exp(-s)s^3/6+O(1). The two exclusions defining good vertices
each cost O(1) in this weighted count.

For a gap ell=1 or 2 between repeated visits to v, fixing its first
cyclic position gives weight
(P^ell)_vv(P^{n-ell})_vv. Every positive power of P has entries
at most C/N: multiply on the left by a stochastic matrix.
For n>2, summing over positions, v, and ell gives at most
2C^2 n/N<=2C^2 B. Exact-three-visit restrictions can be removed
when making this nonnegative upper bound.

For a fixed set of three visit positions with all gaps at least
three, the six predecessor/successor positions are distinct as
formal positions. Their marginal weight is a product of three
factors P_vb (P^{ell-2})_ba P_av. Bounding the middle three entries
by C/N leaves six independent row or column probability factors,
each with maximal atom C/N. Any pair equality then has mass at
most C/N, and the 15-pair union bound costs 15C^4/N^4 for this
fixed v and position set. There are at most N n^3/6 such choices,
so the total cost is at most (5/2)C^4 B^3.

These arguments can overcount bad words and allow additional visits;
both changes increase the upper bounds. They prove exactly

$$
G_n:=\sum_x |a(x)|^2 g(x)
=N e^{-s}s^3/6+O_{c,B,C}(1).
$$

There is no assumption of independence between the good-vertex
indicators and no need to estimate their variance.

## 4. Directed last exits and the stack algorithm

Every edge occurrence in the original rooted word may temporarily
be labelled by its position. For each visited nonroot vertex v,
select its last chronological departure. If this selected edge ends
at w different from the root, then the tour departs w at a strictly
later time. The selected departure time at w is therefore larger.
This excludes all cycles of selected edges. A finite forward chain
of them must end at the root, the only vertex without a selected
edge. The selected edges form a directed tree toward the root,
with exactly one outgoing edge at each other visited vertex.

Retain each selected edge as the last item in its outgoing list
and vary the preceding order. The walk that uses each next unused
edge cannot stop at a nonroot vertex: a trail currently ending there
has used one more incoming than outgoing edge, contradicting balanced
total degrees if all outgoing edges were exhausted.

If the walk stops at the root, its used trail is closed, so unused
incoming and outgoing degrees agree at every vertex. If any unused
edge remains at a nonroot v, the last-list edge selected at v is
unused, because only a prefix of the list has been used. Following
that unused selected edge reaches another vertex with unused incoming
and hence unused outgoing degree. The directed tree propagates this
property to the root, contradicting exhaustion there. Thus all edge
occurrences are consumed, and the result is a complete rooted Euler
tour with the same directed edge multiplicities.

The proof handles loops and parallel edges; labelling occurrences
was only a device to make the outgoing lists unambiguous.

## 5. Injectivity as unlabelled vertex words and Jensen's inequality

At each good vertex different from the root there are three outgoing
occurrences with distinct successor labels. Retain the selected last
one and choose either order for the first two. Independent choices
at all these vertices give complete tours by Section 4.

The output vertex word records, in chronological order, all successor
labels at every vertex. Therefore it recovers the binary choice at
each such good vertex. Distinct choices cannot collapse to the same
unlabelled rooted word, even if other vertices have parallel edges.
There are at least 2^{g(x)-1_{root good}}>=2^{g(x)-1} distinct outputs.
The weaker right side remains legitimate when g(x)=0.

For scalar matrix entries, equal directed edge multiplicities imply
exact equality of the two amplitude products; ordering the scalar
factors cannot change the product. Thus every pair counted in the
same edge-count class has weight |a(x)|^2, not merely the same
absolute weight. Summing the constructed subset proves

$$
\mathcal F_{n,N}\ge\tfrac12\sum_x|a(x)|^2 2^{g(x)}
\ge\frac{T_n}{2}\exp\left((\log2)G_n/T_n\right).
$$

The second inequality is ordinary Jensen for the normalized weights
|a(x)|^2/T_n; T_n>0 for large N by the already proved trace estimate.
Since T_n=1+O_C(2^{-n}) and G_n=N exp(-s)s^3/6+O(1), this gives
the exponential bound in source (1.5), uniformly on c<=s<=B.

## 6. Signed complement, rotations and scope

The decomposition into equal and different directed edge counts
partitions all ordered rooted pairs exactly. Both classes are
invariant under exchanging the two words, so their sums are real.
Unitarity gives |Tr U^n|^2<=N^2. Subtracting the positive lower
bound for F yields source (1.6), a genuinely negative upper bound
of exponential magnitude once N is large.

For each original word, forward and reverse rotation classes
together have at most 2n distinct rooted members. Their intersection
with its equal-edge-count class contributes at most 2n|a(x)|^2.
This proves (1.7) without assuming primitive words and without
assigning an amplitude phase to reversed paths that have different
edge counts.

The additional bound on R in Section 6 is correct. For
S_uv=sqrt(P_uv P_vu), S is symmetric substochastic and has entries
at most C/N. Therefore every S^n also has entries at most C/N,
so Tr S^n<=C. The absolute reversed-rotation sum is bounded by
n Tr S^n<=nC, whether or not some rotations coincide. Since the
forward class D is nonnegative, W=Z-C obeys

$$
\mathcal W_{n,N}\le N^2+nC-\mathcal C_{n,N}.
$$

This proves exponential positive and negative subclasses within Z.
It does not determine their small signed residue. In particular,
the source explicitly leaves its weighted assertion (6.2) unproved;
the notation b_* there belongs to the separately selected test and
is not an input to any theorem proved in this source.

The implication to the exact original U_N uses only (1.1), previously
established along all sufficiently large odd N with fixed C=9 and
fixed tau. There is no dimension average or replacement ensemble.

## 7. Independent finite combinatorial check

The self-contained companion dual_audit_exponential_edge_checks.py,
SHA256 951a42c00340c80260083d8a6e244bd90148629263e382c2e226d414fc0372af,
enumerates all 9,828 words of lengths 3,...,8 over three symbols.
At each nonroot vertex with exactly three distinct successor labels
it performs all binary choices permitted by the last-exit rule.
The weaker eligibility condition is enough for the combinatorial
proof; the stronger good-vertex condition is used only in the
analytic weighted-mean estimate.

The script verified 11,232 complete, distinct rooted output tours,
including 1,260 original words with a nontrivial binary choice.
Every selected last-exit graph was a rooted tree; every constructed
walk consumed each edge occurrence once; all output directed edge
counts agreed with the original counts; different binary choices
gave different vertex words. These exact checks are corroboration,
not a substitute for Sections 4--5's proof.
