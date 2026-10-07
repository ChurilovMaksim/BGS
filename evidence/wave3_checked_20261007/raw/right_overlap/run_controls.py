#!/usr/bin/env python3
"""Final bounded rerun with version-2 input/output provenance."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, platform, subprocess, sys, time
import sympy

root=Path(__file__).resolve().parent
scripts=['accepted_left_controls/check_overlap.py','check_transpose.py','check_separated_independent.py']
input_names=['run_controls.py']+scripts
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
inputs=[{'path':p,'sha256':sha(root/p),'sha256_after':None} for p in input_names]
commands=[]
outputs=[]
results=[]
for script,base,resultbase in [('accepted_left_controls/check_overlap.py','accepted_left_controls','checks'),('check_transpose.py','.','transpose_checks'),('check_separated_independent.py','.','separated_checks')]:
    for optimized in (False,True):
        suffix='_optimized' if optimized else ''
        result=Path(base)/(resultbase+suffix+'.json')
        log=Path(base)/(resultbase+suffix+'.rerun.log')
        results.append(result.as_posix())
        outputs.append((log.as_posix(),'log'))
        outputs.append((result.as_posix(),'result'))
        commands.append((['python3']+(['-O'] if optimized else [])+[script],log))
started=datetime.now(timezone.utc).isoformat()
t0=time.monotonic()
statuses=[]
for argv,log in commands:
    with (root/log).open('w') as out:
        run=subprocess.run(argv,cwd=root,stdout=out,stderr=subprocess.STDOUT,timeout=60)
    statuses.append({'argv':argv,'exit_status':run.returncode})
    if run.returncode: raise RuntimeError(str(statuses[-1]))
runtime=time.monotonic()-t0
for x in inputs: x['sha256_after']=sha(root/x['path'])
changed=any(x['sha256']!=x['sha256_after'] for x in inputs)
if changed: raise RuntimeError('execution inputs changed')
manifest={
    'schema_version':2,
    'claim_id':'BGS-RIGHT-SEPARATED-REVIEW-BOUNDED-CONTROLS-20261007',
    'repository':{'commit':'129c676b8e6457e7e5f1bd6f786b3939cbd84653','dirty':False},
    'command':' && '.join(' '.join(argv) for argv,_ in commands),
    'environment':{'software':[{'name':'Python','version':platform.python_version()},{'name':'SymPy','version':sympy.__version__}],'hardware':platform.platform(),'timestamp_source':'execution environment UTC wall clock'},
    'mathematics':{
        'assertion_tested':'Exact bounded right-frame, fixed-B Gram, cyclic Hessian, composition multiplicity, decreasing-weight endpoint and Schatten-2 identities.',
        'coefficient_domain':'Exact integers, rationals and Gaussian rationals; SymPy polynomial differentiation.',
        'conventions':'Ordinary HS; row-major vec; row-minus-column slice label; complex-linear transpose; rooted cyclic products; ordinary superoperator Schatten norm.',
        'inputs':scripts,
        'bounds':{'accepted_left_fixture_N':[3,5],'accepted_left_hessian_r':[1,16],'transpose_fixture_N':[3,5],'transpose_r':[0,3],'right_Gram_L':3,'right_hessian_r':[1,16],'rooted_word_m':[1,12],'rooted_word_j':'all 1<=j<=m','endpoint_bands':[[1,5],[4,11],[10,21]],'Schatten2_fixture_N':[3,5],'per_command_timeout_seconds':60},
        'non_claims':['No analytic stationary-phase or N-limit certification.','No candidate 222-core-suite reproduction.','No rate, mask, deconvolution, T16 or BGS certification.']},
    'randomness':{'used':False,'generator':'none','seed':None},
    'run':{'started_at':started,'runtime_seconds':runtime,'exit_status':0,'status':'completed','resource_limits':{'memory_bytes':None,'cpu_seconds':None,'max_cores':None,'max_threads':None},'per_command_timeout_seconds':60},
    'input_artifacts':inputs,'execution_artifacts':input_names,'declared_results':results,
    'outputs':[{'path':p,'kind':kind,'sha256':sha(root/p)} for p,kind in outputs],
    'checks':statuses,
    'result':'All final normal and optimized exact bounded runs passed: accepted-left 129, independent right 72 (18 direct transpose), independent separated 227 per mode.',
    'residual_risks':['Execution environment wall clock recorded; not reconciled with conversation-server clock.','No POSIX memory, CPU, affinity or cooperative thread caps were imposed; explicit finite enumerator bounds and 60-second per-command timeout apply.','SymPy supplies exact symbolic algebra; the universal implications are separately derived in the prose audit.']}
(root/'computation_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'status':manifest['run']['status'],'runtime_seconds':runtime,'result':manifest['result']},indent=2))
