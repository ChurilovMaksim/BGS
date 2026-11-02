import numpy as np
from collections import defaultdict
from itertools import product

def fix_mod_q(P, q):
    vecs=[]
    y1_all=np.arange(q, dtype=np.int64)
    for y0 in range(q):
        a=np.full(q, y0, dtype=np.int64); b=y1_all.copy()
        seq=[a.copy(), b.copy()]
        for _ in range(P):
            c=(6*b-a)%q; a,b=b,c; seq.append(b.copy())
        ok=(seq[P]==y0)&(seq[P+1]==y1_all)
        for j in np.where(ok)[0]:
            vecs.append(tuple(int(seq[k][j]) for k in range(P)))
    return vecs

def d4():
    out=[]
    for b in range(4):
        for sgn in (1,-1):
            pi=tuple((sgn*i+b)%4 for i in range(4))
            if pi not in out: out.append(pi)
    return out
PIS=d4()
def per_class(p):
    return tuple(tuple(sorted(p[j] for j in range(len(p)) if j%4==r)) for r in range(4))
def pi_pattern(cp,cpp):
    return [pi for pi in PIS if all(cpp[r]==cp[pi[r]] for r in range(4))]
def pi_v(v,vp):
    return [pi for pi in PIS if all(vp[r]==v[pi[r]] for r in range(4))]
def has_bijective_tau(p,pp,v,vp):
    # matching k -> j with p[j]==pp[k] and v[j%4]==vp[k%4]
    P=len(p)
    adj=[[j for j in range(P) if p[j]==pp[k] and v[j%4]==vp[k%4]] for k in range(P)]
    match_r=[-1]*P
    def try_k(u,seen):
        for w in adj[u]:
            if seen[w]: continue
            seen[w]=True
            if match_r[w]==-1 or try_k(match_r[w],seen):
                match_r[w]=u; return True
        return False
    for u in range(P):
        if not try_k(u,[False]*P): return False
    return True

for P,q in [(8,512)]:
    vecs=fix_mod_q(P,q)
    groups=defaultdict(list)
    for v_ in vecs: groups[tuple(sorted(v_))].append(v_)
    pcs={v_: per_class(v_) for v_ in vecs}
    vtypes=[]
    for a1,b1 in product(range(3), repeat=2):
        vtypes.append(tuple((a1,b1,(-a1)%3,(-b1)%3)))
    found=0; total_pairs=0
    for ms, vs in groups.items():
        for p in vs:
            cp=pcs[p]
            for pp in vs:
                if pp==p: continue
                total_pairs+=1
                cpp=pcs[pp]
                pis_pat=pi_pattern(cp,cpp)
                # v pairs: vp in D4 orbit of v
                for v in vtypes:
                    for pi3 in PIS:
                        vp=tuple(v[pi3[r]] for r in range(4))
                        pis3=pi_v(v,vp)
                        if set(pis_pat)&set(pis3): continue
                        if has_bijective_tau(p,pp,v,vp):
                            print("BIJECTIVE-TAU COUNTEREXAMPLE p=",p,"pp=",pp,"v=",v,"vp=",vp,"pi_pat=",pis_pat,"pi_v=",pis3)
                            found+=1
                            if found>=5: raise SystemExit
    print("P",P,"total pattern pairs",total_pairs,"bijective-tau counterexamples",found)
