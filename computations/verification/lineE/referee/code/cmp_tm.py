"""Compare exact class-sum |Z(nu*)|^2 (full alphabet) with transfer-operator prediction (auditor's tmop), k1 kick eta=2."""
import sys,json,numpy as np; sys.path.insert(0,'.')
from aud import *; from tmop import *
eta=2.0; G=ghat(K1,eta)
rows=[json.loads(l) for l in open('../logs/classes.jsonl') if '"kick": "k1"' in l]
cfgs=[(6,2.0,120),(10,2.6,140),(12,3.0,150)]
SP={cfg:spectra(G,cfg[0],cfg[1],cfg[2]) for cfg in cfgs}
for r in rows:
    m=r['m']; out=[f"m={m} class|Z(nu*)|^2={r['Z2_nustar']:.10g}"]
    for cfg in cfgs:
        z=abs(Zpred(m,SP[cfg]))**2; out.append(f"L={cfg[0]}:{z:.10g} (rel {abs(z/r['Z2_nustar']-1):.1e})")
    # minus residue: conj-form with -c and -kappa  -> operator with c-> -c, kappa->-kappa
    print('  '.join(out),flush=True)
# minus residue check at L=12
spm=spectra(G,12,3.0,150,c=-C0)
for r in rows:
    m=r['m']; z=abs(Zpred(m,spm,kap=(-kappa(m))%8))**2
    print(f"m={m} minus-residue class={r['Z2_minus']:.10g} TO(c->-c,kappa->-kappa)={z:.10g} rel {abs(z/r['Z2_minus']-1):.1e}")
