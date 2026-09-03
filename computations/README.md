# Computations

The supported implementation layer is intentionally small and scientific in
scope.

- `python/` — reusable exact/symbolic finite-field and matrix-element routines.
- `cpp/fourth_moment_pair_key_verifier.cpp` — independent finite verifier for
  the exact pair-key fourth-moment reduction.
- `cpp/mobius_pair_key_diagnostic.cpp` — historical-Möbius versus corrected
  pair-key diagnostic. Its name is deliberately diagnostic: it is not the
  current proof object.
- `cpp/cat_map_order.cpp` — finite-field cat-map order scanner/calibrator.
- `cpp/relation_shape_automaton.cpp` — exact relation/shape dynamic-programming
  kernel recovered from the useful Julia line.
- `verification/current_regression.py` — fast current finite gate tying the
  active mathematics to preserved anchors.

The broader historical Python/C/Julia/diagnostic surface is preserved under
`record/corpus/code/` and `record/corpus/experiments/`. Presence there is
provenance, not an API guarantee or a theorem-status label.

Fortran is intentionally absent for now: no current dense numerical hot kernel
has been profiled strongly enough to justify a Fortran implementation. The
language decision is made after profiling, not to satisfy a language quota.
