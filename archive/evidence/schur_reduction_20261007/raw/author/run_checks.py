#!/usr/bin/env python3
from pathlib import Path
import datetime,hashlib,json,os,platform,resource,subprocess,sys,time
import sympy
ROOT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
inputs=['checks.py','run_checks.py','candidate_v1.md','source_manifest.json']
before={p:sha(ROOT/p) for p in inputs}
cpu=min(os.sched_getaffinity(0))
def limits():
 os.sched_setaffinity(0,{cpu});resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3));resource.setrlimit(resource.RLIMIT_CPU,(60,60))
env=os.environ.copy();env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
start=time.monotonic();stamp=datetime.datetime.now(datetime.timezone.utc).isoformat();status='timed_out';code=124
with (ROOT/'verified_checks.json').open('w') as out, (ROOT/'verified_checks.stderr').open('w') as err:
 try:
  run=subprocess.run([sys.executable,'checks.py'],cwd=ROOT,env=env,preexec_fn=limits,timeout=70,stdout=out,stderr=err);code=run.returncode;status='completed' if code==0 else 'failed'
 except subprocess.TimeoutExpired:err.write('70-second wall timeout.\n')
repo='/workspace/shared/BGS'
manifest={'schema_version':2,'claim_id':'BGS-BALANCED-SCALAR-SCHUR-ENERGY-CANDIDATE','repository':{'commit':subprocess.check_output(['git','-C',repo,'rev-parse','HEAD'],text=True).strip(),'dirty':bool(subprocess.check_output(['git','-C',repo,'status','--porcelain'],text=True))},'command':[sys.executable,'run_checks.py'],'environment':{'software':[{'name':'Python','version':sys.version},{'name':'SymPy','version':sympy.__version__}],'hardware':platform.platform()},'mathematics':{'assertion_tested':'Exact scalar logarithmic Schur increments and positive pair-energy coefficients, determinant and contraction-energy identities, scalar phase second/fourth moments by rational residues, equal-principal-modulus counterexample, cyclic-permutation controls.','coefficient_domain':'Q(i), Q(sqrt(3)) and exact rational symbolic residues','conventions':'Ordinary traces, normalized torus measure, left coordinate phases, analytic logarithm zero at origin, r=exp(-s/N).','inputs':inputs,'bounds':{'word_dimension':3,'word_powers':[1,2,3,4,5,6],'literal_radii':['1/3','2/3'],'cycle_dimensions':[2,3,5,7],'max_cycle_power':15,'scalar_moment_samples':3},'non_claims':['No actual fixed-tau matrix numerics','No asymptotic radial estimate or pair universality','No higher factorial-order theorem','No independent review']},'randomness':{'used':False,'generator':'none','seed':None},'run':{'started_at':stamp,'runtime_seconds':time.monotonic()-start,'exit_status':code,'status':status,'resource_limits':{'memory_bytes':2*1024**3,'cpu_seconds':60,'max_cores':1,'max_threads':1},'wall_timeout_seconds':70,'cpu_affinity':cpu},'input_artifacts':[{'path':p,'sha256':before[p],'sha256_after':sha(ROOT/p)} for p in inputs],'execution_artifacts':inputs,'declared_results':['verified_checks.json'],'outputs':[{'path':p,'sha256':sha(ROOT/p),'kind':'result' if p.endswith('.json') else 'log'} for p in ['verified_checks.json','verified_checks.stderr']],'checks':[{'check':'Exact finite script checks','passed':code==0}],'result':'implementation and finite assertion verified in the stated range' if code==0 else 'incomplete run','residual_risks':['Symbolic arithmetic is not formal certification','No independent proof audit yet','Inherited FM-021/FM-022 analytic inputs were not recertified']}
(ROOT/'execution_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'status':status,'exit_status':code,'runtime_seconds':manifest['run']['runtime_seconds']}));sys.exit(code)
