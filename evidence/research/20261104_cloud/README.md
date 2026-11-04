# Research note, 4 November 2026

Independent pass on the open gate of Theorem R♯-mod v5 (BGS-TRACE-325): hypothesis H1 (BGS-TRACE-336) and the Kotecký–Preiss input H3 (BGS-TRACE-301). Frozen R′ (BGS-TRACE-206) and microscopic BGS (BGS-BGS-001) stay open. The claim registry is not modified.

| File | Role |
|---|---|
| `FRONTIER.md` | Proved versus conditional, and the route that is still alive |
| `proofs/01_span_bound.md` | [P] Digit span ≤ ⌊log_ε(\|N\|/2)⌋ + 3, sharp at α = 2 |
| `proofs/02_propF_disjoint.md` | [P] A positive-proportion subset of the Prop. F neighbourhood lies outside the bad set |
| `proofs/03_uniform_norm_obstruction.md` | [P mod N_H ≤ 2.91656] The uniform step-norm cannot prove an H1 shell |
| `proofs/04_propK_sharp.md` | [P+CA mod H1] Tail with the sharp length; idealised prime 3067 at C ≤ 0.082, still 1409 at C ≤ 8.8×10^{-4} |
| `proofs/05_digit_alphabet.md` | [P] Code letters lie in {−1, 0, 1} |
| `proofs/06_background_factor.md` | [P in the point-insertion model] \|w̃/w\| ≤ exp(−c ℓ) < 1, so 3067 stays sufficient |
| `proofs/07_phasekeeping_gap.md` | [P] The order-unit prefactor misses C ≤ 8.8×10^{-4} by 1.3×10^4 |
| `proofs/08_transfer_24580.md` | [CA], weights [N]: norm majorant on 24 580 vertices has ρ ≥ 571.90, so the prefactor at rate 0.28 is infinite |
| `numerics/transfer_24580.py` | Exact graph, power iteration, flint Collatz bounds |
| `proofs/09_phase_carry.md` | [N] Phased carry boxes E ≤ 10: rate 0.272551, prefactor still rising |
| `numerics/phase_carry.py` | Float rebuild of the sesquilinear carry step |
| `SELF_REFEREE.md` | Corrections and the bounds of the tags |
| `numerics/span_exact.py` | Exact integer digits, census through shell 16 |
| `numerics/kp_sharp.py` | Ball arithmetic for the tail and the crossover |
| `RUN.md` | Commands, coverage, hashes, non-claims |

The length that Prop. K had left as a sketch is a theorem, and inside the point-insertion model the renormalised activity is smaller than the bare one, so 3067 stays a sufficient idealised threshold. H1 at C ≤ 8.8×10^{-4} is not proved: the order-unit norm is too crude by four orders of magnitude, and the phase-keeping graph was not evaluated.
