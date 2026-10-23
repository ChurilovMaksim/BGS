"""Exact minimal cores and their all-m embedding polynomial, one prime per run."""
import json
import math
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path


def multiply(poly,constant,linear):
    out=[F(0)]*(len(poly)+1)
    for i,x in enumerate(poly):out[i]+=constant*x;out[i+1]+=linear*x
    return out


def main(prime,destination):
    target=Path(destination)
    binary=target.parent/'open_second_order_checker'
    build=subprocess.run(['g++','-O2','-std=c++20','open_second_order.cpp','-o',str(binary)],capture_output=True,text=True)
    assert build.returncode==0,build.stderr
    run=subprocess.run([str(binary.resolve())],input=str(prime)+'\n',capture_output=True,text=True)
    assert run.returncode==0,run.stderr
    rows=[json.loads(line) for line in run.stdout.splitlines()]
    assert [r['q'] for r in rows]==list(range(3,13))
    polynomial=[F(0)]*13
    for row in rows:
        q=row['q']
        for edges,coefficient12 in enumerate(row['histogram12']):
            if edges==0 or coefficient12==0:continue
            term=[F(coefficient12,12*q*math.factorial(edges-1))]
            term=multiply(term,0,1)
            for j in range(edges-1):term=multiply(term,-q+edges-1-j,1)
            for j,x in enumerate(term):polynomial[j]+=x
    def embedding(m):
        total=F(0)
        for row in rows:
            q=row['q']
            if q>m:continue
            for edges,v in enumerate(row['histogram12']):
                factor=int(m==q) if edges==0 else F(m,q)*math.comb(m-q+edges-1,edges-1)
                total+=F(v,12)*factor
        return total
    previous=[]
    for path in ('second_order_run/result.json','second_order_extended_run/result.json'):
        previous.extend(json.loads(Path(path).read_text())['records'])
    controls=[]
    for row in previous:
        if row['p']!=prime:continue
        actual=F(row['m'])*embedding(row['m'])
        assert actual==F(row['variance_second_coefficient'])
        controls.append({'m':row['m'],'coefficient':str(actual)})
    # This is an exact polynomial construction, not extrapolation from samples.
    values=[]
    for m in range(17,31):
        value=sum((x*m**j for j,x in enumerate(polynomial)),F(0))
        assert value==embedding(m)
        values.append({'m':m,'normalized_coefficient':str(value)})
    (target.parent/'engine_stderr.txt').write_text(run.stderr)
    target.write_text(json.dumps({'status':'passed','p':prime,'minimal_core_histograms':rows,
                                 'stable_polynomial_coefficients':[str(x) for x in polynomial],
                                 'finite_overlap_controls':controls,'stable_evaluations':values,
                                 'scope':'All-m interpretation is conditional on the separate rank-four open-core bound proof; no all-order or Heisenberg inference'},indent=2)+'\n')
    print(json.dumps({'status':'passed','p':prime,'cycles':sum(r['coverage'] for r in rows),'engine':run.stderr.strip(),
                      'stable_polynomial':[str(x) for x in polynomial],'overlap':controls,
                      'nonzero_histograms':[{'q':r['q'],'by_common_edges':r['histogram12']} for r in rows if any(r['histogram12'])]}))


if __name__=='__main__':main(int(sys.argv[1]),sys.argv[2])
