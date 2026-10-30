import numpy as np, json
from lift import ops, wk1, LAM
for eta in [0.25,0.5,0.75,1.0,1.1,1.2,1.25,1.5,1.75,2.0,2.25,2.5,2.75,3.0,3.5,4.0,5.0]:
    out={}
    for a in (0,2,4,6):
        V,E=ops(wk1(eta,a),30,5,1.2,0.8,35)
        ev=np.sort(abs(np.linalg.eigvals(V)))[::-1]; ee=np.sort(abs(np.linalg.eigvals(E)))[::-1]
        out[a]=(round(ev[0],5),round(ev[1],5),round(ee[0],5))
    print(json.dumps(dict(eta=eta,lam14=round(LAM**.25,5),sectors=out)),flush=True)
