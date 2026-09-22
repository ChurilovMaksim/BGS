# Reconstruction and preservation boundary

The repository was reconstructed from two overlapping sources: the supplied
`BGS.zip` research snapshot and the Git history of `ChurilovMaksim/BGS`.
Preservation and scientific authority are deliberately separated.

## Supplied snapshot

The supplied ZIP is reproducibly identified by:

- SHA-256: `afac3d3baa0876de7d4f63d1f164d0ebc388e139881771b54cd686f88ac2bbf8`;
- archive size: `45,752,245` bytes;
- `1100` files;
- `115,910,280` uncompressed bytes;
- `31` Julia paths, reducing to `23` byte-distinct Julia sources.

`record/inventory_snapshot.py` regenerates a per-file path/size/SHA-256
inventory when the ZIP is available locally. The original snapshot is not
copied into `main`; Git history plus the original ZIP preserve the source
material without making obsolete files look maintained.

The last curated `main` commit that still carried the broad historical corpus
was `d0e414ec26ff7e43ad59e80f77c9d8c679e87c4b`.

## Why the archive trees were removed from the current branch

Keeping `record/corpus`, checkpoints, historical language ports and formal
drafts inside `main` preserved bytes but became actively harmful:

- GitHub Linguist counted obsolete languages as current;
- stale producer paths encouraged evidence to depend on archived code;
- duplicate Python/TeX/Lean/C++ obscured the maintained implementation;
- old theorem labels and `PASS` fields remained searchable beside corrected
  statements.

All scientifically useful information identified during reconstruction is now
either promoted to a maintained derivation/producer/certificate, summarized in
the claim/retraction/migration records, or deliberately left in Git history.

## Completeness boundary

No finite editorial audit can prove that an old notebook contains no
undiscovered idea. The reproducible claim is narrower:

- the original snapshot is hash-accounted and inventoried;
- every scientifically distinct result found during reconstruction has a
  current status or explicit quarantine/retraction;
- every promoted evidence file has a maintained producer/reference;
- current Python, C++, Lean and TeX surfaces are CI-checked;
- the current tree contains no duplicate historical workspace and no `.jl`
  source.

That is the repository contract for the next researcher.

## Final end-to-end audit additions

The closing audit found one additional numerical-only defect: the reconstructed
spectral diagnostic formed the correct Hermitian matrix `M+M^*` but then
diagonalized its entrywise real part. The corrected producer now diagonalizes
the full complex Hermitian matrix, the committed numerical evidence was
regenerated, and CI recomputes those complete records. This did not affect any
exact pair-key/Cayley identity or Lean certificate.

The same pass promoted the general constrained-pair count `(K-1)(K-2)` from a
mere finite check to its correct **EXACT** status, renamed the misleading
`second_moment_reduction.json` certificate to `cayley_fixed_k_audit.json`, and
extended the structural audit to all Markdown relative links and active Lean
proof placeholders.
