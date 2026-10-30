import numpy as np
def restricted(build,m,a,b,gh,RHO,K):
    parts,nu,S=build(m,a,b,gh,RHO,K)
    tg={n:(P!=0).argmax(axis=0) for n,(Mn,P) in parts.items()}
    orb={0}; fr=[0]
    while fr:
        s=fr.pop()
        for n in tg:
            t=int(tg[n][s])
            if t not in orb: orb.add(t); fr.append(t)
    idx=sorted(orb)
    sub={n:(Mn,P[np.ix_(idx,idx)]) for n,(Mn,P) in parts.items()}
    return sub,idx,nu
