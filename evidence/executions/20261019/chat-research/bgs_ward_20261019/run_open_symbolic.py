import json
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path

target=Path(sys.argv[1]);binary=target.parent/'open_port_symbolic'
build=subprocess.run(['g++','-O2','-std=c++20','open_port_symbolic.cpp','-o',str(binary)],capture_output=True,text=True)
(target.parent/'compiler_stderr.txt').write_text(build.stderr);assert build.returncode==0,build.stderr
run=subprocess.run([str(binary.resolve())],capture_output=True,text=True)
(target.parent/'engine_stderr.txt').write_text(run.stderr);assert run.returncode==0,run.stderr
rows=[json.loads(line) for line in run.stdout.splitlines()]
old=json.loads(Path('dependencies/full_port_reference.json').read_text());ref={(r['q'],r['p']):r for r in old['rows']}
primes=(3,5,7,11,13,17,19,23,29);assert len(rows)==90
summary=[]
for p in primes:
    polys=[{} for _ in range(4)];symbolic=[[F(0)]*4 for _ in range(4)]
    for r in rows:
        if r['p']!=p:continue
        # Channel values already compared independently on three primes; compare the new fields to that complete coefficient list.
        reference=ref[r['q'],p if p in (3,5,13) else 13]
        assert r['primitive12']==reference['primitive12']
        weights=(F(1),F(-1,2),F(2,3),F(1,4))
        for c in range(4):
            assert sum(x*w for x,w in zip(r['connected_type_counts'][c],weights))==F(r['primitive12'][c],12)
            if r['primitive12'][c]:polys[c][r['q']]=F(r['primitive12'][c],12*r['q'])
            for t,count in enumerate(r['connected_type_counts'][c]):symbolic[c][t]+=F(count,r['q'])
    values=[sum(pol.values(),F(0)) for pol in polys]
    summary.append({'p':p,'value_at_one':[str(v) for v in values],
                    'symbolic_coefficients_in_order_1_a2_a3_a2sq':[[str(v) for v in row] for row in symbolic],
                    'polynomials':[{str(q):str(v) for q,v in pol.items()} for pol in polys]})
    assert all(v==0 for v in values)
data={'status':'completed_all_prime_symbolic_kernel','rows':rows,'summary':summary,
      'scope':'Exact finite open-kernel data and a connected-cluster refinement; universal gluing and a higher-order Ward identity require separate proofs.'}
target.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps({k:v for k,v in data.items() if k!='rows'}))
