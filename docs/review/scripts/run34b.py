import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import sys
sys.path.insert(0, _BGS_ROOT + r"\src")
import numpy as np
from catmap_core import U_cat
from master_formula_r4 import weyl_matrix
from master_formula_strong import find_orbit_H

def simulate(m, ens, tr2_target, trials=20, seed=0):
    rng=np.random.default_rng(seed); tot=0
    for _ in range(trials):
        if ens=="GUE":
            X=rng.normal(size=(m,m))+1j*rng.normal(size=(m,m)); M=(X+X.conj().T)/2
        else:
            X=rng.normal(size=(m,m)); M=(X+X.T)/2
        s2=np.trace(M@M).real
        if s2<=0: continue
        sc=np.sqrt(tr2_target/s2)
        tot+=sc**4*np.trace(np.linalg.matrix_power(M,4)).real/trials
    return tot

p,K=2207,9; A=[2,1,1,1]
H=find_orbit_H(p,A); k=len(H)
U=U_cat(A,p)
T10=weyl_matrix(1,0,p); T01=weyl_matrix(1,1,p)
V=T10+T10.conj().T+0.7*(T01+T01.conj().T)
w,v=np.linalg.eig(U)
from collections import Counter
keys=Counter([(round(float(x.real),5),round(float(x.imag),5)) for x in w])
key,_=keys.most_common(1)[0]
idx=[i for i,x in enumerate(w) if abs(x-complex(*key))<1e-4]
m=len(idx); B=v[:,idx]
W=B.conj().T@(V@B); mu=np.trace(W)/m
Wc=W-mu*np.eye(m,dtype=complex)
tr2=float(np.real(np.trace(Wc@Wc)))
tr4=float(np.real(np.trace(np.linalg.matrix_power(Wc,4))))
g=simulate(m,"GUE",tr2); o=simulate(m,"GOE",tr2)
print(f"p={p} k={k} ({'even' if k%2==0 else 'odd'}) m={m}")
print(f"TrW4={tr4:.3f} GUE={g:.3f}(d={abs(tr4-g):.3f}) "
      f"GOE={o:.3f}(d={abs(tr4-o):.3f})")
print("closer:", "GUE" if abs(tr4-g)<abs(tr4-o) else "GOE")
