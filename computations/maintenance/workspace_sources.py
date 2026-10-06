#!/usr/bin/env python3
"""Explicit, untrusted-by-default SHA-256 source snapshots for archive replay."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess

SCHEMA = 'bgs-archive-source-manifest-v1'
# Generated/developer state only. Historical evidence and binary inputs ARE hashed.
EXCLUDED = {'.git', 'build', '__pycache__', '.pytest_cache', '.mypy_cache',
            '.venv', 'venv', '.local', '.research-cache', 'scratch', '.lake',
            '.idea', '.vscode'}


def digest(path: Path) -> str:
    if path.is_symlink() or not path.is_file():
        raise ValueError(f'Source is missing, nonregular, or a symlink: {path}')
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_root(root: Path) -> bool:
    try:
        result = subprocess.run(['git', 'rev-parse', '--show-toplevel'], cwd=root,
                                text=True, capture_output=True, check=True)
        return Path(result.stdout.strip()).resolve() == root.resolve()
    except (OSError, subprocess.CalledProcessError):
        return False


def provenance(root: Path) -> dict:
    if not git_root(root):
        return {'input_commit': None, 'dirty': None, 'upstream_commit': None}
    commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
    dirty = bool(subprocess.check_output(['git', 'status', '--porcelain'], cwd=root, text=True))
    return {'input_commit': commit, 'dirty': dirty, 'upstream_commit': None}


def inventory(root: Path) -> dict[str, str]:
    paths = sorted(p for p in root.rglob('*')
                   if not any(part in EXCLUDED for part in p.relative_to(root).parts))
    return {p.relative_to(root).as_posix(): digest(p) for p in paths
            if p.is_file() or p.is_symlink()}


def read_manifest(path: Path) -> dict[str, str]:
    def unique_object(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f'Duplicate manifest key: {key}')
            result[key] = value
        return result
    data = json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique_object)
    if not isinstance(data, dict) or data.get('schema') != SCHEMA or 'upstream_commit' not in data or data['upstream_commit'] is not None:
        raise ValueError('Unknown manifest schema or unverified upstream commit claim')
    files = data.get('files')
    if not isinstance(files, dict) or not files:
        raise ValueError('Archive manifest must contain a nonempty files map')
    for rel, value in files.items():
        p = PurePosixPath(rel)
        if (not rel or not p.parts or p.is_absolute() or '..' in p.parts or str(p) != rel
                or '\\' in rel or any(part in EXCLUDED for part in p.parts)):
            raise ValueError(f'Unsafe/excluded manifest path: {rel!r}')
        if not isinstance(value, str) or len(value) != 64 or any(c not in '0123456789abcdef' for c in value):
            raise ValueError(f'Invalid SHA-256 for {rel}')
    return files


def validate(root: Path, expected: dict[str, str]) -> dict[str, str]:
    actual = inventory(root)
    if actual != expected:
        missing = sorted(expected.keys() - actual.keys())
        added = sorted(actual.keys() - expected.keys())
        changed = sorted(p for p in actual.keys() & expected.keys() if actual[p] != expected[p])
        raise ValueError(f'Archive source mismatch: missing={missing}, added={added}, changed={changed}')
    return actual


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--output', type=Path, required=True,
                        help='Use build/ or a destination outside the source root.')
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output.resolve()
    if output.is_relative_to(root) and not any(p in EXCLUDED for p in output.relative_to(root).parts):
        parser.error('Manifest output must be outside the inventoried source (for example build/).')
    files = inventory(root)
    if not files:
        parser.error('Source inventory is empty')
    data = {'schema': SCHEMA, 'upstream_commit': None,
            'provenance': 'Local byte snapshot; neither authenticates an upstream commit nor proves correctness.',
            'files': files}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(f'Wrote {len(files)} file hashes to {output}; upstream_commit=null')


if __name__ == '__main__':
    main()
