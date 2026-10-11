"""Independent exact controls of the positive occupation lift over F_3.

Two evaluations are compared: direct word grouping, and diagonalization of
finite-field quadratic forms followed by exact Eisenstein arithmetic.
Finite checks support debugging; they do not replace the general proof.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations, product
from math import comb, factorial
from pathlib import Path
import datetime
import hashlib
import json
import platform
import time

ROOT=Path(__file__).resolve().parent


def multiply(z,w):
    """(a+b omega)(c+d omega), with omega^2+omega+1=0."""
    a,b=z
    c,d=w
    return a*c-b*d,a*d+b*c-b*d


def add(z,w):
    return z[0]+w[0],z[1]+w[1]


def scale(z,t):
    return t*z[0],t*z[1]


def gaussian(matrix):
    """Normalized F_3 quadratic Gaussian sum, exactly in Q(omega)."""
    a=[[x%3 for x in row] for row in matrix]
    z=Fraction(1),Fraction(0)
    while a:
        size=len(a)
        pivot=next((i for i in range(size) if a[i][i]),None)
        if pivot is None:
            edge=next(((i,j) for i in range(size) for j in range(i+1,size)
                       if a[i][j]),None)
            if edge is None:
                break
            i,j=edge
            # Congruence replacing e_i by e_i+e_j makes its diagonal nonzero.
            a[i]=[(a[i][k]+a[j][k])%3 for k in range(size)]
            for k in range(size):
                a[k][i]=(a[k][i]+a[k][j])%3
            pivot=i
        order=[pivot]+[i for i in range(size) if i!=pivot]
        a=[[a[i][j] for j in order] for i in order]
        coefficient=a[0][0]
        assert coefficient in (1,2)
        factor=(Fraction(1,3),Fraction(2,3))
        if coefficient==2:
            factor=scale(factor,-1)
        z=multiply(z,factor)
        inverse=coefficient  # 1^{-1}=1 and 2^{-1}=2 in F_3.
        a=[[(a[i][j]-a[i][0]*inverse*a[0][j])%3
            for j in range(1,size)] for i in range(1,size)]
    return z


def quadratic_difference(n,b,cycle):
    d=len(b)
    size=n*d
    a=[[0]*size for _ in range(size)]
    for vertices,sign in ((list(range(n)),1),(list(cycle),-1)):
        for k in range(n):
            i,j=vertices[k],vertices[(k+1)%n]
            for u in range(d):
                for v in range(d):
                    x,y=i*d+u,j*d+v
                    coefficient=sign*b[u][v]*2  # 1/2=2 in F_3.
                    a[x][y]+=coefficient
                    a[y][x]+=coefficient
    return a


def restrict_vertices(a,d,u,v):
    """Pull back along x_v=x_u, without counting normalization 1/N."""
    size=len(a)
    kept=[i for i in range(size) if not v*d<=i<(v+1)*d]
    index={old:new for new,old in enumerate(kept)}
    mapping=[index[u*d+(i-v*d)] if v*d<=i<(v+1)*d else index[i]
             for i in range(size)]
    result=[[0]*len(kept) for _ in kept]
    for i in range(size):
        for j in range(size):
            result[mapping[i]][mapping[j]]+=a[i][j]
    return result


def norm_squared(counts):
    a,b,c=counts
    return a*a+b*b+c*c-a*b-a*c-b*c


def one_case(b,n):
    d=len(b)
    points=list(product(range(3),repeat=d))
    N=len(points)
    edge=[[sum(x[u]*b[u][v]*y[v] for u in range(d) for v in range(d))%3
           for y in points] for x in points]
    groups=defaultdict(lambda:[0,0,0])
    for word in product(range(N),repeat=n):
        occupation=[0]*N
        for x in word:
            occupation[x]+=1
        exponent=sum(edge[word[k]][word[(k+1)%n]] for k in range(n))%3
        groups[tuple(occupation)][exponent]+=1
    moment=lift=collision=0
    for occupation,counts in groups.items():
        amplitude=norm_squared(counts)
        multiplicity=1
        collisions=0
        for number in occupation:
            multiplicity*=factorial(number)
            collisions+=comb(number,2)
        moment+=amplitude
        lift+=multiplicity*amplitude
        collision+=multiplicity*collisions*amplitude
    denominator=N**n
    moment=Fraction(moment,denominator)
    lift=Fraction(lift,denominator)
    collision=Fraction(collision,denominator)
    assert 0<=lift-moment<=collision
    by_cycles=(Fraction(0),Fraction(0))
    by_collision=(Fraction(0),Fraction(0))
    for tail in permutations(range(1,n)):
        cycle=(0,)+tail
        a=quadratic_difference(n,b,cycle)
        by_cycles=add(by_cycles,scale(gaussian(a),n))
        for u in range(n):
            for v in range(u+1,n):
                pulled=restrict_vertices(a,d,u,v)
                by_collision=add(by_collision,scale(gaussian(pulled),Fraction(n,N)))
    assert by_cycles==(lift,0),(b,n,by_cycles,lift)
    assert by_collision==(collision,0),(b,n,by_collision,collision)
    return {'p':3,'d':d,'N':N,'B':b,'n':n,'words':N**n,
            'occupation_classes':len(groups),'M_n':str(moment),'S_n':str(lift),
            'positive_collision_majorant':str(collision),
            'lift_difference':str(lift-moment),'quadratic_evaluation_matches':True}


def main():
    began=datetime.datetime.now(datetime.timezone.utc).isoformat()
    t=time.monotonic()
    source=Path(__file__)
    before=hashlib.sha256(source.read_bytes()).hexdigest()
    cases=[]
    for b,ns in (([[1]],range(3,8)),([[1,0],[0,1]],range(3,6)),
                 ([[1,1],[0,1]],range(3,6))):
        for n in ns:
            cases.append(one_case(b,n))
    assert hashlib.sha256(source.read_bytes()).hexdigest()==before
    result={'all_passed':True,'coefficient_domain':'Exact integers and Fraction in Q(omega_3)',
            'cases':cases}
    output=ROOT/'occupation_lift_results.json'
    output.write_text(json.dumps(result,indent=2)+'\n')
    manifest={'schema_version':1,'claim_id':'occupation_lift_exact_controls',
      'repository':{'commit':None,'dirty':True},
      'command':['python','occupation_lift_check.py'],
      'environment':{'software':[{'name':'Python','version':platform.python_version()}],
                     'hardware':platform.machine(),'outer_wall_timeout_seconds':45},
      'mathematics':{'assertion_tested':'Positive occupation lift and aggregate collision comparison; independent exact finite-field Gaussian evaluation of all oriented cycles.',
                    'coefficient_domain':'Integer counts; rational Eisenstein coordinates',
                    'conventions':'omega^2+omega+1=0; Gaussian normalization over F_3; x_v=x_u costs 1/N.',
                    'inputs':[{'path':source.name,'sha256':before}],
                    'bounds':{'cases':len(cases),'maximum_words':max(x['words'] for x in cases),'p':3,'d':[1,2],'n':[3,7]},
                    'non_claims':['Finite agreement is not a general proof or a BGS result.']},
      'randomness':{'used':False},
      'run':{'started_at':began,'runtime_seconds':time.monotonic()-t,'exit_status':0},
      'outputs':[{'path':output.name,'sha256':hashlib.sha256(output.read_bytes()).hexdigest()}],
      'checks':['input hash unchanged','nonnegative occupation norm sums',
                '0<=S-M<=aggregate collision sum','direct words and quadratic diagonalization agree exactly'],
      'result':'All 11 finite cases agree exactly in Q(omega_3).',
      'residual_risks':['Finite cases do not prove the asymptotic theorem.','No n comparable to N universality test.','No CPU or memory certificate; external wall cap only.']}
    (ROOT/'occupation_lift_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'passed':True,'cases':len(cases),'seconds':manifest['run']['runtime_seconds']}))


if __name__=='__main__':
    main()
