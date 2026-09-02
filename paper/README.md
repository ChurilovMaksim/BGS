# Paper / manuscript corpus

The manuscript sources are retained because they contain useful exposition, theorem statements, computations and patch history. **There is currently no proof-complete BGS manuscript.** Root `STATUS.md` controls mathematical status.

## Contents

- `sections/` — manuscript sections and modular source material retained for future rewriting.
- `patches/` — historical patch scripts used to modify manuscript sources. They are provenance and may contain old paths.
- `final/` — historical compiled/source snapshots that were once labelled final. The label is historical, not a current claim of correctness.
- `historical_snapshots/` — duplicate/root paper snapshots moved into one clearly historical location.

## Critical M1 warning

`final/mobius_fiber_theorem.*` and the corresponding historical `M4D_PROOF.*` snapshot do **not** establish M1. The audit found a load-bearing gap in the twist-summed energy argument, an invalid `O(1/K^2)=o(1)` promotion for fixed `K`, and an advertised envelope contradicted by the paper's own `K=17` numerical row. See `research/M1.md` and `STATUS.md`.

These sources remain in the repository because their exact identities, parametrisations and failed proof route are useful starting material. They must be edited against the current dependency graph before any new manuscript is promoted as current.