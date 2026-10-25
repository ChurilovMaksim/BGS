#!/usr/bin/env python3
"""Check new edition integrity, code/JSON syntax and local Markdown targets.

In a complete checkout no options are needed. --known-tree may supply an
authenticated Git tree (list of path/type/sha records) for a partial overlay;
this checks target existence against that tree, not unavailable file contents.
Math semantics, external URLs and arbitrary historical heading anchors are
outside this check. Source/math/build review coverage is recorded separately.
Registered succession: a markdown link whose target no longer exists still
passes iff archive/MANIFEST-P2SPECTRAL.md records it as succeeded by an
existing path; anything else fails exactly as before.
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


def load_succession(path):
    """Read the succession table from a package manifest.

    Only the section headed '## Succession table' is read, and only its
    table rows. Returns (mapping, errors); any malformed row voids the
    whole mapping (fail-closed) and is reported as an error. A missing
    manifest yields an empty mapping with no error, so trees predating
    the manifest behave exactly as before.
    """
    if not path.exists():
        return {}, []
    lines = path.read_text().splitlines()
    in_section = False
    table = {}
    errors = []
    for line in lines:
        if line.startswith('#'):
            if in_section:
                break
            if line.startswith('## ') and 'Succession table' in line:
                in_section = True
            continue
        if not in_section:
            continue
        s = line.strip()
        if not s:
            continue
        if not s.startswith('|'):
            errors.append('non-table line in succession section: ' + s[:80])
            continue
        cells = [c.strip() for c in s.strip('|').split('|')]
        if cells and cells[0] == 'Old path':
            continue
        if cells and all(set(c) <= set('-: ') for c in cells):
            continue
        if len(cells) != 2 or not cells[0] or not cells[1]:
            errors.append('malformed succession row: ' + s[:80])
            continue
        old, new = cells
        bad = (old == new or old.startswith('/') or new.startswith('/')
               or '..' in old.split('/') or '..' in new.split('/')
               or ' ' in old or ' ' in new
               or re.match(r'^[A-Za-z]+:', old) or re.match(r'^[A-Za-z]+:', new))
        if bad:
            errors.append('invalid succession row: ' + s[:80])
            continue
        if old in table and table[old] != new:
            errors.append('conflicting succession rows for: ' + old)
            continue
        table[old] = new
    if errors:
        return {}, errors
    return table, []

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--known-tree',type=Path)
    args=ap.parse_args();known=set()
    if args.known_tree:
        t=json.loads(args.known_tree.read_text());t=t.get('tree',[]) if isinstance(t,dict) else t
        known={x['path'] for x in t if x['type']=='blob'}
    known|={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()}
    c=json.loads((ROOT/'record/spectral_research/catalog.json').read_text());raw=reconstruct(c)
    failures=[];files=[];py=0;js=0;links=0
    succession, succession_errors = load_succession(ROOT/'archive/MANIFEST-P2SPECTRAL.md')
    failures += [['succession manifest malformed', e] for e in succession_errors]
    for e in c['entries']:
        p=ROOT/e['target'];expected=projection(e,raw,c['entries'])
        if not p.exists() or p.read_bytes()!=expected:failures.append(['source projection',e['target']])
        files.append(p)
    # Redfix 2026-10-25 (Wave-6-style path refresh): the seven maintained
    # notes were relocated in phase 2 to mathematics/fixed-map/ with the
    # dated suffix dropped; the checker hardcodes the pre-move paths.
    maintained=['fixed-map/coordinate_return_quartic.md','fixed-map/inserted_trace_coboundary.md',
                'fixed-map/spectral_orbit_distance.md','fixed-map/pell_weighted_curvature.md',
                'fixed-map/finite_grid_one_step_trace.md','fixed-map/displacement_density_trace_bound.md',
                'fixed-map/fixed_kick_uniform_trace_bound.md']
    markdown=[p for p in files if p.suffix=='.md']
    markdown+=list((ROOT/'mathematics/spectral_research/topics').glob('*.md'))
    markdown+=[ROOT/'mathematics/spectral_research/README.md',ROOT/'record/spectral_research/review_matrix.md']
    markdown += [ROOT/'mathematics'/s for s in maintained]
    markdown += [ROOT/'record/spectral_research/spectral_final_integration.md', ROOT/'record/remaining_breakthrough_task_20261021.md', ROOT/'record/spectral_research/trace_closure.md']
    markdown += [ROOT/'evidence/executions/20261021/spectral-final/README.md',
                 ROOT/'computations/reference/spectral_research/README.md']
    markdown += [ROOT/'literature/bowen_ruelle_trace_closure_20261021.md',
                 ROOT/'evidence/executions/20261022/trace-closure/README.md']
    for p in markdown:
        rel=p.relative_to(ROOT).as_posix();s=plain_markdown(p.read_text())
        for m in re.finditer(r'\[[^\]\n]+\]\(([^\s)]+)\)',s):
            t=m[1]
            if re.match(r'^[A-Za-z]+:',t) or t.startswith('#'):continue
            target=posixpath.normpath(posixpath.join(posixpath.dirname(rel),t.split('#')[0]));links+=1
            successor = succession.get(target)
            link_ok = (target in known or any(x.startswith(target.rstrip('/')+'/') for x in known)
                       or (successor is not None and (successor in known or any(x.startswith(successor.rstrip('/')+'/') for x in known))))
            if not link_ok:
                failures.append(['link target',rel,t])
    for p in list((ROOT/'computations/reference/spectral_research').rglob('*.py'))+[
        ROOT/'computations/maintenance'/s for s in ['rebuild_spectral_corpus.py','render_spectral_research.py']]+[
        ROOT/'computations/verification'/s for s in ['replay_spectral_corpus.py','weighted_trace_hessian_checks.py','check_spectral_edition.py','trace_closure_checks.py']]:
        try:ast.parse(p.read_text(),filename=str(p));py+=1
        except SyntaxError as exc:failures.append(['Python syntax',str(p),str(exc)])
    for evidence_root in ['evidence/executions/20261021/spectral-final',
                          'evidence/executions/20261022/trace-closure']:
      for p in (ROOT/evidence_root).rglob('*'):
        if not p.is_file() or not (p.suffix=='.json' or p.name.endswith('.json.gz')):continue
        try:json.loads(gzip.decompress(p.read_bytes()) if p.name.endswith('.gz') else p.read_bytes());js+=1
        except (ValueError,OSError) as exc:failures.append(['JSON syntax',str(p),str(exc)])
    rows=json.loads((ROOT/'record/claims.json').read_text())['claims'];by={r['id']:r for r in rows}
    expected_states={'108':'proved','109':'proved','110':'proved','111':'proved','112':'proved','113':'proved'}
    for n,state in expected_states.items():
        r=by['BGS-TRACE-'+n]
        if r['state']!=state or not (ROOT/r['source']).exists():failures.append(['core claim',n])
    for cid in ['BGS-BGS-001','BGS-TRACE-005']:
        if by[cid]['state']!='open':failures.append(['open frontier changed',cid])
    # Check registered graph/path closure against actual files or the explicit
    # authenticated inventory. This does not read unavailable baseline proofs.
    if len(by)!=len(rows):failures.append(['duplicate claim ID'])
    ext=json.loads((ROOT/'literature/external_dependencies.json').read_text())['dependencies']
    extids={e['id'] for e in ext}
    def available(path):
        return path in known or any(x.startswith(path.rstrip('/')+'/') for x in known)
    for row in rows:
        for dep in row.get('dependencies',[]):
            if dep not in by:failures.append(['missing claim dependency',row['id'],dep])
        for dep in row.get('external_dependencies',[]):
            if dep not in extids:failures.append(['missing external dependency',row['id'],dep])
        for field in ['source','evidence','verifiers','formalization','manuscript','proof_dependencies']:
            vals=row.get(field,[]);vals=[vals] if isinstance(vals,str) else vals
            for path in vals:
                if not available(path):failures.append(['registered path',row['id'],path])
    visiting=set();done=set()
    def visit(cid):
        if cid in visiting:
            failures.append(['dependency cycle',cid]);return
        if cid in done:return
        visiting.add(cid)
        for dep in by[cid].get('dependencies',[]):
            if dep in by:visit(dep)
        visiting.remove(cid);done.add(cid)
    for cid in by:visit(cid)
    result={'result':'PASS' if not failures else 'FAIL','source_units':len(c['entries']),
            'markdown_files_checked':len(markdown),'local_link_targets_checked':links,
            'reference_and_new_python_syntax_files':py,'evidence_json_files':js,
            'known_tree_used':bool(args.known_tree),'registered_claims':len(rows),
            'registry_graph_and_path_inventory_checked':True,'unavailable_baseline_proofs_read':False,
            'failures':failures}
    print(json.dumps(result,indent=2))
    if failures:raise SystemExit(1)

if __name__=='__main__':main()
