# NOTES_N17b (Line N17b) — H7: levels other than h_p
## 2026-11-01 01:52:48 +0500 — start: (1) re-derive W′ level structure from TRACE-206; (2) small-p level data; (3) draft v2; (4) optional p=17 q=103.
## 2026-11-01 02:12:11 +0500 — progress
- TRACE-206 frozen def read (audit/pr60/record/claims.json); TRACE-213 exact identity W' = NR/phi + sum Dev/phi reproduced to 5e-15 at m=9..17 (b_exact_dev.py, exact Line E/G tables).
- a_levels.py: level lists p=3..13 — every divisor d<=sqrt h is included at these m (threshold excludes nothing for (+-2,8)); (+-2,16) excluded at some levels.
- c_member_dev.py (direct TW at member nu) abandoned: TW state space b^2 explodes for member nu (b ~ 8d). Killed.
- d_g3dev.py (TRACE-212 I2' member formula from twisted sums): m=15 reproduces exact Dev to 4-5 digits. Launching m=21 (DMAX 1000), 33 (400), 39 (650) background nice 19.
- Steering received 02:07: referee lineN14 (N13b/N14b READY after minor fixes) -> v2 sections in N17b + THEOREM_DRAFT v2.
## 2026-11-01 02:28:07 +0500 — progress
- m=21 done (hp 239 Dev/phim +0.214/+0.211; d=7 -0.0129/-0.0127). m=33 running, m=39 queued.
- g_threshold.py: m0=15 for (+-2,8) inclusion of all d<=sqrt h (fixed h indexing bug: h_m=S_{(m-1)/2}).
- e_crossover.py: gas G vs Robin I_p bound: first p=1386 (1289: 10.99 vs 12.85).
- REPORT_N17b.md drafted (sec 1-3, 5, 6; table + sec 7 pending). N13b S reconciliation: 7743-7371=372=n_23+n_353 (hp-div members).
## 2026-11-01 03:07:10 +0500 — final
- Jobs checked alive at 02:57 (no relaunch needed). m=33, m=39 done (logs/d33.out, d39.out, d_g3dev_m{33,39}.json); h_units.py table in S_rho units -> REPORT sec 4.
- REPORT sec 2b: per-level negative Dev bounded a priori only by floor (h_p/d)S_rho [P]; gas beats Robin(I_p) from p>=1386 under hyp (i)-(iii); does NOT beat tau(h_m) (Nicolas-Robin) -> H7* needed.
- THEOREM_DRAFT_v2.md written (v1 unchanged, sha 447da47f... as in N16b manifest).
- p=17 q=103 exact mixed run started 03:06:43 +0500 (nice 19) in post_manifest/ — excluded from manifest, still running.
- Manifest next; nothing appended after.
