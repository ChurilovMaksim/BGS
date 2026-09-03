# Lean certificates

The active Lean layer contains finite/combinatorial certificates that are useful to the current argument.  Open/specification-only files from the historical workspace are not imported here; they remain in the archive.

Current source set:
- `TorusLevelSets.lean` — finite level-set/orbit counts at `N=199`;
- `ScaleLaw.lean` — finite scale-law arithmetic at `N=199`;
- `K2Reduction.lean` — finite `k=2` constraint/bijection certificate at `N=53`;
- `K4Variety.lean` — finite `k=4` variety/key-count certificate at `N=53`;
- `M1DegenerateFiber.lean` — finite certificates for the `d=0` exceptional fiber.

Lean/lake are not installed in the current execution environment, so the reorganized import set is **UNVERIFIED BUILD in this session**.  Historical build claims remain provenance only until a fresh `lake build` is recorded.  Python/C++ checks do not substitute for Lean kernel verification.
