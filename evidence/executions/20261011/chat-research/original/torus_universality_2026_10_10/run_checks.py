"""Bounded finite controls and complete v1-compatible run record.

No Git reads or writes. Cooperative BLAS caps and per-process wall caps are
recorded; this is not a v2 resource certificate or a formal mathematical proof.
"""
from pathlib import Path
import datetime
import hashlib
import json
import os
import platform
import subprocess
import sys
import tempfile
import time

ROOT=Path(__file__).resolve().parent


def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    inputs=['weight_check.py','weight_check.cpp','phase_controls.py','run_checks.py']
    before={p:digest(ROOT/p) for p in inputs}
    began=datetime.datetime.now(datetime.timezone.utc).isoformat()
    clock=time.monotonic()
    env=os.environ.copy()
    env.update(OPENBLAS_NUM_THREADS='2',OMP_NUM_THREADS='2')
    argv=[]
    logs=[]
    with tempfile.TemporaryDirectory(prefix='bgs_torus_exact_') as td:
        binary=str(Path(td)/'weight_check')
        jobs=[['g++','-std=c++20','-O2','-Wall','-Wextra','weight_check.cpp','-o',binary],
              [sys.executable,'weight_check.py'],[binary],
              [sys.executable,'phase_controls.py']]
        for j,command in enumerate(jobs):
            process=subprocess.run(command,cwd=ROOT,env=env,capture_output=True,text=True,timeout=45)
            argv.append(command)
            log=ROOT/f'check_{j}_execution.log'
            log.write_text(process.stdout+process.stderr)
            logs.append(log)
            assert process.returncode==0,(command,process.stderr)
            if j==2:
                result=json.loads(process.stdout)
                assert result['all_passed'] is True
                (ROOT/'weight_cpp_results.json').write_text(json.dumps(result,indent=2)+'\n')
    py=json.loads((ROOT/'weight_check_results.json').read_text())
    cpp=json.loads((ROOT/'weight_cpp_results.json').read_text())
    assert py['cases']==cpp['cases'],'independent enumerations disagree'
    assert before=={p:digest(ROOT/p) for p in inputs},'input changed during execution'
    elapsed=time.monotonic()-clock
    import numpy
    outputs=logs+[ROOT/p for p in ['weight_check_results.json','weight_cpp_results.json','phase_controls_results.json']]
    record={
      'schema_version':1,'claim_id':'torus_weight_and_phase_finite_controls',
      'repository':{'commit':None,'dirty':True},
      'command':[sys.executable,'run_checks.py'],
      'environment':{'software':[{'name':'Python','version':platform.python_version()},
                                {'name':'NumPy','version':numpy.__version__},
                                {'name':'g++','version':subprocess.check_output(['g++','--version'],text=True).splitlines()[0]}],
                     'hardware':platform.machine(),'subprocess_commands':argv,
                     'thread_caps':{'OPENBLAS_NUM_THREADS':2,'OMP_NUM_THREADS':2},
                     'wall_timeout_seconds_per_process':45},
      'mathematics':{
        'assertion_tested':'Finite exact zero/root multiplicities and Weyl dimensions; agreement of independent Python/C++ enumerations; occupation-average third form factor; bilinear Fourier Q identities; sampled adjoint Haar variance.',
        'coefficient_domain':'Python integer/Fraction; checked C++ int128/int64; complex128 phase identities and sampled Haar matrices',
        'conventions':'Dominant integral U(N) weights of central charge zero; right QR phase correction; P=|U|², Q_ij=U_ij conjugate(U_ji).',
        'inputs':[{'path':p,'sha256':h} for p,h in before.items()],
        'bounds':{'N_2_to_7_weight_box':[-2,2],'N_2_to_5_extra_weight_box':[-4,4],
                  'exact_weight_cases':py['exact_cases'],
                  'third_formula_N':[2,3,4,5,7],'third_formula_families':['Haar','identity','cyclic'],
                  'bilinear_p_d':[[3,2],[3,3],[3,4],[5,2]],'bilinear_ranks':[0,2],
                  'Haar_variance_N':[2,4,8,16,32],'samples_each':2400,
                  'formula_tolerance':2e-12,'Q_tolerance':3e-12,'small_bilinear_occupation_tolerance':3e-11},
        'non_claims':['Finite weight boxes do not prove the universal dimension bound.',
                      'Haar variance samples are reported with standard errors, not exact certificates.',
                      'No form factor at n comparable to N is computed.',
                      'No Lean compilation or BGS proof.']},
      'randomness':{'used':True,'generator':'NumPy PCG64','seed':101064271},
      'run':{'started_at':began,'runtime_seconds':elapsed,'exit_status':0},
      'outputs':[{'path':p.name,'sha256':digest(p)} for p in outputs],
      'checks':['all process exits zero','input hashes unchanged','finite inequalities asserted',
                'independent Python/C++ records identical','occupation grouping agrees with third trace formula',
                'Fourier matrices unitary and Q³=p^(-r)Q within stated tolerances'],
      'result':f"All deterministic finite controls passed; {py['exact_cases']} exact weight cases. Haar variances retain Monte Carlo uncertainty.",
      'residual_risks':['Version 1 record, not a v2 bounded-run certificate.',
                        'No aggregate CPU or memory cap; thread caps cooperative.',
                        'No Git snapshot: the work is deliberately outside BGS.',
                        'Floating checks depend on stated tolerances; Lean is unavailable.']}
    (ROOT/'computation_manifest.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'passed':True,'weight_cases':py['exact_cases'],'runtime_seconds':elapsed}))


if __name__=='__main__':main()
