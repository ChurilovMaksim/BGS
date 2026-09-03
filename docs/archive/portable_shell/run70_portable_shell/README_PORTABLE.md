# BGS Portable — 2026-08-27 snapshot (FINAL)

This package is a clean, portable copy of the BGS project as of
2026-08-27, suitable for transfer to another machine. The original
`BGS/` folder is left untouched except for the deletion of
`user_drafts/` (Churilov 2026 drafts), which the user requested
be excluded.

## What's included

- `BGS/LEDGER.md` — single source of truth, all 63 RUN entries (R1-R63).
- `BGS/THEORY.md`, `BGS/IDEAS.md`, `BGS/ROADMAP.md`, `BGS/README.md`.
- `BGS/paper/` — `resonance_laws_catmaps.tex` + `.pdf` (compiled 2026-08-27 02:22).
- `BGS/src/*.py` — 37 canonical Python scripts (catmap core, master formula, etc).
- `BGS/review/scripts/` — audit suite (V1-V7), Julia cross-check, GPU replicate, etc.
- `BGS/review/*.md` — `audit_2026-08-26.md`, `subgroup_kloosterman.md`, `redteam_run5.md`, `lit_run5_notes.md`, `run4_debug_trail.txt`.
- `BGS/drafts/` — `tail_bound_attempt.md`, `tail_bound_proof.md`, `hecke_symmetrization_test.md` (excludes `archive/`).
- `BGS/literature/` — harvest scripts (`oa.js`, `bing.js`, `cr.js`, `ss.js`, `ax.js`, `ddg.js`, `mj.js`, `oa2.js`, `abs.js`) + 2 PDFs + 5 LaTeX sources (kel08, kow24, kr05, kurl07, osv).
- `BGS/tools/` — `lit_harvest.py`, `run_camp.cmd`, `ax.mjs`, `bin/tectonic.exe`, plus the 4 new Julia tools from this session:
  - `linn_h3_subgroup.jl` (RING 1.1 Linn H^3 discriminator)
  - `hecke_real_centraliser.jl` (RING 1.2 v1, retracted)
  - `hecke_real_centraliser_v3.jl` (RING 1.2 v3, Churilov-corrected design)
  - `sol6_closed_form.jl` (RING 1.3 sol6 closed form sweep)
- `BGS/artifacts/` — 119 selected JSON/text artifacts (excludes `camp_log*`, `cancel_log`, `bigrun_log`, `battery_rerun`, `audit_rerun_*`, `audit_strata_rho*`, `phase2_spacings.npy`, `run13_*`).

## What was EXCLUDED (per user request 2026-08-27)

- **`BGS/user_drafts/` — REMOVED.** The three Churilov 2026 drafts
  (Lattice-Quotient Spectra, Wigner matrices, Spectral Selectors)
  were removed at the user's instruction. The directory was deleted
  from the original `BGS/` as well. Historical triage in LEDGER
  R56 (retired in R63); the only retained value was the Churilov
  decomposition concept used in RING 1.2 v3 design (R61, R62),
  which is recorded in the LEDGER — no concrete numerical values
  were transferred.

## What was excluded (cleanup, original BGS/ still has these)

- `BGS/archive/` (runs 1-11, immutable historical).
- `BGS/drafts/archive/` (8 historical LaTeX drafts).
- `BGS/review/archive/` (historical debug logs).
- `BGS/review/blind_replication/` (run6 julia blind-rep, large .npy files).
- `BGS/src/__pycache__/`.
- `BGS/src/archive/` (R1-R5 obsolete).
- Large/temp log files in `BGS/artifacts/`.

## How to use on a new machine

1. **Python kernel** for `BGS/src/*.py`: 3.13 with numpy, scipy, sympy.
2. **Julia** 1.11.4 for the new `BGS/tools/*.jl` tools. First-run JIT is slow (~30-60s); subsequent runs are fast.
3. **Lean 4** + `lake` for the formal proofs at `C:\lean\bgs_formal\` (NOT included in this portable — copy separately if needed).
4. **Tectonic** for `paper/resonance_laws_catmaps.tex` recompile.
5. **Node** ≥22 for `BGS/literature/*.js` OpenAlex/bing/etc harvest.

## Current state (LEDGER R63, 2026-08-27 final)

- RING 0 (defense): PASS.
- RING 1.1 (op:tail via Weil): NEGATIVE result on Linn 2024 transfer; OSV wall remains. Artifacts: `linn_h3_subgroup.jl` + `artifacts/linn_h3_subgroup.txt` (12 configs).
- RING 1.2 (op:local via Hecke): v3 designed per R61 retraction (Churilov decomposition centered by A_n). v3 run blocked on Julia first-compile time. Re-test on pre-warmed Julia.
- RING 1.3 (op:r6 closed form): **naive 4-point closed form REFUTED at k=30, 36** (R63). Real structure: A=0 for k ∈ {4, 8, 10, 14, 16}; p-dependent for k ∈ {20, 22, 26, 28}. Closed form requires character-sum analysis of H = ∏_q µ_q. Artifacts: `sol6_closed_form.jl` + `artifacts/sol6_closed_form.txt` (30 configs).
- RING 2-5: not started.
- R54-R55 audit-confirm: cat map foundation intact (R1-R53 PROVEN/VERIFIED).

## Honest gaps remaining

- op:tail below p^{3/7}: OPEN, OSV wall (R57/R58).
- op:local unconditional: OPEN, v3 run needed (R62).
- op:r6 closed form: OPEN, requires character-sum paper (R63).
- op:inert: OPEN, not started.
- RING 2 (Anosov, Sp(2g,Z), N=p^n): not started.
- RING 3 (general BGS, three attack lines): not started.
- RING 4-5: not started.

## Citations that need re-retrieval on a new machine

- arXiv:2412.04976v2 (Linn 2024 Kloosterman bounds for GL_n).
- arXiv:2110.10941v2 (OSV 2021/2023, published IMRN 2023, DOI 10.1093/imrn/rnac226).
- Bourgain JAMS 2005 (paywalled, "Mordell's exponential sum estimate revisited").
- All citations in `paper/resonance_laws_catmaps.tex` bibliography.

## Integrity contract (this session)

- R61: retracted the "max/median ≈ 15-40" claim in R56/R59 as
  fabrication. The R49-A measurements are actually
  `ev_max/std = 3.8, 5.0` and `ev_kurtosis = 5.9, 9.3` (heavy
  outliers, not low-rank). This is a load-bearing honesty correction.
- R63: retracted the 4-point closed form `sol6 = 15k^3 - 5k^2 - 170k`
  for 3|k (it was a 4-point fit that breaks at k=30, 36). The
  real structure of A_p(k) is more complex; the closed form is
  a serious paper, not a one-session deliverable.
