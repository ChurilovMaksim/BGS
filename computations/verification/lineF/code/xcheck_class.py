"""Independent cross-check: full-alphabet lifted-operator law vs referee's exact class sums |Z_m(nu*)|^2 (k1, eta=2)."""
import sys, json, numpy as np
sys.path.insert(0,'computations/verification/lineE/step2')
from lawlib import law_params
from tm49 import csec
from lift import ops, wk1, LAM
ev={}
for a in (0,2,4,6):
    V,E=ops(wk1(2.0,a),22,4,1.2,0.8,45)
    ev[a]=(np.linalg.eigvals(V),np.linalg.eigvals(E))
for line in open('computations/verification/lineE/referee/logs/classes.jsonl'):
    d=json.loads(line)
    if d['kick']!='k1': continue
    m=d['m']; P=law_params(m,1,+1); cs=csec(P['kappa'])
    Z=(1-LAM**-m)*sum(cs[a]*(np.sum(ev[a][0]**m)-np.sum(ev[a][1]**m)) for a in (0,2,4,6))
    print(json.dumps(dict(m=m,kappa=P['kappa'],Z2_class=d['Z2_nustar'],Z2_lift=abs(Z)**2,rel=abs(abs(Z)**2-d['Z2_nustar'])/d['Z2_nustar'])))
