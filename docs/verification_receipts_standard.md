# Verification receipts standard (В.4 proposal)

> Status: PROPOSED by phase-7 В.4 (2026-10-25), staging only. Not yet
> adopted by the repo. Landing requires the usual per-push approval;
> adoption does not change any claim state, source, id or title, and
> does not touch the approved literal (93).

## 1. Purpose

Every verification gate in this repository must leave a receipt that a
third party can re-derive without trusting the reporter: one command,
one environment, one input snapshot, one output hash, one exit code.
A receipt is not a proof certificate (see `REPRODUCE_unified.md`: a
hash match or a passing check is not a proof of an asymptotic claim).
It is the minimum evidence that the check actually ran, on what, and
with what result.

## 2. Scope

This standard applies to:

- the `verify_workspace.py` runner surface (top-level
  `computations/verification/*.py` with `__main__`, the
  `spectral_diagnostics verify` item, all `computations/cpp` targets,
  and the two dependent replays);
- the CI/REPRODUCE gates (registry, repository, bibliographic,
  text-control, render `--check`, sync `--check`, manuscript-reference
  audit, wave2/wave3 integration audits, wave2/wave3 `--check-sources`,
  portable/full replays, fixed-map supplement, spectral corpus
  check/replay, unittest discover);
- any new checker added later: no new checker lands without a receipt
  template entry (command + negative control, §5).

Wolfram (`.wl`) checks are covered in form but not in execution on
machines without a Wolfram Engine: their receipts must say
`engine: unavailable` and must never be recorded as passes.

## 3. One receipt per gate run

One JSON object per gate run, written outside the source tree
(`build/` or an external logs directory — never into a committed
evidence directory, and never overwriting a committed receipt).
Field names are fixed; unknown fields are forbidden (a receipt with
extra fields fails schema validation, so a reporter cannot smuggle in
an unreviewed claim).

```json
{
  "schema": "bgs-verification-receipt-v1",
  "gate": "wave3_integration_audit",
  "command": ["python3", "computations/verification/wave3_integration_audit.py"],
  "command_line": "python3 computations/verification/wave3_integration_audit.py",
  "working_directory": "<repo root, as invoked>",
  "snapshot_commit": "5f234063aa8d4967c823c557ba1afcadfe229242",
  "snapshot_kind": "git-commit | archive-manifest-sha256 | local-bytes (uncommitted)",
  "source_tree_sha256": "<sha256 of the sorted path->sha256 manifest, or null if not computed>",
  "environment": {
    "platform": "<platform.platform()>",
    "python": "3.12.3",
    "python_flags": "PYTHONOPTIMIZE=0 (assertions on; -O runs are labelled, never silent)",
    "packages": {"numpy": "2.3.5", "sympy": "1.14.0", "mpmath": "1.3.0",
                 "matplotlib": "3.10.8", "scipy": "1.17.0"},
    "compiler": "c++ (GNU 13.3.0)",
    "boost_lib_version": "1_89",
    "pandoc": "3.12.1",
    "cmake": "3.28.x",
    "git": "2.x",
    "wolfram_engine": "available <version> | unavailable"
  },
  "input_hashes": {
    "record/claims.json": "<sha256>",
    "record/claim_integration_epochs.json": "<sha256>"
  },
  "output_hashes": {
    "stdout_log": "<sha256 of the full captured log file>"
  },
  "exit_code": 0,
  "status": "passed | failed | timeout | blocked | unavailable",
  "seconds": 12.4,
  "negative_control": {
    "case": "tampered hash: wave3_manuscript_mapping section_sha256 -> zeros",
    "tampered_exit_code": 1,
    "log_sha256": "<sha256>"
  },
  "notes": "Free text only for scope limits (e.g. 'byte/link checks; no proof audit'). Never for results."
}
```

Rules:

1. **Command is literal.** The `command` array is what was executed,
   from the repository root, with no shell interpolation. A receipt
   whose command differs from the documented one-command entry in the
   checker matrix is invalid.
2. **Environment is measured, not copied from requirements.**
   `requirements.txt` pins are the *required* environment; the receipt
   records the *observed* environment. A run under different package
   versions is a different receipt: it must say so, and it must not be
   presented as the pinned-environment result. The
   `verify_workspace.py` preflight (exact `==` pins) is the
   enforcement mechanism for the full runner; individual gates run
   outside the runner must still record observed versions.
3. **Snapshot commit is exact.** For a git checkout, the full 40-hex
   HEAD plus a dirty/clean flag. For an archive/ZIP snapshot, the
   SHA-256 of the archive manifest (`workspace_sources.py` schema
   `bgs-archive-source-manifest-v1`) and the explicit statement that
   no upstream commit is authenticated. Never synthesize a commit id
   for a partial overlay.
