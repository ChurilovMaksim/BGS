# Wave 27, task 1: lemma M4 proved (level-4 collapsed shift)

## 1. Statement

Let p be odd, modulus p⁴, R = Z[√2], α = 3+2√2, L₀ = ord(α mod p),
γ = α^{L₀} = 1 + p·u with k = 1 (u ≢ 0 mod p), s = 3 (m = L₀·p³).
Write u ≡ μ√2 mod p (μ ≠ 0) and u = μ√2 + p·u₁ mod p².
Let A, A′ be units with equal global multisets {Tr(Aα^i)} mod p⁴,
and let π, η be the level-3 output (repaired f = 3, (1,2)):
A′ = A^ε·α^s·(1 + pη) with η ≡ 0 mod p, η = pη₁ + p²η₂,
Tr(η₁) = 0 (so η₁ = ν₁√2). Then the level-4 per-class multisets
match under π. In particular the rigid-block shift vanishes: δ = 0
for every collapsed orbit. This closes G1 at f = 4, case (1,3).

## 2. Orbit structure

For C ∈ R and j ∈ Z/p³, Φ_C(j) = Tr(Cγ^j)
= Tr(C) + jp·T₁ + C(j,2)p²·T₂ + C(j,3)p³·T₃ mod p⁴,
Tᵢ = Tr(Cu^i). Collapsed means T₁ ≡ 0 mod p, i.e. C ≡ c ≠ 0 mod p
(unit case; c = 0 is the induction case). Key fact:
T₂ ≡ Tr(c·2μ²) = 4cμ² ≢ 0 mod p, so t₂ ≠ 0 for every collapsed
unit orbit — the degenerate t₂ = 0 cases never occur here.
With j = a + pb + p²c′: Φ_C(j) = Tr(C) + p²D_a + p³·b·L_a mod p⁴,
D_a = a·T₁′ + C(a,2)·T₂ (mod p²), L_a = t₂(a − a₀) (mod p),
vertex a₀ = 1/2 − t₁/t₂. Hence: lines a ≠ a₀ are full p³-lines
(p values, mult p each, in one mod-p³ fiber); the vertex block
a = a₀ is a single rigid value κ = Tr(C) + p²D_{a₀} with mult p².
Non-collapsed orbits (T₁ ≢ 0) have p³ distinct values; in each
mod-p³ fiber their p values form a full line.

## 3. Lemma I1 (general, proved)

Tr(u₁) ≡ 2μ² mod p. Proof: N(γ) = 1. Write u = a + b√2.
N(1 + pu) = 1 + 2pa + p²(a² − 2b²) = 1 gives 2a + p(a² − 2b²) = 0,
so p | a; write a = pa₁. Then 2a₁ + p²a₁² − 2b² = 0, so
a₁ ≡ b² mod p. Since μ ≡ b mod p and u₁ ≡ a₁ + b₁√2 mod p
(b = μ + pb₁), Tr(u₁) = 2a₁ ≡ 2b² ≡ 2μ² mod p. ∎
Verified: 0 violations at all 92 k = 1 primes ≤ 500 (13, 31 are k ≥ 2).

## 4. Twist and reduction to τ₂ = 0

Twist: Δ_C(j) = p·Tr(Cηγ^j) ≡ p²Tr(Cη₁) + p³(j·Tr(Cη₁u) + Tr(Cη₂))
mod p⁴. Since Tr(η₁) = 0, p²Tr(Cη₁) ≡ 0 mod p³, so fibers
(mod p³) are preserved. Non-collapsed orbits and collapsed lines
are preserved: within a fiber the twist shift is constant
(j ≡ a mod p fixed in the fiber), permuting the full line.
For the rigid block, κ′ = κ + p³δ with
δ = ν₁·c·(2μ² − Tr(u₁))/μ + c·τ₂, τ₂ = Tr(η₂).
By I1 the first term vanishes: δ = c·τ₂. So M4 ⟺ τ₂ = 0.

## 5. Fiber argument: τ₂ = 0

Fix a mod-p³ fiber w. Its multiset = uniform layers + rigid values.
Uniform layers: every line block and every full block contributes
the full F_p layer in its fiber (mult p resp. mult 1), and the
twist permutes each layer within itself. So the multiset of rigid
values {κ_O} in fiber w is preserved: {κ_O + p³δ_O} = {κ_O}.
All rigid orbits in fiber w share residue c = w/2 mod p
(κ_O ≡ w mod p gives 2c_O ≡ w mod p), hence all δ_O = c·τ₂ = δ.
Collapsed γ-orbits number 0 or d, d = gcd(L₀,2) ≤ 2: indeed
Aα^i is real mod p ⟺ L₀ | 2(i − i₀), giving d·p³ values of i,
i.e. d γ-orbits. So fiber w holds ≤ 2 rigid orbits.
With 1 orbit, δ = 0 at once. With 2, {t₁ + δ, t₂ + δ} = {t₁, t₂}
gives δ = 0 (p odd: else 2δ = 0). Hence c·τ₂ = 0, so τ₂ = 0,
δ = 0 for every rigid block. Lines and full blocks are already
invariant, so per-class multisets match under π. ∎

## 6. Numerical confirmations (not proofs)

- Full G1′ at (108,3) mod 81: 6561 A, 45 groups, 0 D₄-bad pairs.
- Full G1′ at (750,5) mod 625 (new, C++): α^750 ≡ 1, γ = α⁶ =
  (226,110) of order 125, u ≡ 2√2 mod 5; 390625 A, 321 groups,
  0 groups failing class-pair constancy.
- Rigid formula κ′ = κ + 27δ verified at (108,3): 33,697,296
  rigid checks, 0 bad; δ = 0 in all cases (consistent with §5).

## 7. Limits

Proof uses the level-3 input (π, normalized η, Tr(η₁) = 0) from the
repaired f = 3, (1,2) argument (wave 26); it is a proof sketch at
that interface, not a Lean formalization. Divisible A (c = 0) goes
by induction to level 3, as in wave 26. No repository touched,
no Lean built. Remaining at f = 4: R30 (case (3,1)) only.
