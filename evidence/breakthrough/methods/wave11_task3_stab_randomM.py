# Lemma S fails for arbitrary multisets (not a pure D4 lemma).
# Random M (class multisets size 2 over {0,1,2,3}), random v, all gamma in D4.
import random
def d4():
    out=[]
    for b in range(4):
        for sgn in (1,-1):
            pi=tuple((sgn*i+b)%4 for i in range(4))
            if pi not in out: out.append(pi)
    return out
PIS=d4()
random.seed(1)
fails=0; total=0
for trial in range(30000):
    M=tuple(tuple(sorted(random.randrange(4) for _ in range(2))) for _ in range(4))
    Stab=[d for d in PIS if all(M[d[r]]==M[r] for r in range(4))]
    a,b=random.randrange(3),random.randrange(3)
    v=tuple((a,b,(-a)%3,(-b)%3))
    blocks={}
    for r,val in enumerate(v): blocks.setdefault(val,set()).add(r)
    Fblocks=list(blocks.values())
    for gamma in PIS:
        ok=True
        for F in Fblocks:
            u1=tuple(sorted(x for s in F for x in M[s]))
            u2=tuple(sorted(x for s in F for x in M[gamma[s]]))
            if u1!=u2: ok=False; break
        if not ok: continue
        total+=1
        if not any(all({delta[gamma[s]] for s in F}==F for F in Fblocks) for delta in Stab):
            fails+=1
            if fails<=3: print("FAIL M",M,"v",v,"gamma",gamma,"Stab",Stab)
print(f"gamma-cases={total} fails={fails}")
