#!/usr/bin/env python3
"""Verify this import's bytes, recorded scope and scientific metadata.

This is an integrity and scope check, not a proof checker. The pinned remote
tree authenticates paths absent from the explicitly partial local overlay.
"""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import argparse
import ast
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[3]
RAW=Path('evidence/executions/20261019/chat-research')
INTEGRATION=Path('evidence/executions/20261019/repository-integration')


def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())


def reconstruct_tree(objects):
    root={}
    for path,mode,sha in objects:
        at=root;parts=path.split('/')
        for part in parts[:-1]:at=at.setdefault(part,{})
        at[parts[-1]]=(mode,sha)
    def recurse(node):
        entries=[]
        for name,value in node.items():
            is_tree=isinstance(value,dict)
            mode,sha=('40000',recurse(value)) if is_tree else value
            key=name.encode()+(b'/' if is_tree else b'')
            body=mode.encode()+b' '+name.encode()+b'\0'+bytes.fromhex(sha)
            entries.append((key,body))
        body=b''.join(value for key,value in sorted(entries))
        return hashlib.sha1(b'tree '+str(len(body)).encode()+b'\0'+body).hexdigest()
    return recurse(root)


def main(output):
    inventory=load(ROOT/'archive/record/chat_integration_20261019_inventory.json')
    assert inventory['file_count']==len(inventory['files'])
    syntax=0;json_files=0
    for entry in inventory['files']:
        p=ROOT/entry['repository_path']
        assert p.is_file() and digest(p)==entry['sha256'],p
        assert p.stat().st_size==entry['bytes'],p
        assert p.read_bytes()[:4]!=b'\x7fELF'
        if p.suffix=='.py':ast.parse(p.read_text(),filename=str(p));syntax+=1
        if p.suffix=='.json':load(p);json_files+=1
    audit=load(ROOT/RAW/'bgs_integration_20261019/all_packet_audit.json')
    valid=0;stale=[];statuses=Counter()
    for row in audit['runs']:
        root=ROOT/RAW/row['packet'];p=root/row['manifest'];obj=load(p)
        assert digest(p)==row['sha256'],p
        assert obj['schema_version']==2
        statuses[obj['run']['status']]+=1
        errors=[]
        for entry in obj.get('input_artifacts',[]):
            q=root/entry['path']
            if not q.is_file() or digest(q)!=entry['sha256']:
                errors.append('input changed since the run: '+entry['path'])
            assert entry['sha256']==entry.get('sha256_after',entry['sha256'])
        for entry in obj['outputs']:
            q=root/entry['path']
            assert q.is_file() and digest(q)==entry['sha256'],q
        if errors:
            assert row['packet']=='bgs_focus_20261017'
            assert row['manifest']=='transmission_run/manifest.json'
            assert errors==['input changed since the run: verify_transmission_bridge.py']
            assert obj['run']['status']=='failed' and not row['valid']
            stale.append(str(p.relative_to(ROOT)))
        else:
            assert row['valid'];valid+=1
    assert len(audit['runs'])==64 and valid==63 and len(stale)==1
    assert dict(statuses)=={'completed':58,'failed':5,'timeout':1}
    invalid=load(ROOT/RAW/'bgs_integration_20261019/source_three_v1_audit.json')
    assert 'invalid implementation' in invalid['mathematical_verdict']
    prefix=load(ROOT/RAW/'bgs_integration_20261019/source_three_v2_run/result.json')
    assert prefix['status']=='completed_exact_bounded_prefix'
    assert prefix['equal_across_three_tested_fields']
    assert all(x['prefix_central'] for x in prefix['summary'])
    assert max(x['q'] for x in prefix['rows'])==9
    base=load(ROOT/INTEGRATION/'base_objects.json')
    assert reconstruct_tree(base['objects'])==base['base_tree']
    remote={p:(mode,sha) for p,mode,sha in base['objects']}
    remote_dirs={str(Path(p).parent) for p in remote}
    def exists(rel):
        if (ROOT/rel).exists() or rel in remote:return True
        return any(p.startswith(rel.rstrip('/')+'/') for p in remote)
    registry=load(ROOT/'record/claims.json');rows=registry['claims']
    external=load(ROOT/'literature/external_dependencies.json')['dependencies']
    external_ids={row['id'] for row in external}
    assert len(external_ids)==len(external)
    by_id={r['id']:r for r in rows};assert len(by_id)==len(rows)==159
    assert by_id['BGS-BGS-001']['state']=='open' and by_id['BGS-TRACE-005']['state']=='open'
    for row in rows:
        assert exists(row['source']),row['source']
        assert row['id'] in (ROOT/row['source']).read_text(),row['id']
        for key in ('evidence','verifiers','formalization','manuscript','proof_dependencies'):
            assert all(exists(x) for x in row.get(key,[])),(row['id'],key)
        assert all(x in by_id for x in row['dependencies'])
        assert all(x in external_ids for x in row.get('external_dependencies',[]))
    graph=load(ROOT/'record/scientific_dependencies.json')
    assert set(graph['nodes'])==set(by_id)
    edges={(e['from'],e['to'],e['type']) for e in graph['edges']}
    expected={(dep,r['id'],'scientific-prerequisite') for r in rows for dep in r['dependencies']}
    assert edges==expected
    done=set();active=set()
    def visit(cid):
        assert cid not in active,'dependency cycle'
        if cid in done:return
        active.add(cid)
        for dep in by_id[cid]['dependencies']:visit(dep)
        active.remove(cid);done.add(cid)
    for cid in by_id:visit(cid)
    topics=load(ROOT/'record/mathematics_topics.json')['topics']
    registered={p for values in topics.values() for p in values}
    exempt={'README.md','results.md','results_20260907_addendum.md','open_questions.md'}
    current={str(p.relative_to(ROOT)) for p in (ROOT/'mathematics').glob('*.md') if p.name not in exempt}
    assert registered==current, (current-registered,registered-current)
    assert all(exists(p) for p in registered)
    newmath=[p for p in current if p.endswith('_20261019.md')]
    broken=[]
    for name in newmath+['README.md','README.ru.md','archive/record/chat_integration_20261019.md']:
        p=ROOT/name
        for target in re.findall(r'\[[^\]]*\]\(([^)\s]+)\)',p.read_text()):
            if '://' in target or target.startswith('#'):continue
            q=(p.parent/target.split('#',1)[0]).resolve()
            if not q.is_relative_to(ROOT.resolve()) or not exists(str(q.relative_to(ROOT.resolve()))):
                broken.append([name,target])
    assert not broken,broken
    registry_spec=importlib.util.spec_from_file_location('strict_registry',ROOT/'computations/verification/scientific_registry_audit.py')
    auditor=importlib.util.module_from_spec(registry_spec);registry_spec.loader.exec_module(auditor)
    def require_path(rel,*,allow_build=False):
        assert (allow_build and rel.startswith('build/')) or exists(rel),rel
    auditor.require_path=require_path
    strict_claims,strict_ids=auditor.audit_claims()
    auditor.audit_external(strict_claims)
    auditor.audit_graph(strict_claims)
    auditor.audit_errata()
    auditor.audit_topics()
    spec=importlib.util.spec_from_file_location('tex_audit',ROOT/'computations/maintenance/audit_manuscript_references.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    tex=module.audit(ROOT)
    assert not tex['errors'] and not tex['unresolved_labels'] and not tex['duplicate_labels'],tex
    build=load(ROOT/INTEGRATION/'manuscript_build_accepted.json')
    assert build['status']=='PASS' and build['sources_unchanged']
    assert not build['forbidden_warnings']
    for name,h in build['source_sha256'].items():assert digest(ROOT/name)==h,name
    # Only source syntax and provenance are checked for the preserved scripts.
    # The invalid prefix is deliberately not run and not counted as evidence.
    result={'status':'passed_scoped_integration_integrity_and_metadata_checks',
            'base_main':base['base_commit'],'authenticated_base_tree':base['base_tree'],
            'imported_files':len(inventory['files']),'python_sources_parsed':syntax,'json_files_parsed':json_files,
            'manifest_records':64,'valid_provenance_records':63,'stale_historical_failed_records':stale,
            'program_statuses':dict(statuses),'completed_but_invalid_mathematical_records':[
                str(RAW/'bgs_integration_20261019/source_three_run/manifest.json')],
            'registered_claims':len(rows),'new_claims':11,'new_canonical_math_sources':len(newmath),
            'existing_registry_functions_passed':['audit_claims','audit_external','audit_graph','audit_errata','audit_topics'],
            'manuscript_pages':build['page_count'],'manuscript_include_audit':tex,
            'full_goal_status':'OPEN',
            'scope':'Complete changed/imported bytes and registry/DAG with remote path existence authenticated by the pinned Git tree. This local overlay is not a full checkout; no full-workspace regression or mathematical theorem certification is claimed.'}
    p=Path(output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','imported_files','registered_claims','manifest_records','valid_provenance_records','manuscript_pages')}))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True)
    args=parser.parse_args();main(args.output)
