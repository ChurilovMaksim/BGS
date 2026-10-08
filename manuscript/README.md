# Consolidated manuscript

[BGS_unified.tex](BGS_unified.tex) is the single maintained publication root
on `main`. It presents the research corpus; the scientific-status authority
is [the claim ledger](../record/claim_ledger.md), followed by canonical
mathematical sources under [mathematics/](../mathematics/README.md).

The current verified build is **280 pages**. The
[8 October build and visual-review packet](../evidence/executions/20261008/phase-channel-jet/README.md)
records a three-pass build without unresolved references/citations or
horizontal overflow. Its visual inspection covers the revised title, four
new continuation pages and a bibliography page; it does not re-certify every
historical page or proof.

## Mathematical content and submission coverage

The [phase-channel/jet section](unified_sections/phase_channel_jet_20261008.tex)
presents TRACE-053/054/056, including the optimal matrix coefficient $4/3$,
and explicitly retains TRACE-055 as verification-pending. The
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
execution input named by the [22 September manifest](../evidence/20260922/run_manifest.json),
not a second maintained publication root.


## Editorial architecture for a continuing research manuscript

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
