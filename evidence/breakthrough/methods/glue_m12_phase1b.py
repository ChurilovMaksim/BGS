import json, sys
from collections import defaultdict
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
# load taus from previous run? regenerate q121 taus quickly via stored json from tau2? Use glue_m12_taus.json survivors (that was all-component survivors, wrong) - regenerate:
from collections import Counter
import math
def tau_count(v):
    prod=1
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
print("taus:",len(taus), flush=True)
def crt_vec(comp):
    out=[]
    for j in range(m):
        x=0
        for q in QS:
            Mq=D//q; inv=pow(Mq,-1,q)
            x=(x+comp[q][j]*Mq*inv)%D
        out.append(x)
    return tuple(out)
def w_of(y):
    w=[]
    for i in range(m):
        val=6*y[i]-y[(i-1)%m]-y[(i+1)%m]
        assert val%D==0
        w.append(val//D)
    return tuple(w)

found=[]
for ti,tau in enumerate(taus):
    # per component distinct D-subsets
    comp_opts=[]
    feasible=True
    for q in QS:
        opts={}  # frozenset of dihedral indices -> example v
        for v in FIX[q]:
            w=apply_perm(v,tau)
            if w not in FIXSET[q]: continue
            dset=frozenset(i for i,d in enumerate(DIH) if apply_perm(v,d)==w)
            # note: apply_perm(v,d)==w means v∘d = v∘tau
            if dset not in opts: opts[dset]=v
        if not opts: feasible=False; break
        comp_opts.append(list(opts.items()))
    if not feasible: continue
    # backtrack: possible dihedral indices set, try to empty it
    # order components by min subset size
    order=sorted(range(len(QS)), key=lambda qi: min(len(s) for s,_ in comp_opts[qi]))
    sol=[None]
    def bt(idx, possible, chosen):
        if sol[0] is not None: return
        if not possible:
            sol[0]=dict(chosen); return
        if idx==len(order): return
        qi=order[idx]
        for dset,v in comp_opts[qi]:
            newp=possible & set(dset)
            chosen[QS[qi]]=v
            bt(idx+1, newp, chosen)
            del chosen[QS[qi]]
            if sol[0] is not None: return
    bt(0, set(range(len(DIH))), {})
    solution=sol[0]
    if solution is not None:
        comp=solution
        y=crt_vec(comp)
        y2=tuple(y[tau[j]] for j in range(m))
        assert canon_gamma(y)!=canon_gamma(y2), "canon check failed"
        wy=w_of(y); wy2=w_of(y2)
        rec={"tau":tau,"comp":{str(q):comp[q] for q in QS},"y":y,"y2":y2,
             "w_sorted":sorted(wy),"w2_sorted":sorted(wy2),"pw_separates":sorted(wy)!=sorted(wy2),
             "canon_y":canon_gamma(y),"canon_y2":canon_gamma(y2)}
        found.append(rec)
        print("FOUND split for tau",tau, flush=True)
        print(json.dumps(rec, indent=1), flush=True)
        break
    if ti%1000==0: print(f"  {ti} taus processed, found={len(found)}", flush=True)
print("DONE found:",len(found))
json.dump(found, open('/home/hatch/workspace/bgs-breakthrough/methods/glue_m12_phase1b_found.json','w'), indent=1)
