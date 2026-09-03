# Computations

The supported implementation layer is intentionally small.

- `python/` — reusable exact/symbolic and matrix-element routines.
- `cpp/` — performance-critical exhaustive kernels and independent finite
  verifiers.
- `verification/current_regression.py` — fast current finite gate.

The much larger historical Python/C/diagnostic surface is preserved under
`record/corpus/code/` and `record/corpus/experiments/`. It is kept because
negative and intermediate computations matter scientifically, but it is not
automatically part of the supported API.

Useful historical Julia algorithms that survived audit have supported C++
replacements here (`cpp/shape/relation_automaton.cpp`,
`cpp/number_theory/catmap_order.cpp`). Falsified Julia lines are not ported
as production code; see `record/julia_migration.md`.
