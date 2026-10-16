#!/usr/bin/env python3
"""Exact finite CUE fourth cumulant checks via ordered set partitions.
This only verifies reference-ensemble algebra, not a deterministic BGS limit.
"""
from fractions import Fraction
from itertools import permutations
from collections import defaultdict

def partitions(seq):
    if not seq:
        yield ()
        return
    a=seq[0]
    for rest in partitions(seq[1:]):
        yield ((a,),)+rest
        for i in range(len(rest)):
            yield rest[:i]+((a,)+rest[i],)+rest[i+1:]

PARTS=tuple(tuple(p) for part in partitions(tuple(range(4))) for p in permutations(part))

def fourth(n,m,k):
    f=(m,-m,k,-k)
    answer=Fraction(0)
    for p in PARTS:
        steps=[sum(f[j] for j in block) for block in p]
        s=0; lo=0; hi=0
        for st in steps:
            s+=st;lo=min(lo,s);hi=max(hi,s)
        answer+=Fraction((-1)**(len(p)-1),len(p))*max(0,n-(hi-lo))
    return answer

def formula(n,m,k):
    return (2*max(0,n-max(m,k))-max(0,n-m-k)-max(0,n-abs(m-k)))

def main():
    count=0
    for n in range(1,16):
        for m in range(1,36):
            for k in range(1,36):
                exact=fourth(n,m,k)
                expected=formula(n,m,k)
                if exact != expected:
                    raise RuntimeError((n,m,k,exact,expected))
                count+=1
    print('reference cumulant checks:',count)
    print('ordered partitions:',len(PARTS))
    for m,k in [(11,3),(11,7),(11,11)]:
        hist=defaultdict(Fraction)
        by_l=defaultdict(lambda:defaultdict(Fraction))
        f=(m,-m,k,-k)
        for p in PARTS:
            s=0;lo=0;hi=0
            for block in p:
                s+=sum(f[j] for j in block);lo=min(lo,s);hi=max(hi,s)
            hist[hi-lo]+=Fraction((-1)**(len(p)-1),len(p))
            by_l[len(p)][hi-lo]+=Fraction((-1)**(len(p)-1),len(p))
        print(m,k,dict(hist),{j:dict(v) for j,v in by_l.items()})

if __name__=='__main__': main()
