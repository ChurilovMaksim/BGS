import numpy as np, math, collections
def fix_pts_np(m,q):
    A,B = np.meshgrid(np.arange(q), np.arange(q), indexing='ij')
    a=A.ravel().astype(np.int64); b=B.ravel().astype(np.int64)
    seqs=[a,b]
    for _ in range(m):
        seqs.append((6*seqs[-1]-seqs[-2])%q)
    ok=(seqs[m]==a)&(seqs[m+1]==b)
    return np.stack([s[ok] for s in seqs[:m]],axis=1), np.stack([a[ok],b[ok]],axis=1)

def gamma_canon(v,m):
    best=None
    for k in range(m):
        for sgn in (1,-1):
            w=tuple(v[(sgn*j+k)%m] for j in range(m))
            if best is None or w<best: best=w
    return best

m,q=8,512
pts,seeds=fix_pts_np(m,q)
t=2  # v2(e4)=2
# parameters: T' = v1//8 mod 64, S = ((v0-3*v1)%512)//64 mod 8  (since 2^{4+t}=64)
byms={}
for idx,v in enumerate(pts):
    byms.setdefault(tuple(sorted(v.tolist())),[]).append(idx)
for ms,idxs in byms.items():
    canons={}
    for i in idxs:
        canons.setdefault(gamma_canon(pts[i],m),[]).append(i)
    if len(canons)>1:
        print(f"split multiset pts={len(idxs)}")
        for c,ii in canons.items():
            # list all (T',S) for points in this canon (should be multiple points per canon? canon is orbit, points in orbit have different seeds but same canon vector; pick first)
            i0=ii[0]
            v0,v1=seeds[i0].tolist()
            Tp=(v1//8)%64
            S=((v0-3*v1)%512)//64
            print(f"  canon ex seed=({v0},{v1}) Tp={Tp} S={S} npts_in_canon={len(ii)} pt={pts[i0].tolist()}")
        # also list all Tp,S in each canon
        for c,ii in canons.items():
            pars=set()
            for i in ii:
                v0,v1=seeds[i].tolist()
                pars.add(((v1//8)%64, ((v0-3*v1)%512)//64))
            print(f"   canon params (Tp,S) set size {len(pars)}: {sorted(pars)[:20]}")
