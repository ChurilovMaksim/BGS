"""Line B full diagonal kick (and k1, f7) at eta=2: |Z(nu)|^2 at N == -+196 (a=7) from the referee's exact class sums T(r)
vs the 49-state transfer-operator law (float Galerkin). Kick coefficients rebuilt here from computations/verification/lineB/common/model.py rules."""
import os, numpy as np, sys, math, json
from lawlib import *
from tm49 import Z_TO
def rC(k): return {0:1.0,1:.5,-1:.5,7:-.5,-7:-.5,6:-.25,-6:-.25,8:-.25,-8:-.25}.get(k,0.0)
def fdiag():
    C={}
    for k in range(-9,10):
        v=(0.5 if k in (7,-7) else 0)+rC(k)/10+(rC(k-1)-rC(k+1))/(200j)-(0.1 if k==0 else 0)
        if abs(v)>0: C[k]=complex(v)
    return C
KICKS={'full':fdiag(),'k1':{1:0.45,-1:0.45},'f7':{7:0.45,-7:0.45}}
def ghat_of(C,eta,L,NF=8192):
    th=np.arange(NF)/NF; f=sum(c*np.exp(2j*np.pi*k*th) for k,c in C.items()).real
    g=np.fft.fft(np.exp(1j*eta*f))/NF; n=np.fft.fftfreq(NF,1/NF).astype(int)
    G=dict(zip(n.tolist(),g.tolist())); return {k:G[k] for k in range(-L,L+1)}
def Zclass(T,m,nu):
    d=mdata(m); h=d['h']; v=(-pow(16,-1,h)*pow(nu,-1,h)*pow(d['yp'],-1,h))%h
    r=np.arange(h); return abs(np.sum(T*np.exp(2j*np.pi*v*r/h)))**2/h**2
if __name__=='__main__':
    kick=sys.argv[1]; ms=[int(x) for x in sys.argv[2].split(',')]; L=int(sys.argv[3]); K=int(sys.argv[4]); rho=float(sys.argv[5])
    eta=2.0; G=ghat_of(KICKS[kick],eta,L)
    for m in ms:
        try: T=np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','referee','logs',f'T_{kick}_eta2.0_m{m}.npy'))   # referee class-sum tables (referee/code/run_classes.py)
        except FileNotFoundError: T=None
        for s in (+1,-1):
            nu=nu_res(m,7,s); zc=Zclass(T,m,nu) if T is not None else float('nan')
            zt=Z_TO(G,m,7,s,rho,K)
            print(json.dumps(dict(kick=kick,m=m,N_mod_h=-s*196,nu=nu,Z2_class=zc,Z2_TO=abs(zt)**2,rel=abs(abs(zt)**2-zc)/zc if T is not None else None,L=L,K=K,rho=rho)),flush=True)
