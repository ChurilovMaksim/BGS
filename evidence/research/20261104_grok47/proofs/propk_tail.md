# Prop. K with the proved span

The span input of N20 Prop. K is now Corollary D of `span_law.md`. This file recomputes the tail and the gas-versus-Robin crossover with that input. Status: **[P] as interval arithmetic, conditional on H1-shell and on the cited finite activity.** It does not prove H1-shell. It does not change the registered threshold 3307.

## 1. The tail, with the same hypotheses as N20

Fix ρ = 0.28, β = 2 log(1/ρ) / log λ, and q = 2^{(3/2)(1−β)}. Arb at 300 bits encloses

β = 1.4442975085259294 ± 10⁻⁸⁸, q = 0.6300567728342319 ± 10⁻⁸⁸,

in agreement with the N20 enclosure q = 0.630056772834 ± 2.4·10⁻¹³. H1-shell(C, J₀) means

S₂(j) = Σ_{bad, shell j} |r_A r_B|² ≤ C · 2^{j(1−β)} for every j > J₀.

The passage from S₂ to Σ |w| is the project’s ℓ³ ≤ ℓ² bound, cited as proved (Lean `l3_le_l2`, N13): per shell, Σ |w| ≤ S₂^{3/2}. With the factor 2 from the two sites,

T₀ = 2 Σ_{j>J₀} Σ_{bad} |w| e^{a ℓ} ≤ 2 C^{3/2} Σ_{j>J₀} e^{a ℓⱼ} qʲ,

and likewise for T₁ with an extra factor ℓⱼ, provided ℓ(γ) ≤ ℓⱼ on shell j. N20 took ℓⱼ = 2j + g₀ and factored e^{a g₀} (q e^{2a})ʲ. Corollary D allows

ℓⱼ = κ j + 3 + g₀,

hence e^{a ℓⱼ} ≤ exp(a(κ j + 3 + g₀)) and the base q e^{2a} may be replaced by q e^{a κ}, with prefactor exp(a(3+g₀)) in place of exp(a g₀). The inequality is non-strict because span < κ j + 3 implies span ≤ κ j + 3.

Throughout, J₀ = 12 and g₀ = 4, the values in the v5 statement of H1-shell.

The finite part is not recomputed from the operator rows. TRACE-321 records the unweighted activity 2 Σ |w| = 2.031569·10⁻⁶ for bad classes, j ≤ 12, g₀ = 4, core functional. This note uses the one-digit-larger majorant W₀ = 2.03157·10⁻⁶. For j ≤ 12, Corollary C gives span < κ·12 + 3 < 12.44, so span ≤ 12 and ℓ ≤ 16. The weighted finite part therefore satisfies

S₀^{fin}(a) ≤ W₀ e^{16.44 a}, S₁^{fin}(a) ≤ 16.44 S₀^{fin}(a),

where 16.44 is a convenient upper bound of κ·12 + 3 + 4 (the arb value is 16.4372…). Both the old tail and the sharp tail are added to this same finite majorant, so the comparison isolates the span input. The true finite part of N15 sits under this majorant. N16’s measured +2.4% true-functional correction on j ≤ 10 is outside the argument, as it was outside Prop. K.

KP is the project’s criterion: an a > 0 with S₀ + S₁/(1+g₀) ≤ a, where Sᵢ = Sᵢ^{fin} + Tᵢ. The activity that enters the gas exponent is S₀, identified with A_bad^{KP} exactly as in N20. The fixed-point loop here multiplies the upper endpoint by 1+10⁻⁹. N20’s `tail_kp.py` multiplies by 1.02 on each iteration, which is why the published a = 2.70·10⁻³ at C = 0.082 sits about two percent above a bare fixed point. The numbers below are bare fixed points of the majorant. They are not a re-issue of the published a.

Re Λ_lo′ = 6.234·10⁻⁴ and δ_true ≤ 5.0313·10⁻⁶ are inputs (TRACE-326 for the δ_true bound). Budget means Re Λ_lo′ − S₀ − δ_true.

## 2. Fixed points [P], arb, 300 bits

Source: `code/propk_sharp.py`, output `logs/propk_sharp.json`. Every printed figure is rounded outward from the arb endpoint.

