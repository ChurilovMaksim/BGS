# BGS-TRACE-118 integer certificate

28 October 2026. Arithmetic is exact: Python `fractions.Fraction` and an independent C++ base-\(10^9\) integer type. No floating comparison is used for a theorem.

## Coverage

- All 32 Fourier modes of `fCoeff`, Hermitian symmetry, the mass \(\sigma=66033/160000\), the mode \((7,0)=9/20\), and the strict majorant \(B=184981/160000\).
- The hand product \(\gamma(1)=-7/2000000\), and a direct scan of \(C^r\) modulo \(u_{203}\) for every lag \(1\le r\le202\). The only hits are the four ordered pairs at lags \(1\) and \(202\).
- The archimedean square \(104^2\cdot2>128^2\) and the box classification of \(C\) at lag \(1\).
- Pell recurrence through \(m=410\), including the norm, oddness, and the bases \(u_5=41\), \(u_7=239\), \(u_9=1393\).
- Size inequalities that force every congruence with \(t\le100\), and the middle lag \(t=101\), to be an exact vector equality.
- The cleared Abel comparison at \(n=203\), failure of the one-term comparison at the same index, the vacuous third-order majorant and the vacuous Hilbert--Schmidt triangle at \(n=205\), the pure second-order room at \(n=205\), and the pure second-order ceiling at \(n=207\).
- The same four-hit overlap scan at \(n=205\) and \(n=207\).

`receipt.json` is the Python run. It records \(u_{203}\) (78 decimal digits) and SHA-256 hashes of the certificate sources.

## Commands

```text
python3 computations/verification/orbit_orthogonal_spike.py --output evidence/executions/20261028/orbit-orthogonal-spike/receipt.json
g++ -std=c++20 -O2 -Wall -Wextra -Wpedantic -fsanitize=undefined computations/cpp/orbit_orthogonal_spike.cpp -o /tmp/orbit_orthogonal_spike
/tmp/orbit_orthogonal_spike
lean formalization/Bgs/OrbitOrthogonalRational.lean
```

The C++ binary printed `orbit_orthogonal_spike passed u_203_digits=78 hits=4 gamma=-7/2000000 quadrature=above one_term=below sentinel_205=vacuous`. Lean 4.33.1 exited 0. Aggregate `lake build` was not run.

## Non-claims

A pass does not prove BGS-TRACE-005 or BGS-BGS-001, the limit \(N\to\infty\), a gap at a generic odd dimension, or a positive lower bound at \(n=205\). The silence at \(n=205\) is a failure of these remainders. The ceiling at \(n=207\) is a failure of the second-order disk, not a proved drop of \(L_N\).
