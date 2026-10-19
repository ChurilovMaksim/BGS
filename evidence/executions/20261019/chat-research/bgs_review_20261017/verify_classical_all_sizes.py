#!/usr/bin/env python3
"""Exact nonnormal stochastic-complement, Green and return-clock controls."""
from fractions import Fraction as F
from itertools import combinations
import json, platform, sys


def eye(n):
    return [[F(i==j) for j in range(n)] for i in range(n)]


def transpose(a):
    return list(map(list,zip(*a)))


def add(a,b,scale=1):
    return [[x+scale*y for x,y in zip(r,s)] for r,s in zip(a,b)]


def mul(a,b):
    return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]


def sub(a,rows,cols):
    return [[a[i][j] for j in cols] for i in rows]


def inverse(a):
    n=len(a)
    x=[row[:]+erow for row,erow in zip(a,eye(n))]
    for j in range(n):
        pivot=next(i for i in range(j,n) if x[i][j])
        x[j],x[pivot]=x[pivot],x[j]
        scale=x[j][j]
        x[j]=[z/scale for z in x[j]]
        for i in range(n):
            if i!=j:
                scale=x[i][j]
                x[i]=[z-scale*w for z,w in zip(x[i],x[j])]
    return [row[n:] for row in x]


def make_case(n):
    # Convex combination of two permutation matrices, generally nonnormal.
    q=[[F(0) for j in range(n)] for i in range(n)]
    perm=list(range(n));perm[0],perm[1]=perm[1],perm[0]
    for i in range(n):
        q[i][(i+1)%n]+=F(1,3)
        q[i][perm[i]]+=F(2,3)
    alpha=F(2,5)
    P=[[F(1,n)*(1-alpha)+alpha*q[i][j] for j in range(n)] for i in range(n)]
    return P,alpha


def checks(n):
    p,eps=make_case(n)
    J=[[F(1,n)]*n for _ in range(n)]
    M=add(inverse(add(add(eye(n),p,-1),J)),eye(n),-1)
    C=n*max(z for row in p for z in row)
    B=C+(C-1)/(1-eps)
    assert max(abs(z) for row in M for z in row)<=B/n
    nonnormal=mul(p,transpose(p))!=mul(transpose(p),p)
    cases=0
    maximum_error=F(0)
    maximum_clock=F(0)
    for m in range(1,n+1):
        Q=add(eye(m),[[F(1,m)]*m for _ in range(m)],-1)
        for A in combinations(range(n),m):
            E=[i for i in range(n) if i not in A]
            K=sub(p,A,A)
            h=[F(0)]*m
            if E:
                inv=inverse(add(eye(len(E)),sub(p,E,E),-1))
                K=add(K,mul(mul(sub(p,A,E),inv),sub(p,E,A)))
                h=[row[0] for row in mul(mul(sub(p,A,E),inv),[[F(1)] for _ in E])]
            assert all(z>=0 for row in K for z in row)
            assert all(sum(row)==1 for row in K)
            assert all(sum(col)==1 for col in zip(*K))
            Jm=[[F(1,m)]*m for _ in range(m)]
            Mc=add(inverse(add(add(eye(m),K,-1),Jm)),eye(m),-1)
            assert Mc==mul(mul(Q,sub(M,A,A)),Q)
            assert add(K,Jm,-1)==mul(mul(Q,sub(M,A,A)),add(eye(m),K,-1))
            err=max(abs(K[i][j]-F(1,m)) for i in range(m) for j in range(m))
            assert err<=4*B/n
            assert sum(h)==n-m
            clock=max(abs(x-F(n-m,m)) for x in h)
            assert clock<=2*B
            maximum_error=max(maximum_error,err)
            maximum_clock=max(maximum_clock,clock)
            cases+=1
    return {'N':n,'all_nonempty_subsets':cases,'nonnormal':nonnormal,
            'spectral_gap_upper_bound_exact':str(eps),'C_exact':str(C),
            'max_entry_error_exact':str(maximum_error),
            'max_clock_deviation_exact':str(maximum_clock)}


def main():
    rows=[checks(n) for n in range(3,9)]
    assert any(x['nonnormal'] for x in rows)
    result={'status':'passed','python':platform.python_version(),'cases':rows,
            'non_claims':['Finite controls are not an asymptotic proof.',
                          'No equality between classical and quantum transmission is claimed.']}
    with open(sys.argv[1],'w') as f:
        json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'status':'passed','subsets':sum(r['all_nonempty_subsets'] for r in rows),
                      'N':[3,8]},sort_keys=True))


if __name__=='__main__':main()
