"""
RUN 18: MOMENT HIERARCHY - compute Tr[W^r] for r=2..10 and compare
with Wigner-Dyson predictions. Tests feasibility of Carleman approach.
"""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import sys, os, json, math
import numpy as np
sys.path.insert(0, _BGS_ROOT + r"\src")
from catmap_core import U_cat
from master_formula_r4 import build_V, projector_eigenspace
from master_formula_strong import find_orbit_H

ART=_BGS_ROOT + r"\artifacts"

def wd_moment(r, beta):
    """Gaussian beta-ensemble prediction for E[Tr(W^r)] normalised.
    For beta=2 (GUE): only even r nonzero; Tr[W^(2m)] = Catalan(m)*M^m
    where M = dim. For GOE additional terms."""
    if r % 2 != 0:
        return 0.0
    m = r // 2
    # Catalan number C_m
    cat = math.factorial(2*m)//(math.factorial(m)*math.factorial(m+1))
    return float(cat)

def main():
    print("=== RUN 18: moment hierarchy ===")
    results=[]
    p=101
    A=[2,1,1,1]
    U=U_cat(A,p)
    Fd={(1,0):1.0+0j,(0,1):0.7+0.3j}
    V=build_V(Fd,p)
    spaces=projector_eigenspace(U)
    lam,Pl,m=spaces[0]
    Vl=Pl@V@Pl
    mu=complex(np.trace(Vl))/m
    W=Vl-mu*np.eye(p,dtype=complex)
    # Normalise so that Tr[W^2]=1 (standard unfolding)
    tr2=float(np.real(np.trace(W@W)))
    if abs(tr2)>1e-12:
        Wn=W/math.sqrt(abs(tr2))
    else:
        Wn=W
    for r in range(2,11):
        val=float(np.real(np.trace(np.linalg.matrix_power(Wn,r))))
        pred_gue=wd_moment(r,2)
        results.append(dict(r=r,tr=val,pred=pred_gue))
        print(f"r={r}: Tr[W^n^r]={val:.5f}, GUE_Catalan={pred_gue}")
    json.dump(results, open(os.path.join(ART,"run18_hierarchy.json"),"w"), indent=1)

if __name__=="__main__":
    main()
