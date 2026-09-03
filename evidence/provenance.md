# Evidence provenance

This file maps promoted evidence to the code or historical computation that produced it. Paths under `record/corpus/` are provenance, not active theorem sources.

| Evidence | Current status | Producer / validator |
|---|---|---|
| `certificates/second_moment_reduction.json` | exact finite certificate | `computations/verification/mixed_cayley_energy.py`; regenerated and compared in CI |
| `certificates/fourth_moment_factorization.json` | exact finite regression | historical `record/corpus/experiments/verification/verify_fourth_moment_factorization.py`; independent current C++/Python pair-key gates |
| `certificates/twisted_jacobi_scalar_formula.json` | finite implementation cross-check | historical `record/corpus/experiments/verification/verify_twisted_jacobi_scalar_formula.py`; active arithmetic library retained |
| `certificates/twisted_jacobi_moments.json` | finite preserved q-curve regression | historical `record/corpus/experiments/verification/verify_twisted_jacobi_moments.py`; reference inputs under `evidence/reference/r82/` |
| `certificates/cayley_exception_k23.json` | exact finite negative control | historical producer restored in `record/corpus/experiments/verification/verify_cayley_anchor_k23.py`; independently recomputed by current gates |
| `numerical/goe_spacing.json` | descriptive finite spacing diagnostic | historical `record/corpus/experiments/spectral/goe_spacing.py`; inferential KS labels removed |
| `numerical/matched_window_count_variance.json` | descriptive matched-GOE diagnostic | historical `record/corpus/experiments/spectral/number_variance.py`; renamed because the algorithm is not standard stationary number variance |

Older JSON records may contain generation-time paths beginning with `experiments/` or `results/`. CI requires every such producer/reference to resolve either to an active file, to `record/corpus/<old path>`, or, for old `results/...` inputs, to the corresponding `evidence/...` path.
