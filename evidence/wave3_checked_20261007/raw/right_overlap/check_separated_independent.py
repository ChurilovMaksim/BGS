#!/usr/bin/env python3
"""Exact bounded checks of separated-proof algebra and combinatorics.

No asymptotic claims. Exhaustive binary necklaces through m=12; all fiber
counts in three finite bands; direct right cat Hessians r=1..16; S2 formula
in N=3,5 Gaussian-rational unitary fixtures. Uses explicit failures under -O.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path
import hashlib, json, sys, time
import sympy as s

start=time.monotonic()
checks=[]
def require(ok,name):
    if not bool(ok): raise RuntimeError(name)
    checks.append(name)
def compositions(total,length):
    if length==1:
        yield (total,)
    else:
        for n in range(total+1):
            for rest in compositions(total-n,length-1): yield (n,)+rest
def necklace(word):
    return min(word[i:]+word[:i] for i in range(len(word)))

for m in range(1,13):
    for j in range(1,m+1):
        slots=Counter()
        for chosen in combinations(range(m),j):
            a=set(chosen)
            slots[necklace(''.join('D' if i in a else 'T' for i in range(m)))]+=1
        gaps=Counter()
        for ns in compositions(m-j,j):
            word=''.join('D'+'T'*n for n in ns)
            gaps[necklace(word)]+=Fraction(m,j)
        require(slots==gaps,f'rooted once-counted cyclic coefficient m={m} j={j}')
        require(sum(gaps.values())==comb(m,j),f'normalization m={m} j={j}')

for lo,hi in ((1,5),(4,11),(10,21)):
    for j in range(1,lo+1):
        if j==1: direct=Fraction(1)
        else:
            direct=sum(Fraction(comb(total+j-2,j-2),comb(max(lo,total+j)-1,j-1))
                       for total in range(hi-j+1))
        expected=1+sum(Fraction(j-1,m-1) for m in range(lo+1,hi+1))
        require(direct==expected,f'decreasing weight endpoint count band={lo}:{hi} j={j}')

for r in range(1,17):
    xx=s.symbols(f'x0:{r}')
    c,d=s.symbols('c d')
    Q=lambda u,v: -(3*u*u-2*u*v+3*v*v)/8
    zz=[xx[0]+d]+list(xx[1:])+[xx[0]+c]
    phi=Q(xx[0]+c,xx[0])-Q(xx[0]+d,xx[0])+sum(Q(zz[k],zz[k+1]) for k in range(r))
    H=s.hessian(phi,xx)
    shift=s.zeros(r)
    for k in range(r): shift[k,(k+1)%r]=1
    expected=-s.Rational(3,2)*s.eye(r)+(shift+shift.T)/4
    require(all(s.expand(v)==0 for v in H-expected),f'direct right internal Hessian r={r}')
    vc=s.Matrix([s.diff(phi,x,c) for x in xx])
    vd=s.Matrix([s.diff(phi,x,d) for x in xx])
    ec=s.zeros(r,1); ed=s.zeros(r,1)
    if r==1: ec[0]=-1; cd=s.Rational(1,4)
    else:
        ec[0]=-s.Rational(5,4); ec[-1]+=s.Rational(1,4)
        ed[0]=-s.Rational(1,4); ed[1]+=s.Rational(1,4); cd=0
    require(vc==ec and vd==ed and s.diff(phi,c,d)==cd,f'direct right external vectors r={r}')
    Mr=s.Matrix([[3,4],[2,3]])**r
    schur=cd-(vc.T*H.inv()*vd)[0]
    require(schur==(Mr[0,0]+1)/(4*Mr[0,1]),f'direct right Schur value r={r}')

for n in (3,5):
    v=s.Matrix(range(1,n+1))
    H=s.eye(n)-2*v*v.T/(v.T*v)[0]
    U=s.simplify(H*s.diag(*[s.I**j for j in range(n)])*H)
    require(all(s.expand(z)==0 for z in U.conjugate().T*U-s.eye(n)),f'S2 fixture unitarity N={n}')
    D=s.zeros(n*n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    if (j-i)%n==(l-k)%n:
                        D[i*n+j,k*n+l]=U[i,k]*s.conjugate(U[j,l])
    lhs=s.simplify(sum(s.conjugate(z)*z for z in D))
    rhs=s.simplify(sum(abs(U[x,y])**2*abs(U[(x+c)%n,(y+c)%n])**2
                       for c in range(n) for x in range(n) for y in range(n)))
    require(lhs==rhs,f'ordinary superoperator Schatten-2 entry identity N={n}')
    delta=max(abs(z)**2 for z in U)
    require(lhs<=delta*n*n,f'flatness Schatten-2 bound N={n}')
    ident=s.Matrix([1 if i==j else 0 for i in range(n) for j in range(n)])
    require(all(s.expand(z)==0 for z in D*ident-ident) and
            all(s.expand(z)==0 for z in D.conjugate().T*ident-ident),
            f'identity reducing direction N={n}')

root=Path(__file__).resolve().parent
report={'status':'passed','python_optimization':sys.flags.optimize,'check_count':len(checks),
        'checks':checks,'arithmetic':'exact integers, rationals and Gaussian rationals; SymPy differentiation',
        'scope':'all binary insertion slot patterns m=1..12 and every j=1..m; three endpoint bands; right cat r=1..16; S2 and identity mode N=3,5. No analytic-limit or candidate-suite certificate.',
        'elapsed_seconds':time.monotonic()-start,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(root/('separated_checks_optimized.json' if sys.flags.optimize else 'separated_checks.json')).write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ('status','python_optimization','check_count','elapsed_seconds','scope')},indent=2))
