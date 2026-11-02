# Wave 43, task 5 — the Pairing Lemma for JBL: REFUTED (exact counterexample)

## Verdict

The Pairing Lemma (wave 40 §3) is **false** as stated: per-class
marginals agreeing up to a common π do **not** imply per-class
joints agreeing up to the same π. Exact counterexample at
m = 32, component pair (q₂, q) = (8192, 17), verified by an
independent recomputation (`wave43_PairingLemma_check.py`,
ALL CHECKS PASS). This kills the direct route's pairing step as
a standalone lemma; it does **not** refute JBL itself (see §5).
Repository untouched; no Lean built.

## 1. The witness

Genuine parameters (ker(α³² − 1) in each component):

- A = (B₂, B_q) = ((0, 128) mod 8192, (1, 0) mod 17)
- A′ = (B₂, B_q·β) = ((0, 128) mod 8192, (−1, 0) mod 17),

where β = α⁴. The shift is by β on the odd component only; the
pattern component is untouched.

Key arithmetic: β = α⁴ ≡ **−1 mod 17R** (577 ≡ −1, 408 ≡ 0
mod 17). So the odd class sequence alternates, and shifting by β
is just negation: it swaps the two odd values in each class.

## 2. Marginals agree, joints agree under no π

Per-class marginals of A and A′ are **exactly equal** (not just
up to π): pattern marginals are identical since B₂ is unchanged,
and odd marginals are preserved because shifting a cyclic class
sequence permutes its multiset. The marginal π-set is exactly
{ id } — the common π is unique.

The joint π-set is **empty**: no π ∈ D₄ matches the joints of A′
to those of A. Class 0 alone already kills it:

- A, class 0:  {(0, 2)×4, (4096, 15)×4}
- A′, class 0: {(0, 15)×4, (4096, 2)×4}

The pattern class sequence is (0, 4096, 0, 4096, …) and the odd
class sequence is (2, 15, 2, 15, …); shifting the odd component
by β swaps 2 ↔ 15 and **crosses the pairing**. Since the
marginal π is unique (id) and id is not a joint π, the lemma's
conclusion fails. (The pair is not saved by any other π: the
joint π-set is empty, not merely disjoint from {id}.)

## 3. The general criterion: period coprimality

Per class r, write f(k) = Tr(B₂βᵏ) mod q₂ (pattern sequence) and
g(k) = Tr(B_qβᵏ) mod q (odd sequence), k ∈ Z/S, S = m/4, with
periods p₂, p_q. Two lemmas, both proved:

- **(a) p₂ is a power of 2.** β = α⁴ = 577 + 408√2 ≡ 1 mod 8R,
  so by binomial induction ord_{2^e}(β) | 2^{e−3}; the pattern
  period divides that order.
- **(b) Joint = Cartesian product iff gcd(p₂, p_q) = 1.** If the
  periods are coprime, k ↦ (k mod p₂, k mod p_q) is a bijection
  Z/(p₂p_q) → Z/p₂ × Z/p_q, so each pair (f(a), g(b)) occurs
  exactly S/(p₂p_q) times: the joint multiset is forced by the
  two marginal multisets, and the Pairing Lemma holds for that
  parameter pair (after wave-40 transport to π = id).

Hence the Pairing Lemma holds for a component pair **iff**
gcd(p₂, p_q) = 1 for every genuine parameter pair, and it fails
as soon as one pair has both periods even. At (32, 17): class-0
pattern period 2 (2048 of 8192 params) and class-0 odd period 2
(272 of 289 params) — the witness above is one of 2048 × 272
such dangerous pairs at class 0 alone.

## 4. Why the earlier tests passed (0 crossed pairings)

| case | pattern periods | odd periods | why safe |
| m = 8, (512, 9/289) | 2-power | 1 (constant/class) | odd side trivial |
| m = 16, (2048, 9) | 1, 2 | 1 (constant/class) | odd side trivial |
| m = 24, (512, 81/25/49/121) | 1 (constant/class) | 1, 3 | pattern side trivial |
| m = 24, (512, 289) | 1 | 1, 2 | pattern side trivial |
| **m = 32, (8192, 17)** | **1, 2, 4** | **1, 2** | **both sides even → crossed** |

The earlier 0-failure runs were cases where one side was always
trivial (constant pattern, or odd period odd). m = 32 is the
first tested case where both sides are simultaneously nontrivial
with a common factor 2. (At m = 32, q = 577, odd periods are
{1, 4} — even periods there too, with pattern periods up to 4;
the (8192, 17) witness is the smallest.)

## 5. What this does and does not kill

- **Killed:** the Pairing Lemma as a standalone step. Wave 40 §5's
  "sole gap of the direct route beyond PC" is now a refutation,
  not an open lemma: marginals ⟹ joints is false in general.
- **Not killed:** JBL itself. JBL's hypothesis is strictly
  stronger — the two parameters must share the **global** joint
  multiset (all classes pooled). For the witness pair the global
  multisets **differ** (check (6) in the verifier), so this pair
  is not a JBL counterexample. A pairing step for JBL would need
  the global hypothesis, or a different argument exploiting it
  (e.g. cross-class compensation, which the marginal-only
  statement cannot see).
- **Open, restated:** JBL for m divisible by 8 (direct route needs
  a replacement for the pairing step); PC in general; Lean
  formalisation (nothing here is a Lean theorem).

## Files

- This note: `methods/wave43_PairingLemma.md`
- `methods/wave43_PairingLemma_check.py` (independent verifier,
  ALL CHECKS PASS)
- Prior: `methods/wave40_JBL_direct.md` (§3 lemma, §4 tests),
  `methods/wave40_JBL_direct.py` (test code whose definitions
  this note follows exactly)
