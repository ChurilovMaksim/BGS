#!/usr/bin/env python3
"""Generate the fixed-map manuscript chapter from its maintained proof source."""
import argparse
import hashlib
import json
import re
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT/'mathematics/fixed-map/fixed_map_resolvent_frontier.md'
TARGET = ROOT/'manuscript/unified_sections/fixed_map_frontier.tex'



def normalize_table_rules(body: str) -> str:
    """Canonicalize Pandoc 2.17/3.1.3 booktabs-only footer placement.

    The renderer changed presentation, not table cells. Normalize only the
    exact empty last-foot form; retain all content and fail-closed comparison.
    """
    def table(match):
        block = match.group(0)
        footer = '\\bottomrule\\noalign{}\n\\endlastfoot\n'
        if footer not in block:
            return block
        block = block.replace(footer, '', 1)
        block = block.replace('\\toprule\\noalign{}', '\\toprule')
        block = block.replace('\\midrule\\noalign{}', '\\midrule')
        return block.replace('\\end{longtable}', '\\bottomrule\n\\end{longtable}', 1)
    return re.sub(r'\\begin\{longtable\}.*?\\end\{longtable\}',
                  table, body, flags=re.DOTALL)


def normalize_longtable_caption_type(body: str) -> str:
    """Drop Pandoc 3.12.1's captionless-longtable counter guard.

    Pandoc 3.12.1 wraps captionless longtables in
    {\\def\\LTcaptype{none} ... \\end{longtable} \\n}. Local TeX Live
    2026's longtable errors on it ("No counter 'none' defined",
    reproduced in isolation on the fixed-map frontier table). A
    captionless longtable never steps any counter, so removing the
    wrapper is behavior-preserving. A captioned table carrying the
    guard, or any surviving guard after substitution, fails loudly
    instead of silently renumbering tables or breaking the build.
    Follows the normalize_table_rules precedent in this file.
    """
    def strip(match):
        block = match.group(1)
        if '\\caption' in block:
            raise ValueError('captioned longtable with LTcaptype guard: refusing to strip')
        return block
    body = re.sub(r'\{\\def\\LTcaptype\{none\} % do not increment counter\n'
                  r'(\\begin\{longtable\}.*?\\end\{longtable\})\n\}',
                  strip, body, flags=re.DOTALL)
    if 'LTcaptype' in body:
        raise ValueError('surviving LTcaptype guard after normalization')
    return body


def render():
    ast = json.loads(subprocess.run(['pandoc','-f','markdown','-t','json'],
        input=SOURCE.read_text(),text=True,capture_output=True,check=True).stdout)
    def visit(node):
        if isinstance(node, dict):
            if node.get('t') == 'Link':
                url = node['c'][2][0]
                if not url.startswith(('http:', 'https:', '#')):
                    rel = (SOURCE.parent/url).resolve().relative_to(ROOT)
                    if not (ROOT/rel).is_file():
                        raise ValueError('Missing manuscript link: '+str(rel))
                    node['c'][2][0] = 'https://github.com/ChurilovMaksim/BGS/blob/main/'+str(rel)
            for value in node.values():
                visit(value)
        elif isinstance(node, list):
            for value in node:
                visit(value)
    visit(ast)
    body = subprocess.run(['pandoc','-f','json','-t','latex','--id-prefix=fixed-map-',
                           '--wrap=preserve'],input=json.dumps(ast),text=True,
                          capture_output=True,check=True).stdout
    body = normalize_table_rules(body)
    body = normalize_longtable_caption_type(body)
    return ('% Source SHA256: '+hashlib.sha256(SOURCE.read_bytes()).hexdigest()+'\n'+body)



# Wave 4(c) pandoc pin: byte-exact --check output is pandoc-version-sensitive
# (the pre-regen TeX carried \\hypertarget wrappers that pandoc 3.12.1 does
# not emit). All sync output in this repo is generated with pandoc 3.12.1;
# CI must install that exact version (see the Wave 4 report for the workflow
# pin). Any other version fails loudly here instead of producing silent drift.
PANDOC_VERSION = 'pandoc 3.12.1'
def require_pandoc():
    try:
        out = subprocess.run(['pandoc', '--version'], capture_output=True, text=True, check=True).stdout
    except FileNotFoundError:
        raise RuntimeError('pandoc not found on PATH; sync requires pandoc 3.12.1')
    first = out.splitlines()[0] if out.splitlines() else ''
    if first != PANDOC_VERSION:
        raise RuntimeError('sync requires %s, found %r; byte-exact output is pandoc-version-sensitive' % (PANDOC_VERSION, first))

if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--check', action='store_true')
    args = p.parse_args()
    # Wave 4(c) correction (parent decision): TARGET is hand-edited since
    # Pass 1/2 (amsthm conversions incl. Theorem 70.8 FLOW-020 + scope note).
    # Regenerating it from .md would silently destroy those edits (verified:
    # regen drops all 17 amsthm environments to 0). TeX is the source of
    # truth for this file, so sync neither checks nor writes it; this guard
    # exists so no future regen run can repeat that destruction.
    if True:  # hand-edited target guard (TARGET only; see comment above)
        if args.check:
            print('SKIP fixed-map source synchronization: TARGET hand-edited since Pass 1/2; TeX is source of truth')
            raise SystemExit(0)
        raise SystemExit('refusing to overwrite hand-edited TARGET (Pass 1/2 amsthm conversions); TeX is source of truth')
    require_pandoc()
    expected = render()
    if args.check:
        if not TARGET.is_file() or TARGET.read_text() != expected:
            raise SystemExit('Stale fixed-map manuscript section')
    else:
        TARGET.write_text(expected)
    print('PASS fixed-map source synchronization')
