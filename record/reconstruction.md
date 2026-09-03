# Reconstruction and preservation boundary

Date: 2026-09-03

This file records what was reconstructed and what the current repository
chooses to preserve. Mathematical status lives in `claim_ledger.md`; failure
mechanisms live in `retractions.md`.

## Supplied source snapshot

The user-supplied research snapshot was `BGS.zip`.

- SHA-256: `afac3d3baa0876de7d4f63d1f164d0ebc388e139881771b54cd686f88ac2bbf8`
- compressed size: `45,752,245` bytes
- files: `1,100`
- uncompressed payload: `115,910,280` bytes
- broad original directories: `data` 443 files, `docs` 382, `code` 175,
  `formal` 57, `paper` 37, plus root notes/tools
- duplicate SHA-256 groups: `228`
- redundant byte-identical file copies: `266`
- Python sources: `329`
- Julia paths: `31`
- byte-distinct Julia sources: `23`
- Lean sources: `6`
- TeX sources: `26`
- PDF files: `11`

`inventory_snapshot.py` can regenerate a deterministic path/size/SHA-256
manifest from the supplied ZIP when it is present locally. The ZIP itself is
not duplicated inside Git.

## Git reconstruction history

Important preservation points:

- `06e8173d9a538412f3bd9212296e1664c4e25584` — broad pre-compact
  reconstruction;
- `a06f4b32831d3e21e74c3fa1c6892da068aa6599` — corrected pair-key
  reconstruction;
- `d0e414ec26ff7e43ad59e80f77c9d8c679e87c4b` — last `main` snapshot before
  the final archive/copy cleanup; it still contains the curated
  `record/corpus`, checkpoints, historical C++ and formal drafts.

The current branch intentionally does **not** carry those historical trees a
second time. Git history is the archive.

## Current preservation policy

The maintained tree follows **preserve useful evidence, trust narrowly**:

1. `mathematics/`, `computations/`, `formalization/`, `evidence/`,
   `literature/` and `manuscript/` are the scientific working surface.
2. `record/` contains only compact status/provenance records needed to
   understand that surface.
3. Every promoted JSON evidence object resolves to a **current producer** and
   current reference inputs; CI no longer falls back to an archive path.
4. Every maintained C++ source is built by CMake.
5. Every active Lean module is imported by `formalization/Bgs.lean` and built
   by Lake.
6. No `.jl` source is tracked anywhere on the current branch.
7. Byte-identical maintained source/document duplicates are rejected by the
   repository audit.
8. False historical code is described by its failure mechanism and recoverable
   commit, not kept executable merely as museum material.
9. A fixed finite certificate is never promoted to a uniform theorem without a
   separate proof.

## Why the historical corpus was removed from `main`

The earlier reconstruction kept a broad `record/corpus/` for archaeology. That
was useful during recovery but became actively harmful after the audit:

- GitHub Linguist counted obsolete Julia and other archived languages as if
  they were current;
- stale producer paths encouraged evidence to depend on archived code;
- duplicate Python/TeX/Lean/C++ obscured which implementation was maintained;
- old theorem labels and `PASS` fields remained searchable next to corrected
  statements.

All scientifically useful information identified in the corpus has now been
either promoted to a maintained derivation/producer/certificate, summarized in
the claim/retraction/migration records, or deliberately left in Git history.

## Completeness boundary

No finite editorial audit can prove that an old notebook contains no
undiscovered idea. The reproducible claim is narrower:

- the original snapshot is hash-accounted and inventoried;
- every scientifically distinct result found during reconstruction has a
  current status or an explicit retraction;
- every promoted evidence file has a maintained producer/reference;
- current Python, C++, Lean and TeX surfaces are all CI-checked;
- the current tree contains no duplicate historical workspace.

That is the repository contract for the next researcher.
