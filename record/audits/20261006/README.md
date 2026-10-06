# Scientific audit dossier — 6 October 2026

**Review in progress. Deterministic BGS remains open.** This dossier separates checked proof implications, conditional applications, finite verification and material still awaiting review. It concerns revision of the existing corpus; new solution attempts remain paused.

The [revision record](../../corpus_revision_20261006.md) explains the supplied review and repository changes. [Machine-readable coverage](coverage.json) pins the exact reviewed and current source hashes, records the scope of each reading, and identifies dependencies that are not yet covered. The [claim ledger](../../claim_ledger.md) remains the scientific-status authority. A review finding is not an external referee certificate, a formal analytic proof, or a novelty determination.

## What the review establishes

### Frozen-map structure and quantitative repairs

The repaired [symmetry proof](../../../mathematics/fixed_model_symmetry_theorem.md) now gives its norm conventions, explicit Green-operator conjugacy construction, complete affine/Pell candidate classification, rational period-three coefficient intervals and a uniform quadratic remainder. The changed implications received an independent reconstruction. The [exact certificate](../../../evidence/executions/20261006/corpus-revision/period_three_exact.json) and [independent certificate](../../../evidence/executions/20261006/corpus-revision/period_three_independent.json) are finite rational checks supporting that argument; neither is a proof of BGS.

The [effective spectral floor](../../../mathematics/frozen_effective_gap_floor.md) now takes the coefficient-field norm of the scaled integral polynomial and includes the positive denominator cost when returning to the discriminant. Roy's exact theorem and its application were checked. The separate frozen-model audit reconstructs the previously inherited FM-008 imaginary-time witness, including its all-dimension algebraic argument, as well as FM-007's logarithmic trace estimate and FM-013's bounded fixed traces. Exceptional dimensions, algebraic-time restrictions and eventual thresholds are preserved. The floor remains submicroscopic.

### Actual-start noisy limits and heat dynamics

The [circular Dyson proof](../../../mathematics/circular_dyson_actual_start.md) was checked at the contour, crossing-residue, winding, repeated-start and Fredholm passages. The [transport theorem](../../../mathematics/local_moment_transport.md) and [all-order chain law](../../../mathematics/coboundary_all_order_limit.md) were reviewed with their local moment and spatial L2 implications. The finite arbitrary-start kernel and ergodicity inputs retain their exact source boundaries.

The complementary heat-dynamics review independently reconstructs the complete quartic Wick drift and Möbius/Itô projection coefficients, closing those previously inherited algebraic leaves. It also checks the stochastic comparisons, stable-degree projections and pair-heat identities. These audits fit together; they are not two independent certifications of every step of the same chain.

The conclusions remain distinct: FLOW-014 gives an actual-start weak local noisy law on its logarithmic-time polynomial-step schedule; FLOW-017 gives all fixed factorial orders on a different superpolynomial schedule. No signed deterministic noise-removal estimate, faster clock-time theorem for the actual start, growing-order theorem or single polynomial all-order schedule has been established.

### Arithmetic, returns and resonance

All 36 Cayley-arithmetic source files received section-level reading. The review found genuine small-degree and domain defects: the ratio coefficient formula fails at K=3; low subresultant and exterior-power constructions need explicit endpoint conventions; a general determinant coefficient omitted an adjugate term; and some finite-range descriptions overstated their coverage. Scoped repairs preserve the intended large-parameter statements. Exact support, one-way support obstructions and equality of valuations remain different assertions. Some external subresultant, number-field and prime-distribution leaves remain conditional in this review. Neither sparse near-quadratic energy nor the largest-split-divisor target was proved.

The 26 return/Pell notes received full source reading and argument-level reconstruction of their scoped theorem implications. The gas estimates were not independently rederived constant by constant. The harmonic-return dependency on the harmonic-transition phase estimate is now explicit. Return laws, exceptional smooth-conjugacy constructions and local-process obstructions retain their distinct scaling assumptions; fixed moments do not determine a microscopic law.

