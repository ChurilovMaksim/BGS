"""Run the exact core computations in a new directory without changing certified runs."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

parser=argparse.ArgumentParser()
parser.add_argument('output',help='A new output directory; must not already exist')
parser.add_argument('--all',action='store_true',help='Also repeat all earlier exact controls')
parser.add_argument('--with-sampling',action='store_true',help='Repeat descriptive Monte Carlo data')
args=parser.parse_args()
root=Path(__file__).resolve().parent
out=Path(args.output).resolve()
out.mkdir(parents=True,exist_ok=False)
env=os.environ.copy()
env.update({'PYTHONDONTWRITEBYTECODE':'1','OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1'})
cases=[]
if args.all:
    cases.extend([
        ('cores',['verify_rank_two_cores.py']),
        ('signed',['verify_signed_rank_v2.py']),
        ('second',['verify_second_order.py']),
        ('second_extended',['verify_second_order_extended.py'])
    ])
cases.extend([
    ('open_p13',['verify_open_second_order.py','13']),
    ('universal',['verify_universal_open_second.py'])
])
if args.with_sampling:cases.append(('sampling',['sample_actual_form_factor.py']))
for name,arguments in cases:
    destination=out/name
    destination.mkdir()
    result=destination/'result.json'
    run=subprocess.run([sys.executable,*arguments,str(result)],cwd=root,env=env,text=True,capture_output=True,timeout=180)
    (destination/'stdout.txt').write_text(run.stdout)
    (destination/'stderr.txt').write_text(run.stderr)
    assert run.returncode==0,(name,run.returncode,run.stderr)
    record=json.loads(result.read_text())
    assert record['status']=='passed'
    if name=='universal':
        assert all(all(x=='0' for x in poly) for poly in record['stable_polynomials'].values())
    print(name,'passed',flush=True)
print('Reproduction completed. The original certified runs were read only.')
