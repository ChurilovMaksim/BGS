# Constructive-batch execution evidence

This package records bounded execution and provenance checks. It is not a mathematical proof audit or a BGS theorem. The initial frozen local archive passed 178/178 workspace checks with 1,786 unchanged files and no source-validation error. Its upstream provenance remains null. Integration base 300d99270d11c87d0aa84e9d8f624491788629ba is context only, not authenticated archive provenance.

## Actual scope

- The maintenance suite passed 43/43 normally and 43/43 under an optimized parent. The workspace verifier itself ran with an unoptimized parent; its child assertions were enabled.
- The supplement passed 28/28 selected isolated replays, with 116 inventory files. Its explicit exclusions remain in supplement.json.
- All 22 prior standalone C++ source/binary pairs matched the 23 C++ workspace executions. There was no new C++ compilation in this batch. The previous build receipt is referenced explicitly.
- Lean actually ran an incremental full active build: 19 active modules, 22 successful Lake jobs, with SevenPrimary freshly compiled and prior modules replayed. The log retains native-decision-generated axioms. The 21 input hashes include the active root, toolchain and recorded module sources; they do not mean 21 active theorem modules. Generic polynomial/Rabin semantics, rank lifting, the analytic arguments and the actual commutant theorem are outside this formalized scope.
- All 178 raw workspace logs and 28 supplement logs were hash-verified. The full index is retained, together with the seven newly added workspace-check logs.

## Manuscript history and repaired scope

The original three-pass manuscript build is preserved as FAIL: three overfull boxes, despite zero compiler return codes. Two subsequent setup attempts failed before substantive compilation (missing format, then kpathsea database lookup). Their failed manifests and available logs remain separate.

The final repaired build passed three passes, with 266 pages, 88 unchanged TeX inputs and no forbidden warning. Exactly two TeX files differ from the initial snapshot: discretionary line-break markers in five source filenames. source-delta.json records before/after hashes and exact replacements; those replacements were independently replayed against the initial bytes. Every source hash, pass-log hash, final LaTeX-log hash and PDF hash was independently matched. The integrator reports visual inspection of physical pages 258–263, covering the repaired paragraphs and new sections, with no clipping, overlap or glyph defects. The recorded image hashes and PDF identity were independently verified here; this curation does not claim another visual inspection or a full-document review. The PDF is fingerprinted here, not embedded.

## Snapshot and curation boundaries

The initial workspace run predates the typesetting repair, this evidence package and later integration records. It is not relabeled as a run of those later bytes. One later final-snapshot workspace run may be appended separately after integration. Its receipts necessarily postdate that frozen source snapshot; they do not recursively certify their own inclusion.

Machine-specific paths use declared roles in path-roles.json. raw-public-hashes.json records raw and curated digests for each imported artifact, including factored source manifests. JSON serialization and declared path replacements are the only public transformations. No historical raw receipt is overwritten. Source files in an inventory are not distinct executions or proof readings. Fixed-strength microscopic BGS remains OPEN.
