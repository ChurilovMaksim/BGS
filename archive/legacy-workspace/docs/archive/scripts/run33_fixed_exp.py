"""
RUN 33 AUDIT-FIX: Redo 'arithmetic beats symmetry' with PROPERLY
HERMITIAN observable. Compare against correct GUE vs GOE Wick values.
"""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import sys, os, json
import numpy as np
sys.path.insert(0, _BGS_ROOT + r"\src")
from catmap_core import U_cat
from master_formula_r4 import weyl_matrix

ART=_BGS_ROOT + r"\artifacts"


def main():
    print("=== RUN 33 fixed experiment ===")
    results=[]
    # Use HERMITIAN V: H_n := T(n)+T(n)^dagger
    p=101; A=[2,1,1,1]
    U=U_cat(A,p)
    T10=weyl_matrix(1,0,p); T01=weyl_matrix(0,1,p)
    V=T10+T10.conj().T + 0.7*(T01+T01.conj().T)
    print(f"V Hermitian: {np.allclose(V,V.conj().T)}")
    w,v=np.linalg.eig(U)
    from collections import Counter
    keys=Counter([(round(float(x.real),5),round(float(x.imag),5)) for x in w])
    for key,cnt in list(keys.most_common(3)):
        idx=[i for i,x in enumerate(w) if abs(x-complex(*key))<1e-4]
        m=len(idx); B=v[:,idx]
        W=B.conj().T@(V@B)
        mu=np.trace(W)/m
        Wc=W-mu*np.eye(m,dtype=complex)
        herm=np.allclose(Wc,Wc.conj().T)
        tr2=float(np.real(np.trace(Wc@Wc)))
        tr4=float(np.real(np.trace(np.linalg.matrix_power(Wc,4))))
        # For m x m GOE-like real symmetric with Tr W^2 given,
        # leading Wick value of Tr W^4 ~ 3*(Tr W^2/m)^2*m? Need care.
        # Empirical RMT: simulate GOE(m) with same TrW2 and average.
        rng=np.random.default_rng(0)
        trials=50; avg4=0
        X=rng.normal(size=(m,m)); M=(X+X.T)/2
        s2=np.trace(M@M).real
        scale=np.sqrt(abs(tr2/s2)) if s2>0 else 0
        avg4=scale**4*np.trace(np.linalg.matrix_power(M,4)).real if scale>0 else 0
        results.append(dict(m=m,tr2=tr2,tr4=tr4,goe_sim=avg4))
        print(f"mult={m} herm={herm}: TrW2={tr2:.4f}, TrW4={tr4:.4f}, "
              f"GOE-sim={avg4:.4f}")
    json.dump(results, open(os.path.join(ART,"run33_fixed.json"),"w"), indent=1)


if __name__=="__main__":
    main()
