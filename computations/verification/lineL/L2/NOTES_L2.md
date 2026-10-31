# NOTES_L2
- 13:15 start. Task: open range c_W p^2<q<L_m via cat-map structure: (a) collision count mod q-ideal, (b) vs L_m, (c) numerics h_{3p}.
- 13:20 numerics m=15 q=41: |D|=0.452 vs target^m 42.3, |Z|/q 209; meansq 2.54; phase-blind Dpb~-2e-4 (!). Steering: do REPORT_L_v2 + K2_v3 fixes first.
- 13:35 REPORT_L_v2.md + lineK/K2/REPORT_K2_v3.md (W-F7 errata, own manifest SHA256_K2_v3.txt) done; L manifest regenerated (excludes L2/).
- 13:50 survey: fixed O(h) nu0 search (was the bottleneck) + matmul; m=21 q=239 done (|D|^(1/m)=1.12, msq 1770, trunc L10K40 identical). Batch run_iso.sh restarted.
- 14:00 survey (iso lines, (2,8)-res nu0, L8 K32): |D|^(1/m): 15/41 0.95(|D|.45), 21/239(r=7) 1.120, 33/353(r=11) 0.995, 33/23 0.832,
  39/313 0.856, 39/79 0.920, 39/599 0.963, 51/103 0.931, 51/409 0.855, 57/457 0.848, 21/4663 0.845. All << 1.28359.
  msq tiny for r=m; larger for r=m/3 (inherited from h_p). phase-blind Dpb ~ 0 (relative 1e-8..1e-20). 51/15607 running.
  (a)/(b) analysis: CS barrier G^{2m}/q -> needs q>=3.407^m (8) / 2.583^m (16); main term |Z|^2/q dominates for q<2.227^m;
  height zone only q >~ 1.457 lam^{r-1} >= 1.7996^m-ish > L_m. => collision/height methods cannot reach open range [P].
- 14:25 prec_chk m=57 q=457: double vs longdouble rel<=5e-12, K32 vs K40 identical (logs via rerun; 183/367 running -> logs/prec_chk_183_367.log).
- 14:35 iso table (code/mktable.py): worst |D|^(1/m)=1.12 (inherited r=p levels 239@21, 15607@51 1.10); full-rank ~0.82-0.87. Launched full_level.py (D_iso + E_b all t) for small q -> logs/full_level.jsonl. Next: write REPORT_L2.md.
- 14:50 REPORT_L2.md drafted (tables to be filled by fill step).
- resume 14:10(user clock): full_level done 15/41(+-), 33/23, 39/79, 51/103: K1 combo rate 1.12,1.046,1.071,1.092; running 21/239 full, iso 129/19609 ... Plan: wait for these, kill rest (37223,54121 too costly), fill tables, manifest.
- added Lemma B3 (sum over prime ideals; dual height) to REPORT_L2 §3.
- FINAL: killed remaining runs; tables filled (23 iso cases, 6 full levels incl. 21/239: K1 combo 1.178); labels tightened; manifest SHA256_L2.txt.
