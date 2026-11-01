#!/usr/bin/env python3
"""Reproducible negative controls for the Tier-1 gates (phase-7 В.4).

Usage (from a scratch COPY of the repository -- never the live tree):

    python3 computations/maintenance/v4_negative_controls.py \
        --tree /path/to/scratch-copy --logs /tmp/v4-nc-logs

For each gate the harness runs the baseline (expect exit 0), applies
ONE broken-input tamper to the scratch copy only, re-runs (expect
nonzero), then restores the tampered bytes and verifies restoration
by SHA-256. It never writes to the source tree it was invoked from,
never changes a claim, and never weakens a check: a gate that does not
fail on its tamper is reported INSENSITIVE, not patched into passing.

Gate list (tamper type in brackets):
  registry_audit           [missing file: one claim source deleted]
  repository_audit         [corrupted tree: forbidden .jl file added]
  bibliographic_audit      [tampered hash: byte appended to digest-pinned cache]
  text_control_audit       [forbidden byte: NUL appended to README.md]
  render_*_check (x7)      [tampered generated view: marker appended]
  frozen_packets_check     [tampered pin: byte appended to a frozen packet file]
  sync_* write refusal (x3)[guard: write mode on hand-edited target refuses]
  manuscript_references    [corrupted binding: dangling citation key]
  wave2_check_sources      [tampered pin: wave2 contract bytes altered]
  wave3_check_sources      [wrong count: declared_check_count 72 -> 999]
  wave2_integration_audit  [corrupted binding: one scoped pin sha flipped]
  wave3_integration_audit  [tampered hash: mapping section_sha256 -> zeros]
  fixed_map_supplement     [missing file: one inventory file deleted]
  spectral_corpus_check    [tampered projection: bytes appended to a source]
  spectral_corpus_replay   [same tamper, fresh output dir]
  spectral_edition_missing [missing input: --known-tree nonexistent]
  unittest_discover        [suite sensitivity: failing test file added]

The full runner-surface mutation sweep (one flipped comparison per
checker, В.4) is a heavier procedure documented in
record/checker_matrix_20261025.md; it is not re-run by this harness.
This file lives under computations/maintenance/ deliberately: the
verify_workspace.py runner only discovers computations/verification/
top-level files, so adding this harness does not change the runner
surface (237 items).
"""
from __future__ import annotations
import argparse, hashlib, json, os, shutil, subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def run(argv, cwd, env, timeout=600):
    t0 = time.monotonic()
    try:
        r = subprocess.run(argv, cwd=cwd, env=env, text=True,
                           capture_output=True, timeout=timeout)
        return r.returncode, (r.stdout + r.stderr)[-2500:], round(time.monotonic() - t0, 1)
    except subprocess.TimeoutExpired:
        return 124, "[TIMEOUT]", timeout


class Case:
    def __init__(self, tree: Path, logs: Path):
        self.tree = tree
        self.logs = logs
        self.backups: dict[str, bytes | None] = {}

    def backup(self, rel: str) -> None:
        p = self.tree / rel
        self.backups[rel] = p.read_bytes() if p.is_file() else None

    def restore_all(self) -> bool:
        ok = True
        for rel, orig in list(self.backups.items()):
            p = self.tree / rel
            if orig is None:
                if p.exists():
                    p.unlink()
            else:
                p.write_bytes(orig)
            if (p.read_bytes() if p.is_file() else None) != orig:
                ok = False
        self.backups.clear()
        return ok


def append_text(case: Case, rel: str, text: str):
    def f():
        case.backup(rel)
        p = case.tree / rel
        p.write_text(p.read_text() + text)
    return f


def append_bytes(case: Case, rel: str, data: bytes):
    def f():
        case.backup(rel)
        p = case.tree / rel
        p.write_bytes(p.read_bytes() + data)
    return f


def delete_file(case: Case, rel: str):
    def f():
        case.backup(rel)
        (case.tree / rel).unlink()
    return f


def create_file(case: Case, rel: str, data: bytes):
    def f():
        case.backup(rel)
        (case.tree / rel).write_bytes(data)
    return f


