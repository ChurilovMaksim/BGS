# Repository reconciliation: executed scope

Checked source commit: `0db5021c18a35f5b46b9b816c803628831200170`.
Its tree is `e3dd0256ade4d3a5c2a59afb2a7f6d32f4811195`, based on
main `7ada29670c0cefe0a27f10b27ccfd594afca68da`. The host used a full
authenticated source reconstruction, not a Git checkout. Accordingly the
workspace runner honestly records archive mode and null Git/upstream commit
fields; `checked_source_delta.json` records the separate Git-object identity.

| Evidence | Actual coverage |
|---|---|
| `baseline_integrity.json` | All 5,876 original blobs and original executable modes; five host extraction modes repaired locally |
| `workspace.json.gz`, `selected_checks.json` | 198 selected root Python replays, exact commands and caps, all passed; 5,884-file source profile unchanged |
| `tests.log` | 239 maintenance/adversarial tests passed |
| `consistency_gates.json` | 13 current registry, metadata, link, generation, synchronization and reference gates passed |
| `integrity.json`, `semantic_preservation.json` | 707 Python ASTs, 2,293 JSON paths with three documented historical exceptions, seven maintained YAMLs, three shell syntax checks; 325 proof notes and scientific registries unchanged |
| `cpp_compile.json` | Fourteen standard-library sources under computations/cpp compiled with GNU C++ 13.3; not executed |
| `manuscript_build.json`, `pdf_qa.json` | Three TeX passes, 311 pages, independent PDF hash/page check and visual review of pages 1, 305–308, 311 |

`execution_archive.tar.gz` preserves the actual replay logs and generated
replay artifacts, maintenance logs and TeX logs. `archive_members.json`
pins every member; `receipt.json` pins the packet files. The complete raw workspace JSON is stored losslessly in `workspace.json.gz`;
`receipt.json` records both raw and compressed hashes. The generated PDF,
page images and C++ binaries are not committed; their observed hashes are
recorded. A selected-page inspection is not full-page or mathematical review.

Python 3.12.14 ran the five exact package pins in requirements.txt; the CI
target remains Python 3.13. Full CMake/Boost execution, fresh Lean compilation,
Wolfram and dated nested standalone snapshot replays are not covered.
Twenty-four Bgs modules plus the umbrella were inspected as source only.
Absence of admission-like source lines is not Lean certification.

To reproduce the exact input, use the checked source commit in a separate
checkout and the selection in selected_checks.json. workspace_command.json
records actual host paths; replace input/output paths for the local machine.
Use archive mode only for a source archive matching source_manifest.json,
or the runner's normal Git mode in a clean checkout. The four excluded
root-Python tasks and all broader exclusions are explicit in selected_checks.json.

The interrupted earlier proposal and its lost raw logs are not accepted
execution evidence. interrupted_proposal_manifest.json preserves proposed
file hashes for recovery provenance only. The fresh receipts above supersede
earlier observed summaries; no old log was fabricated or recertified.
The subsequent commit adds this packet and limited landing-page corrections;
the final consistency gates are recorded separately. Hosted CI status is
available on GitHub and is distinct from these local results.

[Repository review](../../../../record/repository_reconciliation_20261020.md).
BGS-BGS-001 and BGS-TRACE-005 remain OPEN. No complete proof review,
external refereeing, priority determination or BGS solution is claimed.
