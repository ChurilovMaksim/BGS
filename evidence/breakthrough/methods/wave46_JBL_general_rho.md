# Wave 46, task 6 — JBL general common-π: fiber theorem + strong form REFUTED

## Verdict

**The strong form of the multi-component common-π step is FALSE.**
For mixed-fiber pairs, triple matching at q does NOT force joints
under every pair-level π: exact counterexamples at q = 577 below
(§5). But the step is **PROVED in full generality whenever pair
fibers are class-homogeneous** (Theorem B, §1) — that covers both
GPL families, ~95% of genuine pairs at m = 32, every q, every ρ,
with no condition on α at all. Wave 45's α¹⁶ ≡ 1 hypothesis was
needed only for its conjugation proof, not for the conclusion.
Repository untouched; no Lean built.

## 1. Theorem B (fiber theorem, proved)

Setup: pair (A, A′) with equal pair-globals, π in the pair joint
π-set, ρ a pair witness (bijection of positions, pair-value
preserving, class(ρ(j)) = π(class(j))). A fiber is the set of
positions sharing one (pattern, odd) pair-value. Triple matching
at q means equal multisets of (pattern, odd, q) triples.

**Theorem.** If every fiber of A is class-homogeneous (contained
in one class mod t), then triple matching at q implies joints at
q agree under π — for every q, every ρ, no α hypothesis.

