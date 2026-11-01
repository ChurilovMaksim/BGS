#!/usr/bin/env python3
"""Render manuscript/appendix_a_claim_index.tex from record/claims.json.

The appendix maps every registered claim to its mentions in the TeX inputs
reachable from manuscript/BGS_unified.tex (excluding the appendix itself).
A mention is either the full identifier (``BGS-TRACE-095``) or, for the
TRACE family only, the short form used in section prose (``TRACE-095``),
provided the full identifier exists in the registry.  The claim-state figure
is drawn in TikZ from the same registry counts, so the appendix cannot drift
from the registry silently.  ``--check`` fails if the committed file differs.

The output records navigation only; it certifies nothing mathematically.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
MANUSCRIPT = ROOT / 'manuscript'
TARGET = MANUSCRIPT / 'appendix_a_claim_index.tex'
STATES = ('proved', 'verification-pending', 'conditional', 'open', 'refuted')
FULL = re.compile(r'(?<![A-Za-z0-9])BGS-[A-Z]+-\d{3,4}(?![0-9])')
SHORT = re.compile(r'(?<![A-Za-z0-9-])TRACE-(\d{3})(?![0-9])')


def reachable() -> list[Path]:
    """TeX inputs in depth-first \\input order, master first, appendix excluded."""
    order: list[Path] = []
    seen: set[Path] = set()

    def visit(path: Path) -> None:
        path = path.resolve()
        if path in seen or not path.is_file():
            return
        seen.add(path)
        order.append(path)
        for line in path.read_text(encoding='utf-8').splitlines():
            code = re.split(r'(?<!\\)%', line, maxsplit=1)[0]
            for rel in re.findall(r'\\input\{([^}]+)\}', code):
                target = MANUSCRIPT / rel
                if not target.suffix:
                    target = target.with_suffix('.tex')
                visit(target)

    visit(MANUSCRIPT / 'BGS_unified.tex')
    return [p for p in order if p != TARGET.resolve()]


def mentions(known: set[str]) -> dict[str, list[tuple[str, int]]]:
    found: dict[str, list[tuple[str, int]]] = {}
    for path in reachable():
        rel = path.relative_to(MANUSCRIPT.resolve()).as_posix()
        for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            code = re.split(r'(?<!\\)%', line, maxsplit=1)[0]
            ids = set(FULL.findall(code))
            ids |= {f'BGS-TRACE-{m}' for m in SHORT.findall(code)}
            for cid in ids & known:
                entry = found.setdefault(cid, [])
                if (rel, number) not in entry:
                    entry.append((rel, number))
    return found


def figure(counts: Counter) -> list[str]:
    total = sum(counts.values())
    scale = 9.0 / max(counts.values())
    lines = [r'\begin{figure}[htbp]', r'\centering',
             r'\begin{tikzpicture}[x=1cm,y=0.62cm]']
    for row, state in enumerate(STATES):
        y = -row
        width = counts[state] * scale
        lines.append(rf'\node[anchor=east,font=\small] at (-0.15,{y}) {{{state}}};')
        if width:
            lines.append(rf'\fill[black!{60 - 10 * row}] (0,{y - 0.3:.2f}) rectangle ({width:.3f},{y + 0.3:.2f});')
        lines.append(rf'\node[anchor=west,font=\small] at ({width + 0.1:.3f},{y}) {{{counts[state]}}};')
    lines += [r'\end{tikzpicture}',
              rf'\caption{{Registered claim states ({total} claims), drawn from \texttt{{record/claims.json}}. '
              r'``Proved'' is the registered project scope, not external refereeing.}',
              r'\label{fig:registry-status}', r'\end{figure}']
    return lines


def render() -> str:
    data = json.loads((ROOT / 'record/claims.json').read_text(encoding='utf-8'))
    claims = sorted(data['claims'], key=lambda c: c['id'])
    known = {c['id'] for c in claims}
    counts = Counter(c['state'] for c in claims)
    unknown = set(counts) - set(STATES)
    if unknown:
        raise SystemExit(f'Unknown claim states: {sorted(unknown)}')
    where = mentions(known)
    out = [
        r'\section*{Appendix A: Claim index}',
        r'This index is generated from \path{record/claims.json} by',
        r'\path{computations/maintenance/render_appendix_a.py}.',
        f'The registry contains {len(claims)} claims: {counts["proved"]} proved, '
        f'{counts["verification-pending"]} verification-pending,',
        f'{counts["conditional"]} conditional, {counts["open"]} open and '
        f'{counts["refuted"]} refuted. ``Proved\'\' denotes the registered project scope,',
        r"not independent external refereeing. The table maps each ID to its current",
        r"mentions in the manuscript's reachable TeX inputs, excluding this index itself;",
        r'the short form TRACE-$nnn$ used in section prose counts as a mention.',
        r'A registry-only entry has no body mention; its proof and evidence remain in',
        r'its authoritative source. In particular, the Lines I--N results',
        r'(BGS-TRACE-211 onwards, including the conditional Theorem R$\sharp$-mod v4,',
        r'BGS-TRACE-299) are not yet written up in this manuscript and appear here as',
        r'registry-only; see \path{RESULTS.md}. File line numbers are navigation, not proof certification.',
    ]
    out += figure(counts)
    out += [
        r'\begin{center}', r'\small',
        r'\begin{longtable}{>{\raggedright\arraybackslash}p{0.18\textwidth}>{\raggedright\arraybackslash}p{0.16\textwidth}>{\raggedright\arraybackslash}p{0.52\textwidth}}',
        r'Claim ID & State & Manuscript mentions (file:line) \\', r'\hline', r'\endfirsthead',
        r'Claim ID & State & Manuscript mentions (file:line) \\', r'\hline', r'\endhead',
    ]
    for claim in claims:
        refs = where.get(claim['id'], [])
        cell = '; '.join(rf'\path{{{f}}}:{n}' for f, n in refs) if refs else '--- (registry only)'
        out.append(rf'\texttt{{{claim["id"]}}} & {claim["state"]} & {cell} \\')
    out += [r'\end{longtable}', r'\end{center}']
    return '\n'.join(out) + '\n'


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='fail if the committed appendix is stale')
    args = parser.parse_args()
    text = render()
    if args.check:
        current = TARGET.read_text(encoding='utf-8') if TARGET.exists() else ''
        if current != text:
            print('appendix A is stale; run computations/maintenance/render_appendix_a.py', file=sys.stderr)
            return 1
        print('appendix-a: OK')
        return 0
    TARGET.write_text(text, encoding='utf-8')
    print(f'wrote {TARGET.relative_to(ROOT)}')
    return 0


if __name__ == '__main__':
    if not __debug__:
        raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
    sys.exit(main())
