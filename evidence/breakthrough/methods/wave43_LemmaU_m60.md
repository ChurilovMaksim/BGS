# Wave 43, task 1 — Lemma U at m=60: full-cycle rigidity, proved for the small pairs

## Verdict

Lemma U holds at m=60 for every pair of small constraining components
(81, 121, 361, 3481): 0 conflicts in exact censuses totalling 2,026,078
points. Every ℘-collision is dihedral, a partial move (partial conjugation
and/or partial negation), or a p=3 kernel translation. No fourth mechanism
exists at any tested pair. The large components 601² and 2281² are NOT
covered (see §7).

## 1. Setup

m = 60, u = 30, β = α², α = 3+2√2. Constraining components (q | Tr(α³⁰)+2):
81 (3⁴, f=2), 121 (11²), 361 (19²), 3481 (59²), 361201 (601²), 5202961 (2281²).
α³⁰ ≡ −1 mod p^f at every component, so block1 = −block0 and
℘ = block0 ∪ (−block0), with blocks indexed by k ∈ Z/30.
Trace cycles satisfy s_{k+1} = 34 s_k − s_{k−1}. The fiber group is
G = ⟨simultaneous shift, simultaneous reversal, simultaneous negation⟩
on cycle-pairs; a ℘-group is a union of G-orbits, and Lemma U is the claim
that the block pair is constant on each group.

## 2. Period rigidity (main pair 121 × 361)

R/11 and R/19 are fields (2 is a non-residue mod 11, 19). β^d − 1 norms:
mod 11: unit for d ∈ {1,2,3,5,10}, zero only at d = 6; mod 19: unit for
d ∈ {1,2,3,5,6}, zero only at d = 10. Hence trace-cycle periods are
T_a ∈ {1,6} (120 cycles of period 6, 1 zero) and T_b ∈ {1,10}
(360 of period 10, 1 zero). Antiperiods: β³ ≡ −1 mod 11 and mod 9,
β⁵ ≡ −1 mod 19 and mod 59 (checked). So shift-by-antiperiod = negation
on every small side. Period cases are (6,10), (1,10), (6,1), (1,1) only;
gcd(T_a, T_b) ∈ {1,2}, and gcd = 1 occurs only in degenerate cases.

## 3. Kernel lemma at p = 3

(Tr, Tr∘β) = (2a, 7a+3b) mod 9 has determinant 6, not a unit: the trace
cycle determines C ∈ R/9 only up to the kernel {(0,0),(0,3),(0,6)}.
Verified exactly: 27 distinct cycles from 81 parameters, every fiber
exactly one kernel triple. Kernel translates have identical trace cycles,
hence identical blocks — they are not conflicts, and Lemma U is unaffected
by them. Work henceforth is on cycle-pairs (kernel-quotiented).

## 4. Three full-cycle lemmas for (121, 361), checked exactly

L1 (19-side): any β-cycle with value multiset M(s) or M(−s) is dihedral
(shift/reversal) to s or −s. 0 violations over 361 × 361.
L3 (19-side single): M(x) ∪ M(y) = M(t) ∪ M(−t) implies
{M(x),M(y)} = {M(t),M(−t)}. 0 violations over 406 multiset pairs.
L2′ (11-side fibers): for period-6 cycles, the fiber data over the 19-side
is exactly the even/odd value multisets E = {x₀,x₂,x₄}, O = {x₁,x₃,x₅}
(fiber over s_j is {x_j, x_{j+2}, x_{j+4}} since k ≡ j mod 10 gives
k ≡ j, j+4, j+2 mod 6). If {E(x),O(x)} = {E(t),O(t)} (in either order),
then x is dihedral to t or to −t. 1080 matches, 0 violations.
So fiber data determines the cycle up to dihedral moves and one parity
bit — the interleaving of E and O.

## 5. Assembly for (121, 361)

(1,10), (6,1), (1,1): trivial or by L3 (single-component recombination
impossible). (6,10) generic: by L1, the second coordinates of a
recombinant partition are M(s), M(−s) in some order; the fibers over s_j
then force {E,O} = {E(t),O(t)} by L2′, so the recombinant first coordinate
is dihedral to t or to −t. The residual freedom is exactly the parity
bit: the two interleavings of (E,O) into a β-cycle. Flipping the bit is
the partial negation on one side (shift by the antiperiod: 3 on the
11-side, 5 on the 19-side), and it preserves the block pair — verified
exactly: every 2-orbit ℘-group at (11,19) is partial-move related (§6).
Hence every ℘-collision is dihedral or a partial move, and blocks are
preserved. This is the m=60 analogue of the m=30 proof, with the new
parity mechanism replacing the product mechanism (no gcd = 1
non-degenerate case exists here: periods are only 6 and 10).

## 6. Exact census: all six small pairs, 0 conflicts, 0 unexplained groups

| pair | points | ℘-groups | conflicts | 2-orbit groups (mechanism) |
|---|---|---|---|---|
| (81, 121) | 9,801 | 307 | 0 | 0 |
| (81, 361) | 29,241 | 286 | 0 | 45 (18 rev-only, 27 rev+neg) |
| (81, 3481) | 281,961 | 2,298 | 0 | 493 (290 rev-only, 203 rev+neg) |
| (121, 361) | 43,681 | 628 | 0 | 225 (90 rev-only, 135 rev+neg) |
| (121, 3481) | 421,201 | 5,004 | 0 | 2,465 (1450 rev-only, 1015 rev+neg) |
| (361, 3481) | 1,256,641 | 63,393 | 0 | 0 |

"rev-only" = the two orbits are related by a partial reversal (partial
conjugation) but not by a partial negation; "rev+neg" = related by both
(they coincide on degenerate pure-√2/real parameters, where reversal =
negation on that side's cycle). At (361, 3481) both β-orders are 10, so
there is no parity bit (pairs indexed by k mod 10 only) and no multi-orbit
group at all. An earlier size-based reading ("clean" pairs) was wrong:
collisions hide inside groups of size ≤ 120; the correct criterion is
the number of G-orbits, used here.

## 7. Conclusion and limits

Lemma U is proved at m=60 for all pairs among {81, 121, 361, 3481}:
collisions are exactly dihedral moves, partial conjugations, partial
negations, and p=3 kernel translations, all block-preserving. NOT covered:
pairs involving 601² or 2281² (β-orders 30, 30 there — equal orders, as in
the clean (361, 3481) pair, but no census or proof was run; 601² × 121
alone is 43.7M points). PAIR's remaining gap at m=60 is exactly those two
components. No Lean built, repository untouched.
Scripts: wave43_LemmaU_m60_test.py, wave43_LemmaU_m60_pairs.py,
wave43_LemmaU_m60_cycles.py, wave43_LemmaU_m60_parity.py,
wave43_LemmaU_m60_partial.py, wave43_LemmaU_m60_lemmas.py.
