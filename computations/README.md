# Computations

The maintained computational surface is deliberately compact and independently cross-checked. Historical language ports, one-shot publication migrators, and exploratory branch source trees are not kept as parallel implementations on `main`.

## C++20 — exact/exhaustive kernels

`cpp/` contains the independent exact finite verifiers, including the Cayley energy/resultant kernels, Pell relation/orthogonality checks, fixed-strength locality checks, hyperbolic-period checks, and the noncommuting return-word certificate. Every tracked `.cpp` file must occur in `CMakeLists.txt`; `repository_audit.py` enforces that invariant.

## Python — checked arithmetic and orchestration

`python/bgs/` contains the maintained finite-field, discrete-log, pair-key and twisted-Jacobi primitives with fail-fast validation.

`verification/` contains the scientific gates and exact/finite regressions. `maintenance/verify_workspace.py` orchestrates their execution and the C++ verifier surface without mutating committed evidence. `maintenance/build_unified_manuscript.py` is the sole maintained manuscript builder.

`maintenance/sync_return_sections.py` is the maintained Markdown-to-TeX
synchronizer for the six return-law chapters. It transforms document links
through the Pandoc syntax tree so mathematical brackets are not rewritten as
links. `--check` detects stale generated source.

For focused execution, repeat `verify_workspace.py --only NAME`; the
[reproduction guide](../REPRODUCE_unified.md) gives the return-law selection.
Focused execution is recorded in the manifest and does not claim full coverage.

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
