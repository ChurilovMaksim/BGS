# Candidate: complete unmarked distinct-port three-block cancellation

Checkpoint RECONNECT-20261006-C; base0ffb20cc152d0ddd2620887e46d21d1120b95fd8. NEW AUTHOR PROOF, awaiting independent review. Earlier accepted files are unchanged. This is one fixed-complexity path-pair family, not full deterministic BGS.

## Claim

Let U_N be the actual frozen propagator. Use the proved subsidiary bounds q_N=max|U_xy|²<=C/N and ||P_N^L-J_N||<=2^-L eventually. Let T_m be the set of ordered coordinate-word pairs (x,y) for which some three cyclic nonempty blocks of x, with pairwise distinct initial vertex labels, reorder from A B C to A C B to give a cyclic rotation of y. Count each ordered pair once. Then for every smooth weight w compactly supported in (0,infinity),

N^-2 sum_m w(m/N) sum_((x,y) in T_m) a(x) conjugate(a(y)) ->0.

The proof below gives error O_w((log N)^5/N) plus superpolynomial and exponential terms. It is not an assertion that all noncyclic pairs belong to T_m, nor that the higher signed hierarchy vanishes.

Set K=ceil(log N), so on the fixed positive Heisenberg band m exceeds every fixed multiple of K eventually. Use K-uniqueness and the exact marked expression from the previous two notes.

## 1. Strengthening: two long blocks suffice for cut uniqueness

Suppose x is K-unique and at least two original blocks B,C have length>=4K; the third A need only be nonempty. An alternative triple may have any positive lengths.

As in the all-long proof, superimposing the alternative three cuts on y leaves a common K-anchor inside each of B,C. K-uniqueness identifies their exact x positions. The two anchors cannot lie in the same alternative block: the cyclic distance from the B-anchor to the C-anchor in y exceeds its distance in x by |A|, strictly between0 andm; a single forward block would preserve that distance.

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

All outputs of a K-unique x are primitive when m>6K: more than m/2 output K-substrings lie wholly inside shared blocks and are pairwise distinct. A nontrivial period would inject that set into its smaller complement. This is the same argument as in the all-long proof and does not require all blocks to be long.

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

Words that fail K-uniqueness have superpolynomially small normalized total absolute marked weight by the repeated-substring rank>=K/2 bound in long_block_unmarking.md. Its deliberately loose bound O(N^8 q^(K/2)) suffices unchanged.

For K-unique ambiguous words, section1 leaves only length triples with two short blocks, at most O(K²) possibilities. For each triple, section2 leaves O(K³) competing triples. Each imposes rank>=2 and costs absolute weight at most C³q² by sections3–4. Multiplying by the m² independent trace starts and the N^-2 band normalization (O(N) values of m) gives

O_w(N K^5 q²)=O_w(K^5/N).

This is an upper bound on the ambiguous marked mass, using a union bound over alternatives; overcounting is harmless here because this bound is absolute.

For every remaining K-unique unambiguous pair, primitivity of both words and uniqueness of the cut set give exactly three marked representations, from cyclic block labeling. Hence the actual unmarked sum is one third of the marked sum away from the bounded exceptional sets. Unmarked exceptional mass is at most its marked absolute mass because every member has a representation. Combining these estimates proves the claimed scoped family cancellation, subject to independent verification of the new combinatorial steps.

## 6. Finite discriminators and scope

check_short_blocks.py found a K=3-unique length12 ambiguous pair with cut triples(5,6,9),(5,8,9); short cluster a b a b, a!=b. Its arbitrary-long-C extension shows the mechanism survives large alphabet/dimension and has rank2. For this fixed short pattern, the preceding bound alone yields normalized O(1/N).

check_single_repeat.py exhausts all451 words consisting of otherwise distinct position labels with one pair identified, for m=4,...,14, and every cut triple. No admissible ambiguity occurs. This is diagnostic finite evidence; section3 supplies the general algebraic proof.

The two-long refinement, localization and rank argument are NEW, not covered by the earlier all-long independent audit. They require fresh review before promotion. Even if accepted, this closes only the three-block distinct-port family. General path-pair permutations, repeated-port sectors, intersections among different families, growing encounter complexity, super-Heisenberg plateau restoration and higher joint traces remain open.
