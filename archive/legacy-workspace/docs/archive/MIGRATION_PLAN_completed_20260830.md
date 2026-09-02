# MIGRATION PLAN — BGS workspace cleanup (2026-08-30)

This plan reorganises the BGS workspace into a human-readable structure with
**one canonical paper**. It is approved by the user but final paper strategy
(α / β / γ) and rebrand scope (R1 / R2 / R3) need explicit confirmation.

## KEEP / RETIRED / GARBAGE inventory

### KEEP (132 scripts in main paths) — to be renamed into thematic subfolders

These are scripts that have references in `LEDGER.md`, `THEORY.md`,
`artifacts/MANIFEST.md`, `paper/*.tex`, or the run-completion `.json` files.

| refs | old path | new path | topic |
|---|---|---|---|
|   5 | src/audit_matching.py | src/diagnostics/audit_matching.py | diagnostics |
|  31 | src/audit_tail_bound.py | src/diagnostics/audit_tail_bound.py | diagnostics |
|  12 | src/barrier_slack.py | src/theorems/theorem_g_moment_closed.py | theorems |
|  47 | src/catmap_core.py | src/core/catmap_core.py | core |
|  55 | src/catmap_independent.py | src/core/catmap_independent.py | core |
|  28 | src/char_expansion_cert.py | src/kloosterman/char_expansion_cert.py | kloosterman |
|   9 | src/check_split_vs_inert.py | src/kloosterman/check_split_vs_inert.py | kloosterman |
|  43 | src/compression_spacings.py | src/diagnostics/compression_spacings.py | diagnostics |
|  26 | src/deligne_check.py | src/kloosterman/deligne_check.py | kloosterman |
|  11 | src/deligne_check_ext.py | src/kloosterman/deligne_check_ext.py | kloosterman |
|  26 | src/desym_large_m.py | src/diagnostics/desym_large_m.py | diagnostics |
|  11 | src/desym_large_m2.py | src/diagnostics/desym_large_m2.py | diagnostics |
|  17 | src/desym_ratio_statistic.py | src/diagnostics/desym_ratio_statistic.py | diagnostics |
|  10 | src/diag_conditional_prob.py | src/diagnostics/diag_conditional_prob.py | diagnostics |
|  14 | src/ensemble_excess.py | src/diagnostics/ensemble_excess.py | diagnostics |
|  15 | src/ensemble_moments.py | src/diagnostics/ensemble_moments.py | diagnostics |
|  11 | src/exact_verify_run5.py | src/diagnostics/exact_verify_run5.py | diagnostics |
|   7 | src/exceptional_set.py | src/kloosterman/exceptional_set.py | kloosterman |
|  11 | src/fast_weil.py | src/kloosterman/fast_weil.py | kloosterman |
|  10 | src/find_small_period_primes.py | src/kloosterman/find_small_period_primes.py | kloosterman |
|  12 | src/haar_surrogate.py | src/diagnostics/haar_surrogate.py | diagnostics |
|  24 | src/hecke_centring_refutation.py | src/diagnostics/hecke_centring_refutation.py | diagnostics |
|  17 | src/hecke_local_law_test.py | src/diagnostics/hecke_local_law_test.py | diagnostics |
|   9 | src/hecke_matrix_elements.py | src/diagnostics/hecke_matrix_elements.py | diagnostics |
|  15 | src/lemmaF_quadratic_phase.py | src/theorems/lemma_f_quadratic_phase.py | theorems |
|  82 | src/master_formula.py | src/theorems/master_formula.py | theorems |
|  22 | src/master_formula_r4.py | src/theorems/master_formula_r4.py | theorems |
|  28 | src/master_formula_strong.py | src/theorems/master_formula_strong.py | theorems |
|  65 | src/master_general.py | src/theorems/master_general.py | theorems |
|  15 | src/moment_certification.py | src/diagnostics/moment_certification.py | diagnostics |
|   7 | src/pair_classifier.py | src/diagnostics/pair_classifier.py | diagnostics |
|  36 | src/parity_desymmetrised.py | src/theorems/theorem_d_parity_dichotomy.py | theorems |
|   5 | src/phase1c_forms.py | src/diagnostics/phase1c_forms.py | diagnostics |
|  17 | src/phase2_beta.py | src/diagnostics/phase2_beta.py | diagnostics |
|   5 | src/phase2_mc_reference.py | src/diagnostics/phase2_mc_reference.py | diagnostics |
|   6 | src/phase2_pooled.py | src/diagnostics/phase2_pooled.py | diagnostics |
|   9 | src/phase3_Apk_sweep.py | src/diagnostics/phase3_Apk_sweep.py | diagnostics |
|  10 | src/phase3_Dpk.py | src/diagnostics/phase3_Dpk_sweep.py | diagnostics |
|   4 | src/phase3_odd_fit.py | src/diagnostics/phase3_odd_fit.py | diagnostics |
|  14 | src/phase3_r6_families.py | src/diagnostics/phase3_r6_families.py | diagnostics |
|  13 | src/pstar_scan.py | src/kloosterman/pstar_scan.py | kloosterman |
|  11 | src/r75_multiples.py | src/theorems/theorem_h_shape_decomposition.py | theorems |
|  11 | src/r76_phi_ensemble.py | src/shape_automaton/phi_ensemble.py | shape_automaton |
|   3 | src/r77_automaton.py | src/shape_automaton/sofic_automaton.py | shape_automaton |
|   7 | src/r78_eps_minus.py | src/shape_automaton/eps_minus_antiperiodic.py | shape_automaton |
|   4 | src/r79_automaton_jl.jl | src/shape_automaton/julia_relation_automaton.jl | shape_automaton |
|   4 | src/r80_e_residue.py | src/large_m/e_residue.py | large_m |
|  14 | src/r80_julia_bigdp.jl | src/large_m/julia_bigdp.jl | large_m |
|   9 | src/r80_jweight_dp.py | src/shape_automaton/jweight_dp.py | shape_automaton |
|   7 | src/r80_wrap_collisions.py | src/shape_automaton/wrap_collisions.py | shape_automaton |
|   1 | src/r81_bigdp_dense.jl | src/large_m/bigdp_dense.jl | large_m |
|   1 | src/r81_bigdp_r104.jl | src/large_m/bigdp_r104.jl | large_m |
|   2 | src/r81_cdense_transfer.jl | src/large_m/cdense_transfer.jl | large_m |
|  11 | src/r81_local_law_pilot.py | src/large_m/local_law_pilot.py | large_m |
|   3 | src/r81b_rigidity_discriminator.py | src/large_m/rigidity_discriminator.py | large_m |
|   3 | src/r81c_rigidity_control.py | src/large_m/rigidity_control.py | large_m |
|   3 | src/r81d_coherent_mode.py | src/large_m/coherent_mode.py | large_m |
|   4 | src/r81e_dp_debug.jl | src/large_m/dp_debug.jl | large_m |
|   9 | src/r82_dp_exact.jl | src/shape_automaton/dp_exact.jl | shape_automaton |
|   6 | src/r82_dp_lib.jl | src/shape_automaton/dp_library.jl | shape_automaton |
|   9 | src/r82_shape_modes.py | src/large_m/shape_modes.py | large_m |
|  10 | src/r82b_dp_push.jl | src/shape_automaton/dp_push.jl | shape_automaton |
|   6 | src/r82c_density_shape.py | src/large_m/density_shape.py | large_m |
|  10 | src/r82d_orbit_invariant.py | src/large_m/orbit_invariant.py | large_m |
|   6 | src/r82e_edge_vs_bulk.py | src/large_m/edge_vs_bulk.py | large_m |
|  11 | src/r82f_torus_rigidity.py | src/large_m/torus_rigidity.py | large_m |
|  13 | src/r82g_q_curve.py | src/large_m/q_curve.py | large_m |
|   6 | src/r82h_normal_form.py | src/large_m/normal_form.py | large_m |
|  15 | src/r82j_closed_form.py | src/theorems/theorem_ii_twisted_jacobi.py | theorems |
|  23 | src/r82k_bgs_large_m.py | src/large_m/bgs_large_m.py | large_m |
|   5 | src/r82l_second_moment_exact.py | src/large_m/second_moment_exact.py | large_m |
|   7 | src/r82n_fourth_moment.py | src/large_m/fourth_moment.py | large_m |
|   6 | src/r82o_rigidity_long_range.py | src/large_m/rigidity_long_range.py | large_m |
|   6 | src/r82p_rigidity_control.py | src/large_m/rigidity_control_v2.py | large_m |
|   4 | src/r82q_spectral_fourth.py | src/large_m/spectral_fourth.py | large_m |
|   8 | src/r82r_small_spacings.py | src/large_m/small_spacings.py | large_m |
|   3 | src/r82s_crossing_deficit.py | src/large_m/crossing_deficit.py | large_m |
|   7 | src/r82t_second_moment_raw.py | src/large_m/second_moment_raw.py | large_m |
|   7 | src/r82u_catalan_honest.py | src/large_m/catalan_honest.py | large_m |
|   2 | src/r82v_branch_third.py | src/large_m/branch_third.py | large_m |
|   4 | src/r82w_family_second_moment.py | src/large_m/family_second_moment.py | large_m |
|  15 | src/reduced_resonance.py | src/core/reduced_resonance.py | core |
|   3 | src/resolve_1122.py | src/diagnostics/resolve_1122.py | diagnostics |
|   4 | src/ring2_subgroup_kloosterman.py | src/core/ring2_subgroup_kloosterman.py | core |
|  11 | src/single_orbit_trend.py | src/diagnostics/single_orbit_trend.py | diagnostics |
|   7 | src/smoothness_check.py | src/diagnostics/smoothness_check.py | diagnostics |
|  16 | src/subgroup_kloosterman_energy.py | src/kloosterman/subgroup_kloosterman_energy.py | kloosterman |
|   2 | src/task_a_entries.py | src/diagnostics/task_a_entries.py | diagnostics |
|   2 | src/task_b_compensation.py | src/diagnostics/task_b_compensation.py | diagnostics |
|   5 | src/task_k22_anomaly.py | src/diagnostics/task_k22_anomaly.py | diagnostics |
|   4 | src/test_arithmetic_perturbation.py | src/diagnostics/test_arithmetic_perturbation.py | diagnostics |
|  20 | src/theoremB_covariance.py | src/theorems/theorem_a_covariance.py | theorems |
|  15 | src/theoremE_operator.py | src/theorems/theorem_e_operator_proof.py | theorems |
|  16 | src/theoremE_torus_repair.py | src/theorems/theorem_e_hecke_torus.py | theorems |
|  17 | src/theta_square_theorem.py | src/theorems/theorem_c_theta_square.py | theorems |
|  37 | src/verify_mean_law.py | src/diagnostics/verify_mean_law.py | diagnostics |
|   9 | src/verify_perturbation_unitary.py | src/diagnostics/verify_perturbation_unitary.py | diagnostics |
|   9 | src/verify_perturbation_wd.py | src/diagnostics/verify_perturbation_wd.py | diagnostics |

