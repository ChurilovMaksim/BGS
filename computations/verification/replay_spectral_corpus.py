#!/usr/bin/env python3
"""Replay the 56 bounded author checks in a disposable historical workspace.

Requires numpy and mpmath for the few original scripts importing them. Document
builders and Wolfram programs are not run. All original Python asserts are
enabled even if this launcher is invoked with -O. Logs remain in --output-dir.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import subprocess
import sys
import tempfile
import time

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'computations/maintenance'))
from rebuild_spectral_corpus import reconstruct
PACKET=ROOT/'evidence/executions/20261021/spectral-final'

def limits():
    resource.setrlimit(resource.RLIMIT_CPU,(35,35))
    resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
    resource.setrlimit(resource.RLIMIT_FSIZE,(20*1024**2,20*1024**2))

def sha(b):return hashlib.sha256(b).hexdigest()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output-dir',required=True,type=Path)
    args=ap.parse_args(); out=args.output_dir.resolve();out.mkdir(parents=True,exist_ok=True)
    c=json.loads((ROOT/'record/spectral_research/catalog.json').read_text()); raw=reconstruct(c)
    inventory=json.loads((PACKET/'fresh/script_inventory.json').read_text())
    scripts=[r['path'] for r in inventory if r['run']]
    scripts.append('research_round7_2026_10_21/root_unipotent_exact_checks.py')
    frozen=json.loads((PACKET/'fresh/frozen_recovery.json').read_text())
    runs=[]
    with tempfile.TemporaryDirectory(prefix='bgs-spectral-replay-') as tmp:
        work=Path(tmp)
        for e in c['entries']:
            rel=Path(e['original_path'])
            if rel.is_absolute() or '..' in rel.parts:raise ValueError('Unsafe original path')
            b=raw[e['raw_offset']:e['raw_offset']+e['raw_bytes']]
            if sha(b)!=e['sha256']:raise ValueError('Source identity')
            p=work/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
        snapshots={}
        for f in frozen:
            n=f['before_round']
            begin=re.search(rb'^<!-- BEGIN COMPLETE PRECEDING MASTER ROUND'+str(n).encode()+rb' -->\r?\n',raw,re.M)
            end=re.search(rb'^<!-- END COMPLETE PRECEDING MASTER ROUND'+str(n).encode()+rb' -->',raw[begin.end():],re.M)
            middle=raw[begin.end():begin.end()+end.start()]
            found=None
            for left in range(4):
                for right in range(4):
                    b=middle[left:len(middle)-right if right else None]
                    if sha(b)==f['sha256']:found=b;break
                if found is not None:break
            if found is None:raise ValueError('Cannot reconstruct historical snapshot '+str(n))
            snapshots[n]=found;p=work/f'research_history_frozen/master_before_round{n}.md'
            p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(found)
        patch=json.loads((work/'research_round14_2026_10_21/structural/main_cr_editorial_patch.json').read_text())
        phase=work/patch['file']; final_phase=phase.read_bytes()
        env=os.environ.copy();env['OPENBLAS_NUM_THREADS']='1';env['OMP_NUM_THREADS']='1'
        env.pop('PYTHONOPTIMIZE',None)
        for rel in scripts:
            context='final embedded source bytes';extra=[]
            if rel.endswith('r9_arithmetic_galois_check.py'):
                (work/'Spectral_research_master.md').write_bytes(snapshots[9]);context='exact master before round9'
            if rel.endswith('r7_audit_physical_fixed_powers49_checks.py'):
                (work/'Spectral_research_master.md').write_bytes(snapshots[7]);context='exact master before round7'
            if rel.endswith('verify_spectral_simplicity.py'):
                # Redfix 2026-10-25 (U3, second leg): this script's default
                # --output overwrites spectral_simplicity_certificates.json
                # next to itself, which is also the pinned input that
                # arithmetic_second_order.py later hash-asserts. Redirect
                # the regenerated output to the receipt directory so the
                # staged pinned bytes survive; the script's own checks
                # still run unchanged and its exit code is still gated.
                extra=['--output',str(out/'research_continuation_2026_10_20__verify_spectral_simplicity.regenerated_certificates.json')];context='regenerated output redirected out of staged tree; pinned input preserved'
            if rel.endswith('arithmetic_endpoint_global_content_probe.py'):
                extra=['--n','3','--max-total','3'];context='bounded CLI: n=3, max-total=3'
            if rel.endswith('r14_coordinate_phase_audit_checks.py'):
                old=final_phase
                for change in reversed(patch['patches']):
                    k=change['offset_zero_based'];before=bytes.fromhex(change['delete_hex']);after=bytes.fromhex(change['insert_hex'])
                    if old[k:k+len(after)]!=after:raise ValueError('Editorial patch context')
                    old=old[:k]+before+old[k+len(after):]
                if sha(old)!=patch['old_sha256']:raise ValueError('Historical phase identity')
                phase.write_bytes(old);context='pre-editorial phase hash '+patch['old_sha256']
            name=rel.replace('/','__');start=time.monotonic();source_sha=sha((work/rel).read_bytes())
            staged_orig=None
            if rel.endswith('arithmetic_second_order.py'):
                # Redfix 2026-10-25 (U3): this byte-exact catalog script
                # hardcodes the original author's scratch prefix
                # /workspace/scratch/e111873eea6c, which exists on no
                # replay machine. The harness already stages the two
                # pinned inputs it reads (sibling script bytes ==
                # INPUT_SHA, certificates bytes == INITIAL_CERTIFICATES_SHA)
                # into the disposable workspace, so only the prefix is
                # translated, exactly once, after source_sha is recorded
                # from the original bytes. The sha assertions still run
                # unchanged; any drift of the anchor fails loudly.
                staged=work/rel;staged_orig=staged.read_bytes();text=staged_orig.decode()
                anchor="Path('/workspace/scratch/e111873eea6c/research_continuation_2026_10_20')"
                if text.count(anchor)!=1:raise ValueError('Stale scratch prefix drift')
                staged.write_text(text.replace(anchor,'Path(%r)'%str(work/'research_continuation_2026_10_20')))
                context='stale absolute scratch prefix translated to disposable workspace; sha assertions unchanged'
            try:
                with (out/(name+'.stdout')).open('w') as stdout,(out/(name+'.stderr')).open('w') as stderr:
                    try:
                        p=subprocess.run([sys.executable,str(work/rel),*extra],cwd=work,env=env,
                                         stdout=stdout,stderr=stderr,timeout=40,preexec_fn=limits)
                        code=p.returncode
                    except subprocess.TimeoutExpired:code='timeout'
            finally:
                phase.write_bytes(final_phase)
                if staged_orig is not None:(work/rel).write_bytes(staged_orig)
            runs.append({'path':rel,'source_sha256':source_sha,'args':extra,'context':context,
                         'exit_code':code,'seconds':round(time.monotonic()-start,3)})
    result={'schema':'bgs-spectral-replay-v1','source_sha256':c['source_sha256'],
            'resource_caps':{'cpu_seconds':35,'wall_seconds':40,'memory_bytes':2*1024**3,'output_file_bytes':20*1024**2},
            'runs':runs,'passed':sum(r['exit_code']==0 for r in runs),'total':len(runs),
            'non_claim':'Finite original checks only; no asymptotic theorem or full manuscript certification.'}
    (out/'receipt.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'passed':result['passed'],'total':len(runs),'output':str(out)}))
    if result['passed']!=len(runs):raise SystemExit(1)

if __name__=='__main__':main()
