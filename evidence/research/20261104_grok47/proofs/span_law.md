# The balanced ε-span of a class in ℤ[√2]

Status of the theorem below: **[P]**. Finite sharpness witnesses: **[P]** (exact integer digits, arb enclosures). Exhaustive comparison with `digits.eps_digits` through shell 14: **[P]** as a finite check of that comparison. Nothing in this file discharges H1, H3, or R′.

Notation is the project’s. ε = 1+√2, ε̄ = 1−√2 = −ε⁻¹, λ = ε² = 3+2√2, N(ε) = −1. For α = a + b√2 ∈ ℤ[√2], N(α) = a² − 2b² = σ₊(α)σ₋(α). The class of α is its orbit under α ↦ ±εᵏα. The fundamental domain used for enumeration is σ₊(α) > 0 and 1 ≤ σ₊(α)/|σ₋(α)| < λ.

## 1. Digits

Let μ = (√2/4) α and θₖ = σ₊(μ) εᵏ. The conjugate embedding is θ̄ₖ = σ₋(μ) ε̄ᵏ. Then θₖ + θ̄ₖ = Tₖ ∈ ℤ. Explicitly, if α εᵏ = A + B√2, then θₖ = B/2 + (A/4)√2 and Tₖ = B, and

|θₖ θ̄ₖ| = |N(α)|/8.

The sequence θₖ obeys the recurrence of ε, namely θₖ = 2θₖ₋₁ + θₖ₋₂, and Tₖ obeys the same recurrence. |θₖ| is strictly increasing by the factor ε (θₖ = 0 would force α = 0), and |θ̄ₖ| is strictly decreasing by the factor ε.

Write nₖ = ⌊θₖ + 1/2⌋ and τₖ = θₖ − nₖ, so τₖ ∈ [−1/2, 1/2). The digit is the integer

Eₖ = nₖ − 2nₖ₋₁ − nₖ₋₂ = 2τₖ₋₁ + τₖ₋₂ − τₖ.

This is the project’s letter. In `computations/verification/lineN14/code/digits.py`, `eps_word` sets Eₖ = −(τₖ − 2τₖ₋₁ − τₖ₋₂) on the interleaved ε-chain. Section 4 identifies that chain with red(θₖ).

**Lemma 1 [P].** Eₖ ∈ {−1, 0, 1}.

Each τ lies in [−1/2, 1/2), so 2τₖ₋₁ ∈ [−1, 1), τₖ₋₂ ∈ [−1/2, 1/2), and −τₖ ∈ (−1/2, 1/2]. The sum is strictly greater than −2 and strictly less than 2, so the only possible integers are −1, 0, 1. (N14 recorded the coarser bound |Eₖ| ≤ 2 as a sketch. The half-open interval upgrades it.)

**Lemma 2 [P].** θₖ ∈ ℤ + 1/2 if and only if A = 0 and B is odd, hence |θₖ| = 1/2 if and only if α εᵏ = ±√2.

If A ≠ 0 then (A/4)√2 is irrational, so θₖ is irrational. If A = 0 then θₖ = B/2, a half-integer precisely when B is odd, and equal to ±1/2 precisely when B = ±1.

Thus there is a single class on which |θₖ| or |θ̄ₖ| ever equals 1/2: the class of √2, with |N| = 2. Call it the exceptional class.

## 2. Support

Let Kₗ = min{k : |θₖ| ≥ 1/2} and Kᵣ = max{k : |θ̄ₖ| ≥ 1/2}. Both exist: |θₖ| → ∞ as k → +∞ and |θₖ| → 0 as k → −∞, and |θ̄ₖ| = |N|/(8|θₖ|).

**Lemma 3 [P].** nₖ = 0 for every k < Kₗ. For every k > Kᵣ one has |θ̄ₖ| < 1/2, hence θₖ ∈ (Tₖ − 1/2, Tₖ + 1/2) and nₖ = Tₖ. Consequently Eₖ = 0 for k < Kₗ and for k > Kᵣ + 2.

For k < Kₗ, |θₖ| < 1/2, so θₖ ∈ (−1/2, 1/2) and ⌊θₖ + 1/2⌋ = 0. For k > Kᵣ the conjugate is strictly inside (−1/2, 1/2) of the integer Tₖ, so the balanced floor is Tₖ. The recurrence Tₖ = 2Tₖ₋₁ + Tₖ₋₂ then kills Eₖ once three consecutive n’s equal the corresponding T’s.

