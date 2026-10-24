# BGS consolidated research manuscript

## Trace closure edition, 22 October 2026

The [new section](unified_sections/spectral_trace_closure_20261022.tex)
closes TRACE-109/110 and presents TRACE-112/113. The current three-pass
build has **324 pages**, no unresolved references or citations, and no
horizontal overflow. The new section's three pages were visually inspected;
two inherited long-path overflows were corrected by typesetting alone.
[Build receipt](../evidence/executions/20261022/trace-closure/manuscript_build.json)
and [scientific review](../record/spectral_research/trace_closure.md).
Earlier build counts and warnings below refer to their dated revisions.
The microscopic signed hierarchy and BGS remain open.


## Final spectral edition, 21 October 2026

The new [spectral section](unified_sections/spectral_final_20261021.tex)
summarizes TRACE-108--111 with exact proved/conditional boundaries.
The current three-pass build has **322 pages**, no unresolved references,
and no overflow in the new section. Three new-section pages were inspected.
Two inherited long-path overflows remain in older sections and are recorded
in the [build receipt](../evidence/executions/20261021/spectral-final/manuscript_build.json).
The [thematic proof edition](../mathematics/spectral_research/README.md)
and [integration review](../record/spectral_research/spectral_final_integration.md)
control mathematical status. Earlier dated build claims below refer to their
original source revisions.

[BGS_unified.tex](BGS_unified.tex) is the single maintained publication root
on `main`. It presents the research corpus; current registered status is
in [claims.json](../record/claims.json), with the dated narrative in
[the claim ledger](../record/claim_ledger.md), followed by canonical
mathematical sources under [mathematics/](../mathematics/README.md).

**Current continuation, 19 October 2026:** the new
[phase-cluster section](unified_sections/phase_cluster_continuation_20261019.tex)
records fixed-trace laws, the full four-port cancellation and second-defect sum,
the joint quartic family for tau<1/9, and the exact positive Cauchy-source boundary.
[Maintained mathematical sources](../mathematics/phase_ensemble_continuation_20261019.md)
control its scope. The feedback and fixed-channel implications retain their
explicit conditional inputs. The frozen-model signed hierarchy and BGS remain open.

The accepted three-pass build has **311 pages**, with no horizontal overflow
or unresolved references/citations and unchanged TeX input hashes.
[Build receipt](../archive/evidence/executions/20261019/repository-integration/manuscript_build_accepted.json)
and the rejected first-build logs are retained.
[Remote workflow disposition](../archive/evidence/executions/20261019/repository-integration/publication_c49e351.json)
records startup failures without executed code steps; remote build success is not asserted. The rejected build exposed an
inherited unbreakable source path; only its typesetting was corrected. Earlier page counts and visual checks refer to their original source
revisions; they do not certify this later section. The 12 October manuscript
summary's unresolved trajectory premise was subsequently addressed by TRACE-080
in its explicit startup/cutoff regime. Microscopic reference identification
and the fixed propagator remain separate open obligations.

The [scientific corpus atlas](../docs/corpus_atlas.md) maps the seven
principal subject areas to their canonical proofs, bibliography and evidence
and records why retained historical copies must not be deleted in bulk.

## Mathematical content and submission coverage

The [phase-channel/jet section](unified_sections/phase_channel_jet_20261008.tex)
presents TRACE-053/054/056, including the optimal matrix coefficient $4/3$,
and explicitly retains TRACE-055 as verification-pending. TRACE-055 is
therefore not in the same status class as TRACE-053/054/056: it has no
maintained proof source in `mathematics/` (its registry source is the
dated research checkpoint `record/research_checkpoint_20261008.md`) and
must not be cited as a reconstructed analytic result. The
[attached-PDF review](../literature/phase_channel_jet_sources_20261008.md)
states which final-section assertions have maintained proofs and which
remain unpromoted. The consolidated build is not a blanket acceptance of
the submitted 293-page article.

The fixed-map chapter includes FM-018/019's auxiliary gap results. FM-020's
[original-channel theorem](../mathematics/original_channel_gap.md) closes the
original two-copy microscopic-rate question. Nonlinear quenched control,
higher-copy estimates, signed noise removal and deterministic BGS retain
separate open boundaries. Earlier wording about the original rate is
superseded at precisely this scope.

## Maintained and generated sources

