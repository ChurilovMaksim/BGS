# Lines N2–N4 integration: check results after the owner audit of PR #66 (branch line-N2N4 vs main 5c292e7e)

The branch includes a merge of origin/main 5c292e7e. Logs are in `owner_audit_pr66/`.

## Checker suite

| check | branch | main 5c292e7e | known-failing? |
|---|---|---|---|
| render_bibliography --check | exit 0 | exit 0 | |
| render_claim_registry --check | exit 0 | exit 0 | |
| render_errata --check | exit 0 | exit 0 | |
| render_research_views --check | exit 0 | exit 0 | |
| render_spectral_research --check | exit 0 | exit 0 | |
| render_status --check | exit 0 | exit 0 | |
| scientific_registry_audit | OK (382 claims, 68 EXT) | **exit 1**: "claim verification inventory source blob is stale" | main only. Commit 5c292e7e edited claims 152 and 157 without refreshing the inventory; the branch inventory mirrors them. |
| repository_audit | exit 0 | exit 0 | |
| wave3_integration_audit | exit 0 | exit 0 | |
| wave2_integration_audit | exit 1: "integrated wrapper mapping changed" | exit 1, same | pre-existing on both |
| audit_manuscript_references --check | exit 0 | exit 0 | |
| bibliographic_metadata_audit | exit 1: **only** "EXT-BR-1975: dependency graph changed" | exit 1, same single line | pre-existing on both (R2). The 5 #66 regressions are fixed by `registry_metadata_20261031_lineN2N4.json`. |
| bibliographic_metadata_audit --self-test (CI form) | exit 1, EXT-BR-1975 only | exit 1, same | pre-existing on both |
| check_spectral_edition | exit 1: source-projection list (spectral-final certificates .json.gz) | exit 1, identical output | pre-existing on both |
| sync_return_sections --check | exit 1: "pandoc not found on PATH" | exit 1, same | environment (no pandoc 3.12.1 on the box) |
| sync_finite_orbit_section --check | exit 0 (SKIP: TeX is source of truth) | exit 0 | |
| sync_fixed_map_section --check | exit 0 | exit 0 | |

The branch fails the same checkers as main, with the same messages, apart from paths: wave2, bibliographic (×2, EXT-BR-1975 only),
check_spectral_edition and sync_return_sections. Main also fails scientific_registry_audit (stale inventory).

## Integration checks and Lean

| check | branch |
|---|---|
| proved_deps_gate_N2N4.py, strict 244..298 | GATE_OK, no cycles, closure conditions present |
| proved_deps_gate_MN.py (#65), lineL proved_deps_gate.py (#64) | GATE_OK / GATE_OK |
| lineN2N4_checks.py | LINE_N2N4_CHECKS_OK |
| check_schur_xy.py / blocks16_exact_inner.py | SCHUR_XY_OK / BLOCKS16_EXACT_OK |
| lake exe cache get / lake build Bgs | exit 0 / "Build completed successfully (8843 jobs)" (includes main's LineDCoeffReality, LineDStrongKickConc); no sorryAx; axioms ⊆ {propext, Classical.choice, Quot.sound} |

## Unittest

The suite has 256 tests and was run sequentially.

| tree | result |
|---|---|
| branch, with `formalization/.lake` moved aside, like the main worktree | failures=116, errors=103, skipped=1 |
| main 5c292e7e, clean worktree | failures=117, errors=104, skipped=1 |

The branch failure list is a strict subset of main's. Main also fails two tests: `test_registry_nodes` ERROR
`test_inventory_snapshot_and_statement_only_open_claim` and FAIL `test_inventory_metadata_drift_rejected`. Both come from main's
stale inventory.

A first branch run, made with the 8 GB built `.lake` present, had three extra errors: `test_fractional_routing` and two in
`test_schur_portability`. Their cause was `[Errno 28] No space left on device` while the tests copied `.lake` into /tmp overlays. Each
passes alone. That run is discarded (environment). Lists: `owner_audit_pr66/unittest_failures_{branch,main_5c292e7e}.txt`.

---

# Earlier record (PR #66 head 9849ee67)

| check | branch | main 3c7ac4a6 |
|---|---|---|
| render_bibliography --check | OK | OK |
| render_claim_registry --check | OK | OK |
| render_errata --check | OK | OK |
| render_research_views --check | exit 0 | exit 0 |
| render_spectral_research --check | exit 0 | exit 0 |
| render_status --check | OK | OK |
| scientific_registry_audit | OK (382 claims, 68 EXT) | OK (369 claims, 68 EXT) |
| repository_audit | exit 0 (incl. check_lean_coverage) | exit 0 |
| wave3_integration_audit | exit 0 | exit 0 |
| wave2_integration_audit | exit 1 "integrated wrapper mapping changed" (pre-existing) | same |
| audit_manuscript_references --check | exit 0 | exit 0 |
| proved_deps_gate_N2N4.py, strict 244..298 | GATE_OK, no cycles, closure conditions present | n/a |
| proved_deps_gate_MN.py (#65), lineL proved_deps_gate.py (#64) | GATE_OK / GATE_OK | n/a |
| lineN2N4_checks.py (registered numbers vs logs) | LINE_N2N4_CHECKS_OK | n/a |
| check_schur_xy.py (N4-F8; six Schur reruns) | SCHUR_XY_OK (bit-identical α, β, f, d; d = √(x/y)/max) | n/a |
| blocks16_exact_inner.py (N4-F5) | BLOCKS16_EXACT_OK (128 blocks) | n/a |
| referee/author reruns ref_n2.py, ref_n3_consts.py, a_index_identity.py | exit 0 (integration_reruns/) | n/a |
| iso_coverage.py (PR #65) rerun | byte-identical to the committed log, 26 s | |
| manifests | all OK except the 4 excluded .npy and the 2 relative ../N2, ../N3 paths of SHA256_N4 (see manifests.log) | |
| lake exe cache get / lake build Bgs | exit 0 / Build completed successfully (8841 jobs); 23 `#print axioms`, only propext, Classical.choice, Quot.sound | |
| unittest (clean worktrees, 256 tests, run one after the other) | failures=116 errors=103 skipped=1 | failures=116 errors=103 skipped=1 |

Unittest failure/error id lists (`unittest_failures_branch.txt`, `unittest_failures_main.txt`) have 218 lines each and are identical (comm
diff empty). Branch run: clean worktree of commit de09ffb4 (no .lake). An earlier pair of runs was concurrent. In that pair the branch run
showed 40 fewer `test_assertion_entry_policy` subtest failures (for `lineC/independent_replay/fit.py`) than main. Run sequentially, the
two lists are identical, and that module alone gives the same 104 failures and 2 errors on both trees. The concurrent runs are discarded.
