import sys,time,numpy as np; sys.path.insert(0,'.'); from aud import *
for kick,C in (('k1',K1),('full',fullkick())):
  for m,L in ((5,7),(7,3)):
    eta=2.0; T=classes(C,eta,m); Z2=Zabs2_all(T,m); d=data(m)
    nus=[nustar(m),nustar(m,-1)]+[nu for nu in list(Z2)[:4]]
    for nu in nus:
        zn=nsum_Z(C,eta,m,nu,L)
        print(kick,'m',m,'nu',nu,'class |Z|^2=%.10g'%Z2[nu],'nsum(L=%d) |Z|^2=%.10g'%(L,abs(zn)**2),flush=True)
    print(kick,'m',m,'F=',np.mean(list(Z2.values())),'sum|T|.. Parseval check avg_nu|Z|^2 at eta=0 ->',flush=True)
