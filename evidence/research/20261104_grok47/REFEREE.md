# Self-referee

Read against `proofs/span_law.md` and `proofs/propk_tail.md`. Each item is a place the argument can fail, followed by the check that was actually made.

## 1. Overstatement of the logical status

The failure mode is to read Theorem A as a discharge of H1 or H3, or to read the prime 3067 as a new p₁.

Theorem A is a statement about the length of a digit word. H1-shell is a statement about Σ |r_A r_B|². The tail arithmetic multiplies those two statements; it does not produce the second from the first. `FRONTIER.md` states the remaining hypotheses in the same list as the new prime. The registry was not edited, and 3307 is reproduced on the published input δ = 3.4962·10⁻⁴.

TRACE-332 stays conditional after this note. Two of its three sketches, background interplay and polymer normalisation, are not touched. Only the span sketch is replaced, and only inside this directory.

## 2. The odd-site boundary

`eps_digits` stores τ_{2t−1} = −red(−θ_{2t−1}). The identity −red(−x) = red(x) fails when red(x) = −1/2, where the left side equals +1/2. A missed odd half-integer would shift the project digit by the coboundary δ_k − 2δ_{k−1} − δ_{k−2} and could change the span by O(1).

Lemma 8 says a fundamental-domain representative has no half-integer θ_k at an odd index, because α ε^k = B√2 would push the ratio σ₊/|σ₋| outside [1, λ). The even sites store red(θ) directly, including the value −1/2. The exceptional magnitude |θ| = 1/2 occurs only for the class of √2 (Lemma 2), which was computed by hand: the word is [1, −1], span 2.

Check. Every fundamental-domain class with |N| < 2¹⁵, 20434 classes, matches `eps_digits` after rounding, including every class that does hit a half-integer at an even index (3√2, 5√2, 7√2 among them). A systematic off-by-one would have appeared. Shells 12–14 were compared separately (`logs/word_match_j12_14.json`, 17880/17880) because the first audit stopped the float comparison at j ≤ 11.

Residual risk. The lemma is only as strong as the ratio computation under ε^{−k}. A referee who rejects Lemma 8 still has the exhaustive match through shell 14, which covers every shell that has been certified for the finite part and two shells past J₀. The tail shells j > 14 rely on the lemma.

## 3. Constants 1 and 3 versus the measured 2.77

N20 recorded max(span − 0.787 j) = 2.77 for j ≤ 14. Theorem A controls span − L, and L can be smaller than κ j by almost 1 when |N| is just above 2ʲ. The witness α = 116 has span − κ·13 ≈ 2.776 and span − L ≈ 2.99966. Both numbers are right, and they are different quantities. Quoting 2.77 as a defect against L would be a false sharpness claim; the note uses the arb enclosure of span − L.

The note does not claim that the defect is dense in (1, 3). Density was not proved. The witnesses only forbid a uniform improvement of either constant by 10⁻³.

## 4. Bad classes versus all classes

The near-3 witness α = 116 has an internal zero run of 9, so it is charged to the gas of several polymers, not to one bad cluster at g₀ = 4. Using it as evidence that the H1 tail needs the constant 3 would be an overstatement.

The bad witness is α = 118, run 3, defect 2.96087. The tail uses span < κ j + 3 for every class, which includes the bad ones, and 2.96087 shows that a bad-class constant below 2.96 already fails by shell 13. The constant 3 is not saturated by a bad class inside |N| < 2¹⁵. A later bad class could sit closer. The proof does not need it to: the inequality used in the tail is the one that holds for every class.

The count 17255 in `bad_defect.json` includes model classes. The extremal witnesses 118 and 14√2 are not among the five model types.

## 5. Finite-part majorant

`tail_kp.py` reads certified rows from `/workspace/bgs-lineN`, which is not in this checkout. The finite part was therefore not replayed term by term. The note uses W₀ = 2.03157·10⁻⁶, one unit in the last place above the registered 2.031569·10⁻⁶, times e^{aℓ} with ℓ ≤ 16.44. That is an upper bound only if TRACE-321’s figure is the unweighted 2Σ|w| and every bad j ≤ 12 cluster has ℓ ≤ 16.44. The first is how N20 states the figure. The second is Corollary C plus integrality (span ≤ 12 on shell 12, and the audit’s maximum span on shell 12 is 12).

