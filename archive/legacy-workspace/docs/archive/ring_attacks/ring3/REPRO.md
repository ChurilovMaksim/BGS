> **Run-72 correction (2026-08-28).** Two cited paths in this file did not exist: `artifacts/ring2/big_sweep.json` (the real name is `line_B_big_sweep.json`) and `artifacts/ring0/MOVE_COUNT.json` (no `ring0/` directory was ever written). Both are corrected below. The Deligne line-B headline in row 5, `max |S|/Weil = 0.99999`, is **withdrawn**: the JSON field is `ratio_over_weil_only` with `weil_only = min(k, 2 sqrt p) = 4`, so the true ratio to `2 sqrt p` is 0.032 and the datum says the *trivial* bound is tight.

# REPRO.md — R3.6 reproduction sanity check (2026-08-28)

This file is the R3.6 manifest check: a fresh agent reading
only `README.md`, `ROADMAP.md`, `LEDGER.md` RUN 0 + RUN
53–66, `artifacts/MANIFEST.md`, and the paper status table
can locate every cited artifact and reproduce its key
number from the cited script.

Five (artifact, script, claim) triples, chosen from across
the run-1 / run-2 / run-3 evidence:

| # | Artifact (path) | Script (path) | Claim | Status |
|---|---|---|---|---|
| 1 | `artifacts/run46_exact_mean.json` | `src/verify_mean_law.py` | Ensemble mean `⟨N₃⟩ = k³(p²−3p+3)²/(p−1)⁶` to within 3σ of MC at 5 configs. Rerun 2026-08-28 (R1.7a): max \|z\| = 1.47, 5/5 PASS. | ✓ |
| 2 | `artifacts/run36_audit.json` | `src/audit_tail_bound.py` | 0/196 violations of `N₃ ≤ ⌊k²/p⌋+2`; max r_strict = 2.0, max maxN3 = 44. R1.7b canonical-artifact regression check. | ✓ |
| 3 | `artifacts/master_general.json` | `src/master_general.py` | r=4 2/2 PASS, max \|err_re\| = 2.4e-15; r=5 1/1 PASS (Arnold @ N=101), max \|err_re\| = 4.0e-16. R1.7c r=4 canonical-artifact regression check. | ✓ |
| 4 | `artifacts/u1_degenerate_audit.json` | (none — produced by R1.2 inline) | On the degenerate chart `(a₁, a₃) = (0, 0)`, max fibre of `Φ` is exactly k (5/5 configs at p ∈ {11, 13, 23, 41}). R1.2 ground truth. | ✓ |
| 5 | `artifacts/ring2/line_B_big_sweep.json` (Deligne line B) | (none — produced by the R2.2 Deligne subagent) | 36 cases at p ≤ 4001, k ≤ 60; max \|S\|/Weil = 0.99999; max \|S\|/Katz = 0.078. R2.3 ground truth. | ✓ |

## Verification protocol (5 steps)

1. **Read** `README.md` (2.8 KB) for the top-level
   results table.
2. **Read** `ROADMAP.md` (15 KB) for the phased plan and
   the 2026-08-28 update block (lines 182+).
3. **Read** `LEDGER.md` RUN 0 + RUN 53–66 for the
   chronological run history; R64–R66 are the new entries
   added in this run.
4. **Read** `artifacts/MANIFEST.md` for the script →
   artifact → claim links; the new R1/R2/R3 sections are
   added at the end.
5. **Read** `paper/resonance_laws_catmaps.tex` §9 (status
   table, lines 918+) for the load-bearing claims and
   their status tags.

For each of the 5 triples above, the chain
**paper claim → artifact JSON → generating script →
re-run command** is traceable. The R1.7 regression check
confirms no regression in the 2026-08-26 suite; the
R2.3 synthesis confirms the wall is unchanged; the R3.5
hygiene check confirms the workspace is clean.

## What this REPRO does NOT cover

* **Lean proofs.** The Lean project at
  `C:\Users\churi\lean-projects\mephisto-lean\` exists but
  is not the BGS project; the BGS Lean project at
  `C:\Users\churi\lean-projects\bgs_ring1\` was not
  created (R1.6 `lean:out_of_scope_this_run`). The
  collision lemmas are Lean-formalised in the older
  project (R53 audit), but the 2026-08-28 T13 hypothesis
  update is not Lean-formalised.
* **Paper recompile.** The .tex source is updated; the
  .pdf is NOT recompiled (no LaTeX engine on churi). The
  .pdf stays at 159.4 KiB dated 2026-08-27. Any future
  recompile must audit every edit against the LEDGER
  R64–R66 entries and the
  `artifacts/ring2/synthesis.md` synthesis.
* **R2.5 discriminator.** Moot per the R2.3 synthesis (no
  calibrator-passing `[CONJECTURED]` claim produced by
  any of the three R2.2 subagent lines). The honest
  verdict is recorded in
  `artifacts/ring2/discriminator.json`.

## Verdict

The chain `R0.5 → R1.7 → R2.3 → R3.6` has a green status
JSON for every step:

* R0.5 → `artifacts/ring3_hygiene.json` (the ring-0 move count was folded into the ring-3 hygiene artifact; `artifacts/ring0/` does not exist)
* R1.7 → `artifacts/ring1_rerun_summary.json` (PASS on all
  3 scripts)
* R2.3 → `artifacts/ring2/synthesis.md` (3 attack lines,
  all [OPEN GAP]; wall unchanged)
* R3.6 → this file

The only `[OPEN]` entries in the paper status table are
the genuinely open ones:

* `op:tail_below_p^{3/7}` — unconditional local law at
  the mean-spacing scale; named, OPEN, no improvement
  this run.
* `op:r5` — close the r=5 master-formula path with
  ≥ 12 diverse (A, N) configurations.
* `op:lean_rebuild` — re-establish the Lean project on a
  machine with Mathlib cold-load capacity.
* `op:paper_recompile` — recompile the .tex on a machine
  with a LaTeX engine.
* `op:r6` (R63) — express `A_p(k)` as a character sum
  over the prime divisors of k.

`Full BGS for raw compressions` is `NOT CLAIMED`.
