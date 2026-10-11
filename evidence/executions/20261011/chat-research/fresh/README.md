# Fresh integration checks, 11 October 2026

The [circular control manifest](circular-controls/manifest.json) pins nine active
inputs and eleven declared result/log files. Its resource-limited run compiled
and executed the independent C++ integer SSYT code and the exact Python
controls. The unindexed temporary executable was removed after execution;
all declared outputs are retained. Validate it from the BGS root with:

```sh
python3 computations/verification/chat_20261011/audit_tools/validate_manifest.py \
  evidence/executions/20261011/chat-research/fresh/circular-controls/manifest.json \
  --root .
```

The [fresh C++ build](cpp_build.json) records all 24 Release targets, source
and executable hashes, and the actual compiler/configuration logs.

The [Lean receipt](lean_execution.json) and both unedited Lake logs document
actual compilation of 23 active modules and the narrower scope of the three
new finite Std kernels. The executable-path adapter is recorded explicitly.
Existing native_decide trust assumptions remain visible in the axiom reports.
The Mathlib draft is not part of that compilation.

The [Wolfram receipt](walsh_wolfram_scope.json) points to the actual tool response
and the maintained integer source. It covers seven finite Walsh matrices and
one rational identity. It does not certify the analytic clock obstruction.

The [manuscript build](manuscript-build_manifest.json) records the preceding three-pass
283-page PDF snapshot. The [visual review](manuscript-visual-review.json)
covers only pages 278–280, containing the new chapter. Generated binaries and
page images are build products; TeX source hashes and unedited build logs are
retained here.

The [initial workspace report](workspace-initial.json) retains a 215/217 run:
both failures required explicit registration of the new claim epoch. All
scientific controls passed. The corrected epoch preserves the original 39
external theorem contracts and admits exactly seven reviewed additions;
five negative controls protect that boundary. A corrected full run is recorded
separately, rather than rewriting this failed run.

These receipts establish execution and finite coverage. Mathematical proofs,
external-source applicability and open assumptions are evaluated in the
[scientific disposition](../../../../../record/chat_integration_20261011.md).

The [corrected complete workspace report](20261011-workspace-corrected.json)
passed **217/217** checks with unchanged input hashes. Its unedited aggregate
log and the **236-test** maintenance log are retained here. Per-verifier log
hashes and source/executable hashes are in the full report; legacy per-verifier
working logs and generated certificate files remain reproducible build outputs
outside the source tree, not additional proof claims.

The source snapshot is explicit in that report. Subsequent edits only update
proof exposition, documentation, metadata and these new receipt objects; no
verifier, C++ or Lean source changed. A final editorial delta records those
paths. Remote CI checks the final committed tree independently.

The [final manuscript build](manuscript-final/build_manifest.json) includes the rounding-continuity corollary and produces **284 pages**. Its [visual review](manuscript-final/visual_review.json) covers pages 278–281. The preceding 283-page receipt remains a separate source snapshot.

The [final editorial delta](final_editorial_delta.json) confirms that the active Python, C++, Lean and Wolfram source hashes remain those of the complete run. The documented version-2 reproduction command also completed successfully after its input list was synchronized with the contract.
