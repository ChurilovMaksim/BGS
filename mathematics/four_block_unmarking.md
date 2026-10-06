# Once-counted reduced distinct-port four-block cancellation

Proposed claim BGS-TRACE-016. Base:0ffb20cc152d0ddd2620887e46d21d1120b95fd8. Project analytic proof with independent internal review and a separately scoped computer-assisted classification input. No external referee, global priority, or full analytic formalization claim.

## 1. Objects, hypotheses and theorem

Let U_N be unitary and put P_N(x,y)=|U_N(x,y)|², J_N(x,y)=1/N. Assume q_N=max P_N(x,y)<=C/N and, for all sufficiently large N, ||P_N^L-J_N||op<=2^-L simultaneously for every integer L>=0. The generic theorem below uses only these hypotheses and unitarity. BGS-FM-021, `position_chain_mixing.md`, supplies them for the unchanged odd-dimensional U_N=exp(i10^-80 N A_N)M_N of `fixed_map_path_model.md`. They are not a spectral-universality criterion and can hold for spectrally nonuniversal families.

A rooted coordinate word is x=(x_0,...,x_(m-1)) in {0,...,N-1}^m. Put x_m=x_0 and a(x)=product_(j=0)^(m-1) U_(x_j,x_(j+1)). To define T_m^(4), choose four DISTINCT SOURCE POSITIONS on the oriented index circle of x; cyclically label the four intervening nonempty contiguous blocks A,B,C,D. Require their INITIAL VERTEX VALUES to be pairwise distinct. A rooted pair (x,y) belongs to T_m^(4) exactly when y is one of the rooted cyclic rotations of A D C B for at least one such cut choice. T_m^(4) is a SET of ordered tuples: multiple cut witnesses or block labels never create extra elements. For m<4 it is empty. Write W(x,y)=a(x)conjugate(a(y)).

The ordering A D C B is genuinely reduced: none of the original four block-successor boundaries is retained. It is the only reduced one-cycle ordering on four cyclically labeled blocks. Contracting an unchanged boundary before imposing distinctness on genuine ports would lower the number of blocks; artificial interior marks with distinctness constraints cannot be silently erased.

For every smooth w compactly supported in (0,infinity),

N^-2 sum_m w(m/N) sum_((x,y) in T_m^(4)) W(x,y) ->0.

More precisely, if supp(w) is contained in [a,b] with0<a<b, K=ceil(log N), and N is sufficiently large, the absolute value of this COMPLETE signed band sum is at most

O_w(K^10/N)+O_w(N^10(C/N)^(K/2))+O_w(N^5 2^(-(aN-4)/4)).

Constants may depend on the fixed matrix-family bounds and w. The startup threshold inherited from FM-021 is not effective. This controls one once-counted family; it neither exhausts the trace expansion nor justifies truncating growing reconnection complexity.

The classification input is `four_cut_rank_two_classification.md`. Its universal statement is a computer-assisted theorem consisting of an independently audited mathematical compression/cyclic-word reduction and an exact bounded kernel. `../formalization/Bgs/FourCutKernel.lean` certifies only the bounded kernel proposition described in that source; the universal compression and the analytic proof here remain unformalized.

## 2. Marked and local-overlap contractions

Index blocks modulo4, with old successor i+1 and new successor i-1. For nonnegative internal link lengths L_i define

E(L)=sum_(a1,a2,a3,a4 distinct; b1,b2,b3,b4) product_i [(P^Li)_(ai,bi) U_(bi,a_(i+1)) conjugate(U_(bi,a_(i-1)))].

Expanding each Markov power represents the common internal path in its block, of vertex length L_i+1. Define M_m=m² sum_(sum Li=m-4) E(L). The m² choices are independent trace roots WITH multiplicity. This is not yet a once-counted pair sum.

If any one link is J, summing its b_i gives delta_(a_(i+1),a_(i-1))/N=0 by unitarity and distinct ports. Replace the longest link by P^L-J. Its entries are bounded by2^-L; the eight connector magnitudes cost q^4; sum the other three stochastic rows. Thus

|E(L)|<=N^5q^4 2^-max Li<=C^4N2^-max Li.

There are binom(m-1,3) compositions, so the normalized marked band sum is O_w(N^5 2^(-(aN-4)/4)), including every zero internal length.

Let O_m be the marked subcollection with A=(a), B=(b,a,b), and arbitrary nonempty C,D. For LC+LD=m-6 its local contraction is

