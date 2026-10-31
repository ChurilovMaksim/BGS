"""Sanity: the arb-built core matrix of i_verify.py equals the lift.py float matrix (beta=0) at a few twists."""
import sys, numpy as np, runpy, math
typ,K0,rho,K=sys.argv[1],int(sys.argv[2]),sys.argv[3],int(sys.argv[4])
sys.argv=['i_verify.py',typ,str(K0),rho,str(K),'/dev/null','1','20','x','y']
src=open('/workspace/bgs-lineN/N3/code/i_verify.py').read().split("print('blocks built'")[0]
g={}; exec(src,g)
sys.path.insert(0,'/workspace/bgs-lineF/code')
from lift import ops, wk1
w0=wk1(2.0,0)
V,E=ops(w0,20,K0,float(rho),float(rho),K,beta=0.0); Lf=V if typ=='V' else E
A=sum(g['Bf'][n] for n in g['Bf'])
print('max|diff|',np.abs(A-Lf).max(),'max|L|',np.abs(Lf).max(), 'rad max',max(r.max() for r in g['Brad'].values()))
