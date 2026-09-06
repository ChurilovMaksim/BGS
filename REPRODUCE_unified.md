# Consolidated research packet — final main, 6 September 2026

The canonical editable publication entry point is
`manuscript/WoW_unified.tex`. The repository-wide scientific status authority
remains `record/claim_ledger.md`; the final recovery/audit record is
`record/final_consolidation_audit_20260906.md`.

The recovery was performed only by fast-forward commits. It restored the
previously unmerged fixed-strength, smooth-cohomology and coboundary work, the
local noncommuting/nondegeneracy theorem notes, and three additional omitted
Cayley packets (subgroup curve, elliptic product rows, projective Bezout). All
remote research branches that diverged from the final line are preserved as
exact Git-tree snapshots under `archive/branch-snapshots/`.

The original 204-file delivery was recovered from the user's ChatGPT Library
and verified before finalization:

```text
WoW_consolidated_research.zip
bytes   2605999
sha256  8addfd45f0c8d3d43d06472477aa8c5aac8eb3f2b94082fe6b715b20a3447099
files   204
```

Its byte-level provenance, the companion patch hash, and the hashes of the two
compressed binary members are recorded in
`archive/delivery-20260906/README.md`. The outer ZIP remains the authoritative
historical container; it is not re-encoded through the GitHub connector because
large binary/base64 transport can be truncated. The maintained sources and all
divergent Git branch trees are preserved directly in `main`.

Install Python dependencies and run the structural/build graph gate first:

```sh
python -m pip install -r requirements.txt
python computations/verification/repository_audit.py
```

Build every maintained C++ verifier and execute the complete maintained
Python/C++ verification surface with hashed logs:

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

Build the canonical manuscript without publishing into the source tree:

```sh
python computations/maintenance/build_unified_manuscript.py \
  --output-dir build/unified-paper
```

To publish a locally verified PDF explicitly:

```sh
python computations/maintenance/build_unified_manuscript.py --publish
```

The final reconstructed manuscript check recorded in
`record/final_manuscript_build_20260906.json` completed three TeX passes with
no forbidden warnings, unchanged TeX inputs and 93 pages. That check is
manuscript-build evidence, not full-repository CI or a mathematical proof audit.

The GitHub Actions attempts observed during finalization did not receive a
runner (`runner_id=0`, no executed steps), so this file does not claim a green
remote CI run. The workflows themselves have been repaired so the next
provisioned runner exercises the canonical unified builder and the complete
maintained C++/Lean graph.

Scientific scope is unchanged by synchronization: no positive generic
microscopic BGS theorem, no established world-priority claim, and no complete
formalization of the analytic argument are inferred from repository recovery.
