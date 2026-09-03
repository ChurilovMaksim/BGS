"""
RUN 29: MOMENT HIERARCHY done RIGHT.
Use orthonormal basis of eigenspace; normalise W by sqrt(Tr[W^2]/m);
compute rho_m = Tr[W^(2m)] / m / sigma^(2m) and compare to Catalan.
sigma^2 := Tr[W^2]/m.
"""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import sys, os, json
import numpy as np
sys.path.insert(0, _BGS_ROOT + r"\src")
from catmap_core import U_cat
from master_formula_r4 import weyl_matrix

ART=_BGS_ROOT + r"\artifacts"


def catalan(n):
    from math import comb
    return comb(2*n,n)//(n+1)


def get_compressed_W(p, K, A=[2,1,1,1]):
    U=U_cat(A,p)
    w,v=np.linalg.eig(U)
    from collections import Counter
    keys=Counter([(round(float(x.real),5),round(float(x.imag),5)) for x in w])
    key,_=keys.most_common(1)[0]
    idxs=[i for i,x in enumerate(w) if abs(x-complex(*key))<1e-4]
    m=len(idxs)
    B=v[:,idxs]
    T10=weyl_matrix(1,0,p); T01=weyl_matrix(0,1,p)
    V=T10+T10.conj().T+0.7*(T01+T01.conj().T)
    W=B.conj().T@(V@B)
    mu=np.trace(W)/m
    return W-mu*np.eye(m,dtype=complex), m


def main():
    print("=== RUN 29 moment hierarchy correct ===")
    results=[]
    for p,K in [(2207,9),(1597,9),(2161,11)]:
        try:
            W,m=get_compressed_W(p,K)
        except MemoryError:
            continue
        tr2=float(np.real(np.trace(W@W)))
        sig2=tr2/m
        row=dict(p=p,m=m,sigma2=sig2,moments={})
        print(f"\np={p} m={m}: sigma^2={sig2:.5f}")
        print(f"{'m':>3} {'rho_m':>12} {'Catalan':>8} {'ratio':>8}")
        for mm in [1,2,3,4]:
            tr=float(np.real(np.trace(np.linalg.matrix_power(W,2*mm))))
            rho=tr/m/(sig2**mm) if sig2>0 else 0
            cat=catalan(mm)
            ratio=rho/cat if cat>0 else 0
            row["moments"][mm]=dict(rho=rho,catalan=cat,ratio=ratio)
            print(f"{mm:>3} {rho:>12.5f} {cat:>8} {ratio:>8.4f}")
        results.append(row)
    json.dump(results, open(os.path.join(ART,"run29_moments.json"),"w"), indent=1)


if __name__=="__main__":
    main()
