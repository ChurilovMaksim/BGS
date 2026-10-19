import json
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path

target=Path(sys.argv[1]);binary=target.parent/'port_kernel'
build=subprocess.run(['g++','-O2','-std=c++20','port_kernel.cpp','-o',str(binary)],capture_output=True,text=True)
(target.parent/'compiler_stderr.txt').write_text(build.stderr)
assert build.returncode==0,build.stderr
run=subprocess.run([str(binary.resolve())],capture_output=True,text=True)
(target.parent/'engine_stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
rows=[json.loads(line) for line in run.stdout.splitlines()]
old=json.loads(Path('dependencies/primitive_reference.json').read_text())
reference={(r['q'],r['p']):r for r in old['rows']}
assert len(rows)==30
summary=[]
for p in (3,5,13):
    selected=[r for r in rows if r['p']==p]
    assert sum(r['coverage'] for r in selected)==43954712
    polys=[{},{}]
    for r in selected:
        ref=reference[r['q'],p]
        assert sum(r['all12'])==ref['all12']
        assert sum(r['primitive12'])==ref['primitive12']
        for channel in (0,1):
            if r['primitive12'][channel]:polys[channel][r['q']]=F(r['primitive12'][channel],12*r['q'])
    values=[sum(v.values(),F(0)) for v in polys]
    assert sum(values)==0
    summary.append({'p':p,'P_identity':{str(q):str(v) for q,v in polys[0].items()},
                    'P_cycle':{str(q):str(v) for q,v in polys[1].items()},
                    'value_at_one':[str(v) for v in values],
                    'derivative_at_one':[str(sum(q*v for q,v in pol.items())) for pol in polys],
                    'tensor_zero':all(v==0 for v in values)})
data={'status':'completed_exact_channel_split','cycles':43954712,'rows':rows,'summary':summary,
      'scope':'Exact boundary-permutation decomposition of the previously complete h=2,e=3 primitive table. No higher-defect conclusion inferred.'}
target.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({k:v for k,v in data.items() if k!='rows'}))
