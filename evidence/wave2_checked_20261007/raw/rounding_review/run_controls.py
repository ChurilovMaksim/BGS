import datetime, hashlib, json, os, platform, subprocess, sys, time
from pathlib import Path
import numpy, scipy
out=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
script=out/'check_companions.py'; before=sha(script)
started=datetime.datetime.now(datetime.timezone.utc).isoformat(); clock=time.monotonic()
env={**os.environ,'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1'}
argv=[sys.executable,str(script)]
p=subprocess.run(argv,cwd=out,env=env,capture_output=True,text=True,timeout=60)
elapsed=time.monotonic()-clock
(out/'stdout.txt').write_text(p.stdout); (out/'stderr.txt').write_text(p.stderr)
assert p.returncode==0 and sha(script)==before
controls=json.loads((out/'controls.json').read_text())
manifest={
 'schema_version':1,'claim_id':'BGS-WAVE2-ROUNDING-COMPANIONS-BOUNDED-CONTROLS',
 'repository':{'commit':'d37c92e563d10d25bb1d6ab85bedffc1f160f773','dirty':True,'note':'Read-only non-Git source snapshot includes checked staged additions; authoritative snapshot manifest SHA256 d6d5ade7444d9a2de43be89fd9636554404a275aa6703fa93910e55c1a1826ba. No repository edit.'},
 'command':argv,
 'environment':{'software':[{'name':'python','version':platform.python_version()},{'name':'numpy','version':numpy.__version__},{'name':'scipy','version':scipy.__version__}],'hardware':platform.platform(),'limits':'60-second subprocess timeout; BLAS/OpenMP requested one thread (cooperative); no hard memory or CPU-affinity limit.'},
 'mathematics':{'assertion_tested':'Exact complete-pair/balanced/offcharge decomposition and disjoint literal Hamming/switch masks; finite perturbation norm and normalized word inequalities; finite growing-period phase-split diagnostics.','coefficient_domain':'Gaussian integers with explicit common denominators for masks; IEEE complex128 floating linear algebra and scalar bump values otherwise.','conventions':'Ordinary traces, N^-2 time aggregation, charges y-x modulo N, rooted cyclic paths, ordinary matrix/HS operator norms.','inputs':[{'path':str(script),'sha256_before':before,'sha256_after':sha(script)}]+[{'snapshot_relative_path':p,'sha256':h} for p,h in controls['source_pins'].items()], 'bounds':{'masks':{'N':3,'m':[1,2,3,4,5],'ordered_pairs':66429,'switch_cutoffs':[0,1,2]},'norm_N':[3,5,9],'word_lengths':[1,2,3,7,17],'split_primes':[5,11],'split_trace_powers':'1 through 2N','smooth_band':'(1,2), L=256; finite N=1025,4097,16385'},'non_claims':['No numerical proof of asymptotic divergence, spectral irrationality, compactness, or actual-model identities.','No rounding of actual U_N at enormous fixed-tau startup was performed.','No analytic source theorem is inferred from bounded execution.']},
 'randomness':{'used':True,'generator':'numpy default_rng PCG64','seed':20261007},
 'run':{'started_at':started,'runtime_seconds':elapsed,'exit_status':p.returncode},
 'outputs':[{'path':name,'sha256':sha(out/name)} for name in ['controls.json','stdout.txt','stderr.txt']],
 'checks':['All 24 consumed source pins match the supplied checked snapshot manifest.','Source manifest SHA256 matches exact parent pin.','Gaussian-rational input unitarity checked exactly.','All 66429 path-pair classifications enumerated without symmetry reductions.','Continuity and split inequalities passed with disclosed floating tolerances.','Smooth-band return sum exceeds the fixed Abel constant by more than one.'],
 'result':'Implementation and finite exact assertions verified in stated ranges; floating diagnostics conditional on stated tolerances. Universal conclusions are established by the separate proof audit.',
 'residual_risks':['Version-1 manifest has legacy provenance limits. Explicit execution-input hashes are nevertheless recorded.','Floating bounds are diagnostics without interval certificates.','Source dependency acceptance is imported with exact bytes and scopes; no full re-audit of all earlier analytic theorems.']}
(out/'computation_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(p.stdout,end='');print('Runtime seconds:',elapsed)
