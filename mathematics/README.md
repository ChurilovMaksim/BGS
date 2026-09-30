# Mathematics

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
limit, with a separate conditional fixed-time model input.

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
