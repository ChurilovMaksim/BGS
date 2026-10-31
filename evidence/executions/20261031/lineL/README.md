# Line L + L2 + L3 integration evidence (31 October 2026)

* `receipt.json`: base, ids, states, sha256 of every packet file, Lean module and logs in this directory.
* `INTEGRATION.md`: what was integrated, the errata applied at integration, state reviews, deviations.
* `integration_reruns/`: scratch-copy reruns of the OP certificate, the constants and two L3 checks (`summary.txt`).
* `lake_cache_get.log`, `lake_build_Bgs.log`: `nice -n 10 lake exe cache get` then `nice -n 10 lake build Bgs` (exit 0, 8836 jobs).
* `lean_axioms_LineLConst.log`: `#print axioms` output of `formalization/Bgs/LineLConst.lean` (no axioms).
* `checkers.log`, `checkers_baseline_main_e9e1550a.log`: the checker suite on this branch and on main.
