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
DIH=set(bytes(p) for p in dihedral_perms(m))
FIX={q:fix_mod(q) for q in [128,81,25,49,121]}
def tau_count(v):
    prod=1
    for n in Counter(v).values(): prod*=math.factorial(n)
    return prod
sets={}
for q in [121,25,49,81,128]:
    fib=defaultdict(list)
    for v in FIX[q]: fib[tuple(sorted(v))].append(v)
    s=set()
    for key,vs in fib.items():
        for v in vs:
            if tau_count(v)>20000: continue
            pos_by_val=defaultdict(list)
            for i,val in enumerate(v): pos_by_val[val].append(i)
            for w in vs:
                cand=[pos_by_val[w[j]] for j in range(m)]
                used=[False]*m; tau=[0]*m
                def bt(j):
                    if j==m:
                        s.add(bytes(tau)); return
                    for i in cand[j]:
                        if not used[i]:
                            used[i]=True; tau[j]=i; bt(j+1); used[i]=False
                bt(0)
    sets[q]=s
    print(f"q={q} tau_set={len(s)}", flush=True)
inter=set.intersection(*sets.values())
print("intersection all 5:", len(inter), "non-dihedral:", len(inter-DIH))
json.dump([list(t) for t in sorted(inter-DIH)], open('/home/hatch/workspace/bgs-breakthrough/methods/glue_m12_tau_inter.json','w'))
# also pairwise intersections with 121
for q in [25,49,81,128]:
    print(f"121 & {q}:", len(sets[121]&sets[q]))
