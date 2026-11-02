from collections import Counter, defaultdict
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
def period(v):
    for p in range(1,m+1):
        if m%p==0 and all(v[i]==v[i%p] for i in range(m)): return p
    return m
for q in [128,81,25,49,121]:
    F=fix_mod(q)
    print(f"\nq={q} |Fix|={len(F)}")
    print(" periods:", Counter(period(v) for v in F))
    print(" value-count patterns:", Counter(tuple(sorted(Counter(v).values())) for v in F))
    # first few non-zero
    for v in F[1:4]: print("  ",v, "period",period(v))
    # check reflection symmetry: v[j]==v[-j] ?
    def refl(v): return all(v[j]==v[(-j)%m] for j in range(m))
    print(" reflection-symmetric count:", sum(refl(v) for v in F))
    # check v[j]+v[j+6] constant?
    sums=Counter()
    for v in F:
        sums[tuple((v[j]+v[(j+6)%m])%q for j in range(6))]+=1
    print(" v[j]+v[j+6] patterns (first 3):", list(sums.items())[:3])
