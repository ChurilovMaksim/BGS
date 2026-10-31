# Evidence: Line K (2026-10-31)

Claims BGS-TRACE-234..247 (and annotations to 206, 231, 233). Packet:
[`computations/verification/lineK/`](../../../../computations/verification/lineK/REPORT_v2.md). Note:
[`mathematics/fixed-map/lineK_harg_removal.md`](../../../../mathematics/fixed-map/lineK_harg_removal.md).

* `receipt.json` records:
  * the sha256 of every Line K file in this change: the packet, the Lean module, the note, the source review, the metadata snapshot,
    and the logs here;
  * the claim ids and states;
  * the referee verdicts;
  * the pre-polish sha256 of `K2/REPORT_K2_v2.md` (W-F7 was applied at integration).
* `INTEGRATION.md`: base commit, id assignment, claim table, registry changes, W-F7, Lean coverage, deviations, and the checks.
* `lake_cache_get.log`: `lake exe cache get` ("No files to download"). Mathlib comes from the cache and is not built from source.
* `lake_build_Bgs.log`: `nice -n 10 lake build Bgs`, exit 0. It builds `Bgs.LineKFinite`. Its `#print axioms` output is extracted in
  `lean_axioms_LineKFinite.log`: no axioms, or propext and Quot.sound only; no sorryAx and no `native_decide`.
* `lean_gaps/`: the full Lemma K3(a) range 447..2645. The 62 chunk files `computations/verification/lineK/lean/K3Gaps_*.lean` and
  `K3Finite.lean` were recompiled one at a time with `nice -n 10 lean` (toolchain 4.33.1, core only) by `run.py`.
  * `summary.txt` gives the exit code, time and the running maximum RSS for each file.
  * `log_*.txt` holds the compiler output, including `#print axioms`.
  * `K3Gaps_1547` (n = 100) was OOM-killed (exit −9, ~12.2 GB). `split_1547/` re-checks its range 1547..1646 as five n = 20 chunks
    with identical definitions; all exit 0 and are axiom-free.
  * These files are **not** part of `lake build Bgs`, because a 100-modulus chunk needs 12 GB or more.
* `integration_reruns/`: the author scripts `k3_harg`, `k1_cone_check`, `k2_SZ`, `k2_large_v2` and `K2/w1_weil_check`, rerun at
  integration in a scratch copy of the packet (`run.sh`). Every log is byte-identical to the author's log, and every JSON output is
  byte-identical to the committed one (`summary.txt`). `k2_SZ.py` reads the Line J J3 rest certificates from the absolute path
  `/workspace/bgs-lineJ/J3`, so it reran against the box copy of Line J (read-only).
* `checkers.log`: the required checks on this branch. `checkers_baseline_main_121df8b4.log` holds the same checks on pristine main,
  where the failures are pre-existing.
