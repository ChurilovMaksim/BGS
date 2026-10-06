# Long-block unmarking by unique substring anchors

Checkpoint RECONNECT-20261006-B, base 0ffb20cc152d0ddd2620887e46d21d1120b95fd8. Continuation of constant_gap_and_marked_cancellation.md; new author proof awaiting independent review. No repository modification or BGS promotion.

## Result and boundary

Assume the actual-model subsidiary bounds proved in the companion: P_xy<=q_N=C/N, and ||P^L-J||op<=2^-L eventually. Fix a positive compact Heisenberg band aN<=m<=bN and put K=ceil(log N).

Let H_m be the UNMARKED ordered word-pair set admitting a three-block cyclic decomposition x=A B C, y a cyclic rotation of A C B, with pairwise distinct first vertices of A,B,C and each block containing at least4K vertices. Each ordered pair is included once, regardless of its representations. Then its signed trace-path sum has vanishing N^-2 smooth band normalization, faster than every power of N.

This is a scoped actual unmarked-family estimate, not only a marked estimate. It leaves pairs admitting only short-block decompositions, other reconnection patterns, the plateau, and higher joint traces open. Constants and startup depend on the fixed actual tau.

## 1. Pure word uniqueness lemma

A cyclic word x of length m is K-unique if all m cyclic substrings of K consecutive vertices are distinct. Suppose x=A B C, each block length>=4K, and their first vertices are distinct. If y=A C B cyclically, then there is exactly one unordered triple of cut positions in x with pairwise distinct first vertices that produces this cyclic y. The alternative block lengths are unrestricted.

Proof. Superimpose on cyclic y the three original block boundaries and the three boundaries of an alternative decomposition producing y. Each original block has at most three alternative cuts, so it is split into at most four intervals. Its length>=4K implies one such interval contains at least K vertices. Choose a K-vertex anchor in each original block that is wholly within a single alternative block. In both representations this anchor is a substring of x. K-uniqueness forces its two occurrences in x to have exactly the same start index, not merely the same label sequence.

These three anchors occur in cyclic order A,B,C in x and A,C,B in y. Each alternative block must contain exactly one anchor. Indeed, if two anchors belonged to the same block, their circular order together with the third anchor would be unchanged by permuting the occupied blocks; that contradicts the reversed three-anchor circular order. (Equivalently, with only two occupied blocks, one cannot reverse the cyclic order of three marked positions while preserving their order inside each block.)

Associate each alternative block with its anchor. Let a_i be the old cut before block i, and let its alternative cut be a_i+delta_i, using the unique integer lift in the interval between its preceding and its own anchor. Both cuts lie in this interval. Between anchor i and the next anchor i-1 in y, the change in distance caused by the alternate cuts is delta_(i+1)-delta_(i-1). The anchors occupy the same y positions, so all these differences vanish. Thus delta_1=delta_2=delta_3=delta.

If delta>0, at each original y junction the alternative word has not yet switched blocks. Equality at this single vertex forces the original first vertices a_(i+1) and a_(i-1) to have equal labels. All three original port labels would be equal, contrary to hypothesis. If delta<0, compare at each new junction instead: the new first vertices a_(i+1)+delta and a_(i-1)+delta must have equal labels, contrary to the alternative distinct-port hypothesis. Thus delta=0 and the cuts coincide.

K-uniqueness makes x primitive. It also makes y primitive in this situation: let G be the y positions whose K-substring lies wholly within one original block. There are at least m-3(K-1)>m/2 such positions. Their substrings are all distinct, since their x positions are distinct. A nonzero period shift of y would send G injectively into its complement (otherwise two equal K-substrings occur within original blocks), impossible because |G|>m/2. Finally y cannot be a rotation of x, since the three unique anchors have different circular orders.

## 2. Repeated-substring equality budget

For distinct cyclic positions s,t in a word of length m, require equality of their K-substrings, with K<=m/4. The equality graph on the m position variables contains the K edges (s+j,t+j), 0<=j<K, modulo m. There are no loops and no repeated unordered edges: a repeated reversed edge would require t-s=m/2 and both starts in an interval of length K<m/2. Every vertex has degree at most2. Each component is a path or a simple cycle, hence the rank of the equality constraints (number of vertices minus number of components, including isolated vertices) is at least K/2.

Consider the absolute weight of any fixed three-block reconnection representation. The shared internal edges contribute products of P; the six connector amplitudes contribute at most q_N³. Summing the internal path products without any equality conditions gives N³, one freely summed initial vertex per open block. With an equality graph of rank r, reveal the three chains sequentially, each in its forward order. Every vertex after the first occurrence of its equality class is forced by already revealed labels. At most three of these forced vertices are chain starts; each remaining one has conditional transition probability at most q_N. Therefore the internal weight sum restricted by the equalities is at most N³ q_N^max(r-3,0). Including connectors, for r>=3 it is at most N³ q_N^r.

For K>=6 the union bound over fewer than m² substring-position pairs thus gives

sum_(represented x not K-unique) |a(x) conjugate(a(y))| <= m² N³ q_N^(K/2)

for each fixed length triple and fixed marked trace starts. This is an absolute bound on this exceptional set only; no absolute bound is claimed for the full spectral sum.

## 3. Passing from marked to unmarked long blocks

Sum the marked contractions over all length triples with each n_i=L_i+1>=4K and total m. The companion theorem bounds each by C³N2^-max Li, and hence their m²-start weighted total is exponentially small on the band.

Restricting this marked sum to K-unique x changes it by at most

m² [number of triples] m² N³ q_N^(K/2),

where the first m² is the two trace starts and the second is the substring-pair union bound. Since the number of triples<=m², its N^-2 band normalization is O_(a,b,w)(N^8 q_N^(K/2)). With K=ceil(log N), q_N=C/N, this decays faster than every fixed inverse power of N.

By section1, each K-unique unmarked ordered pair in H_m has exactly three marked representations, corresponding to the three cyclic labels of its unique cut triple; x and y are primitive, so the two trace-start counts introduce no extra stabilizer. Thus the unmarked K-unique sum is exactly one third of the restricted marked sum.

The exceptional unmarked pairs have at least one representation, so their absolute weight is bounded by the exceptional marked absolute sum above. This proves the full H_m assertion, including pairs with multiple long-block representations. Moreover, any pair admitting both a long-block and a different short-block representation is in this negligible repeated-substring exceptional set.

## 4. Executed large-alphabet discriminator

check_long_blocks.py uses exact word comparisons, not floating arithmetic. It checks20 randomly generated K-unique words in each of three settings K=1,2,3, m=12K, alphabets12,20,20, with original block lengths4K. For each it exhausts every alternative cut triple, including arbitrarily short blocks, and verifies uniqueness and primitivity of y.

It also inflates the known ambiguous word001212 by substituting three disjoint internally unique words of length12. This produces length72 on an alphabet of36, with two distinct admissible cut triples and all original blocks at least12 long. The example contains repeated length3 substrings, as the lemma predicts. This shows ambiguity is not solely a bounded-alphabet or short-block phenomenon, while identifying the repeated-word mechanism that the weighted bound suppresses. These finite checks support the combinatorial proof, not an asymptotic experiment at the physical tau.

## 5. Remaining task

The unresolved three-block sector now consists of pairs with no all-long representation: every admissible decomposition has at least one block shorter than4 ceil(log N). Its number of possible length triples is only O(m log N), but that counting saving alone does not overcome the actual normalization or justify signed cancellation. A further exact cluster decomposition, with its canonical endpoint masks controlled, is needed. The general encounter hierarchy remains open; no claim of asymptotic impossibility follows from the earlier small counterexamples.
