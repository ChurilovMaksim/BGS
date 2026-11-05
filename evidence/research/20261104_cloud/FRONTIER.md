# Frontier note, 4 November 2026

Scope of this note: the conditional Theorem R♯-mod v5 (BGS-TRACE-325) for the frozen k1 kick at η = 2, and the open inputs that still separate it from a refutation of frozen R′ (BGS-TRACE-206). Microscopic fixed-strength BGS (BGS-BGS-001) stays open. Nothing here is a registration. `record/claims.json` is unchanged.

Labels: [P] proof written in this directory; [P-sketch] outline with a named gap; [CA] interval arithmetic; [P-arith] the same float-plus-exact-integer standard as the v5 crossover; [N] unchecked numerics; [H] hypothesis. A finite computation is not an asymptotic theorem.

## What is unconditional

Frozen R′ is open. It is not refuted at any single prime, and W′_{3p}/m → ∞ is not proved.

The following are proved at the scope already registered, and this note does not reopen them.

- The structural bookkeeping of the gas: positivity, the TRACE-213 level identity, the coding lemma, Lemmas P/P′, the carry reductions, Lemma J (ε-carries, |e| ≤ 51, 6145 pair states), the renewal Lemma R, and Prop. F’s lower bound on the unrestricted joint torus mean.
- H2 and H4. The true-functional interaction constant satisfies δ_true ≤ 5.0313×10^{-6} for every window length (BGS-TRACE-326).
- The finite bad shells j ≤ 14 for the core functional: C_cert ≤ 4.36×10^{-4} (BGS-TRACE-331). By Prop. F those shells are not evidence for the tail.
- Prop. K’s arithmetic implication from an H1 shell bound to a Kotecký–Preiss weight, except the two sketches named below.

The November 2026 breakthrough package (`evidence/breakthrough/`) is a separate method search (Δ→0, JBL, Lemma U, Gap G). Its standing open fronts do not feed H1, H3, or the gas exponent. It does not change the status of R′ or of BGS-BGS-001.

## What Theorem R♯-mod v5 actually says

Let m = 3p with p prime. Write

B_p = (n/h_p) [(2(1+Re Λ_lo′)^p exp(−p(δ + A_bad^KP)) − 1 − |X_tail| − |X_cross| − |Y| − e^{−0.28 p})^2 − 1] − I_p − ε_16 − ε_fl − ε_other,

with Re Λ_lo′ = 6.234×10^{-4} and δ = δ_true. If B_p ≥ κ > 0 for infinitely many primes past the thresholds in `THEOREM_DRAFT_v5.md`, then W′_{3p}/m → ∞ and frozen R′ fails along m = 3p.

That implication is [P mod inputs], with one [P-sketch] step: the passage from the Kotecký–Preiss logarithm to a modulus, which charges the background-renormalised activity S_0(a) and has no sign information on bad clusters (referee lineN22).

## Inputs, as of this note

| Input | Registered state | After this note |
|---|---|---|
| H0 | Standing package, taken as given | unchanged |
| H1 = BGS-TRACE-336 | open [H]: bad joint second moment on the ε-chain, C ≤ 0.082 at J_0 = 12, plus H1-ali | **still open.** Prop. F and the uniform step-norm majorant are both unavailable as proofs (below) |
| H2 | met | unchanged |
| H3 = BGS-TRACE-301 | open; superseded in substance by Prop. K | **still open.** The span sketch inside the implication H1 ⇒ H3 is now [P]. Background renormalisation remains [P-sketch] |
| H4 | met, δ_true ≤ 5.0313×10^{-6} | unchanged |
| H5 | open (composite h_p, or infinitude of 𝒫) | unchanged |
| H6 | open (p_0 and squarefreeness of h_p) | unchanged |
| H7* | open (included levels other than h_p, rate < 1.42785) | unchanged; needed even on 𝒫 |
| H8 | open; on prime h_p it reduces to H1 | unchanged |

On the subsequence 𝒫 = {p : h_p prime}, H5 drops out and the squarefree half of H6 drops out. Infinitude of 𝒫 is the negation of R_NSW (BGS-TRACE-210) and is open. H1, the p_0 half of H6, and H7* remain even on 𝒫.

The idealised rate-budget threshold (tails = Y = X_cross = ε = 0, n/h_p := 1) is the first prime 3307 if H1 holds at C ≤ 0.082, and 1409 if it holds at C ≤ 8.8×10^{-4}. The first is fragile under the background normalisation (+1% in S_0 moves it to 3359). The second is stable up to a factor two in A_bad^KP. Additive budgets are uncomputed. Both numbers are conditional on H1.

