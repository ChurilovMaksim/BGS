# Research record

`record/` is now a **compact provenance and status layer**, not an archive
source tree.

Authoritative living files:

- `claim_ledger.md` — repository-wide status of current and historically
  important claims;
- `retractions.md` — false/superseded statements and their failure mechanisms;
- `reconstruction.md` — source-snapshot inventory and Git preservation
  boundary;
- `julia_migration.md` — path-complete disposition of all 31 historical Julia
  files;
- `inventory_snapshot.py` — deterministic inventory/hash tool for the supplied
  ZIP when that ZIP is available locally.

The old `corpus/`, `checkpoints/`, `engineering/` and `formal_drafts/` trees
were removed from the current branch on 2026-09-03. They duplicated material
already preserved by Git and made obsolete Julia/Python/TeX/Lean code look
current to both humans and GitHub Linguist.

The last `main` commit before that cleanup is
`d0e414ec26ff7e43ad59e80f77c9d8c679e87c4b`. Historical bytes remain
recoverable from Git history; they carry no authority over the current claim
ledger.
