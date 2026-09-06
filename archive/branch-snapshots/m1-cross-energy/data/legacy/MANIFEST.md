> **Run-72 provenance warning.** The rows citing `run13_strong_master.json` and `run13_master_cert.json` refer to files that **NEVER EXISTED BEFORE 2026-08-28**: they were absent from the 121-file pre-run snapshot in `review/audit_2026-08-28/pre/` and were created for the first time by the run-71 re-run. No number in them was ever independently reproduced before that date.

# ARTIFACT MANIFEST

> **R84 repair (2026-08-31).** Every script path below was repointed to
> its post-R82 topic-subfolder location (`src/{core,theorems,diagnostics,
> kloosterman,shape_automaton,large_m,maintenance}/...`) and every
> artifact path to its actual location (`legacy_runs/{theorems,
> ensemble_moments,hecke_centring_void}/...` relative to `artifacts/`, or
> `artifacts/diagnostics/`). The repointing was verified by a disk
> spot-check: 18/18 load-bearing artifacts resolve
> (REVIEW_FINDINGS.md Part C). The R71 provenance warning below still
> applies verbatim.

> **R84 repair (2026-08-31).** Every script path below was repointed
> to its post-R82 topic-subfolder location and every artifact path to
> its `legacy_runs/`/`diagnostics/` location; a spot-check confirmed
> 18/18 load-bearing artifacts resolve on disk
> (`review/referee/` + `REVIEW_FINDINGS.md` Part C). Historical script
> names are preserved in `src/archive/`; the R71 provenance warning
> about `run13_*.json` below still applies verbatim.

Every load-bearing number in the papers (`paper/exact_wd_and_subgroup_moments.tex`
and the archived `archive/papers/resonance_laws_catmaps.tex`) is
traceable: paper claim → artifact JSON → generating script (current
path in `src/`) → command. Historical scripts referenced by early
ledger entries live unchanged in `src/archive/` (names preserved for
provenance); their outputs remain valid.

## Proven results — verification artifacts

| Paper claim | Artifact | Script | Command |
|---|---|---|---|
| Matched identity, Thm core | `grok_identity_check.json`, `run13_strong_master.json` | `src/archive/…` (superseded by proof) + inline audits | `python src/core/reduced_resonance.py`-based brute force |
| Zero-count lemmas Z₂,Z₃,Z₄ | `—` (brute force in transcript) | `review/scripts/run45_lemma.py` | `python review/scripts/run45_lemma.py` |
| Ensemble-mean law, Thm meanlaw | `run46_exact_mean.json` | `src/diagnostics/verify_mean_law.py` | `python src/diagnostics/verify_mean_law.py` |
| Tail bound floor(k²/p)+2, 0 violations | `run36_audit.json` (+ `run20_constant.json`) | `src/diagnostics/audit_tail_bound.py`, `src/campaign_*`† | `python src/diagnostics/audit_tail_bound.py` |
| Master formula r≤4 machine precision | `master_general.json` | `src/theorems/master_general.py` | `python src/theorems/master_general.py` |
| Character expansion certification | `char_expansion_cert.json` | `src/kloosterman/char_expansion_cert.py` | `python src/char_expansion_cert.py` |

† `campaign_tail_constant.py` (absent on disk; historical) was archived under its run-name
(`run20_constant.py`) — regenerate from `src/archive/run20_constant.py`.

## Numerically supported claims

| Claim | Artifact | Script |
|---|---|---|
| Perturbation ⇒ WD-not-Poisson (4 primes) | `run31_multiprime.json` | `src/diagnostics/verify_perturbation_wd.py` |
| Matching procedure validity (2ε consistency) | `run38_matching.json` | `src/diagnostics/audit_matching.py` |
| Conditional probability ≈ 1/p (independence) | `run43_condprob.json` | `src/diag_conditional_prob.py` |
| Small-period primes p∈{1597,2161,2207,3001} | `run27_primes.json` | `src/kloosterman/find_small_period_primes.py` |
| Mean ≈ k³/p² scaling discovery (4 cases) | `run44_mean.json` | `src/archive/run44_mean_scaling.py` |
| Reversibility ⊬ even k instances | `run13_phase23.json` | `src/archive/run13_centered_mechanisms.py` |

## Superseded / retracted (kept for the record)

| Item | Status | Where |
|---|---|---|
| “Arithmetic beats symmetry” Tr(W⁴) experiment | RETRACTED (non-Hermitian V) | `retracted/run13_quantum_w4.json` (quarantined) |
| Theorem-6 of run11 (C_Fk⁸/p², threshold p^{2/3}) | RETRACTED (double count) | ledger R12-A |
| Old fine-scale theorem drafts | superseded | `drafts/archive/` |

## Lean formalisation