E_local(LC,LD)=sum_(a,b,c,d distinct; u,v) P_(b,a)P_(a,b)(P^LC)_(c,u)(P^LD)_(d,v)
  U_(a,b)conjugate(U_(a,d)) U_(b,c)conjugate(U_(b,a))
  U_(u,d)conjugate(U_(u,b)) U_(v,a)conjugate(U_(v,c)),

and O_m=m² sum E_local. Uniform C gives delta_(d,b)/N=0; uniform D gives delta_(a,c)/N=0. The two short-edge probabilities cost q², eight connectors cost q^4, and the remaining sums cost at most N^5 after the other stochastic row is summed. Therefore

|E_local|<=N^5q^6 2^-max(LC,LD)<=C^6N^-1 2^(-(m-6)/2).

O_m consequently has an exponentially small normalized band sum. It is literally a subcollection of the parameter tuples in M_m, a fact used below for exceptional words.

## 3. Equality budgets, primitivity and rank-one exclusion

A cyclic word x is K-unique when its m cyclic length-K vertex substrings are pairwise distinct; equivalently, equal K-words imply equal starting positions. If two distinct starts have equal K-substrings, their K equality edges form a graph of maximum degree2, with no loops or repeated unordered edges when K<=m/4. Its paths and simple cycles impose equality rank at least K/2. Reveal the four open chains sequentially: at most four forced visits can occur at chain starts; each remaining forced transition costs q. Together with q^4 connectors, the fixed-length exceptional weight is at most N^4 q^(K/2) for K>=8. Fewer than m² substring-start pairs, O(m³) length quadruples, m² roots and the N^-2 band normalization give O_w(N^10 q^(K/2)). This is an absolute bound only on the exceptional set, not the complete spectral sum.

K-unique x is primitive. Every four-block output y is also primitive for m>8K: at least m-4(K-1)>m/2 output K-substrings remain inside shared blocks and are pairwise distinct. A nonzero period would inject these positions into their smaller complement, impossible.

For a general equality graph of rank s, its four starting vertices must lie in different equality classes or the distinct-port sum is zero. Fix all four start labels first (at most N^4 choices), then reveal internal transitions in forward chain order. Exactly s subsequent visits are forced to already known class values, each costing at most q; fixing starts changes no row transition law. Including connectors gives absolute weight<=N^4q^(s+4)<=C^4q^s. No independence of overlapping equality events is assumed.

Two aligned positional outputs induce a relative source permutation tau. Its equality rank is m minus its number of cycles. Rank0 means the same positional output cycle and hence the same genuine cut set. Rank1 is impossible for distinct admissible cut sets. Indeed tau=(p q) forces x_p=x_q. Let c be the original predecessor m-cycle and r the first output predecessor cycle; the second is r'=tau r tau. The first distinct-port condition leaves at least one of p,q uncut, say q, so r(q)=c(q)=s. If r'(p)=c(p), then tau(s)=c(p): for s outside{p,q} this violates injectivity of c, while s=p creates a2-cycle and s=q a fixed point. If r'(q)=c(q), then r(p)=tau(s): for s outside{p,q} this violates injectivity of r, while s=p creates a2-cycle and s=q is again impossible. Thus both p,q are new cut heads, contradicting the second distinct-port condition. Here m>2, as throughout the eventual band.

## 4. Symbolic competing-cut localization: definitions

Let x be a cyclic word of length m, K-unique in the sense that its m cyclic length-K vertex substrings are pairwise distinct; equal K-words therefore imply equal starts. Two reduced r-block representations of the same cyclic output y give bijections f,g from SOURCE positions to OUTPUT positions. Choose their actual cyclic alignment so y_(f(i))=x_i=y_(g(i)). Each bijection is a translation modulo m on every one of its source blocks, and has a nonzero translation jump at each genuine source cut. Initial vertex values at the r cuts of EACH representation are pairwise distinct. The two block-order patterns may differ.

A common source refinement has at most2r intervals, obtained from the union of the two source cut sets. Put R=(r+1)K and assume m>2rR. Arguments concern discrete intervals of vertex positions, not real endpoints.

### 4.1. A long common source interval forces identical translations

Let I lie in one f-source block and one g-source block, with |I|>=R. Its g-image is a cyclic interval and meets at most r old OUTPUT cuts. Splitting at those cuts gives at most r+1 intervals, so one contains K consecutive output vertices. Its source preimage J under g has K consecutive vertices in I. On g(J), the inverse old map f^-1 is a translation because it lies within one old output block.

