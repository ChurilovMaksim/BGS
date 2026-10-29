# BGS-TRACE-121 integer certificate

29 October 2026. Arithmetic is exact: Python `fractions.Fraction` and an independent C++ base-\(10^9\) integer type. No floating comparison is used for a theorem.

## Coverage

- The exponential majorants \(e^{6/7}\le23441/9947\), \(e^{2/7}\le45187/33957\) and \(e^{6/49}\le31780817/28118111\), and the degree-4 partial sum \(213457/83521\) of \(e^{16/17}\).
- The cleared comparisons placing \(p=7\) and every \(7^k\), \(k\ge2\), above \(3/4\), and every split-half prime \(p\ge17\) below \(41/60\).
- The prime-power ceilings \(59/144\), \(349/1200\), \(3287/4840\) and \(427139065/600824064\), and the kicked sums against \(13/420\).
- The split-half tower window \(N\le10^{25}\). The long, seven, and ordinary prime comparisons use the \(10^{26}\) defect of BGS-TRACE-120.
- The witnesses \(t(7)=3\), \(t(13)=14\) with depth \(2\), and \(t(31)=15\) with depth \(2\).
- The Pell induction through \(u_{207}\) and its \(79\) digits.
- The order trichotomy for every odd prime through \(500\), and the kernel formula for every odd prime \(p\le80\) at modulus \(p^k\), \(k\le3\), whenever the modulus is at most \(1000\).

`receipt.json` records those windows and SHA-256 hashes of the certificate sources.

## Commands

```text
python3 computations/verification/order_trichotomy_abel.py
g++ -std=c++20 -O2 -Wall -Wextra -Wpedantic computations/cpp/order_trichotomy_abel.cpp -o /tmp/order_trichotomy_abel
/tmp/order_trichotomy_abel
lean formalization/Bgs/OrderTrichotomyRational.lean
```

Lean 4.33.1 exited 0. The literal power \(10^{100}\) was reduced with `exponentiation.threshold` set to 4096. Aggregate `lake build` was not run: the Mathlib cache was not present. The new module imports only the Lean prelude. The C++ build warns under `-Wpedantic` because the fraction type uses `__int128`, as the order-ladder certificate does, and the binary exits 0.

## Non-claims

A pass does not prove BGS-TRACE-005 or BGS-BGS-001, a density of any order class, a modulus divisible by two distinct primes, the signed off-diagonal sum, the limit, or the kicked statistic at \(u_{207}\). The census through the stated prime caps is a finite check of the order and kernel formulae, not a density theorem.
