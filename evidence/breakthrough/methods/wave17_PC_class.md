# Wave 17, task 2 — Lemma PC generalised to a class: PROVED for (m, 3, 17), 8 | m

## Theorem (class)

Let 8 | m, t = 4, classes O_r = {r, r+4, …} (size m/4). Let a (mod 3),
b (mod 17) be recurrence sequences of length m, d₁, d₂ ∈ D_m, and
Π₁, Π₂ the π-sets for (a, d₁(a)) and (b, d₂(b)). If the pair multiset
is preserved, {(a_{d₁(j)}, b_{d₂(j)})} = {(a_j, b_j)} as multisets (∗),
then Π₁ ∩ Π₂ ≠ ∅. This is non-degenerate: neither Πᵢ is forced full.

## 1. The primes are forced, not chosen

The (8,3,17) proof of wave 14 rests on two structural pillars. Each
forces its prime uniquely (α = 3+2√2, R = ℤ[√2], α⁴ = 577+408√2).

**Doubling side.** If every sequence mod p is t-periodic (class
multiset = repeats of one value v_r), then for A = 1 the traces give
Tr(α^t) = 2 and Tr(α^{t+1}) = 6, forcing α^t = 1 in R/p. For t = 4:
α⁴ − 1 = 576+408√2, and p divides it in R iff p | 576 and p | 408,
iff p | gcd(576,408) = 24, iff p ∈ {2, 3}. The only odd doubling
prime is **3**.

**Symmetric-pair side.** If every sequence mod p is t-antiperiodic
(class multiset = copies of {w_r, −w_r}), the same trace argument
forces α^t = −1. For t = 4: α⁴ + 1 = 578+408√2, and p divides it iff
p | gcd(578,408) = 34, iff p ∈ {2, 17}. The only odd symmetric prime
is **17**.

**No mixed case.** α⁴ − 1 = 24√2·α² and α⁴ + 1 = 34α² factor as
primes in {2, 3, 17} times units, so no prime has α⁴ = (1, −1) in the
split case either: α⁴ is never mixed, and outside {3, 17} it is
neither 1 nor −1.

**Other t.** t = 2 (m ≡ 2 mod 4): doubling needs α² = 1, but
α² − 1 = 16+12√2 has gcd(16,12) = 4, so p = 2 only — no odd doubling
prime, hence no non-degenerate pair at t = 2. (The symmetric prime
α² = −1 is p = 3, since gcd(18,12) = 6, but Fix_m mod 3 = {0} for
m ≡ 2 mod 4 because α^m = −1 there, so that side is degenerate.)
t = 1 (m odd): D₁ is trivial, PC is vacuous.

**Divisibility.** 3 | D_m ⟺ 4 | m (wave 9 valuation), and
17 | D_m ⟺ 8 | m: mod 17, α ↦ (15, 8), both of order 8, and
s_m = 15^m + 8^m ≡ 2 (mod 17) only for m ≡ 0 (mod 8). So the
non-degenerate class is exactly 8 | m with (p₁, p₂) = (3, 17).

## 2. Proof for the whole class (multiplicity scaling)

Let m = 8n. Everything in wave 14, §§1–7, goes through with one
change: multiplicities. Mod 3, α⁴ = 1, so a is 4-periodic and the
class-r multiset of a is 2n copies of v_r, with the same
v = (−x, −y, x, y) over 𝔽₃ (the computation uses only R/3).
Mod 17, α⁴ = −1, so b is 4-antiperiodic and the class-r multiset of
b is n copies of {w_r, −w_r}. Each d ∈ D_m induces
π_d(r) = εr + k (mod 4) ∈ D₄ — well defined since 4 | m — mapping
O_r bijectively onto O_{π_d(r)}.

Reduction: pairs in class r are n copies of (v_r, w_r) and n copies
of (v_r, −w_r); mixed pairs in class r are n copies of
(v_{π₁(r)}, w_{π₂(r)}) and n copies of (v_{π₁(r)}, −w_{π₂(r)}).
Grouping by first coordinate and dividing multiplicities by n gives
exactly condition (P) of wave 14, §2. The recovery lemma is
unchanged (a union of symmetric pairs with multiplicity n determines
the pair multiset, since n·mult determines mult). The fibre
analysis is unchanged: v over 𝔽₃ has fibres of size ≤ 2 (𝔽₃ˣ = {±1}
forces x = ±y or one zero), the reflection ρ ∈ Stab(v) swaps within
pair fibres and fixes singletons, and cases (A)/(B) are identical.
Assembly is identical: δ ∈ Stab(v)·Stab(C) gives
π = σ_c ∘ π₂ ∈ Π₁ ∩ Π₂. ∎

**Degenerate boundary.** For m ≡ 4 (mod 8), Fix_m mod 17 = {0}
(α^m = −1, so (α^m − 1)B = −2B = 0), hence Π₂ = D₄ trivially and PC
holds degenerately for (m, 3, 17). The theorem above is stated for
8 | m precisely to exclude this.

## 3. Where the argument breaks outside the class

Take p = 5, a legitimate PC prime (5 | D₁₂). Mod 5,
α⁴ ≡ 2+3√2 ≢ ±1. The sequence from A = 1 has s_j mod 5 =
2, 1, 4, 3, 4, …: y₄ = 4 while y₀ = 2 and −y₀ = 3, so it is neither
4-periodic nor 4-antiperiodic. Class multisets mod 5 are therefore
neither repeated values nor symmetric pairs in general — both
pillars fail at step 1. By the §1 gcd argument this happens for
every prime outside {3, 17} at t = 4: the (8,3,17) argument cannot
be transplanted to other primes, only to other m.

## 4. Numerical confirmation at new members of the class

Exact C++ check ([wave17_PC_class_check.cpp](sandbox://workspace/bgs-breakthrough/methods/wave17_PC_class_check.cpp)):
all recurrence sequences mod 3 (9) and mod 17 (289), all
(d₁, d₂) ∈ D_m × D_m, pair-multiset preservation tested exactly,
Π₁ ∩ Π₂ computed exactly for every preserved case.

| m | (d₁,d₂) cases | preserved | bad |
|---|---|---|---|
| 16 | 2,663,424 | 1,090,560 | 0 |
| 24 | 5,992,704 | 2,453,760 | 0 |

Structural assertions passed for every enumerated sequence:
4-periodicity mod 3, 4-antiperiodicity mod 17, m-periodicity.

## 5. Scope

This closes PC for (m, 3, 17) with 8 | m — infinitely many m, one
prime pair. General PC (arbitrary p₁, p₂ | D_m) remains open: the
proof uses t = 4, α⁴ = ±1, and the 𝔽₃ fibre bound, none of which
survives outside this class. Repository untouched; no Lean built;
nothing here is a Lean theorem.
