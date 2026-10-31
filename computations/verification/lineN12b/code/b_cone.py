"""N12b coarse cone pre-flight [N] (centre values, NOT rigorous): k=3 blocks on a GxG cell graph of twist pairs, closed theta-box excluded.
Cell c (centre y): u_c = backward-iterated dominant direction in v~ (J steps); P_c = M(t2)M(t1)M(t0) at centre; SVD -> sigma1,sigma2,u_L.
Edge c->c' (c' meets F^3(c), sampled densely): |alpha| = |u'^* P u|, beta = ||(u'^*P) Q_c||, gamma = ||Q' P u||, D <= sigma1*sin(u',u_L) + sigma2.
Bound: vector iteration W_{c'} = max_c B_e W_c (nonneg 2x2) -> rate r; Gamma_pf = MU * r^{1/3}.  Also scalar (cone-only) rate with |alpha|.
usage: b_cone.py G TH [J]"""
import sys, json, time, os, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N12b/code'); from common import *
G=int(sys.argv[1]); TH=float(sys.argv[2]); J=int(sys.argv[3]) if len(sys.argv)>3 else 10
cen=(np.indices((G,G)).reshape(2,-1).T+0.5)/G
def okc(y):
    z=np.array(y)
    for i in range(3):
        if inbox(z,TH): return False
        z=F(z)
    return True
good=np.array([okc(y) for y in cen]); idx=-np.ones(G*G,int); idx[good]=np.arange(good.sum()); C=np.where(good)[0]
print('cells',len(C),flush=True)
ck=f'logs/b_cone_G{G}_th{TH}_cells.npz'
if os.path.exists(ck):
    zz=np.load(ck); U=zz['U']; PU=zz['PU']; UL=zz['UL']; S1=zz['S1']; S2=zz['S2']; PH=zz['PH']; start=int(zz['done'])
else:
    n=len(C); U=np.zeros((n,495),complex); PU=np.zeros((n,495),complex); UL=np.zeros((n,495),complex); S1=np.zeros(n); S2=np.zeros(n); PH=np.zeros((n,495),complex); start=0
t0=time.time()
Pc={}
for k in range(start,len(C)):
    y=cen[C[k]]
    # past direction
    hist=[y]; z=y.copy()
    for i in range(J): z=np.array([(6*z[0]-z[1])%1,z[0]]); hist.append(z)
    v=np.ones(495,complex)
    for i in range(J,0,-1): v=M(hist[i][0])@v; v/=np.linalg.norm(v)
    U[k]=v
    ts=[y[0],y[1],(6*y[1]-y[0])%1]; P=M(ts[2])@M(ts[1])@M(ts[0])
    Us,sv,Vh=np.linalg.svd(P); S1[k]=sv[0]; S2[k]=sv[1]; UL[k]=Us[:,0]; PU[k]=P@v
    PH[k]=P.conj().T@np.zeros(495)  # placeholder (u'^*P computed per edge below needs P): store P's action via low-rank
    np.save(f'logs/_P_{G}_{k}.npy',P.astype(np.complex64)) if False else None
    Pc[k]=P
    if (k+1)%100==0:
        np.savez(ck,U=U,PU=PU,UL=UL,S1=S1,S2=S2,PH=PH,done=k+1); print(k+1,round(time.time()-t0),flush=True)
# edges
sub=np.linspace(0,1,int(sys.argv[4]) if len(sys.argv)>4 else 400,endpoint=False)+0.5/400
A3=np.array([[0,1],[-1,6]]); F3=np.linalg.matrix_power(A3,3)
E=[]; t1=time.time()
for k in range(len(C)):
    y0=cen[C[k]]-0.5/G
    # dense sample along unstable direction across the cell
    eu=np.array([1,3+2*np.sqrt(2)]); eu/=np.abs(eu).max()
    pts=[]
    for a in (0.1,0.5,0.9):
        for b in sub: pts.append(y0+np.array([a,b])/G)
    pts=np.array(pts); img=(pts@F3.T)%1
    cells=np.unique((np.floor(img[:,0]*G).astype(int))*G+np.floor(img[:,1]*G).astype(int))
    P=Pc[k]; u=U[k]; Pu=PU[k]
    for c2 in cells:
        j=idx[c2]
        if j<0: continue
        u2=U[j]; uP=u2.conj()@P; al=abs(uP@u); be=np.sqrt(max(np.linalg.norm(uP)**2-al**2,0))
        ga=np.linalg.norm(Pu-u2*(u2.conj()@Pu)); sn=np.sqrt(max(1-abs(u2.conj()@UL[k])**2,0)); D=S1[k]*sn+S2[k]
        E.append((k,j,al,be,ga,D))
    if (k+1)%200==0: print('edges',k+1,len(E),round(time.time()-t1),flush=True)
E=np.array(E); src=E[:,0].astype(int); dst=E[:,1].astype(int)
def rate(B11,B12,B21,B22,it=60):
    W=np.ones((len(C),2)); hist=[]
    for n in range(it):
        a=B11*W[src,0]+B12*W[src,1]; q=B21*W[src,0]+B22*W[src,1]
        Wn=np.zeros_like(W); np.maximum.at(Wn[:,0],dst,a); np.maximum.at(Wn[:,1],dst,q)
        m=Wn.max(); hist.append(m); W=Wn/m
    return float(np.exp(np.mean(np.log(hist[-20:])))),hist
r2,h2=rate(E[:,2],E[:,3],E[:,4],E[:,5])
rs,hs=rate(E[:,2],0*E[:,3],0*E[:,4],0*E[:,5])
res=dict(G=G,TH=TH,J=J,cells=len(C),edges=len(E),mean_outdeg=len(E)/len(C),Gamma_pf_2x2=MU*r2**(1/3),Gamma_pf_alpha_only=MU*rs**(1/3),
         max_rate_sigma1=float(MU*S1.max()**(1/3)),max_rate_sigma2=float(MU*S2.max()**(1/3)),
         q_alpha=[float(np.quantile(MU*E[:,2]**(1/3),q)) for q in (0.5,0.9,0.99,1)],
         q_D=[float(np.quantile(MU*E[:,5]**(1/3),q)) for q in (0.5,0.9,0.99,1)],
         q_gamma=[float(np.quantile(E[:,4],q)) for q in (0.5,0.9,0.99,1)],q_beta=[float(np.quantile(E[:,3],q)) for q in (0.5,0.9,0.99,1)],
         hist2=[float(x) for x in h2[-5:]],sec=round(time.time()-t0))
print(json.dumps(res,indent=1)); json.dump(res,open(f'logs/b_cone_G{G}_th{TH}.json','w'),indent=1)
