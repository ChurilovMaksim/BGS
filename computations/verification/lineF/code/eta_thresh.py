import numpy as np
from lift import ops, wk1, LAM
t=LAM**.25
def top(eta,a=4):
    V,E=ops(wk1(eta,a),30,5,1.2,0.8,35); return max(abs(np.linalg.eigvals(V)))
for lo,hi in [(0.75,1.0),(3.0,3.5)]:
    flo=top(lo)-t
    for it in range(14):
        mid=(lo+hi)/2; fm=top(mid)-t
        if (fm>0)==(flo>0): lo,flo=mid,fm
        else: hi=mid
    print('threshold eta (sector 4, |mu|=lam^1/4):',round((lo+hi)/2,4),flush=True)
