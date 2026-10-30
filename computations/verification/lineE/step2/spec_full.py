"""Float spectrum of the 49-state resonance operators L_b (b=0,2,4,6) for a kick, s=+-1; top eigenvalue moduli."""
import numpy as np, sys, json
from lawlib import *
from tm49 import build, csec
from cmp_full import KICKS, ghat_of
kick=sys.argv[1]; m=int(sys.argv[2]); L=int(sys.argv[3]); K=int(sys.argv[4]); rho=float(sys.argv[5]); eta=float(sys.argv[6]) if len(sys.argv)>6 else 2.0
G=ghat_of(KICKS[kick],eta,L)
for s in (+1,-1):
    P=law_params(m,7,s); cs=csec(P['kappa'])
    for b in (0,2,4,6):
        Op,_=build(G,m,7,s,b,rho,K); ev=np.linalg.eigvals(Op); ev=ev[np.argsort(-abs(ev))]
        print(json.dumps(dict(kick=kick,eta=eta,m_mod8=m%8,s=s,b=b,abs_cb=abs(cs[b]),top=[[round(abs(z),6),round(float(np.angle(z)),4)] for z in ev[:6]],K=K,L=L,rho=rho)),flush=True)
