"""referee lineN21b: independent arb certification of the N15 step-norm table N_H(d) = ||T (A_d/s) T^{-1}||_2.
A_d = sum_n w_4(n) e(n d) M_n.
 - M_n: N12 a_ops midpoints, each entry widened by the recorded data radius RAD (|re|+|im| radius) -> exact enclosure of the Line F blocks.
 - w_4(n): recomputed here in arb (N6 cert_core formula: i^(n mod 4) J_n(1.8) e(cc n^2/2 + n/2), cc = 1/(lam - 1/lam)); the ball
   used is the union of this arb value and the float COEF0 midpoint (so the float definition is covered too).
 - s: the float s from the N12 npz (exact definition of the normalisation, as everywhere in N13/N15/N21).
 - T^{-1}: float Ti; ||T A Ti (T Ti)^{-1}|| <= ||T A Ti||/(1-eta), eta >= ||T Ti - I||_F (arb).
 - ||S||_2 at a cell centre (S = T Ahat Ti in arb): float SVD S_mid = U Sig V^*;  ||S|| <= sig_max sqrt((1+||U^*U-I||_F)(1+||V^*V-I||_F)) + ||S - U Sig V^*||_F
   with all products in arb (rigorous; no eigen-solver trusted).
 - |n| <= NT terms in arb; |n| > NT tail bounded by sum |C_n| ||T||_F ||M_n||_F ||Ti||_F (arb).
usage: nh_arb.py part nparts [cells]   -> logs/nh_arb_p{part}.jsonl   ;  nh_arb.py lip  -> logs/nh_arb_lip.json"""
import sys, json, time, math, numpy as np
from flint import arb, acb, acb_mat, ctx
ctx.prec=64
z=np.load('/workspace/bgs-lineN/N12/logs/a_ops.npz',allow_pickle=True)
NS=[int(n) for n in z['NS']]; MS=z['MS']; COEF0=z['COEF0']; D=int(z['D']); RAD=float(z['RAD'])
zz=np.load('/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz'); T=zz['T']; s=complex(zz['s']); Ti=np.linalg.inv(T)
NT=30; NC=2048; h=arb(1)/NC
def tomat(X,rad=0.0):
    return acb_mat(X.shape[0],X.shape[1],[acb(arb(float(x.real),rad),arb(float(x.imag),rad)) if rad else acb(complex(x)) for x in X.ravel()])
def fro_up(M):
    t=arb(0)
    for row in M.tolist():
        for e in row: a=e.real; b=e.imag; t+=a*a+b*b
    return t.sqrt()
def mid_np(M): return np.array([[complex(float(e.real.mid()),float(e.imag.mid())) for e in row] for row in M.tolist()])
pi=arb.pi(); I=acb(0,1); lam=3+2*arb(2).sqrt(); cc=1/(lam-1/lam); x=arb(9)/10*arb('2.0')
def w4(n):
    J=x.bessel_j(arb(abs(n)))*(1 if (n>=0 or n%2==0) else -1)
    return (I**(n%4))*J*(2*pi*I*(cc*n*n/2+arb(4*n)/8)).exp()
sA=acb(s.real,s.imag)
C={}; cdev=0.0
for k,n in enumerate(NS):
    w=w4(n); f=acb(complex(COEF0[k])); dv=abs(w-f); cdev=max(cdev,float((dv/abs(w)).upper()) if n!=0 or True else 0)
    w=acb(w.real.union(f.real),w.imag.union(f.imag)) if hasattr(arb,'union') else w
    C[n]=w/sA
Tm=tomat(T); Tim=tomat(Ti)
E=Tm*Tim-tomat(np.eye(D)); eta=fro_up(E); assert float(eta.upper())<1e-6
nT=fro_up(Tm); nTi=fro_up(Tim)
tail=arb(0)
for k,n in enumerate(NS):
    if abs(n)>NT: tail+=abs(C[n])*nT*(arb(float(np.linalg.norm(MS[k])))*(1+arb("1e-9"))+RAD*D)*nTi
TM={}
def get_TM():
    for k,n in enumerate(NS):
        if abs(n)<=NT: TM[n]=Tm*tomat(MS[k],RAD)*Tim
def norm2_up(S):
    Sm=mid_np(S); U,sg,Vh=np.linalg.svd(Sm)
    A1=tomat(U*sg[None,:])*tomat(Vh); R=S-A1; r=fro_up(R)
    Ua=tomat(U); Va=tomat(Vh)
    eu=fro_up(tomat(U.conj().T)*Ua-tomat(np.eye(D))); ev=fro_up(Va*tomat(Vh.conj().T)-tomat(np.eye(D)))
    return arb(float(sg[0]))*((1+eu)*(1+ev)).sqrt()+r, float(sg[0])
if __name__=='__main__':
    mode=sys.argv[1]
    t0=time.time(); get_TM(); print('setup',round(time.time()-t0,1),'eta',eta.str(5),'tail',tail.str(5),'w4 vs COEF0 max rel dev %.3g'%cdev,flush=True)
    if mode=='lip':
        L=arb(0); out={}
        for n in TM:
            if n==0: continue
            b,_=norm2_up(TM[n]); out[n]=float(b.upper()); L+=2*pi*abs(n)*abs(C[n])*b
        for k,n in enumerate(NS):
            if abs(n)>NT: L+=2*pi*abs(n)*abs(C[n])*nT*(arb(float(np.linalg.norm(MS[k])))*(1+arb("1e-9"))+RAD*D)*nTi
        L=L/(1-eta)
        json.dump(dict(Lip_H_referee=float(L.upper()),normTM=out,eta=float(eta.upper()),tail=float(tail.upper())),open('../logs/nh_arb_lip.json','w'),indent=1)
        print('Lip',L.str(8)); sys.exit()
    part,nparts=int(sys.argv[1]),int(sys.argv[2])
    cells=(json.load(open(sys.argv[3][1:])) if sys.argv[3].startswith('@') else [int(c) for c in sys.argv[3].split(',')]) if len(sys.argv)>3 else range(NC)
    order_idx={k:i for i,k in enumerate(cells)}
    out=open(f'../logs/nh_arb_p{part}.jsonl','a')
    for k in cells:
        if order_idx[k]%nparts!=part: continue
        t=time.time(); c=-arb(1)/2+(2*k+1)*h/2
        S=acb_mat(D,D)
        for n in TM: S+=TM[n]*(C[n]*(2*pi*I*n*c).exp())
        b,sf=norm2_up(S)
        val=(b+tail)/(1-eta)
        out.write(json.dumps(dict(k=k,c=float(c.mid()),center_up=float(val.upper()),svd_float=sf,secs=round(time.time()-t,1)))+'\n'); out.flush()
