"""Compile exact finite signed formula and check independent phase coefficients."""
import itertools
import json
import math
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path


def phase_cumulants(bound):
    f=[F(1,math.factorial(n)**2) for n in range(bound+1)]
    log=[F(0)]
    for n in range(1,bound+1):
        log.append(f[n]-sum(k*log[k]*f[n-k] for k in range(1,n))/n)
    a=[log[n]*math.factorial(n) for n in range(bound+1)]
    kappa=[a[n]*math.factorial(n) for n in range(bound+1)]
    assert all(x.denominator==1 for x in kappa)
    return a,[int(x) for x in kappa]


def partitions(n):
    if n==0:
        yield ()
        return
    def generate(labels,blocks):
        if len(labels)==n:
            yield tuple(labels)
            return
        for b in range(blocks+1):
            yield from generate(labels+[b],max(blocks,b+1))
    yield from generate([0],1)


def weight_checks(a):
    count=0
    for n in range(9):
        all_parts=list(partitions(n))
        representatives={}
        for occupation in all_parts:
            kind=tuple(sorted(occupation.count(k) for k in set(occupation)))
            representatives.setdefault(kind,occupation)
        assert len(representatives)==[1,1,2,3,5,7,11,15,22][n]
        for occupation in representatives.values():
            total=F(0)
            for pi in all_parts:
                if any(pi[i]==pi[j] and occupation[i]!=occupation[j]
                       for i in range(n) for j in range(i)):
                    continue
                sizes=[pi.count(k) for k in sorted(set(pi))]
                total+=math.prod(a[s] for s in sizes)
            target=F(1,math.prod(math.factorial(occupation.count(k)) for k in set(occupation)))
            assert total==target
            count+=1
    return count


def physical_moment(p,m):
    vertices=list(itertools.product(range(p),repeat=2))
    n=len(vertices)
    coefficients={}
    for word in itertools.product(range(n),repeat=m):
        occupancy=[0]*n
        for v in word:occupancy[v]+=1
        phase=sum(vertices[word[j]][0]*vertices[word[(j+1)%m]][1]
                  -vertices[word[j]][1]*vertices[word[(j+1)%m]][0] for j in range(m))%p
        coefficients.setdefault(tuple(occupancy),[0]*p)[phase]+=1
    total=[0]*p
    for v in coefficients.values():
        for i,x in enumerate(v):
            for j,y in enumerate(v):total[(i-j)%p]+=x*y
    reduced=[v-total[-1] for v in total[:-1]]
    assert not any(reduced[1:])
    return F(reduced[0],n**m)


def main(destination):
    target=Path(destination)
    target.parent.mkdir(exist_ok=True,parents=True)
    a,kappa=phase_cumulants(8)
    # Exact permutation symmetry reduces occupations to block-size types;
    # every possible refining partition is still explicitly summed.
    weight_count=weight_checks(a)
    binary=target.parent/'signed_rank_checker'
    compilation=subprocess.run(['g++','-O2','-std=c++20','signed_rank.cpp','-o',str(binary)],text=True,capture_output=True)
    assert compilation.returncode==0,compilation.stderr
    request='4\n3 8\n5 8\n7 6\n13 6\n'+' '.join(map(str,kappa[1:]))+'\n'
    run=subprocess.run([str(binary.resolve())],input=request,text=True,capture_output=True)
    assert run.returncode==0,run.stderr
    (target.parent/'rank_engine_stderr.txt').write_text(run.stderr)
    records=[]
    lookup={}
    first=json.loads(Path('core_run/result.json').read_text())
    first_lookup={(r['p'],r['m']):F(r['normalized_first_correction'])
                  for r in first['embedding_predictions']}
    for line in run.stdout.splitlines():
        row=json.loads(line)
        coefficients=[F(int(x),row['scale']) for x in row['scaled_coefficients']]
        assert coefficients[0]==row['m'] and coefficients[-1]==0
        assert coefficients[row['m']-1]==kappa[row['m']]
        if row['m']>=3:
            assert coefficients[1]==row['m']*first_lookup[row['p'],row['m']]
        row['coefficients']=[str(x) for x in coefficients[:-1]]
        records.append(row)
        lookup[row['p'],row['m']]=coefficients
    physical=[]
    for p,maximum in ((3,5),(5,4)):
        n=p*p
        for m in range(1,maximum+1):
            actual=physical_moment(p,m)
            polynomial=lookup[p,m]
            expected=sum(coefficient/n**degree for degree,coefficient in enumerate(polynomial))
            assert actual==expected
            physical.append({'N':n,'m':m,'exact_variance':str(actual)})
    negative=next(r for r in physical if r['N']==9 and r['m']==3)
    assert F(negative['exact_variance'])!=3+F(3,9)
    result={'status':'passed','a_n':[str(x) for x in a[1:]],'kappa_n':kappa[1:],
            'partition_weight_checks':weight_count,'polynomials':records,'physical_checks':physical,
            'negative_control':'Gaussian-only trace-three variance disagrees with circular phases',
            'scope':'Finite exact verification of the signed formula, not a Heisenberg-scale theorem'}
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','polynomials':len(records),'physical_checks':len(physical),
                      'partition_weight_checks':weight_count,'rank_engine':run.stderr.strip()}))


if __name__=='__main__':main(sys.argv[1])
