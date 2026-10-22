# Independent adversarial audit: complete distinct-port three-block family

## Claim and verdict

**Proved as written.** For the actual frozen family, assuming the already independently audited q_N<=C/N and ||P^L-J||<=2^-L, the once-counted ordered-pair set T_m in the candidate has vanishing N^-2 smooth compact positive Heisenberg-band sum. Its error is O_w((log N)^5/N), plus superpolynomial and exponential terms. There is no additional cyclic-start, competing-cut, or normalization factor in this scope.

Audited candidate SHA256: ecaa44655e5c8c2257d7b0f300119b7a6a24f3ec70d976f9be3ca4a7ec65ee27. Base: 0ffb20cc152d0ddd2620887e46d21d1120b95fd8. Earlier accepted proof and audit files are unchanged. The argument below is a fresh derivation of the new implications, not reliance on earlier successful reviews or finite examples.

## 1. Two-long uniqueness: passed

Let B,C have lengths >=4K and let A be nonempty. The original/alternative common-interval construction supplies one K-anchor inside B and one inside C. K-uniqueness identifies their source positions exactly. Let d be the oriented B-anchor-to-C-anchor distance in x. Its distance in y increases by |A|, with both distances strictly between 0 and m. If both anchors belonged to one alternative block, that oriented distance would be preserved, a contradiction.

They therefore occupy different alternative blocks. If the third alternative block lies in the B-to-C gap of x, reversing the block order decreases d by its length. If it lies in the other gap, reversing the order increases d by its length. Neither calculation wraps by m: the unoccupied block is wholly in the corresponding gap. The observed increase |A| forces this block to lie in the C-to-B gap and have exactly |A| vertices.

The two cuts bounding this alternative A-block lie in the same lifted C-to-B anchor gap as the old A endpoints. Their shifts are equal, delta_A=delta_B=delta. Compare the direct C-to-B junction of y. If delta>0, the new block switch has not happened at the old switch: the two readings are the old A and B first vertices. Their equality violates original distinct ports. If delta<0, compare at the new switch instead, obtaining equality of the new A and B first vertices. Thus both A endpoints are fixed.

Only the B/C cut can move. For a forward movement W, write C=W C'. With the common C' anchor chosen as cyclic root, the two output sequences are cyclically C' B A W and C' B W A. Cancelling the identical initial C' B segment leaves A W=W A. Its first letters identify the original A and C ports, forbidden. For a backward movement, write B=B' W; the same comparison leaves W A=A W and identifies the new A and C ports. Hence the last cut is fixed too. These cancellations hold for nonempty W of any allowed length; the anchor prevents the moved boundary crossing the root used in the comparison.

Consequently a genuinely ambiguous K-unique pair has two blocks shorter than 4K in every representation. On m>>K it has exactly one long block. Competing short representations have not been omitted.

## 2. Localization and cyclic alignment: passed

Rotate each two-short representation to x=C A B and its output to C B A, using the original coordinate circle for both. Its positional permutation is supported in the cyclic interval I=A B of length <8K; the long C portion is unchanged positionwise. Every competing representation also has a short support interval I' of length <8K by the previous step.

Suppose the two natural outputs agree after a shift r. A K-substring meets I for at most |I|+K-1 starts, and similarly for the shifted I'. Thus fewer than 18K starts are excluded. For m>18K there is a common unaffected substring. Equality then gives the source x substrings at starts j and j+r equal. K-uniqueness forces r=0 modulo m. This proves a unique alignment without paying an extra factor m.

With zero shift, disjoint supports I,I' would force each output to be identical to x: on I only the first can differ, on I' only the second can differ, and outside both neither differs. But swapping A B nontrivially changes it, since A B=B A would identify their first letters. Thus I and I' meet. Their union has length <16K and contains all three alternative cuts. It lies in a fixed O(K)-neighborhood of the original cluster, independent of vertex labels. There are at most O(K³) unordered candidate cut triples in that neighborhood, with an absolute constant. Wraparound changes no count.

## 3. Equality rank and rank-one exclusion: passed

Represent the two aligned output words by bijections f,g from output positions to source position labels. Their equality imposes x_v=x_(tau(v)) for tau=g composed with f inverse. The equality partition is exactly the cycle partition of tau, so its rank is m minus its number of cycles. Let c be the original predecessor m-cycle, and r the first output predecessor m-cycle. The second is r'=tau r tau inverse.

