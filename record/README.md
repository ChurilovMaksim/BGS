# Research record

`record/` is a compact provenance and status layer, not an archive source tree.

See [the final handoff](final_research_handoff_20260921.md) for the integrated
20--21 September state and
[the verified-state reconciliation](verified_state_reconciliation_20260921.md)
for the later forensic recovery of the 14--16 September BGS working dossiers.
The earlier [recovery audit](recovery_audit_20260920.md) remains the preceding
checkpoint, not the final status authority.

## Authoritative living status files

- `claim_ledger.md` — repository-wide claim status, including the September 20--21 recovery and repaired Heisenberg direct-attack layer;
- `claim_ledger_addendum_20260907.md` — authoritative dated extension for later/corrected September 7 scopes; it wins over older prose in those scopes;
- `research_routes.md` — route-level log of advances, obstructions and closure conditions; status still comes from the ledgers above;
- `retractions.md` — false/superseded statements and failure mechanisms;
- `verified_state_reconciliation_20260921.md` — selective promotion/quarantine map for the recovered v7--v11 and 16 September working state; historical `[PROVEN]` labels outside this reconciliation are not current authority;
- `final_branch_reconciliation_20260921.md` — final all-branch / early-artifact preservation audit before promotion to `main`; records why diverged legacy workspaces are preserved by refs rather than re-vendored;
- `session_science_sync_20260907.md` — late-session byte/readback and rerun audit;
- `session_integrity_audit_20260907.md` — repeated cross-layer integrity audit after synchronization;
- `reconstruction.md` — source-snapshot inventory and Git preservation boundary;
- `julia_migration.md` — path-complete disposition of historical Julia files;
- `inventory_snapshot.py` — deterministic inventory/hash tool for a supplied ZIP when locally available.

Dated review files under `record/` document narrower theorem/evidence scopes; they do not override the claim ledgers unless explicitly incorporated by the dated addendum.

Historical `corpus/`, `checkpoints/`, `engineering/` and `formal_drafts/` trees were removed from the current branch because they duplicated Git-preserved history and made obsolete source look current. Historical bytes remain recoverable from Git; they carry no authority over the current ledgers.

Execution evidence is separated from source presence. A GitHub workflow ending before any step executes (`steps=[]`) is an infrastructure non-run, not a scientific failure or pass. Likewise the presence of a Lean source does not establish compilation unless an actual build is recorded.
