# Supported C++20 components

This directory contains the small set of performance-critical or independently verifying components for which C++ is preferable to the repository's Python research layer. It is not a mandate to translate analysis, plotting, symbolic derivations, or orchestration code into C++.

## Components

- `m1/cross_term_energy.cpp` — canonical producer for the finite M1 historical-Mobius-vs-pair-key diagnostic. The old heavy Python producer was retired after the C++ implementation reproduced the preserved `N=53,K=13` and `N=199,K=11` anchors. It uses `long double` complex arithmetic and direct circular convolutions/DFTs to keep the finite diagnostic transparent.
- `number_theory/catmap_order.cpp` — cat-map matrix-order and prime-scan work consolidated from useful historical Julia utilities, with the old full-order/projective-order naming ambiguity removed.
- `shape/relation_automaton.cpp` — exact arbitrary-precision relation dynamic program replacing the useful corrected Julia Run-82/shape-automaton stack. Requires Boost.Multiprecision headers (`libboost-dev` on Ubuntu/Debian).
- `verification/fourth_moment_factorization.cpp` — independent exact C++ verifier for the pair-key fourth-moment factorization; its duplication of the Python verifier is intentional because implementation independence is part of the certificate.

## Build discipline

CI compiles every supported executable with C++20 and strict warnings:

`g++ -std=c++20 -O2 -Wall -Wextra -Wpedantic -Werror ...`

The repository health workflow also runs each component's deterministic regression/verification mode. A new C++ component should be added only when at least one of these is true:

1. a profiled finite-field/exhaustive kernel is materially cheaper in C++;
2. arbitrary-precision or low-level data structures materially simplify an exact computation;
3. an independent implementation is scientifically useful as a verification certificate.

Do not keep a second active Python implementation after migration unless that independence is itself useful scientifically. Historical producers remain recoverable through Git history and, where applicable, the immutable legacy snapshot.

For migration rationale and preserved anchors, see `research/engineering/language_migration.md`, `research/engineering/performance_migration.md`, and the relevant files under `results/`.
