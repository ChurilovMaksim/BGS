# BGS-TRACE-120 integer certificate

28 October 2026. Arithmetic is exact: Python `fractions.Fraction` and an independent C++ base-\(10^9\) integer type. No floating comparison is used for a theorem.

## Coverage

- The exponential majorants \(e^{5/6}\le361/156\), \(e^{3/4}\le17/8\), the partial sums \(1957/720\), \(109/15\) and \(5647/2401\), and the four-term sum \(70600/83521\).
- The cleared comparisons \(156/205>3/4\), \((19/20)^2\cdot70600/83521>3/4\), \(7/12<5/7<3/4\), \(41/60<5/7\) and \(2401/3246<3/4\).
- The short window \(N\le10^{39}\) and the long window \(p\le10^{26}\).
- The gcd of the entries of \(C^t-I\) through \(t=40\), and agreement of the divisibility order with matrix powering for every odd modulus through \(300\).
- The witnesses \(N=35\) (order \(6\), not a Pell value, one return below \(3/4\)), \(p=5\) (order \(6\)) and \(p=7\) (order \(3\), neither hypothesis).
- The \(32\)-mode majorant \(B=184981/160000\).
- An exact cyclotomic evaluation, in Python only, of \(\lvert\operatorname{Tr}M_p^m\rvert^2\) at \(p=5\) and \(p=7\). The C++ program does not repeat that trace.

`receipt.json` records the finite census inside that modulus cap and SHA-256 hashes of the certificate sources.

## Commands

```text
python3 computations/verification/order_ladder_abel.py
g++ -std=c++20 -O2 -Wall -Wextra -Wpedantic computations/cpp/order_ladder_abel.cpp -o /tmp/order_ladder_abel
/tmp/order_ladder_abel
lean formalization/Bgs/OrderLadderRational.lean
```

Lean 4.33.1 exited 0. The literal powers through \(10^{104}\) were reduced with `exponentiation.threshold` set to 4096. Aggregate `lake build` was not run: the Mathlib cache was not present. The new module imports only the Lean prelude. The C++ build warns under `-Wpedantic` because the fraction type uses `__int128`, as the kick-blind certificate does, and the binary exits 0. GitHub Actions on the preceding spikes was skipped in about three seconds; this certificate was checked locally.

## Non-claims

A pass does not prove BGS-TRACE-005 or BGS-BGS-001, the limit \(N\to\infty\), a CUE value at a long-order prime, or the kicked statistic at \(u_{207}\). The prime \(p=7\) meets neither order hypothesis. The census through modulus \(300\) is a finite check of the order criterion, not a density theorem.
