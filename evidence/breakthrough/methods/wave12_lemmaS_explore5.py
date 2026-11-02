# Refined: is F_r determined by (A_r, parity)? And M_r by (A_r, parity, delta)?
from collections import Counter
def block_vals(T,D,Q,P):
    c=[1,3]; e=[0,1]
    for _ in range(P):
        c.append((6*c[-1]-c[-2])%Q); e.append((6*e[-1]-e[-2])%Q)
    return [ (T*c[s]+D*e[s])%Q for s in range(P) ]
import random
random.seed(23)
stat={}
for trial in range(400):
    t=random.randint(5,9); Q2=2**(t+1); Mlen=2**(t-3); P2=2*Mlen
    T=random.randrange(Q2); D=random.randrange(0,Q2,8)
    B=block_vals(T,D,Q2,P2)
    F={}; A={}
    for r in range(4):
        vals=[B[s] for s in range(Mlen) if s%4==r]
        F[r]=tuple(sorted(vals)); A[r]=tuple(sorted(v%(2**t) for v in vals))
    for r in range(4):
        for rp in range(r+1,4):
            if A[r]==A[rp]:
                key=('same-parity' if (r%2)==(rp%2) else 'diff-parity')
                d=stat.setdefault(key,[0,0]); d[0]+=1
                if F[r]!=F[rp]: d[1]+=1
print("A-equal pairs: F-differ by parity:",stat)
# Also: M_r determined by (A_r, parity, delta)? Check full level-(t+1) class multisets:
stat2={}
for trial in range(400):
    t=random.randint(5,9); Q2=2**(t+1); Mlen=2**(t-3); P2=2*Mlen
    T=random.randrange(Q2); D=random.randrange(0,Q2,8)
    B=block_vals(T,D,Q2,P2)
    d=(D//8)&1; T2=T&1
    Mfull={}; A={}
    for r in range(4):
        vals=[B[s] for s in range(P2) if s%4==r]
        Mfull[r]=tuple(sorted(vals))
        fvals=[B[s] for s in range(Mlen) if s%4==r]
        A[r]=tuple(sorted(v%(2**t) for v in fvals))
    delta={r:((d + T2*(r%2))%2) for r in range(4)}
    for r in range(4):
        for rp in range(r+1,4):
            if A[r]==A[rp] and delta[r]==delta[rp]:
                key=('same-parity' if (r%2)==(rp%2) else 'diff-parity')
                dd=stat2.setdefault(key,[0,0]); dd[0]+=1
                if Mfull[r]!=Mfull[rp]: dd[1]+=1
print("A-equal & delta-equal pairs: Mfull-differ by parity:",stat2)
# Q: in PL collisions at level t+1, what happens? Collect collision examples with A-matching type and parity pattern
L=5; Q=2**(L+3); P=2**L
ncol=0; examples=[]
for T in range(Q):
    for D in range(0,Q,8):
        B=block_vals(T,D,Q,P)
        M=tuple(tuple(sorted(B[j] for j in range(P) if j%4==r)) for r in range(4))
        pairs=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
        unions={}
        for pr in pairs: unions.setdefault(tuple(sorted(M[pr[0]]+M[pr[1]])),[]).append(pr)
        for u,prs in unions.items():
            for i in range(len(prs)):
                for j in range(i+1,len(prs)):
                    ncol+=1
                    if len(examples)<8: examples.append((T,D,prs[i],prs[j]))
print(f"L=5 collisions={ncol} examples={examples}")