The same output substring is therefore the K-substring of x at J and at f^-1g(J). K-uniqueness identifies their source starts. Consequently f^-1g is the identity on J. Since f,g are translations on I, their offsets coincide on all of I.

Thus every common-refinement interval on which f!=g has length<R. The mismatch set D={i:f(i)!=g(i)} has cardinality at most2r(R-1). In particular it is not the entire circle.

### 4.2. Every mismatch component starts at a COMMON cut

Let u be the first source position of a connected component of D. Then f(u-1)=g(u-1), while f(u)!=g(u). Suppose f had no source cut at u. Then f(u)=f(u-1)+1. Necessarily g has a genuine source cut at u, since otherwise both maps would remain the same translation there.

The new block ending at u-1 is followed in OUTPUT order by a new block whose source head is v. Hence

g(v)=g(u-1)+1=f(u-1)+1=f(u).

Since g(u)!=f(u), v!=u. Both u and v are new cut heads. Equality of the output words gives x_u=y_(f(u))=y_(g(v))=x_v, contradicting the new distinct-port condition. Therefore f has a cut at u. Swapping f and g proves g has a cut there too.

So each mismatch component begins at a common old/new head. This is the step that handles arbitrarily short blocks; long-interval arguments alone do not justify localization.

Any new cut either lies in or at the right boundary of a mismatch component, or has matching maps on both sides. In the latter case its nonzero jump is also an old jump, so it is an old cut. In the former case it lies at forward distance at most|D| from that component's common starting cut. Consequently every new cut is within2r(r+1)K vertices of some old cut. The reverse statement is symmetric.

For fixed r there are therefore O_r(K^r) competing unordered source cut sets. There are only finitely many reduced block patterns for fixed r.

### 4.3. No extra cyclic-alignment factor

Given two cut sets and their block-order patterns, choose a deterministic longest interval in their common source refinement. Its length is at least m/(2r)>R. If the cyclic outputs can agree, the long-interval argument forces the translation offsets there to coincide. This prescribes their relative output-root shift uniquely, using only the cut geometry, before label assignments are summed. Thus the enumeration of possible equality graphs uses no additional factor m. This also includes degenerate equal lengths: no distinct-offset assumption was used.

## 5. Three fixed anchors rigidify a reduced four-block reversal

For four reduced blocks, the only one-cycle ordering with every boundary changed is A D C B. Suppose two representations have fixed common source positions inside THREE different original blocks. The three anchors occur in reverse cyclic order in y compared with x. Thus no alternative block can contain two anchors: any such block would preserve their order along with the third anchor, contradicting the reversed three-anchor cyclic order. Each of three alternative blocks contains one anchor, and the fourth contains none.

Choose anchors X,Y,Z in original blocks B,C,D. They denote specified source/output POSITIONS; their single vertex labels need not differ. Write the source arcs and original block cuts as

x=X u Y v Z w,
u=u1 u2, v=v1 v2, w=w1 A w2.

Here A is the nonempty unanchored original block. The other source blocks are w2 X u1, u2 Y v1, v2 Z w1. The original y, rooted at X, is

X [u1 A v2] Z [w1 u2] Y [v1 w2].

All displayed prefix/suffix words may be empty; A is not. The alternative unanchored block E lies in exactly one of the three source anchor gaps. The following exhaustive word-equation cases prove it must equal A with identical cuts. Every use of a first letter below follows a nonempty word T,A or E, so empty prefix pieces cause no exception.

### Case W: E lies in the same gap w

Write u=p1 p2, v=q1 q2, w=r1 E r2. Output equality gives

u1 A v2=p1 E q2, w1 u2=r1 p2, v1 w2=q1 r2.

Compare v1v2=q1q2 and v1w2=q1r2. If q1=v1T with T nonempty, then v2=Tq2 and w2=Tr2, identifying the old B and D first letters. If v1=q1T, then q2=Tv2 and r2=Tw2, identifying the new B and D first letters. Both violate distinct ports. Hence q1=v1,q2=v2,r2=w2.

Now w1 A=r1 E and w1 u2=r1 p2. If r1=w1T nontrivially, A=TE and u2=Tp2, identifying old A,C ports. If w1=r1T, E=TA and p2=Tu2, identifying new E,C ports. Therefore r1=w1,E=A,p2=u2, and u=p1p2 forces p1=u1. Every cut is unchanged.

