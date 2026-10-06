# Once-counted distinct-port three-block cancellation

Proposed claim BGS-TRACE-015. Base: 0ffb20cc152d0ddd2620887e46d21d1120b95fd8. Project analytic proof with independent internal adversarial review. This is one fixed-complexity path-pair family, not full deterministic BGS. No external referee, global priority or analytic formalization claim.

## Claim

Use the unchanged odd-dimensional U_N=exp(i 10^-80 N A_N)M_N of `fixed_map_path_model.md`. The dependency BGS-FM-021, `position_chain_mixing.md`, supplies the subsidiary bounds q_N=max|U_xy|²<=C/N and ||P_N^L-J_N||<=2^-L eventually. Let T_m be the set of ordered coordinate-word pairs (x,y) for which some three cyclic nonempty blocks of x, with pairwise distinct initial vertex labels, reorder from A B C to A C B to give a cyclic rotation of y. Here a word is a rooted tuple x=(x_0,...,x_(m-1)) in {0,...,N-1}^m, a(x)=product_(j=0)^(m-1) U_(x_j,x_(j+1)), with x_m=x_0. Precisely: choose three distinct cut positions on the oriented coordinate circle of x, cyclically label the resulting nonempty contiguous blocks A,B,C, require their first vertex VALUES to be pairwise distinct, and require y to be one of the rooted cyclic rotations of the concatenation A C B. T_m is the set of rooted ordered tuples (x,y) satisfying this existential condition; multiple witnesses do not create additional elements. Count each ordered pair once. Then for every smooth weight w compactly supported in (0,infinity),

N^-2 sum_m w(m/N) sum_((x,y) in T_m) a(x) conjugate(a(y)) ->0.

The proof below gives error O_w((log N)^5/N) plus superpolynomial and exponential terms. The combinatorial and cancellation theorem uses only unitarity, the entry bound q_N<=C/N, and the stated mixing estimate for P_N. Actual frozen-model input enters solely through FM-021. Accordingly this fixed-family conclusion is compatible with other, even spectrally nonuniversal, unitary families satisfying those matrix estimates; it is not a spectral-universality criterion. It is not an assertion that all noncyclic pairs belong to T_m, nor that the higher signed hierarchy vanishes.

Set K=ceil(log N), so on the fixed positive Heisenberg band m exceeds every fixed multiple of K eventually. A word is K-unique when its m cyclic length-K vertex substrings are all distinct. The proof below is self-contained apart from the two FM-021 matrix estimates just stated. Define the marked sum M_m=m² sum_(L1+L2+L3=m-3; Li>=0) E_dist(L1,L2,L3), where

E_dist(L)=sum_(a1,a2,a3 distinct; b1,b2,b3) product_i (P^Li)_(ai,bi) U_(bi,a_(i+1)) conjugate(U_(bi,a_(i-1))).

Indices are modulo3. Expanding P powers gives three shared open coordinate chains; their block lengths are n_i=L_i+1. The factor m² enumerates the two independent trace roots with multiplicity, not an unmarked-pair count. If any link is replaced by J, summing its b_i gives delta_(a_(i+1),a_(i-1))/N=0. Choose the longest link, write P^L=J+(P^L-J), bound its entries by2^-L, bound the six connector magnitudes by q³, and sum the other two stochastic rows. This gives |E_dist(L)|<=C³N2^-max Li. Therefore the marked band sum is exponentially small up to a polynomial factor, including Li=0. No uniform unmarking factor is assumed for the exceptional set.

## 1. Strengthening: two long blocks suffice for cut uniqueness

Suppose x is K-unique and at least two original blocks B,C have length>=4K; the third A need only be nonempty. An alternative triple may have any positive lengths.

Superimpose the three alternative cuts on cyclic y. Each original long block is divided into at most four intervals; length>=4K ensures one contains K consecutive vertices. Choose such an anchor inside each of B,C. Each anchor lies wholly inside an original and an alternative block. K-uniqueness identifies their exact x positions. The two anchors cannot lie in the same alternative block: the cyclic distance from the B-anchor to the C-anchor in y exceeds its distance in x by |A|, strictly between0 andm; a single forward block would preserve that distance.

Thus the two anchors belong to distinct alternative blocks, and the third block has no anchor. Its x interval lies in one of the two gaps between the anchors. If it lay in the B-to-C gap, reversal would DECREASE the B-to-C cyclic distance by its positive length. The actual increase is |A|. Hence it lies in the C-to-B gap, has exactly length |A|, and is the alternative A-block.

