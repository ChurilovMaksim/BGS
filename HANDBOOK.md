# Working handbook

`STATUS.md` is the canonical claim index.  This handbook defines how to use the **full** research workspace without confusing preserved experiments with current certificates.

## Status vocabulary

- **PROVED** — analytic/formal statement with every load-bearing assumption explicit and no unresolved admitted step.
- **REPRODUCED** — a computational identity/regression rerun in the current canonical code.
- **FINITE-N EXACT** — an exact statement about a stated finite design; not automatically uniform/asymptotic.
- **NUMERICAL EVIDENCE** — finite computation supporting or falsifying a hypothesis.
- **OPEN GAP** — a missing analytic step blocks the desired theorem.
- **INVALID / SUPERSEDED** — a route contains a demonstrated defect and cannot support downstream claims.
- **HISTORICAL** — retained provenance; not current authority.

## Trust layers

Use `STATUS.md`, `THEORY.md`, `research/`, `code/math/`, `code/verification/`, `code/experiments/`, `code/maintenance/`, `results/`, `inputs/`, and the explicitly described formal sources first.  These form the canonical layer.

The broader `code/{core,diagnostics,kloosterman,large_m,shape_automaton,sp4,theorems,utils}`, `data/`, `docs/`, and manuscript sources are the research corpus.  They are intentionally available in normal paths because they contain useful derivations, counterexamples, calibrations, and intermediate results.  A research-corpus `PASS` or `[PROVEN]` label is not enough to promote it.

`archive/legacy-workspace/`, `code/legacy_*`, old audit snapshots, and `paper/historical_snapshots/` are historical provenance.

## Current rank-1 chain

The surviving chain is

`twisted-Jacobi kernel -> R82 reproduction -> exact k=2 reduction -> independent new-prime regression -> numerical spectral evidence -> M1 open problem`.

The current analytic target is `research/M1.md`.  The historical Möbius-fiber theorem and the R86 trace-fluctuation shortcut are not valid bridges across this gap.

## Before committing

Run:

```bash
python code/maintenance/repo_health.py
python code/maintenance/audit_inventory.py
python code/verification/baseline_r82.py
python code/verification/h3_k2_exact_reduction.py
python code/verification/theorem_ii_new_primes.py
```

Run expensive numerical experiments separately and record whether an output is a fresh rerun or a retained historical result.  `results/verified/` is reserved for audited computational certificates; `results/numerical/` is current numerical evidence; `results/historical-numerical/` is quarantine/superseded evidence.

## Promotion workflow

To promote an old script/result into the canonical layer:

1. locate its original producer using `docs/audit/PRODUCER_PATH_MAP.md` and the historical record;
2. state exactly what mathematical object/statistic the script computes;
3. migrate old `src/` / `artifacts/` paths without rewriting the old result file itself;
4. check the comparison/reference distribution and all normalisations;
5. rerun it from current code with deterministic inputs where feasible;
6. give the output a trust label no stronger than the rerun establishes;
7. update `STATUS.md` only if a load-bearing claim genuinely changes.

Failed or superseded experiments should normally be preserved with an explicit reason rather than deleted.

## Formal layer

Lean sources live under `formal/Bgs/`.  `sorry`, `opaque` placeholders, or specification-only definitions must remain visible as open obligations.  Generated `.lake/build` and package trees are not source and must not be committed.

## Historical-text rule

Do not mechanically rewrite old ledgers, manuscript derivations, or historical JSON to make them look current.  Add an audit record or a current manifest entry instead.  The known mojibake in `docs/HISTORY_FULL_PRE_REBUILD.md` is recorded rather than silently rewritten in this structural sync; the audit contains a verified reversible repair method for a dedicated migration.