### Case U: E lies in gap u

Write u=p1 E p2, v=q1q2, w=r1r2. The alternative source block order, starting with the X-anchored block, is (r2 X p1), E, (p2 Y q1), (q2 Z r1). Its reduced reverse ordering rooted at X is

X [p1 q2] Z [r1 p2] Y [q1 E r2].

Thus the CORRECT output equations are

u1 A v2=p1 q2, w1 u2=r1 p2, v1 w2=q1 E r2.

Compare the prefixes q1,v1 of the common source arc v=v1v2=q1q2.

- If q1=v1 T with T nonempty, then v2=Tq2 and w2=T E r2. The old D and B blocks have the same first letter, violating old distinct ports.
- If v1=q1 T with T nonempty, then q2=T v2 and E r2=T w2. Since E is nonempty, the new D and E blocks have the same first letter, violating new distinct ports.
- If q1=v1, then q2=v2 and w2=E r2. Source equality w1 A w2=r1r2 right-cancels to r1=w1 A E. The second output equation gives u2=A E p2. Hence old C and A have the same first letter, again forbidden.

Every case is impossible. Empty prefix or suffix pieces are allowed; all first-letter comparisons use an explicitly nonempty T, A or E.

### Case V: E lies in gap v

Write u=p1p2, v=q1 E q2, w=r1r2. The alternative source block order is (r2 X p1), (p2 Y q1), E, (q2 Z r1). Its reduced reverse ordering rooted at X is

X [p1 q2] Z [r1 E p2] Y [q1 r2].

Thus the CORRECT output equations are

u1 A v2=p1 q2, w1 u2=r1 E p2, v1 w2=q1 r2.

Compare prefixes p1,u1 of the source arc u=u1u2=p1p2.

- If p1=u1 T with T nonempty, then u2=Tp2. The first output equation gives A v2=Tq2. Thus old C and A have the same first letter, forbidden by old distinct ports.
- Otherwise write u1=p1 T, allowing T to be empty. Then p2=T u2. The second output equation right-cancels to w1=r1 E T. Source equality for w then gives r2=E T A w2. The new X-anchored block B and the new block E have the same first letter, because E is nonempty. This violates new distinct ports.

Again every case is impossible, including equality of the compared prefix lengths.

This proves three-anchor rigidity without unequal-length or generic-position assumptions. It is a symbolic word proof, not extrapolation from the finite three-anchor searches.

## 6. High-rank exceptional mass

The repeated-K-substring estimate for r=4 bounds the complete non-K-unique marked absolute band mass by O_w(N^10q^(K/2)), superpolynomially small. Any unmarked exceptional pair has at least one marked parameter tuple, so its absolute weight is bounded by that marked exceptional mass. O_m's exceptional absolute mass is also bounded by it, since O_m is a marked subcollection. Thus all comparisons below may first be made on K-unique x, then extended with only a constant multiple of that superpolynomial error, without assumptions on periodic exceptional words.

K-unique x and all its four-block outputs are primitive once m>8K: at least m-4(K-1)>m/2 output K-substrings lie inside shared blocks and are distinct. For such a fixed rooted ordered pair let r(x,y) be the number of admissible unordered cut sets. Each cut set gives exactly FOUR marked parameter tuples, from cyclic block labels, and no extra root stabilizer.

If three original blocks have length at least 5K, superimpose the four alternative output cuts on each. One of at most five pieces contains a common K-anchor. Equality of output substrings and K-uniqueness identify its exact source position. Section 5 then gives uniqueness. Together with Section 4 this establishes:

- if three original blocks have length>=5K, their fixed common anchors force uniqueness;
- every competing cut lies O(K) from some original cut, so there are O(K^4) alternatives;
- a deterministic long common source interval uniquely fixes the cyclic alignment.

Therefore an ambiguous original representation has two short lengths, giving O(K²m) original length quadruples. Each alternative imposing equality rank>=3 costs at most C^4q³, by exposing the four starts first. Together with O(K^4) alternatives, m² trace roots and the normalized band sum, the absolute marked mass of representations participating in at least one rank>=3 relation is

B=O_w(N²K^6q³)=O_w(K^6/N).

Every pair has r(x,y)<=R_K=O(K^4), by localization relative to any one of its cut sets.

## 7. Rank-two representation graph and absence of triangles

For one K-unique rooted pair make a graph whose vertices are its admissible cut sets; join two vertices when their relative positional equality rank is2. Distinct vertices cannot have rank0, and rank1 is excluded by the general predecessor-transposition argument. All nonedges therefore have rank>=3.

