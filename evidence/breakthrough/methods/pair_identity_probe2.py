import json, numpy as np, sys
sys.path.insert(0,'/home/hatch/workspace/bgs-breakthrough/methods')
from collections import defaultdict

def kernel_mod(m,mod):
    res=[]
    for a in range(mod):
        for b in range(mod):
            seq=[a,b]
            for _ in range(m):
                seq.append((6*seq[-1]-seq[-2])%mod)
            if seq[m]==a and seq[m+1]==b:
                res.append(seq[:m])
    return np.array(res,dtype=np.int64)
def crt_combine(A,mod_a,B,mod_b,m):
    inv=pow(mod_a,-1,mod_b)
    diff=(B[None,:,:]-A[:,None,:])%mod_b
    t=(diff*inv)%mod_b
    return (A[:,None,:]+mod_a*t).reshape(-1,m)
def crt_pts(m,mods):
    pts=kernel_mod(m,mods[0]); cur=mods[0]
    for mod in mods[1:]:
        pts=crt_combine(pts,cur,kernel_mod(m,mod),mod,m); cur*=mod
    return pts
def V4_tors_AP(m):
    # v_i = a + i*d in Z/4, m*d=0; lift to 0..3; z = Hv/4
    out=[]
    for a in range(4):
        for d in range(4):
            if (m*d)%4!=0: continue
            v=tuple((a+i*d)%4 for i in range(m))
            hv=tuple(6*v[i]-v[(i-1)%m]-v[(i+1)%m] for i in range(m))
            assert all(x%4==0 for x in hv), (m,a,d,v,hv)
            out.append(tuple(x//4 for x in hv))
    return out
def D4_orbit(vec):
    t=len(vec); res=set()
    for b in range(t):
        res.add(tuple(vec[(r+b)%t] for r in range(t)))
        res.add(tuple(vec[(-r+b)%t] for r in range(t)))
    return res
def check_full(m,mods,D):
    pts=crt_pts(m,mods)
    assert len(pts)==D, (len(pts),D)
    print(f"m={m} pts={len(pts)}",flush=True)
    tors=np.array(V4_tors_AP(m),dtype=np.int64)
    print(f"  |Z|={len(tors)} tors rows (first4)={tors[:,:4].tolist()}",flush=True)
    pair=np.sort(pts@tors.T,axis=1)
    sorted_keys=np.sort(pts,axis=1)
    uniq_fib,fib_id=np.unique(sorted_keys,axis=0,return_inverse=True); fib_id=np.asarray(fib_id).reshape(-1)
    n_fib=len(uniq_fib)
    import math
    t=math.gcd(m,4)
    # class sums over +4 orbits: classes = i mod t (t|m so well defined)
    Y=np.zeros((len(pts),t),dtype=np.int64)
    for r in range(t):
        Y[:,r]=pts[:,r::t].sum(axis=1) if False else pts[:,[i for i in range(m) if i%t==r]].sum(axis=1)
    def varying(arr):
        if arr.ndim==1: arr=arr.reshape(-1,1)
        comb=np.concatenate([fib_id.reshape(-1,1).astype(np.int64),arr.astype(np.int64)],axis=1)
        uc=np.unique(comb,axis=0); cnt=np.bincount(uc[:,0],minlength=n_fib)
        return int((cnt>1).sum())
    print(f"  t={t} fibers={n_fib} pair_sorted varying={varying(pair)} sortedY varying={varying(np.sort(Y,axis=1))} Y varying={varying(Y)}",flush=True)
    # D_t orbit check (t=1 trivial, t=2: D2 = both perms, t=4: D4 as above)
    bad=0; tot=0
    # group indices by fiber using dict on fib_id (slow-ish but ok for 39k)
    by=defaultdict(list)
    for i,f in enumerate(fib_id): by[int(f)].append(i)
    for f,idx in by.items():
        base=tuple(Y[idx[0]].tolist()); orb=D4_orbit(base)
        for i in idx:
            tot+=1
            if tuple(Y[i].tolist()) not in orb: bad+=1
    print(f"  Y in D_t-orbit of fiber-first Y: violations={bad}/{tot}",flush=True)

check_full(4,[9,128],1152)
check_full(6,[32,25,49],39200)

# ---- m=12 lifts of mod-81 bad fiber ----
from gluing_components import fix_mod
m=12; D=1536796800; q=81; M=D//q; inv=pow(M%q,-1,q)
def phi(t): return (t*M*inv)%D
vecs=fix_mod(m,q)
by=defaultdict(list)
for v in vecs: by[tuple(sorted(v))].append(v)
bad=[(s,vs) for s,vs in by.items() if len({tuple(sorted(v)) for v in vs})>=0 and len(vs)>0]
# find aff-bad: use canon from gluing_components
from gluing_components import aff_perms, canon
perms=aff_perms(m)
target=None
for s,vs in by.items():
    cs={canon(v,perms,m) for v in vs}
    if len(cs)>1: target=(s,vs,cs); break
s,vs,cs=target
print(f"m=12 mod81 bad fiber: sorted={s} nvec={len(vs)} ncanon={len(cs)}",flush=True)
lifts=[tuple(phi(t) for t in v) for v in vs]
assert all(tuple(sorted(y))==tuple(sorted(lifts[0])) for y in lifts)
tors12=np.array(V4_tors_AP(12),dtype=np.int64)
print("  |Z12|=",len(tors12),flush=True)
# compare tors set with oprime_m12 tors_z
mj=json.load(open('/home/hatch/workspace/bgs-breakthrough/methods/oprime_m12_counterexample_result.json'))
print("  tors match oprime_m12 json:", set(map(tuple,tors12.tolist()))==set(map(tuple,mj['tors_z'])),flush=True)
pairs=[tuple(sorted(int(np.dot(np.array(y),z)) for z in tors12)) for y in lifts]
print("  pair_sorted identical across all lifts:", len(set(pairs))==1,flush=True)
Y12=np.array([[sum(y[i] for i in range(12) if i%4==r) for r in range(4)] for y in lifts],dtype=np.int64)
print("  Y lifts:\n",Y12.tolist(),flush=True)
base=tuple(Y12[0].tolist()); orb=D4_orbit(base)
print("  all Y in D4-orbit of first:", all(tuple(row.tolist()) in orb for row in Y12),flush=True)
print("  sorted Y identical:", len({tuple(sorted(row.tolist())) for row in Y12})==1,flush=True)
