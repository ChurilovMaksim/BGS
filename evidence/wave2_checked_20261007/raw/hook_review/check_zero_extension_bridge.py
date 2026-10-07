#!/usr/bin/env python3
"""Bounded exact cycle-index bridge regression; no writes outside this directory.

The tested arithmetic and fixture definitions are shared with the copied
authored checker. Cycle-index exterior polynomials and power-sum complete
polynomials are constructed separately here, without its hook recursion.
"""
from fractions import Fraction as F
from itertools import product, permutations
from collections import Counter
from math import factorial
from functools import lru_cache
import json, pathlib, hashlib, time
from check_grouping_review_copy import G, fixtures, hook_polys

ROOT = pathlib.Path(__file__).resolve().parent

def require(ok, message):
    if not ok:
        raise RuntimeError(message)

def plus(A,B,scale=1):
    out = dict(A)
    for k,v in B.items():
        out[k] = out.get(k,G()) + v*scale
    return {k:v for k,v in out.items() if v}

def times(A,B):
    out = {}
    for k,v in A.items():
        for l,w in B.items():
            n = tuple(a+b for a,b in zip(k,l))
            out[n] = out.get(n,G())+v*w
    return {k:v for k,v in out.items() if v}

@lru_cache(None)
def cycle_types(m):
    answer = Counter()
    for perm in permutations(range(m)):
        visited = set()
        lengths = []
        for a in range(m):
            if a in visited:
                continue
            j, size = a, 0
            while j not in visited:
                visited.add(j)
                j = perm[j]
                size += 1
            lengths.append(size)
        answer[tuple(sorted(lengths))] += 1
    require(sum(answer.values())==factorial(m),'complete permutation cycle types')
    return answer

def direct_power_trace(U,m):
    N = len(U)
    answer = {}
    for w in product(range(N),repeat=m):
        z = G(1)
        for k in range(m):
            z *= U[w[k]][w[(k+1)%m]]
        n = tuple(w.count(k) for k in range(N))
        answer[n] = answer.get(n,G())+z
    return {k:v for k,v in answer.items() if v}

start = time.monotonic()
rows = []
zero_character_checks = 0
for name,U,authored_limit in fixtures():
    N = len(U)
    limit = min(authored_limit,6)
    unit = {(0,)*N:G(1)}
    power = [None]+[direct_power_trace(U,m) for m in range(1,limit+1)]
    exterior = [unit]
    complete = [unit]
    for degree in range(1,limit+1):
        ej = {}
        for lengths, count in cycle_types(degree).items():
            term = unit
            for length in lengths:
                term = times(term,power[length])
            ej = plus(ej,term,F((-1)**(degree-len(lengths))*count,factorial(degree)))
        exterior.append(ej)
        hd = {}
        for length in range(1,degree+1):
            hd = plus(hd,times(power[length],complete[degree-length]),F(1,degree))
        complete.append(hd)
    for m in range(N+1,limit+1):
        signed,B,principal_exterior,recursive_complete = hook_polys(U,m)
        for j in range(0,min(m,N)+1):
            require(exterior[j]==principal_exterior[j],name+' cycle index vs principal minor')
        for j in range(N+1,m+1):
            require(exterior[j]=={},name+' appended exterior character vanishes')
            zero_character_checks += 1
        require(complete[:m+1]==recursive_complete,name+' independent complete polynomial')
        truncated, extended = {},{}
        for j in range(1,m+1):
            term = times(exterior[j],complete[m-j])
            extended = plus(extended,term,(-1)**(j-1)*j)
            if j<=N:
                truncated = plus(truncated,term,(-1)**(j-1)*j)
        require(truncated==extended==signed==power[m],name+' full zero-extension bridge')
        completed_covariance = sum(v.norm() for v in extended.values())
        require(G(completed_covariance)==B,name+' unchanged signed covariance')
        rows.append({'family':name,'N':N,'m':m,
                     'zero_exterior_degrees':list(range(N+1,m+1)),
                     'truncated_equals_extended_equals_trace':True,
                     'signed_covariance':str(B)})

def mark(lengths,N=None):
    answer = 0
    for mask in product((0,1),repeat=len(lengths)):
        j = sum(a*b for a,b in zip(lengths,mask))
        if N is None or j<=N:
            answer += (-1)**(sum(mask)+1)*j
    return answer

require([mark((1,1),1),mark((2,),1)]==[2,0],'literal N1 m2 witness')
require([mark((1,1)),mark((2,))]==[0,2],'extended N1 m2 bridge')
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
receipt = {
    'status':'zero-character bridge regression passed',
    'cases':len(rows),'rows':rows,
    'zero_exterior_character_checks':zero_character_checks,
    'N1_m2_witness':{'truncated_cycle_weights':[2,0],'extended_cycle_weights':[0,2]},
    'arithmetic':'exact Q(i), fractions.Fraction; shared checked G arithmetic and fixtures',
    'construction':'explicit permutation cycle-index exterior polynomials; direct rooted-word power sums; power-sum complete recursion',
    'elapsed_seconds':time.monotonic()-start,
    'script_sha256':sha(pathlib.Path(__file__)),
    'shared_checker_sha256':sha(ROOT/'check_grouping_review_copy.py'),
    'corrected_proof_sha256':sha(ROOT/'hook_tree_current_identity_v2.md'),
    'nonclaims':['No finite-check extrapolation','No new asymptotic estimate','No BGS operator evaluation'],
}
(ROOT/'zero_extension_bridge_results.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
