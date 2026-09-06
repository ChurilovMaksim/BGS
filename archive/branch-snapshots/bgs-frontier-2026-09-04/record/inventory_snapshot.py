#!/usr/bin/env python3
"""Create a deterministic per-file inventory for a preserved research ZIP.

Usage:
    python record/inventory_snapshot.py /path/to/BGS.zip > snapshot_manifest.tsv

The output columns are path, uncompressed bytes, SHA-256, coarse class and the
first byte-identical path (if any). The script never interprets a claim as
true merely because a file exists.
"""
from __future__ import annotations

import hashlib
import sys
import zipfile
from collections import Counter
from pathlib import PurePosixPath


def classify(path: str) -> str:
    p = path.lower()
    suffix = PurePosixPath(path).suffix.lower()
    if "/.lake/build/" in p or "/.lake/packages/" in p:
        return "generated-formal-build"
    if suffix == ".jl":
        return "julia-source"
    if suffix == ".lean":
        return "lean-source"
    if suffix in {".py", ".c", ".cc", ".cpp", ".h", ".hpp", ".js"}:
        return "code-source"
    if suffix == ".tex":
        return "manuscript-source"
    if suffix == ".pdf":
        return "compiled-paper-or-reference"
    if suffix == ".json":
        return "research-data"
    if suffix in {".log", ".out", ".err", ".hash"}:
        return "run-record"
    if suffix == ".md":
        if "/review/" in p or "/audit/" in p:
            return "review-record"
        if "/archive/" in p or "history" in p:
            return "historical-note"
        return "research-note"
    return "other"


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: inventory_snapshot.py BGS.zip")
    zip_path = sys.argv[1]
    seen: dict[str, str] = {}
    class_counts: Counter[str] = Counter()
    with zipfile.ZipFile(zip_path) as archive:
        infos = sorted((i for i in archive.infolist() if not i.is_dir()), key=lambda i: i.filename)
        print("path\tbytes\tsha256\tclass\tduplicate_of")
        for info in infos:
            data = archive.read(info)
            digest = hashlib.sha256(data).hexdigest()
            category = classify(info.filename)
            class_counts[category] += 1
            duplicate_of = seen.setdefault(digest, info.filename)
            if duplicate_of == info.filename:
                duplicate_of = ""
            print(f"{info.filename}\t{len(data)}\t{digest}\t{category}\t{duplicate_of}")
    print("# class counts: " + ", ".join(f"{k}={v}" for k, v in sorted(class_counts.items())), file=sys.stderr)


if __name__ == "__main__":
    main()