| C | span input | a ≤ | S₀ ≤ | T₀ ≤ | budget ≥ |
| --- | --- | ---: | ---: | ---: | ---: |
| 0.082 | 2j+g₀ | 2.63843·10⁻³ | 3.43990·10⁻⁴ | 3.41868·10⁻⁴ | 2.74379·10⁻⁴ |
| 0.082 | κj+3+g₀ | 1.52670·10⁻³ | 3.24088·10⁻⁴ | 3.22004·10⁻⁴ | 2.94281·10⁻⁴ |
| 0.04 | 2j+g₀ | 8.51962·10⁻⁴ | 1.11780·10⁻⁴ | 1.09720·10⁻⁴ | 5.06588·10⁻⁴ |
| 0.04 | κj+3+g₀ | 5.16211·10⁻⁴ | 1.09716·10⁻⁴ | 1.07667·10⁻⁴ | 5.08652·10⁻⁴ |
| 8.8·10⁻⁴ | 2j+g₀ | 1.13859·10⁻⁵ | 2.38007·10⁻⁶ | 3.48113·10⁻⁷ | 6.15988·10⁻⁴ |
| 8.8·10⁻⁴ | κj+3+g₀ | 1.03520·10⁻⁵ | 2.37997·10⁻⁶ | 3.48048·10⁻⁷ | 6.15988·10⁻⁴ |
| 4.4·10⁻⁴ | 2j+g₀ | 9.65698·10⁻⁶ | 2.15497·10⁻⁶ | 1.23070·10⁻⁷ | 6.16213·10⁻⁴ |
| 4.4·10⁻⁴ | κj+3+g₀ | 9.29149·10⁻⁶ | 2.15494·10⁻⁶ | 1.23051·10⁻⁷ | 6.16213·10⁻⁴ |

Reading the C = 0.082 row. The KP threshold a falls by about forty percent, because T₁ carries the length and κ j + 3 is a little under forty percent of 2j on the first tail shells. The gas sees S₀, which does not carry a free factor of ℓ. At this C the tail dominates S₀, and S₀ falls only from 3.440·10⁻⁴ to 3.241·10⁻⁴, a relative drop of about six percent. At C = 8.8·10⁻⁴ the finite part dominates, the tail is a few parts in 10⁷, and S₀ is unchanged in the first four significant figures.

At the published a = 2.6925·10⁻³, held fixed so that only the tail formula changes, the ratio of the sharp T₀ to the 2j-tail T₀ is at most 0.96077 for C = 0.082 (`at_published_a` in the same log). The six-percent figure is the span effect itself. The further movement of the fixed point comes from feeding the smaller length back into a.

## 3. Crossover [P] for a stated δ, matching the v5 implementation

`code/crossover_sharp.py` is an independent mpmath (80 digits) transcription of the arithmetic in `computations/verification/lineN_theorem_draft/V5/code/crossover_v5.py`.

- h₁-slot = 7, then h ← 6h − h_prev, run (p−1)/2 − 1 times. This is the NSW sequence: h(3) = 7, h(5) = 41, h(7) = 239. K_p = 4h_p² + 3.
- Robin, in the form the project uses: σ(n)/n < e^γ log log n + 0.6483 / log log n for n ≥ 3, applied as an upper bound for σ(K_p)/K_p − 1 with L = log K_p. This note did not reopen Robin’s paper. Agreement with the registered primes checks the transcription, not the citation.
- G(p) = (2b^p − 1)² − 1 with log b = log(1+R) − δ and R = 6.234·10⁻⁴.
- A prime is recorded when G(p) > robin(log K_p). The real threshold uses the envelope log K_p ≤ (2p+1) log ε, proved in Lemma 10. Monotonicity: at the first integer p₀ where G exceeds the envelope, the derivatives satisfy G′ > (envelope)′. For larger p the inequality persists. G′(p) = 4 b^p (2 b^p − 1) log b is increasing once log b > 0, and every δ in the table satisfies log b = log(1+R) − δ > 2.7·10⁻⁴. The envelope derivative decreases for p ≥ 3: with L = (2p+1) log ε and c = 0.6483, d(robin)/dL = e^γ/L − c/(L (log L)²), and this is decreasing in L as soon as e^γ > c (1 + 2/log L)/(log L)². At p = 3 one has K_3 = 199 and L = log 199 > 5, where the right-hand side is below 0.6 and e^γ > 1.7; larger L only improves the inequality.

