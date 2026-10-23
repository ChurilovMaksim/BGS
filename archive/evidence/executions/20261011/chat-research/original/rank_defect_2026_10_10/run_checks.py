"""Reproduce the finite checks with pinned inputs and schema-v2 evidence.

Requires Python 3.10+ and g++ supporting C++17, on Linux. No third-party
Python packages, external network, Git operations, Lean, or Wolfram needed.
The stored Wolfram receipt is checked separately, not re-executed.
"""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import math
import os
import platform
import resource
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
INPUTS = ['run_checks.py','next_order.cpp','independent_checks.py','orbit_checks.py',
          'resummation_checks.py','occupation_rank_checks.py',
          'symbolic_checks.wl','wolfram_results.json']
RESULTS = ['next_order_results.json','independent_results.json','orbit_results.json',
           'resummation_results.json','occupation_rank_results.json']
LIMITS = {'memory_bytes':1024**3,'cpu_seconds':120,'max_cores':1,'max_threads':1,
          'wall_seconds':180,'per_command_wall_seconds':60,'max_output_bytes':3_000_000}


def digest(name):
    return sha256((ROOT/name).read_bytes()).hexdigest()


def cpu_used():
    parent = resource.getrusage(resource.RUSAGE_SELF)
    children = resource.getrusage(resource.RUSAGE_CHILDREN)
    return parent.ru_utime+parent.ru_stime+children.ru_utime+children.ru_stime


