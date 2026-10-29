# BGS-TRACE-125 integer certificate

29 October 2026. Arithmetic is exact: Python `fractions.Fraction` and an independent C++ integer program. The Pell norm at large indices is compared with an explicit 128-bit product. No floating comparison is used for a theorem.

## Coverage

- All 32 nonzero Fourier modes, the Hermitian symmetry, and the mass \(66033/160000\).
- The exact lag-1 products, equal to \(-7/2000000\), and the cleared coefficient \(1650797/4000000\).
- The exponent-1 box count for \(C\) and for \(C^{-1}\).
- The archimedean integer \(104^2\cdot2-128^2=5248\), the quadratic seed \(f(17)=11470\), and the positivity identity for \(7u^2-10u+19\).
- The exhaustive support scan at \(N=u_5=41\). The scans at \(n=7,9,11\) repeat a count already proved for every odd \(n\ge7\).

`receipt.json` records the SHA-256 hashes of the certificate sources.

## Commands

```text
python3 computations/verification/uniform_orbit_overlap.py
g++ -std=c++20 -O2 -Wall -Wextra -Wpedantic computations/cpp/uniform_orbit_overlap.cpp -o /tmp/uniform_orbit_overlap
/tmp/uniform_orbit_overlap
lean formalization/Bgs/UniformOrbitOverlapRational.lean
```

Each command exited 0. The C++ compile produced no warning. Lean 4.33.1 exited 0. Aggregate `lake build` was not run. The new module imports only the Lean prelude.

## Non-claims

A pass does not prove BGS-TRACE-005 or BGS-BGS-001. It does not bound the third-order remainder, does not give \(L_N(U_N;1)>3/4\) at any new dimension, and does not estimate the signed off-diagonal sum at times of order \(N\). The pure cat map is already non-CUE by BGS-TRACE-117.
