# Era-baseline attestation — the held 20261016 integration packets

**Date:** 2026-10-23. **Scope:** `evidence/executions/20261016/abel-gaussian`
and `evidence/executions/20261016/wick-poisson`, the two integration-verifier
packets landed on 2026-10-16 and held from phase-1 archiving. **Method:**
era-baseline re-execution under the packets' original, untouched pins
(`--baseline-tree`), as proven by the phase-7 pin census
(`p7_20261016_work/CENSUS.md` in the rework workbench) and re-run end-to-end
for this attestation. This attestation **does not modify** the 20261016
manifests or any packet file, and it supersedes nothing: the packets remain
immutable provenance for their own revision.

## Why the pins fail on the current tree

The two integration verifiers check 97 sha256 pins. On the current tree 45
fail — 43 stale and 2 missing — **all inside the two `source_manifest.json`
files**; every execution-layer pin (abel receipt 19/19, C++ 2/2, wick exact
manifest 5/5, the shared historical-provenance pin) still verifies, and no
packet-science file is stale. The census attributed every stale pin to a
breaking commit; the classes are (a) editorial/path-only change and
(b) content growth of a shared context file by later programme results.
Class (d), unexplained drift: **zero pins**.

- `84a06b056` (2026-10-16, the Wick landing, 33 minutes after the abel
  manifest's last edit) broke 18 abel pins by registering BGS-TRACE-094.
- `c49e351f3` (2026-10-19, phase-cluster wave) broke 14 wick pins and 1 abel
  pin by registering BGS-TRACE-096…105.
- `0db5021c1` (2026-10-20 reconcile) broke 4 wick pins (small verification-
  guard and documentation edits, including the snapshot-doctrine note
  itself); `6974bb490` (science repair) 1 wick pin (proof-environment titles
  only); `7fb99b4d7` (spectral corpus) 1 wick pin (one header line).
- The rework's share is 3 pins: package D (`6c2ec7c6a`, 2026-10-22) migrated
  `record/history` → `archive/history` references, one of them inside
  `verify_integration.py` itself (a change the verifier required to keep
  working). The phase-3 disclosure footnote `bb1513a32` broke **no** pin —
  both README pins were already stale; this corrects the earlier record.
- The 2 missing pins are class (c): package F-2 relocated
  `record/research_continuation_20261016.md` and
  `record/wick_poisson_continuation_20261016.md` to `archive/record/…` as
  byte-identical copies; the digests still match at the new paths.

The staleness is by recorded design: the verifier home's README states
"This is a dated snapshot check: do not refresh historical hashes to admit
later editorial revisions." Re-pinning is therefore not a repair; the
doctrine-compliant attestation is the era-baseline re-execution below.
Downstream, nothing is affected: BGS-TRACE-092/093/094 (all `proved`,
analytic proof primary) name the finite scripts — not the integration
verifiers — in their `verifiers[]`, and their evidence files are byte-intact
with all internal pins green.

## Era-baseline method

Each verifier accepts `--baseline-tree <inventory.json>`, where the
inventory's `commit` must equal a hardcoded constant (abel `b425a361…`,
wick `f78ec82f…`) and supplies **path existence only**; pin digests are
always checked against local bytes. An era tree was assembled from the
current tree by restoring era bytes — fetched from git history at the
packet's landing commit (abel ⇔ tree @ `f78ec82f…`, 2026-10-16 13:52 UTC;
wick ⇔ tree @ `84a06b05…`, 2026-10-16 14:25 UTC) — for everything the
verifier *reads*: the pin-true overlay of every manifest path, the era
registry auditor (`scientific_registry_audit.py`, sha256 `27c9a394…` in
both eras), the era registry files and claim sources, an era-consistent
`mathematics/` set (post-era notes removed: 17 files for abel, 16 for
wick), the pre-package-D `record/history/2026/chat_20261015/` provenance
copies the era abel script reads, and for wick the era manuscript
(`BGS_unified.tex` + all `unified_sections/*.tex` at `84a06b05…`; 45 files
restored, 4 post-era sections removed), which its TeX stage audits.

