# Artifacts MANIFEST

Index of machine-readable outputs in `artifacts/`. Each row maps an output
file to the script/command that produced it. Recreated on 2026-09-01 (RUN 91)
after the R85-R87 hostile audit confirmed all listed artifacts reproduce.
R108 (2026-09-02): independent referee suite added — `code/referee/` scripts
with outputs in `data/referee/` (k=4 verification, N=3571 arbitration,
exact-layer checks, 16-design K-sweep, block decomposition, extraction test).

## Top-level run directories

| Path | Run(s) | Contents | Generator |
|---|---|---|---|
| `artifacts/r87/` | R87 | baseline_check.json, cycle1_hecke_basis.json, cycle2_toy_subweyl.json, cycle3_trace_fluctuation.json, cross_key_julia.txt | src/large_m/{baseline_repro_r82,theorem_ii_extended,toy_subweyl,trace_fluctuation}.py, src/large_m/cross_key_check.jl |
| `artifacts/r91/` | R91 | cycle2c_multiplicative_toy.json (+ .log) | src/large_m/cycle2c_multiplicative_toy.py |
| `artifacts/diagnostics/` | R6-R91 | 93 files: moment tables, census runs, falsifiers, logs (see below) | various src/large_m/, src/diagnostics/ |
| `artifacts/legacy_runs/` | R1-R82 | certified closed-form and design artifacts (q-curve .npz, closed_form.json, theorem certificates) | archived run scripts |
| `artifacts/referee_r83/` | R83 | referee pass evidence | referee pass scripts |
| `artifacts/julia_logs/` | R80+ | Julia engine logs | Julia runs |

## Key certified artifacts (load-bearing)

