# Source of truth

This file is the short operational map. Detailed policy is in
`record/repository_conventions.md`.

When surfaces disagree, resolve them in this order:

1. `record/claim_ledger.md` — current scientific status and scope.
2. `record/claims.json` — stable machine-readable IDs and links for core load-bearing claims and programme obligations; it is intentionally not a replacement for the full ledger.
3. authoritative proof sources in `mathematics/`.
4. exact external dependency records in `literature/external_dependencies.json`.
5. formal kernels in `formalization/`, within their stated trust boundary.
6. maintained verification sources in `computations/`.
7. promoted evidence in `evidence/`.
8. `manuscript/BGS_unified.tex` and publication candidates in `papers/`.
9. dated historical reviews and Git history.

The manuscript is publication-facing exposition, not an independent authority
that can strengthen a theorem. Evidence records cannot strengthen the
asymptotic scope of the proof they accompany. Historical files cannot override
a later correction.

The fixed-strength microscopic BGS claim is currently OPEN.
