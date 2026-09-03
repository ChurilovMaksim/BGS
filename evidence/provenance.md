# Evidence provenance

Every promoted evidence object resolves to a maintained producer in the
current tree. CI does not fall back to a historical archive path.

| Evidence | Current interpretation | Maintained producer / validator |
|---|---|---|
| `certificates/cayley_fixed_k_audit.json` | exact finite fixed-`K` matching/resultant and Cayley audit | `computations/verification/mixed_cayley_energy.py`; regenerated structurally in CI |
| `certificates/fourth_moment_factorization.json` | exact finite pair-key/fourth-moment regression | `computations/cpp/fourth_moment_pair_key_verifier.cpp`; Python anchors in `current_regression.py` |
| `certificates/twisted_jacobi_scalar_formula.json` | finite floating-point implementation cross-check | `computations/verification/twisted_jacobi_regression.py` |
| `certificates/twisted_jacobi_moments.json` | finite preserved q-curve regression | `computations/verification/twisted_jacobi_regression.py`; reference hashes checked before use |
| `certificates/cayley_exception_k23.json` | independent exact finite non-uniformity witness | `computations/cpp/cayley_energy_verifier.cpp`, Python regression and Lean `CayleyEnergy.lean` |
| `numerical/goe_spacing.json` | descriptive full-Hermitian finite spacing diagnostic | `computations/analysis/spectral_diagnostics.py spacing`; complete record checked by `verify` mode in CI |
| `numerical/matched_window_count_variance.json` | descriptive full-Hermitian matched-GOE forward-window diagnostic | `computations/analysis/spectral_diagnostics.py window`; complete record checked by `verify` mode in CI |

The reference q-curves live only under `evidence/reference/r82/`; their
SHA-256 digests are pinned in `twisted_jacobi_regression.py`.

`cayley_exception_k23.json` intentionally overlaps one row of
`cayley_fixed_k_audit.json`: it is retained because its producer is an
independent C++ implementation and its validators include Lean. This is an
independent negative-control surface, not an accidental archive duplicate.

Historical producer names remain recoverable from Git history but are no
longer part of the active provenance chain.
