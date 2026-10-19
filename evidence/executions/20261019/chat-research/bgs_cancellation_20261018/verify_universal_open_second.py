"""Prime-complete open cores: the large-prime transfer is proved separately."""
import json
import math
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path
from verify_open_second_order import multiply

target=Path(sys.argv[1])
binary=target.parent/'universal_open_second_checker'
build=subprocess.run(['g++','-O2','-std=c++20','universal_open_second.cpp','-o',str(binary)],capture_output=True,text=True)
assert build.returncode==0,build.stderr
run=subprocess.run([str(binary.resolve())],capture_output=True,text=True)
assert run.returncode==0,run.stderr
rows=[json.loads(line) for line in run.stdout.splitlines()]
primes=(3,5,7,11,13,17,19,23,29)
assert [(r['q'],r['p']) for r in rows]==[(q,p) for q in range(3,13) for p in primes]
reference={r['q']:r['histogram12'] for r in json.loads(Path('open_second_order_p13_run/result.json').read_text())['minimal_core_histograms']}
for row in rows:
    if row['p']==13:assert row['histogram12'][1:]==reference[row['q']][1:]
    assert row['histogram12'][0]==0
    assert row['histogram12'][-1]=={3:8,4:9}.get(row['q'],0)
polynomials={}
for p in primes:
    poly=[F(0)]*13
    for row in rows:
        if row['p']!=p:continue
        q=row['q']
        for edges,v in enumerate(row['histogram12']):
            if edges==0 or v==0:continue
            term=[F(v,12*q*math.factorial(edges-1))]
            term=multiply(term,0,1)
            for j in range(edges-1):term=multiply(term,-q+edges-1-j,1)
            for j,x in enumerate(term):poly[j]+=x
    polynomials[str(p)]=[str(x) for x in poly]
(target.parent/'engine_stderr.txt').write_text(run.stderr)
target.write_text(json.dumps({'status':'passed','primes':primes,'open_core_histograms':rows,
                             'stable_polynomials':polynomials,
                             'scope':'Finite exact open cores. All-odd-prime and all-m interpretation requires the separate support and Pfaffian proofs.'},indent=2)+'\n')
print(json.dumps({'status':'passed','primes':primes,'cycle_types_visited':sum(r['coverage'] for r in rows if r['p']==3),
                  'stable_polynomials':polynomials,'engine':run.stderr.strip()}))
