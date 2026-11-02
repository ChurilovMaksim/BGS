import numpy as np
from collections import defaultdict, Counter
import math, sys

def fix_mod_q_np(q, m):
    # vectorized over (y0,y1): for each y0, array y1=0..q-1, iterate recurrence
    res=[]
    y1_all=np.arange(q, dtype=np.int64)
    for y0 in range(q):
        a=np.full(q, y0, dtype=np.int64)
        b=y1_all.copy()
        seq=[a.copy(), b.copy()]
        for _ in range(m):
            c=(6*b-a)%q
            a,b=b,c
            seq.append(b.copy())
        # seq[m]==y0 and seq[m+1]==y1 ; seq list: seq[0]=y0, seq[1]=y1, seq[k]=y_k for k>=2? check indexing:
        # after loop, seq has m+2 entries: indices 0..m+1, where seq[m] should be y_m, seq[m+1]=y_{m+1}
        ok=(seq[m]==y0)&(seq[m+1]==y1_all)
        idx=np.where(ok)[0]
        for j in idx:
            vec=tuple(int(seq[k][j]) for k in range(m))
            res.append(vec)
    return res

def fix_mod_q_bruteforce(q, m):
    res=[]
    for y0 in range(q):
        for y1 in range(q):
            seq=[y0,y1]
            for _ in range(m):
                seq.append((6*seq[-1]-seq[-2])%q)
            if seq[m]==y0 and seq[m+1]==y1:
                res.append(tuple(seq[:m]))
    return res

def Yvec(y, t):
    Y=[0]*t
    for i,v in enumerate(y):
        Y[i%t]+=v
    return tuple(Y)

def main(m):
    t=math.gcd(m,4)
    assert t==4, "only t=4 here"
    # D_m factorization via sympy
    import sympy as sp
    s0,s1=2,6
    if m==1: D=4
    else:
        for _ in range(2,m+1):
            s0,s1=s1,6*s1-s0
        D=s1-2
    fac=sp.factorint(D)
    q2=2**fac.get(2,0); q3=3**fac.get(3,0)
    print(f"\nm={m} D={D} fac={fac} q2={q2} q3={q3}", flush=True)
    perms=[]
    for b in range(4):
        for sgn in (1,-1):
            pi=tuple((sgn*i+b)%4 for i in range(4))
            if pi not in perms: perms.append(pi)
    def apply(v, pi): return tuple(v[pi[i]] for i in range(4))
    def pi_set(Y, Yp): return frozenset(idx for idx,pi in enumerate(perms) if apply(Y,pi)==Yp)

    def component_pairs(q):
        vecs=fix_mod_q_np(q, m) if q>=128 else fix_mod_q_bruteforce(q, m)
        print(f" q={q} |Fix|={len(vecs)} (expect {q})", flush=True)
        assert len(vecs)==q, f"Fix size mismatch q={q} got {len(vecs)}"
        groups=defaultdict(list)
        for v in vecs: groups[tuple(sorted(v))].append(v)
        pairs=[]
        for vs in groups.values():
            for z in vs:
                Yq=tuple(x%q for x in Yvec(z,t))
                for zp in vs:
                    if zp==z: continue
                    Ypq=tuple(x%q for x in Yvec(zp,t))
                    pis=pi_set(Yq, Ypq)
                    if not pis:
                        print(f"  !! component Lemma Y FAILS mod {q}: {z} -> {zp}")
                    else:
                        pairs.append((z, zp, pis))
        print(f"  pairs ordered: {len(pairs)}, pi-size dist: {Counter(len(p[2]) for p in pairs)}", flush=True)
        return pairs

    pairs2=component_pairs(q2)
    pairs3=component_pairs(q3) if q3>1 else [( (0,)*m, (0,)*m, frozenset(range(len(perms))) )]

    def has_common_sigma(z2, z2p, z3, z3p):
        # Kuhn matching, left i -> right j with z2[j]==z2p[i] and z3[j]==z3p[i]
        adj=[[j for j in range(m) if z2[j]==z2p[i] and z3[j]==z3p[i]] for i in range(m)]
        match_r=[-1]*m
        def try_k(u, seen):
            for v in adj[u]:
                if seen[v]: continue
                seen[v]=True
                if match_r[v]==-1 or try_k(match_r[v], seen):
                    match_r[v]=u; return True
            return False
        for u in range(m):
            seen=[False]*m
            if not try_k(u, seen): return False
        return True

    incompat=0; found=0
    for (z2,z2p,pis2) in pairs2:
        for (z3,z3p,pis3) in pairs3:
            if pis2 & pis3: continue
            incompat+=1
            if has_common_sigma(z2,z2p,z3,z3p):
                print(" FOUND MIXING:", z2, "->", z2p, sorted(pis2), "|", z3, "->", z3p, sorted(pis3), flush=True)
                found+=1
                if found>=3: break
        if found>=3: break
    print(f" RESULT m={m}: incompatible pairs={incompat}, mixing with common sigma found={found}")
    return found

for m in [int(x) for x in sys.argv[1:]]:
    main(m)
