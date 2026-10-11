"""Reproduce all new collision controls with per-job wall limits."""
from pathlib import Path
import datetime
import hashlib
import json
import platform
import subprocess
import sys
import tempfile
import time

ROOT=Path(__file__).resolve().parent


def main():
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    t=time.monotonic()
    sources=['cycle_rank_check.cpp','occupation_lift_check.py',
             'partition_form_factor.py','leading_collision_check.py','run_collision_checks.py']
    before={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources}
    commands=[]
    with tempfile.TemporaryDirectory(prefix='bgs_collision_') as directory:
        binary=str(Path(directory)/'cycle_rank_check')
        jobs=[['g++','-std=c++20','-O2','-Wall','-Wextra','cycle_rank_check.cpp','-o',binary],
              [binary],*[ [sys.executable,name] for name in sources[1:4] ]]
        for number,command in enumerate(jobs):
            result=subprocess.run(command,cwd=ROOT,capture_output=True,text=True,timeout=45)
            commands.append(command)
            (ROOT/f'collision_check_{number}.log').write_text(result.stdout+result.stderr)
            assert result.returncode==0,(command,result.stderr)
            if number==1:
                data=json.loads(result.stdout)
                assert data['all_passed']
                (ROOT/'cycle_rank_results.json').write_text(json.dumps(data,indent=2)+'\n')
    assert before=={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources}
    result_names=['cycle_rank_results.json','occupation_lift_results.json',
                  'partition_form_factor_results.json','leading_collision_results.json']
    manifest={'schema_version':1,'claim_id':'collision_controls_combined',
      'repository':{'commit':None,'dirty':True},'command':[sys.executable,'run_collision_checks.py'],
      'environment':{'software':[{'name':'Python','version':platform.python_version()},
                                {'name':'g++','version':subprocess.check_output(['g++','--version'],text=True).splitlines()[0]}],
                     'hardware':platform.machine(),'wall_timeout_seconds_per_job':45,
                     'subprocess_commands':commands},
      'mathematics':{'assertion_tested':'Exact modular cycle ranks, occupation lift, partition polynomial resummation and leading correction coefficients.',
                    'coefficient_domain':'Integer modular arithmetic; exact rational Eisenstein coordinates',
                    'conventions':'Individual scripts record ranges and rejected observations.',
                    'inputs':[{'path':p,'sha256':h} for p,h in before.items()],
                    'bounds':{'cycle_n_max':10,'occupation_n_max':7,'full_partition_n_max':6,'leading_n_max':20},
                    'non_claims':['Finite checks do not prove uniform universality or BGS.','Lean is not executed.']},
      'randomness':{'used':False,'generator':'','seed':None},
      'run':{'started_at':started,'runtime_seconds':time.monotonic()-t,'exit_status':0},
      'outputs':[{'path':name,'sha256':hashlib.sha256((ROOT/name).read_bytes()).hexdigest()} for name in result_names],
      'checks':['all processes exit zero','all input hashes unchanged','all exact asserted checks pass'],
      'result':'All collision controls reproduced successfully; false stronger rank/pattern claims remain recorded as rejected observations.',
      'residual_risks':['No aggregate CPU or memory certificate.','Per-job wall cap only.','Theory is independently audited, not formally verified.']}
    (ROOT/'collision_computation_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'all_passed':True,'runtime_seconds':manifest['run']['runtime_seconds']}))


if __name__=='__main__':
    main()
