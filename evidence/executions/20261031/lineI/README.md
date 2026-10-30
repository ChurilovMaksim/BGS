# Evidence: Line I (2026-10-31)

Claims BGS-TRACE-211..220. Packet: [`computations/verification/lineI/`](../../../../computations/verification/lineI/README.md).
Note: [`mathematics/fixed-map/lineI_rprime_reduction.md`](../../../../mathematics/fixed-map/lineI_rprime_reduction.md).

* `receipt.json`: sha256 of every Line I file in this change (packet, Lean modules, note, logs here), the claim ids and states, the
  referee verdict, the pre-fix sha256 of the documents edited for DF1–DF7, and the code/input hashes of the DF4 rerun.
* `INTEGRATION.md`: base commit, id assignment, the registry changes, the DF edits, deviations, and the list of checks.
* `lake_cache_get.log`: `lake exe cache get` (Mathlib from cache; not built from source).
* `lake_build_Bgs.log`: `nice -n 10 lake build Bgs` on the final sources, exit 0 ("Build completed successfully (8815 jobs)").
  `Bgs.LineI` and `Bgs.LineIArith` are built there, and their `#print axioms` output is in the log.
* `AxiomsLineI.lean`, `lean_axioms_LineI.log`: `lake env lean` axioms check for all 17 Line I declarations. Only propext,
  Classical.choice and Quot.sound appear. There is no sorryAx and no `native_decide` (`Lean.ofReduceBool`).
* `axioms_coverage.log`: the static `#print axioms` coverage, 1314/1314.
* `checkers.log`: the required checks on this branch. `checkers_baseline_main_4f5056b8.log` holds the same checks on pristine main;
  the failures there are pre-existing.
* `integration_reruns/`: reruns at integration in a scratch copy of the packet. The integration identity checks and the composite-d
  check are byte-identical to the committed logs. The DF2 `sym_v3`/`cert_v3` reruns are sha-identical to the committed JSONs.
