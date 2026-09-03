# M1 executable workstream

Status: **ACTIVE RESEARCH / M1 ASYMPTOTIC ASSEMBLY NOT YET PROVED**.

This directory is intentionally compact. Active load-bearing calculations are implemented in Python and independently in C++17 where feasible; compiled binaries and scratch runs are never committed.

## Cycle 001 — exact assembly

- `cross_twist_energy.py` — transparent weighted key table, quotient-character projector, full twist energy, cross terms, and singular/regular decomposition.
- `cross_twist_energy.cpp` — independent C++17 implementation of the anchor calculation with its own integer loops and character transform.
- `run_suite.py` — compiles C++ in a temporary directory, cross-checks `N=53,199,461`, and runs the 14-case falsifier sweep.

Run:

```bash
python code/research/m1/run_suite.py
```

Result: `results/research/m1/cross_twist_suite.json`.

## Cycle 002 — regular Weil hypothesis

- `regular_weil_classifier.py` — Python exponent/divisor classifier plus temporary C++ compilation.
- `regular_weil_classifier.cpp` — independent C++17 classification of the generic and `d=±1` residue geometries.

Run:

```bash
python code/research/m1/regular_weil_classifier.py
```

Result: `results/research/m1/regular_weil_classifier.json`.

The general mathematical proof is in `research/M1_WEIL_002.md`: a polynomial domain mask converts the restricted rational sum to the exact complete polynomial sum required by the standard multiplicative-character Weil theorem. The programs are regression checks for the residue bookkeeping, not substitutes for that theorem.

## Trust boundary

- exact integer identities may be promoted only as finite algebraic/combinatorial facts unless separately proved in general;
- the cycle-002 `3 sqrt(N)` regular single-twist bound is an analytic lemma because the non-power classification is proved generally and then a cited standard Weil theorem is applied;
- Python/C++ agreement is independent computational evidence, not a theorem by itself;
- observed scaling is falsifier/calibration evidence only;
- the assembled cross-twist M1 energy remains open.

Authoritative status: `research/M1.md` and root `STATUS.md`.
