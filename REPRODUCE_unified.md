# Consolidated research packet - 6 September 2026

The canonical editable entry point is `manuscript/WoW_unified.tex`. The main
branch was recovered in two fast-forward commits on 6 September 2026: first the
previously unmerged fixed-strength, smooth-cohomology and coboundary sources,
then the two local-only theorem notes. Large binary artifacts are intentionally
not claimed as synchronized unless their Git blob is verified byte-for-byte.

Build the article with:

```sh
python computations/maintenance/build_unified_manuscript.py --publish
```

For a full local overlay of the original 204-file consolidation packet, download
`WoW_consolidated_research.zip` from the ChatGPT delivery, extract it, and copy
its `WoW_consolidated/` tree over a fresh `main` checkout without deleting other
files. Then run the integration helper with `--check` before writing changes.

The proof status remains scoped: no positive generic BGS theorem, no established
world-priority claim and no new complete Lean formalization are inferred from
repository synchronization.
