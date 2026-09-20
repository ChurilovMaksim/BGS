"""Exact Pell orbit tests. No eigenvalue simulation or asymptotic inference.

The all-K theorem is proved in sparse_orbit_theorem.md. These checks
independently verify its integer identities and try to falsify its
two-frequency consequence, including composite moduli and periods.
"""
import json
from math import gcd
from random import Random


def pell(k):
    a,b=1,0
    for _ in range(k):a,b=a+2*b,a+b
    return a,b


def mul(a,b,n=None):
    c=tuple(tuple(sum(a[i][h]*b[h][j] for h in range(2))
                  for j in range(2)) for i in range(2))
    return c if n is None else tuple(tuple(x%n for x in row) for row in c)


def power(k,n=None):
    a=((3,4),(2,3));out=((1,0),(0,1))
    while k:
        if k&1:out=mul(out,a,n)
        a=mul(a,a,n);k//=2
    return out


def act(a,v,n=None):
    w=tuple(sum(a[i][j]*v[j] for j in range(2)) for i in range(2))
    return w if n is None else tuple(x%n for x in w)


def divisors(k):return [d for d in range(1,k+1) if k%d==0]


def orbit_period(v,k,n,powers):
    for d in divisors(k):
        if act(powers[d],v,n)==v:return d
    raise AssertionError('Pell period failed')


def run():
    rng=Random(20260918)
    identity_cases=0
    for k in range(3,204,2):
        n,f=pell(k)
        assert n*n-2*f*f==-1
        sk=power(k)
        assert sk==((1+2*n*n,4*n*f),(2*n*f,1+2*n*n))
        for d in divisors(k):
            nd,fd=pell(d)
            assert n%nd==0
            sd=power(d)
            assert sd==((1+2*nd*nd,4*nd*fd),(2*nd*fd,1+2*nd*nd))
            ratio=n//nd
            for _ in range(4):
                v=(rng.randrange(n),rng.randrange(n))
                assert (act(sd,v,n)==v)==(v[0]%ratio==v[1]%ratio==0)
                w=(ratio*rng.randrange(nd),ratio*rng.randrange(nd))
                assert act(sd,w,n)==w
            identity_cases+=1

    # Small norm labels, all relative shifts. Search below and above the
    # sufficient threshold; report exceptions instead of suppressing them.
    vectors=[(a,b) for a in range(-3,4) for b in range(-3,4)
             if 0<abs(a)+abs(b)<=3]
    rows=[]
    for k in (9,15,21,25,27,33,35,39,45,49,63,99,105,193,195,197,199,201,203):
        n,_=pell(k);powers={d:power(d,n) for d in divisors(k)}
        short=0;nonzero=0
        for d in range(k):
            sd=power(d,n)
            for w in vectors:
                sw=act(sd,w,n)
                for v in vectors:
                    r=((v[0]+sw[0])%n,(v[1]+sw[1])%n)
                    if r==(0,0):continue
                    nonzero+=1
                    short+=orbit_period(r,k,n,powers)<k
        if k>=39:assert short==0
        rows.append(dict(K=k,nonzero_pairs=nonzero,short_orbit_pairs=short))

    # Independently stress the entire l1 radius used by the frozen symbol.
    radius9=[(a,b) for a in range(-9,10) for b in range(-9,10)
             if 0<abs(a)+abs(b)<=9]
    stress=0
    for k in (39,45,63,99,105,195,201,203):
        n,_=pell(k);powers={d:power(d,n) for d in divisors(k)}
        for _ in range(5000):
            v=rng.choice(radius9);w=rng.choice(radius9);d=rng.randrange(k)
            sw=act(power(d,n),w,n)
            r=((v[0]+sw[0])%n,(v[1]+sw[1])%n)
            if r!=(0,0):assert orbit_period(r,k,n,powers)==k
            stress+=1

    sharp=[]
    for k in (9,15,21,25,27,33,35,39,49,99,105,195,201,203):
        p=next(d for d in divisors(k) if d>1);ell=k//p
        n,_=pell(k);r=[0,0]
        for j in range(p):
            v=act(power(j*ell,n),(1,0),n)
            r=[(r[h]+v[h])%n for h in range(2)]
        r=tuple(r);assert r!=(0,0)
        period=orbit_period(r,k,n,{d:power(d,n) for d in divisors(k)})
        assert period==ell
        sharp.append(dict(K=k,terms=p,period=period,label=list(r)))

    assert pell(39)[0]>270**6
    return dict(identity_divisor_cases=identity_cases,pair_rows=rows,
                radius9_random_stress_cases=stress,sharp_examples=sharp,
                threshold_certificate=dict(N39=pell(39)[0],rhs=270**6),
                scope='Exact finite checks; the separate proof supplies all-K quantifiers')


if __name__=='__main__':print(json.dumps(run(),indent=2))
