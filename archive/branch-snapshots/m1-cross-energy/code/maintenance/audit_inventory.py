"""Build a deterministic inventory of the WoW repository.

The inventory is descriptive, not a proof certificate.  It records every
tracked-style file visible in a checkout, its SHA-256 digest, trust layer,
duplicate relationship, and a few migration/status sentinels.  Generated
caches and runtime scratch files are excluded.
"""
from __future__ import annotations

from collections import defaultdict
from datetime import date
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs" / "audit" / "FILE_INVENTORY.generated.json"

SKIP_PARTS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".venv",
    "venv",
}
SKIP_PREFIXES = (
    "archive/legacy-workspace/",
    "formal/.lake/build/",
    "formal/.lake/packages/",
    "scratch/",
    ".local/",
)
TEXT_EXTS = {
    ".py", ".md", ".tex", ".txt", ".jl", ".js", ".mjs", ".sh",
    ".toml", ".cmd", ".log", ".err",
}
STALE_TOKENS = ("src/", "artifacts/", "LEDGER.md", "ROADMAP.md")
STATUS_MARKERS = (
    "[PROVEN]", "[CONJECTURED]", "[NUMERICALLY-SUPPORTED]", "OPEN GAP",
    "RETRACT", "VOID", "QUARANTIN",
)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def skipped(path: Path) -> bool:
    r = rel(path)
    if any(part in SKIP_PARTS for part in path.relative_to(ROOT).parts):
        return True
    if r in {"docs/audit/FILE_INVENTORY.generated.json", "docs/audit/FILE_INVENTORY_SUMMARY.json"}:
        return True
    if any(r.startswith(prefix) for prefix in SKIP_PREFIXES):
        return True
    if r.startswith("results/") and r.endswith(".log"):
        return True
    return False


def trust_layer(r: str) -> str:
    if r.startswith("archive/legacy-workspace/"):
        return "historical"
    if r.startswith("code/legacy_") or r.startswith("paper/historical_snapshots/"):
        return "historical"
    if r.startswith("docs/archive/") or r in {
        "docs/THEORY_FULL_PRE_REBUILD.md",
        "docs/HISTORY_FULL_PRE_REBUILD.md",
        "data/LEGACY_MANIFEST.md",
    }:
        return "historical"
    canonical_prefixes = (
        "research/", "code/math/", "code/verification/", "code/experiments/",
        "code/maintenance/", "results/verified/", "results/numerical/",
        "results/historical-numerical/", "inputs/", "formal/",
    )
    if r in {"README.md", "STATUS.md", "THEORY.md", "HISTORY.md", "HANDBOOK.md", "requirements.txt", ".gitignore"}:
        return "canonical"
    if r.startswith(canonical_prefixes):
        return "canonical"
    return "research"


def main() -> int:
    paths = sorted(p for p in ROOT.rglob("*") if p.is_file() and not skipped(p))
    digest_to_paths: dict[str, list[str]] = defaultdict(list)
    raw: list[dict[str, object]] = []

    for path in paths:
        r = rel(path)
        data = path.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        digest_to_paths[digest].append(r)
        item: dict[str, object] = {
            "path": r,
            "size": len(data),
            "sha256": digest,
            "extension": path.suffix.lower() or None,
            "trust": trust_layer(r),
        }
        if path.suffix.lower() in TEXT_EXTS:
            try:
                text = data.decode("utf-8-sig")
            except UnicodeDecodeError as exc:
                item["text_decode"] = f"FAIL: {exc}"
            else:
                stale = [token for token in STALE_TOKENS if token in text]
                markers = [marker for marker in STATUS_MARKERS if marker in text]
                if stale:
                    item["stale_tokens"] = stale
                if markers:
                    item["status_markers"] = markers
        raw.append(item)

    first_for_digest = {digest: min(items) for digest, items in digest_to_paths.items()}
    duplicate_groups = 0
    duplicate_copies = 0
    for item in raw:
        digest = str(item["sha256"])
        members = digest_to_paths[digest]
        if len(members) > 1:
            item["duplicate_of"] = first_for_digest[digest]
    for members in digest_to_paths.values():
        if len(members) > 1:
            duplicate_groups += 1
            duplicate_copies += len(members) - 1

    trust_counts: dict[str, int] = defaultdict(int)
    for item in raw:
        trust_counts[str(item["trust"])] += 1

    payload = {
        "schema": 1,
        "generated_for_audit_date": str(date(2026, 9, 3)),
        "note": "Generated inventory of the working/corpus surface outside the embedded legacy-workspace snapshot; trust labels describe repository role, not mathematical truth.",
        "embedded_archive_snapshot": {"path": "archive/legacy-workspace/", "tree_sha": "6c17a3536a60321f11d2e6a5b3d62b222d1bb6f6", "coverage": "reviewed separately against the pre-Git ZIP and preserved as provenance"},
        "self_excluded": "docs/audit/FILE_INVENTORY.generated.json",
        "summary": {
            "files": len(raw),
            "unique_sha256": len(digest_to_paths),
            "duplicate_groups": duplicate_groups,
            "duplicate_path_copies": duplicate_copies,
            "trust_counts": dict(sorted(trust_counts.items())),
        },
        "files": raw,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
