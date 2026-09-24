# Computations

The maintained computational surface is deliberately compact and independently cross-checked. Historical language ports, one-shot publication migrators, and exploratory branch source trees are not kept as parallel implementations on `main`.

## C++20 — exact/exhaustive kernels

`cpp/` contains the independent exact finite verifiers, including the Cayley energy/resultant kernels, Pell relation/orthogonality checks, fixed-strength locality checks, hyperbolic-period checks, and the noncommuting return-word certificate. Every tracked `.cpp` file must occur in `CMakeLists.txt`; `repository_audit.py` enforces that invariant.

## Python — checked arithmetic and orchestration

`python/bgs/` contains the maintained finite-field, discrete-log, pair-key and twisted-Jacobi primitives with fail-fast validation.

`verification/` contains the scientific gates and exact/finite regressions.
[`nonlinear_pressure_variance.py`](verification/nonlinear_pressure_variance.py)
independently assembles the physical symbol and checks the exact rational
Fourier variance for `BGS-FM-006`; its finite arithmetic does not prove
the pressure theorem.
`verification/scientific_registry_audit.py` checks the machine-readable claim,
dependency, paper, evidence, environment, and topic contracts before expensive
science runs. `maintenance/render_claim_registry.py --check` prevents the
human claim index from drifting from `record/claims.json`.
`maintenance/verify_workspace.py` orchestrates scientific Python/C++
execution without mutating committed evidence. `maintenance/build_unified_manuscript.py`
is the sole maintained consolidated-manuscript builder.

`maintenance/sync_return_sections.py` is the maintained Markdown-to-TeX
synchronizer for the six return-law chapters. It transforms document links
through the Pandoc syntax tree so mathematical brackets are not rewritten as
links. `--check` detects stale generated source.

For focused execution, repeat `verify_workspace.py --only NAME`; the
[reproduction guide](../REPRODUCE_unified.md) gives the return-law selection.
Focused execution is recorded in the manifest and does not claim full coverage.

The return-local-limits verifier checks exact rational window probabilities
for simple spectral clouds, including an independent brute-force enumerator.
Separate floating and symbolic controls check density transport, its origin
Jacobian, and free Brownian support-gap calculus. The Wolfram cross-check is
retained in [return_gap.wl](verification/return_gap.wl); the full Python
entry point is [return_local_limits.py](verification/return_local_limits.py).
Neither program proves weak process convergence or the analytic return law.

One-shot scripts that used to integrate research branches into older standalone papers have been retired from `main`; their history remains in Git. New scientific work should change the canonical source/verifier directly rather than regenerate superseded article copies.

`analysis/spectral_diagnostics.py` and the figure scripts retain useful finite numerical experiments with corrected semantics. Their outputs are descriptive/regression evidence and are not promoted to asymptotic or microscopic BGS theorems.

## Language policy

- **C++20:** expensive exact enumeration and independent finite verifiers.
- **Python:** symbolic/exact orchestration, transparent reference implementations and finite numerical analysis.
- **Lean 4:** formal finite certificates and falsifiers.
- **TeX:** the single consolidated manuscript source.
- **Fortran:** introduce only if profiling identifies a genuine dense numerical hot path that materially benefits from it.
- **Julia:** retired; zero tracked `.jl` sources and no tracked Julia project environment.

The goal is not a language percentage. It is one maintained implementation per scientific role, with independent checks where they materially increase confidence.
## Recovered fixed-map computations

The source and historical finite evidence for the fixed-map continuation
are indexed in [the supplement](../supplement/fixed_map/README.md).
Run `python computations/maintenance/verify_fixed_map_supplement.py` from
the root for inventory/syntax checks and 28 isolated replays. The runner
keeps generated outputs under `build/` and does not overwrite evidence.
This complements the existing whole-workspace runner.

The late 20--21 September continuation also has a compact exact regression
gate at `verification/bgs_20260921_regression.py`.  It checks the
three-orientation algebra, Fourier-line recurrence identities, the frozen
full-symbol variance, and the local-jet negative control.  It is included
automatically in a complete `verify_workspace.py` run.  Its scope is exact
finite/symbolic regression only, not proof of the analytic asymptotic
theorems or fixed-`tau` BGS.

The 23 September verifiers `frozen_full_lag_gap.py` and
`frozen_kick_rank.py` check the exact physical-symbol expansion and finite
Jacobi/rank diagnostics, respectively. Both are discovered by the whole-
workspace runner and write scoped JSON outputs under its log directory.
Their finite runs are not proofs of the infinite-lag or all-dimension claims.

The submitted article's three retained 24 September checks are
[`frozen_seven_cut.py`](verification/frozen_seven_cut.py),
[`frozen_total_minors.py`](verification/frozen_total_minors.py), and
[`frozen_antireversor.py`](verification/frozen_antireversor.py).
They replay finite geometry, 5-adic/Fourier subset arithmetic, and an
exhaustive integer cyclotomic certificate, respectively. All are included
in the full verification runner, have dated immutable reference outputs
under `evidence/20260924/`, and are available as focused selections.
The analytic and all-dimension steps are documented separately in
[`record/submitted_article_review_20260924.md`](../record/submitted_article_review_20260924.md).
