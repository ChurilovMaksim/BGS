#!/usr/bin/env python3
"""Exact finite checks for BGS-FM-007, adapted from the supplied PDF verify_v7.py.
No floating-point eigenvalues, parameter averaging or asymptotic inference.
The unrestricted-N proofs are in mathematics/frozen_seven_cut_reduction.md.
"""
import argparse
import json
from fractions import Fraction as F
from math import prod
from pathlib import Path

def determinant(a):
    a=[[F(x) for x in row] for row in a]
    n=len(a)
    out=F(1)
    for i in range(n):
        pivot=next((j for j in range(i,n) if a[j][i]),None)
        if pivot is None:
            return F(0)
        if pivot!=i:
            a[i],a[pivot]=a[pivot],a[i]
            out=-out
        p=a[i][i]
        out*=p
        for j in range(i+1,n):
            q=a[j][i]/p
            for z in range(i+1,n):
                a[j][z]-=q*a[i][z]
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",type=Path,default=Path("validation_v7.json"))
    args=ap.parse_args()
    counts={}
    residues=[]
    for a in range(1,7):
        err=[F((2*j*a+7)//14)-F(j*a,7) for j in range(7)]
        assert sum(x*x for x in err)==F(4,7)
        assert max(map(abs,err))==F(3,7)
        residues.append([str(x) for x in err])
    counts["nonzero_residue_classes"]=6
    dims=0
    for n in range(15,20002,2):
        s=[(2*j*n+7)//14 for j in range(7)]+[n]
        h=(n+1)//2
        cuts=[(x-h)%n for x in s[:-1]]
        assert len(set(cuts))==7
        assert len({z for x in cuts for z in (x,(x+1)%n)})==14
        gaps=[s[j+1]-s[j] for j in range(7)]
        assert sum(gaps)==n
        assert all(g in (n//7,(n+6)//7) for g in gaps)
        err=[F(s[j])-F(j*n,7) for j in range(7)]
        assert sum(x*x for x in err)==(F(0) if n%7==0 else F(4,7))
        assert max(map(abs,err))==(F(0) if n%7==0 else F(3,7))
        dims+=1
    counts["odd_dimensions_with_exact_cut_geometry"]=dims
    assert F(196,100)*F(4,7)==F(28,25)
    assert F(196,200)*F(9,49)==F(9,50)
    assert F(28,25)/4==F(7,25)
    assert F(9,50)/4==F(9,200)
    counts["norm_and_transport_constants"]=4

    # Infinite weighted power sum via an exact finite sum plus its exact tail.
    sums=0
    for q in (F(1,5),F(2,7),F(1,2),F(4,5),F(97,101)):
        exact=q*(1+q)/(1-q)**3
        for m in range(41):
            tail=q**(m+1)*(F((m+1)**2,1)/(1-q)
                         +2*(m+1)*q/(1-q)**2
                         +q*(1+q)/(1-q)**3)
            assert sum(F(k*k)*q**k for k in range(1,m+1))+tail==exact
            sums+=1
    counts["weighted_second_power_sum_identities"]=sums

    occ=0
    for k in range(2,15):
        for m in range(2*k,251):
            assert prod(range(m-k+1,m+1))>=F(m,2)**k
            occ+=1
    counts["local_factorial_occupancy_bounds"]=occ

    # Change from the last point as reference to any other labelled point.
    reanchors=0
    for k in range(2,15):
        d=k-1
        coords=[[int(i==j) for j in range(d)] for i in range(d)]+[[0]*d]
        for anchor in range(k):
            a=[[coords[i][j]-coords[anchor][j] for j in range(d)]
               for i in range(k) if i!=anchor]
            assert abs(determinant(a))==1
            reanchors+=1
    counts["unimodular_reanchoring_matrices"]=reanchors

    # Count all matrix entries between a block and its complement.
    blocks=0
    for n in range(15,300,2):
        s=[(2*j*n+7)//14 for j in range(7)]+[n]
        sizes=[s[j+1]-s[j] for j in range(7)]
        for mask in range(1,127):
            d=sum(sizes[j] for j in range(7) if mask&(1<<j))
            assert sum(sizes[a]*sizes[b] for a in range(7)
                       for b in range(7)
                       if mask&(1<<b) and not(mask&(1<<a)))==d*(n-d)
            blocks+=1
    counts["noninvariant_union_block_identities"]=blocks

    # Exact finite CUE Abel identity, checked as a finite sum plus constant tail.
    cue=0
    for n in range(3,31):
        for q in (F(1,5),F(2,7),F(3,4)):
            total=sum(m*q**m for m in range(1,n))+n*q**n/(1-q)
            assert total==q*(1-q**n)/(1-q)**2
            cue+=1
    counts["finite_CUE_Abel_identities"]=cue

    output={"status":"all exact new-reduction checks passed",
            "arithmetic":"integer and Fraction only",
            "counts":counts,"rounding_residue_errors":residues,
            "scope":"Finite identities only; general proofs in mathematics/frozen_seven_cut_reduction.md; no spectral simulation."}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(output,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(output,ensure_ascii=False,indent=2))
if __name__=="__main__":
    main()
