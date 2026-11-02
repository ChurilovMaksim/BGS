# Breakthrough integration receipt — 2026-11-02 (evening)

Seamless integration of the autonomous BGS breakthrough program record into
the repository structure, not a folder dump.

## Base

- Branch `main`, HEAD re-verified immediately before push:
  `4b86d7f306473837127b0ee67769aac0c15343e3` (PR #79, Lean batch 5).
- No existing file modified except `evidence/README.md`, which was extended
  by appending one section to the exact remote content at that HEAD
  (verified byte-identical prefix). No registry change, no change to
  `formalization/Bgs.lean`, no change to any existing Lean module, no
  change to the other agent's Line E work.

## Contents (842 files, ~6.7 MB, all UTF-8, no binaries, no symlinks)

- `evidence/breakthrough/methods/` — 774 wave notes and check scripts
  (day-1 swarm M01–M10, waves 3–47, extension 47x), exactly as run.
- `evidence/breakthrough/working/` — 47 text files from auxiliary working
  directories (`audit/`, `cleanup-plan/`, `frozen-map/`, `g4/`, `g4check/`,
  `literature/`, `numerics/`); binaries, logs, and `.json` files excluded.
- `evidence/breakthrough/PROGRAM.md`, `DAY1_REPORT.md` — program plan and
  day-1 report.
- `evidence/breakthrough/README.md` — index with per-wave status and the
  standing open fronts.
- `formalization/drafts/` — 16 Lean drafts, each with a header stating its
  exact test-copy build result and `sorry` count. None is imported by
  `formalization/Bgs.lean`.

## Parallel re-verification (fresh runs, 2026-11-02 evening)

All four checks MATCH the notes exactly, no discrepancies:

- A — ψ-analysis (`wave47_GapG_psi_check.py`, ~10 s, exit 0): valuations
  and residues r=3..12 exact; census (128,128) 32768/32768 valid, reps
  exactly 2; all violation counters 0.
- B — T_k periods (`wave47_Tk_periods_A.py`, `wave47_Tk_periods_B.py`,
  ~0.5 s each): 39 fibers = 39 Γ-orbits, 0 split, 0 mixed-period; p=4o
  everywhere; max period N/4 at m=32/64/128/256.
- C — F1 (`wave47_F1_check.py`, 5.3 s, exit 0): m=36 and m=252: 324 tested,
  0 mismatches, 0 collisions; m=108: 2916 tested, 0/0.
- D — DIV/PAR (`wave46_GapG_DIV_PAR_check.py`, ~2 s, exit 0, ALL CHECKS
  PASS): V1–V4 and residues for s=1..12; Cassini sign −1 for n≤200;
  P_n mod 4 period 4 for n≤100; divided-system enumeration at (128,128)
  = 8 solutions, 0 violations; DIV on 200 random sequences at three
  sizes, 0 violations.

## Excluded, honestly

- 8 large census data files, 1.3 GB total (`.json`/`.npz`/`.npy`/`.bin`):
  the connector snapshot limit (16 MiB UTF-8) cannot carry them; they stay
  local and are summarized in the wave notes.
- Run logs, binary pickles, `.json` result files, and the superseded draft
  `LineBRadicalDraft_v1_preAPIfix.lean`.
- Still pending at push time (not included as finished): PC triple
  intersections (wave 47, runs pending, note included with verdict TBD),
  Lean draft of DIV/PAR lemma V3 (sequential build still running), exact
  Δ(48) (background enumeration still running).

## Status honesty

Every claim in this package keeps the status its note gives it: proved,
proved modulo named lemmas, census-confirmed, sampling, sketch, or draft
with `sorry`. Nothing here changes any registered claim status, and BGS in
full generality remains open.
