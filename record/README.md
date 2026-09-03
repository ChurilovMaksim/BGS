# Research record

`record/` preserves information needed to audit how the current mathematics was obtained. It is not a second active source tree.

## Authoritative record files

- `claim_ledger.md` — status of every current or historically important claim.
- `retractions.md` — explicit false/superseded statements and mechanisms.
- `reconstruction.md` — reconstruction and completeness policy.
- `julia_migration.md` — disposition of all historical Julia paths.
- `inventory_snapshot.py` — reproducible ZIP inventory/hashing tool.
- `checkpoints/` — exact pre-consolidation status/index/theory snapshots.
- `engineering/` — migration notes and historical computational diagnostics.
- `formal_drafts/` — useful formal drafts that are not part of the active Lean library.
- `corpus/` — broad historical source/data/manuscript corpus.

## Trust boundary

`record/corpus/` and `record/checkpoints/` are provenance. Their old labels (`[PROVEN]`, theorem numbers, `PASS`, etc.) are historical text, not current status. Promotion requires an explicit entry in `claim_ledger.md` and, where applicable, a current derivation or reproducible certificate.

Exact old Git tree/blob objects are reused where preservation matters, so moving material into the record does not rewrite its contents.

Files unrelated to the cat-map research programme (for example historical LLM benchmark comparisons accidentally bundled into the workspace) are not kept in the current branch. They remain recoverable from Git history but are not research provenance for this project.