**Lemma 10 [P].** For every prime p ≥ 3, log K_p < (2p+1) log ε.

Let u₀ = 1, u₁ = 7, u_{n+1} = 6u_n − u_{n−1}. The characteristic root is λ, and

u_n = (ε/2) λ^n + (ε̄/2) λ^{−n}.

The second coefficient is negative, so u_n < (ε/2) λ^n. The index in the recurrence is n = (p−1)/2, and h_p = u_n. Therefore 4h_p² < ε² λ^{p−1} = λ^p, and K_p < λ^p + 3. For p ≥ 1 one has λ^p + 3 ≤ λ^{p+1/2}, because √λ − 1 = √2 > 3/λ^p. Hence log K_p < (p + 1/2) log λ = (2p+1) log ε.

The program was checked against the three registered inputs before any new δ was used:

| δ | first integer past the envelope | first prime | primes in [p₁, 5000] that fail |
| --- | ---: | ---: | --- |
| 3.4962·10⁻⁴ (registered v5 input at C ≤ 0.082) | 3305 | 3307 | none |
| 5.0313·10⁻⁶ (δ_true alone) | 1397 | 1399 | none |
| 7.4115·10⁻⁶ (registered robust input) | 1402 | 1409 | none |

## 4. What the sharp span does to the conditional prime

δ_eff ≤ S₀ + δ_true, with S₀ the upper endpoint from §2. The prime for that upper bound is a sufficient prime: a smaller true activity only makes G larger.

| hypothesis on C | span input | δ_eff ≤ | sufficient prime |
| --- | --- | ---: | ---: |
| 0.082 | 2j+g₀, this majorant | 3.490213·10⁻⁴ | 3299 |
| 0.082 | κj+3+g₀ | 3.2911833·10⁻⁴ | 3067 |
| 0.04 | 2j+g₀, this majorant | 1.16811·10⁻⁴ | 1733 |
| 0.04 | κj+3+g₀ | 1.14748·10⁻⁴ | 1721 |
| 8.8·10⁻⁴ | either | 7.4115·10⁻⁶ | 1409 |
| 4.4·10⁻⁴ | either | 7.1863·10⁻⁶ | 1409 |

Log: `logs/crossover_sharp.json`. Each row has `mono_ok` true and an empty violation list through 5000.

The registered prime 3307 is the prime for δ = 3.4962·10⁻⁴. This program returns 3307 on that input. The eight-prime gap from 3307 down to 3299 is the gap between the published δ and this note’s 2j-majorant (no 1.02 inflation, finite part replaced by W₀ e^{aℓ}). It is not a correction of the register.

The span theorem, inside the same majorant, moves the C = 0.082 row from 3299 to 3067. That is the effect of replacing 2j+g₀ by κj+3+g₀. It is available only if H1-shell holds at C ≤ 0.082, together with the rest of the v5 hypotheses (H0, H5–H8, B_p ≥ κ for infinitely many p, and the additive budgets that v5 still treats as idealised). At the robust size C = 8.8·10⁻⁴ the same substitution leaves the prime at 1409.

Holding a fixed at the published 2.6925·10⁻³ and inserting only the sharp tail produces δ_eff ≤ 3.36206·10⁻⁴ and prime 3163. The KP-consistent figure is 3067, because a is solved simultaneously with the tail.

## 5. Status line

[P] Theorem A and Corollaries B–D, including the identification Lemma 8.

[P] The arithmetic of §§2–4, conditional on H1-shell(C, 12) for the stated C, on TRACE-321’s unweighted finite activity, on δ_true ≤ 5.0313·10⁻⁶, and on Re Λ_lo′ = 6.234·10⁻⁴.

[P-sketch], unchanged from N20: background interplay of polymers, and the per-site normalisation that identifies the gas weight with S₀.

[H], unchanged: H1-bad for j > 14, H1-ali, H5–H8, and R′.
