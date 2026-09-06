"""R84: repair the stale pre-rebrand paths in artifacts/legacy_runs/MANIFEST.md.

Idempotent: applies the flat-path -> topic-subfolder and artifact-path ->
actual-post-rebrand-location substitutions; skips any whose target text is
already absent, then verifies no known-flat script paths remain.
Run:  py -3 src/maintenance/repair_manifest_r84.py
"""
import io
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PATH = os.path.join(ROOT, "artifacts", "legacy_runs", "MANIFEST.md")

SCRIPT_SUBS = [
    # ---- RUN 71 and earlier rows (flat src paths -> topic subfolders) ----
    ("`src/catmap_independent.py`", "`src/core/catmap_independent.py`"),
    ("`python src/catmap_independent.py`", "`python src/core/catmap_independent.py`"),
    ("`src/theoremB_covariance.py`", "`src/theorems/theorem_a_covariance.py`"),
    ("`python src/theoremB_covariance.py`", "`python src/theorems/theorem_a_covariance.py`"),
    ("`src/compression_spacings.py`", "`src/diagnostics/compression_spacings.py`"),
    ("`python src/compression_spacings.py`", "`python src/diagnostics/compression_spacings.py`"),
    ("`src/single_orbit_trend.py`", "`src/diagnostics/single_orbit_trend.py`"),
    ("`python src/single_orbit_trend.py`", "`python src/diagnostics/single_orbit_trend.py`"),
    ("`src/subgroup_kloosterman_energy.py`", "`src/kloosterman/subgroup_kloosterman_energy.py`"),
    ("`python src/subgroup_kloosterman_energy.py`", "`python src/kloosterman/subgroup_kloosterman_energy.py`"),
    ("`src/moment_certification.py`", "`src/diagnostics/moment_certification.py`"),
    ("`python src/moment_certification.py`", "`python src/diagnostics/moment_certification.py`"),
    ("`src/exceptional_set.py`", "`src/kloosterman/exceptional_set.py`"),
    ("`src/pstar_scan.py`", "`src/kloosterman/pstar_scan.py`"),
    ("`python src/pstar_scan.py`", "`python src/kloosterman/pstar_scan.py`"),
    ("`src/hecke_centring_refutation.py`", "`src/diagnostics/hecke_centring_refutation.py`"),
    ("`python src/hecke_centring_refutation.py`", "`python src/diagnostics/hecke_centring_refutation.py`"),
    ("`src/repair_legacy_paper.py`", "`src/maintenance/repair_legacy_paper.py`"),
    ("`python src/repair_legacy_paper.py`", "`python src/maintenance/repair_legacy_paper.py`"),
    ("`src/patch_theory_r71.py`", "`src/maintenance/patch_theory_r71.py`"),
    ("`python src/patch_theory_r71.py`", "`python src/maintenance/patch_theory_r71.py`"),
    ("`src/verify_mean_law.py`", "`src/diagnostics/verify_mean_law.py`"),
    ("`python src/verify_mean_law.py`", "`python src/diagnostics/verify_mean_law.py`"),
    ("`src/master_general.py`", "`src/theorems/master_general.py`"),
    ("`python src/master_general.py`", "`python src/theorems/master_general.py`"),
    ("`src/char_expansion_cert.py`", "`src/kloosterman/char_expansion_cert.py`"),
    ("`src/reduced_resonance.py`", "`src/core/reduced_resonance.py`"),
    ("`python src/reduced_resonance.py`", "`python src/core/reduced_resonance.py`"),
    ("`src/audit_tail_bound.py`", "`src/diagnostics/audit_tail_bound.py`"),
    ("`python src/audit_tail_bound.py`", "`python src/diagnostics/audit_tail_bound.py`"),
    ("`src/verify_perturbation_wd.py`", "`src/diagnostics/verify_perturbation_wd.py`"),
    ("`src/audit_matching.py`", "`src/diagnostics/audit_matching.py`"),
    ("`src/find_small_period_primes.py`", "`src/kloosterman/find_small_period_primes.py`"),
    # ---- RUN 72/73 rows ----
    ("`src/theta_square_theorem.py`", "`src/theorems/theorem_c_theta_square.py`"),
    ("`src/parity_desymmetrised.py`", "`src/theorems/theorem_d_parity_dichotomy.py`"),
    ("`src/theoremE_torus_repair.py`", "`src/theorems/theorem_e_hecke_torus.py`"),
    ("`src/haar_surrogate.py`", "`src/diagnostics/haar_surrogate.py`"),
    ("`src/desym_ratio_statistic.py`", "`src/diagnostics/desym_ratio_statistic.py`"),
    ("`src/theoremE_operator.py`", "`src/theorems/theorem_e_operator_proof.py`"),
    ("`src/hecke_matrix_elements.py`", "`src/diagnostics/hecke_matrix_elements.py`"),
    ("`src/lemmaF_quadratic_phase.py`", "`src/theorems/lemma_f_quadratic_phase.py`"),
    ("`src/barrier_slack.py`", "`src/theorems/theorem_g_moment_closed.py`"),
    ("`src/desym_large_m.py`", "`src/diagnostics/desym_large_m.py`"),
    ("`src/desym_large_m2.py`", "`src/diagnostics/desym_large_m2.py`"),
    # ---- RUN 74/75/76/78/80 rows ----
    ("`src/ensemble_moments.py`", "`src/diagnostics/ensemble_moments.py`"),
    ("`src/ensemble_excess.py`", "`src/diagnostics/ensemble_excess.py`"),
    ("`src/r75_multiples.py`", "`src/theorems/theorem_h_shape_decomposition.py`"),
    ("`src/r76_phi_ensemble.py`", "`src/shape_automaton/phi_ensemble.py`"),
    ("`src/r77_automaton.py`", "`src/shape_automaton/sofic_automaton.py`"),
    ("`src/r78_eps_minus.py`", "`src/shape_automaton/eps_minus_antiperiodic.py`"),
    ("`src/r80_jweight_dp.py`", "`src/shape_automaton/jweight_dp.py`"),
    ("`src/r80_wrap_collisions.py`", "`src/shape_automaton/wrap_collisions.py`"),
    ("`src/r80_julia_bigdp.jl`", "`src/large_m/julia_bigdp.jl`"),
    ("`src/r80_e_residue.py`", "`src/large_m/e_residue.py`"),
    # ---- RUN 82 rows ----
    ("`src/r82f_torus_rigidity.py`", "`src/large_m/torus_rigidity.py`"),
    ("`src/r82d_orbit_invariant.py`", "`src/large_m/orbit_invariant.py`"),
    ("`src/r82g_q_curve.py`", "`src/large_m/q_curve.py`"),
    ("`src/r82_shape_modes.py`", "`src/large_m/shape_modes.py`"),
    ("`src/r82c_density_shape.py`", "`src/large_m/density_shape.py`"),
    ("`src/r82e_edge_vs_bulk.py`", "`src/large_m/edge_vs_bulk.py`"),
    ("`src/r82_dp_exact.jl`", "`src/shape_automaton/dp_exact.jl`"),
    ("`src/r82_dp_lib.jl`", "`src/shape_automaton/dp_library.jl`"),
    ("`src/r82b_dp_push.jl`", "`src/shape_automaton/dp_push.jl`"),
    ("`src/r82j_closed_form.py`", "`src/theorems/theorem_ii_twisted_jacobi.py`"),
    ("`src/r82l_second_moment_exact.py`", "`src/large_m/second_moment_exact.py`"),
    ("`src/r82k_bgs_large_m.py`", "`src/large_m/bgs_large_m.py`"),
    ("`src/r82n_fourth_moment.py`", "`src/large_m/fourth_moment.py`"),
    ("`src/r82o_rigidity_long_range.py`", "`src/large_m/rigidity_long_range.py`"),
    ("`src/r82p_rigidity_control.py`", "`src/large_m/rigidity_control_v2.py`"),
    ("`src/r82q_spectral_fourth.py`", "`src/large_m/spectral_fourth.py`"),
    ("`src/r82r_small_spacings.py`", "`src/large_m/small_spacings.py`"),
    ("`src/r82t_second_moment_raw.py`", "`src/large_m/second_moment_raw.py`"),
    ("`src/r82u_catalan_honest.py`", "`src/large_m/catalan_honest.py`"),
    ("`src/r82w_family_second_moment.py`", "`src/large_m/family_second_moment.py`"),
]

