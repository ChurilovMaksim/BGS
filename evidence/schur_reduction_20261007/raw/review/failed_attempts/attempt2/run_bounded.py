#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,subprocess,resource,os,sys,time,datetime,platform
import sympy
ROOT=Path(__file__).resolve().parent
inputs=['check_independent.py','run_bounded.py','source_manifest.json','pinned/bgs_balanced_phase_closure/candidate_v1.md','pinned/BGS/supplement/fixed_map/weighted-secular/determinant_boundary.md']
sha=lambda x:hashlib.sha256((ROOT/x).read_bytes()).hexdigest()
before={p:sha(p) for p in inputs};cpu=min(os.sched_getaffinity(0));limit=160;wall=180

def caps():
 os.sched_setaffinity(0,{cpu});resource.setrlimit(resource.RLIMIT_CPU,(limit,limit));resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',NUMEXPR_NUM_THREADS='1')
started=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.monotonic();code=124;status='timed_out'
with (ROOT/'checks.json').open('w') as out,(ROOT/'checks.stderr').open('w') as err:
 try:
  p=subprocess.run([sys.executable,'check_independent.py'],cwd=ROOT,env=env,preexec_fn=caps,timeout=wall,stdout=out,stderr=err);code=p.returncode;status='completed' if code==0 else 'failed'
 except subprocess.TimeoutExpired:err.write('Declared 180-second wall cap reached.\n')
sm=json.loads((ROOT/'source_manifest.json').read_text())
manifest={'schema_version':2,'claim_id':'BGS-SCHUR-REDUCTION-INDEPENDENT-AUDIT','repository':{'commit':sm['canonical_commit'],'dirty':bool(sm['canonical_status'])},'command':[sys.executable,'run_bounded.py'],'environment':{'software':[{'name':'Python','version':sys.version},{'name':'SymPy','version':sympy.__version__}],'hardware':platform.platform()},'mathematics':{'assertion_tested':'Principal-minor Newton reconstruction versus matrix-recurrence transfer/log/positive-energy coefficients; exact phase quadrature; complex-radius determinant and loss identities; Laurent moment series; exact coherence and principal-modulus witnesses; degenerate and cyclic controls.','coefficient_domain':'Q(i), Q(sqrt(3)), exact symbolic/rational arithmetic','conventions':'Ordinary traces, normalized independent left coordinate phases, analytic log at zero. Derivative z*d/dz.','inputs':inputs,'bounds':{'dimensions':[1,2,3,4],'power_max_by_dimension':{'1':5,'2':5,'3':4,'4':4},'orders_by_dimension':{'1':1,'2':2,'3':6,'4':2},'phase_grid':'all fourth roots independently for N=2,3, m=1..3','complex_radius':'(2+i)/5','moment_samples':3,'moment_max_radial_degree':12,'cycle_dimensions':[1,2,3,4,7],'cycle_max_power':'3N+1'},'non_claims':['No microscopic N limit','No computation of actual fixed-tau operator','No proof of FM-021/FM-022','No off-charge or higher-factorial closure','No formal verification']},'randomness':{'used':False,'generator':'none','seed':None},'run':{'started_at':started,'runtime_seconds':time.monotonic()-t,'exit_status':code,'status':status,'resource_limits':{'memory_bytes':2*1024**3,'cpu_seconds':limit,'max_cores':1,'max_threads':1},'wall_timeout_seconds':wall,'cpu_affinity':cpu},'input_artifacts':[{'path':p,'sha256':before[p],'sha256_after':sha(p)} for p in inputs],'execution_artifacts':inputs,'declared_results':['checks.json'],'outputs':[{'path':p,'sha256':sha(p),'kind':'result' if p.endswith('.json') else 'log'} for p in ['checks.json','checks.stderr']],'checks':[{'check':'Independent bounded finite algebra','passed':code==0}],'result':'implementation and finite assertion verified in the stated range' if code==0 else 'failed; inspect exact error log','residual_risks':['Finite exact computations support only their stated ranges','Symbolic library trust','Analytic proof audited in separate prose','Concurrent canonical integration is outside this snapshot']}
(ROOT/'execution_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'status':status,'exit_status':code,'runtime_seconds':manifest['run']['runtime_seconds']}));sys.exit(code)
