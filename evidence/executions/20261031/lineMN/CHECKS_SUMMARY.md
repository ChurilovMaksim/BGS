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

## Rerun after the owner audit of PR #65 (fix commit b09ae6e3)

R1–R3, S1–S3 applied (claims 246, 247, 258, 278, 279, 280, 284; EXT-CP-2011; REPORT_N_v2 §2, §3, W⁺, §12 I-1/I-5; note; sources).
Registry, inventory (blob 1541d7bc…), epochs (regenerated, byte-identical) and metadata snapshot (sha256 fd9f2a1c…) regenerated; receipt 89 files.

| check | result |
|---|---|
| iso_coverage.py (new; analytic case split for all p + grid 10^264.5..10^400 and larger p, all 4 families) | ISO_COVERAGE_OK: 0 uncovered with Gauss + 3/8 + 5/8; 4748748 uncovered with Gauss + 5/8 only (first at log10 p = 266.4) |
| render --check ×6 | OK |
| scientific_registry_audit | OK (369 claims, 68 EXT) |
| repository_audit, wave3 | exit 0 |
| wave2, sync_return_sections, check_spectral_edition, bibliographic EXT-BR-1975 | same pre-existing failures as main e4042ef2 |
| proved_deps_gate_MN.py / lineL gate | GATE_OK / GATE_OK |
| lineMN_checks.py | ALL_OK (log identical) |
| lake exe cache get / lake build Bgs | exit 0 / Build completed successfully (8838 jobs), no sorry |
| unittest (clean worktree of b09ae6e3, 256 tests) | 116F / 103E / 1 skipped; list identical to main (unittest_failures_branch_audit65.txt vs unittest_failures_main.txt, empty diff) |
