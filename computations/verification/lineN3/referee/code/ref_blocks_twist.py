"""Referee: i_verify.py core blocks vs Line F lift.py (independent float construction) at nonzero twists, Nmax=60."""
import sys, numpy as np, math
typ,K0,rho,K=sys.argv[1],int(sys.argv[2]),sys.argv[3],int(sys.argv[4])
sys.argv=['i_verify.py',typ,str(K0),rho,str(K),'/dev/null','1','60','x','y']
src=open('/workspace/bgs-lineN/N3/code/i_verify.py').read().split("print('blocks built'")[0]
g={}; exec(src,g)
sys.path.insert(0,'/workspace/bgs-lineF/code')
from lift import ops, C0
from scipy.special import jv
for tau in (0.3,0.5,0.501375,0.9):
    w=lambda n: (1j)**(n%4)*jv(n,1.8)*np.exp(2j*np.pi*(C0*n*n/2+n*tau))
    V,E=ops(w,60,K0,float(rho),float(rho),K,beta=0.0); Lf=V if typ=='V' else E
    A=sum(np.exp(2j*np.pi*n*tau)*g['Bf'][n] for n in g['Bf'])
    print(typ,'tau',tau,'max|diff|',np.abs(A-Lf).max(),'max|L|',np.abs(Lf).max(),flush=True)
