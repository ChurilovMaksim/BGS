# Independent internal review: exact pair heat and actual-start smoothing

Base: `1e25c415239c283652c9155d03b0924b8aa61674`.
One fresh read-only reviewer reconstructed the new analytic implications
in three successive passes, followed by a check of the final exponent
wording. These are passes by one reviewer, not independent external
referees. The tasks did not supply an author verdict. The author separately
checked sources and executed the finite verifiers.

**Verdict: H1--H31 proved as written relative to the pinned inherited
stable Haar, Wick-generator and actual exponential-trace inputs.**
Full deterministic BGS, the actual unperturbed pair statistic and world
priority are not established by this review.

## Exact obligations checked

| Obligation | Independently reconstructed implication | Boundary |
|---|---|---|
| H1--H13 | Determinant-ratio hook basis, Gaussian Gram identity, cut-and-join eigenvectors, mixed Wick eigenrates and every signed contraction in the pointwise heat formula | Stable range 2m<=N; N=2,m=1 handled directly; inherited FLOW-020 G6/G15 retained |
| H14--H17 | Exact Haar heat norm, autocorrelation, triangular spectral measure and fixed microscopic-time profile | Haar L2, not actual-map point evaluation; inverse statement requires a nonzero statistic and the stated recovery equation |
| H18--H21 | Clock specialization, determinant residues, their gap dependence and the complete actual signed heat defect | Clock is a control spectrum; residues require simple spectrum but the coefficient formula allows repeated eigenvalues |
| H22--H25 | Simple spectra matching all specified Q_N=o(N) short traces, global exponential bound, uniform macroscopic measure and separated pair values | Arbitrary-start information limitation, not a chaotic-map counterexample |
| H26--H28 | Interior log-determinant control, reflected numerator, coefficient-circle bound and combined signed compensation estimate | Finite-dimensional correction exp(b) retained; no microscopic gap bound or noisy concentration assumed |
| H29--H31 | Actual-map short-window specialization, superpolynomial stable-band smoothed form factor and different signed defects for the matching starts | FLOW-020 G8 inherited; time constant depends on a; the actual unperturbed signed band remains OPEN |

The reviewer reconstructed the coefficient-generating Gaussian identity
and retained the scalar contraction -m y^(m-1). The full top-Wick operator
was used, not an inference from its interval of eigenvalues. The mixed
rate is m+m(m-1-r-s)/N; this fixes the exact exponential multiplying K_m.
The contour review checked both interior radii and the reflection identity,
then combined the square and compensating terms before applying the trace
window. These checks address the new argument rather than re-auditing the
full packet proof behind the inherited exponential trace estimate.

For the matching spectra, the reviewer checked the odd factor subsequence,
the exact short-trace identity, simplicity after the distinct tiny phase
offsets, and the pair-statistic error from those offsets. The contour
estimate subsequently shows that both heat-smoothed statistics vanish
on the same schedule while their signed defects remain different.
Neither construction is the prescribed U_N.

## Corrections before acceptance

The first pass found a reversed explanatory comparison of clock pointwise
decay and Haar norm decay. The clock rate is faster for m>=2; the text
was corrected. The inverse clause now explicitly excludes the zero test
and states its recovery equation. The N=2,m=1 case is checked separately
because the inherited recorded operator statement starts at N>=3.

The second pass requested a different clock-center index so it cannot be
confused with the band endpoint b; the construction now uses h. The
author had already retained the finite-dimensional correction as exp(b)
before the third pass. That pass requested displaying the full
uncontracted exponent, including +xi*t, before the bound absorbing it.
The final wording makes that correction explicit. The closing check
confirmed that the positive analytic verdict is unchanged.

| Reviewed or promoted version | SHA256 |
|---|---|
| Initial H1--H21 submission | `54ff5239f34b9beb98772fd8bf9bb7224bab6297d3aecb800d825eed91e184f8` |
| Added H22--H25 and first-pass corrections | `4279355aa51740981d80906bcfefdd839c937804c4cfd416a7bc88ecb83548dc` |
| Added H26--H31, before final exponent wording | `2579166c1e669a890e60814af5a901465c81d59aad51190b74670ffce6ab88a2` |
| Accepted complete mathematical body | `a7b9b2b136a9fbe7ac3d50737b8434a3fda09eb010ef5f6679d481861822a9d0` |
| Promoted proof, only its status header changed | `abd5c0ab8c132667a0b7a91390ce4da3072f779a1440d72f33b35da5726d8cb2` |

The author verified byte identity after the status header between the
accepted and promoted files. These hashes identify review scope; they
are not formal proof certificates.

## Execution, source and trust boundary

The reviewer did not execute the maintained checker or the Wolfram
source. Their results are author execution, not attributed to the
reviewer. The Python implementation uses exact Fraction arithmetic and
rational real/imaginary pairs. Reused modules import NumPy, but their
floating diagnostics are not executed by the new checks.

The [source audit](../literature/heisenberg_pair_heat_sources_20261005.md)
credits prior cut-and-join heat calculus and determinant resummation.
The reviewer checked the new direct derivation relative to the inherited
stable Haar input; bibliographic metadata, global overlap and world
priority were not independently certified. There is no new analytic
Lean certificate, external referee report, proof of unperturbed
Heisenberg cancellation, higher-order heat extension or full BGS result.
