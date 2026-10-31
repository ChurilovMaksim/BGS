"""N9b [N]: float feasibility test of the 'scalar potential + graph max-mean-cycle' route to a certificate for
Gamma_out(theta) = growth of the 8V cocycle along cat-map orbit segments avoiding the theta-box of the slow fixed point (0,0).
psi_k(y) = (1/k) log ||P_k(y)||_2 (k-step block from y; averaging over shifts gives log||P_n|| <= sum_i psi_k(T^i y) + O(k)).
Grid GxG of twist-pair cells, centre values (NOT sup over cell -> not rigorous), edges = cells met by the image parallelogram,
cells entirely inside the box removed.  Max mean cycle by value iteration.  usage: b_mmc.py G k theta"""
import sys, math, json, time, numpy as np
sys.path.insert(0,'/workspace/bgs-lineF/code')
from lift import ops, wk1
G=int(sys.argv[1]); k=int(sys.argv[2]); TH=[float(x) for x in sys.argv[3].split(',')]
K0,r,K,beta,N0=3,1.2,20,2.5,10
Bn={}
for n in range(-N0,N0+1):
    V,E=ops(lambda m,n=n: 1.0 if m==n else 0.0, N0,K0,r,r,K,beta=beta); Bn[n]=V
ns=np.array(sorted(Bn)); Bst=np.stack([Bn[n] for n in ns]); w0=wk1(2.0,4); w=np.array([w0(int(n)) for n in ns])
def Lbatch(t): return np.tensordot(w[None,:]*np.exp(2j*np.pi*np.outer(t,ns)),Bst,axes=([1],[0]))
t0=time.time(); d=1.0/G
cx=(np.arange(G)+0.5)*d
X0,X1=np.meshgrid(cx,cx,indexing='ij'); pts=np.stack([X0.ravel(),X1.ravel()],1)
psi=np.zeros(len(pts)); B=256
for s in range(0,len(pts),B):
    y=pts[s:s+B].copy(); P=np.broadcast_to(np.eye(Bst.shape[1],dtype=complex),(len(y),)+Bst.shape[1:]).copy()
    for i in range(k):
        P=np.matmul(Lbatch(y[:,0]),P); y=np.stack([y[:,1],(6*y[:,1]-y[:,0])%1.0],1)
    psi[s:s+B]=np.log(np.linalg.norm(P,ord=2,axis=(1,2)))/k
print('psi computed',round(time.time()-t0,1),'max exp(psi)=%.4f'%math.exp(psi.max()),flush=True)
# edges: cell (a,b) -> (b, j) with j covering 6y - x for y in cell b, x in cell a
idx=lambda a,b:(a%G)*G+(b%G)
succ=[]
for a in range(G):
    for b in range(G):
        lo=6*b*d-(a+1)*d; hi=6*(b+1)*d-a*d
        js=range(int(math.floor(lo/d)),int(math.ceil(hi/d)))
        succ.append([idx(b,j) for j in js])
succ=np.array([s+[s[-1]]*(9-len(s)) for s in succ])
res={}
for th in TH:
    def inbox(c): # cell fully inside box |x|<=th,|y|<=th (torus)
        a,b=c//G,c%G
        def full(i):
            lo,hi=i*d,(i+1)*d
            return (hi<=th) or (lo>=1-th)
        return full(a) and full(b)
    alive=np.array([not inbox(c) for c in range(G*G)])
    Vv=np.where(alive,0.0,-1e9); T=600; hist=[]
    for t in range(T):
        nxt=Vv[succ].max(axis=1)
        Vv=np.where(alive,psi+nxt,-1e9); hist.append(Vv.max())
    rate=(hist[-1]-hist[T//2-1])/(T-T//2)
    res[th]=math.exp(rate)
    print('theta',th,'Gamma_out estimate exp(maxmean psi_%d)=%.4f'%(k,math.exp(rate)),flush=True)
json.dump(dict(G=G,k=k,res=res,maxpsi=math.exp(psi.max()),sec=round(time.time()-t0,1)),open(f'logs/b_mmc_G{G}_k{k}.json','w'))
