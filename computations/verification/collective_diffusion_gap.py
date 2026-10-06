#!/usr/bin/env python3
"""Exact finite controls for FM-019; no analytic gap or BGS certification.

Raw coordinate commutators are compared with total-Weyl blocks over
Z[zeta_N]. Gauges use Q[zeta_(2N)], keeping every wrap sign. Projection
eigenvectors, kernel compression and finite Hardy matrices are rational.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
import json
from pathlib import Path

from frozen_operator_transfer_coercivity import cyclotomic, remainder

Poly = dict[int, F]


def add(*ps: Poly) -> Poly:
    r: dict[int, F] = defaultdict(F)
    for p in ps:
        for k, v in p.items():
            r[k] += v
    return {k: v for k, v in r.items() if v}


def scale(p: Poly, x: F | int) -> Poly:
    assert isinstance(x, (F, int)), type(x)
    assert all(isinstance(v, F) for v in p.values())
    return {k: v*x for k, v in p.items() if v*x}


def mul(p: Poly, q: Poly, modulus: int) -> Poly:
    r: dict[int, F] = defaultdict(F)
    for a, x in p.items():
        for b, y in q.items():
            r[(a+b) % modulus] += x*y
    return {k: v for k, v in r.items() if v}


def phase(k: int, modulus: int) -> Poly:
    return {k % modulus: F(1)}


@lru_cache(maxsize=None)
def canonical(modulus: int, items: tuple[tuple[int, F], ...]) -> tuple[F, ...]:
    v = [F(0)]*modulus
    for k, x in items:
        v[k % modulus] += x
    return tuple(remainder(v, list(cyclotomic(modulus))))


def equal(p: Poly, q: Poly, modulus: int) -> bool:
    r = add(p, scale(q, -1))
    return canonical(modulus, tuple(sorted(r.items()))) == (0,)


def comm_coefficient(t: int, n: int) -> Poly:
    h = (n+1)//2
    return add(phase(h*t, n), scale(phase(-h*t, n), -1))


def coefficients(a: int, c: int, n: int) -> tuple[Poly, Poly]:
    x, y = comm_coefficient(a,n), comm_coefficient(c,n)
    return add(scale(mul(x,x,n),-1),scale(mul(y,y,n),-1)), scale(mul(x,y,n),-1)


def q_coordinate_checks(counts: Counter) -> None:
    for n in [3,5,7]:
        h=(n+1)//2
        for a in range(n):
            for c in range(n):
                diag, off = coefficients(a,c,n)
                for x in range(n):
                    for y in range(n):
                        diff=add(phase(x,n),phase(y,n),scale(phase(x+a,n),-1),scale(phase(y+c,n),-1))
                        conjugate={(-k)%n:v for k,v in diff.items()}
                        actual=mul(diff,conjugate,n)
                        relative=x-y+h*(a-c)
                        predicted=add(diag,mul(off,add(phase(relative,n),phase(-relative,n)),n))
                        assert equal(actual,predicted,n), (n,a,c,x,y)
                        counts['q_coordinate_coefficients']+=1
                # Multiplication by the unchanged Weyl entry makes this test
                # valid for every pair of b,d; count their actual coverage.
                counts['q_full_basis_coordinate_coverage']+=n**4


def pair_matrix(n: int, v: tuple[int,int], w: tuple[int,int]) -> dict[tuple[int,int,int,int],Poly]:
    a,b=v; c,d=w; h=(n+1)//2
    return {(x,y,(x+a)%n,(y+c)%n):phase(b*(x+h*a)+d*(y+h*c),n)
            for x in range(n) for y in range(n)}


def collective_comm(matrix: dict, step: int, n: int) -> dict:
    result={}
    for (x,y,u,v),p in matrix.items():
        terms=[(((x-step)%n,y,u,v),1),((x,(y-step)%n,u,v),1),
               ((x,y,(u+step)%n,v),-1),((x,y,u,(v+step)%n),-1)]
        for key,sgn in terms:
            result[key]=add(result.get(key,{}),scale(p,sgn))
    return {k:p for k,p in result.items() if p}


def p_coordinate_checks(counts: Counter) -> None:
    for n in [3,5]:
        for a in range(n):
            for b in range(n):
                for c in range(n):
                    for d in range(n):
                        v=(a,b); w=(c,d)
                        actual=collective_comm(collective_comm(pair_matrix(n,v,w),-1,n),1,n)
                        diag, off=coefficients(b,d,n)
                        predicted={}
                        for vv,ww,coef in [(v,w,diag),(((a+1)%n,b),((c-1)%n,d),off),
                                           (((a-1)%n,b),((c+1)%n,d),off)]:
                            for key,p in pair_matrix(n,vv,ww).items():
                                predicted[key]=add(predicted.get(key,{}),mul(coef,p,n))
                        for key in actual.keys() | predicted.keys():
                            assert equal(actual.get(key,{}),predicted.get(key,{}),n),(n,v,w,key)
                            counts['p_coordinate_entries']+=1
                        counts['p_full_weyl_pairs']+=1


def squared_sine(exponent: int, modulus: int) -> Poly:
    return scale(add({0:F(2)},scale(phase(exponent,modulus),-1),scale(phase(-exponent,modulus),-1)),F(1,4))


def gauge_checks(counts: Counter) -> None:
    for n in range(3,34,2):
        modulus=2*n; h=(n-1)//2
        for k in range(-h,h+1):
            sa=squared_sine(k,modulus); ca=add({0:F(1)},scale(sa,-1))
            for a in range(n):
                sy=squared_sine(2*a-k,modulus); cy=add({0:F(1)},scale(sy,-1))
                gd=scale(add(mul(sa,cy,modulus),mul(ca,sy,modulus)),8)
                go=scale(add(mul(sa,cy,modulus),scale(mul(ca,sy,modulus),-1)),4)
                diag,off=coefficients(a,k-a,n)
                lift=lambda p:{2*j:x for j,x in p.items()}
                assert equal(lift(diag),gd,modulus),(n,k,a,'diagonal')
                counts['gauge_diagonals']+=1
                for b in [0,1,n-1]:
                    for step in [-1,1]:
                        dest=(b+step)%n
                        sign=1 if (k*(dest-b)) % 2 == 0 else -1
                        holonomy=(1 if k % 2 == 0 else -1) if b+step<0 or b+step>=n else 1
                        assert equal(scale(lift(off),sign),scale(go,holonomy),modulus),(n,k,a,b,step)
                        counts['gauge_edges_with_wraps']+=1


def projection(n: int, f: dict, rows: bool) -> dict:
    result={}
    for a in range(n):
        if not a:
            for b in range(1,n):
                key=(a,b) if rows else (b,a)
                result[key]=f.get(key,F(0))
        else:
            keys=[(a,b) if rows else (b,a) for b in range(n)]
            mean=sum((f.get(key,F(0)) for key in keys),F(0))/n
            result.update({key:mean for key in keys})
    return result


def projection_checks(counts: Counter) -> None:
    for n in range(3,34,2):
        vertices=[(a,b) for a in range(n) for b in range(n) if (a,b)!=(0,0)]
        vectors=[({key:F(1) for key in vertices},F(1)),
                 ({key:F(-n if key[0]==0 else 1) for key in vertices},F(1,n*n))]
        for j in range(1,n-1):
            vectors.append(({(0,j):F(1),(0,n-1):F(-1)},F(1,n)))
            vectors.append(({(a,b):F(1 if a==j else -1) for a in [j,n-1] for b in range(n)},F(1,n)))
        assert len(vectors)==2*n-2
        for f,eigenvalue in vectors:
            assert projection(n,f,True)=={key:f.get(key,F(0)) for key in vertices}
            answer=projection(n,projection(n,f,False),True)
            assert all(answer[key]==eigenvalue*f.get(key,F(0)) for key in vertices),(n,eigenvalue)
            counts['projection_eigenvectors']+=1
        counts['projection_dimensions']+=1


def compression_checks(counts: Counter) -> None:
    for n in range(3,34,2):
        modulus=2*n
        cos_sum={}
        for a in range(n):
            cos_sum=add(cos_sum,add({0:F(1)},scale(squared_sine(2*a,modulus),-1)))
        assert equal(cos_sum,{0:F(n,2)},modulus)
        counts['cosine_weight_sums']+=1
        for c,d in [(F(0),F(1)),(F(1),F(0)),(F(1),F(-2)),(F(1,3),F(5,7))]:
            energy={}
            for a in range(n):
                weight=add({0:F(1)},scale(squared_sine(2*a,modulus),-1))
                for b in range(n):
                    left=c+(d if (a,b)==(0,0) else 0)
                    right=c+(d if (a,(b+1)%n)==(0,0) else 0)
                    energy=add(energy,scale(weight,(left+right)**2))
            predicted=2*n*n*c*c+2*d*d+8*c*d
            assert equal(energy,{0:predicted},modulus),(n,c,d)
            counts['kernel_compression_cases']+=1


def hardy_checks(counts: Counter) -> None:
    for j in range(1,21):
        # Exact LDL of 4 diag(4^ell) - T* diag(4^j) T, T_jell=1_{j<=ell}.
        matrix=[[F(4*4**a if a==b else 0)-sum(F(4**k) for k in range(min(a,b)+1))
                 for b in range(j)] for a in range(j)]
        lower=[[F(0)]*j for _ in range(j)]; pivots=[]
        for a in range(j):
            lower[a][a]=F(1)
            pivot=matrix[a][a]-sum(lower[a][k]**2*pivots[k] for k in range(a))
            assert pivot>0,(j,a,pivot)
            pivots.append(pivot)
            for b in range(a+1,j):
                lower[b][a]=(matrix[b][a]-sum(lower[b][k]*lower[a][k]*pivots[k] for k in range(a)))/pivot
        for a in range(j):
            for b in range(j):
                assert matrix[a][b]==sum(lower[a][k]*pivots[k]*lower[b][k] for k in range(min(a,b)+1))
                counts['hardy_ldl_entries']+=1
        counts['hardy_positive_matrices']+=1


def main() -> None:
    # These exact finite controls rely on assertions; never certify a run
    # in which Python has removed them (including PYTHONOPTIMIZE).
    if not __debug__:
        raise RuntimeError(
            "Verification requires assertions; disable -O and PYTHONOPTIMIZE"
        )
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args(); counts=Counter()
    q_coordinate_checks(counts); p_coordinate_checks(counts)
    gauge_checks(counts); projection_checks(counts); compression_checks(counts); hardy_checks(counts)
    result={'claim_id':'BGS-FM-019','status':'PASS','arithmetic':'Exact integers, Fraction and cyclotomic reduction over Q',
            'counts':dict(counts),'non_claims':['No universal analytic gap, effective constant, Trotter asymptotic, actual spectral moment, original noise removal, BGS or analytic Lean certification is computed']}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
