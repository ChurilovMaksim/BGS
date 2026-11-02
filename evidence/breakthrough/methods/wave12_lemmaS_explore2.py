# Test pure-combinatorial step (2): profile preservation => stabilizer correction, for RANDOM M.
import random
from collections import Counter
def d4():
    out=[]
    for b in range(4):
        for sgn in (1,-1):
            pi=tuple((sgn*i+b)%4 for i in range(4))
            if pi not in out: out.append(pi)
    return out
PIS=d4()
def vtypes():
    seen=set(); out=[]
    for a in range(3):
        for b in range(3):
            v=(a,b,(-a)%3,(-b)%3)
            if v not in seen: seen.add(v); out.append(v)
    return out
def blocks_of(v):
    d={}
    for r,val in enumerate(v): d.setdefault(val,[]).append(r)
    return [set(x) for x in d.values()]
random.seed(7)
fails=0; total=0; ex=[]
for trial in range(200000):
    # random M: 4 multisets of size 3 over values 0..5
    M=tuple(tuple(sorted(random.randrange(6) for _ in range(3))) for _ in range(4))
    Stab=[d for d in PIS if all(M[d[r]]==M[r] for r in range(4))]
    for v in vtypes():
        Fb=blocks_of(v)
        for gamma in PIS:
            # profile preservation: for each block F, multiset {M_r: r in F} == {M_r: r in gamma(F)}
            ok=True
            for F in Fb:
                gF={gamma[s] for s in F}
                if Counter(M[s] for s in F)!=Counter(M[s] for s in gF): ok=False; break
            if not ok: continue
            total+=1
            good=False
            for delta in Stab:
                if all({delta[gamma[s]] for s in F}==F for F in Fb): good=True; break
            if not good:
                fails+=1
                if len(ex)<5: ex.append((M,v,gamma,Stab))
print(f"profile-preserving cases={total} fails={fails}")
for e in ex: print("EX",e)