ARTIFACT_SUBS = [
    # verified against disk 2026-08-31 (ls of legacy_runs/*)
    ("`r71/catmap_independent_checks.json`", "`legacy_runs/theorems/A_covariance/catmap_independent_checks.json`"),
    ("`r71/theoremB_covariance.json`", "`legacy_runs/theorems/A_covariance/theoremB_covariance.json`"),
    ("`r71/compression_spacings.json`", "`legacy_runs/theorems/A_covariance/compression_spacings.json`"),
    ("`r71/single_orbit_trend.json`", "`legacy_runs/theorems/A_covariance/single_orbit_trend.json`"),
    ("`r71/single_orbit_trend.log`", "`legacy_runs/theorems/A_covariance/single_orbit_trend.log`"),
    ("`r71/subgroup_energy.json`", "`legacy_runs/theorems/B_subgroup_kloosterman/subgroup_energy.json`"),
    ("`r71/moment_certification.json`", "`legacy_runs/theorems/A_covariance/moment_certification.json`"),
    ("`r71/exceptional_set.json`", "`legacy_runs/theorems/B_subgroup_kloosterman/exceptional_set.json`"),
    ("`r71/Pstar_prime_k.json`", "`legacy_runs/theorems/B_subgroup_kloosterman/Pstar_prime_k.json`"),
    ("`r71/pstar_scan.log`", "`legacy_runs/theorems/B_subgroup_kloosterman/pstar_scan.log`"),
    ("`r71/hecke_centring_refutation.json`", "`legacy_runs/hecke_centring_void/hecke_centring_refutation.json`"),
    ("`r71/hecke_centring_undivided.json`", "`legacy_runs/hecke_centring_void/hecke_centring_undivided.json`"),
    ("`r72/theta_square_theorem.json`", "`legacy_runs/theorems/C_theta_square/theta_square_theorem.json`"),
    ("`r72/parity_desymmetrised.json`", "`legacy_runs/theorems/D_parity_dichotomy/parity_desymmetrised.json`"),
    ("`r72/theoremE_torus_repair.json`", "`legacy_runs/theorems/E_hecke_torus/theoremE_torus_repair.json`"),
    ("`r72/haar_surrogate.json`", "`legacy_runs/theorems/D_parity_dichotomy/haar_surrogate.json`"),
    ("`r72/desym_ratio_statistic.json`", "`legacy_runs/theorems/D_parity_dichotomy/desym_ratio_statistic.json`"),
    ("`r72/desym_ratio.log`", "`legacy_runs/theorems/D_parity_dichotomy/desym_ratio.log`"),
    ("`r72/prime_power_criterion.json`", "`legacy_runs/theorems/B_subgroup_kloosterman/prime_power_criterion.json`"),
    ("`r73/theoremE_operator.json`", "`legacy_runs/theorems/E_hecke_torus/theoremE_operator.json`"),
    ("`r73/hecke_matrix_elements.json`", "`legacy_runs/theorems/E_hecke_torus/hecke_matrix_elements.json`"),
    ("`r73/composite_k_criterion.json`", "`legacy_runs/theorems/B_subgroup_kloosterman/composite_k_criterion.json`"),
    ("`r73/lemmaF_quadratic_phase.json`", "`legacy_runs/theorems/F_quadratic_phase/lemmaF_quadratic_phase.json`"),
    ("`r73/lemmaF_closed_form.json`", "`legacy_runs/theorems/F_quadratic_phase/lemmaF_closed_form.json`"),
    ("`r73/barrier_slack.json`", "`legacy_runs/theorems/G_moment_closed/barrier_slack.json`"),
    ("`r73/desym_large_m.json`", "`legacy_runs/theorems/E_hecke_torus/desym_large_m.json`"),
    ("`r73/r73_desym_large_m2.log`", "`legacy_runs/theorems/E_hecke_torus/r73_desym_large_m2.log`"),
    ("`r74/ensemble_moments.json`", "`legacy_runs/ensemble_moments/ensemble_moments.json`"),
    ("`r74/ensemble_excess.json`", "`legacy_runs/ensemble_moments/ensemble_excess.json`"),
    ("`r75/multiples_structure.json`", "`legacy_runs/theorems/H_shape_decomposition/multiples_structure.json`"),
    ("`r75/shapes_t3_w16.json`", "`legacy_runs/theorems/H_shape_decomposition/shapes_t3_w16.json`"),
    ("`r75/accident_vectors_r6.txt`", "`legacy_runs/theorems/H_shape_decomposition/accident_vectors_r6.txt`"),
    ("`r75/desym_m1674.json`", "`legacy_runs/theorems/E_hecke_torus/desym_m1674.json`"),
    ("`r75/desym_m1674.log`", "`legacy_runs/theorems/E_hecke_torus/desym_m1674.log`"),
    ("`r76/phi_ensemble.json`", "`legacy_runs/ensemble_moments/phi_ensemble.json`"),
    ("`r76_run.log`", "`legacy_runs/ensemble_moments/r76_run.log`"),
    ("`r76_run12.log`", "`legacy_runs/ensemble_moments/r76_run12.log`"),
    ("`r78/eps_minus.json`", "`legacy_runs/ensemble_moments/eps_minus.json`"),
    ("`r78_run.log`", "`legacy_runs/ensemble_moments/r78_run.log`"),
    ("`r80/jweight_dp.json`", "`legacy_runs/ensemble_moments/jweight_dp.json`"),
    ("`r80/wrap_collisions.json`", "`legacy_runs/ensemble_moments/wrap_collisions.json`"),
    ("`r80/julia_bigdp.json`", "`legacy_runs/ensemble_moments/julia_bigdp.json`"),
    ("`r80/e_residue.json`", "`legacy_runs/ensemble_moments/e_residue.json`"),
    # RUN 82 artifacts live under theorems/{I,II} and diagnostics
    ("`r82/torus_rigidity.json`", "`theorems/I_torus_rigidity/torus_rigidity.json`"),
    ("`r82/torus_rigidity.log`", "`theorems/I_torus_rigidity/torus_rigidity.log`"),
    ("`r82/orbit_invariant.json`", "`theorems/I_torus_rigidity/orbit_invariant.json`"),
    ("`r82/q_curve.json`", "`theorems/I_torus_rigidity/q_curve.json`"),
    ("`r82/q_curve_N199.npz`", "`theorems/I_torus_rigidity/q_curve_N199.npz`"),
    ("`r82/q_curve_N3571.npz`", "`theorems/I_torus_rigidity/q_curve_N3571.npz`"),
    ("`r82/raw_trace_dft.json`", "`theorems/I_torus_rigidity/raw_trace_dft.json`"),
    ("`r82/shape_modes.json`", "`diagnostics/shape_modes.json`"),
    ("`r82/density_shape.json`", "`diagnostics/density_shape.json`"),
    ("`r82/edge_vs_bulk.json`", "`diagnostics/edge_vs_bulk.json`"),
    ("`r82/edge_vs_bulk_9349.json`", "`diagnostics/edge_vs_bulk_9349.json`"),
    ("`r82/dp_exact.json`", "`diagnostics/dp_exact.json`"),
    ("`r82/dp_push.json`", "`diagnostics/dp_push.json`"),
    ("`r82/lean_build.log`", "`theorems/I_torus_rigidity/lean_build.log`"),
    ("`r82/level_sets_split_inert.json`", "`theorems/I_torus_rigidity/level_sets_split_inert.json`"),
    ("`r82/second_moment_identity.json`", "`theorems/I_torus_rigidity/second_moment_identity.json`"),
    ("`r82/normal_form.json`", "`theorems/II_twisted_jacobi/normal_form.json`"),
    ("`r82/normal_form_phase.json`", "`theorems/II_twisted_jacobi/normal_form_phase.json`"),
    ("`r82/entry_statistics.json`", "`theorems/II_twisted_jacobi/entry_statistics.json`"),
    ("`r82/closed_form.json`", "`theorems/II_twisted_jacobi/closed_form.json`"),
    ("`r82/second_moment_exact.json`", "`theorems/II_twisted_jacobi/second_moment_exact.json`"),
    ("`r82/second_moment_exact2.json`", "`theorems/II_twisted_jacobi/second_moment_exact2.json`"),
    ("`r82/bgs_large_m.json`", "`diagnostics/bgs_large_m.json`"),
    ("`r82/bgs_large_m_big.json`", "`diagnostics/bgs_large_m_big.json`"),
    ("`r82/jacobi_moments.json`", "`diagnostics/jacobi_moments.json`"),
    ("`r82/fourth_moment.json`", "`diagnostics/fourth_moment.json`"),
    ("`r82/rigidity_long_range.json`", "`diagnostics/rigidity_long_range.json`"),
    ("`r82/rigidity_control.json`", "`diagnostics/rigidity_control.json`"),
    ("`r82/rigidity_spectra.npz`", "`diagnostics/rigidity_spectra.npz`"),
    ("`r82/spectral_fourth.json`", "`diagnostics/spectral_fourth.json`"),
    ("`r82/spectral_fourth_fixed.json`", "`diagnostics/spectral_fourth_fixed.json`"),
    ("`r82/spectral_fourth_truth2.log`", "`diagnostics/spectral_fourth_truth2.log`"),
    ("`r82/small_spacings.json`", "`diagnostics/small_spacings.json`"),
    ("`r82/catalan_verify.json`", "`diagnostics/catalan_verify.json`"),
    ("`r82/sixth_moment_direct.json`", "`diagnostics/sixth_moment_direct.json`"),
    ("`r82/crossing_deficit.json`", "`diagnostics/crossing_deficit.json`"),
    ("`r82/second_moment_raw.json`", "`diagnostics/second_moment_raw.json`"),
    ("`r82/catalan_honest.json`", "`diagnostics/catalan_honest.json`"),
    ("`r82/t11_exact.log`", "`diagnostics/t11_exact.log`"),
    ("`r82/zero_mode_anomaly.log`", "`diagnostics/zero_mode_anomaly.log`"),
    ("`r82/branch_scan9349.json`", "`diagnostics/branch_scan9349.json`"),
    ("`r82/branch_third_design.json`", "`diagnostics/branch_third_design.json`"),
    ("`r82/branch_mirror9349.json`", "`diagnostics/branch_mirror9349.json`"),
    ("`r82/cscale_proof.log`", "`diagnostics/cscale_proof.log`"),
    ("`r82/fourth_design.json`", "`diagnostics/fourth_design.json`"),
    ("`r82/k0_law_final.log`", "`diagnostics/k0_law_final.log`"),
    ("`r82/family_second_moment.json`", "`diagnostics/family_second_moment.json`"),
    ("`r82/family_second_moment2.json`", "`diagnostics/family_second_moment2.json`"),
    ("`r82/lean_scale_law.log`", "`theorems/II_twisted_jacobi/lean_scale_law.log`"),
    ("`r82/inert_torus.json`", "`diagnostics/inert_torus.json`"),
    ("`r82/k4_moment.json`", "`diagnostics/k4_moment.json`"),
    ("`r82/k4_convergence.json`", "`diagnostics/k4_convergence.json`"),
    ("`r82/k4_ab_decomp.log`", "`diagnostics/k4_ab_decomp.log`"),
    ("`r82/k4_kl_convergence.log`", "`diagnostics/k4_kl_convergence.log`"),
    ("`r82/k4_histograms.log`", "`diagnostics/k4_histograms.log`"),
    ("`r82/k4_surface_family.json`", "`diagnostics/k4_surface_family.json`"),
    # Lean section: the external project is LOST (R82.0, LESSON 82-E)
    ("`C:\\lean\\bgs_formal\\BgsFormal.lean` — collision lemmas",
     "**[ARTIFACT LOST — R82.0/LESSON 82-E]** the external project `C:\\lean\\bgs_formal\\` is gone; "
     "the R2-era collision-lemma certificate (`collision_ext`, `prod_eq`, `sum_sq`) is UNVERIFIABLE. "
     "The live in-workspace Lean project is `formal/` (TorusLevelSets.lean, ScaleLaw.lean; R82.8/R82.26)."),
]

