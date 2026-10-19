"""Bounded exact extraction of the first two signed coefficients only."""
import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


def main(destination):
    target=Path(destination)
    binary=target.parent/'second_order_checker'
    compilation=subprocess.run(['g++','-O2','-std=c++20','second_order.cpp','-o',str(binary)],capture_output=True,text=True)
    assert compilation.returncode==0,compilation.stderr
    requests=[(p,m) for p in (3,5,13) for m in range(3,11)]+[(13,11)]
    request=str(len(requests))+'\n'+'\n'.join(f'{p} {m}' for p,m in requests)+'\n'
    run=subprocess.run([str(binary.resolve())],input=request,capture_output=True,text=True)
    assert run.returncode==0,run.stderr
    records=[json.loads(line) for line in run.stdout.splitlines()]
    assert [(r['p'],r['m']) for r in records]==requests
    previous=json.loads(Path('signed_run_v2/result.json').read_text())
    lookup={(r['p'],r['m']):[Fraction(x) for x in r['coefficients']] for r in previous['polynomials']}
    overlap=0
    for row in records:
        first=Fraction(row['m']*row['first12'],12)
        second=Fraction(row['m']*row['second12'],12)
        if (row['p'],row['m']) in lookup:
            expected=lookup[row['p'],row['m']]
            assert first==expected[1] and second==expected[2]
            overlap+=1
        if row['m']>=9:
            assert first==0
        row['variance_first_coefficient']=str(first)
        row['variance_second_coefficient']=str(second)
    (target.parent/'engine_stderr.txt').write_text(run.stderr)
    target.write_text(json.dumps({'status':'passed','records':records,'full_polynomial_overlap_checks':overlap,
                                 'scope':'Exact finite coefficients, without a large-m or Heisenberg extrapolation'},indent=2)+'\n')
    print(json.dumps({'status':'passed','records':len(records),'overlap':overlap,'engine':run.stderr.strip(),
                      'new_coefficients':[r for r in records if r['m']>=9]}))


if __name__=='__main__':main(sys.argv[1])