4. **Exit code is never rewritten.** Timeouts are `timeout`
   (runner code 124), spawn failures `blocked` (126/127), a missing
   engine or unmet pin `unavailable`. A gate that could not run is
   never recorded as `passed`, and a `failed` gate is never relabelled.
5. **Logs are hashed, not summarized.** The full stdout/stderr log is
   kept and its SHA-256 recorded. A receipt that cites only a tail
   excerpt is incomplete.
6. **No weakening.** A receipt template, a matrix entry, or a harness
   change must never lower a threshold, drop an assertion, enlarge a
   tolerance, or skip a pinned file to obtain a pass. Fixes go through
   the checker's own amendment/governance channel (claims channel,
   epoch amendments, reviewed pin translations), never through the
   receipt layer.

## 4. Negative controls (§5 of the matrix)

Every receipt for a gate that claims `passed` must name the negative
control that was run against the *same* gate on the *same* snapshot
(or the most recent snapshot on which the gate's inputs did not
change, with that snapshot named):

- **tampered hash** — one pinned SHA-256 replaced; gate must fail;
- **missing file** — one required input removed; gate must fail;
- **wrong count** — one declared count changed; gate must fail;
- **corrupted binding** — one binding/mapping entry altered; gate must fail;
- **forbidden byte / dangling reference** — for byte/reference audits;
- **mutation** — for self-contained computation checkers: one
  comparison flipped in a scratch copy; gate must fail.

A gate with no demonstrated negative control is listed as UNCOVERED
in the checker matrix and its receipts must say
`"negative_control": null` with `"status"` unchanged — the absence is
disclosed, never papered over.

## 5. Template receipt (copy, fill, hash)

```json
{
  "schema": "bgs-verification-receipt-v1",
  "gate": "<gate id from the checker matrix>",
  "command": ["<exact argv>"],
  "command_line": "<same command as one shell line>",
  "working_directory": "<repo root>",
  "snapshot_commit": "<40-hex HEAD or null for archive mode>",
  "snapshot_kind": "git-commit | archive-manifest-sha256 | local-bytes (uncommitted)",
  "source_tree_sha256": "<or null>",
  "environment": {
    "platform": "", "python": "", "python_flags": "",
    "packages": {"numpy": "", "sympy": "", "mpmath": "",
                 "matplotlib": "", "scipy": ""},
    "compiler": "", "boost_lib_version": "", "pandoc": "",
    "cmake": "", "git": "", "wolfram_engine": ""
  },
  "input_hashes": {},
  "output_hashes": {"stdout_log": ""},
  "exit_code": 0,
  "status": "passed",
  "seconds": 0.0,
  "negative_control": {"case": "", "tampered_exit_code": 0, "log_sha256": ""},
  "notes": ""
}
```

## 6. Where receipts live

- Per-run receipts: `build/receipts/<gate>-<date>.json` (git-ignored
  build output) or the CI artifact directory for that run.
- The checker matrix (which gates exist, their one-commands, their
  negative-control status, and their UNAVAILABLE dispositions) is the
  durable record: `record/checker_matrix_<date>.md`, refreshed only by
  a full В.4-style re-sweep, never by hand-editing a single row.
- Historical evidence under `evidence/` and `archive/` is never
  rewritten to satisfy this standard; a historical run keeps its
  original receipt format, and any gap is disclosed in the matrix.

## 7. Known environment deviations (2026-10-25, this VM)

Recorded here so that future receipts are not misread:

- This VM's system Python stack (numpy 1.26.4, sympy 1.12, mpmath
  1.2.1 by module version — importlib metadata reports 0.0.0 for it,
  scipy 1.11.4, matplotlib 3.6.3) does **not** match `requirements.txt`
  (numpy 2.3.5, sympy 1.14.0, mpmath 1.3.0, scipy 1.17.0,
  matplotlib 3.10.8). The full `verify_workspace.py` run therefore
  fails its own version preflight on this VM before any check runs.
  Individual gates that pass under 1.26.4 are valid *observed-1.26.4*
  results, not pinned-environment results. (Local pandoc is 3.12.1,
  matching the sync pin; local Boost headers are 1_89; cmake 3.28.3;
  git 2.43.0; Python 3.12.3.)
- `resonant_density_audit.py` is a pinned-numpy-2 gate by
  requirements; its behaviour under 1.26.4 must be reported per-run
  (see the В.4 matrix), never assumed.
- The Wolfram Engine is unavailable on this VM (no Wolfram ID);
  all 28 `.wl` checks are UNAVAILABLE here, not failed and not passed.
- The 2-vCPU box times out the heavyweight exact checks first:
  `collective_diffusion_gap.py` (Hardy block) and
  `imported_finite_controls/hardy/verify_hardy.py` are timeout risks
  at the runner's 360 s budget; their receipts must carry the
  declared budget and the observed seconds, and a timeout is a
  `timeout`, never a pass.
