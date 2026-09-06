#!/usr/bin/env python3
"""Repository-wide structural/provenance audit for the curated research branch.

This gate is intentionally stricter than language-specific tests. It checks the
maintained source tree while treating ``archive/`` as immutable provenance-only
data. Archived branch/delivery snapshots are deliberately excluded from active
source duplication, link, Julia, C++ and Lean coverage checks.
"""
from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

EXPECTED_TOP_LEVEL = {
    ".github", ".gitignore", "CMakeLists.txt", "README.md",
    "REPRODUCE_unified.md", "archive", "assets", "computations", "evidence",
    "formalization", "literature", "manuscript", "mathematics", "record",
    "requirements-nondegeneracy.txt", "requirements.txt",
}
FORBIDDEN_PATHS = {
    Path("record/corpus"), Path("record/checkpoints"),
    Path("record/engineering"), Path("record/formal_drafts"),
}
TEXT_DUPLICATE_SUFFIXES = {
    ".cpp", ".h", ".hpp", ".lean", ".md", ".py", ".tex", ".yml", ".yaml",
}
SKIP_DIR_NAMES = {".git", ".lake", "__pycache__", "build", "archive"}
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def _markdown_without_code(text: str) -> str:
    """Exclude fenced and inline code while retaining real Markdown links."""
    lines = []
    fence_char = None
    fence_length = 0
    for line in text.splitlines(keepends=True):
        match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line.rstrip("\n"))
        if fence_char is not None:
            if match and match.group(1)[0] == fence_char and len(match.group(1)) >= fence_length and not match.group(2).strip():
                fence_char = None
            lines.append("\n")
            continue
        if match and not (match.group(1)[0] == "`" and "`" in match.group(2)):
            fence_char, fence_length = match.group(1)[0], len(match.group(1))
            lines.append("\n")
        else:
            lines.append(line)
    return re.sub(r"(?<!`)(`+)(?!`)(.*?)(?<!`)\1(?!`)", " ", "".join(lines), flags=re.S)


def check_markdown_parser() -> None:
    sample = "`Z[T](w_e,w_f)` and [real](README.md)\n```text\n[x](not-a-link)\n```\n"
    assert MARKDOWN_LINK_RE.findall(_markdown_without_code(sample)) == ["README.md"]
    assert MARKDOWN_LINK_RE.findall(_markdown_without_code("[broken](missing.md)")) == ["missing.md"]
    assert MARKDOWN_LINK_RE.findall(_markdown_without_code("````\n```\n[x](fake)\n````\n[ok](README.md)")) == ["README.md"]


