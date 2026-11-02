# Wave 20, task 1 — milestone-2 elaboration probe (TEST COPY ONLY)

CONCISE note. No file in the main repository was touched, nothing pushed,
one sequential `lake build` at a time. Test-copy project:
`~/workspace/bgs-formalization/formalization/` (toolchain v4.33.1, Mathlib
v4.33.1 oleans prebuilt). The M2 draft itself was NOT modified by this
task (see the mid-session observation below).

## Verdict

The milestone-2 draft does NOT build as written, but it is exactly TWO
defects away from building (modulo `sorry` warnings): one blocking
command-order error (exact copy), and ONE error category — the same
`π r` type mismatch as milestone 1's `componentY_mod3`, occurring in
four theorems. Everything else elaborates.

## Defect 1 (blocking, exact copy): import after module docstring

File placed verbatim at `Bgs/Breakthrough/LemmaYM2.lean` in the test copy.
Build fails in under 7 s, before any name resolution:

- `error: LemmaYM2.lean:17:0: invalid 'import' command, it must be used
  in the beginning of the file`
- Cause (same as milestone 1): the draft's long `/-! ... -/` header is a
  module-doc command, and Lean requires `import` before every other
  command. The header must move below the import (or become a plain
  `/- -/` comment). This defect persists after the mid-session import
  correction below — it is about position, not the module path.

## Defect 2 (only error category in the probe): `π r` type mismatch × 4

Probe file `Bgs/Breakthrough/ProbeM2.lean`: draft with `import Mathlib`
first plus stub Derand definitions (mutual `pellX`/`pellY`, `Dm` as in
main's account, mirroring the wave-18 probe). Single sequential build:
906 s, 8706 jobs, `BUILD_EXIT: 1`, no olean. Exactly four errors, all
the same category — `∀ r` binds `r : ℕ` (from `classSum` /
`perClassMultiset`), but `π : Fin t → Fin t` is applied to it:

| probe line | theorem | expected type |
|---|---|---|
| 87:49 | `componentY_mod3pow` (Stage 3) | `Fin 4` |
| 114:38 | `componentY_mod2pow` (Stage 4) | `Fin (m.gcd 4)` |
| 137:42 | `pattern_mod32` (Stage 5) | `Fin 4` |
| 148:38 | `pattern_lemma` (Stage 5) | `Fin 4` |

Fix (diagnosis only, NOT applied here): the milestone-1 fix, applied
four times — bind `r : Fin t` and use `.val` on the class sums, as wave
19 task 1 did for `componentY_mod3`. Mathematical meaning unchanged:
the class sums / per-class multisets of `y'` are a dihedral permutation
of those of `y`.

## What elaborates

- All 7 definitions: `seqFrom`, `IsFix`, `classSum`, `seqMultiset`,
  `perClassMultiset`, `IsDihedral`, `block`.
- 8 theorems with only `sorry` warnings: `v3_Dm`, `scaling_div`,
  `scaling_bij`, `top_digit`, `alpha_pow`, `doubling`, `block_period`,
  `block_shift` (probe lines 49, 54, 61, 71, 91, 97, 118, 123).
- UNCHECKED spots from the draft header, now RESOLVED: the
  cross-modulus `ZMod` casts in `scaling_bij` (T3.1), `top_digit`
  (T3.2) and `doubling` (T4.2) all elaborate, as do the `Fin` /
  `Multiset` / `Finset` notations — same pattern as milestone 1, where
  every header-UNCHECKED spot resolved.

## Test-copy limitation (separate from defects 1–2)

This test copy is an old snapshot with NO Derand module at all, so the
real import line is unverifiable here regardless of path. The probe
uses `import Mathlib` + stubs, exactly as the wave-18/19 milestone-1
probes did.

## Mid-session observation: the draft's import line changed during the probe

The draft file on disk changed while the probe build was running
(mtime 2026-11-01 15:25 UTC): line 17 now reads the FLAT
`import Bgs.LineBDerand` (wave-6-verified), where the copy made at the
start of this task had the DOTTED `import Bgs.LineB.Derand`. That edit
was made by other work, not by this task; the probe is unaffected by it
(the probe replaces the import with `import Mathlib` + stubs either
way), and the exact-copy check was re-run against the corrected file
(defect 1 persists). The flat path now matches wave 6, but its
correctness against current main is for the import-verification work
to confirm, not this probe.

## Caveats

- Stubs are not main's definitions; if main's `Dm` differs in type from
  the stub (`Nat → Int`), statements using `(Dm m).toNat` need a cast
  check — same caveat as milestone 1's `pellQ`/`pellP`.
- All 12 proofs are `sorry`: this is statement well-formedness only,
  not a proof, and nothing here is for main until every `sorry` is
  replaced and `sorryAx = 0`.

## Files

- This note: `methods/wave20_task1_M2_elaboration.md`
- Exact copy (test copy only): `Bgs/Breakthrough/LemmaYM2.lean`
- Probe (test copy only): `Bgs/Breakthrough/ProbeM2.lean`
- Probe build log: `methods/wave20_probeM2_build.log`
