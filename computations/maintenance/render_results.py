#!/usr/bin/env python3
"""Render RESULTS.md, the top-level summary of what the programme established.

Inputs: record/claims.json (states, titles, sources, Lean links),
record/results_spec.json (headline selection, short labels, known issues),
formalization/Bgs/*.lean (module and legacy native_decide counts) and
computations/maintenance/frozen_evidence_packets.json. States always come from
the registry; the spec never asserts a state. RESULTS.md is a navigation
surface, not a status authority (see SOURCE_OF_TRUTH.md).

  python computations/maintenance/render_results.py          # write
  python computations/maintenance/render_results.py --check  # fail if stale
"""
from __future__ import annotations
import argparse
import collections
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = 'RESULTS.md'
STATES = ('proved', 'verification-pending', 'conditional', 'open', 'refuted')
STATE_TEXT = {
    'proved': 'proved',
    'verification-pending': 'verification-pending',
    'conditional': 'conditional',
    'open': 'open',
    'refuted': 'refuted',
}


def cell(text: str) -> str:
    return text.replace('|', '\\|').replace('\n', ' ')


def lean_stats(root: Path) -> dict:
    files = sorted((root / 'formalization' / 'Bgs').rglob('*.lean'))
    uses = {}
    for f in files:
        s = f.read_text(encoding='utf-8')
        s = re.sub(r'/-.*?-/', '', s, flags=re.S)
        s = re.sub(r'--[^\n]*', '', s)
        s = re.sub(r'"[^"\n]*"', '', s)
        n = len(re.findall(r'\bnative_decide\b', s))
        if n:
            uses[f.relative_to(root / 'formalization').as_posix()] = n
    return {'modules': len(files), 'native': uses}


