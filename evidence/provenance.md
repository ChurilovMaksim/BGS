# Evidence provenance map

Retained JSON certificates are treated as immutable scientific records: their
`producer` field records the path that generated the file at the time of the
audited run. The repository was subsequently reorganized. This map resolves
those generation-time names without rewriting numerical payloads or pretending
a fresh rerun happened when it did not.

| Evidence | Generation-time producer | Present source / validation |
|---|---|---|
| `certificates/fourth_moment_factorization.json` | `experiments/verification/verify_fourth_moment_factorization.py` | historical generator at `record/corpus/experiments/verification/verify_fourth_moment_factorization.py`; active independent C++ verifier `computations/cpp/fourth_moment_pair_key_verifier.cpp`; fast anchor gate `computations/verification/current_regression.py` |
| `certificates/second_moment_reduction.json` | `experiments/verification/verify_second_moment_reduction.py` | historical exact generator at `record/corpus/experiments/verification/verify_second_moment_reduction.py`; current claim boundary in `mathematics/cayley_additive_energy.md` |
| `certificates/cayley_exception_k23.json` | `experiments/verification/verify_cayley_anchor_k23.py` | historical generator at `record/corpus/experiments/verification/verify_cayley_anchor_k23.py`; independently rechecked by `computations/verification/current_regression.py` and Lean `formalization/Bgs/CayleyExceptionalK23.lean` |
| `certificates/twisted_jacobi_scalar_formula.json` | `experiments/verification/verify_twisted_jacobi_scalar_formula.py` | preserved at `record/corpus/experiments/verification/verify_twisted_jacobi_scalar_formula.py`; certificate records the fresh 2026-09-03 rerun |
| `certificates/twisted_jacobi_moments.json` | `experiments/verification/verify_twisted_jacobi_moments.py` | preserved at `record/corpus/experiments/verification/verify_twisted_jacobi_moments.py`; its three R82 inputs now live under `evidence/reference/r82/` with the recorded SHA-256 values unchanged |
| `numerical/goe_spacing.json` | `experiments/spectral/goe_spacing.py` | preserved at `record/corpus/experiments/spectral/goe_spacing.py`; numerical evidence only |
| `numerical/goe_number_variance.json` | `experiments/spectral/number_variance.py` | preserved at `record/corpus/experiments/spectral/number_variance.py`; numerical evidence only |

CI mechanically verifies that each JSON `producer` resolves either as a current
path or under `record/corpus/`, and that legacy `results/reference/...` keys in
retained certificates resolve to the promoted `evidence/reference/...` files.

This distinction matters: a path migration is not a fresh scientific rerun.
The repository preserves the original producer identity and separately records
which current independent checks have actually been executed.
