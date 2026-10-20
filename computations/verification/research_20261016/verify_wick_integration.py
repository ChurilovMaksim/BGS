#!/usr/bin/env python3
"""Current TRACE-094 pins/registry/link checks; no theorem truth or full build."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re

from verify_integration import prose

ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'evidence/executions/20261016/wick-poisson'
BASE='f78ec82ffe8c6535c961abc969a719704bf3e942'


def need(ok,message):
    if not ok:
        raise RuntimeError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    value=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline-tree',type=Path)
    parser.add_argument('--output',required=True,type=Path)
    args=parser.parse_args()
    tree=json.loads(args.baseline_tree.read_text()) if args.baseline_tree else {
        'commit':BASE,'sha':None,'tree':[]}
    need(tree['commit']==BASE,'Unexpected pinned base inventory')
    remote={row['path'] for row in tree['tree']}
    remote_only=set()
    def exists(path):
        if (ROOT/path).exists():return True
        if path.rstrip('/') in remote:
            remote_only.add(path)
            return True
        return False
    audit=module('bgs_registry',ROOT/'computations/verification/scientific_registry_audit.py')
    def require_path(path,*,allow_build=False):
        if allow_build and path.startswith('build/'):return
        need(exists(path),'Missing registered path: '+path)
    audit.require_path=require_path
    claims,ids=audit.audit_claims()
    external=audit.audit_external(claims)
    audit.audit_graph(claims)
    audit.audit_errata()
    audit.audit_topics()
    for cid in ('BGS-TRACE-005','BGS-BGS-001'):
        need(claims[cid]['state']=='open','Physical target was promoted: '+cid)
    need(claims['BGS-TRACE-094']['state']=='proved','Missing scoped new disposition')
    renderer=module('bgs_renderer',ROOT/'computations/maintenance/render_claim_registry.py')
    need(renderer.render()==(ROOT/'record/claim_registry.md').read_text(), 'Stale generated registry')

    pins=json.loads((PACKET/'source_manifest.json').read_text())
    need(pins['base_commit']==BASE,'Unexpected source-pin base')
    for rel,digest in pins['sha256'].items():
        need((ROOT/rel).is_file(),'Pinned source must be actual local bytes: '+rel)
        need(sha(ROOT/rel)==digest,'Source changed after pinning: '+rel)

    execution=json.loads((PACKET/'exact/manifest.json').read_text())
    need(execution['schema_version']==2,'Wrong execution manifest version')
    need(execution['run']['status']=='completed' and execution['run']['exit_status']==0,
         'Exact finite run did not complete successfully')
    for item in execution['input_artifacts']:
        need(sha(ROOT/item['path'])==item['sha256_after']==item['sha256'],
             'Executed source changed: '+item['path'])
    for item in execution['outputs']:
        need(sha(ROOT/item['path'])==item['sha256'],'Executed result changed: '+item['path'])
    result=json.loads((PACKET/'exact/result.json').read_text())
    need(result['status']=='PASS','Finite program did not report PASS')

    broken=[]
    for rel in pins['changed_markdown']:
        src=ROOT/rel
        for target in re.findall(r'\]\(([^)\s]+)(?:\s+[^)]*)?\)',prose(src.read_text())):
            if target.startswith(('http:','https:','mailto:','#')):continue
            dest=(src.parent/target.split('#')[0]).resolve()
            try:destrel=dest.relative_to(ROOT.resolve()).as_posix()
            except ValueError:
                broken.append((rel,target));continue
            if not exists(destrel):broken.append((rel,target))
    need(not broken,'Broken current source links: '+str(broken))

    manuscript=module('bgs_tex_audit',ROOT/'computations/maintenance/audit_manuscript_references.py')
    tex=manuscript.audit(ROOT)
    need(not(tex['errors'] or tex['unresolved_labels'] or tex['duplicate_labels']),
         'Active TeX source/reference check failed')
    (PACKET/'manuscript_checks.json').write_text(json.dumps(tex,indent=2)+'\n')
    archive=ROOT/'record/history/2026/chat_20261015'
    provenance=json.loads((archive/'provenance.json').read_text())
    need(sha(archive/'BGS_complete_research_2026-10-15.md')==provenance['source_document_sha256'],
         'Imported historical source bytes changed')
    report={'schema':'bgs-wick-poisson-integration-v1','status':'PASS',
      'base_commit':BASE,'tree_sha':tree['sha'],
      'mode':'Partial pinned source snapshot; remote inventory supplies path existence only'
             if args.baseline_tree else 'Local source bytes; no inventory fallback',
      'claims':len(ids),'external_dependencies':len(external),'source_pins':len(pins['sha256']),
      'changed_markdown_checked':len(pins['changed_markdown']),
      'remote_inventory_entries':len(remote),'remote_only_path_checks':len(remote_only),
      'physical_targets_open':True,'historical_source_bytes_preserved':True,
      'scope':'Registry/DAG/topics/errata, generated registry, current source pins, one actual exact execution packet, changed Markdown paths and active TeX references. No full workspace, PDF, Lean or physical asymptotic certification.'}
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
