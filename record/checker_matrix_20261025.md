# Checker matrix — phase-7 В.4 (2026-10-25)

> Snapshot: `ChurilovMaksim/BGS` main HEAD
> `5f234063aa8d4967c823c557ba1afcadfe229242` (V2 waves 1A–6 + L6).
> Staging only in В.4; landing requires the usual per-push approval.
> This document changes no claim state, source, id or title, and does
> not touch the approved literal (93 epoch amendments; 199 claims =
> 173 proved / 12 verification-pending / 9 conditional / 5 open).
> Method, full baseline/mutation tables and live-blob evidence: the
> В.4 report (`bgs_rework_exec/phase7_v2/remainder/v4/REPORT.md` in the
> coordinator's workspace; the machine-readable CSVs are staged under
> `logs/` next to this matrix's delivery, not in the repo).
> Environment of the sweep: Python 3.12.3, numpy 1.26.4, sympy 1.12,
> mpmath 1.2.1, scipy 1.11.4, matplotlib 3.6.3, pandoc 3.12.1 (via
> `~/.local/bin`), Boost headers 1_89, cmake 3.28.3, git 2.43.0, 2 vCPU.
> `requirements.txt` pins differ (numpy 2.3.5, sympy 1.14.0, mpmath
> 1.3.0, scipy 1.17.0, matplotlib 3.10.8) — see §5.1: receipts from this
> sweep are *observed-1.26.4* results, not pinned-environment results.

## 1. Universe

446 inventoried files: Tier A runner surface 236 (206 top-level
`computations/verification/*.py` loop items + `spectral_diagnostics
verify` + 27 C++ targets + 2 dependent replays), top-level no-main
modules 3, subdir verification files 104 (62 with `__main__`, 42
without), maintenance files 19, maintenance tests 38, Wolfram files
28, supplement verifiers 2, analysis files 10, `python/bgs` library
files 6. Checker denominator for negative controls = files with a
documented standalone one-command: Tier A (236) + the 17 non-runner
Tier-1 gates of §2 + the 15 imported-controls tasks of §4.

## 2. Tier-1 gates: one-command + negative control

Commands run from the repository root unless noted. "Demonstrated"
means baseline exit 0 and tampered exit nonzero on a scratch copy,
with tampered bytes restored and verified by SHA-256. The
reproducible harness is `computations/maintenance/
v4_negative_controls.py` (maintenance dir on purpose: the runner only
discovers `verification/` top-level files, so the harness does not
change the 236-item surface).

| Gate | One-command | Negative control (tamper → exit) | Verdict |
|---|---|---|---|
| Registry audit | `python3 computations/verification/scientific_registry_audit.py` | Missing file: one claim source deleted → 1 | Demonstrated |
| Repository audit | `python3 computations/verification/repository_audit.py` | Corrupted tree: forbidden `.jl` file added → 1 | Demonstrated |
| Bibliographic audit | `python3 computations/verification/bibliographic_metadata_audit.py --self-test` | Tampered hash: byte appended to digest-pinned metadata cache → 1 | Demonstrated |
| Text-control audit | `python3 computations/verification/text_control_audit.py` | Forbidden byte: NUL appended to `README.md` → 1 | Demonstrated |
| Render claim registry | `python3 computations/maintenance/render_claim_registry.py --check` | Tampered view: marker in `record/claim_registry.md` → 1 | Demonstrated |
| Render errata | `python3 computations/maintenance/render_errata.py --check` | Tampered view: marker in `ERRATA.md` → 1 | Demonstrated |
| Render status | `python3 computations/maintenance/render_status.py --check` | Tampered view: marker in `STATUS.md` → 1 | Demonstrated |
| Render bibliography | `python3 computations/maintenance/render_bibliography.py --check` | (a) Comment line appended → 0, INSENSITIVE for that tamper (canonical form ignores comments); (b) first `\bibitem` key renamed (`BGS1984` → `v4-nonexistent-key`) → 1 | Demonstrated (key rename) |
| Render research views | `python3 computations/maintenance/render_research_views.py --check` | Tampered view: marker in `record/scientific_dependency_graph.md` → 1 | Demonstrated |
| Render spectral research | `python3 computations/maintenance/render_spectral_research.py --check` | Baseline red (4 stale topic views); tamper adds a 5th stale view | Baseline-red, sensitivity shown |
| Sync finite-orbit | `python3 computations/maintenance/sync_finite_orbit_section.py --check` | Guarded skip (exit 0, SKIP message); write mode refuses (exit 1) | Demonstrated (refusal) |
| Sync fixed-map | `python3 computations/maintenance/sync_fixed_map_section.py --check` | Guarded skip (exit 0, SKIP message); write mode refuses (exit 1) | Demonstrated (refusal) |
| Sync return sections | `python3 computations/maintenance/sync_return_sections.py --check` | Requires pandoc 3.12.1 on PATH (see §5.4); PATH-fixed: `--check` exit 0 (SKIP), write mode refuses exit 1 | Demonstrated (refusal) |
| Manuscript references | `python3 computations/maintenance/audit_manuscript_references.py --check` | Corrupted binding: dangling `\cite{v4-nonexistent-key}` → 1 | Demonstrated |
| Wave2 `--check-sources` | `python3 computations/verification/wave2_portable_replay.py --check-sources` | Tampered pin: wave2 contract bytes altered → 1 | Demonstrated |
| Wave3 `--check-sources` | `python3 computations/verification/wave3_checked_replay.py --check-sources` | Wrong count: `declared_check_count` 72 → 999 → 1 | Demonstrated |
| Wave2 integration audit | `python3 computations/verification/wave2_integration_audit.py` | Corrupted binding: one scoped pin SHA flipped → 1 | Demonstrated |
| Wave3 integration audit | `python3 computations/verification/wave3_integration_audit.py` | Tampered hash: mapping `section_sha256` → zeros → 1 | Demonstrated |
| Fixed-map supplement | `python3 computations/maintenance/verify_fixed_map_supplement.py --audit-only` | Baseline red: inventory hash mismatch, 2 files (§5.2) | Baseline-red |
| Spectral corpus check | `python3 computations/maintenance/rebuild_spectral_corpus.py --check` | Baseline red: 3 projection mismatches; tamper adds a 4th (§5.2) | Baseline-red, sensitivity shown |
| Spectral corpus replay | `python3 computations/verification/replay_spectral_corpus.py --output-dir <outside-tree>` | Baseline red: 55/56 passed (§5.2) | Baseline-red |
| Spectral edition | `python3 computations/verification/check_spectral_edition.py` | Baseline red: stale path crash (§5.3); missing-input variant (`--known-tree` nonexistent) fails at the known-tree read → 1 | Baseline-red; missing-input demonstrated |
| Trace closure (`-O`) | `python3 -O computations/verification/trace_closure_checks.py` | Baseline pass; NC via Tier-A mutation sweep | See §3 |
| Unittest suite | `python3 -m unittest discover -s computations/maintenance/tests -q` | Gate-script runs timed out at 600 s (exit 124) baseline and tampered — no verdict yet; 1800 s re-run in report §5 | See report |
| Wave2 portable replay | `python3 computations/verification/wave2_portable_replay.py --output-dir <outside-tree>` | Baseline only; NC via `--check-sources` + integration audit | See report |
| Wave3 checked replay | `python3 computations/verification/wave3_checked_replay.py --output-dir <outside-tree>` | Baseline only; NC via `--check-sources` + integration audit | See report |
| Imported integration | `python3 computations/verification/imported_finite_controls/verify_integration.py --output <outside-tree>` | Baseline red: stale manifest paths (§5.3) | Baseline-red |
| Locality packet | `python3 computations/maintenance/verify_locality_packet.py --build <build> --logs <logs> --output <json>` | ⚠ Writes 3 outputs into `evidence/certificates/` inside the tree it runs on — run only on a disposable copy, never on the live tree. Disposable-copy run: FAIL, 33/35 pass; nonpasses are `spectral_diagnostics` (exit 124 at the packet's 180 s budget) and `cpp_resonance_complex_replay` (exit 2, bare-arg gap) | Aggregate FAIL (2 items, both dispositioned in report §5) |
| Full runner | `python3 computations/maintenance/verify_workspace.py --build <build> --logs <logs> --output <json> [--archive-manifest <manifest>]` | UNAVAILABLE on this VM: version preflight (§5.1) | Unavailable |

## 3. Tier-A runner surface: baseline + mutation

Baseline (runner-equivalent commands, 240 s budget, 900 s for
`research_checkpoint_replay`): **236 items → 220 pass, 9 fail,
7 timeout**. Both dependent replays passed
(`check_resonance_certificate` 0.6 s, `extremal_independent_replay`
1.2 s); C++ 26/27 pass; `research_checkpoint_replay` passed in
383.4 s. The 9 fails: 3 environment-blocked (sympy 1.12 ×2, numpy
1.26 `trapezoid` ×1), 3 red on main (stale path ×2, stale pin ×1),
3 runner-mapping gaps (bare command can never pass — true commands
in report §4.4: margin PASS 1.1 s, complex replay `8` PASS 0.3 s,
corpus replay 55/56 red). The 7 timeouts at 240 s, re-run at 360 s:
4 pass (fixed-harmonic 116.2 s, fractional 2_3 166.4 s, fractional
3_2 162.8 s, intermediate-old-layers 89.3 s), 2 timeout at 360 s
(spectral-smoothing, spectral-diagnostics), 1 self-limit SIGKILL
(factorial-diagonal, own `RLIMIT_CPU 280`).

Mutation negative controls, four rounds (report §4.3 for method and
round history): **220 demonstrated of 236** — COVERED 200,
COVERED-BY-GATE-NC 9, COVERED-BY-DELEGATED 10,
COVERED-BY-DEPENDENT 1 (`cpp_extremal_resonance_replay` bare, via
its dependent replay). **No INSENSITIVE and no NO-MUTATION-FOUND
rows remain.** The 16 rows without a demonstrated NC are exactly
the baseline-not-pass rows (report §8): 3 env-blocked, 3 red on
main, 3 arg-gaps (2 of which pass on their true command but have
no broken-input run yet), 3 timeout/self-limit, 4 pass-at-360
items that were timeouts at sweep time and so were never mutated.
Machine-readable verdicts: `logs/mutation.csv` (staged with this
matrix's delivery).

## 4. Imported-controls tasks (15, `tasks.json` commands)

14 pass, 1 timeout (disposable copy, `tasks.json` commands):

| Task | Seconds | Verdict |
|---|---|---|
| audit | 8.8 | pass |
| filters | 8.0 | pass |
| coboundary | 0.2 | pass |
| mesoscopic | 0.1 | **VACUOUS-STANDALONE** (no `__main__`, zero checks run; historical receipt equally vacuous, empty `outputs_sha256`) |
| agent_audit | 0.3 | pass |
| root_lift | 10.3 | pass |
| closure | 1.1 | pass |
| scaled_overlap | 12.0 | pass |
| cue_covariance | 8.3 | pass |
| deaveraging | 1.2 | pass |
| edge_occupation | 0.6 | pass |
| collision | 3.3 | pass |
| bounded_secular (`--sizes 19,31`) | 0.7 | pass |
| deleted_clock (`verify_final_attempt.py`) | 0.2 | pass |
| hardy | 180.0 | **TIMEOUT** at its `tasks.json` budget; also times out at 360 s standalone (§5.5) |

The receipt checker `verify_integration.py` does NOT execute these
tasks; it verifies the 20261016 receipt pins (baseline red, §2).

## 5. UNAVAILABLE dispositions (exact reasons)

### 5.1 Full runner — version
`verify_workspace.py` preflight exit 2 (archive-manifest mode, Boost
include supplied): numpy 2.3.5 vs 1.26.4; sympy 1.14.0 vs 1.12; mpmath
1.3.0 vs 0.0.0 (metadata; module 1.2.1); matplotlib 3.10.8 vs 3.6.3;
scipy 1.17.0 vs 1.11.4. No check runs under the runner on this VM.

### 5.2 Supplement inventory + spectral projections — stale pins (red on main)
See report §6.1–6.2. Governed regen required; not weakened, not
staged.

### 5.3 Stale Phase-2 paths — red on main
`check_spectral_edition.py` (`mathematics/
coordinate_return_quartic_20261021.md` vs relocated
`mathematics/fixed-map/coordinate_return_quartic.md`),
`exact_homoclinic.py` (binding `public_path`
`mathematics/four_branch_parametrix.md` vs byte-identical relocated
file, SHA `c696ebd…`), `verify_integration.py` (11 manifest
`canonical_path`s `mathematics/*_20261015.md` vs relocated
`mathematics/fixed-map/*.md`). Governed Wave-6-style path refresh
required; not staged.

### 5.4 Sync return sections — pandoc PATH
`sync_return_sections.py` requires pandoc 3.12.1 on PATH
(`require_pandoc()`); on this VM pandoc lives at `~/.local/bin/pandoc`
and is not on the default PATH, so the first sweep run failed before
any check. PATH-fixed re-measurement (report §5): `--check` exit 0
(SKIP for hand-edited chapters), write mode refuses exit 1. The
one-command for this gate must therefore include
`PATH="$HOME/.local/bin:$PATH"` on this VM (CI installs pandoc
3.12.1 via the pinned .deb).

### 5.5 Hardy verifiers — budget
`verify_hardy.py` standalone times out at 180 s (its `tasks.json`
budget) AND at 360 s (runner budget, exit 124), on bytes identical
to the 20261016 receipt source (SHA `26cea639…`, historical PASS
9.7375 s with `python3 -O`). The file has zero `assert` statements,
so `-O` cannot explain 9.7 s → >360 s: environment/machine slowdown,
not a checker regression. `collective_diffusion_gap.py` (own
`hardy_checks` block) passes in 23.0 s inside its Tier-A item, so the
risk is the standalone task only. Disposition: TIMEOUT-AT-360 on this
VM; governed budget decision, never shrink the check.

### 5.6 Wolfram (28 files) — engine
No Wolfram Engine on this VM. All `.wl` files are UNAVAILABLE here:
not passed, not failed.

## 6. UNCOVERED list

No Tier-A INSENSITIVE or NO-MUTATION-FOUND rows remain. UNCOVERED =
the 16 baseline-not-pass Tier-A rows (report §8: 3 env-blocked, 3
red on main, 3 arg-gaps, 3 timeout/self-limit, 4 pass-at-360 never
mutated) + Tier-B individual standalones with a baseline pass but
no NC (`verify_wick_poisson`, `fractional_hamming/
synthesis_checks`, `pair_probe` 137.2 s) + the 15 imported-controls
tasks (no individual NC; receipt + `verify_integration` pin check
itself red) + Tier-1 baseline-red gates (supplement audit, spectral
corpus check/replay, spectral-research views, spectral edition
bare, `verify_integration`, `verify_wick_integration` — stale
20261016 README pin). Subdir modules without a standalone command,
maintenance builders, no-main modules, library primitives and
figure generators are not checkers and are listed separately in
report §8, never counted. Wolfram (28 files) is UNAVAILABLE (§5.6),
not uncovered-by-omission. `mesoscopic` is VACUOUS-STANDALONE (§4):
there is no check there to control.

## 7. Receipts standard

See `docs/verification_receipts_standard.md` (staged with this
matrix): schema `bgs-verification-receipt-v1`, literal command,
measured environment, snapshot commit or archive-manifest SHA, input /
output SHA-256s, unrewritten exit code, negative-control case. No
weakening rule (§6 of that document).
