# NOTES V5 (final assembly) — times box-local (UTC+5)
- 10:49 started. Read the lineN21b report, THEOREM_DRAFT_v4 and N20 v2 diff (patch applies cleanly; result identical to N20/scratch/THEOREM_DRAFT_v5_proposed_v2.md).
- 10:50 Crossover decision: A_bad^KP enters the exponent (N14 §1 item 4, per-site normalisation; KP log→modulus). v4 B_p omitted it, and leaving it out cannot be justified. Ran crossover (N19b logic) at δ_eff for C = 0.082 / 0.04 / 8.8e-4 / 4.4e-4 (N20 tail_kp_v2 S₀ values) and at the v4-style 2.0629e-6. The first four runs used N21/code/crossover_N21.py; their outputs were moved from N21/logs to V5/logs and renamed (the N21 v2 manifest still verifies). Then V5/code/crossover_v5.py (same logic, V5 output path) for 7.1864e-6 and 5.0313e-6.
- 10:51–10:55 V5/code/assemble_v5.py: v4 + N20 diff + v5 edits → THEOREM_DRAFT_v5.md; THEOREM_DRAFT_v4_to_v5.diff; CLAIMS_PROPOSED_v5.md.
- 10:53 manifest.
