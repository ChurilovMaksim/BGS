"""Record actual completed standalone computations without inspecting BGS."""
import datetime
import hashlib
import json
import os
import platform
from pathlib import Path
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parent


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def run(name, argv, inputs, scientific_outputs, assertion, bounds, non_claims):
    input_before={p:digest(ROOT/p) for p in inputs}
    start=datetime.datetime.now(datetime.timezone.utc).isoformat()
    clock=time.monotonic()
    env=os.environ.copy()
    env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
    process=subprocess.run(argv,cwd=ROOT,env=env,capture_output=True,text=True,timeout=120)
    elapsed=time.monotonic()-clock
    input_after={p:digest(ROOT/p) for p in inputs}
    log=ROOT/(name+'_execution.log')
    log.write_text(process.stdout+process.stderr)
    assert process.returncode==0,(name,process.returncode,process.stderr)
    assert input_before==input_after, 'input changed during run'
    outputs=[]
    for p in [*scientific_outputs,log.name]:
        assert (ROOT/p).is_file()
        outputs.append({'path':p,'sha256':digest(ROOT/p)})
    versions=[{'name':'Python','version':platform.python_version()}]
    if name!='jacobian_exact':
        import numpy, scipy
        versions.extend([{'name':'NumPy','version':numpy.__version__},{'name':'SciPy','version':scipy.__version__}])
    else:
        compiler=subprocess.run(['g++','--version'],capture_output=True,text=True,check=True).stdout.splitlines()[0]
        versions.append({'name':'g++','version':compiler})
    record={
        'schema_version':1,'claim_id':name+'_finite_control',
        'repository':{'commit':None,'dirty':True},
        'command':argv,
        'environment':{'software':versions,'hardware':platform.machine()+' '+platform.processor(),
            'thread_caps':{'OPENBLAS_NUM_THREADS':1,'OMP_NUM_THREADS':1},'wall_timeout_seconds':120},
        'mathematics':{'assertion_tested':assertion,'coefficient_domain':'Gaussian rationals with checked 128-bit arithmetic' if name=='jacobian_exact' else
                      ('fractions.Fraction / complex128' if name=='finite_stiefel_check' else 'complex128'),
            'conventions':'Right logarithmic generators; retained directions use rows of S; real Hermitian coordinates.',
            'inputs':[{'path':p,'sha256':h} for p,h in input_before.items()],
            'bounds':bounds,'non_claims':non_claims},
        'randomness':{'used':name not in ('jacobian_exact','mub_clock_check'),'generator':'NumPy PCG64' if name not in ('jacobian_exact','mub_clock_check') else 'none',
            'seed':202610094 if name=='fresh_phase_check' else (202610093 if name=='finite_stiefel_check' else
                   (202610092 if name=='stiefel_probe' else (202610091 if name not in ('jacobian_exact','mub_clock_check') else None)))},
        'run':{'started_at':start,'runtime_seconds':elapsed,'exit_status':process.returncode},
        'outputs':outputs,'checks':['zero exit status','input hashes unchanged','scientific assertions inside executed program'],
        'result':'Finite assertions passed in the stated range.',
        'residual_risks':['Version 1 record; standalone files are not Git versioned; hashes identify inputs.']+([] if name=='jacobian_exact' else ['Floating tolerance and finite random sampling.'])}
    (ROOT/(name+'_manifest.json')).write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'name':name,'runtime_seconds':elapsed,'exit_status':process.returncode,'input_files':len(inputs)}),flush=True)


def main():
    target=sys.argv[1]
    if target=='frame_probe':
        run(target,[sys.executable,'frame_probe.py'],['frame_probe.py'],['frame_probe_results.json'],
            '624 phase-cavity realizations: unitarity, spectral derivatives covariance row sums, tight normalization, projector energy identity, numerical frame rank diagnostics.',
            {'N':[101,197,389],'m':[4,8],'samples':624,'absolute_residual_threshold':2e-8},
            ['No full conditional covariance test.','No limiting universality or BGS proof.','Numerical rank is not an exact rank certificate.'])
    elif target=='projection_evolution':
        run(target,[sys.executable,'projection_evolution.py'],['projection_evolution.py','frame_probe.py'],['projection_evolution_results.json'],
            '12 nested paths: exact rank-one projection deletion compared to direct QR/Gram projection and direct Schur complements at selected depths.',
            {'N':101,'paths':12,'u_min':3,'check_depths':[101,50,24,12,6,3],'absolute_residual_threshold':5e-8},
            ['No uniform stochastic contraction estimate.','No inverse-clock limiting theorem.','No BGS proof.'])
    elif target=='jacobian_exact':
        run(target,['/tmp/bgs_jacobian_exact'],['jacobian_exact.cpp'],[],
            '10 exact graph-reflection witnesses; 120 phase derivatives; unitary input, identity cavity, rank m² minor with determinant one.',
            {'m_min':1,'m_max':5,'N':'m² or m²+2','cases':10,'phase_channels':120},
            ['Finite witness control is not the analytic null-set or submersion proof.','No BGS proof.'])
    elif target=='stiefel_probe':
        run(target,[sys.executable,'stiefel_probe.py'],['stiefel_probe.py','frame_probe.py'],['stiefel_probe_results.json'],
            '576 direct Gaussian/Stiefel frames: tight normalization, trace, and measured HS defect compared with the separately derived fixed-m coefficients.',
            {'N':[512,2048],'m':[2,4,8],'samples':576,'normalization_residual_threshold':1e-10},
            ['Finite-N sample means are not exact asymptotic values.','No transfer to phase cavities.','No BGS proof.'])
    elif target=='finite_stiefel_check':
        run(target,[sys.executable,'finite_stiefel_check.py'],['finite_stiefel_check.py'],['finite_stiefel_check_results.json'],
            'Exact rational beta-moment identities and positive-series expectation intervals; floating controls of the row-frame differential and its HS bound.',
            {'m':[1,2,3,4,8,16,31],'N':'m, m+1, 2m, 4m, m², or max(m,128)','series_terms':64,
             'differential_samples':128,'relative_finite_difference_threshold':2e-8},
            ['Finite exact rational controls are not the full universal proof.',
             'Floating differential controls are not formal verification.',
             'No transfer to phase cavities.','No BGS proof.'])
    elif target=='mub_clock_check':
        run(target,[sys.executable,'mub_clock_check.py'],['mub_clock_check.py','frame_probe.py'],['mub_clock_check_results.json'],
            'Complete MUB fourth frame identity, flat-clock covariance formula, rotated-design mixture, and direct graph-reflection Schur realization.',
            {'m':[3,5,7],'r':'2m','a':0.4,'absolute_residual_threshold':2e-8},
            ['Pointwise static obstruction, not phase-ensemble or BGS counterexample.',
             'Graph reflection does not supply classical mixing hypotheses.',
             'Floating computation is not a formal proof.'])
    elif target=='fresh_phase_check':
        run(target,[sys.executable,'fresh_phase_check.py'],['fresh_phase_check.py'],['fresh_phase_check_results.json'],
            'One-fresh-phase averages of the deleted projector, inverse clock, and removed output leverage, including isolated-channel controls.',
            {'m':[2,3,5,8],'samples':64,'phase_grid_size':4096,'absolute_residual_threshold':2e-9},
            ['Only first conditional averages, not nonlinear energy drift.',
             'Finite floating phase quadrature is not formal certification.',
             'No BGS proof.'])
    else:
        raise ValueError(target)


if __name__=='__main__':
    main()
