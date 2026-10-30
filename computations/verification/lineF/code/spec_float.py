import numpy as np, sys, math
from lift import *
w=wk1(2.0,4,L=3); V,E=ops(w,3,3,1.2,0.8,40); ev=np.linalg.eigvals(V); ee=np.linalg.eigvals(E)
for m in range(1,6):
    b=brute(w,3,m); t=(np.sum(ev**m)-np.sum(ee**m))*(1-LAM**-m); print('trace-id m',m,abs(b-t)/abs(b))
for (K0,r,rE,K) in [(3,1.2,0.8,40),(3,1.5,1.0,50),(4,1.5,1.0,50)]:
  for a in (4,0,2,6):
    V,E=ops(wk1(2.0,a),17,K0,r,rE,K)
    ev=np.linalg.eigvals(V); ee=np.linalg.eigvals(E)
    ev=ev[np.argsort(-abs(ev))]; ee=ee[np.argsort(-abs(ee))]
    print(K0,r,rE,K,'a',a,'V',np.round(abs(ev[:5]),6),'E',np.round(abs(ee[:4]),6))
