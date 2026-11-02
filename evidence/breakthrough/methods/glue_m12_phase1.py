import json, random
from collections import defaultdict, Counter
m=12
D=1536796800
QS=[128,81,25,49,121]
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
DIH=dihedral_perms(m)
DIHSET=set(DIH)
def apply_perm(v,p): return tuple(v[p[j]] for j in range(m))
def canon_gamma(v): return min(apply_perm(v,p) for p in DIH)
FIX={q:fix_mod(q) for q in QS}
FIXSET={q:set(v) for q,v in FIX.items()}
# tau set from q121, non-constant only (tau_count<=20000, which for 121 is all non-constant)
def tau_count(v):
    import math; prod=1
    for n in Counter(v).values(): prod*=math.factorial(n)
    return prod
fib=defaultdict(list)
for v in FIX[121]: fib[tuple(sorted(v))].append(v)
taus=set()
for key,vs in fib.items():
    for v in vs:
        if tau_count(v)>20000: continue
        pos_by_val=defaultdict(list)
        for i,val in enumerate(v): pos_by_val[val].append(i)
        for w in vs:
            cand=[pos_by_val[w[j]] for j in range(m)]
            used=[False]*m; tau=[0]*m
            def bt(j):
                if j==m: taus.add(tuple(tau)); return
                for i in cand[j]:
                    if not used[i]:
                        used[i]=True; tau[j]=i; bt(j+1); used[i]=False
            bt(0)
taus=[t for t in taus if t not in DIHSET]
print("non-dihedral taus from q121:", len(taus), flush=True)
# CRT
def crt_vec(comp):
    # comp: dict q->vector
    out=[]
    for j in range(m):
        x=0
        for q in QS:
            Mq=D//q; inv=pow(Mq,-1,q)
            x=(x+comp[q][j]*Mq*inv)%D
        out.append(x)
    return tuple(out)
def w_of(y):
    # Hy/D as integers, y in 0..D-1 representatives
    w=[]
    for i in range(m):
        val=6*y[i]-y[(i-1)%m]-y[(i+1)%m]
        assert val%D==0, (val,D)
        w.append(val//D)
    return tuple(w)

found=[]
checked=0
for tau in taus:
    S={}
    ok=True
    for q in QS:
        lst=[v for v in FIX[q] if apply_perm(v,tau) in FIXSET[q]]
        S[q]=lst
        if not lst: ok=False; break
    if not ok: continue
    checked+=1
    # generic combo: max distinct values, non-zero preferred
    comp={}
    for q in QS:
        cand=[v for v in S[q] if any(v)]
        if not cand: cand=S[q]
        comp[q]=max(cand, key=lambda v: len(set(v)))
    y=crt_vec(comp)
    y2=tuple(y[tau[j]] for j in range(m))
    if canon_gamma(y)!=canon_gamma(y2):
        wy=w_of(y); wy2=w_of(y2)
        found.append({"tau":tau,"comp":{str(q):comp[q] for q in QS},"y":y,"y2":y2,
                      "w_sorted":sorted(wy),"w2_sorted":sorted(wy2),"pw_separates":sorted(wy)!=sorted(wy2)})
        print("FOUND generic:", found[-1], flush=True)
        break
print("taus checked (all S nonempty):", checked, "found:", len(found))
json.dump(found, open('/home/hatch/workspace/bgs-breakthrough/methods/glue_m12_phase1_found.json','w'), indent=1)