### KEEP — tools/ utilities

| refs | old path | new path |
|---|---|---|
|  12 | tools/find_small_ord_primes.jl | src/utils/find_small_ord_primes.jl |
|  91 | tools/hecke_real_centraliser.jl | src/utils/hecke_real_centraliser.jl |
|  14 | tools/linn_h3_subgroup.jl | src/utils/linn_h3_subgroup.jl |
|   4 | tools/lit_harvest.py | src/utils/lit_harvest.py |
|  22 | tools/projective_order_brute.jl | src/utils/projective_order_brute.jl |
|  14 | tools/sol6_closed_form.jl | src/utils/sol6_closed_form.jl |
|  35 | tools/subgroup_kloosterman.py | src/utils/subgroup_kloosterman.py |
|1820 | tools/ax.mjs | literature/harvest/ax.mjs |

### RETIRED (61 scripts) — move to archive/

- `tools/hecke_real_centraliser_v3..v10.jl` (8 files): VOID per LEDGER R71.6
  ("Hecke-centring collapse"); the v7-fixed is the last attempt before
  retraction. Move all to `archive/hecke_centring_failed_line/`. The plain
  `tools/hecke_real_centraliser.jl` (without version suffix) is KEPT — it's
  the canonical utility used elsewhere.
- `src/archive/runNN_*.py` (53 files): legacy R12–R66 era scripts that have
  been superseded. Move to `archive/scripts/`.

