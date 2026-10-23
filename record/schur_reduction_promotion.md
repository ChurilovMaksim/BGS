# Exact balanced-pair Schur reduction: integration proposal

**Status: sealed OUTSIDE-CANONICAL portable overlay, not a canonical checkout.**
This proposal changes no canonical registry or repository file. No commit,
push, manuscript build, external review, or formalization is claimed.

## Accepted mathematical content

The maintained source is `mathematics/balanced_pair_schur_reduction.md`.
It curates the exact candidate, SHA-256
`736cce3e0129c8252edba22d6abeb201528f5cc0d3780ac9efa6d70ecb9330fe`,
accepted by the fresh-context internal review, SHA-256
`f7d59a7a3c821afce10ed2a594a9a1769d7618393fa4ba35ae8f16368a610c90`.
The original theorem and full review, including their source, execution,
delivery, failed-attempt and closing-source records, remain byte-for-byte in
`archive/evidence/schur_reduction_20261007/raw/` (generated caches excluded).

Proved: for every finite unitary U and independent left coordinate phases,
the full balanced pair Abel transform equals the sum of positive scalar
Schur energies. The three-radius expected dilogarithm criterion is equivalent
to its proposed microscopic limit. Conditional second/fourth elimination
moments, the boundary Poisson marginal and finite clock/principal-minor
nonimplications are established within their stated domains.

OPEN: the actual microscopic radial limit, deterministic nonzero-charge
comparison, propagation of initial flatness/mixing/reverse-kernel estimates
through elimination, higher factorial hierarchy, TRACE-005 and BGS.

## Dependency and scope handoff

- Exact finite-N identities: unitarity/contractivity, determinant Schur
  complement, analytic trace-log expansion, martingale and phase
  orthogonality, elementary scalar integration. No actual-model analytic
  input is needed for these universal finite-N reductions.
- Three-radius positivity holds after phase expectation, coordinate by
  coordinate. Do not assert pathwise convexity.
- Abel-to-compact uses the prior determinant-boundary positive-measure
  argument. Compact-to-Abel requires a compact majorant through frequency
  zero plus the Fejer tail estimate. Separated positive bands alone are not
  the asserted converse premise.
- The actual boundary-density consequence uses only inherited FM-021
  entrywise flatness. Its initial mixing and FM-022 reverse-kernel decay
  do not become elimination-propagation theorems. Their analytic proofs are
  not recertified by this promotion.
- The Poisson law is the standard inner-function/harmonic-measure consequence,
  reconstructed here. No new external theorem or novelty claim is added.
- The cycle control has delay N for f=z h and N-1 for h; it violates actual
  flatness/mixing and only obstructs closure from the boundary law/mean delay.
- The principal-minor witness and strict-contraction coherence witness are
  exact finite controls, not actual-family asymptotic counterexamples.
- At r=1 and |a|=1 use decoupling, never a formal 0/0 intensity ratio.

`schur_reduction_integration_proposal.json` gives machine-readable proposed
relationships. The sole integrator should assign an unused claim ID and
update authorities, theorem/navigation indexes and manuscript exposition in
one reviewed change. This overlay deliberately edits none of those registries.
The result is a distinct full-balanced-target reduction; it does not estimate
the earlier disjoint Hamming/low-switch residual or identify centered
projectors with raw path masks.

## Portable checks and trust boundary

From any working directory, using the overlay or eventual repository root R:

    python3 -B R/computations/verification/balanced_pair_schur.py

This source-bound no-argument check is silent on success. It runs both exact
families in a temporary directory. Maintained port imports and their own
no-argument invocations are silent and do not run the scientific jobs.

For recorded normal/optimized replay:

    python3 -B R/computations/verification/balanced_pair_schur.py --output-dir OUTPUT --modes normal optimized
    python3 -B R/computations/maintenance/tests/test_schur_portability.py -v
    python3 -B -O R/computations/maintenance/tests/test_schur_portability.py -v

Use the bounded entry point for scientific execution; direct port --output
invocation is an implementation interface and does not enforce OS caps itself.
The entry point pins the replay source; that source pins an immutable binding
manifest; the manifest pins exact controls, comparison code, maintained proof,
and all original author/reviewer evidence used in replay. Full runner and
entry-point bytes are also recorded before/after execution. The delivery seal
pins every maintained file, including tests and the entry point. Output paths
are relative to the recorded artifact root; output destinations colliding
with authenticated inputs or historical evidence are rejected.

Expected result bytes are authenticated and cached before any child execution.
Only the exact top-level JSON paths `/runtime_seconds`, `/python`, and `/sympy`
are separated from scientific equality. Their original and observed values
and raw hashes remain in each result. Runtime must be finite, nonnegative and
within that family's wall cap. Environment fields must be nonempty bounded
strings. Every other value, key, type, array order and structure is compared
exactly; no recursive name-based exclusion is used. Diagnostics return at most
12 mismatch paths of at most 240 characters. JSON duplicate keys and nonfinite
constants are rejected. Input bytes are checked again after execution.

Each author child retains 60 CPU seconds, 70 wall seconds and 2 GiB address
space. Each independent child retains 160 CPU seconds, 180 wall seconds and
2 GiB. Library thread variables are set to 1 cooperatively. Maintained replay
does not force CPU affinity or promise a one-core OS cap. Manifest max_cores
records the inherited allowed CPU count, not a new affinity restriction. The historical
one-core runs and their original identities are preserved unchanged.

## Verification and interpretation

Recorded scientific outputs agree across normal and -O execution on:

- Python 3.12.14, Clang 22.1.3; SymPy 1.14.0
- Python 3.13.5, GCC 14.2.0; SymPy 1.13.3

No claim of Python 3.13.9 testing is made. Full exact-library and executable
provenance, expected/observed values, commands, bounds and timings are retained
in `archive/evidence/schur_reduction_20261007/portable/`.

The adversarial suite checks root and nested-key injection, changed scientific
values/types/structure, malformed runtime/environment metadata, duplicate
JSON keys, bounded diagnostics, eight source-corruption targets, entry-point
source corruption in both optimizer modes, and an executing-child overwrite
of the expected reference. Its cached-reference test requires both scientific
mismatch and post-run source-change rejection. Mathematical failure branches
are independently forced during each full replay to verify they survive -O.

Maintained files are checked for trailing whitespace, missing EOF newlines and
extra EOF blank lines. One known extra EOF blank line is retained in the
lossless historical review validator, matching its original bytes; the review
itself explicitly records that difference from the author's validator.

Finite algebraic passes and source-integrity controls do not certify the
analytic proof in a proof assistant, prove the open N-limit, or independently
reprove inherited analytic inputs. The new curation is not a second external
review. Relocation checks establish portable execution only.
