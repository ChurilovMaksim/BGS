# BGS-TRACE-124 integer certificate

29 October 2026. Arithmetic is exact: Python `fractions.Fraction` and an independent C++ base-\(2^{32}\) integer type. No floating comparison is used for a theorem.

## Coverage

- The fourteen orders through \(47\), by the divisibility criterion, including the witnesses at \(37\), \(41\), \(43\), and \(47\).
- The five products of \(23\) with an odd prime below \(50\). Only \(23\cdot37\) is non-short.
- The five explicit tower majorants, each strictly below \(5/7\), and the gap \(575/22594<13/420\) at \(3\cdot23\).
- The six tail identities, their first differences, and their constant second differences.
- The cubic comparison for primes at least \(31\).
- The drop inequalities, including the shortness of radical \(105\) and of \(315\).
- The degree-four lower bounds on the above-side towers, each above \(82/105\).
- All twenty-seven inert comparisons for partners \(13\) through \(39\), and the scaled tail at partner \(40\), which lies above \(3/4\) and below \(82/105\).
- The defect comparison \(D(2\cdot10^{26})<857840479/16733546028\), and the majorant exceeding \(1\) at \(10^{78}\).

`receipt.json` records the windows and the SHA-256 hashes of the certificate sources.

## Commands

```text
python3 computations/verification/odd_modulus_abel.py
g++ -std=c++20 -O2 -Wall -Wextra -Wpedantic computations/cpp/odd_modulus_abel.cpp -o /tmp/odd_modulus_abel
/tmp/odd_modulus_abel
lean formalization/Bgs/OddModulusRational.lean
```

The Python program printed `odd-modulus-abel: pass`. The C++ binary exited 0 with no pedantic warning and printed the same sentence. Lean 4.33.1 exited 0. Aggregate `lake build` was not run. The new module imports only the Lean prelude.

## Non-claims

A pass does not prove BGS-TRACE-005 or BGS-BGS-001, a density of any order class, the signed off-diagonal sum, or the limit. The kick is not claimed for a ceiling tower, for an inert exponent-one partner \(q\ge40\), for \(N=15r>2\cdot10^{26}\), or at \(u_{207}\).
