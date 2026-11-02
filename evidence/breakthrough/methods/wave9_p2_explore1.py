import itertools, collections, math

def fix_mod(m,q):
    pts=[]
    for a in range(q):
        for b in range(q):
            seq=[a,b]
            for _ in range(m):
                seq.append((6*seq[-1]-seq[-2])%q)
            if seq[m]==a and seq[m+1]==b:
                pts.append(tuple(seq[:m]))
    return pts

def Yvec(v,m):
    t=math.gcd(m,4)
    Y=[0]*t
    for i,x in enumerate(v):
        Y[i%t]=(Y[i%t]+x)
    return tuple(Y)

def D_orbit(Y):
    t=len(Y)
    orb=set()
    for b in range(t):
        orb.add(tuple(Y[(i+b)%t] for i in range(t)))
        orb.add(tuple(Y[(-i+b)%t] for i in range(t)))
    return orb

for m in [8,12]:
    # D_m v2
    # compute D via recurrence s
    s0,s1=2,6
    # s_m
    seq=[2,6]
    for _ in range(m):
        seq.append(6*seq[-1]-seq[-2])
    Dm=seq[m]-2
    print(f"m={m} D={Dm} v2={ (Dm & -Dm).bit_length()-1 if Dm!=0 else 0 } factor odd={Dm//(Dm & -Dm)}")
    for a in range(1,6):
        q=2**a
        pts=fix_mod(m,q)
        print(f"  a={a} q={q} |Fix|={len(pts)} (expect {q} if q|D else ?)")
        # Y distinct
        Ys=collections.Counter(Yvec(v,m) for v in pts)
        print(f"    distinct Y mod q: {len(Ys)}")
        # group by multiset
        byms={}
        bad=0
        for v in pts:
            ms=tuple(sorted(v))
            y=Yvec(v,m)
            byms.setdefault(ms, set()).add(y)
        # check D orbit: for each ms, all Y in one D orbit?
        badms=0
        for ms,yset in byms.items():
            # pick first, check all in its orbit
            y0=next(iter(yset))
            orb=D_orbit(y0)
            if not yset.issubset(orb):
                badms+=1
        print(f"    multisets={len(byms)} bad_multisets={badms}")
