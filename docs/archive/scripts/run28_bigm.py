"""
RUN 28: SPECTRAL TEST AT LARGE m using small-order primes.
"""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import sys, os, json
import numpy as np
sys.path.insert(0, _BGS_ROOT + r"\src")
from catmap_core import U_cat
from master_formula_r4 import weyl_matrix, projector_eigenspace

ART=_BGS_ROOT + r"\artifacts"


def main():
    print("=== RUN 28 large-m spectral ===")
    results=[]
    for p,K in [(2207,9)]:
        A=[2,1,1,1]
        U=U_cat(A,p)
        T10=weyl_matrix(1,0,p); T01=weyl_matrix(0,1,p)
        V=T10+T10.conj().T+0.7*(T01+T01.conj().T)
        spaces=projector_eigenspace(U,tol=1e-4)
        lam,Pl,m=max(spaces,key=lambda t:t[2])
        u,s,vh=np.linalg.svd(Pl)
        basis=u[:,:m]
        W=basis.conj().T@(V@basis)
        mu=np.trace(W)/m
        W=W-mu*np.eye(m,dtype=complex)
        Wn=W/np.sqrt(m)
        ev=np.linalg.eigvalsh(Wn)
        # KS distance to semicircle on [-2,2]
        bins=np.linspace(-2.5,2.5,80)
        hist,_=np.histogram(ev,bins=bins,density=True)
        centers=(bins[:-1]+bins[1:])/2
        target=np.sqrt(np.clip(4-centers**2,0,None))/(2*np.pi)
        # Normalise both to unit integral for fair comparison
        dx=bins[1]-bins[0]
        hist_norm=hist/ (hist.sum()*dx)
        ks=float(np.max(np.abs(hist_norm-target)))
        print(f"p={p} K={K} m={m}: eig range [{ev.min():.3f},{ev.max():.3f}] "
              f"KS={ks:.4f}")
        results.append(dict(p=p,K=K,m=m,ks=ks,
                            eigs_sample=ev[:100].tolist()))
    json.dump(results, open(os.path.join(ART,"run28_bigm.json"),"w"), indent=1)


if __name__=="__main__":
    main()
