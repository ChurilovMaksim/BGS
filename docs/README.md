# Documentation map

`docs/` keeps the broad research record visible in ordinary working paths. It is not the authoritative source for present theorem status; use root `STATUS.md` for that.

## Current navigation

- root `RESEARCH_INDEX.md` — whole-program map and directory guide.
- root `STATUS.md` — authoritative theorem/draft/retraction boundary.
- `research/theory.md` — current detailed mathematical core.
- `research/ledger.md` — current research chronology.
- `research/problems/m1_fluctuation_energy.md` — present load-bearing M1 problem.

## Research corpus

- `literature/` — historical literature notes and source reconnaissance.
- `review/` — referee/red-team/model-review material and repository audits.
- `ideas.md` — accumulated research ideas.
- `cycle2_falsifier.md` — falsifier work retained as part of the solution history.
- `trace_fluctuation_lemma.md` — conjectural/draft trace-fluctuation work; respect its local status labels.
- `sp4_project_scope.md` — rank-2/Sp4 scope notes.
- `REVIEW_FINDINGS.md` — later review findings; prefer this when it conflicts with the older `REVIEW_ERRORS.md`.
- `REVIEW_ERRORS.md` — historical review report preserved because some findings were later corrected/refined.

## Detailed historical record

- `THEORY_FULL_PRE_REBUILD.md` — full pre-rebuild theory notebook. It contains valuable derivations and historical theorem labels, some of which are now retracted.
- `HISTORY_FULL_PRE_REBUILD.md` — full old research ledger, preserved verbatim. It contains known text-encoding mojibake from an earlier mishandling; this is a quality defect, not missing data.
- `archive/` — old run handoffs, ledger entries and snapshots retained at their original research granularity.

Historical Julia files that used to appear under `docs/archive/` or review scripts are intentionally absent from this active tree after the language migration. Their unique source copies remain in `archive/legacy-workspace/`; `research/engineering/language_migration.md` records the disposition of every Julia path.

When two documents disagree about whether something is proved, `STATUS.md` wins. Do not delete the older document merely because its conclusion was superseded: it may contain the derivation, counterexample, numerical design or literature trail needed for the next iteration.