**Proof.** Fix class r. Partition A′-positions j ≡ r by fibers
F′ ⊆ class r (homogeneous by ρ⁻¹ applied to A's fibers). For
F′, ρ(F′) = F is the A-fiber with the same pair-value v, and
F ⊆ class π(r). Triple matching groups triples by pair-value,
so the q-multiset on F′ equals that on F; pair-value is constant
v on both, hence {(v, bp_j) : j ∈ F′} = {(v, b_i) : i ∈ F} as
multisets. Union over F′ ⊆ class r gives
{(pp_j, bp_j) : j ≡ r} = {(p_i, b_i) : i ≡ π(r)}. ∎

This subsumes wave 45 §3–§4 (both GPL families have fibers
{i, i+16}, hence homogeneous) and needs no twist, no spanning,
no N(α) = 1. The only way the step can fail is a mixed-class
fiber — and those exist (§4).

## 2. Twist remark (why wave 45's α¹⁶ was spurious for reversal)

Uniform twist α^{ρ(j)} = γ·φ(α^j) (φ ∈ {id, conj}) plus
fiber-sum spanning implies pointwise b_{ρ(j)} = bp_j, hence
joints under π. Reversal ρ(j) = c − j always has uniform twist
γ = α^c, φ = conj (uses only N(α) = 1), at EVERY q. Block
reversal has piecewise twist ε_j ∈ {1, α¹⁶} (ε_j = α¹⁶ when
j mod 16 > 9), uniform iff α¹⁶ = 1. Theorem B makes both remarks
unnecessary for homogeneous fibers, but they explain the
wave-45 proofs: reversal never needed α¹⁶ = 1.

## 3. Pell classification: the α¹⁶ ≢ 1 components

Let β = 1 + √2, α = β², βⁿ = aₙ + bₙ√2. Then β⁶⁴ ≡ 1 mod q
iff q | gcd(a₆₄ − 1, b₆₄), and a₆₄ − 1 = 4b₃₂²,
b₆₄ = 2a₃₂b₃₂ give gcd = 2b₃₂ (using a₃₂ odd,
gcd(a₃₂, b₃₂) = 1). So primes with α³² ≡ 1 are exactly the
prime divisors of b₃₂ = 2⁵·3·17·577·665857. Among them,
β³² ≡ 1 (α¹⁶ ≡ 1) at 3, 17, 577 (they divide a₃₂ − 1), and
β³² ≡ −1 (α¹⁶ ≡ −1, α³² ≡ 1) at 665857 only (it divides
a₃₂ + 1, not a₃₂ − 1). So 665857 is the UNIQUE odd prime with
α³² = 1, α¹⁶ ≢ 1. Note 17, 577 are the actual D₃₂ odd
components. Verified directly: α¹⁶ ≡ −1, α³² ≡ 1 mod 665857R.

## 4. Census: mixed fibers are common, never rich

Genuine pairs at m = 32, (8192, 17): |G2| = 8192, |Gq| = 289,
2,367,488 pairs, 6,159 global groups (as wave 44). Every genuine
B₂ is divisible by 64 (min v₂ ≥ 6), so p[i+16] = p[i] always.
Mixed-class fibers occur in 118,912 pairs (5.0%), of which
114,560 nondegenerate (B₂ ≠ 0, B_q ≠ 0); 744 multi-member mixed
groups, 704 nondegenerate. Mixed pairs are always coarse:
max over mixed members of min(#distinct p, #distinct a) = 4,
attained at (8, 4). So the fiber theorem's hypothesis fails on
a real 5% minority, not a degenerate corner.

## 5. Triple tests at q = 577 (complete enumeration, all 577² C's)

Method: per pair, group all C (resp. C′) by triple signature
(per-pair-value q-multisets, numpy) and check joints under each
pair-π, with joint-key aggregation; counts below are exact.

Top mixed pair A = ((8064,8128),(16,8)) vs ((384,64),(5,12)),
π-set {(1,2,3,0), (2,1,0,3)}, 8 fibers of size 4: only 1
triple-matching pair in the whole 577² × 577² space, and it
passes under both π's. Triple matching is extremely restrictive
for fine fibers.

Loop over mixed pairs (9 completed, counts identical in all):
each has nfib = 5, fiber sizes [4,4,8,8,8], 83,521 common
signatures, 1,329,409 triple-matching (C, C′) pairs, and
661,248 bad under EACH pair-π — e.g. A = ((0,512),(0,1)) vs
((0,512),(0,16)), π-set {id, reversal}; also A = ((2048,512),
(0,4)) vs ((0,512),(1,5)), π-set {(1,2,3,0), (3,2,1,0)}. The
strong form fails massively, not marginally. Yet fail-both = 0
in all 9 pairs: every triple pair passes under id or reversal
(single-q weak form holds empirically here).

Explicit witnesses (pair above, triples equal by direct check):
C = (1,1), C′ = (1,576) = conj(C) fails under id;
C = (1,1), C′ = (239,408) fails under reversal. Mixed fibers
of A: (4096,8) at [1,3,9,11,17,19,25,27] and (4096,9) at
[5,7,13,15,21,23,29,31] (classes 1, 3).

## 6. Tests at q = 665857 (α¹⁶ = −1)

GPL families (homogeneous fibers): sign-pattern enumeration
(2¹⁶ patterns, solve from 2 fibers, verify all 16): 3 random
C's each, 2 solutions per C (global ±), 6 + 6 triple pairs,
0 joints-bad — Theorem B confirmed in the α¹⁶ = −1 regime.
Mixed pair of §5 (size-4 fibers {w, z, −w, −z}): dihedral-option
solving (8 options per fiber, complete per C): 500 random C's,
0 triple-matching pairs at all — the step holds vacuously
there; the signature map is too injective at large q for
mixed-pair collisions to occur generically.

## 7. What remains open (precise)

- Strong form: REFUTED (§5). Single-q weak form (some pair-π
  works per triple pair) HOLDS in all 9 mixed pairs tested
  (fail-both = 0) — but only empirically, at q = 577; a proof
  is open. Cross-component consistency (q₁ forces id while
  q₂ forces reversal, killing any common π) is untested — it
  needs two extensions at once, the next decisive experiment.
- General m: Theorem B is m-free, but fiber homogeneity at
  other m, and which ρ's occur there, are open.
- Prime-power components with α¹⁶ ≢ 1 (lifting 665857 to
  665857^e, Wieferich-type) untested.
- Lean formalisation: nothing here is a Lean theorem.

## Files

- This note: `methods/wave46_JBL_general_rho.md`
- `methods/wave46_rho_probe1.py`, `wave46_rho_probe2b.py`,
  `wave46_rho_pell.py`, `wave46_rho_b2scan.py`
- `methods/wave46_rho_genuine.py`, `wave46_rho_genuine2.py`,
  `wave46_rho_census_save.py`, `wave46_rho_groups.pkl`,
  `wave46_rho_pick2.py`
- `methods/wave46_rho_sign665857.py`, `wave46_rho_triple577.py`,
  `wave46_rho_triple_fast.py`, `wave46_rho_witness.py`
- `methods/wave46_rho_dihedral665857.py`,
  `wave46_rho_dihedral665857b.py`
- Prior: `methods/wave45_JBL_commonpi.md`,
  `methods/wave44_JBL_pairing_replacement.md`
