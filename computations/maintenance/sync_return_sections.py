#!/usr/bin/env python3
"""Keep the return-law TeX chapters synchronized with their mathematical sources.

Pandoc preserves TeX mathematics. Equation tags receive a chapter-family
prefix to distinguish them from the older manuscript. --check never writes.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
SOURCES = (
    ('returns/fixed_harmonic_return_gas', 'gas'),
    ('returns/analytic_kick_return_gas', 'position'),
    ('returns/periodic_point_trace_comparison', 'periodic'),
    ('returns/phase_space_return_gas', 'phase'),
    ('returns/general_cat_return_laws', 'general'),
    ('returns/return_trace_obstruction', 'obstruction'),
)


def render(name, prefix):
    source = ROOT/'mathematics'/f'{name}.md'
    text = source.read_text()
    # LaTeX supplies hierarchical heading numbers; avoid printing them twice.
    text = re.sub(r'^(#{2,6}\s+)\d+(?:\.\d+)*\.?\s+', r'\1', text, flags=re.M)
    # New-family equation numbers are unique in the consolidated publication.
    text = re.sub(r'\\tag\{([UPRGAS]\d+[a-z]?)\}',r'\\tag{Ret.\1}',text)
    text = re.sub(r'\(([UPRGAS]\d+[a-z]?)\)',r'(Ret.\1)',text)
    # Links to other proof modules remain navigable in the source repository.
    parsed=subprocess.run(['pandoc','--from=markdown+tex_math_dollars','--to=json'],
                          input=text,text=True,check=True,capture_output=True)
    document=json.loads(parsed.stdout)
    mathematics=[]
    def links(node):
        if isinstance(node,dict):
            if node.get('t')=='Math':
                mathematics.append(node['c'][1])
            if node.get('t')=='Link':
                target=node['c'][2][0]
                if not target.startswith(('http:', 'https:', '#')):
                    relative=(source.parent/target).resolve().relative_to(ROOT)
                    node['c'][2][0]='https://github.com/ChurilovMaksim/BGS/blob/main/'+str(relative)
            for value in node.values():links(value)
        elif isinstance(node,list):
            for value in node:links(value)
    links(document)
    result = subprocess.run(
        ['pandoc','--from=json','--to=latex',
         '--id-prefix=return-'+prefix+'-','--wrap=preserve'],
        input=json.dumps(document),text=True,check=True,capture_output=True).stdout
    # The source modules have local section/theorem numbering. Make that
    # convention explicit instead of silently pointing at unrelated chapters.
    note = (r'\par\smallskip\noindent\emph{Numbering convention: section and theorem '
            r'references within this chapter use the source module\textquotesingle s local '
            r'numbering; source Section 1 is subsection \thesection.1. '
            r'Equation references carry the prefix Ret.}\par\smallskip'+'\n')
    first_label = result.index('\n', result.index(r'\label{')) + 1
    result = result[:first_label] + note + result[first_label:]
    # These marks are legal UTF-8 prose but unsupported by the pinned pdfLaTeX setup.
    for a,b in {'²':'\\textsuperscript{2}','⁴':'\\textsuperscript{4}',
                '≤':r'\(\le\)','≥':r'\(\ge\)','→':r'\(\to\)'}.items():
        result=result.replace(a,b)
    for formula in mathematics:
        if formula not in result:
            raise RuntimeError('Math content changed while converting '+str(source)+': '+formula[:80])
    header=('% Source: mathematics/'+name+'.md\n'
            '% Source SHA256: '+hashlib.sha256(source.read_bytes()).hexdigest()+'\n')
    return header+result



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

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    require_pandoc()
    # Wave 4(c) correction (parent decision): ALL six return-law chapters are
    # hand-edited since Pass 1 (amsthm conversions); regen from .md would
    # silently destroy those edits (verified: regen drops every amsthm
    # environment to 0). TeX is the source of truth for these files; sync
    # neither checks nor writes them. A future non-hand-edited chapter still
    # goes through the byte-exact path below. Write mode refuses up front
    # (before any write) so a regen run can never partially overwrite.
    HAND_EDITED_PREFIXES={'gas','position','periodic','phase','general','obstruction'}
    if not args.check and any(prefix in HAND_EDITED_PREFIXES for _,prefix in SOURCES):
        raise SystemExit('refusing to overwrite hand-edited chapters (Pass 1 amsthm conversions); TeX is source of truth')
    stale=[];skipped=[]
    for name,prefix in SOURCES:
        target=ROOT/'manuscript/unified_sections'/('return_'+prefix+'.tex')
        if prefix in HAND_EDITED_PREFIXES:
            if args.check:skipped.append(str(target.relative_to(ROOT)))
            continue
        content=render(name,prefix)
        if args.check:
            if not target.exists() or target.read_text()!=content:stale.append(str(target.relative_to(ROOT)))
        else:target.write_text(content)
    if stale:raise SystemExit('Stale generated chapters: '+', '.join(stale))
    if skipped:print('SKIP hand-edited chapters (TeX is source of truth): '+', '.join(skipped))
    elif args.check:print('PASS return-law source synchronization')
    else:print(f'Updated {len(SOURCES)} return-law chapters')


if __name__=='__main__':
    main()
