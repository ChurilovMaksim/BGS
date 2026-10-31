import sys,time,numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
for p in [7,11,13]:
    m=3*p; h,nu0=nu_rho(m,1); tw=TW(m,nu0,L=8,K=16)
    T=np.random.rand(128,m); t=time.time(); Zbatch(tw,T); dt=time.time()-t
    print(p,m,'S',tw.S,'K',tw.K,'letters',len(tw.ns),'sec/eval',dt/128,flush=True)
