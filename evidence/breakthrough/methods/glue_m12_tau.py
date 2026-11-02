import json, itertools
from collections import defaultdict
m=12
def fix_mod(q):
    res=[]
    for a in range(q):
        for b in range(q):
            seq=[a,b]
            for _ in range(m):
                seq.append((6*seq[-1]-seq[-2])%q)
            if seq[m]==a and seq[m+1]==b:
                v=tuple(seq[:m])
                if all((6*v[i]-v[(i-1)%m]-v[(i+1)%m])%q==0 for i in range(m)):
                    res.append(v)
    return res
def dihedral_perms(m):
    perms=[]
    for k in range(m):
        perms.append(tuple((j+k)%m for j in range(m)))
        perms.append(tuple((k-j)%m for j in range(m)))
    return sorted(set(perms))
DIH=set(dihedral_perms(m))
def apply_perm(v,p):
    return tuple(v[p[j]] for j in range(m))

FIX={q:fix_mod(q) for q in [128,81,25,49,121]}
FIXSET={q:set(v) for q,v in FIX.items()}
# fibers for 121
fib=defaultdict(list)
for v in FIX[121]: fib[tuple(sorted(v))].append(v)
print("q121 fibers:", {k:len(v) for k,v in fib.items()})

def gen_taus(v,w):
    # tau[j] in positions i with v[i]==w[j], all distinct
    cand=[]
    for j in range(m):
        cand.append([i for i in range(m) if v[i]==w[j]])
    out=[]
    used=[False]*m
    tau=[0]*m
    def bt(j):
        if j==m:
            out.append(tuple(tau)); return
        for i in cand[j]:
            if not used[i]:
                used[i]=True; tau[j]=i; bt(j+1); used[i]=False
    bt(0)
    return out

taus=set()
for key,vs in fib.items():
    for v in vs:
        for w in vs:
            for t in gen_taus(v,w):
                taus.add(t)
print("tau candidates from q121:", len(taus), "dihedral among them:", len(taus & DIH))
# filter: tau must have S_q nonempty for all q
def has_S(q,tau):
    Fs=FIXSET[q]
    for v in FIX[q]:
        if apply_perm(v,tau) in Fs:
            return True
    return False

survivors=[]
for tau in taus:
    if tau in DIH: continue
    ok=True
    for q in [25,49,81,128]:
        if not has_S(q,tau):
            ok=False; break
    if ok:
        survivors.append(tau)
print("surviving non-dihedral taus (all components have some v with v∘tau in Fix):", len(survivors))
json.dump({"taus_total":len(taus),"survivors":[list(t) for t in survivors]}, open('/home/hatch/workspace/bgs-breakthrough/methods/glue_m12_taus.json','w'))
for t in survivors[:20]: print(t)
