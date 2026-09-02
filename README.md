# WoW — BGS research workspace

This `main` is the canonical working state rebuilt on 2026-09-02. It is intentionally small at the active surface and complete at the provenance surface.

The shortest authoritative statement is [`STATUS.md`](STATUS.md). The current solution path is [`research/README.md`](research/README.md). Historical theorem labels, old PDFs and old run ledgers are evidence/provenance, not current status.

## Current boundary of knowledge

The best non-error rank-1 line currently consists of:

1. the twisted-Jacobi representation and R82 baseline reproduction;
2. the exact `k=2` fluctuation reduction, including `|P|=(K-1)(K-2)`;
3. numerical GOE/rigidity evidence in the desymmetrised sector;
4. an unresolved analytic M1 step controlling the full twist-summed energy.

M1 is **OPEN**. General BGS is **not proved** by this repository.

## Repository map

- `STATUS.md` — canonical claim status.
- `THEORY.md` — current dependency graph only.
- `research/` — active solution branch and the precise M1 target.
- `code/math/` — small load-bearing mathematical kernels.
- `code/verification/` — checks that are allowed to act as current certificates.
- `code/experiments/` — numerical experiments; results are evidence, not proofs.
- `results/verified/` — outputs of the current verified checks.
- `results/numerical/` — retained numerical spectral evidence.
- `results/historical-numerical/` — useful old measurements whose interpretation was superseded or quarantined.
- `inputs/r82-legacy/` — read-only preserved inputs needed to reproduce the R82 baseline.
- `formal/` — Lean sources.
- `docs/audit/` — review/audit records relevant to the current reset.
- `archive/legacy-workspace/` — the entire pre-rebuild workspace, byte-for-byte by Git tree reference. Do not use it as the default source tree.
- `paper/` — no active proof-complete paper at present.

## Reproduce the audited core

Tested rebuild runtime: Python 3.13.5, NumPy 2.3.5, SymPy 1.14.0.

```bash
python -m pip install -r requirements.txt
python code/maintenance/repo_health.py
python code/verification/baseline_r82.py
python code/verification/h3_k2_exact_reduction.py
python code/verification/theorem_ii_new_primes.py
```

The last command defaults to the two practical audited designs. Use `--all` only when you intentionally want the two very large historical designs.

## Rule for future work

New research belongs in the active tree only when its assumptions and output semantics are clear. A failed proof attempt or superseded experiment is moved to `archive/` rather than left beside current certificates. Numerical evidence must remain labelled numerical until the analytic step it is meant to support is actually proved.
