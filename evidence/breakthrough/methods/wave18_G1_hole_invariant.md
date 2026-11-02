# Wave 18, task 3 — second-digit statistic vs the G1 twist at p=13: YES, it distinguishes

**Verdict: YES.** At p=13, every genuine twist changes the second-digit
distribution of orbit values — marginal, conditional-on-v0, and joint
(full multiset) alike. No genuine twist is invisible to it.
Context in one line: see [wave16_G1_f2s0.md](sandbox://workspace/bgs-breakthrough/methods/wave16_G1_f2s0.md)
§5 (power sums S_r = 0 for r < L₀, S_{L₀} = L₀·f·(B−B̄), so power sums
cannot see the twist when B is real mod p).

## Setup

R = ℤ[√2], p = 13, modulus p² = 169. α = 3+2√2 has order 14 mod 13 and
mod 169 (s = 0). G = ⟨α⟩ mod 169 (14 elements); H0 = ⟨α²⟩ (7 elements,
t = 2 case). Twist: A′ = A·(1+13f), f = c√2, c = 1..12 (ζ ∈ G is
irrelevant: it permutes the orbit). Second digit: v = v0 + 13·v1,
v0 = v mod 13, v1 ∈ {0..12}. Orbit values: Tr(Az) mod 169, z ∈ G (resp. H0).
Exact integer arithmetic throughout; repository untouched, no Lean build.

## Numbers (exhaustive over all units A mod 169)

- Units mod 169: 28,392. Twist pairs (A, c): 340,704.
- G-orbit multiset preserved: 26,208 pairs; H0-orbit preserved: 13,104.
- **All preserving pairs are trivial:** A′ equals Az or Āz for some
  z in the group (the twist is an allowed symmetry in disguise).
  Genuine preserving pairs: **0** (both G and H0).
- Genuine twists (A′ not G/conj-G-related): 314,496.
  Among them: v1-marginal coincidences **0**, conditional-on-v0
  coincidences **0**, joint-distribution coincidences **0**.

## Two illustrative cases

- Trivial preserving case: A = (1,2), c = 3 — G-orbit multiset identical
  ([2,10,22,24,39,62,82,87,107,130,145,147,159,167] both), but A′ is
  conj-G-related to A, so this is symmetry, not a twist.
- Genuine case: A = (0,1) = √2, c = 1 — untwisted orbit values are all
  doubled ([0,0,8,8,48,48,58,58,111,111,121,121,161,161]), twisted are
  all distinct; v1 marginals differ (untwisted {0:4,3:2,4:2,8:2,9:2,12:2}
  vs twisted {0:2,1:2,2:1,4:1,6:2,9:1,10:1,11:2,12:2}); all 21 (v0,v1)
  cells differ.

## Structural remark

B real mod 13 is **automatic** at p=13: for all 168 units mod 13,
A¹⁴ has b-component 0 mod 13 (A¹⁴ lands in the unique order-12 subgroup
of F₁₆₉×, i.e. F₁₃×). So the power-sum gap condition is vacuous here —
power sums never see any twist at p=13 — yet the second-digit
distribution always does. The invisibility of wave 16 §5 does not
extend from power sums to the full multiset.

## Scope (honest limits)

- p = 13 only. The hole proper needs 4 | L₀, which fails at p=13
  (L₀ = 14); this test rules out the twist mechanism at p=13, it does
  not close f = 2 s = 0 in general and says nothing about p = 31 or
  1546463 (same test would be needed there).
- Direct multiset comparison (via second digits) rules out the twist
  at p=13; it is not a proof of L6, only the absence of a
  counterexample at this prime.

## Files

- This note: [wave18_G1_hole_invariant.md](sandbox://workspace/bgs-breakthrough/methods/wave18_G1_hole_invariant.md)
- Check script: [wave18_G1_hole_check.py](sandbox://workspace/bgs-breakthrough/methods/wave18_G1_hole_check.py)
