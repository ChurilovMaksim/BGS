> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round5_2026_10_21/audit_exponential_coherent_edge_classes.md`. Embedded SHA256: `effadaa4e2b66189a077f65cc6a50019781024d020c0ffd46d2197511b21dbbf`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit: exponential coherent edge classes

Round 5, 21 October 2026. Auditor: /root/audit_uniform_word_r4.

## 1. Frozen target and verdict

I read the complete source root_exponential_coherent_edge_classes.md and
independently verified its SHA-256:

001fd27ca128f1a00417838e0f4b07d7ad19f291e8c2c5fbb593e614d2ec29e0.

No target file was modified. I reconstructed the rank-one generating
function, the good-vertex loss estimates, the last-exit tree argument, and
the injectivity into unlabelled rooted vertex words.

**Verdict.** Under (1.1), the exponential lower bound (1.5), the forced
negative complement (1.6), and the corresponding conclusion after removal
of forward and reversed rotation classes are proved as stated. The
independently audited physical kernel and oscillatory matrix argument
verify (1.1) with $C=9$ for the original fixed-kick family along all odd
dimensions. No gap was found in this structural theorem.

The proof does not evaluate the small residual after cancellation, does not
establish a local spectral limit, and does not construct a countersequence
for $H_{\rm diag}$. In particular the full remaining phase sum cannot be
bounded below by the positive subclass.

## 2. Resolvent bounds, determinant identity, and coefficient extraction

Put $A=P-J$. Exact double stochasticity gives $AJ=JA=0$, so
$P^k=J+A^k$. The row and column estimates
$$
\sum_y(P_{vy}-1/N)^2
=\sum_yP_{vy}^2-1/N\le(C-1)/N
$$
and their column counterparts are correct. Consequently
$$
|(A^k)_{vv}|\le(C-1)N^{-1}2^{-(k-2)},\quad k\ge2,
$$
by placing $A^{k-2}$ between a row and a column of $A$. Normality is not
needed. Likewise
$$
|\operatorname{Tr}A^n|
\le\|A\|_{\rm HS}^2\|A\|_{\rm op}^{n-2}
\le(C-1)2^{-(n-2)},\quad n\ge2.
$$
Thus $T_n=\operatorname{Tr}P^n=1+O_C(2^{-(n-2)})$, with no extra factor $N$.

For
$$
R_v(\lambda)=\sum_{k\ge1}(A^k)_{vv}\lambda^{-k},
$$
the series is analytic on $|\lambda|>1/2$. At $|\lambda|\ge3/4$, its
first term contributes at most $4C/(3N)$, and the remaining geometric sum
at most $16(C-1)/(3N)$. For the derivative, the respective bounds are
$$
\frac{16C}{9N},\qquad \frac{256(C-1)}{9N}.
$$
These imply precisely
$$
|R_v|\le20C/(3N),\qquad |R_v'|\le31C/N.
$$

The diagonal tilt counts visits at the departing vertex of every cyclic
edge. Hence
$$
G_{v,n}(z)=\operatorname{Tr}[(I+(z-1)E_v)P]^n
=\sum_x w(x)z^{\#\{j:x_j=v\}}
$$
is the exact visit polynomial for the rooted closed-path weights
$w(x)=|a(x)|^2$.

Write $\eta=z-1$. The rank-one determinant multiplier is
$$
1-\eta e_v^*P(\lambda I-P)^{-1}e_v
=1-\frac{\eta}{N(\lambda-1)}-\eta R_v(\lambda).
$$
Its sign follows from $\lambda I-D_zP=\lambda I-P-\eta e_ve_v^*P$.
Multiplication by the characteristic polynomial of $P$ gives
$$
\det(\lambda I-D_zP)
=\det_{\boldsymbol1^\perp}(\lambda I-A)
\left[(\lambda-1)(1-\eta R_v(\lambda))-\frac{\eta}{N}\right].
$$
In particular the prefactor has dimension $N-1$, not $N$; no extra zero
eigenvalue or missing factor $\lambda$ has entered the formula. Apparent
poles at $\lambda=1$ cancel. The derivation initially holds outside the
spectra and then throughout the region in question by analyticity.

For $|z|\le2$, $|\eta|\le3$. If $N\ge80C$, then
$|\eta R_v|\le1/4$ on $|\lambda|\ge3/4$. Every characteristic root in
that region is a fixed point of
$$
F(\lambda)=1+\frac{\eta}{N(1-\eta R_v(\lambda))}
$$
and satisfies $|\lambda-1|\le4/N$. For large $N$, $F$ maps the closed
disk $|\lambda-1|\le6/N$ strictly inside itself. Its derivative is bounded by
$$
\frac{|\eta|^2}{N}\frac{|R_v'|}{|1-\eta R_v|^2}
\le496C/N^2.
$$
The disk lies within $|\lambda|\ge3/4$; integration of this derivative on
line segments gives a genuine contraction of the complex disk. There is
exactly one fixed point. It is a simple characteristic root: the scalar
bracket equals $(1-\eta R_v)(\lambda-F(\lambda))$, whose derivative at
the fixed point is nonzero. The remaining $N-1$ roots have modulus at
most $3/4$.

The expansion error of this fixed point is at most $80C/N^2$:
$$
\left|\lambda-1-\frac{\eta}{N}\right|
\le\frac{|\eta|}{N}\frac{|\eta R_v|}{|1-\eta R_v|}
\le80C/N^2.
$$
The logarithm expansion adds at most $16/N^2$ for sufficiently large $N$,
so the claimed bound $96C/N^2$ is valid. Taking $n\le BN$ powers gives
$$
\lambda(z)^n=e^{(n/N)(z-1)}+O_{B,C}(N^{-1})
$$
uniformly on the full disk. The trace is the sum of eigenvalue powers, even
when the matrix is not diagonalizable; the other eigenvalues contribute at
most $N(3/4)^n$. For $n\ge cN$, this is absorbed into $O_{c,C}(N^{-1})$.

Cauchy's coefficient formula on $|z|=2$ is therefore applicable to the
difference of the exact visit polynomial and $e^{s(z-1)}$. It gives,
uniformly over vertices and $c\le s=n/N\le B$,
$$
\sum_{x:\,\#\{j:x_j=v\}=m}w(x)
=e^{-s}s^m/m!+O_{c,B,C,m}(N^{-1}).
$$
No stationary-chain probability measure, independence approximation, or
unproved Poisson law is used.

## 3. Counting good vertices without hidden correlations

For $m=3$, summing the preceding coefficient over the $N$ possible hubs
gives $Ne^{-s}s^3/6+O(1)$. The additional exclusions have bounded total
weighted cost.

First, every entry of every $P^k$, $k\ge1$, is at most $C/N$, because
its entries are convex combinations of entries of $P$. For a pair of
cyclic positions separated by $\ell=1,2$, the exact weight with both labels
equal to $v$ is
$$
(P^\ell)_{vv}(P^{n-\ell})_{vv}.
$$
Any excluded hub with exactly three visits and a short gap satisfies at
least one such condition. Summing over all positions, both gap lengths,
and all vertices gives at most $2C^2n/N\le2C^2B$. Multiple counting only
enlarges this nonnegative bound.

Next fix an unordered triple of positions with all cyclic gaps at least
three. Their six neighboring positions are distinct as positions, including
when a gap is exactly three. For a fixed hub, after summation over all
interior labels, the weight has the product form
$$
\prod_{j=1}^3
P_{v b_j}(P^{\ell_j-2})_{b_j a_{j+1}}P_{a_{j+1}v}.
$$
All three middle powers have positive exponent and hence are at most $C/N$.
The six remaining factors are three row distributions and three column
distributions, each of total mass one and maximum atom $C/N$. Their product
distribution gives any specified pair-equality probability at most $C/N$.
The 15-pair union bound therefore yields $15C^4/N^4$ for this fixed hub and
position set. Summing over $N$ hubs and at most $n^3/6$ position sets
gives $(5/2)C^4B^3$.

Allowing additional visits in these upper bounds only enlarges the lost
weight. Thus the weighted mean of the good-vertex count is indeed
$$
G_n=\sum_xw(x)g(x)=Ne^{-s}s^3/6+O_{c,B,C}(1).
$$

## 4. The last-exit tree and completion of the greedy tour

This is the principal combinatorial point. Fix one rooted cyclic vertex
word, temporarily label each edge occurrence by its original time, and put
$r=x_0$. Every visited vertex has balanced incoming and outgoing degree.

For each $v\ne r$, select its last departure edge in the original tour.
If that edge ends at $w\ne r$, the last departure time of $w$ is strictly
larger than that of $v$: the walk departs $w$ at the next time, which is
strictly before the final return to $r$. Hence selected edges contain no
directed cycle. Every finite chain of them terminates at $r$, the only
visited vertex without a selected outgoing edge.

Fix each selected edge last in its vertex's outgoing list. Arbitrarily
order the preceding edge occurrences and choose a root list. Follow the
next unused item in the current vertex's list, starting at $r$.

The walk cannot stop away from $r$: at its current nonroot endpoint, used
incoming degree exceeds used outgoing degree by one, so exhaustion of the
outgoing list would exceed the total incoming degree, contrary to balance.
If it stops at $r$, its used trail is closed and used degrees agree at
every vertex. If unused edges remained at a nonroot vertex, its selected
last edge would still be unused, since the algorithm consumes each list
in order. Its endpoint would have unused incoming degree and therefore
unused outgoing degree. Following the selected tree propagates this
property to $r$, contradicting exhaustion of the root list. All edges
must therefore be used, and the result is a rooted Euler tour.

This proof treats directed parallel edges correctly; it does not assume
the multigraph is simple.

## 5. Injectivity after erasing the artificial edge labels

At each good nonroot vertex there are exactly three outgoing occurrences
with distinct successor labels. Preserve its selected last edge and choose
either order for its other two outgoing edges. Keep every other list fixed.
The choices at different good vertices are independent choices of lists,
and the previous section proves that every joint choice produces a valid
full tour.

Distinct choices produce distinct unlabelled rooted vertex words. Such a
word records the chronological successor list at each vertex. At a good
vertex the three recorded successor labels are distinct, so its two choices
cannot give the same list. If two binary vectors differ at that vertex,
their resulting words must differ. Parallel edges at other vertices cannot
remove this discrepancy. This is stronger than injectivity only among the
temporarily labelled tours.

The root is conservatively left unchanged. Therefore each original $x$
has at least
$$
2^{g(x)-1_{\{r\ {\rm good}\}}}\ge2^{g(x)-1}
$$
distinct rooted partners with exactly the same directed edge counts. The
case $g(x)=0$ causes no problem: the original word supplies one partner,
which exceeds the fractional lower bound $1/2$.

No global injectivity across different first words $x$ is needed in the
ordered-pair sum, since its first coordinate already distinguishes those
pairs. Identical directed edge counts imply identical complex amplitudes
by commutativity of scalar multiplication, including paths with zero
amplitude. Every counted pair therefore contributes precisely $w(x)\ge0$.
This proves
$$
\mathcal F_{n,N}\ge\frac12\sum_xw(x)2^{g(x)}.
$$

## 6. Jensen, scale, and exclusions

The exact total weight is $T_n=\sum_xw(x)>0$ for large $N$.
Normalizing these weights and applying convexity gives
$$
\mathcal F_{n,N}\ge
\frac{T_n}{2}\exp\!\left((\log2)\frac{G_n}{T_n}\right).
$$
Only the first weighted moment of $g$ is used; independence or concentration
of the good-vertex indicators is not required. Since
$T_n=1+O_C(2^{-cN+2})$ and $G_n=Ne^{-s}s^3/6+O(1)$, division by $T_n$
changes the exponent by $O(1)$, uniformly on $[c,B]$. This proves (1.5).

The partition by equal versus unequal edge-count matrices is exact and
invariant under exchanging the two words. Its two sums are real, and
$$
|\operatorname{Tr}U_N^n|^2=\mathcal F_{n,N}+\mathcal G_{n,N}.
$$
Unitarity bounds the left side by $N^2$, proving the stated upper bound for
the unequal-edge-count complement. Since $e^{-s}s^3$ has a strictly positive
minimum on $[c,B]$, the negativity and exponential magnitude follow
uniformly for sufficiently large $N$.

For each $x$, its forward and reverse rotation classes together contain
at most $2n$ distinct rooted words. Among those with equal edge counts,
each summand is $w(x)$. Removing them therefore loses at most $2nT_n$,
regardless of periodicities or overlap of the classes. This proves (1.7);
an $O(N)$ loss leaves the exponential lower bound unchanged up to an
additive constant in its exponent.

For the last negative-complement assertion one needs only the elementary
bound on the reversed class. The symmetric matrix
$S_{xy}=\sqrt{P_{xy}P_{yx}}$ has row sums at most one, maximum entry $C/N$,
and the same properties for its positive powers. Hence
$\operatorname{Tr}S^n\le C$. There are at most $n$ reversed rooted
partners per first word, so the absolute reverse-class sum is at most
$n\operatorname{Tr}S^n\le nC$. Forward contributions are nonnegative.
The identity
$$
|\operatorname{Tr}U_N^n|^2=D_{n,N}+R_{n,N}+\mathcal C_{n,N}+\mathcal W_{n,N}
$$
therefore gives exactly
$\mathcal W_{n,N}\le N^2+nC-\mathcal C_{n,N}$.

## 7. Scope of the result

The stronger all-time $D/R$ estimates quoted in the target's final
paragraph come from its separate physical-cycle source; they are not needed
for this exponential theorem. The definitions of those disjoint classes
agree with the exclusions used here. The displayed fixed-test $Z$ limit
remains explicitly unproved.

This result shows, for the actual original matrices, why a sum of absolute
values or a positive coherent subclass cannot establish the required
spectral estimate. The cancellation already has exponential size at
$n\asymp N$. The desired spectral statistic concerns the polynomial-scale
residue of that cancellation and all higher factorial moments, which this
argument does not determine.
