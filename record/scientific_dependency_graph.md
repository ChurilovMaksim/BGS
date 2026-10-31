# Scientific dependency graph

Generated from [claims.json](claims.json) by `computations/maintenance/render_research_views.py`.
The [registry](claims.json) controls registered status; the [ledger](claim_ledger.md) explains changes. The JSON view has the same complete adjacency.

**408 registered nodes; 832 direct prerequisite edges.**

An edge records a scoped programme prerequisite; it does not discharge a hypothesis.
“None registered” does not mean unconditional or self-contained.
External locators and mappings are in the [external registry](../literature/external_dependencies.json).

BGS-BGS-001 and BGS-TRACE-005 remain OPEN. Auxiliary ensembles and
abstract-family obstructions retain their original models and proof boundaries.

| Claim and source | State | Direct registered prerequisites | Registered external inputs | Direct consumers |
|---|---|---|---|---:|
| [BGS-BGS-001](../mathematics/fixed-map/fixed_map_resolvent_frontier.md) | open | `BGS-FM-001`, `BGS-FM-002`, `BGS-FM-003`, `BGS-FM-004`, `BGS-LOOP-001`, `BGS-TRACE-004`, `BGS-TRACE-005` | `EXT-BH-2026` | 0 |
| [BGS-CAYLEY-001](../mathematics/cayley-arithmetic/fourth_moment_reduction.md) | proved | None registered | None registered | 1 |
| [BGS-CAYLEY-002](../mathematics/cayley-arithmetic/cayley_additive_energy.md) | proved | `BGS-CAYLEY-001` | None registered | 3 |
| [BGS-CAYLEY-003](../mathematics/cayley-arithmetic/cayley_direct_energy.md) | verification-pending | `BGS-CAYLEY-002` | `EXT-VM-2015` | 1 |
| [BGS-CAYLEY-004](../mathematics/cayley-arithmetic/cayley_curve_uniform.md) | proved | `BGS-CAYLEY-002` | `EXT-CZ-2013` | 1 |
| [BGS-CAYLEY-005](../mathematics/open_questions.md) | open | `BGS-CAYLEY-002`, `BGS-CAYLEY-003`, `BGS-CAYLEY-004` | None registered | 0 |
| [BGS-CAYLEY-006](../mathematics/cayley-arithmetic/cayley_trace_gaussian_limit.md) | proved | None registered | `EXT-BORDA-2020`, `EXT-FI-1980`, `EXT-WANG-1982`, `EXT-ZAGIER-1997` | 0 |
| [BGS-CAYLEY-007](../mathematics/cayley-arithmetic/cayley_product_row_real_trace_ideal.md) | proved | None registered | `EXT-BT-1971` | 0 |
| [BGS-CAYLEY-008](../mathematics/cayley-arithmetic/cayley_scaling_rigidity.md) | proved | None registered | None registered | 0 |
| [BGS-CAYLEY-009](../mathematics/spectral-obstructions/magnetic_quotient_semicircle.md) | proved | None registered | None registered | 0 |
| [BGS-CAYLEY-010](../manuscript/general_spectra.tex) | proved | None registered | None registered | 0 |
| [BGS-CAYLEY-011](../mathematics/cayley-arithmetic/fibonacci_ratio_energy_proof.md) | proved | None registered | None registered | 0 |
| [BGS-CUE-001](../mathematics/spectral-obstructions/cue_singular_energy.md) | proved | None registered | `EXT-BAB-2013` | 0 |
| [BGS-CUE-002](../mathematics/trace-bridge/full_pair_cue_covariance.md) | proved | `BGS-TRACE-002` | None registered | 0 |
| [BGS-FLOW-001](../mathematics/fixed-map/coboundary_spectral_flow_bound.md) | proved | None registered | None registered | 0 |
| [BGS-FLOW-002](../mathematics/fixed-map/coboundary_spectral_flow_bound.md) | proved | None registered | None registered | 0 |
| [BGS-FLOW-003](../mathematics/fixed-map/quadratic_coboundary_noise.md) | proved | None registered | None registered | 8 |
| [BGS-FLOW-004](../mathematics/fixed-map/quadratic_noise_coupling.md) | proved | `BGS-FLOW-003` | None registered | 5 |
| [BGS-FLOW-005](../mathematics/fixed-map/quadratic_noise_reversibility.md) | proved | `BGS-FLOW-003`, `BGS-FLOW-004` | None registered | 2 |
| [BGS-FLOW-006](../mathematics/fixed-map/quadratic_noise_trace_fluctuations.md) | proved | `BGS-FLOW-003`, `BGS-FLOW-005` | None registered | 0 |
| [BGS-FLOW-007](../mathematics/fixed-map/quadratic_noise_clock_limit.md) | proved | `BGS-FLOW-004`, `BGS-FLOW-005` | `EXT-FORRESTER-1996` | 5 |
| [BGS-FLOW-008](../mathematics/fixed-map/coboundary_fourth_order_drift.md) | proved | `BGS-FLOW-003` | None registered | 2 |
| [BGS-FLOW-009](../mathematics/fixed-map/coboundary_mobius_diffusion.md) | proved | `BGS-FLOW-003`, `BGS-FLOW-004`, `BGS-FLOW-007`, `BGS-FLOW-008` | None registered | 5 |
| [BGS-FLOW-010](../mathematics/fixed-map/coboundary_joint_limit.md) | proved | `BGS-FLOW-003`, `BGS-FLOW-004`, `BGS-FLOW-007`, `BGS-FLOW-008`, `BGS-FLOW-009` | None registered | 3 |
| [BGS-FLOW-011](../mathematics/fixed-map/coboundary_polynomial_limit.md) | proved | `BGS-FLOW-003`, `BGS-FLOW-007`, `BGS-FLOW-009`, `BGS-FLOW-010` | None registered | 2 |
| [BGS-FLOW-012](../mathematics/fixed-map/coboundary_general_start.md) | proved | `BGS-FLOW-009`, `BGS-FLOW-010`, `BGS-FLOW-011`, `BGS-FM-013` | None registered | 4 |
| [BGS-FLOW-013](../mathematics/fixed-map/dyson_relaxation_obstruction.md) | proved | `BGS-FLOW-012` | `EXT-POPESCU-2023` | 1 |
| [BGS-FLOW-014](../mathematics/fixed-map/circular_dyson_actual_start.md) | proved | `BGS-FLOW-012`, `BGS-FM-017` | `EXT-KLZF-2022` | 3 |
| [BGS-FLOW-015](../mathematics/fixed-map/microscopic_noise_removal.md) | proved | `BGS-FLOW-007`, `BGS-FLOW-014`, `BGS-FM-013`, `BGS-TRACE-001` | `EXT-EHL-2018`, `EXT-LEMOINE-2025` | 3 |
| [BGS-FLOW-016](../mathematics/fixed-map/local_moment_transport.md) | proved | `BGS-FLOW-004`, `BGS-FLOW-009`, `BGS-FLOW-014` | `EXT-KLZF-2022` | 2 |
| [BGS-FLOW-017](../mathematics/fixed-map/coboundary_all_order_limit.md) | proved | `BGS-FLOW-010`, `BGS-FLOW-011`, `BGS-FLOW-012`, `BGS-FLOW-014`, `BGS-FLOW-016`, `BGS-FM-013`, `BGS-TRACE-001` | `EXT-SOSH-2000` | 2 |
| [BGS-FLOW-018](../mathematics/fixed-map/clock_structure_and_noise_scale.md) | proved | `BGS-FLOW-007`, `BGS-FLOW-015`, `BGS-FLOW-016`, `BGS-FLOW-017`, `BGS-TRACE-007` | `EXT-FORRESTER-1996`, `EXT-KT-2009` | 0 |
| [BGS-FLOW-019](../mathematics/fixed-map/fixed_degree_heat_projection.md) | proved | `BGS-FLOW-015`, `BGS-FLOW-017`, `BGS-FM-013` | `EXT-DE-2001` | 1 |
| [BGS-FLOW-020](../mathematics/fixed-map/growing_degree_trace_projection.md) | proved | `BGS-FLOW-015`, `BGS-FLOW-019`, `BGS-FM-007`, `BGS-FM-013` | `EXT-DE-2001`, `EXT-GHANMI-2017` | 1 |
| [BGS-FLOW-021](../mathematics/fixed-map/heisenberg_pair_heat_formula.md) | proved | `BGS-FLOW-020` | `EXT-DE-2001` | 0 |
| [BGS-FLOW-022](../mathematics/pell/pell_floquet_normal_form.md) | proved | None registered | None registered | 0 |
| [BGS-FLOW-023](../mathematics/pell/pell_coboundary_resonance.md) | proved | None registered | None registered | 0 |
| [BGS-FLOW-024](../mathematics/pell/pell_coboundary_resonance.md) | proved | None registered | None registered | 0 |
| [BGS-FLOW-025](../mathematics/pell/pell_floquet_normal_form.md) | proved | None registered | None registered | 0 |
| [BGS-FM-001](../mathematics/fixed-map/fixed_model_symmetry_theorem.md) | proved | None registered | None registered | 24 |
| [BGS-FM-002](../mathematics/fixed-map/fixed_model_pell_crossover.md) | proved | None registered | None registered | 1 |
| [BGS-FM-003](../mathematics/fixed-map/fixed_map_moment_control_and_transfer.md) | proved | None registered | None registered | 2 |
| [BGS-FM-004](../mathematics/fixed-map/three_orientation_resolvent_barrier.md) | conditional | `BGS-FM-003` | None registered | 1 |
| [BGS-FM-005](../mathematics/fixed-map/frozen_kick_rank_boundary.md) | proved | None registered | `EXT-EV-2015` | 2 |
| [BGS-FM-006](../mathematics/fixed-map/nonlinear_bracket_pressure.md) | proved | `BGS-FM-001` | `EXT-PESIN-1977`, `EXT-PP-1990`, `EXT-RUELLE-1978` | 1 |
| [BGS-FM-007](../mathematics/fixed-map/frozen_seven_cut_reduction.md) | proved | `BGS-FM-001`, `BGS-FM-005`, `BGS-TRACE-001` | None registered | 4 |
| [BGS-FM-008](../mathematics/fixed-map/frozen_algebraic_spectral_simplicity.md) | proved | `BGS-FM-005` | `EXT-POPESCU-2023` | 4 |
| [BGS-FM-009](../mathematics/fixed-map/frozen_common_antireversor_certificate.md) | proved | `BGS-FM-001` | `EXT-POPESCU-2023` | 0 |
| [BGS-FM-010](../mathematics/fixed-map/frozen_arithmetic_trace_rigidity.md) | proved | `BGS-FM-001`, `BGS-FM-008` | `EXT-POPESCU-2023` | 1 |
| [BGS-FM-011](../mathematics/fixed-map/frozen_effective_gap_floor.md) | proved | `BGS-FM-008` | `EXT-ROY-2016` | 0 |
| [BGS-FM-012](../mathematics/fixed-map/frozen_periodic_point_annihilator.md) | proved | `BGS-FM-001` | None registered | 1 |
| [BGS-FM-013](../mathematics/fixed-map/fixed_time_wavepacket_trace_bound.md) | proved | `BGS-FM-001` | None registered | 6 |
| [BGS-FM-014](../mathematics/fixed-map/frozen_phase_finite_type.md) | proved | `BGS-FM-001` | None registered | 2 |
| [BGS-FM-015](../mathematics/fixed-map/frozen_commutator_action.md) | proved | `BGS-FM-001`, `BGS-FM-014` | None registered | 0 |
| [BGS-FM-016](../mathematics/fixed-map/egorov_overlap_rigidity.md) | proved | `BGS-FLOW-003`, `BGS-FM-001` | None registered | 1 |
| [BGS-FM-017](../mathematics/fixed-map/frozen_mesoscopic_regularity.md) | proved | `BGS-FLOW-009`, `BGS-FLOW-012`, `BGS-FLOW-013`, `BGS-FM-007`, `BGS-FM-013` | None registered | 1 |
| [BGS-FM-018](../mathematics/fixed-map/frozen_operator_transfer_coercivity.md) | proved | `BGS-FM-001`, `BGS-FM-006` | `EXT-PP-1990` | 5 |
| [BGS-FM-019](../mathematics/fixed-map/collective_diffusion_gap.md) | proved | `BGS-FM-018` | None registered | 1 |
| [BGS-FM-020](../mathematics/fixed-map/original_channel_gap.md) | proved | `BGS-FM-019` | None registered | 0 |
| [BGS-FM-021](../mathematics/fixed-map/position_chain_mixing.md) | proved | `BGS-FM-001` | None registered | 17 |
| [BGS-FM-022](../mathematics/fixed-map/reversed_path_decay.md) | proved | `BGS-FM-001` | None registered | 4 |
| [BGS-FM-023](../mathematics/spectral-obstructions/arithmetic_translation_exclusion.md) | proved | `BGS-FM-001`, `BGS-FM-016`, `BGS-FM-018` | None registered | 1 |
| [BGS-FM-024](../mathematics/fixed-map/actual_seven_primary_commutant.md) | proved | `BGS-FM-001`, `BGS-FM-008` | `EXT-POPESCU-2023` | 0 |
| [BGS-FM-025](../mathematics/fixed-map/uniform_five_cluster_simplicity.md) | proved | `BGS-FM-001`, `BGS-FM-008` | `EXT-POPESCU-2023` | 0 |
| [BGS-FM-026](../mathematics/fixed-map/literal_time_multiplicity_bounds.md) | proved | `BGS-FM-001` | `EXT-POPESCU-2023` | 0 |
| [BGS-FM-027](../mathematics/trace-bridge/phase_trace_checkpoint.md) | proved | `BGS-FM-021` | None registered | 4 |
| [BGS-FM-028](../mathematics/trace-bridge/phase_trace_checkpoint.md) | proved | `BGS-FM-018` | None registered | 4 |
| [BGS-FM-029](../mathematics/trace-bridge/phase_trace_checkpoint.md) | proved | `BGS-FM-018` | `EXT-ROY-2016` | 1 |
| [BGS-FM-030](../mathematics/trace-bridge/phase_trace_checkpoint.md) | proved | `BGS-FM-021` | `EXT-BHATIA-2002` | 0 |
| [BGS-FM-031](../mathematics/fixed-map/ordinary_compact_stratum_centering.md) | proved | `BGS-TRACE-023` | `EXT-ZIRN-2021` | 0 |
| [BGS-FM-032](../mathematics/fixed-map/quantum_cyclic_cohomology.md) | proved | `BGS-FM-001`, `BGS-TRACE-009` | None registered | 0 |
| [BGS-FM-033](../mathematics/fixed-map/scaled_weyl_overlap.md) | conditional | `BGS-FM-014`, `BGS-FM-023` | None registered | 0 |
| [BGS-FM-034](../mathematics/locality/fixed_strength_locality.md) | proved | None registered | None registered | 0 |
| [BGS-FM-035](../mathematics/locality/fixed_strength_locality.md) | proved | None registered | None registered | 0 |
| [BGS-FM-036](../mathematics/locality/fixed_strength_locality.md) | proved | None registered | None registered | 0 |
| [BGS-FM-037](../mathematics/foundations/earlier_foundations.md) | proved | None registered | None registered | 0 |
| [BGS-FORMAL-001](../formalization/README.md) | proved | None registered | None registered | 0 |
| [BGS-FORMAL-002](../mathematics/fixed-map/four_cut_rank_two_classification.md) | proved | None registered | None registered | 1 |
| [BGS-FORMAL-003](../formalization/seven_primary_certificate.md) | proved | None registered | None registered | 0 |
| [BGS-FUP-001](../mathematics/fixed-map/offdiagonal_digit_fup.md) | proved | None registered | `EXT-COHEN-2025` | 0 |
| [BGS-INFO-001](../mathematics/open_questions.md) | open | None registered | None registered | 0 |
| [BGS-LOOP-001](../mathematics/fixed-map/fixed_map_resolvent_frontier.md) | conditional | `BGS-FM-007`, `BGS-TRACE-002` | `EXT-BH-2026` | 1 |
| [BGS-RES-001](../mathematics/resonance-cohomology/fourier_line_resonance_coercivity.md) | proved | None registered | None registered | 1 |
| [BGS-RES-002](../mathematics/resonance-cohomology/local_jet_resonance_obstruction.md) | proved | None registered | None registered | 1 |
| [BGS-RES-003](../mathematics/open_questions.md) | open | `BGS-RES-001`, `BGS-RES-002` | None registered | 0 |
| [BGS-RES-004](../mathematics/resonance-cohomology/finite_orbit_resonance_rigidity.md) | proved | None registered | None registered | 0 |
| [BGS-RES-005](../mathematics/resonance-cohomology/frozen_full_lag_resonance.md) | proved | None registered | None registered | 0 |
| [BGS-RES-006](../mathematics/fixed-map/fixed_map_resolvent_frontier.md) | proved | None registered | None registered | 2 |
| [BGS-RES-007](../mathematics/fixed-map/fixed_map_resolvent_frontier.md) | proved | `BGS-FM-007`, `BGS-RES-006` | None registered | 0 |
| [BGS-RES-008](../mathematics/pell/pell_sharp_orbit_coercivity.md) | proved | None registered | None registered | 0 |
| [BGS-RES-009](../manuscript/unified_sections/spectral_modules.tex) | proved | None registered | None registered | 0 |
| [BGS-RES-010](../manuscript/unified_sections/spectral_modules.tex) | proved | None registered | None registered | 0 |
| [BGS-RES-011](../manuscript/unified_sections/spectral_modules.tex) | proved | None registered | None registered | 0 |
| [BGS-RES-012](../manuscript/unified_sections/spectral_modules.tex) | proved | None registered | None registered | 0 |
| [BGS-RES-013](../manuscript/unified_sections/spectral_modules.tex) | proved | None registered | None registered | 0 |
| [BGS-RES-014](../mathematics/resonance-cohomology/resonance_riesz_regularization.md) | conditional | None registered | None registered | 1 |
| [BGS-RES-015](../mathematics/resonance-cohomology/two_window_resonance_crossover.md) | proved | `BGS-RES-014` | None registered | 0 |
| [BGS-RES-016](../mathematics/information-theory/multiradius_polynomial_rigidity.md) | proved | None registered | None registered | 0 |
| [BGS-RES-017](../mathematics/fixed-map/balanced_phase_controllability.md) | proved | None registered | None registered | 0 |
| [BGS-RES-018](../mathematics/resonance-cohomology/entire_temporal_gauge.md) | proved | None registered | None registered | 0 |
| [BGS-RES-019](../mathematics/resonance-cohomology/resonance_wiener_stability.md) | proved | None registered | None registered | 0 |
| [BGS-RES-020](../mathematics/resonance-cohomology/generic_wiener_resonance.md) | proved | None registered | None registered | 0 |
| [BGS-RES-021](../manuscript/unified_sections/analytic_resonance_rigidity.tex) | proved | None registered | None registered | 0 |
| [BGS-RES-022](../mathematics/resonance-cohomology/resonance_nondegeneracy_and_hessian.md) | verification-pending | None registered | None registered | 1 |
| [BGS-RES-023](../mathematics/resonance-cohomology/resonance_nondegeneracy_and_hessian.md) | proved | `BGS-RES-022` | None registered | 0 |
| [BGS-RET-001](../mathematics/pell/pell_harmonic_returns.md) | proved | `BGS-RET-002` | `EXT-DEMNI-2016` | 0 |
| [BGS-RET-002](../mathematics/pell/pell_harmonic_transition.md) | proved | None registered | None registered | 1 |
| [BGS-RET-003](../mathematics/returns/noncommuting_return_words.md) | conditional | None registered | None registered | 0 |
| [BGS-RET-004](../mathematics/returns/noncommuting_return_words.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-001](../mathematics/trace-bridge/trace_to_local_statistics_bridge.md) | proved | None registered | None registered | 11 |
| [BGS-TRACE-002](../mathematics/trace-bridge/trace_to_local_statistics_bridge.md) | proved | `BGS-TRACE-001` | None registered | 8 |
| [BGS-TRACE-003](../mathematics/trace-bridge/trace_to_local_statistics_bridge.md) | proved | `BGS-TRACE-002` | None registered | 4 |
| [BGS-TRACE-004](../mathematics/trace-bridge/bandlimited_correlation_extension.md) | proved | `BGS-TRACE-003` | None registered | 2 |
| [BGS-TRACE-005](../mathematics/open_questions.md) | open | `BGS-FM-001`, `BGS-TRACE-003` | None registered | 1 |
| [BGS-TRACE-006](../mathematics/trace-bridge/clustered_abel_window_boundary.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-007](../mathematics/fixed-map/fixed_map_resolvent_frontier.md) | proved | None registered | `EXT-CK-2006` | 2 |
| [BGS-TRACE-008](../mathematics/trace-bridge/two_clock_gram_falsifier.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-009](../mathematics/fixed-map/prime_resonant_sector.md) | proved | `BGS-FM-001`, `BGS-FM-010`, `BGS-TRACE-003` | `EXT-RAINS-2003` | 4 |
| [BGS-TRACE-010](../mathematics/trace-bridge/signed_heisenberg_comparison.md) | proved | `BGS-TRACE-001`, `BGS-TRACE-002`, `BGS-TRACE-003` | `EXT-DE-2001` | 1 |
| [BGS-TRACE-011](../mathematics/trace-bridge/resonant_cubic_density_control.md) | proved | `BGS-TRACE-001`, `BGS-TRACE-009`, `BGS-TRACE-010` | `EXT-DE-2001` | 1 |
| [BGS-TRACE-012](../mathematics/fixed-map/folded_quadratic_resonance_control.md) | proved | `BGS-FM-001`, `BGS-TRACE-001`, `BGS-TRACE-009`, `BGS-TRACE-011` | None registered | 0 |
| [BGS-TRACE-013](../mathematics/spectral-obstructions/arithmetic_word_expansion_obstruction.md) | proved | None registered | `EXT-BG-2008`, `EXT-DIRICHLET-1837`, `EXT-GAE-2007`, `EXT-POPESCU-2023` | 0 |
| [BGS-TRACE-014](../mathematics/spectral-obstructions/isospectral_clock_moment_control.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-015](../mathematics/fixed-map/three_block_unmarking.md) | proved | `BGS-FM-021` | None registered | 0 |
| [BGS-TRACE-016](../mathematics/fixed-map/four_block_unmarking.md) | proved | `BGS-FM-021`, `BGS-FORMAL-002` | None registered | 0 |
| [BGS-TRACE-017](../mathematics/fixed-map/factorial_wkb_reduction.md) | proved | `BGS-FM-001`, `BGS-TRACE-001`, `BGS-TRACE-002` | None registered | 1 |
| [BGS-TRACE-018](../mathematics/fixed-map/winding_defect_locality.md) | proved | `BGS-FM-001`, `BGS-FM-012` | None registered | 1 |
| [BGS-TRACE-019](../mathematics/fixed-map/selected_weighted_coefficient.md) | proved | `BGS-FM-001`, `BGS-TRACE-017`, `BGS-TRACE-018` | `EXT-MANE-1981`, `EXT-PP-1990`, `EXT-RUELLE-1978` | 0 |
| [BGS-TRACE-020](../mathematics/fixed-map/factorial_ordered_diagonal.md) | proved | `BGS-FM-021`, `BGS-TRACE-002` | None registered | 1 |
| [BGS-TRACE-021](../mathematics/trace-bridge/phase_trace_checkpoint.md) | proved | `BGS-FM-021`, `BGS-FM-027`, `BGS-TRACE-001`, `BGS-TRACE-020` | None registered | 1 |
| [BGS-TRACE-022](../mathematics/trace-bridge/phase_trace_checkpoint.md) | proved | `BGS-FM-021` | None registered | 0 |
| [BGS-TRACE-023](../mathematics/trace-bridge/phase_trace_checkpoint.md) | proved | None registered | `EXT-ZIRN-2021` | 6 |
| [BGS-TRACE-024](../mathematics/fixed-map/actual_one_pinch_disappearance.md) | proved | `BGS-FM-021`, `BGS-FM-027`, `BGS-FM-028`, `BGS-TRACE-023` | None registered | 1 |
| [BGS-TRACE-025](../mathematics/fixed-map/rounding_simple_spectrum_endpoint_barriers.md) | proved | `BGS-FM-027`, `BGS-FM-028`, `BGS-FM-029`, `BGS-TRACE-021`, `BGS-TRACE-023` | None registered | 0 |
| [BGS-TRACE-026](../mathematics/fixed-map/hook_tree_phase_current_reduction.md) | proved | `BGS-FM-021`, `BGS-FM-022`, `BGS-TRACE-023` | None registered | 0 |
| [BGS-TRACE-027](../mathematics/fixed-map/weighted_phase_coherence_covariance.md) | proved | `BGS-FM-021`, `BGS-FM-022` | None registered | 0 |
| [BGS-TRACE-028](../mathematics/fixed-map/right_frame_unmasked_pinch_hierarchy.md) | proved | `BGS-FM-021`, `BGS-FM-028`, `BGS-TRACE-023`, `BGS-TRACE-024` | None registered | 1 |
| [BGS-TRACE-029](../mathematics/fixed-map/convex_pinch_weak_noise_and_deconvolution.md) | proved | `BGS-FM-021`, `BGS-FM-027`, `BGS-FM-028`, `BGS-TRACE-023`, `BGS-TRACE-028` | None registered | 0 |
| [BGS-TRACE-053](../mathematics/trace-bridge/max_entry_phase_channel.md) | proved | None registered | None registered | 4 |
| [BGS-TRACE-054](../mathematics/trace-bridge/sharp_inner_jet.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-055](../archive/record/research_checkpoint_20261008.md) | verification-pending | `BGS-TRACE-053` | None registered | 0 |
| [BGS-TRACE-056](../mathematics/trace-bridge/phase_channel_real_flow.md) | proved | `BGS-TRACE-053` | None registered | 2 |
| [BGS-TRACE-057](../mathematics/trace-bridge/source_covariance.md) | proved | None registered | None registered | 1 |
| [BGS-TRACE-058](../mathematics/trace-bridge/integrable_phase_absorption.md) | proved | None registered | None registered | 1 |
| [BGS-TRACE-059](../mathematics/trace-bridge/physical_source_transport.md) | proved | `BGS-TRACE-053`, `BGS-TRACE-056`, `BGS-TRACE-057` | None registered | 0 |
| [BGS-TRACE-060](../mathematics/trace-bridge/delay_bootstrap.md) | conditional | None registered | `EXT-TROPP-2011` | 2 |
| [BGS-TRACE-061](../mathematics/trace-bridge/fresh_phase_average.md) | proved | None registered | None registered | 1 |
| [BGS-TRACE-062](../mathematics/trace-bridge/flat_completion.md) | proved | `BGS-TRACE-061` | None registered | 0 |
| [BGS-TRACE-063](../mathematics/trace-bridge/nonlinear_coercivity.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-064](../mathematics/trace-bridge/torus_contraction.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-065](../mathematics/trace-bridge/coherence_form_factor.md) | proved | None registered | None registered | 1 |
| [BGS-TRACE-066](../mathematics/trace-bridge/previous_rank_results.md) | proved | `BGS-TRACE-065` | `EXT-AGG-1989` | 0 |
| [BGS-TRACE-067](../mathematics/trace-bridge/jack_coefficient_theorem.md) | proved | None registered | None registered | 1 |
| [BGS-TRACE-068](../mathematics/trace-bridge/phase_contraction.md) | proved | `BGS-TRACE-067` | `EXT-JM-2015`, `EXT-MATSUMOTO-2007`, `EXT-OO-1997`, `EXT-VV-2017` | 2 |
| [BGS-TRACE-069](../mathematics/trace-bridge/exact_cumulants.md) | proved | `BGS-TRACE-068` | `EXT-MATSUMOTO-2007` | 1 |
| [BGS-TRACE-070](../mathematics/trace-bridge/form_factor_curve.md) | proved | `BGS-TRACE-068`, `BGS-TRACE-069` | `EXT-HSW-1999` | 0 |
| [BGS-TRACE-071](../mathematics/trace-bridge/laplace_path_transport.md) | proved | `BGS-TRACE-053`, `BGS-TRACE-056`, `BGS-TRACE-058` | None registered | 1 |
| [BGS-TRACE-072](../mathematics/trace-bridge/deterministic_path_transport.md) | proved | `BGS-FM-018`, `BGS-TRACE-071` | None registered | 0 |
| [BGS-TRACE-073](../mathematics/trace-bridge/schur_censoring_gap.md) | conditional | `BGS-FM-021`, `BGS-FM-022` | None registered | 3 |
| [BGS-TRACE-074](../mathematics/trace-bridge/unitary_two_step_obstruction.md) | proved | None registered | None registered | 2 |
| [BGS-TRACE-075](../mathematics/trace-bridge/two_step_restoring_drift.md) | proved | `BGS-TRACE-074` | None registered | 1 |
| [BGS-TRACE-076](../mathematics/trace-bridge/haar_feedback_clock_law.md) | proved | `BGS-TRACE-060` | None registered | 0 |
| [BGS-TRACE-077](../mathematics/trace-bridge/green_compression_gap.md) | proved | `BGS-FM-021`, `BGS-TRACE-073`, `BGS-TRACE-074` | None registered | 3 |
| [BGS-TRACE-078](../mathematics/trace-bridge/two_step_increment_variance.md) | proved | None registered | None registered | 1 |
| [BGS-TRACE-079](../mathematics/trace-bridge/two_step_stopped_concentration.md) | proved | `BGS-FM-021`, `BGS-TRACE-075`, `BGS-TRACE-077`, `BGS-TRACE-078` | None registered | 1 |
| [BGS-TRACE-080](../mathematics/trace-bridge/unconditional_feedback_flatness.md) | proved | `BGS-FM-021`, `BGS-FM-022`, `BGS-TRACE-060`, `BGS-TRACE-073`, `BGS-TRACE-077`, `BGS-TRACE-079` | None registered | 1 |
| [BGS-TRACE-081](../mathematics/spectral-obstructions/flat_spectrum_obstruction.md) | proved | None registered | None registered | 2 |
| [BGS-TRACE-082](../mathematics/spectral-obstructions/coherence_memory_plateau.md) | proved | `BGS-TRACE-081` | None registered | 1 |
| [BGS-TRACE-083](../mathematics/spectral-obstructions/coherent_first_return_pulse.md) | proved | `BGS-TRACE-081`, `BGS-TRACE-082` | None registered | 0 |
| [BGS-TRACE-084](../mathematics/trace-bridge/resonant_mesoscopic_criterion.md) | proved | `BGS-TRACE-009` | None registered | 0 |
| [BGS-TRACE-085](../mathematics/trace-bridge/root_lifting_sector_boundary.md) | proved | `BGS-TRACE-001`, `BGS-TRACE-002` | `EXT-DE-2001` | 0 |
| [BGS-TRACE-086](../mathematics/trace-bridge/all_order_process_closure.md) | proved | `BGS-TRACE-001`, `BGS-TRACE-002`, `BGS-TRACE-004` | None registered | 1 |
| [BGS-TRACE-087](../mathematics/trace-bridge/parameter_deaveraging.md) | proved | `BGS-TRACE-086` | `EXT-DE-2001` | 0 |
| [BGS-TRACE-088](../mathematics/trace-bridge/equal_edge_occupation.md) | proved | `BGS-FM-021` | None registered | 1 |
| [BGS-TRACE-089](../mathematics/trace-bridge/collision_crossover.md) | proved | `BGS-TRACE-088` | `EXT-PITTEL-2016` | 0 |
| [BGS-TRACE-090](../mathematics/trace-bridge/bounded_radial_ratios.md) | proved | None registered | None registered | 1 |
| [BGS-TRACE-091](../mathematics/trace-bridge/hardy_spectral_remainder.md) | proved | `BGS-TRACE-007`, `BGS-TRACE-090` | None registered | 0 |
| [BGS-TRACE-092](../mathematics/trace-bridge/abel_clock_rigidity.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-093](../mathematics/trace-bridge/gaussian_equal_edge.md) | proved | None registered | `EXT-BF-2023`, `EXT-KPSS-2002` | 1 |
| [BGS-TRACE-094](../mathematics/trace-bridge/wick_collision_poisson.md) | proved | `BGS-TRACE-093` | `EXT-CS-2006` | 0 |
| [BGS-TRACE-095](../mathematics/trace-bridge/phase_ensemble_continuation.md) | conditional | `BGS-TRACE-073`, `BGS-TRACE-077`, `BGS-TRACE-080` | None registered | 0 |
| [BGS-TRACE-096](../mathematics/trace-bridge/phase_ensemble_continuation.md) | verification-pending | None registered | None registered | 0 |
| [BGS-TRACE-097](../mathematics/trace-bridge/phase_ensemble_continuation.md) | conditional | None registered | None registered | 0 |
| [BGS-TRACE-098](../mathematics/trace-bridge/phase_ensemble_continuation.md) | verification-pending | None registered | None registered | 1 |
| [BGS-TRACE-099](../mathematics/trace-bridge/phase_ensemble_continuation.md) | verification-pending | `BGS-TRACE-098` | None registered | 0 |
| [BGS-TRACE-100](../mathematics/trace-bridge/phase_ensemble_continuation.md) | verification-pending | None registered | None registered | 1 |
| [BGS-TRACE-101](../mathematics/trace-bridge/phase_neutral_primitives.md) | verification-pending | `BGS-TRACE-100` | None registered | 2 |
| [BGS-TRACE-102](../mathematics/trace-bridge/phase_second_defect.md) | verification-pending | `BGS-TRACE-101` | None registered | 1 |
| [BGS-TRACE-103](../mathematics/trace-bridge/phase_quartic_cluster_sum.md) | verification-pending | `BGS-TRACE-101`, `BGS-TRACE-102` | `EXT-STANLEY-1981` | 0 |
| [BGS-TRACE-104](../mathematics/trace-bridge/phase_cayley_cauchy_transfer.md) | verification-pending | None registered | None registered | 0 |
| [BGS-TRACE-105](../mathematics/trace-bridge/cauchy_positive_source_boundary.md) | verification-pending | None registered | None registered | 0 |
| [BGS-TRACE-106](../mathematics/fixed-map/physical_kick_trace_decay.md) | proved | None registered | None registered | 1 |
| [BGS-TRACE-107](../mathematics/fixed-map/physical_trace_polynomial_approximation.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-108](../mathematics/fixed-map/coordinate_return_quartic.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-109](../mathematics/fixed-map/inserted_trace_coboundary.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-110](../mathematics/fixed-map/spectral_orbit_distance.md) | proved | `BGS-TRACE-112`, `BGS-TRACE-113` | None registered | 0 |
| [BGS-TRACE-111](../mathematics/fixed-map/pell_weighted_curvature.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-112](../mathematics/fixed-map/displacement_density_trace_bound.md) | proved | `BGS-TRACE-106` | None registered | 1 |
| [BGS-TRACE-113](../mathematics/fixed-map/fixed_kick_uniform_trace_bound.md) | proved | None registered | `EXT-BR-1975` | 2 |
| [BGS-TRACE-114](../mathematics/fixed-map/balanced_rounding_research_20261027.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-115](../mathematics/trace-bridge/microscopic_unitary_stability_20261027.md) | proved | `BGS-RES-006` | None registered | 1 |
| [BGS-TRACE-116](../mathematics/trace-bridge/microscopic_unitary_stability_20261027.md) | proved | `BGS-TRACE-113`, `BGS-TRACE-115` | None registered | 0 |
| [BGS-TRACE-117](../mathematics/fixed-map/kick_blind_arithmetic_spike.md) | proved | None registered | None registered | 4 |
| [BGS-TRACE-118](../mathematics/fixed-map/orbit_orthogonal_kick_spike.md) | proved | `BGS-TRACE-117` | None registered | 2 |
| [BGS-TRACE-119](../mathematics/fixed-map/positive_time_spike.md) | proved | `BGS-TRACE-118` | None registered | 0 |
| [BGS-TRACE-120](../mathematics/fixed-map/order_ladder_abel.md) | proved | `BGS-TRACE-117` | None registered | 4 |
| [BGS-TRACE-121](../mathematics/fixed-map/order_trichotomy_abel.md) | proved | `BGS-TRACE-120` | None registered | 3 |
| [BGS-TRACE-122](../mathematics/fixed-map/crt_composite_abel.md) | proved | `BGS-TRACE-120`, `BGS-TRACE-121` | None registered | 2 |
| [BGS-TRACE-123](../mathematics/fixed-map/squarefree_product_abel.md) | proved | `BGS-TRACE-120`, `BGS-TRACE-121`, `BGS-TRACE-122` | None registered | 1 |
| [BGS-TRACE-124](../mathematics/fixed-map/odd_modulus_abel.md) | proved | `BGS-TRACE-120`, `BGS-TRACE-121`, `BGS-TRACE-122`, `BGS-TRACE-123` | None registered | 0 |
| [BGS-TRACE-125](../mathematics/fixed-map/uniform_orbit_overlap.md) | proved | `BGS-TRACE-117`, `BGS-TRACE-118` | None registered | 0 |
| [BGS-TRACE-126](../mathematics/fixed-map/interaction_phase_form_factor.md) | proved | `BGS-TRACE-117` | None registered | 7 |
| [BGS-TRACE-127](../mathematics/fixed-map/diagonal_phase_form_factor.md) | proved | `BGS-TRACE-126` | None registered | 4 |
| [BGS-TRACE-128](../mathematics/fixed-map/diagonal_phase_short_time.md) | proved | `BGS-TRACE-127` | None registered | 3 |
| [BGS-TRACE-129](../mathematics/fixed-map/scalar_return_bessel.md) | proved | `BGS-TRACE-126` | None registered | 4 |
| [BGS-TRACE-130](../mathematics/fixed-map/sixteen_phase_symmetry.md) | proved | `BGS-TRACE-126`, `BGS-TRACE-129` | None registered | 3 |
| [BGS-TRACE-131](../mathematics/fixed-map/hyperbolic_diagonal_form_factor.md) | proved | `BGS-TRACE-126`, `BGS-TRACE-127`, `BGS-TRACE-130` | None registered | 7 |
| [BGS-TRACE-132](../mathematics/fixed-map/hyperbolic_short_time_limit.md) | proved | `BGS-TRACE-127`, `BGS-TRACE-128`, `BGS-TRACE-130`, `BGS-TRACE-131` | None registered | 0 |
| [BGS-TRACE-133](../mathematics/fixed-map/revival_closure_law.md) | proved | `BGS-TRACE-126`, `BGS-TRACE-129`, `BGS-TRACE-131` | None registered | 5 |
| [BGS-TRACE-134](../mathematics/fixed-map/revival_closure_law.md) | proved | `BGS-TRACE-126`, `BGS-TRACE-129`, `BGS-TRACE-133` | None registered | 1 |
| [BGS-TRACE-135](../mathematics/fixed-map/revival_closure_law.md) | proved | `BGS-TRACE-126`, `BGS-TRACE-133` | None registered | 1 |
| [BGS-TRACE-136](../mathematics/fixed-map/revival_closure_law.md) | open | `BGS-TRACE-129`, `BGS-TRACE-135` | None registered | 0 |
| [BGS-TRACE-137](../mathematics/fixed-map/revival_closure_law.md) | open | `BGS-TRACE-133`, `BGS-TRACE-134` | None registered | 0 |
| [BGS-TRACE-140](../mathematics/fixed-map/momentum_phase_cue.md) | proved | `BGS-TRACE-128`, `BGS-TRACE-131` | None registered | 2 |
| [BGS-TRACE-141](../mathematics/fixed-map/momentum_phase_cue.md) | proved | `BGS-TRACE-140` | None registered | 0 |
| [BGS-TRACE-142](../mathematics/fixed-map/momentum_phase_cue.md) | verification-pending | `BGS-TRACE-130`, `BGS-TRACE-140` | None registered | 0 |
| [BGS-TRACE-143](../mathematics/fixed-map/random_phase_encounter_pairs.md) | proved | `BGS-TRACE-127`, `BGS-TRACE-131` | None registered | 1 |
| [BGS-TRACE-144](../mathematics/fixed-map/random_phase_encounter_pairs.md) | proved | `BGS-TRACE-143` | None registered | 3 |
| [BGS-TRACE-145](../mathematics/fixed-map/random_phase_encounter_pairs.md) | proved | `BGS-TRACE-144` | None registered | 1 |
| [BGS-TRACE-146](../mathematics/fixed-map/random_phase_encounter_pairs.md) | proved | `BGS-TRACE-128`, `BGS-TRACE-144`, `BGS-TRACE-145` | None registered | 2 |
| [BGS-TRACE-147](../mathematics/fixed-map/random_phase_encounter_pairs.md) | verification-pending | `BGS-TRACE-144`, `BGS-TRACE-146` | None registered | 1 |
| [BGS-TRACE-148](../mathematics/fixed-map/random_phase_encounter_pairs.md) | open | `BGS-TRACE-147` | None registered | 1 |
| [BGS-TRACE-149](../mathematics/fixed-map/band_limited_kick_bridge.md) | proved | `BGS-TRACE-131`, `BGS-TRACE-133` | None registered | 2 |
| [BGS-TRACE-150](../mathematics/fixed-map/band_limited_kick_bridge.md) | proved | `BGS-TRACE-149` | None registered | 1 |
| [BGS-TRACE-151](../mathematics/fixed-map/band_limited_kick_bridge.md) | proved | `BGS-TRACE-133`, `BGS-TRACE-149` | None registered | 4 |
| [BGS-TRACE-152](../mathematics/fixed-map/band_limited_kick_bridge.md) | proved | `BGS-TRACE-151` | None registered | 1 |
| [BGS-TRACE-153](../mathematics/fixed-map/band_limited_kick_bridge.md) | verification-pending | `BGS-TRACE-152`, `BGS-TRACE-156` | None registered | 1 |
| [BGS-TRACE-154](../mathematics/fixed-map/band_limited_kick_bridge.md) | proved | `BGS-TRACE-151` | None registered | 1 |
| [BGS-TRACE-155](../mathematics/fixed-map/band_limited_kick_bridge.md) | open | `BGS-TRACE-154` | None registered | 0 |
| [BGS-TRACE-156](../mathematics/fixed-map/band_limited_kick_bridge.md) | proved | `BGS-TRACE-151` | None registered | 1 |
| [BGS-TRACE-157](../mathematics/fixed-map/band_limited_kick_bridge.md) | proved | `BGS-TRACE-150`, `BGS-TRACE-151` | None registered | 2 |
| [BGS-TRACE-158](../mathematics/fixed-map/band_limited_kick_bridge.md) | conditional | `BGS-TRACE-153`, `BGS-TRACE-157` | None registered | 0 |
| [BGS-TRACE-159](../mathematics/fixed-map/band_limited_kick_bridge.md) | open | `BGS-TRACE-157` | None registered | 0 |
| [BGS-TRACE-160](../mathematics/fixed-map/band_limited_kick_bridge.md) | proved | `BGS-TRACE-146` | None registered | 2 |
| [BGS-TRACE-161](../mathematics/fixed-map/band_limited_kick_bridge.md) | open | `BGS-TRACE-160` | None registered | 0 |
| [BGS-TRACE-162](../mathematics/fixed-map/band_limited_kick_bridge.md) | open | `BGS-TRACE-148`, `BGS-TRACE-160` | None registered | 0 |
| [BGS-TRACE-163](../mathematics/fixed-map/derandomized_fixed_kick.md) | proved | `BGS-TRACE-131` | None registered | 9 |
| [BGS-TRACE-164](../mathematics/fixed-map/derandomized_fixed_kick.md) | conditional | `BGS-TRACE-131`, `BGS-TRACE-163` | None registered | 1 |
| [BGS-TRACE-165](../mathematics/fixed-map/derandomized_fixed_kick.md) | proved | `BGS-TRACE-163` | None registered | 12 |
| [BGS-TRACE-166](../mathematics/fixed-map/derandomized_fixed_kick.md) | proved | None registered | None registered | 2 |
| [BGS-TRACE-167](../mathematics/fixed-map/derandomized_fixed_kick.md) | proved | `BGS-TRACE-166` | None registered | 0 |
| [BGS-TRACE-168](../mathematics/fixed-map/derandomized_fixed_kick.md) | proved | `BGS-TRACE-165`, `BGS-TRACE-166` | None registered | 2 |
| [BGS-TRACE-169](../mathematics/fixed-map/derandomized_fixed_kick.md) | proved | `BGS-TRACE-165` | None registered | 2 |
| [BGS-TRACE-170](../mathematics/fixed-map/derandomized_fixed_kick.md) | proved | `BGS-TRACE-165`, `BGS-TRACE-169` | None registered | 14 |
| [BGS-TRACE-171](../mathematics/fixed-map/derandomized_fixed_kick.md) | proved | `BGS-TRACE-170` | None registered | 2 |
| [BGS-TRACE-172](../mathematics/fixed-map/derandomized_fixed_kick.md) | proved | `BGS-TRACE-170` | None registered | 1 |
| [BGS-TRACE-173](../mathematics/fixed-map/derandomized_fixed_kick.md) | proved | `BGS-TRACE-171`, `BGS-TRACE-172` | None registered | 0 |
| [BGS-TRACE-174](../mathematics/fixed-map/derandomized_fixed_kick.md) | conditional | `BGS-TRACE-170`, `BGS-TRACE-171` | None registered | 0 |
| [BGS-TRACE-175](../mathematics/fixed-map/derandomized_fixed_kick.md) | proved | `BGS-TRACE-163` | None registered | 0 |
| [BGS-TRACE-176](../mathematics/fixed-map/derandomized_fixed_kick.md) | conditional | `BGS-TRACE-165`, `BGS-TRACE-168` | None registered | 1 |
| [BGS-TRACE-177](../mathematics/fixed-map/derandomized_fixed_kick.md) | open | `BGS-TRACE-170` | None registered | 3 |
| [BGS-TRACE-178](../mathematics/fixed-map/derandomized_fixed_kick.md) | proved | `BGS-TRACE-169` | None registered | 1 |
| [BGS-TRACE-179](../mathematics/fixed-map/derandomized_fixed_kick.md) | refuted | `BGS-TRACE-170`, `BGS-TRACE-177` | None registered | 3 |
| [BGS-TRACE-180](../mathematics/fixed-map/derandomized_fixed_kick.md) | open | `BGS-TRACE-176`, `BGS-TRACE-179` | None registered | 0 |
| [BGS-TRACE-181](../mathematics/fixed-map/derandomized_fixed_kick.md) | open | `BGS-TRACE-164`, `BGS-TRACE-168` | None registered | 0 |
| [BGS-TRACE-182](../mathematics/fixed-map/derandomized_fixed_kick.md) | open | `BGS-TRACE-177`, `BGS-TRACE-178` | None registered | 1 |
| [BGS-TRACE-183](../mathematics/fixed-map/resonant_residue_lineE.md) | proved | `BGS-TRACE-163` | None registered | 8 |
| [BGS-TRACE-184](../mathematics/fixed-map/resonant_residue_lineE.md) | proved | `BGS-TRACE-183` | None registered | 8 |
| [BGS-TRACE-185](../mathematics/fixed-map/resonant_residue_lineE.md) | proved | `BGS-TRACE-184` | None registered | 3 |
| [BGS-TRACE-186](../mathematics/fixed-map/resonant_residue_lineE.md) | proved | `BGS-TRACE-184`, `BGS-TRACE-185` | None registered | 1 |
| [BGS-TRACE-187](../mathematics/fixed-map/resonant_residue_lineE.md) | proved | `BGS-TRACE-163`, `BGS-TRACE-165`, `BGS-TRACE-170`, `BGS-TRACE-186` | None registered | 1 |
| [BGS-TRACE-188](../mathematics/fixed-map/resonant_residue_lineE.md) | conditional | `BGS-TRACE-165`, `BGS-TRACE-170`, `BGS-TRACE-184`, `BGS-TRACE-185` | None registered | 0 |
| [BGS-TRACE-189](../mathematics/fixed-map/resonant_residue_lineE.md) | open | `BGS-TRACE-183`, `BGS-TRACE-184` | None registered | 0 |
| [BGS-TRACE-190](../mathematics/fixed-map/resonant_residue_lineE.md) | open | `BGS-TRACE-163`, `BGS-TRACE-183` | None registered | 1 |
| [BGS-TRACE-191](../mathematics/fixed-map/resonant_residue_lineE.md) | open | `BGS-TRACE-185` | None registered | 0 |
| [BGS-TRACE-192](../mathematics/fixed-map/resonant_residue_lineE.md) | open | `BGS-TRACE-182`, `BGS-TRACE-190` | None registered | 0 |
| [BGS-TRACE-193](../mathematics/fixed-map/resonant_residue_lineE.md) | proved | `BGS-TRACE-163`, `BGS-TRACE-165`, `BGS-TRACE-170`, `BGS-TRACE-187` | None registered | 1 |
| [BGS-TRACE-194](../mathematics/fixed-map/resonant_residue_lineE.md) | proved | `BGS-TRACE-163`, `BGS-TRACE-183`, `BGS-TRACE-184` | None registered | 3 |
| [BGS-TRACE-195](../mathematics/fixed-map/resonant_residue_lineE.md) | proved | `BGS-TRACE-163`, `BGS-TRACE-165`, `BGS-TRACE-170` | None registered | 0 |
| [BGS-TRACE-196](../mathematics/fixed-map/resonant_residue_lineE.md) | conditional | `BGS-TRACE-165`, `BGS-TRACE-170`, `BGS-TRACE-179`, `BGS-TRACE-194` | None registered | 0 |
| [BGS-TRACE-197](../mathematics/fixed-map/lifted_transfer_lineF.md) | proved | `BGS-TRACE-183`, `BGS-TRACE-184` | None registered | 17 |
| [BGS-TRACE-198](../mathematics/fixed-map/lifted_transfer_lineF.md) | proved | `BGS-TRACE-197` | None registered | 17 |
| [BGS-TRACE-199](../mathematics/fixed-map/lifted_transfer_lineF.md) | proved | `BGS-TRACE-165`, `BGS-TRACE-170`, `BGS-TRACE-197`, `BGS-TRACE-198` | None registered | 8 |
| [BGS-TRACE-200](../mathematics/fixed-map/lifted_transfer_lineF.md) | proved | `BGS-TRACE-193`, `BGS-TRACE-199` | None registered | 0 |
| [BGS-TRACE-201](../mathematics/fixed-map/lifted_transfer_lineF.md) | proved | `BGS-TRACE-165`, `BGS-TRACE-170`, `BGS-TRACE-197`, `BGS-TRACE-198` | None registered | 0 |
| [BGS-TRACE-202](../mathematics/fixed-map/lifted_transfer_lineF.md) | open | `BGS-TRACE-197` | None registered | 0 |
| [BGS-TRACE-203](../mathematics/fixed-map/resonance_classification_lineG.md) | proved | `BGS-TRACE-183`, `BGS-TRACE-184`, `BGS-TRACE-194` | None registered | 9 |
| [BGS-TRACE-204](../mathematics/fixed-map/resonance_classification_lineG.md) | proved | `BGS-TRACE-203`, `BGS-TRACE-212` | None registered | 1 |
| [BGS-TRACE-205](../mathematics/fixed-map/resonance_classification_lineG.md) | open | `BGS-TRACE-203`, `BGS-TRACE-204` | None registered | 1 |
| [BGS-TRACE-206](../mathematics/fixed-map/resonance_classification_lineG.md) | open | `BGS-TRACE-179`, `BGS-TRACE-205` | None registered | 19 |
| [BGS-TRACE-207](../mathematics/fixed-map/lineH_49state_certificate.md) | proved | `BGS-TRACE-194`, `BGS-TRACE-197` | None registered | 3 |
| [BGS-TRACE-208](../mathematics/fixed-map/lineH_49state_certificate.md) | proved | `BGS-TRACE-197`, `BGS-TRACE-207` | None registered | 1 |
| [BGS-TRACE-209](../mathematics/fixed-map/lineH_49state_certificate.md) | proved | `BGS-TRACE-165`, `BGS-TRACE-170`, `BGS-TRACE-207`, `BGS-TRACE-208` | None registered | 0 |
| [BGS-TRACE-210](../mathematics/fixed-map/derandomized_fixed_kick.md) | open | `BGS-TRACE-170`, `BGS-TRACE-177` | None registered | 1 |
| [BGS-TRACE-211](../mathematics/fixed-map/lineI_rprime_reduction.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-212](../mathematics/fixed-map/lineI_rprime_reduction.md) | proved | `BGS-TRACE-183` | None registered | 14 |
| [BGS-TRACE-213](../mathematics/fixed-map/lineI_rprime_reduction.md) | proved | `BGS-TRACE-206` | None registered | 12 |
| [BGS-TRACE-214](../mathematics/fixed-map/lineI_rprime_reduction.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-215](../mathematics/fixed-map/lineI_rprime_reduction.md) | proved | `BGS-TRACE-197`, `BGS-TRACE-203`, `BGS-TRACE-212`, `BGS-TRACE-216` | `EXT-RS-1962` | 1 |
| [BGS-TRACE-216](../mathematics/fixed-map/lineI_rprime_reduction.md) | proved | `BGS-TRACE-203` | None registered | 7 |
| [BGS-TRACE-217](../mathematics/fixed-map/lineI_rprime_reduction.md) | proved | `BGS-TRACE-183`, `BGS-TRACE-184`, `BGS-TRACE-198`, `BGS-TRACE-199`, `BGS-TRACE-215`, `BGS-TRACE-216` | None registered | 0 |
| [BGS-TRACE-218](../mathematics/fixed-map/lineI_rprime_reduction.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-219](../mathematics/fixed-map/lineI_rprime_reduction.md) | proved | None registered | `EXT-BHV-2001`, `EXT-CARMICHAEL-1913` | 0 |
| [BGS-TRACE-220](../mathematics/fixed-map/lineI_rprime_reduction.md) | open | `BGS-TRACE-206`, `BGS-TRACE-213` | None registered | 0 |
| [BGS-TRACE-221](../mathematics/fixed-map/lineJ_d7_twisted_coefficient.md) | proved | `BGS-TRACE-197`, `BGS-TRACE-198`, `BGS-TRACE-199`, `BGS-TRACE-203`, `BGS-TRACE-212`, `BGS-TRACE-216`, `BGS-TRACE-222` | None registered | 6 |
| [BGS-TRACE-222](../mathematics/fixed-map/lineJ_d7_twisted_coefficient.md) | proved | `BGS-TRACE-203`, `BGS-TRACE-216` | None registered | 5 |
| [BGS-TRACE-223](../mathematics/fixed-map/lineJ_d7_twisted_coefficient.md) | proved | `BGS-TRACE-197`, `BGS-TRACE-198`, `BGS-TRACE-203`, `BGS-TRACE-216`, `BGS-TRACE-222` | None registered | 4 |
| [BGS-TRACE-224](../mathematics/fixed-map/lineJ_d7_twisted_coefficient.md) | proved | None registered | None registered | 1 |
| [BGS-TRACE-225](../mathematics/fixed-map/lineJ_d7_twisted_coefficient.md) | proved | `BGS-TRACE-197`, `BGS-TRACE-198`, `BGS-TRACE-199`, `BGS-TRACE-206`, `BGS-TRACE-212`, `BGS-TRACE-213`, `BGS-TRACE-216`, `BGS-TRACE-221`, `BGS-TRACE-222`, `BGS-TRACE-223`, `BGS-TRACE-224` | None registered | 12 |
| [BGS-TRACE-226](../mathematics/fixed-map/lineJ_d7_twisted_coefficient.md) | proved | `BGS-TRACE-197`, `BGS-TRACE-203`, `BGS-TRACE-207` | None registered | 14 |
| [BGS-TRACE-227](../mathematics/fixed-map/lineJ_d7_twisted_coefficient.md) | proved | `BGS-TRACE-212`, `BGS-TRACE-225`, `BGS-TRACE-226`, `BGS-TRACE-228` | None registered | 12 |
| [BGS-TRACE-228](../mathematics/fixed-map/lineJ_d7_twisted_coefficient.md) | proved | `BGS-TRACE-206`, `BGS-TRACE-212` | None registered | 15 |
| [BGS-TRACE-229](../mathematics/fixed-map/lineJ_d7_twisted_coefficient.md) | proved | `BGS-TRACE-212` | None registered | 11 |
| [BGS-TRACE-230](../mathematics/fixed-map/lineJ_d7_twisted_coefficient.md) | proved | None registered | None registered | 14 |
| [BGS-TRACE-231](../mathematics/fixed-map/lineJ_d7_twisted_coefficient.md) | conditional | `BGS-TRACE-206`, `BGS-TRACE-212`, `BGS-TRACE-213`, `BGS-TRACE-225`, `BGS-TRACE-227`, `BGS-TRACE-228`, `BGS-TRACE-230`, `BGS-TRACE-232`, `BGS-TRACE-235` | `EXT-DAVENPORT-1980`, `EXT-VINOGRADOV-1937`, `EXT-WEYL-1916` | 2 |
| [BGS-TRACE-232](../mathematics/fixed-map/lineJ_d7_twisted_coefficient.md) | open | `BGS-TRACE-206`, `BGS-TRACE-213`, `BGS-TRACE-225`, `BGS-TRACE-228` | None registered | 2 |
| [BGS-TRACE-233](../mathematics/fixed-map/lineJ_d7_twisted_coefficient.md) | open | `BGS-TRACE-223` | None registered | 0 |
| [BGS-TRACE-234](../mathematics/fixed-map/lineK_harg_removal.md) | proved | None registered | None registered | 1 |
| [BGS-TRACE-235](../mathematics/fixed-map/lineK_harg_removal.md) | proved | `BGS-TRACE-223`, `BGS-TRACE-225`, `BGS-TRACE-234` | `EXT-DAVENPORT-1980`, `EXT-DIRICHLET-1837`, `EXT-VINOGRADOV-1937`, `EXT-WEYL-1916` | 9 |
| [BGS-TRACE-236](../mathematics/fixed-map/lineK_harg_removal.md) | proved | `BGS-TRACE-225`, `BGS-TRACE-227`, `BGS-TRACE-231`, `BGS-TRACE-235` | None registered | 1 |
| [BGS-TRACE-237](../mathematics/fixed-map/lineK_harg_removal.md) | proved | `BGS-TRACE-206`, `BGS-TRACE-212`, `BGS-TRACE-226`, `BGS-TRACE-229` | None registered | 7 |
| [BGS-TRACE-238](../mathematics/fixed-map/lineK_harg_removal.md) | proved | `BGS-TRACE-198`, `BGS-TRACE-199`, `BGS-TRACE-206`, `BGS-TRACE-213`, `BGS-TRACE-225`, `BGS-TRACE-226`, `BGS-TRACE-227`, `BGS-TRACE-228`, `BGS-TRACE-230` | None registered | 13 |
| [BGS-TRACE-239](../mathematics/fixed-map/lineK_harg_removal.md) | open | `BGS-TRACE-235`, `BGS-TRACE-238` | None registered | 1 |
| [BGS-TRACE-240](../mathematics/fixed-map/lineK_harg_removal.md) | conditional | `BGS-TRACE-231`, `BGS-TRACE-232`, `BGS-TRACE-235`, `BGS-TRACE-236`, `BGS-TRACE-237`, `BGS-TRACE-238`, `BGS-TRACE-239` | None registered | 0 |
| [BGS-TRACE-241](../mathematics/fixed-map/lineK_harg_removal.md) | proved | `BGS-TRACE-230` | `EXT-WEIL-1948` | 6 |
| [BGS-TRACE-242](../mathematics/fixed-map/lineK_harg_removal.md) | proved | `BGS-TRACE-221`, `BGS-TRACE-226` | None registered | 5 |
| [BGS-TRACE-243](../mathematics/fixed-map/lineK_harg_removal.md) | proved | `BGS-TRACE-221`, `BGS-TRACE-226`, `BGS-TRACE-241` | None registered | 8 |
| [BGS-TRACE-244](../mathematics/fixed-map/lineK_harg_removal.md) | proved | `BGS-TRACE-221`, `BGS-TRACE-226`, `BGS-TRACE-243`, `BGS-TRACE-249`, `BGS-TRACE-250`, `BGS-TRACE-251` | None registered | 4 |
| [BGS-TRACE-245](../mathematics/fixed-map/lineK_harg_removal.md) | proved | `BGS-TRACE-197`, `BGS-TRACE-212`, `BGS-TRACE-213`, `BGS-TRACE-225`, `BGS-TRACE-226`, `BGS-TRACE-227`, `BGS-TRACE-228`, `BGS-TRACE-229`, `BGS-TRACE-235`, `BGS-TRACE-238`, `BGS-TRACE-241`, `BGS-TRACE-242`, `BGS-TRACE-243`, `BGS-TRACE-244`, `BGS-TRACE-250`, `BGS-TRACE-251`, `BGS-TRACE-252` | None registered | 7 |
| [BGS-TRACE-246](../mathematics/fixed-map/lineK_harg_removal.md) | proved | `BGS-TRACE-197`, `BGS-TRACE-212`, `BGS-TRACE-213`, `BGS-TRACE-225`, `BGS-TRACE-226`, `BGS-TRACE-227`, `BGS-TRACE-228`, `BGS-TRACE-235`, `BGS-TRACE-237`, `BGS-TRACE-238`, `BGS-TRACE-241`, `BGS-TRACE-242`, `BGS-TRACE-244`, `BGS-TRACE-245`, `BGS-TRACE-252`, `BGS-TRACE-283` | None registered | 5 |
| [BGS-TRACE-247](../mathematics/fixed-map/lineK_harg_removal.md) | open | `BGS-TRACE-243`, `BGS-TRACE-244` | None registered | 0 |
| [BGS-TRACE-248](../mathematics/fixed-map/lineL_op_open_range.md) | proved | None registered | None registered | 6 |
| [BGS-TRACE-249](../mathematics/fixed-map/lineL_op_open_range.md) | proved | `BGS-TRACE-197`, `BGS-TRACE-221`, `BGS-TRACE-226` | None registered | 5 |
| [BGS-TRACE-250](../mathematics/fixed-map/lineL_op_open_range.md) | proved | `BGS-TRACE-243`, `BGS-TRACE-248`, `BGS-TRACE-249` | None registered | 10 |
| [BGS-TRACE-251](../mathematics/fixed-map/lineL_op_open_range.md) | proved | `BGS-TRACE-248`, `BGS-TRACE-250` | None registered | 6 |
| [BGS-TRACE-252](../mathematics/fixed-map/lineL_op_open_range.md) | proved | `BGS-TRACE-243`, `BGS-TRACE-250`, `BGS-TRACE-251` | None registered | 9 |
| [BGS-TRACE-253](../mathematics/fixed-map/lineL_op_open_range.md) | proved | `BGS-TRACE-226`, `BGS-TRACE-227`, `BGS-TRACE-238`, `BGS-TRACE-252` | None registered | 2 |
| [BGS-TRACE-254](../mathematics/fixed-map/lineL_op_open_range.md) | proved | `BGS-TRACE-206`, `BGS-TRACE-248` | None registered | 2 |
| [BGS-TRACE-255](../mathematics/fixed-map/lineL_op_open_range.md) | proved | `BGS-TRACE-237` | None registered | 8 |
| [BGS-TRACE-256](../mathematics/fixed-map/lineL_op_open_range.md) | open | `BGS-TRACE-237`, `BGS-TRACE-255` | None registered | 0 |
| [BGS-TRACE-257](../mathematics/fixed-map/lineL_op_open_range.md) | proved | `BGS-TRACE-197`, `BGS-TRACE-212`, `BGS-TRACE-213`, `BGS-TRACE-225`, `BGS-TRACE-226`, `BGS-TRACE-227`, `BGS-TRACE-228`, `BGS-TRACE-235`, `BGS-TRACE-237`, `BGS-TRACE-238`, `BGS-TRACE-241`, `BGS-TRACE-245`, `BGS-TRACE-255` | None registered | 0 |
| [BGS-TRACE-258](../mathematics/fixed-map/lineL_op_open_range.md) | proved | `BGS-TRACE-198`, `BGS-TRACE-246`, `BGS-TRACE-251`, `BGS-TRACE-252`, `BGS-TRACE-283` | None registered | 0 |
| [BGS-TRACE-259](../mathematics/fixed-map/lineL_op_open_range.md) | proved | `BGS-TRACE-254`, `BGS-TRACE-255` | None registered | 2 |
| [BGS-TRACE-260](../mathematics/fixed-map/lineL_op_open_range.md) | proved | `BGS-TRACE-250`, `BGS-TRACE-259` | None registered | 0 |
| [BGS-TRACE-261](../mathematics/fixed-map/lineL_op_open_range.md) | proved | `BGS-TRACE-230`, `BGS-TRACE-248`, `BGS-TRACE-259` | None registered | 1 |
| [BGS-TRACE-262](../mathematics/fixed-map/lineL_op_open_range.md) | proved | `BGS-TRACE-238`, `BGS-TRACE-252`, `BGS-TRACE-253`, `BGS-TRACE-261` | None registered | 0 |
| [BGS-TRACE-263](../mathematics/fixed-map/lineL_op_open_range.md) | proved | `BGS-TRACE-206`, `BGS-TRACE-212`, `BGS-TRACE-254` | None registered | 2 |
| [BGS-TRACE-264](../mathematics/fixed-map/lineL_op_open_range.md) | proved | `BGS-TRACE-238`, `BGS-TRACE-255`, `BGS-TRACE-263` | None registered | 1 |
| [BGS-TRACE-265](../mathematics/fixed-map/lineL_op_open_range.md) | proved | `BGS-TRACE-230`, `BGS-TRACE-263`, `BGS-TRACE-264` | None registered | 2 |
| [BGS-TRACE-266](../mathematics/fixed-map/lineL_op_open_range.md) | proved | `BGS-TRACE-203`, `BGS-TRACE-206`, `BGS-TRACE-216`, `BGS-TRACE-230`, `BGS-TRACE-277` | None registered | 2 |
| [BGS-TRACE-267](../mathematics/fixed-map/lineL_op_open_range.md) | proved | `BGS-TRACE-243`, `BGS-TRACE-255` | None registered | 0 |
| [BGS-TRACE-268](../mathematics/fixed-map/lineL_op_open_range.md) | proved | `BGS-TRACE-255` | None registered | 0 |
| [BGS-TRACE-269](../mathematics/fixed-map/lineMN_conductor_structure.md) | proved | `BGS-TRACE-230` | None registered | 1 |
| [BGS-TRACE-270](../mathematics/fixed-map/lineMN_conductor_structure.md) | proved | `BGS-TRACE-225`, `BGS-TRACE-227`, `BGS-TRACE-235` | None registered | 0 |
| [BGS-TRACE-271](../mathematics/fixed-map/lineMN_conductor_structure.md) | proved | `BGS-TRACE-198`, `BGS-TRACE-199`, `BGS-TRACE-225`, `BGS-TRACE-228`, `BGS-TRACE-230`, `BGS-TRACE-238`, `BGS-TRACE-246`, `BGS-TRACE-269`, `BGS-TRACE-273` | None registered | 2 |
| [BGS-TRACE-272](../mathematics/fixed-map/lineMN_conductor_structure.md) | proved | `BGS-TRACE-206` | None registered | 0 |
| [BGS-TRACE-273](../mathematics/fixed-map/lineMN_conductor_structure.md) | proved | `BGS-TRACE-198`, `BGS-TRACE-199`, `BGS-TRACE-206` | None registered | 4 |
| [BGS-TRACE-274](../mathematics/fixed-map/lineMN_conductor_structure.md) | open | `BGS-TRACE-206`, `BGS-TRACE-238` | None registered | 0 |
| [BGS-TRACE-275](../mathematics/fixed-map/lineMN_conductor_structure.md) | proved | `BGS-TRACE-206`, `BGS-TRACE-237`, `BGS-TRACE-238` | None registered | 1 |
| [BGS-TRACE-276](../mathematics/fixed-map/lineMN_conductor_structure.md) | open | `BGS-TRACE-206`, `BGS-TRACE-221`, `BGS-TRACE-222`, `BGS-TRACE-228`, `BGS-TRACE-229`, `BGS-TRACE-293` | None registered | 0 |
| [BGS-TRACE-277](../mathematics/fixed-map/lineMN_conductor_structure.md) | proved | `BGS-TRACE-230` | None registered | 6 |
| [BGS-TRACE-278](../mathematics/fixed-map/lineMN_conductor_structure.md) | proved | `BGS-TRACE-230`, `BGS-TRACE-241`, `BGS-TRACE-243`, `BGS-TRACE-245`, `BGS-TRACE-250`, `BGS-TRACE-252` | None registered | 4 |
| [BGS-TRACE-279](../mathematics/fixed-map/lineMN_conductor_structure.md) | proved | `BGS-TRACE-230`, `BGS-TRACE-278` | `EXT-CP-2011`, `EXT-OSV-2023`, `EXT-OSV-2024` | 1 |
| [BGS-TRACE-280](../mathematics/fixed-map/lineMN_conductor_structure.md) | proved | `BGS-TRACE-245`, `BGS-TRACE-252`, `BGS-TRACE-278`, `BGS-TRACE-279` | `EXT-CP-2011`, `EXT-OSV-2023`, `EXT-OSV-2024` | 1 |
| [BGS-TRACE-281](../mathematics/fixed-map/lineMN_conductor_structure.md) | proved | `BGS-TRACE-230`, `BGS-TRACE-245`, `BGS-TRACE-278` | `EXT-BOURGAIN-2005` | 1 |
| [BGS-TRACE-282](../mathematics/fixed-map/lineMN_conductor_structure.md) | open | `BGS-TRACE-278` | None registered | 1 |
| [BGS-TRACE-283](../mathematics/fixed-map/lineMN_conductor_structure.md) | proved | `BGS-TRACE-198`, `BGS-TRACE-230`, `BGS-TRACE-243`, `BGS-TRACE-250`, `BGS-TRACE-251`, `BGS-TRACE-252`, `BGS-TRACE-277` | None registered | 3 |
| [BGS-TRACE-284](../mathematics/fixed-map/lineMN_conductor_structure.md) | proved | `BGS-TRACE-246`, `BGS-TRACE-271`, `BGS-TRACE-283` | None registered | 0 |
| [BGS-TRACE-285](../mathematics/fixed-map/lineMN_conductor_structure.md) | proved | `BGS-TRACE-266`, `BGS-TRACE-277` | None registered | 2 |
| [BGS-TRACE-286](../mathematics/fixed-map/lineN2N4_inherited_level.md) | proved | `BGS-TRACE-197`, `BGS-TRACE-198`, `BGS-TRACE-212`, `BGS-TRACE-213`, `BGS-TRACE-225`, `BGS-TRACE-226`, `BGS-TRACE-227`, `BGS-TRACE-228`, `BGS-TRACE-229`, `BGS-TRACE-235`, `BGS-TRACE-237`, `BGS-TRACE-238`, `BGS-TRACE-241`, `BGS-TRACE-242`, `BGS-TRACE-245`, `BGS-TRACE-246`, `BGS-TRACE-253` | None registered | 0 |
| [BGS-TRACE-287](../mathematics/fixed-map/lineN2N4_inherited_level.md) | open | `BGS-TRACE-228`, `BGS-TRACE-229`, `BGS-TRACE-242`, `BGS-TRACE-245`, `BGS-TRACE-246` | None registered | 0 |
| [BGS-TRACE-288](../mathematics/fixed-map/lineN2N4_inherited_level.md) | proved | `BGS-TRACE-228`, `BGS-TRACE-229`, `BGS-TRACE-266`, `BGS-TRACE-277`, `BGS-TRACE-285` | None registered | 2 |
| [BGS-TRACE-289](../mathematics/fixed-map/lineN2N4_inherited_level.md) | proved | `BGS-TRACE-242`, `BGS-TRACE-248`, `BGS-TRACE-249`, `BGS-TRACE-250`, `BGS-TRACE-288` | None registered | 1 |
| [BGS-TRACE-290](../mathematics/fixed-map/lineN2N4_inherited_level.md) | proved | `BGS-TRACE-248`, `BGS-TRACE-249`, `BGS-TRACE-250` | None registered | 1 |
| [BGS-TRACE-291](../mathematics/fixed-map/lineN2N4_inherited_level.md) | proved | `BGS-TRACE-230`, `BGS-TRACE-277` | None registered | 2 |
| [BGS-TRACE-292](../mathematics/fixed-map/lineN2N4_inherited_level.md) | proved | `BGS-TRACE-229`, `BGS-TRACE-255`, `BGS-TRACE-291` | None registered | 1 |
| [BGS-TRACE-293](../mathematics/fixed-map/lineN2N4_inherited_level.md) | proved | `BGS-TRACE-228`, `BGS-TRACE-229` | None registered | 1 |
| [BGS-TRACE-294](../mathematics/fixed-map/lineN2N4_inherited_level.md) | proved | `BGS-TRACE-198`, `BGS-TRACE-249`, `BGS-TRACE-250` | None registered | 1 |
| [BGS-TRACE-295](../mathematics/fixed-map/lineN2N4_inherited_level.md) | proved | `BGS-TRACE-198`, `BGS-TRACE-222`, `BGS-TRACE-226` | None registered | 1 |
| [BGS-TRACE-296](../mathematics/fixed-map/lineN2N4_inherited_level.md) | proved | `BGS-TRACE-228`, `BGS-TRACE-229`, `BGS-TRACE-288`, `BGS-TRACE-289`, `BGS-TRACE-290`, `BGS-TRACE-294`, `BGS-TRACE-295` | None registered | 3 |
| [BGS-TRACE-297](../mathematics/fixed-map/lineN2N4_inherited_level.md) | proved | `BGS-TRACE-197` | None registered | 1 |
| [BGS-TRACE-298](../mathematics/fixed-map/lineN2N4_inherited_level.md) | open | `BGS-TRACE-255`, `BGS-TRACE-291`, `BGS-TRACE-292`, `BGS-TRACE-297` | None registered | 0 |
| [BGS-TRACE-299](../mathematics/fixed-map/lineN5N18_gas_conditional.md) | conditional | `BGS-TRACE-206`, `BGS-TRACE-210`, `BGS-TRACE-213`, `BGS-TRACE-227`, `BGS-TRACE-271`, `BGS-TRACE-273`, `BGS-TRACE-296`, `BGS-TRACE-300`, `BGS-TRACE-301`, `BGS-TRACE-302`, `BGS-TRACE-303`, `BGS-TRACE-304`, `BGS-TRACE-305`, `BGS-TRACE-306`, `BGS-TRACE-307`, `BGS-TRACE-308`, `BGS-TRACE-309`, `BGS-TRACE-310`, `BGS-TRACE-311`, `BGS-TRACE-312`, `BGS-TRACE-313`, `BGS-TRACE-314`, `BGS-TRACE-315`, `BGS-TRACE-317`, `BGS-TRACE-318`, `BGS-TRACE-319`, `BGS-TRACE-320`, `BGS-TRACE-321`, `BGS-TRACE-322`, `BGS-TRACE-323`, `BGS-TRACE-324` | None registered | 0 |
| [BGS-TRACE-300](../mathematics/fixed-map/lineN5N18_gas_conditional.md) | open | `BGS-TRACE-309`, `BGS-TRACE-312` | None registered | 3 |
| [BGS-TRACE-301](../mathematics/fixed-map/lineN5N18_gas_conditional.md) | open | `BGS-TRACE-300`, `BGS-TRACE-307`, `BGS-TRACE-321` | None registered | 1 |
| [BGS-TRACE-302](../mathematics/fixed-map/lineN5N18_gas_conditional.md) | open | `BGS-TRACE-307`, `BGS-TRACE-322` | None registered | 1 |
| [BGS-TRACE-303](../mathematics/fixed-map/lineN5N18_gas_conditional.md) | open | `BGS-TRACE-313`, `BGS-TRACE-319`, `BGS-TRACE-320` | None registered | 1 |
| [BGS-TRACE-304](../mathematics/fixed-map/lineN5N18_gas_conditional.md) | open | `BGS-TRACE-296`, `BGS-TRACE-315` | None registered | 1 |
| [BGS-TRACE-305](../mathematics/fixed-map/lineN5N18_gas_conditional.md) | open | `BGS-TRACE-223`, `BGS-TRACE-227`, `BGS-TRACE-238`, `BGS-TRACE-244`, `BGS-TRACE-251`, `BGS-TRACE-252`, `BGS-TRACE-265`, `BGS-TRACE-273`, `BGS-TRACE-275`, `BGS-TRACE-280`, `BGS-TRACE-281`, `BGS-TRACE-282`, `BGS-TRACE-317` | None registered | 1 |
| [BGS-TRACE-306](../mathematics/fixed-map/lineN5N18_gas_conditional.md) | open | `BGS-TRACE-300`, `BGS-TRACE-308`, `BGS-TRACE-320` | None registered | 1 |
| [BGS-TRACE-307](../mathematics/fixed-map/lineN5N18_gas_conditional.md) | proved | `BGS-TRACE-309`, `BGS-TRACE-311` | None registered | 6 |
| [BGS-TRACE-308](../mathematics/fixed-map/lineN5N18_gas_conditional.md) | proved | `BGS-TRACE-309` | None registered | 2 |
| [BGS-TRACE-309](../mathematics/fixed-map/lineN5N18_gas_conditional.md) | proved | `BGS-TRACE-213`, `BGS-TRACE-313` | None registered | 8 |
| [BGS-TRACE-310](../mathematics/fixed-map/lineN5N18_gas_conditional.md) | proved | `BGS-TRACE-198`, `BGS-TRACE-309` | None registered | 2 |
| [BGS-TRACE-311](../mathematics/fixed-map/lineN5N18_gas_conditional.md) | proved | `BGS-TRACE-309` | None registered | 3 |
| [BGS-TRACE-312](../mathematics/fixed-map/lineN5N18_gas_conditional.md) | proved | `BGS-TRACE-309` | None registered | 2 |
| [BGS-TRACE-313](../mathematics/fixed-map/lineN5N18_gas_conditional.md) | proved | `BGS-TRACE-229`, `BGS-TRACE-285` | None registered | 5 |
| [BGS-TRACE-314](../mathematics/fixed-map/lineN5N18_gas_conditional.md) | proved | `BGS-TRACE-198`, `BGS-TRACE-226`, `BGS-TRACE-227`, `BGS-TRACE-228`, `BGS-TRACE-229` | None registered | 1 |
| [BGS-TRACE-315](../mathematics/fixed-map/lineN5N18_gas_conditional.md) | proved | `BGS-TRACE-265`, `BGS-TRACE-277` | None registered | 3 |
| [BGS-TRACE-316](../mathematics/fixed-map/lineN5N18_gas_conditional.md) | proved | `BGS-TRACE-206`, `BGS-TRACE-315` | None registered | 0 |
| [BGS-TRACE-317](../mathematics/fixed-map/lineN5N18_gas_conditional.md) | proved | `BGS-TRACE-206`, `BGS-TRACE-213`, `BGS-TRACE-273` | None registered | 2 |
| [BGS-TRACE-318](../mathematics/fixed-map/lineN5N18_gas_conditional.md) | proved | `BGS-TRACE-307`, `BGS-TRACE-310` | None registered | 1 |
| [BGS-TRACE-319](../mathematics/fixed-map/lineN5N18_gas_conditional.md) | proved | `BGS-TRACE-313` | None registered | 3 |
| [BGS-TRACE-320](../mathematics/fixed-map/lineN5N18_gas_conditional.md) | verification-pending | `BGS-TRACE-296`, `BGS-TRACE-319` | None registered | 3 |
| [BGS-TRACE-321](../mathematics/fixed-map/lineN5N18_gas_conditional.md) | proved | `BGS-TRACE-307`, `BGS-TRACE-309` | None registered | 2 |
| [BGS-TRACE-322](../mathematics/fixed-map/lineN5N18_gas_conditional.md) | verification-pending | `BGS-TRACE-307` | None registered | 2 |
| [BGS-TRACE-323](../mathematics/fixed-map/lineN5N18_gas_conditional.md) | verification-pending | `BGS-TRACE-311` | None registered | 1 |
| [BGS-TRACE-324](../mathematics/fixed-map/lineN5N18_gas_conditional.md) | verification-pending | `BGS-TRACE-198`, `BGS-TRACE-199`, `BGS-TRACE-313` | None registered | 1 |