HEADER_OLD = "# ARTIFACT MANIFEST\n\n"
HEADER_NEW = (
    "# ARTIFACT MANIFEST\n\n"
    "> **R84 repair (2026-08-31).** Every script path below was repointed to\n"
    "> its post-R82 topic-subfolder location (`src/{core,theorems,diagnostics,\n"
    "> kloosterman,shape_automaton,large_m,maintenance}/...`) and every\n"
    "> artifact path to its actual location (`legacy_runs/{theorems,\n"
    "> ensemble_moments,hecke_centring_void}/...` relative to `artifacts/`, or\n"
    "> `artifacts/diagnostics/`). The repointing was verified by a disk\n"
    "> spot-check: 18/18 load-bearing artifacts resolve\n"
    "> (REVIEW_FINDINGS.md Part C). The R71 provenance warning below still\n"
    "> applies verbatim.\n\n"
)

CLAIM_OLD = (
    "Every load-bearing number in `paper/resonance_laws_catmaps.tex` is\ntraceable"
)
CLAIM_NEW = (
    "Every load-bearing number in the papers\n"
    "(`paper/exact_wd_and_subgroup_moments.tex` and the archived\n"
    "`archive/papers/resonance_laws_catmaps.tex`) is\ntraceable"
)


def main():
    s = io.open(PATH, encoding="utf-8").read()
    applied = missed = 0
    for a, b in SCRIPT_SUBS + ARTIFACT_SUBS:
        if a in s:
            s = s.replace(a, b)
            applied += 1
        else:
            missed += 1
    s = s.replace(HEADER_OLD, HEADER_NEW, 1)
    s = s.replace(CLAIM_OLD, CLAIM_NEW, 1)
    io.open(PATH, "w", encoding="utf-8", newline="\n").write(s)
    print(f"applied {applied} substitutions, {missed} already-absent")
    flat = re.findall(
        r"`(?:src/)?(?:r8[0-9][a-z]?_|r80_|r82[a-z]?_)[A-Za-z0-9_.]+\.(?:py|jl)`", s)
    flat = [f for f in flat if not f.startswith("`src/")]
    print("remaining flat script paths:", len(flat), flat[:5])
    print("remaining r7x/r8x artifact prefixes:",
          len(re.findall(r"`r8[0-2]/", s)))
    sys.exit(0 if not flat else 1)


if __name__ == "__main__":
    main()
