# Reproducible computations

The maintained programs check exact finite identities, enumerate bounded
cases, run numerical controls and build publication/formalization artifacts.
Every output must state its arithmetic and coverage. Passing a computation
cannot supply a missing analytic limit.

[The reproduction guide](../REPRODUCE_unified.md) gives environment pins,
whole-workspace commands and Git/archive source modes. Commands below run
from the repository root. Generated results belong under `build/` or a
specified temporary output directory; committed historical evidence is not
an output target for a replay.

## Languages and scientific roles

| Surface | Role |
|---|---|
| [verification/](verification/) | Scientific gates, exact finite regressions and explicitly labelled quadrature controls |
| [python/bgs/](python/bgs/) | Validated finite-field, discrete-log, pair-key and twisted-Jacobi primitives |
| [cpp/](cpp/) | Independent C++20 exact/exhaustive verifiers; every tracked `.cpp` is registered in the root CMake target set |
| [wolfram/](wolfram/) and registered `.wl` checks | Symbolic identity sources; an execution claim requires an actual preserved evaluator response |
| [analysis/](analysis/) and [experiments/](experiments/) | Descriptive finite diagnostics and reproducible figures |
| [maintenance/](maintenance/) | Fail-closed source synchronization, evidence-aware orchestration and manuscript building |
| [formalization/](../formalization/README.md) | Lean finite/algebraic certificates, with explicit trust dependencies |

One maintained implementation per scientific role is preferred. Independent
representations are retained when they materially improve verification.

## Phase-channel and matrix-jet controls

| Source | Actual finite check |
|---|---|
| [phase_channel_jet.py](verification/phase_channel_jet.py) | Complex phase-character quadrature, noncommuting cascade identities, inner-function jet and scalar real-flow quadrature |
| [phase_occupation_jet_verifier.cpp](cpp/phase_occupation_jet_verifier.cpp) | Exact independent occupation multiplicities at degrees two and three |
| [phase_channel_jet.wl](wolfram/phase_channel_jet.wl) | Poisson differential and count-polynomial identities |
| [microscopic_pair_reference.py](analysis/microscopic_pair_reference.py) | Analytic Sine2/Poisson reference figure for the README; no sampled map spectra |

The [8 October packet](../evidence/executions/20261008/phase-channel-jet/README.md)
records commands, source hashes, tolerances and actual execution. Replay to a
fresh output location:

```sh
python computations/verification/phase_channel_jet.py --output build/phase-channel-jet.json
c++ -std=c++20 -O2 -Wall -Wextra -Werror computations/cpp/phase_occupation_jet_verifier.cpp -o /tmp/bgs-phase-occupation
/tmp/bgs-phase-occupation
python computations/analysis/microscopic_pair_reference.py
```

These controls accompany TRACE-053/054/056. They do not certify the submitted
deep-source barriers, anisotropic source hierarchy or BGS.

## Selected verification families

| Family | Entry points and boundary |
|---|---|
| Frozen-map arithmetic | [frozen_arithmetic_traces.py](verification/frozen_arithmetic_traces.py), [prime_resonant_audit.py](verification/prime_resonant_audit.py): exact bounded modular/character controls; tiny fixed coupling and Heisenberg cancellation are not simulated |
| Actual transfer and common-noise gaps | [operator transfer](verification/frozen_operator_transfer_coercivity.py), [collective diffusion](verification/collective_diffusion_gap.py): exact cyclotomic/rational controls; the [spectrum experiment](experiments/collective_diffusion_spectrum.py) is separately float64 |
| Joint traces and heat | [signed Heisenberg](verification/signed_heisenberg_audit.py), [pair heat](verification/heisenberg_pair_heat_formula.py), [growing-degree projection](verification/growing_degree_trace_projection.py): finite generators, characters and normalizations; not actual asymptotic trace estimates |
| Noisy local laws and removal | [general start](verification/coboundary_general_start.py), [circular relaxation](verification/circular_dyson_relaxation.py), [moment transport](verification/local_moment_transport.py), [noise removal](verification/microscopic_noise_removal.py): bounded exact/quadrature controls, not enormous stochastic-chain simulation |
| Unmasked insertions | [wave3_checked_replay.py](verification/wave3_checked_replay.py), [wave3_integration_audit.py](verification/wave3_integration_audit.py): source-bound exact/floating replay and separate lineage/scope checks |
| Return/local laws | [return_local_limits.py](verification/return_local_limits.py), [return_gap.wl](verification/return_gap.wl): finite window, normalization and calculus checks; weak process limits require the analytic proof |
| Frozen-map supplement | [supplement guide](../supplement/fixed_map/README.md), [verify_fixed_map_supplement.py](maintenance/verify_fixed_map_supplement.py): preserved inputs and isolated bounded replays |

