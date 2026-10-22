# Scientific dependency graph

Generated from [claims.json](claims.json) by `computations/maintenance/render_research_views.py`.
The [ledger](claim_ledger.md) controls scientific status; the JSON view has the same complete adjacency.

**197 registered nodes; 241 direct prerequisite edges.**

An edge records a scoped programme prerequisite; it does not discharge a hypothesis.
“None registered” does not mean unconditional or self-contained.
External locators and mappings are in the [external registry](../literature/external_dependencies.json).

BGS-BGS-001 and BGS-TRACE-005 remain OPEN. Auxiliary ensembles and
abstract-family obstructions retain their original models and proof boundaries.

| Claim and source | State | Direct registered prerequisites | Registered external inputs | Direct consumers |
|---|---|---|---|---:|
| [BGS-BGS-001](../mathematics/fixed_map_resolvent_frontier.md) | open | `BGS-FM-001`, `BGS-FM-002`, `BGS-FM-003`, `BGS-FM-004`, `BGS-LOOP-001`, `BGS-TRACE-004`, `BGS-TRACE-005` | `EXT-BH-2026` | 0 |
| [BGS-CAYLEY-001](../mathematics/fourth_moment_reduction.md) | proved | None registered | None registered | 1 |
| [BGS-CAYLEY-002](../mathematics/cayley_additive_energy.md) | proved | `BGS-CAYLEY-001` | None registered | 3 |
| [BGS-CAYLEY-003](../mathematics/cayley_direct_energy.md) | verification-pending | `BGS-CAYLEY-002` | `EXT-VM-2015` | 1 |
| [BGS-CAYLEY-004](../mathematics/cayley_curve_uniform.md) | proved | `BGS-CAYLEY-002` | `EXT-CZ-2013` | 1 |
| [BGS-CAYLEY-005](../mathematics/open_questions.md) | open | `BGS-CAYLEY-002`, `BGS-CAYLEY-003`, `BGS-CAYLEY-004` | None registered | 0 |
| [BGS-CAYLEY-006](../mathematics/cayley_trace_gaussian_limit.md) | proved | None registered | None registered | 0 |
| [BGS-CAYLEY-007](../mathematics/cayley_product_row_real_trace_ideal.md) | proved | None registered | None registered | 0 |
| [BGS-CAYLEY-008](../mathematics/cayley_scaling_rigidity.md) | proved | None registered | None registered | 0 |
| [BGS-CAYLEY-009](../mathematics/magnetic_quotient_semicircle.md) | proved | None registered | None registered | 0 |
| [BGS-CAYLEY-010](../manuscript/general_spectra.tex) | proved | None registered | None registered | 0 |
| [BGS-CUE-001](../mathematics/cue_singular_energy.md) | proved | None registered | `EXT-BAB-2013` | 0 |
| [BGS-CUE-002](../mathematics/full_pair_cue_covariance_20261015.md) | proved | `BGS-TRACE-002` | None registered | 0 |
| [BGS-FLOW-001](../mathematics/coboundary_spectral_flow_bound.md) | proved | None registered | None registered | 0 |
| [BGS-FLOW-002](../mathematics/coboundary_spectral_flow_bound.md) | proved | None registered | None registered | 0 |
| [BGS-FLOW-003](../mathematics/quadratic_coboundary_noise.md) | proved | None registered | None registered | 8 |
| [BGS-FLOW-004](../mathematics/quadratic_noise_coupling.md) | proved | `BGS-FLOW-003` | None registered | 5 |
| [BGS-FLOW-005](../mathematics/quadratic_noise_reversibility.md) | proved | `BGS-FLOW-003`, `BGS-FLOW-004` | None registered | 2 |
| [BGS-FLOW-006](../mathematics/quadratic_noise_trace_fluctuations.md) | proved | `BGS-FLOW-003`, `BGS-FLOW-005` | None registered | 0 |
| [BGS-FLOW-007](../mathematics/quadratic_noise_clock_limit.md) | proved | `BGS-FLOW-004`, `BGS-FLOW-005` | `EXT-FORRESTER-1996` | 5 |
| [BGS-FLOW-008](../mathematics/coboundary_fourth_order_drift.md) | proved | `BGS-FLOW-003` | None registered | 2 |
| [BGS-FLOW-009](../mathematics/coboundary_mobius_diffusion.md) | proved | `BGS-FLOW-003`, `BGS-FLOW-004`, `BGS-FLOW-007`, `BGS-FLOW-008` | None registered | 5 |
| [BGS-FLOW-010](../mathematics/coboundary_joint_limit.md) | proved | `BGS-FLOW-003`, `BGS-FLOW-004`, `BGS-FLOW-007`, `BGS-FLOW-008`, `BGS-FLOW-009` | None registered | 3 |
| [BGS-FLOW-011](../mathematics/coboundary_polynomial_limit.md) | proved | `BGS-FLOW-003`, `BGS-FLOW-007`, `BGS-FLOW-009`, `BGS-FLOW-010` | None registered | 2 |
| [BGS-FLOW-012](../mathematics/coboundary_general_start.md) | proved | `BGS-FLOW-009`, `BGS-FLOW-010`, `BGS-FLOW-011`, `BGS-FM-013` | None registered | 4 |
| [BGS-FLOW-013](../mathematics/dyson_relaxation_obstruction.md) | proved | `BGS-FLOW-012` | `EXT-POPESCU-2023` | 1 |
| [BGS-FLOW-014](../mathematics/circular_dyson_actual_start.md) | proved | `BGS-FLOW-012`, `BGS-FM-017` | `EXT-KLZF-2022` | 3 |
| [BGS-FLOW-015](../mathematics/microscopic_noise_removal.md) | proved | `BGS-FLOW-007`, `BGS-FLOW-014`, `BGS-FM-013`, `BGS-TRACE-001` | `EXT-EHL-2018`, `EXT-LEMOINE-2025` | 3 |
| [BGS-FLOW-016](../mathematics/local_moment_transport.md) | proved | `BGS-FLOW-004`, `BGS-FLOW-009`, `BGS-FLOW-014` | `EXT-KLZF-2022` | 2 |
| [BGS-FLOW-017](../mathematics/coboundary_all_order_limit.md) | proved | `BGS-FLOW-010`, `BGS-FLOW-011`, `BGS-FLOW-012`, `BGS-FLOW-014`, `BGS-FLOW-016`, `BGS-FM-013`, `BGS-TRACE-001` | `EXT-SOSH-2000` | 2 |
| [BGS-FLOW-018](../mathematics/clock_structure_and_noise_scale.md) | proved | `BGS-FLOW-007`, `BGS-FLOW-015`, `BGS-FLOW-016`, `BGS-FLOW-017`, `BGS-TRACE-007` | `EXT-FORRESTER-1996`, `EXT-KT-2009` | 0 |
| [BGS-FLOW-019](../mathematics/fixed_degree_heat_projection.md) | proved | `BGS-FLOW-015`, `BGS-FLOW-017`, `BGS-FM-013` | `EXT-DE-2001` | 1 |
| [BGS-FLOW-020](../mathematics/growing_degree_trace_projection.md) | proved | `BGS-FLOW-015`, `BGS-FLOW-019`, `BGS-FM-007`, `BGS-FM-013` | `EXT-DE-2001`, `EXT-GHANMI-2017` | 1 |
| [BGS-FLOW-021](../mathematics/heisenberg_pair_heat_formula.md) | proved | `BGS-FLOW-020` | `EXT-DE-2001` | 0 |
| [BGS-FLOW-022](../mathematics/pell_floquet_normal_form.md) | proved | None registered | None registered | 0 |
| [BGS-FLOW-023](../mathematics/pell_coboundary_resonance.md) | proved | None registered | None registered | 0 |
| [BGS-FLOW-024](../mathematics/pell_coboundary_resonance.md) | proved | None registered | None registered | 0 |
| [BGS-FLOW-025](../mathematics/pell_floquet_normal_form.md) | proved | None registered | None registered | 0 |
| [BGS-FM-001](../mathematics/fixed_model_symmetry_theorem.md) | proved | None registered | None registered | 24 |
| [BGS-FM-002](../mathematics/fixed_model_pell_crossover.md) | proved | None registered | None registered | 1 |
| [BGS-FM-003](../mathematics/fixed_map_moment_control_and_transfer.md) | proved | None registered | None registered | 2 |
| [BGS-FM-004](../mathematics/three_orientation_resolvent_barrier.md) | conditional | `BGS-FM-003` | None registered | 1 |
| [BGS-FM-005](../mathematics/frozen_kick_rank_boundary.md) | proved | None registered | `EXT-EV-2015` | 2 |
| [BGS-FM-006](../mathematics/nonlinear_bracket_pressure.md) | proved | `BGS-FM-001` | `EXT-PESIN-1977`, `EXT-PP-1990`, `EXT-RUELLE-1978` | 1 |
| [BGS-FM-007](../mathematics/frozen_seven_cut_reduction.md) | proved | `BGS-FM-001`, `BGS-FM-005`, `BGS-TRACE-001` | None registered | 4 |
| [BGS-FM-008](../mathematics/frozen_algebraic_spectral_simplicity.md) | proved | `BGS-FM-005` | `EXT-POPESCU-2023` | 4 |
| [BGS-FM-009](../mathematics/frozen_common_antireversor_certificate.md) | proved | `BGS-FM-001` | `EXT-POPESCU-2023` | 0 |
| [BGS-FM-010](../mathematics/frozen_arithmetic_trace_rigidity.md) | proved | `BGS-FM-001`, `BGS-FM-008` | `EXT-POPESCU-2023` | 1 |
| [BGS-FM-011](../mathematics/frozen_effective_gap_floor.md) | proved | `BGS-FM-008` | `EXT-ROY-2016` | 0 |
| [BGS-FM-012](../mathematics/frozen_periodic_point_annihilator.md) | proved | `BGS-FM-001` | None registered | 1 |
| [BGS-FM-013](../mathematics/fixed_time_wavepacket_trace_bound.md) | proved | `BGS-FM-001` | None registered | 6 |
| [BGS-FM-014](../mathematics/frozen_phase_finite_type.md) | proved | `BGS-FM-001` | None registered | 2 |
| [BGS-FM-015](../mathematics/frozen_commutator_action.md) | proved | `BGS-FM-001`, `BGS-FM-014` | None registered | 0 |
| [BGS-FM-016](../mathematics/egorov_overlap_rigidity.md) | proved | `BGS-FLOW-003`, `BGS-FM-001` | None registered | 1 |
| [BGS-FM-017](../mathematics/frozen_mesoscopic_regularity.md) | proved | `BGS-FLOW-009`, `BGS-FLOW-012`, `BGS-FLOW-013`, `BGS-FM-007`, `BGS-FM-013` | None registered | 1 |
| [BGS-FM-018](../mathematics/frozen_operator_transfer_coercivity.md) | proved | `BGS-FM-001`, `BGS-FM-006` | `EXT-PP-1990` | 5 |
| [BGS-FM-019](../mathematics/collective_diffusion_gap.md) | proved | `BGS-FM-018` | None registered | 1 |
| [BGS-FM-020](../mathematics/original_channel_gap.md) | proved | `BGS-FM-019` | None registered | 0 |
| [BGS-FM-021](../mathematics/position_chain_mixing.md) | proved | `BGS-FM-001` | None registered | 17 |
| [BGS-FM-022](../mathematics/reversed_path_decay.md) | proved | `BGS-FM-001` | None registered | 4 |
| [BGS-FM-023](../mathematics/arithmetic_translation_exclusion.md) | proved | `BGS-FM-001`, `BGS-FM-016`, `BGS-FM-018` | None registered | 1 |
| [BGS-FM-024](../mathematics/actual_seven_primary_commutant.md) | proved | `BGS-FM-001`, `BGS-FM-008` | `EXT-POPESCU-2023` | 0 |
| [BGS-FM-025](../mathematics/uniform_five_cluster_simplicity.md) | proved | `BGS-FM-001`, `BGS-FM-008` | `EXT-POPESCU-2023` | 0 |
| [BGS-FM-026](../mathematics/literal_time_multiplicity_bounds.md) | proved | `BGS-FM-001` | `EXT-POPESCU-2023` | 0 |
| [BGS-FM-027](../mathematics/phase_trace_checkpoint.md) | proved | `BGS-FM-021` | None registered | 4 |
| [BGS-FM-028](../mathematics/phase_trace_checkpoint.md) | proved | `BGS-FM-018` | None registered | 4 |
| [BGS-FM-029](../mathematics/phase_trace_checkpoint.md) | proved | `BGS-FM-018` | `EXT-ROY-2016` | 1 |
| [BGS-FM-030](../mathematics/phase_trace_checkpoint.md) | proved | `BGS-FM-021` | `EXT-BHATIA-2002` | 0 |
| [BGS-FM-031](../mathematics/ordinary_compact_stratum_centering.md) | proved | `BGS-TRACE-023` | `EXT-ZIRN-2021` | 0 |
| [BGS-FM-032](../mathematics/quantum_cyclic_cohomology_20261015.md) | proved | `BGS-FM-001`, `BGS-TRACE-009` | None registered | 0 |
| [BGS-FM-033](../mathematics/scaled_weyl_overlap_20261015.md) | conditional | `BGS-FM-014`, `BGS-FM-023` | None registered | 0 |
| [BGS-FM-034](../mathematics/fixed_strength_locality.md) | proved | None registered | None registered | 0 |
| [BGS-FM-035](../mathematics/fixed_strength_locality.md) | proved | None registered | None registered | 0 |
| [BGS-FM-036](../mathematics/fixed_strength_locality.md) | proved | None registered | None registered | 0 |
| [BGS-FORMAL-001](../formalization/README.md) | proved | None registered | None registered | 0 |
| [BGS-FORMAL-002](../mathematics/four_cut_rank_two_classification.md) | proved | None registered | None registered | 1 |
| [BGS-FORMAL-003](../formalization/seven_primary_certificate.md) | proved | None registered | None registered | 0 |
| [BGS-FUP-001](../mathematics/offdiagonal_digit_fup.md) | proved | None registered | `EXT-COHEN-2025` | 0 |
| [BGS-INFO-001](../mathematics/open_questions.md) | open | None registered | None registered | 0 |
| [BGS-LOOP-001](../mathematics/fixed_map_resolvent_frontier.md) | conditional | `BGS-FM-007`, `BGS-TRACE-002` | `EXT-BH-2026` | 1 |
| [BGS-RES-001](../mathematics/fourier_line_resonance_coercivity.md) | proved | None registered | None registered | 1 |
| [BGS-RES-002](../mathematics/local_jet_resonance_obstruction.md) | proved | None registered | None registered | 1 |
| [BGS-RES-003](../mathematics/open_questions.md) | open | `BGS-RES-001`, `BGS-RES-002` | None registered | 0 |
| [BGS-RES-004](../mathematics/finite_orbit_resonance_rigidity.md) | proved | None registered | None registered | 0 |
| [BGS-RES-005](../mathematics/frozen_full_lag_resonance.md) | proved | None registered | None registered | 0 |
| [BGS-RES-006](../mathematics/fixed_map_resolvent_frontier.md) | proved | None registered | None registered | 1 |
| [BGS-RES-007](../mathematics/fixed_map_resolvent_frontier.md) | proved | `BGS-FM-007`, `BGS-RES-006` | None registered | 0 |
| [BGS-RES-008](../mathematics/pell_sharp_orbit_coercivity.md) | proved | None registered | None registered | 0 |
| [BGS-RES-009](../manuscript/unified_sections/spectral_modules.tex) | proved | None registered | None registered | 0 |
| [BGS-RES-010](../manuscript/unified_sections/spectral_modules.tex) | proved | None registered | None registered | 0 |
| [BGS-RES-011](../manuscript/unified_sections/spectral_modules.tex) | proved | None registered | None registered | 0 |
| [BGS-RES-012](../manuscript/unified_sections/spectral_modules.tex) | proved | None registered | None registered | 0 |
| [BGS-RES-013](../manuscript/unified_sections/spectral_modules.tex) | proved | None registered | None registered | 0 |
| [BGS-RES-014](../mathematics/resonance_riesz_regularization.md) | conditional | None registered | None registered | 1 |
| [BGS-RES-015](../mathematics/two_window_resonance_crossover.md) | proved | `BGS-RES-014` | None registered | 0 |
| [BGS-RES-016](../mathematics/multiradius_polynomial_rigidity.md) | proved | None registered | None registered | 0 |
| [BGS-RES-017](../mathematics/balanced_phase_controllability.md) | proved | None registered | None registered | 0 |
| [BGS-RES-018](../mathematics/entire_temporal_gauge.md) | proved | None registered | None registered | 0 |
| [BGS-RES-019](../mathematics/resonance_wiener_stability.md) | proved | None registered | None registered | 0 |
| [BGS-RES-020](../mathematics/generic_wiener_resonance.md) | proved | None registered | None registered | 0 |
| [BGS-RES-021](../manuscript/unified_sections/analytic_resonance_rigidity.tex) | proved | None registered | None registered | 0 |
| [BGS-RES-022](../mathematics/resonance_nondegeneracy_and_hessian.md) | verification-pending | None registered | None registered | 1 |
| [BGS-RES-023](../mathematics/resonance_nondegeneracy_and_hessian.md) | proved | `BGS-RES-022` | None registered | 0 |
| [BGS-RET-001](../mathematics/pell_harmonic_returns.md) | proved | `BGS-RET-002` | `EXT-DEMNI-2016` | 0 |
| [BGS-RET-002](../mathematics/pell_harmonic_transition.md) | proved | None registered | None registered | 1 |
| [BGS-RET-003](../mathematics/noncommuting_return_words.md) | conditional | None registered | None registered | 0 |
| [BGS-RET-004](../mathematics/noncommuting_return_words.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-001](../mathematics/trace_to_local_statistics_bridge.md) | proved | None registered | None registered | 11 |
| [BGS-TRACE-002](../mathematics/trace_to_local_statistics_bridge.md) | proved | `BGS-TRACE-001` | None registered | 8 |
| [BGS-TRACE-003](../mathematics/trace_to_local_statistics_bridge.md) | proved | `BGS-TRACE-002` | None registered | 4 |
| [BGS-TRACE-004](../mathematics/bandlimited_correlation_extension.md) | proved | `BGS-TRACE-003` | None registered | 2 |
| [BGS-TRACE-005](../mathematics/open_questions.md) | open | `BGS-FM-001`, `BGS-TRACE-003` | None registered | 1 |
| [BGS-TRACE-006](../mathematics/clustered_abel_window_boundary.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-007](../mathematics/fixed_map_resolvent_frontier.md) | proved | None registered | `EXT-CK-2006` | 2 |
| [BGS-TRACE-008](../mathematics/two_clock_gram_falsifier.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-009](../mathematics/prime_resonant_sector.md) | proved | `BGS-FM-001`, `BGS-FM-010`, `BGS-TRACE-003` | `EXT-RAINS-2003` | 4 |
| [BGS-TRACE-010](../mathematics/signed_heisenberg_comparison.md) | proved | `BGS-TRACE-001`, `BGS-TRACE-002`, `BGS-TRACE-003` | `EXT-DE-2001` | 1 |
| [BGS-TRACE-011](../mathematics/resonant_cubic_density_control.md) | proved | `BGS-TRACE-001`, `BGS-TRACE-009`, `BGS-TRACE-010` | `EXT-DE-2001` | 1 |
| [BGS-TRACE-012](../mathematics/folded_quadratic_resonance_control.md) | proved | `BGS-FM-001`, `BGS-TRACE-001`, `BGS-TRACE-009`, `BGS-TRACE-011` | None registered | 0 |
| [BGS-TRACE-013](../mathematics/arithmetic_word_expansion_obstruction.md) | proved | None registered | `EXT-BG-2008`, `EXT-DIRICHLET-1837`, `EXT-GAE-2007`, `EXT-POPESCU-2023` | 0 |
| [BGS-TRACE-014](../mathematics/isospectral_clock_moment_control.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-015](../mathematics/three_block_unmarking.md) | proved | `BGS-FM-021` | None registered | 0 |
| [BGS-TRACE-016](../mathematics/four_block_unmarking.md) | proved | `BGS-FM-021`, `BGS-FORMAL-002` | None registered | 0 |
| [BGS-TRACE-017](../mathematics/factorial_wkb_reduction.md) | proved | `BGS-FM-001`, `BGS-TRACE-001`, `BGS-TRACE-002` | None registered | 1 |
| [BGS-TRACE-018](../mathematics/winding_defect_locality.md) | proved | `BGS-FM-001`, `BGS-FM-012` | None registered | 1 |
| [BGS-TRACE-019](../mathematics/selected_weighted_coefficient.md) | proved | `BGS-FM-001`, `BGS-TRACE-017`, `BGS-TRACE-018` | `EXT-MANE-1981`, `EXT-PP-1990`, `EXT-RUELLE-1978` | 0 |
| [BGS-TRACE-020](../mathematics/factorial_ordered_diagonal.md) | proved | `BGS-FM-021`, `BGS-TRACE-002` | None registered | 1 |
| [BGS-TRACE-021](../mathematics/phase_trace_checkpoint.md) | proved | `BGS-FM-021`, `BGS-FM-027`, `BGS-TRACE-001`, `BGS-TRACE-020` | None registered | 1 |
| [BGS-TRACE-022](../mathematics/phase_trace_checkpoint.md) | proved | `BGS-FM-021` | None registered | 0 |
| [BGS-TRACE-023](../mathematics/phase_trace_checkpoint.md) | proved | None registered | `EXT-ZIRN-2021` | 6 |
| [BGS-TRACE-024](../mathematics/actual_one_pinch_disappearance.md) | proved | `BGS-FM-021`, `BGS-FM-027`, `BGS-FM-028`, `BGS-TRACE-023` | None registered | 1 |
| [BGS-TRACE-025](../mathematics/rounding_simple_spectrum_endpoint_barriers.md) | proved | `BGS-FM-027`, `BGS-FM-028`, `BGS-FM-029`, `BGS-TRACE-021`, `BGS-TRACE-023` | None registered | 0 |
| [BGS-TRACE-026](../mathematics/hook_tree_phase_current_reduction.md) | proved | `BGS-FM-021`, `BGS-FM-022`, `BGS-TRACE-023` | None registered | 0 |
| [BGS-TRACE-027](../mathematics/weighted_phase_coherence_covariance.md) | proved | `BGS-FM-021`, `BGS-FM-022` | None registered | 0 |
| [BGS-TRACE-028](../mathematics/right_frame_unmasked_pinch_hierarchy.md) | proved | `BGS-FM-021`, `BGS-FM-028`, `BGS-TRACE-023`, `BGS-TRACE-024` | None registered | 1 |
| [BGS-TRACE-029](../mathematics/convex_pinch_weak_noise_and_deconvolution.md) | proved | `BGS-FM-021`, `BGS-FM-027`, `BGS-FM-028`, `BGS-TRACE-023`, `BGS-TRACE-028` | None registered | 0 |
| [BGS-TRACE-053](../mathematics/max_entry_phase_channel.md) | proved | None registered | None registered | 4 |
| [BGS-TRACE-054](../mathematics/sharp_inner_jet.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-055](../record/research_checkpoint_20261008.md) | verification-pending | `BGS-TRACE-053` | None registered | 0 |
| [BGS-TRACE-056](../mathematics/phase_channel_real_flow.md) | proved | `BGS-TRACE-053` | None registered | 2 |
| [BGS-TRACE-057](../mathematics/source_covariance_20261011.md) | proved | None registered | None registered | 1 |
| [BGS-TRACE-058](../mathematics/integrable_phase_absorption_20261011.md) | proved | None registered | None registered | 1 |
| [BGS-TRACE-059](../mathematics/physical_source_transport_20261011.md) | proved | `BGS-TRACE-053`, `BGS-TRACE-056`, `BGS-TRACE-057` | None registered | 0 |
| [BGS-TRACE-060](../mathematics/delay_bootstrap_20261011.md) | conditional | None registered | `EXT-TROPP-2011` | 2 |
| [BGS-TRACE-061](../mathematics/fresh_phase_average_20261011.md) | proved | None registered | None registered | 1 |
| [BGS-TRACE-062](../mathematics/flat_completion_20261011.md) | proved | `BGS-TRACE-061` | None registered | 0 |
| [BGS-TRACE-063](../mathematics/nonlinear_coercivity_20261011.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-064](../mathematics/torus_contraction_20261011.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-065](../mathematics/coherence_form_factor_20261011.md) | proved | None registered | None registered | 1 |
| [BGS-TRACE-066](../mathematics/previous_rank_results_20261011.md) | proved | `BGS-TRACE-065` | `EXT-AGG-1989` | 0 |
| [BGS-TRACE-067](../mathematics/jack_coefficient_theorem_20261011.md) | proved | None registered | None registered | 1 |
| [BGS-TRACE-068](../mathematics/phase_contraction_20261011.md) | proved | `BGS-TRACE-067` | `EXT-JM-2015`, `EXT-MATSUMOTO-2007`, `EXT-OO-1997`, `EXT-VV-2017` | 2 |
| [BGS-TRACE-069](../mathematics/exact_cumulants_20261011.md) | proved | `BGS-TRACE-068` | `EXT-MATSUMOTO-2007` | 1 |
| [BGS-TRACE-070](../mathematics/form_factor_curve_20261011.md) | proved | `BGS-TRACE-068`, `BGS-TRACE-069` | `EXT-HSW-1999` | 0 |
| [BGS-TRACE-071](../mathematics/laplace_path_transport_20261011.md) | proved | `BGS-TRACE-053`, `BGS-TRACE-056`, `BGS-TRACE-058` | None registered | 1 |
| [BGS-TRACE-072](../mathematics/deterministic_path_transport_20261011.md) | proved | `BGS-FM-018`, `BGS-TRACE-071` | None registered | 0 |
| [BGS-TRACE-073](../mathematics/schur_censoring_gap_20261011.md) | conditional | `BGS-FM-021`, `BGS-FM-022` | None registered | 3 |
| [BGS-TRACE-074](../mathematics/unitary_two_step_obstruction_20261012.md) | proved | None registered | None registered | 2 |
| [BGS-TRACE-075](../mathematics/two_step_restoring_drift_20261012.md) | proved | `BGS-TRACE-074` | None registered | 1 |
| [BGS-TRACE-076](../mathematics/haar_feedback_clock_law_20261012.md) | proved | `BGS-TRACE-060` | None registered | 0 |
| [BGS-TRACE-077](../mathematics/green_compression_gap_20261013.md) | proved | `BGS-FM-021`, `BGS-TRACE-073`, `BGS-TRACE-074` | None registered | 3 |
| [BGS-TRACE-078](../mathematics/two_step_increment_variance_20261013.md) | proved | None registered | None registered | 1 |
| [BGS-TRACE-079](../mathematics/two_step_stopped_concentration_20261013.md) | proved | `BGS-FM-021`, `BGS-TRACE-075`, `BGS-TRACE-077`, `BGS-TRACE-078` | None registered | 1 |
| [BGS-TRACE-080](../mathematics/unconditional_feedback_flatness_20261013.md) | proved | `BGS-FM-021`, `BGS-FM-022`, `BGS-TRACE-060`, `BGS-TRACE-073`, `BGS-TRACE-077`, `BGS-TRACE-079` | None registered | 1 |
| [BGS-TRACE-081](../mathematics/flat_spectrum_obstruction_20261014.md) | proved | None registered | None registered | 2 |
| [BGS-TRACE-082](../mathematics/coherence_memory_plateau_20261014.md) | proved | `BGS-TRACE-081` | None registered | 1 |
| [BGS-TRACE-083](../mathematics/coherent_first_return_pulse_20261014.md) | proved | `BGS-TRACE-081`, `BGS-TRACE-082` | None registered | 0 |
| [BGS-TRACE-084](../mathematics/resonant_mesoscopic_criterion_20261015.md) | proved | `BGS-TRACE-009` | None registered | 0 |
| [BGS-TRACE-085](../mathematics/root_lifting_sector_boundary_20261015.md) | proved | `BGS-TRACE-001`, `BGS-TRACE-002` | `EXT-DE-2001` | 0 |
| [BGS-TRACE-086](../mathematics/all_order_process_closure_20261015.md) | proved | `BGS-TRACE-001`, `BGS-TRACE-002`, `BGS-TRACE-004` | None registered | 1 |
| [BGS-TRACE-087](../mathematics/parameter_deaveraging_20261015.md) | proved | `BGS-TRACE-086` | `EXT-DE-2001` | 0 |
| [BGS-TRACE-088](../mathematics/equal_edge_occupation_20261015.md) | proved | `BGS-FM-021` | None registered | 1 |
| [BGS-TRACE-089](../mathematics/collision_crossover_20261015.md) | proved | `BGS-TRACE-088` | `EXT-PITTEL-2016` | 0 |
| [BGS-TRACE-090](../mathematics/bounded_radial_ratios_20261015.md) | proved | None registered | None registered | 1 |
| [BGS-TRACE-091](../mathematics/hardy_spectral_remainder_20261015.md) | proved | `BGS-TRACE-007`, `BGS-TRACE-090` | None registered | 0 |
| [BGS-TRACE-092](../mathematics/abel_clock_rigidity_20261016.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-093](../mathematics/gaussian_equal_edge_20261016.md) | proved | None registered | `EXT-BF-2023`, `EXT-KPSS-2002` | 1 |
| [BGS-TRACE-094](../mathematics/wick_collision_poisson_20261016.md) | proved | `BGS-TRACE-093` | `EXT-CS-2006` | 0 |
| [BGS-TRACE-095](../mathematics/phase_ensemble_continuation_20261019.md) | conditional | `BGS-TRACE-073`, `BGS-TRACE-077`, `BGS-TRACE-080` | None registered | 0 |
| [BGS-TRACE-096](../mathematics/phase_ensemble_continuation_20261019.md) | verification-pending | None registered | None registered | 0 |
| [BGS-TRACE-097](../mathematics/phase_ensemble_continuation_20261019.md) | conditional | None registered | None registered | 0 |
| [BGS-TRACE-098](../mathematics/phase_ensemble_continuation_20261019.md) | verification-pending | None registered | None registered | 1 |
| [BGS-TRACE-099](../mathematics/phase_ensemble_continuation_20261019.md) | verification-pending | `BGS-TRACE-098` | None registered | 0 |
| [BGS-TRACE-100](../mathematics/phase_ensemble_continuation_20261019.md) | verification-pending | None registered | None registered | 1 |
| [BGS-TRACE-101](../mathematics/phase_neutral_primitives_20261019.md) | verification-pending | `BGS-TRACE-100` | None registered | 2 |
| [BGS-TRACE-102](../mathematics/phase_second_defect_20261019.md) | verification-pending | `BGS-TRACE-101` | None registered | 1 |
| [BGS-TRACE-103](../mathematics/phase_quartic_cluster_sum_20261019.md) | verification-pending | `BGS-TRACE-101`, `BGS-TRACE-102` | `EXT-STANLEY-1981` | 0 |
| [BGS-TRACE-104](../mathematics/phase_cayley_cauchy_transfer_20261019.md) | verification-pending | None registered | None registered | 0 |
| [BGS-TRACE-105](../mathematics/cauchy_positive_source_boundary_20261019.md) | verification-pending | None registered | None registered | 0 |
| [BGS-TRACE-106](../mathematics/physical_kick_trace_decay.md) | proved | None registered | None registered | 1 |
| [BGS-TRACE-107](../mathematics/physical_trace_polynomial_approximation.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-108](../mathematics/coordinate_return_quartic_20261021.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-109](../mathematics/inserted_trace_coboundary_20261021.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-110](../mathematics/spectral_orbit_distance_20261021.md) | proved | `BGS-TRACE-112`, `BGS-TRACE-113` | None registered | 0 |
| [BGS-TRACE-111](../mathematics/pell_weighted_curvature_20261021.md) | proved | None registered | None registered | 0 |
| [BGS-TRACE-112](../mathematics/displacement_density_trace_bound_20261021.md) | proved | `BGS-TRACE-106` | None registered | 1 |
| [BGS-TRACE-113](../mathematics/fixed_kick_uniform_trace_bound_20261021.md) | proved | None registered | `EXT-BR-1975` | 1 |
