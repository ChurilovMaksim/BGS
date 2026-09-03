#!/usr/bin/env python3
"""Repository-wide structural/provenance audit for the curated research branch.

This gate is intentionally stricter than language-specific tests.  It prevents
historical workspace copies, Julia sources, orphaned producers, unimported Lean
modules, unbuilt C++ sources, and byte-identical source/document duplicates from
creeping back into ``main``.
"""
from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

EXPECTED_TOP_LEVEL = {
    ".github",
    ".gitignore",
    "CMakeLists.txt",
    "README.md",
    "assets",
    "computations",
    "evidence",
    "formalization",
    "literature",
    "manuscript",
    "mathematics",
    "record",
    "requirements.txt",
}
FORBIDDEN_PATHS = {
    Path("record/corpus"),
    Path("record/checkpoints"),
    Path("record/engineering"),
    Path("record/formal_drafts"),
}
TEXT_DUPLICATE_SUFFIXES = {
    ".cpp",
    ".h",
    ".hpp",
    ".lean",
    ".md",
    ".py",
    ".tex",
    ".yml",
    ".yaml",
}
SKIP_DIR_NAMES = {".git", ".lake", "__pycache__", "build"}


def files_under(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIR_NAMES for part in path.parts):
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


def check_no_historical_copies_or_julia() -> None:
    for relative in sorted(FORBIDDEN_PATHS):
        if (ROOT / relative).exists():
            raise AssertionError(f"forbidden historical copy tree exists: {relative}")

    julia = [p.relative_to(ROOT) for p in files_under(ROOT) if p.suffix == ".jl"]
    if julia:
        raise AssertionError(f"tracked Julia sources remain: {julia}")


def check_no_duplicate_text_sources() -> None:
    groups: dict[str, list[Path]] = defaultdict(list)
    for path in files_under(ROOT):
        if path.suffix.lower() not in TEXT_DUPLICATE_SUFFIXES:
            continue
        data = path.read_bytes()
        if len(data) < 64:
            continue
        digest = hashlib.sha256(data).hexdigest()
        groups[digest].append(path.relative_to(ROOT))
    duplicates = [sorted(paths) for paths in groups.values() if len(paths) > 1]
    if duplicates:
        formatted = "; ".join(", ".join(map(str, group)) for group in duplicates)
        raise AssertionError(f"byte-identical maintained text/source duplicates: {formatted}")


def check_evidence_provenance() -> None:
    for path in sorted((ROOT / "evidence").rglob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        producer = data.get("producer")
        if producer:
            producer_path = ROOT / str(producer)
            if not producer_path.is_file():
                raise AssertionError(
                    f"{path.relative_to(ROOT)}: unresolved active producer {producer}"
                )
        refs = data.get("reference_inputs", {})
        if refs is not None:
            if not isinstance(refs, dict):
                raise AssertionError(
                    f"{path.relative_to(ROOT)}: reference_inputs must be an object"
                )
            for relative in refs:
                candidate = ROOT / relative
                if not candidate.is_file():
                    raise AssertionError(
                        f"{path.relative_to(ROOT)}: missing reference input {relative}"
                    )


def check_lean_import_graph() -> None:
    module_dir = ROOT / "formalization" / "Bgs"
    modules = {f"Bgs.{p.stem}" for p in module_dir.glob("*.lean")}
    imports = set()
    for line in (ROOT / "formalization" / "Bgs.lean").read_text(
        encoding="utf-8"
    ).splitlines():
        line = line.strip()
        if line.startswith("import "):
            imports.add(line.removeprefix("import ").strip())
    if modules != imports:
        missing = sorted(modules - imports)
        extra = sorted(imports - modules)
        raise AssertionError(f"Lean import mismatch: missing={missing}, extra={extra}")


def check_cpp_build_coverage() -> None:
    cmake = (ROOT / "CMakeLists.txt").read_text(encoding="utf-8")
    sources = sorted((ROOT / "computations" / "cpp").glob("*.cpp"))
    orphaned = [
        str(path.relative_to(ROOT))
        for path in sources
        if str(path.relative_to(ROOT)).replace("\\", "/") not in cmake
    ]
    if orphaned:
        raise AssertionError(f"C++ sources not covered by CMake: {orphaned}")


def check_readme_relative_links() -> None:
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    targets = re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text)
    missing: list[str] = []
    for raw in targets:
        target = raw.strip().split()[0].strip("<>")
        if (
            not target
            or target.startswith(("http://", "https://", "#", "mailto:"))
        ):
            continue
        target = target.split("#", 1)[0]
        if not target:
            continue
        if not (ROOT / target).exists():
            missing.append(raw)
    if missing:
        raise AssertionError(f"README relative links do not resolve: {missing}")


def main() -> None:
    check_top_level()
    check_no_historical_copies_or_julia()
    check_no_duplicate_text_sources()
    check_evidence_provenance()
    check_lean_import_graph()
    check_cpp_build_coverage()
    check_readme_relative_links()
    print("repository structural/provenance audit: PASS")


if __name__ == "__main__":
    main()
