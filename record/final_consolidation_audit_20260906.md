# Final consolidation audit — corrected canonical-main cleanup (2026-09-06)

This record supersedes the repository-shape conclusions of the earlier recovery audit. It does not alter the mathematical claim ledger.

## Corrections made

1. **Historical branch trees are metadata-only.** The earlier recovery commit copied complete divergent branch trees under `archive/branch-snapshots/`. That reintroduced superseded source code, including 62 `.jl` files, into an otherwise Julia-free repository. Those copied trees are removed. `archive/branch-snapshots/README.md` retains branch/head/tree SHAs, while Git refs/history remain the byte-authoritative recovery mechanism.

2. **Julia is retired globally.** The active computational stack is Python/C++/Lean/TeX. The structural audit now scans the whole checkout, including `archive/`, and rejects `.jl`, `Project.toml`, and `Manifest.toml`.

3. **One publication surface.** Five old standalone `.tex/.pdf` article pairs and obsolete top-level manuscript fragments are removed from the current tree. They remain recoverable from Git history. `manuscript/WoW_unified.tex` is the sole maintained publication entry point; workflows build only it.

4. **One verification/publication architecture.** Stale specialized workflows and one-shot branch-integration/publication scripts that regenerated superseded article copies are removed. The maintained workflow surface is `ci.yml`, `build-manuscript.yml`, and the read-only `research-snapshot.yml`. The maintained orchestration is `verify_workspace.py` plus `build_unified_manuscript.py`; scientific verifier/source files themselves are retained.

5. **The canonical manuscript is self-contained by construction.** The previous `main` master referenced missing `arithmetic_core.tex`, `floquet.tex`, `coboundary.tex`, `locality.tex`, and `nondegeneracy.tex`. Missing consolidated material was recovered from the byte-verified 204-file delivery. Long recovered sections are stored as non-overlapping sequential `*_partN.tex` inputs. Existing later corrections, notably `arithmetic_core_part3.tex`, were preserved rather than overwritten by older delivery bytes. The structural audit resolves every `\\input{...}` and fails closed on a missing target.

6. **Build graph remains current.** The CMake graph still covers every maintained C++ verifier; `Bgs.lean` remains the import surface for active finite Lean certificates; `verify_workspace.py` retains the earlier fix that supplies required CLI outputs in temporary/log locations instead of mutating committed evidence.

## Evidence retained from this session

- recovered delivery: 204 files, 2,605,999 bytes, SHA-256 `8addfd45f0c8d3d43d06472477aa8c5aac8eb3f2b94082fe6b715b20a3447099`;
- recovered Cayley subgroup-curve, elliptic product-row, and projective-Bezout packages remain in the active research tree;
- `return_word_certificate.cpp` was compiled/executed under C++20 with strict warnings and passed 30 geometry obligations plus 11 free-word tests;
- radius-8 arbitrary-phase nondegeneracy generation/replay passed: 5,704 deductions (`3293 P`, `1077 S`, `1229 D`, `105 F`); Hessian and finite quantum-variance checks passed;
- the earlier reconstructed-corpus manuscript build completed three TeX passes and 93 pages without unresolved references/citations or overfull-box warnings. This is preserved as historical build evidence, but it is explicitly **not** represented as a clean-checkout build of the pre-cleanup `main`, because that tree was missing canonical inputs.

## Structural invariants after cleanup

`repository_audit.py` now fails if any of the following regressions occurs: tracked Julia/project environment; vendored historical branch source below `archive/branch-snapshots`; a legacy standalone manuscript or committed manuscript PDF; a missing canonical TeX input; a specialized workflow outside the canonical three; a retired one-shot publisher/integrator; an orphaned C++ source; or an active Lean module omitted from `Bgs.lean`.

## Scientific scope

`record/claim_ledger.md` remains authoritative. Repository cleanup does not promote any finite certificate, obstruction theorem, numerical regression, or recovered lemma to positive generic microscopic BGS/GOE/COE universality. That positive universality problem remains open.

## Cloud CI caveat

The GitHub Actions attempts inspected during the earlier finalization terminated before executing job steps (`runner_id=0`/no step logs). Therefore this audit does not infer a green remote CI result from those runs. A provisioned runner on the corrected canonical tree must be judged separately.
