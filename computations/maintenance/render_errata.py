#!/usr/bin/env python3
"""Render ERRATA.md from record/errata.json."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'record'/'errata.json'
TARGET=ROOT/'ERRATA.md'

def esc(value: object) -> str:
    return str(value).replace('|',r'\|').replace('\n',' ')

def render() -> str:
    data=json.loads(SOURCE.read_text(encoding='utf-8'))
    rows=sorted(data['entries'],key=lambda row:row['id'])
    out=[
        '# Errata and permanent corrections','',
        'This file is generated from `record/errata.json`. The complete failure',
        'mechanisms and historical context remain authoritative in',
        '`record/retractions.md`.','',
        '| ID | Affected route | Disposition | Downstream status |',
        '|---|---|---|---|',
    ]
    for row in rows:
        out.append(
            f"| `{esc(row['id'])}` | {esc(row['title'])} | "
            f"{esc(row['disposition'])} | {esc(row['downstream'])} |"
        )
    out.extend(['',
        'New scientific corrections are recorded in `record/retractions.md` first,',
        'then normalized into `record/errata.json` and regenerated here.',''])
    return '\n'.join(out)

def main() -> int:
    parser=argparse.ArgumentParser()
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    expected=render()
    if args.check:
        if not TARGET.is_file() or TARGET.read_text(encoding='utf-8')!=expected:
            raise SystemExit('ERRATA.md is stale; run render_errata.py')
        print('errata-render: OK')
        return 0
    TARGET.write_text(expected,encoding='utf-8')
    print(TARGET.relative_to(ROOT))
    return 0

if __name__=='__main__':
    raise SystemExit(main())
