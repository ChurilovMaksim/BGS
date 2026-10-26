# Research working rules

This is a mathematical research repository, not a claim of a solved BGS conjecture.

## Authorities and conventions

Read `SOURCE_OF_TRUTH.md`, `docs/repository_conventions.md`,
`RESEARCH.md`, `record/claim_ledger.md`, `record/claims.json`,
`mathematics/results.md`, and `mathematics/open_questions.md` before opening a route. Search the existing
proofs and research records before calling an argument new. The machine-readable registry and SOURCE_OF_TRUTH.md control current status;
the dated ledger explains changes and historical notes remain historical.

Use C f = f composed with A transpose when frequencies evolve by A.
Distinguish oriented A-orbits from signed orbits, classical from quantum
parameters, and fixed coupling from shrinking coupling. Do not change an
existing convention silently. Preserve the original hypotheses in an audit.

## Research cycle

Write the exact claim, dependency closure, success criterion, and cheapest
counterexample test. Pursue a route to a proof, counterexample, conditional
reduction, or identified missing implication. Record those outcomes rather
than a transcript. A closed subsidiary question is not BGS universality.

For each result, separate a mathematical proof, an external theorem with
its exact locator, a finite computation, a heuristic, and an open assumption.
A prior result rediscovered here must be credited as prior. No numerical
experiment, CI pass, source file, or agreement between implementations
establishes an asymptotic theorem by itself.

## Durable layout and review

- `mathematics/`: maintained proofs and their exact boundaries.
- `computations/verification/`: reproducible checks; declare arithmetic,
  inputs, coverage, exclusions, resource caps, and non-claims.
- `evidence/`: dated results with hashes, commands, and actual execution scope.
- `record/`: research outcomes and audits. Preserve indexed historical records.
- `literature/`: exact-source checks and priority limitations.
- `formalization/`: state whether each source was actually compiled and what
  proposition, rather than an entire unformalized argument, was certified.
- `manuscript/`: publication view synchronized with its stated source.

For the 22 September finite-orbit section, the September rule naming the
Markdown proof canonical is SUPERSEDED by the user-approved Pass-1 edition:
the TeX file (`manuscript/unified_sections/finite_orbit_resonance.tex`) is
the source of truth -- its hand edits carry the theorem environments and
global numbering, and regenerating it from Markdown would destroy them. The
Markdown note
(`mathematics/resonance-cohomology/finite_orbit_resonance_rigidity.md`)
remains a maintained proof, but it no longer governs the TeX section; the
sync script intentionally reports SKIP for this target. The same
TeX-canonical status holds for the other seven Pass-1/2 hand-edited
sections (`fixed_map_frontier`, `return_gas`, `return_position`,
`return_periodic`, `return_phase`, `return_general`, `return_obstruction`):
never regenerate these eight TeX files from Markdown, in either check or
write mode. The September reproduction record
(`record/research_pass_20260922.md`) remains historical. This paragraph is
the phase-7 seal-gate re-baseline (2026-10-26): it records the governed
Pass-1 supersession, while the v1 checked-replay seal still pins the
pre-edit AGENTS.md bytes and the portable replay is the live gate. Other
subsystems retain their existing documented build and validation procedures.

Do not delete unrelated or unread material to make a workspace look clean.
Do not relabel a partial local overlay as a full repository checkout. Report
local changes, commits, pushes, full builds, and limited checks separately.
The user authorized work on main; preserve a clean base, review the diff,
and do not force-push or rewrite history.
