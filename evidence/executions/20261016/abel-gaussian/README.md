# Execution and review scope

Base: `b425a36141cd81c7ef4e832984e7f7ff5074ddc7`. Date: 16 October 2026.

The maintained proofs are
[Abel rigidity](../../../../mathematics/abel_clock_rigidity_20261016.md) and
[flat Gaussian comparison](../../../../mathematics/gaussian_equal_edge_20261016.md).
Independent internal reviews and coordinator reconstruction are recorded
separately from the finite checks. No external referee certification is claimed.

`receipt.json` pins actual Python commands, time limits, output and source
hashes. Each child uses `python -O`; explicit exceptions keep checks active.
The Abel controls use mpmath at 60 decimal digits with stated tolerances;
the word, Fock and generic tensor controls use exact integer/rational arithmetic.
The optional C++ receipt records its actual compiler and bounded finite run.
The Monte Carlo result is exploratory, even though its sampled finite model
is exact. It is not an asymptotic proof.

`wolfram_result.json` preserves the actual connector output, including the
three zero symbolic residuals. The Wolfram source is committed with the Python
and C++ programs. `integration_checks.json` records metadata, links and receipt
pins for this partial pinned source snapshot; remote path existence is not
substituted for mathematical source bytes. `manuscript_checks.json` is a static
TeX include/citation/reference audit, not a PDF render or build.

No complete repository pytest, analytic Lean build, literal tau=10^-80
semiclassical experiment, deterministic signed comparison or BGS solution was
executed or certified in this checkpoint. The original TRACE-005 and BGS
terminal claims remain open.

## Remote CI observation

On scientific commit `658a3ebbf6f9c61084f27ac7d7aa37976a362657`, both
GitHub workflows concluded `failure`. The failed jobs had runner_id=0,
no runner name and empty step arrays; the downstream jobs were skipped.
The connector returned NOT_FOUND for the requested job log and did not expose
the annotations endpoint. The underlying cause is unknown here, so no billing
or source-code diagnosis is asserted. [Exact observation](remote_ci.json).
The local PASS receipts are valid within their stated scope; no successful
full remote CI, PDF build or Lean build follows from them.
