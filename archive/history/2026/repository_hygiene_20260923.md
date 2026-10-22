# Repository-wide editorial and verification pass — 23 September 2026

Base commit: `a826199e134832c5c9fa0184fc0143dbefe47b2b`.
This is a structural and editorial pass, not a new mathematical result or an
independent rereview of all 27 registered proofs. `BGS-BGS-001` and the
model-specific `BGS-TRACE-005` remain **OPEN**.

## Corpus and decisions

- Inventoried all 727 tracked paths and their top-level roles. The current
  claim and topic registries cover 27 claim IDs and the maintained mathematics
  notes. Existing structural and scientific registry audits passed.
- Checked the 263 tracked Markdown files for local links: 378 syntactic
  relative-link candidates, with only four false positives arising from
  mathematical notation that matches a simple Markdown regex; no confirmed
  missing file targets. Independently confirmed that 79 TeX files (the master
  and 78 inputs) form the reachable consolidated manuscript.
- The one excluded `manuscript/finite_orbit_note.tex` is a historical execution
  input named in `evidence/20260922/run_manifest.json`, so deleting/moving it
  would break recorded provenance. The only four identical Git blobs are empty
  historical stdout/stderr files from two certificates; these paths retain
  their distinct execution meanings. No scientifically justified deletion was
  identified. The manuscript audit now rejects additional unused TeX inputs.
- Updated the stale public status date, the scientific changelog, historical
  navigation, the review order, publication-candidate scope notes, and the
  reproduction/manuscript guides. The dated evidence taxonomy now identifies
  mixed packets separately from canonical execution manifests, and the
  registry audit checks referenced historical directories.
- The common verification runner now captures scoped JSON for the two newest
  checks. All three manuscript/release CI workflows check synchronization of
  the six return-law chapters, the finite-orbit chapter, and the fixed-map
  chapter; the independent manuscript workflow also watches its generator.

## Execution and limits

| Check | Observed result |
|---|---|
| `scientific_registry_audit.py`, `repository_audit.py`, both generated indexes' `--check`, three chapter synchronizers' `--check`, and `python3 -m compileall -q computations` | Passed. Structural checks and compilation are not mathematical proof audits. |
| `verify_workspace.py --only frozen_full_lag_gap --only frozen_kick_rank --allow-dirty` | 2/2 passed; outputs and source/log hashes in ignored `build/hygiene-checks/` and `build/hygiene-workspace.json`. The checkout was deliberately dirty while these edits were in progress. |
| `verify_fixed_map_supplement.py --audit-only` | Passed inventory/source validation; executed zero scientific replays. |
| `verify_fixed_map_supplement.py --output-dir build/hygiene-fixed-map` | 23/28 passed. Five isolated scripts stopped on import of missing `sympy` or `mpmath`: `coherent-return/gap_identity.py`, three `report-audit-20260919` scripts, and `fixed-map-audit/classical.py`. These are environment non-runs, not adverse numerical or mathematical outcomes. |
| `build_unified_manuscript.py --output-dir build/hygiene-paper` | Three pdfLaTeX passes, 233 pages, no gated reference/layout warnings; ignored PDF SHA256 `e6d26829ff2b8de27b97492cc2efc4a4c2f04b0c6dc14af52419ef69fb213625`. Typesetting is not proof validation. |
| Four workflow YAML files | Parsed with a YAML loader; their job maps are present. Cloud workflows were not executed by this local pass. |

An attempted installation of the two pinned packages into ignored
`build/python-deps/` returned “No matching distribution found” in this
restricted runtime. CMake, Boost headers, and Lake were not available here;
the full Python/C++ suite and Lean build were **not run** in this pass.
This does not supersede the scoped successful executions recorded in
`record/integration_20260922.md` and `record/integration_20260923.md`.

Historical scientific assertions and evidence files were left byte-for-byte
unchanged. Future work on `BGS-TRACE-005` begins from the existing open
obligation rather than from these editorial checks.
