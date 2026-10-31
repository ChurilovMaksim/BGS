"""N4 (B) [CA]: Lambda_free^{8E} via the phase-blind Schur certificate (b16_schur.py ... 0 8) + Line F 8E error terms (certE_eta2.json)."""
import json, numpy as np
from flint import arb
cj=json.load(open('/workspace/bgs-lineF/logs/certE_eta2.json')); sj=json.load(open('logs/b8_schur_E.json')); d=np.load('logs/b8_schur_E_d.npy')
eps=arb(cj['delta1'])+arb(cj['delta2'])+arb(cj['Delta']); Xn=arb(cj['Xnorm']); f=arb(sj['f_core'])
nR=arb(1/float(d.min()))*(1+arb('1e-12')); nRi=arb(1)*(1+arb('1e-12'))
b=f/(Xn*(nRi+1)); pen=eps*max(nR,arb(1),b)*(nRi+1+1/b); L=f+pen
res=dict(f_core=float(f),normR=float(nR.upper()),eps=float(eps.upper()),Xnorm=float(Xn),b=float(b.mid()),penalty=float(pen.upper()),Lambda_free_upper=float(L.upper()),
  threshold=2.01046,unit_point_rate=float((L*arb('1.0519234')).root(3).upper()),kappa=float((max(nR,arb(1),b)*(nRi+1+1/b)).upper()))
print(json.dumps(res)); json.dump(res,open('logs/b8E_final.json','w'),indent=1)
