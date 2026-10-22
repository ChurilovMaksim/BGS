# First-seven extension integration, 6 October 2026

Base: `66724291b2ec77c22823f52ecc5ee56278fed096`. This pass integrated
only the accepted first unramified seven-primary extension. It did not
commit or publish, and includes no later ramified candidate.

FM-024 now covers scalar complex joint commutant of the actual pair for
odd N>7 with 7|N and 5∤N, retaining both separately reviewed component proofs.
The combined odd N>=3,35∤N,N≠7 consequence explicitly uses prior FM-008's
simple-A/nonzero-M-entry theorem and preserves its review boundary. The
algebraic-entry literal-U corollary is extended by the existing coefficient
separation argument; no scalar full complex U commutant or seven-divisible
spectral simplicity is asserted. FORMAL-003 remains unchanged.

The accepted proof and fresh independent review hashes are preserved in
`first_seven_promotion_mapping.json`, together with the original 29-input
manifest. The sole data payload is the 241,060-byte reviewed serialization;
large duplicate development JSON datasets and executables are not installed.
Normal and optimized replay each rebuild all 17,046 determinant evaluations,
field/gcd/Bezout/root-order checks, six dictionary controls and actual residue
controls at N=7,21,63. The latter controls alone are not the uniform proof.

The optimized replay compiles with NDEBUG. Explicit failures, silent imports,
source-output rejection and data-tampering rejection passed. Five malformed
C++ inputs were rejected. The full maintenance suite passed 46 tests both
normally and under optimized Python. Registry, 317 bibliography mutation
controls, repository/text/assertion guards, registry/errata rendering, all
three pinned-Pandoc synchronization guards, and diff whitespace checks passed.
A separate explicit scan checked every newly created and modified text file,
including untracked files; existing untouched legacy files were not relabeled
clean. Final test receipts are in the external first-seven validation run.

The conservative FM-008 dependency adds one inherited external reachability
edge to FM-024. The explicit bibliography impact review records it without
altering any old source observation, locator, hash or applicability status.

Whole-workspace replay, manuscript compilation, supplement checks, remote CI,
commit and publication remain separate final gates owned by the parent.

## Subsequent execution acceptance

The frozen 1,888-file archive passed all 179 workspace checks and 28
supplement entries. The manuscript passed its three-pass warning/reference
gate at 266 pages; pages 262–264 were visually inspected. Existing 22 corpus
C++ binaries were source/hash-bound for 23 actual executions. No new Lean
build was run: unchanged inputs and the prior successful build log were
verified. The new first-seven verifier separately compiles its own helpers.

[Compact validation evidence](../evidence/executions/20261006/first-seven-validation/receipt.json)
is an explicitly post-run, evidence-only append, not part of its own tested
snapshot. The original CMake-PATH preflight failure is preserved; the rerun
used the same source snapshot with verified local tools and no source repair.
The exact index/record append delta is in first_seven_postrun_evidence_delta.json.
No ramified candidate, noise identity, commit or publication is included here.
