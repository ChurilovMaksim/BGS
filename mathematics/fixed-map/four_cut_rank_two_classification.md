# Rank-two four-cut classification

Status: computer-assisted mathematical proof, independently reviewed on 6 October 2026. The separate bounded Lean certificate is recorded as BGS-FORMAL-002; it does not formalize this universal reduction.

Canonical scope: a specified rank-two relation between reduced four-block decompositions with distinct ports. No full four-block unmarking or BGS claim is made here.

Source convention: source predecessor c(j)=j-1 modulo m and reduced output order A D C B. Composition acts right to left.

## Exact classification

For m>4, consider two DIFFERENT reduced four-block decompositions of the same cyclic coordinate-word pair, each with four pairwise distinct port values. Lift their equal output strings to source-position labels, after the actual cyclic alignment. Suppose the resulting relative permutation tau has equality rank2.

Then tau is a product of two transpositions, not a3-cycle. Its support is four CONSECUTIVE source vertices carrying alternating values a,b,a,b with a!=b. If the first position is s, the two cut sets are precisely

{s,s+1,s+4,z} and {s,s+3,s+4,z}

modulo m, for a fourth cut z outside that four-vertex cluster and its end. Thus the ambiguity is exactly the two splittings (a)|(b a b) and(a b a)|(b), with the same remaining C,D blocks. This is a statement about a specified rank2 relation between representations, not yet a complete unmarking theorem at r=4.

## 1. Cycle conventions and all alignments

Let c(j)=j-1 modm be the original predecessor m-cycle on source positions. For four cut heads H={h0,h1,h2,h3} in cyclic order, the unique reduced one-trace ordering is A D C B. Its predecessor cycle is r=c h where h=(h0 h2)(h1 h3). Every head in H genuinely changes predecessor, including singleton blocks; every other head retains its predecessor.

An equality of the two output label words under ANY cyclic alignment gives a relative source-position bijection tau and r'=tau r tau^-1. Equality rank2 means either tau is a3-cycle or it is two disjoint transpositions. These are all possibilities since rank=m-number_of_cycles. Root positions do not appear in the predecessor-cycle relation, so this formulation includes all cyclic alignments rather than fixing an arbitrary root.

The label equality classes are the cycles of tau. Other incidental label equalities may be removed by assigning fresh labels outside these classes. This cannot spoil either distinct-port condition. Thus finite enumeration may use exactly these forced identifications, with every other source position given its own label.

## 2. Bounded reduction preserving GENUINE cuts

Put S=support(tau), and let succ=c^-1 be the original source successor. Since h'=c^-1 r'=c^-1 tau c h tau^-1, its support H' is contained in S union succ(S) union H. Preserve the vertex set

T=S union succ(S) union H.

Its size is at most12 for two transpositions and at most10 for a3-cycle. In particular T contains BOTH cut-head sets H,H'. Contract all other vertices in the source and the two output cycles.

Why genuine cut status survives, rather than only abstract conjugacy: for the first decomposition, each maximal shared block has its initial cut head in H retained. Deleting interior vertices shortens that block but never erases it. Its last retained vertex is consequently distinct from the last retained vertex of every other block. At a cut head, the source and reordered output use predecessor tails belonging to different blocks; these remain different after contraction. At a non-cut retained head, source and output traverse the same retained portion of one block, so no new predecessor change is introduced. Therefore the contracted first decomposition has EXACTLY H as genuine cuts. Apply the identical argument with H' to the second decomposition; T contains H' as proved above. Both retain their cyclic order and the crossing double-transposition predecessor formula.

The set T is tau-invariant, since it contains S and tau fixes its complement. Deleting the same tau-fixed vertices from conjugate cycles commutes with conjugation, so the contracted cycles still satisfy r'_T=tau r_T tau^-1. Both remain single cycles. Labels at the retained cut heads and both distinct-port conditions are unchanged.

Preserving succ(S) is also important for lifting the conclusion. If two successive supported positions had a nonempty source gap, the immediate successor of its first supported position is outside S and is retained. Thus a nonconsecutive support cannot become four consecutive positions after contraction. Likewise the preserved immediate successor of the final supported position ensures the endpoint s+4 in the kernel lifts to the ACTUAL immediate endpoint of the four-vertex cluster. The fourth cut z is retained. Therefore both the consecutive-support conclusion and the displayed exact cut form lift without expanding a short cluster into a long word.

