"""
RUN 35 AUDIT-2: Verify perturbation -> WD with CORRECT ensemble.
E was COMPLEX Hermitian => GUE, but we tested against GOE surmise!
Redo with both surmises and check which fits.
"""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import sys, os, json
import numpy as np
sys.path.insert(0, _BGS_ROOT + r"\src")
from catmap_core import U_cat
from scipy.optimize import linear_sum_assignment
from scipy.stats import kstest

ART=_BGS_ROOT + r"\artifacts"


def run_case(p, A=[2,1,1,1], eps=1e-4, seed=0, real_perturb=False):
    rng=np.random.default_rng(seed)
    U=U_cat(A,p)
    w0=np.linalg.eigvals(U)
    if real_perturb:
        X=rng.normal(size=(p,p)); E=(X+X.T)/2   # real symmetric = GOE
    else:
        X=rng.normal(size=(p,p))+1j*rng.normal(size=(p,p))
        E=(X+X.conj().T)/2                       # complex Hermitian = GUE
    Up=U+eps*E/np.linalg.norm(E)
    wp=np.linalg.eigvals(Up)
    C=np.abs(wp[:,None]-w0[None,:])
    ri,ci=linear_sum_assignment(C)
    splits={}
    for i,j in zip(ri,ci):
        key=(round(float(w0[j].real),4),round(float(w0[j].imag),4))
        splits.setdefault(key,[]).append(float(np.angle(wp[i])))
    big=sorted([sorted(v) for v in splits.values() if len(v)>=15],
               key=len,reverse=True)[:3]
    all_sp=[]
    for arr in big:
        arr=np.array(arr); sp=np.diff(arr); sp=sp/sp.mean()
        all_sp.extend(sp.tolist())
    sp=np.sort(np.array(all_sp))
    cdf_wd_go=lambda x: 1-np.exp(-np.pi*x**2/4)          # GOE surmise
    cdf_wd_gue=lambda x: 1-(1-np.exp(-4*x**2/np.pi))     # placeholder
    # Proper GUE surmise CDF has erf form; approximate numerically:
    from scipy.special import erf
    def cdf_gue(x):
        # P_GUE(s) = (32/pi^2) s^2 exp(-4 s^2 / pi)
        # integrate numerically via cumulative sum on fine grid
        return None
    ks_go,_=kstest(sp,cdf_wd_go)
    # Numerical GUE CDF
    grid=np.linspace(0,max(sp.max(),5),20000)
    pdf=(32/np.pi**2)*grid**2*np.exp(-4*grid**2/np.pi)
    dx=grid[1]-grid[0]
    cdf_grid=np.cumsum(pdf)*dx; cdf_grid/=cdf_grid[-1]
    from scipy.interpolate import interp1d
    F=interp1d(grid,cdf_grid,bounds_error=False,fill_value=(0,1))
    d=np.abs(F(sp)-np.arange(1,len(sp)+1)/len(sp)).max()
    return dict(p=p,n=len(sp),
                ks_GOE=float(ks_go),
                ks_GUE=float(d))


def main():
    print("=== RUN 35 audit: which surmise? ===")
    res=[]
    for p in [2207,1597,2161,3001]:
        for rp in [False,True]:
            tag="GUE-pert" if not rp else "GOE-pert"
            try:
                r=run_case(p,seed=p,real_perturb=rp)
                res.append(dict(tag=tag,**r))
                print(f"p={p} {tag}: n={r['n']} "
                      f"KS_GOE={r['ks_GOE']:.4f} KS_GUE={r['ks_GUE']:.4f}")
            except Exception as e:
                print(f"p={p} {tag}: err {e}")
    json.dump(res, open(os.path.join(ART,"run35_surmise.json"),"w"), indent=1)


if __name__=="__main__":
    main()
