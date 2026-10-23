# Independent semantic audit of the bounded four-cut Lean certificate

## Normalized claim and verdict

**Computationally verified only in a stated range.** The Lean sources faithfully encode the independently reviewed finite rank-two predicate: for every two-transposition support/classes and four-head set at 5 <= m <= 12, all 560 accepted directed matches have the exact local alternating form; for every oriented three-cycle and four-head set at 5 <= m <= 10 there are no accepted matches. Configuration totals are 3858 and 650. The m=4 exclusions also compile by ordinary `decide`. No semantic defect was found.

This is a fresh isolated semantic review and reproduction, not merely acceptance of the earlier audit's verdict. The abstract contraction/lifting argument, correspondence theorem between arbitrary cyclic words and list encodings, and analytic BGS statements are NOT formalized in these Lean files. The full Boolean certificates use Lean's declared native-evaluation trust extension.

## Dependencies

1. Mathematical source: [canonical classification](../mathematics/four_cut_rank_two_classification.md), supported by the [independent mathematical review](four_cut_rank_two_review_20261006.md).
2. Finite model: source positions 0,...,m-1, predecessor c(x)=x-1 mod m, four increasing heads, equality classes of a rank-two permutation.
3. Executable translation in `FourCut.lean`, semantically checked below.
4. `Certificate.lean` supplies finite Boolean equalities using `native_decide`; `Endpoint.lean` supplies m=4 equalities using ordinary `decide`.
5. Universal claims additionally require the abstract reduction and lifting, outside the formal certificate. Analytic consequences require still further arguments.

## Semantic obligations

### Enumeration: passed

The recursive choose function includes a chosen first element or excludes it. On an increasing duplicate-free range this yields each increasing k-element subset exactly once, by induction on the input list. Pair supports have four elements and the three pairings exhaust the three fixed-point-free involutions. Triple supports have three elements and both cyclic orientations are present. No rank-two cycle type is omitted: rank is the sum of cycle lengths minus one over nontrivial cycles. Every possible first four-head set is enumerated. Sorted cyclic order picks a root but does not restrict head sets; crossing opposite heads is invariant under rotating the four ordered heads.

`through` includes exactly 5,...,maxSize. Configuration counts independently equal 3*sum(C(m,4),m=5..12)=3858 and 2*sum(C(m,3),m=5..10)=650. `Stats.add` sums exact natural numbers and ANDs all validity flags, so its final true flag cannot hide a false case. Rejected candidates contribute neutral statistics. Identical accepted head sets are NOT silently discarded: they make validity false, a harmless stronger assertion than the distinct-decomposition theorem requires.

### Permutation and label orientation: passed

Generated classes are disjoint and internally duplicate-free. `cycleMap` sends each class entry to its next entry, including the wraparound. `tau` composes these disjoint cycles; reversing each cycle gives the true inverse. Reversing the order of cycles is unnecessary because disjoint cycles commute. `label` maps a whole class to its first entry and fixes every outside vertex; distinct classes cannot share representatives. Thus these labels express exactly the forced equality relation, and no accidental additional equality.

For h=[a,b,c,d], `crossing` is (a c)(b d). `pred(crossing h x)` equals c composed with h, not its reverse. The conjugate computed by Lean is precisely tau composed with c composed with crossing(H) composed with tau inverse. Natural subtraction in `(x+m-1)%m` is ordinary modular predecessor on all enumerated m>=4; no truncation corner is involved.

Independently, form the four nonempty source blocks and concatenate them as A,D,C,B. Its predecessor at a,b,c,d is respectively c(c),c(d),c(a),c(b), and at every other position it is the source predecessor. Applying tau to the entire position word conjugates its predecessor by tau in exactly the encoded direction. This independently checks the permutation convention rather than copying its formula.

### Genuine heads and all cyclic alignments: passed

H' is extracted from ALL m positions at which the conjugated predecessor differs from the source predecessor. Exactly four changes, distinct forced port labels, and equality with c composed with crossing(H') at every position are required. H' is sorted by the range filter. Therefore it is an actual genuine cut set, not a guessed witness. The first head set is genuine because four nonempty source blocks have four different predecessor tails, including singleton blocks. The crossing cycle is a single output cycle by its explicit ADCB construction.

Cycle conjugacy removes the arbitrary output root: applying tau to one directed position cycle gives the other if and only if the two resulting lists agree after a cyclic rotation. Label constancy on tau cycles then gives equal cyclic label words. Conversely, an aligned cyclic output equality gives the relative map tau and this conjugacy. Thus every specified rank-two cyclic alignment is covered; no need to enumerate an extra root parameter. This correspondence is semantically checked here, not a Lean theorem.

### Exact local pattern, forbidden endpoint and ports: passed

`localForm` requires support equal to four consecutive modular positions, equalities at offsets 0/2 and 1/3, and inequality between these pairs. It then requires BOTH exact cut sets {s,s+1,s+4,z} and {s,s+3,s+4,z}, allowing either ordering. No mere locality score is substituted.

