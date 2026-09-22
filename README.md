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

The authoritative theorem scopes are not inferred from this summary. They are recorded in the claim ledger and the maintained mathematical notes.

## Where to start

For a mathematical reader or referee, the recommended order is:

1. [Claim ledger](record/claim_ledger.md) — repository-wide authority for the current status of claims.
2. [Results index](mathematics/results.md) — concise map of established results and their boundaries.
3. [Fixed-map frontier](mathematics/fixed_map_resolvent_frontier.md) — the maintained frozen model and the remaining BGS estimate.
4. [Open questions](mathematics/open_questions.md) — unresolved obligations only.
5. [Trace-to-local-statistics bridge](mathematics/trace_to_local_statistics_bridge.md) — exact Heisenberg-scale reduction.
6. [Research manuscript](manuscript/BGS_unified.tex) — consolidated long-form exposition.
7. [Literature map](literature/bibliography.md) — load-bearing external results and scope checks.
8. [Evidence provenance](evidence/provenance.md) — interpretation of promoted certificates and numerical records.
9. [Retractions](record/retractions.md) — false, superseded, or insufficient historical routes.
10. [Repository conventions](record/repository_conventions.md) — source-of-truth, synchronization, archival, and review policy.

## Evidence and claim discipline

The project distinguishes the following levels:

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

The current status authority is [record/claim_ledger.md](record/claim_ledger.md). Historical notes, old commits, finite computations, and manuscript prose do not silently strengthen it.

## Research corpus

| Area | Role |
|---|---|
| [mathematics/](mathematics/README.md) | Maintained theorem statements, proofs, reductions, counterexamples, and open problems |
| [manuscript/](manuscript/README.md) | Canonical consolidated research manuscript |
| [literature/](literature/bibliography.md) | Theorem-level source map and literature boundary |
| [formalization/](formalization/README.md) | Lean 4 algebraic kernels and finite certificates with an explicit trust boundary |
| [computations/](computations/README.md) | Exact/finite verification, independent implementations, and numerical diagnostics |
| [evidence/](evidence/provenance.md) | Promoted certificates, reference data, and execution provenance |
| [record/](record/claim_ledger.md) | Claim authority, audits, retractions, research process, and historical decisions |
| [supplement/fixed_map/](supplement/fixed_map/README.md) | Detailed fixed-map derivations and replayable evidence |
| [archive/](archive/branch-snapshots/README.md) | Historical provenance only; not a competing source of current truth |

## Reproducibility

The repository is designed so that theorem statements, verification code, formal certificates, manuscript text, and status records can be audited separately.

The structural gate is:

```sh
python -m pip install -r requirements.txt
python computations/verification/repository_audit.py
```

The maintained Python/C++ verification surface is:

```sh
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

See [REPRODUCE_unified.md](REPRODUCE_unified.md) for the complete reproduction contract and the exact boundary between local execution records and cloud CI.

## Publication and review model

`manuscript/BGS_unified.tex` is the single maintained long-form research manuscript. It is a consolidated research record rather than a claim that every theorem family should be submitted as one journal article. Focused publication should extract coherent theorem families while preserving the repository-level dependency graph and provenance.

The repository is maintained as a long-term scientific record: corrected results remain traceable, retractions are explicit, historical evidence is not rewritten, and generated publication surfaces are synchronized from their maintained mathematical sources where applicable.

## Authorship and scope

Maintainer and manuscript author: **Maksim Churilov**.

The repository does not claim a general proof of the BGS conjecture, external priority for the full project corpus, or independent referee validation of every project theorem. The goal is to make the exact boundary between proved mathematics, imported theorems, finite evidence, conditional reductions, and open problems inspectable.
