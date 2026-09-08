# Reproduce the current consolidated research state

The canonical editable publication entry point is `manuscript/WoW_unified.tex`. The authoritative scientific-status ledger is `record/claim_ledger.md`; the consolidation audit is `record/final_consolidation_audit_20260906.md`.

The original 204-file consolidation delivery was recovered from the user's Library and byte-verified before cleanup:

```text
WoW_consolidated_research.zip
bytes   2605999
sha256  8addfd45f0c8d3d43d06472477aa8c5aac8eb3f2b94082fe6b715b20a3447099
files   204
```

Byte-level delivery provenance is recorded in `archive/delivery-20260906/README.md`. Historical divergent branch heads/tree SHAs are recorded in `archive/branch-snapshots/README.md`; their source trees are deliberately not vendored into `main`.

Run the structural gate first:

```sh
python -m pip install -r requirements.txt
python computations/verification/repository_audit.py
```

Build and execute the maintained C++/Python verification surface:

```sh
cmake -S . -B build/cmake -DCMAKE_BUILD_TYPE=Release
cmake --build build/cmake --parallel
python computations/maintenance/verify_workspace.py \
  --build build/cmake \
  --logs build/verification-logs \
  --output build/workspace-verification.json
```

Build every active Lean module:

```sh
(cd formalization && lake build)
```

Build the canonical manuscript without writing a generated PDF into the source tree:

```sh
python computations/maintenance/build_unified_manuscript.py \
  --output-dir build/unified-paper
```

Generated PDFs stay in `build/`; the repository structural gate rejects PDFs
in `manuscript/`. Distribute the built PDF separately. The maintained
`--publish` switch is a legacy local export and does not publish to GitHub.

Important audit correction: the earlier recorded 93-page manuscript check was a successful build of the reconstructed 204-file consolidation corpus with the current master TeX. It was not a proof that the then-current clean Git checkout was self-contained; that checkout was missing several `\input` targets. The cleanup commit fixes that defect and the structural audit now fails whenever any canonical TeX input is absent.

The active stack is Python/C++/Lean/TeX. Julia is retired and `repository_audit.py` rejects tracked `.jl`, `Project.toml`, and `Manifest.toml` files anywhere in the checkout, including `archive/`.

The finalization-era GitHub Actions attempts that were inspected had `runner_id=0`/no executed steps, so no green cloud-CI claim is inferred from them. Local verification evidence and cloud-runner status must remain separate.

Repository synchronization does not change mathematical scope: positive generic microscopic BGS/GOE/COE universality remains open, and finite certificates or obstruction results are not promoted to that theorem.
