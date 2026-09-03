# Research record

This directory is the provenance and audit layer. It is intentionally broader
than the active theorem surface.

Start with:

1. `reconstruction.md` — what was recovered from the ZIP and Git history;
2. `claim_ledger.md` — current status of scientific claims;
3. `retractions.md` — routes that must not silently return;
4. `julia_migration.md` — all 31 historical Julia paths and their disposition;
5. `ledger.md` — detailed research ledger retained from the broad reconstruction.

`corpus/` contains the browsable historical research corpus: code, data,
documents, inputs and experiments. It includes successes, intermediate work,
negative results and obsolete APIs. It is evidence/provenance, not a theorem
namespace.

`inventory_snapshot.py` deterministically inventories the external `BGS.zip`
by path, byte size and SHA-256 when that snapshot is available locally.
