# Final consolidation audit — corrected canonical main (2026-09-06)

This record supersedes earlier repository-shape and delivery-state conclusions. It does not alter the mathematical claim ledger.

## Corrections made

1. **Historical branch trees are metadata-only.** An earlier recovery commit copied complete divergent branch trees under `archive/branch-snapshots/`, reintroducing superseded source code, including 62 `.jl` files. Those copies are removed. `archive/branch-snapshots/README.md` retains branch/head/tree identifiers; Git refs/history remain the byte-authoritative provenance mechanism.

2. **Julia is retired globally.** The maintained computational stack is Python/C++/Lean/TeX. The structural audit scans the whole checkout, including `archive/`, and rejects `.jl`, `Project.toml`, and `Manifest.toml` anywhere.

3. **There is one publication surface.** Superseded standalone `.tex/.pdf` article pairs and obsolete manuscript fragments were removed from canonical `main`; they remain recoverable from Git history. `manuscript/BGS_unified.tex` is the sole maintained publication entry point and the canonical workflows build only it.

4. **There is one maintained verification/publication architecture.** Stale specialized workflows and one-shot integration/publication scripts that regenerated superseded copies were removed. The maintained orchestration is `verify_workspace.py` plus `build_unified_manuscript.py`; the scientific verifier/source corpus itself is retained.

5. **The canonical manuscript is self-contained and the recovered segmentation is TeX-safe.** The pre-cleanup master referenced missing arithmetic, Floquet, coboundary, locality and nondegeneracy consolidated inputs. Those missing sections were recovered from the byte-verified 204-file delivery as non-overlapping sequential `*_partN.tex` inputs. A clean reconstruction exposed two purely syntactic arithmetic split defects: `arithmetic_core_part3.tex` ended inside display math while part4 began with a blank line, and the part4/part5 boundary cut an `align` environment. The final repair only redistributes the boundary newline and `\end{align}` marker; no formula, theorem, hypothesis or proof text is changed. The apparent `arithmetic_core_part3` difference from the verified delivery was checked bytewise and is only a newline relocation.

6. **The fail-closed build gate remains effective after segmentation.** The old builder validated inherited Floquet mathematical tokens only for a file literally named `floquet.tex`; after the section became `floquet_part1..4`, that semantic gate was unreachable. The corrected builder concatenates exactly the reachable sequential `floquet_partN` inputs and applies the original artifact/token checks to that canonical family, in addition to recursive input hashing, three LaTeX passes and warning/source-immutability gates.

7. **Current scientific subtrees were preserved.** Relative to the pre-cleanup main state, `mathematics/`, `evidence/`, `formalization/`, `literature/`, and `assets/` retain identical Git tree SHAs. Inside `computations/`, the `analysis/`, `cpp/`, and `python/` trees are likewise unchanged; maintenance was pruned only of obsolete one-shot publication/integration scripts, while the active verification/build orchestration was retained and strengthened.

## Evidence retained and rechecked

- recovered delivery: 204 files, 2,605,999 bytes, SHA-256 `8addfd45f0c8d3d43d06472477aa8c5aac8eb3f2b94082fe6b715b20a3447099`;
- recovered Cayley subgroup-curve, elliptic product-row, and projective-Bezout packages remain in the active research tree;
- `return_word_certificate.cpp` was compiled/executed under C++20 with strict warnings and passed 30 geometry obligations plus 11 free-word tests;
- radius-8 arbitrary-phase nondegeneracy generation/replay passed 5,704 deductions (`3293 P`, `1077 S`, `1229 D`, `105 F`); Hessian and finite quantum-variance checks passed;
- the corrected canonical-current manuscript reconstruction uses exact master blob `f07bd4e85aab77e7aaec2059c7da95fbb2953530`, repaired arithmetic blobs `b62037646644b0af694f9aaeb0b09bf7c70f9352` and `e6d9c77473463f4653ad1808e719898c64a5dc6a`, corrected addendum blob `47a9f42068c5dd8a3ed2066b3d9e0342efc94a10`, and corrected builder blob `7780d97855bc0f5bd62b628308c75ea698d0c552`;
- the fail-closed builder passed on 49 reachable TeX inputs: three pdfTeX passes, 93 pages, `sources_unchanged=true`, no forbidden warnings, PDF size 887,748 bytes. The deterministic-run PDF SHA-256 is `366ef6a2e79831cbb47bea4b1d9bd6b895be7583835754be8304c09fa51283ca`.

These are repository/build/certificate checks, not a claim of complete independent referee acceptance of every mathematical statement.

## Structural invariants after cleanup

`repository_audit.py` fails if any of the following regressions occurs: tracked Julia/project environment; vendored historical branch source below `archive/branch-snapshots`; a legacy standalone manuscript or committed manuscript PDF; a missing canonical TeX input; a specialized workflow outside the canonical set; a retired one-shot publisher/integrator; an orphaned C++ source; or an active Lean module omitted from `Bgs.lean`.

The canonical build additionally fails on a missing/nonlocal TeX input, a changed source during the build, unresolved references/citations, horizontal overflow, duplicated destinations, inherited-core artifact regressions, missing restored Pell/Floquet mathematical tokens, or noncontiguous canonical Floquet parts.

## Scientific scope

`record/claim_ledger.md` remains authoritative. Repository cleanup does not promote any finite certificate, obstruction theorem, numerical regression, recovered lemma, recurrence-scale law or exceptional construction to positive generic microscopic BGS/GOE/COE universality. That positive universality problem remains open.

## Cloud CI caveat

The GitHub Actions runs inspected for the cleanup commit terminated before executing job steps (`runner_id=0`, `steps=[]`). Therefore their red status is a runner-provisioning/infrastructure event, not a failing repository command, and no green remote-CI result is claimed. A provisioned runner on the corrected canonical tree must be judged separately.
