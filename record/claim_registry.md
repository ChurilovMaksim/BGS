# Stable claim registry

This file is generated from `record/claims.json`. It is a navigation
surface, not an independent status authority; `claim_ledger.md` wins.

Core load-bearing claims, theorem bridges, and open programme obligations. The claim ledger remains the complete status authority and may contain additional scoped results not assigned a stable core ID.

| Claim ID | State | Title | Authoritative source | Boundary / closure |
|---|---|---|---|---|
| `BGS-BGS-001` | **OPEN** | Fixed-strength microscopic BGS universality for the maintained frozen map | [source](../mathematics/fixed_map_resolvent_frontier.md) | Prove the required model-specific Heisenberg-scale joint-trace or equivalent mixed-resolvent estimate on every compact Fourier support, then verify the stated unfolding and symmetry-class hypotheses. |
| `BGS-CAYLEY-001` | **PROVED** | Pair-key and fourth-moment reduction | [source](../mathematics/fourth_moment_reduction.md) | Finite-field reduction; not a microscopic spectral theorem. |
| `BGS-CAYLEY-002` | **PROVED** | Cayley additive-energy reduction | [source](../mathematics/cayley_additive_energy.md) | Reduces the mixed layer to additive energy; does not close the centered pointwise target. |
| `BGS-CAYLEY-003` | **PROVED** | Direct K^(8/3) Cayley energy bound in the explicit subgroup-size range | [source](../mathematics/cayley_direct_energy.md) | Applies in the stated range; it does not reach the centered K^(2+o(1)) target. |
| `BGS-CAYLEY-004` | **PROVED** | Uniform subgroup-curve Cayley energy bound | [source](../mathematics/cayley_curve_uniform.md) | Uniform K^(8/3)+K^4/p scale; does not prove centered quadratic pointwise energy. |
| `BGS-CAYLEY-005` | **OPEN** | Sharp centered pointwise Cayley energy target | [source](../mathematics/open_questions.md) | Prove the centered K^(2+o(1)) estimate, or an equivalent common-split-divisor theorem strong enough to imply it. |
| `BGS-FM-001` | **PROVED** | Frozen-model classical symmetry theorem | [source](../mathematics/fixed_model_symmetry_theorem.md) | Excludes ordinary C1 centralizers/reversors and relevant affine C1 conjugacies in the stated small-coupling range; does not exclude N-dependent quantum symmetries or prove BGS. |
| `BGS-FM-002` | **PROVED** | Odd-Pell full-symbol Gaussian crossover | [source](../mathematics/fixed_model_pell_crossover.md) | Frozen epsilon_K=tau N_K lies outside the proved bounded crossover window. |
| `BGS-FM-003` | **PROVED** | Fixed-map moment controls, falsifier, and perturbation transfer | [source](../mathematics/fixed_map_moment_control_and_transfer.md) | Low-order and one-orientation loop information does not identify CUE. |
| `BGS-FM-004` | **CONDITIONAL** | Three-orientation mixed-resolvent lower barrier | [source](../mathematics/three_orientation_resolvent_barrier.md) | Normalized mixed-residual decay hypotheses remain unproved for the frozen propagator. |
| `BGS-FM-005` | **PROVED** | Actual frozen-kick Jacobi decomposition and exact low-rank obstruction | [source](../mathematics/frozen_kick_rank_boundary.md) | Exact rank bound for every odd N and algebraic nonzero kick; approximate rank bound only before eigenphase wrapping. Does not imply mixed traces or local RMT. |
| `BGS-FORMAL-001` | **VERIFICATION-PENDING** | Active Lean algebraic/finite kernel graph | [source](../formalization/README.md) | Source presence does not establish compilation; analytic BGS theorems are not formalized. |
| `BGS-INFO-001` | **OPEN** | Full vanishing-noise tomography transition | [source](../mathematics/open_questions.md) | Determine matching minimax upper and lower transitions for the full moment class in the varying-noise regime. |
| `BGS-LOOP-001` | **CONDITIONAL** | Full mixed loop hierarchy implies target compact anchored correlations | [source](../mathematics/fixed_map_resolvent_frontier.md) | The external characterization is available; the model-specific approximate mixed hierarchy remains open. |
| `BGS-RES-001` | **PROVED** | Sharp Fourier-line resonance coercivity | [source](../mathematics/fourier_line_resonance_coercivity.md) | Closes Fourier-line classes in the stated coercive range; arbitrary two-dimensional analytic symbols remain open. |
| `BGS-RES-002` | **PROVED** | Local-jet resonance obstruction | [source](../mathematics/local_jet_resonance_obstruction.md) | Local polynomial counterexample; not a periodic torus counterexample. |
| `BGS-RES-003` | **OPEN** | All-members analytic resonance nondegeneracy | [source](../mathematics/open_questions.md) | Prove impossibility of a nonconstant real-analytic solution to the stated nonlinear coboundary equation, or construct one. |
| `BGS-RES-004` | **PROVED** | Smooth finite-orbit Poisson-bracket lag independence | [source](../mathematics/finite_orbit_resonance_rigidity.md) | A fixed finite number of signed A-frequency orbits, smooth observables and finite lag combinations. The analytic infinite-orbit and quantum BGS targets remain open. |
| `BGS-RES-005` | **PROVED** | Full-lag uniform classical Riesz gap for the frozen physical symbol under linear transport | [source](../mathematics/frozen_full_lag_resonance.md) | All positive lags and all linear-map translates; stable for arbitrary M1 perturbations of radius 1/100. Does not cover nonlinear transport, quantum Heisenberg traces, or BGS. |
| `BGS-RET-001` | **PROVED** | Harmonic return law for the actual kicked Pell propagator | [source](../mathematics/pell_harmonic_returns.md) | Fixed multiplicity and logarithmic return time; not Heisenberg-scale microscopic BGS. |
| `BGS-RET-002` | **PROVED** | Harmonic-scale global transition in the fixed Pell cat map | [source](../mathematics/pell_harmonic_transition.md) | Global compressed-observable law; not local eigenphase statistics of a fixed propagator. |
| `BGS-TRACE-001` | **PROVED** | Partition-Mobius formula for distinct-index spectral sums | [source](../mathematics/trace_to_local_statistics_bridge.md) | Deterministic finite-N identity. |
| `BGS-TRACE-002` | **PROVED** | Exact Fourier trace representation of microscopic factorial statistics | [source](../mathematics/trace_to_local_statistics_bridge.md) | Compact Fourier support probes trace powers of order N. |
| `BGS-TRACE-003` | **PROVED** | Weighted Heisenberg-scale joint-trace comparison is sufficient for band-limited microscopic RMT correlations | [source](../mathematics/trace_to_local_statistics_bridge.md) | Sufficiency theorem only; the required model-specific Heisenberg-scale estimate is open. |
| `BGS-TRACE-004` | **PROVED** | Every-compact-bandwidth comparison extends to Schwartz correlation tests | [source](../mathematics/bandlimited_correlation_extension.md) | Requires positive normalized spectral averages and a reference Schwartz limit; a single fixed bandwidth is insufficient. |
| `BGS-TRACE-005` | **OPEN** | Model-specific Heisenberg-scale desymmetrized joint-trace estimate | [source](../mathematics/open_questions.md) | Prove the correctly desymmetrized weighted joint-trace comparison, or an equivalent mixed-resolvent hierarchy, uniformly on every compact Fourier support. |
| `BGS-TRACE-006` | **PROVED** | Clustered Abel lower bound and simple-spectrum Heisenberg-window falsifier | [source](../mathematics/clustered_abel_window_boundary.md) | Abstract unitary spectra. The Abel consequence for the compensated Pell family depends on its separate project pinning theorem; no frozen-map mixed cancellation is asserted. |

External theorem dependencies are pinned in
`../literature/external_dependencies.json`; the maintained programme DAG is
in `scientific_dependencies.json` and `scientific_dependency_graph.md`.
