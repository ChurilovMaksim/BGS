from collections import Counter
def mul(x,y,m): return ((x[0]*y[0]+2*x[1]*y[1])%m, (x[0]*y[1]+x[1]*y[0])%m)
def tr(C): return (2*C[0])
B=(17,12)
def beta_pows(m,n):
    r=[(1,0)]; 
    for _ in range(n): r.append(mul(r[-1],B,m))
    return r
def trseq(C,m,n):
    bp=beta_pows(m,n)
    return tuple((2*(mul(C,bp[k],m)[0]))%m for k in range(n))
def dihedral(C,m,per):
    # rotations beta^k C, conjugates, negations; per = period length bound (15 or 5)
    bp=beta_pows(m,per); out=set()
    for k in range(per):
        D=mul(C,bp[k],m); Dc=(D[0],(-D[1])%m)
        for E in (D,Dc):
            out.add(E); out.add(((-E[0])%m,(-E[1])%m))
    return out
# ---- Check 1: 29-side ----
m=29; per=5
params=[(a,b) for a in range(m) for b in range(m)]
seqs={C:trseq(C,m,per) for C in params}
bad1=[]
for C in params:
    s=seqs[C]; pm=Counter(s)+Counter(((-v)%m for v in s))
    for D in params:
        md=Counter(seqs[D])
        if all(md[v]<=pm[v] for v in md):
            # D's cycle values fit in +-s; is D dihedral to C or -C?
            if D not in dihedral(C,m,per) and D not in dihedral(((-C[0])%m,(-C[1])%m),m,per):
                bad1.append((C,D,seqs[C],seqs[D]))
print('CHECK1 29-side: exceptions =',len(bad1))
for e in bad1[:10]: print('  ',e)
# ---- Check 2: 25-side fibers (generic C: nonzero, not in 5R) ----
m=25
def fibers(C):
    t=trseq(C,m,15)
    return Counter(tuple(sorted((t[j],t[j+5],t[j+10]))) for j in range(5))
params25=[(a,b) for a in range(m) for b in range(m)]
generic=[C for C in params25 if C!=(0,0) and not (C[0]%5==0 and C[1]%5==0)]
fib={C:fibers(C) for C in params25}
bad2=[]
for C in generic:
    for D in params25:
        if fib[D]==fib[C] and D not in dihedral(C,m,15):
            bad2.append((C,D))
print('CHECK2 25-fibers generic: exceptions =',len(bad2))
for e in bad2[:10]: print('  ',e)
# ---- Check 3: 25-side single component, values in +-t ----
bad3=[]
for C in params25:
    t=trseq(C,m,15); pm=Counter(t)+Counter(((-v)%m for v in t))
    for D in params25:
        md=Counter(trseq(D,m,15))
        if all(md[v]<=pm[v] for v in md):
            if D in dihedral(C,m,15): continue
            # scaling? D = lam*C for unit lam, C pure-sqrt2?
            pure = (C[0]==0)
            scal=False
            if pure:
                for lam in range(m):
                    if (lam*lam)%m==1 or True:
                        pass
                # check D = lam*C mod 25 for some unit lam
                for lam in range(m):
                    if (lam*C[1])%m==D[1] and D[0]==0 and (lam%5 in (1,4) or True):
                        # need lam unit
                        import math
                        if math.gcd(lam,m)==1: scal=True
            if not scal: bad3.append((C,D))
print('CHECK3 25-single: non-dihedral non-scaling exceptions =',len(bad3))
for e in bad3[:10]: print('  ',e)
