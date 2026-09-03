# Reconstruction and completeness record

Date: 2026-09-03

This file defines the preservation boundary for the repository. Mathematical status lives in `claim_ledger.md`; retracted statements live in `retractions.md`.

## Source snapshot

The user-supplied research snapshot is `BGS.zip`.

- SHA-256: `afac3d3baa0876de7d4f63d1f164d0ebc388e139881771b54cd686f88ac2bbf8`
- compressed size: `45,752,245` bytes
- files: `1,100`
- uncompressed payload: `115,910,280` bytes
- original broad directories: `data` 443 files, `docs` 382, `code` 175, `formal` 57, `paper` 37, plus root notes/tools
- duplicate SHA-256 groups: `228`
- redundant byte-identical file copies: `266`
- Python sources: `329`
- Julia paths: `31`
- byte-distinct Julia sources: `23`
- Lean sources: `6`
- TeX sources: `26`
- PDF files: `11`

A deterministic per-file inventory (path, byte size, SHA-256, coarse class and byte-identical predecessor) was generated during the audit. `inventory_snapshot.py` regenerates the manifest from the supplied ZIP whenever that source file is available locally; the ZIP itself is not duplicated into this Git repository.

Generated Lean build state, bundled tool binaries, caches and byte-identical copies are not retained merely for volume. Scientific preservation is content-based, not file-count-based.

## Git provenance

Commit `06e8173d9a538412f3bd9212296e1664c4e25584` is the broad pre-compact reconstruction. Commit `a06f4b32831d3e21e74c3fa1c6892da068aa6599` contains important pair-key repairs but compressed the visible corpus too aggressively. The current tree reuses exact historical Git objects where they remain useful, while separating them from active mathematics.

Historical checkpoints that would otherwise contradict the current claim ledger are stored under `record/checkpoints/`; they are snapshots, not living documentation. Broad source/data/review material is under `record/corpus/`. Files unrelated to the cat-map project, such as accidental LLM benchmark comparisons, were removed from the current branch rather than preserved as fake research provenance; Git history still records their former presence.

## Current preservation policy

The repository follows **preserve useful evidence, trust narrowly**:

1. `mathematics/`, `computations/`, `formalization/`, `evidence/`, `literature/` and `manuscript/` are the active scientific surface.
2. Every active mathematical claim has one authoritative status in `claim_ledger.md` and a current derivation, finite certificate, numerical label, or explicit open/draft status.
3. Broad historical files remain under `record/` only when they can still help reconstruct a result, reproduce an old output, explain a retraction, migrate useful code, or prevent regression.
4. A false historical claim may be preserved as a negative control; a scientifically irrelevant file is not preserved just because it existed in the ZIP.
5. Historical labels such as `[PROVEN]`, theorem-like filenames, or old `PASS` fields have no authority outside the current ledger.
6. Exact duplicates are represented once where possible; Git history is preferred over cloning a second archive.
7. Julia migration is path-complete in `julia_migration.md`; falsified Julia is not mechanically translated.

## Semantic completeness check

Mechanical completeness and scientific completeness are different.

- **Mechanical source accounting:** the ZIP hash, file counts and deterministic inventory make the original 1,100 paths auditable.
- **Claim accounting:** `claim_ledger.md`, `retractions.md`, the consolidated `mathematics/` files and the manuscript cover the current exact results, finite certificates, useful earlier foundations, numerical diagnostics, theorem drafts and known failures.
- **Implementation accounting:** every promoted JSON producer/reference must resolve in CI; active Python compiles; current exact finite regressions run; active C++ builds; every active Lean module must occur in the root import graph and `lake build` must succeed.
- **Manuscript accounting:** the article contains the current pair-key/Cayley chain, finite exceptional sets, negative control, elliptic obligations, retained earlier results, corrected numerical interpretation, retractions that matter to interpretation, and the still-open BGS bridge. TeX is independently compiled in CI and a dedicated workflow commits the synchronized PDF.

No finite audit can prove the metaphysical statement that a human could never extract another useful idea from an old notebook. The strongest defensible guarantee is narrower and testable: every scientifically distinct result identified by the source inventory, historical status/index checkpoints, promoted evidence, current producers and retraction review is either represented in the active scientific narrative with an honest status, retained as useful historical provenance, or deliberately excluded as irrelevant/duplicate/generated material.
