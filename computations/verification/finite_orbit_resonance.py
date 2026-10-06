#!/usr/bin/env python3
"""Exact finite checks for finite_orbit_resonance_rigidity.md.

No finite sweep proves the analytic theorem. In the separation regression,
all cross-pair gaps m>=0 are covered for the explicitly listed target gaps:
a proved recurrence-growth stopping criterion replaces a guessed m cutoff.
Arithmetic is Python integers, including Gaussian-integer Fourier coefficients.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
import hashlib
import json
import platform
import random
import time
from collections import defaultdict
from pathlib import Path

Vec = tuple[int, int]
Mat = tuple[tuple[int, int], tuple[int, int]]
GI = tuple[int, int]

def mv(a: Mat, v: Vec) -> Vec:
    return (a[0][0]*v[0]+a[0][1]*v[1], a[1][0]*v[0]+a[1][1]*v[1])

def neg(v: Vec) -> Vec:
    return (-v[0], -v[1])

def add(u: Vec, v: Vec) -> Vec:
    return (u[0]+v[0], u[1]+v[1])

def scale(n: int, v: Vec) -> Vec:
    return (n*v[0], n*v[1])

def det(u: Vec, v: Vec) -> int:
    return u[0]*v[1]-u[1]*v[0]

def inv(a: Mat) -> Mat:
    assert a[0][0]*a[1][1]-a[0][1]*a[1][0] == 1
    return ((a[1][1], -a[0][1]), (-a[1][0], a[0][0]))

def qp(a: Mat, v: Vec) -> int:
    return det(v, mv(a, v))

def step(a: Mat, v: Vec, n: int) -> Vec:
    b = a if n >= 0 else inv(a)
    for _ in range(abs(n)):
        v = mv(b, v)
    return v

def canonical(a: Mat, v: Vec, signed: bool = False) -> Vec:
    """Exact minimum of (Euclidean norm squared,x,y) on one orbit.

    The squared norm along A^n v is alpha*lambda^(2n)+beta*lambda^(-2n)
    plus a constant, alpha,beta>0, even for negative trace. Strict convexity
    makes a discrete local minimum global. Equal neighboring minima use lex.
    """
    if v == (0, 0):
        return v
    ai = inv(a)
    key = lambda z: (z[0]*z[0]+z[1]*z[1], z[0], z[1])
    for _ in range(10000):
        w = min((mv(a, v), v, mv(ai, v)), key=key)
        if w == v:
            if signed:
                return min(v, canonical(a, neg(v)), key=key)
            return v
        v = w
    raise RuntimeError('orbit reduction cap reached; no result certified')

def seeds_in_box(a: Mat, radius: int) -> list[Vec]:
    return sorted({canonical(a, (x,y), True)
        for x in range(-radius, radius+1)
        for y in range(-radius, radius+1) if x or y})

def cross_candidates(a: Mat, u: Vec, v: Vec, bound: int):
    """Yield (m,A^m v,b_m) until no later |b_m| can be <= bound.

    b_m=Q(u+A^m v)-Q(u)-Q(v), c_m=s^m b_m.
    c_(m+2)=T*c_(m+1)-c_m, T=|tr A|>=3.
    Once 0<|c_previous|<=|c_current| with the same sign, all subsequent
    magnitudes grow strictly. The omitted current and later terms exceed bound.
    """
    tr = a[0][0]+a[1][1]
    s = 1 if tr > 0 else -1
    prev = None
    vv = v
    qsum = qp(a,u)+qp(a,v)
    for m in range(10000):
        b = qp(a, add(u,vv))-qsum
        c = (s**m)*b
        if prev is not None and prev*c > 0 and abs(c) >= abs(prev) and abs(c) > bound:
            return
        yield m, vv, b
        prev = c
        vv = mv(a,vv)
    raise RuntimeError('recurrence cap reached; no exhaustive gap claim')

def separation_case(a: Mat, radius: int, nmax: int) -> dict:
    seeds = seeds_in_box(a, radius)
    targets = defaultdict(list)
    for i,u in enumerate(seeds):
        for j,v in enumerate(seeds):
            av = v
            for n in range(1,nmax+1):
                av = mv(a,av)
                for eps in (-1,1):
                    w = add(u,scale(eps,av))
                    if w == (0,0):
                        continue
                    targets[qp(a,w)].append((i,j,n,eps,canonical(a,w,True)))
    bad = set()
    invariant_hits = orbit_hits = tested = 0
    max_m = 0
    for k,u in enumerate(seeds):
        for l,v in enumerate(seeds):
            qsum = qp(a,u)+qp(a,v)
            bound = max(abs(q-qsum) for q in targets)
            for m,av,b in cross_candidates(a,u,v,bound):
                max_m = max(max_m,m)
                for delta in (-1,1):
                    tested += 1
                    q = qsum+delta*b
                    hits = targets.get(q,())
                    if not hits:
                        continue
                    w = add(u,scale(delta,av))
                    if w == (0,0):
                        continue
                    cw = canonical(a,w,True)
                    for i,j,n,eps,target in hits:
                        invariant_hits += 1
                        if cw != target:
                            continue
                        orbit_hits += 1
                        if not (i==k and j==l and m==n and eps==delta):
                            bad.add((i,j,n,eps,k,l,m,delta))
    bad_gaps = sorted({t[2] for t in bad})
    assert not any(n > nmax//2 for n in bad_gaps), (a,bad_gaps)
    return dict(A=a, radius=radius, seeds=seeds, target_gaps=[1,nmax],
        channel_types='all ordered families, both signs',
        cross_gaps='all m>=0 by certified recurrence stopping', max_m=max_m,
        cross_patterns=tested, invariant_hits=invariant_hits, orbit_hits=orbit_hits,
        exceptional_gaps=bad_gaps, exceptional_patterns=len(bad),
        exception_examples=sorted(bad)[:8],
        nonclaim='No computed cutoff is asserted uniformly in A or seed families.')

def giadd(a: GI,b: GI) -> GI:
    return (a[0]+b[0],a[1]+b[1])

def gimul(a: GI,b: GI) -> GI:
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])

def conj(a: GI) -> GI:
    return (a[0],-a[1])

def bracket(a: Mat, g: dict[Vec,GI], r: int) -> dict[Vec,GI]:
    """Return exact coefficients of {g,C^r g}/(4*pi^2)=h_r/pi."""
    out: dict[Vec,GI] = defaultdict(lambda:(0,0))
    transformed = [(step(a,v,r),cv) for v,cv in g.items()]
    for u,cu in g.items():
        for av,cv in transformed:
            z = add(u,av)
            d = -det(u,av)
            out[z] = giadd(out[z],scale(d,gimul(cu,cv)))
    return {z:c for z,c in out.items() if c != (0,0)}

def channel_case(a: Mat, seed: int) -> dict:
    rng = random.Random(seed)
    vs = seeds_in_box(a,1)[:3]
    coefficients = []
    g = {}
    for v in vs:
        c = {j:(rng.randint(-3,3),rng.randint(-3,3)) for j in range(-4,5)}
        coefficients.append(c)
        for j,cj in c.items():
            w = step(a,v,j)
            g[w]=cj
            g[neg(w)]=conj(cj)
    comparisons = nonzero = 0
    for r in (1,2,4):
        h=bracket(a,g,r)
        sums = defaultdict(lambda:(0,0))
        for w,c in h.items():
            sums[canonical(a,w)] = giadd(sums[canonical(a,w)],c)
        for i,u in enumerate(vs):
            for j,v in enumerate(vs):
                ci,cj=coefficients[i],coefficients[j]
                def corr(n,eps):
                    out=(0,0)
                    for t,cit in ci.items():
                        cjt=cj.get(t+n,(0,0))
                        out=giadd(out,gimul(cit,conj(cjt) if eps==-1 else cjt))
                    return out
                for eps in (-1,1):
                    for n in range(6,14):
                        av=step(a,v,n)
                        target=canonical(a,add(u,scale(eps,av)))
                        expected=scale(-eps*det(u,av),add(corr(n-r,eps),neg(corr(n+r,eps))))
                        actual=sums.get(target,(0,0))
                        assert actual == expected, (a,i,j,r,eps,n,actual,expected)
                        comparisons += 1
                        nonzero += expected != (0,0)
    return dict(A=a,seeds=vs,seed=seed,temporal_support=[-4,4],
        lags=[1,2,4],tested_gaps=[6,13],channel_types='all ordered families, both signs',
        exact_comparisons=comparisons,nonzero_comparisons=nonzero,
        arithmetic='Gaussian integers')

def scalar_and_negative_controls() -> dict:
    identities = 0
    for q in range(-9,10):
        for x in range(-9,10):
            for y in range(-9,10):
                if x+y == 2*q and x*y == q*q:
                    assert x == y == q
                identities += 1
    # PP*=1 does NOT make P Laurent polynomial without growth restriction.
    # Formal exponent: (z-z^-1)+(z^-1-z)=0. This is an algebraic negative control.
    return dict(real_root_degeneracy_integer_cases=identities,
        all_pass_negative_control='P(z)=exp(z-z^-1), PP*=1; growth O(r), not O(log^2 r)',
        polynomial_negative_control='g constant gives every bracket zero; excluded by contract')

def main() -> None:
    p=argparse.ArgumentParser()
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--quick',action='store_true')
    args=p.parse_args()
    start=time.monotonic()
    bases=[((2,1),(1,1)),((3,2),(4,3)),((0,-1),(1,4)),((1,3),(1,4))]
    mats=bases+[tuple(tuple(-x for x in row) for row in a) for a in bases]
    if args.quick:
        mats=mats[:2]
    sep=[separation_case(a,2,24) for a in mats]
    chans=[channel_case(a,20260922+i) for i,a in enumerate(mats)]
    result=dict(status='passed finite assertions, not a machine proof of analytic theorem',
        base_revision='39d4e01ae6a6b3eb472ab30266b708ca71a70a16',
        python=platform.python_version(),platform=platform.platform(),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        separation=sep,channels=chans,controls=scalar_and_negative_controls(),
        duration_seconds=time.monotonic()-start)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status=result['status'],matrices=len(mats),
        exact_channel_comparisons=sum(c['exact_comparisons'] for c in chans),
        cross_patterns=sum(s['cross_patterns'] for s in sep),
        largest_exceptional_gap=max((max(s['exceptional_gaps'],default=0) for s in sep)),
        duration_seconds=result['duration_seconds']),indent=2))

if __name__ == '__main__':
    main()
