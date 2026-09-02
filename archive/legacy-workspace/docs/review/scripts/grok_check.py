# VERIFY Grok's central claim: exact identity (no asymptotics)
# For fully-matched (+,-,+,-) resonance: sol == #pairings exactly
import json
from sympy import isprime, primitive_root

def n_order(a,p):
    x,o=a,1
    while x!=1: x=x*a%p; o+=1
    return o

def brute_sol(p, H):
    inv={h:pow(h,p-2,p) for h in H}
    L={}
    for h1 in H:
        for h3 in H:
            kk=((h1+h3)%p,(inv[h1]+inv[h3])%p); L[kk]=L.get(kk,0)+1
    tot=0
    for h2 in H:
        for h4 in H:
            kk=((h2+h4)%p,(inv[h2]+inv[h4])%p)   # POSITIVE sums match
            if kk in L: tot+=L[kk]
    return tot

def wd_pairings(k, has_m1):
    return (3*k*(k-1)) if has_m1 else (2*k*k-k)

results=[]
for p in [101,211,4099]:
    g=int(primitive_root(p))
    divs=[d for d in range(2,min(300,p)) if (p-1)%d==0]
    for k in divs[:6]:
        av=pow(g,(p-1)//k,p); assert n_order(av,p)==k
        H=set(); x=1
        for _ in range(k): H.add(x); x=x*av%p
        sol=brute_sol(p,H)
        has_m1=(p-1)in H
        pm=wd_pairings(k,has_m1)
        match="EXACT" if sol==pm else f"MISMATCH diff={sol-pm}"
        results.append({"p":p,"k":k,"sol":sol,"pairings":pm,
                       "has_-1":has_m1,"match":match})
        print(f"p={p} k={k} (-1inH={has_m1}): sol={sol} pairings={pm} -> {match}")

json.dump(results, open("artifacts/grok_identity_check.json","w"), indent=1)
print("\nSaved artifacts/grok_identity_check.json")
