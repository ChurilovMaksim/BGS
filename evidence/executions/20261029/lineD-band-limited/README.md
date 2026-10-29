# Line D execution evidence (29–30 October 2026)

## Research-box logs (deposited with the packet; not re-executed in this integration)

* `lean_v2_build.sh`: isolated Lean build (fresh copy of the formalization tree, `lake exe cache get` first, then
  `lake build Bgs.LineDCerts`, sha256 and grep). Results: `lean_v2_cache_get.log` (exit 0, 8689 cached files, no Mathlib
  build), `lean_v2_build.log` (Built Bgs.LineDCerts 46 s, "Build completed successfully", exit 0; axioms ∅ or {propext}),
  `lean_v2_grep.log` (no sorry/native_decide/admit/implemented_by/extern/unsafe/opaque/axiom/import), `lean_v2_import_test.log`
  (a file with `import Bgs.LineDCerts` compiles). The script names the research-box paths `/workspace/bgs-lineD` and
  `/workspace/bgs-build`; it is a record of that run, not a repository command.
* Numerical logs: `computations/verification/lineD/logs/`; referee replay and logs: `computations/verification/lineD/referee_replay/`.
* Monte Carlo seeds: p = 101 seed 11 (flat), seed 3 (diag7, k7only); p = 211 seed 21; p = 401 seed 41.

## Integration build (this checkout, Lean 4.33.1)

`integration_lake_build_Bgs.log` is `lake exe cache get` followed by a full `lake build Bgs`.

* Cache: exit 0, "No files to download", "Already decompressed 8690 file(s)". The Mathlib package oleans came from that cache. Mathlib was not built from source. The in-repo modules under `formalization/Bgs/Mathlib/` are part of `Bgs` and were compiled against those oleans.
* Build: exit 0, "Built Bgs.LineDCerts (40s)", "Build completed successfully (8796 jobs)", elapsed 240 s.
* `integration_axioms.log` (`lake env lean` on `AxiomsLineD.lean`, exit 0). No axioms for `hx_ok`, `fix_count`, `D_values`, `hx_control`, `fix_control`. Axiom `propext` only for `rad_count`, `coll4_ok`, `coll6_ok`, `rad_control`, `coll_control`. The same lines appear in the build log from the `#print axioms` commands at the end of `LineDCerts.lean`.
* `integration_grep.log`: the module matches none of sorry, native_decide, admit, implemented_by, extern, unsafe, opaque, an axiom declaration, or import.
* Checker logs from this integration: `integration_checkers.log`, `integration_unittests.log`, `integration_compileall.log`.

`receipt.json` records the sha256 of the packet tarball and of the integrated files. On main `d6fa6e2a` the highest registered TRACE id was BGS-TRACE-148, so BGS-TRACE-149 was the next free id. Historical gaps BGS-TRACE-138 and BGS-TRACE-139 were left unused. The Line B packet had not merged, and these statements were not renumbered.
