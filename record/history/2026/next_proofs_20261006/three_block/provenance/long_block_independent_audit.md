# Independent audit: long-block unmarking

## Claim and verdict

**Proved as written.** Given the companion's established actual-model bounds q_N=max|U_ab|²<=C/N and ||P^L-J||<=2^-L eventually, the once-counted ordered-pair set H_m defined in the candidate has a signed N^-2 smooth compact positive Heisenberg-band sum smaller than every fixed inverse power of N. H_m consists precisely of pairs admitting an A B C -> A C B cyclic reconnection with distinct first-vertex ports and all three blocks of at least 4 ceil(log N) vertices.

There is no surviving multiplicity or normalization gap for this all-long-admitting sector. Pairs admitting only short-block representations, other encounter patterns, and higher trace orders remain outside this result.

Candidate SHA256: bb63c25bb78953262d9e686b0570713e812c76f5c4552164011393e67fb3ea23. Base: 0ffb20cc152d0ddd2620887e46d21d1120b95fd8. Companion SHA256 remains 156808b1febd7b61a8aff4e4756314934e5cb6b471c7e5a2f15a6f5f64f216af; the prior review artifact is unchanged. This is a proof audit, not inference from the supplied random finite checks.

## 1. Uniqueness, including competing short blocks

Fix the actual cyclic y positions. Superimpose the original and alternative three-cut partitions of y. An original block of at least 4K vertices is split by at most three alternative cuts into at most four nonempty intervals. One interval has at least K vertices. Choose an anchor K-substring there for each original block. Each anchor is internal to both partitions. Both readings map it to a cyclic K-substring of x; K-uniqueness forces the two starting indices in x to agree exactly.

The three anchors have cyclic order (1,2,3) in x and (1,3,2) in y. If only one or two alternative blocks contained them, their cyclic order could not change: with two occupied blocks, the two anchors in one block retain their linear order and the third lies in the other block; reversing the order of two occupied blocks only cyclically rotates the resulting three-anchor order. Thus the alternative partition has exactly one anchor per block. This conclusion does not impose a lower bound on alternative block lengths; that each contains a K-anchor follows from the argument, rather than being assumed.

Index each alternative block by its anchor. Its start a'_i and the original start a_i both lie in the same circular interval between anchor i-1 and anchor i in x. Choose their lifts in that interval and let delta_i=a'_i-a_i. The successor anchor of i in y is i-1. The distance from anchor i to anchor i-1 changes by delta_(i+1)-delta_(i-1), because the exit boundary of block i is the start of block i+1 in x, while the entry boundary is the start of block i-1. Anchor locations in y agree, so these differences vanish, forcing a common delta.

For delta>0, the alternative boundary occurs delta vertices later at each original y junction. At the old junction following block i, the original reading is x_(a_(i-1)), while the alternative reading is x_(a_(i+1)). Equality forces these port labels equal, contradicting distinct original ports. For delta<0, use the earlier alternative junction: the two readings are x_(a_(i-1)+delta) and x_(a_(i+1)+delta), contradicting distinct alternative ports. Hence delta=0 and all cuts coincide. Circular wrap is covered by the lifts between neighboring anchors; no globally chosen zero cut or unproved linear order is required.

## 2. Primitivity and cyclic-start stabilizers

K-unique x is primitive, since a nontrivial period would repeat every K-substring. In y, the positions whose K-substrings stay in one original block form a set G of size m-3(K-1)>m/2, since m>=12K. Their substrings are pairwise different: their original starts in x are different. A nonzero period shift of y would map G into its complement, otherwise two positions of G would carry equal substrings. Such an injection is impossible. Thus y is also primitive.

Nor can y be a rotation of x: under such a rotation each selected anchor would map to its unique x occurrence, preserving cyclic order, contradicting (1,2,3) versus (1,3,2). This also shows the good sector introduces no cyclic-diagonal overlap.

For a fixed rooted ordered pair in the good sector there is one unordered cut triple, exactly three cyclic labels for its blocks, and exactly one rotation of each resulting primitive word to the specified root. Therefore the full marked count, including the two m-start sums, is exactly three. Restricting all block lengths to at least 4K retains all three labels of the unique triple. No factor m, m², or stabilizer remains.

