# Reproduce the current consolidated research state

The canonical editable publication entry point is `manuscript/BGS_unified.tex`. The authoritative scientific-status ledger is `record/claim_ledger.md`; the consolidation audit is `record/final_consolidation_audit_20260906.md`.

The 4 October actual-start comparison, cluster obstruction, logarithmic
phase bounds and circular relaxation are reviewed in `record/general_start_review_20261004.md`.
Their finite controls require the pinned Python requirements and run as:

```sh
python3 computations/verification/coboundary_general_start.py \
  --output build/general-start-replay.json
python3 computations/verification/circular_dyson_relaxation.py \
  --output build/circular-dyson-replay.json
```

This checks finite normalizations, geometry and prior kernel conventions;
it is not a Brownian simulation or an asymptotic BGS certificate.

The finite-orbit section has a maintained mathematical source and a generated
TeX view. Validate it with
`python computations/maintenance/sync_finite_orbit_section.py --check`.
The 22 September proof, audit, source-level Lean kernels and exact finite
regressions are indexed in `record/integration_20260922.md`.

The 24 September audit of the submitted 87-page fixed-map article and the
exact boundaries of its three retained claims are in
`record/submitted_article_review_20260924.md`. The attached source and
outputs were replayed in isolation; the compact maintained versions can be
reproduced with:

```sh
python -S computations/verification/frozen_seven_cut.py \
  --output build/frozen_seven_cut.json
python -S computations/verification/frozen_total_minors.py \
  --output build/frozen_total_minors.json
python -S computations/verification/frozen_antireversor.py \
  --output-dir build/frozen_antireversor
cmp evidence/20260924/frozen_seven_cut.json build/frozen_seven_cut.json
cmp evidence/20260924/frozen_total_minors.json build/frozen_total_minors.json
cmp evidence/20260924/antireversor/certificate_result.json \
  build/frozen_antireversor/certificate_result.json
```

The antireversor reference CSVs can be compared in the same manner.
Alternatively select these three names with repeated `--only` arguments
in `verify_workspace.py`. None of these finite computations evaluates the
unproved sine-kernel or Abel limits.

The next two submitted continuations are audited in
`record/two_continuations_review_20260924.md`. To reproduce their retained
integer-only regression for `BGS-FM-010`:

```sh
python -S computations/verification/frozen_arithmetic_traces.py \
  --output build/frozen_arithmetic_traces.json
cmp evidence/20260924/frozen_arithmetic_traces.json \
  build/frozen_arithmetic_traces.json
```

This checks finite fixed-point counts and a rational kick-coefficient
margin, not the all-dimension proof, the effective `BGS-FM-011` bound,
or any microscopic statistic.

To check the finite normalizations of the two-clock Gram falsifier and
the pair-resolvent identity (`BGS-TRACE-008`, `BGS-RES-006`), run:

```sh
python -S computations/verification/gram_resolvent_normalization.py
```

The eight deterministic finite cases do not establish the asymptotic
counterexample or the fixed-map CUE limit; their proofs and boundaries
are in `mathematics/two_clock_gram_falsifier.md` and
`mathematics/fixed_map_resolvent_frontier.md`.

Byte-level delivery provenance is recorded in `archive/delivery-20260906/README.md`. Historical divergent branch heads/tree SHAs are recorded in `archive/branch-snapshots/README.md`; their source trees are deliberately not vendored into `main`.

## Git checkout and ZIP/archive execution

The runner supports two explicit source modes. In a Git checkout, it requires
an initially clean worktree unless `--allow-dirty` is deliberately supplied.
It hashes tracked and nonignored untracked files, checks content again after
execution, and records the initial local `HEAD` as `input_commit`. That local
commit is not a verified upstream identity: `upstream_commit` remains null.
Do not initialize a synthetic Git repository to make an archive look upstream.

A ZIP without `.git` must use an explicit file SHA-256 manifest. The archive
publisher should generate a manifest for the exact bytes being distributed,
ship it alongside the archive, and publish its SHA-256 through the delivery
channel. If no publisher manifest exists, the recipient can create a local
baseline before running checks:

```sh
python computations/maintenance/workspace_sources.py --root . \
  --output build/archive-source-manifest.json
python computations/maintenance/verify_workspace.py \
  --archive-manifest build/archive-source-manifest.json \
  --build build/cmake --logs build/verification-logs \
  --output build/workspace-verification.json
```

The manifest schema is `bgs-archive-source-manifest-v1`, with an explicit
`files` map from relative POSIX paths to SHA-256 and `upstream_commit: null`.
A recipient-created manifest only establishes a baseline for those local
bytes; it does not authenticate the publisher, original ZIP, or upstream
revision. Keep the original manifest rather than regenerating it after a
failed comparison. For archives, both commit fields and Git status fields
are null. Neither a hash match nor a successful check is a proof certificate.

