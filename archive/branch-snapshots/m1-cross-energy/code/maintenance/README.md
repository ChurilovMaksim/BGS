# Maintenance and audit gates

`repo_health.py` is the fast non-mutating gate for the current repository.  It verifies the presence of the canonical and restored research layers, rejects generated build/cache files, compiles all Python sources, enforces current paths only in canonical runtime code, parses the JSON corpus, and checks quarantine/status sentinels such as the invalid `N=95419` result and the superseded trace-fluctuation route.

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python code/maintenance/repo_health.py
```

`audit_inventory.py` regenerates the full on-demand `docs/audit/FILE_INVENTORY.generated.json` with path, size, SHA-256 digest, trust layer, duplicate relationship, and migration/status sentinels:

```bash
PYTHONDONTWRITEBYTECODE=1 python code/maintenance/audit_inventory.py
```

The generated full inventory is ignored by Git; the checked-in `docs/audit/FILE_INVENTORY_SUMMARY.json` records the synchronization snapshot.  The inventory is descriptive, not a mathematical certificate.

Old `src/`, `artifacts/`, `LEDGER.md`, and similar strings are allowed in the research/historical corpus because mutating provenance would be worse than preserving migration debt.  They are not allowed in current canonical runtime code.

Pre-rebuild one-off maintenance scripts are preserved in `code/legacy_maintenance/`; do not treat them as current gates.