At C = 0.082 the finite piece is about 2·10⁻⁶ against a tail of 3.2·10⁻⁴. An error of a factor two in the finite piece moves S₀ by less than one percent. lineN22’s sensitivity is about fifty primes per percent of S₀ near 3307, so this majorant is coarser than the span effect (3299 against 3067) and finer than the gap one would care about if H1 were the only remaining hypothesis. It is not a recomputation of `a_cert3`.

The core-functional restriction is inherited. N16 measured a +2.4% true-functional correction on j ≤ 10. Applying the sharp span to the true functional was not done.

## 6. The 2j column is not a bit-replay of `tail_kp_v2.json`

N20’s solver sets a ← 1.02·(KP left-hand side) each iteration, so the published a = 2.70·10⁻³ is an inflated fixed point. This note’s 2j column is the bare fixed point of a majorant, a ≤ 2.63843·10⁻³, S₀ ≤ 3.43990·10⁻⁴. The published activity at C = 0.082 is ≤ 3.4457·10⁻⁴. The relative gap is about 0.2%. The crossover program, on the published δ = 3.4962·10⁻⁴, returns 3307. On this note’s 2j-majorant δ it returns 3299. Those two facts are both in `logs/crossover_sharp.json`. Treating 3299 as a correction of 3307 would be a misreading of the inflation.

## 7. Robin’s constant

The bound σ(n)/n < e^γ log log n + 0.6483/log log n is used as `crossover_v5.py` uses it. Robin 1984 was not re-opened. A wrong constant would move every prime in the table, including the sanity check 3307, by the same transcription. It would not by itself invent the gap between 3299 and 3067, which is a gap between two δ’s fed to one function.

Lemma 10, the envelope log K_p < (2p+1) log ε, is proved from the closed form of the NSW recurrence and does not depend on Robin. The prime test itself uses log K_p, not the envelope. The envelope is used for the real threshold and for the derivative comparison that extends the inequality past 5000.

## 8. Monotonicity past the first prime

G′(p) = 4x(2x−1) log b with x = b^p. For every δ in the table, log b = log(1+R) − δ > 2.7·10⁻⁴ (the tight case is the published δ = 3.4962·10⁻⁴; R − δ itself is 2.74·10⁻⁴, and the earlier draft of this sentence said 3·10⁻⁴, which is false). So G′ is positive and increasing. The p-derivative of the Robin envelope decreases for p ≥ 3, by the comparison recorded in `proofs/propk_tail.md` §3. Checking G′ > (envelope)′ at the first integer therefore persists. The program records that comparison and records that no prime from the first prime through 5000 fails against the exact log K_p. A zero of log b would kill the argument; it does not occur for these δ.

## 9. κ against λ

The rate κ = log 2 / log ε is the shell-to-span conversion because |N| doubles once per shell and the digit step is ε, not λ. Using log 2 / log λ would halve the length, cut the tail base illegally, and move 3067 by an amount the theorem does not justify. The note states the base explicitly. The arb ball is in `logs/propk_sharp.json`.

## 10. Enumeration completeness

A dropped class would fake the sharpness search and the word match. The shell counts 1, 1, 3, 4, 11, 20, 42, 78, 161, 316, 643, 1274, 2555, 5100, 10225 agree with N20 through j = 14. The fundamental-domain predicate is exact integer arithmetic (sign of p + q√2 by comparing squares). Theorem A itself does not use the enumeration; it is a statement about every α ≠ 0. The enumeration is the witness search and the comparison with `eps_digits`.

## 11. What was not run

`tail_kp.py`, `a_cert3`, and the Lean files were not re-executed. Paths under `/workspace/bgs-lineN` are absent. No claim is made that a Lean checker accepted Theorem A. The integer and arb scripts that were executed are listed in `RUN.md`.
