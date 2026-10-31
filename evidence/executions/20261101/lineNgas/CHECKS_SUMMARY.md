# Lines N5–N19b integration: check results (branch lineN-gas-conditional vs main 0f57c1ad)

| check | branch | main 0f57c1ad |
|---|---|---|
| render_bibliography / claim_registry / errata / research_views / spectral_research / status --check | all exit 0 | all exit 0 |
| scientific_registry_audit | OK (408 claims, 68 EXT) | **exit 1**: inventory source blob stale (main commit 0f57c1ad changed 163's formalization; the branch inventory mirrors it) |
| repository_audit | exit 0 | exit 0 |
| wave3_integration_audit | exit 0 | exit 0 |
| wave2_integration_audit | exit 1, "integrated wrapper mapping changed" | same (pre-existing) |
| audit_manuscript_references --check | exit 0 | exit 0 |
| bibliographic_metadata_audit (plain and --self-test) | exit 1, EXT-BR-1975 only | same (pre-existing) |
| check_spectral_edition | exit 1 | same output (pre-existing) |
| sync_return_sections --check | exit 1, pandoc not installed | same (environment) |
| sync_finite_orbit_section / sync_fixed_map_section --check | exit 0 | exit 0 |
| proved_deps_gate_Ngas.py (strict 244..324) | GATE_OK, no cycles, closure conditions present | n/a |
| manifests | all OK or explained (`manifests.log`) | n/a |
| lake exe cache get / lake build Bgs | exit 0 / Build completed successfully (8855 jobs); 168 new `#print axioms`, no sorryAx | n/a |
| unittest (256 tests, run sequentially) | failures=116, errors=104, skipped=1 | failures=117, errors=104, skipped=1 |

**Unittest.**
* Main has two failures the branch does not: `test_registry_nodes` (ERROR `test_inventory_snapshot_and_statement_only_open_claim` and
  FAIL `test_inventory_metadata_drift_rejected`). Both come from main's stale inventory.
* The branch has one error main does not: `test_fractional_routing … test_current_routing_and_corruption_contract`. It **passes when
  run alone** (46 s, OK). The same environment-dependent behaviour was seen in PR #66, where the cause was the test copying the 8 GB
  built `formalization/.lake` into /tmp overlays. The main worktree has no `.lake`.
* Apart from those, the failure lists are identical (`unittest_failures_{branch,main_0f57c1ad}.txt`).
