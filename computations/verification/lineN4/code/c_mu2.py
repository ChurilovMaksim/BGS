"""N4 (C) [N]: leading eigenvalues of the untwisted lifted operators (eta=2) per sector a, Line F space, to size the
sub-leading growth |mu_2| that governs the remainder after subtracting the rank-one slow term (gauge lemma)."""
import sys, numpy as np
sys.path.insert(0,'/workspace/bgs-lineF/code')
from lift import ops, wk1
for (K0,K) in [(4,30),(4,45),(5,45)]:
    for a in [4,0,2,6]:
        V,E=ops(wk1(2,a),60,K0,1.2,0.8,K,beta=0.0)
        ev=np.linalg.eigvals(V); ev=ev[np.argsort(-abs(ev))][:5]
        ee=np.linalg.eigvals(E); ee=ee[np.argsort(-abs(ee))][:3]
        print(K0,K,'a',a,'V',np.round(abs(ev),5),'E',np.round(abs(ee),5),flush=True)
