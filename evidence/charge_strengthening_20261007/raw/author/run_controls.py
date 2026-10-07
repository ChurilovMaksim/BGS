#!/usr/bin/env python3
import hashlib,json,os,platform,resource,subprocess,sys,time
from pathlib import Path
R=Path(__file__).resolve().parent
FILES=['check_exact.py','onestep_charge_gap.md','global_switch_transfer.md','rounding_gap_obstruction.md']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def limits():
 resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
 resource.setrlimit(resource.RLIMIT_CPU,(60,60))
 env=os.environ.copy()
 for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:env[k]='1'
 return env
before={p:sha(R/p) for p in FILES};jobs=[]
for tag,extra,expected in [('normal',[],0),('optimized',['-O'],0),('injected',['-O'],1)]:
 cmd=[sys.executable]+extra+[str(R/'check_exact.py')]+(['--inject-failure'] if tag=='injected' else [])
 t=time.monotonic(); p=subprocess.run(cmd,capture_output=True,text=True,env=limits(),timeout=70)
 (R/f'{tag}.stdout').write_text(p.stdout);(R/f'{tag}.stderr').write_text(p.stderr)
 if (p.returncode==0)!=(expected==0):raise RuntimeError(f'{tag} exit {p.returncode}')
 jobs.append({'tag':tag,'command':cmd,'returncode':p.returncode,'elapsed_seconds':time.monotonic()-t,'stdout_sha256':sha(R/f'{tag}.stdout'),'stderr_sha256':sha(R/f'{tag}.stderr')})
if (R/'normal.stdout').read_bytes()!=(R/'optimized.stdout').read_bytes():raise RuntimeError('optimized output differs')
after={p:sha(R/p) for p in FILES}
if before!=after:raise RuntimeError('input mutated during run')
(R/'exact_results.json').write_bytes((R/'normal.stdout').read_bytes())
manifest={'python':sys.version,'platform':platform.platform(),'arithmetic':'exact Python integers for Gaussian numerators; no numerical libraries','caps':{'address_space_bytes':512*1024**2,'cpu_seconds':60,'subprocess_wall_seconds':70},'source_hashes_before':before,'source_hashes_after':after,'jobs':jobs,'result_sha256':sha(R/'exact_results.json'),'analytic_nonclaim':'These are bounded auxiliary-matrix identities, not asymptotic or literal-tau computation.'}
(R/'control_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'status':'passed','ordered_pairs':json.loads((R/'exact_results.json').read_text())['total_ordered_pairs'],'result_sha256':manifest['result_sha256']},indent=2))
