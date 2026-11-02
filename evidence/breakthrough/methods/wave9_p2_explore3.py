import numpy as np, math, collections

def fix_pts_np(m,q):
    A,B = np.meshgrid(np.arange(q), np.arange(q), indexing='ij')
    a=A.ravel().astype(np.int64); b=B.ravel().astype(np.int64)
    seqs=[a,b]
    for _ in range(m):
        seqs.append((6*seqs[-1]-seqs[-2])%q)
    ok=(seqs[m]==a)&(seqs[m+1]==b)
    pts=np.stack([s[ok] for s in seqs[:m]],axis=1)
    return pts

def d4_orbit_tuple(tup):
    t=len(tup); orb=set()
    for b in range(t):
        orb.add(tuple(tup[(i+b)%t] for i in range(t)))
        orb.add(tuple(tup[(-i+b)%t] for i in range(t)))
    return orb

for m,q in [(8,512),(12,128),(8,64),(12,32),(16,128)]:
    pts=fix_pts_np(m,q)
    t=math.gcd(m,4)
    byms={}
    for idx,v in enumerate(pts):
        byms.setdefault(tuple(sorted(v.tolist())),[]).append(idx)
    # per-class multisets: for each point, tuple of sorted class multisets (as tuple of tuples)
    bad_class=0; bad_class_examples=[]
    for ms,idxs in byms.items():
        # canonical per-class multiset up to D4: compute set of D4-orbits of the tuple-of-multisets
        def class_ms(v):
            return tuple(tuple(sorted(v[i::t].tolist())) if False else tuple(sorted([v[j] for j in range(m) if j%t==r])) for r in range(t))
        # note: classes are i%t, but step: indices i with i%t==r
        cms=set()
        for i in idxs:
            cm=class_ms(pts[i])
            # D4 orbit of cm (tuple of tuples)
            orb=d4_orbit_tuple(cm)
            cms.add(tuple(sorted(orb)) if False else min(orb))  # representative: min element of orbit
        if len(cms)>1:
            bad_class+=1
            if len(bad_class_examples)<3:
                bad_class_examples.append((ms,idxs,cms))
    print(f"m={m} q={q} |Fix|={len(pts)} multisets={len(byms)} bad_perclass_multisets={bad_class}")
    for ms,idxs,cms in bad_class_examples:
        print("  example total ms:",ms)
        for i in idxs[:6]:
            v=pts[i]
            cm=tuple(tuple(sorted([v[j] for j in range(m) if j%t==r])) for r in range(t))
            print("   pt",v.tolist(),"class_ms",cm)
