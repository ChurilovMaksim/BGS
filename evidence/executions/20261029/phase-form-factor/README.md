# BGS-TRACE-126 certificate

29 October 2026. The symbol arithmetic is exact: Python `fractions.Fraction` and independent C++ `int64` arithmetic. The cyclotomic witness and the prime-revival coefficient are exact. Matrix comparisons are float64 checks of the trace closure, the interaction picture and the two symmetries at dimension 7.

## Coverage

- The 32 Fourier modes, Hermitian symmetry, energy \(66033/160000\), parity energy \(663/4000000\), and majorant \(184981/160000\).
- The unreduced reversal sum \(66031/80000\), and the folded parity and reversal defects at every odd modulus from 3 through 77. Both vanish at \(N=7\) and are positive otherwise. The stable values hold for every odd \(N\ge 19\) (parity) and every odd \(N\ge 79\) (reversal).
- The nonzero cyclotomic element at \(N=11\), \(m=3\).
- The prime-revival identity \(D_2=-m(\sigma-\sigma_0(p))p^2\). The zero-mode energies are \(\sigma_0(3)=81/64000\), \(\sigma_0(5)=1/320000\), \(\sigma_0(7)=81/200\) and \(\sigma_0(p)=0\) for the primes \(p\ge 11\) in the certificate. The rational values are \(D_2(3,4)=-1184949/80000\), \(D_2(5,6)=-79239/1280\), \(D_2(7,3)=-181251/160000\) and \(D_2(41,5)=-111001473/32000\).
- The folded identity \(A_7=(9/10)I\), in exact coefficients and on the literal matrix.
- Floating-point agreement of the Gauss-sum trace, the order-two coefficient, the interaction picture, and one two-pair torus average. At \(N=7\) a central difference of the fixed-kick squared trace is flat, while the phase-averaged coefficient is the nonzero rational above.

## Self-red-team correction, 29 October 2026

The first draft stated \(D_2=-m\sigma N^2\) at every odd prime. That step is false at \(p=3,5,7\): symbol modes congruent to \(0\) act as the identity and lie in the image \(\{0\}\). The corrected coefficient keeps \(\sigma_0(p)\). The same draft used \((2N+|R|)|R|\) as the remainder after the displayed quadratic polynomial. That comparison bounds \(|f|^2-|P_2|^2\) only. The polynomial \(|P_2|^2\) still contains the cubic and quartic terms. The averaged remainder now includes the quartic bound \(N^2 x^4/4\), and the fixed-kick remainder also includes \(N^2 x^3\). The derivative remainder is the integral form, because the trace is complex-valued. A third slip wrote \(\eta^2 N m^2=O(1/N)\); under the truncation that quantity is \(O(N)\), and the relative correction is \(m\eta^2\).

`receipt.json` records the SHA-256 hashes of the certificate sources.

## Commands

```text
python3 computations/verification/interaction_phase_form_factor.py
g++ -std=c++20 -O2 -Wall -Wextra -Wpedantic computations/cpp/interaction_phase_form_factor.cpp -o /tmp/interaction_phase_form_factor
/tmp/interaction_phase_form_factor
lean formalization/Bgs/PhaseFormFactorRational.lean
```

Lean 4.33.1 exited 0. Aggregate `lake build` was not run. The new module imports only the Lean prelude. The C++ binary exits 0 with no pedantic warning.

## Non-claims

A pass does not prove BGS-TRACE-005 or BGS-BGS-001, a revival limit, or the absence of every N-dependent antiunitary. The phase average is not the fixed kick.
