#!/usr/bin/env python3
"""Rebuild the appendix's covariance table by permutation Gram inversion."""
from collections import Counter
from fractions import Fraction as F
from itertools import permutations
from functools import lru_cache
import json, platform, sys


@lru_cache(None)
def perms(s):return tuple(permutations(range(s)))
def compose(p,q):return tuple(p[q[i]] for i in range(len(p)))
def inv(p):return tuple(p.index(i) for i in range(len(p)))
def cycles(p):
    unseen=set(range(len(p)));c=0
    while unseen:
        c+=1;j=next(iter(unseen))
        while j in unseen:unseen.remove(j);j=p[j]
    return c


@lru_cache(None)
def weingarten(n,s):
    ps=perms(s);d=len(ps)
    a=[[F(n**cycles(compose(inv(p),q))) for q in ps]+[F(p==ps[0])] for p in ps]
    # Solve the exact permutation Gram system, without using the supplied character table.
    for j in range(d):
        p=next(i for i in range(j,d) if a[i][j])
        a[p],a[j]=a[j],a[p]
        pivot=a[j][j];a[j]=[v/pivot for v in a[j]]
        for i in range(d):
            if i!=j:
                v=a[i][j]
                if v:a[i]=[x-v*y for x,y in zip(a[i],a[j])]
    w={p:a[i][-1] for i,p in enumerate(ps)}
    assert sum(F(n**cycles(p))*w[p] for p in ps)==1
    return w


# A diagram is (unconjugated edges, conjugated edges), summed over all its vertex labels.
DIAGRAMS={
 'A':(((0,0),),((0,0),)),
 'F':(((0,1),(0,1)),((0,1),(0,1))),
 'H':(((0,0),(0,0)),((0,0),(0,0))),
 'C':(((0,1),(1,0)),((0,1),(1,0))),
 'A2':(((0,0),(1,1)),((0,0),(1,1))),
 'Q':(((0,0),(1,1)),((0,1),(1,0))),
 'Qb':(((0,1),(1,0)),((0,0),(1,1)))
}


@lru_cache(None)
def moment_terms(names):
    u=[];v=[];nv=0
    for name in names:
        a,b=DIAGRAMS[name];k=1+max(x for edge in a+b for x in edge)
        u.extend((i+nv,j+nv) for i,j in a)
        v.extend((i+nv,j+nv) for i,j in b);nv+=k
    s=len(u);counts=Counter()
    for sigma in perms(s):
        for tau in perms(s):
            parents=list(range(nv))
            def find(x):
                while parents[x]!=x:x=parents[x]
                return x
            def union(a,b):parents[find(a)]=find(b)
            for a in range(s):
                union(u[a][0],v[sigma[a]][0]);union(u[a][1],v[tau[a]][1])
            classes=len({find(j) for j in range(nv)})
            counts[(compose(tau,inv(sigma)),classes)]+=1
    return s,counts


@lru_cache(None)
def moment(n,names):
    s,terms=moment_terms(names);w=weingarten(n,s)
    return sum(F(count*n**classes)*w[p] for (p,classes),count in terms.items())


def means(n):return {'A':F(1),'F':F(2*n,n+1),'H':F(2,n+1),'C':F(n+2,n+1),'A2':F(n+2,n+1),'Q':F(1,n+1),'Qb':F(1,n+1)}


def main():
    cases=[]
    for n in (4,5,7,10):
        mu=means(n)
        for a in DIAGRAMS:assert moment(n,(a,))==mu[a],(n,a)
        D=n*(n+1)**2*(n+2)*(n+3)
        numer=[
          [4*n*(n-1)*(n+2),4*(n-1)*(n+2),4*n*(n+2),4*n*(n+2),4*n*(n+2)],
          [0,20*n*n+20*n+8,12*n*n+12*n+4,8*n**3+44*n*n+36*n+4,12*n*n+12*n+4],
          [0,0,2*n**3+16*n*n+18*n+6,4*n**3+24*n*n+24*n+6,6*n*n+4*n],
          [0,0,0,4*n**4+34*n**3+92*n*n+66*n+6,4*n**3+22*n*n+16*n],
          [0,0,0,0,n**3+12*n*n+15*n+6]]
        names=['F','H','C','A2','Q']
        for i,a in enumerate(names):
            for j in range(i,5):
                b=names[j]
                aa=['Q','Qb'] if a=='Q' else [a]
                bb=['Q','Qb'] if b=='Q' else [b]
                expectation=sum(moment(n,(x,y)) for x in aa for y in bb)/len(aa)/len(bb)
                covariance=expectation-mu[a]*mu[b]
                assert covariance==F(numer[i][j],D),(n,a,b,covariance,F(numer[i][j],D))
        expected={'F':F(0),'H':F(4,(n+1)*(n+2)),
                  'C':F(2,(n+1)*(n+2)),'A2':F(2*(n+3),(n+1)*(n+2)),'Q':F(2,(n+1)*(n+2))}
        for b,val in expected.items():
            assert moment(n,('A',b))-mu['A']*mu[b]==val
        imaginary=(2*moment(n,('Q','Qb'))-moment(n,('Q','Q'))-moment(n,('Qb','Qb')))/4
        assert imaginary==F(1,(n+1)*(n+2))
        assert moment(n,('A','A'))-1==F(1,n+1)
        cases.append({'N':n,'covariance_entries_verified':15,'degree_one_cross_covariances':5,
                      'imaginary_Q_variance_exact':str(imaginary)})
    out={'status':'passed','python':platform.python_version(),'cases':cases,
         'method':'Exact inversion of permutation Gram matrices through tensor degree four, followed by vertex-label union-find sums.',
         'non_claims':['The reverse-transfer coefficients DR14--DR16 are separate formulas and are not established by this covariance check.',
                       'No control of a growing harmonic remainder.']}
    with open(sys.argv[1],'w') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps({'status':'passed','N':[r['N'] for r in cases],'table_entries':60}))


if __name__=='__main__':main()
