import math
def mul(x,y,P): return ((x[0]*y[0]+2*x[1]*y[1])%P,(x[0]*y[1]+x[1]*y[0])%P)
def tr(x,P): return (2*x[0])%P
def alpha_pow(i,P):
    r=(1,0); a=(3,2)
    for _ in range(i): r=mul(r,a,P)
    return r
for m,P in [(36,27),(12,81)]:
    powers=[alpha_pow(i,P) for i in range(m)]
    data={}
    for a in range(P):
        for b in range(P):
            A=(a,b); y=tuple(tr(mul(A,ai,P),P) for ai in powers); data[A]=y
    groups={}
    for A,y in data.items(): groups.setdefault(tuple(sorted(y)),[]).append(A)
    print(f"=== m={m} P={P} groups={len(groups)}")
    for ms,As in groups.items():
        Ns=set((a*a-2*b*b)%P for (a,b) in As)
        if len(Ns)>1:
            print(" group size",len(As),"Ns",sorted(Ns),"Ns mod 9",sorted(set(n%9 for n in Ns)) if P>=9 else None,"Ns mod 3",sorted(set(n%3 for n in Ns)))
            print("  multiset",ms[:12],"...")
