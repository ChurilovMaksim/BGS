# Wave 26, task 2 — The next non-degenerate PC case: (12, 3, 5), PROVED

## Verdict

The next genuinely non-degenerate PC triple outside the (3,17)/8|m class
is **(m, p₁, p₂) = (12, 3, 5)**, and PC is **proved** for it (§§2–5 below),
not only verified. The checker (wave26_PC_check.cpp, exact arithmetic,
fibre reduction e = d₂∘d₁⁻¹) confirms: 115,776 preserved cases, 0 bad,
with a non-degeneracy witness (§6). Repository untouched; no Lean built.

## 1. Search order: why (12, 3, 5) is next

PC setup (wave 14): sequences a_j = Tr(Aα^j) mod p₁, b_j = Tr(Bα^j) mod p₂,
α = 3+2√2, classes O_r = {r, r+t, …}, t = gcd(m,4), d ∈ D_m,
π_d(r) = εr+k mod t, Πᵢ = {π ∈ D_t : class multisets match};
hypothesis (∗): pair multiset preserved; conclusion Π₁ ∩ Π₂ ≠ ∅.
Non-degenerate = neither Πᵢ forced full (both sides vary).
Odd m is vacuous (D₁ trivial); m = 4 has only prime 3. Results:

| triple | preserved | bad | nondeg | reason |
|---|---|---|---|---|
| (6, 5, 7) | 79,632 | 0 | NO | known degenerate: 7-side forced full |
| (8, 3, 17) | 272,640 | 0 | YES | the excluded class (reproduces wave 14 exactly) |
| (10, 29, 41) | 84,336,400 | 0 | NO | 41-side forced full: ord(α)=5 mod 41, so α ∈ ⟨α²⟩ and every class has the same 5-orbit multiset (contrast ord(α)=10 mod 29) |
| (12, 3, 5) | 115,776 | 0 | YES | **next: proved below** |
| (12, 3, 7) | 254,016 | 0 | NO | 7-side forced full (ord(α)=3 mod 7) |
| (12, 3, 11) | 316,224 | 0 | YES | found, proof not attempted here |
| (12, 5, 7) | 318,528 | 0 | NO | known degenerate (wave 15) |
| (12, 5, 11) | 590,400 | 0 | YES | found, proof not attempted here |
| (12, 7, 11) | 1,479,744 | 0 | NO | 7-side forced full |

Checker validation: (8,3,17) reproduces wave 14's 272,640 preserved cases
exactly (297 skipped constant-side pairs contribute 297·256); (6,5,7)
reproduces wave 13's degeneracy (side 2 forced full). All odd p | D_m
satisfy α^m ≡ 1 mod p (norm argument: X_m ≡ 1 forces Y_m ≡ 0), so the
enumeration is all of R/p₁ × R/p₂.

## 2. The mod-3 side (wave 14, unchanged)

α⁴ = 1 mod 3, so a is 4-periodic; class-r multiset of a is {v_r ×3} with
v = (−x, −y, x, y) mod 3 for A = (x,y). If A = 0, Π₁ = D₄ (trivial).
Else v-fibres have size ≤ 2 (𝔽₃ˣ = {±1}), and some reflection
ρ = (−1,k) ∈ Stab(v), ρ ≠ id, swaps within pair fibres and fixes
singletons (cases: x=0 → k=2; y=0 → k=0; x=y → k=1; x=−y → k=3).
Hence Π₁ = δ₁·Stab(v) ∋ {δ₁, δ₁ρ}, δ₁ = π_{d₁}.

## 3. The mod-5 side: triangles, not symmetric pairs

