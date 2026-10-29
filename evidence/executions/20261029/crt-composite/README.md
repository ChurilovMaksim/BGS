# BGS-TRACE-122 integer certificate

29 October 2026. Arithmetic is exact: Python `fractions.Fraction` and an independent C++ base-\(2^{32}\) integer type. No floating comparison is used for a theorem.

## Coverage

- The nine orders below \(30\), by the divisibility criterion, and the absence of a short prime in that range.
- The degree-four lower bounds at \(N=21\) and for three times a short prime, both above \(3/4\) and above \(82/105\).
- The degree-eight ceilings at the three explicit semiprimes and at every tail corner, all below \(5/7\).
- The expansion of the seven-family majorant \(\varphi(q)-3/4\) and the positivity integers for every integer \(q\ge13\).
- The defect endpoint at \(10^{26}\), reused from BGS-TRACE-120 for every odd dimension in that range.
- The reduction of every nonsplit tail at a smaller prime at least \(37\) to one degree-eight majorant, including the odd inert-half corner.
- A finite sandwich of every semiprime whose prime factors are less than \(100\).

`receipt.json` records the windows and the SHA-256 hashes of the certificate sources.

## Commands

```text
python3 computations/verification/crt_composite_abel.py
g++ -std=c++20 -O2 -Wall -Wextra -Wpedantic computations/cpp/crt_composite_abel.cpp -o /tmp/crt_composite_abel
/tmp/crt_composite_abel
lean formalization/Bgs/CrtCompositeRational.lean
```

Lean 4.33.1 exited 0. The literal power \(10^{104}\) was reduced with `exponentiation.threshold` set to 4096. Aggregate `lake build` was not run. The new module imports only the Lean prelude. The C++ binary exits 0 with no pedantic warning.

## Non-claims

A pass does not prove BGS-TRACE-005 or BGS-BGS-001, a density of any order class, a modulus with three or more distinct prime factors, the signed off-diagonal sum, the limit, or the kicked statistic at \(u_{207}\). The sandwich below the stated prime cap is a finite check of the case split, not a density theorem.
