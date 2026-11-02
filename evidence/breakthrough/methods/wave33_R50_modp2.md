# Wave 33, task 5 — R50 mod-p² step: PROVED IN CORRECTED FORM

**Verdict.** The power-sum step holds, but wave-32 §5's stated
conclusion "→ η = b√2" is FALSE as written. The exact conclusion
is η ≡ b√2 + p²b₀² (mod p³), b₀ ≡ b (mod p). The extra term is
forced by the p⁴ term in the squared-trace expansion, which is
invisible at level p⁴ (R40) but visible at level p⁵ (R50).

## 1. Statement

p odd, R = Z[√2], H ⊆ R/p⁵ cyclic norm-1, |H| = n ≥ 3,
gcd(n, p) = 1. Units C, C′ mod p⁵ with the same H-orbit multiset
{Tr(Cζ) : ζ ∈ H} mod p⁵. (The real-case hypothesis is not used
in this step, exactly as in R40 Step 2.)

**Mod-p² step (corrected).** After the L6 normalisation
(wave-25, f = 2, s = 0) C′ ≡ C (mod p²), write C′ = C(1 + p²η),
η ∈ R/p³. Then the r = 2 power sum forces
η ≡ b√2 + p²b₀² (mod p³) for some b ∈ Z/p³, b₀ ≡ b (mod p),
and every such η satisfies the r = 2 equation.

## 2. Proof

Tr(C′ζ) = Tr(Cζ) + p²Tr(ηCζ), so mod p⁵:
ΣTr(C′ζ)² − ΣTr(Cζ)²
  = 2p²·ΣTr(Cζ)Tr(ηCζ) + p⁴·ΣTr(ηCζ)² ≡ 0.
With w = Cζ: Tr(w)Tr(ηw) = ηw² + η̄w̄² + Tr(η)N(w), and
Σζ² = Σζ̄² = 0 (β² ≠ 1 as n ≥ 3; β² − 1 is a unit mod p, hence
in R/p⁵), so ΣTr(Cζ)Tr(ηCζ) = n·Tr(η)·N(C). Likewise
ΣTr(ηCζ)² = 2n·N(η)·N(C). Dividing by 2p²nN(C) (p odd,
gcd(n, p) = 1, N(C) a unit):
  Tr(η) + p²N(η) ≡ 0 (mod p³).                (*)
Write η = a + b√2. Mod p², (*) gives 2a ≡ 0, so a ≡ 0 (mod p²);
write a = p²a₂. Then (*) mod p³ gives 2a₂ − 2b² ≡ 0 (mod p)
(a² ≡ 0 mod p), i.e. a₂ ≡ b₀² (mod p). Conversely any
η = b√2 + p²b₀² satisfies (*), since b² ≡ b₀² (mod p). ∎

## 3. Why R40 did not see it

At level p⁴ the p⁴ term vanishes mod p⁴, so (*) collapses to
Tr(η) ≡ 0 (mod p²) and η = b√2 (b ∈ Z/p²) is exact there. At
level p⁵ the p⁴ term survives and contributes exactly p²N(η),
shifting a₂ from 0 to b₀². The naive lift "η = b√2" is therefore
not a proof gap that can be patched by a stronger argument: it
is refuted by the r = 2 equation itself for every b ≢ 0 (mod p).

## 4. Numerical check (exact integers)

Teichmüller H = ⟨β⟩, β⁶ = 1 mod 5⁵ (n = 6), β³ = 1 mod 7⁵
(n = 3); random units C; twist C(1 + p²η):
- p = 5, 40 trials: pure η = b√2 fails the r = 2 power sum in
  all 29 trials with b ≢ 0 (mod 5); corrected η passes all 40.
- p = 7, 20 trials: pure fails in all 20 (b ≢ 0 mod 7);
  corrected passes all 20. Script: wave33_R50_modp2_check.py.

## 5. Consequence for R50

The remaining p³/p⁴/p⁵ fibre-pair analysis must carry the twist
as C(1 + p²b√2 + p⁴b₀²), not C(1 + p²b√2); the p⁴b₀² term is a
level-p⁴ correction that the R40 fibre argument never met. The
r = 2 sum alone leaves b₁, b₂ (b mod p³) unconstrained. Not
claimed: the p³/p⁴/p⁵ analysis, or Lean. Repository untouched.
