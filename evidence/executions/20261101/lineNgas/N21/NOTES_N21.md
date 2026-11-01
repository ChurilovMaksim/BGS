# NOTES N21 — H4 (core→true conversion) final push
All times are box-local (Asia/Yekaterinburg, UTC+5). Entries before 09:41 were reconstructed from file mtimes and the run logs; entries after that were written live with `date`.

- 09:00 (UTC+5) start. Read THEOREM_DRAFT_v4 (H4 row), N15/N16 reports, audit lineN16, claims 299/302/307/318/322, N16 conv_vec.py, N15 c3_mid/rig/conv, N8 n8_cert, N14 f_post2/d_decay2, N19b a_crossover_v3.
- 09:14 created N21/{code,logs,lean}.
- ~09:20 code/conv_c.py: Lemma C, a self-contained two-sided vector conversion. Test: logs/convC_test.out (09:22). Singles have E/|r| ≈ 1.9–3.7e-3, dominated by err_dPi.
- ~09:23 launched replay (2 parts, the 1560 N15 jobs) and ext G=16..80 (5 parts).
- 09:29 **found F21-2**: digits.py runs at mp.dps=34, so the twists are wrong for G ≥ 22 (rel. error 1.7e-16 at G=22, 1.5e-11 at G=30, 6e-4 at G=40). Killed ext and moved its rows to logs/discarded_dps34/. Patched conv_c (mp.dps=160, S2/LAM recomputed). Relaunched ext for G=16..60 at 09:30. The G ≤ 15 replay is unaffected (twists identical at G ≤ 20, checked).
- 09:34 conv_c.chain: added a keep= hook (array export only; numerics unchanged).
- 09:36 replay done (1560 rows).
- 09:38 code/f_postC.py (N14 f_post2 formulas, arb). Partial result: δ_true(G≤15) ≤ 2.2102e-6 (N16 had 2.470e-6). Box-widening dev_by_G is flat at ≈1.29e-7 for G ≥ 12, so it does not decay.
- 09:36–09:40 code/tail_DT.py (Lemma Q + Lemma D^T analytic tail, arb). First version: crossL bounded with Γ_j, giving T(40)=3.4e-7. The covector-side crossL bound gives T(40)=4.9e-9; Σ_{G≥40} ≤ 8.83e-9, remainder G>200 ≤ 9e-53.
- 09:39 `lake exe cache get` in /workspace/audit/lineN12/lean/proj: "No files to download, Already decompressed 8690 file(s)".
- 09:40 fixed the CX/CY envelope constants in the G>GMAX remainder (a missing 1/ρ on the X side; affects only the 1e-52 remainder).
- 09:41 code/crossover_N21.py (verbatim N19b logic, N21 output path). Reproduces 1390/1399 at δ=2.47e-6.
- 09:47 [v2 correction, referee F7: really 09:45, the file mtime of tail_DT_40_200.{json,out}; this entry was written afterwards, not live] tail_DT 40..200 (KK=18, fixed envelope): Σ_{G≥40} ≤ 8.829e-9, remainder G>200 ≤ 1.03e-52.
- 09:49 tail_DT parametrised by the anchor-window padding KK (only the singles' window changes; the lemma is unchanged). KK=16 allows cuts from G=36 on: T(36)=1.83e-7 (> box 1.29e-7), T(37)=6.17e-8, T(38)=2.69e-8, T(39)=1.10e-8, then identical to KK=18. Decision: use the box for 16 ≤ G ≤ 36 and analytic KK=16 for G ≥ 37.
- 09:51 resumed after an interruption. The ext runs were at G ≈ 44–46; I killed them because G ≥ 37 is covered analytically. Partial rows for G ≥ 45 are kept but unused.
- 09:52 Lean LineN21Arith.lean EXIT 0. The first attempt failed on rounding margins (RA, Rem, |s/μ|, m1/m2); I loosened the decimals and split out the divisions.
- 09:52 final_delta: δ_true ≤ 5.0313e-6. crossover: first int 1397, first prime 1399, mono ok.
- 09:54 REPORT_N21.md written; SHA256 manifest.
- 10:09 referee lineN21 verdict READY AFTER FIXES F1–F9; read in full.
- 10:10 F1 (tail_DT Ψ^max), F8 (f_postC arb accumulation), final_delta v2 paths; OUTSUF env for v2 outputs.
- 10:10 reruns: f_postC_v2 (Σ16..36 = 2.71265528e-6), tail_DT_36_60_KK16_v2 and tail_DT_40_200_v2 bit-identical to v1; final_delta_v2 5.03124773e-6.
- 10:11 Lean v2 (LineN21Arith_v2.lean, 24 theorems), cache get "No files to download", EXIT 0. v1 Lean file restored unchanged.
- 10:11 code/v1/ reconstructed (3 files, hashes match the v1 manifest). NOTES 09:47 entry annotated (really 09:45).
- 10:12 REPORT_N21_v2.md written; manifests + self-hashes.
