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

The 20--21 September continuation adds a theorem excluding smooth classical
centralizers/reversors for the actual frozen model, a full-symbol odd-Pell
Gaussian crossover with exact variance `1650797/4000000`, a stronger
three-orientation mixed-loop barrier, and sharp resonance coercivity on every
Fourier-line (H^{1+\beta}) class in its stated positive-coercivity range.
These advances remove several candidate obstructions but do not provide the
missing Heisenberg-scale quantum cancellation estimate.

**Microscopic BGS universality remains open.** The analytic results are project
proofs with limited internal review; external priority and external referee
validation have not been established. Lean checks a smaller algebraic and
finite layer. Numerical experiments do not certify asymptotic theorems.

## Start here

- [Final recovery/integration audit](record/final_research_handoff_20260921.md): reconciles the late handoff, old PRs, replay status, and the remaining target.
- [14--16 September dossier reconciliation](record/verified_state_reconciliation_20260921.md): recovers the earlier Heisenberg-scale direct attack, promotes only repaired claims, and records later retractions.
- [Exact fixed-map Weyl path escape](mathematics/fixed_map_weyl_path_escape.md) and [19-adic dephasing](mathematics/hyperbolic_19adic_dephasing.md): recovered direct Heisenberg-time structure.
- [Repaired cyclic CUE ramp](mathematics/fixed_map_unistochastic_ramp.md): the corrected frozen one-step FIO has an eventual uniform unistochastic gap and its exact cyclic path sector supplies the CUE ramp below the plateau; the post-cyclic residual remains open.
- [All-time classical stability sum](mathematics/fixed_map_classical_sum_rule.md): exact periodic counts and exponentially accurate stability-weighted sum for the corrected frozen classical map.
- [Exact history/reconnection algebra](mathematics/quantum_history_reconnection.md) and [unitary encounter envelope](mathematics/unitary_encounter_envelope.md): finite-dimensional normalization/long-link identities and a convergent universal combinatorial envelope; genuine partner localization and the post-cyclic residual remain open.
- [Recovery audit](record/recovery_audit_20260920.md): reconciled the preceding chat/repository state and recovered omitted amendments.

- [Fixed-map frontier](mathematics/fixed_map_resolvent_frontier.md): the exact frozen model, mixed-loop criterion, new low-order bounds, and the unresolved estimate.
- [Reproducible fixed-map supplement](supplement/fixed_map/README.md): recovered proofs, Python/C++/Wolfram sources and finite evidence; [current verification review](record/fixed_map_publication_20260920.md).
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
| [supplement/fixed_map](supplement/fixed_map/README.md) | Indexed fixed-map proofs and computational evidence, with isolated replay |
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
python computations/maintenance/sync_fixed_map_section.py --check
python computations/maintenance/build_unified_manuscript.py --output-dir build/unified-paper
```

The [reproduction guide](REPRODUCE_unified.md) provides the complete Python/C++
run, focused return-law checks, and Lean build. Generated reports and PDFs stay
in `build/`; source, formalization, and maintained programs belong in `main`.
Historical run counts and manuscript page counts are kept in dated reviews,
so they cannot be mistaken for a fresh full verification.

To audit and replay the recovered fixed-map research:

```sh
python computations/maintenance/verify_fixed_map_supplement.py
python computations/verification/bgs_20260921_regression.py --output build/bgs-20260921-regression.json
python computations/verification/bgs_heisenberg_path_audit.py --output build/bgs-heisenberg-path-audit.json
python computations/verification/hyperbolic_19adic_audit.py --output build/hyperbolic-19adic-audit.json
python computations/verification/fixed_map_unistochastic_ramp_audit.py
python computations/verification/fixed_map_classical_sum_rule_audit.py
python computations/verification/quantum_history_reconnection_audit.py
python computations/verification/unitary_encounter_envelope_audit.py
```

This writes fresh reports to `build/fixed-map-replay/` and preserves the
retained evidence. The mixed-loop hypotheses for the fixed coupling are
still unproved; successful finite checks do not establish universality.

The scientific scope is determined by explicit hypotheses and proofs, not by
repository synchronization or a successful software build.
