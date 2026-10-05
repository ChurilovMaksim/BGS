# Mathematics

[growing_degree_trace_projection.md](growing_degree_trace_projection.md)
gives the exact Wick evaluation cost, actual logarithmic projection
rate $N^{-1/4}$, universal degree-cost lower bound, sublinear blindness
to a fixed pair test and its particular Haar-$L^2$ inverse obstruction.
The complete actual complementary value remains open.

[clock_structure_and_noise_scale.md](clock_structure_and_noise_scale.md)
gives exact finite clock covariance, signed compensation, the sharp pair
rate and all-order critical limits.
[fixed_degree_heat_projection.md](fixed_degree_heat_projection.md)
estimates every fixed neutral projection for the actual map and proves
compact projected CUE agreement at $O(N^{-1/2})$. Its complement is open.

[local_moment_transport.md](local_moment_transport.md) proves a packing
theorem and all-order projected-to-Dyson transfer at $t^2\log N\to0$.
[coboundary_all_order_limit.md](coboundary_all_order_limit.md) extends the
actual-start original random chain to every fixed factorial order, with
one superpolynomial step sequence, $L^2$ origin averages and full signed
Fourier comparison. Its exact deterministic transfer condition is stated;
actual vanishing and full BGS remain open.

[microscopic_noise_removal.md](microscopic_noise_removal.md) proves the
exact integrated Laplace defect and four scoped transfer boundaries,
including all-order flat heat jets with a positive eventual defect and
an actual-map obstruction to unscaled full-class stationarity.
Deterministic signed noise removal remains open.

[coboundary_general_start.md](coboundary_general_start.md) preserves the
bounded-trace original start in the stochastic comparison.
[dyson_relaxation_obstruction.md](dyson_relaxation_obstruction.md) gives a
prescribed-time empty noisy limit. [frozen_mesoscopic_regularity.md](frozen_mesoscopic_regularity.md)
derives logarithmic initial density, local heat-phase stationary points
and exponentially suppressed unweighted vertical phase tails
from the existing trace window.
[circular_dyson_actual_start.md](circular_dyson_actual_start.md) closes
the circular kernel and Fredholm argument at t=8g and transfers Sine_2
to the original chain from the actual map. Deterministic BGS remains open.

[coboundary_polynomial_limit.md](coboundary_polynomial_limit.md)
closes the polynomial-step clock-to-Sine question for the original
random chain, with a dimension-uniform derivative proof and the earlier
$O_f(N^{-1/3})$ smooth-test rate. The deterministic BGS target stays open.

[resonant_cubic_density_control.md](resonant_cubic_density_control.md)
proves the local-density resonant cubic deletion, its critical tail boundary
and a deterministic pair-compatible cluster obstruction. Actual-map
hypotheses and BGS remain open.

[signed_heisenberg_comparison.md](signed_heisenberg_comparison.md)
proves the universal absolute-norm obstruction and separates signed
CUE calibration from an unrealized phase table and the actual-map frontier.

The [Heisenberg-note completions](../record/heisenberg_note_review_20260930.md)
add scalar finite type, an explicit classical action remainder and an
ideal-alphabet Fourier FUP classification, with separate quantum boundaries.

This directory contains the authoritative maintained mathematical derivations.
False or superseded routes are summarized in `../record/retractions.md` and
remain recoverable from Git history rather than being duplicated as current
source.

Stable proof-file paths are intentionally preserved. The thematic organization
is provided by [topic views](topics/README.md), whose complete membership is
machine-readable in `../record/mathematics_topics.json` and checked by the
scientific registry audit.

The [quadratic-noise continuation](../record/quadratic_noise_review_20260929.md)
links the covariance, coupling, reversibility, trace CLTs and clock local
limit. Its bounded fixed-time model input is now proved by the separate
[odd-N packet/frame argument](fixed_time_wavepacket_trace_bound.md);
the sharper historical Faure adaptation remains conditional.

## Reading order

The current fixed-family branch is consolidated in
[fixed_map_resolvent_frontier.md](fixed_map_resolvent_frontier.md), with
[full supplementary derivations and computations](../supplement/fixed_map/README.md).

1. `results.md` — concise theorem index.
2. `open_questions.md` — current closure obligations, keyed to stable claim IDs.
3. `trace_to_local_statistics_bridge.md` — exact deterministic route from joint traces to microscopic tests.
   `clustered_abel_window_boundary.md` records a sharp limit of what cluster
   and Abel information alone can infer about positive Heisenberg-time windows.
4. `fixed_map_resolvent_frontier.md` — maintained frozen-model frontier.
   It now contains the exact adjoint-resolvent representation of the pair
   Abel limit, its universal regular-polygon lower floor, and smooth
   scalar-resolvent transfer to the seven-cut **full** propagator;
   `two_clock_gram_falsifier.md` rules out a tempting sufficiency claim
   even with simple, weakly Haar spectra and bounded local occupancy;
   `frozen_spectral_flow_controls.md` audits the phase-flow identities,
   ordered kick product, and isospectral control example.
   `frozen_kick_rank_boundary.md` and `frozen_full_lag_resonance.md` record
   the exact kick-rank and linear-transport classical results, respectively.
   `nonlinear_bracket_pressure.md` determines the failure of the same
   normalization for nonlinear classical transport; none supplies the open
   Heisenberg-scale quantum estimate. The 24 September continuation
   `frozen_seven_cut_reduction.md`, `frozen_algebraic_spectral_simplicity.md`
   and `frozen_common_antireversor_certificate.md` record a fixed-coupling
   reduction and scoped qualitative spectral obstructions. The later
   `frozen_arithmetic_trace_rigidity.md` and `frozen_effective_gap_floor.md`
   give exact trace nonvanishing and a submicroscopic explicit gap floor;
   none supplies that estimate.
5. `fourth_moment_reduction.md` and `cayley_additive_energy.md` — exact pair-key and Cayley reductions.
6. `general_cat_return_laws.md`, `pell_harmonic_transition.md`, and `pell_harmonic_returns.md` — global return/observable laws with explicit microscopic boundaries.
7. `topics/README.md` — thematic navigation across the full maintained corpus.
   `finite_orbit_resonance_rigidity.md` contains the 22 September smooth
   finite-orbit theorem and its explicit infinite-orbit boundary.
8. `earlier_foundations.md` — older results that survived audit in their safe present scope.

The old `elliptic_pencil.md` is retained as a historical theorem-draft route;
the maintained corrected off/off result is
`offoff_elliptic_spike_theorem.md`.

## Evidence levels

- **EXACT** — current algebraic/analytic derivation with explicit hypotheses;
- **EXACT + EXTERNAL-THEOREM** — exact project reduction whose input is an identified external theorem;
- **FINITE-CERTIFICATE** — exact finite statement at explicit parameters;
- **FINITE-REGRESSION** — finite implementation/reference agreement;
- **NUMERICAL** — descriptive floating-point evidence only;
- **DRAFT** — route with named unresolved obligations;
- **OPEN** — closure condition not achieved;
- **RETRACTED / SCOPED-HISTORICAL / NOT-PROMOTED** — no current theorem authority.

Repository-wide status authority is `../record/claim_ledger.md`.
`../record/claims.json` assigns stable IDs and cross-layer links but does not
override the ledger. Dated addenda and reviews are historical/source records;
their surviving conclusions matter only insofar as they are incorporated into
the current ledger and maintained proof sources.

Neither a finite verifier, a source file, nor a manuscript sentence may
silently strengthen the current claim ledger.
