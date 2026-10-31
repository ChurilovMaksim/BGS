# Lines M and N integration evidence (31 October 2026)

* `receipt.json`: base, ids, states, and the sha256 of every packet file, Lean module, source note, metadata snapshot and log in this directory.
* `INTEGRATION.md`: what was integrated, the Line N errata written at integration, the annotations, the excluded files and the deviations.
* `integration_reruns/`: scratch-copy reruns of four author scripts, all identical (`summary.txt`).
* `manifests.log`: `sha256sum -c` of the four packet manifests. The only failures are the third-party literature files that were deliberately not copied.
* `lake_cache_get.log`, `lake_build_Bgs.log`: `nice -n 10 lake exe cache get`, then `nice -n 10 lake build Bgs` (exit 0, 8838 jobs).
* `lean_axioms_LineMArith.log`, `lean_axioms_LineNArith.log`: `#print axioms` for every theorem. Only propext, Classical.choice and Quot.sound appear, or no axioms at all; no sorryAx.
* `checkers.log`, `checkers_baseline_main_e4042ef2.log`, `unittest_failures_branch.txt`, `unittest_failures_main.txt`: the checker suite on this branch and on main.
