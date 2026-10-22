#!/usr/bin/env python3
"""Exact rational Schur/Kostka compression of Haar occupation projection."""
import functools,itertools,json,math,time
from fractions import Fraction
from collections import Counter
import sympy as s


@functools.lru_cache(None)
def partitions(n,cap=None):
    if n==0:return ((),)
    if cap is None:cap=n
    return tuple((a,)+p for a in range(min(cap,n),0,-1) for p in partitions(n-a,a))


def hooks(lam):
    for i,row in enumerate(lam):
        for j in range(row):
            yield i,j,row-j+sum(v>j for v in lam[i+1:])


def dimensions(lam,n):
    f=Fraction(math.factorial(sum(lam)),1)
    dim=Fraction(1)
    for i,j,h in hooks(lam):
        f/=h;dim*=Fraction(n+j-i,h)
    assert f.denominator==dim.denominator==1
    return int(f),int(dim)


@functools.lru_cache(None)
def strips(lam,k):
    if k<0:return ()
    ranges=[range(lam[i+1] if i+1<len(lam) else 0,lam[i]+1) for i in range(len(lam))]
    out=[]
    for nu in itertools.product(*ranges):
        if sum(lam)-sum(nu)==k:
            out.append(tuple(x for x in nu if x))
    return tuple(out)


@functools.lru_cache(None)
def kostka(lam,content):
    if not content:return int(not lam)
    if sum(lam)!=sum(content):return 0
    return sum(kostka(nu,content[:-1]) for nu in strips(lam,content[-1]))


def orbit_count(mu,n):
    out=math.factorial(n)//math.factorial(n-len(mu))
    for count in Counter(mu).values():out//=math.factorial(count)
    return out


def matrix(n,m):
    ps=[x for x in partitions(m) if len(x)<=n]
    dims=[dimensions(x,n) for x in ps]
    K=s.Matrix([[kostka(lam,mu) for mu in ps] for lam in ps])
    weights=[s.Rational(orbit_count(mu,n)*math.prod(math.factorial(x) for x in mu),math.factorial(m)) for mu in ps]
    S=K*s.diag(*weights)*K.T
    B=s.diag(*[s.Rational(f,d) for f,d in dims])*S
    f=s.Matrix([a for a,b in dims]);d=s.Matrix([b for a,b in dims])
    P=f*d.T/s.Integer(n)**m
    assert B*f==f and d.T*B==d.T and P*P==P
    assert sum(a*b for a,b in dims)==n**m
    # Each Schur dimension is the content-weight sum of its Kostka numbers.
    assert K*s.Matrix([orbit_count(mu,n) for mu in ps])==d
    return ps,B,P


def evaluate(n,m):
    ps,B,P=matrix(n,m)
    C=s.eye(len(ps))-B+P
    inv=C.inv(method='DM')
    answer=s.factor(s.trace(inv)-len(ps))
    trh=s.factor(s.trace(B)-1)
    bound=s.factor(s.Rational(n+1,n)*trh)
    assert answer>=trh and answer<=bound
    return dict(N=n,m=m,partition_dimension=len(ps),A_exact=str(answer),A=float(answer),
                sum_H_trace_exact=str(trh),sum_H_trace=float(trh),
                norm_based_upper_exact=str(bound),
                matrix_trace=str(s.trace(B)))


if __name__=='__main__':
    start=time.perf_counter()
    pairs=[(n,m) for n in [3,5,7,9] for m in range(2,11)]
    rows=[]
    for n,m in pairs:
        r=evaluate(n,m);rows.append(r)
    print(json.dumps({'arithmetic':'exact SymPy rational matrices and integer horizontal-strip Kostka recursion',
                      'rows':rows,'runtime_seconds':time.perf_counter()-start},indent=2))
