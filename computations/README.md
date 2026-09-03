# Computations

The maintained computational surface is deliberately compact and independently
cross-checked. Historical language ports and exploratory work are not kept as
parallel source trees.

## C++20 — exact/exhaustive kernels

- `cpp/fourth_moment_pair_key_verifier.cpp` — independent implementation of
  the corrected pair-key geometry, coupling totals and finite fourth-moment
  factorization anchors.
- `cpp/cayley_energy_verifier.cpp` — exact mixed Cayley-energy verifier with
  generic and exceptional controls for `K=11,13` plus the explicit
  `(p,K)=(461,23)` non-uniformity witness.
- `cpp/cat_map_order.cpp` — exact order/split-prime utility and regression for
  the old Julia order/comment mismatch.

All `.cpp` files in this directory must appear in `CMakeLists.txt`;
`repository_audit.py` enforces that rule.

## Python — reference arithmetic, symbolic work and orchestration

`python/bgs/` contains checked finite-field, discrete-log, pair-key and
twisted-Jacobi primitives. Mathematical design metadata is validated rather
than treated as an annotation. In particular, `jacobi_matrix` accepts a
validated sub-sector of the annihilator (such as a parity sector) and rejects
characters outside it.

`verification/` contains the maintained gates:

- `current_regression.py` — fast exact anchors and fail-fast API contracts;
- `mixed_cayley_energy.py` — 720 matching systems, exact cyclotomic resultants
  for `K=11,13`, finite reduction checks and the `K=23` witness;
- `twisted_jacobi_regression.py` — current producer for preserved
  twisted-Jacobi finite regressions;
- `repository_audit.py` — whole-tree structure, language, duplicate, provenance,
  Lean-import and CMake-coverage checks.

`analysis/spectral_diagnostics.py` keeps the useful finite spectral experiments
with corrected semantics. It reports descriptive distances/statistics only; it
does not expose the old IID-KS or stationary-number-variance overclaims.

## Language policy

- **C++20:** expensive exact enumeration and independent finite verifiers.
- **Python:** symbolic/exact orchestration, transparent reference
  implementations and finite numerical analysis.
- **Lean 4:** formal finite certificates and falsifiers.
- **TeX:** the manuscript.
- **Fortran:** not currently justified by profiling; introduce it only for a
  genuine dense numerical hot path.
- **Julia:** **zero tracked `.jl` sources in the current branch.** Every useful
  historical Julia path is dispositioned in `../record/julia_migration.md`;
  original bytes remain available in Git history and the supplied snapshot.

The goal is not to maximize a language percentage. The goal is one maintained
implementation per scientific role, with independent checks where they buy
confidence.
