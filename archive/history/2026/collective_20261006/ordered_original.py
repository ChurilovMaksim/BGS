#!/usr/bin/env python3
"""Exact independent finite audit using ordered-word permutation operators.
No Kostka recursion is used to construct the tested Haar compression.
"""
import itertools as it, math, json, time, sys, importlib.util
from collections import Counter, defaultdict
from pathlib import Path
import numpy as np
import sympy as s
ROOT=Path(__file__).resolve().parents[1]

def parts(n,cap=None):
    if not n: yield (); return
    for a in range(min(n,n if cap is None else cap),0,-1):
        for p in parts(n-a,a):yield (a,)+p

def compositions(n,k):
    if k==1:yield (n,);return
    for a in range(n+1):
        for tail in compositions(n-a,k-1):yield (a,)+tail

def cycle_type(p):
    used=set(); out=[]
    for i in range(len(p)):
        if i in used:continue
        c=0;j=i
        while j not in used:used.add(j);c+=1;j=p[j]
        out.append(c)
    return tuple(sorted(out,reverse=True))

def psd(M):
    M=s.MutableDenseMatrix(M)
    while M.rows:
        assert M==M.T
        assert all(x>=0 for x in M.diagonal())
        ids=[i for i in range(M.rows) if M[i,i]>0]
        if not ids:assert M==s.zeros(M.rows);return
        j=ids[0];rest=[i for i in range(M.rows) if i!=j]
        M=M.extract(rest,rest)-M.extract(rest,[j])*M.extract([j],rest)/M[j,j]

def insertion(word,N):
    d=N-1; zero=(0,)*d; out={zero:s.Integer(1)}
    for color in word:
        nxt=defaultdict(lambda:s.Integer(0))
        vals=[int(color==i)-int(color==N-1) for i in range(d)]
        for a,v in out.items():
            nxt[a]+=v
            for j,c in enumerate(vals):
                if c:
                    b=list(a);b[j]+=1;nxt[tuple(b)]+=v*c
        out=dict(nxt)
    return out

def run(N,m):
    words=list(it.product(range(N),repeat=m)); index={w:i for i,w in enumerate(words)}; D=len(words)
    contents=list(compositions(m,N)); ci={c:i for i,c in enumerate(contents)}
    wc=[tuple(w.count(j) for j in range(N)) for w in words]
    counts=[wc.count(c) for c in contents]; metric=s.diag(*counts)
    classes=list(parts(m)); class_id={c:i for i,c in enumerate(classes)}
    ops=np.zeros((len(classes),D,D),dtype=np.int64)
    for p in it.permutations(range(m)):
        c=class_id[cycle_type(p)]
        for j,w in enumerate(words):ops[c,index[tuple(w[p[k]] for k in range(m))],j]+=1
    flat=ops.reshape(len(classes),-1); gram=s.Matrix(flat@flat.T)
    piv=gram.rref()[1]; gram=gram.extract(piv,piv)
    V=s.zeros(len(piv),len(contents))
    for a,j in enumerate(piv):
        for k,w in enumerate(words):V[a,ci[wc[k]]]+=int(ops[j,k,k])
    F=V.T*gram.inv()*V; H=metric.inv()*F
    assert H.rank()==len([p for p in classes if len(p)<=N])
    basis=[a for q in range(m+1) for a in compositions(q,N-1)]
    X=s.Matrix([[insertion(tuple(j for j,c in enumerate(content) for _ in range(c)),N).get(a,0) for a in basis] for content in contents])
    assert X.det()!=0
    raw=X.T*metric*X; invariant=X.T*F*X
    deg=[sum(a) for a in basis]
    for i in range(len(basis)):
        for j in range(len(basis)):
            if deg[i]!=deg[j]:assert raw[i,j]==invariant[i,j]==0
    blocks=[]
    for q in range(m+1):
        ix=[i for i,d in enumerate(deg) if d==q]; G=raw.extract(ix,ix); B=invariant.extract(ix,ix); h=G.inv()*B
        r=sum(1 for p in parts(q) if all(2<=j<=N for j in p))
        assert h.rank()==r
        psd(B)
        if q==0:assert h==s.ones(1)
        elif q==1:assert h==s.zeros(len(ix))
        else:psd(G/s.Integer(N+1)-B)
        if q>0: assert (G-B).det()>0
        if N==2:
            assert h==s.Matrix([[s.Rational(1,q+1) if q%2==0 else 0]])
        blocks.append({'q':q,'dimension':len(ix),'rank':r,'trace':str(s.trace(h)),'charpoly':str(h.charpoly().as_expr())})
    P=s.ones(len(contents),1)*s.Matrix([counts]).reshape(1,len(contents))/s.Integer(N)**m
    assert P*P==P and H*P==P and P*H==P
    A=s.factor(s.trace((s.eye(len(contents))-H+P).inv())-len(contents))
    # Orthogonal comparison with author Kostka code only after direct construction.
    spec=importlib.util.spec_from_file_location('author_kostka',ROOT/'frozen/bgs_weighted_plateau_independent/hierarchy/kostka_resolvent.py'); author=importlib.util.module_from_spec(spec); spec.loader.exec_module(author)
    ps,B,PB=author.matrix(N,m)
    lam=s.Symbol('lambda'); cp=H.charpoly(lam).as_expr(); bp=B.charpoly(lam).as_expr()
    assert s.expand(cp-lam**(len(contents)-len(ps))*bp)==0
    assert A==s.Rational(author.evaluate(N,m)['A_exact'])
    return {'N':N,'m':m,'ordered_word_dimension':D,'occupation_dimension':len(contents),'central_rank':len(piv),'A_exact':str(A),'degree_blocks':blocks,'direct_vs_kostka_charpoly':'exact match'}

if __name__=='__main__':
    start=time.perf_counter(); rows=[]
    for N,m in [(2,1),(2,2),(2,3),(2,4),(2,5),(3,1),(3,2),(3,3),(3,4),(4,2),(4,3)]:
        rows.append(run(N,m));print(f'passed N={N}, m={m}',file=sys.stderr,flush=True)
    print(json.dumps({'method':'Ordered tensor words, central sums of actual slot permutation matrices, exact rational invariant projection; independent of Kostka construction','arithmetic':'Python integers, exact SymPy rationals; integer NumPy Gram products with maximal entries below 2^63','rows':rows,'runtime_seconds':time.perf_counter()-start,'non_claims':['Finite range only; no asymptotic inference','Does not numerically approximate Haar','Does not evaluate literal fixed-tau map']},indent=2))
