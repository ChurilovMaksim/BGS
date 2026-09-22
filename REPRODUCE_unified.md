# Reproduce the current consolidated research state

The canonical editable publication entry point is `manuscript/BGS_unified.tex`. The authoritative scientific-status ledger is `record/claim_ledger.md`; the consolidation audit is `record/final_consolidation_audit_20260906.md`.

The finite-orbit section has a maintained mathematical source and a generated
TeX view. Validate it with
`python computations/maintenance/sync_finite_orbit_section.py --check`.
The 22 September proof, audit, source-level Lean kernels and exact finite
regressions are indexed in `record/integration_20260922.md`.

Byte-level delivery provenance is recorded in `archive/delivery-20260906/README.md`. Historical divergent branch heads/tree SHAs are recorded in `archive/branch-snapshots/README.md`; their source trees are deliberately not vendored into `main`.

Run the cheap fail-closed metadata and structural gates first:

```sh
python computations/verification/scientific_registry_audit.py
python computations/verification/repository_audit.py
```

Then install the pinned Python requirements before scientific computation:

```sh
python -m pip install -r requirements.txt
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

To reproduce only the ten return-law checks (without compiling C++):

```sh
python computations/maintenance/verify_workspace.py \
  --build build/cmake --logs build/return-checks \
  --output build/return-checks/manifest.json \
  --only general_cat_return_laws --only phase_space_return_gas \
  --only periodic_point_trace_comparison --only fixed_harmonic_return_gas \
  --only analytic_kick_return_gas --only even_period_spin_resonance \
  --only hyperbolic_return_pressure --only pell_resonance_lattice \
  --only return_trace_obstruction --only return_local_limits
```

A focused manifest records its selection and does not certify the complete
historical suite. Each return-law producer receives a separate JSON output
path; the runner records the source hash, exit status and log hash.

Build every active Lean module with the version pinned in
`formalization/lean-toolchain`. Source presence is not compilation evidence:

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

Repository synchronization does not change mathematical scope: fixed-strength
microscopic BGS/GOE/COE/GUE universality remains open, and finite certificates
or obstruction results are not promoted to that theorem.

The machine-readable scientific state is split deliberately:
`record/claim_ledger.md` controls status,
`record/claims.json` supplies stable IDs and cross-layer links,
`literature/external_dependencies.json` pins load-bearing external theorem
locators, and `environment/runtime-manifest.json` describes the intended
execution environment. A scientific release should preserve all four.

Reproduce the new analytic illustration with
`python computations/analysis/return_obstruction_figure.py`. The plotted curves
are analytic limits and lower bounds, not measured cat-map spectra.
# Fixed-map supplement, 20 September 2026

The additional dependency `scipy==1.17.0` is pinned in `requirements.txt`.
From the root run:

```sh
python computations/maintenance/verify_fixed_map_supplement.py
python computations/maintenance/sync_fixed_map_section.py --check
```

The first command checks every retained inventory hash and Python source,
and runs 28 isolated finite replays, including independent C++ replay and
weighted minors through N=23. Results go to `build/fixed-map-replay/`.
Exploratory echo and redesigned-symbol monodromy simulations, and Wolfram
scripts, retain their dated evidence and are not counted as fresh runs.
The new Lean kernel is included in the pinned `lake build`; its current
execution status must be read separately from earlier 16-module reports.
See [the publication review](record/fixed_map_publication_20260920.md).
