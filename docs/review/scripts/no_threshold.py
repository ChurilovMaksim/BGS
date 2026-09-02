import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
# Test corrected theorem: no threshold on k
# Compute full Tr[V_lam^4] and compare with WD_4 for LARGE k/p^(2/3)
import math, os, sys
import numpy as np
sys.path.insert(0, _BGS_ROOT + r"\src")
from catmap_core import U_cat, ord_pm

def weyl(n1,n2,N):
    w=np.exp(2j*np.pi/N); bi=pow(2,-1,N)
    xs=np.arange(N); sh=np.zeros((N,N),complex)
    sh[xs,(xs-n1)%N]=1.0
    return (w**((n2*xs-bi*n1*n2)%N))[:,None]*sh

results=[]
for (A,p,k_target) in [([2,1,1,1],101,None),
                        ([3,1,2,1],211,None)]:
    U=U_cat(A,p)
    w,v=np.linalg.eig(U)
    # find eigenvalue with largest degeneracy
    vals=[(float(np.real(vv)),float(np.imag(vv))) for vv in w]
    from collections import Counter
    cnt=Counter([(round(a,6),round(b,6)) for a,b in vals])
    lam_key,_=cnt.most_common(1)[0]
    m=sum(1 for a,b in vals if (round(a,6),round(b,6))==lam_key)
    lam=lam_key[0]+1j*lam_key[1]
    Pl=np.zeros((p,p),complex)
    for i,vv in enumerate(w):
        if abs(vv-lam)<1e-5: Pl+=np.outer(v[:,i].conj(),v[:,i])
    V=weyl(1,0,p)+0.7*weyl(0,1,p)
    Vl=Pl@V@Pl
    tr4=float(np.real(np.trace(np.linalg.matrix_power(Vl,4))))
    M2=(abs(1)**4+abs(0.7)**4)
    # crude WD: use 2*M2^2 for GUE-like; refine later
    wd4_crude=2*M2**2
    ratio=k_ratio = m/(p**(2/3))
    results.append({"A":A,"p":p,"k":m,"tr4":tr4,"wd4_crude":wd4_crude,
                   "k_over_p23":round(ratio,2)})
    print(f"A={A} p={p}: k={m}, k/p^(2/3)={ratio:.2f}")
    print(f"  Tr[V_lam^4]={tr4:.3f}  crude WD_4={wd4_crude:.3f}"
          f"  diff/tr4={abs(tr4-wd4_crude)/max(abs(tr4),1):.3f}")

import json
json.dump(results, open("artifacts/run12_no_threshold_check.json","w"), indent=1)
print("\nSaved artifacts/run12_no_threshold_check.json")
