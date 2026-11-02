# Wave 31, task 4 — COH at m=36 across ALL components: HOLDS

## Verdict

COH holds at m=36, exactly and exhaustively over all joint-global
groups: for every pair sharing the joint global multiset, a single
(j, c) works across all components simultaneously. No COH
counterexample exists at m=36, so the R**+COH route to JBL survives
here too. COH in general remains open; this is m=36 only (m=12 was
wave 30). Repository untouched; no Lean built.

## Setup

D_36 = 2^7·3^6·5^2·7^2·11^2·73^2·179^2·197^2·199^2, so the full
component set is {128, 729, 25, 49, 121, 5329, 32041, 38809, 39601}
(9 components). Genuine parameters per component are small:
|G| = 128, 729, 25, 49, 121, 5329, 32041, 38809, 39601. For odd
q = p^2, α^36 ≡ 1 + p·unit·√2 (mod q), so G_q = p·(R/pR) exactly;
for 128, G = {(16a, 8b)}; for 729, G = 27·(R/27R). Both kernels were
re-checked by brute force (128 and 729 pairs). The trace window is
Z/36, dihedral maps number 72.

## Reduction (wave-30 method, adapted)

For genuine A, S(A) = (Tr(Aα^i))_{i∈Z/36}. A pair shares the joint
global multiset iff some permutation σ of Z/36 sends S(A) to S(A′)
componentwise. COH holds for the pair iff some τ ∈ Dih_36 satisfies
S′_q − τ(S_q) ∈ ShiftSeq_q for every q, where ShiftSeq_q = {0} for
q ≠ 729 (Ann traces vanish; Ann(729) = {0}, Ann(128) has 16
elements) and ShiftSeq_729 is the shadow sequence set below. Two
structural facts, both verified exactly, make the test exhaustive
without enumerating 3.6×10^27 global parameters:

- Classes equal dihedral images at every q ≠ 729 (0 non-dihedral
  class sequences at 128, 25, 49, 121, 5329, 32041, 38809, 39601).
  Hence σ-validity at q ≠ 729 depends only on value patterns.
- At q = 729, all 118,401 ordered class pairs are enumerated
  directly (17 classes, sizes 1, 4, 12, 36, 324).

## Correction to the shadow at 729 (found en route)

The wave-28 rule "Shadow = {27D : D ∈ R/(q/27)R}" extrapolates
WRONGLY to q = 729: it gives all multiples of 27, i.e. every
genuine parameter, which would trivialize the test. The mechanism
(C-shifts by multiples of 3 are invisible, B = 27C) gives instead
Shadow(729) = {81D mod 729 : D ∈ R/9R} (all multiples of 81, 81
values). Confirmed by the wave-28 signature test at (128, 729):
93,312 parameters, 520 groups — D-orbit + Ann escapes 64/520;
+{27D : D ∈ R/3R} still 64; +{27D : D ∈ R/9R} escapes 56;
+{81D : D ∈ R/9R} escapes 0/520. The uniform rule is
Shadow = {3·d_q·D : D ∈ R/9R} with d_q the B-divisor (9 at 243,
27 at 729). ShiftSet_729 has 81 distinct sequences.

## The test

- Phase 1 (729 unconstrained, T full): pattern-tuple DFS over the
  8 non-729 components (patterns 2, 5, 7, 13, 38, 38, 20, 11; PQ
  counts 3, 16, 37, 145, 1369, 1369, 361, 100), with bipartite
  matching pruning and dead-state memoization: 2,561,920 nodes,
  5 s, 0 failures.
- Phase 2 (729-constrained): with the corrected ShiftSet, T-masks
  are full for 1,761 pairs (Phase-1 territory) and have size
  exactly 18 for the other 116,640 pairs, collapsing to 6,480
  distinct (T, Allow) keys. Pattern-tuple DFS over all 6,480 keys
  (4 threads): 10,780,776 nodes, 15 s, 0 failures.
- A pair fails iff all alive masks are nonempty and
  (∩ alive) ∩ T = ∅; both phases cover all cases (T-full pairs
  are covered by Phase 1, since dropping the 729 constraint only
  weakens the failure condition).

## Independent cross-check (Python, random sampling)

Random permutations σ of Z/36 with random genuine patterns per
component (independent code path): 3,000 σ trials, all realizable,
0 failures. Agrees with the exhaustive C++ result.

## Counts, honestly

Failing joint-global groups at m=36: 0 (exhaustive over the failure
condition, not by enumerating groups). Total number of joint-global
groups was NOT enumerated (infeasible at D_36 ≈ 3.6×10^27); the
claim is "every group admits a single (j, c)", not a group census.
The result depends on the shadow identification above (empirically
pinned at (128, 729) by the 0/520 signature coverage) and on the
wave-30 sequence criterion (ShiftSeq = {0} off the collapse
component), applied here with the single collapse component 729.

## Files

- This note: `methods/wave31_COH_m36.md`
- `methods/wave31_COH_m36_phase1.cpp` (Phase 1 DFS),
  `methods/wave31_COH_m36_phase2keys.cpp` (729 T-masks),
  `methods/wave31_COH_m36_phase2dfs.cpp` (Phase 2 DFS),
  `methods/wave31_COH_m36_shadow729.py` (shadow identification),
  `methods/wave31_COH_m36_crosscheck.py` (random cross-check).
- Prior: `methods/wave30_COH_m12.md` (m=12 method),
  `methods/wave28_JBL_Rstar_243.md` (shadow rule, corrected here).
