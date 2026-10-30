# Editorial reading map — BGS

This page is a **navigation and presentation guide**, not a theorem statement or proof certification. English is the primary public-facing language; [the Russian README](../README.ru.md) parallels the top-level account.

## Three complementary reading modes

**New reader:** [README](../README.md) → [background](reader_guide.en.md) → [research brief](../RESEARCH.md) → [open problems](../mathematics/open_questions.md). The README introduces the original conjecture before describing internal project results.

**Referee:** [source-of-truth hierarchy](../SOURCE_OF_TRUTH.md) → [registered claim](../record/claims.json) → [claim registry](../record/claim_registry.md) → [status ledger](../record/claim_ledger.md) → authoritative [mathematical proof](../mathematics/README.md) → [external dependencies](../literature/README.md) → [review protocol](../REVIEWING.md). Read a complete proof and its assumptions before declaring an external result applicable or establishing priority.

**Reproducer:** [reproduction](../REPRODUCE_unified.md) → [computation guide](../computations/README.md) → [formalization limits](../formalization/README.md) → [dated evidence](../evidence/README.md). A completed build or finite test certifies only its explicit checked target.

## Research manuscript versus paper candidates

[The full manuscript](../manuscript/README.md) is a living, comprehensive history of work and mathematical development. Its breadth is intentional. [Focused publication scopes](../papers/README.md) represent potential articles whose final contents, novelty and referee clearance are evaluated separately. Changes to expository text must never silently change a source theorem, a claim status, the recorded hypotheses or an immutable execution receipt.

## Visual evidence policy

An analytic reference curve is labelled **reference**, never simulation. A schematic is labelled **map**, never a demonstrated implication. An experiment must identify its finite dimensions, coupling, sample/ensemble, algorithm and limitation. Prefer SVG for vector diagrams and compact legible figures; do not introduce decorative art as evidence.

## Editorial change protocol

Keep stable proof paths and claim IDs. Prefer link-based topic maps to mass moves or duplicated statements. Update both top-level languages when status, scope or displayed formulas change. Resolve old corrections via the [errata](../ERRATA.md) and [history index](../archive/history/2026/INDEX.md) instead of overwriting original records. New claims or new citation dependencies follow [CONTRIBUTING.md](../CONTRIBUTING.md). Distinguish project-proof status from external independent refereeing.

## Integration epochs and scientific CI

The Wave2 and Wave3 replays bind historical source bytes, exact theorem contracts and scoped integrations. The [explicit later-ID manifest](../record/claim_integration_epochs.json) permits separately reviewed new claims without broadening those historical review statements. It rejects undeclared IDs and checks each listed current status and source. Scientific CI is a maintained consistency audit and cannot replace mathematical refereeing.

## Corpus-scale editing and scientific provenance

Use the [scientific corpus atlas](corpus_atlas.md) to distinguish maintained
proofs from historical snapshots and to navigate the entire manuscript by
mathematical regime. Repeated Git blob hashes inside `evidence/` are
**not** sufficient grounds for deletion: old manifests often identify an
exact historical path, and a copied proof may document which text was
reviewed at a particular moment. Change a canonical proof path only when
every dependency, literal source pin and manuscript input has been checked.

A bibliography entry should be metadata, not a miniature proof verdict.
Record which theorem is imported, its locator, and the model-specific
hypothesis bridge separately. The original 1984 BGS observation concerned
GOE-class Sinai-billiard evidence, whereas the maintained unitary-class
target asks for `Sine_2` after symmetry resolution; never conflate their
symmetry classifications.

