"""A separate, bounded extension; previous executed files stay immutable."""
import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

target=Path(sys.argv[1])
binary=target.parent/'second_order_checker'
build=subprocess.run(['g++','-O2','-std=c++20','second_order.cpp','-o',str(binary)],capture_output=True,text=True)
assert build.returncode==0,build.stderr
requests=[(3,11),(13,12)]
request=str(len(requests))+'\n'+'\n'.join(f'{p} {m}' for p,m in requests)+'\n'
run=subprocess.run([str(binary.resolve())],input=request,capture_output=True,text=True)
assert run.returncode==0,run.stderr
rows=[json.loads(line) for line in run.stdout.splitlines()]
assert [(r['p'],r['m']) for r in rows]==requests
for row in rows:
    assert row['first12']==0
    row['variance_first_coefficient']='0'
    row['variance_second_coefficient']=str(Fraction(row['m']*row['second12'],12))
(target.parent/'engine_stderr.txt').write_text(run.stderr)
target.write_text(json.dumps({'status':'passed','records':rows,
                             'scope':'Two new finite coefficients only, not a stable-range theorem'},indent=2)+'\n')
print(json.dumps({'status':'passed','records':rows,'engine':run.stderr.strip()}))
