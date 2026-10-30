"""Pre-registered transfer-operator predictions of |Z_m(nu)|^2 at N == -+196 for the Line B full kick (eta=2), float Galerkin.
Written with a UTC timestamp before the certified class sums at the same m are available."""
import json, sys, time, numpy as np
from lawlib import *
from tm49 import build, csec
from cmp_full import KICKS, ghat_of
L=int(sys.argv[1]); K=int(sys.argv[2]); rho=float(sys.argv[3]); ms=[int(x) for x in sys.argv[4].split(',')]
G=ghat_of(KICKS['full'],2.0,L); cache={}
for m in ms:
    for s in (+1,-1):
        P=law_params(m,7,s); cs=csec(P['kappa']); Z=0
        for b in (0,2,4,6):
            key=(s,b)
            if key not in cache:
                Op,_=build(G,m,7,s,b,rho,K); cache[key]=np.linalg.eigvals(Op)
            Z+=cs[b]*(1-LAM**(-m))*np.sum(cache[key]**m)
        rec=dict(utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),m=m,N_mod_h=-s*196,Z2_pred=abs(Z)**2,L=L,K=K,rho=rho)
        print(json.dumps(rec),flush=True); open('predictions.jsonl','a').write(json.dumps(rec)+'\n')
