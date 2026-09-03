# ARTIFACT MANIFEST

Every load-bearing number in `paper/resonance_laws_catmaps.tex` is
traceable: paper claim → artifact JSON → generating script (current
path in `src/`) → command. Historical scripts referenced by early
ledger entries live unchanged in `src/archive/` (names preserved for
provenance); their outputs remain valid.

## Proven results — verification artifacts

| Paper claim | Artifact | Script | Command |
|---|---|---|---|
| Matched identity, Thm core | `grok_identity_check.json`, `run13_strong_master.json` | `src/archive/…` (superseded by proof) + inline audits | `python src/reduced_resonance.py`-based brute force |
| Zero-count lemmas Z₂,Z₃,Z₄ | `—` (brute force in transcript) | `review/scripts/run45_lemma.py` | `python review/scripts/run45_lemma.py` |
| Ensemble-mean law, Thm meanlaw | `run46_exact_mean.json` | `src/verify_mean_law.py` | `python src/verify_mean_law.py` |
| Tail bound floor(k²/p)+2, 0 violations | `run36_audit.json` (+ `run20_constant.json`) | `src/audit_tail_bound.py`, `src/campaign_*`† | `python src/audit_tail_bound.py` |
| Master formula r≤4 machine precision | `master_general.json` | `src/master_general.py` | `python src/master_general.py` |
| Character expansion certification | `char_expansion_cert.json` | `src/char_expansion_cert.py` | `python src/char_expansion_cert.py` |

† `campaign_tail_constant.py` was archived under its run-name
(`run20_constant.py`) — regenerate from `src/archive/run20_constant.py`.

## Numerically supported claims

| Claim | Artifact | Script |
|---|---|---|
| Perturbation ⇒ WD-not-Poisson (4 primes) | `run31_multiprime.json` | `src/verify_perturbation_wd.py` |
| Matching procedure validity (2ε consistency) | `run38_matching.json` | `src/audit_matching.py` |
| Conditional probability ≈ 1/p (independence) | `run43_condprob.json` | `src/diag_conditional_prob.py` |
| Small-period primes p∈{1597,2161,2207,3001} | `run27_primes.json` | `src/find_small_period_primes.py` |
| Mean ≈ k³/p² scaling discovery (4 cases) | `run44_mean.json` | `src/archive/run44_mean_scaling.py` |
| Reversibility ⊬ even k instances | `run13_phase23.json` | `src/archive/run13_centered_mechanisms.py` |

## Superseded / retracted (kept for the record)

| Item | Status | Where |
|---|---|---|
| “Arithmetic beats symmetry” Tr(W⁴) experiment | RETRACTED (non-Hermitian V) | `run13_quantum_w4.json` |
| Theorem-6 of run11 (C_Fk⁸/p², threshold p^{2/3}) | RETRACTED (double count) | ledger R12-A |
| Old fine-scale theorem drafts | superseded | `drafts/archive/` |

## Lean formalisation

`C:\lean\bgs_formal\BgsFormal.lean` — collision lemmas
`collision_ext`, `prod_eq`, `sum_sq`; build green
(`lake build`, mathlib v4.33.0).

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
