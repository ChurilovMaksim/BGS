# Independent audit: rank-two four-cut classification

## Normalized claim and verdict

**Proved as written, by a computer-assisted finite proof with a valid universal reduction.** For two distinct reduced four-block decompositions with pairwise distinct port values, any specified rank-two relative position permutation between cyclically aligned equal outputs is the local alternating four-vertex relation in the candidate. It cannot be a three-cycle. The cut sets are exactly {s,s+1,s+4,z} and {s,s+3,s+4,z}, with z outside the cluster and its endpoint. The associated single local overlap indicator preserves cancellation on a long C or D link.

This is not a complete once-counted four-block-family estimate: higher-rank ambiguity, intersections and multiplicity corrections remain outside it.

Candidate SHA256: 186ed316e53053d310ed21af49fd05c845fd0b10bb4def309af33bac0ac80aac. Base: 0ffb20cc152d0ddd2620887e46d21d1120b95fd8. The audited source is preserved in the evidence provenance; this publication record is editorially curated from that audit.

## 1. Cycle semantics, all cyclic alignments, and equality labels

Write c(j)=j-1 modulo m. Enumerating the six rooted cyclic orders of four blocks shows only A D C B changes every original boundary. Its predecessors at the ordered heads h0,h1,h2,h3 are respectively c(h2),c(h3),c(h0),c(h1). Thus r=c h, with h=(h0 h2)(h1 h3). Each is a genuine change even for singleton blocks because different nonempty blocks have different final positions.

Given two cyclically aligned output position strings f,g, their label equality has relative position map tau=g composed with f inverse. Predecessor cycles obey r'=tau r tau^-1, independent of which common cyclic root was used. Conversely, such cycle conjugacy maps the whole oriented output cycle to the other; when labels are constant on tau-cycles it produces a valid cyclic label-word equality. Therefore predecessor enumeration covers all alignments rather than fixing an unsupported one.

Equality rank is m minus the number of cycles of tau. Rank two has exactly two possible nontrivial cycle types: one three-cycle, or two disjoint transpositions. Assigning one label per forced tau-cycle and distinct labels elsewhere preserves the equality and cannot destroy either existing distinct-port condition. Removing incidental equalities is therefore legitimate for the finite certificate. The classification concerns a specified rank-two relation; it need not be the only possible alignment for a word with additional coincidences.

## 2. Universal finite reduction: passed

From h'=c^-1 tau c h tau^-1, support(h') is contained in succ(S) union H union S. Hence T=S union succ(S) union H contains both H and H'. Its size is <=12 for two transpositions and <=10 for one three-cycle.

Retaining all cut heads ensures every source block of both decompositions remains nonempty. Contracting deleted interior vertices leaves the different predecessor tails at each genuine head distinct: they are last retained vertices of different nonempty blocks. At every other retained vertex, the source and corresponding output travel through the same block, so its predecessor remains unchanged. This proves the contracted changed-head sets are exactly H and H', not just subsets, and their cyclic order is preserved.

Since T contains all of S, every deleted vertex is fixed by tau and T is tau-invariant. Deletion from a cycle can be defined by taking the first retained predecessor encountered. That operation commutes with tau, so r'_T=tau r_T tau^-1. Each contracted cycle remains a single cycle. Support and rank of tau, both port-distinctness conditions, and the fact that H differs from H' all survive.

Four distinct port classes require at least four equality classes. Since rank is two, the contracted dimension is at least six. Thus the enumerated m>=5 ranges have a harmless extra empty case and do not miss a smaller kernel.

For lifting locality, if an internal gap between two successive supported vertices were nonempty, its first vertex would be succ(s) outside S and would be retained. It would remain between those vertices after contraction. Therefore compressed consecutive support cannot arise from a nonconsecutive original cluster. Once the four supported vertices are consecutive, succ(last) is also retained; the compressed s+4 head lifts to the actual immediate endpoint, not the far end of a deleted gap. The additional head z is retained as well. Thus the exact cut pattern, including its cluster endpoint, lifts to the original word. No arbitrary gap has silently been collapsed into a false short-word conclusion.

## 3. Finite-kernel coverage and independently executed evidence

The Python kernel enumerates all four-element supports, all three pairings, and all four-head sets for m=5,...,12. It also enumerates all three-element supports and both orientations for m=5,...,10. For each it computes the full conjugated predecessor array, extracts its actual changed-head set, requires exactly four distinct forced labels there, and checks the crossing-double-transposition formula. It tests the full local alternating pattern and BOTH exact head sets. Failures use explicit exceptions, not optimization-removable assertions.

The counts of raw possibilities are independently checked by binomial identities:
- 3 sum_(m=5)^12 binom(m,4)=3[binom(13,5)-binom(5,5)]=3858.
- 2 sum_(m=5)^10 binom(m,3)=2[binom(11,4)-binom(5,4)]=650.
The correct second count is 650 oriented three-cycles, not 6,503.

Independent reproduction ran the Python kernel and separately compiled and ran the C++ kernel using g++ -std=c++17 -O2 -Wall -Wextra -pedantic. Compilation produced a zero-byte warning log. Both returned 560 directed pair matches and zero three-cycle matches. The C++ code is a separate implementation of the same permutation mathematics; agreement alone is not treated as validation of the mathematical reduction.

