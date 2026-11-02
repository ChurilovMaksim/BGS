from collections import Counter
import math
def mul(x,y,m): return ((x[0]*y[0]+2*x[1]*y[1])%m, (x[0]*y[1]+x[1]*y[0])%m)
B=(17,12)
def beta_pows(m,n):
    r=[(1,0)]
    for _ in range(n): r.append(mul(r[-1],B,m))
    return r
def trseq(C,m,n):
    bp=beta_pows(m,n)
    return tuple((2*mul(C,bp[k],m)[0])%m for k in range(n))
def dihedral(C,m,per):
    bp=beta_pows(m,per); out=set()
    for k in range(per):
        D=mul(C,bp[k],m); Dc=(D[0],(-D[1])%m)
        for E in (D,Dc):
            out.add(E); out.add(((-E[0])%m,(-E[1])%m))
    return out
m=25; per=15
params=[(a,b) for a in range(m) for b in range(m)]
M={C:Counter(trseq(C,m,per)) for C in params}
def neg(C): return ((-C[0])%m,(-C[1])%m)
other=[]; scaling=[]; ndih=0
for C in params:
    T=M[C]+M[neg(C)]
    dih=dihedral(C,m,per)  # dihedral already closed under negation
    for D in params:
        if M[D]+M[neg(D)]==T:
            if D in dih: ndih+=1; continue
            scal=False
            if C[0]==0 and D[0]==0:
                for lam in range(m):
                    if math.gcd(lam,m)==1 and (lam*C[1])%m==D[1]: scal=True
            if scal: scaling.append((C,D))
            else: other.append((C,D))
print('dihedral matches:',ndih)
print('scaling-classified:',len(scaling))
print('OTHER exceptions:',len(other))
for e in other[:20]: print('  ',e)
# also: what are the scaling pairs? check lam values
lams=set()
for (C,D) in scaling:
    for lam in range(m):
        if math.gcd(lam,m)==1 and (lam*C[1])%m==D[1]: lams.add(lam)
print('scaling lams:',sorted(lams))
