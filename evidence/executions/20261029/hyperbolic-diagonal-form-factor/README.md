# BGS-TRACE-131 certificate

Integer checks of the companion identity, the prime kernel trichotomy, the trace-equivalent split at trace \(-16\) modulo \(3\), the prime-power count \(49\), and the revival rationals \(-42025/8\) and \(-375/8\). Floating-point checks of unitarity, flatness, symmetry, the squared-trace identity, and the time-one Bessel evaluation. Python also checks the Haar values at times one through three and the revival jet at \(N=5\), \(m=3\), \(\eta=0.02\).

A pass checks the finite statements in `mathematics/fixed-map/hyperbolic_diagonal_form_factor.md`. It does not prove them, and it does not prove BGS-TRACE-005 or BGS-BGS-001. It does not prove a fixed-time limit.

Coverage. Traces \(3\) through \(8\) and \(-16\), indices through \(12\). Matrices of traces \(6\), \(5\), \(4\), \(3\), and \(-16\). Odd moduli through \(21\) for the matrix checks in Python, through \(15\) in C++, plus the kernel at \(49\). Primes \(5\) through \(19\) for the trichotomy, \(392\) rows in both programs. The time-one defect at \(N=9\), \(\eta=1\), for trace \(5\), is \(1.623121560698\) in both programs. The Python revival jet is \(-46.858421501748\), against \(-375/8=-46.875\).

```sh
python3 computations/verification/hyperbolic_diagonal_form_factor.py
g++ -std=c++20 -O2 -Wall -Wextra -Wpedantic computations/cpp/hyperbolic_diagonal_form_factor.cpp -o /tmp/hyperbolic_diagonal_form_factor
/tmp/hyperbolic_diagonal_form_factor
```

Lean, with the toolchain `leanprover/lean4:v4.33.1`, decides the integer comparisons only. The aggregate build

```sh
cd formalization && lake exe cache get && lake build Bgs
```

exited 0 on 29 October 2026 (`8791` jobs). The log is [build_bgs.log](build_bgs.log), sha256 `2118079bc22700518846e55ca75c84e3a5d0f64fbcaf786ea7c2bd0e3d938b8c`. The same log is stored with the aggregate receipts.
