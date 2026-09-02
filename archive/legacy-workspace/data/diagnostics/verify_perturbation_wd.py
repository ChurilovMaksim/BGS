"""
RUN 31: VERIFY perturbation -> WD across MULTIPLE primes.
Tests robustness of Run 30 breakthrough.
"""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys, os, json
import numpy as np
sys.path.insert(0, _BGS_ROOT + r"\src")
from catmap_core import U_cat
from scipy.optimize import linear_sum_assignment
from scipy.stats import kstest

ART=_BGS_ROOT + r"\artifacts"


def test_prime(p, A=[2,1,1,1], eps=1e-4, min_cluster=15, seed=0):
    rng=np.random.default_rng(seed)
    U=U_cat(A,p)
    w0=np.linalg.eigvals(U)
    X=rng.normal(size=(p,p))+1j*rng.normal(size=(p,p))
    E=(X+X.conj().T)/2
    Up=U+eps*E/np.linalg.norm(E)
    wp=np.linalg.eigvals(Up)
    C=np.abs(wp[:,None]-w0[None,:])
    ri,ci=linear_sum_assignment(C)
    splits={}
    for i,j in zip(ri,ci):
        key=(round(float(w0[j].real),4),round(float(w0[j].imag),4))
        splits.setdefault(key,[]).append(float(np.angle(wp[i])))
    big=sorted([sorted(v) for v in splits.values() if len(v)>=min_cluster],
               key=len,reverse=True)[:3]
    all_sp=[]
    cluster_sizes=[]
    for arr in big:
        arr=np.array(arr); sp=np.diff(arr); sp=sp/sp.mean()
        all_sp.extend(sp.tolist()); cluster_sizes.append(len(arr))
    sp=np.sort(np.array(all_sp))
    ks_wd,_=kstest(sp,lambda x:1-np.exp(-np.pi*x**2/4))
    ks_pois,_=kstest(sp,lambda x:1-np.exp(-x))
    return dict(p=p,n_spacings=len(sp),
                clusters=cluster_sizes,
                ks_wd=float(ks_wd), ks_poiss=float(ks_pois))


def main():
    print("=== RUN 31 multi-prime verification ===")
    results=[]
    primes_with_small_K=[2207,1597,2161,3001]
    for p in primes_with_small_K:
        try:
            r=test_prime(p,seed=p)
            results.append(r)
            verdict="WD" if r["ks_wd"]<r["ks_poiss"] else "?"
            print(f"p={p}: n={r['n_spacings']}, "
                  f"KS_WD={r['ks_wd']:.4f}, KS_Pois={r['ks_poiss']:.4f} "
                  f"[{verdict}]")
        except Exception as e:
            print(f"p={p}: error {e}")
    json.dump(results, open(os.path.join(ART,"run31_multiprime.json"),"w"),
              indent=1)


if __name__=="__main__":
    main()
