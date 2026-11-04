# Frontier, 4 November 2026

## Third target: H7* rates on the included levels

The span law and the H7*/H8 obstruction below are kept as records. The third target is the per-step sector rate on the included \(K_p\)-divisors other than \(7\), against \(T' = 1.42785\). The proof note is `proofs/h7_rates.md`. The self-referee is `REFEREE_H7_RATES.md`.

What that note establishes, inside this directory only, and only for the single-disc Galerkin model that reproduces the three TRACE-223 discs at level \(7\):

- **[CA]** At \(d = 31\), every nonzero class and every sector has rate at most \(1.0923934786042258\).
- **[CA]** At \(d = 49\) and \(d = 217\), every nonzero class in the surviving sectors \(a\in\{0,4\}\) has rate at most \(1.2876123688383678\) and \(1.2892227802420704\) respectively. Both maxima sit on the level-\(7\) survivor, copied by the phase identity.
- **[CA]** Three included conductors have a surviving-sector orbit above \(T'\): \(1.4587724665845072\) at \(d = 3437426497\), \(\beta = (-208,0)\); \(1.5119805994002586\) at \(d = 24061985479\), \(\beta = (227,227)\); \(1.4686852970394264\) at \(d = 2735635252619983\), \(\beta = (-89,0)\). Sector \(0\) is a surviving sector, so the cancellation on sectors \(2\) and \(6\) does not remove them.
- **[P]** No uniform majorant under \(T'\) falls out of \(d\equiv 1\pmod 3\). The untwisted step exceeds \(T'\), inheritance covers only a sublattice, the period is \(3p\), and the length bound \(\log_\lambda d < 3p/4 - 1/6\) does not control the spectral radius. The third crossing lies above \(\sqrt{\mu^*_{\mathrm{model}}}\).

H7* stays open. The seventeen conductors that were only searched along rays are not certified under \(T'\). The model is not the multi-disc operator of TRACE-223. `record/claims.json` was not edited.

Independent note on the open inputs of Theorem R♯-mod v5 (BGS-TRACE-325). The claim registry, `README`, and the hash-pinned sources are unchanged. Status tags in this directory are local to the note: **[P]** proved here, **[P-sketch]** a written argument with a named gap, **[N]** a numerical observation, **[C]** a conjecture. A finite computation is not an asymptotic theorem.

`evidence/breakthrough/` is about the Δ → 0, JBL, Lemma U, and Gap G package. It does not speak to H1 or H3. The governing statement of v5 is `computations/verification/lineN_theorem_draft/THEOREM_DRAFT_v5.md`, with the N20 re-scoping in `evidence/executions/20261101/lineNgas/N20/REPORT_N20_v2.md`.

## Second target: H7* and H8

The span law below is kept as a record of the first target. The second target is H7* (BGS-TRACE-305) and H8 (BGS-TRACE-306). The proof note is `proofs/h7_h8.md`. The self-referee is `REFEREE_H7H8.md`.

What that note proves, inside this directory only:

- **[P]** \(7 \mid K_p\) and \(7 \nmid h_p\) for every prime \(p \ge 5\), by the recurrence modulo \(7\). TRACE-265 had checked the finite range \(p = 5,\ldots,23\). Level \(7\) stays the covered level (TRACE-223). The identity \(h_{3p} = h_p K_p\) is re-proved from the closed form; the rank-\(3p\) statement is cited.
- **[P]** Every prime factor of \(K_p\) is congruent to \(1\) modulo \(3\). This is weaker than N8b’s congruence modulo \(6p\), which is cited and not re-proved.
- **[P, finite]** Complete trial-proved factorisations of \(K_p\) for \(5 \le p \le 31\). On the NSW primes \(p = 5, 7, 19, 29\), H7* inside the inclusion range \(d \le \sqrt{h_m}\) still contains \(K_p\)-divisors other than \(7\). At \(p = 7\) that list contains the prime power \(49\). At \(p = 5\), \(31^2\) divides \(K_5\) and sits above \(\sqrt{h_{15}}\).
- **[P]** A close return at the weakest \(\varepsilon\) allowed by Lemma E (TRACE-268) is shorter than the \(3p\)-factor trace by more than \(p + 7/4\), on every level \(d \le \sqrt{h_m}\). This blocks using one close return as a smallness certificate for the whole product. It does not determine the sign of \(\mathrm{Dev}_d\).
- **[P, arithmetic]** Substituting the caps \(\Lambda \le 1.9656353\) and \(r_2 \le 1.0529012\) produces \(c_{\mathrm{del}} \approx 0.73753152\), and \(\tfrac32 c_{\mathrm{del}} > 1.106\). At \(\ell_0 = p/4\) and \(\bar\rho \le 0.28\), the amplified wrap covers \(\theta < 0.16662\), while the substituted first-moment range still reaches \(\theta > 0.26224\). Covering every divisor forces \(\ell_0/p > 0.75025\). Inserting \(c_{\mathrm{del}}\) as the wrap exponent leaves a length \(\approx 0.55333\, p\).

H7* and H8 stay open. The floor comparison is conditional on an upper shape \(e^{0.05 p}\) for the positive term. The wrap obstruction is the amplified-weight case (N16b (c2)). Unit weights reduce H8 to H1, which this note does not attack. Lemma 2 of N14b stays a sketch.

## What the register already separates

Frozen R′ (BGS-TRACE-206) is open. It is the conjecture W′_m = o(m) for the k₁ kick 0.9 cos(2πq) at η = 2, odd m. Nothing below refutes it or proves it.

Theorem R♯-mod v5 is conditional. If H0, H1, H5–H8 hold and B_p ≥ κ > 0 for infinitely many primes p at least the threshold, then W′_{3p}/m → ∞ and frozen R′ fails along m = 3p. H2 and H4 are met. H3 follows from H1 by Prop. K (BGS-TRACE-332), conditional on H1-shell. The v5 threshold quoted in the draft is p ≥ 3307 when the H1 constant is C ≤ 0.082, and p ≥ 1409 when C ≤ 8.8·10⁻⁴. Those primes are conditional arithmetic. They are not a new official threshold, and this note does not replace them.

| Input | Register status | What is actually proved |
| --- | --- | --- |
| H0 | taken as given | Line F/J package cited by the draft; Prop X′ (TRACE-324) is verification-pending |
| H1 = H1-bad + H1-ali (TRACE-336) | open | Shell law for j ≤ 14, core functional only, C_cert ≤ 4.36·10⁻⁴ (Thm A, TRACE-331). Prop. F (TRACE-329): no unrestricted carry or torus bound can give H1 |
| H2 | met | δ_int^core ≤ 5.14476·10⁻⁷ |
| H3 (TRACE-301) | open as a claim; substance is Prop. K | [P + CA modulo H1-shell]. The span bound ℓ ≤ 2j + g₀ was [P-sketch]. Background interplay and polymer normalisation were [P-sketch] |
| H4 (TRACE-302) | met | δ_true ≤ 5.0313·10⁻⁶ |
| H5 (TRACE-303) | open | c_B = 0.7375 is [P-sketch]; the needed c < 0.387 is open. On the NSW-prime set 𝒫 the mixed-class clause is vacuous, and infinitude of 𝒫 is open |
| H6 (TRACE-304) | open | explicit p₀ for C′ uncomputed; squarefreeness of h_p is Wieferich-type |
| H7* (TRACE-305) | open | signed control of included levels below the floor, including prime powers dividing K_p. Theorem W is non-vacuous only at p far beyond the crossover |
| H8 (TRACE-306) | open | on prime h_p it reduces to H1 [P-sketch]; composite h_p is free only under an extra smallness condition |
| R′ (TRACE-206) | open | not refuted |
| BGS-BGS-001, TRACE-005 | open | untouched |

## The route

The obstruction inside H1 is not a missing length estimate. Prop. F already rules out every bound that uses the unrestricted joint torus mean. The joint collision relation is ε-adic, with carries |e| ≤ 51 and 6145 pair states (Lemma J); the 633-state λ-graph is only the single-window subsystem. A direct Markov certificate on that system, at block size 495⁴, is not a computation this note can close. Scalar letterwise contraction diverges (N14: κ_v up to 38). The cellwise lower bounds N_H ≥ 1 (N13 §4.2) imply that a product of norms cannot decay; the N15 table’s 2048 cell upper bounds are all above 1.04, so they also do not yield a geometric mean below 1.

H5 and H7* are real open estimates, and either one blocks v5 even after H1. They are not the cheapest step that was still marked as a sketch inside an otherwise written implication. That step is the span bound in Prop. K.

The attack is that span bound. The result is a theorem for the length, a sharp pair of constants, and a recomputed tail. H1-bad and H1-ali stay open, so H3 stays conditional and R′ stays open.

## What was proved in this note

**Theorem A [P]** (`proofs/span_law.md`). For α ∈ ℤ[√2] \ {0}, with L = log(|N(α)|/2) / log ε and with span the length of the balanced ε-digit word,

L + 1 < span < L + 3.

The length is constant on the class modulo ±ε^ℤ. The digits lie in {−1, 0, 1}. For every class except the class of √2, span = Kᵣ − Kₗ + 3 exactly, where Kₗ and Kᵣ are the thresholds |θ| ≥ 1/2 and |θ̄| ≥ 1/2. The √2 class has span 2 and Kᵣ − Kₗ + 3 = 3, and still satisfies the strict inequalities (L = 0).

**Corollary C [P].** On shell j, where 2ʲ ≤ |N| < 2ʲ⁺¹,

span < κ j + 3, κ = log 2 / log ε ≈ 0.7864397013573949.

This is the constant N20 wrote as 0.787. It is log 2 / log ε, not log 2 / log λ.

**Corollary D [P].** The cluster length ℓ = span + g₀ used by Prop. K satisfies ℓ < κ j + 3 + g₀. For j ≥ 3 this is stronger than ℓ ≤ 2j + g₀, which is therefore a theorem for those shells. The old label [P-sketch] on the span bound is discharged in this note. It is not discharged in the registry: `record/claims.json` was not edited.

**Sharpness [P].** The constants 1 and 3 cannot be improved by 10⁻³. For α = 116, |N| = 13456, span = 13 and the defect span − L equals 2.99966264991176 within 10⁻⁵⁹. For α = 82√2, |N| = 13448, span = 11 and the defect equals 1.00033740024810 within 10⁻⁵⁹. Both words were computed with integer arithmetic (integer square roots), and the logarithms are arb enclosures. The class 116 has an internal zero run of 9, so it is not a single polymer at g₀ = 4. The bad class α = 118, |N| = 13924, run 3, has defect 2.96087221277804. A uniform bound span ≤ L + 2.96 already fails on a bad class of shell 13.

**Identification [P].** On a fundamental-domain representative the project’s `eps_digits` word is this digit word (Lemmas 7 and 8). Every class with |N| < 2¹⁵ was compared: 20434 words, 0 mismatches. Shell counts match N20 from j = 0 through j = 14, ending at 10225 classes in shell 14.

**Tail arithmetic [P], conditional** (`proofs/propk_tail.md`). Assume H1-shell(C, J₀ = 12) and the cited unweighted finite activity 2Σ|w| ≤ 2.03157·10⁻⁶ (TRACE-321, core functional, j ≤ 12, g₀ = 4). Replace ℓ ≤ 2j + g₀ by ℓ ≤ κ j + 3 + g₀ inside the N20 tail, and solve KP in arb.

At C = 0.082 the activity S₀ falls from ≤ 3.43990·10⁻⁴ to ≤ 3.24088·10⁻⁴. The KP threshold a falls from ≤ 2.63843·10⁻³ to ≤ 1.52670·10⁻³. The gas sees S₀, not a, so the exponent moves by about six percent, not by the forty percent visible in a. The length weight is what moves a; e^{aℓ} with aℓ of size a few thousandths is what moves S₀.

The same program reproduces the registered crossover inputs: δ = 3.4962·10⁻⁴ gives the prime 3307, δ = 5.0313·10⁻⁶ gives 1399, and δ = 7.4115·10⁻⁶ gives 1409. Under the sharp-span majorant at C = 0.082, a sufficient prime is 3067. Under the same program’s 2j-majorant the prime is 3299. The gap 3307 − 3299 is the bookkeeping gap between the published δ and this majorant (the published solver inflates a by 1.02 each iteration). The gap 3299 − 3067 is the span theorem. At C = 8.8·10⁻⁴ either span input leaves the prime at 1409, because the finite part dominates the tail.

These primes are conditional on H1-shell, on H0, H5–H8, on B_p ≥ κ for infinitely many p, and on the additive budgets v5 still treats as idealised. They are not a replacement for 3307 or 1409.

## What remains a sketch or a hypothesis

- H1-bad for shells j > 14, at C ≤ 0.082. Open. The finite-shell margin (about 186× at C_cert ≤ 4.36·10⁻⁴) says nothing about the tail, by Prop. F.
- H1-ali, the near-collision and box constants. Open. A Lipschitz bound on |r|² through the N_H table (Lip_H ≈ 167) is too crude to start a Beurling–Selberg estimate; that route was not pursued.
- Background interplay and polymer normalisation inside Prop. K. Still [P-sketch], exactly as N20 left them. Accepting Theorem A does not make TRACE-332 unconditional.
- H5, in particular c < 0.387 against the sketch c_B = 0.7375; or else infinitude of the NSW-prime set 𝒫.
- H6 (p₀ and squarefree h_p). H7* and H8 stay open after the second note: that note gave the included \(K_p\)-divisors other than \(7\) no rate below \(T'\), and the amplified wrap at \(\ell_0 = p/4\) is outside the range the substituted \(c_B\) covers. The third note, at the top of this file, gives Galerkin rates for those divisors. It does not close H7*. H8 on prime \(h_p\) still reduces to H1 only as a sketch.
- The passage of A_bad^{KP} into the gas exponent is used here as v5 uses it. The draft header still marks that correction [P-sketch], with lineN22 recording it as correct and necessary.

## Where a proof of H1 would have to go

A bound that can survive Prop. F has to use the bad restriction: digits in {−1, 0, 1}, no internal ε-zero-run of length g₀, and, by Theorem A, word length strictly between L+1 and L+3. That is a description of the support of the sum, not an estimate of Σ |r_A r_B|². The sum is still a joint second moment on the ε-adic carry system. Closing it is the remaining content of H1-bad. This note does not claim a transfer-matrix bound, a sofic presentation, or a value of C.
