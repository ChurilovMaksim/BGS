import math
from collections import defaultdict
ALPHA=(3,2); M_CASE=36; Q2,Q=128,729
def mul(a,b,M): return ((a[0]*b[0]+2*a[1]*b[1])%M,(a[0]*b[1]+a[1]*b[0])%M)
def conj(a,M): return (a[0]%M,(-a[1])%M)
def pw(a,n,M):
    r=(1,0)
    for _ in range(n): r=mul(r,a,M)
    return r
def tr(a,M): return (2*a[0])%M
def genuine(M,m):
    d=pw(ALPHA,m,M); delta=((d[0]-1)%M,d[1])
    return [(x,y) for x in range(M) for y in range(M) if mul(delta,(x,y),M)==(0,0)]
def ann_m(M,m):
    pows=[pw(ALPHA,n,M) for n in range(m)]
    return {(x,y) for x in range(M) for y in range(M) if all(tr(mul((x,y),p,M),M)==0 for p in pows)}
def order(a,M):
    cur=(1,0)
    for j in range(1,1000000):
        cur=mul(cur,a,M)
        if cur==(1,0): return j
    raise RuntimeError
m=M_CASE; t=math.gcd(m,4); S=m//t
alphas2=[pw(ALPHA,r,Q2) for r in range(t)]; alphasq=[pw(ALPHA,r,Q) for r in range(t)]
betas2=[pw(pw(ALPHA,t,Q2),s,Q2) for s in range(S)]; betasq=[pw(pw(ALPHA,t,Q),s,Q) for s in range(S)]
G2,Gq=genuine(Q2,m),genuine(Q,m)
A2,Aq=ann_m(Q2,m),ann_m(Q,m)
print(f"|G128|={len(G2)} |G729|={len(Gq)} |Ann128|={len(A2)} |Ann729|={len(Aq)}",flush=True)
def tables(G,M,alphas,betas):
    out={}
    for A in G:
        tab=[]
        for r in range(t):
            base=mul(A,alphas[r],M)
            tab.append(tuple(tr(mul(base,betas[s],M),M) for s in range(S)))
        out[A]=tuple(tab)
    return out
T2=tables(G2,Q2,alphas2,betas2); Tq=tables(Gq,Q,alphasq,betasq)
groups=defaultdict(list)
for a2 in G2:
    ptab=T2[a2]
    for aq in Gq:
        otab=Tq[aq]
        sig=tuple(tuple(sorted(zip(ptab[r],otab[r]))) for r in range(t))
        groups[sig].append((a2,aq))
sizes=sorted(len(v) for v in groups.values())
print(f"pairs={len(G2)*len(Gq)} groups={len(groups)} min={sizes[0]} max={sizes[-1]} singletons={sum(1 for s in sizes if s==1)}",flush=True)
o2,oq=order(ALPHA,Q2),order(ALPHA,Q); L=o2*oq//math.gcd(o2,oq)
print(f"ord128={o2} ord729={oq} L={L}",flush=True)
pow2=[(1,0)]
for _ in range(L): pow2.append(mul(pow2[-1],ALPHA,Q2))
def coverage(shadow_q,label):
    bad=[]
    for sig,members in groups.items():
        A0=members[0]; tabs=[]
        for c in (0,1):
            tab=defaultdict(list); base=conj(A0[1],Q) if c else A0[1]; cur=base
            for j in range(oq):
                tab[cur].append(j); cur=mul(cur,ALPHA,Q)
            tabs.append(tab)
        for A in members:
            ok=False
            for c in (0,1):
                base2=conj(A0[0],Q2) if c else A0[0]
                for w in shadow_q:
                    target=((A[1][0]-w[0])%Q,(A[1][1]-w[1])%Q)
                    for j0 in tabs[c].get(target,[]):
                        j=j0
                        while j<L:
                            b2=mul(base2,pow2[j],Q2)
                            d2=((A[0][0]-b2[0])%Q2,(A[0][1]-b2[1])%Q2)
                            if d2 in A2: ok=True; break
                            j+=oq
                        if ok: break
                    if ok: break
                if ok: break
            if not ok: bad.append((A0,A)); break
    print(f"{label}: escapes={len(bad)}/{len(groups)}",flush=True)
    for A0,A in bad[:3]: print(f"  rep {A0} member {A}",flush=True)
    return bad
coverage({(0,0)},"orbit+Ann only")
coverage({(27*a%Q,27*b%Q) for a in range(3) for b in range(3)},"orbit+Ann+{27D:D in R/3R}")
coverage({(27*a%Q,27*b%Q) for a in range(9) for b in range(9)},"orbit+Ann+{27D:D in R/9R}")
coverage({(81*a%Q,81*b%Q) for a in range(9) for b in range(9)},"orbit+Ann+{81D:D in R/9R}")
