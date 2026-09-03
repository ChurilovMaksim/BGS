# M1 — fluctuation energy and cross-twist cancellation

## Goal

Prove an asymptotic fluctuation estimate strong enough to connect the exact even-moment reduction to the desired local spectral law, in a precisely stated regime for `(N,K,m)`.

## Exact starting point

For ordered twist pairs `tau`, write the relevant fiber contribution as `A_tau` and its convolution contribution as `F_tau=A_tau*A_tau`.  The energy is

`E = ||sum_tau F_tau||_2^2`.

It must be expanded as diagonal plus cross terms.  No cross term may be dropped without exact orthogonality or a quantitative cancellation theorem.

## Known failure modes of the historical proof

1. `O(1/K^2)` is not `o(1)` when `N -> infinity` with fixed `K`.
2. The old numerical table itself exceeded its stated `16/K^2` envelope at `K=17`.
3. Cross-twist terms were omitted.
4. Fourier/Parseval normalizations were inconsistent.
5. Perfect-power exclusions were asserted rather than proved.
6. The uniform `4 sqrt(N)` fiber bound misses the exact `d=0` semi-trivial degeneracy.
7. The R86/R87 noncommutative-binomial shortcut is invalid as stated.

## Work packages

### A. Exact fiber/divisor classification
Classify every collision among zero, pole, `0` and infinity for `u^r v_d(u)^s`, including `d=0,±1`, and formulate the correct character-order congruences.

### B. Exact cross-Gram formula
Fix one Fourier normalization and express `<F_tau,F_sigma>` as a character sum suitable for cancellation, not as a product of independent upper bounds.

### C. Exceptional-fiber extraction
Evaluate exceptional fibers exactly and remove them before any Weil/Deligne estimate.

### D. Generic finite-field estimate
Verify the divisor/perfect-power hypotheses and only then invoke an appropriate character-sum theorem.

### E. Summed cancellation and scaling
Control the full Gram sum with the true number of twists and prove a remainder that tends to zero in the declared regime.

## Falsifiers

Use at least `N=53,199,3571` and additional split primes.  Vary `K` where possible so apparent `N` decay cannot be confused with a small `K`-dependent constant.

## Status

OPEN.  Current computations diagnose the missing terms; they do not yet prove the desired asymptotic estimate.
