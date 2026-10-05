# Computations

[heisenberg_pair_heat_formula.py](verification/heisenberg_pair_heat_formula.py)
checks exact hook Gram matrices, cut-and-join and two mixed generators,
complete Wick compensation on genuine diagonal unitaries, triangular
mode multiplicities and finite contour exponents. Arithmetic is rational.
The separate [Wolfram source](verification/heisenberg_pair_heat_checks.wl)
was evaluated. These checks do not certify analytic asymptotics, the
actual unperturbed Heisenberg traces or deterministic BGS.

[growing_degree_trace_projection.py](verification/growing_degree_trace_projection.py)
checks exact Wick/Gram and Mehler coefficients, actual unitary trace
designs, full tensor Casimirs, high-band blindness/covariance and
independently enumerated permutation cut-and-join versus the top-Wick
generator. Arithmetic is rational; composition counts are bookkeeping,
not an analytic packet or BGS certificate.

[clock_structure_and_heat_projection.py](verification/clock_structure_and_heat_projection.py)
checks rational Fourier selection, clock generator jets, compensated
mesh masses, Abel signs, stable Gram matrices and cross-block determinant
surrogates. Complex128 kernel and variance comparisons are diagnostics;
no stochastic trajectory or asymptotic theorem is computationally certified.

[local_moment_transport.py](verification/local_moment_transport.py)
integrates rational periodic windows exactly, checks packing witnesses
and collapsed-clock high-order failures, and differentiates low-degree
characters with the direct radial Laurent generator. The bounded packet
separates these controls from numerical unitary matching. It does not
simulate the enormous chain, certify asymptotic transfer or solve BGS.

[microscopic_noise_removal.py](verification/microscopic_noise_removal.py)
compares the mixed-trace generator with an independent direct radial Laurent
implementation in Fraction arithmetic, checks finite character/gap geometry
and records quadrature resolution for the local Laplace and Fredholm tests.
The [bounded packet](../evidence/executions/20261005/noise-removal/manifest.json)
contains 348 exact generator equalities and 630 charge-closure checks.
It does not certify all-order flatness, entropy, actual noise removal or BGS.

[coboundary_general_start.py](verification/coboundary_general_start.py)
checks exact exponents and Brownian normalization, 120-digit balanced
cluster traces, independent spectral matching and uniform-origin geometry,
Poisson/Möbius and clock-potential bounds, and the prior arbitrary-start kernel's finite
normalization. It does not sample Brownian endpoints, run enormous step
counts, prove global kernel asymptotics or establish deterministic BGS.

[circular_dyson_relaxation.py](verification/circular_dyson_relaxation.py)
independently calibrates sine interpolation, shifted backward heat,
rectangle orientation and the crossing residue against Fourier formulas.
Exact rational exponents check the balanced comparison rule. The bounded
packet records 144 residue cases and 32 heat cases; finite quadrature
does not certify the analytic contour/Fredholm proof.

[resonant_density_audit.py](verification/resonant_density_audit.py)
checks signed Fourier/Holder identities and all counterterms, exact
realizable clusters, all-band CUE covariance and independent density
moments. The [Wolfram checks](verification/resonant_density_checks.wl)
were executed. No frozen-map density or BGS estimate is inferred.

[signed_heisenberg_audit.py](verification/signed_heisenberg_audit.py)
checks exact CUE cycles/covariances against independent representations,
finite absolute-norm bounds and a negative spectral-moment determinant.
[Wolfram algebra](verification/signed_heisenberg_checks.wl) was actually
evaluated. Neither certifies an asymptotic estimate for the frozen map.

[prime_resonant_audit.py](verification/prime_resonant_audit.py) checks
exact prime orders, split/nonsplit parity, -98/29/97 orbit arithmetic,
control matrix orientation and Fejer combs. Tiny frozen coupling and
asymptotic cancellation are not numerically certified.

[heisenberg_note_audit.py](verification/heisenberg_note_audit.py)
checks exact symbol/annihilator and analytic-constant arithmetic, finite
CUE factorial cycles against two existing references, rational digit
geometry and independent matrix conventions. Finite checks do not certify
the analytic action proof, external FUP theorem or deterministic CUE.

The maintained computational surface is deliberately compact and independently cross-checked. Historical language ports, one-shot publication migrators, and exploratory branch source trees are not kept as parallel implementations on `main`.

## C++20 — exact/exhaustive kernels

`cpp/` contains the independent exact finite verifiers, including the Cayley energy/resultant kernels, Pell relation/orthogonality checks, fixed-strength locality checks, hyperbolic-period checks, and the noncommuting return-word certificate. Every tracked `.cpp` file must occur in `CMakeLists.txt`; `repository_audit.py` enforces that invariant.

## Python — checked arithmetic and orchestration

`python/bgs/` contains the maintained finite-field, discrete-log, pair-key and twisted-Jacobi primitives with fail-fast validation.

