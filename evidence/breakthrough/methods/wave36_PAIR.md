# Wave 36, task 3 — lemma PAIR: proved under one-sided disjoint supports,
reduced to Lemma U in general

## Verdict

PAIR is **proved whenever at least one of the two constraining
components has disjoint even/odd supports** (Theorem 2 below — this
covers 473,318/516,564 = 91.6% of fiber pairs at m = 30, (625, 841)).
In full generality PAIR is **reduced to one named lemma, Lemma U**
(§4): the pair multiset determines the unordered block pair. Lemma U
is open; no counterexample to PAIR was found anywhere (m = 18:
942,780 pairs; m = 30: 516,564 pairs at (625, 841), 0 failures,
Π never empty). The remaining gap is exactly the pairs whose
supports overlap at **both** components (8.4% at (625, 841)).

## 1. Setup and the β-orbit reduction

Let m = 2u, u odd, q odd prime power, constraining (q | Tr(α^u)+2).
Kernel vectors y ∈ (Z/q)^m satisfy y_{i+1} = 6y_i − y_{i−1}, i.e.
y_i = Tr(Bα^i) for B ∈ ker(α^m − 1) ⊂ R/qR. Classes: E = even
positions, O = odd positions. Since u is odd, i ↦ i+u swaps E and O,
and even positions are i = 2k, odd positions i = u + 2k, k ∈ Z/u.
Hence, with β = α²,

- M_E = {y_i : i even} = T(B) := {Tr(Bβ^k) : k ∈ Z/u},
- M_O = {y_i : i odd} = T(α^u B).

For a fiber pair (B, B′) at component q:

- id ∈ Π_q ⟺ T(B′) = T(B) and T(α^u B′) = T(α^u B),
- swap ∈ Π_q ⟺ T(B′) = T(α^u B) and T(α^u B′) = T(B).

At two constraining components (q_a, q_b), the pair multiset is

  ℘ = T_pair(B^a, B^b) ∪ T_pair(α^u B^a, α^u B^b),

where T_pair(C^a, C^b) = {(Tr(C^a β^k), Tr(C^b β^k)) : k ∈ Z/u}
(block 0 = even positions, block 1 = odd positions). PAIR's
hypothesis is ℘′ = ℘; its conclusion is Π_{q_a} ∩ Π_{q_b} ≠ ∅.
Standing hypothesis (as in wave 35): Π_q ≠ ∅ by G1/G2, so failure
means complementary singletons: ({id}, {swap}) or ({swap}, {id}).

## 2. Theorem (one-sided disjoint supports ⟹ PAIR)

If supp(M^b_E) ∩ supp(M^b_O) = ∅ (disjoint supports at component b,
for the base pair), then Π_a ∩ Π_b ≠ ∅. By symmetry, disjointness
at either component suffices.

Proof. Suppose Π_a = {id}, Π_b = {swap} (the other case is symmetric).
Block-0′ pairs (Tr(B'^a β^k), Tr(B'^b β^k)) have first coordinates
in T(B'^a) = T(B^a) = M^a_E (id at a) and second coordinates in
T(B'^b) = T(α^u B^b) = M^b_O (swap at b). A block-0′ pair (x, y) has
y ∈ supp(M^b_O); if it occurred in block 0, its second coordinate
would lie in supp(M^b_E), contradicting disjointness at b. Hence
every block-0′ pair lies in block 1, so block 0′ ⊆ block 1 as
multisets; both have u pairs, so block 0′ = block 1. First-coordinate
marginals give T(B'^a) = T(α^u B^a); with id at a, T(B'^a) = T(B^a),
so T(B^a) = T(α^u B^a). Then swap ∈ Π_a: T(B'^a) = T(α^u B^a) holds,
and T(α^u B'^a) = T(α^u B^a) = T(B^a) by id at a. This contradicts
Π_a = {id}. ∎

Case Π_a = {swap}, Π_b = {id}: block-0′ pairs have second coordinates
in M^b_E; a pair in block 1 would have second coordinate in M^b_O,
impossible by disjointness at b, so block 0′ = block 0; first
marginals give T(B'^a) = T(B^a), and swap at a gives
T(B'^a) = T(α^u B^a), so T(B^a) = T(α^u B^a), hence id ∈ Π_a,
contradicting Π_a = {swap}. ∎

Remark. The proof uses only that block 0′ cannot straddle blocks
under disjointness; it does not identify the blocks. Note also that
under disjoint supports Π_q cannot be "both" (both ⟹ M_E = M_O as
multisets ⟹ equal supports, contradicting disjointness unless
empty), so the singleton analysis above is exhaustive.

## 3. What the theorem does not cover

Pairs whose supports overlap at both components (for base and other):
there the block-0′ pairs can hide in either block and the counting
above gives no contradiction. This is the only gap: at (625, 841),
43,246/516,564 pairs (8.4%) are uncovered, with 0 failures observed.
The §5 lead of wave 35 (disjoint supports at both components) is
subsumed: one side suffices, by the argument above.

## 4. Reduction: PAIR ⟸ Lemma U

**Lemma U.** The pair multiset ℘ determines the unordered pair
{T_pair(C^a, C^b), T_pair(α^u C^a, α^u C^b)}.

If Lemma U holds, then ℘′ = ℘ forces either block 0′ = block 0 and
block 1′ = block 1 (marginals give id at both components) or
block 0′ = block 1 and block 1′ = block 0 (marginals give swap at
both). Either way Π_a ∩ Π_b ≠ ∅. So PAIR follows from Lemma U,
and Lemma U is the exact remaining gap: it is the statement that
two β-orbit trace-pair multisets cannot be re-split into a
different pair of β-orbit trace-pair multisets with the same union.
It is false for abstract multisets (e.g. {1,2} ∪ {2,3} = {1,3} ∪
{2,2}), so a proof must use the trace structure (the two blocks
are related by the α^u-twist and each is a single β-orbit), which
is not carried out here.

## 5. Computational evidence (exact)

- m = 18, (25, 38809): 970,225 slice points, 27,445 fibers, 942,780
  pairs, 0 common-π failures (wave 35).
- m = 30, (625, 841): kernels by exact brute force (625, 841
  vectors); 525,625 points, 9,061 fibers, 516,564 pairs, 0 failures,
  Π never empty at either component. Support-disjointness rates:
  49.9% of points at 625, 83.2% at 841; pairs covered by Theorem 2:
  473,318 (91.6%); uncovered pairs: 43,246, 0 failures among them.
- m = 30, (625, 72361): kernels verified (brute force for 625;
  B = 269·C parametrisation for 72361, using
  α^30 = 1 + 269·265·√2 mod 269²); chunked-hash test with exact
  re-verification of every hash group: 45,225,625 points, 757,116
  verified fiber groups, 44,468,508 pairs, 0 common-π failures.
- m = 30, (841, 72361): same method: 60,855,601 points, 1,018,188
  verified fiber groups, 59,837,412 pairs, 0 common-π failures.
  All three constraining pairs at m = 30 now pass; total new
  evidence at m = 30: 104,822,485 pairs, 0 failures.

## 6. What PAIR needs next

Lemma U (§4), or a counterexample in the both-supports-overlap
regime. If Lemma U is proved, the t = 2 class-partition lemma is
complete (a ≠ b by wave-34 2-periodicity counting; a = b by
wave-35 §2 + PAIR), and the t = 2 case of JBL's class part is
closed. No Lean work was done (per brief); repository untouched.
