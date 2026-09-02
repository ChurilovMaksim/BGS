"""
RUN 34 AUDIT-FIX 2: Redo 'arithmetic beats symmetry' CORRECTLY.
Use Hermitian V; compare Tr(W^4) to BOTH GUE-sim and GOE-sim.
Cases where A reversible but k odd (arithmetic says GUE).
"""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import sys, os, json
import numpy as np
sys.path.insert(0, _BGS_ROOT + r"\src")
from catmap_core import U_cat
from master_formula_r4 import weyl_matrix
from master_formula_strong import find_orbit_H

ART=_BGS_ROOT + r"\artifacts"


def simulate_moment(m, ensemble, tr2_target, trials=30, seed=1):
    """Average Tr(M^4) over random m x m GUE or GOE scaled to given TrW2."""
    rng=np.random.default_rng(seed)
    tot=0
    for t in range(trials):
        if ensemble=="GUE":
            X=rng.normal(size=(m,m))+1j*rng.normal(size=(m,m))
            M=(X+X.conj().T)/2
        else:
            X=rng.normal(size=(m,m))
            M=(X+X.T)/2
        s2=np.trace(M@M).real
        if s2<=0: continue
        sc=np.sqrt(tr2_target/s2)
        tot += sc**4*np.trace(np.linalg.matrix_power(M,4)).real/trials
    return tot


def main():
    print("=== RUN 34 fixed arb-vs-sym ===")
    cases=[([2,1,1,1],101),([2,1,1,1],199),
           ([2,1,1,1],211),([5,2,2,1],199)]
    results=[]
    for (A,p) in cases:
        H=find_orbit_H(p,A)
        if H is None: continue
        k=len(H)
        U=U_cat(A,p)
        T10=weyl_matrix(1,0,p); T01=weyl_matrix(1,1,p)  # different freqs for variety
        V=T10+T10.conj().T + 0.7*(T01+T01.conj().T)
        w,v=np.linalg.eig(U)
        from collections import Counter
        keys=Counter([(round(float(x.real),5),round(float(x.imag),5)) for x in w])
        key,cnt=keys.most_common(1)[0]
        idx=[i for i,x in enumerate(w) if abs(x-complex(*key))<1e-4]
        m=len(idx); B=v[:,idx]
        W=B.conj().T@(V@B); mu=np.trace(W)/m
        Wc=W-mu*np.eye(m,dtype=complex)
        tr2=float(np.real(np.trace(Wc@Wc)))
        tr4=float(np.real(np.trace(np.linalg.matrix_power(Wc,4))))
        gue_sim=simulate_moment(m,"GUE",tr2,seed=p)
        goe_sim=simulate_moment(m,"GOE",tr2,seed=p)
        d_gue=abs(tr4-gue_sim); d_goe=abs(tr4-goe_sim)
        closer="GUE" if d_gue<d_goe else "GOE"
        results.append(dict(A=A,p=p,k=k,m=m,tr4=tr4,
                            gue=gue_sim,goe=goe_sim,closer=closer))
        print(f"A={A} p={p} k={k} m={m}: TrW4={tr4:.4f}")
        print(f"   GUE-sim={gue_sim:.4f}(d={d_gue:.4f}) "
              f"GOE-sim={goe_sim:.4f}(d={d_goe:.4f}) -> {closer}")
    json.dump(results, open(os.path.join(ART,"run34_fixed_arb.json"),"w"),
              indent=1)


if __name__=="__main__":
    main()
