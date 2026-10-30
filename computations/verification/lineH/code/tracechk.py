"""Line H: independent consistency check of the cert49_build operators (the exact objects that are certified) against the
referee's exact full-alphabet class sums (audit/lineE T_full_eta2.0_m*.npy):  |Z_m(nu*)|^2 vs |(1-lam^-m) sum_b c_b (Tr V_b^m - Tr E_b^m)|^2.
Float only, small Galerkin degree. Usage: tracechk.py prefV prefE"""
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-next/lineE/step2')
from lawlib import law_params, nu_res
from tm49 import csec
from cmp_full import Zclass
LAM=3+2*np.sqrt(2); s=-1
pV,pE=sys.argv[1:3]; ms=(5,7,11,13)
def traces(M):
    P={1:M}; P[2]=M@M; P[4]=P[2]@P[2]; P[5]=P[4]@M; P[7]=P[5]@P[2]; P[11]=P[7]@P[4]; P[13]=P[11]@P[2]
    return {m:np.trace(P[m]) for m in ms}
tr={}
for b in (0,2,4,6):
    tr[('V',b)]=traces(np.load(f'{pV}_b{b}_mid.npy')); tr[('E',b)]=traces(np.load(f'{pE}_b{b}_mid.npy'))
for m in ms:
    T=np.load(f'/workspace/audit/lineE/logs/T_full_eta2.0_m{m}.npy')
    P=law_params(m,7,s); cs=csec(P['kappa'])
    Z=(1-LAM**-m)*sum(cs[b]*(tr[('V',b)][m]-tr[('E',b)][m]) for b in (0,2,4,6))
    assert all(abs(cs[b])<1e-12 for b in (1,3,5,7)) and all(abs(abs(cs[b])-0.5)<1e-12 for b in (0,2,4,6))
    zc=Zclass(T,m,nu_res(m,7,s))
    print(json.dumps(dict(m=m,s=s,kappa=P['kappa'],Z2_class=zc,Z2_cert49=abs(Z)**2,rel=abs(abs(Z)**2-zc)/zc)),flush=True)
