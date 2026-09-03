# Evidence provenance

This file maps promoted evidence to the current verifier or to the historical computation that produced it. Paths under `record/corpus/` are provenance, not active theorem sources.

| Evidence | Current status | Producer / validator |
|---|---|---|
| `certificates/second_moment_reduction.json` | exact finite certificate | `computations/verification/mixed_cayley_energy.py`; regenerated and compared in CI |
| `certificates/fourth_moment_factorization.json` | exact finite regression | `computations/cpp/fourth_moment_pair_key_verifier.cpp`; fast Python anchors in `current_regression.py` |
| `certificates/twisted_jacobi_scalar_formula.json` | finite implementation cross-check | historical producer `record/corpus/experiments/verification/verify_twisted_jacobi_scalar_formula.py`; active arithmetic primitives retained |
| `certificates/twisted_jacobi_moments.json` | finite preserved q-curve regression | historical producer `record/corpus/experiments/verification/verify_twisted_jacobi_moments.py`; inputs under `evidence/reference/r82/` |
| `certificates/cayley_exception_k23.json` | exact finite negative control | historical producer restored under `record/corpus/experiments/verification/verify_cayley_anchor_k23.py`; independently recomputed by current Python and Lean gates |
| `numerical/goe_spacing.json` | descriptive finite spacing diagnostic | historical `record/corpus/experiments/spectral/goe_spacing.py`; old IID-KS pass semantics removed |
| `numerical/matched_window_count_variance.json` | descriptive matched-GOE diagnostic | historical `record/corpus/experiments/spectral/number_variance.py`; renamed because the algorithm is not stationary `Sigma^2(L)` |

The promoted fourth-moment record was deliberately reduced during the editorial audit to quantities checked by the active C++ verifier. Historical heuristic `B(0)` error-bound fields remain recoverable in Git history but are no longer promoted evidence.

Older retained JSON may contain generation-time paths beginning with `experiments/` or `results/`. CI requires every such producer/reference to resolve either to an active file, to `record/corpus/<old path>`, or, for old `results/...` inputs, to the corresponding `evidence/...` path.
