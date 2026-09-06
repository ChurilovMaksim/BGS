# Paper / manuscript corpus

The manuscript sources are retained because they contain useful exposition, theorem statements, computations, and patch history. **There is currently no proof-complete BGS manuscript.** Root `STATUS.md` controls mathematical status.

- `sections/` contains modular manuscript source material for future rewriting.
- `patches/` contains historical patch scripts; they are provenance and may use old paths.
- `final/` contains historical source/PDF snapshots once labelled final; the label is not a current correctness claim.
- `historical_snapshots/` collects additional duplicate/root paper snapshots.

`final/mobius_fiber_theorem.*` and the historical `M4D_PROOF.*` snapshot do not establish M1. The full audit also superseded the R86/R87 trace-fluctuation shortcut; manuscript text that depends on either route must be rewritten against current `THEORY.md` before promotion. See `research/M1.md`, `STATUS.md`, and `docs/audit/CLAIM_STATUS_MAP.md`.

The source/PDF corpus is intentionally preserved because exact identities, parametrisations, exposition, and failed routes are useful research material. A future current manuscript should be built from the audited dependency graph rather than by relabelling an old `final` file.
