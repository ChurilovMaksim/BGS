import json
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path

target=Path(sys.argv[1]);binary=target.parent/'open_port_kernel'
build=subprocess.run(['g++','-O2','-std=c++20','open_port_kernel.cpp','-o',str(binary)],capture_output=True,text=True)
(target.parent/'compiler_stderr.txt').write_text(build.stderr);assert build.returncode==0,build.stderr
run=subprocess.run([str(binary.resolve())],capture_output=True,text=True)
(target.parent/'engine_stderr.txt').write_text(run.stderr);assert run.returncode==0,run.stderr
rows=[json.loads(line) for line in run.stdout.splitlines()]
old=json.loads(Path('dependencies/closed_port_reference.json').read_text())
ref={(r['q'],r['p']):r for r in old['rows']}
assert len(rows)==30
summary=[]
for p in (3,5,13):
    polys=[{} for _ in range(4)]
    for r in rows:
        if r['p']!=p:continue
        for c in (0,1):
            assert r['all12'][c]==ref[r['q'],p]['all12'][c]
            assert r['primitive12'][c]==ref[r['q'],p]['primitive12'][c]
        for c in range(4):
            if r['primitive12'][c]:polys[c][r['q']]=F(r['primitive12'][c],12*r['q'])
    summary.append({'p':p,'channels':['identity','rho','rho_inverse','all_transpositions'],
                    'polynomials':[{str(q):str(v) for q,v in pol.items()} for pol in polys],
                    'value_at_one':[str(sum(pol.values(),F(0))) for pol in polys],
                    'derivative_at_one':[str(sum(q*v for q,v in pol.items())) for pol in polys]})
data={'status':'completed_full_open_channel_split','rows':rows,'summary':summary,
      'scope':'All enumerated open path covers at q<=12, fields 3,5,13. Completeness in all q is a separate mathematical obligation.'}
target.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps({k:v for k,v in data.items() if k!='rows'}))
