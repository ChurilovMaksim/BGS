"""
RUN 21: DIRECT SPECTRAL DISTRIBUTION of W vs semicircle.
Compute eigenvalues of centered compressed operator W, normalise,
compare empirical density with Wigner semicircle.
"""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import sys, os, json
import numpy as np
sys.path.insert(0, _BGS_ROOT + r"\src")
from catmap_core import U_cat
from master_formula_r4 import build_V, projector_eigenspace

ART=_BGS_ROOT + r"\artifacts"

def semicircle(x):
    """Standard semicircle density on [-2,2]."""
    return np.sqrt(np.clip(4-x*x, 0, None))/(2*np.pi)

def main():
    print("=== RUN 21: spectral distribution ===")
    results=[]
    for p in (211, 401):
        A=[2,1,1,1]
        U=U_cat(A,p)
        Fd={(1,0):1.0+0j,(0,1):0.7+0.3j}
        V=build_V(Fd,p)
        spaces=projector_eigenspace(U)
        # pick largest multiplicity eigenspace
        lam,Pl,m=max(spaces,key=lambda t:t[2])
        Vl=Pl@V@Pl
        mu=complex(np.trace(Vl))/m
        W=Vl-mu*np.eye(p,dtype=complex)
        ev=np.linalg.eigvals(W)/np.sqrt(m)
        # Kolmogorov-Smirnov style distance to semicircle on [-2,2]
        real_ev=ev.real  # take real parts for comparison
        bins=np.linspace(-2.5,2.5,50)
        hist,_=np.histogram(real_ev,bins=bins,density=True)
        centers=(bins[:-1]+bins[1:])/2
        target=semicircle(centers)
        ks=float(np.max(np.abs(hist-target)))
        results.append(dict(p=p,m=m,eigs_real=real_ev[:50].tolist(),
                            ks_distance=ks))
        print(f"p={p} m={m}: KS-distance to semicircle={ks:.4f}")
    json.dump(results, open(os.path.join(ART,"run21_spectral.json"),"w"),
              indent=1)

if __name__=="__main__":
    main()
