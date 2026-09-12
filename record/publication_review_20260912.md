# Publication and reproducibility review — 12 September 2026

## Purpose and boundary

This revision integrates existing return-law proofs into the canonical article,
updates research navigation, and verifies the maintained computational and
formalization interfaces. It is not a new full proof audit or an external
referee report. No BGS closure or priority claim is added.

## Changes

- The five return-law proof modules become chapters of the single canonical
  TeX manuscript. A maintained Pandoc synchronizer records source hashes,
  preserves mathematical content, and gives new equation tags a `Ret.` prefix.
  Local section/theorem references are explicitly explained in each chapter.
- README is shortened to a research entry point; RESEARCH.md records the model
  choice, contribution boundaries, and decisive next questions. Historical
  execution narratives remain in dated records instead of the front page.
- The verifier runner now supplies the mandatory output argument for all eight
  return-law producers and supports explicitly recorded focused selections.
- The general note states the exact classical action normalization
  `kappa = epsilon/(2 pi N)`; the earlier `epsilon/N` wording described a scale.
- The invariant modulo-two refinement gains polarization and central-parity
  Lean checks. Existing proof modules and C++ kernels are retained.
- Manuscript workflows check synchronization and install Pandoc and the extra
  TeX packages needed by the actual source. Cloud execution is not asserted.

## Executed checks

The eight focused Python checks all exited zero. Their finite and numerical
scope remains the scope documented by their individual producers. The input
Git commit was `83b48105757a0b01bb6e5c86438894b344a3dd63`; this publication revision
was an uncommitted working-tree change during execution. The verifier source
hashes below identify the executed programs without implying a clean checkout.

| Producer | Execution | Source SHA-256 |
|---|---|---|
| analytic_kick_return_gas | PASS | `9864c2ae144b8628bd78f530ee2b164443d29b8dae9275f39fb5936e9f262a27` |
| even_period_spin_resonance | PASS | `d9296cdc1abd14fea773d849a1992ea11d763b1fd21f648d62588dff509e68b5` |
| fixed_harmonic_return_gas | PASS | `783cd67b2aed5417c5f2a076839f2b417c54c62c7e55f4cc78c1052aaf29849e` |
| general_cat_return_laws | PASS | `c9683699c0857778427f3a5aca548e59173904fee32ff1effd653a7c4f5c9e6c` |
| hyperbolic_return_pressure | PASS | `deb55ebaa89fb1825432ba46dabb9bff3dca1f5ae43ac36c6dee7f6972d22411` |
| pell_resonance_lattice | PASS | `ff3ddd3447cb57366555b81d86a57c8d9990a8d7ea1e32332c104c5f229e6554` |
| periodic_point_trace_comparison | PASS | `ea3662c3a89c991cd608f1b929cfdcb06280f4d25437dc9bd1f21a66c4b9b807` |
| phase_space_return_gas | PASS | `c7fd044539aa16bf5b01fc961bc32fff10626959f570d3ca516d890fd034bf7f` |

The complete historical Python/C++ suite was not rerun. No new C++ source was
needed for publication integration. Commands for focused and complete runs
are in [REPRODUCE_unified.md](../REPRODUCE_unified.md).

The official Lean 4.33.1 Linux archive was checked against release SHA-256
`890afd185370f85666025b883914ab4f4b339136f8c96167b69cfb62aecaf235`.
The full project built successfully: 16 active modules, 19 Lake jobs.
`refinement_polarization` and `nontrivial_central_parity` have empty printed
axiom lists. Other modules retain the native-evaluation trust boundary
specified in [formalization/README.md](../formalization/README.md).
The existing proc-self compatibility shim was used in this environment.

The canonical article built successfully with three pdfLaTeX passes to
214 pages. The builder rejected no undefined references/citations, duplicate
PDF destinations, or overfull boxes. Generated source was checked for drift. All 1,656 source math nodes were
found unchanged in the generated TeX after the declared equation-tag renaming;
the synchronizer now enforces this preservation check on every run.
Title, theorem, equation, and chapter-opening pages were visually inspected;
this was a layout sample, not a visual review of all 214 pages.

PDF SHA-256 for this execution: `2734e5a1889d66037507679b631c71312ac0d1878102298da239b808f3d00bb4`.
Build timestamps can change PDF bytes on another run. The build manifest
records the input source hashes and remains with the generated PDF in
`build/unified-paper/`; execution logs remain in `build/publication-return-checks/`.

The structural repository gate and whitespace check are run before publication.
Generated binaries, PDF intermediates, and local toolchain installations are
excluded from Git. Unique mathematical sources and historical audit provenance
are preserved; publication cleanup does not erase earlier corrections.

## Remaining publication work

This is a consolidated research collection suitable for a scoped review.
A focused journal submission should select one coherent theorem family and
obtain an independent proof and literature audit. A grant submission still
requires a specific call, investigator details, resources, and budget.
The global logarithmic-time results do not close the fixed-classical-strength,
Heisenberg-time microscopic BGS problem.
