# Code map

The code tree contains both the canonical audited layer and the broader research corpus.

## Canonical layer

- `math/` — load-bearing mathematical kernels used by current checks.
- `verification/` — current reproducibility/identity/regression checks.
- `experiments/` — current numerical spectral experiments. Their outputs are evidence, not proofs.
- `maintenance/` — repository health gate.

These directories must use current paths and are the default starting point for new work.

## Restored research corpus

- `core/` — cat-map quantisation and core constructions.
- `diagnostics/` — diagnostic, falsifier and calibration scripts.
- `kloosterman/` — subgroup/Kloosterman explorations.
- `large_m/` — large-m moment, spectral and M1/M2 investigations.
- `shape_automaton/` — shape/word/automaton investigations.
- `sp4/` — rank-2/Sp4 experiments.
- `theorems/` — theorem-oriented computational derivations.
- `utils/` — supporting utilities.
- `llm/` — local research-assistance helpers retained from the workspace.

All restored Python sources are required to remain syntactically valid, but many scripts predate the `src -> code` and `artifacts -> data/results` migration. A stale path in one of these research directories is a migration task, not evidence that the mathematical experiment should be deleted.

## Historical code

- `legacy_verification/` — pre-rebuild verification scripts, including checks later superseded or quarantined.
- `legacy_maintenance/` — pre-rebuild one-off repository/ledger maintenance scripts.

Do not use a historical script as a certificate without first porting it to current paths, checking the statistic it computes and reproducing its output.