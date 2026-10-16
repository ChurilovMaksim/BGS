#!/usr/bin/env python3
"""Read-only metadata, source-pin and execution-scope audit, not theorem truth."""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
EVIDENCE=ROOT/'evidence/executions/20261016/abel-gaussian'


def need(ok,message):
    if not ok:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prose(text):
    """Ignore literal/code and math, where [N](x) is not a file link."""
    text=re.sub(r'```[\s\S]*?```|~~~[\s\S]*?~~~','',text)
    text='\n'.join(line for line in text.splitlines()
                   if not line.startswith(('    ','\t')))
    text=re.sub(r'`[^`\n]+`','',text)
    text=re.sub(r'\\\[[\s\S]*?\\\]|\$\$[\s\S]*?\$\$','',text)
    return re.sub(r'\$[^$\n]+\$','',text)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--baseline-tree',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    tree=json.loads(args.baseline_tree.read_text())
    need(tree['commit']=='b425a36141cd81c7ef4e832984e7f7ff5074ddc7',
         'Unexpected pinned inventory commit')
    remote={r['path'] for r in tree['tree']}
    remote_only=set()
    def exists(rel):
        if (ROOT/rel).exists():return True
        if rel.rstrip('/') in remote:
            remote_only.add(rel)
            return True
        return False
    spec=importlib.util.spec_from_file_location('registry',ROOT/'computations/verification/scientific_registry_audit.py')
    auditor=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(auditor)
    def require_path(rel,*,allow_build=False):
        if allow_build and rel.startswith('build/'):return
        need(exists(rel),'Missing registered path: '+rel)
    auditor.require_path=require_path
    claims,ids=auditor.audit_claims()
    external=auditor.audit_external(claims)
    auditor.audit_graph(claims)
    auditor.audit_errata()
    auditor.audit_topics()
    for cid in ('BGS-BGS-001','BGS-TRACE-005'):
        need(claims[cid]['state']=='open','Physical target promoted: '+cid)
    for cid in ('BGS-TRACE-092','BGS-TRACE-093'):
        need(claims[cid]['state']=='proved','New disposition missing: '+cid)

    manifest=json.loads((EVIDENCE/'source_manifest.json').read_text())
    for rel,sha in manifest['sha256'].items():
        need((ROOT/rel).is_file(),'Pinned source is not actual local bytes: '+rel)
        need(digest(ROOT/rel)==sha,'Changed pinned source: '+rel)
    receipt=json.loads((EVIDENCE/'receipt.json').read_text())
    expected={'abel','rigidity','factorial','hessian','generic_tensors','symbolic_mean'}
    need({t['name'] for t in receipt['tasks']}==expected,'Incomplete finite coverage')
    for t in receipt['tasks']:
        need(t['status']=='PASS' and t['returncode']==0,'Finite task did not pass: '+t['name'])
        need(digest(HERE/t['source'])==t['source_sha256'],'Stale executed source')
        for rel,sha in t.get('dependencies_sha256',{}).items():
            need(digest(HERE/rel)==sha,'Stale executed dependency: '+rel)
        need(digest(EVIDENCE/t['name']/'result.json')==t['result_sha256'],
             'Changed finite result: '+t['name'])
        need(digest(EVIDENCE/t['name']/'stderr.log')==t['stderr_sha256'],
             'Changed finite stderr: '+t['name'])
    cpp=json.loads((EVIDENCE/'cpp_metadata.json').read_text())
    need(cpp['status']=='PASS','C++ replay failed')
    need(digest(HERE/'sample_conditioned_ewens.cpp')==cpp['source_sha256'],
         'Stale C++ source')
    need(digest(EVIDENCE/'cpp_replay.json')==cpp['result_sha256'],'Changed C++ output')
    # Validate links for the changed Markdown surfaces; remote inventory provides
    # existence only, never source content or theorem verification.
    broken=[]
    for rel in manifest['changed_markdown']:
        src=ROOT/rel
        for target in re.findall(r'\]\(([^)\s]+)(?:\s+[^)]*)?\)',prose(src.read_text())):
            if target.startswith(('http:','https:','mailto:','#')):continue
            dest=(src.parent/target.split('#')[0]).resolve()
            try:destrel=dest.relative_to(ROOT.resolve()).as_posix()
            except ValueError:
                broken.append((rel,target));continue
            if not exists(destrel):broken.append((rel,target))
    need(not broken,'Broken changed-source links: '+str(broken))
    archive=ROOT/'record/history/2026/chat_20261015'
    provenance=json.loads((archive/'provenance.json').read_text())
    need(digest(archive/'BGS_complete_research_2026-10-15.md')==provenance['source_document_sha256'],
         'Historical recovered source bytes changed')
    report=dict(schema='bgs-abel-gaussian-integration-v1',status='PASS',
                base_commit=tree['commit'],tree_sha=tree['sha'],
                mode='Partial pinned source snapshot with remote path-existence inventory',
                claims=len(ids),external_dependencies=len(external),
                executed_finite_tasks=len(receipt['tasks']),source_pins=len(manifest['sha256']),
                changed_markdown_checked=len(manifest['changed_markdown']),
                remote_inventory_entries=len(remote),remote_only_path_checks=len(remote_only),
                physical_targets_open=True,historical_source_bytes_preserved=True,
                scope='Registry/DAG/errata/topics, local source hashes, six finite receipts, C++ replay, Markdown links and preserved historical source. No full pytest, PDF/Lean build or physical asymptotic theorem.')
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
