# Wave 13, task 2 (retry) — Lemma PC for m = 6, p₁ = 5, p₂ = 7: PROVED

## Statement

As in [wave12_g3_common_pi.md](wave12_g3_common_pi.md)
§3b, restricted to m = 6, p₁ = 5, p₂ = 7 (both divide
D₆ = 39200 = 2⁵·5²·7²). Let a (mod 5), b (mod 7) be recurrence
sequences of length 6 (y_{j+1} = 6y_j − y_{j−1}), d₁, d₂ ∈ D₆,
and Πᵢ the π-set for (sequence, dᵢ(sequence)) over the classes
O_r = {i : i ≡ r (mod t)}, t = gcd(6, 4) = 2, D₂ = {id, swap}.

**Theorem.** Π₁ ∩ Π₂ ≠ ∅. In fact this holds for *all* a, b, d₁, d₂
— the pair-multiset-preservation hypothesis (∗) is not even needed.
Moreover Π₂ = {id, swap} always, and Π₁ always contains id (k₁ even)
or swap (k₁ odd), where d₁(j) = ε₁j + k₁.

## Proof

**Step 1 — classes.** t = 2: classes are even positions {0,2,4} and
odd positions {1,3,5}.

**Step 2 — dihedral maps permute parity classes (general fact).**
Write d(j) = εj + k (mod 6), ε = ±1. Since 6 is even and ε is odd,
parity(d(j)) = parity(j) ⊕ parity(k): d maps the even class
bijectively onto the class of parity k, and the odd class onto the
class of parity 1 − k. Hence the per-class multisets of d(a) are
exactly a's per-class multisets, under id if k is even and under swap
if k is odd. So Π₁ ∋ id (k₁ even) or Π₁ ∋ swap (k₁ odd); Π₁ ≠ ∅
for every a and every d₁. (This step is general; the special input
is Step 3.)

**Step 3 — mod 7 sequences are 3-periodic, so both classes coincide.**
M = [[6,−1],[1,0]] satisfies M³ ≡ I (mod 7) by direct computation
(M² ≡ [[0,1],[6,6]], M³ ≡ [[1,0],[0,1]]), so every recurrence
sequence b mod 7 has b_{j+3} = b_j. Its even class is
{b₀, b₂, b₄} = {b₀, b₂, b₁} and its odd class is {b₁, b₃, b₅} =
{b₁, b₀, b₂} — the same multiset. The same holds for d₂(b), which
is also 3-periodic (d₂(j+3) ≡ d₂(j) ± 3 (mod 6), and b is 3-periodic).
Hence Π₂ = {id, swap} for every b and every d₂.

**Conclusion.** Π₁ ∩ Π₂ = Π₁ ≠ ∅. ∎

## Independent numerical confirmation (not part of the proof)

Fresh implementation (no wave-12 code reused):
[wave13_PC_m6.py](wave13_PC_m6.py)
enumerates all 25 × 49 = 1225 pairs (a, b) and all 12 × 12 pairs
(d₁, d₂): **79 632 preserved cases, 0 bad** — reproducing wave 12's
count exactly. The π-shapes match the proof: Π₂ is full in all
79 632 cases; Π₁ is full in 43 344, {id} in 18 144, {swap} in 18 144,
never empty. A separate unconditional check confirms Π₁ ≠ ∅ for all
300 pairs (a, d₁) and Π₂ full for all 588 pairs (b, d₂).

## Scope and what remains

- This closes Lemma PC **only for (m, p₁, p₂) = (6, 5, 7)**. General
  PC is still open: Step 2 generalises (d always induces a class map
  in D_t), but Step 3 used the accident that period 3 (mod 7) against
  classes mod 2 makes the two class multisets coincide. For other
  (m, p₁, p₂) the intersection needs genuine coupling, not this trick.
- This does not close G3 in general, nor G1/G2, nor exact per-class.
  Repository untouched; no Lean built; nothing here is a Lean theorem.
