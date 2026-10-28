# BGS-TRACE-119 integer certificate

28 October 2026. Arithmetic is exact: Python `fractions.Fraction` and an independent C++ base-\(10^9\) integer type. No floating comparison is used for a theorem.

## Coverage

- All 32 Fourier modes of `fCoeff`, Hermitian symmetry, the mass \(\sigma=66033/160000\), and the strict majorant \(B=184981/160000\). The C++ program checks the same nonzero support and the archimedean bound; the Python program recomputes \(\sigma\) and \(B\).
- The bound \(\lvert2k\pm\ell\sqrt2\rvert\le18\) on every nonzero mode, by the integer square test.
- The pigeonhole diameter \(205-\lceil205/11\rceil=186\).
- The norm block \((18\cdot11)^2\alpha^{372}<2u_{205}^2\), and the gap comparison \(4860\beta^5<1\) with \(\beta^5=u_{10}-v_{10}\sqrt2\).
- The scale \(x=n\theta B<7/2\), the window bounds \(\Phi(2,2)<9/100\) and \(\sum_{m=3}^{11}\Phi(m,4(m-1)+1)<1/23\), the tail majorant at \(7/2\), and the identity \(2097/32890<1/12\).
- The cleared Abel comparison \((1-410/u_{205})(1-\varepsilon_2-1/12)^2>3/4\).

`receipt.json` is the Python run. It records \(u_{205}\) (79 decimal digits, prefix `14722633416904597515`) and SHA-256 hashes of the certificate sources.

## Commands

```text
python3 computations/verification/positive_time_spike.py --output evidence/executions/20261028/positive-time-spike/receipt.json
g++ -std=c++20 -O2 -Wall -Wextra -Wpedantic -fsanitize=undefined computations/cpp/positive_time_spike.cpp -o /tmp/positive_time_spike
/tmp/positive_time_spike
lean formalization/Bgs/PositiveTimeRational.lean
```

The C++ binary printed `positive_time_spike passed u_205_digits=79 modes=32 gap<=4 error<1/12`. Lean 4.33.1 exited 0 with `exponentiation.threshold` set to 4096, so the literal powers through \(10^{880}\) were reduced. Aggregate `lake build` was not run: the Mathlib cache was not present. The new module imports only the Lean prelude. GitHub Actions on the preceding spike was skipped in about three seconds; this certificate was checked locally.

## Non-claims

A pass does not prove BGS-TRACE-005 or BGS-BGS-001, the limit \(N\to\infty\), a gap at a generic odd dimension, or a positive lower bound at \(n=207\). The third-order operator-norm remainder and the Hilbert--Schmidt triangle remain silent at \(n=205\). The ceiling at \(n=207\) is a failure of the second-order disk, not a proved drop of \(L_N\).
