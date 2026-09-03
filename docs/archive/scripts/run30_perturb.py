"""
RUN 30: PERTURBED SPECTRUM - does splitting follow WD?
Eigenvalues of U_A are degenerate in clusters. Add eps*random unitary,
measure spacing statistics WITHIN each cluster after unfolding.
"""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import sys, os, json
import numpy as np
sys.path.insert(0, _BGS_ROOT + r"\src")
from catmap_core import U_cat

ART=_BGS_ROOT + r"\artifacts"


def unfold(levels):
    """Simple unfolding by cumulative count."""
    s=np.sort(levels); n=len(s)
    return np.arange(1,n+1)/n, s


def main():
    rng=np.random.default_rng(42)
    print("=== RUN 30 perturbed spectrum ===")
    p=101; A=[2,1,1,1]
    U=U_cat(A,p)
    w0=np.linalg.eigvals(U)
    phases0=np.angle(w0); phases0=np.sort(phases0)

    # Build random Hermitian perturbation
    X=rng.normal(size=(p,p))+1j*rng.normal(size=(p,p))
    Eps=(X+X.conj().T)/2  # Hermitian

    eps=0.0001
    Upert=U+eps*Eps/np.linalg.norm(Eps)
    # Re-unitarise approximately via QR? For small eps just take phases.
    wp=np.linalg.eigvals(Upert)
    ph=np.sort(np.angle(wp))

    # Cluster: group phases within tol
    tol=0.002
    clusters=[]; cur=[ph[0]]
    for x in ph[1:]:
        if x-cur[-1]<tol: cur.append(x)
        else: clusters.append(cur); cur=[x]
    clusters.append(cur)
    big=[c for c in clusters if len(c)>=5]
    print(f"clusters >=5 levels: {len(big)}")

    results=[]
    for ci,c in enumerate(big[:3]):
        arr=np.array(c)
        # Spacings inside cluster
        sp=np.diff(arr); sp=sp/sp.mean()
        sp=np.sort(sp)
        n=len(sp)
        # Compare with GOE Wigner surmise P(s)=pi/2*s*exp(-pi*s^2/4)
        from scipy.stats import kstest
        cdf=lambda x: 1-np.exp(-np.pi*x**2/4)   # Wigner surmise CDF
        stat,pv=kstest(sp,cdf)
        print(f"cluster {ci}: n={n} mean_s={sp.mean():.3f} "
              f"KS={stat:.4f} p={pv:.4f}")
        results.append(dict(cluster=ci,n=n,mean=float(sp.mean()),
                            ks=float(stat),pvalue=float(pv),
                            spacings=sp.tolist()))
    json.dump(results, open(os.path.join(ART,"run30_perturb.json"),"w"),
              indent=1)


if __name__=="__main__":
    main()
