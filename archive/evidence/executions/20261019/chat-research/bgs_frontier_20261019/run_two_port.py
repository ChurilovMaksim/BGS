import json
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path

target=Path(sys.argv[1]);folder=target.parent;binary=folder/'two_port_kernel'
build=subprocess.run(['g++','-O2','-std=c++20','two_port_kernel.cpp','-o',str(binary)],capture_output=True,text=True)
(folder/'compiler_stderr.txt').write_text(build.stderr);assert build.returncode==0,build.stderr
run=subprocess.run([str(binary.resolve())],capture_output=True,text=True)
(folder/'engine_stderr.txt').write_text(run.stderr);assert run.returncode==0,run.stderr
rows=[json.loads(line) for line in run.stdout.splitlines()]
assert len(rows)==100
expected={5:F(-2,3),6:F(-29,12),8:F(9,8),9:F(9,4),10:F(9,8)}
summaries=[]
for p in (3,5,7,11,13,17,19,23,29,31):
    pols=[{},{}]
    for row in rows:
        if row['p']!=p:continue
        for channel,numerator in enumerate(row['connected12']):
            if numerator:pols[channel][row['q']]=F(numerator,12*row['q'])
    assert pols[0]==expected,('closed connected P22 mismatch',p,pols[0])
    summaries.append({'p':p,'polynomials':[{str(q):str(a) for q,a in pol.items()} for pol in pols],
                      'values_at_one':[str(sum(pol.values(),F(0))) for pol in pols]})
data={'status':'passed_connected_two_port_kernel_and_closed_reference','rows':rows,'summary':summaries,
      'scope':'Exact open rank-four support enumeration through q=12. All-prime completeness uses the existing rank-four support and Pfaffian bounds.'}
target.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps({'status':data['status'],'summary':summaries}))
