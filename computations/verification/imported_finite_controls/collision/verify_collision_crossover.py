#!/usr/bin/env python3
"""Finite checks for a square-root-time equal-edge crossover.

This is NOT a numerical proof of BGS or of any large-N limit.
The checks are exact integer/rational except displayed float summaries.
No assertions are disabled by python -O.  Standard library only.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
from itertools import product, permutations
import json
import math
from pathlib import Path
import time


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ArithmeticError(message)


def bareiss(a: list[list[int]]) -> int:
    if not a:
        return 1
    a = [r[:] for r in a]
    sign, old = 1, 1
    for k in range(len(a)-1):
        if a[k][k] == 0:
            row = next((j for j in range(k+1,len(a)) if a[j][k]), None)
            if row is None:
                return 0
            a[k],a[row]=a[row],a[k]
            sign=-sign
        pivot=a[k][k]
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)):
                val=a[i][j]*pivot-a[i][k]*a[k][j]
                require(val % old == 0, 'non-exact Bareiss division')
                a[i][j]=val//old
            a[i][k]=0
        old=pivot
    return sign*a[-1][-1]


def edges(word: tuple[int,...], n: int) -> tuple[int,...]:
    a=[0]*(n*n)
    for i,x in enumerate(word):
        a[n*x+word[(i+1)%len(word)]]+=1
    return tuple(a)


def best_count(e: tuple[int,...], n: int) -> int:
    r=[sum(e[i*n:(i+1)*n]) for i in range(n)]
    active=[i for i in range(n) if r[i]]
    require(all(r[j]==sum(e[i*n+j] for i in range(n)) for j in range(n)),
            'unbalanced edge table')
    lap=[[((r[i] if i==j else 0)-e[i*n+j]) for j in active]
         for i in active]
    t=bareiss([row[:-1] for row in lap[:-1]])
    numerator=sum(r)*t*math.prod(math.factorial(r[i]-1) for i in active)
    denominator=math.prod(math.factorial(v) for v in e)
    require(numerator % denominator == 0, 'noninteger BEST result')
    return numerator//denominator


def pairings(items: tuple[int,...]):
    if not items:
        yield ()
        return
    a=items[0]
    for i in range(1,len(items)):
        b=items[i]
        tail=items[1:i]+items[i+1:]
        for rest in pairings(tail):
            yield ((a,b),)+rest


def one_cycle(partners: list[int]) -> bool:
    n=len(partners)
    if n==0:
        return True
    cur=0
    for count in range(1,n+1):
        cur=(partners[cur]+1)%n
        if cur==0:
            return count==n
    return False


def reconnections(m: int, pairs: tuple[tuple[int,int],...]) -> int:
    ans=0
    for mask in range(1<<len(pairs)):
        # An odd number of transpositions cannot preserve a single cycle.
        if mask.bit_count()%2:
            continue
        p=list(range(m))
        for j,(a,b) in enumerate(pairs):
            if mask>>j & 1:
                p[a],p[b]=b,a
        ans+=one_cycle(p)
    return ans


def signed_cycle_sum(m: int, pairs: tuple[tuple[int,int],...]) -> int:
    total=0
    for mask in range(1<<len(pairs)):
        p=list(range(m))
        for j,(a,b) in enumerate(pairs):
            if mask>>j & 1:
                p[a],p[b]=b,a
        succ=[(p[i]+1)%m for i in range(m)]
        seen=set(); components=0
        for start in range(m):
            if start in seen:
                continue
            components+=1; cur=start
            while cur not in seen:
                seen.add(cur); cur=succ[cur]
        total+=(-1)**components
    return total


def word_reconnections(word: tuple[int,...]) -> int:
    places={x:[] for x in set(word)}
    for i,x in enumerate(word):
        places[x].append(i)
    require(max(map(len,places.values()))<=2,'triple vertex in chord test')
    return reconnections(len(word),tuple(tuple(v) for v in places.values() if len(v)==2))


def cycle_partition(p: tuple[int,...]) -> list[list[int]]:
    seen=set(); out=[]
    for a in range(len(p)):
        if a in seen:
            continue
        cur=a; block=[]
        while cur not in seen:
            seen.add(cur); block.append(cur); cur=p[cur]
        out.append(block)
    return out


def join_count(blocks: list[list[int]], extra: tuple[tuple[int,...],...], m:int) -> int:
    parent=list(range(m))
    def root(a):
        while parent[a]!=a:
            parent[a]=parent[parent[a]]; a=parent[a]
        return a
    for b in list(blocks)+list(extra):
        for a in b[1:]:
            parent[root(a)]=root(b[0])
    return len({root(a) for a in range(m)})


def z_factorial(n:int,m:int,c:F=F(1)) -> F:
    return math.prod(F(1)+F(j)*c/n for j in range(m))


def flat_chord_upper(n:int,m:int) -> F:
    # E[T(chords) 1_{all occupancies <=2}] for iid uniform words.
    total=F(0)
    for k in range(m//2+1):
        v=m-k
        if v>n:
            continue
        falling=math.prod(range(n-v+1,n+1))
        total += F(falling*math.factorial(m),
                   n**m*math.factorial(m-2*k)*math.factorial(k)*(k+1))
    return total


def flat_enclosure(n:int,m:int) -> tuple[F,F,F]:
    g=flat_chord_upper(n,m)
    z=z_factorial(n,m)
    edge=z*F(24*math.comb(m,2),n*n)
    triple=z*F(6*math.comb(m,3),n*n)
    return max(F(0),g-edge),g,g+triple


def enumerate_words() -> dict:
    count_words=count_types=count_chord=0
    records=[]
    specs=[(2,m) for m in range(3,9)]+[(3,m) for m in range(3,8)]+[(4,6)]
    for n,m in specs:
        cnt=Counter(); chord_total=0
        for w in product(range(n),repeat=m):
            e=edges(w,n);cnt[e]+=1;count_words+=1
            occ=Counter(w)
            if max(occ.values())<=2:
                h=word_reconnections(w)
                expected=F(m*h,math.prod(math.factorial(v) for v in e))
                require(expected.denominator==1,'fractional rooted chord count')
                require(best_count(e,n)==expected,'BEST versus chord switching')
                chord_total+=h;count_chord+=1
        for e,c in cnt.items():
            require(best_count(e,n)==c,'BEST versus direct enumeration')
            r=[sum(e[i*n:(i+1)*n]) for i in range(n)]
            require(F(c,m)<=math.prod(math.factorial(x) for x in r),'factorial domination')
        b_over_m=F(sum(c*c for c in cnt.values()),m*n**m)
        g=flat_chord_upper(n,m)
        require(F(chord_total,n**m)==g,'flat chord expression')
        lo,_,hi=flat_enclosure(n,m)
        require(lo<=b_over_m<=hi,'finite flat enclosure')
        count_types+=len(cnt)
        records.append({'N':n,'m':m,'B_over_m':str(b_over_m),'chord_expression':str(g)})
    return {'words':count_words,'edge_types':count_types,'chord_word_checks':count_chord,'records':records}


def chord_checks(max_k:int=6) -> list[dict]:
    out=[]
    for k in range(max_k+1):
        num=cyclic=total_t=0
        for pairs in pairings(tuple(range(2*k))):
            p=list(range(2*k))
            for a,b in pairs:
                p[a],p[b]=b,a
            cyclic+=one_cycle(p)
            total_t+=reconnections(2*k,pairs)
            if k:
                require(signed_cycle_sum(2*k,pairs)==0, "signed determinant cancellation")
            num+=1
        target=F(1,k+1) if k%2==0 else F(0)
        require(F(cyclic,num)==target,'one-cycle chord formula')
        require(F(total_t,num)==F(2**k,k+1),'all-subsets chord sum')
        out.append({'chords':k,'matchings':num,'single_cycles':cyclic,
                    'mean_reconnections':str(F(total_t,num))})
    return out


def permutation_checks() -> dict:
    checks=0; perms=0
    for m in range(3,8):
        families=[((0,1,2),)]
        if m>=4:
            families += [((0,2),(1,3)),((0,1,2,3),)]
        if m>=5:
            families += [((0,1),(2,3,4)),]
        x=F(1,7)
        sums={pi:F(0) for pi in families}
        z=F(0)
        for p in permutations(range(m)):
            blocks=cycle_partition(p);perms+=1
            z+=x**(m-len(blocks))
            for pi in families:
                sums[pi]+=x**(m-join_count(blocks,pi,m))
        require(z==math.prod(1+j*x for j in range(m)),'Ewens normalization')
        for pi,v in sums.items():
            k=len({i for b in pi for i in b});rank=k-len(pi)
            require(v<=z*math.factorial(k)*x**rank,'weighted equality bound')
            checks+=1
    return {'permutations':perms,'partition_inequalities':checks}


def matrix_product(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(a))) for j in range(len(a))]
            for i in range(len(a))]


def markov_checks() -> list[dict]:
    out=[]
    n=3
    p=[[F(1,2),F(1,3),F(1,6)],
       [F(1,6),F(1,2),F(1,3)],
       [F(1,3),F(1,6),F(1,2)]]
    c=F(3,2);x=c/n
    for m in (5,6,7):
        weights={};z=F(0);ft=F(0);fe=F(0);ff=F(0)
        b_total=F(0)
        for w in product(range(n),repeat=m):
            weight=math.prod(p[w[j]][w[(j+1)%m]] for j in range(m))
            z+=weight
            e=edges(w,n); weights[e]=weight
            r=Counter(w); f=math.prod(math.factorial(v) for v in r.values())
            ff+=f*weight
            if max(r.values())>=3:ft+=f*weight
            if max(e)>=2:fe+=f*weight
        power=[[F(i==j) for j in range(n)] for i in range(n)]
        for _ in range(m):power=matrix_product(power,p)
        require(sum(power[i][i] for i in range(n))==z,'Markov loop normalization')
        zperm=z_factorial(n,m,c)
        require(ff<=c*zperm,'factorial weighted Markov bound')
        require(ft<=c*zperm*math.comb(m,3)*6*x*x,'triple weighted bound')
        require(fe<=c*zperm*math.comb(m,2)*24*x*x,'edge weighted bound')
        for e,weight in weights.items():
            count=best_count(e,n)
            b_total+=count*count*weight
        out.append({'N':n,'m':m,'loop_normalization':str(z),'equal_edge_mass':str(b_total),
                    'factorial_weight':str(ff),'triple_weight':str(ft),'edge_repeat_weight':str(fe)})
    return out


def finite_tables() -> list[dict]:
    out=[]
    for n in (101,1009,10007,100003):
        m=math.isqrt(n)
        lo,g,hi=flat_enclosure(n,m)
        lam=m*m/(2*n)
        target=math.sinh(lam)/lam
        out.append({'N':n,'m':m,'B_over_m_lower':float(lo),'chord_sum':float(g),
                    'B_over_m_upper':float(hi),'sinh_lambda_over_lambda':target,
                    'bounds_exact_rational':True})
    return out


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=Path(__file__).with_name('verification.json'))
    ap.add_argument('--max-chords',type=int,default=6)
    args=ap.parse_args()
    if not 0<=args.max_chords<=7:
        ap.error('--max-chords must be between 0 and 7')
    start=time.time()
    data={'scope':'Finite checks only. No numerical proof of BGS or of large-N limits.',
          'word_checks':enumerate_words(),
          'chord_checks':chord_checks(args.max_chords),
          'weighted_permutation_checks':permutation_checks(),
          'markov_checks':markov_checks(),
          'flat_finite_enclosures':finite_tables()}
    data['elapsed_seconds']=time.time()-start
    args.output.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'passed','words':data['word_checks']['words'],
                      'edge_types':data['word_checks']['edge_types'],
                      'chord_word_checks':data['word_checks']['chord_word_checks'],
                      'matchings':sum(x['matchings'] for x in data['chord_checks']),
                      'seconds':data['elapsed_seconds']},indent=2))
    print(json.dumps(data['flat_finite_enclosures'],indent=2))

if __name__=='__main__':
    main()