def edit_json(case: Case, rel: str, mutate):
    def f():
        case.backup(rel)
        p = case.tree / rel
        data = json.loads(p.read_text())
        mutate(data)
        p.write_text(json.dumps(data, indent=2) + "\n")
    return f


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--tree", type=Path, required=True,
                    help="Scratch copy of the repository (NOT the live tree).")
    ap.add_argument("--logs", type=Path, required=True)
    ap.add_argument("--only", action="append", default=[],
                    help="Run only these gate names; repeatable.")
    args = ap.parse_args()
    tree, logs = args.tree.resolve(), args.logs.resolve()
    if tree == ROOT.resolve():
        ap.error("--tree must be a scratch copy, not the repository this script lives in")
    logs.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1",
               MPLBACKEND="Agg", PYTHONOPTIMIZE="0")
    case = Case(tree, logs)
    py = sys.executable
    ver, maint = "computations/verification/", "computations/maintenance/"
    first_source = json.loads((tree / "record/claims.json").read_text())["claims"][0]["source"]
    supp_first = json.loads((tree / "supplement/fixed_map/inventory.json").read_text())["files"][0]["path"]

    def scoped_tamper():
        rel = "record/wave2_scoped_input_bindings.json"
        case.backup(rel)
        p = tree / rel
        data = json.loads(p.read_text())
        k = sorted(data["files"])[0]
        old = data["files"][k]["sha256"]
        data["files"][k]["sha256"] = ("0" if old[0] != "0" else "1") + old[1:]
        p.write_text(json.dumps(data, indent=2) + "\n")

    def wave2_pin_tamper():
        rel = "record/wave2_replay_contract.json"
        case.backup(rel)
        p = tree / rel
        p.write_text(p.read_text().replace("tasks", "taskX", 1))

    spectral_rel = "record/spectral_research/sources/research_round14_2026_10_21/round14_main_report.md"
    gates = [
        ("registry_audit", [py, ver + "scientific_registry_audit.py"],
         delete_file(case, first_source), "missing file: " + first_source),
        ("repository_audit", [py, ver + "repository_audit.py"],
         create_file(case, "computations/verification/zz_v4_nc.jl", b"// V4 negative control\n"),
         "corrupted tree: forbidden .jl file"),
        ("bibliographic_audit", [py, ver + "bibliographic_metadata_audit.py", "--self-test"],
         append_bytes(case, "evidence/source_metadata/registry_metadata_20261101_lineNv5.json", b" "),
         "tampered hash: byte appended to digest-pinned metadata cache"),
        ("text_control_audit", [py, ver + "text_control_audit.py"],
         append_bytes(case, "README.md", b"\x00"), "forbidden byte: NUL in README.md"),
        ("render_claim_registry_check", [py, maint + "render_claim_registry.py", "--check"],
         append_text(case, "record/claim_registry.md", "\n<!-- V4-NC -->\n"), "tampered generated view"),
        ("render_errata_check", [py, maint + "render_errata.py", "--check"],
         append_text(case, "ERRATA.md", "\n<!-- V4-NC -->\n"), "tampered generated view"),
        ("render_status_check", [py, maint + "render_status.py", "--check"],
         append_text(case, "STATUS.md", "\n<!-- V4-NC -->\n"), "tampered generated view"),
        ("render_results_check", [py, maint + "render_results.py", "--check"],
         append_text(case, "RESULTS.md", "\n<!-- V4-NC -->\n"), "tampered generated view"),
        ("render_appendix_a_check", [py, maint + "render_appendix_a.py", "--check"],
         append_text(case, "manuscript/appendix_a_claim_index.tex", "\n% V4-NC\n"), "tampered generated view"),
        ("frozen_packets_check", [py, maint + "frozen_packets.py", "--check"],
         append_bytes(case, "computations/verification/lineJ/J3/code/levels_survey.py", b"\n"), "tampered frozen packet file"),
        ("render_bibliography_check", [py, maint + "render_bibliography.py", "--check"],
         append_text(case, "manuscript/unified_bibliography.tex", "\n% V4-NC\n"), "tampered generated view"),
        ("render_research_views_check", [py, maint + "render_research_views.py", "--check"],
         append_text(case, "record/scientific_dependency_graph.md", "\n<!-- V4-NC -->\n"), "tampered generated view"),
        ("manuscript_references_check", [py, maint + "audit_manuscript_references.py", "--check"],
         append_text(case, "manuscript/BGS_unified.tex", "\n\\cite{v4-nonexistent-key}\n"),
         "corrupted binding: dangling citation key"),
        ("wave2_check_sources", [py, ver + "wave2_portable_replay.py", "--check-sources"],
         wave2_pin_tamper, "tampered pin: wave2 contract bytes"),
        ("wave3_check_sources", [py, ver + "wave3_checked_replay.py", "--check-sources"],
         edit_json(case, "record/wave3_replay_contract.json",
                   lambda d: d["tasks"][0].__setitem__("declared_check_count", 999)),
         "wrong count: declared_check_count 72 -> 999"),
        ("wave2_integration_audit", [py, ver + "wave2_integration_audit.py"],
         scoped_tamper, "corrupted binding: scoped pin sha flipped"),
        ("wave3_integration_audit", [py, ver + "wave3_integration_audit.py"],
         edit_json(case, "record/wave3_manuscript_mapping.json",
                   lambda d: d.__setitem__("section_sha256", "0" * 64)),
         "tampered hash: mapping section_sha256 -> zeros"),
        ("fixed_map_supplement_audit", [py, maint + "verify_fixed_map_supplement.py", "--audit-only"],
         delete_file(case, "supplement/fixed_map/" + supp_first),
         "missing file: " + supp_first),
        ("spectral_corpus_check", [py, maint + "rebuild_spectral_corpus.py", "--check"],
         append_bytes(case, spectral_rel, b"\nV4-NC\n"), "tampered projection source"),
        ("spectral_corpus_replay", [py, ver + "replay_spectral_corpus.py", "--output-dir",
                                    str(logs / "spectral-replay")],
         append_bytes(case, spectral_rel, b"\nV4-NC\n"), "tampered projection source"),
        ("spectral_edition_missing_input", [py, ver + "check_spectral_edition.py",
                                            "--known-tree", str(tree / "does-not-exist-v4")],
         None, "missing input (this run itself is the control; expect nonzero)"),
        ("unittest_discover", [py, "-m", "unittest", "discover", "-s",
                               "computations/maintenance/tests", "-q"],
         create_file(case, "computations/maintenance/tests/test_zz_v4_nc.py",
                     b"import unittest\nclass T(unittest.TestCase):\n    def test_v4_nc_fails(self):\n        self.assertEqual(1, 2)\n"),
         "suite sensitivity: failing test file added"),
    ]
    # Guarded-skip sync gates: --check SKIPs hand-edited targets; the
    # control is that write mode refuses. Handled as refusal cases.
    sync_refusals = [
        ("sync_finite_orbit_section_write_refusal", [py, maint + "sync_finite_orbit_section.py"]),
        ("sync_fixed_map_section_write_refusal", [py, maint + "sync_fixed_map_section.py"]),
        ("sync_return_sections_write_refusal", [py, maint + "sync_return_sections.py"]),
    ]
    results = []
    for name, argv, tamper, desc in gates:
        if args.only and name not in args.only:
            continue
        base_code, base_out, base_s = run(argv, tree, env)
        (logs / (name + ".baseline.log")).write_text(base_out)
        if tamper is None:
            verdict = ("NEGATIVE-CONTROL-DEMONSTRATED (missing input)"
                       if base_code != 0 else "INSENSITIVE-TO-THIS-TAMPER")
            results.append({"gate": name, "baseline_exit": base_code, "tampered_exit": base_code,
                            "tamper": desc, "verdict": verdict})
            print(name, base_code, verdict, flush=True)
            continue
        tamper()
        t_code, t_out, t_s = run(argv, tree, env)
        (logs / (name + ".tampered.log")).write_text(t_out)
        restored = case.restore_all()
        verdict = ("NEGATIVE-CONTROL-DEMONSTRATED" if base_code == 0 and t_code != 0
                   else ("BASELINE-RED" if base_code != 0 else "INSENSITIVE-TO-THIS-TAMPER"))
        results.append({"gate": name, "baseline_exit": base_code, "tampered_exit": t_code,
                        "tamper": desc, "restored_ok": restored, "verdict": verdict})
        print(name, "base=", base_code, "tampered=", t_code, verdict, flush=True)
    for name, argv in sync_refusals:
        if args.only and name not in args.only:
            continue
        code, out, _ = run(argv, tree, env)
        (logs / (name + ".log")).write_text(out)
        verdict = ("NEGATIVE-CONTROL-DEMONSTRATED (refusal)" if code != 0
                   else "INSENSITIVE-TO-THIS-TAMPER")
        results.append({"gate": name, "baseline_exit": code, "tampered_exit": code,
                        "tamper": "guard: write mode on hand-edited target must refuse",
                        "verdict": verdict})
        print(name, code, verdict, flush=True)
    (logs / "results.json").write_text(json.dumps(results, indent=1) + "\n")
    bad = [r for r in results if r["verdict"] not in ("NEGATIVE-CONTROL-DEMONSTRATED",
                                                      "NEGATIVE-CONTROL-DEMONSTRATED (refusal)",
                                                      "NEGATIVE-CONTROL-DEMONSTRATED (missing input)")]
    print(f"{len(results) - len(bad)}/{len(results)} negative controls demonstrated; "
          f"non-demonstrated: {[r['gate'] for r in bad]}")
    return 0 if not bad else 1


if __name__ == "__main__":
    raise SystemExit(main())
