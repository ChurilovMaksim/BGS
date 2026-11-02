import numpy as np, math, collections
def fix_pts_np(m,q):
    A,B = np.meshgrid(np.arange(q), np.arange(q), indexing='ij')
    a=A.ravel().astype(np.int64); b=B.ravel().astype(np.int64)
    seqs=[a,b]
    for _ in range(m):
        seqs.append((6*seqs[-1]-seqs[-2])%q)
    ok=(seqs[m]==a)&(seqs[m+1]==b)
    return np.stack([s[ok] for s in seqs[:m]],axis=1), np.stack([a[ok],b[ok]],axis=1)

def d4_canonical(Yrow):
    t=len(Yrow); best=None
    for b in range(t):
        for sgn in (1,-1):
            w=tuple(Yrow[(sgn*i+b)%t] for i in range(t))
            if best is None or w<best: best=w
    return best

for m,q in [(8,512),(12,128),(16,2048)]:
    if m==16:
        # q=2048 seeds 4M too large for numpy grid? 2048^2=4.2M x 16 steps ok maybe memory ~ 4M*8*16*8 bytes ~500MB too large. skip if heavy
        print("skip m=16 q=2048 for now"); continue
    pts,seeds=fix_pts_np(m,q)
    t=math.gcd(m,4)
    Y=np.zeros((len(pts),t),dtype=np.int64)
    for i in range(m):
        Y[:,i%t]=(Y[:,i%t]+pts[:,i])%q
    canons=collections.Counter(d4_canonical(tuple(y)) for y in Y)
    print(f"m={m} q={q} pts={len(pts)} distinctY={len(np.unique(Y,axis=0))} Y-D4-orbits={len(canons)} orbit size dist={collections.Counter(canons.values())}")
    # multisets count
    byms={}
    for idx,v in enumerate(pts):
        byms.setdefault(tuple(sorted(v.tolist())),[]).append(idx)
    print(f"   multisets={len(byms)}")
    # Check: does Y-canonical determine multiset? i.e. same Y-canon -> same multiset?
    bycanon={}
    bad=0
    for idx,v in enumerate(pts):
        c=d4_canonical(tuple(Y[idx].tolist()))
        ms=tuple(sorted(v.tolist()))
        if c in bycanon and bycanon[c]!=ms: bad+=1
        bycanon.setdefault(c,ms)
    print(f"   Y-canon -> multiset conflicts: {bad} (0 means Y orbit determines multiset)")
    # Power sums: does multiset determine Y-canon? already Lemma Y. Check sum of squares per multiset vs Y?
    # For each multiset, print Y canon and power sums p1,p2 mod q
    # Also check: seed (v0,d) parameters: v0, d=v1-3v0 mod q, scaled?
    # For m=8, seeds are multiples of 8; print (v0//8, d//8 mod64) for points in one multiset
    if m==8:
        for ms,idxs in list(byms.items())[:2]:
            print("  multiset example, points:")
            for i in idxs[:8]:
                v=pts[i]; s=seeds[i]
                print(f"    seed={s.tolist()} v0//8={s[0]//8} d//8={(s[1]-3*s[0])%q//8} Y={Y[i].tolist()} canon={d4_canonical(tuple(Y[i].tolist()))}")
