# Sources and priority boundary: resonant density control

Checked 1 October 2026. Elementary positive smoothing, arithmetic
projection, Holder and interpolation are prior methods. The project does
not claim to have invented these tools or established world-first priority.

## Load-bearing reference moment theorem

Diaconis--Evans, *Linear functionals of eigenvalues of random matrices*,
Trans. AMS 353 (2001), 2615--2633, DOI
[10.1090/S0002-9947-01-02800-8](https://doi.org/10.1090/S0002-9947-01-02800-8).
The primary [author-hosted PDF](https://statistics.berkeley.edu/sites/default/files/tech-reports/577.pdf)
was reopened; Theorem 2.1(a), printed pp. 3--4, is the source already
pinned as EXT-DE-2001. In TRACE-011 it is applied to the CUE background
of dimension H=N-K, with positive-cone endpoint b<1/4 and actual maximum
weighted degree 4bN<=H for sufficiently large q. It matches the finite
second/fourth/sixth moments used in the mixed-cluster variance proof.

The all-band pair covariance bound is **not** an application of Gaussian
matching outside this range. Its cumulant formula and safe constant 26H
are derived from the finite projection determinant in the proof. The bin
third/sixth moment bounds and their covariance inequality are separately
derived from the same positive determinant, not assumed independent.

## Related prior work, not a theorem dependency

Lagarias and Rodgers, *Higher Correlations and the Alternative Hypothesis*,
[arXiv:1905.12123v3](https://arxiv.org/abs/1905.12123v3), 19 August 2019;
Quarterly J. Math. 71 (2020), 257--280, DOI
[10.1093/qmathj/haz043](https://doi.org/10.1093/qmathj/haz043).
The primary abstract describes point-process constructions illustrating
the insufficiency of known restricted correlations for a zeta-zero
alternative. Only the abstract and bibliographic record were inspected
in this cycle; no theorem, exact analogy to all-band pair tests, or
priority conclusion is imported from it. This is related literature to
study further, not proof authority for TRACE-011.

## Earlier project results

[TRACE-009](../mathematics/prime_resonant_sector.md) supplies the actual
oriented block and pair mass criterion. [TRACE-010](../mathematics/trace-bridge/signed_heisenberg_comparison.md)
supplies the exact signed cubic target, reference variance and older
cardinality-dependent budget. The finite homometric example in
[the CUE upload review](../archive/record/cue_upload_review_20260927.md) already
refutes pair-only determination of higher statistics. The new result is
the density-conditioned resonant deletion and critical-tail construction,
not the general fact that pairs need not determine triples.
