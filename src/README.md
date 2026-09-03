# Computational sources

Only code that supports the active scientific state is kept here.

- `python/bgs/` contains readable reference implementations of finite-field arithmetic, key geometry and twisted Jacobi sums.
- `cpp/m1/` contains the performance-critical exhaustive M1 diagnostic.
- `cpp/verification/` contains an independent exact fourth-moment verifier.

Historical Julia programs and unrelated migration experiments are not kept in the active tree; Git history preserves them.

Language policy:

- **Python** for symbolic/exact orchestration, readable reference implementations, analysis and plotting;
- **C++20** for combinatorial enumeration, exhaustive finite-field search and independent high-performance verification;
- **Fortran** only when profiling identifies a dense array-oriented numerical kernel for which it is materially superior;
- **Lean** for theorem statements and finite/combinatorial formal verification.

A language rewrite is promoted only after regression against preserved mathematical anchors.