"""[N] check Line F representation of Z0 for rho=(+-2,8) against zpred Zh[0,0]."""
import numpy as np, sys
sys.path.insert(0,'/workspace/bgs-lineI/dom_v3')
from law import mdata
LAM=3+2*np.sqrt(2); mus=1.3572399242659728-1.3516424762972736j
def e(x): return np.exp(2j*np.pi*x)
for m in (39,63,81,99,105,117,123):
    D=mdata(m); h=D['h']; yp=D['yp']
    nus=next(x for x in [((-1)*pow(4,-1,h))%h+s*h for s in (0,1)] if x%2==1)
    k=(-4*nus-1)//h; assert (-4*nus-1)%h==0
    kap=(k*yp)%8
    c4=-e(kap/8)/2; c0=e(kap/8)/2
    pm=(1-LAM**-m)*c4*mus**m; pp=np.conj((1-LAM**-m)*c0*mus**m)
    Zm=np.load(f'/workspace/bgs-lineI/data/zpred_d7_-2_8_m{m}_K40.npy')[0,0]
    Zp=np.load(f'/workspace/bgs-lineI/data/zpred_d7_2_8_m{m}_K40.npy')[0,0]
    print(m,'k',k,'kappa',kap,'(-2,8) ratio',Zm/pm,' (2,8) ratio',Zp/pp)
