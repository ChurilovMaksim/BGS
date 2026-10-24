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
    "research-release.yml",
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
    ROOT / "README.ru.md",
    ROOT / "REPRODUCE_unified.md",
    ROOT / "computations" / "README.md",
    ROOT / "record" / "claim_ledger.md",
    ROOT / "docs" / "repository_conventions.md",
    ROOT / "record" / "claims.json",
    ROOT / "record" / "claim_registry.md",
    ROOT / "record" / "errata.json",
    ROOT / "record" / "scientific_dependencies.json",
    ROOT / "record" / "generated_sources.json",
    ROOT / "record" / "mathematics_topics.json",
    ROOT / "literature" / "external_dependencies.json",
    ROOT / "evidence" / "index.json",
    ROOT / "environment" / "runtime-manifest.json",
    ROOT / "papers" / "README.md",
    ROOT / "CITATION.cff",
    ROOT / "SOURCE_OF_TRUTH.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "REVIEWING.md",
    ROOT / "record" / "consolidation_map.json",
    ROOT / "record" / "final_consolidation_audit_20260906.md",
    MAINTENANCE / "verify_workspace.py",
    MAINTENANCE / "render_claim_registry.py",
    MAINTENANCE / "render_errata.py",
    MAINTENANCE / "build_unified_manuscript.py",
    ROOT / "computations" / "verification" / "repository_audit.py",
    ROOT / "computations" / "verification" / "scientific_registry_audit.py",
    ROOT / "formalization" / "Bgs.lean",
    ROOT / "CMakeLists.txt",
    MANUSCRIPT / "BGS_unified.tex",
    MANUSCRIPT / "README.md",
    ROOT / "archive" / "branch-snapshots" / "README.md",
    ROOT / "archive" / "delivery-20260906" / "README.md",
]

ACTIVE_MARKDOWN = [
    ROOT / "record" / "return_local_limits_review_20260913.md",
    ROOT / "literature" / "return_local_limits_sources.md",
    ROOT / "mathematics" / "returns" / "return_trace_obstruction.md",
    ROOT / "record" / "return_obstruction_review_20260912.md",
    ROOT / "RESEARCH.md",
    ROOT / "record" / "publication_review_20260912.md",
    ROOT / "record" / "final_research_handoff_20260921.md",
    ROOT / "mathematics" / "fixed-map" / "fixed_model_symmetry_theorem.md",
    ROOT / "mathematics" / "fixed-map" / "fixed_model_pell_crossover.md",
    ROOT / "mathematics" / "fixed-map" / "fixed_map_moment_control_and_transfer.md",
    ROOT / "mathematics" / "three_orientation_resolvent_barrier.md",
    ROOT / "mathematics" / "resonance-cohomology" / "fourier_line_resonance_coercivity.md",
    ROOT / "mathematics" / "resonance-cohomology" / "local_jet_resonance_obstruction.md",
    ROOT / "README.md",
    ROOT / "README.ru.md",
    ROOT / "REPRODUCE_unified.md",
    ROOT / "computations" / "README.md",
    MANUSCRIPT / "README.md",
    ROOT / "archive" / "branch-snapshots" / "README.md",
    ROOT / "archive" / "delivery-20260906" / "README.md",
]


def fail(msg: str) -> None:
    raise RuntimeError(msg)



def check_canonical_identity() -> None:
    active_roots = [
        ROOT / "README.md",
        ROOT / "README.ru.md",
        ROOT / "REPRODUCE_unified.md",
        ROOT / "CMakeLists.txt",
        ROOT / ".github" / "workflows",
        ROOT / "manuscript",
        ROOT / "mathematics",
        ROOT / "computations",
        ROOT / "formalization",
    ]
    forbidden = ("ChurilovMaksim/WoW", "WoW research programme", "WoW_unified", "wow_catmap_verifiers")
    offenders: list[str] = []
    for root in active_roots:
        paths = [root] if root.is_file() else [p for p in root.rglob("*") if p.is_file()]
        for p in paths:
            if p.resolve() == Path(__file__).resolve():
                continue
            if p.suffix.lower() not in {".md", ".tex", ".py", ".cpp", ".c", ".yml", ".yaml", ".toml", ".txt", ""}:
                continue
            text = p.read_text(encoding="utf-8", errors="replace")
            hits = [token for token in forbidden if token in text]
            if hits:
                offenders.append(f"{p.relative_to(ROOT)}: {', '.join(hits)}")
    if offenders:
        fail("legacy WoW identity remains on active surface: " + "; ".join(offenders))

    if (MANUSCRIPT / "WoW_unified.tex").exists():
        fail("legacy manuscript entry point is still present")
    if not (MANUSCRIPT / "BGS_unified.tex").is_file():
        fail("canonical manuscript entry point manuscript/BGS_unified.tex is missing")

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

    master = MANUSCRIPT / "BGS_unified.tex"
    text = master.read_text(encoding="utf-8")
    inputs = re.findall(r"\\input\{([^}]+)\}", text)
    if not inputs:
        fail("BGS_unified.tex has no inputs")
    missing: list[str] = []
    for raw in inputs:
        p = MANUSCRIPT / raw
        if p.suffix == "":
            p = p.with_suffix(".tex")
        if not p.is_file():
            missing.append(str(p.relative_to(ROOT)))
    if missing:
        fail("unresolved manuscript inputs: " + ", ".join(missing))

    # A separate finite-orbit note was actually compiled in the historical
    # 2026-09-22 delivery. Keep that source for its recorded execution; reject
    # other unused TeX copies, which would create competing publication roots.
    reachable: set[Path] = set()
    def visit(path: Path) -> None:
        if path in reachable:
            return
        reachable.add(path)
        for raw in re.findall(r"\\input\{([^}]+)\}", path.read_text(encoding="utf-8")):
            dep = MANUSCRIPT / raw
            if dep.suffix == "":
                dep = dep.with_suffix(".tex")
            if not dep.is_file():
                fail(f"unresolved nested manuscript input: {dep.relative_to(ROOT)}")
            visit(dep)
    visit(master)
    orphaned = {p for p in MANUSCRIPT.rglob("*.tex") if p not in reachable}
    historical = {MANUSCRIPT / "finite_orbit_note.tex"}
    if orphaned != historical:
        fail("unexpected unused manuscript TeX sources: " +
             ", ".join(str(p.relative_to(ROOT)) for p in sorted(orphaned ^ historical)))

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


