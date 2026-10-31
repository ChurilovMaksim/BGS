# m = 17 verification evidence for Line E (PR #57) and Line G (PR #58) claims (31 October 2026, UTC+5)

This folder adds the m = 17 outputs that were pending when Lines E and G were integrated. It adds **evidence and annotations
only**. No claim changes state, and no proved scope is extended. Numerics at a single m are finite-m evidence ([CA] for the Line E
certificate, [N] for the Line G float evaluation). They prove nothing about m → ∞.

## Contents
* `lineE/cert_m17_full.out`: the m = 17 certificate record for the Line B diagonal kick at η = 2, with residues N ≡ ±196 only.
* `lineE/cert_class.jsonl`: the author's certificate file. Its m = 5..13 lines are byte-identical to
  `computations/verification/lineE/step2/cert_class.jsonl`, and the m = 17 line is appended.
* `lineE/PROVENANCE.txt`:
  * sha256 of the kernel binary, the compiler, and the FMA count of its disassembly (0);
  * diffs of the author's scratch `cert_class.py` / `zres.c` against the repository versions. The differences are a docstring,
    the import path, and the `fp-contract=off` pragma; the binary has no FMA anyway.
* `lineG/eval17_full.log`, `eval17_full.json`, `formula_table_full_17.json`: the Line G float evaluation of the pre-registered
  full-kick m = 17 tests in `computations/verification/lineG/PREDICTIONS_m17.json` (sha256 `fa8505f5…aa344`, unchanged).
* `lineG/batch_orb.log`: the class-sum run log. For the full kick at m = 17 it records 152 007 280 321 canonical orbits, 0
  period-check failures, and the sha256 of `Torb_full_m17.bin`. `lineG/REPORT_section5.md` is §5 of the Line G author report.
* `lineG/EXCLUDED_BINARIES.txt`: the sha256 of `Torb_full_m17.bin` (25.7 MB, not committed; regenerable with Line G's `batch_orb`).
* `check/m17_crosscheck.py` and `.log`: an independent bookkeeping check written for this PR, ending `ALL_OK`. In exact rationals it:
  * recomputes F_17 ≥ (1/φ)Σ_{N=±196}|Z|²_lower, hence F_17/2m ≥ 23.4893 and W̃rest_17/m ≥ 42.9787;
  * checks that the Line G float values lie inside the certified enclosures;
  * compares the Line E predictions at m = 11, 13, 17;
  * checks the Line G test bands and the predictions sha.

  It does not recompute any class sum or certificate.
* `receipt.json`: sha256 of every file above.

## Claims annotated (`record/claims.json`; states unchanged)
| claim | state | annotation |
|---|---|---|
| BGS-TRACE-195 | proved (m = 11, 13) | m = 17 author certificate recorded as evidence: F_17/2m ≥ 23.4893, W̃rest_17/m ≥ 42.9787 (±196 only). It is **not** added to the proved scope, because it has not been reproduced with the referee's independent directed-rounding kernel and has not been refereed. |
| BGS-TRACE-196 | conditional | The pre-registered m = 17 predictions agree with the certificate to a relative 7.2e-5 / 4.5e-5. No tolerance was pre-registered, so this is a consistency check, not part of the closure condition. |
| BGS-TRACE-179 | refuted | Pointer only: the m = 17 certificate is evidence, not part of the refutation. |
| BGS-TRACE-206 | open | The full-kick part of the pre-registered test was evaluated and all 6 tests PASS (float). This is not a test of R′ (k1 kick). The k1 outcome is still not registered. |

## Not done
* No independent reproduction of the m = 17 certificate. The author kernel took 49 552 s.
* No ±4 residues at m = 17.
* The k1 m = 17 outcome (Line G REPORT §5, all 15 tests PASS) is not registered here.
* Prose notes (`resonant_residue_lineE.md`, the Line G note) are not edited. They still say "pending", and the claim annotations
  supersede them.