def main():
    started = datetime.now(timezone.utc).isoformat()
    start = time.monotonic()
    baseline_cpu = cpu_used()
    pinned = {name:digest(name) for name in INPUTS}
    compiler = shutil.which('g++')
    if not compiler:
        raise RuntimeError('g++ is required')
    compiler_version = subprocess.run([compiler,'--version'],check=True,
                                      capture_output=True,text=True,timeout=5).stdout.splitlines()[0]
    selected_cpu = min(os.sched_getaffinity(0))
    env = dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OMP_NUM_THREADS='1',
               OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1',NUMEXPR_NUM_THREADS='1')
    commands = []
    status,exit_status = 'completed',0

    def execute(argv):
        remaining_wall = LIMITS['wall_seconds']-(time.monotonic()-start)
        remaining_cpu = LIMITS['cpu_seconds']-(cpu_used()-baseline_cpu)
        if remaining_wall<=0 or remaining_cpu<=0:
            raise RuntimeError('Aggregate resource budget exhausted')
        timeout = min(LIMITS['per_command_wall_seconds'],remaining_wall)
        ceiling = max(1,math.ceil(remaining_cpu))
        def restrict():
            resource.setrlimit(resource.RLIMIT_AS,(LIMITS['memory_bytes'],LIMITS['memory_bytes']))
            resource.setrlimit(resource.RLIMIT_CPU,(ceiling,ceiling+1))
            os.sched_setaffinity(0,{selected_cpu})
        before = time.monotonic()
        result = subprocess.run(argv,cwd=ROOT,env=env,preexec_fn=restrict,
                                capture_output=True,text=True,timeout=timeout)
        commands.append({'argv':argv,'runtime_seconds':time.monotonic()-before,
                         'exit_status':result.returncode,'stdout':result.stdout,
                         'stderr':result.stderr})
        if len(result.stdout.encode())+len(result.stderr.encode())>LIMITS['max_output_bytes']:
            raise RuntimeError('Command output limit exceeded')
        if result.returncode:
            raise RuntimeError('Command failed: '+str(argv))
        if cpu_used()-baseline_cpu>LIMITS['cpu_seconds']:
            raise RuntimeError('Aggregate CPU budget exceeded')
        return result.stdout

    try:
        # Declared output paths are cleared before execution, so stale results
        # cannot turn an incomplete run into a successful evidence record.
        for name in RESULTS:
            (ROOT/name).unlink(missing_ok=True)
        with TemporaryDirectory(prefix='bgs_rank_defect_') as build_directory:
            binary = str(Path(build_directory)/'next_order')
            execute([compiler,'-O2','-std=c++17','-Wall','-Wextra','-Wpedantic',
                     str(ROOT/'next_order.cpp'),'-o',binary])
            cpp = json.loads(execute([binary,'10']))
            assert cpp['all_passed']
            (ROOT/RESULTS[0]).write_text(json.dumps(cpp,indent=2)+'\n')
            for script in ('independent_checks.py','orbit_checks.py',
                           'resummation_checks.py','occupation_rank_checks.py'):
                execute([sys.executable,str(ROOT/script)])
        for name in RESULTS:
            assert json.loads((ROOT/name).read_text())['all_passed'],name
        symbolic = json.loads((ROOT/'wolfram_results.json').read_text())
        assert symbolic['submitted_code']==(ROOT/'symbolic_checks.wl').read_text()
        assert symbolic['parsed_result']['all_passed']
        assert all(symbolic['parsed_result']['checks'].values())
        assert all(pinned[name]==digest(name) for name in INPUTS)
    except subprocess.TimeoutExpired as exc:
        status,exit_status = 'timeout',1
        commands.append({'failure':str(exc)})
    except Exception as exc:
        status,exit_status = 'failed',1
        commands.append({'failure':str(exc)})

    (ROOT/'run_log.json').write_text(json.dumps({'subcommands':commands,
        'selected_cpu':selected_cpu,'cpu_seconds_observed':cpu_used()-baseline_cpu,
        'budget_note':'Wall time limits and Linux child CPU/address-space/affinity limits '
                      'were used; aggregate CPU checked between commands. Output limit '
                      'checked after each command. This is not a hard process-tree memory sum.'},indent=2)+'\n')
    output_records = [{'path':'run_log.json','sha256':digest('run_log.json'),'kind':'log'}]
    for name in RESULTS:
        if (ROOT/name).is_file():
            output_records.append({'path':name,'sha256':digest(name),'kind':'result'})
    manifest = {
        'schema_version':2,'claim_id':'finite-rank-and-occupation-checks-2026-10-10',
        'repository':{'path':'.','commit':'unavailable: standalone research outside BGS',
                      'dirty':False,'scope':'No Git repository was inspected or modified.'},
        'command':[sys.executable,'run_checks.py'],
        'environment':{'platform':platform.platform(),'software':[
            {'name':'Python','version':platform.python_version()},
            {'name':'g++','version':compiler_version}]},
        'mathematics':{
            'assertion_tested':'Finite cycle ranks, exact coefficients, active-defect identities, '
                               'word-orbit counts, inactive resummation, and occupation rank controls.',
            'coefficient_domain':'Exact integers, Fraction rationals, finite fields; '
                                 'Decimal saddle and seeded floating-point illustrations separately labelled.',
            'conventions':'x=N^(-1/2) for polynomials; original R distinct from restricted rank; '
                          'C++ d=0 mod 4, Python all d mod 4; word-orbit multiplicities are counted once.',
            'inputs':INPUTS,
            'bounds':{'cpp_n':[3,10],'primes':[3,5,7],'full_python_n':[3,6],
                      'truncated_python_p3_n':[7,8,9],'resummation_n':[0,8],
                      'occupation_exact_N':[2,3,4],'occupation_exact_n':[3,6],
                      'illustration_N':[256,1024,4096],'illustration_samples':40},
            'non_claims':['Finite computations do not prove the general mathematical theorems.',
                          'Numerical illustrations are not error certificates.',
                          'No formal verification in Lean, local BGS proof, or priority claim.']},
        'randomness':{'used':True,'generator':'Python random.Random (MT19937)',
                      'seed':20261010,'scope':'Large-N occupation illustrations only.'},
        'input_artifacts':[{'path':name,'sha256':pinned[name],'sha256_after':digest(name)}
                           for name in INPUTS],
        'execution_artifacts':INPUTS,'declared_results':RESULTS,
        'run':{'started_at':started,'runtime_seconds':time.monotonic()-start,
               'exit_status':exit_status,'status':status,'resource_limits':LIMITS,
               'missing_results':[name for name in RESULTS if not (ROOT/name).is_file()],
               'invalid_results':[]},
        'outputs':output_records,
        'checks':['Each regenerated result has all_passed=true.',
                  'Independent congruence and row-elimination methods agree.',
                  'All execution-input hashes unchanged.',
                  'Stored remote Wolfram code matches its receipt; remote evaluation not repeated.'],
        'result':'All declared finite checks passed.' if status=='completed' else 'Run incomplete; inspect run_log.json.',
        'residual_risks':['Original proofs require human review, not merely these finite checks.',
                          'The source ActiveDefect.lean is an uncompiled arithmetic draft.',
                          'Resource limits apply as documented in run_log.json, not as a process-tree guarantee.']}
    (ROOT/'computation_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'status':status,'runtime_seconds':manifest['run']['runtime_seconds'],
                      'declared_results':len(RESULTS),'manifest':'computation_manifest.json'}))
    return exit_status


if __name__=='__main__':
    raise SystemExit(main())
