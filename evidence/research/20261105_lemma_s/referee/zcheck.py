import sys, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N6/code')
from twb import TW, Zbatch, nu_rho
m,D=33,8119; h,nu0=nu_rho(m,1); tw=TW(m,nu0,L=8,K=16)
f=np.load('/workspace/research1105b/logs/lvl/p11_s1_ii.npz'); Z0=complex(f['Z0'])
idx=np.argsort(-np.abs(f['Zh']))[:6]
def lam(x,y): return (3*x+4*y)%D,(2*x+3*y)%D
def taus(bx,by):
    x,y=1,0; T=[]
    for i in range(m): T.append((2*(bx*x+2*by*y))%D/D); x,y=lam(x,y)
    return T
rows=[]
for k in idx:
    bx,by=int(f['bx'][k]),int(f['by'][k])
    vs=[(bx,by),lam(bx,by),((-bx)%D,(-by)%D),(bx,(-by)%D)]
    Z=Zbatch(tw,np.array([taus(*v) for v in vs]))
    print(bx,by,'stored',abs(f['Zh'][k]/Z0),'recomp',np.abs(Z/Z0),'maxreldiff',np.max(np.abs(Z-f['Zh'][k]))/abs(f['Zh'][k]))
Z00=Zbatch(tw,np.zeros((1,m)))[0]; print('Z0',Z0,Z00)
