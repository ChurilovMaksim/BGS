# Corpus revision and independent-review response — 6 October 2026

**Status: scoped corpus review and local acceptance complete; corrected batches published with subsequent supplements tracked below. Research resumption requires successful remote acceptance of the corrected revision.** This revision repairs the existing corpus before further BGS research. It is not a claim of complete theorem certification.

## Revision base and publication boundary

The original user-supplied review inspected a 999-file archive. FM-020 was subsequently published as `9ed03f7c352430b748a76f1ab12eac96220ce57c`; its renderer-only repair is `131e8aac5684f72cc993a54a46237a812a577ae9`. Both workflows at that repaired commit passed: [scientific checks](https://github.com/ChurilovMaksim/BGS/actions/runs/37468406871) and [manuscript](https://github.com/ChurilovMaksim/BGS/actions/runs/37468406835). Later research artifacts are not promoted in this revision.

The structural inventory pins 1,014 tracked files at the FM-020 research commit; the renderer repair and this working revision add/change files. Its file count must not be presented as the final revision count. A file inventory, a test pass, and a theorem audit are different evidence.

## Response to the ten review items

| Item | Finding and disposition | Acceptance disposition |
|---|---|---|
| 1 | Confirmed. Bridge §7 now requests signed (15S), retaining the absolute sufficient implication and the averaged-case distinction. | Local synchronization passed; final remote receipt pending |
| 2 | Confirmed exposition gap. FM-001 now gives norms, a Green-operator conjugacy construction, affine/Pell classification, rational period-three intervals and a uniform remainder. Fresh independent review passed the repaired steps. | Exact certificates preserved; scoped dependency review complete |
| 3 | Confirmed missing explanation. FM-011 explicitly norms the scaled polynomial K^J P and tracks the full field-degree denominator cost. | Proof/evidence synchronized; final remote receipt pending |
| 4 | Repaired to the justified sum of three contributions in the explicit bound. The prior product was not automatically a counterexample to its weaker bound. | Locally complete; final remote receipt pending |
| 5 | Confirmed. Corvaja–Zannier title corrected; DOI and relevant theorem remain unchanged. | Metadata guard and mutation tests passed |
| 6 | Confirmed. FKM source is Counting sheaves using spherical codes, arXiv:1210.0851v5, 17 August 2013. Historical stable ID is preserved. | Metadata guard and mutation tests passed |
| 7 | Added a separate cached source-metadata guard with negative mutation tests. Metadata identity is explicitly not theorem applicability. | CI integrated; local final run passed |
| 8 | Reconciled actual-start weak relaxation, superpolynomial all-order transfer, faster-time questions and deterministic noise removal. | Current/history reconciliation completed |
| 9 | Added explicit non-Git archive manifests and null upstream provenance, with source-change detection and negative tests. | 159-check Git checkpoint and 161-check archive run passed |
| 10 | Repaired the CR-corrupted distinct-index formula and added a maintained-text control-character guard. | Passed in repaired-source execution |

## Structural changes

- English/Russian entry pages are concise and synchronized. Mathematical background is separated into reader guides.
- The research brief states the current model and signed target once; cumulative historical summaries are no longer prepended to it.
- The current claim ledger precedes dated acceptance history. Its broader theorem tables are retained; the core JSON registry does not silently replace them.
- Exact previous living-document bytes are retained with hashes in [the revision archive](history/2026/corpus_revision_20261006/manifest.json).
- Canonical proof paths and immutable execution evidence are preserved. Byte-identical evidence/log files were not deleted merely because they look duplicated.

## Mathematical review coverage

The targeted status audit covers the bridge, TRACE-010 contradiction and four repaired source passages. The FM-001/FM-011 repairs received a fresh independent reconstruction and rational certificate. The FLOW-014/FLOW-017 audit reconstructs contour uniformity, repeated-start limits, Fredholm/factorial passages, transport and spatial L2 averaging, while naming its inherited algebraic leaves. Family audits of arithmetic, fixed-model dependencies, returns/Pell, resonance/locality, heat dynamics, spectral bridges, channels and information-theory material are reconciled in the complete scoped coverage dossier.

The registered dependency graph is acyclic and structurally consistent. This does not establish that every edge contains sufficient hypotheses or that all informal dependencies were registered. Review findings outside the supplied ten items remain part of this revision.

## Verification boundary

The pre-revision source baseline passed 156 Python/C++ checks, 21 C++ builds and the pinned Lean 4.33.1 build (17 active modules, 20 Lake jobs, printed axiom lists). Those results do not certify subsequent changes; the repaired corpus must be rerun as its own pinned execution. The current Lean build closes the previously pending compilation check, not the unformalized analytic estimates.

Completion requires: checked repairs and dependency impact, coherent current documentation, source metadata checks, archive and Git reproduction, regenerated manuscript sections, an immutable final source manifest, and successful verification at the actual published revision. Unresolved mathematical review leaves will be listed explicitly rather than erased or renamed as completed.

## Additional findings beyond the initial ten items

- Small-degree arithmetic statements and order-three subresultant constructions now state their valid ranges and trivial low-degree exceptions. The determinant coefficient includes its omitted adjugate contribution. These repairs preserve intended large-parameter conclusions.
- FM-002's general-symbol paragraph now explicitly separates the zero Fourier mode; its detailed finite-alphabet and sparse-orbit proof inputs are linked.
- TRACE-011's general raw extension now includes active zero frequencies in its energy; a clock witness shows why they cannot be omitted.
- Oriented/signed-orbit wording, representative-change weights and superseded finite-support status have been corrected.
- Pure-loss verification no longer introduces binary64 division into high-precision arithmetic; new precision and mutation controls pass. The nonexistent ISS arXiv v4 locator is corrected to v1.
- The runner protects sources and manifests from output overlap, disables inherited Python optimization for assertion-based checks, records compiler-selected Boost, and blocks dependent replays after a failed producer. A C++ signed overflow was repaired with boundary-prime sanitizer tests.
- [Spectral preprocessing](audits/spectral_diagnostics_correction_20261006.md) now preserves level order and reports undefined spread honestly. All 168 original processing instances and nine bandwidth/edge settings were replayed. Sensitivity is material; no robust GOE-agreement assertion is made. Original numerical records remain historical and unchanged.

## Completed reading map and remaining acceptance work

[The consolidated dossier](audits/20261006/README.md) accounts for all 162 root mathematics files: 159 scoped semantic readings and three indexes. Its 124 passed-for-reviewed-scope and 35 conditional-on-named-inputs dispositions are not 159 unconditional theorem certifications. External inputs, inherited proof leaves, numerical evidence and formal kernels remain separately labelled.

The first checked publication checkpoint and subsequent final acceptance must be identified by their actual remote commits and execution receipts. The corrected source snapshot has now passed a separate complete 161-check archive-mode execution. Final publication and remote acceptance remain pending; the earlier 159-check frozen checkpoint is not relabelled as validation of later changes.

## First checked publication checkpoint

The [frozen execution receipt](../evidence/executions/20261006/corpus-revision/checkpoint/receipt.json) records 159/159 Python/C++ checks, 17 infrastructure tests, 308 metadata mutation tests across 34 cached identities, affected C++ UBSan checks and a 256-page source-synchronized manuscript build. The snapshot excludes the pending spectral-diagnostics repair and later research. This is an incremental checked checkpoint of the in-progress corpus revision, not a declaration that all mathematical audits are complete.

## Final repaired-source local acceptance

The [final execution receipt](../evidence/executions/20261006/corpus-revision/final/receipt.json) records the immutable archive source manifest and 161/161 successful Python/C++ runs with unchanged source fingerprints and genuinely null Git provenance. All 21 C++ programs were freshly compiled and their resulting executable hashes matched the executed binaries. Seventeen maintenance tests passed under both ordinary and optimized parent Python. The pinned Lean build completed 17 active modules in 20 jobs with printed trust dependencies. A separately source-pinned manuscript build passed at 256 pages. These are execution and compilation claims, not certification of the unformalized analytic corpus.

The archive run includes the corrected spectral diagnostics and TRACE-011 repair. Subsequent documentation/evidence changes are recorded separately; no later source is silently assigned the archive run's identity. Both workflows for the first published checkpoint `25cde6388a41d31c9d64bfbc889086e27103f42c` succeeded: [scientific checks](https://github.com/ChurilovMaksim/BGS/actions/runs/37476525838) and [manuscript](https://github.com/ChurilovMaksim/BGS/actions/runs/37476525812). The final correction batch still requires its own remote acceptance.

The scoped overhaul leaves named external-source and application conditions visible. In particular, the unretrieved original Pesin theorem text and identified arithmetic reference leaves are not reported as newly verified primary-source applications. The deterministic signed BGS obligation remains open.

## Published final correction batch and subsequent source supplement

The corrected diagnostics, completed scoped coverage and final local execution artifacts are published as [98a22bef5385ebc5c3bcf132c994a6e514cfc59c](https://github.com/ChurilovMaksim/BGS/commit/98a22bef5385ebc5c3bcf132c994a6e514cfc59c), parent `25cde6388a41d31c9d64bfbc889086e27103f42c`, exact tree `309db7e68a67fcfb43a02d1c4f8a113719943751`. Both remote workflows succeeded: [scientific checks](https://github.com/ChurilovMaksim/BGS/actions/runs/37480746956) and [manuscript](https://github.com/ChurilovMaksim/BGS/actions/runs/37480746943). The subsequent standalone guard and source-note supplement require their own checks.

A subsequent [entropy-source supplement](../literature/smooth_area_entropy_supplement_20261006.md) verifies the needed formula through Mañé (1981), p.95 equation (2), and the complete 1983 errata. This closes the mathematical entropy-input retrieval gap through an alternate primary source while preserving the original Pesin-text locator limitation and original snapshot records.

## Fourth supplied review: standalone certificate safety

A fresh negative control confirms that direct optimized execution of `collective_diffusion_gap.py` could print PASS after Python removed its assertions. The aggregate runner already explicitly enables child assertions, so this finding does not invalidate the recorded normal runs or the unchanged mathematical identities. The standalone entry now rejects disabled assertions before verification or certificate output. A maintained regression checks valid and temporarily mutated sources across ordinary Python, `-O`, `-OO`, and both optimization environment settings. [The narrow receipt](../evidence/executions/20261006/standalone-guard/receipt.json) records 18 maintenance tests passing normally and under an optimized parent, including ten new CLI subcases per run. Earlier execution hashes are preserved and the changed verifier is explicitly reconciled in coverage.

The other supplied proposals are mathematical additions, not discovered errors in the maintained FM-019 theorem. Their submitted numerical attachments were not supplied here and their reported counts are not promoted as independently reproduced evidence. The phase-helper precision observation does not establish an incorrect returned Hermitian reconstruction.
