# Scientific contribution protocol

BGS is maintained as a scientific record. Contributions are reviewed by the
claim they change, not by the amount of code they contain.

## Change classes

Every pull request should identify one primary class:

1. **THEOREM** — a new theorem or a stronger theorem-level statement.
2. **CORRECTION** — a correction, weakened hypothesis, changed constant, or
   retraction.
3. **EXTERNAL-DEPENDENCY** — a new or changed use of a theorem from the
   literature.
4. **VERIFICATION** — an exact finite certificate, independent
   implementation, or regression.
5. **NUMERICAL** — descriptive finite-precision evidence.
6. **FORMALIZATION** — Lean source or trust-boundary change.
7. **PUBLICATION** — manuscript/exposition change with no stronger scientific
   claim.
8. **INFRASTRUCTURE** — repository, build, reproducibility, or governance
   change.

## Promotion contract

A theorem-level change is ready only when all applicable surfaces agree:

- a precise statement, hypotheses, proof, and boundary in `mathematics/`;
- a stable claim ID in `record/claims.json`;
- claim status in `record/claim_ledger.md`;
- dependencies in `record/scientific_dependencies.json`;
- exact external theorem locators in `literature/external_dependencies.json`;
- verification/formalization links when they materially reduce proof risk;
- manuscript integration when the long-form scientific story changes;
- an explicit correction/retraction record when superseding an older route.

Finite experiments must state the finite proposition they test. Numerical
agreement is not promoted into an asymptotic theorem.

## Required PR evidence

The PR body must state: scientific change class; affected claim IDs; source
files; verification commands actually executed; external theorem dependencies
added or changed; and any checks that could not run.

If GitHub Actions fails before allocating a runner (`runner_id=0`,
`steps=[]`), record it as an infrastructure non-run, never as a scientific
failure or pass.

## Branch discipline

The canonical branch is `main`. Research branches are temporary review
surfaces. After checks and review, accepted work is merged to `main`; branches
must not become parallel sources of scientific truth.

Do not force-update `main` to erase concurrent history.

## Evidence discipline

Historical evidence is immutable in meaning. Do not rename or rewrite a
recorded historical path, artifact name, execution environment, or hash merely
to make old evidence look current. Add a new record that supersedes or
interprets the old one.

See `REVIEWING.md`, `SOURCE_OF_TRUTH.md`, and
`docs/repository_conventions.md`.
