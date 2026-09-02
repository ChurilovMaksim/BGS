"""
RUN 26: RESOLVENT APPROACH TO LOCAL LAW.
Compute G(z) = Tr[(zI-W)^{-1}]/m for z in upper half-plane,
compare against predicted Stieltjes transforms.
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
    print("=== RUN 26 resolvent ===")
    results=[]
    for p in (211,):
        A=[2,1,1,1]; U=U_cat(A,p)
        T10=weyl_matrix(1,0,p); T01=weyl_matrix(0,1,p)
        V=T10+T10.conj().T+0.7*(T01+T01.conj().T)
        spaces=projector_eigenspace(U)
        lam,Pl,m=max(spaces,key=lambda t:t[2])
        # Extract orthonormal basis of range(Pl) via SVD
        u,s,vh=np.linalg.svd(Pl)
        basis=u[:,:m]   # p x m
        Vl_c = basis.conj().T @ (V @ basis)   # m x m
        mu=np.trace(Vl_c)/m
        W=Vl_c-mu*np.eye(m,dtype=complex)
        Wn=W/np.sqrt(m)
        ev=np.linalg.eigvalsh(Wn)
        print(f"p={p} m={m}: eig range [{ev.min():.3f},{ev.max():.3f}]")
        row={}
        for y in [0.05,0.1,0.2,0.5,1.0,2.0]:
            z=1j*y
            G=np.trace(np.linalg.inv(z*np.eye(m)-Wn))/m
            row[y]=dict(re=float(np.real(G)),im=float(-np.imag(G)))
        results.append(dict(p=p,m=m,resolvent=row))
        print("  Im(z)   Re(G)     -Im(G)")
        for y,d in row.items():
            print(f"  {y:.2f}  {d['re']:+8.4f}  {d['im']:8.4f}")
    json.dump(results, open(os.path.join(ART,"run26_resolvent.json"),"w"),
              indent=1)


if __name__=="__main__":
    main()
