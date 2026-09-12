# Reproduce the current consolidated research state

The canonical editable publication entry point is `manuscript/WoW_unified.tex`. The authoritative scientific-status ledger is `record/claim_ledger.md`; the consolidation audit is `record/final_consolidation_audit_20260906.md`.

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

To reproduce only the nine return-law checks (without compiling C++):

```sh
python computations/maintenance/verify_workspace.py \
  --build build/cmake --logs build/return-checks \
  --output build/return-checks/manifest.json \
  --only general_cat_return_laws --only phase_space_return_gas \
  --only periodic_point_trace_comparison --only fixed_harmonic_return_gas \
  --only analytic_kick_return_gas --only even_period_spin_resonance \
  --only hyperbolic_return_pressure --only pell_resonance_lattice \
  --only return_trace_obstruction
```

A focused manifest records its selection and does not certify the complete
historical suite. Each return-law producer receives a separate JSON output
path; the runner records the source hash, exit status and log hash.

Build every active Lean module with the version pinned in
`formalization/lean-toolchain`:

```sh
(cd formalization && lake build)
```

The six return-law TeX sections are generated from their Markdown proof
sources. The current generated chapters use Pandoc 3.1.3. Install that
version for byte-for-byte regeneration, edit those proof sources, then synchronize:

```sh
python computations/maintenance/sync_return_sections.py
python computations/maintenance/sync_return_sections.py --check
```

Other manuscript sections remain directly maintained TeX. Build the canonical
manuscript with pdfLaTeX without writing a generated PDF into the source tree:

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

Reproduce the new analytic illustration with
`python computations/analysis/return_obstruction_figure.py`. The plotted curves
are analytic limits and lower bounds, not measured cat-map spectra.
