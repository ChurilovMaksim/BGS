#!/usr/bin/env python3
"""Durable Wave3 bounded replay. Provenance is never scientific equality.

Reuses the authenticated explicit-assertion bootstrap and strict typed comparison
protocol of Wave2, without changing its pinned adapter or historical receipts.
"""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
from wave2_checked_replay import (require, digest, strict_json, safe_path,
    compare, BOOTSTRAP, child_limits, output_directory)

ROOT=Path(__file__).resolve().parents[2]
BINDINGS='record/wave3_replay_source_bindings.json'
CONTRACT='record/wave3_replay_contract.json'

def source_bytes(root=ROOT):
    data=strict_json(safe_path(root,BINDINGS).read_bytes())
    require(data['schema']=='bgs-wave3-replay-source-bindings-v1','unknown Wave3 bindings')
    cached={}
    for rel,expected in data['files'].items():
        value=safe_path(root,rel).read_bytes();require(digest(value)==expected,'changed Wave3 input: '+rel);cached[rel]=value
    return cached

def run(root=ROOT,output=None):
    output=output_directory(root,output)
    receipt={'schema':'bgs-wave3-durable-replay-v1','status':'running','tasks':[],'artifacts':[],
             'python':sys.version,'optimization':sys.flags.optimize,'whole_suite_run':False,
             'manuscript_build_run':False,'formal_compile_run':False,
             'unavailable_author_222_suite_replayed':False,
             'scope':'Four fresh bounded controls in three domains; exact controls and disclosed floating diagnostics remain separate from analytic proof.'}
    def publish():
        if output is not None:(output/'replay_manifest.json').write_text(json.dumps(receipt,indent=2)+'\n')
    def retain(name,data):
        if output is not None:
            (output/name).write_bytes(data);receipt['artifacts'].append({'path':name,'bytes':len(data),'sha256':digest(data)})
    publish()
    try:
        cached=source_bytes(root);contract=strict_json(cached[CONTRACT]);require(contract['schema']=='bgs-wave3-replay-contract-v1','unknown Wave3 contract')
        require(len(contract['tasks'])==4,'Wave3 replay task closure differs')
        receipt['source_hashes']={p:digest(v) for p,v in cached.items()};receipt['adapter_bootstrap_sha256']=digest(BOOTSTRAP.encode())
        retain('source_bindings.original.json',safe_path(root,BINDINGS).read_bytes());retain('replay_contract.original.json',cached[CONTRACT])
        env=dict(os.environ);env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',NUMEXPR_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1',PYTHONOPTIMIZE='0')
        mode=['-'+'O'*sys.flags.optimize] if sys.flags.optimize else []
        for task in contract['tasks']:
            name=task['name'];row={'name':name,'domain':task['domain'],'status':'running'};receipt['tasks'].append(row);publish();expected=cached[task['expected']];retain(name+'.expected.raw',expected)
            with tempfile.TemporaryDirectory(prefix='bgs-wave3-'+name+'-') as tmp:
                work=Path(tmp);source=work/Path(task['source']).name;source.write_bytes(cached[task['source']])
                config={'source':str(source),'snapshot_root':str(work),'snapshot_adapter':False,'historical_manifest_digest':'','scoped_manifest_digest':'','shared_modules':[],'adapter_receipt':str(work/'adapter_receipt.json')}
                command=[sys.executable,*mode,'-c',BOOTSTRAP,json.dumps(config)];row['command']=[sys.executable,*mode,'-c','authenticated explicit-assertion bootstrap',json.dumps(config)];start=time.monotonic()
                try:
                    result=subprocess.run(command,cwd=work,env=env,capture_output=True,timeout=task['timeout_seconds'],preexec_fn=child_limits);row.update(exit_status=result.returncode,seconds=time.monotonic()-start)
                    for stream in ['stdout','stderr']:retain(name+'.'+stream,getattr(result,stream))
                except subprocess.TimeoutExpired as error:
                    row.update(exit_status=None,seconds=time.monotonic()-start)
                    for stream in ['stdout','stderr']:retain(name+'.'+stream,getattr(error,stream) or b'')
                    raise
                ar=work/'adapter_receipt.json'
                if ar.is_file():retain(name+'.adapter.json',ar.read_bytes())
                generated=task.get('optimized_generated_result',task['generated_result']) if mode else task['generated_result'];out=work/generated
                raw=out.read_bytes() if out.is_file() and not out.is_symlink() else None
                if raw is not None:retain(name+'.actual.raw',raw)
                require(result.returncode==0,name+' failed: '+result.stderr.decode(errors='replace')[-1500:]);require(raw is not None and len(raw)<2**20,'missing/oversized fresh result')
                require(source.is_file() and not source.is_symlink() and source.read_bytes()==cached[task['source']],'copied checker changed')
                require(ar.is_file(),'missing adapter receipt');adapter=strict_json(ar.read_bytes());require(adapter['python_optimization']==sys.flags.optimize,'child optimization differs');require(all(x['snapshot_redirects']==x['manifest_redirects']==0 for x in adapter['records']),'unexpected provenance remap')
                context={'optimization':sys.flags.optimize,'source_digest':digest(cached[task['source']]),'extra_digests':set(),'historical_manifest_digest':'','scoped_manifest_digest':'','snapshot_pins':{}}
                details=compare(strict_json(expected),strict_json(raw),task,context);row.update(status='passed',source_sha256=context['source_digest'],expected_raw_sha256=digest(expected),actual_raw_sha256=digest(raw),**details)
                observed=strict_json(raw);field=task['count_field'];require(observed[field]==task['declared_check_count'],'bounded coverage differs');row.update(check_count=observed[field],arithmetic_scope=task['arithmetic_scope']);publish()
        require(source_bytes(root)==cached,'original Wave3 inputs changed during execution')
        receipt.update(status='passed',original_sources_unchanged=True,copied_checkers_authenticated=True,expected_bytes_cached_before_execution=True,scientific_equality=True,scientific_comparison_mode='strict_typed_exact_with_contract_declared_numeric_diagnostics',provenance_excluded_from_scientific_comparison=True);publish();return receipt
    except Exception as error:
        if receipt['tasks'] and receipt['tasks'][-1]['status']=='running':receipt['tasks'][-1].update(status='failed',failure=str(error))
        receipt.update(status='failed',failure=str(error));publish();raise

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check-sources',action='store_true');parser.add_argument('--output-dir',type=Path);args=parser.parse_args()
    if args.check_sources:source_bytes();print('Wave3 source closure: OK')
    else:result=run(output=args.output_dir);print('Wave3 replay: '+result['status']+' (4 tasks, three bounded domains)')

if __name__=='__main__':main()
