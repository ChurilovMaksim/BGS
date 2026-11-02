# Wave 47x, task B — Conjugate-prime twins: classified, and they DO feed genuine ℘-collisions

## Verdict

The wave-46 mod-49 twin is not a curiosity: the mechanism is fully classified (split case,
theorem §2), no twin outside it was found at any searched modulus (§3), and mirror twins
feed genuine ℘-collisions exactly at g | ord(b mod p^a) (§4). The mod-49 instance itself
is virtual for ℘ (49 is Lemma-U-inadmissible), but a REAL instance exists at (137², 137),
u = 2329, g = 17 (§5). Consequence: any Lemma-U closure must list mirror twins as a
mechanism alongside dihedral / partial conjugation / scaling / kernel, or restrict to units.

## 1. Setup

p split: R/p^f ≅ (ℤ/p^f)², β ↦ (b, b⁻¹), T = ord(b), cycle t_k = c₁b^k + c₂b^{-k}.
Valuation pattern (v_p(c₁), v_p(c₂)); ∞ for a zero component. Dihedral moves and scaling
preserve patterns (up to swap), so twins with different patterns are genuine L1 failures.

## 2. Mechanism theorem (split case, proved)

Let C have pattern (a, 0) or (0, a), 1 ≤ a ≤ f−1, unit entry y; let D have pattern (0, ∞)
or (∞, 0) with entry d. If v_p(T) + a ≥ f (i.e. p^{f−a} | T), then M(C) = y⟨b⟩ and
M(D) = d⟨b⟩, so M(C) = M(D) ⟺ d/y ∈ ⟨b⟩; in particular d ≡ y mod p^a suffices, since
then d/y ∈ 1 + p^aℤ/p^f ⊆ ⟨b⟩. Proof: φ(u) = yu⁻¹ + p^a·x·u is injective on ⟨b⟩
((u−v)(p^a·x·uv − y) = 0, second factor a unit), and (φ(u)/y)^T = 1 by the binomial
valuation bound v_p(T) + a ≥ f, so φ(u) ∈ y⟨b⟩; cardinality gives equality. The
same-multiset class is ⋃ over residues ȳ ∈ ⟨b̄⟩ of F(ȳ, a), F = {unit entry ≡ ȳ mod p^a,
other entry ≡ 0 mod p^a, both orientations} (higher levels a' > a and the singular
(∞, 0) pattern are included, since ≡ 0 mod p^a is weaker). At f = 1 there are no
genuine twins (a = f is scaling-absorbed); in the inert case none (valuation mismatch;
same-level reduces to unit L1*). Ramified p = 2 not covered.

## 3. Search: no twin outside the classification

| modulus | T | twin groups | patterns | size check |
|---|---|---|---|---|
| 49 | 21 | 2 | (0,1),(0,2),(1,0),(2,0) | 294 = 3 fibers × 98 |
| 289 | 68 | 4 | same | 2312 = 4 × 578 |
| 529 | 253 | 2 | same | 11638 = 11 × 1058 |
| 343 | 147 | 2 (per 147) + 2 (per 21) | (0,1),(0,2),(0,3),(1,0),(2,0),(3,0); per-21: (1,2),(1,3),(2,1),(3,1) | 14406 = 3 × 4802; per-21 = 7×49-twins |
| f = 1, split 7,17,23,31,41,47 | — | 0 | — | — |
| inert 121, 169 | 66, 7 | 0 | — | — |

Sample probes follow the criterion exactly: cond true ⟹ all M == M true (41², 47², 17²,
7³ a = 1, 2); cond false ⟹ all false (31²); NEG probes follow d/y ∈ ⟨b⟩ (47², 7³: d = 2
true, d = 3 false). (An early inert run flagged 5 artifacts from a sign error in the
conjugate branch of the search script; fixed, rerun → 0.)

## 4. σ-dichotomy and the feeding criterion (proved; verified at 49, 17², 41², 137²)

For a mirror twin D' (zero component, same orientation as C's unit component):
σ'(k) ≡ k mod m, m = ord(b mod p^a). For a cross twin D: σ(k) ≡ −k mod m. (Shadow:
reduce the trace equality mod p^a; the unit component forces the index congruence.)
For generic s (distinct values, negation-free), the diagonal X of (t', s) equals block0
⟺ σ' preserves mod-g classes (CRT bijection; block1 excluded by negation-freeness).
Hence: **mirror twins feed ℘-collisions at every g | m**; cross twins only at
gcd(m, g) | 2, i.e. for odd g (Lemma U) only g = 1 (Cartesian triviality). Numerically
cross twins also failed at 49 (g = 7) and 137² (g = 17), where the shadow is silent.

## 5. Real instance: (137², 137), u = 2329, g = 17

ord(β) mod 137² = 2329 = 17·137; ord(α) = 4658; α^2329 ≡ (−1, −1) mod 137² with u = 2329
odd → A-side admissible (B-side 137: ord(α) = 34, 2329 ≡ 17 mod 34 ⟹ α^2329 ≡ −1 mod 137).
C = (137, 1) pattern (1, 0), mirror D' = (0, 1): cycles period 2329, 2329 distinct values,
equal multisets, σ' ≡ id mod 17, σ' ≠ id. Unit B-side S = (1, 2) at 137: s period 17,
distinct, negation-free. Then block0' = block0 exactly (2329 pairs) ⟹ ℘(t', s) = ℘(t, s),
while the cross twin gives block0' ≠ block0. (t', s) is not dihedral/scaling of (t, s)
(patterns (∞, 0) vs (1, 0)/(0, 1) are preserved), not a partial conjugation (t' ≠ reversal
of t; also g = 17 ≥ 3 forbids it for generic cycles), not kernel (p ≠ 3), not Cartesian
(g = 17 ≠ 1). The mod-49 twin is virtual for ℘: ord(α) mod 49 = 21 is odd, so
α^u = −1 never; same obstruction at 343, 529, 961, 1681, 2209, and at 289 (ord α = 136,
v₂ = 3, no odd u). Scan of split primes ≤ 2000: exactly 9 have v₂(ord ε₁) = 2
(137, 521, 569, 593, 857, 953, 1321, 1777, 1993), all with p | T₂ — real twin components
are not rare; 137 is the smallest.

## 6. Remaining gaps

- Ramified p = 2 unexamined. Degenerate B-side (s with negation pairs/repeats) interacting
  with twins untested; the generic-s case is settled. No Lean formalization; repo untouched.
- Scripts: wave47x_twin49.py, wave47x_twins_search.py (+search2), wave47x_twins_pfeed.py,
  wave47x_twins_admiss.py, wave47x_twins_pred2.py, wave47x_twins_scan.py,
  wave47x_twins_real137.py (+real137b/c), wave47x_twins_sigma.py, wave47x_twins_inert.py,
  wave47x_debug11.py, wave47x_debug25.py (all in this directory).
