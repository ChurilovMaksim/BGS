# Working handbook

`STATUS.md` is the canonical claim index. This file says how to work in the rebuilt repository.

## Status vocabulary

- **PROVED** — analytic/formal statement with all load-bearing assumptions explicit.
- **REPRODUCED** — a computational identity/check rerun in the current tree.
- **NUMERICAL EVIDENCE** — finite computation supporting or falsifying a hypothesis.
- **OPEN GAP** — a missing analytic step blocks the claimed theorem.
- **ARCHIVED** — provenance only; not current authority.

## Active rank-1 chain

The current chain is `twisted-Jacobi kernel -> R82 reproduction -> exact k=2 reduction -> M1 open problem`.

The corresponding files are `code/math/twisted_jacobi.py`, `code/math/jacobi.py`, the three scripts under `code/verification/`, and `research/M1.md`.

## Verification

Run:

```bash
python code/maintenance/repo_health.py
python code/verification/baseline_r82.py
python code/verification/h3_k2_exact_reduction.py
python code/verification/theorem_ii_new_primes.py
```

The two very large Theorem-II designs are opt-in with `--all`.

## Experiments

`code/experiments/` contains current numerical spectral experiments. Their JSON outputs belong under `results/numerical/`. A passing statistical test is evidence, not an analytic theorem. Quarantined or superseded measurements belong under `results/historical-numerical/` or the full legacy archive.

## Formal layer

Lean sources are in `formal/Bgs/`. Generated `.lake/build` and package trees are not source and must not be committed into the active tree.

## Archive rule

If an old calculation becomes relevant, recover it from `archive/legacy-workspace/`, audit its assumptions and paths, and then promote a cleaned version into the active tree. Do not run the archive wholesale as if it were current code.
