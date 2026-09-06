# WoW — arithmetic quantum maps and quantum-chaos verification

This branch is the canonical, current research state. Historical branch source trees are not vendored into `main`; Git history and `archive/branch-snapshots/README.md` retain their provenance.

## Current scientific status

The repository contains exact arithmetic reductions, finite-field/Cayley energy results, Pell/Floquet and coboundary resonance laws, fixed-strength locality/conjugacy results, finite arbitrary-phase nondegeneracy certificates, Hessian obstructions, and noncommuting return-word constructions developed in the research programme. The authoritative status of individual claims is `record/claim_ledger.md`.

A positive generic microscopic BGS/GOE/COE universality theorem is **not** claimed and remains open. Finite certificates, negative obstruction theorems, and regression computations must not be promoted to such a theorem.

## Canonical publication

There is one maintained publication entry point:

`manuscript/WoW_unified.tex`

Build it with:

```sh
python computations/maintenance/build_unified_manuscript.py --output-dir build/unified-paper
```

The older standalone article copies were consolidated into this manuscript and are kept only in Git history, not as parallel publication surfaces.

## Verification

```sh
python -m pip install -r requirements.txt
python computations/verification/repository_audit.py
cmake -S . -B build/cmake -DCMAKE_BUILD_TYPE=Release
cmake --build build/cmake --parallel
python computations/maintenance/verify_workspace.py --build build/cmake --logs build/verification-logs --output build/workspace-verification.json
(cd formalization && lake build)
```

The active computational stack is Python/C++/Lean/TeX. Julia is retired from the repository and the structural audit rejects any tracked `.jl`, `Project.toml`, or `Manifest.toml` file.

## Provenance

The recovered 204-file consolidation delivery is identified by SHA-256 `8addfd45f0c8d3d43d06472477aa8c5aac8eb3f2b94082fe6b715b20a3447099`; byte-level details are in `archive/delivery-20260906/README.md`. Historical research heads/tree hashes are metadata-only in `archive/branch-snapshots/README.md`.

Reproduction instructions and the final consolidation audit are in `REPRODUCE_unified.md` and `record/final_consolidation_audit_20260906.md`.
