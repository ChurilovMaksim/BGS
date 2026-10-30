import sys, time; sys.path.insert(0,'.')
from own_fast import *
import own_lift
# 1) fast==slow
w=wk1(2.0,4); V1,E1=build(w,10,2,1.0,0.6,12); V2,E2=own_lift.build(w,10,2,1.0,0.6,12)
print('fast vs slow',abs(V1-V2).max(),abs(E1-E2).max(),flush=True)
# 2) vectorised brute force m=5 L=12 vs full-alphabet lift (C unchanged)
def brute5(eta,kappa,L,Cc=C,m=5):
    from scipy.special import jv
    Cy=np.roll(np.eye(m),1,axis=1); G=np.linalg.inv(6*np.eye(m)-Cy-Cy.T)*(Cc/C)
    ns=np.arange(-L,L+1); gh=(1j)**(ns%4)*jv(ns,0.9*eta)
    grids=np.meshgrid(*([ns]*m),indexing='ij'); n=np.stack([g.ravel() for g in grids],1).astype(float)
    amp=np.ones(len(n),complex)
    for j in range(m): amp*=gh[(n[:,j]+L).astype(int)]
    q=np.einsum('ki,ij,kj->k',n,G,n); S=n.sum(1)
    return np.sum(amp*np.exp(2j*np.pi*(0.5*q+kappa*S**2/8)))
kap={5:7,7:5,9:3,11:1,13:7,15:5}
ev={}
for a in (0,2,4,6):
    V,E=build(wk1(2.0,a),30,5,1.0,0.6,36); ev[a]=(np.linalg.eigvals(V),np.linalg.eigvals(E))
def Zl(m,ev): c=ca(kap[m]); return (1-LAM**-m)*sum(c[a]*(np.sum(ev[a][0]**m)-np.sum(ev[a][1]**m)) for a in (0,2,4,6))
zb=brute5(2.0,7,12); zl=Zl(5,ev); print('m5 brute L12',zb,'lift',zl,'rel',abs(zb-zl)/abs(zb),flush=True)
# 3) physical finite-N traces (repo Line E table, direct chirp-DFT code): |Tr U_N^m|^2, N=h_m-4, c->c(1+4/N)
tab={5:(37,121.83215496),7:(235,2120.2047659),9:(1389,29946.148430),11:(8115,405032.63049),13:(47317,5456806.8166)}
for m,(Nn,val) in tab.items():
    Cc=C*(1+4/Nn); evN={}
    for a in (0,2,4,6):
        V,E=build(wk1(2.0,a,Cc),30,5,1.0,0.6,36,Cc); evN[a]=(np.linalg.eigvals(V),np.linalg.eigvals(E))
    z=Zl(m,evN); print('m',m,'N',Nn,'direct',val,'lift',abs(z)**2,'rel',abs(abs(z)**2-val)/val,flush=True)
