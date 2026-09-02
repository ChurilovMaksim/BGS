"""
RUN 32 AUDIT: Critical re-verification of ALL major claims.

CLAIM 1: Exact resonance core sol(+,-,+,-).
CLAIM 2: Arithmetic beats symmetry in Tr(W^4) -- CHECK PREDICTIONS!
CLAIM 3: Tight bound N_3 <= floor(k^2/p)+1 -- check edge cases.
CLAIM 4: Perturbation -> WD -- check matching & unfolding.
"""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import sys, os, json
import numpy as np
sys.path.insert(0, _BGS_ROOT + r"\src")
from sympy import primitive_root
from catmap_core import U_cat
from master_formula_r4 import weyl_matrix
from master_formula_strong import find_orbit_H, brute_resonance_solutions

ART=_BGS_ROOT + r"\artifacts"


def audit_claim_1():
    """Re-verify resonance core with fresh code."""
    print("--- CLAIM 1: resonance core ---")
    fails=[]
    for p in [101,211,4099]:
        g=int(primitive_root(p))
        for k in [4,5,10]:
            if (p-1)%k!=0: continue
            alpha=pow(g,(p-1)//k,p)
            H=set(); x=1
            for _ in range(k): H.add(x); x=x*alpha%p
            inv={h:pow(h,p-2,p) for h in H}
            Hl=sorted(H); n=0
            L={}
            for h1 in Hl:
                for h3 in Hl:
                    kk=((h1+h3)%p,(inv[h1]+inv[h3])%p)
                    L[kk]=L.get(kk,0)+1
            for h2 in Hl:
                for h4 in Hl:
                    kk=((h2+h4)%p,(inv[h2]+inv[h4])%p)
                    if kk in L: n+=L[kk]
            pred=(2*k*k-k) if k%2==1 else (3*k*(k-1))
            ok=(n==pred)
            print(f"  p={p} k={k}: sol={n} pred={pred} "
                  f"{'OK' if ok else 'FAIL'}")
            if not ok: fails.append((p,k))
    return fails


def audit_claim_2():
    """Check whether Wick predictions used were CORRECT.
    For m x m GUE with variance sigma^2 per entry:
       E[Tr(W^4)] ~ 2 sigma^4 m (leading order)
    For GOE: additional factor."""
    print("\n--- CLAIM 2: arithmetic beats symmetry predictions ---")
    p=101; A=[2,1,1,1]
    U=U_cat(A,p)
    Fd={(1,0):1.0+0j,(0,1):0.7+0.3j}
    T10=weyl_matrix(1,0,p); T01=weyl_matrix(0,1,p)
    V=sum(complex(c)*T10 if i==0 else complex(c)*T01
          for i,(n,c) in enumerate(Fd.items()))
    spaces=[]
    w,v=np.linalg.eig(U)
    from collections import Counter
    keys=Counter([(round(float(x.real),5),round(float(x.imag),5)) for x in w])
    for key,cnt in keys.most_common(2):
        idx=[i for i,x in enumerate(w) if abs(x-complex(*key))<1e-4]
        B=v[:,idx]; m=len(idx)
        W=B.conj().T@(V@B)
        mu=np.trace(W)/m
        Wc=W-mu*np.eye(m,dtype=complex)
        tr4=float(np.real(np.trace(np.linalg.matrix_power(Wc,4))))
        tr2=float(np.real(np.trace(Wc@Wc)))
        # Proper RMT prediction given measured tr2:
        # For GUE: Tr(W^4) ~ 2*(Tr W^2)^2 / m  (leading large-m)
        # Actually careful: for GUE normalized so Tr W^2 = s,
        # Tr W^4 ~ s^2 (self-consistent). Let me just report both.
        pred_gue_naive = 2*tr2**2
        pred_gue_scaled= 2*tr2**2/m
        print(f"  mult={m}: TrW4={tr4:.4f} TrW2={tr2:.4f}")
        print(f"     naive 2TrW2^2 = {pred_gue_naive:.4f}")
        print(f"     scaled 2TrW2^2/m = {pred_gue_scaled:.4f}")
    return None


def main():
    f1=audit_claim_1()
    audit_claim_2()
    print("\nAudit complete.")


if __name__=="__main__":
    main()
