"""
RUN 38 AUDIT-4: Verify eigenvalue matching in perturbation experiment.
Check that clusters are correctly tracked; spacings are within-cluster.
"""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys, os, json
import numpy as np
sys.path.insert(0, _BGS_ROOT + r"\src")
from catmap_core import U_cat
from scipy.optimize import linear_sum_assignment

ART=_BGS_ROOT + r"\artifacts"


def main():
    rng=np.random.default_rng(99)
    p=2207; A=[2,1,1,1]
    print("Computing eig(U)...")
    U=U_cat(A,p)
    w0=np.linalg.eigvals(U)
    X=rng.normal(size=(p,p))+1j*rng.normal(size=(p,p))
    E=(X+X.conj().T)/2

    # Two different eps values -> matched clusters should agree
    results={}
    for eps in [1e-5, 1e-4]:
        Up=U+eps*E/np.linalg.norm(E)
        wp=np.linalg.eigvals(Up)
        C=np.abs(wp[:,None]-w0[None,:])
        ri,ci=linear_sum_assignment(C)
        splits={}
        maxdist=0
        for i,j in zip(ri,ci):
            d=C[i,j]; maxdist=max(maxdist,d)
            key=(round(float(w0[j].real),4),round(float(w0[j].imag),4))
            splits.setdefault(key,[]).append(float(np.angle(wp[i])))
        sizes=sorted([len(v) for v in splits.values()],reverse=True)[:5]
        results[eps]=dict(max_match_dist=float(maxdist),
                          top_cluster_sizes=sizes)
        print(f"eps={eps}: max match dist={maxdist:.2e}, "
              f"top cluster sizes={sizes}")
    # Consistency check: same clusters found at both eps?
    s1=set(results[1e-5]["top_cluster_sizes"])
    s2=set(results[1e-4]["top_cluster_sizes"])
    print(f"cluster-size overlap between eps runs: {s1 & s2}")
    json.dump(results, open(os.path.join(ART,"run38_matching.json"),"w"),
              indent=1)


if __name__=="__main__":
    main()