Independent reproduction of the supplied direct cyclic-word grouping found: 3843 pair partitions at m=6,...,12, with 280 ambiguous output groups. Its original check only classified support locality. To close that coverage distinction, the independent direct-word checker constructs blocks as explicit position lists, permutes them in order 0,3,2,1, canonically roots the LABEL words, and groups equal outputs without predecessor-conjugacy formulas. It reconstructs the relative position permutation afterwards and checks its rank and both exact cut sets, with z explicitly excluded from the five-position cluster-plus-endpoint.

That independent checker found:
- 3843 pair partitions, 280 ambiguous output groups, 280 unordered pairs, all 280 passing the full exact classification;
- 315 three-equality partitions at m=6,...,10, no ambiguity.
The omitted m=5 cases have only three forced label classes and cannot support four distinct ports. The direct triple grouping covers both possible oriented relative maps by grouping all output equalities, although it enumerates the equality partition only once. The 280 unordered matches agree with 560 directed permutation matches.

These are exact integer/word computations, with no floating arithmetic or random sampling. Their universal force comes from Section 2, not from the counts alone.

## 4. The local overlap mask and uniform-link cancellation

For H={s,s+1,s+4,z}, write the source as a | b a b | C | D. The alternative cuts give a b a | b | C | D. Both reduce to the same output cycle, since their displayed outputs rotate respectively to D C b a b a. The mask is exactly the two equalities at positions s and s+2, and s+1 and s+3, together with the ordinary distinctness of a,b,c,d. No absence of additional coincidences is required.

The start ports of both representations are the same four labels a,b,c,d. Consequently the alternate distinct-port requirement introduces no new restriction on either long-block endpoint. The internal weights of C and D are their ordinary P-powers. In the A D C B ordering, the C endpoint has connector factor U_(u,d) conjugate(U_(u,b)); replacing its link by J gives delta_(d,b)/N=0. Likewise the D endpoint has U_(v,a) conjugate(U_(v,c)), whose uniform sum is delta_(a,c)/N=0. Both vanish by the original port distinctness.

A singleton C or D has endpoint equal to its start and cannot be treated as a free endpoint within this masked expression. The candidate explicitly avoids that error: choose the longer block, whose length is at least (m-4)/2 and is >=2 eventually. Its final vertex is a separate position not in the local equality mask. Its positive internal length permits the free endpoint sum after P^L is replaced by J.

The final explicit formula is also correct: the short internal edges contribute P_(b,a)P_(a,b), while the four connector pairs are U_(a,b)conjugate(U_(a,d)), U_(b,c)conjugate(U_(b,a)), U_(u,d)conjugate(U_(u,b)), and U_(v,a)conjugate(U_(v,c)). These are exactly the source order A B C D and output order A D C B. Replacing the longer link by Delta bounds its free endpoint sum by N||Delta||. The four port sums cost at most N^4, eight connector magnitudes cost q^4, the two short internal edges cost q^2, and the other long chain sums stochastically to one. Hence the residual is at most N^5 q^6 2^-max(L_C,L_D)<=C^6 N^-1 2^-((m-6)/2), since m=6+L_C+L_D. The estimate also permits the other link to have internal length zero. Any fixed polynomial number of starts/cuts preserves exponential band decay. This establishes a genuinely signed estimate for the full specified local overlap, with no K-uniqueness restriction or arbitrary canonical mask.

## Obligation matrix and remaining gap

Passed: unique reduced four-block cycle convention; all cyclic alignments; forced-label reduction; preservation of both genuine cut sets; compressed dimension bound; equality-rank preservation; nonlocal-gap witness and exact endpoint lifting; exhaustive coverage of both rank-two cycle types; exact finite checks in two languages and direct word representation; free long endpoint despite port distinctness.

Out of scope: higher-rank relations, masks requiring exact multiplicity or no other overlaps, unions/intersections of local events, three-or-more-short-block diagrams in a complete four-cut unmarking argument, arbitrary higher-r families and deterministic BGS. In particular, imposing an additional history-dependent canonicalization mask could destroy the endpoint sum again. The present classification does not justify that step.

## Reproduction artifacts and publication provenance

The [canonical classification](../mathematics/four_cut_rank_two_classification.md) is supported by the source snapshot and independent word results in [evidence provenance](../evidence/executions/20261006/four-cut-kernel/provenance/). The promoted portable Python and C++ controls reproduce the same finite counts; their new executions are in [the current receipt](../evidence/executions/20261006/four-cut-kernel/receipt.json). Historical audit coverage above is distinct from this later merged-module reproduction.

This publication record preserves the original mathematical findings and scope, while replacing private execution locations and first-person bookkeeping. The original review SHA256 and this curated record SHA256 are paired in [publication provenance](../evidence/executions/20261006/four-cut-kernel/publication_provenance.json). Original review hash: e5882116544f44789ceeec83b9fafea3b9c43fe05b53bdef79d296c072887ec5.
