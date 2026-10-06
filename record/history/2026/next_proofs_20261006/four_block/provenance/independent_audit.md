# Independent audit: symbolic localization and once-counted four-block cancellation

## Claim and current verdict

**The claimed theorem is proved by the repaired combined argument below. The initially frozen symbolic source contains incorrect Case U/V output equations and requires their replacement before acceptance as written.** All remaining implications in the four-block candidate pass independent review.

Initial symbolic source SHA256: 5e067febe2dcc26d9b41c181e5bd1c48ff21af38d4edde23e3069df48bda269a.
Four-block candidate SHA256: b40c0122dc1ed60c31c8eaccf270a643dcd6776e0799cf2686651b258a7c5473.
Base: 0ffb20cc152d0ddd2620887e46d21d1120b95fd8.

Under the already audited q<=C/N and ||P^L-J||<=2^-L hypotheses, the once-counted distinct-port reduced four-block family has normalized signed compact positive Heisenberg-band error O((log N)^10/N), plus superpolynomial and exponential terms. This is one fixed-complexity family, not deterministic BGS.

## 1. Short-cluster-safe competing-cut localization

Use source-to-output bijections f,g with the actual cyclic output alignment. They are translations on each respective block. At a genuine source cut their translation offsets jump: otherwise the output successor of the preceding source block would be its original next block, contrary to reduction.

On a common-refinement source interval I of length >=R=(r+1)K, the g-image meets at most r old output cuts. Among its at most r+1 pieces is a K-substring lying in one old output block. Pulling that substring back by g and f produces two consecutive source K-substrings with equal labels. K-uniqueness equates their source starts, hence f and g have the same translation offset on I. This includes cyclic wrap and does not require generic or unequal block lengths.

Every mismatching refinement interval therefore has length <R. There are at most 2r such intervals, so |D|<=2r(R-1)<m. At a mismatch-component start u, the previous positions agree. If f had no cut there, f(u)=f(u-1)+1. The block ending at u-1 under g has an output successor whose source head v obeys g(v)=g(u-1)+1=f(u). Since g(u)!=f(u), v!=u. Both u,v are g-cut heads, and output equality gives x_u=x_v, contradicting the new distinct-port condition. Swapping f,g proves that every component begins at a common cut.

A new cut within a mismatch component or at its end lies at forward distance <=|D| from that common old cut. A new cut with matching maps on both sides has the same nonzero jump under f and is itself old. Consequently all new cuts lie in a deterministic O_r(K)-sized union of neighborhoods of old cuts, giving O_r(K^r) candidate unordered cut sets. This proof handles arbitrary singleton and short blocks; localization is not inferred merely from the existence of long pieces.

Choose deterministically a longest common-refinement interval. It has length >=m/(2r)>R. Equality of output words must align the two translation offsets there, prescribing their relative output-root shift uniquely from cut geometry and block patterns before any labels are summed. No additional factor m is needed. Graph estimates may then drop K-uniqueness after fixing that necessary alignment.

## 2. Three-anchor word equations: error and complete repair

The anchor distribution argument is valid. Three original anchors occur in reversed cyclic order under the reduced four-block reversal. If two belonged to one alternative block, their circular order together with the third would be preserved; with only two occupied blocks, switching the block order only cyclically rotates that triple. Hence three alternative blocks each contain one anchor and the remaining nonempty block E lies in one source anchor gap.

With original notation
x=X u Y v Z w,
u=u1 u2, v=v1 v2, w=w1 A w2,
the original output rooted at X is
X [u1 A v2] Z [w1 u2] Y [v1 w2].
Anchors mean fixed source/output POSITIONS, so the arc word equations are valid even if the single letters X,Y,Z coincide.

### Same gap W: the written argument passes

For u=p1p2, v=q1q2, w=r1 E r2, the output equations in the source are correct. Comparing q1,v1 forces equality: a nonempty difference identifies either old B/D first letters or new B/D first letters. Then r2=w2 and comparison of r1,w1 identifies old A/C or new E/C first letters unless r1=w1. Thus E=A and every cut agrees. Empty pieces are harmless because each contradiction uses a specifically nonempty difference word and an actual nonempty block.

### Gap U: initially printed output equations are wrong

If u=p1 E p2, v=q1q2, w=r1r2, the alternative source block order is the X-anchored block, E, the Y-anchored block, the Z-anchored block. Its reversed reduced output places E AFTER the Y-anchored block. The CORRECT equations are
u1 A v2=p1 q2,
w1 u2=r1 p2,
v1 w2=q1 E r2.
The initial source instead placed E in the middle equation.

These corrected equations give a short complete contradiction. Compare prefixes q1,v1 of the common word v:
- If q1=v1 T with T nonempty, then v2=Tq2 and w2=T E r2. Old D and B therefore have the same first letter.
- If v1=q1 T with T nonempty, then q2=T v2 and E r2=T w2. Since E is nonempty, new D and E have the same first letter.
- If q1=v1, then q2=v2 and w2=E r2. Comparing w1 A w2=r1r2 gives r1=w1 A E, and the second equation gives u2=A E p2. Old C and A then have the same first letter.
Every case contradicts the relevant distinct-port condition.

### Gap V: initially printed output equations are wrong

If u=p1p2, v=q1 E q2, w=r1r2, the alternative source order is the X-anchored block, the Y-anchored block, E, the Z-anchored block. The correct reduced output puts E between the Z and Y anchors. Its equations are
u1 A v2=p1 q2,
w1 u2=r1 E p2,
v1 w2=q1 r2.
The initial source instead placed E in the last equation.

