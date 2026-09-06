# Temporal resonance hierarchy and spectral modules

Proof authority: `manuscript/unified_sections/temporal_resonance.tex` and
`manuscript/unified_sections/spectral_modules.tex`, both included by the single
canonical master `manuscript/WoW_unified.tex`.

For every hyperbolic A in SL(2,Z) and nonconstant real finite Fourier symbol g,
h_r={g,C^r g}/(4 pi) are independent modulo L2 coboundaries. The highest-lag
support lemma excludes every other iterate, not just a finite orbit window.
Quadratic temporal cancellations are exactly the zero lag-diagonal sums.
For finite filters P,Q the criterion is P(z^-1)Q(z)=P(z)Q(z^-1); second-order
self-response classes agree exactly when finite autocorrelations agree.

The continuation proves freeness of all h_r over the temporal Laurent ring,
all-frequency spectral positivity, and window-uniform Riesz bounds for each
fixed finite set of lags. For every finite Fourier symbol, the high-lag
coercivity exponent is classified by the common divisor of its orbit filters
at the two hyperbolic circles. A one-harmonic repair has the uniform crossover
(n^(-2q)+epsilon^2)^2. These are classical observable-covariance theorems.

The quantum continuation gives an exact cyclic module and all-time variance
for regular semisimple finite quantum maps. It includes odd periods, balanced
phases at even periods, and a factor-four rank loss at purely real/imaginary
phase for even periods. It is not an eigenphase-universality theorem.

## Reproduction

From a complete checkout:

```sh
mkdir -p build/temporal
python computations/verification/extremal_resonance.py --cases 1000 --max-lag 10 --algebra-cases 20 --output build/temporal/extremal.json --replay build/temporal/extremal.replay
c++ -std=c++20 -O2 -Wall -Wextra -Wpedantic computations/cpp/extremal_resonance_replay.cpp -o build/temporal/extremal_replay
build/temporal/extremal_replay build/temporal/extremal.replay
python computations/verification/temporal_soft_modes.py --output build/temporal/soft.json
python computations/verification/temporal_quantum_variance.py --output build/temporal/quantum.json
python computations/verification/spectral_module_regression.py --output build/temporal/modules.json
python computations/verification/general_symbol_covariance.py --output build/temporal/general.json
python computations/verification/quantum_cyclic_module.py --prime-limit 251 --output build/temporal/cyclic.json
python computations/verification/quantum_phase_completion.py --prime-limit 131 --output build/temporal/phase.json
python computations/verification/cayley_scaling_rigidity.py --prime-limit 251 --output build/temporal/cayley.json
```

Geometry, orbit sums, sparse Gram matrices and rational Rayleigh quotients use
exact arithmetic. Dense quantum matrices and displayed numerical eigenvalues
are explicitly floating-point diagnostics. Tests are not proofs of limits.
`formalization/drafts/TemporalCancellation.lean` contains only a telescoping
kernel and finite identities; its compilation has not been verified here.
No full BGS result, external priority, or independent referee acceptance is
claimed. The completed proofs concern the stated finite-Fourier and finite-
field scopes, not arbitrary analytic symbols or kicked spectral statistics.
