# M1 cross-twist workstream

Status: **ACTIVE RESEARCH / NOT A PROOF OF M1**.

This directory contains the executable finite-field laboratory for the current M1 bottleneck. It is intentionally small:

- `cross_twist_energy.py` — transparent NumPy implementation of the weighted key table, quotient-character projector, full twist energy, and singular/regular decomposition.
- `cross_twist_energy.cpp` — independent C++17 implementation of the same anchor computation. It uses no NumPy/BLAS and exists to catch implementation-specific mistakes.
- `run_suite.py` — compiles the C++ implementation in a temporary directory, cross-checks the anchor cases, and runs the finite-N falsifier sweep.

Run from repository root:

```bash
python code/research/m1/run_suite.py
```

The generated research result is `results/research/m1/cross_twist_suite.json`. No compiled binary is committed.

## Trust boundary

Exact finite-N identities verified here may be promoted as finite combinatorial/algebraic facts. Observed scaling, a passing Weil-envelope falsifier, or close Python/C++ agreement is not an asymptotic proof. The authoritative theorem status remains `research/M1.md` and `STATUS.md`.
