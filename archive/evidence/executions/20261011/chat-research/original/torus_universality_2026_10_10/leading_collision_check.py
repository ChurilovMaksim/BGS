"""Exact coefficient of 1/N using the rank-two cycle classification.

The general classification is proved in collision_resummation.md, not by
this program. Higher corrections and growing-n estimates are not inferred.
"""
from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path
import datetime
import hashlib
import json
import platform
import time
from occupation_lift_check import add, gaussian, quadratic_difference, restrict_vertices, scale
from partition_form_factor import quotient, rank

ROOT=Path(__file__).resolve().parent


def orientations(cycle):
    where=cycle.index(0)
    forward=tuple(cycle[where:]+cycle[:where])
    return forward,(0,)+tuple(reversed(forward[1:]))


def zero_restrictions(matrix):
    active=[i for i,row in enumerate(matrix) if any(v%3 for v in row)]
    compact=[[matrix[i][j] for j in active] for i in active]
    pairs=[]
    for i,j in combinations(range(len(active)),2):
        pulled=restrict_vertices(compact,1,i,j)
        if all(v%3==0 for row in pulled for v in row):
            pairs.append((active[i],active[j]))
    return pairs


def qtrace(k,r):
    if k%2:
        return Fraction(1,3**(r*(k//2)))
    return Fraction(3**r,3**(r*(k//2)))


def leading_coefficient(b,n):
    c=len(b)
    core_size=3**c
    r=0 if c==1 else 2
    pair_sum=sum((n-l)*qtrace(l,r)*qtrace(n-l,r) for l in range(1,n))
    result=(Fraction(-n,2)*(comb(n,2)+pair_sum),Fraction(0))
    cycles=[]
    for l in range(2,n-1):
        cycles.append(([0]+list(reversed(range(1,l+1)))+list(range(l+1,n)),2))
    for l in range(3,n-2):
        swapped=list(range(n))
        swapped[0],swapped[l]=swapped[l],swapped[0]
        cycles.append((swapped,1))
    for cycle,expected_zero_pairs in cycles:
        subtotal=(Fraction(0),Fraction(0))
        for oriented in orientations(cycle):
            scalar=quadratic_difference(n,[[1]],oriented)
            assert rank(tuple(tuple(v%3 for v in row) for row in scalar))==2
            pairs=zero_restrictions(scalar)
            assert len(pairs)==expected_zero_pairs
            core=quadratic_difference(n,b,oriented)
            subtotal=add(subtotal,scale(gaussian(core),n*core_size))
            for u,v in pairs:
                subtotal=add(subtotal,scale(gaussian(restrict_vertices(core,c,u,v)),Fraction(-n,2)))
        # Each unordered pair of marked cuts/centers has two marked origins.
        result=add(result,scale(subtotal,Fraction(n,2)))
    assert result[1]==0,(b,n,result)
    return result[0]


def main():
    start=datetime.datetime.now(datetime.timezone.utc).isoformat()
    t=time.monotonic()
    names=['leading_collision_check.py','occupation_lift_check.py','partition_form_factor.py']
    inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in names}
    all_polynomials=json.loads((ROOT/'partition_form_factor_results.json').read_text())['cases']
    cases=[]
    for b in ([[1]],[[1,1],[0,1]]):
        for n in range(3,21):
            value=leading_coefficient(b,n)
            match=[x for x in all_polynomials if x['B0']==b and x['n']==n]
            if match:
                assert value==(3**len(b))*Fraction(match[0]['coefficients'].get('2','0'))
            if b==[[1]]:
                target=-9 if n==3 else (-24 if n==4 else -2*n*n)
                assert value==target,(b,n,value,target)
            conjectural=Fraction(-2*n*n,3**(n-3)) if n>=5 and len(b)==2 else None
            cases.append({'B0':b,'n':n,'coefficient_of_1_over_N':str(value),
                          'full_partition_polynomial_checked':bool(match),
                          'matches_observed_nonsymmetric_pattern':None if conjectural is None else value==conjectural})
    assert inputs=={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in names}
    output=ROOT/'leading_collision_results.json'
    output.write_text(json.dumps({'all_passed':True,'cases':cases,
       'warning':'Nonsymmetric pattern is a finite observation; symmetric formula has a separate proof.'},indent=2)+'\n')
    manifest={'schema_version':1,'claim_id':'leading_collision_finite_controls',
      'repository':{'commit':None,'dirty':True},'command':['python','leading_collision_check.py'],
      'environment':{'software':[{'name':'Python','version':platform.python_version()}],
                     'hardware':platform.machine(),'outer_wall_timeout_seconds':45},
      'mathematics':{'assertion_tested':'Leading 1/N coefficient from rank-two cycles and rank-zero pair restrictions, matching full partition calculations where available.',
                    'coefficient_domain':'Rational Eisenstein coordinates and exact F_3 ranks',
                    'conventions':'Coefficients in M_n, not M_n/n; cyclic-origin multiplicity n/2; oriented representations n.',
                    'inputs':[{'path':p,'sha256':h} for p,h in inputs.items()],
                    'bounds':{'n':[3,20],'cases':len(cases),'p':3},
                    'non_claims':['No uniform high-time bound or proof of the reported nonsymmetric pattern.']},
      'randomness':{'used':False},
      'run':{'started_at':start,'runtime_seconds':time.monotonic()-t,'exit_status':0},
      'outputs':[{'path':output.name,'sha256':hashlib.sha256(output.read_bytes()).hexdigest()}],
      'checks':['input hashes unchanged','all imaginary coefficients vanish',
                'all full-polynomial comparisons match','symmetric coefficients match proved formula'],
      'result':'All finite checks passed; nonsymmetric pattern reported as an observation.',
      'residual_risks':['Relies on rank-two classification outside the finite verification.','No uniform high-time bound.','External wall cap only.']}
    (ROOT/'leading_collision_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'passed':True,'seconds':manifest['run']['runtime_seconds'],
                      'pattern_failures':[x for x in cases if x['matches_observed_nonsymmetric_pattern'] is False],
                      'nonsymmetric_coefficients':[x['coefficient_of_1_over_N'] for x in cases if len(x['B0'])==2]}))


if __name__=='__main__':
    main()
