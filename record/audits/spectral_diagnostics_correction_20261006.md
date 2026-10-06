# Spectral diagnostic correction, 6 October 2026

Scope: external review round 3, defects 1 and 2 only. This is a numerical
method correction, not new BGS research or a verification of an asymptotic law.

## Historical evidence and reproduced failures

`evidence/numerical/goe_spacing.json` and
`evidence/numerical/matched_window_count_variance.json` remain byte-for-byte
historical artifacts. Their polynomial unfolding has a known order-preservation
defect. They must not be cited as validated statistical evidence or as the output
of the corrected producer. The new files with suffix `_monotone_v2.json`
supersede their numerical diagnostic role without rewriting the old results.

The original degree-11 least-squares CDF fit has three adjacent inversions at
(p,K,a,q)=(3571,17,2469,1). The largest negative gap is -0.8672741670539494.
The small design (199,11,139), q=[1], one GOE realization, seed=20260901,
L=2,3 exactly reproduces unequal means with the old false zero standardized
difference. Raw reproduction is in `spectral_legacy_defects_20261006.json`.
Across the full original designs, legacy nonmonotone counts are 2/40, 5/43,
3/25, and 3/60 respectively: 13 defective processing instances among 168,
with overlapping cat-map designs. Matching GOE processing does not cancel this.

## Corrected method and contract

For sorted raw levels lambda_j, n>=4, set
h = 1.06 s n^(-1/5) b, where s is their sample standard deviation (ddof=1),
and b>0 is the bandwidth factor. Define
U(x) = sum_j Phi((x-lambda_j)/h), the integrated Gaussian kernel density.
Its derivative is sum_j phi((x-lambda_j)/h)/h > 0 for finite x and h>0.
Thus raw level order is preserved in exact arithmetic. Floating-point outputs
are checked for finite values and negative differences; ties are allowed.
This is smoothing, not the empirical rank CDF, and does not force unit gaps.

Only raw levels are sorted. Both gap extraction and the forward-window
statistic reject transformed inversions. The old `unfold_polynomial` function
is retained exclusively to reproduce the known failure in explicit regressions;
active report generation never calls it. Input shape, finiteness, positive
bandwidth/spread, positive window width, and trimming bounds are checked.
For optional edge trimming, fit all levels first, then remove floor(n e)
levels at each end; at least four levels must remain. Default b=1 and e=0.
Spacing gaps are divided by their retained mean. Window widths stay in the
integrated-density coordinate and remain anchored, edge-truncated windows.
Neither their statistic nor its sensitivity is stationary number variance.

The descriptive difference uses sample standard deviations (ddof=1) divided
by square roots of sample counts, combined by a Euclidean norm. With fewer
than two observations in either group the standardized value and scale are
JSON null, status `insufficient_replicates`. With two or more in both groups
but zero denominator, the standardized value is null, status `zero_spread`,
including equal means. Absolute mean difference is always retained. No null
is interpreted as agreement. q-values need not be independent; this scaling
is descriptive and supplies neither a z-test nor confidence calibration.

## Verification and sensitivity

`python computations/analysis/spectral_diagnostics.py verify` now first runs
`computations/verification/spectral_diagnostics_contracts.py`, then recomputes
and compares only the two corrected v2 evidence files (tolerance 1e-9).
A PASS is explicitly numerical regression, not statistical/scientific truth.
Negative tests include the actual polynomial inversion, injected transformed
inversions, nonfinite/degenerate inputs, insufficient replicates and both
zero-spread cases. Invariants include monotonicity, affine-scale equivariance,
input permutation invariance, duplicate levels, nonconstant gaps, and unit
mean normalized gaps. The existing both-sided empirical-CDF test also passes.

`computations/verification/spectral_smoothing_sensitivity.py` reuses raw
spectra across the prespecified grid b={0.5,1,2}, e={0,0.05,0.1}, for every
original design and seed, without choosing a winning setting. Results are
`evidence/numerical/spectral_smoothing_sensitivity_v2.json`. All corrected
spacing transformations have positive adjacent gaps in that tested range.
CDF sup-distances range 0.01314–0.03012 for p=3571 and 0.007897–0.01056
for p=19489. At L=12 the cat-map forward-window variance ranges
2.4984–4.1938. This substantial window-statistic sensitivity prevents treating
one setting as robust quantitative GOE agreement. The nominal bandwidth is a
smoothing convention, not an independently validated density model.

Commands (from repository root, Python/NumPy/SciPy float64):

- `OPENBLAS_NUM_THREADS=1 python computations/verification/spectral_diagnostics_contracts.py`
- `OPENBLAS_NUM_THREADS=1 python computations/analysis/spectral_diagnostics.py spacing --output evidence/numerical/goe_spacing_monotone_v2.json`
- `OPENBLAS_NUM_THREADS=1 python computations/analysis/spectral_diagnostics.py window --output evidence/numerical/matched_window_count_variance_monotone_v2.json`
- `OPENBLAS_NUM_THREADS=1 python computations/verification/spectral_smoothing_sensitivity.py > evidence/numerical/spectral_smoothing_sensitivity_v2.json`
- `OPENBLAS_NUM_THREADS=1 python computations/analysis/spectral_diagnostics.py verify`
- `OPENBLAS_NUM_THREADS=1 python computations/verification/cdf_sup_regression.py`

No historical JSON, mathematical theorem, model convention, or statistical
threshold was altered. Full complex Hermitian diagonalization remains intact.
