# Prop. K with the proved span

Status: the length input is **[P]** (span theorem). The tail sums are **[CA]**. The crossover is **[P-arith]** in the sense of the v5 script: IEEE floats for the gas, exact integers for K_p, and a monotonicity comparison. Everything in the table is conditional on H1-shell. Background renormalisation stays **[P-sketch]**. H1 and H3 stay open.

## 1. The tail with a sharp length

Assume H1-shell(C, J_0, ρ) at ρ = 0.28 and J_0 = 12: for every j > 12,

S_2(j) ≤ C · 2^{j(1 − β)}, β = 2 ln(1/ρ) / ln λ.

The identity (Σ x_i^3)^2 ≤ (Σ x_i^2)^3 for x_i ≥ 0 (BGS, `formalization/Bgs/LineN13Arith.lean`, `l3_le_l2`) gives Σ |w| ≤ S_2(j)^{3/2} on each shell. Hence

Σ_{bad, shell j} |w| ≤ C^{3/2} q^j, q = 2^{(3/2)(1−β)}.

Ball arithmetic at precision 200 gives

β ∈ [1.4442975085259294268 ± 4.1×10^{-20}], q ∈ [0.63005677283423193771 ± 2.8×10^{-21}].

The span theorem supplies ℓ(γ) = span(γ) + g_0 ≤ θ j + 3 + g_0 with θ = log_ε 2 < 4/5 and g_0 = 4. Therefore

Σ |w| e^{a ℓ} ≤ C^{3/2} e^{a(g_0+3)} (q e^{a θ})^j.

The per-site tail used by Prop. K carries the same factor 2 as N20 `tail_kp.py` (the class modulo ±ε^ℤ). With r = q e^{a θ} < 1 and J = 13,

T_0 ≤ 2 C^{3/2} e^{a(g_0+3)} Σ_{j≥J} r^j,

T_1 ≤ 2 C^{3/2} e^{a(g_0+3)} Σ_{j≥J} (θ j + 3 + g_0) r^j.

The slope θ = 2 and the additive 0 recover the N20 majorant ℓ ≤ 2j + g_0. Both series are closed forms and are evaluated in balls.

The finite part j ≤ 12 is the certified list `a_cert3.jsonl`: 4460 bad classes at g_0 = 4 outside the four model classes {(1,0), (0,1), (2,0), (0,2)}. Their spans are the N14 spans, which the exact census matched on all 5109 classes. The sum of the positive terms is inflated by 10^{-9}, the N20 model for a float accumulation of this length. That inflation is part of the upper bound below.

## 2. Fixed points

The Kotecký–Preiss inequality used here is S_0 + S_1/(1+g_0) ≤ a, with S = S^{fin} + T. The weight a is increased until the ball for the left-hand side lies strictly below a. This is a sufficient condition. It is slightly tighter than the published N20 iteration, which multiplies the needed value by 1.02 at every step and therefore stops above the fixed point. Both are valid upper bounds on a working weight. They are not claimed to be the minimal weight.

At J_0 = 12, g_0 = 4:

| Majorant | C | a ≤ | S_0 ≤ | budget left ≥ | δ_eff ≤ | first prime |
|---|---|---|---|---|---|---|
| slope 2, add 0 (same solver) | 0.082 | 2.6375×10^{-3} | 3.4394×10^{-4} | 2.7443×10^{-4} | 3.4897×10^{-4} | 3299 |
| slope 2, N20 published point | 0.082 | 2.6925×10^{-3} | 3.4457×10^{-4} | 2.738×10^{-4} | 3.4962×10^{-4} | **3307** |
| θ = log_ε 2, add 3 | 0.082 | 1.5248×10^{-3} | 3.2405×10^{-4} | 2.9431×10^{-4} | 3.2909×10^{-4} | **3067** |
| slope 4/5, add 3 | 0.082 | 1.5385×10^{-3} | 3.2424×10^{-4} | 2.9413×10^{-4} | 3.2927×10^{-4} | **3067** |
| θ, add 3 | 8.8×10^{-4} | 7.062×10^{-6} | 2.3798×10^{-6} | 6.1599×10^{-4} | 7.4111×10^{-6} | **1409** |
| θ, add 3 | 4.4×10^{-4} | 6.001×10^{-6} | 2.1548×10^{-6} | 6.1621×10^{-4} | 7.1861×10^{-6} | (same regime as 1409) |

Budget left is Re Λ_lo′ − S_0 − δ_true with Re Λ_lo′ = 6.234×10^{-4} and δ_true ≤ 5.0313×10^{-6}. Every KP comparison in the run returned true inside the ball. The rational slope 4/5, which is proved by 225 < 288 and does not need a decimal for θ, gives the same prime as θ.

The regression of the crossover script on the published inputs returned 3307 at δ_eff = 3.4962×10^{-4} and 1409 at 7.4115×10^{-6}, with no violations among primes up to 5000. That is the check that the prime column speaks the same convention as BGS-TRACE-333.

## 3. How to read 3067

The drop from 3299 to 3067 is the span sharpening at fixed solver. The further step from 3299 to the published 3307 is the 1.02 inflation of the weight, which raises S_0 in the fourth digit. Quoting 3067 against 3307 without that split overstates the gain by eight primes.

3067 is fragile in the same way 3307 is. Scaling the sharp S_0 and rebuilding δ_eff gives:

| factor on S_0 | first prime |
|---|---|
| 0.99 | 3037 |
| 1 | 3067 |
| 1.01 | 3109 |
| 1.03 | 3181 |
| 1.10 | 3463 |

A one-percent uncertainty in the background normalisation, which is still a sketch, moves the threshold by about forty primes. The strengthened hypothesis C ≤ 8.8×10^{-4} stays at 1409. The length computation does not make the large-C threshold robust, and it does not move the small-C threshold.

The additive budgets (tails of X, the Y sum, cross lines, ε, and n/h_p) are still idealised at zero, exactly as in BGS-TRACE-333. 3067 is a conditional arithmetic statement inside that idealisation.

## 4. What remains before H3 is a theorem

H3, in the form Prop. K actually uses, still needs:

1. H1-shell at some C for which the row above closes. The finite shells do not provide it (Prop. F; Thm A’s margin is a margin on j ≤ 14).
2. The background step: S_0 has to be computed on the activities renormalised by the model partition function. The numerical rows use the bare certified |w|.
3. The log-to-modulus sentence in v5 §2, which is the same sketch: |ln Ξ_bad| ≤ p S_0(a) with no sign on the bad clusters.

Item 1 is the analytic gate. Items 2 and 3 are the reason a closed H1-shell would still leave a [P-sketch] in the exponent of B_p until they are written out. The span is no longer on that list.