### GARBAGE (no references anywhere) — archive but tagged

These 17 files in `src/archive/` have no references at all and look unused:

```
src/archive/bgs_core.py
src/archive/run17b_maxN3_vs_k.py
src/archive/run17c_refined.py
src/archive/run18_hierarchy.py
src/archive/run30_perturb.py
src/archive/run32_audit.py
src/archive/run35_audit.py
src/archive/run41_audit.py
src/archive/run42_esd.py
src/archive/run43_parity.py
src/archive/run44_class.py
src/archive/run45_seeds.py
src/archive/run46_symmetry.py
src/archive/run46b_halfperiod.py
src/archive/run47_seedinv.py
src/archive/run48_orbitinv.py
src/archive/run48b_support.py
```

Move to `archive/scripts/` and tag in `archive/RETIRED.md` as
"unused — no LEDGER/THEORY/MANIFEST citation".

## Paper strategy — three options

The user requested "ONE final paper". Two papers currently exist:

- `paper/exact_wd_and_subgroup_moments.tex` (R71–R82, 9 theorems A..I, II) —
  the live, comprehensive paper.
- `paper/resonance_laws_catmaps.tex` (R12–R20, resonance-laws tail) — legacy,
  largely superseded by R71.5 retraction of T20 and by the run-12 retraction.

