#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANUSCRIPT = ROOT / "manuscript"
WORKFLOWS = ROOT / ".github" / "workflows"
MAINTENANCE = ROOT / "computations" / "maintenance"

LEGACY_MANUSCRIPT = {
    "arithmetic_cat_map_moments.tex", "arithmetic_cat_map_moments.pdf",
    "cyclotomic_row_support_frontier.tex", "cyclotomic_row_support_frontier.pdf",
    "magnetic_quotient_semicircle.tex", "magnetic_quotient_semicircle.pdf",
    "pell_coboundary_resonance.tex", "pell_coboundary_resonance.pdf",
    "pell_floquet_normal_form.tex", "pell_floquet_normal_form.pdf",
    "fixed_strength_section.tex", "general_hyperbolic_section.tex",
    "pell_coboundary_section.tex", "pell_floquet_section.tex",
    "pell_gaussian_section.tex", "pell_weighted_echo_section.tex",
    "README_unified.md", "build_rigidity_paper.py",
}

ALLOWED_WORKFLOWS = {
    "build-manuscript.yml",
    "ci.yml",
    "research-snapshot.yml",
}

STALE_MAINTENANCE = {
    "integrate_general_hyperbolic.py",
    "integrate_magnetic_audit.py",
    "integrate_pell_echo.py",
    "integrate_smooth_recurrence.py",
    "integrate_unified_manuscript.py",
    "package_magnetic_research.py",
    "publish_coboundary.py",
    "publish_fixed_strength.py",
    "publish_pell_research.py",
    "render_pell_floquet.py",
}

REQUIRED = [
    ROOT / "README.md",
    ROOT / "REPRODUCE_unified.md",
    ROOT / "computations" / "README.md",
    ROOT / "record" / "claim_ledger.md",
    ROOT / "record" / "consolidation_map.json",
    ROOT / "record" / "final_consolidation_audit_20260906.md",
    MAINTENANCE / "verify_workspace.py",
    MAINTENANCE / "build_unified_manuscript.py",
    ROOT / "computations" / "verification" / "repository_audit.py",
    ROOT / "formalization" / "Bgs.lean",
    ROOT / "CMakeLists.txt",
    MANUSCRIPT / "WoW_unified.tex",
    MANUSCRIPT / "README.md",
    ROOT / "archive" / "branch-snapshots" / "README.md",
    ROOT / "archive" / "delivery-20260906" / "README.md",
]

ACTIVE_MARKDOWN = [
    ROOT / "record" / "return_local_limits_review_20260913.md",
    ROOT / "literature" / "return_local_limits_sources.md",
    ROOT / "mathematics" / "return_trace_obstruction.md",
    ROOT / "record" / "return_obstruction_review_20260912.md",
    ROOT / "RESEARCH.md",
    ROOT / "record" / "publication_review_20260912.md",
    ROOT / "record" / "final_research_handoff_20260921.md",
    ROOT / "record" / "verified_state_reconciliation_20260921.md",
    ROOT / "mathematics" / "fixed_map_weyl_path_escape.md",
    ROOT / "mathematics" / "hyperbolic_19adic_dephasing.md",
    ROOT / "mathematics" / "one_shear_antiunitary_no_go.md",
    ROOT / "mathematics" / "fixed_map_unistochastic_ramp.md",
    ROOT / "mathematics" / "fixed_map_classical_sum_rule.md",
    ROOT / "mathematics" / "quantum_history_reconnection.md",
    ROOT / "mathematics" / "unitary_encounter_envelope.md",
    ROOT / "computations" / "verification" / "quantum_history_reconnection_audit.py",
    ROOT / "computations" / "verification" / "unitary_encounter_envelope_audit.py",
    ROOT / "computations" / "verification" / "fixed_map_unistochastic_ramp_audit.py",
    ROOT / "computations" / "verification" / "fixed_map_classical_sum_rule_audit.py",
    ROOT / "computations" / "verification" / "bgs_heisenberg_path_audit.py",
    ROOT / "computations" / "verification" / "hyperbolic_19adic_audit.py",
    ROOT / "mathematics" / "fixed_model_symmetry_theorem.md",
    ROOT / "mathematics" / "fixed_model_pell_crossover.md",
    ROOT / "mathematics" / "fixed_map_moment_control_and_transfer.md",
    ROOT / "mathematics" / "three_orientation_resolvent_barrier.md",
    ROOT / "mathematics" / "fourier_line_resonance_coercivity.md",
    ROOT / "mathematics" / "local_jet_resonance_obstruction.md",
    ROOT / "README.md",
    ROOT / "REPRODUCE_unified.md",
    ROOT / "computations" / "README.md",
    MANUSCRIPT / "README.md",
    ROOT / "archive" / "branch-snapshots" / "README.md",
    ROOT / "archive" / "delivery-20260906" / "README.md",
]


def fail(msg: str) -> None:
    raise RuntimeError(msg)


def check_required() -> None:
    missing = [str(p.relative_to(ROOT)) for p in REQUIRED if not p.is_file()]
    if missing:
        fail("missing required files: " + ", ".join(missing))