α⁶ = 1 mod 5, ζ := α⁴ has order 3, ζ² = α², 1+ζ+ζ² = 0.
Class O_r = {r, r+4, r+8} carries the triangle
T_r = {Tr(Bα^r), Tr(Bα^r ζ), Tr(Bα^r ζ²)} (sums to 0 mod 5).
Since α² ∈ ⟨ζ⟩, Bα^{r+2} lies in the same ζ-coset as Bα^r, so
**CM^b = (M, N, M, N)** with M = T(B), N = T(Bα), for every B
(verified: 0 pattern violations over all 25 B).
If M = N, Π₂ = D₄ (trivial). Else Stab of the pattern is the Klein
group K = {id, s₂, ρ₀, ρ₂} (shifts by 0,2; reflections −r, −r+2),
index 2 in D₄, and Π₂ = δ₂·K, δ₂ = π_{d₂}.

## 4. Reduction (P) and the triangle recovery lemma

Grouping (∗) by first coordinate p (a is constant = v_r on class r):
original pairs with first coordinate p give ⊔_{r ∈ F} T_r, mixed pairs
give ⊔_{s : δ(s) ∈ F} T_s, where F is the v-fibre of p and
δ = π₁∘π₂⁻¹. Hence (P): ⊔_{f ∈ F} T_{ε(f)} = ⊔_{f ∈ F} T_f with
ε = δ⁻¹, for every v-fibre F. Since |F| ≤ 2, (P) implies the
item-level condition (I): {T_{ε(f)} : f ∈ F} = {T_f : f ∈ F}, provided:

**Lemma (triangle recovery).** The 7 orbit-triangles mod 5 —
(0,0,0), (0,1,4), (0,2,3), (1,1,3), (1,2,2), (2,4,4), (3,3,4) —
have the property that T_a ⊔ T_b = T_c ⊔ T_d implies
{T_a, T_b} = {T_c, T_d}. Verified exhaustively: 0 collisions among all
pairs of unions. (|F| = 1 is trivial; |F| = 2 is the lemma.)

## 5. Assembly (wave 14 §§5–7 verbatim, with triangles for pairs)

Singletons give T_{ε(s)} = T_s pointwise; pair fibres give match-or-swap
by (I). The case analysis (A)/(B) uses only fibre sizes ≤ 2 and
ρ ∈ Stab(v), so it yields E = T or E = T∘ρ (E = T∘ε), hence
δ ∈ Stab(v)·Stab(T); writing δ = σ_v ∘ σ_c, the element
π = σ_c ∘ π₂ lies in Π₁ ∩ Π₂ (same computation as wave 14 §7).
This proves PC for (12, 3, 5). ∎

## 6. Obstruction: what blocks a direct (3,17) transplant

- No ±1: at t = 4 the only odd primes with α⁴ = ±1 are 3 and 17
  (gcd argument, wave 17 §1). At (12,3,5) the 5-side has α⁴ = ζ of
  order 3, so classes are triangles, not symmetric pairs: the
  (3,17) recovery lemma (mult_U(y) counts pairs) does not apply and
  is replaced by the finite 7-triangle recovery lemma of §4, which
  is a specific-prime check, not a general lemma.
- Antiperiodicity is replaced by the (M,N,M,N) pattern (coset
  argument α² ∈ ⟨ζ⟩), and Stab(T) = K replaces Stab(C).
- Π-shapes alone do NOT force the conclusion: Π₁ = δ₁·{id,ρ} and
  Π₂ = δ₂·K can be disjoint as sets (e.g. ρ ∈ K with δ₂⁻¹δ₁ ∉ K).
  The hypothesis (∗) is essential — it supplies (P), and only
  through (P)→(I)→assembly does the intersection follow.
  A proof that only bounds Π₁, Π₂ is impossible in general.

## 7. Non-degeneracy witness and scope

Witness (d₁ = d₂ = id): A giving v = (0,2,0,1) (fibres [0,2],[1],[3]),
Π₁ = {id, ρ₂} (mask 65); B giving triangles ((2,4,4),(1,1,3),(2,4,4),
(1,1,3)), Π₂ = K (mask 85); intersection {id} ≠ ∅, both proper
subsets of D₄. Neither side is forced full (checker flags 0,0).
Open: proofs for (12,3,11) and (12,5,11); general PC; Lean formalisation
of any of this. The class (m,3,17), 8|m, is now joined by at least one
proved non-degenerate triple, but no new infinite class is claimed.
