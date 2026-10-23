# Repository conventions and scientific governance

**Status:** active repository process specification.

This document defines how the BGS research repository is organized as a long-term scientific record. It complements the mathematical claim ledger; it does not alter theorem status.

## 1. Canonical identity

The canonical project and repository name is **BGS**.

Active source, documentation, manuscript, workflow, package/project identifiers, generated links, and newly produced artifacts use the BGS name. Legacy identifiers may remain only inside immutable historical evidence or archival records when changing them would falsify a recorded filename, path, execution environment, hash, or delivered artifact.

## 2. Source-of-truth hierarchy

When two surfaces disagree, use the following order:

1. `record/claims.json` — current registered status, stable IDs and links; its generated human-readable view is `record/claim_registry.md`;
2. `record/claim_ledger.md` — dated narrative of status changes and evidentiary scope, consistent with the registry;
3. maintained proof sources in `mathematics/`;
4. explicit load-bearing external sources in `literature/`;
5. formal statements in `formalization/`, within their stated trust boundary;
6. reproducible verification sources in `computations/`;
7. promoted execution evidence in `evidence/`;
8. the consolidated manuscript, paper manifests, and README summaries;
9. historical records and Git history.

Historical material never overrides a later correction in the current claim ledger.

## 3. Scientific promotion rule

A substantive result is considered integrated only when the relevant layers agree:

- theorem statement, assumptions, proof, and boundary in `mathematics/`;
- claim status in `record/claim_ledger.md` and a stable ID/cross-links in `record/claims.json`;
- theorem index entry when the result is part of the maintained corpus;
- external theorem locator and hypothesis mapping in `literature/external_dependencies.json` when a source is load-bearing;
- verification or formalization when these materially increase confidence;
- manuscript integration when the result changes the long-form scientific narrative;
- explicit retraction or supersession record when an earlier route becomes false.

Finite computation may support a theorem route but may not be promoted into an asymptotic theorem.

## 4. Maintained versus generated material

Maintained mathematical sources are edited at their authoritative source location.

Generated manuscript chapters must be regenerated from their source or verified with a fail-closed synchronization check. Generated PDFs, logs, caches, and build trees do not belong in the active source tree unless they are deliberately promoted as evidence with provenance.

The consolidated manuscript has one active entry point:

`manuscript/BGS_unified.tex`.

Parallel manuscript roots are not maintained on `main`.

## 5. Evidence immutability

Evidence records describe what was actually run or delivered. Do not rewrite historical paths, artifact names, environment paths, source hashes, or execution metadata merely to make old records look current.

Corrections are appended through a new review, evidence object, or claim-ledger entry. Historical mistakes remain traceable.

## 6. Verification tiers

Use increasingly expensive verification only as needed:

1. structural/static repository audit;
2. exact small-instance and adversarial checks;
3. maintained Python verification;
4. independent C++ or alternative representation where valuable;
5. formal finite/algebraic checking in Lean;
6. manuscript synchronization and build;
7. full-workspace regression;
8. external referee-level proof audit.

A successful software run certifies only the proposition actually tested.

## 7. Branch and review discipline

Small editorial or mechanically checked changes may be direct, but theorem changes, status changes, new evidence, and cross-layer refactors should use a branch and pull request.

Research branches are temporary review surfaces, not parallel truths. They should be merged, superseded, or closed once their mathematical disposition is known. Force-updating the canonical branch to erase concurrent history is avoided.

## 8. Naming and links

Internal links should be relative whenever possible. Links that must point to GitHub use the canonical `ChurilovMaksim/BGS` repository.

Names of maintained tools, temporary CI directories, package/project identifiers, and new artifacts should use the `bgs` / `BGS` prefix consistently.

## 9. Publication architecture

The consolidated manuscript is a research record. Journal submissions should normally extract a coherent theorem family with a sharply bounded dependency set rather than treating the entire repository as a single article.

Every publication candidate should state:

- the exact theorem family being submitted;
- external theorem dependencies;
- which computations are proof-supporting and which are illustrative;
- the verification commit;
- unresolved neighbouring questions that are intentionally out of scope.

## 10. Long-term repository hygiene

Prefer one maintained implementation per scientific role, with independent implementations only when they increase verification value.

Retire obsolete publishers, duplicated manuscripts, stale experiment copies, and dead integration scripts after their history is safely preserved. Keep `main` navigable to a new researcher without requiring reconstruction of the project's chronological development.

The repository should remain usable in three modes: mathematical reading, independent verification, and historical audit. Stable proof paths are preferred over bulk renames; thematic navigation is maintained through `mathematics/topics/` and `record/mathematics_topics.json`.
