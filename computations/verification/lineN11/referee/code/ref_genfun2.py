"""Referee N11: independent evaluation of corrected gas form X = 2[(1+L)^p - 1], L = R + 2w*, and of N11's certified
Re L_lo reconstructed from the archived enclosures (N8 fam/near0 Re_w_lower, N9 z0_e4 Re_w_lower, N9 z0_e4s2 |w| upper)."""
import cmath, json, math
ws=complex(3.43580e-4,1.95796e-4); R=complex(6.1850e-5,-1.9431e-5); L=R+2*ws
def Xp(p): return 2*((1+L)**p-1)
def Xe(p): return 2*(cmath.exp(p*L)-1)
out=dict(Lambda=[L.real,L.imag])
fn=None; fe=None; neg=0; tot=0; m29=(9,0)
for p in range(3,200001,2):
    X=Xp(p); tot+=1
    if X.real<0:
        neg+=1; fn=fn or p
    if fe is None and Xe(p).real<0: fe=p
    if p>=29 and abs(1+X)<m29[0]: m29=(abs(1+X),p)
out.update(first_neg_product=fn,first_neg_exp=fe,neg_frac=neg/tot,min_abs_1pX_p_ge_29=m29)
for p in (47,1165,10001): X=Xp(p); out[f'X_{p}']=[X.real,X.imag,abs(X)]
d={k:json.load(open(f)) for k,f in [('fam','/workspace/bgs-lineN/N8/logs/n8_cert_fam.json'),('near0','/workspace/bgs-lineN/N8/logs/n8_cert_near0.json'),
   ('e4','/workspace/bgs-lineN/N9/logs/n9_cert_z0_e4.json'),('e4s2','/workspace/bgs-lineN/N9/logs/n9_cert_z0_e4s2.json')]}
lo=2*(d['fam']['Re_w_lower']+d['near0']['Re_w_lower']+d['e4']['Re_w_lower'])-2*d['e4s2'].get('absw_upper',4.24e-8)
out['ReL_lo_reconstructed']=lo; out['absw_e4s2_used']=d['e4s2'].get('absw_upper')
out['bounds']={p:2*((1+lo)**p-1) for p in (1289,2000,5000,10000)}
print(json.dumps(out,indent=1)); json.dump(out,open('logs/ref_genfun2.json','w'),indent=1)
