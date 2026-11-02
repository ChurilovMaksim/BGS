import json, numpy as np
m=8; D=1331712; MODS=(9,289,512)
def kernel_mod(mod):
    res=[]
    for a in range(mod):
        for b in range(mod):
            seq=[a,b]
            for _ in range(m):
                seq.append((6*seq[-1]-seq[-2])%mod)
            if seq[m]==a and seq[m+1]==b:
                res.append(seq[:m])
    return np.array(res,dtype=np.int64)
kernels=[kernel_mod(mod) for mod in MODS]
def crt_combine(A,mod_a,B,mod_b):
    inv=pow(mod_a,-1,mod_b)
    diff=(B[None,:,:]-A[:,None,:])%mod_b
    t=(diff*inv)%mod_b
    return (A[:,None,:]+mod_a*t).reshape(-1,m)
pts=crt_combine(kernels[0],9,kernels[1],289)
pts=crt_combine(pts,9*289,kernels[2],512)
print("pts",pts.shape,flush=True)
Hy=6*pts-np.roll(pts,1,axis=1)-np.roll(pts,-1,axis=1)
assert np.all(Hy%D==0)
w=Hy//D
sorted_keys=np.sort(pts,axis=1)
uniq_fib,fib_id=np.unique(sorted_keys,axis=0,return_inverse=True)
fib_id=np.asarray(fib_id).reshape(-1)
n_fib=len(uniq_fib)
print("fibers",n_fib,flush=True)
# class sums
Y=np.zeros((len(pts),4),dtype=np.int64)  # y sums mod4 classes
W=np.zeros((len(pts),4),dtype=np.int64)
for r in range(4):
    Y[:,r]=pts[:,r::4].sum(axis=1)
    W[:,r]=w[:,r::4].sum(axis=1)
Ey=pts[:,0::2].sum(axis=1); Oy=pts[:,1::2].sum(axis=1)
Ew=w[:,0::2].sum(axis=1); Ow=w[:,1::2].sum(axis=1)
# V4 / tors via brute for m=8 is 65536, fine
V4=[]
for code in range(4**m):
    v=[];c=code
    for i in range(m):
        v.append(c%4);c//=4
    hv=[6*v[i]-v[(i-1)%m]-v[(i+1)%m] for i in range(m)]
    if all(x%4==0 for x in hv):
        V4.append(v)
print("V4",len(V4),flush=True)
tors=np.array([[ (6*v[i]-v[(i-1)%m]-v[(i+1)%m])//4 for i in range(m)] for v in V4],dtype=np.int64)
print("tors:\n",tors,flush=True)
pair=np.sort(pts@tors.T,axis=1)
def varies(arr):
    # arr: (N,) or (N,k); count fibers with >1 distinct value
    if arr.ndim==1: arr=arr.reshape(-1,1)
    uniq,inv=np.unique(np.concatenate([fib_id.reshape(-1,1),arr],axis=1),axis=0,return_inverse=False),None
    # simpler: use dict-free approach: unique rows of (fib,arr) count per fiber via np.unique on combined
    combined=np.concatenate([fib_id.reshape(-1,1).astype(np.int64),arr.astype(np.int64)],axis=1)
    uc=np.unique(combined,axis=0)
    cnt=np.bincount(uc[:,0],minlength=n_fib)
    return int((cnt>1).sum()), cnt
for name,arr in [("pair_sorted",pair),("Y (mod4 sums)",Y),("sorted Y",np.sort(Y,axis=1)),
                 ("W (mod4 sums)",W),("sorted W",np.sort(W,axis=1)),
                 ("Ey",Ey),("Ew",Ew),("Ey+Oy total",Ey+Oy)]:
    nv,cnt=varies(arr)
    print(f"{name}: fibers varying = {nv} / {n_fib}",flush=True)
# For bad fibers specifically, show examples: first bad fiber points
# find fiber with >1 gamma orbit: need gamma canon
gam_perms=[]
for k in range(8):
    gam_perms.append([(j+k)%8 for j in range(8)]); gam_perms.append([(k-j)%8 for j in range(8)])
gam_perms=np.array(gam_perms,dtype=np.int64)
def lex_canon(arr):
    out=np.empty_like(arr); CH=50000
    for s in range(0,len(arr),CH):
        chunk=arr[s:s+CH]
        permuted=np.stack([chunk[:,p] for p in gam_perms],axis=1)
        mask=np.ones((len(chunk),len(gam_perms)),dtype=bool)
        for c in range(arr.shape[1]):
            vals=np.where(mask,permuted[:,:,c],np.iinfo(np.int64).max)
            mask&=(permuted[:,:,c]==vals.min(axis=1,keepdims=True))
        chosen=mask.argmax(axis=1)
        out[s:s+CH]=permuted[np.arange(len(chunk)),chosen]
    return out
gam_canon=lex_canon(pts)
uniq_gam,gam_id=np.unique(gam_canon,axis=0,return_inverse=True); gam_id=np.asarray(gam_id).reshape(-1)
gam_fiber=np.empty(len(uniq_gam),dtype=np.int64); gam_fiber[gam_id]=fib_id
orbits=np.bincount(gam_fiber,minlength=n_fib)
bad=np.where(orbits>1)[0]
print("bad fibers",len(bad),flush=True)
# show first 3 bad fibers: Y, W, Ey, pair for each orbit representative
for bf in bad[:3]:
    idx=np.where(fib_id==bf)[0]
    print(f"\nBAD fiber {bf} key={uniq_fib[bf]} points={len(idx)}")
    seen=set()
    for i in idx:
        g=int(gam_id[i])
        if g in seen: continue
        seen.add(g)
        print(f"  orbit rep y={pts[i].tolist()} Ey={Ey[i]} Oy={Oy[i]} Y={Y[i].tolist()} W={W[i].tolist()} Ew={Ew[i]} pair={pair[i].tolist()}")
json.dump({"n_fib":int(n_fib),"bad":int(len(bad))},open('/home/hatch/workspace/bgs-breakthrough/methods/pair_fiber_probe_summary.json','w'))