def render(root: Path = ROOT) -> str:
    reg = json.loads((root / 'record/claims.json').read_text(encoding='utf-8'))
    spec = json.loads((root / 'record/results_spec.json').read_text(encoding='utf-8'))
    if spec.get('schema') != 'bgs-results-spec-v1':
        raise SystemExit('results spec schema changed')
    claims = {c['id']: c for c in reg['claims']}
    count = collections.Counter(c['state'] for c in reg['claims'])
    if set(count) - set(STATES):
        raise SystemExit('unknown registry state: ' + ', '.join(sorted(set(count) - set(STATES))))
    lean_claims = sum(1 for c in reg['claims'] if c['formalization'] and c['state'] != 'open')
    lean = lean_stats(root)
    frozen = json.loads((root / 'computations/maintenance/frozen_evidence_packets.json').read_text(encoding='utf-8'))
    for c in ('BGS-BGS-001', 'BGS-TRACE-005', 'BGS-TRACE-206'):
        if claims[c]['state'] != 'open':
            raise SystemExit(c + ' is no longer open: rewrite the RESULTS.md summary by hand before rendering')
    if claims['BGS-TRACE-325']['state'] != 'conditional':
        raise SystemExit('BGS-TRACE-325 is no longer conditional: rewrite the RESULTS.md summary by hand before rendering')
    total = len(reg['claims'])
    L = []
    w = L.append
    w('# BGS programme: what was achieved')
    w('')
    w(f'*Generated from [`record/claims.json`](record/claims.json) (registry updated {reg["updated"]}) and '
      '[`record/results_spec.json`](record/results_spec.json) by `computations/maintenance/render_results.py`. '
      'Do not edit by hand. This page is a summary for navigation. The registry decides every status; see '
      '[SOURCE_OF_TRUTH.md](SOURCE_OF_TRUTH.md).*')
    w('')
    w('## In one paragraph')
    w('')
    w('This repository studies the Bohigas–Giannoni–Schmit (BGS) conjecture for one explicitly specified quantized, kicked cat '
      'map on the torus. **The BGS limit for this map is not proved.** Fixed-strength microscopic universality '
      '(BGS-BGS-001) and the model-specific signed trace estimate that would close the gap (BGS-TRACE-005) are both **open**. '
      f'Around that target, the programme registers {total} precisely scoped claims. {count["proved"]} are proved at their stated '
      'scope (project proofs, many computer-assisted, many with an internal independent referee, none externally refereed). '
      'The work ran in eight phases from September to November 2026: Cayley arithmetic, Pell return laws, resonance '
      'cohomology and locality (Phase I); the structure of the fixed map, the exact trace-to-statistics bridge and noisy '
      'Dyson comparisons (Phase II); phase channels, clock laws, collision laws and obstructions (Phase III); uniform '
      'power-trace bounds for the original kick family (Phase IV); arithmetic Abel spikes and exact random-phase form factors '
      '(Phase V); the fixed diagonal kick and a computer-assisted refutation of Conjecture R at η = 2 (BGS-TRACE-179, '
      'Phase VI, Lines B–H); the corrected mean law R′ (BGS-TRACE-206, Phase VII, Lines I–N), which remains **open and '
      'is not refuted**; and five integrations on 4–5 November 2026 (Phase VIII, BGS-TRACE-337..355: the span theorem, '
      'Lemma W with an explicit H6 threshold that is conditional on squarefree h_p and an assumed normalization u = 1, the H7* scope, the arithmetic of h_p, and Lemma S with the polymer gap lemma, the Binet '
      'lattice generator and a conditional H5(b) cross-line constant). The end point of Phase VII, **Theorem R♯-mod v5 (BGS-TRACE-325), is conditional**: it reduces the '
      'failure of frozen R′ along m = 3p to explicitly listed open inputs H0, H1 and H5–H8.')
    w('')
    w('## Status at a glance')
    w('')
    w('| Registered state | Claims | Meaning |')
    w('|---|---:|---|')
    meaning = {
        'proved': 'Project proof at the stated scope, including computer-assisted proofs; not external refereeing',
        'verification-pending': 'Argument or computation exists; an independent check is outstanding',
        'conditional': 'Proved implication from stated hypotheses that are themselves open',
        'open': 'Conjecture, hypothesis or programme obligation without a proof',
        'refuted': 'Shown false as stated',
    }
    for s in STATES:
        w(f'| {STATE_TEXT[s]} | {count.get(s, 0)} | {meaning[s]} |')
    w(f'| **total** | **{total}** | |')
    w('')
    w(f'{lean_claims} non-open claims link Lean 4 files, out of {lean["modules"]} modules in `formalization/Bgs`. '
      'Lean certifies the finite or arithmetic statements named in each claim boundary, not the full analytic arguments.')
    w('')
    w('## Headline results')
    w('')
    w('This is a selection. The complete per-claim list is [`record/claim_registry.md`](record/claim_registry.md), and the '
      'theorem families with their limits are in [`mathematics/results.md`](mathematics/results.md).')
    for g in spec['groups']:
        w('')
        w('### ' + g['title'])
        w('')
        if g.get('note'):
            w(g['note'])
            w('')
        w('| Claim | State | Result (short label) | Lean | Source |')
        w('|---|---|---|---|---|')
        for cid, label in g['claims']:
            if cid not in claims:
                raise SystemExit('results spec names an unknown claim: ' + cid)
            c = claims[cid]
            if c['formalization']:
                leanmark = 'statement only' if c['state'] == 'open' else 'yes'
            else:
                leanmark = '—'
            src = c['source']
            w(f'| `{cid}` | **{c["state"]}** | {cell(label)} | {leanmark} | [{Path(src).name}]({src}) |')
    w('')
    w('## How to read this repository')
    w('')
    w('* **Start here**, then go to [RESEARCH.md](RESEARCH.md) for the dated research brief, '
      '[docs/reader_guide.en.md](docs/reader_guide.en.md) (or [Russian](docs/reader_guide.ru.md)) for the mathematical '
      'introduction, and [docs/corpus_atlas.md](docs/corpus_atlas.md) for a map of every proof note.')
    w('* **Status labels.** Use only the registry state. Inside a note, [P] marks a paper proof, [CA] and [CA-fp] '
      'computer-assisted steps (interval arithmetic or floating point), [N] numerics, which are evidence and not proof, '
      'and [H] a hypothesis. A conditional theorem is exactly as strong as its weakest open input.')
    w('* **Where things live.** `mathematics/` holds proofs and their boundaries. `computations/verification/` holds '
      'reproducible checks; the `line*/` folders are frozen author and referee packets. `evidence/` holds dated receipts. '
      '`formalization/` holds the Lean 4 kernels. `record/` holds the registry, ledger and audits. `manuscript/` holds the '
      'unified PDF source.')
    w('* **Reproduce.** `python computations/verification/scientific_registry_audit.py` checks the registry. '
      '`python -m unittest discover -s computations/maintenance/tests` runs the maintenance tests. `cd formalization && lake '
      'exe cache get && lake build` builds Lean. `python computations/maintenance/build_unified_manuscript.py --output-dir '
      'out` builds the manuscript (pdflatex or tectonic). See [REPRODUCE_unified.md](REPRODUCE_unified.md).')
    w('')
    w('## Known issues')
    w('')
    native = lean['native']
    fmt = {
        'native_decide_uses': sum(native.values()),
        'native_decide_modules': len(native),
        'native_decide_list': ', '.join(f'`{Path(k).stem}` ({v})' for k, v in sorted(native.items())),
        'frozen_files': len(frozen['files']),
    }
    for item in spec['known_issues']:
        w('* ' + item.format(**fmt))
    w('')
    return '\n'.join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    text = render()
    path = ROOT / OUT
    if a.check:
        if not path.is_file() or path.read_text(encoding='utf-8') != text:
            print('results-render: STALE (run computations/maintenance/render_results.py)', file=sys.stderr)
            return 1
        print('results-render: OK')
        return 0
    path.write_text(text, encoding='utf-8')
    print(OUT)
    return 0


if __name__ == '__main__':
    sys.exit(main())
