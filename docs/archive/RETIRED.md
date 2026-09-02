# RETIRED — BGS workspace archive manifest

This directory preserves historical material that has been superseded,
retracted, or is not part of the live workspace. **Nothing is destroyed**.
Every retired file keeps its original name and is reachable for traceability
through its LEDGER/THEORY citation chain.

### `archive/papers/superseded_r108/` (added R108, 2026-09-02)

Superseded pre-R108 paper drafts, retired by the R108 referee audit:

- `BGS_PROOF.tex/.pdf`, `BGS_COMPLETE.tex/.pdf` — early versions of the
  full-chain paper; superseded by `paper/final/bgs_complete_paper.tex`
  (R108-corrected).
- `M4D_PROOF.tex/.pdf` — the original "complete proof of delta = o(1)"
  claim; SUPERSEDED AND RETRACTED (root cause: indexing bug in the
  N=3571 calibration; cross terms uncontrolled; constant 16 wrong;
  fixed-K regime impossible).  Corrected version:
  `paper/final/mobius_fiber_theorem.tex`.  See docs/REVIEW_R108.md.
- `exact_wd_and_subgroup_moments.tex/.pdf` — pre-R82 companion note;
  superseded by `paper/final/cat_map_bgs_main.tex`.

### `archive/papers/stale_pdf_r108/` (added R108)

PDFs compiled from the PRE-correction sources (R95-R101 era).  The
corrected sources are `paper/final/*.tex`; these PDFs are retained only
for traceability and MUST NOT be cited as current.  Recompile the
final .tex files with tectonic on a machine with LaTeX to regenerate.

## Categories

### `archive/hecke_centring_failed_line/`

VOID line — LEDGER R67..R70 measurements retracted by R71.6 ("three
independent defects, all reproduced"):

- `hecke_real_centraliser_v3.jl` .. `hecke_real_centraliser_v9_v10.jl` —
  the Julia probes used to measure Hecke-centring collapse. All show a
  multiplet basis that's actually `U[:, idx]` (columns of the propagator),
  not eigenvectors; the "Hecke mean" is a Haar average that cannot change
  off-diagonal entries; the accumulator is never divided by `n_hecke`.
- R67/R68/R69/R70 reported "5×–7842× reduction" and a "Churilov tail index
  ~ 2.3", all reproduced by an arithmetic-free Haar random frame.

### `archive/kernel_failures/`

Empty — Run-1 (R1–R3) kernel `K(x,y) = p^{-1/2} exp(iπ/p·[c⁻¹(dx²−2xy+ay²) mod 2p])`
fails Egorov covariance by O(1) and was never a valid quantisation. The
retraction text is preserved verbatim in LEDGER.md §0 (RET-1).

### `archive/papers/`

- `resonance_laws_catmaps.{tex,pdf,log}` — legacy paper from R12–R20 era.
  Resonance-laws line (the matched identity, mean law, tail bound,
  r6/r8 laws). Superseded by R71–R82. **See** `paper/exact_wd_and_subgroup_moments.tex`
  for the current state of these results.
- `twisted_lemma_clean.tex` — earlier draft of Lemma F (R73.4).

### `archive/papers/`.`papers/`

`resonance_laws_catmaps.{tex,pdf,log}` lives here.

### `archive/portable_shell/`

Snapshot of the R70-portable workspace tree (HANDOFF.md,
README_PORTABLE.md, lean_projects_setup.log).

### `archive/ring_attacks/`

- `ring1_2/` — Ring 1.2 v6/v9/v10 Hecke-centring probes (replicated defects,
  see R67.6 retraction).
- `ring2/` — Ring 2 attack on the p^{3/7+ε} wall: three parallel cloud
  subagent lines (Stepanov / Deligne / Bourgain), all [OPEN GAP] (R2.5
  moot discriminator). Litwatch summary, synthesis.md, line_A/B/C reports.
- `ring3/` — REPRO.md (R3).
- `frontier/hecke_reciprocity_data.json` — F0 reciprocity probe (negative
  methodological result; the Salié reciprocity is a 3-sum, not a 2-sum).
- `retracted/`, `retracted_run1/` — quarantined artifacts from retracted
  measurements (R12-A, R13 run13_quantum_w4, R16, R22, R25).

### `archive/scripts/`

53 legacy `runNN_*.py` scripts from R12–R66, plus `verify_all2.py`,
`indep_check.py`, etc. — superseded by the r71..r82 scripts. Reference
implementations for tail bounds, k=22 anomaly, etc. Most have a successor
in `src/diagnostics/` or `src/kloosterman/`.

`run4_debug_trail.txt` — Run 4 debug trail.

### Archive creation date

2026-08-30, as part of the workspace cleanup. Original R12–R82 file paths
are preserved in `MIGRATION_PLAN.md` (active path) for back-compat reading
of LEDGER/THEORY.

### `archive/MIGRATION_PLAN_completed_20260830.md`

The 2026-08-30 workspace migration plan, moved here on 2026-08-31 (R84) after
its last open item (MANIFEST path repair) was executed. Historical record of
the KEEP/RETIRED/GARBAGE inventory; the living structure description is
README.md.

### `archive/drafts_pre_R71/`

The three 2026-08-27 working notes (`tail_bound_attempt.md`,
`tail_bound_proof.md`, `hecke_symmetrization_test.md`), superseded by
LEDGER R54/R71 and THEORY sections 9-11; the Hecke-symmetrization verdict is
recorded in R49-A/R71.6. No live claim cites them.
