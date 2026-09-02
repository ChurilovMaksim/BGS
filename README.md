# WoW — BGS research workspace

This repository is the canonical working state for the BGS/cat-map research programme. It is intentionally **complete enough for continued research**, not a minimal release package.

The authoritative current-status file is [`STATUS.md`](STATUS.md). The current best non-error solution path is [`research/README.md`](research/README.md). Historical theorem labels, old PDFs, exploratory scripts and old run ledgers are retained because they contain useful mathematics and experiments, but they do not override `STATUS.md`.

## Current boundary of knowledge

The best audited rank-1 line currently consists of:

1. the twisted-Jacobi representation and R82 baseline reproduction;
2. the exact `k=2` fluctuation reduction, including `|P|=(K-1)(K-2)`;
3. an independent scalar-sum regression check of twisted-Jacobi matrix elements at new split-prime designs;
4. substantial finite-N numerical evidence in the desymmetrised sector;
5. an unresolved analytic M1 step controlling the full twist-summed energy.

M1 is **OPEN**. General BGS is **not proved** by this repository.

## Trust levels

There are three deliberately different layers.

**Canonical / audited.** `STATUS.md`, `research/`, `code/math/`, `code/verification/`, `code/maintenance/`, `results/verified/` and the immutable inputs in `inputs/`. These are the files to use first when continuing the proof programme.

**Research corpus.** `code/core/`, `code/diagnostics/`, `code/kloosterman/`, `code/large_m/`, `code/shape_automaton/`, `code/sp4/`, `code/theorems/`, `code/utils/`, `data/`, `docs/literature/`, `docs/review/`, `paper/sections/` and related files. These contain useful derivations, experiments, diagnostics and intermediate results. They are retained for active research, but individual files may use older paths or assumptions and must be checked before being promoted to a certificate.

**Historical / quarantined.** `archive/legacy-workspace/`, `code/legacy_verification/`, `code/legacy_maintenance/`, `paper/historical_snapshots/` and specifically identified superseded results. These are provenance and raw material, not current theorems.

## Repository map

- `STATUS.md` — current claim status; overrides historical labels.
- `THEORY.md` — current dependency graph and proof boundary.
- `research/` — current solution branch, starting with the exact M1 gap.
- `code/math/` — load-bearing mathematical kernels.
- `code/verification/` — current finite-N regression and identity certificates.
- `code/experiments/` — current numerical experiments.
- `code/{core,diagnostics,kloosterman,large_m,shape_automaton,sp4,theorems,utils}/` — restored research code corpus.
- `data/` — restored research outputs, diagnostics, moments, spectral data, rank-2/Sp4 results and legacy reference inputs. See `data/MANIFEST.md`.
- `results/verified/` — audited outputs of the current checks.
- `results/numerical/` — numerical evidence retained in the canonical layer.
- `results/historical-numerical/` — explicitly superseded/quarantined numerical records.
- `docs/` — current planning plus literature, reviews, audit material, detailed historical theory and run records.
- `formal/` — Lean sources and project files; generated `.lake/build` and dependency caches are intentionally excluded.
- `paper/` — manuscript source corpus. Historical proof-complete labels are not authoritative; see `paper/README.md`.
- `archive/legacy-workspace/` — complete pre-rebuild audited workspace, kept as a last-resort provenance snapshot.

## Reproduce the audited core

Tested rebuild runtime: Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0.

```bash
python -m pip install -r requirements.txt
python code/maintenance/repo_health.py
python code/verification/baseline_r82.py
python code/verification/h3_k2_exact_reduction.py
python code/verification/theorem_ii_new_primes.py
```

The health gate validates the canonical layer strictly and compiles the restored research Python corpus. Older research scripts are not required to satisfy current path conventions until they are promoted back into the canonical layer.

## Rule for future work

Do not delete an experiment merely because its interpretation was superseded. Preserve it with an explicit status. Promote a result to `results/verified/` only when the producing code, assumptions, numerical object and comparison statistic are all clear. A failed proof remains useful provenance but must never be cited as an active theorem.