## 3. Equality graph, overlap, and wrapping

For s!=t modulo m, use K edges {s+j,t+j}, 0<=j<K. There are no loops. Equal unoriented edges at two different j values would have to be reversed, requiring 2(t-s)=0 modulo m and the start-index difference to be m/2. Since K<=m/4, two starts in the length-K cyclic interval cannot differ by m/2. Hence there are K distinct edges.

Each vertex belongs at most once to the first endpoint interval and at most once to the second, so its degree is at most two, including overlap and wrap. Components are paths or simple cycles. A path with e edges has equality rank e. A simple cycle has rank e-1>=e/2. Summing yields rank r>=K/2. Isolated vertices do not affect rank. This is a universal graph argument, not an assumption of disjoint substrings.

## 4. Open-chain equality probability and connector cost

For a fixed block-length triple, all m vertex variables carry three independent open P-chains before the connectors are included. Their unnormalized total mass is N³. Normalize each starting label to uniform probability 1/N; then the remaining labels are exposed in the forward P-transition order, chain by chain.

For a fixed equality partition of rank r, exactly r variables occur after an earlier member of their class. At each such noninitial variable, equality specifies one already known label. Conditional on the full earlier history, its transition probability is at most q_N. At most three forced variables are chain starts; ignoring their constraints only enlarges the bound. Thus the probability of all equalities is at most q_N^max(r-3,0), and the unnormalized internal mass is at most N³ times that quantity. This can be proved by backward conditional expectation over the exposure order; future constraints never alter the transition bound used here.

The product of six connector amplitudes is at most q_N³ pointwise, even on repeated-label configurations. For r>=3 this gives N³ q_N^r, hence at most N³ q_N^(K/2) once K>=6 and q_N<=1. A union bound over fewer than m² pairs of substring starts gives the candidate's exceptional mass. These eventual restrictions hold for K=ceil(log N); finitely many small N have no bearing on the asymptotic statement.

## 5. Signed-to-unmarked passage and exact polynomial normalization

The unrestricted marked long-block sum is exponentially small by the companion. Removing representations with non-K-unique x has absolute cost at most
m² (trace starts) × m² (length triples) × m² (substring pairs) × N³ q_N^(K/2)
= m^6 N³ q_N^(K/2).
On a fixed band aN<=m<=bN, this is O(N^9 q_N^(K/2)) per m. The O(N) values of m and N^-2 normalization give precisely O(N^8 q_N^(K/2)), with a bounded test weight absorbed into the constant.

For K=ceil(log N), log[N^8(C/N)^(K/2)]=-(1/2)(log N)^2+O(log N), hence the error is superpolynomially small. Taking the absolute value here applies only to the repeated-substring exceptional set, not to the complete spectral comparison.

The K-unique restricted marked sum equals three times its once-counted unmarked sum. Every exceptional pair in H_m has at least one retained long representation; all its representations have the same absolute trace-path weight, since cyclic starts do not change a cyclic product. Its once-counted absolute mass is therefore bounded by the exceptional marked mass. This proves the full H_m assertion, including multiple long representations and pairs admitting both long and short representations. In fact the uniqueness lemma forces any pair with a genuinely different short representation to be exceptional.

## Dependencies, obligations, and remaining boundary

Inherited and already independently audited: actual-model q_N<=C/N, eventual power mixing, and exact unrestricted marked contraction. New obligations, all passed above: pure-word uniqueness with unrestricted competing lengths; primitivity; stabilizer count; graph rank under overlap/wrap; open-chain equality probability; normalized exceptional bound; once-counted exceptional domination.

The candidate's random large-alphabet examples are finite supporting evidence only and are unnecessary to this proof. No new external theorem or computation-dependent universal claim is needed. The remaining implication is suppression of pairs for which every admissible representation has a short block; the current unique-anchor argument provides no anchor in that block and cannot be extended by merely counting O(m log N) length triples. The result is a real unmarked-sector advance, not closure of the entire three-block family or BGS.
