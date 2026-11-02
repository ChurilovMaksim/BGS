# Wave 31, task 1 — Joint Lemma for R30: PROVED

**Verdict: the Joint Lemma is proved, and the gap hypothesis is not
needed.** It holds for every base with b₁ ≠ 0, gap or not. Hence
R30 is closed (wave 30's assembly plus this lemma), and G1 at f = 4
is closed in all four (k, s) cases: (2,2) wave 26, (1,3) via M4,
(3,1) via R30, (4,0) via R40 plus R30 for the divisible case.
Repository untouched, no Lean built (proof sketch, not Lean).

## Setup

p odd, R = ℤ[√2], β ∈ T₃ of norm 1 and order H0 ≥ 3, τ ∈ T₃,
B = τ(1 + pλ₁ + p²λ₂), λ₁ = a₁ + b₁√2, λ₂ ∈ R/p, b₁ ≠ 0.
Orbit values v_j = Tr(Bβ^j) mod p³, digits v_j = v0_j + p·v1_j +
p²·v2_j. Write T_j = τβ^j, τ̄_j = T_j mod p = x_j + y_j√2,
t_j = Tr(τ̄_j√2) = 4y_j, N₀ = N(τ̄) (constant on the orbit since
N(β̄) = 1). The p²-twist is B ↦ B(1 + p²σ), σ ∈ R/p.

## Step 1: r = 2 forces Re(σ) = 0

v′_j = v_j + p²·Tr(στ̄_j), so Σ(v′)² − Σv² = 2p²·Σ_j v_jTr(στ̄_j)
mod p³. Mod p, v_j = Tr(τ̄_j), and Tr(x)Tr(y) = Tr(xy) + Tr(xȳ)
gives Σ_j Tr(τ̄_j)Tr(στ̄_j) = Tr(σΣ_j τ̄_j²) + H0·N₀·2Re(σ).
Now Σ_j τ̄_j² = τ̄²Σ_j β̄^{2j} = 0 (β̄² ≠ 1 as H0 ≥ 3), so
preservation forces 4p²H0N₀Re(σ) ≡ 0 mod p³, i.e. Re(σ) = 0
(p ∤ H0, N₀ a unit). Hence σ = g√2, and the twist is the shear
v2_j ↦ v2_j + g·t_j, fixing (v0_j, v1_j).

## Step 2: digit formula (the key lemma)

v1_j = d1_j + Tr(λ₁τ̄_j), where d1_j is the p-digit of Tr(T_j).
Claim: d1_j = D(v0_j, N₀) for a function D. Indeed, ξ ∈ R/p is
determined up to conjugation by (Tr ξ, N ξ), and d1 is
conjugation-invariant (Tr(T_{conj ξ}) = Tr(conj T_ξ) = Tr(T_ξ)).
Since N is constant on the orbit, d1_j depends on τ̄_j only
through v0_j = Tr(τ̄_j). With Tr(λ₁τ̄_j) = a₁v0_j + b₁t_j:
**v1_j = D(v0_j, N₀) + a₁v0_j + b₁t_j.**

## Step 3: (v0, v1) is injective when b₁ ≠ 0

Given (v0_j, v1_j), Step 2 gives t_j = (v1_j − D(v0_j, N₀) −
a₁v0_j)/b₁ (b₁ ≠ 0, p odd). Then (v0_j, t_j) = (2x_j, 4y_j)
determines τ̄_j = x_j + y_j√2, hence j (β̄ has order H0). So
every (v0, v1)-fiber is a singleton.

## Step 4: some t_j ≠ 0

If t_j = 0 for all j, then τ̄ and τ̄β̄ are both real, so β̄ is
real of norm 1, i.e. β̄ = ±1, contradicting H0 ≥ 3.

## Theorem (Joint Lemma)

Let b₁ ≠ 0 and σ ≠ 0. If B(1 + p²σ) preserved the orbit
multiset, Step 1 gives σ = g√2, g ≠ 0, and the twist shears
v2 by g·t_j on singleton fibers (Step 3), so preservation
requires g·t_j = 0 for all j, contradicting Step 4. ∎

## Why moments could not see this (reconciliation with wave 30)

V0-fibers are conjugation-stable, and t flips sign under
conjugation, so every V0-fiber t-moment vanishes — coarse
statistics (marginals, orbit power sums, products) are blind to
the shear. The shear is visible only in the (v0, v1)-conditional
distribution, because within a V0-fiber, v1 = const + b₁·t
(Step 2): the fiber label itself encodes the shear amount. The
wave-30 "fiber power sums matching identically" are over the
coarser V0-fibers; over (v0, v1)-fibers the first power sum
already differs.

## Verification (exact arithmetic)

- Teichmüller orbits at p = 5, 7, 13 (wave-30 setting):
  2299/2299 bases with b₁ ≠ 0 have max (v0, v1)-fiber size 1
  and no nonzero preserving twist (1398 gap, 901 non-gap);
  digit formula holds in 2700/2700 cases.
- Robustness: 1187/1187 random norm-1 β̄ cases (p = 3, 5, 17, 19)
  satisfy injectivity and no-preserving-twist, so the lemma is
  not an artifact of α-powers or of p ∈ {5, 7, 13}.

## Files

- This note: wave31_JointLemma.md
- Checks: wave31_explore.py, wave31_explore3.py, wave31_explore4.py
- Prior: wave30_R30_close.md §4 (statement), wave28_R30_P2.md
  §1 (digit setup), wave27_R30_gapcond.md (gap symmetry, unused)
