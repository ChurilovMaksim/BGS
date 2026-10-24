# Holomorphic shell identifiability and spectral resolution

The maintained proofs are part of the canonical article, not parallel papers:

- `manuscript/unified_sections/holomorphic_shell_rigidity.tex`: finite-rank
  analytic contact bound, shell-and-normal-jet identification, sharpness and
  the punctured-domain obstruction.
- `manuscript/unified_sections/shell_stability_obstruction.tex`: explicit
  bounded polynomial pairs defeating every uniform Holder estimate for
  two-circle intensity recovery, with an exact truncation defect.
- `manuscript/unified_sections/spectral_resolution.tex`: simple unitary clock
  spectra indistinguishable below N/2 trace time, and spectral rounding as a
  negative control for first-order Egorov alone.

## What changed relative to the polynomial theorem

The separated-rank argument uses a confluent dilation determinant of analytic
functions with distinct Taylor orders. It does not truncate the functions.
For a nonzero rank-r kernel the total contact multiplicity on positive product
curves is at most r-1. Thus maps to C^d are identified by 2d total shell/jet
conditions; the count is sharp in one complex dimension. The centre must be in
the analytic domain. The earlier polynomial theorem remains a valid subcase.

Scalar two-circle uniqueness is prior work of Perez (arXiv:2009.02061v2,
Theorem 2.2), and general severe phase-retrieval instability is also prior
literature. Neither is presented as a new discovery. Novelty of the precise
vector-valued/multiplicity extension and explicit quantitative construction
has not been independently established.

The stability lower bound is not a matching rate theorem. The spectral
negative controls do not belong to a proved fixed smooth microlocal class,
and do not settle BGS for the maintained kicked cat map. No positive generic
microscopic universality theorem is asserted.

Exact reproduction and fresh execution metadata are in
`record/holomorphic_shell_review.md` and
`evidence/certificates/holomorphic_shell_review.json`.
