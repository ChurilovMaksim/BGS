import sys,json,numpy as np; sys.path.insert(0,'.')
from aud import *
for kick,m in (('full',7),('full',11),('full',13),('k1',11),('k1',13)):
    T=np.load(f'../logs/T_{kick}_eta2.0_m{m}.npy'); Z2=Zabs2_all(T,m); h=data(m)['h']
    F=np.mean(list(Z2.values()))
    off=196 if kick=='full' else 4
    res=[nu for nu in Z2 if (pow(nu,-1,h)+off)%h==0 or (pow(nu,-1,h)-off)%h==0]
    Fx=(sum(Z2.values())-sum(Z2[n] for n in res))/len(Z2)
    print(f'{kick} m={m} F/2m={F/(2*m):.4f}  resonant residues N=+-{off} (nu={res}) carry {(F-Fx)/(2*m):.4f};  F/2m without them = {Fx/(2*m):.4f}')
