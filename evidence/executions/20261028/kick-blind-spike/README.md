# BGS-TRACE-117 integer certificate

28 October 2026. Arithmetic is exact: Python `fractions.Fraction` and integer Newton square roots, and an independent C++ base-\(10^9\) integer type. No floating comparison is used for a theorem.

## Coverage

- Conjugation phases of \(M_NW_N(k,\ell)\) and \(W_N(C(k,\ell))M_N\), including the displayed quadratic polynomial. SymPy identity over \(\mathbb Q\).
- All 32 Fourier modes of `fCoeff` on \(k\in[-9,9]\), \(\ell\in\{-1,0,1\}\), the mode \((7,0)=9/20\), and the strict majorant \(B=184981/160000\).
- Pell recurrence through \(n=203\): norm \(u_n^2-2v_n^2=(-1)^n\), oddness of every \(u_n\), and \(u_{n}=5u_{n-2}+2u_{n-3}\) for \(n\ge3\). Bases \(u_5=41\), \(u_7=239\).
- Direct cleared Abel gap at every odd \(n\) from 5 through 201 (99 dimensions), the uniform comparison at \(n=201\) against \(\delta_7=14/239\), and the separate \(n=5\) endpoint.
- Sentinel: at \(n=203\), \(\rho_{203}<1\) and the same one-term gap does not exceed \(3/4\).

`receipt.json` is the Python run. It records `u_201` (77 decimal digits), the norm \(-1\), and SHA-256 hashes of the three certificate sources.

## Commands

```text
python3 computations/verification/kick_blind_spike.py --output evidence/executions/20261028/kick-blind-spike/receipt.json
g++ -std=c++20 -O2 -Wall -Wextra -Wpedantic -fsanitize=undefined computations/cpp/kick_blind_spike.cpp -o /tmp/kick_blind_spike
/tmp/kick_blind_spike
lean formalization/Bgs/KickBlindRational.lean
```

The C++ binary printed `kick_blind_spike passed u_201_digits=77 odd_n=5..201 count=99 majorant=184981/160000 sentinel_203=below`. Lean 4.33.1 exited 0. Aggregate `lake build` was not run.

## Non-claims

A pass does not prove BGS-TRACE-005 or BGS-BGS-001, the limit \(N\to\infty\), a gap at a generic odd dimension, or the off-diagonal sum. The failure at \(n=203\) is a failure of this lower bound, not a proved drop of \(L_N\).
