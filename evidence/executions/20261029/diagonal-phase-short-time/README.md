# BGS-TRACE-128 certificate

Floating-point occupation sums for the symmetric cat map and for the row-inverted matrix, together with the integer Kloosterman census at the primes 5 and 7. A pass checks the inequalities in `mathematics/fixed-map/diagonal_phase_short_time.md`. It does not prove them, and it does not prove BGS-TRACE-005 or BGS-BGS-001.

Coverage. Symmetric inequality for times 3, 4 and 5 on the odd moduli 3 through 15, and for time 4 at N=21, 31, 41 and 49. Inversion inequality for times 3 and 4 on the primes from 3 through 31. Times 1 and 2 match the flat-matrix formulae. At p=3 the inversion sum equals the symmetric sum. The symmetry witness is the pair (1,2), except at p=11, where it is (2,0).

Recorded values, Python. At N=3, time 3, the symmetric sum is 3.444444444444, the main term is 1.333333333333 and the slack against 14 is positive. At N=7, time 4, the sum is 5.332361516035. At N=49, time 4, the sum is 7.527892289777 and the main term is 7.056651565249. At p=5, time 3, the inversion sum is 2.920000000000. At p=31, time 4, it is 3.971503994579. The quadruple counts are 36 and 90. C++ agrees to 1e-12; the largest absolute difference is one unit in the twelfth digit at N=49, time 4.

```sh
python3 computations/verification/diagonal_phase_short_time.py
g++ -std=c++20 -O2 -Wall -Wextra -Wpedantic computations/cpp/diagonal_phase_short_time.cpp -o /tmp/diagonal_phase_short_time
/tmp/diagonal_phase_short_time
```

Lean, with the toolchain `leanprover/lean4:v4.33.1`, decides the integer comparisons only:

```sh
lean formalization/Bgs/DiagonalPhaseShortTimeRational.lean
```
