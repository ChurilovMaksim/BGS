# Evidence: Line J (2026-10-31)

Claims BGS-TRACE-221..233. Packet: [`computations/verification/lineJ/`](../../../../computations/verification/lineJ/README.md).
Note: [`mathematics/fixed-map/lineJ_d7_twisted_coefficient.md`](../../../../mathematics/fixed-map/lineJ_d7_twisted_coefficient.md).

* `receipt.json` records:
  * sha256 of every Line J file in this change: packet, Lean module, note, source review, metadata snapshot, and the logs here;
  * the claim ids and states;
  * the referee verdicts;
  * the pre-polish sha256 of `J3/REPORT_J3_v2.md`;
  * the block-basis sha256 (J3-F8).
* `INTEGRATION.md`: base commit, id assignment, claim table, registry changes, the integration polish, deviations, and the checks.
* `lake_cache_get.log`: `lake exe cache get`. Mathlib comes from the cache and is not built from source.
* `lake_build_Bgs.log`: `nice -n 10 lake build Bgs`, exit 0 ("Build completed successfully (8816 jobs)"). It builds
  `Bgs.LineJArith`, whose `#print axioms` output is extracted in `lean_axioms_LineJArith.log`:
  * only propext, Classical.choice and Quot.sound appear;
  * there is no sorryAx and no `native_decide`.
* `checkers.log`: the required checks on this branch. `checkers_baseline_main_195a24f9.log` holds the same checks on pristine main,
  where the failures are pre-existing.
* `integration_reruns/`: author scripts rerun at integration in a scratch copy of the packet (`/tmp/lj/rerun/pkt`, paths remapped by
  `run.sh`). The scripts are `sectors_exact`, `exact_B`, `fixes_checks`, `assemble_v2`, `rat_excl`, `ranks`, `inherit_proof_check`
  and `assemble16`. All JSON outputs equal the committed ones, apart from code-sha and input-path fields, and
  `fixes_checks.log` is byte-identical.