def check_retired_julia() -> None:
    julia = sorted(p.relative_to(ROOT) for p in ROOT.rglob("*.jl") if ".git" not in p.parts)
    env = sorted(
        p.relative_to(ROOT)
        for p in ROOT.rglob("*")
        if p.is_file() and p.name in {"Project.toml", "Manifest.toml"} and ".git" not in p.parts
    )
    bad = julia + env
    if bad:
        fail("retired Julia surface is tracked: " + ", ".join(map(str, bad)))


def check_archive_contract() -> None:
    snap = ROOT / "archive" / "branch-snapshots"
    files = sorted(p.relative_to(snap) for p in snap.rglob("*") if p.is_file())
    if files != [Path("README.md")]:
        fail("archive/branch-snapshots must be metadata-only; found: " + ", ".join(map(str, files)))


def check_manuscript_surface() -> None:
    present_legacy = sorted(name for name in LEGACY_MANUSCRIPT if (MANUSCRIPT / name).exists())
    if present_legacy:
        fail("legacy/duplicate manuscript surface still present: " + ", ".join(present_legacy))

    master = MANUSCRIPT / "WoW_unified.tex"
    text = master.read_text(encoding="utf-8")
    inputs = re.findall(r"\\input\{([^}]+)\}", text)
    if not inputs:
        fail("WoW_unified.tex has no inputs")
    missing: list[str] = []
    for raw in inputs:
        p = MANUSCRIPT / raw
        if p.suffix == "":
            p = p.with_suffix(".tex")
        if not p.is_file():
            missing.append(str(p.relative_to(ROOT)))
    if missing:
        fail("unresolved manuscript inputs: " + ", ".join(missing))

    pdfs = sorted(p.name for p in MANUSCRIPT.glob("*.pdf"))
    if pdfs:
        fail("generated manuscript PDFs must not be committed: " + ", ".join(pdfs))


def check_workflows() -> None:
    present = {p.name for p in WORKFLOWS.glob("*.yml") if p.is_file()}
    if present != ALLOWED_WORKFLOWS:
        fail(
            "workflow surface differs from canonical set; present="
            + ",".join(sorted(present))
            + " expected="
            + ",".join(sorted(ALLOWED_WORKFLOWS))
        )
    legacy_tokens = sorted(name for name in LEGACY_MANUSCRIPT if name.endswith((".tex", ".pdf")))
    offenders: list[str] = []
    for p in WORKFLOWS.glob("*.yml"):
        text = p.read_text(encoding="utf-8")
        if any(tok in text for tok in legacy_tokens):
            offenders.append(str(p.relative_to(ROOT)))
    if offenders:
        fail("workflow still references legacy manuscripts: " + ", ".join(offenders))


def check_maintenance_surface() -> None:
    present = sorted(name for name in STALE_MAINTENANCE if (MAINTENANCE / name).exists())
    if present:
        fail("stale one-shot publisher/integrator(s) still present: " + ", ".join(present))


def check_cpp_coverage() -> None:
    cpp_dir = ROOT / "computations" / "cpp"
    sources = sorted(p.stem for p in cpp_dir.glob("*.cpp"))
    cmake = (ROOT / "CMakeLists.txt").read_text(encoding="utf-8")
    targets = set(re.findall(r"add_executable\s*\(\s*([A-Za-z0-9_.+-]+)\s+[^)]*?([A-Za-z0-9_.+-]+)\.cpp", cmake, re.S))
    covered = {src for _, src in targets}
    missing = [s for s in sources if s not in covered]
    if missing:
        fail("orphaned C++ verifier source(s): " + ", ".join(missing))


def check_lean_coverage() -> None:
    bgs = ROOT / "formalization" / "Bgs"
    modules = sorted(p.stem for p in bgs.glob("*.lean"))
    entry = (ROOT / "formalization" / "Bgs.lean").read_text(encoding="utf-8")
    imports = set(re.findall(r"^import\s+Bgs\.([A-Za-z0-9_]+)\s*$", entry, re.M))
    missing = [m for m in modules if m not in imports]
    if missing:
        fail("Bgs.lean does not import active module(s): " + ", ".join(missing))


def check_active_markdown_links() -> None:
    pat = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    broken: list[str] = []
    for p in ACTIVE_MARKDOWN:
        text = p.read_text(encoding="utf-8", errors="replace")
        for raw in pat.findall(text):
            dest = raw.strip().split("#", 1)[0]
            if not dest or "://" in dest or dest.startswith("mailto:"):
                continue
            target = (p.parent / dest).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                continue
            if not target.exists():
                broken.append(f"{p.relative_to(ROOT)} -> {dest}")
    if broken:
        fail("broken active Markdown link(s): " + "; ".join(broken))


def main() -> int:
    checks = [
        check_required,
        check_retired_julia,
        check_archive_contract,
        check_manuscript_surface,
        check_workflows,
        check_maintenance_surface,
        check_cpp_coverage,
        check_lean_coverage,
        check_active_markdown_links,
    ]
    for fn in checks:
        fn()
        print(f"PASS {fn.__name__}")
    print("PASS repository_audit")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as exc:
        print(f"FAIL repository_audit: {exc}", file=sys.stderr)
        raise SystemExit(1)