**Lemma 4 [P].** On every non-exceptional class, E_{Kₗ} ≠ 0 and E_{Kᵣ+2} ≠ 0. Therefore the nonzero digits are exactly the interval [Kₗ, Kᵣ+2], and

span(α) := (last nonzero index) − (first nonzero index) + 1 = Kᵣ − Kₗ + 3.

Left end. |θ_{Kₗ−1}| < 1/2, so |θ_{Kₗ}| < ε/2. Combined with |θ_{Kₗ}| ≥ 1/2 and the exclusion of equality 1/2,

θ_{Kₗ} ∈ (1/2, ε/2) or θ_{Kₗ} ∈ (−ε/2, −1/2).

In the first subinterval, θ+1/2 ∈ (1, (1+ε)/2) and (1+ε)/2 = 1 + √2/2 < 2, so n_{Kₗ} = 1. In the second, θ+1/2 ∈ (−√2/2, 0), so n_{Kₗ} = −1. The two preceding n’s vanish, hence E_{Kₗ} = n_{Kₗ} ∈ {±1}.

Right end. The same stretching gives 1/2 < |θ̄_{Kᵣ}| < ε/2. Set Δ’s integer T = T_{Kᵣ} and θ = θ_{Kᵣ}. Then θ lies in (T+1/2, T+ε/2) or in (T−ε/2, T−1/2). In the first, θ+1/2 ∈ (T+1, T+(1+ε)/2) ⊂ (T+1, T+2), so n = T+1. In the second, θ+1/2 ∈ (T−√2/2, T), so n = T−1. For the indices k > Kᵣ one has nₖ = Tₖ, and T_{Kᵣ+2} = 2T_{Kᵣ+1} + T_{Kᵣ}, therefore

E_{Kᵣ+2} = T_{Kᵣ+2} − 2T_{Kᵣ+1} − n_{Kᵣ} = T_{Kᵣ} − n_{Kᵣ} ∈ {±1}.

The two endpoints may coincide (Δ = Kᵣ − Kₗ = −2, span 1). They are then two expressions for one and the same nonzero digit.

**Lemma 5 [P], exceptional class.** For α = √2 one has μ = 1/2, θₖ = εᵏ/2, Kₗ = Kᵣ = 0, and the word is [1, −1]. Thus span = 2, while Kᵣ − Kₗ + 3 = 3.

Compute the balanced floors. θ₀ = 1/2, n₀ = 1. θ₁ = (1+√2)/2, n₁ = 1. θ₂ = (3+2√2)/2, n₂ = 3. θ₋₁ = (−1+√2)/2 ∈ (0, 1/2), n₋₁ = 0, and nₖ = 0 for k ≤ −1. Hence E₀ = 1, E₁ = 1 − 2·1 = −1, E₂ = 3 − 2·1 − 1 = 0. For k ≥ 2 the value nₖ equals the trace Tₖ (at k = 2, √2·ε² = 4+3√2), so Eₖ = 0 for k ≥ 2. The right-hand endpoint of Lemma 4 is exactly the site that vanishes.

The class of −√2 is the same orbit. Multiplying by ε shifts the index and does not change the length of the word.

## 3. The span law

Let L(α) = log(|N(α)|/2) / log ε and Δ = Kᵣ − Kₗ.

**Lemma 6 [P].** Δ ≤ L(α), with equality if and only if α is exceptional. Always Δ > L(α) − 2.

At the two thresholds |θ_{Kₗ}| ≥ 1/2 and |θ̄_{Kᵣ}| ≥ 1/2. Since |θ̄_{Kᵣ}| = |θ̄_{Kₗ}| ε^{−Δ} and |θ_{Kₗ} θ̄_{Kₗ}| = |N|/8,

|θ_{Kₗ}| |θ̄_{Kᵣ}| = |N| / (8 ε^Δ) ≥ 1/4,

so ε^Δ ≤ |N|/2 and Δ ≤ L. Equality forces both magnitudes to equal 1/2, which is Lemma 2. In the other direction |θ_{Kₗ}| < ε/2 and |θ̄_{Kᵣ}| < ε/2 hold for every class, because each threshold is the first (respectively last) hit and the previous (next) magnitude is strictly below 1/2. Therefore |N|/(8 ε^Δ) < ε²/4, so Δ > L − 2.

**Theorem A [P].** For every α ∈ ℤ[√2] \ {0},

L(α) + 1 < span(α) < L(α) + 3.

The length depends only on the class of α modulo ±ε^ℤ.

