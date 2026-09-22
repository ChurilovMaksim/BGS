# BGS — arithmetic quantum chaos and spectral universality

Long-horizon research repository on rigorous routes to the Bohigas–Giannoni–Schmit (BGS) conjecture for arithmetic and nonlinear quantum maps.

**Scientific status (22 September 2026):** the fixed-strength microscopic BGS problem for the maintained frozen quantum map remains **OPEN**. The repository contains exact reductions, theorem-level project proofs, external-theorem applications, formal finite certificates, reproducible finite computations, counterexamples to insufficient proof strategies, and a consolidated research manuscript. Numerical agreement is never treated as a proof of universality.

## Research question

The central programme asks when deterministic quantizations of classically chaotic maps exhibit random-matrix local spectral statistics, and what arithmetic, dynamical, cohomological, or symmetry mechanisms can obstruct that limit.

For the maintained fixed nonlinear family

$$
U_N=\\exp(i\\tau N A_N)M_N,\\qquad \\tau=10^{-80},
$$

the decisive unresolved obligation is a model-specific **Heisenberg-scale quantum cancellation estimate**: mixed-resolvent control or an equivalent weighted joint-trace comparison for powers of order $N$. The deterministic trace-to-local-statistics bridge is already available; the missing input is the dynamical estimate for the actual fixed map.

## Current scientific picture

The repository currently establishes, in their stated scopes:

- exact trace-to-microscopic-statistics identities showing why fixed moments and $o(N)$-time trace information do not determine microscopic BGS statistics;
- arithmetic return laws and Gaussian/global limits on explicit cat-map subsequences, together with sharp counterexamples below their regularity thresholds;
- exact finite-field and Cayley-energy reductions, resultant structure, averaged arithmetic bounds, and finite independent certificates;
- a fixed-model classical symmetry theorem excluding ordinary $C^1$ centralizers, reversors, and relevant affine conjugacies in the stated perturbative range;
- a full-symbol odd-Pell Gaussian crossover and a necessary escape condition from the weak-kick obstruction;
- mixed-loop/resolvent identities and conditional barriers that sharpen the fixed-map frontier without identifying the CUE limit;
- resonance/cohomology theorems, including sharp coercivity on complete Fourier-line classes and explicit obstructions to purely local fixed-point arguments;
- negative controls and retractions documenting proof routes that fail.

The authoritative theorem scopes are not inferred from this summary. They are recorded in the claim ledger and maintained mathematical sources.

## Where to start

For a mathematical reader or referee:

1. [Source of truth](SOURCE_OF_TRUTH.md) — the repository authority hierarchy.
2. [Claim ledger](record/claim_ledger.md) — repository-wide authority for current scientific status.
3. [Stable claim registry](record/claim_registry.md), its [machine-readable source](record/claims.json), and the [dependency graph](record/scientific_dependency_graph.md) — stable identities and programme dependencies.
4. [Results index](mathematics/results.md) and [open obligations](mathematics/open_questions.md).
5. [Fixed-map frontier](mathematics/fixed_map_resolvent_frontier.md) and [trace-to-local-statistics bridge](mathematics/trace_to_local_statistics_bridge.md).
6. [Mathematics topic views](mathematics/topics/README.md) — thematic navigation without moving authoritative proof paths.
7. [Research manuscript](manuscript/BGS_unified.tex) — consolidated long-form exposition.
8. [Focused publication candidates](papers/README.md) — scoped paper manifests without duplicated proofs.
9. [External theorem registry](literature/external_dependencies.json), [evidence provenance](evidence/provenance.md), and [errata](ERRATA.md).
10. [Review protocol](REVIEWING.md), [contribution protocol](CONTRIBUTING.md), and [roadmap](ROADMAP.md).

## Evidence and claim discipline