def check_bilingual_readmes() -> None:
    english = ROOT / "README.md"
    russian = ROOT / "README.ru.md"

    texts = {
        english: english.read_text(encoding="utf-8", errors="replace"),
        russian: russian.read_text(encoding="utf-8", errors="replace"),
    }

    required_sections = {
        english: (
            "## What the conjecture asks",
            "## The exact model and target",
            "## Three reconstructed analytic results",
            "## What else is established, and what is missing",
            "## Read, reproduce, and cite",
        ),
        russian: (
            "## О чём гипотеза",
            "## Точная модель и цель",
            "## Три восстановленных аналитических результата",
            "## Другие результаты и оставшийся разрыв",
            "## Чтение, воспроизведение и цитирование",
        ),
    }

    for path, text in texts.items():
        if not text.startswith("# "):
            fail(f"{path.name} must start with an H1")
        if len(re.findall(r"^# ", text, re.M)) != 1:
            fail(f"{path.name} must contain exactly one H1")
        if re.search(r"\\\(|\\\)|\\\[|\\\]", text):
            fail(f"legacy non-GitHub-native math delimiters remain in {path.name}")

        forbidden_math_macros = (
            r"\\operatorname",
            r"\\newcommand",
            r"\\renewcommand",
            r"\\DeclareMathOperator",
            r"\\def",
            r"\\require",
        )
        for macro in forbidden_math_macros:
            if macro in text:
                fail(f"GitHub-unsafe README math macro {macro!r} in {path.name}")

        without_fenced = re.sub(r"```math\n[\s\S]*?\n```", "", text)
        if len(re.findall(r"(?<!\$)\$(?!\$)", without_fenced)) % 2:
            fail(f"unbalanced inline-math delimiters in {path.name}")

        fenced_math = len(re.findall(r"^```math\s*$", text, re.M))
        fenced_other = len(re.findall(r"^```(?:sh|mermaid)\s*$", text, re.M))
        fenced_closers = len(re.findall(r"^```\s*$", text, re.M))
        if fenced_closers != fenced_math + fenced_other:
            fail(f"unbalanced fenced blocks in {path.name}")

        for heading in required_sections[path]:
            if heading not in text:
                fail(f"missing reader section in {path.name}: {heading}")

        image_refs = re.findall(r'<img[^>]+src="([^"]+)"', text)
        image_refs += re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text)
        for raw in image_refs:
            if "://" in raw:
                continue
            target = (path.parent / raw).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                continue
            if not target.is_file():
                fail(f"missing README image asset: {path.name} -> {raw}")

    if "README.ru.md" not in texts[english]:
        fail("README.md does not link to README.ru.md")
    if "README.md" not in texts[russian]:
        fail("README.ru.md does not link back to README.md")

    claim_pattern = re.compile(r"BGS-[A-Z]+-\d{3}")
    english_claims = set(claim_pattern.findall(texts[english]))
    russian_claims = set(claim_pattern.findall(texts[russian]))
    if english_claims != russian_claims:
        fail(
            "bilingual README claim-ID drift: "
            f"English-only={sorted(english_claims-russian_claims)}, "
            f"Russian-only={sorted(russian_claims-english_claims)}"
        )


def check_active_markdown_links() -> None:
    pat = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    broken: list[str] = []
    dynamic = sorted((ROOT / "mathematics" / "topics").rglob("README.md"))
    dynamic += sorted((ROOT / "papers").rglob("README.md"))
    dynamic += sorted((ROOT / "docs").glob("*.md"))
    dynamic += [
        ROOT / "SOURCE_OF_TRUTH.md",
        ROOT / "CONTRIBUTING.md",
        ROOT / "REVIEWING.md",
        ROOT / "RESEARCH.md",
        ROOT / "RELEASES.md",
        ROOT / "ERRATA.md",
        ROOT / "record" / "README.md",
        ROOT / "mathematics" / "README.md",
        ROOT / "evidence" / "provenance.md",
        ROOT / "evidence" / "README.md",
        ROOT / "literature" / "README.md",
    ]
    seen: set[Path] = set()
    for p in [*ACTIVE_MARKDOWN, *dynamic]:
        if p in seen:
            continue
        seen.add(p)
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
        check_canonical_identity,
        check_required,
        check_retired_julia,
        check_archive_contract,
        check_manuscript_surface,
        check_workflows,
        check_maintenance_surface,
        check_cpp_coverage,
        check_lean_coverage,
        check_bilingual_readmes,
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