**α. Drop the legacy, single paper only.**
- `paper/exact_wd_and_subgroup_moments.{tex,pdf,log}` stays.
- `paper/resonance_laws_catmaps.{tex,pdf,log}` → `archive/papers/`.
- Edit `paper/exact_wd_and_subgroup_moments.tex` section "Other corrections"
  to remove the companion-paper reference.
- Single final paper.

**β. Single paper + short resonance summary section.** ← user's stated
preference (option "все вместе" + "одна красивая очень подробная академическая статья").
- `paper/exact_wd_and_subgroup_moments.{tex,pdf,log}` stays.
- Add ONE short section (4 paragraphs) titled "Companion result: resonance
  laws (R12–R20)" summarising the resonance-laws line, citing the archived
  preprint `archive/papers/resonance_laws_catmaps.tex`.
- `paper/resonance_laws_catmaps.{tex,pdf,log}` → `archive/papers/`.
- Final paper remains ONE.

**γ. Two papers, both live.**
- `paper/exact_wd_and_subgroup_moments.tex` → `paper/paper-I-exact-wd.tex`.
- `paper/resonance_laws_catmaps.tex` → `paper/paper-II-resonance-laws.tex`.
- Rename all section-tex files accordingly.
- `README.md` opens with: "Paper I (R71–R82): ...; Paper II (R12–R20): ...".
- Both compile via tectonic.

## Rebrand scope — three options

**R1. Strong rebrand** (recommended).
- `src/` split into 9 thematic subfolders per the table above.
- `artifacts/` split into `theorems/`, `kloosterman/`, `shape_automaton/`,
  `large_m/`, `diagnostics/`, `julia_logs/`, `legacy_runs/`.
- All file:line references in LEDGER/THEORY/MANIFEST/IDEAS/AGENTS/README
  updated. ~30 lines in MANIFEST + ~40 lines in LEDGER.md + ~20 lines in
  THEORY.md + ~10 lines in README.md.
- All scripts renamed. Total ops: ~250 (rename + reference-update).

**R2. Soft rebrand.**
- `src/` split into 9 subfolders.
- `artifacts/` left as-is (r71..r82 subfolders are MANIFEST ground truth).
- `tools/` → `src/utils/`.
- Update only MANIFEST.md cross-references in scripts.
- ~50 ops total.

**R3. Minimal.**
- Move retired to `archive/` only.
- Don't rename `src/` scripts.
- ~30 ops total.

## Execution order (atomic steps, each reversible)

