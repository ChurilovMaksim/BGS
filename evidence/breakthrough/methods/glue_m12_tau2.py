import json, math
from collections import defaultdict, Counter
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

def tau_count(v):
    c=Counter(v); prod=1
    for n in c.values(): prod*=math.factorial(n)
    return prod

taus=set()
skipped=0
for q in [121,128,81,25,49]:
    fib=defaultdict(list)
    for v in FIX[q]: fib[tuple(sorted(v))].append(v)
    for key,vs in fib.items():
        for v in vs:
            tc=tau_count(v)
            if tc>20000:
                skipped+=1; continue
            # positions by value
            pos_by_val=defaultdict(list)
            for i,val in enumerate(v): pos_by_val[val].append(i)
            for w in vs:
                cand=[]
                for j in range(m):
                    cand.append(pos_by_val[w[j]])
                used=[False]*m; tau=[0]*m; cnt=[0]
                def bt(j):
                    if cnt[0]>=20000: return
                    if j==m:
                        taus.add(tuple(tau)); cnt[0]+=1; return
                    for i in cand[j]:
                        if not used[i]:
                            used[i]=True; tau[j]=i; bt(j+1); used[i]=False
                bt(0)
    print(f"q={q} done, taus so far={len(taus)}, skipped_pairs={skipped}", flush=True)
print("tau candidates total:", len(taus), "dihedral among them:", len(taus & DIH))
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
    for q in [25,49,81,128,121]:
        if not has_S(q,tau):
            ok=False; break
    if ok: survivors.append(tau)
print("surviving non-dihedral taus:", len(survivors))
json.dump({"taus_total":len(taus),"survivors":[list(t) for t in survivors]}, open('/home/hatch/workspace/bgs-breakthrough/methods/glue_m12_taus.json','w'))
for t in survivors[:30]: print(t)