## The route that is still alive

H3 is not an independent analytic problem. Prop. K (BGS-TRACE-332) turns an H1 shell bound into a Kotecký–Preiss weight a = a(C), and the v5 exponent then charges A_bad^KP = S_0(a). Two sketches sat inside that implication: the digit span ℓ ≤ 2j + g_0, and the replacement of the bare activity w by the background-renormalised activity w̃.

The span sketch is the one that can be removed by a direct argument. It is removed here.

**Theorem (span).** For every nonzero α ∈ ℤ[√2], the ε-digit span of the code word used by the gas is at most ⌊log_ε(|N(α)|/2)⌋ + 3. In shell j this is at most ⌊j log_ε 2⌋ + 3, hence at most 2j for every j ≥ 3, and at most ⌊4j/5⌋ + 3. The additive 3 is achieved at α = 2. Proof: `proofs/01_span_bound.md` [P]. Exact check through shell j = 16: `numerics/logs/span_exact.json`.

With that length in the tail, the same H1 hypothesis C ≤ 0.082 produces a smaller activity than the slope-2 majorant. At the fixed point of the Kotecký–Preiss map, S_0 ≤ 3.2405×10^{-4} and the idealised crossover moves from the slope-2 value 3299 to **3067**. The published 3307 is the slope-2 majorant at a 2% inflated weight; the same published script returns 3307 on the input 3.4962×10^{-4} and 1409 on 7.4115×10^{-6}. Details: `proofs/04_propK_sharp.md` [P for the length, CA for the sums, P-arith for the crossover, conditional on H1].

3067 is as fragile as 3307: +1% in S_0 moves it to 3109. At the strengthened constant C ≤ 8.8×10^{-4} the idealised prime stays **1409**. The length sharpening does not relax the constant H1 has to meet.

## What cannot prove H1

Three routes are closed as methods.

1. **Unrestricted torus or carry bounds.** Prop. F (BGS-TRACE-329): orbits that shadow the fixed point make the joint mean ≫ the i.i.d. product out to time 10^{10}. A positive-proportion subset of that neighbourhood has an internal ε-zero run longer than g_0 = 4, so the mass that beats the i.i.d. product can be placed on the complement of the bad set (`proofs/02_propF_disjoint.md` [P]). The obstruction stands.
2. **Phase-free carry majorants.** Lemma G / O1: the 633-state λ-graph has adjacency spectral radius at least 20, and a scalar weight κ_1 ≤ 0.012 is forced. Letter weights are larger. Lemma J says this graph is only the single-window subsystem of the 6145-state ε-system.
3. **The uniform step-norm N_H ≤ 2.91656.** Charging that bound on every factor of a word of the proved span already exceeds the whole H1 shell budget at every j ≥ 1, by a factor above 10^4 at j = 1 (`proofs/03_uniform_norm_obstruction.md`). This says the majorant is too crude to be a proof. The certified shell sums through j = 14 are much smaller, so the same estimate does not bear on the truth of H1.

## What a proof of H1 still has to be

A phase-keeping bound on the bad-restricted joint system: A on even ε-sites, B on odd sites, internal zero-runs shorter than g_0 = 4, carries |e| ≤ 51. Lemma R is the bookkeeping that turns first-return norms into a geometric rate. The missing input is those return norms. A direct cone on 495^4 blocks with digit memory about 8 is the natural shape of the certificate and is not a computation that can be run by enumerating the cone.

H1-ali, the near-collision comparison between the lattice and the main term, is a separate open half of H1. The span theorem does not touch it.

Background renormalisation is the other half of the H1-to-threshold step. Inside the point-insertion model it is the explicit factor below, and it is at most 1. Outside that model a one-percent error in S_0 still moves every fragile threshold.

## Continuation: the factor, and the phase-keeping gap

**[P] Digit alphabet.** The code letters satisfy E_k ∈ {−1, 0, 1}. The bound |E| ≤ 2 in N14 was one larger than the range of red allows. Both nonzero letters occur at α = 2. The census through shell 16 (81 709 classes) found no other letter. This does not shrink the 6145 Fourier-carry states. Proof: `proofs/05_digit_alphabet.md`.

**[P, inside the point-insertion model] Background factor.** If the model weight on every interval is (1+Λ)^{length} exp(Δ · length) with Re Λ ≥ 6.234×10^{-4} and |Δ| ≤ δ_true, then

