"""[N] float top |eigenvalues| of built blocks (mid matrices)."""
import sys, numpy as np, json
pre=sys.argv[1]; bs=[int(x) for x in sys.argv[2].split(',')]
out={}
for b in bs:
    A=np.load(f'{pre}_b{b}_mid.npy'); ev=np.sort(np.abs(np.linalg.eigvals(A)))[::-1]
    out[b]=[float(x) for x in ev[:6]]; print(pre,b,out[b][:4],flush=True)
