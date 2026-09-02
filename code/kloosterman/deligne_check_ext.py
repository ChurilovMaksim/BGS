import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import json, os, sys
import numpy as np
from sympy import isprime

ART = _BGS_ROOT + r"\artifacts"
rng = np.random.default_rng(555)

def count_N(p, lam, mu):
    xs = np.arange(1, p, dtype=np.int64)
    inv = np.array([pow(int(x), p - 2, p) for x in xs], dtype=np.int64)
    K12a = (lam[0]*xs[:,None] + lam[1]*xs[None,:]) % p
    K12b = (mu[0]*inv[:,None] + mu[1]*inv[None,:]) % p
    key12 = (K12a*p + K12b).ravel(); del K12a, K12b
    K34a = ((-lam[2])*xs[:,None] - lam[3]*xs[None,:]) % p
    K34b = ((-mu[2])*inv[:,None] - mu[3]*inv[None,:]) % p
    key34 = (K34a*p + K34b).ravel(); del K34a, K34b
    key12.sort(); key34.sort()
    i=j=cnt=0; n1,n2=len(key12),len(key34)
    while i<n1 and j<n2:
        if key12[i]==key34[j]:
            ii=i
            while ii<n1 and key12[ii]==key12[i]: ii+=1
            jj=j
            while jj<n2 and key34[jj]==key34[j]: jj+=1
            cnt += (ii-i)*(jj-j); i,j=ii,jj
        elif key12[i]<key34[j]: i+=1
        else: j+=1
    return cnt

out={"cases":[]}
# regime sweep: p grid + degeneracy parameter eps (labels nearly equal)
for p in (1013, 2053, 4099, 8191):
    if not isprime(p): continue
    lam=[int(v) for v in rng.integers(1,p,size=4)]
    mu=[int(v) for v in rng.integers(1,p,size=4)]
    N=count_N(p,lam,mu)
    d=abs(N-(p-1)**4/p**2)
    out["cases"].append({"p":p,"type":"generic","ratio":float(d/p**1.5)})
    print(f"p={p}: generic ratio={d/p**1.5:.3f}")
    # near-degenerate: lam2 = lam1 + delta etc (approaching Wigner locus)
    for dd in (int(p*0.01)+1, int(p*0.05)+1):
        lam2=list(lam); lam2[1]=(lam[0]+dd)%p
        mu2=list(mu); mu2[1]=(mu[0]+dd)%p
        N2=count_N(p,lam2,mu2)
        d2=abs(N2-(p-1)**4/p**2)
        out["cases"].append({"p":p,"type":f"near_deg_{dd}","ratio":float(d2/p**1.5)})
        print(f"   near-deg d={dd:5d}: ratio={d2/p**1.5:.3f}")
json.dump(out, open(os.path.join(ART,"deligne_check_ext.json"),"w"), indent=1)
print("saved artifacts/deligne_check_ext.json")
