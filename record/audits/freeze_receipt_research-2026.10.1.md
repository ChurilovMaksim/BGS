# BGS research release — freeze receipt

Tag: `research-2026.10.1` · Freeze commit: `491a2425` ·
Tree SHA-256: `8a881a2945290f95861617c8e6326124d457d07829130f941a8e62be0b206867`

Frozen scientific state of the BGS research corpus. This receipt records
what was checked, not a claim that the BGS conjecture is proved —
BGS-001 remains open.

## Freeze chain

- `27f4caf` — seal-gate AGENTS.md text (phase-7 seal-gate re-baseline).
- `15e3bf13` — phase-5 G8 fix: declared args for 3 `verify_workspace`
  checks (236/236).
- `cf096f39` — phase-5 license package (8 files, layered licensing R3).
- `491a2425` — REPRODUCE archive-recipe note (`--logs` must point
  outside the repository). **The tag points at this commit.**
- Note: live `main` has since moved to `058086f1` (Ф.3 batch 2,
  Fm001/Fm021 statements). This receipt lands as a follow-up commit on
  current main after tagging; it does not re-freeze the tree.

## C1 gates re-run on the freeze tree (all green)

| Gate | Outcome |
|---|---|
| G1 registry audits (7 commands) | exit 0 — 199 claims, schema bgs-claims-v1; biblio 515 mutation tests, 57 identities; all renders OK |
| G2 repository audit | exit 0 — PASS all lines |
| G3 RC replay | exit 0 — manifest `passed`, 11/11 tasks |
| G4 wave2 portable replay | exit 0 — manifest `passed`, 8 tasks |
| G5 wave2 integration audit | exit 0 — `passed` (immutable 92, prepared 85, pins 50, prior 96, amended 93) |
| G6 wave3 integration audit | exit 0 — `passed`, L8 counts [72, 227, 1486, 8708] MATCH, Wave2_section_unchanged true |
| G7 closure / scoped | exit 0 |
| G8 C++ verifiers | exit 0 — cmake 3.28.3 + build 100%, compileall 0, supplement 28/28 PASS, verify_workspace 236/236, source_tree_unchanged true, archive mode |
| G9 Lean | exit 0 — 3073 jobs, 0 sorry, 0 errors, 27 modules, toolchain v4.33.1 |
| G10 manuscript | exit 0 — syncs SKIP (TeX source of truth); refs 611 labels / 238 refs / 0 unresolved / 0 duplicate; build PASS, 343 pp |
| G11 full test discover | exit 0 — 251 tests in 371.4 s, OK |

## C2 tree hash

Method: SHA-256 over a canonical listing from the archive manifest
(`workspace_sources.py`, schema `bgs-archive-source-manifest-v1`,
6730 files), sorted by POSIX path, one line per file in `sha256sum`
format (`<sha256>  <relpath>`), concatenated and hashed.

Tree SHA-256: `8a881a2945290f95861617c8e6326124d457d07829130f941a8e62be0b206867`

## C3 manuscript PDF

- Tracked `manuscript/BGS_unified.pdf`: git blob `fcc03478…`
  (unchanged by this run).
- Fresh build from the freeze tree: git blob `c3d9f563…`, pdf_sha256
  `912a003895c3bc92d230b103f2a5e5163072298f1f8fc5bc0ba54f1ea6ca1928`,
  343 pages, 2511192 bytes. Attached to the Release (not committed
  over the tracked file).
- pdftotext diff tracked vs fresh: **0 lines** (33,431 lines each) —
  content identical, metadata-only drift (each build embeds timestamps,
  so rebuild hashes differ run to run). No tracked-PDF churn, per the
  parent decision.

## Registry at freeze

199 claims = 173 proved / 12 verification-pending / 9 conditional /
5 open, schema `bgs-claims-v1`.

- Open (5): BGS-BGS-001, BGS-CAYLEY-005, BGS-INFO-001, BGS-RES-003,
  BGS-TRACE-005.
