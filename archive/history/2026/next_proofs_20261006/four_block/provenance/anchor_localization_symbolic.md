# Symbolic competing-cut localization and three-anchor rigidity

Checkpoint RECONNECT-20261006-F. New author proof for independent review; no repository edits. Base0ffb20cc152d0ddd2620887e46d21d1120b95fd8. This note replaces no accepted artifact and asserts no full four-block spectral theorem.

## 1. Definitions

Let x be a cyclic word of length m, K-unique in the sense that all cyclic K-substrings have distinct starting positions. Two reduced r-block representations of the same cyclic output y give bijections f,g from SOURCE positions to OUTPUT positions. Choose their actual cyclic alignment so y_(f(i))=x_i=y_(g(i)). Each bijection is a translation modulo m on every one of its source blocks, and has a nonzero translation jump at each genuine source cut. Initial vertex values at the r cuts of EACH representation are pairwise distinct. The two block-order patterns may differ.

A common source refinement has at most2r intervals, obtained from the union of the two source cut sets. Put R=(r+1)K and assume m>2rR. Arguments concern discrete intervals of vertex positions, not real endpoints.

## 2. A long common source interval forces identical translations

Let I lie in one f-source block and one g-source block, with |I|>=R. Its g-image is a cyclic interval and meets at most r old OUTPUT cuts. Splitting at those cuts gives at most r+1 intervals, so one contains K consecutive output vertices. Its source preimage J under g has K consecutive vertices in I. On g(J), the inverse old map f^-1 is a translation because it lies within one old output block.

The same output substring is therefore the K-substring of x at J and at f^-1g(J). K-uniqueness identifies their source starts. Consequently f^-1g is the identity on J. Since f,g are translations on I, their offsets coincide on all of I.

Thus every common-refinement interval on which f!=g has length<R. The mismatch set D={i:f(i)!=g(i)} has cardinality at most2r(R-1). In particular it is not the entire circle.

## 3. Every mismatch component starts at a COMMON cut

Let u be the first source position of a connected component of D. Then f(u-1)=g(u-1), while f(u)!=g(u). Suppose f had no source cut at u. Then f(u)=f(u-1)+1. Necessarily g has a genuine source cut at u, since otherwise both maps would remain the same translation there.

The new block ending at u-1 is followed in OUTPUT order by a new block whose source head is v. Hence

g(v)=g(u-1)+1=f(u-1)+1=f(u).

Since g(u)!=f(u), v!=u. Both u and v are new cut heads. Equality of the output words gives x_u=y_(f(u))=y_(g(v))=x_v, contradicting the new distinct-port condition. Therefore f has a cut at u. Swapping f and g proves g has a cut there too.

So each mismatch component begins at a common old/new head. This is the step that handles arbitrarily short blocks; long-interval arguments alone do not justify localization.

Any new cut either lies in or at the right boundary of a mismatch component, or has matching maps on both sides. In the latter case its nonzero jump is also an old jump, so it is an old cut. In the former case it lies at forward distance at most|D| from that component's common starting cut. Consequently every new cut is within2r(r+1)K vertices of some old cut. The reverse statement is symmetric.

For fixed r there are therefore O_r(K^r) competing unordered source cut sets. There are only finitely many reduced block patterns for fixed r.

## 4. No extra cyclic-alignment factor

Given two cut sets and their block-order patterns, choose a deterministic longest interval in their common source refinement. Its length is at least m/(2r)>R. If the cyclic outputs can agree, section2 forces the translation offsets there to coincide. This prescribes their relative output-root shift uniquely, using only the cut geometry, before label assignments are summed. Thus the enumeration of possible equality graphs uses no additional factor m. This also includes degenerate equal lengths: no distinct-offset assumption was used.

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

## 6. Consequences for the four-block counting frontier

If a K-unique word has THREE original blocks of length>=5K, superimposing four alternative cuts gives a common K-anchor in each of them. K-uniqueness fixes their source positions, and section5 forces equality of cuts. Thus every ambiguous K-unique reduced four-block representation has at least TWO blocks shorter than5K. This is stronger than the previously available all-long conclusion.

There are O(K²m) such original length quadruples, O(K^4) competing cut sets by sections2–4, and at most one alignment per candidate. Rank>=3 equality graphs cost at most C^4 q³ under the start-first Markov estimate. After m² roots and N^-2 summation over m~N, their absolute marked mass is therefore

O_w(N² K^6 q³)=O_w(K^6/N).

This high-rank estimate NOW has an explicit competing-cut count; it must not be inferred from the earlier all-long lemma alone.

The remaining normalization-critical rank2 relations are the local abab events identified by the separately reviewed/awaiting-review finite classification, whose individual signed overlap sums have a free long endpoint and decay exponentially. To complete a once-counted four-block theorem still requires exact multiplicity/intersection accounting for those local events. No full four-block or BGS conclusion is asserted here before independent review of this symbolic note and that final accounting step.
