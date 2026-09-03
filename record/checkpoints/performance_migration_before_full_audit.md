# Performance migration ledger

Updated: 2026-09-03.

This ledger records language changes made after the Julia audit. The rule is task-driven rather than language-driven: Python remains the default for readable symbolic/exact orchestration and analysis; C++20 is used for expensive finite-field/exhaustive kernels; Fortran is reserved for a measured dense-numerical use case and is not introduced merely to diversify languages.

## Completed: M1 cross-term diagnostic

### Previous active producer

`experiments/m1/cross_term_energy.py`

The diagnostic compares the historical Mobius-graph assembly with the correct pair-key assembly. Its heavy work consists of finite-field pair enumeration, all twist-pair character accumulation, circular convolutions, and a Fourier-domain correction check.

### Canonical replacement

`src/cpp/m1/cross_term_energy.cpp`

Why C++20 is preferable here:

- the workload is dominated by nested finite-field/exhaustive loops rather than exploratory data analysis;
- direct memory/layout control avoids repeatedly materializing NumPy temporaries in the pair loops;
- the replacement uses `long double` complex arithmetic and direct circular convolutions/DFTs, so the diagnostic does not acquire an external FFT dependency;
- one standalone executable can serve both production and deterministic regression mode.

The old Python producer was deleted from the active tree only after the replacement matched preserved anchors. It remains recoverable in Git history; no extra legacy copy was created.

### Promotion gates

The C++20 producer is compiled with

`-std=c++20 -O2 -Wall -Wextra -Wpedantic -Werror`

and its `verify` mode reproduces the two saved designs:

| Design | Preserved `sum B(t)^2` | Historical normalized energy | C++ correction residuals |
|---|---:|---:|---:|
| `N=53, K=13` | `3,410,502,105` | `3,682,650,293` | time `4.62e-17`, Fourier `1.41e-16` |
| `N=199, K=11` | `115,589,503,389` | `113,859,701,371` | time `2.25e-16`, Fourier `1.12e-15` |

The old NumPy implementation had already passed the same correction identity, with residuals around `1e-13`--`1e-12`. The smaller C++ residuals are a numerical implementation improvement, not a stronger mathematical theorem.

`results/diagnostics/m1_cross_term_energy.json` records the current producer, migration provenance, and regenerated values.

## Existing migrated C++ components

- `src/cpp/shape/relation_automaton.cpp` — exact relation/shape DP consolidated from multiple Julia variants; arbitrary precision through Boost.Multiprecision.
- `src/cpp/number_theory/catmap_order.cpp` — prime/order scan and order semantics consolidated from Julia utilities.
- `src/cpp/verification/fourth_moment_factorization.cpp` — independent verification implementation; the Python/C++ duplication is intentional because independence is part of the scientific certificate.

## What should stay Python

Do not translate a script merely because it is old. In particular, Python remains preferable for:

- symbolic derivation and finite-field formula inspection;
- experiment orchestration and small deterministic falsifiers;
- parsing/aggregation of stored JSON results;
- plotting and statistical post-processing;
- manuscript/repository tooling;
- code whose runtime is dominated by optimized NumPy/SciPy linear algebra unless profiling shows a real bottleneck.

## Fortran decision

There is currently no justified Fortran component. None of the migrated Julia tasks is primarily a large dense BLAS/LAPACK-style numerical kernel for which a standalone Fortran implementation would improve the repository. If profiling later identifies such a kernel, it should be introduced with a measured benchmark, reproducibility test, and one canonical implementation rather than as an additional language copy.

## Next migration-selection rule

For each candidate in the broad `code/` corpus:

1. determine whether the script is still scientifically meaningful;
2. reconstruct and test the statistic/object it actually computes;
3. quarantine rather than port if the underlying claim is false or superseded;
4. profile or analyze asymptotic cost before choosing a new language;
5. compare the replacement with preserved exact invariants or saved outputs;
6. remove the old active producer only after the gate passes; rely on Git/provenance rather than creating another copy.

This keeps the repository multilingual only where the mathematics or performance benefits from it, while avoiding a second wave of redundant implementations.
