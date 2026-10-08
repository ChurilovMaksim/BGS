# Literature and external theorem dependencies

This directory records exact external inputs, related prior results and
limits of source/priority checks. A matching title or abstract is a lead;
it is not the theorem needed by a proof.

Start with the [bibliography](bibliography.md) for the mathematical landscape
and [external_dependencies.json](external_dependencies.json) for registered
load-bearing theorem locators and hypothesis mappings.

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
