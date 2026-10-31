"""N9b [N]: rank-one (cone) reduction estimate of Gamma_out(theta).
u(y) := normalised push-forward of a fixed vector along the j-step history ending at y (u = dominant Oseledets-type direction;
products are numerically rank one: sv2/sv1 ~ 0.43^k).  phi(y) := log|L_{tau_0(y)} u(y)|.  Along true orbits sum phi ~ log|P_n u|.
Graph max-mean-cycle of phi over G x G pseudo-orbit graph with theta-box cells removed (centre-sampled -> [N], not rigorous).
usage: e_cone.py G j thetas"""
import sys, math, json, time, numpy as np
sys.path.insert(0,'/workspace/bgs-lineF/code')
from lift import ops, wk1
G=int(sys.argv[1]); j=int(sys.argv[2]); TH=[float(x) for x in sys.argv[3].split(',')]
K0,r,K,beta,N0=3,1.2,20,2.5,10
Bn={}
for n in range(-N0,N0+1):
    V,E=ops(lambda m,n=n: 1.0 if m==n else 0.0, N0,K0,r,r,K,beta=beta); Bn[n]=V
ns=np.array(sorted(Bn)); Bst=np.stack([Bn[n] for n in ns]); w0=wk1(2.0,4); w=np.array([w0(int(n)) for n in ns])
def Lbatch(t): return np.tensordot(w[None,:]*np.exp(2j*np.pi*np.outer(t,ns)),Bst,axes=([1],[0]))
dimV=Bst.shape[1]; v0=np.random.default_rng(3).standard_normal(dimV)+0j; v0/=np.linalg.norm(v0)
Ainv=lambda y: np.stack([(6*y[:,0]-y[:,1])%1.0,y[:,0]],1)   # inverse of (x,y)->(y,6y-x)
fwd=lambda y: np.stack([y[:,1],(6*y[:,1]-y[:,0])%1.0],1)
t0=time.time(); d=1.0/G; cx=(np.arange(G)+0.5)*d; X0,X1=np.meshgrid(cx,cx,indexing='ij'); pts=np.stack([X0.ravel(),X1.ravel()],1)
phi=np.zeros(len(pts)); B=1024
for s in range(0,len(pts),B):
    y=pts[s:s+B]; hist=[y]
    for i in range(j): hist.append(Ainv(hist[-1]))
    u=np.tile(v0,(len(y),1))
    for i in range(j,0,-1):
        u=np.einsum('sab,sb->sa',Lbatch(hist[i][:,0]),u); u/=np.linalg.norm(u,axis=1,keepdims=True)
    phi[s:s+B]=np.log(np.linalg.norm(np.einsum('sab,sb->sa',Lbatch(y[:,0]),u),axis=1))
print('phi done',round(time.time()-t0,1),flush=True)
idx=lambda a,b:(a%G)*G+(b%G); succ=[]
for a in range(G):
    for b in range(G):
        lo=6*b*d-(a+1)*d; hi=6*(b+1)*d-a*d
        succ.append([idx(b,jj) for jj in range(int(math.floor(lo/d)),int(math.ceil(hi/d)))])
succ=np.array([s+[s[-1]]*(9-len(s)) for s in succ])
def full(i,th): lo,hi=i*d,(i+1)*d; return (hi<=th) or (lo>=1-th)
res={}
for th in TH:
    al=np.array([not(full(c//G,th) and full(c%G,th)) for c in range(G*G)])
    Vv=np.where(al,0.0,-1e9); T=500; h=[]
    for t in range(T):
        Vv=np.where(al,phi+Vv[succ].max(axis=1),-1e9); h.append(Vv.max())
    res[th]=math.exp((h[-1]-h[T//2-1])/(T-T//2))
    print('G',G,'j',j,'theta',th,'-> Gamma_out est %.4f'%res[th],flush=True)
json.dump(dict(G=G,j=j,res=res),open(f'logs/e_cone_G{G}_j{j}.json','w'))
