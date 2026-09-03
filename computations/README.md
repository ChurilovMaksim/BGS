# Computations

The active computational surface is intentionally small and has an explicit scientific contract.

## Python library

`computations/python/bgs/` contains reusable finite-field, pair-key and twisted-Jacobi primitives. Inputs that encode mathematical assumptions (primality, primitive logarithm generators, subgroup/eigenvalue order) are validated rather than silently trusted.

## Exact verification

- `verification/current_regression.py` — fast exact anchors, API fail-fast checks, pair-key bijection and finite fourth-moment anchors.
- `verification/mixed_cayley_energy.py` — exhaustive 720-matching rank audit, exact cyclotomic resultants for `K=11,13`, finite exceptional/non-exceptional design checks and the `(461,23)` non-uniformity witness.

The latter is regenerated in CI and compared with `evidence/certificates/second_moment_reduction.json`.

## C++20

- `cpp/fourth_moment_pair_key_verifier.cpp` — independent finite implementation of the corrected pair-key/fourth-moment geometry.
- `cpp/cat_map_order.cpp` — exact order/split-prime design utility; its regression records that the historical Julia comment claiming order 5 at `p=31` was false (the matrix order is 15).

Historical C++ falsifiers and shape-language experiments are kept under `record/engineering/historical_cpp/`, not built as part of the active mathematical surface.

## Language boundary

No Julia source is allowed under the active `computations/`, `mathematics/`, `formalization/`, `manuscript/` or `evidence/` trees. The 31 historical Julia paths remain inventoried and browsable under `record/`; migration is performed only for useful, independently testable kernels.
