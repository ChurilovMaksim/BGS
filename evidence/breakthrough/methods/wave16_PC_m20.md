# Wave 16, task 2 — Lemma PC for (m, p₁, p₂) = (20, 41, 19): PROVED, degenerate

## Statement

As in [wave12_g3_common_pi.md](wave12_g3_common_pi.md)
§3, let a (mod 41), b (mod 19) be recurrence sequences of length 20
(y_{j+1} = 6y_j − y_{j−1}), d₁, d₂ ∈ D₂₀, d(j) = εj + k (mod 20).
Classes O_r = {r, r+4, r+8, r+12, r+16}, r ∈ ℤ/4, t = gcd(20, 4) = 4,
so each class has size 5. D₄ acts by r ↦ εr + k (mod 4).
Πᵢ = {π ∈ D₄ : per-class multisets of dᵢ(seq) at r equal those of
seq at π(r) for all r}; π_{dᵢ} = (εᵢ, kᵢ mod 4) ∈ Πᵢ always.
Hypothesis (∗): {(a_{d₁(j)}, b_{d₂(j)})} = {(a_j, b_j)} as multisets.

**Theorem.** Π₁ ∩ Π₂ ≠ ∅. In fact this holds for *all* a, b, d₁, d₂
— hypothesis (∗) is not needed, and Π₁ = D₄ always.

## 1. The 41 side: period 5 = class size 5

Work in R = ℤ[√2], α = 3 + 2√2, β = ᾱ, y_j = Tr(Aα^j).
Mod 41, by direct computation:
α² = 17 + 12√2, hence
α⁴ = (17 + 12√2)² = 577 + 408√2 ≡ 3 − 2√2 = β (mod 41),
since 577 = 14·41 + 3 and 408 = 9·41 + 39 ≡ −2.
Therefore α⁵ = αβ = N(α) = 9 − 8 = 1 in R/41.
So every mod-41 sequence is 5-periodic: a_{j+5} = a_j.

Each class O_r = {r + 4k : k = 0..4} meets every residue mod 5
exactly once (r + 4k ≡ r − k mod 5). Hence the class-r multiset
of a is {a₀, a₁, a₂, a₃, a₄} =: W_a, independent of r.
The same holds for d₁(a) (a dihedral image of a recurrence
sequence is a recurrence sequence, hence also 5-periodic, with
class multisets W_a). So for every π ∈ D₄ and every r,
multiset of d₁(a) at r (= W_a) = multiset of a at π(r) (= W_a):
**Π₁ = D₄ always.**

## 2. Assembly

π_{d₂} ∈ Π₂ always (d₂ maps O_r bijectively onto O_{π_{d₂}(r)}).
Since Π₁ = D₄, π_{d₂} ∈ Π₁ as well. Thus Π₁ ∩ Π₂ ∋ π_{d₂} ≠ ∅. ∎

## 3. Degeneracy verdict: YES, degenerate — same mechanism as before

This is degenerate in exactly the sense of (6, 5, 7) and (12, 5, 7):
on one side, the sequence period equals the class size, forcing
that side's Π full. There the period was 3 = class size 3 (mod 7);
here it is 5 = class size 5 (mod 41). The mod-5 side plays no role,
and no new idea toward general PC is used or gained.
The 19 side, by contrast, is genuinely non-degenerate: α⁴ has
order 5 mod 19, class multisets are γ-orbits (γ = α⁴), and Π₂ is
forced full only for the zero sequence (see §4). But the theorem
does not need the 19 side at all.

## 4. Numerical confirmation (exact, [wave16_PC_m20.py](wave16_PC_m20.py))

- α⁴ ≡ β (mod 41), α⁵ = 1 (mod 41): verified.
- All 1681 mod-41 sequences: all four class multisets equal, 0 bad.
- All 361 mod-19 sequences × 40 dihedral maps: π_d ∈ Π₂ always;
  Π₂ full in only 40 of 14440 cases (the zero sequence × 40 d's).
  E.g. B = (0, 1), d = id gives Π₂ = {id, (−1, 2)}, a 2-element set.
- No preserved-pair enumeration was needed: the proof is
  unconditional (∗-free), so enumerating preserved cases would
  only re-verify a weaker statement.

## 5. Scope

This closes PC only for (20, 41, 19), degenerately. General PC
remains open, and the only non-degenerate proved case remains
(8, 3, 17) (symmetric-pair recovery + stabiliser product).
Repository untouched; no Lean built; nothing here is a Lean theorem.