| Source | Editing rule |
|---|---|
| Six `unified_sections/return_*.tex` chapters | Edit the maintained Markdown proofs; regenerate with `computations/maintenance/sync_return_sections.py` |
| Fixed-map frontier | Edit `mathematics/fixed_map_resolvent_frontier.md`; use `computations/maintenance/sync_fixed_map_section.py` |
| Finite-orbit resonance chapter | Edit its registered Markdown authority; use `computations/maintenance/sync_finite_orbit_section.py` |
| Other included TeX sections | Maintain directly, respecting their registered mathematical sources and status |

Each synchronizer accepts `--check` to detect drift. The complete contracts
are in [generated_sources.json](../record/generated_sources.json).
Sequential `*_partN.tex` files are non-overlapping source segments, included
in order to preserve recovered text bytes. They are not competing manuscripts.
Return-law equation tags use the `Ret.` prefix.

A read-only [TeX source/citation audit](../computations/maintenance/audit_manuscript_references.py)
checks the complete included source closure, citation keys and bibliography
uniqueness before both CI manuscript builds. It reports unresolved or
duplicate cross-reference labels separately, without pretending that a
well-formed reference establishes mathematical validity.

## Sections retained outside the consolidated build

Two files in `unified_sections/` are **not** part of the build rooted at
[BGS_unified.tex](BGS_unified.tex):

| File | Status |
|---|---|
| `unified_sections/cayley_curve_uniform.tex` | Excluded from the build; retained as historical material |
| `unified_sections/intermediate_old_layers.tex` | Excluded from the build; retained as historical material |

This exclusion is a recorded editorial fact; it is not a claim that their
contents are superseded or lost. A decision on their final disposition
(reactivation, archival or removal) is the author's.

Eight further sections that do not appear as direct `\input` lines of
`BGS_unified.tex` are included indirectly, through
[final_delivery_note.tex](final_delivery_note.tex), which the root file
inputs; they are part of the build.

## Build

From the repository root:

```sh
python computations/maintenance/build_unified_manuscript.py --output-dir build/unified-paper
```

The builder writes generated artifacts under the requested output directory.
[REPRODUCE_unified.md](../REPRODUCE_unified.md) documents the environment,
source modes and wider verification procedure.

Focused [publication scopes](../papers/README.md) refer to canonical sources
without duplicating proof authority. Old standalone articles are recoverable
from Git history. The retained `finite_orbit_note.tex` is an immutable
execution input named by the [22 September manifest](../archive/evidence/20260922/run_manifest.json),
not a second maintained publication root.


## Editorial architecture for a continuing research manuscript

The current LaTeX title, PDF metadata, and abstract explicitly identify
the programme's central **open** deterministic spectral target and distinguish
the BGS 1984 GOE motivation from this unitary-class Sine$_2$ model.
The structure and order of all incorporated scientific sections are preserved
to maintain the research record; readers should not infer theorem
dependencies from chapter adjacency. The PDF bibliography now includes both
the original BGS paper and the cited loop-equation characterization, and
uses published metadata for the Lounici–Meziani–Peyré tomography article.



The full manuscript is deliberately retained and maintained as an **ongoing
research monograph**. It is not a completed BGS proof, a journal-ready
single-result paper, or a disposable log. The long chronological development
remains useful, but later sections must be read subject to the current
[claim ledger](../record/claim_ledger.md) and explicit corrections.

For readers interested in the original central question, use this route:
[exact model and fixed-map frontier](../mathematics/fixed_map_resolvent_frontier.md)
→ [joint-trace bridge](../mathematics/trace_to_local_statistics_bridge.md)
→ [actual-map intensity/path theorems](../mathematics/position_chain_mixing.md)
→ [balanced pair frontiers](../mathematics/phase_ward_identity.md)
→ [still-open obligations](../mathematics/open_questions.md).
For the broader mathematical programme, follow the
[topic navigator](../mathematics/topics/README.md) and the manuscript
table of contents. The research programme has multiple related but
noninterchangeable asymptotic regimes.

**Editorial guardrails:** preserve the existing TeX root, section input order,
stable labels, theorem statements and protected generated sections unless
their authoritative mathematics is deliberately re-reviewed. Improve the
reader-facing entry points and supplement them with explicit source links
rather than repeatedly reworking the manuscript or silently changing old
proofs. The [editorial reading map](../docs/editorial_guide.md) states the
protocol. A successful LaTeX build is typesetting evidence, not proof evidence.

## Current integration and verification

[The research record](../record/README.md) indexes the 11–19 October continuations.
[The repository audit](../archive/record/repository_reconciliation_20261020.md) records current
source/build checks separately from historical receipts. Integration does not
imply submission, independent refereeing or BGS closure.
