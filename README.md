# WoW — arithmetic quantum chaos

A research collection on quantized hyperbolic toral automorphisms, arithmetic
resonances, and the passage from quantum dynamics to spectral statistics.
The current return-law programme treats every **fixed hyperbolic matrix in
SL(2,Z)** along explicitly constructed arithmetic dimension subsequences.

## Scientific status

The principal current derivations establish Gevrey return laws, a joint
Gaussian limit for period-averaged observables under a square-root logarithmic
Fourier weight, and continuous counterexamples showing the sharpness of that
weight even after quantum centering. Constants depend on the fixed map and
symbol. These are global laws at logarithmic return times.
The [local-limit obstruction](mathematics/return_trace_obstruction.md) now
connects nonuniform short returns to failure of ergodic intensity-one local
limits, under explicitly stated unfolding and scaling conventions.
Its extension quantifies intensity loss, proves a sharp bound for ergodic
local limits among abstract spectra, and shows why the same return law can
coexist with different statistics after unfolding by the local density.

**Microscopic BGS universality remains open.** The analytic results are project
proofs with limited internal review; external priority and external referee
validation have not been established. Lean checks a smaller algebraic and
finite layer. Numerical experiments do not certify asymptotic theorems.

## Start here

- [Research brief](RESEARCH.md): why cat maps, contributions, limitations, and the next decisive questions.
- [General return laws](mathematics/general_cat_return_laws.md): assumptions, statements, proofs, and counterexamples.
- [Results index](mathematics/results.md) and [earlier addendum](mathematics/results_20260907_addendum.md): the broader mathematical corpus.
- [Claim ledger](record/claim_ledger.md) and [scoped addendum](record/claim_ledger_addendum_20260907.md): evidence levels and corrections; the addendum governs claims in its stated scope.
- [Canonical manuscript](manuscript/WoW_unified.tex): one publication entry point, including the six return-law proof modules.
- [Reproduction guide](REPRODUCE_unified.md) and [publication review](record/publication_review_20260912.md): commands and the scope of actual checks.

## Research materials

| Directory | Role |
|---|---|
| [mathematics](mathematics/README.md) | Maintained proofs, theorem index, and unresolved obligations |
| [manuscript](manuscript/README.md) | Canonical TeX source and its component sections |
| [computations](computations/README.md) | Python reference verifiers, independent C++ kernels, and figure producers |
| [formalization](formalization/README.md) | Pinned Lean 4 project and explicit trust boundary |
| [evidence](evidence/provenance.md) | Selected certificates and their provenance |
| [record](record/claim_ledger.md) | Scoped reviews, corrections, and execution records |
| [archive](archive/branch-snapshots/README.md) | Historical provenance; no parallel active branch copies |

## Reproduce

From the repository root, install the Python requirements and run the structural gate:

```sh
python -m pip install -r requirements.txt
python computations/verification/repository_audit.py
```

With Pandoc and a TeX installation available, verify the generated return-law
chapters and build the article:

```sh
python computations/maintenance/sync_return_sections.py --check
python computations/maintenance/build_unified_manuscript.py --output-dir build/unified-paper
```

The [reproduction guide](REPRODUCE_unified.md) provides the complete Python/C++
run, focused return-law checks, and Lean build. Generated reports and PDFs stay
in `build/`; source, formalization, and maintained programs belong in `main`.
Historical run counts and manuscript page counts are kept in dated reviews,
so they cannot be mistaken for a fresh full verification.

The scientific scope is determined by explicit hypotheses and proofs, not by
repository synchronization or a successful software build.
