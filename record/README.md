# Research record

`record/` is the status, governance, and provenance layer of the BGS research
programme.

## Authoritative living surface

- `claim_ledger.md` — sole repository-wide authority for current scientific status;
- `claims.json` — stable machine-readable IDs/cross-links for core load-bearing claims and programme obligations;
- `claim_registry.md` — generated human-readable view of that core registry;
- `scientific_dependencies.json` and `scientific_dependency_graph.md` — maintained theorem/programme DAG;
- `research_routes.md` — route-level advances, obstructions, and closure conditions;
- `retractions.md` — full false/superseded statements and failure mechanisms;
- `errata.json` — normalized correction IDs used to generate the reader-facing `../ERRATA.md`;
- `repository_conventions.md` — scientific repository governance;
- `generated_sources.json` — generated/publication source contracts;
- `mathematics_topics.json` — complete thematic classification of maintained proof notes;
- `branch_protection_policy.md` — intended canonical-branch review policy.

The dated `claim_ledger_addendum_20260907.md` is preserved as historical
source material. It no longer competes with the current consolidated
`claim_ledger.md`.

The dated review [`nonlinear_pressure_review_20260923.md`](nonlinear_pressure_review_20260923.md)
audits the classical pressure claim `BGS-FM-006` and its exact arithmetic;
the missing Heisenberg-time estimate retains its OPEN status.

## Historical record

Dated reviews document what was checked at a particular research state; they
cannot override the living status surface. A curated chronological view is in
[history/2026/INDEX.md](history/2026/INDEX.md).

Historical files remain at stable paths when moving them would break existing
provenance or manuscript references. New dated operational reviews should
normally be created under `history/YYYY/`.

## Execution boundary

Execution evidence is separated from source presence. A GitHub workflow ending
before any step executes (`steps=[]`, `runner_id=0`) is an infrastructure
non-run, not a scientific failure or pass. Likewise, the presence of a Lean
source does not establish compilation unless an actual build is recorded.

See `../SOURCE_OF_TRUTH.md` for the compact repository-wide authority order.
