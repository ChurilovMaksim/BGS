# Line N (R-mix) majorant: exact-mode run p = 17, q = 103 [N]

*Added 1 November 2026 (Asia/Yekaterinburg, UTC+5). Label: [N], floating-point numerics without error control, one prime.*

## What this is
* The run queued in N17b §7 (`computations/verification/lineN17b/REPORT_N17b.md`) and N18b. It started 2026-11-01 03:06:43 and ended
  2026-11-01 11:07:08 (UTC+5), 28824 s.
* Script: `computations/verification/lineN17b/code/a_mixed_majorant.py` (sha256 `ef12bca0…26c`, identical to the lineN16b copy).
  The statistic is the one of N16b §2: E_M = mean of the majorant F_p over the mixed set, W0 = exact collision mass of the majorant,
  c_coll = log(E_M/W0)/log q.
* `a_mixed_p17_q103_exact.json` and `p17_q103_final.out` are the final outputs. The file
  `computations/verification/lineN17b/post_manifest/logs/p17_q103.out` committed earlier is the partial log taken while the run was
  still going (start line only; its hash is in `../receipt.json`). It is left unchanged.

## Result
h₁₇ = 1607521 = 103 · 15607, mixed classes with iso part q = 103, mode exact, n = 25085365308 points (≈ 2.5e10).

| p | q | mode | points | E_M | W0 | E_M/W0 | c_coll |
|---|---|---|---|---|---|---|---|
| 17 | 103 | exact | 2.51e10 | 0.72637 | 2.08247 | 0.3488 | −0.227 |

Earlier rows (N16b §2, `computations/verification/lineN16b/logs/`): exact p = 11 (q = 23, 353), p = 13 (q = 79, 599), p = 17
(q = 15607) have E_M/W0 = 0.174, 0.0337, 0.106, 0.0426, 0.0212 and c_coll = −0.56, −0.58, −0.51, −0.49, −0.40.

## Reading (no more than this)
* E_M < W0 and c_coll < 0, as in every earlier exact row. In that sense the point is **consistent with** the earlier [N] pattern
  "c ≤ 0" recorded for H5(a) (BGS-TRACE-303).
* It is the largest ratio and the c_coll closest to 0 of all exact rows. For the small-q rows the ratio is 0.174 (p = 11, q = 23),
  0.106 (p = 13, q = 79), 0.349 (p = 17, q = 103), so no monotone trend in p is visible.
* The N16b sampled estimate for the same case (2.2e7 points: E_M = 0.136, ratio 0.065, c_coll = −0.59) was low by a factor ≈ 5.3,
  as the heavy-tail caveat of N16b §2 warned. The sampled p = 23 rows should be read with that in mind.
* This is a majorant statement at one prime and one divisor. It is not a proof of (R-mix), it says nothing about uniformity in d or
  about large p, and it does not change the status of BGS-TRACE-303 (open) or BGS-TRACE-299 (conditional).

## Hashes
`SHA256_p17_q103.txt` (paths relative to the repository root; verify with `sha256sum -c` from the root) and `SHA256_p17_q103.txt.sha256`.
