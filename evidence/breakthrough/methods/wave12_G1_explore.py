import math, collections

def seqs(m,P):
    # alpha powers (c_i,d_i) mod P
    c,d=1,0
    powers=[]
    for i in range(m):
        powers.append((c,d))
        c,d=(3*c+4*d)%P,(2*c+3*d)%P
    out={}
    for a in range(P):
        for b in range(P):
            y=tuple((2*(a*c+2*b*d))%P for (c,d) in powers)
            out[(a,b)]=y
    return out

def dcanon(per, t):
    # per: tuple of sorted tuples per class
    best=None
    for b in range(t):
        rot=tuple(per[(i+b)%t] for i in range(t))
        ref=tuple(per[(-i+b)%t] for i in range(t))
        for cand in (rot,ref):
            if best is None or cand<best: best=cand
    return best

def check(m,P):
    t=math.gcd(m,4)
    data=seqs(m,P)
    groups={}
    for A,y in data.items():
        groups.setdefault(tuple(sorted(y)),[]).append((A,y))
    bad=0; total=0
    # invariants varying within group?
    n_var=0; groups_with_nvar=0
    for ms, lst in groups.items():
        total+=1
        canons=set()
        for A,y in lst:
            per=tuple(tuple(sorted(y[i] for i in range(m) if i%t==r)) for r in range(t))
            canons.add(dcanon(per,t))
        if len(canons)>1:
            bad+=1
            print(" BAD group", ms, "canons", canons, "As", [A for A,_ in lst])
        Ns=set((a*a-2*b*b)%P for A,_ in lst for (a,b) in [A])
        if len(Ns)>1:
            groups_with_nvar+=1
    print(f"m={m} P={P} t={t} As={len(data)} groups={total} bad={bad} groups_with_N_variation={groups_with_nvar}")
    # order of alpha mod P
    c,d=1,0
    L=None
    for i in range(1,5000):
        c,d=(3*c+4*d)%P,(2*c+3*d)%P
        if c==1 and d==0:
            L=i; break
    print("  order alpha mod P:", L, " m/L:", m/L if L else None)
    # order mod p
    p=None
    # find prime divisor: P is prime power
    for q in range(2,100):
        if P%q==0: p=q; break
    c,d=1,0
    L0=None
    for i in range(1,5000):
        c,d=(3*c+4*d)%p,(2*c+3*d)%p
        if c==1 and d==0:
            L0=i; break
    print("  p=",p," order mod p:", L0)
    return groups, data

for (m,P) in [(12,9),(42,49),(36,27)]:
    check(m,P)