- Verification-pending (12): BGS-CAYLEY-003, BGS-RES-022,
  BGS-TRACE-055, BGS-TRACE-096, BGS-TRACE-098, BGS-TRACE-099,
  BGS-TRACE-100, BGS-TRACE-101, BGS-TRACE-102, BGS-TRACE-103,
  BGS-TRACE-104, BGS-TRACE-105. (RES-022 not promoted; promotion is a
  separate gated decision.)
- Conditional (9): BGS-FM-004, BGS-FM-033, BGS-LOOP-001, BGS-RES-014,
  BGS-RET-003, BGS-TRACE-060, BGS-TRACE-073, BGS-TRACE-095,
  BGS-TRACE-097.

## Phase-7 scope (Route A)

Phase 7 complete, including remediation dispositions: receipt linkage
for the 11 proved-unevidenced rows, 9 red checker units fixed, 4
environment-blocked units passing in the pinned environment, G8
runner-mapping fix, seal-gate Q1 settled (checked-red /
portable-green). No downgrades were proposed or applied.

## Lean formalization honesty note

Full-tree build (27 modules at freeze): 92 `#print axioms` lines =
61 involving `native_decide` axioms + 31 standard-only. The full build
is therefore NOT standard-axioms-only; that claim holds for the Ф.3
batch modules, not the whole tree. TRACE-005 is statement only.
Formalization continues after this release (Ф.4 full coverage per
plan); at freeze time live main already carries 29 modules (Ф.3
batch 2 landed after the freeze commit).

## Pinned environment

Python 3.12.3 (system) · pinned venv: numpy 2.3.5, sympy 1.14.0,
scipy 1.17.0, matplotlib 3.10.8, mpmath 1.3.0 · cmake 3.28.3 ·
Boost 1.89.0 · TeX Live 2026 · pandoc 3.12.1 · Lean v4.33.1 ·
Mathlib `0df444a360ea`.

## Known-unavailable checks

- GitHub Actions: account billing block (runs die in 2–4 s, never
  start); re-run scheduled 2026-11-02 (CI debt list).
- Checked replay exit 1 on `changed source: AGENTS.md` — Q1-settled
  per disposition #174, not a gate.
- 3 resource-blocked units (2 timeouts-at-360, 1 RLIMIT_CPU
  self-limit-kill) — checks never shrunk to pass.
- Mesoscopic vacuity (structural, helper-only file, no `__main__`).
- 28 Wolfram files without an engine on this VM.

## Decisions (D2–D8, confirmed by the user 2026-10-26)

D2 tag `research-2026.10.1` · D3 MIT line "Copyright (c) 2026 Maksim
Churilov" · D4 CFF = MIT, Zenodo = CC-BY-4.0 · D5 full ID lists ·
D6 GitHub Release + tag via owner browser · D7 V2 §8 Q4 reading
confirmed (Wave 3 first-ever runs of the 5 never-run tasks + 8/8
portable replay close "execution of the two Wave 2/3 replay
experiments by other means") · D8 receipts in-repo under
`record/audits/`.

## Release status (recorded at receipt landing)

Tag `research-2026.10.1` points at
`491a2425c39778f8155cd10b2ca3b49ffab9d690` (verified via API).
Release published (not a draft, not a prerelease):
https://github.com/ChurilovMaksim/BGS/releases/tag/research-2026.10.1
— notes verbatim from the C4 draft, asset
`BGS_unified_fresh_build.pdf` 2511192 bytes, sha256
`912a003895c3bc92d230b103f2a5e5163072298f1f8fc5bc0ba54f1ea6ca1928`.

What remains: Zenodo DOI only after Zenodo issues one (no DOI is
claimed until then) → CI catchup 2026-11-02.

## License

Code MIT (`LICENSE`), texts/data CC BY 4.0
(`LICENSE-CC-BY-4.0.txt`); per-path map in `LICENSE_POLICY.md`.