| Level | Meaning |
|---|---|
| **EXACT** | Maintained project derivation with explicit hypotheses |
| **EXACT + EXTERNAL-THEOREM** | Exact project reduction using a named external theorem whose assumptions are tracked |
| **FINITE-CERTIFICATE** | Exact statement at explicit finite parameters |
| **FINITE-REGRESSION** | Independent implementation/reference agreement at finite parameters |
| **NUMERICAL** | Descriptive floating-point evidence |
| **CONDITIONAL** | Theorem whose stated hypotheses remain unproved for the target model |
| **OPEN** | Required closure condition not established |
| **RETRACTED** | False, superseded, or insufficient route retained for provenance |

The current status authority is [record/claim_ledger.md](record/claim_ledger.md). [record/claims.json](record/claims.json) supplies stable IDs and cross-links but cannot strengthen the ledger. Historical notes, old commits, finite computations, and manuscript prose cannot silently strengthen either.

## Research corpus

| Area | Role |
|---|---|
| [mathematics/](mathematics/README.md) | Maintained theorem statements, proofs, reductions, counterexamples, and open problems |
| [manuscript/](manuscript/README.md) | Canonical consolidated research manuscript |
| [papers/](papers/README.md) | Focused publication scopes linked to stable claim IDs |
| [literature/](literature/bibliography.md) | Theorem-level source map and external-dependency checks |
| [formalization/](formalization/README.md) | Lean 4 algebraic kernels and finite certificates with an explicit trust boundary |
| [computations/](computations/README.md) | Exact/finite verification, independent implementations, and numerical diagnostics |
| [evidence/](evidence/provenance.md) | Promoted certificates, numerical/reference data, and execution provenance |
| [record/](record/README.md) | Claim authority, machine registries, audits, retractions, and historical decisions |
| [environment/](environment/README.md) | Reproducibility target and release environment contract |
| [supplement/fixed_map/](supplement/fixed_map/README.md) | Detailed fixed-map derivations and replayable evidence |
| [archive/](archive/branch-snapshots/README.md) | Historical provenance only; not a competing source of current truth |

## Reproducibility

Start with the two cheap fail-closed gates:

```sh
python computations/verification/scientific_registry_audit.py
python computations/verification/repository_audit.py
```

Then run the maintained Python/C++ verification surface:

```sh
python -m pip install -r requirements.txt
cmake -S . -B build/cmake -DCMAKE_BUILD_TYPE=Release
cmake --build build/cmake --parallel
python computations/maintenance/verify_workspace.py \
  --build build/cmake \
  --logs build/verification-logs \
  --output build/workspace-verification.json
```

The active Lean project is pinned under `formalization/`:

```sh
(cd formalization && lake build)
```

The canonical manuscript is built with:

```sh
python computations/maintenance/sync_return_sections.py --check
python computations/maintenance/sync_fixed_map_section.py --check
python computations/maintenance/build_unified_manuscript.py \
  --output-dir build/unified-paper
```

See [REPRODUCE_unified.md](REPRODUCE_unified.md) and [environment/runtime-manifest.json](environment/runtime-manifest.json) for the execution contract. A GitHub Actions run that ends with `runner_id=0` and `steps=[]` is an infrastructure non-run, not a pass or scientific failure.

## Publication, citation, and review

`manuscript/BGS_unified.tex` is the single maintained programme manuscript. Focused publication candidates under `papers/` select coherent theorem families by stable claim ID and never duplicate proof authority.

Citation metadata is in [CITATION.cff](CITATION.cff). Research-state releases follow [RELEASES.md](RELEASES.md); archival metadata is prepared in `.zenodo.json`, but no DOI is claimed until an external archive issues one. Licensing remains an explicit release decision documented in [LICENSE_POLICY.md](LICENSE_POLICY.md).

The repository is maintained as a long-term scientific record: corrected results remain traceable, retractions are explicit, historical evidence is not rewritten, and generated publication surfaces are synchronized from maintained mathematical sources.

## Authorship and scope

Maintainer and manuscript author: **Maksim Churilov**.

The repository does not claim a general proof of the BGS conjecture, external priority for the full project corpus, or independent referee validation of every project theorem. Its purpose is to make the exact boundary between proved mathematics, imported theorems, finite evidence, conditional reductions, and open problems inspectable.