Compare prefixes p1,u1 of u:
- If p1=u1 T with T nonempty, then u2=Tp2 and the first equation gives A v2=Tq2. Old C and A have the same first letter.
- Otherwise write u1=p1 T, allowing T empty. Then p2=T u2, and the second equation right-cancels to w1=r1 E T. The source equation for w gives r2=E T A w2. New B and E have the same first letter, because E is nonempty.
Again every case is impossible.

This establishes the desired three-anchor rigidity after the explicit repair, including all empty-piece and equal-length degeneracies. If three original blocks have length >=5K, four alternative cuts supply the requisite common K-anchor in each. Hence every ambiguous K-unique four-block representation has at least two blocks shorter than 5K.

## 3. High-rank exceptional budget

There are O(K²m) length quadruples with two short blocks: choose their positions and lengths, then one free remaining length. Localization supplies O(K^4) competing cut sets and exactly one necessary geometric alignment for each. Distinct cut sets cannot have relative rank zero, and rank one is excluded by the independently checked predecessor-transposition argument.

For a rank-s equality graph, incompatible identification of two starting ports contributes zero. Otherwise expose all four starts first. Exactly s later internal vertex visits are forced to known class values; each has conditional transition probability <=q. The four starting sums and eight connector magnitudes yield N^4 q^(s+4)<=C^4q^s. This applies with overlapping equalities and after dropping the K-unique restriction. Thus a rank>=3 alternative costs <=C^4q³.

Including m² roots and the normalized O(N)-term band sum gives
N^-2 × O(N) × O(N²) × O(K²N) × O(K^4) × O(q³)
=O(N²K^6q³)=O(K^6/N).
This is an absolute bound on marked representations incident to a high-rank relation, not merely on the number of relations. A union bound over alternatives provides it directly. Also each pair has at most R_K=O(K^4) cut sets by localization relative to any fixed one.

## 4. Rank-two graph, exact overlap multiplicity, and triangle exclusion

For K-unique x, both words are primitive once m>8K. Indeed at least m-4(K-1)>m/2 output K-substrings are internal to shared blocks and pairwise distinct. A period would inject those starts into their smaller complement. Thus every cut set contributes exactly four marked tuples, corresponding to cyclic block labels, without further root stabilizers.

The accepted rank-two classification identifies every graph edge with one consecutive abab cluster, tau_s=(s,s+2)(s+1,s+3), and exact cuts {s,s+1,s+4,z}/{s,s+3,s+4,z}. For m>8 its start s is unique. Exactly one endpoint has the singleton A and length-three B required by O_m. With these blocks fixed, C,D are the remaining source intervals in their fixed order; primitive trace roots are unique. Consequently O_m counts each unordered rank-two edge exactly once, not four times or twice. Conversely every such local marked tuple gives that edge, even in the presence of extra incidental label equalities.

Use one fixed rooted output to define all positional maps for a pair. Relative maps therefore compose consistently. Two different incident edges have distinct tau_s,tau_t. If their starts are neighboring, their product is a three-cycle; this rank-two type is forbidden by the accepted classification for the third pair of vertices. At displacement two the product consists of two three-cycles; at displacement three, a three-cycle and two transpositions; with disjoint supports, four transpositions. Each has rank four. Negative cyclic displacements give inverse patterns; m>8 excludes a further overlap case. Thus no triangle exists.

If a pair has no high-rank relation, its graph is complete and triangle-free, so it has r=1 or 2 vertices. Its edge count satisfies r-e=1. Therefore its once-counted weight is exactly its M_m/4 contribution minus its O_m contribution.

## 5. Bad pairs and non-K-unique/periodic words

For a bad pair with r>=3, at most one graph vertex is incident to no high-rank relation: two such universal rank-two neighbors would form a triangle with any third vertex. Hence r_hi>=r-1>=r/2. If r=2 and the relation is high-rank, both vertices participate. Thus the high-rank marked bound controls the entire bad marked mass up to factor two.

The coefficient discrepancy satisfies |1-r+e|<=1+r+binom(r,2)<=O(R_K)r. Summing against absolute pair weights costs O(R_K) times that bad marked mass, or O(K^10/N). This is an exact finite graph correction, not an unjustified truncation of inclusion–exclusion.

For non-K-unique x, the repeated-substring equality graph has rank >=K/2. The loose four-chain estimate and polynomial counts yield O(N^10q^(K/2)) after normalization, uniformly over all length quadruples, including zero internal lengths. Every unmarked exceptional pair has at least one marked witness, so its absolute mass is bounded by the full exceptional marked mass. O_m is literally a subset of the marked parameter tuples, so its exceptional absolute mass is bounded by the same quantity. These domination arguments do not require primitivity and remain valid with periodic root multiplicities. Therefore extension from the K-unique sector adds only a constant multiple of this superpolynomial term.

Finally the full marked sum is exponentially small by the accepted uniform-link identity; the local-overlap sum is exponentially small by the separately audited free-long-endpoint contraction. Combining M_m/4-O_m with the two exceptional budgets yields the claimed scoped error. Smooth signed weights cause no issue: absolute error budgets use their absolute values.

## Audit boundary and disposition

All new obligations pass after the explicit U/V repair. No finite three-anchor search, even millions of successful cases, is needed or used to justify the symbolic rigidity. The accepted rank-two computer-assisted classification remains load-bearing, with its separate finite-reduction and kernel audit.

The initial symbolic file must not be promoted unchanged: its U/V equations describe the wrong block order. The repaired proof above closes that precise gap without changing the theorem, hypotheses, constants, or scope. No other gap was found in localization, alignment, rank budget, overlap multiplicity, graph correction, or exceptional-word handling.

Remaining open work concerns repeated genuine ports, other reconnection families, r>=5 short-cluster unmarking, growing complexity, overlaps between families, and the full signed trace hierarchy. None is supplied by this fixed four-block result.
