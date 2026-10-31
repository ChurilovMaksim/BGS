"""[N] validate the exact block decomposition of the (a,16) law: Z via 8 two-state blocks vs the full 64-state Line G law (twist.py), m=15,
and the d=7 twisted traces (class 1:3) the same way.  Single-disc float Galerkin (rho=2.6, K=40, |n|<=10), as Line G."""
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineI/code')
from law import kick_ghat, MC, LAM, mdata
from twist import build, op, Zfrom
J=json.load(open('logs/blocks16_exact.json'))['cases']
gh=kick_ghat('k1',2.0,10); K=40; RHO=2.6
def zc(v): return complex(sum(v[i]*np.exp(2j*np.pi*i/16) for i in range(8)))
def taus(bx,by):
    d=7; out=[]; x,y=1,0
    for i in range(3): out.append(((2*(bx*x+2*by*y))%d)/d); x,y=(3*x+4*y)%d,(2*x+3*y)%d
    return out
for m,a in ((9,2),(9,-2),(15,2)):
    key=f'{(m-3)%48+3},{a}'; C=J[key]; nrm=C['norm2']
    coef=-4*a*(1/(LAM-1/LAM))/16
    for tw in (None,(1,3)):
        tau=[0,0,0] if tw is None else taus(*tw)
        # full 64-state
        parts,nu,S=build(m,a,16,gh,RHO,K)
        Ls=[op(parts,tau[i%3]) for i in range(m)]
        Zf=Zfrom(Ls,m,S,K)
        # blocks
        Zb=0
        for B in C['blocks']:
            Jm=np.array([[zc(B['J_times_nrm'][j][k])/nrm for k in range(2)] for j in range(2)])
            def Am(n):
                A=B['act'][str(n%16)]; M=np.zeros((2,2),complex)
                for i_in in (0,1): M[A['perm'][i_in],i_in]=np.exp(2j*np.pi*A['exps'][i_in]/16)
                return M
            X=None
            for i in range(m):
                L=sum(gn*np.exp(2j*np.pi*n*tau[i%3])*np.exp(2j*np.pi*coef*n*n/2)*np.kron(MC(n,coef,RHO,K),Am(n)) for n,gn in gh.items() if abs(gn)>0)
                X=L if X is None else L@X
            X=X.reshape(K,2,K,2)
            Zb+=np.einsum('ijik,kj->',X,Jm)
        Zb*=(1-LAM**(-m))
        print(m,a,'twist',tw,'Z full',Zf,'Z blocks',Zb,'rel',abs(Zb/Zf-1),flush=True)