Use integer shifts delta_A,delta_B,delta_C for the alternative cuts within their anchor gaps. Equality of A lengths gives delta_A=delta_B=delta. The direct junction C-to-B in y has old endpoints a_A,a_B and new endpoints a_A+delta,a_B+delta. If delta>0, equality at the old junction forces the old A and B initial labels equal. If delta<0, equality at the new junction forces the new A and B initial labels equal. Both violate their respective distinct-port conditions. Thus delta_A=delta_B=0.

Only the B/C cut might move. If it moves forward by a nonempty word W, write C=W C'; then the old and new y, rooted at the common C' anchor, agree precisely only if A W=W A. Their first letters must then agree, identifying the OLD A and C ports. If it moves backwards, the same commutation identifies the NEW A and C ports. Both are forbidden. Thus delta_C=0 and the cuts are identical.

Therefore every genuinely ambiguous K-unique pair has, in EVERY admissible representation, at least two blocks shorter than4K. Since m>>K, it has exactly one long block.

## 2. Localizing the ambiguous two-short-block sector

For a representation with short blocks A,B and long block C, cyclic rotation rewrites the operation as the adjacent exchange

x=C A B, y=C B A.

Its positional permutation is the identity outside the cyclic short cluster I=A B, whose length is <8K. Every competing representation of an ambiguous K-unique pair also has a short cluster I' of length<8K by section1.

First establish that their natural output words on the SAME source coordinate circle agree without an extra cyclic shift. Suppose they agree after a shift r. Exclude output K-substring starts meeting I for the first permutation and the r-shifted I' for the other. Fewer than16K+2(K-1) positions are excluded. Since m>18K, some remaining K-substring is unchanged from x by both permutations. Equality of outputs identifies the K-substrings of x at indices j and j+r. K-uniqueness forces r=0 modm.

If I and I' were disjoint, equality of the naturally aligned outputs, each unchanged outside its own cluster, would force both outputs to equal x. But A B=B A is impossible because A and B have distinct first labels. Thus I and I' intersect. Their union is contained in a cyclic interval of length<16K. Consequently all three competing cut positions lie within an O(K) neighborhood of the original short cluster; there are O(K³) candidate triples, with an absolute implied constant.

This also excludes a cyclic-identical output in this sector: compare its natural output to a rotation of x by the same unchanged-K-substring argument to force zero shift, then invoke A B!=B A.

A K-unique x is primitive, since a proper period would repeat its K-substrings. All outputs of a K-unique x are primitive when m>6K: more than m/2 output K-substrings lie wholly inside shared blocks and are pairwise distinct. A nontrivial period would inject that set into its smaller complement. This argument does not require all blocks to be long.

## 3. Exact rank-one exclusion

Given two positional block-reconnection outputs that agree as label words after their cyclic alignment, their position-label permutations impose an equality graph on x. Its rank is m minus the number of cycles of their relative permutation. Rank0 means identical positional output cycles, hence identical cut triples: the cut heads are exactly the three positions with changed predecessors relative to the original x cycle.

Suppose instead that the rank is1. The relative permutation is a single transposition tau=(p q), so x_p=x_q. Let c be the original predecessor permutation on m distinct position labels, and let r be the first output predecessor permutation. The second output predecessor permutation is r'=tau r tau. Both output cycles are full m-cycles, and each differs from c at exactly its three cut heads.

The first distinct-port condition implies that p,q cannot both be cut heads. Relabel them so q is not cut, hence r(q)=c(q)=s. We show both p and q are cut heads for r', which contradicts the second distinct-port condition.

- r'(p)=tau(s) cannot equal c(p). If s is outside{p,q}, equality violates injectivity of c since c(q)=s already. If s=p, equality gives c(p)=q and c(q)=p, a forbidden2-cycle in the original m-cycle. The case s=q is a forbidden fixed point.
- If r'(q)=c(q)=s, then r(p)=tau(s). For s outside{p,q}, r(p)=r(q)=s violates injectivity. For s=p, r(p)=q and r(q)=p give a forbidden2-cycle in the output m-cycle. Again s=q is impossible.

Here m>2, as always on the asymptotic band. Thus rank1 is impossible. Every distinct admissible representation equality has rank at least2. The explicit a b a b local ambiguity attains rank2, so a blanket rank3 assertion would be false.

## 4. Paying every equality with flat transitions

