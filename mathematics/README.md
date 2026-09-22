# Mathematics

This directory contains the authoritative maintained mathematical derivations.
False or superseded routes are summarized in `../record/retractions.md` and
remain recoverable from Git history rather than being duplicated as current
source.

Stable proof-file paths are intentionally preserved. The thematic organization
is provided by [topic views](topics/README.md), whose complete membership is
machine-readable in `../record/mathematics_topics.json` and checked by the
scientific registry audit.

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
