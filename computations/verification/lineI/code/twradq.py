# quick convergence of r_tw (m=9 case (2,8) only) over (K,rho,L)
import numpy as np, sys
from law import kick_ghat
from twist import build
from twrad2_lib import restricted
d=7; lam=[];x,y=1,0
for i in range(3): lam.append((x,y)); x,y=(3*x+4*y)%d,(2*x+3*y)%d
cls=[(1,0),(0,1),(1,1),(1,2),(1,3),(2,1),(3,1),(1,4),(1,5),(1,6)]
for (K,RHO,L) in [(30,2.6,10),(40,2.6,10),(50,2.6,10),(40,2.3,10),(40,2.9,10),(40,2.6,8),(40,2.6,9)]:
    gh=kick_ghat('k1',2.0,L); sub,idx,nu=restricted(build,9,2,8,gh,RHO,K)
    Lop=lambda tau: sum(np.exp(2j*np.pi*n*tau)*np.kron(Mn,P) for n,(Mn,P) in sub.items())
    ev=np.sort(abs(np.linalg.eigvals(Lop(0.0))))[::-1]
    rs=[]
    for bx in range(d):
      for by in range(d):
        if (bx,by)==(0,0): continue
        t=[((2*(bx*lx+2*by*ly))%d)/d for (lx,ly) in lam]
        Q=Lop(t[2])@Lop(t[1])@Lop(t[0]); rs.append(np.max(abs(np.linalg.eigvals(Q)))**(1/3))
    print(K,RHO,L,'mu',ev[:3].round(6),'rtw sorted top',np.unique(np.round(rs,5))[::-1][:6],flush=True)
