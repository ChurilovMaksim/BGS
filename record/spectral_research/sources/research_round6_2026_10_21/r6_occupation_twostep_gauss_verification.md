> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round6_2026_10_21/r6_occupation_twostep_gauss_verification.md`. Embedded SHA256: `524441a142da1a66c52f50e0269a54c7d6b7104364d1cd31190d4028af99e096`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/histories.md).

# Executed high-precision verification of the exact two-step Gaussian kernel

21 October 2026.

## Exact proof being checked

The independent exact proof is:

- r6_occupation_twostep_gauss.md
- SHA256: 18c580433804f46443d565aed27517bdd5e809017b115c8fb4bc081a215a53da

It proves the all-odd 24-image formula for $M_N^2$, including its scalar normalization, its Weyl covariance, and the exceptional support restriction when $3\mid N$. The verification below is supplemental and is not used to prove the formula.

## Executed implementation

The Wolfram Language source was executed through the available Wolfram evaluator with a 45-second evaluation limit. It completed successfully.

- Source: r6_occupation_twostep_gauss_check.wl
- Source SHA256: 9c3d6a8b0713d615c09fc0acc9a24e50b94ca62ad5fcafa2c07406cf7c921d3d
- Compact result: r6_occupation_twostep_gauss_check.json
- Result SHA256: 9a3c060fe0baacb9a262d6ef751e40e2830bd5b35b8a725c894d5ee4806b0f4b

The working precision was 90 decimal digits. The acceptance threshold for each identity was $10^{-65}$.

The dimensions checked were
$$
 3,5,7,9,11,15,21,25,27,33,45.
$$
Thus the checks include primes, composite dimensions, powers of three, and the edge case $N=3$.

The source forms the original matrix using its modular inverse $8^{-1}$, directly multiplies that matrix by itself, and compares it with separately constructed finite image sums. In particular the tested original square is not constructed by substituting the claimed image formula.

For each dimension it checks the scalar modulus, Gauss norms, normalized image formula, support modulus, row norms, direct completion formulas, both Weyl covariances, both integer-coordinate periods, and Fourier coefficients of the arithmetic correction. Across the run it checks all 5419 entries of the eleven directly multiplied matrix squares and 1032 Fourier coefficients. Every test passed.

Wolfram's resulting residuals were numerical zeros with reported estimated accuracy between approximately 87 and 90 decimal digits. A displayed value such as 0 with an accuracy mark of 87.46 is an approximate zero at that precision, not an exact algebraic zero. These checks are not an interval-arithmetic certificate.

The result object returned by the evaluator was long enough for one detailed per-test array at $N=15$ to be truncated by the tool display. All per-dimension pass indicators, maximum residuals, counts, and global summary fields remained intact. The saved JSON therefore deliberately contains those complete compact fields and does not present a partially displayed detailed array as complete.

## Unexecuted portable prototype

The separate Python prototype r6_occupation_twostep_gauss_check.py requires mpmath. That dependency was absent from the local environment, and installation could not be completed with the available network permissions. The Python prototype was therefore not executed. The executed numerical verification reported above is the Wolfram Language implementation.

## Scope

This is a finite consistency check of an exact initial-kernel identity. It is not a numerical test of the sine-process limit, of $H_{\rm diag}$, or of the two-stage physical asymptotic for the fixed $10^{-80}$ kick. Those claims must be assessed from their mathematical proofs and their stated unresolved estimates.

