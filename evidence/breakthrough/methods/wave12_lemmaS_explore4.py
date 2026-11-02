# Explore F_r (first-half) structure: is F_r determined by A_r? What is phi split?
from collections import Counter
def block_vals(T,D,Q,P):
    c=[1,3]; e=[0,1]
    for _ in range(P):
        c.append((6*c[-1]-c[-2])%Q); e.append((6*e[-1]-e[-2])%Q)
    return [ (T*c[s]+D*e[s])%Q for s in range(P) ]
import random
random.seed(11)
# Q1: within a block at level t+1, for first-half positions, does value mod 2^t determine value mod 2^(t+1)?
bad_within=0; tot_within=0
for trial in range(300):
    t=random.randint(5,9); Q2=2**(t+1); Mlen=2**(t-3); P2=2*Mlen
    T=random.randrange(Q2); D=random.randrange(0,Q2,8)
    B=block_vals(T,D,Q2,P2)
    first=B[:Mlen]
    groups={}
    for v in first:
        groups.setdefault(v%(2**t),set()).add(v)
    for b,s in groups.items():
        tot_within+=1
        if len(s)>1: bad_within+=1
print(f"Q1: first-half groups by mod 2^t: {tot_within}, with >1 lift: {bad_within}")
# Q2: A_r == A_r' => F_r == F_r' ?
bad2=0; tot2=0
for trial in range(300):
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
                tot2+=1
                if F[r]!=F[rp]: bad2+=1
print(f"Q2: A-equal class pairs: {tot2}, F-differ: {bad2}")
# Q3: phi split structure: for each class r, per b: (phi0, phi1). Print a few examples + check phi0-phi1 pattern
for trial in range(3):
    t=6; Q2=2**(t+1); Mlen=2**(t-3); P2=2*Mlen
    T=random.randrange(Q2); D=random.randrange(0,Q2,8)
    B=block_vals(T,D,Q2,P2)
    print(f"--- trial t={t} T={T} D={D} delta-parity: d={(D//8)&1} T2={T&1}")
    for r in range(4):
        vals=[B[s] for s in range(Mlen) if s%4==r]
        cnt=Counter()
        for v in vals: cnt[(v%(2**t), (v>>t)&1)]+=1
        bs=sorted(set(v%(2**t) for v in vals))
        splits=[(b, cnt[(b,0)], cnt[(b,1)]) for b in bs]
        print(f"  r={r} splits(b,phi0,phi1)={splits}")