The resonance/locality/foundations review covers 27 topic files and their relevant manuscript proof authorities. It checks oriented-orbit conventions, summability and truncation, finite-orbit rigidity, compact-tail completion, coercivity and locality. Three proof-preserving corrections distinguish oriented from signed orbits, identify the correctly weighted representative-invariant quantity, and replace an obsolete finite-classification frontier. Conditional Floquet hypotheses and unreviewed reference-source identifications remain visible. The arbitrary analytic nonlinear problem is not closed.

### Information theory and measurement scope

All ten information-theory topic notes and their authoritative TeX arguments were read. The rigidity and measurement-specific inverse/minimax statements pass the reviewed implications under their fixed-parameter and data-domain restrictions. The geometric shadow-tube application remains conditional on (EQ). A binary64 intermediate in a claimed high-precision pure-loss verifier was repaired and exposed by a negative regression; the analytic inequality itself was not refuted. A nonexistent bibliography version was corrected to the authenticated version.

## Factual correction register

| Correction | Mathematical effect | Disposition |
|---|---|---|
| Absolute (15) proposed as deterministic all-order target | Contradicts TRACE-010 in the unaveraged CUE setting | Target changed to signed (15S); absolute sufficient implication retained |
| FM-001 quantitative/classification exposition | Missing explicit load-bearing estimates | Expanded and independently reconstructed |
| FM-011 integral norm and denominator cost | Integer-polynomial hypothesis and lower-bound accounting | Scaled norm and justified three-term constant repaired |
| Obsolete actual-start and original-channel open statuses | Conflated schedules and superseding results | Current/history separation and scoped status corrections |
| Cayley small-degree/domain defects | False endpoint or undefined ancillary expression | Restricted/explicit endpoint branches; intended large-parameter chain retained |
| General frozen-symbol Gaussian extension | Constant symbol invalidates centered claim | Zero constant coefficient required; actual centered theorem unaffected |
| FLOW-016 control-character corruption | Damaged distinct-label formula | Literal distinct-index notation restored |
| O24 CUE centering outside stable ramp | CUE mean is min(m,N), not m for all bands | Ramp/plateau centering repaired; channel estimate unchanged |
| Pure-loss verifier arithmetic domain | Float contamination preceded arbitrary precision | Multiprecision division and adversarial regression added |
| Bibliographic identity/version mismatches | Incorrect metadata, not automatically false theorem use | Primary identity/version corrections; applicability checked separately |
| Archive reproduction without Git provenance | Incomplete source-manifest contract | Explicit archive manifests and negative source-change tests; final integration check pending |

The second supplied review also contains three checked proposals concerning a larger heat-identity domain, positive-measure strip bounds and a critical transport counterexample. They are **not promoted theorem changes in this revision**. Their correctness relative to named inputs must not be confused with adoption into canonical statements.

## Coverage and unresolved review work

The baseline root mathematics inventory has 162 Markdown files excluding its README; three are current or historical status indexes rather than independent proof notes. Coverage is recorded per file, not inferred from a topic name. A partial target/status check does not count as a complete mathematical reading. If a reviewed hash differs from the current source, acceptance requires explicit reconciliation of the difference.

Completed family reviews do not yet cover every spectral-bridge, fixed-control or channel/classical-bound argument. Those remaining families and verification infrastructure are pending. The full list is in [coverage.json](coverage.json), including the registered claim-dependency closure. A registered DAG can be complete as data while omitting a mathematical hypothesis; no registry pass is treated as semantic certification.

Public execution artifacts beyond the linked period-three certificates are still being integrated. Only finalized repository evidence will be linked here. Historical test counts, current repaired-source checks, numerical diagnostics, exact finite certificates and mathematical proofs will remain separate.

## Repository migration integrity

All six preserved pre-revision document snapshots match both their declared SHA-256 hashes and the declared source commit. The complete former ledger tail beginning with its status vocabulary survives in the current ledger, retaining the broader theorem tables outside the core registry. Active local Markdown fragment links were checked without a detected broken target. Compatibility for older published entry-page fragments is a separate migration check: moved headings need redirects even when no current internal link points to them. These checks protect provenance and navigation; they do not establish that all summary wording is mathematically complete.

Canonical proof paths, previous evidence and historical conclusions are preserved. Superseded rates and conditional routes remain readable as history and cannot override current status. No material was deleted merely for duplication.
