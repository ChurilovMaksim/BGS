# Review of the microscopic rounding extension

## Verdict and exact coverage

The accepted candidate was independently internally audited: proved as
written, with no mathematical gap found. This is a project review, not
external referee certification. The publication proof reorganizes the
same argument and makes the gap-transfer constants explicit. Its theorem
is an existence result for each specified K_N=o(N^(1/3)), retaining
simultaneous unnormalized trace l2 convergence, O(N^-1) norm closeness,
simple spectrum and a positive fixed stable-band lower bound.

The audit checked these obligations:

- Independent complex second moments include both variance and squared bias.
- The finite-probability existence argument selects one outcome for the
  whole specified window, not separate outcomes for its individual powers.
- The jitter gives simple spectrum, including circular wrap, and adds
  O(K^(3/2)/N²) to the trace-window l2 error.
- The stable-band lower bound keeps the negative Riemann-sum baseline and
  uses only positivity for the remaining squared traces.
- Diagonal compression proves P continuity without dimension loss.
- Tensor compression proves the Schur bound used for reversed-entry Q.
- Flatness, a fixed singular gap and fixed-observable Egorov errors transfer
  with the stated eventual qualifications.
- FM-007's N^(39/40) logarithmic trace bound is not confused with FM-013's
  separate, nonuniform-in-index O_k(1) fixed-time bounds.
- The inherited FM source statements were inspected for applicability;
  their full analytic dependency chains were not independently reproved.

## Prior ownership and boundary

Spectral rounding, first-order Egorov preservation and simple-spectrum
splitting were already project results in the spectral-resolution manuscript
proposition and its ledger entry. This extension adds the unbiased
low-trace selection, stable-band witness and newer P/Q continuity package.
A bounded repository search found no earlier identical simultaneous
low-trace refinement; this is not an external priority finding.

The altered sequence need not retain exact quantization, arithmetic data,
subprincipal symbols or higher-order microlocal structure. The conclusion
rejects sufficiency of only the enumerated coarse hypotheses. It does not
refute BGS for the prescribed frozen sequence, and does not claim the
entire repository's information is insufficient.

## Proof and computation boundary

The canonical proof is `mathematics/microscopic_rounding_control.md`.
No finite numerical experiment, asymptotic computer proof, external source
priority review, Lean certification or new executable verifier is claimed.
A finite Bernoulli enumeration would only illustrate the expectation
argument and cannot validate the analytic trace window, Riemann-sum limit,
or operator continuity theorem. No verifier is added because it would not
materially strengthen this elementary proof. Consequently normal/-O,
silent-import and fault-injection requirements for new code are inapplicable.
Source-integrity checks are recorded separately in the evidence manifest.

## Destination integration note

The immutable evidence/microscopic_rounding_provenance.json describes the earlier preparation overlay. Its “not integrated” status is historical, and its README/INTEGRATION artifact paths and hashes are preparation-artifact identities, not a list of missing current repository files. Those guide copies are archived under record/history/2026/next_proofs_20261006/rounding/. The current canonical proof and this review are readable curated derivatives; original accepted source/review bytes remain external and are not claimed to have been published here. Destination integration checks are recorded separately in evidence/executions/20261006/next-proof-integration/receipt.json.
