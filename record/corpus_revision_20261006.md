# Corpus revision and independent-review response — 6 October 2026

**Status: IN PROGRESS. New solution attempts are paused.** This revision repairs the existing corpus before further BGS research. It is not a claim of complete theorem certification.

## Revision base and publication boundary

The original user-supplied review inspected a 999-file archive. FM-020 was subsequently published as `9ed03f7c352430b748a76f1ab12eac96220ce57c`; its renderer-only repair is `131e8aac5684f72cc993a54a46237a812a577ae9`. Both workflows at that repaired commit passed: [scientific checks](https://github.com/ChurilovMaksim/BGS/actions/runs/37468406871) and [manuscript](https://github.com/ChurilovMaksim/BGS/actions/runs/37468406835). Later research artifacts are not promoted in this revision.

The structural inventory pins 1,014 tracked files at the FM-020 research commit; the renderer repair and this working revision add/change files. Its file count must not be presented as the final revision count. A file inventory, a test pass, and a theorem audit are different evidence.

## Response to the ten review items

| Item | Finding and disposition | Remaining acceptance step |
|---|---|---|
| 1 | Confirmed. Bridge §7 now requests signed (15S), retaining the absolute sufficient implication and the averaged-case distinction. | Final source/publication synchronization |
| 2 | Confirmed exposition gap. FM-001 now gives norms, a Green-operator conjugacy construction, affine/Pell classification, rational period-three intervals and a uniform remainder. Fresh independent review passed the repaired steps. | Preserve certificates/review and recheck dependents |
| 3 | Confirmed missing explanation. FM-011 explicitly norms the scaled polynomial K^J P and tracks the full field-degree denominator cost. | Final proof/evidence synchronization |
| 4 | Repaired to the justified sum of three contributions in the explicit bound. The prior product was not automatically a counterexample to its weaker bound. | Final publication synchronization |
| 5 | Confirmed. Corvaja–Zannier title corrected; DOI and relevant theorem remain unchanged. | Aggregate metadata check |
| 6 | Confirmed. FKM source is Counting sheaves using spherical codes, arXiv:1210.0851v5, 17 August 2013. Historical stable ID is preserved. | Aggregate metadata check |
| 7 | Added a separate cached source-metadata guard with negative mutation tests. Metadata identity is explicitly not theorem applicability. | CI integration and final run |
| 8 | Reconciled actual-start weak relaxation, superpolynomial all-order transfer, faster-time questions and deterministic noise removal. | Cross-surface/current-history reconciliation |
| 9 | Added explicit non-Git archive manifests and null upstream provenance, with source-change detection and negative tests. | Final aggregate archive/Git runs |
| 10 | Repaired the CR-corrupted distinct-index formula and added a maintained-text control-character guard. | Final aggregate check |

## Structural changes

- English/Russian entry pages are concise and synchronized. Mathematical background is separated into reader guides.
- The research brief states the current model and signed target once; cumulative historical summaries are no longer prepended to it.
- The current claim ledger precedes dated acceptance history. Its broader theorem tables are retained; the core JSON registry does not silently replace them.
- Exact previous living-document bytes are retained with hashes in [the revision archive](history/2026/corpus_revision_20261006/manifest.json).
- Canonical proof paths and immutable execution evidence are preserved. Byte-identical evidence/log files were not deleted merely because they look duplicated.

## Mathematical review coverage

The targeted status audit covers the bridge, TRACE-010 contradiction and four repaired source passages. The FM-001/FM-011 repairs received a fresh independent reconstruction and rational certificate. The FLOW-014/FLOW-017 audit reconstructs contour uniformity, repeated-start limits, Fredholm/factorial passages, transport and spatial L2 averaging, while naming its inherited algebraic leaves. Separate family audits of arithmetic, fixed-model dependencies, returns/Pell, resonance/locality and information-theory material are being reconciled.

The registered dependency graph is acyclic and structurally consistent. This does not establish that every edge contains sufficient hypotheses or that all informal dependencies were registered. Review findings outside the supplied ten items remain part of this revision.

## Verification boundary

The pre-revision source baseline passed 156 Python/C++ checks, 21 C++ builds and the pinned Lean 4.33.1 build (17 active modules, 20 Lake jobs, printed axiom lists). Those results do not certify subsequent changes; the repaired corpus must be rerun as its own pinned execution. The current Lean build closes the previously pending compilation check, not the unformalized analytic estimates.

Completion requires: checked repairs and dependency impact, coherent current documentation, source metadata checks, archive and Git reproduction, regenerated manuscript sections, an immutable final source manifest, and successful verification at the actual published revision. Unresolved mathematical review leaves will be listed explicitly rather than erased or renamed as completed.

## First checked publication checkpoint

The [frozen execution receipt](../evidence/executions/20261006/corpus-revision/checkpoint/receipt.json) records 159/159 Python/C++ checks, 17 infrastructure tests, 308 metadata mutation tests across 34 cached identities, affected C++ UBSan checks and a 256-page source-synchronized manuscript build. The snapshot excludes the pending spectral-diagnostics repair and later research. This is an incremental checked checkpoint of the in-progress corpus revision, not a declaration that all mathematical audits are complete.
