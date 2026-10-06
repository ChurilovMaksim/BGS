#!/usr/bin/env python3
"""Exact finite tests for the spectral covering and unfolding inequalities.

All scalar arithmetic below is rational; no spectral or probabilistic limit
is inferred from the finite examples. The proof is locality_robustness.md.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import random


def segments(left: Q, right: Q) -> list[tuple[Q,Q]]:
    if right < left:
        raise ValueError('invalid oriented interval')
    if right-left >= 1:
        return [(Q(0),Q(1))]
    offset=left.numerator//left.denominator
    left,right=left-offset,right-offset
    return [(left,right)] if right<=1 else [(left,Q(1)),(Q(0),right-1)]


def union_length(arcs: list[tuple[Q,Q]]) -> Q:
    pieces=sorted(p for a,b in arcs for p in segments(a,b))
    if not pieces:
        return Q(0)
    left,right=pieces[0];total=Q(0)
    for a,b in pieces[1:]:
        if a<=right:
            right=max(right,b)
        else:
            total+=right-left
            left,right=a,b
    return total+right-left


def check(points: list[Q], arcs: list[tuple[Q,Q]], length: Q) -> dict:
    points=sorted(x%1 for x in points)
    d,k=len(points),len(arcs)
    total=sum((b-a for a,b in arcs),Q(0))
    assert 0<=total<1 and d>=1 and 0<length<d
    pieces=[p for a,b in arcs for p in segments(a,b)]
    assert all(any(a<=x<=b for a,b in pieces) for x in points)
    gaps=[d*(b-a) for a,b in zip(points,points[1:]+[points[0]+1])]
    assert sum(gaps)==d
    rows=[]
    for x in (Q(1,3),Q(1),Q(4)):
        long=sum(s>x for s in gaps)
        pairs=sum(i!=j and d*min(abs(a-b),1-abs(a-b))<=x
                  for i,a in enumerate(points) for j,b in enumerate(points))
        assert Q(long,d)<=Q(k,d)+total/x
        assert Q(pairs,d)>=1/(Q(k,d)+total/x)-1
        rows.append({'threshold':str(x),'long_gaps':long,'ordered_pairs':pairs})
    hit=union_length([(x-length/d,x) for x in points])
    assert hit<=k*length/d+total
    return {'D':d,'K':k,'cover_length':str(total),
            'window_length':str(length),'exact_hit_probability':str(hit),
            'cover_exceeds_mean_spacing':total*d>1,'threshold_checks':rows}


def unfolding(weights: list[int]):
    m=len(weights);total=sum(weights)
    prefix=[0]
    for w in weights:
        if w<=0: raise ValueError('strictly positive slopes required in this test')
        prefix.append(prefix[-1]+w)
    def f(x: Q) -> Q:
        offset=x.numerator//x.denominator
        r=x-offset
        j=int(m*r)
        return offset+(prefix[j]+(m*r-j)*weights[j])/total
    return f,Q(m*max(weights),total)


def report() -> dict:
    rng=random.Random(20260905)
    rows=[]
    transformed=[]
    for k in (3,5,9):
        for width_factor in (Q(1,1000),Q(1,20),Q(1,4)):
            for trial in range(3):
                points=[];arcs=[]
                for j in range(k):
                    center=Q(j,k)+Q(rng.randrange(-2,3),20*k)
                    width=width_factor/k
                    arcs.append((center-width,center+width))
                    count=1+rng.randrange(2,12)
                    for _ in range(count):
                        points.append(center+width*Q(rng.randrange(-8,9),8))
                rows.append(check(points,arcs,Q(7,4)))
                f,lip=unfolding([1+rng.randrange(1,8) for _ in range(11)])
                image_arcs=[(f(a),f(b)) for a,b in arcs]
                image_cover=sum((b-a for a,b in image_arcs),Q(0))
                assert image_cover<=lip*sum((b-a for a,b in arcs),Q(0))
                assert f(Q(7,13)+1)==f(Q(7,13))+1
                r=check([f(x) for x in points],image_arcs,Q(7,4))
                r['Lipschitz_constant']=str(lip)
                transformed.append(r)
    assert any(r['cover_exceeds_mean_spacing'] for r in rows)
    return {'producer':'computations/verification/locality_robustness.py',
            'status':'PASS','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'Exact finite rational covering, pair-count and origin-probability tests. No asymptotic theorem or interval-certified matrix calculation is inferred.',
            'seed':20260905,'base_cases':len(rows),'unfolded_cases':len(transformed),
            'thresholds_per_case':3,'origin_coverage_checks':len(rows)+len(transformed),
            'checks':rows,'unfolded_checks':transformed}


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    text=json.dumps(report(),indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding='utf-8')
    else: print(text,end='')

if __name__=='__main__': main()
