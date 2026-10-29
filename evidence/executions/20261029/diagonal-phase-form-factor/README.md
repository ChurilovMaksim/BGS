# BGS-TRACE-127 certificate

29 October 2026. The occupation sums are floating-point checks of the counting argument. The kernels, the symbol energy, and the phase identity of \(Q\) are exact integer checks. Python and C++ both perform them. Lean decides the matrix factorizations and the integer gaps. It does not formalize the path count.

## Coverage

- Odd moduli \(3,5,7,9,11,15,21,25,27,35,45,49,63,105\), including \(N=3\), \(5\) and \(7\).
- Times \(1\), \(2\) and \(3\). The occupation sum matches \(1\), \((2N-1)/N\) and \((6N^2-9N+4)/N^2\) with absolute error below \(10^{-11}\).
- \(\lvert\ker(S^2-I)\rvert=1\) and \(\lvert\ker(S^3-I)\rvert\in\{1,49\}\), equal to \(\gcd(14,N)^2\). At \(N=49\) the count is \(49\), not \(2401\).
- The literal squared trace of \(M_N^2\) and \(M_N^m\) at \(m=3\) matches those kernels to absolute error below \(10^{-6}\).
- Flatness of every cat-map entry, and the integer identity of the two triangle sums of \(Q\) for every triple at the odd moduli \(3\) through \(15\).
- Symbol energy \(6603300\) and \(32\) modes.
- One shared splitmix sample, seed \(20261029\), \(24\) draws, \(\eta=2\), dimensions \(3,5,7,11,31\), times \(1\) through \(6\). Python and C++ print the same twelve-digit means. At \(N=7\), time \(3\), the mean is \(44.632431403503\). At \(N=31\), time \(5\), the mean is \(47.417022055369\), and \(\lvert\ker(S^5-I)\rvert=1\).

## Commands

```text
python3 computations/verification/diagonal_phase_form_factor.py
g++ -std=c++20 -O2 -Wall -Wextra -Wpedantic computations/cpp/diagonal_phase_form_factor.cpp -o /tmp/diagonal_phase_form_factor
/tmp/diagonal_phase_form_factor
lean formalization/Bgs/DiagonalPhaseFormFactorRational.lean
```

Lean 4.33.1 exited 0. Aggregate `lake build` was not run. The new module imports only the Lean prelude. The C++ binary exits 0 with no pedantic warning.

## Non-claims

A pass does not prove BGS-TRACE-005 or BGS-BGS-001. It does not identify the sixteen-phase ensemble with CUE or COE. The printed sample means are properties of those \(24\) draws.
