#!/usr/bin/env python3
from pathlib import Path
import datetime,hashlib,json,os,platform,resource,subprocess,sys,time
import sympy
ROOT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
cpu=min(os.sched_getaffinity(0))
def limits():
 os.sched_setaffinity(0,{cpu});resource.setrlimit(resource.RLIMIT_AS,(3*1024**3,3*1024**3));resource.setrlimit(resource.RLIMIT_CPU,(300,300))
env=os.environ.copy();env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
inputs=['independent_controls.py','run_review.py','inputs/candidate_v1.md','input_manifest.json']
before={p:sha(ROOT/p) for p in inputs}; started=datetime.datetime.now(datetime.timezone.utc).isoformat();start=time.monotonic()
log=ROOT/'results/verified_run.log';code=124;status='timed_out'
with log.open('w') as f:
 try:
  r=subprocess.run([sys.executable,'independent_controls.py'],cwd=ROOT,env=env,preexec_fn=limits,timeout=320,stdout=f,stderr=subprocess.STDOUT);code=r.returncode;status='completed' if code==0 else 'failed'
 except subprocess.TimeoutExpired:f.write('\nExplicit 320-second wall timeout.\n')
ok=code==0
results=['results/verified/'+x+'.json' for x in ['full_end','top_gram','torus','network','offcharge_bound','all_results']]
manifest={'schema_version':2,'claim_id':'BGS-FRACTIONAL-HAMMING-INDEPENDENT-AUDIT','repository':{'commit':subprocess.check_output(['git','-C','/workspace/shared/BGS','rev-parse','HEAD'],text=True).strip(),'dirty':True},'command':[sys.executable,'run_review.py'],'environment':{'software':[{'name':'Python','version':sys.version},{'name':'SymPy','version':sympy.__version__}],'hardware':platform.platform()},'mathematics':{'assertion_tested':'Exact literal raw Hamming and charge projections, Lie-kernel Haar invariants, genuine centered ranges and their orthogonal split, proper-support trace annihilation, top Gram, exact finite torus integral, full-rank p/q noncommuting stage seams and bounded off-charge inequality.','coefficient_domain':'QQ(i), exact rational arithmetic; no numerical tolerance','conventions':'Unnormalized HS; R cyclically left-shifts tensor basis tuples; local full-End basis E_ab; top Gram basis E01,E10,E00-E11 with explicit metric. Haar projector from full common infinitesimal commutant.','inputs':inputs,'bounds':{'full_End_N_m':[[2,1],[2,2],[2,3],[3,2]],'all_radii':True,'top_Gram_N_m_r':[2,4,2],'torus_N_m':[[2,3],[3,2]],'phase_grid_order':4,'network_stages':[1,2,3],'offcharge_N':2,'offcharge_m':[1,2,3,4,5,6],'offcharge_r':'0 through floor(m/2)'},'non_claims':['No computational proof of a universal inequality or asymptotic limit.','No recertification of inherited FM-021 parametrix or Haar tail.','Top Gram m4 r2 has n0 and does not verify the sufficient M a_n<1 hypothesis.','Stage phase samples check conventions and are not exhaustive over the torus; exact finite quadrature establishes the projector identity in m<=3 only.','No BGS, plateau or full complement claim.']},'randomness':{'used':False,'generator':'none','seed':None},'run':{'started_at':started,'runtime_seconds':time.monotonic()-start,'exit_status':code,'status':status,'resource_limits':{'memory_bytes':3*1024**3,'cpu_seconds':300,'max_cores':1,'max_threads':1},'wall_timeout_seconds':320,'cpu_affinity':cpu},'input_artifacts':[{'path':p,'sha256':before[p],'sha256_after':sha(ROOT/p)} for p in inputs],'execution_artifacts':inputs,'declared_results':results,'outputs':[{'path':p,'sha256':sha(ROOT/p),'kind':'log' if p.endswith('.log') else 'result'} for p in ['results/verified_run.log']+results if (ROOT/p).exists()],'checks':[{'check':'Exact script assertions','passed':ok}],'result':'implementation and finite assertion verified in the stated range' if ok else 'incomplete run; inspect explicit status and log','residual_risks':['Exact symbolic arithmetic is not formal proof certification.','Candidate actual-family application inherits accepted analytic inputs.']}
(ROOT/'execution_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');print(json.dumps({'status':status,'exit_status':code,'runtime_seconds':manifest['run']['runtime_seconds']}),flush=True);sys.exit(code)
