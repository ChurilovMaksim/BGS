# Literature and external theorem dependencies

## Current metadata coverage

The [explicit audit pointer](metadata_audit.json) selects a **57-record**
snapshot. The [22 October arithmetic review](arithmetic_dependency_closure_20261022.md)
adds five checked source-to-proof mappings for CAYLEY-006/007 to the previous
52 observations, including the [Bowen–Ruelle check](bowen_ruelle_trace_closure_20261021.md).
Earlier observations retain their dates and scope. Metadata agreement does
not certify every application or establish priority. Earlier dated screens
below retain their original coverage.

This directory records exact external inputs, related prior results and
limits of source/priority checks. A matching title or abstract is a lead;
it is not the theorem needed by a proof.

Start with the [bibliography](bibliography.md) for the mathematical landscape
and [external_dependencies.json](external_dependencies.json) for registered
load-bearing theorem locators and hypothesis mappings.

## Bibliographic metadata screen (8 October 2026)

An independent identifier–title audit reviewed all **39** rows of the
[external-dependency registry](external_dependencies.json). Of those,
**33** contain a DOI or arXiv identifier in a form accepted by the
bibliographic resolver. The batch check matched **32** of these
identifier–title pairs directly. The remaining combined
[`EXT-MANE-1981`](external_dependencies.json) row names **both** a 1981
paper and its mandatory 1983 erratum: a one-record comparison flagged
the combined record, but separate checks of
[the original](https://doi.org/10.1017/S0143385700001188) and
[the erratum](https://doi.org/10.1017/S0143385700001863)
each matched the corresponding title and year. This is a
**compound-record formatting issue**, not evidence of a retracted or
fabricated source. The six non-DOI/arXiv registry rows
(`EXT-EV-2015`, `EXT-PESIN-1977`, `EXT-RUELLE-1978`,
`EXT-PP-1990`, `EXT-BG-2008` and `EXT-BHATIA-2002`)
retain their separately recorded source locators; they were **not**
resolved by this automated identifier screen.

The TeX manuscript's newly added
[original BGS publication](https://doi.org/10.1103/PhysRevLett.52.1),
[Bourgade–Huang loop-equation paper](https://arxiv.org/abs/2607.07617),
and [published Lounici–Meziani–Peyré tomography paper](https://doi.org/10.1214/17-AOS1586)
were also matched to their cited identifiers. The original BGS abstract
explicitly concerns **GOE** statistics in Sinai's billiard.
These checks validate bibliographic **identity**, *not* theorem 1.9's
hypothesis mapping in every application, complete mathematical novelty,
author priority, proof correctness or absence of every possible erratum.
All load-bearing theorem locators and project hypotheses still require
the specific proof-level audits prescribed below.

## Source checks by role

| Question | Maintained source note |
|---|---|
| What has the attached article actually established here? | [Phase-channel/jet source and submission disposition](phase_channel_jet_sources_20261008.md) |
| What is the precise BGS scope? | [BGS scope and polynomial flow](bgs_scope_and_polynomial_flow_20261004.md), [all-order sources](all_order_sources_20261005.md) |
| Which classical/noisy mixing results apply to the frozen map? | [Operator transfer](frozen_operator_transfer_sources_20261006.md), [collective diffusion](collective_diffusion_sources_20261006.md), [original channel](original_channel_gap_sources_20261006.md) |
| Which Haar and heat-calculus inputs are used? | [Signed Heisenberg](signed_heisenberg_sources.md), [pair heat](heisenberg_pair_heat_sources_20261005.md), [growing-degree projection](growing_degree_sources_20261005.md) |
| What is imported into the local noisy comparison? | [Actual-start Dyson](actual_start_dyson_sources_20261004.md), [critical noise](critical_noise_sources_20261005.md), [noise removal](noise_removal_sources_20261005.md) |
| Which phase-source reductions retain additional qualifications? | [Wave2 phase/source audit](wave2_phase_orbit_source_qualification_20261007.md), [color-one boundary](color_one_boundary_qualification_20261007.md) |
| Where are the other theorem families sourced? | [Return/local-limit](return_local_limits_sources.md), [Pell/Floquet](pell_floquet_sources.md), [temporal resonance](temporal_resonance_sources.md), [finite orbit](finite_orbit_20260922.md) |

The phase-channel and sharp matrix-jet proofs are self-contained at their
stated scopes. Their external priority is unresolved. The submission review
also preserves the difference between an unpromoted candidate and a proved
counterexample; “verification-pending” does not mean false.

## Load-bearing citation rule

A publication-grade dependency records authors, title, persistent identifier,
pinned version/edition, exact theorem or lemma locator, date checked,
project-specific hypothesis mapping and affected claims. Abstract-level
similarity and search snippets are insufficient. If a needed theorem has
not been inspected, its use retains that explicit boundary.

The [scientific registry audit](../computations/verification/scientific_registry_audit.py)
checks dependency-ID resolution and required external-input declarations.
It does not perform a mathematical literature review. Current normalized
load-bearing dependencies live in the machine registry; specialized notes
retain their actual search/review coverage and earlier corrections.


## Quantum-graph claims and the color-one source qualification

The [2014 publisher abstract](https://doi.org/10.1103/PhysRevLett.112.144102)
and [2015 arXiv abstract](https://arxiv.org/abs/1407.1148) explicitly claim
all-correlation random-matrix limits for their specified graph classes.
Those are **published author claims**, not this repository's own proof
certificates. The [color-one boundary audit](color_one_boundary_qualification_20261007.md)
identifies an unresolved bulk/surface completion for a particular ordinary
coordinate prescription. It does not refute the graph results, and this
project does not independently certify the full graph proof. The
[bibliographic summary](bibliography.md#spectral-spacing-evidence-and-rigorous-model-class-bgs-results)
has been reconciled to this distinction. The original
[BGS 1984 paper](https://doi.org/10.1103/PhysRevLett.52.1) is historically
motivating numerical evidence, not a theorem for the present family.

## Checked 11 October research

The [integration disposition](../record/chat_integration_20261011.md) indexes maximal microscopic paths, source transport, finite-field collision calculus and frozen circular phase laws. The global deterministic BGS and TRACE-005 claims remain open. Original receipts and fresh executions have separate scope.

[Primary circular-phase and stopping sources](circular_phase_sources_20261011.md) pin seven additional references. The 11 October cache remains historical; metadata_audit.json selects the current reviewed cache.
