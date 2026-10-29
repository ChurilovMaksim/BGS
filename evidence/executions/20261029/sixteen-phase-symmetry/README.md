# BGS-TRACE-130 certificate

Integer symbol energy and floating-point checks of the symmetric conjugate and the momentum sine. The antiunitary \(\Theta=DK_0\) is the proof, not this certificate. A pass checks `mathematics/fixed-map/sixteen_phase_symmetry.md`. It does not identify a COE or CUE form factor, and it does not prove BGS-TRACE-005 or BGS-BGS-001.

The scaled \(\ell=1\) energy is \(900\), so the symbol energy is \(9/160000\). At \(N=3,5,7,11\), a random real diagonal square root makes \(D^{1/2}M_ND^{1/2}\) symmetric, and \(B_N=(T_N(1,0)-T_N(-1,0))/(2i)\) is Hermitian and odd under position conjugation.

```sh
python3 computations/verification/sixteen_phase_symmetry.py
g++ -std=c++20 -O2 -Wall -Wextra -Wpedantic computations/cpp/sixteen_phase_symmetry.cpp -o /tmp/sixteen_phase_symmetry
/tmp/sixteen_phase_symmetry
```

Lean, toolchain `leanprover/lean4:v4.33.1`:

```sh
lean formalization/Bgs/SixteenPhaseSymmetryRational.lean
```
