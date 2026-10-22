# External source scope in the final spectral edition

**Later scoped update:** the TRACE-109/110 qualifications below were closed in the
[22 October review](../record/trace_closure_20261022.md). This dated note preserves
the earlier review scope.

Checked 21 October 2026. This source check is distinct from the historical
author audits preserved in the imported corpus.

## Lindemann--Weierstrass leaf in the final arithmetic test

Primary source: Cheng-Chao Huang, *Explicit Bounds for Linear Forms in the
Exponentials of Algebraic Numbers*, ISSAC 2022, DOI
[10.1145/3476446.3536170](https://doi.org/10.1145/3476446.3536170),
[author version v2](https://arxiv.org/html/2112.05004v2), Introduction,
Theorem 1.1. The exact theorem statement was opened and checked.
It gives nonvanishing of an algebraic linear combination of exponentials
of distinct algebraic exponents, with nonzero algebraic coefficients.

Application: if distinct algebraic real $a,b$ had algebraic
$z=e^{im\tau N(a-b)}$, the exponents $0$ and $im\tau N(a-b)$
and coefficients $-z,1$ would violate that statement. They satisfy its
hypotheses because $m\ge1$, $N\ge3$, and the prescribed $\tau$ is nonzero
algebraic. Hence distinct generator eigenvalues do not acquire equal or
root-of-unity kick phases. Multiplicities of the generator are retained.
This qualitative conclusion supplies neither a uniform gap nor the
eigenvectors or local statistics of the noncommuting product.

## Determinantal background and unclosed trace inputs

Alexander Soshnikov, *Determinantal random point fields*,
[arXiv:math/0002099v4](https://arxiv.org/abs/math/0002099v4), is the
existing determinantal-process background reference. Its metadata and scope
were checked; no new theorem application is certified merely by that check.
The maintained TRACE-086 note already spells out the finite CUE determinant,
Bonferroni and smoothing argument used for the sufficient process criterion.

The old Bowen--Ruelle/pressure and exact amplitude chain underlying trace
input (T) was not independently closed by this integration. Imported author
literature verdicts retain that provenance. TRACE-109/110 therefore retain
their stated analytic input qualifications. No new external leaf is silently
added to a proved core claim.
