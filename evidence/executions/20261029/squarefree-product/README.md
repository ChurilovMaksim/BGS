# BGS-TRACE-123 integer certificate

29 October 2026. Arithmetic is exact: Python `fractions.Fraction` and an independent C++ base-\(2^{32}\) integer type. No floating comparison is used for a theorem.

## Coverage

- The ten orders \(t(3),t(5),t(7),t(11),t(13),t(17),t(19),t(23),t(29),t(31)\), by the divisibility criterion, including the witness at \(31\).
- Every least common multiple in the finite tables, and the short-order or strong-shortness flag of each listed product.
- The corner integers for four or more primes, for three primes not divisible by \(15\), and for the return ratio \(152/185\).
- The degree-four lower bound of \(R(152/185)\) and of \(R(88/115)\), both above \(82/105\).
- The eight-term degree-four lower bound at \(N=195\), above \(82/105\).

`receipt.json` records the windows and the SHA-256 hashes of the certificate sources.

## Commands

```text
python3 computations/verification/squarefree_product_abel.py
g++ -std=c++20 -O2 -Wall -Wextra -Wpedantic computations/cpp/squarefree_product_abel.cpp -o /tmp/squarefree_product_abel
/tmp/squarefree_product_abel
lean formalization/Bgs/SquarefreeProductRational.lean
```

Lean 4.33.1 exited 0. Aggregate `lake build` was not run. The new module imports only the Lean prelude. The C++ binary exits 0 with no pedantic warning.

## Non-claims

A pass does not prove BGS-TRACE-005 or BGS-BGS-001, a density of any order class, a modulus divisible by \(p^2\), the signed off-diagonal sum, the limit, or the kicked statistic at \(u_{207}\). The kick on \(N=15r\) is not claimed above \(10^{26}\).
