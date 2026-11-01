"""referee lineN21b: independent rigorous re-computation of the N15 N_H table, SVD+residual method (not N15's repeated squaring).
N_H(d) := ||T Ahat_d T^{-1}||_2, Ahat_d = sum_n w_4(n) e(n d) M_n / s.  Cell k = [-1/2+k h, -1/2+(k+1)h], h = 1/2048, centre c_k.
Rigour: coefficients c_n = C_n e(n c) in arb (python-flint; w_4(n) recomputed from the N6 formula, hull with the float COEF0);
float matrix work under the IEEE-754 binary64 standard model (Higham: complex inner products of length k err <= sqrt2*gamma_{k+2}|x|^T|y|),
every error bound accumulated in Frobenius norm and rounded up by (1+1e-10).  No libm, no eigen-solver trusted (SVD only supplies U,S,V;
the bound ||S|| <= max(sig) ||U|| ||V|| + ||S - U Sig V^*||_F is verified a posteriori).  Label [CA-fp: IEEE standard model].
Cell bound = centre bound + Lip*h/2, Lip from this script (rigorous ||T M_n T^{-1}||_2 bounds), also compared to N13 Lip_H = 167.2134.
usage: nh_fp.py lip | nh_fp.py part nparts"""
import os, sys, json, time, math
os.environ.setdefault('OMP_NUM_THREADS','2'); os.environ.setdefault('OPENBLAS_NUM_THREADS','2')
import numpy as np
from flint import arb, acb, ctx
ctx.prec=80
u=2.0**-53
def gam(k): return k*u/(1-k*u)
def cg(k): return math.sqrt(2)*gam(k+2)
UP=1+1e-10
def fro(M): return float(np.linalg.norm(M))*UP
z=np.load('/workspace/bgs-lineN/N12/logs/a_ops.npz',allow_pickle=True)
NS=[int(n) for n in z['NS']]; MS=z['MS']; COEF0=z['COEF0']; D=int(z['D']); RAD=float(z['RAD'])
zz=np.load('/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz'); T=zz['T']; s=complex(zz['s']); Ti=np.linalg.inv(T)
ETA=2e-15   # >= ||T Ti - I||_F, arb value [1.30e-15 +/- 1.8e-18] (nh_arb.py setup log)
NC=2048
pi=arb.pi(); I=acb(0,1); lam=3+2*arb(2).sqrt(); cc=1/(lam-1/lam); xx=arb(9)/10*arb('2.0')
def w4(n):
    J=xx.bessel_j(arb(abs(n)))*(1 if (n>=0 or n%2==0) else -1)
    return (I**(n%4))*J*(2*pi*I*(cc*n*n/2+arb(4*n)/8)).exp()
sA=acb(s.real,s.imag); C={}
for k,n in enumerate(NS):
    w=w4(n); f=acb(complex(COEF0[k])); w=acb(w.real.union(f.real),w.imag.union(f.imag)); C[n]=w/sA
nT=fro(T); nTi=fro(Ti)
X2=np.empty((len(NS),D,D),complex); nX=np.zeros(len(NS)); eX=np.zeros(len(NS))
for k,n in enumerate(NS):
    M=MS[k]; X1=T@M; X=X1@Ti; X2[k]=X
    # |X - T M Ti| <= cg(D)|X1||Ti| + cg(D)|T||M||Ti| ; data radius |T Delta Ti|_F <= ||T||_F RAD*D ||Ti||_F
    eX[k]=(cg(D)*(fro(X1)*nTi+nT*fro(M)*nTi)+nT*RAD*D*nTi)*UP; nX[k]=fro(X)
def norm2_up(S):
    U,sg,Vh=np.linalg.svd(S)
    US=U*sg[None,:]; P=US@Vh; R=S-P
    eP=(cg(D)*fro(US)*fro(Vh)+2*u*fro(U)*float(sg[0])*fro(Vh))*UP      # |fl(U sig) - U sig| <= u|U||sig| entrywise, then product
    r=fro(R)*(1+2*u)+u*(fro(S)+fro(P))+eP
    EU=U.conj().T@U-np.eye(D); eu=fro(EU)+cg(D)*fro(U)**2+u*math.sqrt(D)
    EV=Vh@Vh.conj().T-np.eye(D); ev=fro(EV)+cg(D)*fro(Vh)**2+u*math.sqrt(D)
    return (float(sg[0])*math.sqrt((1+eu)*(1+ev))+r)*UP, float(sg[0])
def centre(k):
    c=-arb(1)/2+(2*k+1)*arb(1)/(2*NC)
    cn=[C[n]*(2*pi*I*n*c).exp() for n in NS]
    cf=np.array([complex(float(x.real.mid()),float(x.imag.mid())) for x in cn])
    rr=np.array([float(abs(x-acb(complex(f))).upper()) for x,f in zip(cn,cf)])
    ca=np.array([float(abs(x).upper()) for x in cn])
    S=np.tensordot(cf,X2,1)
    dS=(float(ca@eX)+float(rr@nX)+cg(len(NS))*float(np.abs(cf)@nX))*UP
    b,sf=norm2_up(S)
    return (b+dS)/(1-ETA)*UP, sf, dS
if __name__=='__main__':
    if sys.argv[1]=='lip':
        L=0.0; per={}
        for k,n in enumerate(NS):
            if n==0: continue
            b,_=norm2_up(X2[k]); b=b+eX[k]; per[n]=b
            L+=2*math.pi*abs(n)*float(abs(C[n]).upper())*b
        L=L/(1-ETA)*(1+1e-9)
        json.dump(dict(Lip_ref=L,Lip_N13=167.21344682844932,normTM_up=per,eX_max=float(eX.max())),open('../logs/nh_fp_lip.json','w'),indent=1)
        print('Lip_ref',L); sys.exit()
    part,nparts=int(sys.argv[1]),int(sys.argv[2])
    out=open(f'../logs/nh_fp_p{part}.jsonl','a'); t0=time.time()
    for k in range(part,NC,nparts):
        v,sf,dS=centre(k); out.write(json.dumps(dict(k=k,centre_up=v,svd=sf,dS=dS))+'\n'); out.flush()
        if k<nparts*3: print(k,v,round(time.time()-t0,1),flush=True)
