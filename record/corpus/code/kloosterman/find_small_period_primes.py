"""
RUN 27: FIND primes with SMALL ord_p(A) to get LARGE eigenspace dim.
Then redo spectral test with big m.
"""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys, os, json
import numpy as np
from sympy import primerange, primitive_root, factorint
sys.path.insert(0, _BGS_ROOT + r"\src")
from catmap_core import U_cat
from master_formula_r4 import weyl_matrix, projector_eigenspace

ART=_BGS_ROOT + r"\artifacts"


def matrix_order_mod_p(A,p):
    """Projective order: least n with A^n == +-I mod p (audit fix:
    previous version returned n//2+1 on the -I branch, understating
    the order; see audit_orders.json for ground truth)."""
    Am=np.array(A).reshape(2,2)%p
    I=np.eye(2,dtype=int)%p
    X=Am.copy(); n=1
    while not np.array_equal(X,I) and n<10*p:
        X=X@Am%p; n+=1
        if np.array_equal(X,-I%p): return n  # projective order = n
    return n


def main():
    print("=== RUN 27: find small-order primes ===")
    A=[2,1,1,1]
    found=[]
    for p in list(primerange(100,5000)):
        K=matrix_order_mod_p(A,p)
        ratio=p/K
        if K<50:   # want small quantum period
            found.append((p,K,ratio))
            print(f"p={p}: ord={K}, p/ord={ratio:.1f}")
    found.sort(key=lambda t:-t[2])
    print(f"\nTop candidates by p/K:")
    for (p,K,r) in found[:8]:
        print(f"  p={p}, K={K}, p/K={r:.0f}")
    json.dump(found, open(os.path.join(ART,"run27_primes.json"),"w"),
              indent=1)


if __name__=="__main__":
    main()
