"""N9b [N]: same max-mean-cycle test as b_mmc.py but with an adapted Euclidean norm |x|_W=|W x|, W=Q^{1/2},
Q = sum_{j<=J} rho^{-2j} mean_y P_j(y)^* P_j(y) over sampled box-avoiding orbit segments (Lyapunov-type averaged ellipsoid).
usage: c_wnorm.py G k theta rho J"""
import sys, math, json, time, numpy as np
sys.path.insert(0,'/workspace/bgs-lineF/code')
from lift import ops, wk1
G=int(sys.argv[1]); k=int(sys.argv[2]); th=float(sys.argv[3]); rho=float(sys.argv[4]); J=int(sys.argv[5])
K0,r,K,beta,N0=3,1.2,20,2.5,10
Bn={}
for n in range(-N0,N0+1):
    V,E=ops(lambda m,n=n: 1.0 if m==n else 0.0, N0,K0,r,r,K,beta=beta); Bn[n]=V
ns=np.array(sorted(Bn)); Bst=np.stack([Bn[n] for n in ns]); w0=wk1(2.0,4); w=np.array([w0(int(n)) for n in ns])
def Lbatch(t): return np.tensordot(w[None,:]*np.exp(2j*np.pi*np.outer(t,ns)),Bst,axes=([1],[0]))
dimV=Bst.shape[1]; rng=np.random.default_rng(1)
def tdist(x): x=x%1.0; return np.minimum(x,1-x)
def inbox(y): return (tdist(y[:,0])<th)&(tdist(y[:,1])<th)
# Q from sampled orbits (keep only those whose first J+1 pairs avoid the box)
S=4000; y=rng.random((S,2)); ok=np.ones(S,bool); yy=y.copy()
for j in range(J+1): ok&=~inbox(yy); yy=np.stack([yy[:,1],(6*yy[:,1]-yy[:,0])%1],1)
y=y[ok][:1500]; Q=np.zeros((dimV,dimV),complex); P=np.broadcast_to(np.eye(dimV,dtype=complex),(len(y),dimV,dimV)).copy()
for j in range(J+1):
    Q+=rho**(-2*j)*np.einsum('sji,sjk->ik',P.conj(),P)/len(y)
    P=np.matmul(Lbatch(y[:,0]),P); y=np.stack([y[:,1],(6*y[:,1]-y[:,0])%1],1)
ev,U=np.linalg.eigh(Q); W=(U*np.sqrt(ev))@U.conj().T; Wi=(U/np.sqrt(ev))@U.conj().T
print('Q cond %.3g'%(ev.max()/ev.min()),flush=True)
d=1.0/G; cx=(np.arange(G)+0.5)*d; X0,X1=np.meshgrid(cx,cx,indexing='ij'); pts=np.stack([X0.ravel(),X1.ravel()],1)
psi=np.zeros(len(pts)); B=256
for s in range(0,len(pts),B):
    y=pts[s:s+B].copy(); P=np.broadcast_to(np.eye(dimV,dtype=complex),(len(y),dimV,dimV)).copy()
    for i in range(k):
        P=np.matmul(Lbatch(y[:,0]),P); y=np.stack([y[:,1],(6*y[:,1]-y[:,0])%1.0],1)
    psi[s:s+B]=np.log(np.linalg.norm(W@P@Wi,ord=2,axis=(1,2)))/k
idx=lambda a,b:(a%G)*G+(b%G); succ=[]
for a in range(G):
    for b in range(G):
        lo=6*b*d-(a+1)*d; hi=6*(b+1)*d-a*d
        succ.append([idx(b,j) for j in range(int(math.floor(lo/d)),int(math.ceil(hi/d)))])
succ=np.array([s+[s[-1]]*(9-len(s)) for s in succ])
def full(i): lo,hi=i*d,(i+1)*d; return (hi<=th) or (lo>=1-th)
alive=np.array([not(full(c//G) and full(c%G)) for c in range(G*G)])
for name,al in (('box',alive),('free',np.ones_like(alive))):
    Vv=np.where(al,0.0,-1e9); T=600; hist=[]
    for t in range(T):
        Vv=np.where(al,psi+Vv[succ].max(axis=1),-1e9); hist.append(Vv.max())
    print(name,'theta',th,'k',k,'G',G,'rho',rho,'J',J,'-> exp(maxmean)=%.4f'%math.exp((hist[-1]-hist[T//2-1])/(T-T//2)),'max single=%.4f'%math.exp(psi[al].max()),flush=True)