A three-block reorder changes predecessor exactly at its three cut heads: they remain three distinct positions even for singleton blocks. Thus rank zero gives identical output positional cycles and the same cut-head triple.

If rank one, tau=(p q) and x_p=x_q. The first admissible distinct-port condition says p,q cannot both be cut heads; choose q not a head. Put s=c(q)=r(q). To prove p is a new head, suppose r'(p)=tau(s)=c(p). If s is outside {p,q}, injectivity of c fails; if s=p, c has a 2-cycle; s=q would be a fixed point. All are impossible for an m-cycle with m>2. To prove q is a new head, suppose r'(q)=s, equivalently r(p)=tau(s). For s outside {p,q}, injectivity of r fails; for s=p, r has a 2-cycle; s=q is again impossible. Hence p and q are both heads of the second representation, contradicting its distinct-port condition.

Therefore every different admissible cut triple imposes rank at least two. The proof works even if an arbitrary cyclic alignment is allowed; localization has already removed that alignment from the enumeration. It does not claim rank three. Additional accidental label equalities do not rescue a forbidden rank-one graph, because x_p=x_q alone already contradicts the second distinct-port condition.

## 4. Start-first probability payment: passed

For fixed original cuts, the three starting positions must lie in different equality classes, or the distinct-port restriction makes the contribution zero. Fix and sum their distinct labels first, using at most N³ choices. The three open chains now have fixed starts and retain their original forward transition laws P. Reveal their internal vertices in any order respecting each chain's forward order.

Each equality class represented by a start has its first value known from the outset. Each other class gets its first value at its first internal visit. Every remaining occurrence requires one specified label at a transition, whose conditional probability is <=q. If the graph rank is r, precisely r such internal occurrences are forced. Crucially, no forced occurrence is lost to an unrevealed chain start: all starts were exposed first. Iterated conditional expectation proves the product bound q^r without independence between equality events or assumptions about overlapping constraints.

The six connector magnitudes cost at most q³ pointwise. Therefore the total absolute pair weight subject to a compatible graph is <=N³ q^(r+3)<=C³ q^r, and for r>=2 it is <=C³ q² eventually. This estimate applies also after dropping the K-unique restriction, so it is valid inside the localization union bound.

## 5. Primitivity, exact multiplicity, and normalization: passed

K-unique x is primitive. For any three-block output y, the number of positions whose K-substrings stay inside one block is
sum_i max(n_i-K+1,0) >= m-3(K-1)>m/2
when m>6K. Those substrings are pairwise distinct, because their source starts in x differ. A nonzero period of y would inject these positions into their complement, impossible. Thus y is primitive even when two blocks are very short.

For a K-unique unambiguous pair there is one unordered cut triple and precisely three cyclic block labels. Primitivity makes each independent trace root unique; it creates no additional stabilizer or factor m. Consequently its marked multiplicity is exactly three.

Ambiguous K-unique representations have two short lengths, giving O(K²) original length triples. Each has O(K³) competing cut triples after localization. Each competing equality graph costs <=C³q². Independent roots contribute m². Thus their absolute marked mass per m is O(m² K^5 q²). Summing O(N) band lengths and multiplying by N^-2 gives O(N K^5 q²)=O(K^5/N).

The non-K-unique marked mass over all triples retains the previously proved loose bound O(N^8 q^(K/2)) after band normalization; that proof never required long blocks. The unrestricted complete marked sum is exponentially small by the companion. Write E for the total exceptional absolute marked mass. The good unmarked sum is exactly one third of the good marked sum. Every exceptional unmarked pair has at least one representation with the same absolute cyclic-product weight, so its absolute mass is <=E. In particular the difference between the full unmarked sum and one third of the full marked sum is <=4E/3. This explicitly accounts for all possible representation multiplicities without dividing the exceptional set by a false universal factor.

## Dependency boundary and remaining gap

New obligations all passed: two-long uniqueness; O(K³) localization with no extra cyclic shift; rank-one exclusion; full equality payment by start-first exposure; primitivity and multiplicity; normalized O(K^5/N) exceptional bound. Inherited dependencies are only the audited flat-entry/mixing/marked lemmas and repeated-substring exceptional estimate. No finite test or external theorem establishes any of these new universal combinatorial steps.

This does close the full once-counted distinct-port three-block family T_m as defined. It does not cover repeated-port reconnections, arbitrary path-pair permutations, overlaps among different encounter families, growing encounter complexity, or higher joint traces. No implication to complete deterministic BGS is supplied.
