# Verify (a) pair-profile lemma at L=6, (b) segment decomposition formulas, (c) Lemma S for blocks at L=5.
from collections import Counter
def block_vals(T,D,Q,P):
    c=[1,3]; e=[0,1]
    for _ in range(P):
        c.append((6*c[-1]-c[-2])%Q); e.append((6*e[-1]-e[-2])%Q)
    return [ (T*c[s]+D*e[s])%Q for s in range(P) ]
def classes(B,P):
    return tuple(tuple(sorted(B[j] for j in range(P) if j%4==r)) for r in range(4))
# (a) PL at L=6
L=6; Q=2**(L+3); P=2**L
bad=0; tot=0
for T in range(Q):
    for D in range(0,Q,8):
        B=block_vals(T,D,Q,P); M=classes(B,P)
        pairs=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
        unions={}
        for pr in pairs:
            unions.setdefault(tuple(sorted(M[pr[0]]+M[pr[1]])),[]).append(pr)
        for u,prs in unions.items():
            for i in range(len(prs)):
                for j in range(i+1,len(prs)):
                    tot+=1
                    if tuple(sorted([M[prs[i][0]],M[prs[i][1]]]))!=tuple(sorted([M[prs[j][0]],M[prs[j][1]]])):
                        bad+=1
print(f"(a) L=6 pair-union collisions={tot} profile-mismatch={bad}")
# (b) decomposition check at t+1 from t: pick random blocks, verify M_r = F_r + (F_r+2^t delta), theta parity
import random
random.seed(3)
ok=True
for trial in range(200):
    t=random.randint(5,9); Q2=2**(t+1); Mlen=2**(t-3); P2=2*Mlen
    T=random.randrange(Q2); D=random.randrange(0,Q2,8)
    B=block_vals(T,D,Q2,P2)
    tau=(T>>t)&1; dtop=(D>>t)&1; d=(D//8)&1; T2=T&1
    for r in range(4):
        first=[B[s] for s in range(Mlen) if s%4==r]
        second=[B[s+Mlen] for s in range(Mlen) if s%4==r]
        delta=((d + T2*(r%2))%2)
        theta=((tau + dtop*(r%2))%2)
        # first-half values mod 2^t should be level-t segment; top bit of first-half values = theta for all in class?
        tops=set((v>>t)&1 for v in first)
        if tops!={theta}: ok=False; print("theta fail",trial,t,T,D,r,tops,theta)
        # second = first + 2^t*delta mod 2^(t+1)
        if sorted(second)!=sorted([(v + (2**t)*delta)%Q2 for v in first]): ok=False; print("delta fail",trial)
print(f"(b) decomposition formulas ok={ok}")
# (c) Lemma S for blocks at L=5
def d4():
    out=[]
    for b in range(4):
        for sgn in (1,-1):
            pi=tuple((sgn*i+b)%4 for i in range(4))
            if pi not in out: out.append(pi)
    return out
PIS=d4()
L=5; Q=2**(L+3); P=2**L
vtypes=[]
for a in range(3):
    for b in range(3):
        v=(a,b,(-a)%3,(-b)%3)
        if v not in vtypes: vtypes.append(v)
fails=0; total=0
for T in range(Q):
    for D in range(0,Q,8):
        B=block_vals(T,D,Q,P); M=classes(B,P)
        Stab=[d for d in PIS if all(M[d[r]]==M[r] for r in range(4))]
        for v in vtypes:
            blocks={}
            for r,val in enumerate(v): blocks.setdefault(val,[]).append(r)
            Fb=[set(x) for x in blocks.values()]
            for gamma in PIS:
                good=True
                for F in Fb:
                    if Counter(x for s in F for x in M[s])!=Counter(x for s in F for x in M[gamma[s]]): good=False; break
                if not good: continue
                total+=1
                if not any(all({delta[gamma[s]] for s in F}==F for F in Fb) for delta in Stab):
                    fails+=1; print("FAIL",T,D,v,gamma)
print(f"(c) L=5 Lemma S for blocks: gamma-cases={total} fails={fails}")