Subtle point: `localForm` alone does not explicitly exclude z=s+2. Distinctness of its two candidate head lists excludes z=s,s+1,s+3,s+4. In an ACCEPTED case, the first and second head sets already have distinct forced labels. If z=s+2, either proposed head set contains both s and s+2 with the same label. Hence acceptance excludes the remaining forbidden position. The full accepted predicate therefore implies exactly z outside the four-vertex support AND its endpoint. It would be incorrect to claim this exclusion for `localForm` in isolation; this does not weaken the actual certificate. `sameSet` ignores multiplicity, but all relevant generated heads and local candidate heads are duplicate-free, so this is appropriate.

### Small dimensions: passed

At m=4 ordinary `decide` verifies 3 pair configurations and 8 oriented triple configurations, each with zero matches. Four distinct heads do not exist below m=4. More sharply, rank-two forced classes leave m-2 labels, so four distinct ports need m>=6. Thus m=5 is a harmless empty extra case, and neither the original m>4 theorem nor the contracted kernel has a missed small endpoint.

## New execution evidence

The following independent reproduction predates the later merged-module build. Its measured scope is preserved here; source and review hashes are recorded in publication provenance.

1. The independent reproduction compiled six isolated build inputs using the original certificate runner. All four Lean compilation steps exited zero under the existing Lean 4.33.1 (commit 819816b2e0a3bf405af45ae5c7af2491d8f5bee6), Std only. Total 56.42 seconds; full certificate 54.96 seconds; peak child RSS 791972 KiB. Caps: Lean -j1 -M4096, 180 CPU seconds, 200-second full-build wall timeout. Inputs are unchanged before/after, as recorded in the original reproduction manifest.
2. An independent Lean oracle exported actual Lean evaluations for EVERY support/orientation/head-set tuple at m=4..7. The independent translation oracle independently reconstructs source blocks and explicit ADCB position words. It checks labels, tau and its inverse, the complete conjugated predecessor array, genuine H', acceptance, and a conclusion with all five forbidden z positions explicitly excluded. It also independently generates the full Python domain to detect missing or duplicated Lean rows. All 7586 rows passed; accepted pair counts at m=4,5,6,7 are 0,0,12,28; triple counts are all zero. This is an orthogonal finite translation check, not a substitute for the whole-range semantic argument.
3. Recompiled the original independent C++ kernel with `g++ -std=c++17 -O2 -Wall -Wextra -pedantic` and reran it: 3858/560 pair configurations/matches and 650/0 oriented triples/matches. Compiler warning log is empty.
4. Reran the Python permutation kernel: 3858 pair partitions, 560 directed matches, all 560 local alternating; 650 oriented triple cases and zero matches (its Counter omits the zero field). Counts agree with Lean. The previous audit's direct-word 280 unordered matches are consistent with 560 directed matches; this pass did not rerun the earlier full direct-word checker.

## Axioms and proof boundary

Fresh full compilation prints exactly:
- pairs_through_12: [propext, pairs_through_12._native.native_decide.ax_1_1]
- triples_through_10: [propext, triples_through_10._native.native_decide.ax_1_1]

The small diagnostics similarly have their named native_decide axioms. Both m=4 statements print [propext] only. The printed full theorem bodies are `of_decide_eq_true` applied to those native certificates. No sorryAx, user-declared axioms, external result-file input, unsafe predicate, or additional axiom dependency is present in the audited source or the reproduced theorem axiom lists. Expected integer counts are targets to be established, not external oracles. Native evaluation/compiler correctness remains trusted; these are not full-range ordinary kernel-reduction certificates.

## Strongest safe conclusion and remaining gap

The bounded Lean executable certificate is successfully reproduced and semantically matches the reviewed finite classification, with no missing endpoint or alignment identified. Together with the separately audited abstract reduction it supports the existing computer-assisted mathematical theorem. It does NOT upgrade that reduction, word correspondence, local analytic estimate, higher-rank ambiguity, overlap intersections, multiplicity control, or deterministic BGS to a Lean-formalized theorem.

No repair is needed for the bounded artifact. A future stronger formal claim would first require Lean theorems connecting list enumerators and the executable predicate to abstract permutations/cyclic words, followed by compression and lifting. The present result should retain its native trust and bounded formal scope labels.

## Publication provenance

The [canonical classification](../mathematics/four_cut_rank_two_classification.md) and [merged Lean module](../formalization/Bgs/FourCutKernel.lean) are the maintained sources. Original accepted Lean inputs and mathematical source are retained in [evidence provenance](../evidence/executions/20261006/four-cut-kernel/provenance/). The later merged-module execution has its own [receipt](../evidence/executions/20261006/four-cut-kernel/receipt.json), separate from the historical audit runs reported above.

This publication record preserves the mathematical findings and exact scope while curating execution paths and task bookkeeping. The original review SHA256 and curated SHA256 are paired in [publication provenance](../evidence/executions/20261006/four-cut-kernel/publication_provenance.json). Original review hash: f1f37a6798374a3c91a54f04f7e4287d621fc553798a839bfa0d709e75f143c4.
