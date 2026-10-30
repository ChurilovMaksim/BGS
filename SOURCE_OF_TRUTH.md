# Source of truth

This file is the short operational map. Detailed policy is in
`docs/repository_conventions.md`.

When surfaces disagree, resolve them in this order:

1. `record/claims.json` — the primary machine-readable registry of stable claim IDs, links and statuses (`state`) for core load-bearing claims and programme obligations.
2. `record/claim_registry.md` — the generated complete per-claim human-readable surface of `claims.json`; it covers every registered claim and is regenerated and checked from the registry, not edited by hand.
3. `record/claim_ledger.md` — a dated narrative interpretation of current scientific status and scope. It does not override the registry: a claim or status absent from the ledger is not thereby absent from the registry.
4. authoritative proof sources in `mathematics/`.
5. exact external dependency records in `literature/external_dependencies.json`.
6. formal kernels in `formalization/`, within their stated trust boundary.
7. maintained verification sources in `computations/`.
8. promoted evidence in `evidence/`.
9. `manuscript/BGS_unified.tex` and publication candidates in `papers/`.
10. dated historical reviews and Git history.

The `ledger_status` field stored per claim in `record/claims.json` is a
historical free-text transcription of ledger wording. It is not a
machine-checked mirror of `record/claim_ledger.md` (an audit on
30 October 2026 found only 31 of its 266 values verbatim in the ledger;
the 29 October 2026 audit found 29 of its then-232 values)
and must not be used as a synchronisation check between the two files.

The manuscript is publication-facing exposition, not an independent authority
that can strengthen a theorem. Evidence records cannot strengthen the
asymptotic scope of the proof they accompany. Historical files cannot override
a later correction.

The fixed-strength microscopic BGS claim is currently OPEN.
