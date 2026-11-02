# Wave 15, task 2 — Lemma PC for (m, p₁, p₂) = (12, 5, 7): PROVED

## Statement

As in [wave12_g3_common_pi.md](sandbox://workspace/bgs-breakthrough/methods/wave12_g3_common_pi.md)
§3, let a (mod 5), b (mod 7) be recurrence sequences of length 12
(y_{j+1} = 6y_j − y_{j−1}), d₁, d₂ ∈ D₁₂, d(j) = εj + k (mod 12).
Classes O_r = {r, r+4, r+8}, r ∈ ℤ/4, t = gcd(12, 4) = 4, D₄ acting
by r ↦ εr + k (mod 4). Πᵢ = {π ∈ D₄ : per-class multisets of
dᵢ(seq) at r equal those of seq at π(r) for all r}. Hypothesis (∗):
{(a_{d₁(j)}, b_{d₂(j)})} = {(a_j, b_j)} as multisets of pairs.

**Theorem.** Π₁ ∩ Π₂ ≠ ∅. In fact this holds for *all* a, b, d₁, d₂
— hypothesis (∗) is not needed, and Π₂ = D₄ always.

## 1. Every mod-7 recurrence sequence is 3-periodic

Let (y_j) satisfy the recurrence mod 7. Then y₂ = 6y₁ − y₀, and
y₃ = 6y₂ − y₁ = 35y₁ − 6y₀ ≡ y₀ (mod 7), since 35 ≡ 0 and −6 ≡ 1;
y₄ = 6y₃ − y₂ = 7y₀ − 6y₁ ≡ y₁ (mod 7). Hence (y₃, y₄) = (y₀, y₁),
so by induction y_{j+3} = y_j for all j (3 divides 12, so this is
consistent cyclically). In R = ℤ[√2] terms this is α³ = 1 mod 7, but
the direct computation above needs no representation.

## 2. Every class multiset of b equals one fixed W

The class O_r = {r, r+4, r+8} has residues mod 3 equal to
r, r+1, r+2 (since 4 ≡ 1, 8 ≡ 2 mod 3), i.e. all of ℤ/3 exactly once.
Since b_j depends only on j mod 3 (§1), the class-r multiset is
{b^{(0)}, b^{(1)}, b^{(2)}} =: W, independent of r, where b^{(s)} is
the value of b at residue s mod 3.

## 3. Π₂ = D₄

For d₂(j) = εj + k, j = r + 4s ∈ O_r maps to εr + k + 4εs, which
runs over O_{π(r)} with π(r) = εr + k (mod 4); so d₂ bijects O_r
onto O_{π_{d₂}(r)}. Hence the class-r multiset of d₂(b) equals the
class-π_{d₂}(r) multiset of b, which is W by §2. But the class-π(r)
multiset of b is also W for *every* π ∈ D₄. So every π ∈ D₄
satisfies the defining equality of Π₂: Π₂ = D₄.

## 4. Assembly

The same bijection argument gives π_{d₁} ∈ Π₁ always. Since
Π₂ = D₄, π_{d₁} ∈ Π₁ ∩ Π₂. ∎

## 5. Numerical confirmation and scope

Fresh implementation (no wave-12 code reused):
[wave15_PC_m12.py](sandbox://workspace/bgs-breakthrough/methods/wave15_PC_m12.py)
enumerates all 25 × 49 pairs (a, b) and all 24 × 24 pairs (d₁, d₂):
**318,528 preserved cases (reproducing wave 12 exactly), 0 bad**;
the structural checks (3-periodicity mod 7, constant class
multisets, Π₂ = D₄ for every (b, d₂)) all pass.

This closes PC only for (12, 5, 7), and it is degenerate in the same
sense as the wave-13 (6, 5, 7) case: the mechanism is period 3 =
class size 3 at p₂ = 7, so Π₂ is forced full and the mod-5 side and
hypothesis (∗) play no role. It adds no new idea toward general PC,
whose non-degenerate proved case remains (8, 3, 17). Repository
untouched; no Lean built; nothing here is a Lean theorem.