`verification/` contains the scientific gates and exact/finite regressions.
[`nonlinear_pressure_variance.py`](verification/nonlinear_pressure_variance.py)
independently assembles the physical symbol and checks the exact rational
Fourier variance for `BGS-FM-006`; its finite arithmetic does not prove
the pressure theorem.
[`gram_resolvent_normalization.py`](verification/gram_resolvent_normalization.py)
cross-checks finite Toeplitz Gram norms, two-clock Abel sums, the pair
Poisson kernel and adjoint resolvent for `BGS-TRACE-008`/`BGS-RES-006`.
It verifies normalizations, not a limiting spectral theorem.
`verification/scientific_registry_audit.py` checks the machine-readable claim,
dependency, paper, evidence, environment, and topic contracts before expensive
science runs. `maintenance/render_claim_registry.py --check` prevents the
human claim index from drifting from `record/claims.json`.
`maintenance/verify_workspace.py` orchestrates scientific Python/C++
execution without mutating committed evidence. `maintenance/build_unified_manuscript.py`
is the sole maintained consolidated-manuscript builder.

`maintenance/sync_return_sections.py` is the maintained Markdown-to-TeX
synchronizer for the six return-law chapters. It transforms document links
through the Pandoc syntax tree so mathematical brackets are not rewritten as
links. `--check` detects stale generated source.

For focused execution, repeat `verify_workspace.py --only NAME`; the
[reproduction guide](../REPRODUCE_unified.md) gives the return-law selection.
Focused execution is recorded in the manifest and does not claim full coverage.

The return-local-limits verifier checks exact rational window probabilities
for simple spectral clouds, including an independent brute-force enumerator.
Separate floating and symbolic controls check density transport, its origin
Jacobian, and free Brownian support-gap calculus. The Wolfram cross-check is
retained in [return_gap.wl](verification/return_gap.wl); the full Python
entry point is [return_local_limits.py](verification/return_local_limits.py).
Neither program proves weak process convergence or the analytic return law.

One-shot scripts that used to integrate research branches into older standalone papers have been retired from `main`; their history remains in Git. New scientific work should change the canonical source/verifier directly rather than regenerate superseded article copies.

`analysis/spectral_diagnostics.py` and the figure scripts retain useful finite numerical experiments with corrected semantics. Their outputs are descriptive/regression evidence and are not promoted to asymptotic or microscopic BGS theorems.

## Language policy

- **C++20:** expensive exact enumeration and independent finite verifiers.
- **Python:** symbolic/exact orchestration, transparent reference implementations and finite numerical analysis.
- **Lean 4:** formal finite certificates and falsifiers.
- **TeX:** the single consolidated manuscript source.
- **Fortran:** introduce only if profiling identifies a genuine dense numerical hot path that materially benefits from it.
- **Julia:** retired; zero tracked `.jl` sources and no tracked Julia project environment.

The goal is not a language percentage. It is one maintained implementation per scientific role, with independent checks where they materially increase confidence.
## Recovered fixed-map computations

The source and historical finite evidence for the fixed-map continuation
are indexed in [the supplement](../supplement/fixed_map/README.md).
Run `python computations/maintenance/verify_fixed_map_supplement.py` from
the root for inventory/syntax checks and 28 isolated replays. The runner
keeps generated outputs under `build/` and does not overwrite evidence.
This complements the existing whole-workspace runner.

The late 20--21 September continuation also has a compact exact regression
gate at `verification/bgs_20260921_regression.py`.  It checks the
three-orientation algebra, Fourier-line recurrence identities, the frozen
full-symbol variance, and the local-jet negative control.  It is included
automatically in a complete `verify_workspace.py` run.  Its scope is exact
finite/symbolic regression only, not proof of the analytic asymptotic
theorems or fixed-`tau` BGS.

The 23 September verifiers `frozen_full_lag_gap.py` and
`frozen_kick_rank.py` check the exact physical-symbol expansion and finite
Jacobi/rank diagnostics, respectively. Both are discovered by the whole-
workspace runner and write scoped JSON outputs under its log directory.
Their finite runs are not proofs of the infinite-lag or all-dimension claims.

The submitted article's three retained 24 September checks are
[`frozen_seven_cut.py`](verification/frozen_seven_cut.py),
[`frozen_total_minors.py`](verification/frozen_total_minors.py), and
[`frozen_antireversor.py`](verification/frozen_antireversor.py).
They replay finite geometry, 5-adic/Fourier subset arithmetic, and an
exhaustive integer cyclotomic certificate, respectively. All are included
in the full verification runner, have dated immutable reference outputs
under `evidence/20260924/`, and are available as focused selections.
The analytic and all-dimension steps are documented separately in
[`record/submitted_article_review_20260924.md`](../record/submitted_article_review_20260924.md).

The later [`frozen_arithmetic_traces.py`](verification/frozen_arithmetic_traces.py)
checks 1248 exact finite Weyl fixed-point cases and the rational
\(169/500\) orbit margin in `BGS-FM-010`; its dated reference is
[`frozen_arithmetic_traces.json`](../evidence/20260924/frozen_arithmetic_traces.json).
It runs in the whole-workspace suite and by `--only frozen_arithmetic_traces`.
It does not evaluate the kicked traces or validate the asymptotic BGS target.

The 4 October `verification/expansion_wavepacket_audit.py --output <path>` checks exact arithmetic, finite Weil characters, channels and odd coherent frames. `verification/expansion_wavepacket_checks.wl` is an exact algebra replay source; its execution status is recorded separately. Neither certifies a uniform Heisenberg estimate.
