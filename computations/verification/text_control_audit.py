#!/usr/bin/env python3
"""Reject C0 bytes other than TAB/LF in maintained UTF-8 text.

Finite byte hygiene only, not mathematical validation. Binary artifacts and
immutable evidence/archive history are outside this editing policy.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'maintenance'))
from workspace_sources import EXCLUDED

ROOT = Path(__file__).resolve().parents[2]
TEXT_SUFFIXES = {'.md', '.tex', '.bib', '.py', '.cpp', '.hpp', '.h', '.c',
                 '.json', '.toml', '.yaml', '.yml', '.txt', '.lean', '.sh',
                 '.csv', '.tsv', '.cff', '.sty', '.cls', '.cmake'}
TEXT_NAMES = {'AGENTS.md', '.gitignore', 'lean-toolchain', 'LICENSE', 'Makefile'}


def violations(root: Path) -> list[str]:
    errors = []
    for p in sorted(root.rglob('*')):
        rel = p.relative_to(root)
        if any(part in EXCLUDED for part in rel.parts) or rel.parts[0] in {'archive', 'evidence', 'papers'}:
            continue
        if not p.is_file() or (p.suffix.lower() not in TEXT_SUFFIXES and p.name not in TEXT_NAMES):
            continue
        raw = p.read_bytes()
        try:
            raw.decode('utf-8')
        except UnicodeDecodeError:
            errors.append(f'{rel}: maintained text is not UTF-8')
        for offset, value in enumerate(raw):
            if value < 32 and value not in (9, 10):
                errors.append(f'{rel}: byte {offset}: forbidden C0 0x{value:02x}')
    return errors


def main() -> None:
    errors = violations(ROOT)
    if errors:
        raise SystemExit('\n'.join(errors))
    print('Maintained-text C0/UTF-8 audit passed (binary/evidence/archive/papers excluded).')


if __name__ == '__main__':
    main()
