# Bohigas–Giannoni–Schmit programme

[Русская версия](README.ru.md) · [Mathematical background](docs/reader_guide.en.md)

**Deterministic microscopic BGS remains open.** This repository contains mathematical proofs, counterexamples, conditional bridges, numerical experiments and finite formal certificates. Their scopes are kept distinct.

## Current work

The scoped corpus revision has reconciled the supplied reviews, repaired proof exposition and source metadata, separated current status from historical records, and rerun reproducibility checks. All 159 root proof/exposition notes have scoped semantic readings; named conditional inputs remain explicit. New solution work resumes only after the corrected revision passes remote acceptance checks. See the [revision report and coverage](record/corpus_revision_20261006.md).

The central fixed-model obligation is the **signed** Heisenberg-scale joint-trace comparison, for every fixed correlation order and every smooth compact Fourier weight. An absolute all-order deterministic comparison is not the target. The [research brief](RESEARCH.md) states the model, current subsidiary conclusions and exact remaining gap.

## Read the mathematics

- [Theorem-family index](mathematics/results.md): scope-first entry points
- [Canonical proof topics](mathematics/topics/README.md): dependency-ordered reading paths
- [Claim ledger](record/claim_ledger.md): current scientific status and evidence vocabulary
- [Open obligations](mathematics/open_questions.md): unresolved statements, not historical TODOs
- [Source-of-truth policy](SOURCE_OF_TRUTH.md): which source controls a disagreement

The maintained frozen map has fixed coupling tau=10^(-80). Shrinking-coupling arithmetic returns, phase averages and noisy ensembles are different settings. The original two-copy noise channel has a reviewed gap estimate in [FM-020](mathematics/original_channel_gap.md); this does not prove deterministic noise removal or BGS.

## Reproduce and review

Start with [REPRODUCE_unified.md](REPRODUCE_unified.md), which distinguishes a Git checkout from a hash-manifest archive. [REVIEWING.md](REVIEWING.md) specifies theorem-level review. The authoritative manuscript entry is [BGS_unified.tex](manuscript/BGS_unified.tex).

Python/C++ checks certify their implemented finite assertions. Lean checks only the formalized propositions and their trust boundary. Source metadata checks do not certify theorem applicability. Neither a green build nor a complete file inventory certifies the entire analytic corpus.

## Repository map

| Area | Role |
|---|---|
| [mathematics](mathematics/README.md) | Maintained mathematical statements and proofs |
| [literature](literature/README.md) | Exact source identities and dependency mappings |
| [computations](computations/README.md) | Reproducible verification and experiments |
| [formalization](formalization/README.md) | Finite/algebraic Lean kernels and scope |
| [record](record/README.md) | Current status, reviews and historical accountability |
| [papers](papers/README.md) | Bounded publication candidates, not acceptance claims |

## History and attribution

The pre-revision entry page and cumulative status narratives are preserved in [the dated archive](record/history/2026/corpus_revision_20261006/manifest.json). Established literature is credited beside each imported theorem; external priority of project derivations is not implied by a project proof or internal review.

## Earlier section entry points

## 1. Overview

[Read the maintained entry.](RESEARCH.md)

## 2. Background: classical chaos, quantization, and BGS

[Read the maintained entry.](docs/reader_guide.en.md#2-background-classical-chaos-quantization-and-bgs)

## 3. Mathematical formulation of microscopic universality

[Read the maintained entry.](docs/reader_guide.en.md#3-mathematical-formulation-of-microscopic-universality)

## 4. Why Heisenberg time is unavoidable

[Read the maintained entry.](docs/reader_guide.en.md#4-why-heisenberg-time-is-unavoidable)

## 5. The maintained frozen quantum map

[Read the maintained entry.](docs/reader_guide.en.md#5-the-maintained-frozen-quantum-map)

## 6. Notation and scales

[Read the maintained entry.](docs/reader_guide.en.md#6-notation-and-scales)

## 7. The exact trace-to-local-statistics bridge

[Read the maintained entry.](docs/reader_guide.en.md#7-the-exact-trace-to-local-statistics-bridge)

## 8. Research architecture

[Read the maintained entry.](RESEARCH.md)

## 9. Established theorem families

[Read the maintained entry.](mathematics/results.md)

## 10. Negative results and ruled-out shortcuts

[Read the maintained entry.](RESEARCH.md)

## 11. The central open frontier

[Read the maintained entry.](RESEARCH.md)

## 12. What a successful closure would imply

[Read the maintained entry.](RESEARCH.md)

## 13. Evidence, proof, formalization, and trust boundaries

[Read the maintained entry.](REPRODUCE_unified.md)

## 14. Selected project figures

[Read the maintained entry.](docs/reader_guide.en.md#14-selected-project-figures)

## 15. Historical development of the programme

[Read the maintained entry.](record/history/2026/corpus_revision_20261006/manifest.json)

## 16. Glossary

[Read the maintained entry.](docs/reader_guide.en.md#16-glossary)

## 17. Frequently asked questions

[Read the maintained entry.](docs/reader_guide.en.md#17-frequently-asked-questions)

## 18. Literature and relation to the broader BGS landscape

[Read the maintained entry.](docs/reader_guide.en.md#18-literature-and-relation-to-the-broader-bgs-landscape)

## 19. Repository and reproducibility

[Read the maintained entry.](REPRODUCE_unified.md)

<!-- Stable fragment targets retained from the pre-revision reader entry. -->
<a id="arithmetic-quantum-chaos-trace-statistics-and-microscopic-spectral-universality"></a>
<a id="current-status-at-a-glance"></a>
<a id="classical-chaos"></a>
<a id="quantization"></a>
<a id="historical-origin"></a>
<a id="mean-spacing-scale"></a>
<a id="pair-statistics"></a>
<a id="symmetry-class"></a>
<a id="point-process-language"></a>
<a id="hierarchy-of-scales"></a>
<a id="why-such-a-tiny-fixed-parameter-matters"></a>
<a id="why-a-cat-map"></a>
<a id="common-phrases"></a>
<a id="core-trace-and-resolvent-claims"></a>
<a id="91-frozen-map-structure"></a>
<a id="92-resonance-and-cohomology"></a>
<a id="93-arithmetic-and-cayley-energy"></a>
<a id="94-pell-and-return-laws"></a>
<a id="95-clustered-abel-statistics"></a>
<a id="96-exact-resolvent-and-control-identities"></a>
<a id="two-maintained-languages-for-the-same-frontier"></a>
<a id="why-this-is-the-right-bottleneck"></a>
<a id="status-vocabulary"></a>
<a id="is-bgs-solved-in-this-repository"></a>
<a id="what-is-the-single-most-important-missing-theorem"></a>
<a id="why-is-tau10-80-not-effectively-zero"></a>
<a id="why-not-settle-the-problem-numerically"></a>
<a id="why-is-a-cat-map-a-useful-model-if-it-is-arithmetic"></a>
<a id="why-are-there-so-many-side-programmes"></a>
<a id="does-proving-classical-mixing-prove-bgs"></a>
<a id="does-matching-mathbb-emathrmtrv_nm2-for-a-few-m-prove-bgs"></a>
<a id="what-would-count-as-a-genuine-breakthrough-here"></a>
