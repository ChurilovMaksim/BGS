# Reconstruction record

Date: 2026-09-03

This record defines the preservation boundary for the repository rebuild. It is
not a theorem-status document; theorem status lives in `claim_ledger.md` and
the active mathematical notes.

## Source snapshot

The user-supplied research snapshot is `BGS.zip`.

- SHA-256: `afac3d3baa0876de7d4f63d1f164d0ebc388e139881771b54cd686f88ac2bbf8`
- compressed size: `45,752,245` bytes
- files: `1,100`
- uncompressed payload: `115,910,280` bytes
- original broad directories: `data` 443 files, `docs` 382, `code` 175,
  `formal` 57, `paper` 37, plus root notes/tools
- duplicate SHA-256 groups: `228`
- redundant byte-identical file copies: `266`
- Python sources: `329`
- Julia paths: `31`
- byte-distinct Julia sources: `23`
- Lean sources: `6`
- TeX sources: `26`
- PDF files: `11`

During this audit a complete deterministic per-file TSV was generated from the
ZIP (path, byte size, SHA-256, coarse class, byte-identical predecessor). The
repository contains `inventory_snapshot.py`, which regenerates that manifest
byte-for-byte from the preserved ZIP instead of checking in a 1,100-line copy
of metadata for a file that is not itself versioned here. Generated Lean build
products, bundled tool binaries, caches and byte-identical duplicates are not
promoted to the active scientific surface.

## Git provenance

The repository commit

`06e8173d9a538412f3bd9212296e1664c4e25584`

is the last broad-corpus reconstruction immediately before the overly
aggressive compact rebuild. It contains the broad research trees (`code/`,
`data/`, `docs/`, `inputs/`, `research/`, supported `src/` and `experiments/`)
and an immutable pre-restructure provenance snapshot. The current rebuild
reuses those audited Git objects where they remain useful instead of
re-encoding them or creating another duplicate archive.

The compact commit

`a06f4b32831d3e21e74c3fa1c6892da068aa6599`

introduced several correct scientific repairs (especially the corrected
pair-key M1 line and the `(N,K)=(461,23)` Cayley negative control) but again
compressed the visible corpus too far. This rebuild keeps those repairs while
restoring discoverability and provenance.

## Preservation policy

The active repository follows **preserve broadly, trust narrowly**.

1. Current theorem notes, supported implementations, finite certificates,
   numerical evidence, formal sources and the manuscript have human scientific
   paths.
2. Broad historical code/data/review material remains available under
   `record/corpus/`, but it is not automatically trusted.
3. Historical Julia is not duplicated into the active language layer. Every
   path is mapped in `julia_migration.md`; the original bytes are recoverable
   from Git history and hash-accounted by the reproducible ZIP inventory.
4. Retracted arguments remain named in `retractions.md` so future work cannot
   silently resurrect them.
5. No claim is promoted because an old README called it `PROVEN`. Promotion
   requires a derivation, a finite certificate, a successful current
   regression, or a source-exact theorem application with hypotheses checked.

## Completeness checks

The ZIP hash plus deterministic inventory generator is the mechanical
completeness check for the user snapshot. The claim ledger is the semantic
completeness check for scientific conclusions. The Julia inventory is the
language-migration completeness check. The broad `record/corpus/` trees keep
intermediate and negative research directly browsable while avoiding a second
copy of generated `.lake` state, bundled binaries and other build trash.
