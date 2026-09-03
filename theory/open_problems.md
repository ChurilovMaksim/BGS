# Open problems

## Primary target: microscopic BGS statistics

Prove a GOE/GUE-type local eigenphase law for an explicit asymptotic family of quantized hyperbolic cat maps after all relevant exact arithmetic symmetries are removed.

No current result in this repository proves this target.

## A. Close the restricted M1 theorem

Discharge the two obligations in `elliptic_family.md`:

1. algebraic/projective/no-isogeny certificate for the elliptic family;
2. exact uniform trace-sheaf correlation theorem with every hypothesis checked.

This is the highest-value next proof task: it either converts the strongest current route into a theorem or identifies a precise obstruction.

## B. Formalize the exact finite layer

Extend Lean from finite design certificates to generic statements where practical:

- pair-key bijection off the diagonal;
- diagonal multiplicity `N-2`;
- exact `k=2` count `(K-1)(K-2)`;
- exact `V4` inclusion-exclusion formula;
- character-orthogonality collapse to `B(t)`;
- finite Fourier mean/variance identity;
- Cayley transform `d=2/(c(u)-c(v))`.

Lean is a verification track, not a substitute for the l-adic analytic step.

## C. Find the actual bridge from M1 to local statistics

Do not assume a generic Wigner-matrix theorem applies. The arithmetic matrix entries are strongly structured.

A viable local-law program must first specify:

- the correct matrix/resolvent object;
- exact dependence and symmetry structure of entries;
- a comparison, cumulant, Dyson-flow or trace-function mechanism that survives those dependencies;
- the scale at which arithmetic correlations fall below the microscopic spectral error budget.

Only then is it meaningful to import random-matrix local-law technology.

## D. Higher rank

Rank-2/Sp(4) computations are not part of the active theorem chain. Re-enter higher rank only after the rank-1 mechanism is rigorous enough to separate representation-theoretic structure from one-dimensional accidents.

This prevents the historical mistake of promoting low-rank numerical flatness to a general `Sp(2g)` theorem.