Any counterexample to the classification consequently has a reduced counterexample with m<=12 or m<=10, respectively. Four distinct port classes imply m>=5 (indeed>=6 in the nonempty rank2 cases), so the finite ranges below cover all reduced cases. This reduction, rather than the raw success count, makes the exhaustive kernel sufficient for the stated universal classification.

## 3. Executed exhaustive kernel and independent representations

`computations/verification/four_cut_rank_two_kernel.py` enumerates:

- every size-four support and all three pairings, for m=5,...,12;
- every size-three support and BOTH3-cycle orientations, for m=5,...,10;
- every four-head set H with distinct forced labels;
- r=c h, r'=tau r tau^-1, and its actual changed-head set H';
- only cases with exactly four changed heads, distinct forced labels at H', and the crossing double-transposition formula on H'.

Every surviving pair is checked against the full local alternating classification and exact two cut sets, not merely a locality score. Results:3858 pair partitions,560 directed matches, all of the prescribed local form;650 oriented3-cycles, no matches. Failures raise explicit exceptions, independent of Python optimization mode.

`computations/cpp/four_cut_rank_two_kernel.cpp` independently implements this permutation enumeration using exact integers. It compiles under g++ -std=c++17 -O2 -Wall -Wextra -pedantic with no warnings after indentation cleanup. Its outputs agree:3858/560 and650/0. No floating point, randomized sampling or external algebra library is used.

As an orthogonal representation check, the historical `classify_rank_two_kernel.py` directly constructs cyclic label WORDS and groups their reordered outputs, without predecessor-conjugacy formulas. It exhausts3843 pair partitions for m=6,...,12 and finds280 unordered ambiguous outputs, all with consecutive support. This matches560 directed permutation matches; the missing15 partitions at m=5 have too few distinct labels for four distinct ports and produce no matches. Earlier direct word checks of triple equality through m=12 also found no ambiguity.

The reduction and kernel semantics have now passed independent internal review. The universal mathematical classification combines that reviewed reduction with exact finite computation. The separately compiled Lean module certifies only its bounded executable predicates, not this universal argument.


## 4. Source correspondence and formal boundary

The maintained Python checker is `computations/verification/four_cut_rank_two_kernel.py`; its C++ control is `computations/cpp/four_cut_rank_two_kernel.cpp`. Both preserve the reviewed acceptance predicate and use explicit exceptions, never optimization-removable assertions. The portable runner `computations/verification/run_four_cut_kernel.py` executes normal and optimized Python, compiles and runs C++ with NDEBUG enabled, compares exact counts, and optionally requires the pinned Lean build. No build is silently skipped.

In `formalization/Bgs/FourCutKernel.lean`, `choose`, `pairClasses` and `tripleClasses` enumerate supports, the three pairings and both orientations. `label` gives each forced class one representative, `tau` maps each class cyclically and `tauInv` reverses its orientation. `crossing` exchanges opposite cyclic heads. `testHeads` computes tau composed with c composed with crossing(H) composed with tau inverse, recovers ALL changed predecessor positions H', and checks four distinct ports and the second crossing formula. `localForm` checks four consecutive alternating positions and both displayed head sets.

Subtle endpoint exclusion: `localForm` alone does not exclude z=s+2. Accepted heads have distinct forced labels, so z=s+2 would put equal labels at s and s+2 into one proposed head set and is impossible. Distinct candidate heads exclude z=s,s+1,s+3,s+4. The conclusion follows from the complete accepted predicate, not `localForm` alone.

The namespace `Bgs.FourCutKernel` contains exactly four theorem certificates: pair configurations 5..12 equal (3858,560,true), oriented triples 5..10 equal (650,0,true), and the ordinary-decide m=4 exclusions (3,0,true), (8,0,true). The first two use native_decide and declare that trust extension in printed axiom lists; m=4 uses ordinary decide. Abstract contraction/lifting, list-enumerator completeness as mathematical theorems, cyclic-word correspondence, analytic link cancellation and asymptotics remain unformalized. A source file or successful build does not strengthen this scope.

## 5. Independent review and provenance

See `record/four_cut_rank_two_review_20261006.md` for the mathematical audit and `record/four_cut_lean_review_20261006.md` for the fresh semantic Lean audit. The latter independently compared 7586 Lean/Python direct-word rows at m=4..7, including genuine changed-head sets and explicit forbidden endpoints. Earlier full direct-word verification found 280 unordered matches versus the 560 directed matches here. Those historical reviews are publication-facing curated records; their original and curated hashes are paired explicitly, without changing their mathematical findings or execution scope. The new merged-module execution is separately recorded in `evidence/executions/20261006/four-cut-kernel/`.