def files_under(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        try:
            relative = path.relative_to(ROOT)
        except ValueError:
            relative = path
        if any(part in SKIP_DIR_NAMES for part in relative.parts):
            continue
        yield path


def check_top_level() -> None:
    present = {p.name for p in ROOT.iterdir() if p.name != ".git"}
    unexpected = sorted(present - EXPECTED_TOP_LEVEL)
    missing = sorted(EXPECTED_TOP_LEVEL - present)
    if unexpected:
        raise AssertionError(f"unexpected top-level entries: {unexpected}")
    if missing:
        raise AssertionError(f"missing top-level entries: {missing}")


def check_archive_contract() -> None:
    readme = ROOT / "archive" / "branch-snapshots" / "README.md"
    if not readme.is_file():
        raise AssertionError("archive provenance README is missing")
    text = readme.read_text(encoding="utf-8")
    if "provenance" not in text.lower() or "authoritative" not in text.lower():
        raise AssertionError("archive README must mark snapshots as provenance-only")


def check_no_historical_copies_or_julia() -> None:
    for relative in sorted(FORBIDDEN_PATHS):
        if (ROOT / relative).exists():
            raise AssertionError(f"forbidden historical copy tree exists: {relative}")
    julia = [p.relative_to(ROOT) for p in files_under(ROOT) if p.suffix == ".jl"]
    if julia:
        raise AssertionError(f"tracked Julia sources remain in maintained tree: {julia}")


def check_no_duplicate_text_sources() -> None:
    groups: dict[str, list[Path]] = defaultdict(list)
    for path in files_under(ROOT):
        if path.suffix.lower() not in TEXT_DUPLICATE_SUFFIXES:
            continue
        data = path.read_bytes()
        if len(data) < 64:
            continue
        groups[hashlib.sha256(data).hexdigest()].append(path.relative_to(ROOT))
    duplicates = [sorted(paths) for paths in groups.values() if len(paths) > 1]
    if duplicates:
        formatted = "; ".join(", ".join(map(str, group)) for group in duplicates)
        raise AssertionError(f"byte-identical maintained text/source duplicates: {formatted}")


def check_evidence_provenance() -> None:
    promoted_roots = (
        ROOT / "evidence" / "certificates",
        ROOT / "evidence" / "numerical",
    )
    for promoted_root in promoted_roots:
        for path in sorted(promoted_root.glob("*.json")):
            data = json.loads(path.read_text(encoding="utf-8"))
            producer = data.get("producer")
            if not producer:
                raise AssertionError(f"{path.relative_to(ROOT)}: promoted evidence lacks producer")
            if not (ROOT / str(producer)).is_file():
                raise AssertionError(f"{path.relative_to(ROOT)}: unresolved active producer {producer}")
            if not data.get("scope") and not data.get("interpretation"):
                raise AssertionError(f"{path.relative_to(ROOT)}: promoted evidence lacks scope/interpretation")
            refs = data.get("reference_inputs", {})
            if refs is not None:
                if not isinstance(refs, dict):
                    raise AssertionError(f"{path.relative_to(ROOT)}: reference_inputs must be an object")
                for relative in refs:
                    if not (ROOT / relative).is_file():
                        raise AssertionError(f"{path.relative_to(ROOT)}: missing reference input {relative}")
    for path in sorted((ROOT / "evidence" / "reference").rglob("*.json")):
        json.loads(path.read_text(encoding="utf-8"))


def check_lean_import_graph_and_placeholders() -> None:
    module_dir = ROOT / "formalization" / "Bgs"
    modules = {f"Bgs.{p.stem}" for p in module_dir.glob("*.lean")}
    imports = set()
    for line in (ROOT / "formalization" / "Bgs.lean").read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("import "):
            imports.add(line.removeprefix("import ").strip())
    if modules != imports:
        raise AssertionError(
            f"Lean import mismatch: missing={sorted(modules-imports)}, extra={sorted(imports-modules)}"
        )
    placeholders: list[str] = []
    for path in sorted(module_dir.glob("*.lean")):
        text = path.read_text(encoding="utf-8")
        for token in ("sorry", "admit"):
            if re.search(rf"\b{token}\b", text):
                placeholders.append(f"{path.relative_to(ROOT)}:{token}")
    if placeholders:
        raise AssertionError(f"Lean proof placeholders in active modules: {placeholders}")


def check_cpp_build_coverage() -> None:
    cmake = (ROOT / "CMakeLists.txt").read_text(encoding="utf-8")
    sources = sorted((ROOT / "computations" / "cpp").glob("*.cpp"))
    orphaned = [
        str(path.relative_to(ROOT)) for path in sources
        if str(path.relative_to(ROOT)).replace("\\", "/") not in cmake
    ]
    if orphaned:
        raise AssertionError(f"C++ sources not covered by CMake: {orphaned}")


def check_markdown_relative_links() -> None:
    missing: list[str] = []
    for document in sorted(files_under(ROOT)):
        if document.suffix.lower() != ".md":
            continue
        text = document.read_text(encoding="utf-8")
        for raw in MARKDOWN_LINK_RE.findall(_markdown_without_code(text)):
            target = raw.strip().split()[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            candidate = (document.parent / target).resolve()
            try:
                candidate.relative_to(ROOT.resolve())
            except ValueError:
                missing.append(f"{document.relative_to(ROOT)} -> {raw} (outside repo)")
                continue
            if not candidate.exists():
                missing.append(f"{document.relative_to(ROOT)} -> {raw}")
    if missing:
        raise AssertionError("broken Markdown relative links: " + "; ".join(missing))


def check_manuscript_surface() -> None:
    legacy_tex = ROOT / "manuscript" / "arithmetic_cat_map_moments.tex"
    legacy_pdf = ROOT / "manuscript" / "arithmetic_cat_map_moments.pdf"
    unified_tex = ROOT / "manuscript" / "WoW_unified.tex"
    builder = ROOT / "computations" / "maintenance" / "build_unified_manuscript.py"
    final_audit = ROOT / "record" / "final_consolidation_audit_20260906.md"
    reproduce = ROOT / "REPRODUCE_unified.md"
    for path in (legacy_tex, legacy_pdf, unified_tex, builder, final_audit, reproduce):
        if not path.is_file() or path.stat().st_size < 64:
            raise AssertionError(f"required publication surface is missing or unexpectedly small: {path.relative_to(ROOT)}")
    if legacy_tex.stat().st_size < 1024 or legacy_pdf.stat().st_size < 1024 or unified_tex.stat().st_size < 1024:
        raise AssertionError("active manuscript source/PDF is unexpectedly small")


def main() -> None:
    check_markdown_parser()
    check_top_level()
    check_archive_contract()
    check_no_historical_copies_or_julia()
    check_no_duplicate_text_sources()
    check_evidence_provenance()
    check_lean_import_graph_and_placeholders()
    check_cpp_build_coverage()
    check_markdown_relative_links()
    check_manuscript_surface()
    print("repository structural/provenance audit: PASS")


if __name__ == "__main__":
    main()
