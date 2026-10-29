# BGS-TRACE-126 certificate

29 October 2026. The symbol arithmetic is exact: Python `fractions.Fraction` and independent C++ `int64` arithmetic. The cyclotomic witness and the prime-revival coefficient are exact. Matrix comparisons are float64 checks of the trace closure, the interaction picture and the two symmetries at dimension 7.

## Coverage

- The 32 Fourier modes, Hermitian symmetry, energy \(66033/160000\), parity energy \(663/4000000\), and majorant \(184981/160000\).
- The unreduced reversal sum \(66031/80000\), and the folded parity and reversal defects at every odd modulus from 3 through 77. Both vanish at \(N=7\) and are positive otherwise. The stable values hold for every odd \(N\ge 19\) (parity) and every odd \(N\ge 79\) (reversal).
- The nonzero cyclotomic element at \(N=11\), \(m=3\), and the identity \(D_2(41,5)=-111001473/32000\).
- Floating-point agreement of the Gauss-sum trace, the order-two coefficient, the interaction picture, and one two-pair torus average.

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