|w̃(γ)/w(γ)| ≤ exp(−c ℓ(γ)), c = log(1+Re Λ_lo′) − δ_true > 6.181×10^{-4}.

For ℓ ≥ 4 the factor is < 0.997531. Bare moduli dominate the renormalised activities, so the idealised prime **3067** computed from the bare sharp tail remains a sufficient threshold. A further 0.1% enlargement of S_0, a margin for one cut bump, keeps the prime at 3067; a 0.2% enlargement moves it to 3079. The cycle form of this model is the N11 identity, confirmed in structure and not proved. Proof: `proofs/06_background_factor.md`.

**[P] The order-unit norm misses C ≤ 8.8×10^{-4}.** The generic CP prefactor 1.53×2.22 per window squares to 11.54 for the joint pair. That is 1.31×10^4 times 8.8×10^{-4}. Proof: `proofs/07_phasekeeping_gap.md`.

**[CA], weights [N]. The 24 580-vertex norm majorant.** Collatz–Wielandt gives ρ ≥ 571.90 under the N14 letter weights, so the prefactor at rate 0.28 is infinite. Proof: `proofs/08_transfer_24580.md`.

**[N] Phase-keeping boxes through E = 10.** The sesquilinear step was rebuilt and iterated with the blocks kept, up to 441 carry states (4.4 GB). It reproduces the published E = 1 and E = 4 rates. The growth locks at 0.272551, below 0.28, through E = 8; at E = 10 after six steps it is 0.272546 and still approaching that lock. The running prefactor at rate 0.28 is finite on each box and still rising: 17.51 at E = 4, 31.45 at E = 8, 36.73 at E = 10. The slope of 1/share has fallen from about 2.3 to 1.61 and has not hit zero. This is not an interval certificate and not a bound for |e| ≤ 51. H1-bad at C ≤ 8.8×10^{-4} stays open. Proof: `proofs/09_phase_carry.md`.

**[P] The lambda-carry tail past |e| = 14 is empty.** The bounded solutions of e_t − 6 e_{t−1} + e_{t−2} = v_t, |v| ≤ 60, are the convolution against a kernel of ℓ^1 norm 1/4. Thus |e| ≤ 15, with equality only for the two constant letters v = ±60, which never visit 0. Every bounded orbit through 0 has |e| ≤ 14. The kernel tail is geometric with ratio μ = 3−2√2 < 1/5; nine lags already move a carry by less than 10^{-6}. For every E ≥ 14 the truncated operator agrees with the full single-window operator on the orbit of (0,0). There is no series in E left to sum. This does not bound the spectral radius, and it says nothing about the ε-system at 51. Proof: `proofs/10_green_tail.md`.

**[CA] Disk prefixes for E = 0 through 8. [CA, partial] three steps of E = 14. E = 9 through 13 not run.** Entrywise complex disks, built from flint balls at precision 80, enclose the computed steps. For E ≤ 8, every upper endpoint from step 3 on is strictly below 0.28. The E = 8 interval after six steps is [0.272547173, 0.272547426], and the prefix prefactor is 31.4548230. The prefactors, each attained at the third step, are 1.62610257, 6.92654067, 10.8328510, 14.1082483, 17.5072948, 21.2895613, 25.1398208, 28.5948449, 31.4548230. These bound the computed prefix, not every later iterate. The sharp box was stopped after three steps: the rates are 3.9265956038, 0.9447813107, 0.2864721874, and the running product at rate 0.28 is 14.024, 47.319, 48.412. The third rate is still above 0.28, so this is not a bound of the full-carry orbit by 0.28, and 48.412 is not a proved prefactor for every n. Proof: `proofs/11_ball_orbit.md`. H1 remains open.

## Order of work that matches the dependencies

1. The span bound and the digit alphabet are available as inputs. The length is ℓ(γ) ≤ ⌊j log_ε 2⌋ + 3 + g_0, and the letters lie in {−1, 0, 1}.
2. Under the point-insertion model the bare sharp tail already charges an upper bound for the renormalised activity, and 3067 is a sufficient idealised threshold at C ≤ 0.082. It is stable under a 0.1% boundary enlargement and fragile under 1%.
3. The constant C ≤ 8.8×10^{-4} is not reached by the order-unit norm. Closing it requires the phase-keeping contraction on the 24 580-vertex restricted graph, with a prefactor ≤ 8.8×10^{-4}. The finite shells show that a prefactor of that size is compatible with the core functional through j = 14.
4. H5–H8 are independent of this computation. H7* is required even if 𝒫 is infinite. None of them is discharged here.

BGS-BGS-001 remains open on every reading of this note.
