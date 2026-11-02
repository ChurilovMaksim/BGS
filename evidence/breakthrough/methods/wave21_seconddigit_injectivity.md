# Wave 21, task 3 — (v0, t) injectivity on G: PROVED (part (a) only)

**Verdict.** Part (a) of the wave-19 mechanism is proved in general.
Part (b) (dichotomy with power sums) is NOT attempted here, so this
does not prove L6 or the full second-digit lemma. Repository untouched,
no Lean build, exact integer arithmetic in the check.

## Statement

Let R = ℤ[√2], p odd, α = 3+2√2, L₀ = order of α mod p, and assume
α^{L₀} ≡ 1 (mod p²) — this is the k ≥ 2 content of "k = 2, s = 0"
(the exactness k = 2, i.e. ≢ 1 mod p³, is NOT used below). Let
G = ⟨α⟩ mod p², and let A be a unit mod p². Then

**Theorem.** The map z ↦ (Tr(Az) mod p, Tr(A√2·z) mod p) is injective
on G. (Here Tr(A√2·z) = Tr(√2·Az), the t-index of wave 19.)

## Proof

**Step 1 — reduction mod p is injective on G.** Let d ∈ G with
d ≡ 1 (mod p), i.e. d = 1 + pu in R/p². By the binomial theorem,
d^p = 1 (mod p²): the j = 1 term is p·(pu) = p²u ≡ 0, and every
j ≥ 2 term carries p^j with j ≥ 2. Also d^{L₀} = 1, since
α^{L₀} ≡ 1 (mod p²). Now gcd(L₀, p) = 1: α has norm 1, so by the
split/inert dichotomy L₀ | p − ε with ε = (2/p) (norm-1 subgroup of
(R/p)× has order p − ε). By Bézout, d = d^{ap+bL₀} = 1. Hence
z₁ ≡ z₂ (mod p) implies z₁ = z₂ for z₁, z₂ ∈ G.

**Step 2 — (v0, t) determines w = Az mod p.** Write w = x + y√2 with
x, y ∈ 𝔽_p ({1, √2} is a basis of R/p over 𝔽_p, split or inert).
Then Tr(w) = 2x and Tr(√2·w) = Tr(2y + x√2) = 4y. Since p is odd,
2 and 4 are units in 𝔽_p, so x = v0/2 and y = t/4: w is recovered
from (v0, t).

**Step 3 — assembly.** If φ_A(z₁) = φ_A(z₂), Step 2 gives
Az₁ ≡ Az₂ (mod p). A is a unit mod p², hence a unit mod p, so
z₁ ≡ z₂ (mod p); Step 1 gives z₁ = z₂. ∎

## Where each hypothesis is used (sharpness)

- p odd: Step 2 inverts 2 and 4. At p = 2 the formulas collapse.
- A unit: Step 3 inverts A mod p. Without it the claim is false
  already trivially: A ≡ 0 (mod p) gives (v0, t) = (0, 0) for all z.
- α^{L₀} ≡ 1 (mod p²): Step 1 needs d^{L₀} = 1 for d ∈ G. If the
  order mod p² were L₀p instead (k = 1 in the other normalisation),
  G would contain 1 + pu ≠ 1 elements and injectivity would fail.
- Exact k = 2 unused: (a) holds for every k ≥ 2 (wave-12 notation),
  i.e. whenever the order mod p² is still L₀.

## Numerical check (confirmation, not part of the proof)

Script `wave21_injectivity_check.py`: for p = 13 (L₀ = 14) and p = 31
(L₀ = 15), all units A mod p (168 and 900) and all z ∈ G:
**0 collisions** (and α^{L₀} ≡ 1 mod p² confirmed in both cases).

## Scope

Only part (a) is closed. What remains for the second-digit lemma:
part (b), the dichotomy "power sums detect non-real-B twists, second
digits detect real-B twists"; and for G1 itself: the f = 2 s = 0 hole
proper (needs 4 | L₀, no instance below 2×10⁹), f ≥ 4, general PC.
