# Wave 24, task 3: 3-adic LTE for D_m — proved

Unconditional proof, no extra hypothesis. This closes the "proof open"
item in wave-23 §5 and makes the 3-part exponent in RB2 exact.
Repository untouched; no Lean build.

## 0. Definitions

Let α = 1+√2, β = 1−√2, αⁿ = xₙ + yₙ√2 (Pell sequences, xₙ² − 2yₙ² = (−1)ⁿ).
Let ρ = α² = 3+2√2, ρ̄ = 3−2√2, ρᵏ = Xₖ + Yₖ√2, so Xₖ = x_{2k}, Yₖ = y_{2k}.
Main's D_m = ρᵐ + ρ̄ᵐ − 2 = 2(X_m − 1) = 2(x_{2m} − 1).

**Theorem.** v₃(D_m) = 0 if 4 ∤ m; = 2v₃(m) + 2 if 4 | m.

## 1. Closed forms for D_m

Squaring αⁿ gives x_{2n} = xₙ² + 2yₙ² = 2xₙ² − (−1)ⁿ. Hence

  D_m = 2(x_{2m} − 1) = 4x_m² (m odd); = 4(x_m² − 1) = 8y_m² (m even),

using x_m² − 2y_m² = 1 for m even.

## 2. Zeros mod 3

xₙ, yₙ satisfy u_{n+2} = 2u_{n+1} + uₙ, whose matrix has det −1, hence
is invertible mod 3; since (x₈, x₉) ≡ (1, 1) = (x₀, x₁) mod 3, both
sequences have period 8 mod 3:

  xₙ mod 3 = 1,1,0,1,2,2,0,2 (n = 0..7);  yₙ mod 3 = 0,1,2,2,0,2,1,1.

Therefore xₙ ≡ 0 mod 3 ⟺ n ≡ 2 mod 4, and yₙ ≡ 0 mod 3 ⟺ 4 | n.

Consequences: m odd ⟹ v₃(D_m) = 2v₃(x_m) = 0. m ≡ 2 mod 4 ⟹
D_m = 8y_m² with 4 ∤ m, so v₃(y_m) = 0 and v₃(D_m) = 0.

## 3. Reduction for 4 | m

Write m = 2k with k even. Then D_m = 8Yₖ², so it suffices to prove

  v₃(Yₖ) = v₃(k) + 1 for all even k.

## 4. Doubling and the base case

Squaring ρʲ gives Y_{2j} = 2X_jY_j. Let k₀ be even with 3 ∤ k₀,
k₀ = 2j (j odd, 3 ∤ j). Then Y_j = y_{2j} with 2j ≡ 2 mod 4, so
v₃(Y_j) = 0 by §2, and v₃(Y_{k₀}) = v₃(X_j) with X_j = x_{2j} = 2x_j² + 1
(j odd). So the base case is:

**Lemma (mod 9).** For j odd, 3 ∤ j, v₃(2x_j² + 1) = 1.

Proof. α⁶ = 99 + 70√2 ≡ 7√2 (mod 9) and β⁶ ≡ −7√2 (mod 9) in ℤ[√2].
Write j = 6q + r, r ∈ {1, 5} (j odd, 3 ∤ j ⟺ j ≡ 1, 5 mod 6).
Since (7√2)² = 98 ≡ −1 mod 9, (7√2)^q has period 4 in q. For q even,
x_j ≡ (7√2)^q x_r; for q odd, x_j ≡ (7√2)^q y_r√2 (2 is a unit mod 9,
so halving αʲ + βʲ mod 9 is valid). With (x₁, y₁) = (1, 1) and
(x₅, y₅) = (41, 29) ≡ (5, 2) mod 9, the 8 cases give:

  r=1: q≡0→1, q≡2→8, q≡1→5, q≡3→4;  r=5: q≡0→5, q≡2→4, q≡1→1, q≡3→8.

So x_j mod 9 ∈ {1, 4, 5, 8}, hence 2x_j² + 1 mod 9 ∈ {3, 6}, i.e.
v₃ = 1 exactly. ∎

## 5. Tripling (the LTE step)

Cubing ρᵏ gives Y_{3k} = 3Xₖ²Yₖ + 2Yₖ³ = Yₖ(3Xₖ² + 2Yₖ²). If 3 | Yₖ,
then Xₖ² ≡ 1 mod 3 from Xₖ² − 2Yₖ² = 1, so with s = v₃(Yₖ) ≥ 1,

  3Xₖ² + 2Yₖ² = 3(Xₖ² + 2·3^{2s−1}u²),  2s − 1 ≥ 1,

and the bracket is ≡ Xₖ² ≢ 0 mod 3. Hence v₃(3Xₖ² + 2Yₖ²) = 1 exactly,
so v₃(Y_{3k}) = v₃(Yₖ) + 1 whenever 3 | Yₖ.

## 6. Assembly

Write k = 3^s·k₀ with k₀ even, 3 ∤ k₀. By §4, v₃(Y_{k₀}) = 1; applying
§5 s times gives v₃(Yₖ) = 1 + s = v₃(k) + 1. For 4 | m, m = 2k,

  v₃(D_m) = 2v₃(Yₖ) = 2(v₃(k) + 1) = 2v₃(m) + 2,

since v₃(k) = v₃(m/2) = v₃(m). ∎

## 7. Numerical check

Exact integer verification via the Pell recurrence to m = 200 (extending
wave-23's m ≤ 60): zero failures of the formula; D₈ = 1331712 and
D₁₂ = 1536796800 match the known values; the doubling, tripling, and
mod-9 base identities all hold on the same range. No m with a failure
exists in range, and the proof above leaves no room for one anywhere.

## 8. Consequence for RB

The 3-part exponent in RB2 is now exact, not conjectural: the only
possible on-support split 3-modulus is q₃ = 3^{2v₃(m)+2} ≤ 9m², and at
m = 48 the components are 2¹¹ = 2048 and 3⁴ = 81, as corrected in wave 23.
What RB2 still needs is the split-fiber classification at 3^e itself;
the exponent is settled.
