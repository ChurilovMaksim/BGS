# Schur continuation evidence, 11 October 2026

This packet belongs to [the reviewed continuation](../../../../record/cavity_continuation_20261011.md)
from main `4c2afe539ff6b84be907899b38c8e80f94f547e8`. Analytic reconstruction,
finite computation and repository acceptance have separate scopes.

## Analytic review inputs

[review.json](review.json) binds the three independently reconstructed inputs:

- [All-fixed-moment candidate](inputs/all_moment_delay_bootstrap_candidate.md):
  `2b0f8c651ed6e15d803e6af3b0a32c9f712bcb1a28653a74b2ef56afb2be8019`.
- [Censoring/gap draft](inputs/schur_censoring_gap_review_input.md):
  `73cc587de1bfaf5d724fcbbe93c3a236da721fe0e05623f4f20d448177082ea7`.
- [Second/third extension](inputs/second_third_delay_review_input.md):
  `34602f2fca944cc45f4e7d91c081ff30dba837f5b2391e59bfe1f6357362b2cd`.

The maintained proofs include the editorial clarifications from those
reviews. A reviewed byte hash identifies an input, not formal proof-checking.
No external referee or novelty certification is claimed.

## Actual finite executions

| Receipt | Actual result | Scope |
|---|---|---|
| [Python v2 manifest](python-controls-guarded/manifest.json), [results](python-controls-guarded/results.json) | 140 cases, 700 exact lift identities; 19,548 exact clock words; 24 floating unitary diagnostics | Exact finite algebra and separate float64 diagnostics |
| [C++ compile/run receipt](cpp-controls/execution.json), [results](cpp-controls/results.json) | 144 different cases, 720 exact lift identities; fresh source-bound compilation | Exact arbitrary-precision rational algebra |
| [Wolfram receipt](wolfram_execution.json) | Four symbolic checks returned True | Finite identities, with real z in the correction term |

The Python v2 manifest pins four declared inputs and records actual wall,
per-process CPU and memory limits. Its validator has passed against the
current sources. The C++ receipt pins the freshly compiled source, compiler,
executable and outputs. Neither is an asymptotic theorem certificate.

The current Lean module count remains 23, with 26 Lake jobs in the preceding
accepted build; no analytic Schur theorem has been newly formalized.

## Reproduction

From the repository root, with SymPy and NumPy available:

```sh
python3 computations/verification/schur_censoring_and_clock.py
python3 computations/verification/chat_20261011/audit_tools/validate_manifest.py evidence/executions/20261011/cavity-continuation/python-controls-guarded/manifest.json --root .
cmake --build build --target schur_censoring_energy_verifier
./build/schur_censoring_energy_verifier
```

Configure the build as documented in [REPRODUCE](../../../../REPRODUCE_unified.md)
if needed. The Wolfram source is
[schur_censoring_20261011.wl](../../../../computations/wolfram/schur_censoring_20261011.wl).
New executions should write new receipts; retained outputs are not rerun
claims. The prior complete 217-verifier/24-target acceptance belongs to the
[preceding packet](../chat-research/fresh/README.md).

## Corrected verification-policy failure

The first 236-test maintenance run rejected the new Python verifier because
its optimization guard followed standard-library imports. The guard already
rejected optimized execution, but did not satisfy the repository's stricter
entry policy. It was replaced by the canonical before-import guard. The
[previous source](inputs/python_before_guard_policy.py) and original
`python-controls` run remain retained; that receipt identifies the preceding
source bytes and is not current-source validation. The fresh
`python-controls-guarded` receipt validates the corrected source. The finite
mathematical algorithms were unchanged.

## Manuscript and maintenance acceptance

The [fresh manuscript manifest](manuscript/build_manifest.json) records an
actual three-pass **285-page** build with unchanged TeX inputs, no horizontal
overflow and no missing references or citations. Its
[selected visual review](manuscript/visual_review.json) covers only pages
280 and 281, containing the new conditional theorems. PDF and page images
remain reproducible build outputs; unedited TeX logs are retained here.

The [maintenance result](maintenance/result.json) retains both the original
policy failure and the corrected **236-test** pass, with unedited logs.
The corrected source is pinned by the fresh guarded Python manifest above.

The [fresh focused workspace report](workspace/focused_outcomes.json) passed
both newly added verifier entries with identical before/after source hashes.
It records prebuilt CMake executable hashes; the separate C++ receipt provides
actual source-to-binary compilation provenance. The
[repository check](repository_check.json) also records a fresh rehash of all
199 preceding original inputs, the 124-claim/46-reference audit, generated
claim-table agreement and the 416 bibliographic mutation controls. Remote
exact-commit CI is a separate final check; historical 217-check receipts are
not used as acceptance of these new sources.
