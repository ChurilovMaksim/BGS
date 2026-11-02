import math, collections

def analyze(m,P):
    t=math.gcd(m,4)
    c,d=1,0; powers=[]
    for i in range(m):
        powers.append((c,d)); c,d=(3*c+4*d)%P,(2*c+3*d)%P
    data={}
    for a in range(P):
        for b in range(P):
            y=tuple((2*(a*c+2*b*d))%P for (c,d) in powers)
            data[(a,b)]=y
    groups={}
    for A,y in data.items():
        groups.setdefault(tuple(sorted(y)),[]).append((A,y))
    print(f"=== m={m} P={P} t={t}")
    for ms,lst in groups.items():
        Ns={}
        for A,y in lst:
            a,b=A; Ns.setdefault((a*a-2*b*b)%P,[]).append(A)
        if len(Ns)>1:
            print(" multiset:",ms)
            for N,As in sorted(Ns.items()):
                print("   N=",N," As=",As)
            # per-class for one representative each N
            for N,As in sorted(Ns.items()):
                A=As[0]; y=data[A]
                per=tuple(tuple(sorted(y[i] for i in range(m) if i%t==r)) for r in range(t))
                print("    A",A,"per",per)
            # also A mod p, N mod p
            print("   A mod p / N mod p:")
            # p
            p=min(q for q in range(2,100) if P%q==0)
            for A,y in lst:
                print("    ",A,"modp",(A[0]%p,A[1]%p),"Nmodp",(A[0]*A[0]-2*A[1]*A[1])%p)
            print()
for m,P in [(12,9),(42,49)]:
    analyze(m,P)
