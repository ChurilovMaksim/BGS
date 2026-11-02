import numpy as np, math, collections, itertools

def fix_pts_np(m,q):
    # seeds grid
    A,B = np.meshgrid(np.arange(q), np.arange(q), indexing='ij')
    a=A.ravel().astype(np.int64); b=B.ravel().astype(np.int64)
    seqs=[a,b]
    for _ in range(m):
        seqs.append((6*seqs[-1]-seqs[-2])%q)
    ok=(seqs[m]==a)&(seqs[m+1]==b)
    pts=np.stack([s[ok] for s in seqs[:m]],axis=1)
    seeds=np.stack([a[ok],b[ok]],axis=1)
    return pts,seeds

def Yvecs(pts,m):
    t=math.gcd(m,4)
    Y=np.zeros((len(pts),t),dtype=np.int64)
    for i in range(m):
        Y[:,i%t]=(Y[:,i%t]+pts[:,i])%q
    return Y

def gamma_canon(v,m):
    # lexicographic min over dihedral perms j-> +/-j+k, action v'_j = v_{p[j]} ? need consistent; use both conventions? For orbit counting use permutations of positions: tuple sorted by permuted vector
    best=None
    for k in range(m):
        for sgn in (1,-1):
            w=tuple(v[(sgn*j+k)%m] for j in range(m))
            if best is None or w<best: best=w
    return best

for m,q in [(8,512),(12,128)]:
    pts,seeds=fix_pts_np(m,q)
    print(f"\nm={m} q={q} |Fix|={len(pts)}")
    # divisibility of entries
    print("  gcd of all entries:", np.gcd.reduce(pts.ravel()) if len(pts) else None)
    Y=Yvecs(pts,m)
    print("  distinct Y:", len(np.unique(Y,axis=0)))
    # group by multiset
    byms={}
    for idx,v in enumerate(pts):
        ms=tuple(sorted(v.tolist()))
        byms.setdefault(ms,[]).append(idx)
    multi=[(ms,idxs) for ms,idxs in byms.items() if len(idxs)>1]
    print(f"  multisets={len(byms)} multisets with >1 point={len(multi)} max pts per multiset={max(len(vv) for vv in byms.values())}")
    # For multisets with >1 point, count gamma canons and Y orbits
    t=math.gcd(m,4)
    def d_orbit(Yrow):
        orb=set()
        for b in range(t):
            orb.add(tuple(Yrow[(i+b)%t] for i in range(t)))
            orb.add(tuple(Yrow[(-i+b)%t] for i in range(t)))
        return orb
    ex=0
    for ms,idxs in multi[:5]:
        canons=set(gamma_canon(pts[i],m) for i in idxs)
        ys=set(tuple(Y[i].tolist()) for i in idxs)
        print(f"   ex ms size {len(idxs)} pts, gamma_canons={len(canons)}, distinct Y={len(ys)}, Ys={list(ys)[:4]}")
    # seeds sharing multiset: relation?
    # print first multiset with multiple gamma canons
    cnt=0
    for ms,idxs in byms.items():
        canons={}
        for i in idxs:
            canons.setdefault(gamma_canon(pts[i],m),[]).append(i)
        if len(canons)>1:
            cnt+=1
            if cnt<=3:
                print(f"  SPLIT multiset (gamma>1): pts={len(idxs)} canons={len(canons)}")
                for c,ii in canons.items():
                    print(f"    canon seed={seeds[ii[0]].tolist()} Y={Y[ii[0]].tolist()} example pt={pts[ii[0]].tolist()}")
    print(f"  total split multisets (gamma>1): {cnt}")
