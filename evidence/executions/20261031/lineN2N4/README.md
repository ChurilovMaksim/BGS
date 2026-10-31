# Evidence: Lines N2–N4 integration (31 October 2026)

* `INTEGRATION.md`: what was integrated, the N4 errata, the claim mapping, and the PR #65 iso_coverage check.
* `CHECKS_SUMMARY.md`: check results on this branch vs main 5c292e7e (owner audit of #66), and the earlier record vs 3c7ac4a6.
* `receipt.json`: sha256 of every integrated file, ids and states, the excluded large files.
* `manifests.log`: author and referee manifest verification.
* `checkers.log`, `checkers_baseline_main_3c7ac4a6.log`, `unittest_failures_branch.txt`, `unittest_failures_main.txt`: the checker suite on this branch and on main.
* `lake_cache_get.log`, `lake_build_Bgs.log`, `lean_axioms_LineN{2,3,4}Arith.log`: Lean build.
* `integration_reruns/`: reruns of referee/author scripts and of the PR #65 iso_coverage.py.
* `owner_audit_pr66/`: reruns after the owner audit of PR #66: the checker suite on the branch and on main 5c292e7e, the gates, the N4 integration checks, unittest lists, and lake logs.
