# Historical producer-path map — 2026-09-03

This file resolves historical producer labels without rewriting preserved result provenance. A resolved source path means only that the producer can be located; it does not certify the old run.

The audit scanned 62 producer references. 48 were resolvable to a current/recoverable source path and 14 are explicitly inline/non-file computations. The mapping contains 37 distinct historical-to-current path relations. Root `STATUS.md`, `data/MANIFEST.md`, and `results/README.md` control interpretation.

## Main resolved mappings

| Historical path | Current/recoverable path |
|---|---|
| `code/experiments/goe_spacing_n95419.py` | `code/large_m/bgs_spacing_N95419.py` |
| `code/verification/goe_spacing_test.py` | `code/legacy_verification/goe_spacing_test.py` |
| `src/large_m/bgs_spacing_N95419.py` | `code/large_m/bgs_spacing_N95419.py` |
| `src/large_m/number_variance_goe_control.py` | `code/large_m/number_variance_goe_control.py` |
| `src/large_m/theorem_ii_extended.py` | `code/large_m/theorem_ii_extended.py` |
| `src/large_m/toy_subweyl.py` | `code/large_m/toy_subweyl.py` |
| `src/large_m/trace_fluctuation.py` | `code/large_m/trace_fluctuation.py` |
| `src/m1_r5.py` | `docs/archive/scripts/m1_r5.py` |
| `src/r80_e_residue.py` | `code/large_m/e_residue.py` |
| `src/r80_julia_bigdp.jl` | `code/large_m/julia_bigdp.jl` |
| `src/r80_jweight_dp.py` | `code/shape_automaton/jweight_dp.py` |
| `src/r80_wrap_collisions.py` | `code/shape_automaton/wrap_collisions.py` |
| `src/r81_local_law_pilot.py` | `code/large_m/local_law_pilot.py` |
| `src/r81b_rigidity_discriminator.py` | `code/large_m/rigidity_discriminator.py` |
| `src/r81c_rigidity_control.py` | `code/large_m/rigidity_control.py` |
| `src/r81d_coherent_mode.py` | `code/large_m/coherent_mode.py` |
| `src/r82_dp_exact.jl` | `code/shape_automaton/dp_exact.jl` |
| `src/r82_shape_modes.py` | `code/large_m/shape_modes.py` |
| `src/r82b_dp_push.jl` | `code/shape_automaton/dp_push.jl` |
| `src/r82c_density_shape.py` | `code/large_m/density_shape.py` |
| `src/r82d_orbit_invariant.py` | `code/large_m/orbit_invariant.py` |
| `src/r82e_edge_vs_bulk.py` | `code/large_m/edge_vs_bulk.py` |
| `src/r82f_torus_rigidity.py` | `code/large_m/torus_rigidity.py` |
| `src/r82g_q_curve.py` | `code/large_m/q_curve.py` |
| `src/r82h_normal_form.py` | `code/large_m/normal_form.py` |
| `src/r82j_closed_form.py` | `code/theorems/theorem_ii_twisted_jacobi.py` |
| `src/r82k_bgs_large_m.py` | `code/large_m/bgs_large_m.py` |
| `src/r82l_second_moment_exact.py` | `code/large_m/second_moment_exact.py` |
| `src/r82n_fourth_moment.py` | `code/large_m/fourth_moment.py` |
| `src/r82o_rigidity_long_range.py` | `code/large_m/rigidity_long_range.py` |
| `src/r82p_rigidity_control.py` | `code/large_m/rigidity_control_v2.py` |
| `src/r82q_spectral_fourth.py` | `code/large_m/spectral_fourth.py` |
| `src/r82r_small_spacings.py` | `code/large_m/small_spacings.py` |
| `src/r82s_crossing_deficit.py` | `code/large_m/crossing_deficit.py` |
| `src/r82t_second_moment_raw.py` | `code/large_m/second_moment_raw.py` |
| `src/r82u_catalan_honest.py` | `code/large_m/catalan_honest.py` |
| `src/r82w_family_second_moment.py` | `code/large_m/family_second_moment.py` |

## Explicit inline/unresolved producer labels

The following are preserved as inline ledger provenance rather than fabricated source files: R82.19 corrected spectral-fourth, R82.21b Catalan verification, R82.13 second-moment verification, R82.24b fourth-design, R82.25b family-second-moment, R82.30/30b k4 calculations, R82.21 sixth-moment direct, R82.23/23b/24 branch computations, and R82.10 normal-form-phase. Historical labels such as `src/r82m_jacobi_moments.py (inline)` and `src/r82i_entry_statistics.py (inline)` remain unresolved standalone producers.

## Promotion rule

When an old result becomes load-bearing again, locate/port the producer, state the statistic and assumptions, rerun it into `results/verified/` or `results/numerical/`, and leave the original JSON unchanged.
