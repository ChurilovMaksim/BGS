# BGS-TRACE-129 certificate

Integer orbit counts and the floating-point Bessel average of the classical orbit sum. A pass checks `mathematics/fixed-map/scalar_return_bessel.md`. It does not identify the orbit sum with the quantum trace, and it does not prove BGS-TRACE-005 or BGS-BGS-001.

The quadruple excess is 0 at the primes 7, 31, 41 and 47, and 120 at p=11. At lambda=1 the Bessel average is 1.2307 times the exponential at p=11, 0.9880 times it at p=31, and 0.9848 times it at p=47. A Monte Carlo of the orbit sum agrees with the Bessel sum to 0.01 at N=7 and N=11.

```sh
python3 computations/verification/scalar_return_bessel.py
g++ -std=c++20 -O2 -Wall -Wextra -Wpedantic computations/cpp/scalar_return_bessel.cpp -o /tmp/scalar_return_bessel
/tmp/scalar_return_bessel
```

Lean, toolchain `leanprover/lean4:v4.33.1`:

```sh
lean formalization/Bgs/ScalarReturnBesselRational.lean
```