1. **mkdir**: create new folder skeleton (`src/core/`, `src/theorems/`,
   `src/kloosterman/`, `src/shape_automaton/`, `src/large_m/`,
   `src/diagnostics/`, `src/utils/`, `archive/scripts/`,
   `archive/papers/`, `archive/hecke_centring_failed_line/`,
   `archive/kernel_failures/`, `archive/portable_shell/`,
   `archive/ring_attacks/`, `artifacts/theorems/`, etc.).
2. **Move retired scripts**: `src/archive/*` and
   `tools/hecke_real_centraliser_v3..v10.jl` → `archive/`.
3. **Move retired papers**: `paper/resonance_laws_catmaps.{tex,pdf,log}`,
   `paper/twisted_lemma_clean.tex` → `archive/papers/`.
4. **Move portable shell**: `_archive/run70_portable_shell/*` →
   `archive/portable_shell/`.
5. **Move ring attacks**: `artifacts/ring1_2/`, `artifacts/ring2/`,
   `artifacts/ring3/`, `artifacts/frontier/`, `artifacts/retracted/`,
   `artifacts/retracted_run1/` → `archive/ring_attacks/`.
6. **Move Julia logs**: `artifacts/julia/` → `artifacts/julia_logs/`
   (or `archive/julia_logs/` for v3..v10 logs).
7. **Move legacy artifacts**: top-level `artifacts/*.json` (run-era) →
   `artifacts/legacy_runs/` (with `RETIRED.md`).
8. **Move R71..R74 artifacts**: `artifacts/r71/`, `r72/`, `r73/`, `r74/`
   → split between `artifacts/theorems/` (r71..r73) and
   `artifacts/diagnostics/` (r74 ensemble).
9. **Move R75..R82 artifacts**: `artifacts/r75/`, `r76/`, `r78/`, `r80/`
   → `artifacts/shape_automaton/`; `artifacts/r81/`, `r82/` →
   `artifacts/large_m/`.
10. **Rename paper section files**: `paper/r80_section.tex` →
    `paper/section_r80.tex`, etc.
11. **Rename paper patch scripts**: `paper/patch_r80.py` →
    `paper/patch_paper_r80.py`, etc.
12. **Rename `src/` scripts** per the KEEP table above.
13. **Rename `tools/` utilities** per the second KEEP table above.
14. **Update all references** in LEDGER.md, THEORY.md, ROADMAP.md,
    IDEAS.md, AGENTS.md, README.md, artifacts/MANIFEST.md,
    paper/exact_wd_and_subgroup_moments.tex (the companion-paper ref if α/β),
    paper/patch_paper_*.py (path strings inside), src/maintenance/*.py.
15. **Write archive/RETIRED.md**: manifest of all retired files with reasons.
16. **Compile-check**: if LaTeX engine available, run tectonic and
    grep for "undefined" in the kept log (R82.7 lesson).
17. **Rewrite README.md** with new layout and reproduction commands.

## Compile-check (R82.7 lesson)

After step 14, if `tools/bin/tectonic.exe` works, run:

```
cd paper
tools/bin/tectonic.exe -X compile exact_wd_and_subgroup_moments.tex
grep -i "undefined\|warning\|error" exact_wd_and_subgroup_moments.log
```

The grep must return zero matches. If it doesn't, fix before declaring done.

## What is NOT touched (content)

- `THEORY.md`, `LEDGER.md`, `ROADMAP.md`, `IDEAS.md` content — append-only truth.
  Only internal `src/X.py` style references are rewritten.
- `paper/exact_wd_and_subgroup_moments.{tex,pdf,log}` content.
- `formal/Bgs/`, `formal/Bgs.lean`, `formal/lakefile.toml`,
  `formal/lean-toolchain` — Lean project.
- `tools/bin/tectonic.exe` — compile engine.
- `literature/` — harvested sources (kel08, kow24, kr05, kurl07, osv,
  pdf/{gh11,katz_kr}, txt/{gh11,katz_kr}).
- `drafts/` — working notes (hecke_symmetrization_test.md, tail_bound_*).
- `src/maintenance/*.py` content — referenced from paper; paths may be
  updated, but the patches themselves don't change.

## Confirmation requested from user

Please confirm:
1. **Paper strategy**: α / β / γ.
2. **Rebrand scope**: R1 / R2 / R3.

Without explicit confirmation, NO `mv`/`rm` will be performed.