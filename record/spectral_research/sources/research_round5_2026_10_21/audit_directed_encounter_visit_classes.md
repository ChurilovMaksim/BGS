> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round5_2026_10_21/audit_directed_encounter_visit_classes.md`. Embedded SHA256: `ee17f5d87f2c91f64508944eb7ed76033d68b8e3ff363cfe70af5b77c195f2df`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/histories.md).

# Independent audit: exact visit counts and directed encounter classes

Round 5, 21 October 2026. Auditor: /root/audit_uniform_word_r4.

## 1. Targets and verdict

I read the entire frozen source dual_directed_encounter_exact_visit_classes.md
and independently verified SHA-256

1ed54e4498189b1f373840bdbff223f7ee2ace54c83c6333bc396a3ce9c6a854.

I also read and ran dual_directed_encounter_exact_checks.py, SHA-256

96702b6c0e25d4c4da0524449a5ee8781189e90825e7f9f5ec1da0623efba84b.

Its 154 rational generating-function checks and 6966 distinct-partner checks
passed. They are supplemental finite checks; the proof audit below covers
the general assertions independently. No frozen source was changed.

**Verdict.** Equations (3)--(8), including the exact partner factor for every
fixed $m\ge3$, the disjointness across hubs and encounter orders, and the
negative-complement bound are proved as stated. The original-family input
is provided by the independently audited four-branch kernel and oscillatory
matrix theorem. No first gap was found in this stated encounter theorem.
The signed residual required for $H_{\rm diag}$ remains unestimated.

## 2. Generating function with its own constants

The exact identity
$$
G_{v,n}(z)=\operatorname{Tr}[(I+(z-1)E_v)P]^n
=\sum_xw(x)z^{K_v(x)}
$$
counts rooted closed words, with one factor of $z$ for each departure
from $v$. No probability normalization is inserted.

Double stochasticity gives $P^k=J+A^k$, $A=P-J$, and both row and column
squared norms of $A$ are at most $(C-1)/N$. Hence
$$
|(A^k)_{vv}|\le(C-1)N^{-1}2^{-(k-2)}\quad(k\ge2),
\qquad |A_{vv}|\le C/N.
$$
For $|\lambda|\ge3/4$, summation yields
$$
|R_v(\lambda)|\le20C/(3N),\qquad
R_v=e_v^*A(\lambda-A)^{-1}e_v.
$$
The rank-one determinant identity has exactly the factor
$$
\det_{\boldsymbol1^\perp}(\lambda-A)
\left[(\lambda-1)(1-(z-1)R_v)-\frac{z-1}{N}\right].
$$
Its restriction is to dimension $N-1$; its scalar signs and constant
projection $1/N$ are correct.

The dual source uses slightly looser constants than the separate exponential
class note; these also check. For $N\ge\max(288,40C)$, every root with
modulus at least $3/4$ lies within $6/N$ of one and is a fixed point of
$$
F(\lambda)=1+\frac{z-1}{N(1-(z-1)R_v(\lambda))}.
$$
The denominator has modulus at least $1/2$. On that disk,
$|\lambda|\ge7/8$, so
$$
|R_v'(\lambda)|\le\frac{1/2}{(|\lambda|-1/2)^2}<4,
\quad |F'|\le144/N\le1/2.
$$
The disk is mapped into itself and is convex and complete; the derivative
bound gives the required contraction on its line segments. The fixed point
is unique and simple, and all other eigenvalues have modulus below $3/4$.
This argument includes $z=0,1$ and does not presume normality.

The fixed-point equation gives the error bound $120C/N^2$ for
$\lambda-1-(z-1)/N$. The power-series logarithm adds at most $36/N^2$.
For $n\le BN$, exponentiation therefore yields precisely the bound
$$
|\lambda(z)^n-e^{(n/N)(z-1)}|
\le e^{3B+1}B(120C+36)/N
$$
once the exponent error is at most one. The other eigenvalues contribute
at most $N(3/4)^n$ to the trace. This proves (3).

Coefficient extraction on the unit circle gives (4). Using that circle
makes the coefficient-error bound independent of the coefficient index
$m$, as asserted. The estimate is meaningful uniformly for all
$1\le n\le BN$ with its displayed transient term; the simplification at
$n\asymp N$ is made only subsequently.

## 3. The $n/m$ factor and both loss estimates

For a fixed hub and marked cyclic visits with positive gap tuple
$(\ell_1,\ldots,\ell_m)$, the exact unrestricted cut weight is
$$
\prod_{i=1}^m(P^{\ell_i})_{vv}.
$$
Each unordered set of marked visits has exactly $m$ choices of initial
cut. For each ordered gap tuple there are $n$ choices of that cut, whose
summed weights agree by cyclic invariance. Thus the conversion factor
$n/m$ is exact even for periodic underlying words.

For a short gap, choose its slot in $m$ ways and its length in two ways.
The remaining positive gap tuples are at most
$n^{m-2}/(m-2)!$. Every $P^\ell$ has maximum entry $C/N$, so summing
the product over hubs is bounded by $C^m/N^{m-1}$. The resulting loss is
$$
\frac{2C^m}{(m-2)!}(n/N)^{m-1}.
$$
An exact-$m$ hub has one marked set of visits; allowing words with further
visits only increases this nonnegative upper bound.

When all gaps are at least three, the $2m$ neighboring positions are
distinct as positions. Bounding each middle power in
$$
\prod_iP_{vb_i}(P^{\ell_i-2})_{b_i a_i}P_{a_iv}
$$
by $C/N$ leaves a product of $2m$ probability distributions, each with
maximum atom $C/N$. Any two coordinates agree with probability at most
$C/N$. The pair union bound, followed by summation over hubs and gap
tuples, gives
$$
\frac{\binom{2m}{2}C^{m+1}}{m!}(n/N)^m.
$$
The factorial uses the same $n/m$ conversion and the bound
$n^{m-1}/(m-1)!$ for positive tuples. This proves (24) and hence (29),
with its remaining $N^2(3/4)^n$ transient.

## 4. Distinct cyclic orders, primitive words, and hub recovery

At a good hub $v$, exactly $m$ visits divide the cycle into $m$ excursions
having no internal $v$. They are distinct excursions because their first
successor labels are distinct. Thus their cyclic orders number exactly
$(m-1)!$; changing the naming of the first original visit only relabels
this set.

Every reordering preserves directed edge counts and hence the exact complex
amplitude. To distinguish resulting cyclic words, use the trigram arrays
$T_w(u,z)$. Reordering leaves all arrays with center $w\ne v$ unchanged:
interiors are unaltered, and each first and last excursion neighbor keeps
its adjoining $v$. At $v$, an order gives trigrams
$(a_i,v,b_{\sigma(i)})$, with $\sigma$ an $m$-cycle. Distinct incoming
and outgoing neighbor labels determine $\sigma$ uniquely. Thus a nonoriginal
order gives a nonzero change precisely at center $v$.

This proves injectivity across cyclic orders, excludes the original rotation
class, and identifies the hub from the ordered pair of cyclic words. If the
same partner arose from another hub, the support of the nonzero trigram
difference would have to be both singleton centers, which is impossible.
It also proves disjointness across different encounter orders: the recovered
hub cannot have two different values of $K_v(x)$.

Each original or reordered word is primitive. A repeated cyclic block would
repeat every outgoing edge multiplicity at least twice, whereas every
outgoing edge from the good hub to its distinct successors occurs exactly
once. Consequently each partner rotation class contains exactly $n$
distinct rooted words. The exact number per first word is therefore
$$
n((m-1)!-1)g_m(x).
$$
This is a count of distinct unlabelled rooted words, with no hidden
factorial or artificial edge labels.

## 5. Reverse exclusion, symmetry, and the asymptotic constants

The edge from $v$ to one of its successors $b_i$ occurs, but the reverse
edge $b_i\to v$ does not: every predecessor of $v$ is in the disjoint set
of incoming neighbors. Hence the original directed edge-count array is
not symmetric. Reordered words preserve this array, while reversal transposes
it, so no reordered partner belongs to the reversed rotation class.

The relation is symmetric under exchanging the two words. At the changed
hub the same excursion lengths and neighbor sets remain, and reordering back
recovers the original cyclic class as a nonoriginal order. This also makes
the complements used in the signed sums invariant under exchange.

Multiplying the exact partner count by $w(x)$ and summing proves (5).
Substitution of (29) gives
$$
\mathcal E^{(m)}_{n,N}
=N^2\frac{(m-1)!-1}{m!}e^{-t}t^{m+1}
+O_{m,B,C}(N)+O_m(nN^2(3/4)^n).
$$
For $n\ge cN$, the last term is absorbed into $O_{m,B,C}(N)$ after a
threshold depending on $c$. This checks the stated uniformity and error
constant convention. The weighted Riemann-sum normalization is $N^{-3}$,
as in (36); the usual pair normalization $N^{-2}$ leaves a contribution
of order $N$ from this positive class.

For $m=3,4$, the coefficients are $1/6$ and $5/24$, respectively.
At $t=2$ their sum is $28e^{-2}/3>1$. The inequality follows already
from $e<3$, so no numerical approximation is needed. Their proved
disjointness and $|\operatorname{Tr}U^n|^2\le N^2$ yield (8). The stronger
separate all-time reverse-class estimate is unnecessary for (8); when
imported from the physical-cycle theorem, it permits the further stated
interpretation inside $Z_n$.

## 6. Unresolved scope

The encounter classes have actual original-family asymptotics at each
scaled time, without averaging in dimension or replacing quantum phases by
independent variables. They also force a negative contribution from their
complement. None of this evaluates that complement accurately enough to
cancel the explicit order-$N$ weighted contribution and retain the
order-one CUE correction. The signed sum displayed as (40) in the target,
and all higher-order $H_{\rm diag}$ assertions, remain open in this route.
