# WoW — BGS research workspace

This repository is the canonical working state for the BGS/cat-map research programme.  It is intentionally a **full research workspace**, not a minimal release package: useful experiments, diagnostics, finite-N identities, negative results, manuscript material, and provenance are preserved alongside a much narrower authoritative layer.

The authoritative current status is [`STATUS.md`](STATUS.md).  The current best non-error solution path starts in [`research/README.md`](research/README.md) and [`research/M1.md`](research/M1.md).  Historical theorem labels, old PDFs, old `PASS` fields, and run ledgers do not override `STATUS.md`.

## Current boundary of knowledge

The surviving rank-1 line consists of the twisted-Jacobi representation, R82 baseline reproduction, the exact checked `k=2` reduction, an independent direct-sum regression at new split primes, and substantial finite-N spectral evidence.  The load-bearing analytic M1 cross-twist assembly is still open.  General BGS is **not proved** by this repository.

The 2026-09-03 full sync also invalidated the old R86/R87 trace-fluctuation shortcut as stated: it applies a scalar binomial expansion to generally noncommuting matrices.  The document is preserved with an audit notice rather than deleted.

## Trust layers

**Canonical / audited:** `STATUS.md`, `THEORY.md`, `HISTORY.md`, `HANDBOOK.md`, `research/`, `code/math/`, `code/verification/`, `code/experiments/`, `code/maintenance/`, `results/`, `inputs/`, and the explicitly delimited formal sources.

**Research corpus:** `code/core/`, `code/diagnostics/`, `code/kloosterman/`, `code/large_m/`, `code/shape_automaton/`, `code/sp4/`, `code/theorems/`, `code/utils/`, `data/`, `docs/`, and `paper/`.  These contain valuable mathematics and experiments, but individual files may preserve old paths, hypotheses, or historical status words.

**Historical / quarantine:** `archive/legacy-workspace/`, `code/legacy_*`, old audit snapshots, `paper/historical_snapshots/`, and files specifically named in `STATUS.md` / manifests.

## Repository map

- `STATUS.md` — canonical claim/status map.
- `THEORY.md` — present-tense dependency graph and exact proof boundary.
- `research/` — active solution branch; M1 is the current analytic bottleneck.
- `code/` — canonical kernels/checks plus the restored research code corpus.  See `code/README.md`.
- `data/` — broad historical/research output corpus.  See `data/MANIFEST.md`.
- `results/` — status-controlled current/selected results.  See `results/README.md`.
- `docs/` — literature, reviews, plans, detailed historical theory, full ledger, and audit records.
- `formal/` — Lean source tree.  Generated `.lake` build/package state is intentionally excluded.
- `paper/` — manuscript/source corpus.  There is no current proof-complete BGS paper.
- `archive/legacy-workspace/` — full pre-rebuild audited workspace, retained as last-resort provenance.

## Full audit / synchronization records

The current whole-repository review is documented in:

- `docs/audit/full_repository_sync_2026-09-03.md` — human-readable audit and execution matrix;
- `docs/audit/FILE_INVENTORY_SUMMARY.json` — compact inventory summary; regenerate the full path-level inventory with `code/maintenance/audit_inventory.py`;
- `docs/audit/PRODUCER_PATH_MAP.md` — old `src/...` producer names mapped to current code where recoverable;
- `docs/audit/CLAIM_STATUS_MAP.md` — compact map of load-bearing, finite-N, numerical, open, and invalid routes;
- `docs/audit/HISTORY_ENCODING_REPAIR.json` — checksum/method record for the diagnosed historical-ledger mojibake.

## Reproduce the canonical computational core

Tested audit runtime: Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0.

```bash
python -m pip install -r requirements.txt
python code/maintenance/repo_health.py
python code/maintenance/audit_inventory.py
python code/verification/baseline_r82.py
python code/verification/h3_k2_exact_reduction.py
python code/verification/theorem_ii_new_primes.py
```

The matched number-variance experiment can be rerun separately with `code/experiments/number_variance_goe_control.py`.  The GOE spacing experiment is heavier; `results/numerical/bgs_spacing_goe.json` records per-design rerun provenance.  The old `N=95419` ratio-vs-spacing run is quarantined under `results/historical-numerical/`.

## Rule for future work

Preserve broadly, trust narrowly.  Do not delete an experiment merely because its interpretation changed; keep the raw result and state why it is superseded.  Promote an output into `results/verified/` only after the producer, assumptions, numerical object, normalisation, and comparison statistic are all explicit and reproducible.  Update `STATUS.md` only when the mathematical dependency graph genuinely changes.
