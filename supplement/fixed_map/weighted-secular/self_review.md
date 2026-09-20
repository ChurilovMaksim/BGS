# Adversarial self-review

Primary verdict for the original fixed-map claim: **incomplete**.
The smallest missing implication is a uniform estimate of the Abel trace
energy at fixed tau=10^-80. The checks do not provide that estimate.

This is self-review under the mathbox proof-audit workflow, not a fresh
reviewer or formal verification. Reviewed artifact: `determinant_boundary.md`.

## Dependencies and obligations

| Claim / implication | Evidence and verdict |
|---|---|
| Deleted roots -> geometric characteristic polynomial | Exact factorization; passed |
| Common rotation -> coefficient covariance delta_(k,l) | Integer Fourier orthogonality; passed |
| CUE has the same covariance | Weyl alternant/Fourier derivation; passed |
| Deleted clock nevertheless fails weighted pair comparison | Exact powers and Riemann sum; passed |
| Simplicity and bounded local moments of this control | Minimum unfolded gap >=2/3 for N>=2; passed |
| Ratio derivative -> trace squares | Signs, powers r^(2m-2), chain factors N^-2 checked; passed |
| Finite CUE ratio formula | Hook expansion, Schur orthogonality, direct N<=3 quadrature; passed |
| Ratio limit -> Abel limit | Fixed complex bidisc and Cauchy derivative estimate required; passed as a conditional implication |
| Countably many Abel limits -> all compact pair tests | Positive weighted measures on [0,1], including zeroth moment; passed |
| Pair convergence -> Abel convergence | Separate Fejer bound controls tails and keeps a_0=N^2; passed |
| Frozen map satisfies either sufficient estimate | Not proved; incomplete |
| Finite weighted minors resemble independent phases asymptotically | Not asserted and not established |
| Formal or fresh-agent proof certification | Out of scope; none executed |

## Delicate points checked separately

1. The deleted-clock example is an abstract unitary spectrum. It is never
   promoted to a quantization of the original fixed classical map.
2. Determinant covariance and a ratio of determinants are different
   observables. Identical covariance does not license inserting denominators.
3. The CUE ratio uses independent complex parameters b,d, not silently
   conjugated a,c. Conjugation is in U*. Complex-parameter quadrature checks
   this convention. The angular rotation is an exact transform of U.
4. The r^2 factor multiplying the normalized ratio derivative is necessary;
   the independent geometric-sum check detects its omission.
5. Moment n=0 in the compact Laplace proof controls total mass. Omitting it
   could leave an atom at the compactification point x=0.
6. Vague convergence does not by itself control Laplace tails. The converse
   proves a uniform mass bound on translated time intervals using a positive
   Fejer kernel. This uses both a_m>=0 and positive definiteness of a_m.
7. The complement of a narrow subset-frequency window need not be negligible;
   the finite computation explicitly records cancellation across the split.
8. Small fixed tau times an uncontrolled absolute weight is not an o(1)
   estimate. No use is made of floating resolution of the original tiny kick.

No defect requiring restriction of the auxiliary mathematical statements
was found in this pass. This verdict does not establish their novelty or
upgrade the finite floating computations to rigorous enclosures.
