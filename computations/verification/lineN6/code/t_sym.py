import sys,time,numpy as np; sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
m=15; h,nu0=nu_rho(m); tw=TW(m,nu0,L=8,K=16); q=41; pw=lam_pows(m,q)
bs=[(1,0),(3,7),(5,2),(9,11)]
T=[];
for (x,y) in bs:
    for bb in [(x,y),((-x)%q,(-y)%q),(x,(-y)%q),((3*x+4*y)%q,(2*x+3*y)%q)]: T.append(taus_of(bb,pw,q))
t=time.time(); z=Zbatch(tw,T); print(time.time()-t)
print(np.round(z.reshape(4,4),6)); print('single',tw.Z(T[1]))
