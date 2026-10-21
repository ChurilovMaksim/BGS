> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round5_2026_10_21/audit_macroscopic_trigram_coverage_barrier.md`. Embedded SHA256: `21d592609bd5a222b00028fa531ad0a9724e3e808216a982b864a87076eb39f4`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/histories.md).

# Independent audit: macroscopic trigram coverage barrier

Date: 21 October 2026. Auditor: /root/audit_uniform_word_r4.

Frozen target:
arithmetic_macroscopic_trigram_coverage_barrier.md.

Target SHA256:
828b12a6b933e2f541b2296d240555d8caceac407442f27397f050f2bf0928c7.

The hash was independently recomputed and Sections 1--7 were read in
full. The local-pairing count, positive-mass extraction, Euler-tour
construction and all uniformity statements were independently
reconstructed. No earlier audit status was used as proof, and the
frozen source was not modified.

## Verdict

The stated theorem is proved. From the two hypotheses
$$
P_{uv}=|U_{uv}|^2\le C/N,\qquad
\|P-J_N\|_{\rm op}\le\tfrac12,
$$
the proof gives, for any fixed $0<c\le B$ and any positive integer
sequence $q_N=o(N)$,
$$
\mathcal F^{>q_N}_{n,N}
\ge\frac{\alpha}{16}\,2^{\alpha N/2},
\qquad
\alpha=\frac{e^{-B}c^3}{6},
$$
uniformly for $cN\le n\le BN$, for all sufficiently large $N$.
The lower bound is for actual rooted pairs, with no marking or edge
labelling multiplicity. A subset realizing it lies outside forward
and reversed rotation classes.

The original-family application uses the same already audited
physical-kernel and oscillation inputs as the long-arc resummation
theorems, with $C=9$ for every sufficiently large odd $N$.
The new argument is finite dimensional and leaves the original
matrix, its phases and its fixed $\tau$ unchanged.

No substantial gap or constant correction was found. The final
conclusion is a coverage obstruction for directed long-arc
rearrangements. It is not a lower bound on the full signed trace
statistic and is not a counterexample to $H_{\rm diag}$.

## 1. Weighted path estimates

Write $A=P-J_N$. Double stochasticity gives $AJ_N=J_NA=0$.
For either a row or column,
$$
\sum_u|A_{vu}|^2
=\sum_uP_{vu}^2-1/N\le(C-1)/N.
$$
Consequently, for $k\ge2$,
$$
|(A^k)_{vv}|
\le\frac{C-1}{N}2^{-(k-2)}.
$$
Also $\|A\|_{\rm HS}^2\le C-1$, so for $n\ge2$,
$$
|\operatorname{Tr}A^n|
\le\|A\|_{\rm HS}^2\|A\|^{n-2}
\le(C-1)2^{-(n-2)}.
$$
This uses the Hilbert--Schmidt trace inequality and does not require
normality. Thus the total nonnegative closed-path weight is
$$
T_n=\sum_xw(x)=\operatorname{Tr}P^n=1+O_C(2^{-(n-2)}).
$$

For completeness, the visit generating function is exact:
$$
G_{v,n}(z)=\operatorname{Tr}(D_zP)^n
=\sum_xw(x)z^{d_v(x)},\qquad
D_z=I+(z-1)E_v.
$$
Set $\eta=z-1$ and
$$
R_v(\lambda)=\sum_{k\ge1}\lambda^{-k}(A^k)_{vv}.
$$
The preceding diagonal estimates, including
$|A_{vv}|\le C/N$, give
$$
R_v(\lambda)=O_C(N^{-1}),\qquad
R_v'(\lambda)=O_C(N^{-1})
$$
uniformly for $|\lambda|\ge3/4$. Summing the geometric series
and its derivative proves these bounds directly.

The rank-one determinant identity gives
$$
\det(\lambda I-D_zP)
=\det_{{\bf1}^{\perp}}(\lambda I-A)
\left[(\lambda-1)(1-\eta R_v(\lambda))-\eta/N\right].
$$
The resolvent scalar used here is exactly
$$
e_v^*P(\lambda I-P)^{-1}e_v
=\frac1{N(\lambda-1)}+R_v(\lambda).
$$
The pole at one cancels after multiplication, so the determinant
identity extends to that point.

For $|z|\le2$, $|\eta|\le3$. For large $N$,
$|\eta R_v|\le1/4$ outside $3/4$. Every eigenvalue in that
region must therefore satisfy
$$
\lambda=1+\frac{\eta}{N(1-\eta R_v(\lambda))},
\qquad |\lambda-1|\le4/N.
$$
The right side maps the closed disk of radius $6/N$ about one
inside itself and has derivative $O_C(N^{-2})$. The contraction
argument gives a unique fixed point. The zero is simple, since
the derivative of $\lambda$ minus this map is
$1+O_C(N^{-2})$. The perpendicular determinant has no zero
outside radius $1/2$, so this is the only eigenvalue outside
radius $3/4$.

Its expansion and power are
$$
\lambda_v(z)=1+\eta/N+O_C(N^{-2}),\qquad
\lambda_v(z)^n=e^{(n/N)(z-1)}+O_{B,C}(N^{-1})
$$
uniformly for $n\le BN$. The other $N-1$ eigenvalues contribute
at most $N(3/4)^n$ to the trace, even if the matrix is not
diagonalizable. Hence
$$
G_{v,n}(z)
=e^{(n/N)(z-1)}
 +O_{B,C}(N^{-1})+O(N(3/4)^n).
$$
The logarithm used for the distinguished eigenvalue is its
single branch near one; its error is uniform on $|z|\le2$.

Taking $z=2$, or extracting the coefficient of $z^3$ by
Cauchy's integral formula on $|z|=2$, gives respectively
$$
\sum_xw(x)\sum_v2^{d_v(x)}\le2e^B N
$$
for large $N$ in the specified time interval, and
$$
\sum_xw(x)\#\{v:d_v(x)=3\}
=N e^{-s}s^3/6+O_{c,B,C}(1),\qquad s=n/N.
$$
The exponentially small $N^2(3/4)^n$ term is uniform on
$cN\le n\le BN$. These are weighted closed-path identities,
not assumptions of independent path coordinates.

## 2. Good vertices and repeated-edge control

A good vertex has exactly three incoming and three outgoing
edge occurrences, with six pairwise distinct neighbor labels.
This property depends only on the full directed edge-count
array: the three incoming edge multiplicities and the three
outgoing edge multiplicities are one, and the two neighbor
sets are disjoint. It does not depend on how incoming and
outgoing edges are paired into trigrams.

The weighted loss due to a pair of visits at cyclic distance
one or two is at most
$$
n\sum_{\ell=1}^2\sum_v
(P^\ell)_{vv}(P^{n-\ell})_{vv}
\le2C^2n/N\le2C^2B.
$$
Here every positive power of $P$ has entries at most $C/N$,
by multiplying on the left by a stochastic matrix.

For a fixed vertex and three marked visits with all gaps at
least three, summation of the internal pieces leaves three
middle transition factors and six neighbor factors. Bound
the middle factors by $(C/N)^3$. The other factors are
three row distributions and three column distributions.
For any two of the six dummy coordinates the equality
probability is at most $C/N$, regardless of which row or
column distributions are used. The union over fifteen
pairs costs at most $15C/N$. The weight is therefore at
most $15C^4/N^4$ for fixed vertex and visit positions.

There are at most $N\binom n3\le Nn^3/6$ choices. Thus
the total additional loss is at most
$(5/2)C^4B^3$. Allowing extra visits in these bounds only
increases the nonnegative weight. It follows that
$$
\sum_xw(x)g(x)
=N e^{-s}s^3/6+O_{c,B,C}(1).
$$
Loops or a gap of two cannot occur at a good vertex,
because they put a label in both neighbor sets.

For repeated directed edges define
$$
\mathcal J(x)=\sum_{u,v}\binom{L_{uv}(x)}2.
$$
If positions zero and $r$, with $2\le r\le n-2$, carry
the same directed edge $u\to v$, their summed weight is
$$
S_r=\sum_{u,v}P_{uv}^2
(P^{r-1})_{vu}(P^{n-r-1})_{vu}
\le C^3/N^2.
$$
Indeed each connecting power is bounded by $C/N$ and
$\sum_{u,v}P_{uv}^2\le C$. For $r=1$, edge equality
forces $x_0=x_1=x_2=u$, yielding
$$
S_1=\sum_uP_{uu}^2(P^{n-2})_{uu}\le C^3/N^2.
$$
The distance $n-1$ is identical by cyclic symmetry.
All powers are positive for the relevant large $N$,
where $n\ge3$. Each unordered pair of positions is
counted twice by a starting position and nonzero cyclic
distance, so
$$
\sum_xw(x)\mathcal J(x)
=\frac n2\sum_{r=1}^{n-1}S_r
\le C^3B^2/2.
$$
The loop cases and overlapping adjacent edges are thus
explicitly included.

## 3. Uniform positive mass of suitable words

Let
$$
\alpha=e^{-B}c^3/6,\qquad
K_0=\max\{e^2,32e^B/\alpha\}.
$$
The audit writes $K_0$ for the target's constant $K$
to distinguish it from substring lengths in other notes.
Consider words satisfying
$$
g(x)\ge\alpha N/2,\qquad
\sum_v2^{d_v(x)}\le K_0N,\qquad
\mathcal J(x)\le\log N.
$$

Since $e^{-s}s^3/6\ge\alpha$ for $c\le s\le B$,
the first-moment estimate and $g(x)\le N$ give
$$
\sum_{\{g\ge\alpha N/2\}}w(x)
\ge\frac1N\sum_xw(x)g(x)-\frac\alpha2T_n
\ge\alpha/2-o(1)\ge3\alpha/8.
$$
The exponential-visit-budget failure has mass at most
$2e^B/K_0\le\alpha/16$. The repeated-edge-budget failure
has mass at most
$$
\frac{C^3B^2}{2\log N}\le\alpha/16
$$
for large $N$. Subtracting the two losses gives
$$
\sum_{x\in\mathcal A_{n,N}}w(x)\ge\alpha/4.
$$
Every defining condition of $\mathcal A_{n,N}$ depends
only on $L(x)$, so it is shared by all coherent partners.
The threshold may be large, but all constants and the
dependence on fixed $c,B,C$ are legitimate.

## 4. Local-pairing count for actual rooted words

Fix $x$, and distinguish all occurrences of every edge
$u\to v$ by separate labels. An Euler tour gives at each
vertex a bijection from its incoming edge occurrences to
its outgoing edge occurrences, pairing an incoming edge
with its successor in the tour.

For a prescribed centered trigram table $t_{uz}$ at
vertex $v$, its row and column sums are $m_{uv}$ and
$m_{vz}$, where $m_{uv}=L_{uv}(x)$. The exact number
of such local bijections is
$$
\frac{\prod_u m_{uv}!\prod_zm_{vz}!}
     {\prod_{u,z}t_{uz}!}.
$$
For each incoming group $u$, divide its labelled
occurrences among outgoing-neighbor groups of sizes
$t_{uz}$; then for each $z$, biject the assigned
incoming occurrences to the labelled outgoing edges
to $z$. This proves the formula directly, including
loops and parallel edges.

Now fix a set $S$ of vertex labels outside which the
trigram arrays must equal those of $x$. Outside $S$,
use this formula and discard the denominator. Inside
$S$, use the unrestricted count $d_v!$. The resulting
local bijections define a permutation of all labelled
edges. Retaining systems with multiple cycles only
increases an upper bound. A rooted single-cycle tour
also specifies one initial labelled edge, with at
most $n$ possibilities.

It follows that the number of actual rooted vertex
words meeting these conditions is at most
$$
n\left(\prod_{u,v}m_{uv}!^2\right)\prod_{v\in S}d_v!.
$$
Including the factorial numerator at vertices in $S$
in the displayed full product only enlarges the bound.

There is no hidden division by period or artificial
edge labels. Each actual rooted word can be labelled
canonically, using the fixed list of labels for each
directed edge in order of its visits from position zero.
Its local-bijection system together with its initial
labelled edge reconstructs the entire rooted vertex
word uniquely. Thus actual words inject into the
systems counted above; overcounting inadmissible
systems is harmless.

Since $j\le2^{j-1}$ for integers $j\ge1$,
$$
m!\le2^{\binom m2},\qquad
\prod_{u,v}m_{uv}!^2\le4^{\mathcal J(x)}.
$$
For $x\in\mathcal A_{n,N}$, this factor is polynomial
in $N$, because $\mathcal J(x)\le\log N$.

## 5. A uniform subexponential bound on sublinear support

For $r=|S|\ge1$, put $y_v=2^{d_v}\ge1$. The function
$$
f(t)=[\log(et)]^2
$$
is increasing and concave for $t\ge1$, since
$f''(t)=-2\log t/t^2\le0$. Also $\log(d!)\le d^2$
for all nonnegative integers $d$. Jensen's inequality
and $\sum_vy_v\le K_0N$ therefore imply
$$
\sum_{v\in S}\log(d_v!)
\le\frac{r}{(\log2)^2}
\left[\log\left(\frac{eK_0N}{r}\right)\right]^2.
$$
This bounds all subsets $S$ of a given size at once.
It is stronger for this purpose than bounding only the
largest degree.

For $r\le N$, the right side increases with $r$.
Indeed, writing $L_r=\log(eK_0N/r)\ge3$, the derivative
of $rL_r^2$ is $L_r(L_r-2)>0$. For $q\le N/2$,
$$
\sum_{r=0}^q\binom Nr
\le(q+1)\binom Nq\le(q+1)(eN/q)^q.
$$
Combining this with Section 4 gives
$$
\mathcal N_x(q)
\le n\,4^{\mathcal J(x)}(q+1)(eN/q)^q
\exp\left\{
\frac{q}{(\log2)^2}
\left[\log\left(\frac{eK_0N}{q}\right)\right]^2
\right\}.
$$
The empty supporting set is also covered.

For $q_N=o(N)$, eventually $1\le q_N\le N/2$.
Uniformly for $x\in\mathcal A_{n,N}$ and $n\le BN$,
the logarithm of the last bound is
$$
O_B(\log N)+\log(q_N+1)
+q_N\log(eN/q_N)
+\frac{q_N}{(\log2)^2}\log^2(eK_0N/q_N)
=o(N).
$$
The final assertion follows from
$t\log^2(1/t)\to0$ as $t\downarrow0$.
This covers bounded $q_N$ as well as arbitrarily
slow sublinear convergence. The threshold can depend
on the sequence, as allowed in the statement.

## 6. Exponential lower count without edge-label multiplicity

Fix $x\in\mathcal A_{n,N}$ with root $r=x_0$. At every
visited nonroot vertex, select the edge of its last
departure during the rooted tour. These selected edges
form a directed tree toward $r$: if such an edge
ends at another nonroot vertex, the latter has a
strictly later last departure. Hence no selected cycle
can occur, and every selected chain reaches the root.

At each nonroot vertex keep this selected edge last in
its outgoing list. Keep the root list fixed. Following
the next unused outgoing edge produces one closed
tour through all edges. It cannot get stuck away from
the root, by the balance of total incoming and outgoing
degrees. If it closes at the root with some edge unused,
the unused degrees are balanced at every vertex.
An unused outgoing edge at a nonroot vertex forces
its selected last edge to be unused; following the
selected tree then forces an unused outgoing edge
at the root, contradicting that the algorithm stopped.
This also handles vertices not visited before the
premature stopping time.

At each good nonroot vertex the two nonselected
outgoing edges have distinct successor labels.
Independently choose either order for these two.
Keep all other choices fixed. Every resulting list
system yields an Euler tour with the original edge
counts.

Different binary choices give different actual rooted
vertex words, because the word records the order of
its three distinct successor labels at each good
nonroot vertex. Parallel edge labels elsewhere cannot
erase this information. Thus this construction gives
at least
$$
2^{g(x)-1}\ge2^{\alpha N/2-1}
$$
distinct coherent rooted partners.

The subexponential estimate in Section 5 is eventually
at most $2^{\alpha N/2-2}$. Removing all constructed
partners with at most $q_N$ changed trigram centers
therefore leaves at least $2^{\alpha N/2-2}$ partners
for each selected $x$.

Every such pair has exactly equal complex amplitudes,
since it has exactly the same directed edge counts.
It contributes $w(x)\ge0$. Different first rooted
words give different ordered pairs, so summing the
remaining partners and then the mass of
$\mathcal A_{n,N}$ yields
$$
\mathcal F^{>q_N}_{n,N}
\ge\frac{\alpha}{4}\,2^{\alpha N/2-2}
=\frac{\alpha}{16}\,2^{\alpha N/2}.
$$
No absolute-value estimate has replaced a nontrivial
complex phase in this lower bound: the phases agree
exactly.

Forward rotations preserve every centered trigram
array, so none of these pairs can be a forward
rotation. A selected $x$ has a good vertex for
large $N$. For an outgoing neighbor $b$ of such
a vertex $v$, $L_{vb}=1$ while $L_{bv}=0$,
by disjointness of its incoming and outgoing neighbor
sets. Thus $L(x)\ne L(x)^{\mathsf T}$. A reversed
rotation has the transposed edge array, whereas a
coherent partner has the original one. Reversed
rotations are therefore absent as well.

## 7. Coverage consequence and exact limitation

Reordering $r$ directed arcs preserves every trigram
centered at an internal vertex of an arc. Only first
and last vertex labels of arcs can have changed
trigram arrays, so the number of changed centers
is at most $2r$. This argument applies to the
arrays themselves even without equal edge counts;
its restriction to coherent pairs is all that the
theorem needs.

If each arc has at least $L_N$ vertices, then
$$
r\le n/L_N,\qquad
\mathfrak d(x,y)\le2n/L_N\le2BN/L_N.
$$
For any $L_N\to\infty$, the sequence
$$
q_N=\max\{1,\lceil2BN/L_N\rceil\}
$$
is $o(N)$. The lower-bound subclass just constructed
is disjoint from every such rearrangement. This
remains true after union over all numbers of arcs,
all cut positions, all cyclic orders and all roots.
Repeated endpoint labels can only reduce the number
of potentially changed centers.

The result therefore locates exponential positive
coherent mass in the original-family class $Z_n$
which cannot be exhausted by these directed
long-arc operations. It does not preclude negative
contributions from other edge arrays cancelling it.
It also does not apply to operations reversing arc
directions or changing their interiors.

The remaining task is still to control the full
signed interaction of these configurations with
the rest of the pair expansion at the required
polynomial accuracy, and then the higher-order
statistics. The proved positive lower bound supplies
neither a lower bound for the full
$|\operatorname{Tr}U_N^n|^2$ nor an obstruction to
$H_{\rm diag}$ itself.