Other maintained verifiers remain at their stable paths and are indexed by
the corresponding theorem, topic and evidence manifest.

## Repository and publication gates

[scientific_registry_audit.py](verification/scientific_registry_audit.py)
checks claims, dependencies, paper scopes, evidence, environment and topics.
[repository_audit.py](verification/repository_audit.py) checks structural
contracts and active-source navigation. These are consistency gates, not
mathematical proof audits.

```sh
python computations/maintenance/render_claim_registry.py --check
python computations/maintenance/sync_return_sections.py --check
python computations/maintenance/sync_fixed_map_section.py --check
python computations/maintenance/sync_finite_orbit_section.py --check
python computations/maintenance/build_unified_manuscript.py --output-dir build/unified-paper
```

The [workspace runner](maintenance/verify_workspace.py) supports repeated
`--only NAME` selections. Focused execution is recorded as focused; a full
run must use the actual complete source inventory. Do not synthesize a Git
checkout identity for a partial overlay or ZIP.

## Input and diagnostic contracts

[The assertion policy](maintenance/ASSERTION_POLICY.md) distinguishes scripts
that reject optimized Python from explicit-check-only controls. Replays must
respect fresh/empty output-directory requirements and preserve failures.
Exact output comparison excludes execution metadata only where the registered
contract says so.

[The spectral correction record](../record/audits/spectral_diagnostics_correction_20261006.md)
replaces nonmonotone polynomial unfolding with an order-preserving procedure
and explicit sensitivity/undefined-value handling. Historical outputs remain
traceable; corrected finite diagnostics are still not an asymptotic law.
Finite surrogate parameters and changed operators must never be labelled as
spectra of the literal fixed-strength target.


## Portable successor to the sealed Wave2 floating split diagnostic

[Wave2 original v1](verification/wave2_checked_replay.py) remains SHA-sealed
by both historical Wave2 and Wave3 registries. Do **not** change its code,
source-binding hashes, archived inputs, numeric reference, or the original
`1e-12` reference-equality policy. Its `rounding` child chooses a Schur
basis within a repeated-eigenvalue subspace; a subsequent non-scalar diagonal
perturbation depends on that basis. This makes four printed numbers
(`reverse_norm` and `P_centered_norm` at both p=5 and p=11) legitimately
different across BLAS dispatchers. It is **not** evidence of a false
analytic bound.

The separate [portable v2 replay](verification/wave2_portable_replay.py)
authenticates every original source and executes **all eight** unchanged
historical programs and assertions, keeping raw observed/expected artifacts.
It retains *strict typed exact comparison* for all other scientific fields
and the original strict split and reconstruction inequalities. For exactly
four basis-dependent numbers it instead checks the mathematically
proved **basis-independent structural constraints** described in
[the derivation](../docs/wave2_schur_basis_portability.md).
A v2 receipt separately records the actual values, original v1 policy,
new mathematical bound, and whether v1's exact reference equality happened
to hold. It must not label a failed v1 equality as a v1 pass.

The complete workspace runs v1's `--check-sources` authenticator and v2's
full replay as **two separate named checks**. The historical v1 full replay remains executable but its
exact-reference behavior is machine-dependent. To run either version from
the repository root, supply a separate fresh output directory:

```sh
python computations/verification/wave2_checked_replay.py --output-dir build/wave2-v1
python computations/verification/wave2_portable_replay.py --output-dir build/wave2-v2
``` All established source protection stays active.
This is a numerical reproducibility correction, not a new BGS theorem.