The separately scoped rank-two classification says every edge is a local abab flip, with relative permutation

tau_s=(s,s+2)(s+1,s+3)

on four consecutive source positions. Its cut sets are {s,s+1,s+4,z} and {s,s+3,s+4,z}. For m>8 the start s is unique, so the marked local-overlap subcollection O_m counts each UNORDERED graph edge exactly once: choose the endpoint having the singleton A and the length-three B. The two independent trace roots are then uniquely determined by the rooted pair's primitive words.

This graph has no triangle. Relative permutations along two distinct edges from one vertex are tau_s,tau_t. If s=t, the other vertices coincide, since their aligned positional outputs coincide. For distinct s,t, their product has rank4 unless the starts are cyclic neighbors. In the neighbor case the product is a3-cycle, of rank2; that relative type is forbidden by the same rank-two classification. These possibilities follow directly by multiplying the two products of transpositions: displacement1 gives one3-cycle, displacement2 gives two3-cycles, displacement3 gives a3-cycle and two transpositions, and disjoint supports give four transpositions. Negative cyclic displacements are inverses of these cases. Thus no third rank-two edge can close a triangle.

## 8. Exact once-counting correction and error control

Call a pair good if no two of its representations have rank>=3. Its representation graph is complete, hence by triangle-freeness it has r=1 or2. If e is its number of rank-two edges, then r-e=1. Consequently its once-counted contribution equals its contribution to M_m/4 minus its contribution to O_m.

For a bad pair, let r_hi be the number of graph vertices incident to a rank>=3 relation. At most one vertex can have no such relation: two vertices adjacent by rank2 to every other vertex would form a rank-two triangle with any third. Thus r_hi>=r-1>=r/2 (the case r=2 with a high-rank relation has both vertices participating). The high-rank marked bound B therefore controls the entire bad-pair marked mass up to a factor2.

For any bad pair,

|1-r+e|<=1+r+binom(r,2)<=O(R_K)r.

Summing these errors costs O(R_K)B=O_w(K^10/N). No universal division by four is used on the bad set, and no unproved truncation of inclusion-exclusion is needed.

On non-K-unique pairs, compare the actual once-counted sum directly with M_m/4-O_m. Each of its three absolute masses is bounded by the complete exceptional marked mass, the last because O_m is a literal marked subcollection. This remains valid for periodic words and varying root multiplicities. The extra error stays O_w(N^10q^(K/2)).

Combining with the exponential marked and local-overlap estimates proves the stated scoped theorem. The corrected symbolic chain and this multiplicity argument are independently accepted in `../record/four_block_independent_review_20261006.md`. The earlier three-block theorem is unchanged.

## 9. Verification, provenance and precise boundary

The portable entry checker is `../computations/verification/four_block_unmarking.py`. It checks corrected U/V block placement with empty pieces, exact local uniform-link contractions, the local-transposition graph algebra, finite graph correction inequalities and a concrete rank-two overlap. It has a proper main entry point and explicit RuntimeError checks that survive optimized Python. Its finite results do not prove analytic limits. Evidence: `../evidence/executions/20261006/four-block/receipt.json`.

The accepted corrected symbolic source has SHA256 cb7b2591204aaaf04a84388e55eb8dcb37963f8777e94ce26f248008b241e9a6; the accepted once-counting candidate has b40c0122dc1ed60c31c8eaccf270a643dcd6776e0799cf2686651b258a7c5473. Final repaired-source acceptance has a5515224f61335b27d570cd1b31e9108a51caff9d76fe5fcd78e1c674f0500f1. The original U/V placement error, original review and exact correction are retained only as dated provenance. No incorrect U/V equations are active proof inputs.

The four-cut classification is owned by its separate canonical proof and bounded formal module; this theorem does not duplicate their executable kernels or claim their bounded certificate formalizes the universal compression or this analytic chain.

This result controls only the reduced distinct-port four-block family. Repeated genuine ports, non-permutation path pairs, overlaps between different families, r>=5 short-cluster unmarking, growing complexity and the complete signed trace hierarchy remain open. The independently checked microscopic-rounding obstruction shows that coarse flatness/mixing/path bounds cannot alone prove the exact spectral target. Any full-target continuation must exploit exact quantization or phase information beyond these generic hypotheses. BGS-TRACE-005 and BGS-BGS-001 remain OPEN.