On a non-exceptional class, span = Δ + 3. Lemma 6 gives Δ + 3 < L + 3 and Δ + 3 > L + 1. On the exceptional class, L(√2) = log 1 / log ε = 0 and span = 2, so the same strict inequalities hold. Invariance: ε-multiplication shifts Kₗ and Kᵣ by the same integer, and changing the sign of α does not change |θ| or |θ̄|. For a non-exceptional class the length is Δ+3. For the exceptional class the length was computed on one representative.

**Corollary B [P].** The defect span(α) − L(α) lies in the open interval (1, 3). In particular no uniform improvement of either constant is available: the constants 1 and 3 are the best constants that hold for every α.

The open interval is Theorem A. Sharpness of the constants is stronger than the inequalities and is the content of the witnesses in §5: any claimed uniform replacement of 3 by 3−η, or of 1 by 1+η, with η = 10⁻³, already fails for an explicit α with |N| < 2¹⁵.

**Corollary C [P], shell form.** If 2ʲ ≤ |N(α)| < 2ʲ⁺¹, then

span(α) < κ j + 3, κ = log 2 / log ε.

Indeed |N|/2 < 2ʲ, so L < κ j, and Theorem A supplies span < L+3. The constant κ is log 2 / log ε, the same constant the project writes ln 2 / ln ε. It is not log 2 / log λ; that quantity is κ/2.

For the tail this is the input that replaces the sketch span ≤ 0.787 j + O(1) ≤ 2j. Numerically, an arb ball at 300 bits gives

κ ∈ [0.78643970135739488, 0.78643970135739489]

(radius below 10⁻⁸⁸; `logs/propk_sharp.json`).

## 4. Identification with the project word

The span in Prop. K is the length of the word returned by `eps_digits`. This section shows that, on a fundamental-domain representative, that word is the digit word of §1.

`seeds(2a, 2b)` builds the A-embedding b/2 + (a/4)√2, which is θ₀, and the B-embedding

(b−a)/2 + (a−2b)√2/4.

**Lemma 7 [P].** The B-embedding equals −θ₋₁.

θ₀ ε⁻¹ = (b/2 + a√2/4)(−1+√2) = (a−b)/2 + (2b−a)√2/4, and the negative of this is the displayed element.

The project’s even sites are red(θ_{2t}): `core_t` evaluates red(e₁ λᵗ) for t ≤ 0 and red(−e₂ λ⁻ᵗ) for t > 0, and red(θ) = red(−θ̄) because θ+θ̄ ∈ ℤ and red is 1-periodic. The odd sites are τ_{2t−1} = −red(−θ_{2t−1}), by Lemma 7 and the same conjugate reduction.

**Lemma 8 [P].** For a fundamental-domain representative, θₖ is never a half-integer at an odd index. Consequently τ^projₖ = red(θₖ) at every k, and the project digit equals Eₖ.

A half-integer θₖ forces A = 0 and B odd (Lemma 2), so α εᵏ = B√2. The positive representative |B|√2 has ratio σ₊/|σ₋| = 1. Multiplying by ε⁻ᵏ multiplies this ratio by λ⁻ᵏ, because σ₊ scales by ε⁻ᵏ and |σ₋| scales by |ε̄|⁻ᵏ = εᵏ. If k ≥ 1 is odd the ratio is at most λ⁻¹ < 1. If k ≤ −1 is odd the ratio is at least λ. Either case leaves the fundamental domain. So a half-integer inside the domain occurs only at an even index, where the project stores red(θₖ) itself. At odd indices −red(−θ) = red(θ), because the boundary red(θ) = −1/2 does not occur. The integer letters therefore agree, and so do their spans.

(The boundary identity −red(−x) = red(x) fails exactly when red(x) = −1/2, where the left side equals +1/2. Lemma 8 is what keeps that case off the odd sites. On even sites the project stores red(θ) = −1/2 directly, which is the representative used in §1.)

**Finite check [P] of the comparison, not a substitute for Lemmas 7–8.** Every fundamental-domain class with |N| < 2¹⁵ was compared.

- Shells j ≤ 11: 2554 classes, `mp.dps = 80`, `KK = 8`, `tol = 1e-8`, 2554 matches, 0 mismatches (`logs/span_audit.json`).
- Shells j ∈ {12, 13, 14}: 17880 classes, `mp.dps = 60`, `KK = 12`, `tol = 1e-7`, 17880 matches, 0 mismatches (`logs/word_match_j12_14.json`).

