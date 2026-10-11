"""Execute trusted local checks and preserve actual v1 evidence records.

This standalone directory is intentionally outside BGS; no Git inspection.
The schema is the Mathbox v1 compatibility schema, not a v2 provenance claim.
"""
import datetime
import hashlib
import json
import os
import platform
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
CONTRACTS={
 "flat_completion_check":{
  "assertion":"Exact cavity inputs, low-rank unitary patch, preserved covariance, nearly flat transition matrix; sampled overlap second moment.",
  "bounds":{"m":[3,5,7],"N":[396,900,3136],"r":[30,25,49],"a":.4,"direct_schur_max_N":1000,"overlap_phase_samples":12000,"overlap_N":32,"overlap_m":3,"residual_threshold":5e-8},
  "seed":86742091,
  "non_claims":["No phase-averaged covariance theorem.","No dense Schur inverse at N=3136.","No BGS proof or counterexample."]},
 "nonlinear_check":{
  "assertion":"Global determinant coercivity, Mobius invariance, regulator bound, scalar source derivatives, nonnormal matrix-source contractions and both determinant body bounds.",
  "bounds":{"N":[4,8,16],"q":[1,2,3],"radii":[.1,.7,.98,.999999],"ordinary_controls":72,"matrix_source_controls":8,"scalar_derivative_orders":[1,2,3,4],"max_Mobius_tolerance":3e-7},
  "seed":640139,
  "non_claims":["No full supersymmetric integration.","No Grassmann-coefficient bound.","No BGS proof."]},
 "clock_law_check":{
  "assertion":"Regularized quantile spectra, covariance formula, mixture and completion bounds for three laws, including a zero atom and an infinite second moment.",
  "bounds":{"m":[3,5,7,11,31,101,521],"laws":["(delta_0+delta_2)/2","exponential(mean=1)","Pareto(alpha=1.5,mean=1)"],"finite_spectrum_cases":21,"N_matrix_allocations":0,"max_mean_tolerance":3e-12},
  "seed":None,
  "non_claims":["Formal huge N dimensions are not computed matrices.","Pareto higher moments are not uniformly bounded.","No phase law or BGS proof."]},
 "exact_controls":{
  "assertion":"Finite exact nonnormal Julia blocks, nonnegative trace-power coefficients and noncommuting Mobius determinant identities.",
  "bounds":{"Julia_m":[2,3,5],"trace_q":[1,2],"trace_N":4,"trace_orders":[1,2,3,4,5,6,7,8],"Mobius_dimension":2,"Mobius_centers":2},
  "seed":None,
  "non_claims":["Finite exact witnesses are not a formal proof of arbitrary dimensions.","No BGS proof."]}
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    name=sys.argv[1]
    contract=CONTRACTS[name]
    code=name+('.cpp' if name=='exact_controls' else '.py')
    inputs=[code,'run_record.py']
    hashes={p:digest(ROOT/p) for p in inputs}
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    clock=time.monotonic()
    env=os.environ.copy()
    env.update(OPENBLAS_NUM_THREADS='2',OMP_NUM_THREADS='2')
    build_argv=None
    with tempfile.TemporaryDirectory(prefix='bgs_flat_exact_') as td:
        if name=='exact_controls':
            binary=str(Path(td)/'exact_controls')
            build_argv=['g++','-std=c++20','-O2',code,'-o',binary]
            built=subprocess.run(build_argv,cwd=ROOT,env=env,capture_output=True,text=True,timeout=30)
            assert built.returncode==0,built.stderr
            argv=[binary]
        else:
            argv=[sys.executable,code]
        process=subprocess.run(argv,cwd=ROOT,env=env,capture_output=True,text=True,timeout=30)
    elapsed=time.monotonic()-clock
    log=ROOT/(name+'_execution.log')
    log.write_text(process.stdout+process.stderr)
    assert process.returncode==0,(process.returncode,process.stderr)
    assert hashes=={p:digest(ROOT/p) for p in inputs}
    result=ROOT/(name+'_results.json')
    if name=='exact_controls':
        parsed=json.loads(process.stdout)
        assert parsed['all_passed'] is True
        result.write_text(json.dumps(parsed,indent=2)+'\n')
    else:
        assert result.is_file()
    import numpy,scipy
    software=[{'name':'Python','version':platform.python_version()},
              {'name':'NumPy','version':numpy.__version__},
              {'name':'SciPy','version':scipy.__version__}]
    if name=='exact_controls':
        software.append({'name':'g++','version':subprocess.check_output(['g++','--version'],text=True).splitlines()[0]})
    record={
      'schema_version':1,'claim_id':name+'_finite_control',
      'repository':{'commit':None,'dirty':True},'command':argv,
      'environment':{'software':software,'hardware':platform.machine()+' '+platform.processor(),
        'thread_caps':{'OPENBLAS_NUM_THREADS':2,'OMP_NUM_THREADS':2},
        'wall_timeout_seconds_per_process':30,'build_argv':build_argv},
      'mathematics':{'assertion_tested':contract['assertion'],
        'coefficient_domain':'exact Gaussian rational with checked 128-bit arithmetic' if name=='exact_controls' else 'complex128 / float64',
        'conventions':'Common row phases; right normalization of two frames; ordered defect operators; real radii at the boundary.',
        'inputs':[{'path':p,'sha256':h} for p,h in hashes.items()],
        'bounds':contract['bounds'],'non_claims':contract['non_claims']},
      'randomness':{'used':contract['seed'] is not None,'generator':'NumPy PCG64' if contract['seed'] is not None else 'none','seed':contract['seed']},
      'run':{'started_at':started,'runtime_seconds':elapsed,'exit_status':process.returncode},
      'outputs':[{'path':p.name,'sha256':digest(p)} for p in [result,log]],
      'checks':['zero process exit','input hashes unchanged during the run','assertions in the executed program','result exists'],
      'result':'Implemented finite assertions passed in the stated range.',
      'residual_risks':['Version 1 compatibility record; not a v2 bounded-run certificate.',
        'Independent scratch files are not Git versioned; BGS was not inspected.',
        'No formal proof certification; finite bounds do not establish universality.',
        'Thread settings are cooperative; no memory or aggregate CPU limit.']}
    (ROOT/(name+'_manifest.json')).write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'name':name,'runtime_seconds':elapsed,'passed':True}),flush=True)


if __name__=='__main__':
    main()
