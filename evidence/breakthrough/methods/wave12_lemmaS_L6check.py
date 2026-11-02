# Direct Lemma S check for blocks at L=6 (32768 blocks).
def block_vals(T,D,Q,P):
    c=[1,3]; e=[0,1]
    for _ in range(P):
        c.append((6*c[-1]-c[-2])%Q); e.append((6*e[-1]-e[-2])%Q)
    return [ (T*c[s]+D*e[s])%Q for s in range(P) ]
def d4():
    out=[]
    for b in range(4):
        for sgn in (1,-1):
            pi=tuple((sgn*i+b)%4 for i in range(4))
            if pi not in out: out.append(pi)
    return out
PIS=d4()
L=6; Q=2**(L+3); P=2**L
vtypes=[]
for a in range(3):
    for b in range(3):
        v=(a,b,(-a)%3,(-b)%3)
        if v not in vtypes: vtypes.append(v)
fails=0; total=0
for T in range(Q):
    for D in range(0,Q,8):
        B=block_vals(T,D,Q,P)
        M=tuple(tuple(sorted(B[j] for j in range(P) if j%4==r)) for r in range(4))
        Stab=[d for d in PIS if all(M[d[r]]==M[r] for r in range(4))]
        for v in vtypes:
            blocks={}
            for r,val in enumerate(v): blocks.setdefault(val,[]).append(r)
            Fb=[set(x) for x in blocks.values()]
            for gamma in PIS:
                good=True
                for F in Fb:
                    if tuple(sorted(x for s in F for x in M[s]))!=tuple(sorted(x for s in F for x in M[gamma[s]])): good=False; break
                if not good: continue
                total+=1
                if not any(all({delta[gamma[s]] for s in F}==F for F in Fb) for delta in Stab):
                    fails+=1; print("FAIL",T,D,v,gamma)
print(f"L=6 Lemma S for blocks: gamma-cases={total} fails={fails}")
