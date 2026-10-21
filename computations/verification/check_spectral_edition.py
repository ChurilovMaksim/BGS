#!/usr/bin/env python3
"""Check new edition integrity, code/JSON syntax and local Markdown targets.

In a complete checkout no options are needed. --known-tree may supply an
authenticated Git tree (list of path/type/sha records) for a partial overlay;
this checks target existence against that tree, not unavailable file contents.
Math semantics, external URLs and arbitrary historical heading anchors are
outside this check. Source/math/build review coverage is recorded separately.
"""
import argparse
import ast
import gzip
import json
import posixpath
import re
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'computations/maintenance'))
from rebuild_spectral_corpus import reconstruct, projection

def plain_markdown(s):
    out=[];fence=None
    for line in s.splitlines(keepends=True):
        m=re.match(r'^\s*(`{3,}|~{3,})',line)
        if fence:
            out.append('\n')
            if m and m[1][0]==fence[0] and len(m[1])>=len(fence):fence=None
        elif m:fence=m[1];out.append('\n')
        elif line.startswith('    ') or line.startswith('\t'):out.append('\n')
        else:out.append(line)
    s=''.join(out)
    return re.sub(r'`+[^`\n]*`+|\$\$[\s\S]*?\$\$|(?<!\\)\$(?!\$)[\s\S]*?(?<!\\)\$',
                  lambda m:'\n'*m[0].count('\n'),s)

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--known-tree',type=Path)
    args=ap.parse_args();known=set()
    if args.known_tree:
        t=json.loads(args.known_tree.read_text());t=t.get('tree',[]) if isinstance(t,dict) else t
        known={x['path'] for x in t if x['type']=='blob'}
    known|={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()}
    c=json.loads((ROOT/'record/spectral_research/catalog.json').read_text());raw=reconstruct(c)
    failures=[];files=[];py=0;js=0;links=0
    for e in c['entries']:
        p=ROOT/e['target'];expected=projection(e,raw,c['entries'])
        if not p.exists() or p.read_bytes()!=expected:failures.append(['source projection',e['target']])
        files.append(p)
    maintained=['coordinate_return_quartic_20261021.md','inserted_trace_coboundary_20261021.md',
                'spectral_orbit_distance_20261021.md','pell_weighted_curvature_20261021.md']
    markdown=[p for p in files if p.suffix=='.md']
    markdown+=list((ROOT/'mathematics/spectral_research/topics').glob('*.md'))
    markdown+=[ROOT/'mathematics/spectral_research/README.md',ROOT/'record/spectral_research/review_matrix.md']
    markdown += [ROOT/'mathematics'/s for s in maintained]
    markdown += [ROOT/'record'/s for s in ['spectral_final_integration_20261021.md','remaining_breakthrough_task_20261021.md']]
    markdown += [ROOT/'evidence/executions/20261021/spectral-final/README.md',
                 ROOT/'computations/reference/spectral_research/README.md']
    for p in markdown:
        rel=p.relative_to(ROOT).as_posix();s=plain_markdown(p.read_text())
        for m in re.finditer(r'\[[^\]\n]+\]\(([^\s)]+)\)',s):
            t=m[1]
            if re.match(r'^[A-Za-z]+:',t) or t.startswith('#'):continue
            target=posixpath.normpath(posixpath.join(posixpath.dirname(rel),t.split('#')[0]));links+=1
            if target not in known and not any(x.startswith(target.rstrip('/')+'/') for x in known):
                failures.append(['link target',rel,t])
    for p in list((ROOT/'computations/reference/spectral_research').rglob('*.py'))+[
        ROOT/'computations/maintenance'/s for s in ['rebuild_spectral_corpus.py','render_spectral_research.py']]+[
        ROOT/'computations/verification'/s for s in ['replay_spectral_corpus.py','weighted_trace_hessian_checks.py','check_spectral_edition.py']]:
        try:ast.parse(p.read_text(),filename=str(p));py+=1
        except SyntaxError as exc:failures.append(['Python syntax',str(p),str(exc)])
    for p in (ROOT/'evidence/executions/20261021/spectral-final').rglob('*'):
        if not p.is_file() or not (p.suffix=='.json' or p.name.endswith('.json.gz')):continue
        try:json.loads(gzip.decompress(p.read_bytes()) if p.name.endswith('.gz') else p.read_bytes());js+=1
        except (ValueError,OSError) as exc:failures.append(['JSON syntax',str(p),str(exc)])
    rows=json.loads((ROOT/'record/claims.json').read_text())['claims'];by={r['id']:r for r in rows}
    expected_states={'108':'proved','109':'conditional','110':'conditional','111':'proved'}
    for n,state in expected_states.items():
        r=by['BGS-TRACE-'+n]
        if r['state']!=state or not (ROOT/r['source']).exists():failures.append(['core claim',n])
    for cid in ['BGS-BGS-001','BGS-TRACE-005']:
        if by[cid]['state']!='open':failures.append(['open frontier changed',cid])
    result={'result':'PASS' if not failures else 'FAIL','source_units':len(c['entries']),
            'markdown_files_checked':len(markdown),'local_link_targets_checked':links,
            'reference_and_new_python_syntax_files':py,'evidence_json_files':js,
            'known_tree_used':bool(args.known_tree),'failures':failures}
    print(json.dumps(result,indent=2))
    if failures:raise SystemExit(1)

if __name__=='__main__':main()