The era-local content of each tree — every file whose bytes differ from,
or are absent in, the current tree — is inventoried with sha256 digests in
`era_files_abel.json` (216 files) and `era_files_wick.json` (259 files),
together with the lists of files removed relative to the current tree.
Fourteen files per tree were additionally spot-verified against live git
history through the GitHub read tools at the era commits: in all 28 cases
the git blob SHA reported by the API and the fetched bytes match the era
tree exactly (`spot_checks.json`). The verifier-format inventories
actually used are deposited as `inventory_abel.json` /
`inventory_wick.json` (10,193 entries each; both era trees converge to the
same path set under the recipe tree ∪ 20261016 provenance keys ∪
archive-prefix-stripped paths, and the files differ in the `commit`
constant).

## Re-run results (2026-10-23, original pins)

| Run | Status | Claims | Ext. deps | Source pins | Finite tasks | Changed-Markdown files |
|---|---|---:|---:|---:|---:|---:|
| abel `verify_integration.py --baseline-tree` | **PASS** | 147 | 49 | 39 | 6 | 20 |
| wick `verify_wick_integration.py --baseline-tree` | **PASS** | 148 | 50 | 31 | — | 16 |

The full verifier outputs are deposited as `abel_baseline.json` and
`wick_baseline.json`. Both runs also report
`historical_source_bytes_preserved: true`.

One metric differs from the census's first proof and is recorded for
honesty: the census reported 67 remote-only path checks per packet with
inventories of 10,209 / 6,974 entries. These era trees carry more era files
locally (the era sweeps were retried until success — the digest inventories
above), so only 21 (abel) / 22 (wick) existence checks needed the remote
inventory. Every scientific output — status, claim counts, pin counts,
finite tasks — is identical.

The finite science also re-executes on the current tree (fresh run,
2026-10-23, Python 3.12.3 / sympy 1.12):

- `run_checks.py`: **6/6 tasks PASS**; five of six `result.json` files
  reproduce the deposits byte-for-byte. `symbolic_mean` differs in exactly
  one field, `sympy_version` (deposited 1.14.0, local 1.12); all
  mathematical content is identical.
- `verify_wick_poisson.py`: **PASS**, output byte-identical to the
  deposited `exact/result.json`.

## Caveats

- Baseline mode attests the packets against their own era, not against the
  current tree. Current-tree integration is governed by the standing
  registry, repository and navigation gates.
- The C++ replay (`cpp_replay.json`, pins still green) and the Wolfram
  artefacts (`abel_identity.wl`, `wolfram_result.json`) are carried as
  deposited provenance; neither was re-executed for this attestation (no
  Wolfram Engine is available in this environment, and a fresh C++ replay
  is a new execution by the packet README's own warning).
- The wick verifier rewrites `manuscript_checks.json` inside its packet on
  every run; in the era tree it regenerated the era counts (104 input
  files, 519 labels, 70 bibliography keys, 54 cited keys). That file is a
  run output, not an era input, and is excluded from `era_files_wick.json`.
- If a future checkpoint of the *current* state is wanted, it must be
  minted as a new dated manifest; the 2026-10-16 manifests stay untouched.

## Files in this directory

| File | Content |
|---|---|
| `report.md` | This attestation. |
| `abel_baseline.json`, `wick_baseline.json` | Verifier outputs of the 2026-10-23 era-baseline re-runs (both PASS). |
| `inventory_abel.json`, `inventory_wick.json` | The `--baseline-tree` inventories used (path existence; `commit` = the verifier's era constant). |
| `era_files_abel.json`, `era_files_wick.json` | Era-local files per tree with sha256 digests, plus files removed relative to the current tree. |
| `spot_checks.json` | 28 spot verifications against live git history at the era commits (blob SHAs and byte equality). |
