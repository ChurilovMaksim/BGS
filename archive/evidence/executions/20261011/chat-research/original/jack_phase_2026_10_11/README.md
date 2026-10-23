# Phase averaging and frozen circular ensembles

Research checkpoint, 11 October 2026. This directory is independent of the BGS
repository, which has not been read or modified in this session.

The main result is a sharp, nonperturbative variance contraction for spectral
observables under independent diagonal phase averaging. It applies to a
scattering matrix first sampled from CUE, COE or CSE and then frozen.

For beta = 1, 2, 4, with N distinct eigenvalues (N Kramers pairs in CSE),

    Var_Q(E_D f(DQ)) <= Var_circular(f)/(N + 2/beta).

The constant is optimal. In CSE the diagonal phase is repeated on each pair.
A balanced Laurent Jack coefficient estimate proves the COE/CSE cases without
a trace-time truncation. It also gives the CUE coefficient estimate.

Consequently, the full conditional local point-process law converges in
probability, over the frozen scattering matrix, to the intensity-one Sine-beta
law. The comparison with the finite circular ensemble is quantitatively
O(N^(-1/2)) in the bounded Laplace-test metric.

An all-order CSE cumulant estimate further proves a complex Gaussian
trace limit for every growing order n/N→1, normalized by its exact
variance ~N log[N/(|n−N|+1)]/4. The conditional phase law and every
fixed conditional moment converge as well. At n=N there is a quantitative
characteristic-function comparison. The full CUE and CSE form-factor curves
converge in L² in rescaled time, including the integrable CSE singularity.

## Read in this order

- `jack_coefficient_theorem.md`: the algebraic theorem and a direct proof.
- `phase_contraction.md`: compact-group transfer, symmetry conventions and
  sharp test functions.
- `quenched_local_law.md`: conditional probability laws, tightness, scaling
  and exactly what the limit asserts.
- `heisenberg_form_factor.md`: unbounded form-factor comparison at n~N
  for all three ensembles, and at every positive n for CUE/CSE; the CSE
  mean and its logarithmic singularity are derived exactly.
- `exact_cumulants.md`: independent derivation of known finite cumulants,
  improved explicit all-positive-time conditional bounds, and attribution.
- `critical_cse_gaussian.md`: all-order bound, Gaussian critical boundary
  layer, conditional moments and the exact critical block factorization.
- `form_factor_curve.md`: complete CUE/CSE curve comparison in L².
- `sources_and_audit.md`: primary sources and independent audit.
- `previous_rank_results.md`: recovery of the prior unsaved collision/rank
  results, with separate statements of their remaining dependencies.
- `scripts/`, `formal/`, `runs/`: reproducible bounded computations and
  explicit formalization status.

The human proof is the justification for an arbitrary N and signature.
Finite computations are controls, not a replacement for that proof.
The Lean source, if present, is an uncompiled draft of the arithmetic core:
Lean and Mathlib are not installed in this environment.

## Scope

This is a theorem for a random scattering matrix subsequently frozen.
It does not prove BGS for a prescribed deterministic chaotic propagator,
including the Fourier scattering family. A mechanism transferring these
conditional laws to specified deterministic backgrounds remains unproved.
No claim of scientific priority or prize-level novelty is made.

The exact ensemble mean and fourth-cumulant identities are known from
Haake–Sommers–Weber (1999). The sharper phase theorem and the all-order
critical statements are proved here, but their priority has not been settled.

The exact theorem applies to every square-integrable spectral observable.
The form-factor conclusion uses a separate fourth-moment proof; it is not
inferred merely from weak convergence of the local process. Correlation
densities and time maxima are not claimed.

