"""Split the fixed-eta off-diagonal W_m(eta)=F_m(eta)-B_sym into the PARITY part (pairs xi' in Gamma(-xi), not in Gamma xi)
and the rest.  k_nu(-xi)=k_nu(xi) exactly (Q even), so K(xi,-xi)=1/D_eff on the support.
W_par = (1/D_eff) sum_{xi in supp, -xi notin Gamma xi} |Gamma xi| Phi(xi) conj Phi(-xi)   (Phi constant on Gamma-orbits).
Group = Fix(T^m), T=[[0,1],[-1,6]] (q-sequences), Gamma = dihedral shifts/reversals of the q-sequence."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys; sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','phase2'))
from p2lib import *
ms=[int(x) for x in sys.argv[1].split(',')]
etas=[float(x) for x in sys.argv[2].split(',')]
for m in ms:
    O,supp=support_data(m); u=O.units(); T=O.T; d1,d2=O.d1,O.d2
    # orbit size |Gamma xi| = 2m/|Stab|
    stab=np.zeros((d1,d2),np.int64)
    for k in range(m):
        stab+=np.all([T[j]==T[(j+k)%m] for j in range(m)],axis=0)          # rotations
        stab+=np.all([T[j]==T[(k-j)%m] for j in range(m)],axis=0)          # reflections
    osz=2*m//stab
    # index of -xi
    i1=(-np.arange(d1))%d1; i2=(-np.arange(d2))%d2
    neg=lambda A: A[i1][:,i2]
    assert np.all((neg(T[0])+T[0])%d2==0)
    Tn=np.stack([neg(T[j]) for j in range(m)])
    inorb=np.zeros((d1,d2),bool)
    for k in range(m):
        inorb|=np.all([Tn[j]==T[(j+k)%m] for j in range(m)],axis=0)
        inorb|=np.all([Tn[j]==T[(k-j)%m] for j in range(m)],axis=0)
    Deff=supp.sum(); Bsym=osz[supp].sum()/Deff
    print(f'm={m} D_eff={Deff} B_sym={Bsym:.6f} 2m={2*m} #(-xi in Gamma xi on supp)={inorb[supp].sum()} supp symmetric={np.all(neg(supp)==supp)}',flush=True)
    Sn=neg(O.S); sel=supp&~inorb
    for eta in etas:
        Z=O.Z_all(eta)[u]; F=np.mean(np.abs(Z)**2)
        Wpar=np.sum(osz[sel]*np.exp(1j*eta*(O.S[sel]-Sn[sel])))/Deff
        W=F-Bsym; Wr=W-Wpar.real
        print(f'  eta={eta:7g} F/2m={F/(2*m):.4f}  W/2m={W/(2*m):+.4f}  W_par/2m={Wpar.real/(2*m):+.4f} (imag {Wpar.imag:+.1e})  W_rest/2m={Wr/(2*m):+.4f}',flush=True)