Shell cardinalities in the same enumeration are 1, 1, 3, 4, 11, 20, 42, 78, 161, 316, 643, 1274, 2555, 5100, 10225 for j = 0,…,14. These are the cardinalities recorded for Thm A in N20. The model words on the fundamental-domain representatives are odd = [1], √2 = [1, −1], two = [1, 0, −1], 2√2 = [1, 0, 1], four = [1, −1, 0, 1, 1], matching N14 §1.2.

On this range the audit also records 0 support violations and 0 slack anomalies: span = Kᵣ − Kₗ + 3 except for |N| = 2, where the slack is 1. That is a check of Lemmas 4 and 5 on a complete set of classes, not the proof.

## 5. Sharpness witnesses [P]

The defect is enclosed in arb at 200 bits as span − log(|N|/2)/log ε. Both spans were recomputed by the integer digit of §1.

| α | N | shell | word | internal zero run | defect enclosure |
| --- | ---: | ---: | --- | ---: | --- |
| 116 | 13456 | 13 | [1,−1,0⁹,1,1] | 9 | 2.99966264991176 ± 10⁻⁵⁹ |
| 82√2 | 13448 | 13 | [1,1,0⁷,−1,1] | 7 | 1.00033740024810 ± 10⁻⁵⁹ |
| 118 | 13924 | 13 | [1,−1,0³,1,0,−1,0³,1,1] | 3 | 2.96087221277804 ± 10⁻⁵⁹ |

The first two show that the constants in Theorem A are saturated to within 4·10⁻⁴ already for |N| < 2¹⁵. The class 116 is not a single g₀ = 4 polymer: its internal run is 9. The class 118 has internal run 3, so it is bad at g₀ = 4, and its defect is already above 2.960. Among all fundamental-domain classes with |N| < 2¹⁵ whose internal zero run is < 4 (17255 classes, models included; both extremal witnesses below are non-model), the defect enclosures run from above 1.01148986427082 to below 2.96087221277805 (`logs/bad_defect.json`).

So a uniform bound span ≤ L + 2.96 already fails on a bad class of shell 13. The constant 3 in Corollary C is the constant the tail may use, and it is within 0.04 of the defect of an explicit bad class. This note does not claim that the image of the defect is dense in (1, 3).

## 6. What Prop. K may now quote

N20 Prop. K used ℓ(γ) = span + g₀ ≤ 2j + g₀ for j ≥ 5, labelled [P-sketch], with the measured remark that bad classes through shell 14 satisfy span/j ≤ 1.2 and max(span − 0.787 j) = 2.77. Corollary C replaces the sketch.

**Corollary D [P].** For every class in shell j, and every g₀ ≥ 0,

span + g₀ < κ j + 3 + g₀.

In particular the inequality is valid for the bad classes that enter H1-shell (internal ε-zero-run < g₀, non-model). For j ≥ 3 one has κ j + 3 ≤ 2j, so the old majorant 2j + g₀ remains true and is now a theorem rather than a sketch; the tail arithmetic in `proofs/propk_tail.md` uses the sharp majorant.

The coefficient 0.787 in the N20 sketch is this κ, not an experimental fit. Their measured max(span − 0.787 j) = 2.77 on j ≤ 14 is the quantity span − κ j for a class whose L is slightly below κ j. The defect against L, which is the quantity Theorem A controls, reaches 2.9997 on the same range. Both are consistent.

Background interplay and polymer normalisation are untouched. They were [P-sketch] in N20 and they stay [P-sketch].

## 7. Certificate layer for the finite witnesses

The theorem does not depend on floating point. The witnesses do depend on an implementation of ⌊p + q√2⌋. That implementation is `floor_lin` in `code/span_audit.py`, and it is the following fact.

**Lemma 9 [P].** Let s = ⌊√(2q²)⌋ for an integer q ≥ 0, computed as an integer square root. Then s ≤ q√2 < s+1, and equality s = q√2 holds only for q = 0. Hence ⌊p + q√2⌋ = p + s for q ≥ 0, and ⌊p + q√2⌋ = p − s − 1 for q < 0.

Irrationality of √2 gives the strict inequality for q ≠ 0. Python’s `math.isqrt` is the integer square root, and the integers arising for |N| < 2¹⁵ are exact Python integers.

The comparison |θ| ? 1/2 is the sign of (4B² + 2A² − 4) + (4AB)√2, decided by comparing squares when the rational and irrational parts have opposite signs. A zero of that form with the irrational part nonzero would make √2 rational. The audit finds no unexpected zeros: the only slack-1 class through shell 14 is |N| = 2.
