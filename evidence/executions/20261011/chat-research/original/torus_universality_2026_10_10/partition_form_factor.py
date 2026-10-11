"""Exact collision resummation, not a diagonal approximation.

For B=B0 direct-sum I_t over F_3 and t a multiple of four, compute M_n
as a polynomial in x=L^{-1/2}, L=3^t. Coefficients are exact rationals
in Q(omega_3), with their imaginary parts checked to vanish.
This program does not extrapolate a finite-n polynomial to n~N.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from math import comb, factorial
from pathlib import Path
import datetime
import hashlib
import json
import platform
import time
from occupation_lift_check import add, gaussian, quadratic_difference, scale

ROOT=Path(__file__).resolve().parent


def block_coefficients(n):
    a=[Fraction(0)]*(n+1)
    for m in range(1,n+1):
        a[m]=Fraction(1,factorial(m))-sum(
            comb(m-1,k-1)*a[k]*Fraction(1,factorial(m-k))
            for k in range(1,m))
    return a


def partitions(n):
    """Restricted-growth labels enumerate each set partition exactly once."""
    labels=[0]*n
    def walk(position,largest):
        if position==n:
            sizes=[labels.count(k) for k in range(largest+1)]
            yield tuple(labels),tuple(sizes)
            return
        for value in range(largest+2):
            labels[position]=value
            yield from walk(position+1,max(largest,value))
    yield from walk(1,0)


def quotient(a,d,labels):
    size=(max(labels)+1)*d
    out=[[0]*size for _ in range(size)]
    mapping=[labels[i//d]*d+i%d for i in range(len(a))]
    for i,row in enumerate(a):
        for j,value in enumerate(row):
            out[mapping[i]][mapping[j]]+=value
    return tuple(tuple(v%3 for v in row) for row in out)


@lru_cache(maxsize=16384)
def rank(matrix):
    a=[list(row) for row in matrix]
    size=len(a)
    r=0
    for col in range(size):
        pivot=next((i for i in range(r,size) if a[i][col]%3),None)
        if pivot is None:
            continue
        a[r],a[pivot]=a[pivot],a[r]
        inverse=a[r][col]%3
        a[r]=[(v*inverse)%3 for v in a[r]]
        for i in range(r+1,size):
            coefficient=a[i][col]%3
            if coefficient:
                a[i]=[(u-coefficient*v)%3 for u,v in zip(a[i],a[r])]
        r+=1
        if r==size:
            break
    return r


@lru_cache(maxsize=16384)
def cached_gaussian(matrix):
    return gaussian(matrix)


def polynomial(b,n):
    a=block_coefficients(n)
    ps=[]
    for labels,sizes in partitions(n):
        coefficient=Fraction(1)
        for size in sizes:
            coefficient*=a[size]
        ps.append((labels,n-len(sizes),coefficient))
    c=len(b)
    core_size=3**c
    result={}
    diagrams=0
    for tail in permutations(range(1,n)):
        cycle=(0,)+tail
        scalar=quadratic_difference(n,[[1]],cycle)
        core=quadratic_difference(n,b,cycle)
        for labels,h,coefficient in ps:
            exponent=2*h+rank(quotient(scalar,1,labels))
            factor=Fraction(n,core_size**h)*coefficient
            term=scale(cached_gaussian(quotient(core,c,labels)),factor)
            result[exponent]=add(result.get(exponent,(Fraction(0),Fraction(0))),term)
            diagrams+=1
    result={k:v for k,v in result.items() if v!=(0,0)}
    assert all(v[1]==0 for v in result.values()),(b,n,result)
    r=0 if c==1 else 2
    qtrace=Fraction(3**r,3**(r*(n//2))) if n%2==0 else Fraction(1,3**(r*(n//2)))
    assert result[0][0]==n*(1+qtrace),(b,n,result[0],qtrace)
    if n==3:
        assert result=={0:(n*(1+qtrace),0),2:(Fraction(-9,core_size),0),
                        4:(Fraction(4,core_size**2),0)},result
    return {'B0':b,'c':c,'p':3,'n':n,'identity_coordinates_multiple_of':4,
            'variable':'x=L^(-1/2)','diagram_count':diagrams,
            'coefficients':{str(k):str(v[0]) for k,v in sorted(result.items())},
            'value_at_L_1':str(sum(v[0] for v in result.values()))}


def main():
    start=datetime.datetime.now(datetime.timezone.utc).isoformat()
    t=time.monotonic()
    names=['partition_form_factor.py','occupation_lift_check.py']
    inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in names}
    cases=[]
    direct=json.loads((ROOT/'occupation_lift_results.json').read_text())
    for b in ([[1]],[[1,1],[0,1]]):
        for n in range(3,7):
            case=polynomial(b,n)
            match=[x for x in direct['cases'] if x['B']==b and x['n']==n]
            if match:
                assert Fraction(case['value_at_L_1'])==Fraction(match[0]['M_n'])
            case['direct_word_L_1_checked']=bool(match)
            cases.append(case)
    assert inputs=={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in names}
    data={'all_passed':True,'block_coefficients':list(map(str,block_coefficients(8)[1:])),
          'cases':cases,'scope':'Exact finite-n formula for all t divisible by 4; no uniform high-time claim.'}
    output=ROOT/'partition_form_factor_results.json'
    output.write_text(json.dumps(data,indent=2)+'\n')
    manifest={'schema_version':1,'claim_id':'exact_partition_form_factor_controls',
      'repository':{'commit':None,'dirty':True},'command':['python','partition_form_factor.py'],
      'environment':{'software':[{'name':'Python','version':platform.python_version()}],
                     'hardware':platform.machine(),'outer_wall_timeout_seconds':45},
      'mathematics':{'assertion_tested':'Exact partition-weight collision resummation; rational polynomials for finite-field Fourier scattering; comparison with direct words at L=1 and known third moment.',
                    'coefficient_domain':'Exact modular ranks and rational Eisenstein coordinates',
                    'conventions':'Block EGF log(sum z^m/(m!)^2); p=3; identity-coordinate count divisible by 4; polynomial variable L^(-1/2).',
                    'inputs':[{'path':p,'sha256':h} for p,h in inputs.items()],
                    'bounds':{'n':[3,6],'cases':len(cases),'diagrams':sum(x['diagram_count'] for x in cases)},
                    'non_claims':['Finite polynomials do not imply a bound uniform in n.']},
      'randomness':{'used':False},
      'run':{'started_at':start,'runtime_seconds':time.monotonic()-t,'exit_status':0},
      'outputs':[{'path':output.name,'sha256':hashlib.sha256(output.read_bytes()).hexdigest()}],
      'checks':['input hashes unchanged','all nonreal coefficients cancel',
                'constant term equals n(1+Tr Q^n)','third moment polynomial matches independent formula',
                'all available direct occupation values match'],
      'result':'All eight polynomials computed exactly; finite checks passed.',
      'residual_risks':['No bounds uniform in n obtained from these polynomials.','Identity block length restricted modulo four for polynomial convention.','No formal or BGS proof.','External wall cap, no aggregate CPU/memory certificate.']}
    (ROOT/'partition_form_factor_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'passed':True,'seconds':manifest['run']['runtime_seconds'],
                      'diagrams':manifest['mathematics']['bounds']['diagrams'],
                      'leading_coefficients':[{k:v for k,v in x.items() if k in ('B0','n','coefficients')} for x in cases]}))


if __name__=='__main__':
    main()