Archive inventory includes historical evidence and binary inputs. It excludes
only the generated/developer directory names listed in
`computations/maintenance/workspace_sources.py` (notably `build`, `.git`,
virtual environments, Python caches, `.lake`, and scratch directories).
Manifest files must live outside the inventoried tree, for example in `build/`.
Missing, modified, added, unsafe-path, and symlink inputs fail closed; input
changes during execution fail after saving the execution report. Archive mode
cannot be combined with `--allow-dirty`, and cannot replace Git mode inside a
Git checkout. Outputs and build artifacts must stay in `build/` or outside the
source root. An archive nested inside another repository does not inherit its
parent's commit identity.

The cheap provenance and byte-hygiene controls are:

```sh
python -m unittest discover -s computations/maintenance/tests -v
python computations/verification/text_control_audit.py
```

These tests exercise temporary Git and non-Git fixtures, unknown/missing
versions, changed/missing/added source files, unsafe paths, and mutation during
execution. Temporary test commits have no relation to project provenance.
The byte audit rejects every C0 byte except TAB and LF in maintained UTF-8
text; binary formats and immutable `archive/`, `evidence/`, and `papers/`
history are explicitly outside its editing policy.

## Dependencies and execution limits

Use Python with the exact package versions in `requirements.txt` (CI targets
Python 3.13), CMake >= 3.20, a C++20 compiler, and Boost development headers.
The workspace runner rejects missing, unknown, or mismatched pinned Python
package versions before running checks. Selected C++ checks also require
identifiable CMake/compiler/Boost versions. The Boost header probe currently
uses `/usr/include/boost/version.hpp`; a nonstandard Boost installation must
be supported explicitly rather than reported as a verified unknown version.
Python-only focused runs do not require CMake, C++, or Boost; direct
standard-library scripts may still run without the pinned scientific packages,
but the workspace runner requires the complete pinned Python environment.
Missing executables and timeouts are recorded as failed checks, never passes.

Build C++ executables afresh from this source tree before a complete replay.
The runner fingerprints executed binaries/interpreters, sources and logs, but
does not prove that a preexisting binary was built from a given source. Python
package artifact hashes and the OS toolchain are not a hermetic lock. Actual
versions are recorded; Lean/TeX builds are separate and are not inferred from
a Python/C++ pass. Source fingerprints detect before/after changes, not a
transient modification restored during execution. Do not edit inputs while
verification is running.

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

To replay the two 23 September checks without compiling C++, select them
explicitly. The first uses exact rational arithmetic for a finite symbol
check; the second is a floating-point finite-matrix diagnostic:

```sh
python computations/maintenance/verify_workspace.py \
  --build build/cmake --logs build/frozen-checks \
  --output build/frozen-checks/manifest.json \
  --only frozen_full_lag_gap --only frozen_kick_rank
```

The additional nonlinear pressure result has a focused exact Fourier
regression. This verifies its coefficient and fixed-point algebra, not the
analytic pressure theorem or quantum universality:

```sh
python computations/verification/nonlinear_pressure_variance.py \
  --output build/nonlinear_pressure_variance.json
cmp evidence/20260923/nonlinear_pressure_variance.json \
  build/nonlinear_pressure_variance.json
python computations/maintenance/verify_workspace.py \
  --build build/cmake --logs build/nonlinear-check \
  --output build/nonlinear-check/manifest.json \
  --only nonlinear_pressure_variance --allow-dirty
```

Read `record/nonlinear_pressure_review_20260923.md` for the proof audit and
the precise source dependencies of `BGS-FM-006`.

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

The fixed-map frontier and finite-orbit resonance sections have separate
generated TeX views. The 6 October repaired-source build also passed all three
synchronization checks with Pandoc 2.17.1.1; the fixed-map renderer normalizes
its narrowly identified table-footer difference from 3.1.3. Pandoc 3.1.11.1
changes additional heading/anchor output and is not byte-compatible with
these generated views. A check failure with that version is not evidence
that the mathematical source changed: use a verified compatible version
rather than overwriting the generated chapters solely to silence the check.
Check all three generator families before building:

```sh
python computations/maintenance/sync_finite_orbit_section.py --check
python computations/maintenance/sync_fixed_map_section.py --check
```

Other included manuscript sections are directly maintained TeX. Build the
canonical manuscript with pdfLaTeX without writing a generated PDF into the
source tree:

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
## Fixed-map supplement

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
