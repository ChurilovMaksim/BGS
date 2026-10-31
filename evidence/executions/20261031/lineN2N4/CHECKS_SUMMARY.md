# Lines N2–N4 integration — check results (branch line-N2N4 vs main 3c7ac4a6)

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
