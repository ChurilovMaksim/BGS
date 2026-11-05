import sys,time,numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
m=int(sys.argv[1]); B=int(sys.argv[2])
h,nu0=nu_rho(m,1); tw=TW(m,nu0,L=8,K=16)
T=np.random.rand(B,m)
t=time.time(); Z=Zbatch(tw,T); print(m,B,'sec/beta',(time.time()-t)/B, tw.S, len(tw.ns))
