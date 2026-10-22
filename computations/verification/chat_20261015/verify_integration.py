#!/usr/bin/env python3
"""Check integration metadata and fresh receipt pins, never theorem truth.

The optional baseline tree supports a disclosed partial source snapshot.
It substitutes only path existence in the maintained registry auditor;
every mathematical source is still read from actual local bytes.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]

def need(ok, message):
    if not ok:
        raise RuntimeError(message)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline-tree',type=Path)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    tree=json.loads(args.baseline_tree.read_text()) if args.baseline_tree else None
    remote={x['path'] for x in tree['tree']} if tree else set()
    remote_only=set()
    def exists(rel):
        p=ROOT/rel
        if p.exists():return True
        if rel.rstrip('/') in remote:
            remote_only.add(rel);return True
        return False
    path=ROOT/'computations/verification/scientific_registry_audit.py'
    spec=importlib.util.spec_from_file_location('bgs_registry',path)
    auditor=importlib.util.module_from_spec(spec);spec.loader.exec_module(auditor)
    def require_path(rel,*,allow_build=False):
        if allow_build and rel.startswith('build/'):return
        need(exists(rel),'Missing registered path: '+rel)
    auditor.require_path=require_path
    claims,ids=auditor.audit_claims()
    external=auditor.audit_external(claims)
    auditor.audit_graph(claims)
    auditor.audit_errata()
    auditor.audit_topics()
    manifest=json.loads((ROOT/'record/chat_integration_20261016.json').read_text())
    inv=json.loads((ROOT/manifest['historical_inventory']).read_text())
    need(len(inv)==90 and len({r['id'] for r in inv})==90,'Incomplete source inventory')
    receipt=json.loads((ROOT/'evidence/executions/20261016/chat-integration/receipt.json').read_text())
    tasks=json.loads((Path(__file__).parent/'tasks.json').read_text())
    taskmap={t['name']:t for t in tasks}
    need(set(taskmap)=={t['name'] for t in receipt['tasks']},'Replay task coverage differs')
    for task in receipt['tasks']:
        src=Path(__file__).parent/task['source']
        need(src.is_file(),'Replay source missing: '+str(src))
        need(hashlib.sha256(src.read_bytes()).hexdigest()==task['source_sha256'],
             'Stale replay source: '+task['name'])
        need(task['status']=='PASS' and task['returncode']==0,'Incomplete replay: '+task['name'])
        for name,digest in task['outputs_sha256'].items():
            out=ROOT/'evidence/executions/20261016/chat-integration'/task['name']/name
            need(hashlib.sha256(out.read_bytes()).hexdigest()==digest,'Changed replay output: '+name)
    need(claims['BGS-BGS-001']['state']=='open' and claims['BGS-TRACE-005']['state']=='open',
         'Physical BGS target changed unexpectedly')
    added=[r['canonical_path'] for r in manifest['imported_sources']]
    added+=['mathematics/deleted_clock_hardy_boundary_20261015.md',
            'record/chat_integration_20261016.md','literature/chat_integration_sources_20261016.md']
    badlinks=[]
    for rel in added:
        src=ROOT/rel
        for target in re.findall(r'\]\(([^)\s]+)(?:\s+[^)]*)?\)',src.read_text()):
            if target.startswith(('https:','http:','mailto:','#')):continue
            dest=(src.parent/target.split('#')[0]).resolve()
            try:destrel=dest.relative_to(ROOT.resolve()).as_posix()
            except ValueError:
                badlinks.append((rel,target));continue
            if not exists(destrel):badlinks.append((rel,target))
    need(not badlinks,'Broken new-source links: '+str(badlinks))
    archive=ROOT/'archive/history/2026/chat_20261015'
    provenance=json.loads((archive/'provenance.json').read_text())
    need(hashlib.sha256((archive/'BGS_complete_research_2026-10-15.md').read_bytes()).hexdigest()
         ==provenance['source_document_sha256'],'Historical source bytes changed')
    pins={rel:hashlib.sha256((ROOT/rel).read_bytes()).hexdigest() for rel in added}
    report={'schema':'bgs-chat-integration-check-v1','status':'PASS',
            'scope':'Registry claims/external mappings/DAG/errata/topics; all 15 finite replay pins; new-source links; historical-source hash. Not a full workspace pytest, PDF build or Lean build.',
            'mode':'partial pinned snapshot with remote path-existence inventory' if tree else 'local checkout',
            'baseline_commit':manifest['base_commit'],
            'remote_inventory_entries':len(tree['tree']) if tree else 0,
            'remote_only_path_checks':len(remote_only),
            'claims':len(ids),'external_dependencies':len(external),
            'source_inventory_entries':len(inv),'replay_tasks':len(tasks),
            'physical_targets_open':True,'source_sha256':pins}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='source_sha256'},indent=2))

if __name__=='__main__':main()
