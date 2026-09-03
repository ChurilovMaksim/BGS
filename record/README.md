# Research record

`record/` preserves information needed to audit how the current mathematics was obtained. It is not a second active source tree.

## Living record files

- `claim_ledger.md` — authoritative status of current and historically important claims.
- `retractions.md` — false/superseded statements, methodological corrections and failure mechanisms.
- `reconstruction.md` — preservation policy and completeness boundary.
- `julia_migration.md` — path-complete disposition of all 31 historical Julia files.
- `inventory_snapshot.py` — deterministic inventory/hash tool for the supplied ZIP.
- `engineering/historical_cpp/` — useful C++ ports/falsifiers that are intentionally outside the active build.
- `formal_drafts/` — useful formal drafts that are intentionally outside the active Lean library.

## Non-living provenance

- `checkpoints/` — exact pre-consolidation ledgers/status/theory/editorial snapshots. They may contain obsolete paths and overclaims by design; do not edit them into apparent currency.
- `corpus/` — broad historical source/data/manuscript/review material needed for archaeology, producer recovery, negative controls and future migration.

## Trust boundary

Only the living record files above describe the current project. Old labels such as `[PROVEN]`, `PASS`, `final`, theorem numbers, and obsolete directory names inside `checkpoints/` or `corpus/` are historical data, not current status.

Files unrelated to the arithmetic cat-map programme are not retained in the current branch merely because they were bundled into an old workspace. Scientifically useful false files are retained only when their failure mechanism matters for regression or provenance.
