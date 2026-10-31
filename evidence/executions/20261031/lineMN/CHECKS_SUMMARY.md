# Line M/N integration — check results (branch line-MN vs main e4042ef2)

| check | branch | main e4042ef2 |
|---|---|---|
| render_bibliography --check | OK | OK |
| render_claim_registry --check | OK | OK |
| render_errata --check | OK | OK |
| render_research_views --check | exit 0 | exit 0 |
| render_spectral_research --check | exit 0 | exit 0 |
| render_status --check | OK | OK |
| scientific_registry_audit | OK (369 claims, 68 EXT) | OK |
| repository_audit | exit 0 | exit 0 |
| wave3_integration_audit | exit 0 | exit 0 |
| wave2_integration_audit | exit 1 "integrated wrapper mapping changed" (pre-existing) | same |
| audit_manuscript_references --check | exit 0 | exit 0 |
| sync_return_sections --check | exit 1 pandoc missing (pre-existing, environment) | same |
| sync_finite_orbit / fixed_map --check | exit 0 | exit 0 |
| check_spectral_edition | exit 1 (pre-existing) | same |
| bibliographic_metadata_audit --self-test | exit 1 EXT-BR-1975 drift only (pre-existing) | same |
| proved_deps_gate_MN.py strict 244..285 | GATE_OK, no cycles | n/a |
| lineL proved_deps_gate.py | GATE_OK | n/a |
| lineMN_checks.py | ALL_OK | n/a |
| lake exe cache get / lake build Bgs | exit 0 / 8838 jobs OK | |
| unittest (clean worktree, 256 tests) | failures=116 errors=103 skipped=1 | failures=116 errors=103 skipped=1 |

Unittest failure/error id lists (unittest_failures_branch.txt, unittest_failures_main.txt):
219 entries each, identical (comm diff empty in both directions).
Branch run: clean worktree of commit e96e6cd1 (no .lake).
checkers.log was produced in the working tree (with .lake present), so its unittest tail differs; use the clean-worktree lists above.
