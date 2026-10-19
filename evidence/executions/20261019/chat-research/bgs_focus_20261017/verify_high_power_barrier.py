#!/usr/bin/env python3
"""Exact integer/rational finite controls of the auxiliary iid barrier."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import comb, factorial, lgamma, log, prod
import json
import platform
import sys


def tables(n, m):
    c = Counter()
    for word in product(range(n), repeat=m):
        edges = [0]*(n*n)
        for k, a in enumerate(word):
            edges[n*a+word[(k+1) % m]] += 1
        c[tuple(edges)] += 1
    return c


def gaussian_h(n, m):
    return factorial(m)*(comb(n+m,m+1)-(comb(n,m+1) if n>m else 0))


def enum_checks():
    records, table_count, words = [], 0, 0
    for n, maximum in [(2,10),(3,8)]:
        for m in range(1, maximum+1):
            c = tables(n,m)
            hm = sum(count*count*prod(factorial(v) for v in nu)
                     for nu,count in c.items())
            assert hm == gaussian_h(n,m), (n,m,hm,gaussian_h(n,m))
            assert sum(c.values()) == n**m
            tilted = 0
            for nu,count in c.items():
                col = sum(v*(v-1)//2 for v in nu)
                maximum_col = m*(m-1)//2
                assert all(nu[n*a+b]*2 <=m for a in range(n)
                           for b in range(n) if a != b)
                if max(nu)*2 <=m:
                    assert 4*(maximum_col-col)>=m*m
                elif max(nu)<m:
                    r = m-max(nu)
                    assert maximum_col-col>=r*(m-r)
                tilted += count*count*prod(factorial(v) for v in nu)*2**col
            # A lower bound, exact lambda=log(2), no floating comparison.
            full = n*factorial(m)*2**(m*(m-1)//2)
            assert tilted >=full
            if m%2 ==0:
                # The explicit finite upper bound (5), evaluated rationally.
                x = F((n*m)**2, 2**(m//2))
                if x<1:
                    upper = x*(1+x)/(1-x)**3+F(n**(2*m-1),2**(m*m//4))
                    assert F(tilted-full,full)<=upper
            records.append({"n":n,"m":m,"tables":len(c),
                            "h":hm,"tilted_partition_lambda_log2":tilted})
            table_count +=len(c)
            words +=n**m
    return {"ranges":[{"n":2,"m":[1,10]},{"n":3,"m":[1,8]}],
            "words":words,"tables":table_count,"cases":records}


def clique_checks():
    rows = []
    for q,L in [(1,1),(1,3),(2,1),(2,2),(2,3),(3,1)]:
        m=L*q*q
        count=tables(q,m)[(L,)*(q*q)]
        predicted=factorial(L*q)**q//factorial(L)**(q*q)
        assert count ==predicted
        rows.append({"q":q,"L":L,"m":m,"rooted_words":count})
    return rows


def bounded_law_checks():
    R=4096
    probs=[F(1,R),F(R-2,R-1),F(1,R*(R-1))]
    values=[0,1,R]
    assert sum(probs)==1 and all(p>0 for p in probs)
    moments=[sum(p*x**k for p,x in zip(probs,values)) for k in range(1,4)]
    assert moments ==[1,2,4098]
    # Exact positivity using e<3, without certifying a floating e bound.
    assert 3*4098>256*27
    delta=log(3*4098/256)/3-1
    rates=[]
    for q in [3,9,21,51,101,301]:
        n=m=3*q*q
        log_clique=2*q*lgamma(3*q+1)-2*q*q*log(6)+q*q*log(4098)-m*log(n)
        log_g=lgamma(n+m+1)-lgamma(n)-log(m+1)-m*log(n)
        rates.append({"q":q,"N":n,"m":m,
                      "one_clique_log_ratio_per_N_float":(log_clique-log_g)/n})
    return {"R":R,"rational_probabilities":[str(p) for p in probs],
            "moments":[str(x) for x in moments],
            "delta_float":delta,"rate_support_float":rates,
            "floating_evidence_scope":"Stirling-rate illustration only, not a rigorous numerical certificate."}


def tail_bound_direct():
    # Larger m without enumerating all words: partition coefficients from
    # dynamic word counting on N=2, so the explicit tilt bound becomes sharp.
    n=2
    rows=[]
    for m in [18,24,32]:
        counts=Counter()
        for start in range(n):
            dynamic={(start,(0,)*4):1}
            for step in range(m-1):
                nxt=Counter()
                for (last,nu),count in dynamic.items():
                    for b in range(n):
                        vv=list(nu)
                        vv[n*last+b]+=1
                        nxt[(b,tuple(vv))]+=count
                dynamic=nxt
            for (last,nu),count in dynamic.items():
                vv=list(nu)
                vv[n*last+start]+=1
                counts[tuple(vv)]+=count
        assert sum(counts.values())==n**m
        assert sum(c*c*prod(factorial(v) for v in nu)
                   for nu,c in counts.items())==gaussian_h(n,m)
        z=sum(c*c*prod(factorial(v) for v in nu)
              *2**sum(v*(v-1)//2 for v in nu) for nu,c in counts.items())
        full=n*factorial(m)*2**(m*(m-1)//2)
        x=F((n*m)**2,2**(m//2))
        if x<1:
            err=F(z-full,full)
            bound=x*(1+x)/(1-x)**3+F(n**(2*m-1),2**(m*m//4))
            assert err<=bound
            rows.append({"N":n,"m":m,"tables":len(counts),
                         "relative_error_exact":str(err),
                         "relative_bound_exact":str(bound)})
    assert rows
    return rows


def main():
    result={"status":"passed","python":platform.python_version(),
            "enumerations":enum_checks(),"cliques":clique_checks(),
            "bounded_law":bounded_law_checks(),"tilt_bound":tail_bound_direct(),
            "non_claims":["Finite controls do not prove asymptotic theorems.",
                          "No unitary or BGS counterexample is constructed."]}
    with open(sys.argv[1],'w',encoding='utf-8') as f:
        json.dump(result,f,indent=2)
        f.write('\n')
    print(json.dumps({"status":"passed","enumerated_words":result['enumerations']['words'],
                      "tables":result['enumerations']['tables'],"clique_cases":len(result['cliques']),
                      "tilt_bound_cases":len(result['tilt_bound']),
                      "delta_float":result['bounded_law']['delta_float']},sort_keys=True))


if __name__=='__main__':
    main()
