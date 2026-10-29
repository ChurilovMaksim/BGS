# Direct structural check of Lemma 4 and Lemma 5 (independent of the engine).
import itertools, sys, numpy as np
from fractions import Fraction
from collections import Counter
def edges(seq):
    m=len(seq); return Counter(frozenset((seq[j],seq[(j+1)%m])) if seq[j]!=seq[(j+1)%m] else frozenset((seq[j],)) for j in range(m))
def rankQ(B):
    A=[[Fraction(v) for v in row] for row in B]; n=len(A); r=0
    for c in range(n):
        piv=next((i for i in range(r,n) if A[i][c]!=0),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        for i in range(r+1,n):
            f=A[i][c]/A[r][c]
            if f: A[i]=[a-f*b for a,b in zip(A[i],A[r])]
        r+=1
    return r
for m in range(4,11):
    C=list(range(m)); EC=edges(C); dist=Counter(); bad=0; n2opt=nswap=0
    for perm in itertools.permutations(range(1,m)):
        if perm[0]>perm[-1]: continue
        H=[0]+list(perm); EH=edges(H)
        B=np.zeros((m,m),dtype=np.int64)
        for e,c in EC.items():
            a,b=tuple(e); B[a,b]+=c; B[b,a]+=c
        for e,c in EH.items():
            a,b=tuple(e); B[a,b]-=c; B[b,a]-=c
        r=int(np.linalg.matrix_rank(B))
        dist[r]+=1
        if r<=2:
            if rankQ(B)!=r: bad+=1
            k=sum((EC-EH).values())
            is2opt = (k==2)
            isswap = any(H==[ (b if v==a else a if v==b else v) for v in C] or edges([(b if v==a else a if v==b else v) for v in C])==EH
                         for a in range(m) for b in range(a+1,m) if min(b-a,m-b+a)>=3)
            if r==2:
                if is2opt: n2opt+=1
                elif isswap: nswap+=1
                else: bad+=1
            if r==0 and EH!=EC: bad+=1
    print(f"m={m}: #undirected Ham cycles={sum(dist.values())}, rank distribution={dict(sorted(dist.items()))}, rank2: 2-opt={n2opt} (m(m-3)/2={m*(m-3)//2}), swap={nswap} (max(0,m(m-5)/2)={max(0,m*(m-5)//2)}), unclassified={bad}",flush=True)
# Lemma 5: words with same edge multiset as the figure-eight, all gaps
def d(l): return 2 if l>=3 else 1
from sympy.utilities.iterables import multiset_permutations
for m in range(3,10):
    ok=True
    for g in range(1,m):
        x=[j if j!=g else 0 for j in range(m)]
        cnt=sum(1 for y in multiset_permutations(x) if edges(y)==edges(x))
        if cnt!=m*d(g)*d(m-g): ok=False; print("MISMATCH",m,g,cnt)
    print(f"Lemma5 m={m}: counts m*d(g)*d(m-g) for g=1..m-1: {ok}",flush=True)