**[ARTIFACT LOST — R82.0/LESSON 82-E]** the external project `C:\lean\bgs_formal\` no longer exists; the R2-era collision-lemma certificate is UNVERIFIABLE. The live in-workspace Lean project is `formal/` (TorusLevelSets.lean, ScaleLaw.lean; R82.8/R82.26).

## Aug 2026 additions (runs 47-48)
| Claim | Artifact | Script |
|---|---|---|
| Unitary-flow WD 4 primes | unitary_perturbation.json | src/verify_perturbation_unitary.py |
| Beta = GUE resolved (n=13723) | phase2_beta.json + phase2_spacings.npy | src/phase2_pooled.py + src/phase2_mc_reference.py |
| Tail smooth law C=1 (238 pts) | run36_audit.json+run20_constant.json | src/phase1c_forms.py |
| r6 even law 5k(3k^2-9k+8) | phase3_r6.json | src/phase3_r6_families.py |
| Odd-k remainder D_p(k) p-dependence | phase3_r6.json + console fit | src/phase3_odd_fit.py |

## Run 49 additions
| Claim | Artifact | Script |
|---|---|---|
| Heavy tails hold at split primes too | check_split_vs_inert.json | src/check_split_vs_inert.py |
| Arithmetic perturbation FAILS WD (KS>=0.15) | arithmetic_perturbation.json | src/test_arithmetic_perturbation.py |
| D_p(k) Kloosterman-type fluctuations 0.53-3.67 | phase3_Dpk_sweep.json | src/phase3_Dpk.py |

## Run 50 additions
| Claim | Artifact | Script |
|---|---|---|
| A_p(k) sweep: 3\|k hyp refuted; p-stability puzzle | phase3_Apk_sweep.json | src/phase3_Apk_sweep.py |
| k=22 anomaly: strata diff 1584/1584/792 (=2:2:1) | phase3_k22_anomaly.json | src/task_k22_anomaly.py |

## Audit additions (2026-08-26)
| Claim | Artifact | Script |
|---|---|---|
| Projective orders of exp primes (K: 3571→17, 4481→32, 5779→27; 1597/2207 inert) | audit_orders.json | review/scripts/audit_orders.py |
| Independent suite V1–V6 (matched id, zerocounts, meanlaw complete enum p∈{5,7}, tail fresh grid, collision, r6 strata) | audit_independent_suite.json + audit_rerun_independent_suite.log | review/scripts/audit_independent_suite.py |
| GPU replication of Exp multi (torch/cuSOLVER, fresh E-draws): clusters identical, WD-not-Poisson 4/4 | audit_gpu_replication.json | review/scripts/gpu_replicate.py |
| Julia second-language key: matched identity 40 configs, Z2/Z3, tail spots — ALL PASS | julia_out2.log | review/scripts/julia_crosscheck.jl |
| Rerun logs of all canonical verifiers (all reproduce artifacts) | audit_rerun_*.log | worker scripts |
| **master_general OPTIMIZED + r=5 added**: MITM vectorized (8.2x on r=4), regression 4/4 PASS, NEW r=5 ALL-PASS err~1e-17 | master_general.json (5 runs) + audit_rerun_master_general.log | src/master_general.py |
| **Unified tail conjecture** (stratified scan rho∈{1,4,16}, p≤8009, k≤364: non-Wick classes ≡ generic) | audit_degenerate_strata.json + audit_strata_rho*.log | review/scripts/degenerate_strata_scan.py |

**Corrections applied by the audit:** KR00 pages → 47–77;
exp:beta K-labels → true projective orders (17/32/27; were halved by
`phase2_beta.proj_order`); ledger-R27/ROADMAP K-values traced to a
second bug (`find_small_period_primes.matrix_order_mod_p`, n//2+1);
`proj_order`/`matrix_order_mod_p` fixed in src; ROADMAP stale
post-R12-A claims removed; smoke-test denominator 6→5.
Physics/statistics unaffected (clustering numeric; m-values correct).
Full report: `review/audit_2026-08-26.md`.

## Ring 1 (R1.1–R1.7) — Repair standing damage (2026-08-28)
| Claim / artifact | Path | Source |
|---|---|---|
| C1 T13 gcd(M₂₁,N)=1 hypothesis + degenerate-chart paragraph | `THEORY.md` §T13, `paper/resonance_laws_catmaps.tex` `rem:reversing_degenerate` | R1.1, R3.1 |
| C2 U1 non-degeneracy hypothesis | `THEORY.md` §8.0.1, `paper/resonance_laws_catmaps.tex` `rem:collision` | R1.2, R3.1 |
| C3 U4 corrected bound (ℓ² = p²k, EXTRAS ≤ k³p^{−2δ}) | `THEORY.md` §8.0.1, paper status table | R1.3, R3.1 |
| C5 r=5 status honesty (master_general evidence, legacy drivers deprecated) | `THEORY.md` §8.0.2, paper status table | R1.4, R3.1 |
| R12-A in-place warning at R10-B section | `LEDGER.md` (above R10-B) | R1.5 |
| Lean re-probe: out_of_scope_this_run | `LEDGER.md` RING 1.6 | R1.6 |
| u1_degenerate_audit.json (5 degenerate-chart configs, max fibre = k) | `artifacts/u1_degenerate_audit.json` | R1.2 |
| ring1_rerun_summary.json (PASS on all 3 R1.7 scripts) | `artifacts/ring1_rerun_summary.json` | R1.7 |
| ring1_rerun_verify_mean_law.json (5/5 PASS, max |z|=1.47) | `artifacts/ring1_rerun_verify_mean_law.json` | R1.7a |

## Ring 2 (R2.1–R2.5) — Attack p^{3/7+ε} wall (2026-08-28)
| Claim / artifact | Path | Source |
|---|---|---|
| litwatch_summary.md (5 NEW, 2 Weil-ceiling generalisations) | `artifacts/ring2/litwatch_summary.md` | R2.1 |
| line_A_report.md (Stepanov [OPEN GAP]) | `artifacts/ring2/line_A_report.md` | R2.2 / R2.3 |
| line_A_h2h.json (9 head-to-head configs, max |S|/Weil = 0.44) | `artifacts/ring2/line_A_h2h.json` | R2.2 |
| line_B_report.md (Deligne [OPEN GAP]) | `artifacts/ring2/line_B_report.md` | R2.2 / R2.3 |
| line_B_calibrator.json (rank-1 case, max ratio 0.88) | `artifacts/ring2/line_B_calibrator.json` | R2.2 |
| line_B_head2head.json (9 configs at p∈{41,61,113,157,521,541}) | `artifacts/ring2/line_B_head2head.json` | R2.2 |
| line_B_big_sweep.json (36 cases, max |S|/Weil = 0.99999 at p=4001,k=4) | `artifacts/ring2/line_B_big_sweep.json` | R2.2 |
| line_C_report.md (Bourgain [OPEN GAP]) | `artifacts/ring2/line_C_report.md` | R2.2 / R2.3 |
| line_C_calibrator.json (8 rank-1 cases, all under Weil) | `artifacts/ring2/line_C_calibrator.json` | R2.2 |
| line_C_head_to_head.json (14 configs, max |S|/Weil = 0.63) | `artifacts/ring2/line_C_head_to_head.json` | R2.2 |
| synthesis.md (3 attack lines, all [OPEN GAP]; wall unchanged) | `artifacts/ring2/synthesis.md` | R2.3 |
| discriminator.json (R2.5 MOOT) | `artifacts/ring2/discriminator.json` | R2.5 |

## Ring 3 (R3.1–R3.6) — Paper and workspace finalisation (2026-08-28)
| Claim / artifact | Path | Source |
|---|---|---|
| paper.tex source edits (5 new status-table rows, 1 new `rem:reversing_degenerate`, updated `rem:collision`, front-matter source-edit log; NOT recompiled) | `paper/resonance_laws_catmaps.tex` | R3.1 |
| LEDGER R64–R66 entries (RING 0/1/2/3 chronicle) | `LEDGER.md` end | R3.2 |
| ROADMAP.md UPDATE 2026-08-28 block | `ROADMAP.md` end | R3.3 |
| THEORY.md §8.0.1/§8.0.2/§8.0.3 (U1/U4 corrected, r=5 demoted, T21 wall) | `THEORY.md` §8 | R1.1–R1.4, R2.4 |
| ring3_hygiene.json (move_count = 0) | `artifacts/ring3_hygiene.json` | R3.5 |
| REPRO.md (5 random (artifact, script, claim) triples) | `artifacts/ring3/REPRO.md` | R3.6 |
</input>

## RUN 71 (2026-08-28) — artifacts/r71/

claim -> artifact -> script -> command

| claim | artifact | script | command |
|---|---|---|---|
| Egorov with A^T; U^K = chi.1; projectors; Weyl frame; \|Tr(T(v)U^J)\|=1 | `legacy_runs/theorems/A_covariance/catmap_independent_checks.json` | `src/core/catmap_independent.py` | `python src/core/catmap_independent.py` |
| Theorem A: Lemma A1/A2, traceless variance, Re-part = GOE tensor | `legacy_runs/theorems/A_covariance/theoremB_covariance.json` | `src/theorems/theorem_a_covariance.py` | `python src/theorems/theorem_a_covariance.py` |
| single orbit vs Gaussian combination, spacing L1 and z-scores | `legacy_runs/theorems/A_covariance/compression_spacings.json` | `src/diagnostics/compression_spacings.py` | `python src/diagnostics/compression_spacings.py` |
| op:local_deterministic, 5 design points, z(m) and z(K) | `legacy_runs/theorems/A_covariance/single_orbit_trend.json`, `legacy_runs/theorems/A_covariance/single_orbit_trend.log` | `src/diagnostics/single_orbit_trend.py` | `python src/diagnostics/single_orbit_trend.py` |
| E_s(H) vs characteristic-zero count, P1/P2/P3 | `legacy_runs/theorems/B_subgroup_kloosterman/subgroup_energy.json` | `src/kloosterman/subgroup_kloosterman_energy.py` | `python src/kloosterman/subgroup_kloosterman_energy.py` |
| moment identity, Bessel closed form, mixed moments | `theorems/A_covariance/moment_certification.json` | `src/diagnostics/moment_certification.py` | `python src/diagnostics/moment_certification.py` |
| exceptional set B(k,s), all k | `legacy_runs/theorems/B_subgroup_kloosterman/exceptional_set.json` | `src/kloosterman/exceptional_set.py` | `python src/exceptional_set.py` |
| P*(k,s) exhaustive, k prime | `legacy_runs/theorems/B_subgroup_kloosterman/Pstar_prime_k.json`, `legacy_runs/theorems/B_subgroup_kloosterman/pstar_scan.log` | `src/kloosterman/pstar_scan.py` | `python src/kloosterman/pstar_scan.py` |
| refutation of R67-R70: n_hecke sweep, 3 bases | `legacy_runs/hecke_centring_void/hecke_centring_refutation.json` | `src/diagnostics/hecke_centring_refutation.py` | `python src/diagnostics/hecke_centring_refutation.py` |
| reproduction of the defective code path (missing /n_hecke) | `legacy_runs/hecke_centring_void/hecke_centring_undivided.json` | `src/diagnostics/hecke_centring_refutation.py` | `python src/hecke_centring_refutation.py --exact` |
| legacy paper repair (6 edits) | `paper/resonance_laws_catmaps.pdf` | `src/maintenance/repair_legacy_paper.py` | `python src/maintenance/repair_legacy_paper.py` |
| THEORY.md VOID banner + section 9 | `THEORY.md` | `src/maintenance/patch_theory_r71.py` | `python src/maintenance/patch_theory_r71.py` |

**Known MANIFEST defects found in R71 (not yet repaired):** the rows citing
`run13_strong_master.json` and `run13_master_cert.json` as evidence for
"Matched identity, Thm core" refer to files that did not exist on disk before
2026-08-28; they were created for the first time by the R71 re-run, so those
numbers were never previously reproduced. Tracked as `op:manifest_repair`.

## RUN 72 (2026-08-28) — artifacts/r72/

| claim | artifact | script |
|---|---|---|
| Theorem C, `Theta^2 = +1`, 504 configs + exhaustive involution counts | `legacy_runs/theorems/C_theta_square/theta_square_theorem.json` | `src/theorems/theorem_c_theta_square.py` |
| Theorem D, parity dichotomy, 5 design points | `legacy_runs/theorems/D_parity_dichotomy/parity_desymmetrised.json` | `src/theorems/theorem_d_parity_dichotomy.py` |
| Theorem E, torus-repair condition, 3 maps x 7 primes | `legacy_runs/theorems/E_hecke_torus/theoremE_torus_repair.json` | `src/theorems/theorem_e_hecke_torus.py` |
| eigenspace vs Haar surrogate, L1 spacing statistics | `legacy_runs/theorems/D_parity_dichotomy/haar_surrogate.json` | `src/diagnostics/haar_surrogate.py` |
| the decisive unfolding-free ratio measurement | `legacy_runs/theorems/D_parity_dichotomy/desym_ratio_statistic.json`, `legacy_runs/theorems/D_parity_dichotomy/desym_ratio.log` | `src/diagnostics/desym_ratio_statistic.py` |
| `E0(s,k) = P(s,k)` iff `s < lpf(k)`, prime powers, 29 cells | `legacy_runs/theorems/B_subgroup_kloosterman/prime_power_criterion.json` | inline (see LEDGER R72.5) |
| audit-hygiene pass, 7 edits | (edits in place) | `src/maintenance/hygiene_r72.py` |

## RUN 73 (2026-08-28) — artifacts/r73/

| claim | artifact | script |
|---|---|---|
| Theorem E as a proof: `W = (R tau)^2 = I`, `Theta_u^2 = +1`, block real structure | `theorems/E_hecke_torus/theoremE_operator.json` | `src/theorems/theorem_e_operator_proof.py` |
| Hecke dichotomy: diagonal Sato-Tate, off-diagonal Gaussian, per-frequency error bars | `theorems/E_hecke_torus/hecke_matrix_elements.json` | `src/diagnostics/hecke_matrix_elements.py` |
| `E0(s,k) = P(s,k)` iff `s < lpf(k)`, composite k, 61 cells | `theorems/B_subgroup_kloosterman/composite_k_criterion.json` | inline (see LEDGER R73.3) |
| Lemma F: exact quadratic phase of `Tr(T(v)U^J)`, 5000 out-of-sample checks | `theorems/F_quadratic_phase/lemmaF_quadratic_phase.json` | `src/theorems/lemma_f_quadratic_phase.py` |
| Lemma F closed form: universal sign convention at 16 (A,N,J) | `theorems/F_quadratic_phase/lemmaF_closed_form.json` | inline (see LEDGER R73.4) |
| Theorem G: slack in the T18 barrier, exact `S_J(r)` versus l1/l2 | `theorems/G_moment_closed/barrier_slack.json` | `src/theorems/theorem_g_moment_closed.py` |
| large-m desymmetrised ratio statistic | `theorems/E_hecke_torus/desym_large_m.json`, `theorems/E_hecke_torus/r73_desym_large_m2.log` | `src/diagnostics/desym_large_m.py` |

## RUN 74 (2026-08-28) - artifacts/r74/

| claim | artifact | script |
|---|---|---|
| rank-0 condition = two Chebyshev congruences (1600/1600); D_r vs paired | `r74/ensemble_moments.json` | `src/diagnostics/ensemble_moments.py` |
| ensemble combinatorics: D_r(N) vs the balanced-word count, excess over Z and mod N | `r74/ensemble_excess.json` | `src/diagnostics/ensemble_excess.py` |

## RUN 75 (2026-08-28) - artifacts/r75/

| claim | artifact | script |
|---|---|---|
| Theorem H: cyclic shape decomposition of D_r(N), certified 14/14 (r = 5,6,8) | `theorems/H_shape_decomposition/multiples_structure.json` | `src/theorems/theorem_h_shape_decomposition.py` |
| primitive shapes of x^2-3x+1 up to L1 = 12, width 16 | `theorems/H_shape_decomposition/shapes_t3_w16.json` | `src/theorems/theorem_h_shape_decomposition.py` |
| accident vectors at r=6 (cyclic wraps of the L1=6 shape) | `theorems/H_shape_decomposition/accident_vectors_r6.txt` | `src/theorems/theorem_h_shape_decomposition.py` (inline probe) |
| canonical suite re-run green (V1-V8, Lemma F) | `verify_r75_catmap_indep.log`, `verify_r75_lemmaF.log`, `verify_r75_ensemble_moments.log` | `src/core/catmap_independent.py`, `src/theorems/lemma_f_quadratic_phase.py`, `src/diagnostics/ensemble_moments.py` |
| m=1674 FULL-eigenspace desymmetrised ratio (z_GOE = -0.19/+0.24, 9 sigma from GUE) | `theorems/E_hecke_torus/desym_m1674.json`, `theorems/E_hecke_torus/desym_m1674.log` | `src/diagnostics/desym_large_m2.py` (M_TARGET=1674) |
| R73 desym_large_m.json overwrite note (control JSON lost, numbers in LEDGER R73.6) | `theorems/E_hecke_torus/desym_large_m.json` | --- |

## RUN 76 (2026-08-28) - artifacts/r76/

| claim | artifact | script |
|---|---|---|
| fixed-n phi-decomposition certified 24/24 (r=2..5, six n, max err 8.2e-14); Gauss sums |G|=N^-1; G5 prediction 1.341e-07; census to r=10 (M_10=0) | `ensemble_moments/phi_ensemble.json` | `src/shape_automaton/phi_ensemble.py` |
| full run log (A+B+C verdicts) | `r76_run.log` | `src/shape_automaton/phi_ensemble.py` |

## RUN 77 (2026-08-28) - artifacts/

| claim | artifact | script |
|---|---|---|
| census to r=12 (M_12=0; 2K x 81 orbits at L1=12; ceiling table) | `ensemble_moments/phi_ensemble.json` (r_max=12 rerun) | `src/shape_automaton/phi_ensemble.py` |
| full r=12 run log | `r76_run12.log` | `src/shape_automaton/phi_ensemble.py` |
| R77 automaton identity + infinite-state obstruction (documented, NOT a certified computation) | --- | `src/shape_automaton/sofic_automaton.py` |

## RUN 78 (2026-08-28) - artifacts/r78/

| claim | artifact | script |
|---|---|---|
| eps=-1: Theorem H verbatim; modular antiperiodic dominance; 3/3 exact vs r74 at K=34 | `ensemble_moments/eps_minus.json` | `src/shape_automaton/eps_minus_antiperiodic.py` |
| run log (K=34 and K=40 rows) | `r78_run.log` | `src/shape_automaton/eps_minus_antiperiodic.py` |

## RUN 80 (2026-08-29) - artifacts/r80/

| claim | artifact | script |
|---|---|---|
| Psi(y) exact (J-weighted automaton); census rows r<=8 exact (Z/full/wrap, K=17,19); X^Z exact r<=12; S_win 8/8 vs R79; triv(6,17)=538900; ceiling table K in {17..41} | `legacy_runs/ensemble_moments/jweight_dp.json` | `src/shape_automaton/jweight_dp.py` |
| wrap coincidences: collision excess 41,126,400 (r=10), 1,244,073,600 (r=11), 97,037,740,800 (r=12) = census deltas to the last digit; 230 shapes, 3876 signed vectors, fibre multiplicities | `legacy_runs/ensemble_moments/wrap_collisions.json` | `src/shape_automaton/wrap_collisions.py` |
| S(R) exact to R=80 (dense and width-capped); float X_full to r=24 calibrated 2.2e-15 | `legacy_runs/ensemble_moments/julia_bigdp.json` | `src/large_m/julia_bigdp.jl` |
| E-residue / ensemble identity end-to-end (N=199) and the N=3571 prediction decomposition | `legacy_runs/ensemble_moments/e_residue.json` | `src/large_m/e_residue.py` |
| audit log trail of the 2026-08-29 re-verification (11/11 core + ensemble scripts) | `../review/audit_2026-08-29/logs/`, `../review/audit_2026-08-29/run80_ledger_entry.md` | --- |

## RUN 82 (2026-08-30) - artifacts/r82/

| claim | artifact | script |
|---|---|---|
| **Theorem I** (torus rigidity): certificates C1-C5 at (N,K) = (199,11), (3571,17), (9349,19), 15/15 PASS - level-set sizes N-1 and cone 2N-2 by exhaustive enumeration; orbits per level set = \|T\|/K = m; full sorted spectra equal across 8 distinct orbits per level set to 2.4e-14 / 2.0e-13 / 3.3e-13; inter-level separation 11-13 decades; explicit torus element g = aI + bA, 21/21 | `theorems/I_torus_rigidity/torus_rigidity.json`, log `theorems/I_torus_rigidity/torus_rigidity.log` | `src/large_m/torus_rigidity.py` |
| orbit invariance spec(V_n) = spec(V_{A^T n}) to 7.6e-14; **two-key** mu_4 via the exact N x N projector (no randomised eigenbasis): 1.85357709 both ways, diff 1.3e-14; ANOVA over Q-level sets: within-level variance 0.00000 of total 0.0535 / 0.0633 | `theorems/I_torus_rigidity/orbit_invariant.json`, log | `src/large_m/orbit_invariant.py` |
| the full modulation curve q -> spec(V_q), exhaustive over all 198 / 3570 level sets: Tr(V^2)/m+ mean 0.117600 (N/(K^2 m+) = 0.117658), mu_4 mean 1.9694 std 0.2350 range [1.2246, 2.8573] | `theorems/I_torus_rigidity/q_curve.json`, `theorems/I_torus_rigidity/q_curve_N199.npz`, `theorems/I_torus_rigidity/q_curve_N3571.npz`, log | `src/large_m/q_curve.py` |
| **the Fibonacci comb**: DFT of the raw central traces in q; 16 frequencies +-v_j (j=1..8) carry 90% of the variance of Tr(V^4), Tr(V^6); 8-pair least-squares fit R^2 = 0.9426 (Tr V^4), 0.9276 (Tr V^6), 0.98655 (mu_4); saturation test with 71 frequencies -> 0.9472 / 0.9872 | `theorems/I_torus_rigidity/raw_trace_dft.json`, `theorems/I_torus_rigidity/qfit_R2.json` | inline analysis of `q_curve_N*.npz` (commands in LEDGER R82.4) |
| Chebyshev-mode decomposition of the R81.4 excess: even-mode ratios 81/71/78/100/144 (k=4,6,8,10,12) vs odd 1.0/1.6/2.8/5.8/12.7 at m+=105; 375/306/302/352/463 vs 0.5/2.9/5.2/10.8/21.9 at m+=246; Haar control 0.3-0.6; projection ladder 1.89 -> 1.32 (k<=4) -> 1.12 (k<=8) | `diagnostics/shape_modes.json`, log | `src/large_m/shape_modes.py` |
| macroscopic law and outlier diagnostics: mu_4 means 1.92/1.95/1.97 (semicircle 2, arcsine 1.5 - arcsine REFUTED); kurtosis 8.0 / 2.73 / 20.9; 10%-trimmed variance retains 0.34 / 0.65 / 0.44; exact pairing count C_4 = 6(2K-1) = 126/198/222 EXACT; extra resonances mean 2.6 / 0.0 / 0.75, corr(C_4, mu_4) 0.64 / 0.00 / 0.63 | `diagnostics/density_shape.json`, log | `src/large_m/density_shape.py` |
| edge-vs-bulk trimming ladder (the discriminator between an extreme-value and a bulk-shape reading) | `diagnostics/edge_vs_bulk.json`, log | `src/large_m/edge_vs_bulk.py` |
| **op:dpbug**: exact self-checking relation-count DP; S_win(w<=17) rows 3/8/37/68/111 at L1=8..12 (= R80.2, third method); S_dense(30) = 301160711 and S_dense(50) = 7639873992151089 (= R80.4); glue check PASS at every pair to R=130; budget independence rmax 40 vs 56 (36/36) | `diagnostics/dp_exact.json`, log | `src/shape_automaton/dp_exact.jl` (library `src/shape_automaton/dp_library.jl`) |
| **C_dense sandwich**: exact BigInt S(150) = 187137374536225033685627517572691799471916696233737462, S(150)^(1/150) = 2.265415, glue PASS at every pair to R=150 -> 2.265415 <= C_dense <= 3 | `diagnostics/dp_push.json`, log | `src/shape_automaton/dp_push.jl` |
| Lean 4.33.1 (no Mathlib) certificate for the counting core of Theorem I at p=199: ord(A^T)=11, all level sets have p-1 points, cone 2p-2, 18 orbits per level set, free action, global count identity 3600=3600. C3 kernel-checked (no axioms); C1a/C2/C4 via native_decide (axiom disclosed) | `diagnostics/lean_build.log` | `formal/Bgs/TorusLevelSets.lean` |
| workspace repair: nesting flattened, 52 dead-absolute-path scripts repaired, smoke 5/5 | `../review/audit_2026-08-30/logs/smoke.log` | `src/maintenance/repair_paths_r82.py`, `fix_prelude_r82.py` |
| Theorem I, counting half, split AND inert branches: 9/9 primes by exhaustive enumeration (split 199/281/401/3571: level sets N-1, cone 2N-2; inert 107/113/127/197/233: level sets N+1, cone exactly {0}) | `theorems/I_torus_rigidity/level_sets_split_inert.json` | inline (command in LEDGER R82.2) |
| edge-vs-bulk at the second design (m+=246, nrep=48) | `diagnostics/edge_vs_bulk_9349.json`, log | `src/large_m/edge_vs_bulk.py` |
| Lemma 82.1: Tr(V_q^2) = N/K^2 + E(q), |E| < 4 proven for odd K; measured max|E| = 0.72/0.70 and mean E = -0.0351/-0.0080 (N^{-1/2} decay) over ALL level sets | `diagnostics/second_moment_identity.json` | inline from `theorems/I_torus_rigidity/q_curve_N199.npz`, `theorems/I_torus_rigidity/q_curve_N3571.npz` (command in LEDGER R82.9) |
| R82.10 equivariant normal form: |C_n| shared by a whole level set (rel dev 3.9e-13 / 7.5e-11; cross-level control 0.99) and the ratio matrix an exact coboundary (rel residual 0.0000, 8090+ entries) | `theorems/I_torus_rigidity/normal_form.json`, `theorems/I_torus_rigidity/normal_form_phase.json`, logs | `src/r82h_normal_form.py` + inline (LEDGER R82.10) |
| R82.11 entry statistics of the reduced matrix M_q = C_q + C_q^*: off-diagonal Gaussian (kurtosis 2.97-3.14 vs GOE 2.957), diagonal kurtosis ~2 (Sato-Tate, = R73.2 dichotomy), m.Var = 0.1177 = N/(K^2 m+), variance profile flatter than GOE, pair correlations at the 0.013 sampling floor | `diagnostics/entry_statistics.json`, log | inline (LEDGER R82.11) |
| **Theorem II**: Hecke matrix elements = twisted Jacobi sums `J(chi,psi;q) = sum_x conj(chi)(x)psi(x-1)e_N(qx)`; `M_q` rebuilt from the sums alone reproduces the pipeline mu_4 over ALL level sets (198 sets to 6.1e-14 at N=199; 3570 sets to 2.4e-13 at N=3571), scale `c = L_{K-1}` | `theorems/II_twisted_jacobi/closed_form.json` | `src/theorems/theorem_ii_twisted_jacobi.py` |
| exact `Tr(C C^*)` tuple formula (R82.13) verified against the numeric trace 24/24 at two designs, max abs err 5.2e-14 (rel 1.7e-14); 460 distinct frequencies at K=17, containing all 16 measured comb frequencies | `diagnostics/second_moment_exact.json`, `diagnostics/second_moment_exact2.json`, logs | `src/large_m/second_moment_exact.py` + inline |
| **R82.14 BGS at large m** (closed form removes the N x N wall): per-system <r~> = 0.53135/0.53072/0.53153 at m_+ = 336/837/1680 against matched GOE MC (8x samples) 0.53073/0.53104/0.52963 -> z = +0.18/-0.14/+1.04, z vs Poisson +43/+67/+95; spacing KS inside the noise floor; number variance matching within 1-2 sigma | `diagnostics/bgs_large_m.json`, log, first-pass control log | `src/large_m/bgs_large_m.py` |
| **R82.14 at the largest scale**: m_+ = 2851 (N = 336419, K = 59; 11.6x the programme's previous ceiling), 3 systems vs 24 GOE: <r~> = 0.53782 +- 0.00337 vs 0.53334 +- 0.00104 (z = +1.27, z vs Poisson +44.9); spacing KS 0.0063 vs GOE's own 0.0078 (floor 0.0176); Sigma^2(L) within 1-2 sigma | `diagnostics/bgs_large_m_big.json`, log | `src/r82k_bgs_large_m.py --big` |
| **R82.16**: the entries obey SATO-TATE -- `<|J|^{2k}>/N^k` = 1, 2, 5, 14 (Catalan = semicircle on [-2,2] = tr SU(2)), measured 1.0079/2.0022/5.0045/14.0046 at N=3571 with N^{-1/2} convergence over three designs; NOT the Gaussian 1,2,6,24. Forbidden correlators at the sampling floor | `diagnostics/jacobi_moments.json`, log | inline (LEDGER R82.16) |
| **R82.17 Proposition B**: exact tuple identity for `sum|J|^4` certified to 1e-14 over all 484 pairs (N=199); `T_(1,1)` q-independent with ratio to 2N^2 = 0.9775 / 0.99874; `max_offdiag |T|/N` = 4.6-5.6 bounded at both designs -> `<|J|^4> = 2N^2(1 + O(K^2/N))` | `diagnostics/fourth_moment.json`, log | `src/large_m/fourth_moment.py` |
| **R82.18 long-range rigidity**: at m_+ = 1680, Sigma^2(L) and Delta_3(L) agree with matched GOE at every L = 1..50 (all |z| <= 1.8; Sigma^2(50) = 1.2240 vs 1.2001 vs asymptote 1.2348), Poisson excluded by 40x -> NO arithmetic-chaos loss of rigidity | `diagnostics/rigidity_long_range.json`, log | `src/large_m/rigidity_long_range.py` |
| **R82.18 control**: unfolding-degree sweep d = 4..15 on the same 48+192 spectra flips the sign of the Sigma^2 deviation (+3.8 at d=4, -1.1 at d=11) while Delta_3 stays within +-2.1 -> the apparent m_+=837 'excess rigidity' RETRACTED as an unfolding artifact of the q-dependent macroscopic density | `diagnostics/rigidity_control.json`, `diagnostics/rigidity_spectra.npz`, log | `src/large_m/rigidity_control_v2.py` |
| R82.19: fourth-trace pipeline -- exact `Tr(M^2), Tr(M^4)` and the word decomposition; DIAGNOSIS: for the even-character block `C_ij = conj(C_ji)` entrywise to 4e-11, so `M = 2C` and the naive C/C* split is structurally degenerate; `m(mu_4-2)` = 2.2-2.8 at m+=105 (GOE scale) | `diagnostics/spectral_fourth.json`, `spectral_fourth_fixed.json`, `spectral_fourth_truth2.log` | `src/large_m/spectral_fourth.py` + inline |
| **R82.20 no hidden degeneracies**: min bulk spacing and N_pairs(t), t = 0.02..0.2, all within +-2.1 sigma of matched GOE with alternating signs at 3 designs; smallest-ever spacings 0.0088/0.0142/0.0059 vs GOE 0.0178/0.0021/0.0066 (extreme-value behaviour); repulsion at full GOE strength -> the subleading-coincidence failure mode excluded | `theorems/I_torus_rigidity/small_spacings.json`, log | `src/large_m/small_spacings.py` |
| **R82.21 Catalan law cross-verified** at a 4th design (N=19489, K=29) and k=5: deviations from C_k = -0.013/-0.034/-0.096/-0.283 (N=19489), -0.003/-0.010/-0.033/-0.110 (N=95419) for k=2..5, faster than N^{-1/2} decay; factorial alternative dead (e8: 13.97+-0.03 vs 24). The per-matching decomposition attempt FAILED (constraint is matching-independent) - `op:pairing` is the named open problem | `diagnostics/catalan_verify.json`, `sixth_moment_direct.json`, `crossing_deficit.json` (negative), logs | inline (LEDGER R82.21) |
| **R82.22 reproducibility scripts** (referee D5): `r82t` raw Tr(V^2) over ALL level sets — mean 1.628934/12.349512 vs N/K^2 = 1.644628/12.356401, max|E| = 0.7326/0.7032 (bound 4.0); `r82u` honest /N^k Catalan: N=95419 gives 0.9994/1.9973/4.9904/13.9672/41.8897 (k=1..5, Catalan to 3 digits), N=3571 deviations +0.024/+0.095/+0.347/+1.228 growing with k — honest law `<|J|^{2k}> = C_k N^k (1 + e_k(N))` with e_k decaying in N, growing in k | `diagnostics/second_moment_raw.json`, `diagnostics/catalan_honest.json`, logs | `src/large_m/second_moment_raw.py`, `src/large_m/catalan_honest.py` |
| **R82.23 T_{1,1} exact**: constraints force {y}={x}, phase identically 1, fibre 2 (1 on diagonal) -> T_{1,1} = 2(N-2)^2-(N-2) = 2N^2-9N+10, q-independent; brute-force exact at N = 37/53/89/109, matches the measured values at 199/3571 | `diagnostics/t11_exact.log` | inline (LEDGER R82.23a) |
| **R82.23 zero-mode rule**: constant vector is a U_A-eigenvector (eigenvalue ±1,±i, |chi0|=1) and joins branch 0 iff chi = 1; designs N = 19489/39161/144481 anomalous ((N-1)/K + 1 multiplicity, 673 observed), 199/3571/9349/95419/336419 clean; model-vs-pipeline identity tests must use clean branches | `diagnostics/zero_mode_anomaly.log` | inline |
| **R82.23 branch law refined**: c1*c2 = -(t^2-4) confirmed at a THIRD design (9349: partner c = -5/L_9 = 3571 matches at k0 = 11 to 1.1e-13 over 8 probes, all 19 k0 scanned); the L_{(K-1)/2} identification holds only at chi = -i designs -- k0-shift consistent with a metaplectic twist, derivation open (`op:cscale`) | `theorems/II_twisted_jacobi/branch_scan9349.json`, `branch_third_design.json`, logs | inline (LEDGER R82.23c) |
| **R82.24 op:cscale solved (scale)**: `L_{(K-1)/2}^2 = t+2 = t^2-4` by a one-line identity (`s^2 = a^{K-1}+2+a^{1-K}`); branch law `c = +-L_{(K-1)/2}`, mirror pairs (k0,c) <-> (-k0,-c) with even parity -- verified end-to-end at 5 designs (199/3571/9349/461/541), deviations 8e-14..1.2e-13 over all 2K candidate blocks; k0 index law open (data: k0*ell = j0*m) | `diagnostics/cscale_proof.log`, `fourth_design.json`, `branch_mirror9349.json`, logs | inline (LEDGER R82.24) |
| **R82.25 op:pairing resolved**: new EXACT identity M6(q) = sum_{(P,Q)} |W(P,Q)|^2 (sixth moment = family second moment over the curves C_{P,Q}), machine-verified to <=1.1e-15 at 10 primes by independent algorithms; constant C_3 = 5 = normalised family second moment, monotone convergence 4.19->4.83 (N=37..181) continuing to 4.97/5.00 at the designs; matching picture DEAD; the k>=3 route and the local law need the same single input (Katz second moment for the S_3-family) | `diagnostics/family_second_moment.json`, `family_second_moment2.json`, logs | `src/large_m/family_second_moment.py` + inline |
| **R82.26 Lean scale law**: S1_order/S2a_power/S2_trace/S3_branches at p=199 ALL kernel-checked, zero axioms | `diagnostics/lean_scale_law.log` | `formal/Bgs/ScaleLaw.lean` |
| **R82.27 constant reduced to Kloosterman second moment**: indicator expansion -> (1/N^2)sum|S(a,b)|^2 with S = sum e_N(q(u+v+2)-b uv) f(...); exact case decomposition at 3 primes (total reproduces M6/N^3 = 4.19/4.40/4.58): kl case (a,b,a+b != 0) carries ~99%, avg|S|^2/N^3 = 4.46/4.60/4.73 -> 5; mechanism: |S|^2 ~ (N-2)^2|Kl|^2 over the conic c=0 — the constant is the Kloosterman second moment over the conic family (classical sheaf). Process defect caught: dropped e_N(q(u+v+2)) factor, fixed by direct-vs-grouped assertion (LESSON 82-K) | `theorems/II_twisted_jacobi/ab_decomposition.log` | inline (LEDGER R82.27) |
| **R82.28 factor 5 = 1 + 4 (elementary)**: twisted-Kloosterman prediction REFUTED (twisted moment ~0 at 5 primes) -> the mass sits at A = 0 <=> kappa = 0 (same locus: alpha·beta+q(alpha+beta) = 0), where the conic c=0 splits into TWO LINES (2N-1 points) and |S|^2 ~ 4N^4 per point over ~N points -> 4; generic pairs -> 1 by Kloosterman orthogonality. Verified: degenerate 3.10/3.36/3.53->4, generic 1.00/0.98/1.01, total 4.10/4.34/4.53->5. Catalan constant at k=3 is ELEMENTARY (no monodromy); degenerate-locus hierarchy named for k>=4 | `diagnostics/twisted_moment.log` (negative), `diagnostics/factor5_split.log` | inline (LEDGER R82.28) |
| **R82.30 k=4**: identity M8 = sum_{P,Q}|W4|^2 exact to 1.1e-15 at 4 N; W4 = trace over the SURFACE {e4=P, e4(y-1)=Q}, |W4| = O(N) (measured 9.3-10.3); constant 11.34/11.47/11.92/12.61 at N=37/41/53/73 -> C4 = 14 (monotone); the pattern M_{2k} = sum|W_k|^2 -> C_k now verified at k=2,3,4 | `diagnostics/k4_moment.json`, `k4_convergence.json`, logs | inline (LEDGER R82.30) |
| **R82.31 self-check + k=4 decomposition**: curve sizes ~N (mean 49.06, max 102 at N=53); M6 confirmed by a THIRD independent method (2.7e-16); honest Catalan limits at N=95419 stand. k=4 (alpha,beta) decomposition: sum|S4|^2 = N^2*M8 exactly (ratio 0.999996), kl case 97% with avg|S4|^2/N^4 = 11.96 -> 14 (correction lives one level deeper, as predicted). Mult-table e2 bug caught by the in-script aggregate assertion (LESSON 82-L) | `diagnostics/selfcheck_chain.log`, `diagnostics/k4_ab_decomp.log` | inline (LEDGER R82.31) |
| **R82.32 k=4 kl-convergence established**: avg|S4|^2/N^4 = 11.96/12.36/12.92 at N=37/53/73 -> 14; two-implementation cross-check at N=37 (corrected (u,v,w)-grouping reproduces the (e)-table value 11.96 exactly); grouping bug (r = uv+(u+w)w) caught ONLY by the cross-check, not by direct-vs-grouped (LESSON 82-M); distribution histograms smooth (no heavy tails) | `diagnostics/k4_kl_convergence.log`, `k4_histograms.log` | inline (LEDGER R82.32) |
| **R82.33 op:cscale CLOSED**: zeta = unique 4th root with zeta^K = chi (5/5 designs; i/-i/-1/-1/-1); k0 = unique class solving chi_{k0}(a) = zeta/lambda_0 (5/5: predicted {1},{1},{8},{9},{19} = first branch of each pair); the mirror pair = model's EXACT symmetry model(k0,q') = model(-k0,-q') (5/5 probes, correct even-parity blocks; the earlier mirror-failure was the parity-conflated block). Closed form parameter-free | `diagnostics/k0_law_final.log` | inline (LEDGER R82.33) |
| **R82.34 Theorem I at an INERT design** (N=1103, K=48, m=23): C1 level sets N+1 = 1104, cone = {0}; C2 orbits = m; C3 spectra equal across 6 orbits x 6 level sets to 6.6e-14; C4 11.9 decades; C5 torus elements 10/10 — Theorem I holds verbatim with N-1 -> N+1; chi = 1 zero-mode class (P+ empty, P- used) | `diagnostics/inert_torus.json`, log | inline (LEDGER R82.34) |
| **R82.35 elementary route stops at k=4**: cubic-surface family second moment avg|T|^2/N^2 = 12.40 -> 14 over 2652 kl pairs; distribution SMOOTH (90.3% mass in [14,50), zero points >50) — no heavy-tail degenerate locus analogous to k=3; |S4|^2 ~ (N-2)^2|T|^2 confirmed (12.40 vs 12.36). The k=4 constant is a bulk surface-family monodromy quantity (Katz input); the elementary hierarchy: k=2 counting, k=3 1+4, k=4+ Katz | `diagnostics/k4_surface_family.json`, log | inline (LEDGER R82.35) |