| Artifact | What it certifies | Status |
|---|---|---|
| `legacy_runs/theorems/II_twisted_jacobi/closed_form.json` | Theorem II twisted-Jacobi closed form (R82.12) | [PROVEN] |
| `legacy_runs/theorems/I_torus_rigidity/q_curve_N{199,3571}.npz` | q-curves for level-set means (R82) | [PROVEN] |
| `r87/cycle1_hecke_basis.json` | Theorem II at 4 new split primes (N=461,19489,95419,144481), max |J| dev <= 1.5e-12 | [PROVEN] (H1) |
| `r87/cycle2_toy_subweyl.json` | additive toy for H3 (Sub-Weyl mechanism), 12/14 + monotonicity | [NUMERICALLY-SUPPORTED] |
| `r87/cycle3_trace_fluctuation.json` | direct bound |Tr(M^k)-W_k m_+| <= C_k m^{1/2}, C_k <= 0.021 | [NUMERICALLY-SUPPORTED] |
| `r91/cycle2c_multiplicative_toy.json` | multiplicative toy (H3 shape), 14/14 PASS + coset-convolution identity (R91.5) | toy: [NUMERICALLY-SUPPORTED]; identity: [PROVEN] sketch |
| `diagnostics/fifth_mixed_moment.json` | e_{2k}/N^k k=1..5 at (3571,17), Catalan 1/2/5/14/42 confirmed | [NUMERICALLY-SUPPORTED] |
| `diagnostics/fourth_mixed_moment_designs.json` | fourth mixed moment at certified designs (R85) | [NUMERICALLY-SUPPORTED] |
| `diagnostics/t2_multiplicity_falsifier.json` | Theorem T2 (multiplicity = (N-1)/K) at 5 designs + negative control | [PROVEN] (R91.2 fixed) |
| `artifacts/r93/katz_cancellation_explicit.json` | coupled vs uncoupled energy: E_c ~ N^3.3 vs trivial N^7 (Theorem 93.1) | [NUMERICALLY-SUPPORTED] |
| `artifacts/r93/sigma4_third_calibration.json` | third calibration N=3571 (rel std 0.0059) | [NUMERICALLY-SUPPORTED] |
| `artifacts/r93/sigma4_two_point_scaling.json` | two-point rel-fluctuation scaling (exponent -1.06) | [NUMERICALLY-SUPPORTED] |
| `artifacts/r93/sigma4_second_moment.json` | exact second moment model at N=53 (Z0, mean, Var exact) | [PROVEN at N=53] |
| `artifacts/r92/h3_k2_exact_reduction.json` | Theorem 92.1 k=2 exact reduction | [PROVEN] |
| `artifacts/r92/std4_fluctuation_decay.json` | k=4 standardized-moment fluctuation decay | [NUMERICALLY-SUPPORTED] |
| `artifacts/r92/h3_k4_factorization.json` | Theorem 92.2 k=4 factorization | [PROVEN] |
| `artifacts/r92/h3_even_k_template.json` | uniform even-k template (k=6 verified) | [PROVEN at k=6] |
| `artifacts/r92/conic_bound_test.json` | conic-fibration bound test (7x margin) | [NUMERICALLY-SUPPORTED] |
| `artifacts/r92/h3_k2_exact_reduction.json` | Theorem 92.1: k=2 fluctuation = combinatorics (PROVEN) | [PROVEN] |
| `artifacts/r92/std4_fluctuation_decay.json` | k=4 standardized-moment fluctuation decays m^-0.4 | [NUMERICALLY-SUPPORTED] |
| `artifacts/r92/h3_k4_factorization.json` | Theorem 92.2: A4 = m^2 * surface-variety sum (PROVEN at N=53,199) | [PROVEN] |
| `artifacts/r91/bgs_spacing_goe.json` | GOE spacing P(s), parity-odd sector, N=3571/19489 (Theorem 91.6) | [NUMERICALLY-SUPPORTED] |
| `artifacts/r91/bgs_spacing_gaps_ks.json` | corrected KS-on-gaps, 3 designs incl. N=95419 m_+=837 | [NUMERICALLY-SUPPORTED] |
| `artifacts/r91/number_variance_goe_control.json` | spectral rigidity vs matched GOE control, 6/6 PASS (Theorem 91.7) | [NUMERICALLY-SUPPORTED] |
| `artifacts/r91/cycle2c_multiplicative_toy.json` | multiplicative toy (H3 shape) 14/14 + coset-convolution identity | toy [NUM-SUPPORTED]; identity [PROVEN] |
| `artifacts/r91/word_trace_proof.json` | pinned rank-1 algebra + beta_s recurrence for Theorem 91.5 | proof-support |
| `artifacts/r91/bgs_spacing_N95419.json` | full-coset run at N=95419 (mixed parity, Poisson-lean; superseded by parity-split) | diagnostic |
| `diagnostics/surface_term_k5.json` | O(K^2/N) surface-term coefficient fit, c_k k=1..5 | [NUMERICALLY-SUPPORTED, fragile] |

## Diagnostics detail (93 files)

Moment and census tables: catalan_{honest,verify}, fourth_moment, fourth_mixed_moment(_designs), fifth_mixed_moment(_partial), sixth_moment_direct, eighth_moment_direct.log, family_second_moment(2), second_moment_{exact,exact2,identity,raw}, jacobi_moments, spectral_fourth, k4_{moment,convergence,surface_family}, entry_statistics, shape_modes, k0_law(_final), cscale_proof.
Rigidity/edge: rigidity_{control,long_range}, edge_vs_bulk(_9349), crossing_deficit, small_spacings.
Designs/inert: inert_scan, inert_torus, density_shape, orbit_invariant, bgs_large_m(_big).
Falsifiers: t2_multiplicity_falsifier, r86_ledger_health_probe, k4_ab_decomp, k4_histograms, k4_kl_convergence, factor5_split, lean_{build,scale_law}.
Logs: *.log alongside each json (kept; the contract greps them).

## Hygiene

- Generated on demand; all reproduce (R91.1 hostile audit).
- Retracted/voided outputs: see `artifacts/legacy_runs` READMEs and LEDGER RETRACTIONS (R12-A, R61, R67-70, R71.6, R82.1).