For a fixed original triple, the absolute pair weight is exactly the product of the internal P transitions on three open chains times six connector magnitudes, bounded by q³.

For any equality graph of rank r compatible with distinct ports, its three starting vertices belong to DIFFERENT equality classes; otherwise the term vanishes under the distinct-port restriction. Sum their labels first (at most N³ choices), then run the three independent Markov chains from these fixed starts. Whenever a class already represented by a start or earlier internal vertex occurs again, that transition must hit a specified label and costs at most q. Classes with no start receive their first label freely on their first internal visit. Exactly r subsequent occurrences are forced. No constraint is lost at a later chain start because all starts were exposed first. Fixing start labels does not change any transition row law; the initial finite sum remains outside the Markov probability calculation.

Therefore the full absolute weight satisfying this graph is at most N³ q^(r+3)<=C³ q^r. This applies to overlapping constraints without an independence assumption. In particular every competing representation costs at most C³ q² by section3.

## 5. Complete normalized ambiguity bound

The marked sum over all nonnegative link lengths is already exponentially small, including every short boundary, by the any-one-J identity and constant mixing gap.

For completeness, failure of K-uniqueness has the following direct bound. Equal K-substrings starting at distinct positions s,t impose K equality edges (s+j,t+j), 0<=j<K, on the m position variables. Since K<=m/4, there are no loops or repeated unordered edges. The graph has degree at most2; its paths and simple cycles impose equality rank at least K/2. For each of fewer than m² choices (s,t), reveal the three open chains sequentially. At most three rank constraints can fall at unconditioned starts; all others cost a factor q. Including the six connectors, the resulting absolute weight is <=N³q^(K/2) for K>=6. Multiply by at most m² length triples, m² roots and m² substring-position pairs, then sum the O(N) band lengths and divide by N². The result is O_w(N^8 q^(K/2)), which is superpolynomially small when K=ceil(log N) and q<=C/N. This deliberately loose bound is enough; it requires no independent-equality assumption.

For K-unique ambiguous words, section1 leaves only length triples with two short blocks, at most O(K²) possibilities. For each triple, section2 leaves O(K³) competing triples. Each imposes rank>=2 and costs absolute weight at most C³q² by sections3–4. Multiplying by the m² independent trace starts and the N^-2 band normalization (O(N) values of m) gives

O_w(N K^5 q²)=O_w(K^5/N).

This is an upper bound on the ambiguous marked mass, using a union bound over alternatives; overcounting is harmless here because this bound is absolute.

For every remaining K-unique unambiguous pair, primitivity of both words and uniqueness of the cut set give exactly three marked representations, from cyclic block labeling. Hence the actual unmarked sum is one third of the marked sum away from the bounded exceptional sets. Unmarked exceptional mass is at most its marked absolute mass because every member has a representation. Combining these estimates proves the claimed scoped family cancellation. The independent audit of these combinatorial steps is recorded in `../record/three_block_independent_review_20261006.md`. Quantitatively the normalized error is bounded by

O_w(K^5/N)+O_w(N^8(C/N)^(K/2))+O_w(N^5 2^(-(aN-3)/3)),

where [a,b] contains the support of w, 0<a<b, and K=ceil(log N). Constants can depend on the fixed actual model and w; the startup inherited from FM-021 is not effective.

## 6. Evidence and boundary

The portable verifier `../computations/verification/three_block_unmarking.py` checks rational contraction identities, variable marked multiplicities, all 451 single-repeat words with m=4,...,14, 180 two-long K-unique samples with every alternate cut triple exhausted, and a length 54/alphabet 52 local rank-two ambiguity. Arithmetic is exact rational or exact discrete word comparison. The random samples use a recorded deterministic seed and are finite diagnostics only. Execution receipt: `../evidence/executions/20261006/three-block/receipt.json`.

The new proof was independently reviewed against immutable candidate hash ecaa44655e5c8c2257d7b0f300119b7a6a24f3ec70d976f9be3ca4a7ec65ee27; the source manifest retains earlier marked/all-long dependencies and review hashes. The canonical exposition consolidates these accepted implications without strengthening them.

This closes only the once-counted distinct-port three-block family. Repeated-port reconnections, arbitrary path-pair permutations, overlaps among encounter families, growing encounter complexity and higher joint traces remain outside this proof. In particular the full signed remainder must still restore the super-Heisenberg plateau; the weighted local limit and BGS-TRACE-005 remain OPEN. No phase or noise average is used.
